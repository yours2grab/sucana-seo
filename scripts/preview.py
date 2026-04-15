#!/usr/bin/env python3
"""
Sucana SEO Blog Writer — HTML preview generator.

Usage:
    python3 preview.py <path-to-article.md>

Renders the markdown article to a clean HTML file (Inter font, 720px max-width,
purple/pink stage blocks) and opens it in the default browser.

Called at every article review point in the skill:
- After Step 5a opening is drafted
- After Step 5b body is written
- After Step 5c FAQ is added
- In Step 8 final review (Human Loop #5)
- Any time the article file is edited

Never shows markdown in chat. Always renders to HTML and opens the browser.
"""

import sys
import os
import re
import subprocess
import html as htmllib
from pathlib import Path


CSS = """
body {
    font-family: Inter, -apple-system, BlinkMacSystemFont, sans-serif;
    max-width: 720px;
    margin: 40px auto;
    padding: 0 20px;
    color: #1a1a1a;
    line-height: 1.65;
    font-size: 17px;
    background: #fff;
}
h1 { font-size: 40px; line-height: 1.2; margin: 32px 0 16px; color: #0f172a; }
h2 { font-size: 28px; line-height: 1.3; margin: 48px 0 16px; color: #9333EA; }
h3 { font-size: 20px; margin: 32px 0 12px; color: #0f172a; }
p { margin: 16px 0; }
pre {
    background: #FAF5FF;
    border-left: 4px solid #9333EA;
    padding: 20px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 14px;
    line-height: 1.5;
}
code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
p code { background: #f3f0ff; padding: 2px 6px; border-radius: 4px; color: #9333EA; }
table { border-collapse: collapse; margin: 24px 0; width: 100%; font-size: 15px; }
th, td { padding: 12px; text-align: left; border-bottom: 1px solid #e5e5e5; }
th { background: #FAF5FF; color: #9333EA; font-weight: 700; }
strong { color: #1a1a1a; font-weight: 700; }
em { color: #555; font-style: italic; }
ul { margin: 16px 0; padding-left: 24px; }
ol { margin: 16px 0; padding-left: 24px; }
li { margin: 12px 0; }
blockquote {
    border-left: 4px solid #ec4899;
    padding: 8px 20px;
    margin: 24px 0;
    color: #555;
    font-style: italic;
    background: #fef3f8;
}
img { max-width: 100%; border-radius: 8px; margin: 24px 0; }
.stage {
    background: #FAF5FF;
    border-radius: 12px;
    padding: 24px;
    margin: 24px 0;
}
.stage-title { font-size: 20px; font-weight: 700; color: #9333EA; margin-bottom: 16px; }
"""


def md_to_html(md: str) -> str:
    """Minimal markdown → HTML converter tuned for Sucana blog template."""

    # 1. Fenced code blocks (preserve first so later regex does not touch them)
    code_blocks = []
    def code_sub(m):
        code_blocks.append(htmllib.escape(m.group(1)))
        return f'\x00CODEBLOCK{len(code_blocks) - 1}\x00'
    md = re.sub(r'```[a-zA-Z0-9]*\n(.*?)```', code_sub, md, flags=re.DOTALL)

    # 2. Headings
    md = re.sub(r'^### (.+)$', r'<h3>\1</h3>', md, flags=re.MULTILINE)
    md = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md, flags=re.MULTILINE)
    md = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md, flags=re.MULTILINE)

    # 3. Blockquotes
    md = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', md, flags=re.MULTILINE)

    # 4. Bold + italic
    md = re.sub(r'\*\*([^*\n]+)\*\*', r'<strong>\1</strong>', md)
    md = re.sub(r'(?<![\*\w])\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', md)

    # 5. Inline code (after blocks are stashed)
    md = re.sub(r'`([^`\n]+)`', r'<code>\1</code>', md)

    # 6. Images: ![alt](src)
    md = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', md)

    # 7. Links: [text](url)
    md = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', md)

    # 8. Tables (pipe syntax)
    def table_sub(m):
        rows = [r.strip() for r in m.group(0).strip().split('\n') if r.strip()]
        if len(rows) < 2:
            return m.group(0)
        header = [c.strip() for c in rows[0].strip('|').split('|')]
        body_rows = []
        for r in rows[2:]:  # skip separator row (row 1)
            cells = [c.strip() for c in r.strip('|').split('|')]
            body_rows.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
        head_html = '<thead><tr>' + ''.join(f'<th>{c}</th>' for c in header) + '</tr></thead>'
        body_html = '<tbody>' + ''.join(body_rows) + '</tbody>'
        return f'<table>{head_html}{body_html}</table>'
    md = re.sub(
        r'(^\|.+\|$\n^\|[\s\-|:]+\|$\n(?:^\|.+\|$\n?)+)',
        table_sub, md, flags=re.MULTILINE
    )

    # 9. Lists (simple: unordered + ordered)
    def process_lists(text):
        lines = text.split('\n')
        out = []
        i = 0
        while i < len(lines):
            line = lines[i]
            ul_match = re.match(r'^- (.+)$', line)
            ol_match = re.match(r'^\d+\. (.+)$', line)
            if ul_match:
                items = []
                while i < len(lines) and re.match(r'^- (.+)$', lines[i]):
                    items.append(re.match(r'^- (.+)$', lines[i]).group(1))
                    i += 1
                out.append('<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>')
            elif ol_match:
                items = []
                while i < len(lines) and re.match(r'^\d+\. (.+)$', lines[i]):
                    items.append(re.match(r'^\d+\. (.+)$', lines[i]).group(1))
                    i += 1
                out.append('<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>')
            else:
                out.append(line)
                i += 1
        return '\n'.join(out)
    md = process_lists(md)

    # 10. Paragraphs (wrap loose text)
    blocks = md.split('\n\n')
    html_blocks = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        if b.startswith(('<h', '<pre', '<table', '<ul', '<ol', '<blockquote', '<img', '\x00CODEBLOCK')):
            html_blocks.append(b)
        else:
            html_blocks.append(f'<p>{b}</p>')
    result = '\n\n'.join(html_blocks)

    # 11. Restore code blocks
    for i, block in enumerate(code_blocks):
        result = result.replace(f'\x00CODEBLOCK{i}\x00', f'<pre><code>{block}</code></pre>')

    return result


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 preview.py <path-to-article.md>', file=sys.stderr)
        sys.exit(1)

    article_path = Path(sys.argv[1]).expanduser().resolve()
    if not article_path.exists():
        print(f'ERROR: file not found: {article_path}', file=sys.stderr)
        sys.exit(1)

    md = article_path.read_text()
    body = md_to_html(md)
    slug = article_path.stem.lower().replace(' ', '-')[:60]
    preview_path = article_path.parent / f'.preview-{slug}.html'

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Preview: {htmllib.escape(article_path.stem)}</title>
    <style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""

    preview_path.write_text(page)
    subprocess.run(['open', str(preview_path)])
    print(f'HTML preview opened: {preview_path}')


if __name__ == '__main__':
    main()
