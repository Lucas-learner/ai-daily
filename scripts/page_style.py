#!/usr/bin/env python3
"""
站点共享样式与页面骨架：供 md-to-html.py / update-github-pages.py /
update-icloud-index.py 共用，保证各页面风格一致。

- 纯静态、零外部依赖（GitHub Pages 离线可用）
- 暗色模式：默认跟随系统（prefers-color-scheme），可手动切换，选择存 localStorage
- 中文排版优化：PingFang/雅黑字体栈、1.8 行高、加大段落与标题层级对比
"""

# 暗色变量（同时用于"系统暗色 + 未手动指定"和"手动指定深色"两处）
_DARK_VARS = """
    --bg: #0f1115; --card: #171a20; --text: #d3d7dd; --strong: #f0f2f5;
    --muted: #9aa1ab; --border: #2a2f38; --link: #6ea8fe;
    --chip-bg: #23272f; --code-bg: #23262d;
    --topbar-bg: rgba(23, 26, 32, 0.85);
    --shadow: 0 1px 2px rgba(0,0,0,0.4), 0 4px 16px rgba(0,0,0,0.35);
    color-scheme: dark;
"""

BASE_CSS = """
:root {
  --bg: #f5f6f8; --card: #ffffff; --text: #24292f; --strong: #111318;
  --muted: #6b7280; --border: #e3e6ea; --link: #2563eb;
  --chip-bg: #eef1f4; --code-bg: #f1f3f5;
  --topbar-bg: rgba(255, 255, 255, 0.85);
  --shadow: 0 1px 2px rgba(16,24,40,0.05), 0 4px 16px rgba(16,24,40,0.06);
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {""" + _DARK_VARS + """
  }
}
:root[data-theme="dark"] {""" + _DARK_VARS + """
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0; background: var(--bg); color: var(--text); font-size: 16px; line-height: 1.8;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
    "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
  transition: background 0.2s, color 0.2s;
}
a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; }

/* 顶栏 */
.topbar {
  position: sticky; top: 0; z-index: 50;
  display: flex; justify-content: space-between; align-items: center;
  padding: 10px 20px; background: var(--topbar-bg);
  backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border);
}
.site-title { font-weight: 700; color: var(--strong); }
.site-title:hover { text-decoration: none; }
.theme-toggle {
  border: 1px solid var(--border); background: var(--card); color: var(--text);
  border-radius: 999px; padding: 4px 14px; font-size: 13px; cursor: pointer;
}

/* 布局：移动端单列，桌面端带目录侧栏 */
.layout { max-width: 860px; margin: 0 auto; padding: 20px 16px 64px; }
@media (min-width: 1024px) {
  .layout.with-toc {
    max-width: 1180px; display: grid;
    grid-template-columns: 220px minmax(0, 1fr); gap: 28px; align-items: start;
  }
}
.content {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 14px; box-shadow: var(--shadow); padding: 24px 20px;
}
@media (min-width: 640px) { .content { padding: 36px 40px; } }

/* 日期目录（TOC）：移动端折叠顶栏，桌面端 sticky 侧栏 */
.toc { position: sticky; top: 54px; z-index: 40; margin-bottom: 16px; }
.toc-toggle {
  width: 100%; text-align: left; font-size: 15px; cursor: pointer;
  color: var(--text); background: var(--card);
  border: 1px solid var(--border); border-radius: 10px; padding: 10px 14px;
  box-shadow: var(--shadow);
}
.toc-list {
  display: none; list-style: none; margin: 8px 0 0; padding: 8px;
  background: var(--card); border: 1px solid var(--border); border-radius: 10px;
  box-shadow: var(--shadow); max-height: 55vh; overflow-y: auto;
}
.toc.open .toc-list { display: block; }
.toc-list a {
  display: block; padding: 6px 10px; border-radius: 8px;
  color: var(--muted); font-size: 14px;
}
.toc-list a:hover { background: var(--chip-bg); text-decoration: none; }
.toc-list a.active { color: var(--link); background: var(--chip-bg); font-weight: 600; }
@media (min-width: 1024px) {
  .toc { top: 70px; margin-bottom: 0; }
  .toc-toggle { display: none; }
  .toc-list {
    display: block; border: none; background: transparent; box-shadow: none;
    padding: 0; max-height: calc(100vh - 100px);
  }
}

/* 返回顶部 */
.back-to-top {
  position: fixed; right: 20px; bottom: 24px; z-index: 60;
  width: 44px; height: 44px; border-radius: 50%; font-size: 18px; cursor: pointer;
  border: 1px solid var(--border); background: var(--card); color: var(--text);
  box-shadow: var(--shadow); opacity: 0; visibility: hidden;
  transition: opacity 0.2s, visibility 0.2s;
}
.back-to-top.show { opacity: 1; visibility: visible; }

/* 中文排版：标题层级对比、段落间距 */
h1 { font-size: 1.65rem; line-height: 1.35; margin: 0 0 0.4em; color: var(--strong); }
h2 {
  font-size: 1.35rem; margin: 1.8em 0 0.6em; padding-top: 0.5em;
  border-top: 1px solid var(--border); color: var(--strong); scroll-margin-top: 70px;
}
h3 { font-size: 1.1rem; margin: 1.4em 0 0.4em; color: var(--strong); }
p { margin: 0.9em 0; }
ul, ol { padding-left: 1.5em; }
li { margin: 0.35em 0; }
hr { border: none; border-top: 1px solid var(--border); margin: 1.6em 0; }
strong { color: var(--strong); }
code {
  background: var(--code-bg); padding: 2px 6px; border-radius: 6px; font-size: 0.88em;
  font-family: "SF Mono", Menlo, Monaco, Consolas, monospace;
}
pre { background: var(--code-bg); padding: 14px; border-radius: 10px; overflow-x: auto; }
pre code { background: transparent; padding: 0; }
blockquote { margin: 1em 0; padding: 0.2em 1em; border-left: 3px solid var(--border); color: var(--muted); }
table { border-collapse: collapse; width: 100%; margin: 1.2em 0; }
th, td { border: 1px solid var(--border); padding: 8px 10px; text-align: left; }
th { background: var(--chip-bg); }
.meta { color: var(--muted); font-size: 0.9em; }

/* 索引页卡片 */
.card {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 14px; box-shadow: var(--shadow); padding: 20px; margin: 16px 0;
}
.card h2 { border-top: none; padding-top: 0; margin-top: 0; font-size: 1.2rem; }
"""

# 防闪烁：渲染前先从 localStorage 恢复手动选择的主题
HEAD_THEME_JS = """<script>
(function () {
  var t = localStorage.getItem('ai-daily-theme');
  if (t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t);
})();
</script>"""

# 页尾交互：主题切换 / 返回顶部 / 目录折叠 / 阅读位置高亮（元素不存在时自动跳过）
BODY_JS = """<script>
(function () {
  // 主题切换：自动 → 浅色 → 深色 循环，选择存 localStorage
  var themeBtn = document.getElementById('themeToggle');
  function applyTheme(t) {
    if (t === 'auto') document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme', t);
    if (themeBtn) themeBtn.textContent = t === 'dark' ? '🌙 深色' : t === 'light' ? '☀️ 浅色' : '🌗 自动';
  }
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var cur = localStorage.getItem('ai-daily-theme') || 'auto';
      var next = cur === 'auto' ? 'light' : cur === 'light' ? 'dark' : 'auto';
      localStorage.setItem('ai-daily-theme', next);
      applyTheme(next);
    });
    applyTheme(localStorage.getItem('ai-daily-theme') || 'auto');
  }

  // 返回顶部
  var backToTop = document.getElementById('backToTop');
  if (backToTop) {
    window.addEventListener('scroll', function () {
      backToTop.classList.toggle('show', window.scrollY > 600);
    }, { passive: true });
    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 移动端目录折叠（桌面端由 CSS 强制展开）
  var toc = document.getElementById('toc');
  var tocToggle = document.getElementById('tocToggle');
  if (toc && tocToggle) {
    tocToggle.addEventListener('click', function () {
      var open = toc.classList.toggle('open');
      tocToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    toc.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && window.innerWidth < 1024) toc.classList.remove('open');
    });
  }

  // 当前阅读位置在目录中高亮
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc-list a[href^="#"]'));
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var linkById = {};
    var headings = [];
    tocLinks.forEach(function (a) {
      var h = document.getElementById(a.getAttribute('href').slice(1));
      if (h) { linkById[h.id] = a; headings.push(h); }
    });
    var visible = {};
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { visible[en.target.id] = en.isIntersecting; });
      for (var i = 0; i < headings.length; i++) {
        if (visible[headings[i].id]) {
          tocLinks.forEach(function (a) { a.classList.remove('active'); });
          linkById[headings[i].id].classList.add('active');
          break;
        }
      }
    }, { rootMargin: '-70px 0px -65% 0px', threshold: 0 });
    headings.forEach(function (h) { observer.observe(h); });
  }
})();
</script>"""


def page_shell(title, main_html, toc_html="", home_href="index.html",
               content_class="content", extra_js=""):
    """组装完整 HTML 页面：顶栏 + （可选）日期目录 + 主内容 + 返回顶部 + 脚本。"""
    import html as _html

    toc_block = ""
    layout_class = "layout"
    if toc_html:
        toc_block = (
            '<nav class="toc" id="toc" aria-label="日期目录">\n'
            + toc_html + "\n</nav>"
        )
        layout_class = "layout with-toc"

    extra = ("\n<script>\n" + extra_js + "\n</script>") if extra_js else ""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{_html.escape(title)}</title>
{HEAD_THEME_JS}
<style>{BASE_CSS}</style>
</head>
<body>
<header class="topbar">
  <a class="site-title" href="{home_href}">📰 AI日报</a>
  <button id="themeToggle" class="theme-toggle" type="button">🌗 自动</button>
</header>
<div class="{layout_class}">
{toc_block}
<main class="{content_class}">
{main_html}
</main>
</div>
<button id="backToTop" class="back-to-top" type="button" aria-label="返回顶部">↑</button>
{BODY_JS}{extra}
</body>
</html>"""
