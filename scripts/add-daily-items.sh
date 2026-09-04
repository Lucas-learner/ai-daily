#!/bin/bash
set -euo pipefail

# 将当日报条目 JSONL 校验后追加到结构化数据层 data/items/YYYY-MM-DD.jsonl
# 用法：add-daily-items.sh YYYY-MM-DD /path/to/items.jsonl
#
# 每行一条 JSON，字段约定：
#   必有：title / url / source / selected
#   可空：publishedAt / category（ai-models|ai-products|industry|paper|tip|null）/ grade（S|A|B|null）

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

mkdir -p "$TARGET_DIR"

# 校验：每行必须是合法 JSON，且 title/url/source 为非空字符串，selected 为布尔值
python3 - "$ITEMS_FILE" <<'PYEOF'
import json, sys

path = sys.argv[1]
errors = []
valid_categories = {"ai-models", "ai-products", "industry", "paper", "tip", None}
valid_grades = {"S", "A", "B", None}

with open(path, encoding="utf-8") as f:
    lines = [l for l in f.read().splitlines() if l.strip()]

if not lines:
    print(f"Items file is empty: {path}", file=sys.stderr)
    sys.exit(1)

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

if errors:
    for e in errors:
        print(e, file=sys.stderr)
    sys.exit(1)

print(f"validated {len(lines)} items")
PYEOF

cat "$ITEMS_FILE" >> "$TARGET"
TOTAL=$(wc -l < "$TARGET" | tr -d ' ')
echo "Appended items to $TARGET (total $TOTAL)"
