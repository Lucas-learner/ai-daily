#!/Users/macmini/projects/cron/ai-daily/.venv/bin/python3
"""
生成 iCloud ai daily 目录的 index.html 索引页。
"""
from pathlib import Path
from datetime import datetime
import html


def main():
    icloud_dir = Path("/Users/macmini/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily")
    icloud_dir.mkdir(parents=True, exist_ok=True)

    months = sorted([f.stem for f in icloud_dir.glob("2*.md")], reverse=True)

    rows = ""
    for ym in months:
        md = icloud_dir / f"{ym}.md"
        h = icloud_dir / f"{ym}.html"
        mtime = datetime.fromtimestamp(md.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        html_link = f'<a href="{ym}.html">📖 可视化</a>' if h.exists() else '<span style="color:#999">-</span>'
        rows += f"""<tr>
  <td><strong>{html.escape(ym)}</strong></td>
  <td>{html.escape(mtime)}</td>
  <td>{html_link}</td>
  <td><a href="{ym}.md">📝 Markdown</a></td>
</tr>\n"""

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
<table>
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
