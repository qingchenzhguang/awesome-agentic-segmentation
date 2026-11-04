# Awesome Agentic Segmentation

> A curated list of agents, harnesses, tools, and resources for agentic image segmentation.
>
> Explore systems that plan segmentation tasks, use vision tools, inspect masks, and refine results. Find reusable harnesses, agent integrations, evaluation resources, and practical workflows across imaging domains.

**中文版：[README.zh-CN.md](README.zh-CN.md)**

This list is about systems that **do** segmentation work with some autonomy: they decide which tool
to call, inspect the mask that comes back, and act on what they see. A repository is not included
because its name contains "agent"; it is included because its documentation or code shows a
decision, a tool call, and a feedback path — or because it exists to run such a system.

It is deliberately **not** a catalogue of segmentation models, datasets, or papers. Model backends
appear here only when an agent can call them, and plain models are linked from
[Related Resources](#related-resources) instead. The list is broad across domains rather than deep
in one: natural images, medical imaging, remote sensing and microscopy are represented; industrial
inspection is a target domain that has no verified entry yet, and no placeholder is shipped for it.

**Status of this repository:** private, first version, no open-source licence. Every entry below was
checked by reading the project's own documentation and, where marked, its source files on
**2026-11-05**. Nothing was cloned, installed, or run, and no model weights were downloaded. Author
claims are reported as claims, not as results verified here. See
[docs/research-notes.md](docs/research-notes.md) for how entries were selected, what was rejected,
and what remains unverified.

## Contents

- [Start Here](#start-here)
- [Agents & Applications](#agents--applications)
- [Harnesses & Frameworks](#harnesses--frameworks)
- [Tools & Integrations](#tools--integrations)
- [Evaluation & Benchmarks](#evaluation--benchmarks)
- [Examples & Tutorials](#examples--tutorials)
- [Papers & Surveys](#papers--surveys)
- [Related Resources](#related-resources)
- [Contributing](#contributing)
- [License / Usage Notice](#license--usage-notice)

## Legend

Tags are a small controlled vocabulary, not free text. Each entry takes values from these groups; a
few entries legitimately carry two values in a group when the system spans both (for example 2D
slices and 3D volumes).

- **Domain** — `Natural images`, `Medical`, `Remote sensing`, `Microscopy`, `Video`
- **Prompt** — `Text`, `Points`, `Boxes`, `Masks`, `Interactive`, `No prompt`
- **Dimensionality** — `2D`, `3D`, `Video`

Status meanings:

| Status | Meaning |
| --- | --- |
| `Active` | Code and documentation reviewed; the project appears to be developed and usable now. |
| `Maintained` | Usable and documented, but no activity in the months before verification. |
| `Early` | The artifact exists but is explicitly incomplete, a research prototype, or missing released data/weights. |
| `Deprecated` | The owner now points users elsewhere. |
| `Paper only` | We found the paper but no public code, or the code is explicitly unreleased. |
| `Unverified` | Not used in this version; reserved for entries that could not be checked at all. |

"Verified" is the date of the last read-only check. It is not a promise that the project still
works, and it is not a security or clinical review.

## Start Here

The field is young and the vocabulary is unsettled. Three useful entry points:

**1. "Segment this thing I described in words."**
Start with [VASA](https://github.com/Wayne2Wang/VASA), which keeps one working mask and edits it
through planning, scrutiny and error recovery, or with the official
[SAM 3 Agent notebook](https://github.com/facebookresearch/sam3/blob/main/examples/sam3_agent.ipynb),
which shows an MLLM calling SAM 3 tools in a bounded loop. Both need model weights and a VLM
endpoint; neither runs on a laptop CPU.

**2. "Give my coding agent segmentation tools."**
[nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent) is the most complete example
in this list: an MCP server, a workflow skill with a correction playbook, 3D renders as feedback,
and a benchmark of agents annotating 14 volumes. For 2D photos,
[SAM 3 Segmentation Skill](https://github.com/lillyguisnet/sam3-segmentation) packages review
sheets, reversible decisions and COCO export as a skill.

**3. "I want to study or build the harness, not just use one."**
The [agentic-segmentation harness](https://github.com/sameed-khan/agentic-segmentation) documents
versioned presets, per-run traces and evaluation splits for a coding agent driving a 3D segmenter;
[BIABench](https://github.com/BIABench/BIABench) scores both the result and the process across 16
bioimage tasks. Read [Harnesses & Frameworks](#harnesses--frameworks) before
[VisionAgent](https://github.com/landing-ai/vision-agent): VisionAgent is a well-documented
code-generation harness, but its repository description now marks it deprecated.

**If you only have ten minutes**, read the four `Paper only` entries in
[Papers & Surveys](#papers--surveys) and then the [Tools & Integrations](#tools--integrations)
section; they explain the two shapes the field currently takes — a trained agent model, or an
external agent plus MCP/skill tools.

## Agents & Applications

End-to-end systems that carry out multi-step segmentation: they decide what to do next, call a
segmenter or an editor, look at the result, and continue. What the agent decides, which tools it
calls, and where its feedback comes from are stated per entry.

- **[VASA](https://github.com/Wayne2Wang/VASA)** — Training-free vision-harnessing agent for open
  ad-hoc segmentation: a VLM coordinates SAM 3 through planning, mask editing, scrutiny and error
  recovery while keeping one working mask persistent, inspectable and editable, and each run saves a
  trace viewer plus the tool-call history.
  <sub>`Natural images` · `Text` · `2D` · Status: `Early` · Verified: 2026-11-05 · [paper](https://arxiv.org/abs/2605.19410)</sub>

- **[MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent)** — Qwen3-VL agent trained with
  multi-turn reinforcement learning to choose positive/negative points, boxes or an early stop for a
  medical segmenter (MedSAM2, SAM 2.1 or IMISNet), with single-image and batch inference scripts
  plus an RL training recipe.
  <sub>`Medical` · `Points` `Boxes` · `2D` · Status: `Early` · Verified: 2026-11-05 · [paper](https://arxiv.org/abs/2602.03320)</sub>

- **[MedSegAgent](https://github.com/uni-medical/MedSegAgent)** — Multi-agent AutoGen pipeline that
  maps a free-text medical segmentation request to dataset-specific nnU-Net models and label IDs
  through coarse-to-fine query filtering; a TotalSegAgent branch adds a runnable CT/MR segmentation
  service and web viewer.
  <sub>`Medical` · `Text` · `3D` · Status: `Active` · Verified: 2026-11-05</sub>

- **[SegAgent](https://github.com/aim-uofa/SegAgent)** — MLLM trained to imitate human annotator
  trajectories: it issues a sequence of interactions to an interactive segmentor to build and refine
  a mask over several steps, and the weights, inference code and HLMAT trajectory dataset are
  released.
  <sub>`Natural images` · `Text` `Interactive` · `2D` · Status: `Maintained` · Verified: 2026-11-05 · [paper](https://arxiv.org/abs/2503.08625)</sub>

- **[VoxelSage](https://github.com/ZJUMAI/VoxelSage)** — Self-hosted abdominal CT workspace where a
  natural-language agent drives imaging skills — segmentation through VISTA3D or TotalSegmentator,
  quantitative measurements, key-slice selection and interactive 3D reconstruction — behind a web UI
  and a documented Skills API.
  <sub>`Medical` · `Text` `Interactive` · `3D` · Status: `Early` · Verified: 2026-11-05 · [paper](https://arxiv.org/abs/2609.37648)</sub>

- **[GenCellAgent](https://github.com/yuxi120407/GenCELLAgent)** — Training-free multi-agent system
  for cellular microscopy that routes each image to specialist or generalist segmenters (Cellpose,
  µSAM, ERNet, MitoNet, LISA, SegGPT) in a plan–execute–evaluate loop, with VLM-based quality
  scoring, human corrections and remembered configurations.
  <sub>`Microscopy` · `Text` `Interactive` · `2D` · Status: `Early` · Verified: 2026-11-05</sub>

- **[ask-to-mask](https://github.com/janelia-cellmap/ask-to-mask)** — Electron-microscopy organelle
  segmentation with an agentic refinement loop: a vision-language model writes the prompt, a
  generator draws the mask, and a VLM critic drives further iterations; SAM 3 point prompts and
  majority voting over orthogonal planes produce 3D masks.
  <sub>`Microscopy` · `Text` `Points` · `2D` `3D` · Status: `Early` · Verified: 2026-11-05</sub>

- **[FarmSeeker](https://github.com/WithoutOcean/FarmSeeker)** — Remote-sensing farmland
  segmentation agent that detects ambiguous regions, retrieves extra spatio-temporal imagery,
  reasons across dates and refines the mask with SAM 2.1; the accompanying GSFS-Bench is described
  as a global-scale farmland segmentation benchmark that supports reasoning–querying.
  <sub>`Remote sensing` · `Text` `Masks` · `2D` · Status: `Early` · Verified: 2026-11-05</sub>

- **[Refer-Agent](https://github.com/iSEE-Laboratory/Refer-Agent)** — Collaborative multi-agent
  system for referring video object segmentation, where reasoning and reflection stages build and
  check the target description before SAM 2 propagates masks through the video.
  <sub>`Video` · `Text` · `Video` · Status: `Active` · Verified: 2026-11-05 · [paper](https://arxiv.org/abs/2602.03595)</sub>

- **[Agentic-SAM](https://github.com/mdialameh/Agentic-SAM)** — Local ultrasound assistant that uses
  LangGraph tool orchestration over SAM 3, Medical-SAM3 and MedSAM2 to segment a PTMC bounding box,
  track it frame by frame through RFA video and post live tracking notes.
  <sub>`Medical` · `Text` `Boxes` · `2D` · Status: `Early` · Verified: 2026-11-05</sub>

- **[MMedAgent](https://github.com/Wangyixinxin/MMedAgent)** — Multimodal medical agent trained to
  select and call specialist tools, including MedSAM for box-prompted segmentation and Grounding
  DINO plus MedSAM for text-prompted segmentation, across seven imaging modalities.
  <sub>`Medical` · `Text` `Boxes` · `2D` · Status: `Maintained` · Verified: 2026-11-05 · [paper](https://aclanthology.org/2024.findings-emnlp.510/)</sub>

- **[Change-Agent](https://github.com/Chen-Yang-Liu/Change-Agent)** — LLM agent built on Lagent for
  bi-temporal remote-sensing images: it runs a multi-level change interpretation model to obtain
  change masks and descriptions, then answers follow-up questions about the changes.
  <sub>`Remote sensing` · `Text` · `2D` · Status: `Maintained` · Verified: 2026-11-05 · [paper](https://ieeexplore.ieee.org/document/10591792)</sub>

  <sub>Note: the agent layer is an LLM tool router over a fixed change-interpretation model. It does
  not inspect masks and retry, so it fits the agentic criterion more weakly than the entries above.</sub>

- **[LORE](https://github.com/nourhanb/LORE-Interactive-Agentic-Segmentation-Framework-)** —
  Interactive agentic framework for 3D tumor segmentation: a policy observes the current mask, error
  residuals and shape descriptors, chooses which correction to request (click, box, scribble) and
  decides when to stop; the agent code is released, datasets and weights are not.
  <sub>`Medical` · `Interactive` · `3D` · Status: `Early` · Verified: 2026-11-05</sub>

## Harnesses & Frameworks

Reusable execution machinery: planning, tool orchestration, generated code and tests, budgets,
traces, retries, versioned presets, evaluation splits. A general-purpose agent framework belongs
here only when the repository shows a concrete segmentation integration — which is the case for
both entries below.

- **[VisionAgent](https://github.com/landing-ai/vision-agent)** — Library that plans a vision task,
  generates runnable Python that calls a large tool set — including SAM 2-based instance
  segmentation and video tracking — then tests the generated code and iterates until its test case
  passes. The repository description now marks the project deprecated in favour of LandingAI's
  Agentic Document Extraction.
  <sub>`Natural images` · `Text` · `2D` · Status: `Deprecated` · Verified: 2026-11-05</sub>

  <sub>Note: deprecation is stated in the GitHub repository description, not in the README. The
  tool inventory is real (`agentic_sam2_instance_segmentation`, `florence2_sam2_*`, `sam2`, …), but
  new work should not start here.</sub>

- **[agentic-segmentation (coding-agent harness)](https://github.com/sameed-khan/agentic-segmentation)** —
  Research harness in which a general coding agent drives nnInteractive through a small set of
  `seg_*` tools to segment 3D MRI tumours; versioned harness presets, per-run traces, evaluation
  splits and a reproducible experiment log are part of the repository.
  <sub>`Medical` · `Interactive` · `3D` · Status: `Early` · Verified: 2026-11-05</sub>

  <sub>Note: the default branch is `integrate`, heavy run artifacts are tracked with DVC, and the
  README frames the work as an investigation ("whether coding agents can drive 3D interactive
  segmentation tools") rather than a product.</sub>

## Tools & Integrations

Backends, MCP servers, skills, plugins, adapters and fixed pipelines that an agent can call. The
host (who calls it) and the backend (what does the computation) are stated. A wrapper is not an
agent, and none of these entries claims otherwise.

- **[SAM 3](https://github.com/facebookresearch/sam3)** — Meta's promptable concept segmentation
  model, released with inference and fine-tuning code and a bundled agent package in which a
  multimodal LLM calls tools such as `segment_phrase`, `examine_each_mask`, `select_masks` and
  `report_no_mask` over a bounded number of turns.
  <sub>`Natural images` · `Text` `Points` `Boxes` · `2D` · Status: `Active` · Verified: 2026-11-05</sub>

  <sub>Note: weights require accepting the Hugging Face access terms; the repository licence is a
  custom Meta licence (GitHub reports NOASSERTION).</sub>

- **[nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent)** — MCP server plus agent
  skill that gives a host agent (Claude Code, Codex or another MCP client) tools to prompt
  nnInteractive with scribbles, boxes and points, inspect 3D renders, undo and correct; a web demo
  and an agent benchmark are included.
  <sub>`Medical` `Microscopy` · `Interactive` · `3D` · Status: `Active` · Verified: 2026-11-05 · [paper](https://arxiv.org/abs/2610.31080)</sub>

  <sub>Note: the decisions belong to the host agent. The package supplies the tools, a skill with a
  correction playbook and verification guidance, and it declares the `python` tool as a security
  surface with three permission levels.</sub>

- **[SAM 3 Segmentation Skill](https://github.com/lillyguisnet/sam3-segmentation)** — Agent skill
  that wraps SAM 3 behind staged CLI commands — `find`, `click`, `everything`, then `audit`,
  `select`, `review-sheets`, `refine` and `export` — so a host agent can review proposals, record
  reversible decisions and export PNG or COCO RLE masks.
  <sub>`Natural images` · `Text` `Points` `Boxes` · `2D` · Status: `Early` · Verified: 2026-11-05</sub>

  <sub>Note: needs an NVIDIA GPU and accepted SAM 3 access; the author states it was mostly written
  by an AI and not thoroughly human-checked, and that outputs are proposals rather than verified
  masks.</sub>

- **[ComfyUI Segmentation Agent](https://github.com/adambarbato/ComfyUI-Segmentation-Agent)** —
  ComfyUI node that asks a vision LLM to break a character description into SAM 3 phrases, renders
  numbered mask candidates back to the model, and iterates until the model accepts a subset.
  <sub>`Natural images` · `Text` · `2D` · Status: `Early` · Verified: 2026-11-05</sub>

  <sub>Note: the published test file references a class that does not exist in the repository, so
  the test suite appears broken as shipped.</sub>

- **[Grounded SAM 2](https://github.com/IDEA-Research/Grounded-SAM-2)** — Demo pipelines that chain
  Grounding DINO or Florence-2 with SAM 2 for open-vocabulary image masks and video object tracking;
  a fixed pipeline rather than an agent, but a common segmentation backend in agent stacks.
  <sub>`Natural images` `Video` · `Text` · `2D` `Video` · Status: `Maintained` · Verified: 2026-11-05</sub>

  <sub>Note: no feedback loop — text goes to a detector, boxes go to SAM 2, masks come back. Some
  README features are marked as under development.</sub>

- **[proofreader-mcp](https://github.com/janelia-cellmap/proofreader-mcp)** — MCP server for
  image-centric proofreading of segmentation objects: it stores per-object screenshots as
  resources, ranks likely overmerge, oversegment, junk or misclassified cases for the host LLM to
  judge, and records human verdicts without running any model itself.
  <sub>`Microscopy` · `No prompt` · `3D` · Status: `Early` · Verified: 2026-11-05</sub>

- **[gfm-mcp](https://github.com/yuyi1008688/gfm-mcp)** — MCP server that exposes geospatial
  foundation model inference as tools — building extraction, water segmentation, object detection,
  change detection, zero-shot scene classification and embeddings — so an LLM agent can call
  remote-sensing segmentation from CPU.
  <sub>`Remote sensing` · `Text` · `2D` · Status: `Early` · Verified: 2026-11-05</sub>

  <sub>Note: Chinese-first documentation; GPL-3.0; some embedding tools need a proxy for Google
  Earth Engine.</sub>

- **[MCP-Slicer](https://github.com/zhaoyouj/mcp-slicer)** — MCP server that lets a client drive 3D
  Slicer: list MRML nodes, execute Python inside the Slicer environment and capture screenshots of
  slice and 3D views, which supplies the visual feedback step of a ReAct-style loop.
  <sub>`Medical` · `No prompt` · `3D` · Status: `Active` · Verified: 2026-11-05</sub>

  <sub>Note: segmentation is reached through Slicer modules and the Python tool, not through a
  dedicated segmentation tool.</sub>

- **[BioImage-Agent (napari MCP)](https://github.com/llnl/bioimage-agent)** — napari plugin that
  exposes the viewer over MCP through a socket server, letting external agents inspect images and
  call napari's public API from a separate process.
  <sub>`Microscopy` · `No prompt` · `2D` · Status: `Early` · Verified: 2026-11-05</sub>

  <sub>Note: viewer control only; segmentation happens in other napari plugins the agent may call.</sub>

- **[MedMCP](https://github.com/medmcp/medmcp)** — On-premise agentic workspace for medical imaging:
  a locally served model plans the work, installable tool stacks do the computation, and a viewer
  shows images with segmentation overlays; by default nothing leaves the machine.
  <sub>`Medical` · `Text` · `3D` · Status: `Active` · Verified: 2026-11-05</sub>

  <sub>Note: README states it is under active development and not licensed for clinical use.</sub>

## Evaluation & Benchmarks

What is being measured matters: a script that runs without error, a model judging its own mask, and
accuracy against human annotation are three different things. Entries here state which one they do.

- **[BIABench](https://github.com/BIABench/BIABench)** — Benchmark of 16 real bioimage-analysis
  tasks reconstructed from published studies, scored both on the produced result and on how the
  analysis was carried out; it ships adapters for coding agents such as Claude Code, Codex and
  DeepSeek Harness behind a single `run(instruction, input_dir, output_dir)` interface.
  <sub>`Microscopy` · `Text` · `2D` · Status: `Active` · Verified: 2026-11-05 · [paper](https://arxiv.org/abs/2609.34274)</sub>

  <sub>Note: tasks include nuclear segmentation; because outcome and process are scored separately,
  a successful execution is not by itself a quality result.</sub>

**Benchmarks released inside the projects above** (cross-links, not separate entries — a project has
one canonical entry in this list):

- [nnInteractive Agent benchmark](https://github.com/MIC-DKFZ/nninteractive-agent/blob/master/benchmark/README.md)
  — mean Dice of Claude Code and Codex driving nnInteractive on 14 public CT/MRI/PET images and 51
  targets, compared with single-click prompting and a text-only 3D model.
- [HLMAT evaluation](https://github.com/aim-uofa/SegAgent/blob/main/evaltools/eval.md) — mask quality
  after human-like click trajectories, measured with the repository's IoU script.
- [MSTT-199 and BEAMSTER splits](https://github.com/sameed-khan/agentic-segmentation/tree/integrate/eval)
  — coding-agent segmentation of soft-tissue tumours and brain metastases in 3D MRI, with per-run
  scores and trajectories.
- [GSFS-Bench](https://github.com/WithoutOcean/FarmSeeker) — farmland segmentation with
  reasoning-and-querying; dataset not yet released at verification time.
- [MedSegAgent model-selection test set](https://github.com/uni-medical/MedSegAgent/blob/main/evaluate.py)
  — dataset-level hit rate of the routing pipeline, not mask Dice.

## Examples & Tutorials

Runnable walkthroughs. Each one belongs to a project that already has an entry above; it is listed
here as a way in, not as a separate project.

- **[SAM 3 Agent notebook](https://github.com/facebookresearch/sam3/blob/main/examples/sam3_agent.ipynb)** —
  Official notebook that runs the SAM 3 agent end to end: it builds SAM 3, points it at a
  vLLM-served Qwen3-VL, and calls `run_single_image_inference` on a text query, writing the
  prediction, a rendered mask and the agent history.
  <sub>`Natural images` · `Text` · `2D` · From: SAM 3 · Verified: 2026-11-05</sub>

- **[VASA demo and trace viewer](https://github.com/Wayne2Wang/VASA/tree/main/outputs)** — Three
  ready-made queries on the bundled example image with their recorded outputs; opening `trace.html`
  replays planning, tool calls and mask edits step by step without running anything.
  <sub>`Natural images` · `Text` · `2D` · From: VASA · Verified: 2026-11-05</sub>

- **[nnInteractive Agent web demo](https://github.com/MIC-DKFZ/nninteractive-agent#web-demo)** —
  Browser demo that runs the same MCP tools and skill behind a chat with live 2D/3D views, for
  showing agent-driven 3D annotation to people who have no agent installed.
  <sub>`Medical` · `Interactive` · `3D` · From: nnInteractive Agent · Verified: 2026-11-05</sub>

## Papers & Surveys

Research that directly informs segmentation agents. Where a project already has an entry above, its
paper is linked from that entry instead of being listed again. Everything here is marked with what
was actually released.

- **[RSAgent](https://arxiv.org/abs/2512.24023)** — Agentic multimodal LLM for text-guided
  segmentation that queries a segmentation toolbox, observes visual feedback and revises its spatial
  hypothesis over multiple turns; trained with cold-start SFT followed by agentic RL. No public code
  repository was found at verification time.
  <sub>`Natural images` · `Text` · `2D` · Status: `Paper only` · Verified: 2026-11-05</sub>

- **[RSure-Agent](https://github.com/AIRS101/RSure-Agent)** — Remote-sensing agent that verifies
  tool observations before using them in later reasoning to reduce error propagation; the repository
  publishes the site, demo videos and paper, while the core tool-calling and verification code is
  still listed as unreleased.
  <sub>`Remote sensing` · `Text` · `2D` · Status: `Paper only` · Verified: 2026-11-05 · [paper](https://arxiv.org/abs/2610.04836)</sub>

- **[VoxelPrompt](https://arxiv.org/abs/2410.08397)** — Vision-language agent for 3D medical images
  that emits executable instructions to a frozen segmentation network, adapting language prompts to
  volumetric tasks end to end. No public code repository was found at verification time.
  <sub>`Medical` · `Text` · `3D` · Status: `Paper only` · Verified: 2026-11-05</sub>

- **[SEER](https://github.com/Ztrura/SEER)** — Vision-language reasoning model for free-text 3D
  medical segmentation that grounds clinical language in image evidence and emits an executable
  target specification for a segmentation backbone; checkpoints, inference code and an evaluation
  split are released.
  <sub>`Medical` · `Text` · `3D` · Status: `Active` · Verified: 2026-11-05 · [paper](https://arxiv.org/abs/2603.08215)</sub>

  <sub>Note: reasoning is single-pass — it produces a specification rather than iterating with
  tools, which is why it is listed as research and not as an agent system.</sub>

## Related Resources

Links that are useful but are not curated as core entries. They are model layers, adjacent agent
directions, or benchmarks that do not score segmentation.

- [awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) — classic
  segmentation model, dataset and tool index, useful for the model layer this list does not
  catalogue.
- [Awesome-Segment-Anything](https://github.com/liliu-avril/Awesome-Segment-Anything) — promptable
  segmentation paper collection, including SAM-family and interactive segmentation work.
- [awesome-medical-imaging-agents](https://github.com/Nanboy-Ronan/awesome-medical-imaging-agents) —
  broad index of medical imaging agents with a dedicated segmentation-and-annotation section.
- [Awesome-Multimodal-Agent](https://github.com/OpenEnvision/Awesome-Multimodal-Agent) — multimodal
  agent papers adjacent to tool-using segmentation agents.
- [SAM 2](https://github.com/facebookresearch/sam2) — promptable image and video segmentation
  backend used by several agent systems above.
- [nnInteractive](https://github.com/MIC-DKFZ/nnInteractive) — 3D interactive segmentation framework
  behind the nnInteractive Agent entry.
- [MedSAM2](https://github.com/bowang-lab/MedSAM2) — medical promptable segmentation and tracking
  model used as a backend by medical agents here.
- [Seg-Zero](https://github.com/JIA-Lab-research/Seg-Zero) — reasoning-chain segmentation model with
  a separate mask decoder; no tool loop, so it is linked rather than curated as an agent.
- [ThinkGeo](https://github.com/mbzuai-oryx/ThinkGeo) — benchmark for tool-augmented remote-sensing
  agents; not segmentation-scored, so it is linked rather than listed as a segmentation benchmark.

## Contributing

This repository is private for now and not accepting outside contributions. The inclusion criteria,
category rules, entry format, source requirements and maintenance process are documented in
[CONTRIBUTING.md](CONTRIBUTING.md). In short: an entry needs a canonical link, a category, a factual
one-sentence description, a status, a verification date and at least one evidence URL; claims must
come from the project's own repository or paper and must be attributed, and unknown things stay
`unknown`.

Maintenance agents should read [AGENTS.md](AGENTS.md) first.

## License / Usage Notice

**No licence has been chosen for this list.** It is a private compilation at this stage; whether it
becomes public, and under which licence, is the owner's decision and has not been made. Do not
redistribute or reuse the compilation until that decision is published.

Every project linked here remains under its own licence, which the reader must check before use.
Descriptions are short factual summaries with links to the original artefacts; no third-party
README, image, dataset, or code is copied into this repository. Model weights and datasets are not
included and are often gated behind the project's own terms.

Nothing here is medical, safety, or security advice, and no entry has been clinically evaluated. The
verification dates record a read-only check, not an endorsement.

---

**33 entries** across six sections, **5 embedded benchmarks**, **9 related resources**. Last
verification pass: 2026-11-05. Machine-readable records: [data/resources.json](data/resources.json).
Selection notes, rejected candidates and open questions: [docs/research-notes.md](docs/research-notes.md).
