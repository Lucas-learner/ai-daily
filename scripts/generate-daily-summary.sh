#!/bin/bash
set -euo pipefail

# 从当月日报中提取首页摘要卡片内容（今日洞察首句 TL;DR + 当日头条/核心动态清单），生成摘要文件（中间产物，供索引页内嵌后丢弃）。
# 用法：generate-daily-summary.sh YYYY-MM-DD [output-dir]
# 调用方应始终传 output-dir（临时目录）；不传时默认写到 iCloud 目录仅为兼容旧用法。

DATE="${1:-}"
OUT_DIR="${2:-}"
if [ -z "$DATE" ]; then
  echo "Usage: $0 YYYY-MM-DD [output-dir]" >&2
  exit 1
fi

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
# awk 含中文/emoji 匹配，用字节模式规避 macOS BSD awk 的 UTF-8 多字节正则 bug
export LC_ALL=C
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

# 提取首页摘要卡片内容：
# - TL;DR：今日洞察首句（去掉行内加粗后整句加粗）
# - 重点清单：头条全部 + 核心动态补足，合计最多 5 条，链接到当日锚点，不显示分类/标题 emoji
TMP_BODY=$(mktemp)
awk -v date="$DATE" -v ym="$YEAR_MONTH" '
  BEGIN { in_section=0; in_insight=0; n=0; tldr="" }
  $0 ~ ("^## 【" date "】") { in_section=1; next }
  in_section && /^## 【/ { exit }
  in_section && /^### 💡 今日洞察/ { in_insight=1; next }
  in_section && /^### / { in_insight=0 }
  in_insight && /^$/ { next }
  # 跳过旧格式引言行 "今日 AI 行业呈现三大主题："
  in_insight && /^今日 AI 行业呈现.*主题：$/ { next }
  in_insight && tldr=="" {
    line=$0
    sub(/。.*$/, "。", line)
    tldr = line
    gsub(/\*\*/, "", tldr)
    next
  }
  # 新闻标题可能使用 🚀/💰/🤖 等不同 emoji；从独立加粗标题行提取正文，不限定 emoji 类型。
  in_section && !in_insight && /^[^*]*\*\*.*\*\*[[:space:]]*$/ && n<5 {
    line=$0
    sub(/^[^*]*\*\*/, "", line)
    sub(/\*\*[[:space:]]*$/, "", line)
    items[++n] = "- " line
  }
  END {
    if (tldr != "") print "**" tldr "**\n"
    for (i=1; i<=n; i++) print items[i]
    if (n>0) print "……"
  }
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
