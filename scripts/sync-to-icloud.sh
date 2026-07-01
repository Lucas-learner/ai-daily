#!/bin/bash
set -euo pipefail

# 同步指定月份的 md 与 html 到 iCloud，并更新索引页
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
ICLOUD_REPORTS_DIR="$ICLOUD_DIR/reports"

if [ ! -f "$REPORT" ]; then
  echo "Report not found: $REPORT" >&2
  exit 1
fi

# 检查 iCloud 目录是否可访问（避免目录阻塞时产生临时目录/残留文件）
# 使用子进程 + 10 秒超时，touch/rm 任一环节卡住都认为不可用
_icloud_access_ok=0
(
  touch "$ICLOUD_DIR/.sync-healthcheck.$$" 2>/dev/null &&
  rm -f "$ICLOUD_DIR/.sync-healthcheck.$$" 2>/dev/null
) &
_access_pid=$!
for _i in $(seq 1 10); do
  if ! kill -0 $_access_pid 2>/dev/null; then
    wait $_access_pid 2>/dev/null
    _icloud_access_ok=1
    break
  fi
  sleep 1
done
if [ $_icloud_access_ok -eq 0 ]; then
  kill -9 $_access_pid 2>/dev/null
  wait $_access_pid 2>/dev/null
  echo "ERROR: iCloud 目录访问阻塞或超时，跳过同步: $ICLOUD_DIR" >&2
  echo "请检查 iCloud Drive 状态（如 bird 进程、网络连接），恢复后脚本会自动同步。" >&2
  exit 1
fi

mkdir -p "$ICLOUD_DIR" "$ICLOUD_REPORTS_DIR"
cp "$REPORT" "$ICLOUD_REPORTS_DIR/$YEAR_MONTH.md"

if [ -f "$HTML" ]; then
  cp "$HTML" "$ICLOUD_REPORTS_DIR/$YEAR_MONTH.html"
fi

# 生成本月最新日期的摘要卡片（固定 daily-summary.md，不保留历史归档）
LATEST_DATE=$(grep -m1 -oE '^## 【[0-9]{4}-[0-9]{2}-[0-9]{2}】' "$REPORT" | sed 's/## 【//;s/】//')
if [ -n "$LATEST_DATE" ]; then
  "$PROJECT_DIR/scripts/generate-daily-summary.sh" "$LATEST_DATE" || true
fi

# 更新索引页
"$PROJECT_DIR/.venv/bin/python3" "$PROJECT_DIR/scripts/update-icloud-index.py"

echo "Synced $YEAR_MONTH to iCloud: $ICLOUD_DIR"
