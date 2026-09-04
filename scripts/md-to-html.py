#!/usr/bin/env python3
"""
将 Markdown 文件转换为带样式的 HTML。
使用 python-markdown 库，支持表格、代码块、TOC 等扩展。
页面骨架与样式见 scripts/page_style.py（卡片式设计 + 暗色模式）。
"""
import sys
import re
import html
from pathlib import Path

import page_style

# 月报日期二级标题，如 <h2 id="2026-07-30">【2026-07-30】</h2>
DATE_H2_RE = re.compile(r'<h2([^>]*)>【(\d{4}-\d{2}-\d{2})】([^<]*)</h2>')


def get_markdown_module():
    """优先使用项目 venv 中的 markdown 模块。"""
    import importlib.util
    venv_markdown = "/Users/macmini/projects/skills/ai-daily/.venv/lib/python3.9/site-packages"
    if importlib.util.find_spec("markdown") is None and venv_markdown not in sys.path:
        sys.path.insert(0, venv_markdown)
    import markdown
    return markdown


def inline_format(text: str) -> str:
    # Bold **text**
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic *text*
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    # Code `text`
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return html.escape(text, quote=False).replace("&lt;strong&gt;", "<strong>").replace("&lt;/strong&gt;", "</strong>").replace("&lt;em&gt;", "<em>").replace("&lt;/em&gt;", "</em>").replace("&lt;code&gt;", "<code>").replace("&lt;/code&gt;", "</code>")


def fallback_md_to_html(text: str) -> str:
    """当 python-markdown 不可用时使用的简易转换器。"""
    lines = text.splitlines()
    output = []
    in_ul = False
    in_ol = False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            output.append("</ul>")
            in_ul = False
        if in_ol:
            output.append("</ol>")
            in_ol = False

    for raw_line in lines:
        line = raw_line.rstrip()

        if re.fullmatch(r"\s*[-*]{3,}\s*", line):
            close_lists()
            output.append("<hr />")
            continue

        if not line.strip():
            close_lists()
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_lists()
            level = len(m.group(1))
            title = inline_format(m.group(2))
            output.append(f"<h{level}>{title}</h{level}>")
            continue

        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            if not in_ul:
                close_lists()
                output.append("<ul>")
                in_ul = True
            output.append(f"<li>{inline_format(m.group(1))}</li>")
            continue

        m = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m:
            if not in_ol:
                close_lists()
                output.append("<ol>")
                in_ol = True
            output.append(f"<li>{inline_format(m.group(1))}</li>")
            continue

        close_lists()
        output.append(f"<p>{inline_format(line)}</p>")

    close_lists()
    return "\n".join(output)


def add_date_anchors_and_toc(body: str):
    """为日期二级标题补齐锚点 id，并抽取日期目录。

    返回 (body, toc_html)；少于 2 个日期标题时 toc_html 为空，不生成目录。
    """
    dates = []

    def repl(m):
        attrs, date, rest = m.group(1), m.group(2), m.group(3)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            anchor = idm.group(1)
        else:
            anchor = date
            attrs = f' id="{anchor}"' + attrs
        dates.append(anchor)
        return f"<h2{attrs}>【{date}】{rest}</h2>"

    body = DATE_H2_RE.sub(repl, body)
    if len(dates) < 2:
        return body, ""

    items = "".join(
        f'<li><a href="#{d}" title="{d}">{d[5:]}</a></li>' for d in dates
    )
    toc_html = (
        f'<button class="toc-toggle" id="tocToggle" type="button" '
        f'aria-expanded="false">📑 日期目录（{len(dates)} 天）</button>\n'
        f'<ul class="toc-list">{items}</ul>'
    )
    return body, toc_html


def wrap_html(body: str, title: str, toc_html: str = "", home_href: str = "index.html") -> str:
    return page_style.page_shell(
        title, body, toc_html=toc_html, home_href=home_href
    )


def main():
    if len(sys.argv) != 3:
        print("Usage: md-to-html.py input.md output.html", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    try:
        markdown = get_markdown_module()
        body = markdown.markdown(
            md_text,
            extensions=["tables", "fenced_code", "toc", "nl2br"],
            extension_configs={"toc": {"permalink": False}}
        )
    except Exception as e:
        print(f"Warning: python-markdown failed ({e}), using fallback converter", file=sys.stderr)
        body = fallback_md_to_html(md_text)

    title_match = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    title = title_match.group(1) if title_match else "AI日报"

    body, toc_html = add_date_anchors_and_toc(body)

    # reports/ 下的页面上级目录才有索引页，返回链接相应上调一级
    home_href = "../index.html" if Path(html_file).parent.name == "reports" else "index.html"

    html_doc = wrap_html(body, title, toc_html, home_href)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_doc)

    print(f"Generated {html_file}")


if __name__ == "__main__":
    main()
