#!/usr/bin/env python3
"""
将 Markdown 文件转换为带基础样式的 HTML。
使用 python-markdown 库，支持表格、代码块、TOC 等扩展。
"""
import sys
import re
import html


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


def wrap_html(body: str, title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.7; max-width: 800px; margin: 0 auto; padding: 20px; color: #333; background: #fafafa; }}
  h1 {{ font-size: 1.8em; border-bottom: 2px solid #ddd; padding-bottom: 0.3em; color: #222; }}
  h2 {{ font-size: 1.5em; margin-top: 1.5em; border-bottom: 1px solid #eee; padding-bottom: 0.2em; color: #333; }}
  h3 {{ font-size: 1.2em; margin-top: 1.2em; color: #555; }}
  ul, ol {{ padding-left: 1.5em; }}
  li {{ margin: 0.3em 0; }}
  hr {{ border: none; border-top: 1px solid #ddd; margin: 2em 0; }}
  strong {{ color: #111; }}
  code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: "SF Mono", Monaco, monospace; font-size: 0.9em; }}
  pre {{ background: #f4f4f4; padding: 12px; border-radius: 6px; overflow-x: auto; }}
  pre code {{ background: transparent; padding: 0; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
  th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
  th {{ background: #f0f0f0; }}
  p {{ margin: 0.8em 0; }}
  a {{ color: #0366d6; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
{body}
</body>
</html>"""


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

    html_doc = wrap_html(body, title)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_doc)

    print(f"Generated {html_file}")


if __name__ == "__main__":
    main()
