#!/bin/bash
set -euo pipefail

# 从当月日报中提取指定日期的"今日洞察"，生成 iCloud 摘要文件。
# 用法：generate-daily-summary.sh YYYY-MM-DD

DATE="${1:-}"
OUT_DIR="${2:-}"
if [ -z "$DATE" ]; then
  echo "Usage: $0 YYYY-MM-DD [output-dir]" >&2
  exit 1
fi

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
YEAR_MONTH="${DATE:0:7}"
REPORT="$PROJECT_DIR/reports/$YEAR_MONTH.md"

# 默认输出到 iCloud；可通过第二个参数覆盖（如 docs/）
if [ -n "$OUT_DIR" ]; then
  TARGET_DIR="$OUT_DIR"
else
  TARGET_DIR="/Users/macmini/Library/Mobile Documents/com~apple~CloudDocs/数据同步/ai daily"
fi

if [ ! -f "$REPORT" ]; then
  echo "Report not found: $REPORT" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"

# 提取 ### 💡 今日洞察 区块，直到下一个 ## 或文件结束
TMP_BODY=$(mktemp)
awk -v date="$DATE" '
  BEGIN { in_section=0; in_insight=0 }
  $0 ~ ("^## 【" date "】") { in_section=1; next }
  in_section && /^## 【/ { exit }
  in_section && /^### 💡 今日洞察/ { in_insight=1; next }
  in_insight && /^### / { exit }
  # 跳过引言行 "今日 AI 行业呈现三大主题："
  in_insight && /^今日 AI 行业呈现.*主题：$/ { next }
  in_insight && /^$/ && printed==0 { next }
  in_insight { print; printed=1 }
' "$REPORT" > "$TMP_BODY"

if [ ! -s "$TMP_BODY" ]; then
  echo "No insight found for $DATE in $REPORT" >&2
  rm "$TMP_BODY"
  exit 1
fi

# 生成摘要 Markdown
TMP_SUMMARY=$(mktemp)
{
  printf '# 📰 AI日报摘要\n\n'
  printf '> 每日精选洞察，完整日报请查看对应月份文件。\n\n'
  printf '## %s\n\n' "$DATE"
  cat "$TMP_BODY"
  printf '\n📄 [查看 %s 完整日报](reports/%s.html)\n' "$YEAR_MONTH" "$YEAR_MONTH"
} > "$TMP_SUMMARY"

# 写入目标根目录：固定今日摘要入口（覆盖旧文件，不保留历史归档）
cp "$TMP_SUMMARY" "$TARGET_DIR/daily-summary.md"
python3 "$PROJECT_DIR/scripts/md-to-html.py" "$TARGET_DIR/daily-summary.md" "$TARGET_DIR/daily-summary.html"

rm "$TMP_BODY" "$TMP_SUMMARY"

echo "Generated daily summary for $DATE in $TARGET_DIR"
