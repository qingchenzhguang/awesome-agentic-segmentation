# Research notes

Working notes for the first version of **Awesome Agentic Segmentation**. Date of the verification
pass: **2026-11-05**. Everything below records what was read, what was decided, and what is still
unknown. Nothing here was produced by running a listed project.

## 1. What this version contains

- 33 entries: 13 Agent/applications, 2 harnesses, 10 tools/integrations, 1 benchmark, 3 examples,
  4 papers.
- 5 benchmarks that live inside listed projects, cross-linked rather than duplicated as entries.
- 9 related resources that are deliberately outside the curation boundary (model layers, adjacent
  agent directions, non-segmentation benchmarks).
- Coverage by tag: natural images 10, medical 13, remote sensing 4, microscopy 6, video 2
  (an entry can carry two domain tags); 12 entries are 3D and 2 are video. Industrial inspection
  has no verified entry and is not represented by a placeholder.
- Method: read-only. Each project's own README was read; where the entry claims a specific loop,
  tool name or evaluation behaviour, a source file, benchmark directory or paper was read as well.
  No repository was cloned, no package installed, no pipeline executed, and no weights or datasets
  downloaded. `data/resources.json` records a `verification` field per entry (`docs only` or
  `docs+code`) and the evidence URLs that were actually opened.

## 2. What was learned from the existing lists

Seven lists were read on 2026-11-05 for structure, entry format and inclusion boundaries. They do
**not** share a standard; the differences are real and worth recording rather than flattening into
"best practice". Star counts below are what the repositories displayed when read that day; they are
context, not a quality claim, and this list uses no star threshold.

| List | Structure it actually uses | Entry style | Boundary lesson taken |
| --- | --- | --- | --- |
| [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) (~30.8k) | Two H1 sections: open-source projects, closed-source projects; 215 entries flat, categorised by free text | `## [name](url)` + `<details>` with Category / Description / Links | Folding keeps a long page browsable; free-text categories drift (108 distinct values for 215 items), so this list uses a fixed tag vocabulary instead. |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) (~143.9k) | 16 emoji sections over its own template directories | One line per template, linking inside the repo | It is a self-built example library, not a third-party index. Its "hand-built / tested end-to-end" claims apply because the code lives in that repo; they must **not** be copied onto third-party projects, and this list makes no such promise. |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) (~97.3k) | Ten top-level sections, ~60 emoji categories under server implementations | One line, emoji legend for language/scope/OS, third-party score badge | A legend turns tags into a controlled vocabulary at low maintenance cost; per-entry third-party score badges mix "listed" with "rated", which this list avoids. |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (~36.8k) | Sections by vendor, then by language, then community topics | One line per skill; vendor sections folded | Its "curated, not audited" notice and quality criteria are a good model for expectation management; a stated 10-word description limit that 1,239 entries violate is a reminder that unenforced rules are not rules. |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) (~57.2k) | 24 mixed sections, some by resource type rather than topic | One line + shields badges for age, last commit, licence, stars | Replace "I like it" with checkable signals, and state that inclusion is not a promise; first-person editorial voice does not survive a change of maintainer. |
| [mrgloom/awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) (~10.8k) | 22 sections: architectures, datasets, benchmarks, metrics, then by domain | Bare links with framework tags, many duplicates, an "older list" graveyard | It shows which sections a segmentation list needs (datasets, metrics, annotation tools, results) and what happens without dates, descriptions and de-duplication. |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome/blob/main/awesome.md) (~530.8k) | Not a list; a set of rules for lists | n/a | "It's a curation, not a collection"; every entry should say why it is here; leave things out rather than pad. The rules cover format and taste, not technical verification — which is the gap this list tries to fill with dates and evidence. |

Consequences adopted here: one canonical entry per project, a fixed tag vocabulary, a mandatory
verification date and evidence link, and no copied marketing language. Consequences rejected:
per-entry score badges, free-text categories, and any claim that a third-party project is "tested"
by this curation.

### Layout reference

On 2026-11-12 the READMEs were re-typeset after reading
[AgenticGraphics/Awesome-Agentic-Graphics](https://github.com/AgenticGraphics/Awesome-Agentic-Graphics)
on the same day. Borrowed: the centred title with a badge row, the quick-nav strip, the hero figure
with a one-line caption, a *Design space* table that defines the labels before any entry, a *Browse*
table that maps roles to sections, one table per section with a leading intro sentence, a *Notes*
line for caveats that do not fit a cell, the "back to contents" links, and a closing *Open questions*
section.

A second pass on 2026-11-13 removed the per-row `Status · verified` column. Per-entry status and
verification dates are useful to a maintainer but are not what a reader scans a curated list for;
the reference carries neither, and printing them in every row made the tables read like an audit
log. Both now live only in `data/resources.json`, with a single *Maintenance* section explaining how
the list is checked and where the record lives; entries where the distinction changes what the row
*is* — deprecated or paper-only — say so in prose. The table columns are therefore `Project · What
it provides · Scope`, with the controlled tags in the last column. The same pass added a *Patterns*
section, which is the closest analogue of the reference's *Key Findings*: five observations that the
entries themselves support, rather than new claims.

Not borrowed: the `awesome.re` badge (this list is not indexed there), an arXiv/Hugging Face badge
(each entry links its own paper), the citation block (there is no paper), and their paper-table
columns `Publication · Paper Title · Code`, which assume one-line items and a publication date that
software entries do not have.

A local `assets/hero.svg` was drawn for this repository rather than reusing the reference figures;
it is a generic plan → call tools → inspect mask → refine loop, not a claim about any listed system.
Badges are static shields.io images with fixed text, not metrics or embedded third-party services;
they must be updated by hand when counts change. Content was not re-verified for either pass, so
every JSON record still carries the 2026-11-05 verification date; only the presentation changed.

### Visibility and the website

On 2026-11-16 the owner decided to make the repository public and publish a one-page site. The
constraint matters: GitHub Pages on a free account only serves public repositories, and a Pages
site is publicly reachable even when the repository is private on a paid plan, so "a private list
with a public web page" was never an option. The site is generated from `data/resources.json` by
`scripts/build_site.py`, written to `index.html` at the repository root, and published from the
`main` branch; it adds no analytics, no custom domain and no embed beyond the static shields badges.
`index.html` is generated — edit the JSON or the builder, then rebuild. No licence was added: the
list is public to read, but reuse rights remain ungranted until the owner chooses one.

## 3. Why each entry is on the list (short evidence)

Agent/applications:

- **VASA** — the README describes planning, mask editing, scrutiny and error recovery around one
  persistent mask, and points at `src/engine/agent_core.py`; the repository also ships recorded
  traces. Included because the mask, not just the answer, is the state.
- **MedSAM-Agent** — `infer/unibiomed_inference_toolusing.py` contains the loop: the model emits
  points, a box, or a stop, and the segmenter returns a new mask each turn. Included as an example
  of a *trained* segmentation agent.
- **MedSegAgent** — four agent stages with coarse-to-fine filtering (`agents/c2f_tree_search.py`);
  `evaluate.py` scores dataset hit rate, not mask quality, which the entry states explicitly.
- **SegAgent** — the delivered artefact is a trajectory model plus released HLMAT data; the
  interactive segmentor is SimpleClick. Included because the model's output *is* a sequence of
  actions.
- **VoxelSage** — a working app with a documented Skills API, segmentation backends and a 3D
  viewer; the README is explicit that it is research software, not a medical device.
- **GenCellAgent** — a tool router over six named segmenters with a plan–execute–evaluate loop and a
  VLM evaluator; the weaker point is that its performance claims are the authors' and were not
  reproduced.
- **ask-to-mask** — the loop is concrete: VLM prompt → generated mask → VLM critique → iterate, with
  orthogonal-plane voting for 3D. The README itself distinguishes the critic's estimate from ground
  truth.
- **FarmSeeker** — ambiguity detection, extra-imagery retrieval, multi-image reasoning and SAM 2.1
  refinement; the dataset release is still pending and the entry says so.
- **Refer-Agent** — reasoning and reflection agents before SAM 2 propagation; reviewable code and a
  CVPR 2026 paper.
- **Agentic-SAM** — LangGraph tool orchestration around three segmenters, including frame-by-frame
  tracking and live model commentary; a local prototype with a demo video.
- **MMedAgent** — a trained tool-selection agent whose tool table includes two segmentation
  configurations; segmentation is one family among several, which the entry states.
- **Change-Agent** — included with a caveat: the LLM routes queries to a change-interpretation model
  but does not inspect masks and retry, so it fits the agentic criterion more weakly.
- **LORE** — the policy chooses the correction type and the stop point from mask/error state; code
  released, weights and data not, hence `Early`.

Harnesses:

- **VisionAgent** — plan → generate code → test → iterate is documented, and
  `vision_agent/tools/__init__.py` really exposes SAM 2-based segmentation and tracking tools. The
  GitHub repository description now calls the project deprecated, so it is in the list as a
  documented harness with `Deprecated` status, not as a recommendation.
- **agentic-segmentation (coding-agent harness)** — exposes `seg_*` tools, versioned presets,
  per-run traces, evaluation splits and an experiment log; the author frames it as an investigation.

Tools/integrations: **SAM 3** ships an actual agent package (`sam3/agent/agent_core.py` with
`segment_phrase`, `examine_each_mask`, `select_masks`, `report_no_mask`, `zoom_in`, bounded
generations and message pruning). **nnInteractive Agent** is an MCP server plus a workflow skill
with an explicit tool table and a benchmark. **SAM 3 Segmentation Skill** and **ComfyUI Segmentation
Agent** both implement reversible review loops over SAM 3. **Grounded SAM 2** is a fixed pipeline and
is listed as such. **proofreader-mcp**, **gfm-mcp**, **MCP-Slicer**, **BioImage-Agent** and **MedMCP**
are integrations whose host tool does the judgment.

Evaluation: **BIABench** is the only independent benchmark that measures segmentation-adjacent agent
work with both outcome and process scores. The other five benchmark artefacts belong to listed
projects and are cross-linked.

Papers: **RSAgent** and **VoxelPrompt** had no public repository when checked; **RSure-Agent** has a
repository whose release checklist still lists the core code as unreleased; **SEER** releases code
and weights but performs single-pass specification rather than tool iteration.

## 4. Rejected or deferred candidates

Rejected for being the wrong "segmentation" (customer/market segmentation or text chunking):
`ak-1344/Aster` (ASTER, "Agentic Segmentation Through Execution & Reasoning" — retail-bank customer
segmentation), `PASUPULASAITEJA/Customer-Segmentation-Agent`,
`prajaktasawant-30/segmentation-agent`, `Zukhruf-Riaz/Segmentation_Agent`,
`imohuan/novel-segmentation-mcp` (novel/fiction segmentation), `illumio-mcp-skills`
(network segmentation).

Rejected for having no agent loop despite a relevant name or topic:

- `ermongroup/TEOChat` — a temporal earth-observation VLM; the README contains no segmentation
  claim at all.
- `JIA-Lab-research/Seg-Zero`, `JIA-Lab-research/VisionReasoner` — reasoning model plus a separate
  mask decoder in a fixed pipeline; no tool feedback loop. Kept as a related link for Seg-Zero.
- `MIC-DKFZ/agent-sam` — a SAM wrapper for MITK; no decision or feedback layer found.
- `facebookresearch/segment-anything`, `facebookresearch/sam2`, `bowang-lab/MedSAM2`,
  `MIC-DKFZ/nnInteractive` — model backends, linked from Related Resources instead of being curated
  as agents.
- `HanboBizl/AgMTR`, `Chuyun-Shen/Interactive-Medical-Image-Segmentation-with-MARL`,
  `amiralansary/rl-medical` — RL policies or segmentation networks, not tool-using agents.
- `SakashSrivastava/Agentic-Research-Assistant-for-Segmentation-Literature` — RAG over papers; it
  does not perform segmentation.

Deferred rather than rejected (worth another pass):

- `landing-ai/vision-agent-mcp` — repository description says it is deprecated in favour of Agentic
  Document Extraction; the underlying VisionAgent is already listed with `Deprecated` status.
- `AIRS101/RSure-Agent` — code release explicitly pending; listed as `Paper only` for now.
- `IntelliSensing/HiRS-Agent` — README marks code as "Coming Soon"; not verified.
- `Ztrura/SEER` — released and listed, but whether its "skill evolution" is agentic in the tool-loop
  sense is a judgement call recorded in the entry.
- `jasongief/TGS-Agent` — the README could not be read reliably in this environment (empty content
  from the API), so nothing was claimed about it.
- `UniVA-Bench` (Hugging Face dataset) — an `agenticseg` task was reported in search results but the
  task count and protocol were not verified.
- `iizcm/segment-anything-skill` — a thin, spec-like skill; depth of instructions not verified.
- `mbzuai-oryx/ThinkGeo` — a real benchmark, but it scores tool use and answer accuracy, not
  segmentation quality, so it is a related link.
- `ICLR-2027-submission/MISEG-AGENT` — the organisation name alone makes provenance doubtful; no
  claim was made.
- `skulitom/Maskbolt`, `landmarklabs/vision-agent` — README not retrievable from `main` or `master`
  at the time of checking; may have moved or been deleted. A failed fetch is not a 404 judgement, so
  these are deferred rather than called dead.

## 5. Open questions and verification gaps

1. **Star counts and last-commit dates** were read from the GitHub API on 2026-11-05
   (`stargazers_count`, `pushed_at`). They are recorded in the entry notes only where useful and are
   never used as a selection criterion. They change daily.
2. **Licences were not verified uniformly.** Where the README states a licence that conflicts with
   the repository metadata, the entry says so (SegAgent: README says BSD-2-Clause for academic use,
   GitHub reports MIT). SAM 3 and VASA report NOASSERTION because of custom or mixed terms. The
   absence of a licence claim in an entry is deliberate, not an omission.
3. **"Runs" was never verified.** No project was installed or executed, so nothing here is labelled
   as run-verified. Statements like "works on a Mac" or Dice numbers are attributed to the authors.
4. **Medical safety.** Several entries are research software with explicit "not a medical device"
   or "not for clinical use" notices (VoxelSage, MedMCP); these are kept in the entries rather than
   flattened away.
5. **The industrial-inspection domain is missing.** Searches returned anomaly-detection and
   industrial-inspection models, but no agentic segmentation system with an inspectable tool loop
   was verified. The section is omitted rather than filled.
6. **Chinese and English READMEs are hand-mirrored.** They currently list the same 33 projects in the
   same order; the JSON file is the machine-readable record. If they diverge later, the JSON is the
   source of truth.
7. **GitHub HTML pages were not reliably reachable** from this environment; repository pages, README
   files and metadata were read through the GitHub API and raw content, which is why some statements
   about page-level badges and archive banners are marked unknown.

## 6. Follow-up queue

- Re-check the deferred repositories above for code release (RSure-Agent, HiRS-Agent, TGS-Agent) and
  re-title them from `Paper only` if code appears.
- Look for independent evaluation of agentic segmentation beyond BIABench: a benchmark that scores
  mask quality, tool choice and recovery separately would be a better anchor than any single project
  benchmark.
- Search specifically for industrial and 3D-perception agent systems, and for harness work coming
  from the coding-agent side (trace formats, budget accounting, permissioned Python tools).
- Verify whether any of the listed agent skills (nnInteractive Agent, SAM 3 Segmentation Skill,
  ComfyUI node) has an independent third-party evaluation; currently their evidence is author-run.
- Replace `docs only` with `docs+code` for entries where the loop claim still rests on the README
  alone (VASA, SegAgent, GenCellAgent, FarmSeeker, Refer-Agent, MedMCP, gfm-mcp, proofreader-mcp).
