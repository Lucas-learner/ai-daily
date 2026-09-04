#!/Users/macmini/projects/skills/ai-daily/.venv/bin/python3
"""
生成 iCloud ai daily 目录的 index.html 索引页。
页面骨架与样式见 page_style.py，与 GitHub Pages 站点保持一致。
"""
from pathlib import Path
from datetime import datetime
import html
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import page_style


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


def build_summary_card(icloud_dir: Path) -> str:
    """如果存在 daily-summary.html，直接将其内容嵌入 index 顶部。"""
    summary_html = icloud_dir / "daily-summary.html"
    summary_md = icloud_dir / "daily-summary.md"
    if not summary_html.exists():
        return ""

    # 从 H2 提取日期
    date_part = "今日"
    if summary_md.exists():
        for line in summary_md.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                date_part = line.replace("## ", "").strip()
                break

    body_content = extract_main_content(summary_html.read_text(encoding="utf-8"))

    # 清理重复结构：去掉内部 h1/h2 标题和顶部 blockquote 元信息，
    # 索引卡片本身已经显示了标题和日期，正文只保留洞察列表与底部链接。
    body_content = re.sub(r"<h1[^>]*>.*?</h1>", "", body_content, count=1, flags=re.DOTALL)
    body_content = re.sub(r"<h2[^>]*>.*?</h2>", "", body_content, count=1, flags=re.DOTALL)
    body_content = re.sub(r"<blockquote>.*?</blockquote>", "", body_content, count=1, flags=re.DOTALL)
    body_content = body_content.strip()

    return f"""<div class="card">
  <h2>📌 今日摘要（{html.escape(date_part)}）</h2>
  <div class="daily-summary-content">
    {body_content}
  </div>
</div>
"""


def main():
    icloud_dir = Path("/Users/macmini/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily")
    icloud_dir.mkdir(parents=True, exist_ok=True)

    reports_dir = icloud_dir / "reports"
    months = sorted([f.stem for f in reports_dir.glob("2*.md")], reverse=True)

    rows = ""
    for ym in months:
        md = reports_dir / f"{ym}.md"
        h = reports_dir / f"{ym}.html"
        mtime = datetime.fromtimestamp(md.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        html_link = f'<a href="reports/{ym}.html">📖 可视化</a>' if h.exists() else '<span class="meta">-</span>'
        rows += f"""<tr>
  <td><strong>{html.escape(ym)}</strong></td>
  <td>{html.escape(mtime)}</td>
  <td>{html_link}</td>
  <td><a href="reports/{ym}.md">📝 Markdown</a></td>
</tr>\n"""

    summary_card = build_summary_card(icloud_dir)

    main_html = f"""<h1>📰 AI日报索引</h1>
<p class="meta">按月汇总，逆序排列。HTML 为可视化版本，Markdown 为原始文本。</p>
{summary_card}<div class="card">
  <table>
    <thead>
      <tr><th>月份</th><th>更新时间</th><th colspan="2">查看</th></tr>
    </thead>
    <tbody>
{rows}    </tbody>
  </table>
</div>
<p class="meta">本目录由 cron + kimi-code 自动同步。</p>"""

    content = page_style.page_shell("AI日报索引", main_html, content_class="")

    (icloud_dir / "index.html").write_text(content, encoding="utf-8")
    print(f"Updated {icloud_dir / 'index.html'} with {len(months)} months")


if __name__ == "__main__":
    main()
