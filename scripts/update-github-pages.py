#!/Users/macmini/projects/skills/ai-daily/.venv/bin/python3
"""
生成 GitHub Pages 站点索引页 docs/index.html。

设计原则：
- docs/ 目录作为 GitHub Pages 的发布根目录
- 只发布 reports/*.html（可视化日报），不暴露 .md 源文件
- 索引页展示月份列表 + 最新日报摘要卡片 + 按日浏览入口（data/items 有数据时）
- 按日浏览页 docs/days/ 由 build_daily_pages.py 从 data/items/*.jsonl 生成
- 页面骨架与样式见 page_style.py（卡片式设计 + 暗色模式）
"""
from pathlib import Path
from datetime import datetime
import html
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import page_style

# 文件名带连字符，不能直接 import，用 importlib 加载
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "build_daily_pages", Path(__file__).resolve().parent / "build_daily_pages.py"
)
build_daily_pages = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_daily_pages)


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


def build_summary_card() -> str:
    """如果存在 docs/daily-summary.html，将其内容嵌入索引顶部。"""
    summary_html = DOCS_DIR / "daily-summary.html"
    summary_md = DOCS_DIR / "daily-summary.md"
    if not summary_html.exists():
        return ""

    date_part = "今日"
    if summary_md.exists():
        for line in summary_md.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                date_part = line.replace("## ", "").strip()
                break

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


def generate_daily_summary():
    """为 GitHub Pages 生成 docs/daily-summary.html（基于最新日报）。"""
    md_files = sorted(REPORTS_DIR.glob("2*.md"), reverse=True)
    if not md_files:
        return
    latest_md = md_files[0]
    text = latest_md.read_text(encoding="utf-8")
    match = re.search(r"^## 【(\d{4}-\d{2}-\d{2})】", text, re.MULTILINE)
    if not match:
        return
    latest_date = match.group(1)
    import subprocess
    subprocess.run(
        ["bash", str(PROJECT_DIR / "scripts/generate-daily-summary.sh"), latest_date, str(DOCS_DIR)],
        check=True,
    )
    print(f"Generated docs/daily-summary.html for {latest_date}")


def build_days_section(day_entries) -> str:
    """按日浏览入口卡片；无数据时返回空串（索引页不显示入口）。"""
    if not day_entries:
        return ""
    links = ""
    for date, total, selected in day_entries:
        links += (
            f'<a class="day-link" href="days/{date}.html">'
            f'<strong>{html.escape(date[5:])}</strong>'
            f'<span class="meta">{selected}/{total} 精选</span></a>\n'
        )
    return f"""<div class="card">
  <h2>🗓️ 按日浏览</h2>
  <p class="meta">按天查看采集条目池，支持分类筛选与精选/全部切换。</p>
  <div class="day-grid">
{links}  </div>
</div>
"""


def main():
    ensure_docs_reports()
    ensure_nojekyll()
    generate_daily_summary()
    day_entries = build_daily_pages.build()

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

    summary_card = build_summary_card()
    days_section = build_days_section(day_entries)

    main_html = f"""<h1>📰 AI日报</h1>
<p class="meta">每日自动生成的 AI 行业日报归档，按月汇总，逆序排列。</p>
{summary_card}{days_section}<div class="card">
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
    print(f"Updated {DOCS_DIR / 'index.html'} with {len(months)} months, {len(day_entries)} days")


if __name__ == "__main__":
    main()
