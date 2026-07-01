#!/Users/macmini/projects/skills/ai-daily/.venv/bin/python3
"""
生成 GitHub Pages 站点索引页 docs/index.html。

设计原则：
- docs/ 目录作为 GitHub Pages 的发布根目录
- 只发布 reports/*.html（可视化日报），不暴露 .md 源文件
- 索引页展示月份列表 + 最新日报摘要卡片
"""
from pathlib import Path
from datetime import datetime
import html
import re


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

    raw = summary_html.read_text(encoding="utf-8")
    start = raw.find("<body>")
    end = raw.find("</body>")
    if start != -1 and end != -1:
        body_content = raw[start + 6:end].strip()
    else:
        body_content = raw

    body_content = re.sub(r"<h1[^>]*>.*?</h1>", "", body_content, count=1, flags=re.DOTALL)
    body_content = re.sub(r"<h2[^>]*>.*?</h2>", "", body_content, count=1, flags=re.DOTALL)
    body_content = re.sub(r"<blockquote>.*?</blockquote>", "", body_content, count=1, flags=re.DOTALL)
    body_content = body_content.strip()

    return f"""<div style="background:#fff; border-radius:8px; padding:16px; margin:20px 0; box-shadow:0 1px 3px rgba(0,0,0,0.1);">
  <h2 style="font-size:1.2em; margin:0 0 16px; border-bottom:1px solid #eee; padding-bottom:8px;">📌 最新摘要（{html.escape(date_part)}）</h2>
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


def main():
    ensure_docs_reports()
    generate_daily_summary()

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

    content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI日报 | Lucas-learner</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.6; max-width: 760px; margin: 0 auto; padding: 24px; color: #333; background: #fafafa; }}
  h1 {{ font-size: 1.8em; border-bottom: 2px solid #ddd; padding-bottom: 0.3em; }}
  h2 {{ font-size: 1.3em; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  th, td {{ padding: 14px 12px; text-align: left; border-bottom: 1px solid #eee; }}
  th {{ background: #f0f0f0; font-weight: 600; }}
  tr:last-child td {{ border-bottom: none; }}
  a {{ color: #0366d6; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .meta {{ color: #666; font-size: 0.9em; margin-top: 8px; }}
  .badge {{ display: inline-block; padding: 2px 8px; border-radius: 12px; background: #e1f5fe; color: #0277bd; font-size: 0.85em; margin-left: 8px; }}
</style>
</head>
<body>
<h1>📰 AI日报</h1>
<p class="meta">每日自动生成的 AI 行业日报归档，按月汇总，逆序排列。</p>
{summary_card}<table>
  <thead>
    <tr><th>月份</th><th>更新时间</th><th>查看</th></tr>
  </thead>
  <tbody>
{rows}  </tbody>
</table>
<p class="meta">源码仓库：<a href="https://github.com/Lucas-learner/ai-daily">Lucas-learner/ai-daily</a></p>
</body>
</html>"""

    (DOCS_DIR / "index.html").write_text(content, encoding="utf-8")
    print(f"Updated {DOCS_DIR / 'index.html'} with {len(months)} months")


if __name__ == "__main__":
    main()
