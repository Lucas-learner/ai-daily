#!/bin/bash
set -euo pipefail

# 月度归档：将总结插入到上月文件顶部，生成 HTML，同步 iCloud
# 用法：archive-month.sh YYYY-MM /path/to/summary.md

YEAR_MONTH="${1:-}"
SUMMARY_FILE="${2:-}"

if [ -z "$YEAR_MONTH" ] || [ -z "$SUMMARY_FILE" ]; then
  echo "Usage: $0 YYYY-MM /path/to/summary.md" >&2
  exit 1
fi

if [ ! -f "$SUMMARY_FILE" ]; then
  echo "Summary file not found: $SUMMARY_FILE" >&2
  exit 1
fi

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPORT="$PROJECT_DIR/reports/$YEAR_MONTH.md"
HTML="$PROJECT_DIR/reports/$YEAR_MONTH.html"

if [ ! -f "$REPORT" ]; then
  echo "Report not found: $REPORT" >&2
  exit 1
fi

TMP=$(mktemp)
{
  echo "# $YEAR_MONTH 月度总结"
  echo ""
  cat "$SUMMARY_FILE"
  echo ""
  echo "---"
  echo ""
  cat "$REPORT"
} > "$TMP"

mv "$TMP" "$REPORT"

# 生成 HTML
python3 "$PROJECT_DIR/scripts/md-to-html.py" "$REPORT" "$HTML"

# 同步到 iCloud
bash "$PROJECT_DIR/scripts/sync-to-icloud.sh" "$YEAR_MONTH"

echo "Archived $YEAR_MONTH"
