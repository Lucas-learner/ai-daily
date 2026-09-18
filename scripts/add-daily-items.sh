#!/bin/bash
set -euo pipefail

# 将当日报条目 JSONL 校验后追加到结构化数据层 data/items/YYYY-MM-DD.jsonl
# 用法：add-daily-items.sh YYYY-MM-DD /path/to/items.jsonl
#
# 每行一条 JSON，字段约定：
#   必有：title / url / source / selected
#   可空：publishedAt / category（ai-models|ai-products|industry|paper|tip|null）/ grade（S|A|B|null）
#
# 校验分两级：
#   致命（整批拒绝，退出码 1）：JSON 非法、必填字段缺失/类型错误、category/grade 非法
#   丢弃（单行剔除，WARN 提示）：命中聚合站黑名单（scripts/aggregator-blacklist.txt）、
#                                URL 与 data/items/ 历史记录重复（含本批内重复）

DATE="${1:-}"
ITEMS_FILE="${2:-}"

if [ -z "$DATE" ] || [ -z "$ITEMS_FILE" ]; then
  echo "Usage: $0 YYYY-MM-DD /path/to/items.jsonl" >&2
  exit 1
fi

if [ ! -f "$ITEMS_FILE" ]; then
  echo "Items file not found: $ITEMS_FILE" >&2
  exit 1
fi

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="$PROJECT_DIR/data/items"
TARGET="$TARGET_DIR/$DATE.jsonl"
BLACKLIST="$PROJECT_DIR/scripts/aggregator-blacklist.txt"
FILTERED=$(mktemp)
trap 'rm -f "$FILTERED"' EXIT

mkdir -p "$TARGET_DIR"

# 校验 + 过滤：致命错误整批拒绝；黑名单/重复 URL 单行剔除后写入 $FILTERED
python3 - "$ITEMS_FILE" "$TARGET_DIR" "$BLACKLIST" "$FILTERED" <<'PYEOF'
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit

items_path, target_dir, blacklist_path, filtered_path = sys.argv[1:5]
errors = []

valid_categories = {"ai-models", "ai-products", "industry", "paper", "tip", None}
valid_grades = {"S", "A", "B", None}

# 聚合站黑名单（域名，子域名后缀匹配）
blacklist = set()
bp = Path(blacklist_path)
if bp.exists():
    for line in bp.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            blacklist.add(line.lower())

def is_blacklisted(url):
    host = (urlsplit(url).hostname or "").lower()
    return any(host == d or host.endswith("." + d) for d in blacklist)

# 历史 URL（用于精确去重；规范化：去末尾斜杠）
history = set()
for f in Path(target_dir).glob("*.jsonl"):
    for line in f.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            u = json.loads(line).get("url")
        except json.JSONDecodeError:
            continue
        if isinstance(u, str) and u.strip():
            history.add(u.strip().rstrip("/"))

with open(items_path, encoding="utf-8") as f:
    lines = [l for l in f.read().splitlines() if l.strip()]

if not lines:
    print(f"Items file is empty: {items_path}", file=sys.stderr)
    sys.exit(1)

kept = []
dropped_blacklist = 0
dropped_dup = 0

for i, line in enumerate(lines, 1):
    try:
        obj = json.loads(line)
    except json.JSONDecodeError as e:
        errors.append(f"line {i}: invalid JSON: {e}")
        continue
    for field in ("title", "url", "source"):
        if not isinstance(obj.get(field), str) or not obj[field].strip():
            errors.append(f"line {i}: missing or empty '{field}'")
    if not isinstance(obj.get("selected"), bool):
        errors.append(f"line {i}: 'selected' must be true/false")
    if obj.get("category") not in valid_categories:
        errors.append(f"line {i}: invalid category {obj.get('category')!r} (must be one of ai-models/ai-products/industry/paper/tip)")
    if obj.get("grade") not in valid_grades:
        errors.append(f"line {i}: invalid grade {obj.get('grade')!r} (must be S/A/B)")
    if errors and errors[-1].startswith(f"line {i}:"):
        continue  # 本行已有致命错误，不再做丢弃级检查
    url = obj["url"].strip()
    if is_blacklisted(url):
        print(f"WARN line {i}: 聚合站黑名单来源，剔除: {url}", file=sys.stderr)
        dropped_blacklist += 1
        continue
    if url.rstrip("/") in history:
        print(f"WARN line {i}: URL 与历史记录重复，剔除: {url}", file=sys.stderr)
        dropped_dup += 1
        continue
    history.add(url.rstrip("/"))  # 本批内去重
    kept.append(line)

if errors:
    for e in errors:
        print(e, file=sys.stderr)
    sys.exit(1)

with open(filtered_path, "w", encoding="utf-8") as f:
    f.write("\n".join(kept) + ("\n" if kept else ""))

print(
    f"validated {len(lines)} items: kept {len(kept)}, "
    f"dropped blacklist {dropped_blacklist}, dropped duplicate {dropped_dup}"
)
PYEOF

if [ ! -s "$FILTERED" ]; then
  echo "No new items to append (all dropped as blacklisted/duplicate)"
  exit 0
fi

cat "$FILTERED" >> "$TARGET"
TOTAL=$(wc -l < "$TARGET" | tr -d ' ')
echo "Appended items to $TARGET (total $TOTAL)"
