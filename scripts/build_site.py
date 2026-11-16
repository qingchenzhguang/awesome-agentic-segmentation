#!/usr/bin/env python3
"""Build the static one-page site from data/resources.json.

Standard library only. Writes index.html at the repository root, which is what
GitHub Pages serves for a project site. Run from the repository root:

    python scripts/build_site.py

The prose below is site-only copy; the entry data comes from the JSON record so
the page stays in sync with the READMEs.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SECTIONS = [
    (
        "agents",
        "Agents & Applications",
        "Complete systems that decide what to do next, call a segmenter or an editor, look at the result and continue.",
        "Agents & Applications",
    ),
    (
        "harnesses",
        "Harnesses & Frameworks",
        "Reusable execution machinery: planning, code generation and tests, presets, traces, budgets, retries and evaluation splits.",
        "Harnesses & Frameworks",
    ),
    (
        "tools",
        "Tools & Integrations",
        "Backends, MCP servers, skills, plugins and fixed pipelines an agent can call. The host and the backend are the point.",
        "Tools & Integrations",
    ),
    (
        "evaluation",
        "Evaluation & Benchmarks",
        "What is measured matters: a script that runs, a model judging its own mask and accuracy against annotation are different things.",
        "Evaluation & Benchmarks",
    ),
    (
        "examples",
        "Examples & Tutorials",
        "Runnable walkthroughs. Each belongs to a project listed above; it is a way in, not a separate project.",
        "Examples & Tutorials",
    ),
    (
        "papers",
        "Papers & Surveys",
        "Research that directly informs segmentation agents. Where a project has a card, its paper is linked there instead.",
        "Papers & Surveys",
    ),
]

PATTERNS = [
    (
        "Two shapes.",
        "Either a trained model that emits prompts or actions (SegAgent, MedSAM-Agent, MMedAgent, LORE, "
        "RSAgent), or an external coding agent that drives tools through MCP, skills or a node (nnInteractive "
        "Agent, SAM 3 Segmentation Skill, ComfyUI Segmentation Agent, the MCP servers).",
    ),
    (
        "Feedback is mostly visual.",
        "3D renders, slice screenshots, review sheets and VLM critiques are the common loop; a few systems act "
        "on mask geometry or a scalar state instead (MedSAM-Agent's updated mask, LORE's error residuals).",
    ),
    (
        "Medical imaging dominates.",
        "Six of the 13 agent entries and three of the 10 tools are medical; remote sensing and microscopy "
        "contribute distinct patterns — spatio-temporal retrieval and multi-agent tool routing.",
    ),
    (
        "Evaluation is thin.",
        "One independent benchmark (BIABench). Everything else reports author-run numbers, and several "
        "repositories ship no evaluation script at all.",
    ),
    (
        "Industrial inspection is missing.",
        "Searches returned segmentation models and anomaly detectors, but no agent with an inspectable tool "
        "loop, so the section is absent rather than padded.",
    ),
]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def paper_link(entry: dict) -> str:
    for url in entry.get("evidence", []):
        if url != entry["url"] and any(
            host in url for host in ("arxiv.org", "aclanthology.org", "ieeexplore.ieee.org", "doi.org")
        ):
            return url
    return ""


def tags(entry: dict) -> str:
    values = []
    for group in ("domain", "prompt", "dim"):
        values.extend(entry["tags"].get(group, []))
    return "".join(f'<span class="tag">{esc(v)}</span>' for v in values)


def card(entry: dict) -> str:
    link = paper_link(entry)
    paper = f'<a class="paper" href="{esc(link)}">paper</a>' if link else ""
    return f"""      <article class="card" data-text="{esc((entry['name'] + ' ' + entry['description_en'] + ' ' + ' '.join(entry['tags'].get('domain', []))).lower())}">
        <h3><a href="{esc(entry['url'])}">{esc(entry['name'])}</a> {paper}</h3>
        <p>{esc(entry['description_en'])}</p>
        <div class="tags">{tags(entry)}</div>
      </article>
"""


def build() -> str:
    data = json.loads((ROOT / "data" / "resources.json").read_text(encoding="utf-8"))
    entries = data["entries"]
    parts: list[str] = []

    parts.append(
        """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome Agentic Segmentation</title>
<meta name="description" content="A curated list of agents, harnesses, tools and resources for agentic image segmentation.">
<style>
:root{--bg:#ffffff;--fg:#1f2328;--muted:#59636e;--line:#d1d9e0;--card:#f6f8fa;--accent:#0969da;--accent2:#8250df}
@media (prefers-color-scheme: dark){:root{--bg:#0d1117;--fg:#e6edf3;--muted:#9198a1;--line:#30363d;--card:#161b22;--accent:#4493f8;--accent2:#a371f7}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding:0 24px}
header{padding:56px 0 8px;text-align:center}
h1{margin:0 0 8px;font-size:clamp(32px,5vw,46px);letter-spacing:-.02em}
.lede{margin:0 auto;max-width:720px;color:var(--muted);font-size:18px}
.badges{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:18px 0 0}
.badges img{height:20px}
nav{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;padding:24px 0 8px;font-size:14px}
nav a{color:var(--muted);text-decoration:none}
nav a:hover{color:var(--accent)}
.hero{display:block;width:100%;max-width:1000px;margin:20px auto 8px}
.caption{text-align:center;color:var(--muted);font-size:14px;margin:0 0 8px}
main{padding:24px 0 64px}
section{padding:28px 0;border-top:1px solid var(--line)}
section:first-of-type{border-top:0}
h2{font-size:26px;margin:0 0 6px;letter-spacing:-.01em}
.intro{margin:0 0 20px;color:var(--muted);max-width:820px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px}
.card h3{margin:0 0 6px;font-size:17px}
.card h3 a{color:var(--fg);text-decoration:none}
.card h3 a:hover{color:var(--accent)}
.card .paper{font-size:12px;font-weight:500;color:var(--accent);margin-left:6px;text-decoration:none}
.card p{margin:0 0 12px;font-size:14.5px;color:var(--fg)}
.tags{display:flex;gap:6px;flex-wrap:wrap}
.tag{font:12px/1.6 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;color:var(--muted);background:var(--bg);border:1px solid var(--line);border-radius:999px;padding:1px 8px}
.search{display:flex;gap:10px;align-items:center;margin:8px 0 0}
.search input{flex:1;padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--fg);font-size:15px}
.search input:focus{outline:2px solid var(--accent);outline-offset:1px}
.hint{color:var(--muted);font-size:13px;white-space:nowrap}
ul.plain{padding-left:20px}
ul.plain li{margin:0 0 10px}
ul.plain strong{color:var(--fg)}
footer{border-top:1px solid var(--line);padding:28px 0 48px;color:var(--muted);font-size:14px}
footer a{color:var(--accent)}
.hidden{display:none}
</style>
</head>
<body>
<div class="wrap">
<header>
  <h1>Awesome Agentic Segmentation</h1>
  <p class="lede">Agents that plan segmentation, call vision tools, inspect masks, and refine. Plus the harnesses, integrations, benchmarks and papers around them.</p>
  <p class="badges">
    <img src="https://img.shields.io/badge/entries-33-0969da" alt="33 entries">
    <img src="https://img.shields.io/badge/domains-5-1a7f37" alt="5 imaging domains">
    <img src="https://img.shields.io/badge/licence-not%20chosen-bf8700" alt="No licence chosen">
  </p>
  <nav>
    <a href="#overview">Overview</a>
    <a href="#agents">Agents</a>
    <a href="#harnesses">Harnesses</a>
    <a href="#tools">Tools</a>
    <a href="#evaluation">Evaluation</a>
    <a href="#examples">Examples</a>
    <a href="#papers">Papers</a>
    <a href="#related">Related</a>
    <a href="#patterns">Patterns</a>
    <a href="#maintenance">Maintenance</a>
    <a href="https://github.com/qingchenzhguang/awesome-agentic-segmentation">GitHub</a>
    <a href="https://github.com/qingchenzhguang/awesome-agentic-segmentation/blob/main/README.zh-CN.md">中文</a>
  </nav>
</header>
<img class="hero" src="assets/hero.svg" alt="Agent loop: plan, call tools, inspect mask, refine">
<p class="caption">Agents plan a segmentation task, call vision tools, inspect the returned mask and feed what they see into the next step.</p>
<main>
"""
    )

    parts.append(
        """<section id="overview">
<h2>Overview</h2>
<p class="intro">A curated list of agents, harnesses, tools and resources for <strong>agentic image segmentation</strong>: systems that plan segmentation tasks, use vision tools, inspect masks and refine results, plus the integrations, benchmarks and workflows around them.</p>
<p class="intro">A project is in scope when all three hold: an agent <strong>decides</strong> something (which tool, which prompt, whether to stop), it <strong>calls</strong> a segmentation tool whose artifact it receives, and that artifact <strong>feeds back</strong> into the next action. A name containing &ldquo;agent&rdquo; is not evidence of agency.</p>
<p class="intro">This is not a catalogue of segmentation models, datasets or papers. Model backends appear only where an agent can call them; plain models are linked from <a href="#related">Related</a>.</p>
<div class="search"><input id="q" type="search" placeholder="Filter by name, description or domain…" aria-label="Filter entries"><span class="hint" id="count"></span></div>
</section>
"""
    )

    for anchor, title, intro, category in SECTIONS:
        rows = [entry for entry in entries if entry["category"] == category]
        parts.append(f'<section id="{anchor}">\n<h2>{esc(title)}</h2>\n<p class="intro">{esc(intro)}</p>\n<div class="grid">\n')
        for entry in rows:
            parts.append(card(entry))
        parts.append("</div>\n")
        if anchor == "evaluation":
            parts.append(
                '<p class="intro" style="margin-top:24px">Benchmarks released inside listed projects:</p>\n<ul class="plain">\n'
            )
            for bench in data.get("embedded_benchmarks", []):
                parts.append(
                    f'<li><a href="{esc(bench["url"])}">{esc(bench["name"])}</a> — {esc(bench["measures"])} '
                    f'<span class="tag">{esc(bench["host_entry"])}</span></li>\n'
                )
            parts.append("</ul>\n")
        parts.append("</section>\n")

    parts.append('<section id="related">\n<h2>Related Resources</h2>\n<p class="intro">Useful, but outside the curation boundary.</p>\n<ul class="plain">\n')
    for item in data.get("related", []):
        parts.append(f'<li><a href="{esc(item["url"])}">{esc(item["name"])}</a> — {esc(item["why_en"])}</li>\n')
    parts.append("</ul>\n</section>\n")

    parts.append('<section id="patterns">\n<h2>Patterns</h2>\n<p class="intro">Five things the entries have in common — and where they do not.</p>\n<ul class="plain">\n')
    for lead, text in PATTERNS:
        parts.append(f"<li><strong>{esc(lead)}</strong> {esc(text)}</li>\n")
    parts.append("</ul>\n</section>\n")

    parts.append(
        """<section id="maintenance">
<h2>Maintenance</h2>
<p class="intro">The list is kept by reading, not by running. For each candidate: discover through GitHub and the linked awesome lists; read the project's own README and, where the entry claims a loop, the source files that implement it; then record the entry in <a href="https://github.com/qingchenzhguang/awesome-agentic-segmentation/blob/main/data/resources.json">data/resources.json</a>. Nothing is cloned, installed or executed.</p>
<p class="intro">Status and the last-checked date live in that JSON record rather than on every card, so the page stays readable; deprecated or paper-only entries say so in their description. The current snapshot was last checked on <strong>2026-11-05</strong>.</p>
</section>
"""
    )

    parts.append(
        """</main>
<footer>
<div class="wrap">
<p><strong>No licence has been chosen for this list.</strong> Every linked project keeps its own licence, which the reader must check before use. No third-party README, image, dataset or code is copied here. Nothing here is medical, safety or security advice.</p>
<p>Source: <a href="https://github.com/qingchenzhguang/awesome-agentic-segmentation">github.com/qingchenzhguang/awesome-agentic-segmentation</a> · data in <a href="https://github.com/qingchenzhguang/awesome-agentic-segmentation/blob/main/data/resources.json">data/resources.json</a></p>
</div>
</footer>
</div>
<script>
(function(){
  var input = document.getElementById('q');
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card'));
  var count = document.getElementById('count');
  function update(){
    var q = (input.value || '').trim().toLowerCase();
    var shown = 0;
    cards.forEach(function(card){
      var hit = !q || (card.getAttribute('data-text') || '').indexOf(q) !== -1;
      card.classList.toggle('hidden', !hit);
      if (hit) shown++;
    });
    count.textContent = shown + ' / ' + cards.length;
  }
  input.addEventListener('input', update);
  update();
})();
</script>
</body>
</html>
"""
    )
    return "".join(parts)


if __name__ == "__main__":
    output = ROOT / "index.html"
    output.write_text(build(), encoding="utf-8")
    print(f"wrote {output} ({output.stat().st_size} bytes)")
