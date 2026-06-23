#!/bin/bash
set -euo pipefail

# 将单日报内容追加到月报文件顶部（紧跟在月度标题之后）
# 用法：add-daily-entry.sh YYYY-MM-DD /path/to/body.md

DATE="${1:-}"
BODY_FILE="${2:-}"

if [ -z "$DATE" ] || [ -z "$BODY_FILE" ]; then
  echo "Usage: $0 YYYY-MM-DD /path/to/body.md" >&2
  exit 1
fi

if [ ! -f "$BODY_FILE" ]; then
  echo "Body file not found: $BODY_FILE" >&2
  exit 1
fi

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
YEAR_MONTH=$(echo "$DATE" | cut -c1-7)
REPORT="$PROJECT_DIR/reports/$YEAR_MONTH.md"

# 创建当月文件（如不存在）
if [ ! -f "$REPORT" ]; then
  {
    printf '# %s\n\n' "📰 AI日报 | $YEAR_MONTH"
    printf '*本文件汇总 %s 月所有日报，按日期逆序排列。*\n\n' "$YEAR_MONTH"
    printf -- '---\n\n'
  } > "$REPORT"
fi

TMP=$(mktemp)
{
  # 输出月报标题部分（# 开头的标题、说明、第一个 ---）
  awk '
    BEGIN { in_header=1 }
    /^## 【/ { in_header=0 }
    in_header { print }
  ' "$REPORT"

  # 输出新的日期条目
  printf '## 【%s】\n\n' "$DATE"
  cat "$BODY_FILE"
  printf '\n\n---\n\n'

  # 输出已有的日期条目
  awk '
    BEGIN { in_header=1 }
    /^## 【/ { in_header=0 }
    !in_header { print }
  ' "$REPORT"
} > "$TMP"

mv "$TMP" "$REPORT"
echo "Prepended $DATE to $REPORT"
