#!/Users/macmini/projects/skills/ai-daily/.venv/bin/python3
"""
生成 iCloud ai daily 目录的 index.html 索引页。
"""
from pathlib import Path
from datetime import datetime
import html


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

    raw = summary_html.read_text(encoding="utf-8")
    # 提取 <body> ... </body> 之间的内容
    start = raw.find("<body>")
    end = raw.find("</body>")
    if start != -1 and end != -1:
        body_content = raw[start + 6:end].strip()
    else:
        body_content = raw

    # 清理重复结构：去掉内部 h1/h2 标题和顶部 blockquote 元信息，
    # 索引卡片本身已经显示了标题和日期，正文只保留洞察列表与底部链接。
    import re
    body_content = re.sub(r"<h1[^>]*>.*?</h1>", "", body_content, count=1, flags=re.DOTALL)
    body_content = re.sub(r"<h2[^>]*>.*?</h2>", "", body_content, count=1, flags=re.DOTALL)
    body_content = re.sub(r"<blockquote>.*?</blockquote>", "", body_content, count=1, flags=re.DOTALL)
    body_content = body_content.strip()

    return f"""<div style="background:#fff; border-radius:8px; padding:16px; margin:20px 0; box-shadow:0 1px 3px rgba(0,0,0,0.1);">
  <h2 style="font-size:1.2em; margin:0 0 16px; border-bottom:1px solid #eee; padding-bottom:8px;">📌 今日摘要（{html.escape(date_part)}）</h2>
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
        html_link = f'<a href="reports/{ym}.html">📖 可视化</a>' if h.exists() else '<span style="color:#999">-</span>'
        rows += f"""<tr>
  <td><strong>{html.escape(ym)}</strong></td>
  <td>{html.escape(mtime)}</td>
  <td>{html_link}</td>
  <td><a href="reports/{ym}.md">📝 Markdown</a></td>
</tr>\n"""

    summary_card = build_summary_card(icloud_dir)

    content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI日报索引</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.6; max-width: 700px; margin: 0 auto; padding: 24px; color: #333; background: #fafafa; }}
  h1 {{ font-size: 1.6em; border-bottom: 2px solid #ddd; padding-bottom: 0.3em; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  th, td {{ padding: 14px 12px; text-align: left; border-bottom: 1px solid #eee; }}
  th {{ background: #f0f0f0; font-weight: 600; }}
  tr:last-child td {{ border-bottom: none; }}
  a {{ color: #0366d6; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .meta {{ color: #666; font-size: 0.9em; margin-top: 8px; }}
</style>
</head>
<body>
<h1>📰 AI日报索引</h1>
<p class="meta">按月汇总，逆序排列。HTML 为可视化版本，Markdown 为原始文本。</p>
{summary_card}<table>
  <thead>
    <tr><th>月份</th><th>更新时间</th><th colspan="2">查看</th></tr>
  </thead>
  <tbody>
{rows}  </tbody>
</table>
<p class="meta">本目录由 cron + kimi-code 自动同步。</p>
</body>
</html>"""

    (icloud_dir / "index.html").write_text(content, encoding="utf-8")
    print(f"Updated {icloud_dir / 'index.html'} with {len(months)} months")


if __name__ == "__main__":
    main()
