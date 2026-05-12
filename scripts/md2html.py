#!/usr/bin/env python3
"""
md2html.py — 把 Markdown 转成 any-reports 站点的 HTML 单页。

用法:
    python scripts/md2html.py <input.md>
    python scripts/md2html.py <input.md> --slug claude-code-advanced-guide
    python scripts/md2html.py <input.md> --slug foo --title "Foo 报告"

输出:
    ./<slug>.html  （仓库根目录）
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
import unicodedata
from pathlib import Path
from xml.etree import ElementTree as ET

import markdown
from markdown.extensions.toc import TocExtension


ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "scripts" / "template.html"


def slugify(text: str) -> str:
    """轻量 slugify：用于推断输出文件名（与锚点 slug 区分）。"""
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[^\w一-鿿\-]+", "-", text, flags=re.UNICODE)
    text = re.sub(r"-{2,}", "-", text).strip("-").lower()
    return text or "untitled"


def gfm_slugify(text: str, separator: str = "-") -> str:
    """GFM-style slugify：保留中文 + 单字符空格→分隔符，**不**折叠连续分隔符。
    这样 `## A — B` 会被 slug 成 `a--b`（双分隔），与 GitHub 渲染 MD 内手写
    TOC 链接的行为一致 —— 让 `## 📑 目录` 章节里的内部锚点能继续生效。
    """
    t = unicodedata.normalize("NFKC", text).lower()
    t = re.sub(r"[^\w\- ]", "", t, flags=re.UNICODE)
    return t.replace(" ", separator)


def render_markdown(md_text: str) -> tuple[str, list[dict], str]:
    """渲染 MD → (html, toc_tokens, h1_title)。"""
    md = markdown.Markdown(
        extensions=[
            "fenced_code",
            "tables",
            "attr_list",
            "def_list",
            "footnotes",
            "sane_lists",
            "nl2br",
            "admonition",
            "md_in_html",
            "codehilite",
            TocExtension(
                permalink=True,
                anchorlink=False,
                toc_depth="2-4",
                slugify=gfm_slugify,
            ),
        ],
        extension_configs={
            "codehilite": {
                "css_class": "codehilite",
                "guess_lang": False,
                "use_pygments": True,
            },
        },
    )
    html = md.convert(md_text)
    toc_tokens = getattr(md, "toc_tokens", [])

    # 抽 H1 当默认标题
    m = re.search(r"^# +(.+?)$", md_text, flags=re.M)
    h1 = m.group(1).strip() if m else ""
    return html, toc_tokens, h1


def post_process(html: str) -> str:
    """正文 HTML 后处理：外链 target=_blank，emoji 引用块加 callout，等。"""

    # 1) 外链 target=_blank
    def _ext_link(m: re.Match) -> str:
        href = m.group(1)
        if href.startswith(("http://", "https://")) and "pluto235.github.io" not in href:
            return f'<a href="{href}" target="_blank" rel="noopener">'
        return m.group(0)

    html = re.sub(r'<a href="([^"]+)">', _ext_link, html)

    # 2) 以 emoji 开头的 blockquote → callout 样式
    emoji_re = re.compile(
        r"<blockquote>\s*<p>(\s*(?:📢|🎓|💡|⚠️|🔥|✨|⭐|🚀|🎯|📌|❗|‼️|🔑|📝|📊|📈|🐛|🛠️|🤖|⏰|🏆|🎉))",
    )
    html = emoji_re.sub(r'<blockquote class="callout"><p>\1', html)

    return html


def build_nav(toc_tokens: list[dict], max_depth: int = 3) -> str:
    """从 TOC tokens 构建左侧 nav 的 HTML（嵌套 ol/li/a）。"""
    if not toc_tokens:
        return "<p style='color:var(--c-text-mute);font-size:13px'>（无章节）</p>"

    def walk(tokens: list[dict], depth: int) -> str:
        if depth > max_depth or not tokens:
            return ""
        out = ["<ol>"]
        for t in tokens:
            tid = t.get("id", "")
            name = t.get("name", "")
            children_html = walk(t.get("children", []), depth + 1)
            out.append(f'<li><a href="#{tid}">{name}</a>{children_html}</li>')
        out.append("</ol>")
        return "".join(out)

    return walk(toc_tokens, 1)


def build_anchors(toc_tokens: list[dict]) -> str:
    """右侧锚点：扁平列出所有 h2（toc_depth 起点）。"""
    if not toc_tokens:
        return ""
    out = []
    for t in toc_tokens:
        tid = t.get("id", "")
        name = t.get("name", "")
        out.append(f'<li><a href="#{tid}">{name}</a></li>')
    return "".join(out)


def html_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", type=Path, help="Markdown 文件路径")
    ap.add_argument("--slug", help="输出文件名（无扩展），默认从输入文件名推断")
    ap.add_argument("--title", help="页面标题，默认取 MD 中第一个 H1")
    ap.add_argument(
        "--description",
        default="",
        help="meta description，默认空",
    )
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT,
        help=f"输出目录（默认 {ROOT}）",
    )
    args = ap.parse_args()

    if not args.input.exists():
        print(f"error: {args.input} 不存在", file=sys.stderr)
        return 1
    if not TEMPLATE.exists():
        print(f"error: template 缺失 {TEMPLATE}", file=sys.stderr)
        return 1

    md_text = args.input.read_text(encoding="utf-8")
    html_body, toc_tokens, h1 = render_markdown(md_text)
    html_body = post_process(html_body)

    title = args.title or h1 or args.input.stem
    slug = args.slug or slugify(args.input.stem)

    template = TEMPLATE.read_text(encoding="utf-8")
    page = (
        template.replace("{{TITLE}}", html_escape(title))
        .replace("{{DESCRIPTION}}", html_escape(args.description or title))
        .replace("{{ASSETS_PREFIX}}", "")
        .replace("{{NAV}}", build_nav(toc_tokens))
        .replace("{{ANCHORS}}", build_anchors(toc_tokens))
        .replace("{{CONTENT}}", html_body)
        .replace("{{UPDATED_DATE}}", _dt.date.today().isoformat())
    )

    out_path = args.out_dir / f"{slug}.html"
    out_path.write_text(page, encoding="utf-8")
    print(f"wrote {out_path}  ({len(page):,} bytes)")
    print(f"  title:    {title}")
    print(f"  sections: {len(toc_tokens)} top-level")
    return 0


if __name__ == "__main__":
    sys.exit(main())
