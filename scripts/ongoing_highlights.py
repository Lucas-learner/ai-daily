"""Render the curated, short lived event lines on both index pages."""

from datetime import date, timedelta
from pathlib import Path
import html
import json


PROJECT_DIR = Path(__file__).resolve().parent.parent
HIGHLIGHTS_FILE = PROJECT_DIR / "data" / "ongoing-highlights.json"
REPORTS_DIR = PROJECT_DIR / "reports"
MAX_ITEMS = 4
MAX_AGE_DAYS = 7


def render_highlights(as_of: str) -> str:
    """Return an HTML card; omit missing, stale, or unlinked events."""
    if not HIGHLIGHTS_FILE.exists():
        return ""
    today = date.fromisoformat(as_of)
    events = json.loads(HIGHLIGHTS_FILE.read_text(encoding="utf-8"))
    if not isinstance(events, list):
        raise ValueError("ongoing-highlights.json must contain a list")

    rows = []
    seen = set()
    for event in events:
        if not isinstance(event, dict):
            raise ValueError("each ongoing highlight must be an object")
        key = event["id"]
        if key in seen:
            raise ValueError(f"duplicate ongoing highlight id: {key}")
        seen.add(key)
        if event.get("status", "active") != "active":
            continue
        updated = date.fromisoformat(event["updated_date"])
        first = date.fromisoformat(event["first_date"])
        if not (first <= updated <= today) or today - updated >= timedelta(days=MAX_AGE_DAYS):
            continue
        report_date = event["report_date"]
        if report_date > as_of or not (REPORTS_DIR / f"{report_date[:7]}.md").exists():
            continue
        report = (REPORTS_DIR / f"{report_date[:7]}.md").read_text(encoding="utf-8")
        if f"## 【{report_date}】" not in report:
            continue
        title = html.escape(event["title"])
        reason = html.escape(event["reason"])
        href = f"reports/{report_date[:7]}.html#{report_date}"
        rows.append((updated, f'<li><a href="{href}"><strong>{title}</strong></a>'
                              f'<span class="meta"> · 更新于 {updated.isoformat()}</span>'
                              f'<div>{reason}</div></li>'))

    if not rows:
        return ""
    rows.sort(key=lambda row: row[0], reverse=True)
    items = "\n".join(row[1] for row in rows[:MAX_ITEMS])
    return (f'<div class="card ongoing-highlights">\n'
            f'  <h2>🔎 近 7 天持续关注</h2>\n'
            f'  <ul>{items}</ul>\n'
            f'</div>\n')
