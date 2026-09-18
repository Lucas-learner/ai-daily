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

# body 首行若自带日期标题（## 【...】），剥离之，避免与本脚本打印的标题重复
STRIPPED_BODY=$(mktemp)
awk '
  NR==1 && /^## 【/ { skipped=1; next }
  NR==2 && skipped && /^$/ { next }
  { print }
' "$BODY_FILE" > "$STRIPPED_BODY"

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
  cat "$STRIPPED_BODY"
  printf '\n\n---\n\n'

  # 输出已有的日期条目（跳过同日期旧条目，保证幂等：补跑/重跑不会产生重复区块）
  awk -v date="$DATE" '
    BEGIN { in_header=1 }
    /^## 【/ {
      in_header=0
      skip = ($0 == "## 【" date "】")
      if (skip) next
    }
    in_header || skip { next }
    { print }
  ' "$REPORT"
} > "$TMP"

rm -f "$STRIPPED_BODY"
mv "$TMP" "$REPORT"
echo "Prepended $DATE to $REPORT"
