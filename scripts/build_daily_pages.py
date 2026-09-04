#!/Users/macmini/projects/skills/ai-daily/.venv/bin/python3
"""
从结构化条目池 data/items/YYYY-MM-DD.jsonl 生成按日浏览页面 docs/days/YYYY-MM-DD.html。

- 页面顶部为分类筛选 chips（全部/模型/产品/行业/论文/观点），纯前端 JS 筛选，
  无数据的分类自动隐藏
- 区分精选（selected=true，默认显示）与全部条目（可切换）
- data/items/ 为空时不生成任何页面，索引页也不显示入口（向后兼容）

用法：build_daily_pages.py [--items-dir DIR] [--out-dir DIR]
（--items-dir/--out-dir 主要用于用 /tmp 下的样例数据做测试）
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import page_style

PROJECT_DIR = Path(__file__).resolve().parent.parent
ITEMS_DIR = PROJECT_DIR / "data" / "items"
DAYS_DIR = PROJECT_DIR / "docs" / "days"

CATEGORIES = [
    ("ai-models", "模型"),
    ("ai-products", "产品"),
    ("industry", "行业"),
    ("paper", "论文"),
    ("tip", "观点"),
]
CATEGORY_LABELS = dict(CATEGORIES)

DAY_FILE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.jsonl$")
DAY_HTML_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.html$")

# 前端筛选逻辑：分类 chips + 精选/全部切换，纯 vanilla JS
FILTER_JS = """
(function () {
  var items = Array.prototype.slice.call(document.querySelectorAll('.item'));
  if (!items.length) return;
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip'));
  var segBtns = Array.prototype.slice.call(document.querySelectorAll('.seg button'));
  var emptyHint = document.getElementById('emptyHint');
  var state = { cat: 'all', selectedOnly: true };

  // 当天没有精选条目时，默认展示全部
  if (!items.some(function (el) { return el.dataset.selected === '1'; })) {
    state.selectedOnly = false;
  }

  function apply() {
    // 当前范围（精选/全部）内的条目
    var scope = items.filter(function (el) {
      return !state.selectedOnly || el.dataset.selected === '1';
    });
    // 统计各分类条目数，无数据的分类 chip 自动隐藏
    var counts = { all: scope.length };
    scope.forEach(function (el) {
      var c = el.dataset.cat || '';
      if (c) counts[c] = (counts[c] || 0) + 1;
    });
    // 当前分类在该范围内无条目时回退到「全部」
    if (state.cat !== 'all' && !(counts[state.cat] > 0)) state.cat = 'all';
    chips.forEach(function (chip) {
      var c = chip.dataset.cat;
      var n = counts[c] || 0;
      chip.hidden = c !== 'all' && n === 0;
      chip.textContent = chip.dataset.label + ' ' + n;
      chip.classList.toggle('active', c === state.cat);
    });
    var shown = 0;
    items.forEach(function (el) {
      var inScope = !state.selectedOnly || el.dataset.selected === '1';
      var catOk = state.cat === 'all' || el.dataset.cat === state.cat;
      var show = inScope && catOk;
      el.style.display = show ? '' : 'none';
      if (show) shown++;
    });
    segBtns.forEach(function (b) {
      b.classList.toggle('active', (b.dataset.mode === 'selected') === state.selectedOnly);
    });
    if (emptyHint) emptyHint.hidden = shown !== 0;
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () { state.cat = chip.dataset.cat; apply(); });
  });
  segBtns.forEach(function (b) {
    b.addEventListener('click', function () { state.selectedOnly = b.dataset.mode === 'selected'; apply(); });
  });
  apply();
})();
"""


def load_day_items(items_dir: Path) -> dict:
    """读取 items_dir 下所有日期 jsonl，返回 {date: [item, ...]}（日期升序）。"""
    days = {}
    if not items_dir.is_dir():
        return days
    for f in sorted(items_dir.iterdir()):
        if not (f.is_file() and DAY_FILE_RE.match(f.name)):
            continue
        items = []
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Warning: skip invalid JSON line in {f.name}: {e}", file=sys.stderr)
        if items:
            days[f.stem] = items
    return days


def render_day_page(date: str, items: list) -> str:
    """渲染单日页面 HTML。"""
    chips = ['<button class="chip active" type="button" data-cat="all" data-label="全部">全部</button>']
    for key, label in CATEGORIES:
        chips.append(
            f'<button class="chip" type="button" data-cat="{key}" data-label="{label}" hidden>{label}</button>'
        )

    cards = ""
    for it in items:
        cat = it.get("category") or ""
        label = CATEGORY_LABELS.get(cat, "")
        grade = it.get("grade") or ""
        selected = bool(it.get("selected"))
        star = '<span class="star" title="精选">★</span> ' if selected else ""
        badges = ""
        if label:
            badges += f'<span class="badge">{label}</span>'
        if grade:
            badges += f'<span class="badge badge-grade">{html.escape(str(grade))}</span>'
        published = str(it.get("publishedAt") or "").strip()
        time_part = f' · {html.escape(published)}' if published else ""
        cards += f"""<article class="item" data-cat="{html.escape(cat)}" data-selected="{'1' if selected else '0'}">
  <div>{star}<a class="item-title" href="{html.escape(str(it.get('url', '')), quote=True)}" target="_blank" rel="noopener">{html.escape(str(it.get('title', '')))}</a></div>
  <div class="item-meta">{badges}{html.escape(str(it.get('source', '')))}{time_part}</div>
</article>
"""

    main_html = f"""<h1>🗓️ {html.escape(date)}</h1>
<p class="meta">当日采集条目池（共 {len(items)} 条）。精选为入选日报的内容，可切换查看全部。</p>
<div class="toolbar">
  <div class="seg">
    <button type="button" data-mode="selected" class="active">⭐ 精选</button>
    <button type="button" data-mode="all">全部条目</button>
  </div>
</div>
<div class="chips">
{''.join(chips)}
</div>
<div class="items">
{cards}</div>
<p id="emptyHint" class="meta" hidden>该分类下暂无条目。</p>"""

    return page_style.page_shell(
        f"AI日报 | {date}", main_html, home_href="../index.html", extra_js=FILTER_JS
    )


def build(items_dir=None, out_dir=None):
    """生成全部按日页面，返回 [(date, total, selected), ...]（日期逆序）。

    data/items 为空（或无有效条目）时返回 []，并清理已生成的过期页面。
    """
    items_dir = Path(items_dir) if items_dir else ITEMS_DIR
    out_dir = Path(out_dir) if out_dir else DAYS_DIR

    days = load_day_items(items_dir)
    dates = sorted(days.keys(), reverse=True)

    # 清理已无数据对应的过期页面（只删生成器产物格式的文件）
    if out_dir.is_dir():
        for f in out_dir.iterdir():
            if f.is_file() and DAY_HTML_RE.match(f.name) and f.stem not in days:
                f.unlink()
                print(f"Removed stale docs/days/{f.name}")

    if not dates:
        return []

    out_dir.mkdir(parents=True, exist_ok=True)
    result = []
    for date in dates:
        items = days[date]
        selected = sum(1 for it in items if it.get("selected"))
        target = out_dir / f"{date}.html"
        content = render_day_page(date, items)
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            target.write_text(content, encoding="utf-8")
            print(f"Generated docs/days/{date}.html ({selected}/{len(items)} 精选)")
        result.append((date, len(items), selected))
    return result


def main():
    parser = argparse.ArgumentParser(description="生成 docs/days/ 按日浏览页面")
    parser.add_argument("--items-dir", help="条目 jsonl 目录（默认 data/items）")
    parser.add_argument("--out-dir", help="输出目录（默认 docs/days）")
    args = parser.parse_args()

    result = build(items_dir=args.items_dir, out_dir=args.out_dir)
    if not result:
        print("No items data, skip day pages")


if __name__ == "__main__":
    main()
