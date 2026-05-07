#!/usr/bin/env python3
"""
把横纵分析报告的 Markdown 渲染为编辑部长读网页（Optical Essay 美学）。

用法：
    python md_to_web.py input.md output.html --title "研究对象名称" --author "数字生命卡兹克"
    # 可选 --accent 覆盖主色（默认深宝石蓝）：
    python md_to_web.py input.md output.html --title "..." --accent "#2f6b4a"

依赖：
    pip install markdown --break-system-packages

设计基线（Optical Essay）：
- 配色：纸本米 #f4efe4 / 深墨 #121212 / 主色可替换 / 锈橙 #b04824 点睛
- 字体：Fraunces 变轴衬线 + 思源宋体 + JetBrains Mono
- 骨架：封面 hero + Landing TOC 章节（编号/标题/副标题/梗概三列）+ 每章大号 Fraunces Italic 序号 + 首段 drop cap + 右侧固定 side-toc 滚动追踪 + 顶部滚动进度条 + 右下角"返回目录"浮动 pill
- 交互：IntersectionObserver 淡入、侧栏章节跟随高亮、scroll smooth、FAB 锚回 #contents
"""
import argparse
import re
from pathlib import Path

try:
    import markdown as md
except ImportError:
    raise SystemExit("缺少依赖：pip install markdown --break-system-packages")


def slugify(text):
    s = re.sub(r"[^\w\u4e00-\u9fff]+", "-", text).strip("-")
    return s.lower() or "sec"


def add_h_ids(html):
    def repl(m):
        tag, attrs, text = m.group(1), m.group(2), m.group(3)
        if "id=" in attrs:
            return m.group(0)
        return f"<{tag} id=\"{slugify(text)}\"{attrs}>{text}</{tag}>"
    return re.sub(r"<(h[1-6])([^>]*)>(.+?)</\1>", repl, html, flags=re.DOTALL)


def strip_tags(html_fragment):
    """Drop HTML tags and collapse whitespace, return plain text."""
    txt = re.sub(r"<[^>]+>", "", html_fragment)
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt


def truncate_blurb(text, max_chars=90):
    """Truncate to ~max_chars (counts CJK as 1 each), append ellipsis if cut."""
    if not text:
        return ""
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "…"


def extract_chapter_meta(html_body):
    """Walk html_body, return list of {sid, title, subtitle, blurb} per H2 chapter.

    - title: H2 text with leading「一、」style numbering stripped
    - subtitle: text of the FIRST <h3> inside the chapter body (empty if none)
    - blurb: first non-empty <p> text in the chapter, truncated to ~90 chars
    """
    chunks = re.split(r'(<h2 id="[^"]+">.*?</h2>)', html_body)
    metas = []
    i = 1
    while i < len(chunks):
        h2_html = chunks[i]
        body_html = chunks[i + 1] if i + 1 < len(chunks) else ""
        m = re.match(r'<h2 id="([^"]+)">(.+?)</h2>', h2_html, flags=re.DOTALL)
        if not m:
            i += 2
            continue
        sid = m.group(1)
        title_raw = strip_tags(m.group(2))
        title = re.sub(r"^[一二三四五六七八九十]+、\s*", "", title_raw)
        # subtitle: first H3
        h3_match = re.search(r"<h3[^>]*>(.+?)</h3>", body_html, flags=re.DOTALL)
        subtitle = strip_tags(h3_match.group(1)) if h3_match else ""
        # blurb: first non-empty <p>
        blurb = ""
        for p_match in re.finditer(r"<p[^>]*>(.+?)</p>", body_html, flags=re.DOTALL):
            ptext = strip_tags(p_match.group(1))
            if ptext:
                blurb = ptext
                break
        blurb = truncate_blurb(blurb, 90)
        metas.append({"sid": sid, "title": title, "subtitle": subtitle, "blurb": blurb})
        i += 2
    return metas


def build(md_path: Path, out_path: Path, title: str, author: str, accent: str):
    raw = md_path.read_text(encoding="utf-8")

    # 提元信息
    lines = raw.splitlines()
    cover_title, cover_meta = title, ""
    body_lines = []
    first_h1_seen = False
    for ln in lines:
        if not first_h1_seen and ln.startswith("# "):
            if not cover_title or cover_title == title:
                cover_title = ln[2:].strip() or title
            first_h1_seen = True
            continue
        if first_h1_seen and not cover_meta and ln.startswith("> "):
            cover_meta = ln[2:].strip()
            continue
        body_lines.append(ln)
    body_md = "\n".join(body_lines)

    html_body = md.markdown(
        body_md,
        extensions=["tables", "fenced_code", "attr_list", "toc"],
        output_format="html5",
    )
    html_body = add_h_ids(html_body)

    h2_list = re.findall(r'<h2 id="([^"]+)">(.+?)</h2>', html_body)
    side_toc_html = "".join(
        f'<li><a href="#{sid}" data-target="{sid}">{t.split("、")[-1] if "、" in t else t}<span class="side-toc__num">{str(i+1).zfill(2)}</span></a></li>'
        for i, (sid, t) in enumerate(h2_list)
    )

    # Landing TOC: 编号 / 标题+副标题 / 一两句梗概，全行可锚跳
    chapter_metas = extract_chapter_meta(html_body)
    landing_toc_rows = []
    for idx, meta in enumerate(chapter_metas):
        num = str(idx + 1).zfill(2)
        sub_html = f'<div class="landing-toc__sub">{meta["subtitle"]}</div>' if meta["subtitle"] else ""
        blurb_html = meta["blurb"] or "（本章无可供摘录的首段。）"
        landing_toc_rows.append(
            f'''<li class="landing-toc__row">
  <a href="#{meta["sid"]}" data-target="{meta["sid"]}">
    <div class="landing-toc__num">
      <span class="landing-toc__n">{num}</span>
      <span class="landing-toc__code">§ {num}</span>
    </div>
    <div class="landing-toc__main">
      <div class="landing-toc__title">{meta["title"]}</div>
      {sub_html}
    </div>
    <div class="landing-toc__blurb">{blurb_html}</div>
  </a>
</li>'''
        )
    landing_toc_html = "\n".join(landing_toc_rows)

    # 包章节壳
    sections = re.split(r'(<h2 id="[^"]+">.*?</h2>)', html_body)
    chi_num = ["壹","贰","叁","肆","伍","陆","柒","捌","玖","拾"]
    arabic = [f"{n:02d}" for n in range(1, 20)]
    assembled = [sections[0]]
    k = 0
    i = 1
    while i < len(sections):
        h2_tag = sections[i]
        body = sections[i+1] if i+1 < len(sections) else ""
        m = re.match(r'<h2 id="([^"]+)">(.+?)</h2>', h2_tag)
        if m:
            sid, t = m.group(1), m.group(2)
            t_clean = re.sub(r'^[一二三四五六七八九十]+、\s*', '', t)
            assembled.append(f'''
<section class="chapter">
  <header class="chapter__head">
    <div class="chapter__num">
      <span class="chapter__num-arabic">{arabic[k]}</span>
      <span class="chapter__num-chi">{chi_num[k] if k < len(chi_num) else ""}</span>
    </div>
    <h2 id="{sid}" class="chapter__title">{t_clean}</h2>
    <div class="chapter__rule"></div>
  </header>
  <div class="chapter__body">
    {body}
  </div>
</section>''')
            k += 1
        else:
            assembled.append(h2_tag + body)
        i += 2
    html_body = "\n".join(assembled)

    # 首段 drop cap
    def mark_first_para(h):
        def repl(m):
            inner = m.group(1)
            inner_new = re.sub(r'<p>', '<p class="drop-cap">', inner, count=1)
            return m.group(0).replace(inner, inner_new)
        return re.sub(
            r'<div class="chapter__body">\s*(.*?)\s*</div>\s*</section>',
            repl, h, flags=re.DOTALL,
        )
    html_body = mark_first_para(html_body)

    word_count = len(re.sub(r'\s+', '', body_md))

    css = CSS_TEMPLATE.replace("{{ACCENT}}", accent)

    page = HTML_TEMPLATE.format(
        title=cover_title,
        author=author,
        word_count=f"{word_count:,}",
        css=css,
        landing_toc_html=landing_toc_html,
        side_toc_html=side_toc_html,
        html_body=html_body,
        js=JS,
    )

    out_path.write_text(page, encoding="utf-8")
    print(f"[OK] 长读网页已生成：{out_path} ({out_path.stat().st_size // 1024} KB, {word_count:,} 字)")


# ============ CSS 模板（Optical Essay）============
CSS_TEMPLATE = r"""
:root {
  --paper: #f4efe4;
  --paper-2: #ece5d4;
  --ink: #121212;
  --ink-soft: #3a3a3a;
  --ink-dim: #8a857a;
  --rule: #cdc4ad;
  --rule-soft: #e0d9c5;
  --accent: {{ACCENT}};
  --ember: #b04824;
  --serif-en: "Fraunces", "Noto Serif SC", Georgia, serif;
  --serif-cn: "Noto Serif SC", "Source Han Serif SC", "Songti SC", serif;
  --mono: "JetBrains Mono", ui-monospace, "SF Mono", Consolas, monospace;
  --w-read: 680px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 80px; }
body {
  margin: 0; background: var(--paper); color: var(--ink);
  font-family: var(--serif-en), var(--serif-cn);
  font-size: 18px; line-height: 1.78;
  font-feature-settings: "kern", "liga", "palt";
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  background-image:
    radial-gradient(circle at 12% 8%, color-mix(in srgb, var(--accent) 8%, transparent) 0%, transparent 28%),
    radial-gradient(circle at 88% 92%, color-mix(in srgb, var(--accent) 10%, transparent) 0%, transparent 32%);
  background-attachment: fixed;
}
body::before {
  content: ""; position: fixed; inset: 0;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.6  0 0 0 0 0.55  0 0 0 0 0.4  0 0 0 0.06 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
  pointer-events: none; z-index: 1; opacity: 0.7; mix-blend-mode: multiply;
}
.progress {
  position: fixed; top: 0; left: 0; height: 3px; width: 0;
  background: linear-gradient(90deg, var(--accent), var(--ember));
  z-index: 200; transition: width 0.1s linear;
}
.topbar {
  position: fixed; top: 0; left: 0; right: 0;
  padding: 18px 40px 14px; display: flex; justify-content: space-between; align-items: baseline;
  font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--ink-soft); z-index: 150;
  mix-blend-mode: multiply;
}
.topbar .brand { color: var(--accent); font-weight: 600; }
.topbar .brand em { font-style: normal; color: var(--ember); padding: 0 4px; }
.topbar .issue { color: var(--ink-dim); }

.hero {
  min-height: 100vh; display: grid; grid-template-columns: 1fr;
  align-content: center; padding: 120px 48px 80px;
  position: relative; overflow: hidden;
}
.hero__eyebrow {
  font-family: var(--mono); font-size: 12px; letter-spacing: 0.28em;
  text-transform: uppercase; color: var(--accent); margin-bottom: 32px;
  opacity: 0; animation: fadeUp 0.8s 0.1s forwards;
}
.hero__eyebrow::before {
  content: ""; display: inline-block; width: 40px; height: 1px;
  background: var(--accent); margin-right: 16px; vertical-align: middle;
}
.hero__title {
  font-family: var(--serif-cn);
  font-size: clamp(44px, 7.6vw, 112px); line-height: 1.02;
  letter-spacing: -0.01em; font-weight: 700;
  margin: 0 0 28px 0; max-width: 1100px;
  opacity: 0; animation: fadeUp 1s 0.3s forwards;
}
.hero__title .highlight { color: var(--accent); font-style: normal; position: relative; }
.hero__subtitle {
  font-family: var(--serif-en); font-style: italic; font-weight: 300;
  font-size: clamp(18px, 2.1vw, 26px); line-height: 1.4;
  color: var(--ink-soft); max-width: 780px; margin: 0 0 48px 0;
  opacity: 0; animation: fadeUp 1s 0.6s forwards;
}
.hero__meta {
  display: flex; flex-wrap: wrap; gap: 16px 40px;
  font-family: var(--mono); font-size: 12px; letter-spacing: 0.1em;
  color: var(--ink-dim); padding-top: 24px;
  border-top: 1px solid var(--rule); max-width: 780px;
  opacity: 0; animation: fadeUp 1s 0.9s forwards;
}
.hero__meta div strong {
  display: block; color: var(--ink);
  font-family: var(--serif-en); font-size: 15px;
  font-weight: 500; letter-spacing: 0; margin-top: 4px;
}
.hero__lens {
  position: absolute; right: -12vw; top: 18vh;
  width: 64vw; height: 64vw; max-width: 820px; max-height: 820px;
  border: 1px solid color-mix(in srgb, var(--accent) 30%, transparent);
  border-radius: 50%; pointer-events: none;
}
.hero__lens::before, .hero__lens::after {
  content: ""; position: absolute; inset: 12%;
  border-radius: 50%; border: 1px solid color-mix(in srgb, var(--accent) 20%, transparent);
}
.hero__lens::after { inset: 28%; border-color: rgba(176, 72, 36, 0.15); }
.hero__lens-label {
  position: absolute; bottom: -14px; left: 50%; transform: translateX(-50%);
  font-family: var(--mono); font-size: 10px; letter-spacing: 0.24em;
  background: var(--paper); padding: 0 12px; color: var(--ink-dim); text-transform: uppercase;
}
.hero__scroll {
  position: absolute; bottom: 40px; left: 50%; transform: translateX(-50%);
  font-family: var(--mono); font-size: 10px; letter-spacing: 0.3em;
  color: var(--ink-dim); text-transform: uppercase;
  animation: bounce 2.4s infinite ease-in-out;
}
.hero__scroll::after {
  content: ""; display: block; width: 1px; height: 36px;
  background: var(--ink-dim); margin: 12px auto 0;
}
@keyframes fadeUp { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: none; } }
@keyframes bounce { 0%,100% { transform: translate(-50%,0); opacity: 0.7; } 50% { transform: translate(-50%, 8px); opacity: 1; } }

.toc-block {
  max-width: 1180px; margin: 120px auto; padding: 0 48px;
  scroll-margin-top: 80px;
}
.toc-block__head {
  max-width: 760px; margin-bottom: 40px;
}
.toc-block__head h3 {
  font-family: var(--mono); font-size: 11px; letter-spacing: 0.32em;
  text-transform: uppercase; color: var(--accent); margin: 0 0 12px; font-weight: 600;
}
.toc-block__head h4 {
  font-family: var(--serif-cn); font-size: 32px; line-height: 1.25;
  font-weight: 700; margin: 0 0 20px; color: var(--ink);
}
.toc-block__head p {
  font-family: var(--serif-en); font-style: italic; font-size: 16px;
  line-height: 1.7; color: var(--ink-soft);
}
.landing-toc {
  list-style: none; padding: 0; margin: 0;
  border-top: 1px solid var(--accent);
}
.landing-toc__row { border-bottom: 1px dotted var(--rule); }
.landing-toc__row a {
  display: grid;
  grid-template-columns: 110px 1.05fr 1.5fr;
  gap: 32px; padding: 22px 12px 22px 0;
  text-decoration: none; color: var(--ink);
  border-left: 3px solid transparent;
  transition: border-left-color 0.2s ease, background 0.2s ease, padding 0.2s ease;
  align-items: baseline;
}
.landing-toc__row a:hover {
  border-left-color: var(--accent);
  background: color-mix(in srgb, var(--accent) 6%, transparent);
  padding-left: 16px;
}
.landing-toc__num { padding-left: 8px; line-height: 1; }
.landing-toc__n {
  font-family: var(--serif-en); font-style: italic; font-weight: 300;
  font-size: 48px; color: var(--accent); display: block; line-height: 0.95;
  font-variation-settings: "SOFT" 80, "opsz" 144;
}
.landing-toc__code {
  display: block; font-family: var(--mono); font-size: 10px;
  letter-spacing: 0.22em; text-transform: uppercase;
  color: var(--ink-dim); margin-top: 8px;
}
.landing-toc__title {
  font-family: var(--serif-cn); font-size: 20px; font-weight: 600;
  line-height: 1.3; color: var(--ink); margin-bottom: 4px;
}
.landing-toc__sub {
  font-family: var(--serif-en); font-style: italic; font-size: 14px;
  color: var(--ink-soft); line-height: 1.45;
}
.landing-toc__blurb {
  font-family: var(--serif-cn); font-size: 14.5px; line-height: 1.65;
  color: var(--ink-soft); border-left: 1px dotted var(--rule); padding-left: 22px;
}
.landing-toc__row a:hover .landing-toc__blurb {
  color: var(--ink); border-left-color: var(--accent);
}

.back-to-toc {
  position: fixed; right: 24px; bottom: 32px; z-index: 90;
  display: inline-flex; align-items: center; gap: 8px;
  padding: 12px 18px; border-radius: 999px;
  background: color-mix(in srgb, var(--paper) 95%, transparent);
  backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  border: 1px solid var(--accent); color: var(--accent);
  font-family: var(--mono); font-size: 11px; letter-spacing: 0.22em;
  text-transform: uppercase; text-decoration: none; line-height: 1;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  transition: background 0.2s ease, color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
}
.back-to-toc__arrow {
  font-family: var(--serif-en); font-style: italic; font-size: 14px; line-height: 1;
}
.back-to-toc:hover {
  background: var(--accent); color: var(--paper);
  box-shadow: 0 8px 24px rgba(0,0,0,0.18);
  transform: translateY(-2px);
}
@media (max-width: 900px) {
  .back-to-toc { right: 14px; bottom: 16px; padding: 10px 14px; font-size: 10px; letter-spacing: 0.18em; }
  .back-to-toc__arrow { font-size: 13px; }
  .landing-toc__row a { grid-template-columns: 60px 1fr; gap: 14px; padding: 18px 8px; }
  .landing-toc__n { font-size: 30px; }
  .landing-toc__code { font-size: 9px; letter-spacing: 0.16em; }
  .landing-toc__blurb {
    grid-column: 1 / -1; border-left: none; padding-left: 0;
    border-top: 1px dotted var(--rule); padding-top: 12px; margin-top: 4px;
  }
  .toc-block { padding: 0 24px; }
}

.chapter { position: relative; padding: 100px 48px 40px; scroll-margin-top: 80px; }
.chapter__head {
  max-width: 1100px; margin: 0 auto 64px;
  display: grid; grid-template-columns: 180px 1fr; gap: 48px;
  align-items: baseline;
}
.chapter__num { line-height: 1; }
.chapter__num-arabic {
  display: block; font-family: var(--serif-en); font-style: italic; font-weight: 300;
  font-size: clamp(80px, 10vw, 140px); color: var(--accent);
  line-height: 0.85; letter-spacing: -0.04em;
  font-variation-settings: "SOFT" 80, "opsz" 144;
}
.chapter__num-chi {
  display: block; font-family: var(--serif-cn); font-size: 16px;
  letter-spacing: 0.4em; color: var(--ember); margin-top: 12px;
}
.chapter__title {
  font-family: var(--serif-cn); font-size: clamp(28px, 3.8vw, 48px);
  font-weight: 700; line-height: 1.15; margin: 0; color: var(--ink);
  letter-spacing: -0.005em;
}
.chapter__rule { grid-column: 1 / -1; height: 1px; background: var(--rule); margin-top: 32px; }
.chapter__body { max-width: var(--w-read); margin: 0 auto; padding: 0 8px; }

.chapter__body p { margin: 1.5em 0; text-align: justify; hanging-punctuation: first last; hyphens: auto; }
.chapter__body p.drop-cap::first-letter {
  font-family: var(--serif-en); font-style: italic; font-weight: 400;
  float: left; font-size: 5em; line-height: 0.9;
  padding: 0.08em 0.12em 0 0; color: var(--accent);
  font-variation-settings: "SOFT" 100, "opsz" 144;
}
.chapter__body h3 {
  font-family: var(--serif-cn); font-size: 26px; font-weight: 700;
  line-height: 1.3; margin: 3em 0 0.8em; color: var(--ink);
  position: relative; padding-left: 24px;
}
.chapter__body h3::before {
  content: ""; position: absolute; left: 0; top: 0.48em;
  width: 12px; height: 2px; background: var(--ember);
}
.chapter__body h4 {
  font-family: var(--serif-cn); font-size: 20px; font-weight: 600;
  line-height: 1.35; margin: 2.2em 0 0.6em; color: var(--accent);
}
.chapter__body strong {
  font-weight: 700; color: var(--ink);
  background: linear-gradient(to top, color-mix(in srgb, var(--accent) 20%, transparent) 0%, color-mix(in srgb, var(--accent) 20%, transparent) 38%, transparent 38%);
  padding: 0 2px;
}
.chapter__body em { font-style: italic; color: var(--accent); }
.chapter__body blockquote {
  margin: 2em 0; padding: 24px 28px 24px 32px;
  border-left: 2px solid var(--ember);
  background: rgba(176, 72, 36, 0.05);
  font-family: var(--serif-en); font-style: italic;
  font-size: 0.96em; color: var(--ink-soft);
}
.chapter__body blockquote p { margin: 0; }
.chapter__body ul, .chapter__body ol { margin: 1.4em 0; padding-left: 1.6em; }
.chapter__body li { margin: 0.5em 0; }
.chapter__body ul li::marker { color: var(--ember); }
.chapter__body code {
  font-family: var(--mono); font-size: 0.85em;
  background: var(--paper-2); padding: 2px 6px; border-radius: 3px; color: var(--accent);
}
.chapter__body hr {
  border: none; height: 1px; background: var(--rule);
  margin: 3.6em auto; width: 40%; position: relative;
}
.chapter__body hr::after {
  content: "\25C6"; position: absolute; top: -10px; left: 50%; transform: translateX(-50%);
  background: var(--paper); padding: 0 12px; font-size: 12px; color: var(--ember);
}
.chapter__body a {
  color: var(--accent); text-decoration: underline;
  text-underline-offset: 3px; text-decoration-thickness: 1px;
}
.chapter__body table {
  width: 100%; border-collapse: collapse;
  margin: 2.4em 0; font-family: var(--serif-cn);
  font-size: 14px; line-height: 1.55;
}
.chapter__body table thead tr { border-top: 2px solid var(--ink); border-bottom: 1px solid var(--ink); }
.chapter__body table tbody tr { border-bottom: 1px solid var(--rule); }
.chapter__body table th, .chapter__body table td { padding: 12px 10px; text-align: left; vertical-align: top; }
.chapter__body table th {
  font-family: var(--mono); font-size: 11px;
  letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--ink-soft); font-weight: 600;
}

.side-toc {
  position: fixed; right: 24px; top: 50%; transform: translateY(-50%);
  z-index: 50; max-width: 200px;
}
.side-toc ol { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 2px; }
.side-toc a {
  display: flex; align-items: center;
  font-family: var(--mono); font-size: 10px; letter-spacing: 0.08em;
  color: var(--ink-dim); text-decoration: none;
  padding: 6px 4px; border-right: 2px solid transparent;
  text-align: right; justify-content: flex-end; transition: all 0.2s;
}
.side-toc a:hover, .side-toc a.active {
  color: var(--accent); border-right-color: var(--ember);
}
.side-toc a.active { font-weight: 600; }
.side-toc .side-toc__num { color: var(--ember); margin-left: 10px; font-weight: 600; }
@media (max-width: 1280px) { .side-toc { display: none; } }

.colophon {
  max-width: 1100px; margin: 120px auto 80px;
  padding: 60px 48px; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule);
  display: grid; grid-template-columns: 1fr 2fr; gap: 64px;
  font-size: 13px; color: var(--ink-soft); font-family: var(--serif-cn);
}
.colophon h4 {
  font-family: var(--mono); font-size: 10px; letter-spacing: 0.28em;
  color: var(--accent); text-transform: uppercase; margin: 0 0 10px;
}
.colophon p { margin: 0 0 8px; line-height: 1.6; }
.colophon .method { border-left: 2px solid var(--ember); padding-left: 18px; }

@media (max-width: 900px) {
  body { font-size: 17px; }
  .topbar { padding: 14px 20px 10px; font-size: 10px; }
  .hero { padding: 100px 24px 60px; }
  .hero__lens { display: none; }
  .chapter { padding: 60px 24px 20px; }
  .chapter__head { grid-template-columns: 1fr; gap: 16px; }
  .chapter__num-arabic { font-size: 68px; }
  .toc-block { grid-template-columns: 1fr; gap: 40px; padding: 0 24px; }
  .colophon { grid-template-columns: 1fr; gap: 32px; padding: 40px 24px; }
}
.reveal { opacity: 0; transform: translateY(24px); transition: opacity 0.9s cubic-bezier(.2,.6,.2,1), transform 0.9s cubic-bezier(.2,.6,.2,1); }
.reveal.in { opacity: 1; transform: none; }
::selection { background: var(--accent); color: var(--paper); }
"""

JS = r"""
const progress = document.getElementById('progress');
function updateProgress() {
  const h = document.documentElement;
  const max = h.scrollHeight - h.clientHeight;
  progress.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
}
window.addEventListener('scroll', updateProgress, { passive: true });
updateProgress();
const ioReveal = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); ioReveal.unobserve(e.target); } });
}, { threshold: 0.08, rootMargin: '0px 0px -60px 0px' });
document.querySelectorAll('.chapter, .toc-block, .colophon').forEach(el => {
  const rect = el.getBoundingClientRect();
  if (rect.top < window.innerHeight && rect.bottom > 0) return;
  if (rect.bottom <= 0) return;
  el.classList.add('reveal'); ioReveal.observe(el);
});
const tocLinks = document.querySelectorAll('.side-toc a');
const chapters = Array.from(document.querySelectorAll('.chapter'));
function updateActiveToc() {
  const y = window.scrollY + window.innerHeight * 0.35;
  let active = null;
  for (const ch of chapters) { if (ch.offsetTop <= y) active = ch; }
  tocLinks.forEach(a => a.classList.remove('active'));
  if (active) {
    const id = active.querySelector('h2')?.id;
    const link = Array.from(tocLinks).find(a => a.dataset.target === id);
    if (link) link.classList.add('active');
  }
}
window.addEventListener('scroll', updateActiveToc, { passive: true });
updateActiveToc();
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · 横纵分析法深度研究</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..900,0..100;1,9..144,300..900,0..100&family=JetBrains+Mono:wght@400;600&family=Noto+Serif+SC:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>

<div class="progress" id="progress"></div>

<header class="topbar">
  <div class="brand">HV·Analysis<em>/</em>Optical Essay</div>
  <div class="issue">横纵分析法深度研究</div>
</header>

<section class="hero">
  <div class="hero__lens" aria-hidden="true"><span class="hero__lens-label">Deep Research</span></div>
  <p class="hero__eyebrow">横纵分析法深度研究</p>
  <h1 class="hero__title">{title}</h1>
  <p class="hero__subtitle">纵向追时间深度，横向追同期广度，最终交汇出判断。</p>
  <div class="hero__meta">
    <div>LENGTH<strong>{word_count} 字</strong></div>
    <div>METHOD<strong>横纵分析法</strong></div>
    <div>BY<strong>{author}</strong></div>
  </div>
  <div class="hero__scroll">SCROLL</div>
</section>

<section class="toc-block" id="contents">
  <div class="toc-block__head">
    <h3>Table of Contents</h3>
    <h4>本篇目录</h4>
    <p>每章一行：编号 / 章节代号 · 标题 + 副标题 · 一两句梗概。点任一行跳到对应章节；任意位置可用右下角"返回目录"浮动按钮回到这里。</p>
  </div>
  <ol class="landing-toc">{landing_toc_html}</ol>
</section>

<main>{html_body}</main>

<section class="colophon">
  <div>
    <h4>Colophon</h4>
    <p>本页为横纵分析法深度研究 · 长读网页版。</p>
    <p style="margin-top:12px;">正文字体：Fraunces + 思源宋体<br>标题字体：Fraunces Italic SOFT<br>元信息字体：JetBrains Mono</p>
  </div>
  <div class="method">
    <h4>Methodology</h4>
    <p>横纵分析法：纵向追研究对象从诞生到当下的演进，横向以当下为切面做竞争/同类对比，最后交汇两条线给出综合判断。</p>
    <p style="margin-top:12px; font-family:var(--mono); font-size:11px; letter-spacing:0.08em; color: var(--ink-dim);">— End of Report —</p>
  </div>
</section>

<nav class="side-toc" aria-label="章节导航"><ol>{side_toc_html}</ol></nav>

<a class="back-to-toc" href="#contents" aria-label="返回目录">
  <span class="back-to-toc__arrow">↑</span>
  <span class="back-to-toc__label">返回目录</span>
</a>

<script>{js}</script>

</body>
</html>
"""


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Markdown 源文件路径")
    ap.add_argument("output", help="HTML 输出路径")
    ap.add_argument("--title", required=True, help="研究对象名称（用于 title/封面）")
    ap.add_argument("--author", default="数字生命卡兹克", help="作者（默认：数字生命卡兹克）")
    ap.add_argument("--accent", default="#1a3a7c", help="主色 hex（默认深宝石蓝 #1a3a7c，可换 #2f6b4a 绿 / #8a2a44 酒红 / #7d3c98 紫 / #b04824 锈橙）")
    args = ap.parse_args()
    build(Path(args.input), Path(args.output), args.title, args.author, args.accent)
