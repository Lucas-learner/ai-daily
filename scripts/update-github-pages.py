#!/Users/macmini/projects/skills/ai-daily/.venv/bin/python3
"""
生成 GitHub Pages 站点索引页 docs/index.html。

设计原则：
- docs/ 目录作为 GitHub Pages 的发布根目录
- 只发布 reports/*.html（可视化日报），不暴露 .md 源文件
- 索引页展示月份列表 + 最新日报摘要卡片
- 页面骨架与样式见 page_style.py（卡片式设计 + 暗色模式）
"""
from pathlib import Path
from datetime import datetime
import html
import re
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import page_style


PROJECT_DIR = Path("/Users/macmini/projects/skills/ai-daily")
DOCS_DIR = PROJECT_DIR / "docs"
REPORTS_DIR = PROJECT_DIR / "reports"
DOCS_REPORTS_DIR = DOCS_DIR / "reports"


def ensure_docs_reports():
    """把 reports/ 下的 html 文件同步到 docs/reports/，供 Pages 发布。"""
    DOCS_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    for src in sorted(REPORTS_DIR.glob("2*.html")):
        dst = DOCS_REPORTS_DIR / src.name
        content = src.read_bytes()
        if not dst.exists() or dst.read_bytes() != content:
            dst.write_bytes(content)
            print(f"Updated docs/reports/{src.name}")


def ensure_nojekyll():
    """禁用 Jekyll，避免 GitHub Pages 构建时调用 github-metadata API 导致 503 失败。"""
    marker = DOCS_DIR / ".nojekyll"
    if not marker.exists():
        marker.write_text("", encoding="utf-8")
        print("Created docs/.nojekyll")


def extract_main_content(raw: str) -> str:
    """从完整 HTML 中提取正文：新版页面取 <main> 内容，旧版退回 <body> 内容。"""
    m = re.search(r"<main[^>]*>(.*)</main>", raw, re.DOTALL)
    if m:
        return m.group(1).strip()
    start = raw.find("<body>")
    end = raw.find("</body>")
    if start != -1 and end != -1:
        return raw[start + 6:end].strip()
    return raw


def build_summary_card(summary_dir: Path, date_part: str) -> str:
    """把临时目录里的 daily-summary.html 内容嵌入索引顶部（中间文件不留在 docs/）。"""
    summary_html = summary_dir / "daily-summary.html"
    if not summary_html.exists():
        return ""

    body_content = extract_main_content(summary_html.read_text(encoding="utf-8"))

    body_content = re.sub(r"<h1[^>]*>.*?</h1>", "", body_content, count=1, flags=re.DOTALL)
    body_content = re.sub(r"<h2[^>]*>.*?</h2>", "", body_content, count=1, flags=re.DOTALL)
    body_content = re.sub(r"<blockquote>.*?</blockquote>", "", body_content, count=1, flags=re.DOTALL)
    body_content = body_content.strip()

    return f"""<div class="card">
  <h2>📌 最新摘要（{html.escape(date_part)}）</h2>
  <div class="daily-summary-content">
    {body_content}
  </div>
</div>
"""


def generate_daily_summary(workdir: Path) -> str:
    """把最新日报的「今日洞察」摘要生成到 workdir（临时目录），返回日报日期；无日报返回空串。"""
    md_files = sorted(REPORTS_DIR.glob("2*.md"), reverse=True)
    if not md_files:
        return ""
    latest_md = md_files[0]
    text = latest_md.read_text(encoding="utf-8")
    match = re.search(r"^## 【(\d{4}-\d{2}-\d{2})】", text, re.MULTILINE)
    if not match:
        return ""
    latest_date = match.group(1)
    import subprocess
    subprocess.run(
        ["bash", str(PROJECT_DIR / "scripts/generate-daily-summary.sh"), latest_date, str(workdir)],
        check=True,
    )
    return latest_date


def main():
    ensure_docs_reports()
    ensure_nojekyll()

    # 摘要生成到临时目录，内嵌进索引后即弃，docs/ 不留 daily-summary 中间文件
    with tempfile.TemporaryDirectory() as tmp:
        latest_date = generate_daily_summary(Path(tmp))
        summary_card = build_summary_card(Path(tmp), latest_date) if latest_date else ""

    months = sorted([f.stem for f in DOCS_REPORTS_DIR.glob("2*.html")], reverse=True)

    rows = ""
    for ym in months:
        h = DOCS_REPORTS_DIR / f"{ym}.html"
        mtime = datetime.fromtimestamp(h.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        rows += f"""<tr>
  <td><strong>{html.escape(ym)}</strong></td>
  <td>{html.escape(mtime)}</td>
  <td><a href="reports/{ym}.html">📖 可视化日报</a></td>
</tr>\n"""

    main_html = f"""<h1>📰 AI日报</h1>
<p class="meta">每日自动生成的 AI 行业日报归档，按月汇总，逆序排列。</p>
{summary_card}<div class="card">
  <h2>📚 月度归档</h2>
  <table>
    <thead>
      <tr><th>月份</th><th>更新时间</th><th>查看</th></tr>
    </thead>
    <tbody>
{rows}    </tbody>
  </table>
</div>
<p class="meta">源码仓库：<a href="https://github.com/Lucas-learner/ai-daily">Lucas-learner/ai-daily</a></p>"""

    content = page_style.page_shell(
        "AI日报 | Lucas-learner", main_html, content_class=""
    )

    (DOCS_DIR / "index.html").write_text(content, encoding="utf-8")
    print(f"Updated {DOCS_DIR / 'index.html'} with {len(months)} months")


if __name__ == "__main__":
    main()
