#!/bin/bash
set -euo pipefail

# 同步指定月份的 md 与 html 到 iCloud
# 用法：sync-to-icloud.sh YYYY-MM

YEAR_MONTH="${1:-}"
if [ -z "$YEAR_MONTH" ]; then
  echo "Usage: $0 YYYY-MM" >&2
  exit 1
fi

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPORT="$PROJECT_DIR/reports/$YEAR_MONTH.md"
HTML="$PROJECT_DIR/reports/$YEAR_MONTH.html"
ICLOUD_DIR="/Users/macmini/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily"

if [ ! -f "$REPORT" ]; then
  echo "Report not found: $REPORT" >&2
  exit 1
fi

mkdir -p "$ICLOUD_DIR"
cp "$REPORT" "$ICLOUD_DIR/$YEAR_MONTH.md"

if [ -f "$HTML" ]; then
  cp "$HTML" "$ICLOUD_DIR/$YEAR_MONTH.html"
fi

echo "Synced $YEAR_MONTH to iCloud: $ICLOUD_DIR"
