#!/bin/bash
set -euo pipefail

# 本地检索结构化条目池 data/items/*.jsonl
# 用法：
#   query-items.sh [--q 关键词] [--days N | --month YYYY-MM] [--category 五类之一] [--all] [--stats]
#
# 选项：
#   --q 关键词        在 title/source 中不区分大小写匹配
#   --days N          只看最近 N 天（按文件日期，默认 7）
#   --month YYYY-MM   只看指定月份（与 --days 互斥）
#   --category CAT    ai-models / ai-products / industry / paper / tip
#   --all             包含未入选条目（默认只列 selected=true）
#   --stats           聚合统计（分类/来源/每日条数），不列明细

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

python3 - "$PROJECT_DIR/data/items" "$@" <<'PYEOF'
import json, os, sys
from collections import Counter
from datetime import date, timedelta

data_dir = sys.argv[1]
args = sys.argv[2:]

query = None
days = 7
month = None
category = None
include_all = False
stats = False

i = 0
while i < len(args):
    a = args[i]
    if a == "--q":
        i += 1; query = args[i].lower()
    elif a == "--days":
        i += 1; days = int(args[i]); month = None
    elif a == "--month":
        i += 1; month = args[i]
    elif a == "--category":
        i += 1; category = args[i]
    elif a == "--all":
        include_all = True
    elif a == "--stats":
        stats = True
    else:
        print(f"Unknown option: {a}", file=sys.stderr)
        sys.exit(1)
    i += 1

if not os.path.isdir(data_dir):
    print(f"No data directory: {data_dir}（还没有任何条目数据）", file=sys.stderr)
    sys.exit(1)

if month:
    def in_scope(d): return d.startswith(month + "-")
else:
    cutoff = date.today() - timedelta(days=days - 1)
    def in_scope(d): return d >= cutoff.isoformat()

items = []
for fname in sorted(os.listdir(data_dir), reverse=True):
    if not fname.endswith(".jsonl"):
        continue
    fdate = fname[:-6]
    if not in_scope(fdate):
        continue
    with open(os.path.join(data_dir, fname), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            obj["_date"] = fdate
            items.append(obj)

if not include_all:
    items = [o for o in items if o.get("selected")]
if category:
    items = [o for o in items if o.get("category") == category]
if query:
    items = [o for o in items
             if query in (o.get("title") or "").lower()
             or query in (o.get("source") or "").lower()]

if stats:
    print(f"条目总数：{len(items)}（{'全部池' if include_all else '仅精选'}）")
    print("\n按分类：")
    for cat, n in Counter(o.get("category") or "未分类" for o in items).most_common():
        print(f"  {cat}: {n}")
    print("\n按来源 Top 15：")
    for src, n in Counter(o.get("source") or "未知" for o in items).most_common(15):
        print(f"  {src}: {n}")
    print("\n按日期：")
    for d, n in sorted(Counter(o["_date"] for o in items).items(), reverse=True):
        print(f"  {d}: {n}")
else:
    print(f"命中 {len(items)} 条（{'全部池' if include_all else '仅精选'}）\n")
    for o in items:
        star = "★" if o.get("selected") else "·"
        cat = o.get("category") or "-"
        print(f"{star} [{o['_date']}] [{cat}] {o.get('title')}")
        print(f"    {o.get('source')} | {o.get('url')}")
PYEOF
