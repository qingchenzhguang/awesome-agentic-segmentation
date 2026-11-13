<h1 align="center">Awesome Agentic Segmentation</h1>

<p align="center">
  <img src="https://img.shields.io/badge/entries-33-0969da" alt="33 entries">
  <img src="https://img.shields.io/badge/domains-5-1a7f37" alt="5 imaging domains">
  <img src="https://img.shields.io/badge/licence-not%20chosen-bf8700" alt="No licence chosen">
</p>

<p align="center">
  <a href="#overview">Overview</a> &nbsp;·&nbsp;
  <a href="#design-space">Design space</a> &nbsp;·&nbsp;
  <a href="#browse">Browse</a> &nbsp;·&nbsp;
  <a href="#start-here">Start here</a> &nbsp;·&nbsp;
  <a href="#patterns">Patterns</a> &nbsp;·&nbsp;
  <a href="#maintenance">Maintenance</a> &nbsp;·&nbsp;
  <a href="#open-questions">Open questions</a> &nbsp;·&nbsp;
  <a href="#contributing">Contributing</a> &nbsp;·&nbsp;
  <a href="#usage-notice">Usage</a>
</p>

![Agents plan a segmentation task, call vision tools, inspect the returned masks and refine](assets/hero.svg)

*Agents plan a segmentation task, call vision tools, inspect the returned mask and feed what they see into the next step — the loop this list is about.*

## Overview

A curated list of agents, harnesses, tools and resources for **agentic image segmentation**: systems that plan segmentation tasks, use vision tools, inspect masks and refine results, plus the integrations, benchmarks and workflows around them. Chinese: [README.zh-CN.md](README.zh-CN.md).

A project is in scope when all three hold: an agent **decides** something (which tool, which prompt, whether to stop), it **calls** a segmentation tool whose artifact it receives, and that artifact **feeds back** into the next action. A name containing "agent" is not evidence of agency.

This is not a catalogue of segmentation models, datasets or papers. Model backends appear only where an agent can call them; plain models are linked from [Related Resources](#related-resources). Industrial inspection is a target domain with no verified entry, so no placeholder is shipped for it.

## Design space

Each entry is labelled on four dimensions. The labels are a controlled vocabulary rather than free text, so they stay stable as the list grows.

| Dimension | Options |
| :--- | :--- |
| **Role** | Agent & application · Harness · Tool / integration · Benchmark · Example · Paper |
| **Domain** | Natural images · Medical · Remote sensing · Microscopy · Video |
| **Prompt** | Text · Points · Boxes · Masks · Interactive · No prompt |
| **Dimensionality** | 2D · 3D · Video |

## Browse

| Role | What belongs here | Entries |
| :--- | :--- | :---: |
| [Agents & Applications](#agents--applications) | End-to-end systems that plan, call segmentation tools, inspect masks and iterate | 13 |
| [Harnesses & Frameworks](#harnesses--frameworks) | Execution loops, generated code and tests, presets, traces, budgets, evaluation splits | 2 |
| [Tools & Integrations](#tools--integrations) | Backends, MCP servers, skills, plugins and fixed pipelines an agent can call | 10 |
| [Evaluation & Benchmarks](#evaluation--benchmarks) | Benchmarks that score segmentation agents, plus benchmarks embedded in listed projects | 1 + 5 |
| [Examples & Tutorials](#examples--tutorials) | Runnable walkthroughs belonging to listed projects | 3 |
| [Papers & Surveys](#papers--surveys) | Research directly about segmentation agents, tool use and feedback | 4 |
| [Related Resources](#related-resources) | Model layers, adjacent agent directions and non-segmentation benchmarks | 9 |

## Start here

| If you want to… | Start with | Why it fits |
| :--- | :--- | :--- |
| Segment something described in words | [VASA](https://github.com/Wayne2Wang/VASA), [SAM 3 Agent notebook](https://github.com/facebookresearch/sam3/blob/main/examples/sam3_agent.ipynb) | One keeps an editable working mask with trace playback; the other is the official bounded SAM 3 tool loop. Both need weights and a VLM endpoint. |
| Give your coding agent segmentation tools | [nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent), [SAM 3 Segmentation Skill](https://github.com/lillyguisnet/sam3-segmentation) | An MCP server plus a correction skill for 3D; a staged CLI skill with review sheets for 2D photos. |
| Work on 3D medical annotation | [nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent), [agentic-segmentation](https://github.com/sameed-khan/agentic-segmentation) | Tools and a benchmark for one; a documented coding-agent harness with splits and traces for the other. |
| Route medical requests to the right model | [MedSegAgent](https://github.com/uni-medical/MedSegAgent), [MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent) | Model and label routing at dataset level; a trained agent choosing prompts for a medical segmenter. |
| Go beyond natural images | [GenCellAgent](https://github.com/yuxi120407/GenCELLAgent), [ask-to-mask](https://github.com/janelia-cellmap/ask-to-mask), [FarmSeeker](https://github.com/WithoutOcean/FarmSeeker) | Microscopy tool routing, VLM-critique refinement, and remote-sensing retrieval plus SAM 2.1 refinement. |
| Study or build the harness | [agentic-segmentation](https://github.com/sameed-khan/agentic-segmentation), [BIABench](https://github.com/BIABench/BIABench) | Versioned presets and traces; 16 tasks scored on both outcome and process. |

## Patterns

Five things the entries have in common — and where they do not:

- **Two shapes.** Either a trained model that emits prompts or actions (SegAgent, MedSAM-Agent, MMedAgent, LORE, RSAgent), or an external coding agent that drives tools through MCP, skills or a node (nnInteractive Agent, SAM 3 Segmentation Skill, ComfyUI Segmentation Agent, the MCP servers).
- **Feedback is mostly visual.** 3D renders, slice screenshots, review sheets and VLM critiques are the common loop; a few systems act on mask geometry or a scalar state instead (MedSAM-Agent's updated mask, LORE's error residuals).
- **Medical imaging dominates.** Six of the 13 agent entries and three of the 10 tools are medical; remote sensing and microscopy contribute distinct patterns — spatio-temporal retrieval and multi-agent tool routing.
- **Evaluation is thin.** One independent benchmark (BIABench). Everything else reports author-run numbers, and several repositories ship no evaluation script at all.
- **Industrial inspection is missing.** Searches returned segmentation models and anomaly detectors, but no agent with an inspectable tool loop, so the section is absent rather than padded.

## Agents & Applications

Complete systems that decide what to do next, call a segmenter or an editor, look at the result and continue.

| Project | What it provides | Scope |
| :--- | :--- | :--- |
| **[VASA](https://github.com/Wayne2Wang/VASA)** · [paper](https://arxiv.org/abs/2605.19410) | A VLM plans, builds and edits one persistent working mask with SAM 3, scrutinises it and recovers from errors; every run saves a trace viewer and the tool-call history. | `Natural images` · `Text` · `2D` |
| **[MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent)** · [paper](https://arxiv.org/abs/2602.03320) | Qwen3-VL trained with multi-turn RL to choose positive/negative points, boxes or an early stop for a medical segmenter; ships inference scripts and an RL recipe. | `Medical` · `Points` `Boxes` · `2D` |
| **[MedSegAgent](https://github.com/uni-medical/MedSegAgent)** | AutoGen pipeline that routes a free-text request to dataset-specific nnU-Net models and label IDs; a TotalSegAgent branch runs the segmentation and shows it in a viewer. | `Medical` · `Text` · `3D` |
| **[SegAgent](https://github.com/aim-uofa/SegAgent)** · [paper](https://arxiv.org/abs/2503.08625) | MLLM trained to imitate annotator trajectories: it issues a sequence of interactions to an interactive segmentor and refines the mask; weights, code and HLMAT data are released. | `Natural images` · `Text` `Interactive` · `2D` |
| **[VoxelSage](https://github.com/ZJUMAI/VoxelSage)** · [paper](https://arxiv.org/abs/2609.37648) | Self-hosted abdominal CT workspace where a language agent drives segmentation (VISTA3D or TotalSegmentator), measurements, key slices and 3D reconstruction through Skills. | `Medical` · `Text` `Interactive` · `3D` |
| **[GenCellAgent](https://github.com/yuxi120407/GenCELLAgent)** | Training-free router across Cellpose, µSAM, ERNet, MitoNet, LISA and SegGPT in a plan–execute–evaluate loop with VLM scoring, memory and human corrections. | `Microscopy` · `Text` `Interactive` · `2D` |
| **[ask-to-mask](https://github.com/janelia-cellmap/ask-to-mask)** | A VLM writes the prompt, a generator draws the mask and a VLM critic refines it; SAM 3 point prompts with majority voting over orthogonal planes produce 3D masks. | `Microscopy` · `Text` `Points` · `2D` `3D` |
| **[FarmSeeker](https://github.com/WithoutOcean/FarmSeeker)** | Detects ambiguous farmland, retrieves extra spatio-temporal imagery, reasons across dates and refines the mask with SAM 2.1; GSFS-Bench accompanies it. | `Remote sensing` · `Text` `Masks` · `2D` |
| **[Refer-Agent](https://github.com/iSEE-Laboratory/Refer-Agent)** · [paper](https://arxiv.org/abs/2602.03595) | Reasoning and reflection agents build and check the target description before SAM 2 propagates masks through the video. | `Video` · `Text` · `Video` |
| **[Agentic-SAM](https://github.com/mdialameh/Agentic-SAM)** | LangGraph tools over SAM 3, Medical-SAM3 and MedSAM2 for box-prompted PTMC segmentation, frame-by-frame RFA video tracking and live tracking notes. | `Medical` · `Text` `Boxes` · `2D` |
| **[MMedAgent](https://github.com/Wangyixinxin/MMedAgent)** · [paper](https://aclanthology.org/2024.findings-emnlp.510/) | Trained tool selector whose tools include MedSAM box prompts and Grounding DINO + MedSAM text prompts, alongside classification, VQA and report generation. | `Medical` · `Text` `Boxes` · `2D` |
| **[Change-Agent](https://github.com/Chen-Yang-Liu/Change-Agent)** · [paper](https://ieeexplore.ieee.org/document/10591792) | Lagent agent that runs a multi-level change-interpretation model on bi-temporal images, returns change masks and descriptions, and answers follow-up questions. | `Remote sensing` · `Text` · `2D` |
| **[LORE](https://github.com/nourhanb/LORE-Interactive-Agentic-Segmentation-Framework-)** | A policy observes the mask, error residuals and shape descriptors, then chooses the next correction (click, box, scribble) or stops; code released, weights and data not. | `Medical` · `Interactive` · `3D` |

**Notes.** `Change-Agent` fits the agent criterion weakly: its agent layer routes queries to a fixed interpretation model and does not inspect masks and retry. `MMedAgent` uses segmentation as one tool family among several — the entry is about the tool-selection loop, not the segmenter.

[↑ Back to browse](#browse)

## Harnesses & Frameworks

Reusable execution machinery: planning, code generation and tests, presets, traces, budgets, retries and evaluation splits. A general framework is listed only when the repository shows a concrete segmentation integration.

| Project | What it provides | Scope |
| :--- | :--- | :--- |
| **[VisionAgent](https://github.com/landing-ai/vision-agent)** | Plans a vision task, generates Python that calls tools including SAM 2 instance segmentation and video tracking, tests the code and iterates; the repository description marks it deprecated. | `Natural images` · `Text` · `2D` |
| **[agentic-segmentation](https://github.com/sameed-khan/agentic-segmentation)** | A general coding agent drives nnInteractive through `seg_*` tools for 3D MRI tumours; versioned presets, per-run traces, evaluation splits and an experiment log. | `Medical` · `Interactive` · `3D` |

**Notes.** `VisionAgent` is documented and its tool inventory is real, but new work should not start from a deprecated repository. `agentic-segmentation` uses `integrate` as its default branch and DVC for heavy artifacts, and frames itself as an investigation rather than a product.

[↑ Back to browse](#browse)

## Tools & Integrations

Backends, MCP servers, skills, plugins and fixed pipelines an agent can call. The host (who calls) and the backend (who computes) are the point of this section; a wrapper is not an agent.

| Project | What it provides | Scope |
| :--- | :--- | :--- |
| **[SAM 3](https://github.com/facebookresearch/sam3)** | Meta's promptable concept model, with a bundled agent package in which an MLLM calls `segment_phrase`, `examine_each_mask`, `select_masks` and `report_no_mask`. | `Natural images` · `Text` `Points` `Boxes` · `2D` |
| **[nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent)** · [paper](https://arxiv.org/abs/2610.31080) | MCP server plus agent skill: the host agent prompts nnInteractive with scribbles, boxes and points, inspects 3D renders, undoes and corrects. | `Medical` `Microscopy` · `Interactive` · `3D` |
| **[SAM 3 Segmentation Skill](https://github.com/lillyguisnet/sam3-segmentation)** | Skill wrapping SAM 3 in staged CLI commands — find, click, everything, then audit, select, review-sheets, refine and export — with reversible review decisions. | `Natural images` · `Text` `Points` `Boxes` · `2D` |
| **[ComfyUI Segmentation Agent](https://github.com/adambarbato/ComfyUI-Segmentation-Agent)** | ComfyUI node where a vision LLM splits a character description into SAM 3 phrases, inspects numbered mask candidates and accepts a subset. | `Natural images` · `Text` · `2D` |
| **[Grounded SAM 2](https://github.com/IDEA-Research/Grounded-SAM-2)** | Fixed Grounding DINO or Florence-2 → SAM 2 pipelines for open-vocabulary masks and video tracking; a backend, with no feedback loop. | `Natural images` `Video` · `Text` · `2D` `Video` |
| **[proofreader-mcp](https://github.com/janelia-cellmap/proofreader-mcp)** | MCP server that ranks likely overmerge, oversegment, junk or misclassified objects for the host LLM and records human verdicts; it runs no model. | `Microscopy` · `No prompt` · `3D` |
| **[gfm-mcp](https://github.com/yuyi1008688/gfm-mcp)** | MCP tools for geospatial foundation models: building and water segmentation, object and change detection, zero-shot classification and embeddings, on CPU. | `Remote sensing` · `Text` · `2D` |
| **[MCP-Slicer](https://github.com/zhaoyouj/mcp-slicer)** | MCP server driving 3D Slicer: list MRML nodes, run Python in Slicer and capture slice and 3D screenshots to close a ReAct loop. | `Medical` · `No prompt` · `3D` |
| **[BioImage-Agent](https://github.com/llnl/bioimage-agent)** | napari plugin exposing the viewer over MCP so external agents can inspect images and call napari's public API from another process. | `Microscopy` · `No prompt` · `2D` |
| **[MedMCP](https://github.com/medmcp/medmcp)** | On-premise agentic workspace: a locally served model plans, installable tool stacks compute and a viewer shows segmentation overlays; data stays local by default. | `Medical` · `Text` · `3D` |

**Notes.** `SAM 3` weights need Hugging Face terms acceptance, and the repository uses a custom Meta licence. `SAM 3 Segmentation Skill` was largely written by an AI, by the author's own statement, and `ComfyUI Segmentation Agent` ships a test file that imports a class the repository does not define. `gfm-mcp` is GPL-3.0, and `MedMCP` states it is not licensed for clinical use.

[↑ Back to browse](#browse)

## Evaluation & Benchmarks

What is measured matters: a script that runs, a model judging its own mask and accuracy against human annotation are three different things.

| Benchmark | What it measures | Scope |
| :--- | :--- | :--- |
| **[BIABench](https://github.com/BIABench/BIABench)** · [paper](https://arxiv.org/abs/2609.34274) | 16 real bioimage-analysis tasks reconstructed from published studies, scored on both the produced result and the analysis process, behind one `run(instruction, input_dir, output_dir)` interface. | `Microscopy` · `Text` · `2D` |

**Benchmarks released inside listed projects** are cross-linked rather than duplicated as entries, because a project keeps one canonical row in this list.

| Benchmark | Hosted in | What it measures |
| :--- | :--- | :--- |
| [nnInteractive Agent benchmark](https://github.com/MIC-DKFZ/nninteractive-agent/blob/master/benchmark/README.md) | nnInteractive Agent | Mean Dice of Claude Code and Codex driving nnInteractive on 14 public CT, MRI, PET and micro-CT images and 51 targets. |
| [HLMAT evaluation](https://github.com/aim-uofa/SegAgent/blob/main/evaltools/eval.md) | SegAgent | Mask quality after human-like click trajectories, scored with the repository's IoU script. |
| [MSTT-199 and BEAMSTER splits](https://github.com/sameed-khan/agentic-segmentation/tree/integrate/eval) | agentic-segmentation | Coding-agent segmentation of soft-tissue tumours and brain metastases in 3D MRI, with per-run scores and trajectories. |
| [GSFS-Bench](https://github.com/WithoutOcean/FarmSeeker) | FarmSeeker | Farmland segmentation with reasoning-and-querying; dataset not yet released. |
| [MedSegAgent model-selection test set](https://github.com/uni-medical/MedSegAgent/blob/main/evaluate.py) | MedSegAgent | Dataset-level hit rate of the routing pipeline, not mask Dice. |

[↑ Back to browse](#browse)

## Examples & Tutorials

Runnable walkthroughs. Each belongs to a project already listed above; it is a way in, not a separate project.

| Example | What you get | Source |
| :--- | :--- | :--- |
| **[SAM 3 Agent notebook](https://github.com/facebookresearch/sam3/blob/main/examples/sam3_agent.ipynb)** | Official notebook: builds SAM 3, calls a vLLM-served Qwen3-VL, runs `run_single_image_inference` and saves the prediction, mask and agent history. | SAM 3 · `Natural images` |
| **[VASA demo and trace viewer](https://github.com/Wayne2Wang/VASA/tree/main/outputs)** | Three recorded queries; opening `trace.html` replays planning, tool calls and mask edits without running anything. | VASA · `Natural images` |
| **[nnInteractive Agent web demo](https://github.com/MIC-DKFZ/nninteractive-agent#web-demo)** | Browser chat over the same MCP tools and skill, with live 2D/3D views for people without an agent installed. | nnInteractive Agent · `Medical` |

[↑ Back to browse](#browse)

## Papers & Surveys

Research that directly informs segmentation agents. Where a project already has a row above, its paper is linked from that row instead of appearing here again.

| Work | What it contributes | Scope |
| :--- | :--- | :--- |
| **[RSAgent](https://arxiv.org/abs/2512.24023)** | Agentic MLLM that queries a segmentation toolbox, observes visual feedback and revises its spatial hypothesis over multiple turns; no public code repository was found. | `Natural images` · `Text` · `2D` |
| **[RSure-Agent](https://github.com/AIRS101/RSure-Agent)** · [paper](https://arxiv.org/abs/2610.04836) | Remote-sensing agent that verifies tool observations before reusing them; the core tool-calling and verification code is still listed as unreleased. | `Remote sensing` · `Text` · `2D` |
| **[VoxelPrompt](https://arxiv.org/abs/2410.08397)** | Vision-language agent that emits executable instructions to a frozen segmentation network for 3D medical images; no public code repository was found. | `Medical` · `Text` · `3D` |
| **[SEER](https://github.com/Ztrura/SEER)** · [paper](https://arxiv.org/abs/2603.08215) | Reasoning model that grounds clinical language and emits an executable target specification for a segmentation backbone; checkpoints, inference code and an evaluation split are released. | `Medical` · `Text` · `3D` |

[↑ Back to browse](#browse)

## Related Resources

Useful, but outside the curation boundary: model layers, adjacent agent directions, and benchmarks that do not score segmentation.

| Resource | Why it is linked |
| :--- | :--- |
| [awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) | Classic segmentation model, dataset and tool index — the model layer this list does not catalogue. |
| [Awesome-Segment-Anything](https://github.com/liliu-avril/Awesome-Segment-Anything) | Promptable segmentation papers, including SAM-family and interactive segmentation work. |
| [awesome-medical-imaging-agents](https://github.com/Nanboy-Ronan/awesome-medical-imaging-agents) | Broad medical-imaging agent index with a segmentation-and-annotation section. |
| [Awesome-Multimodal-Agent](https://github.com/OpenEnvision/Awesome-Multimodal-Agent) | Multimodal agent papers adjacent to tool-using segmentation agents. |
| [SAM 2](https://github.com/facebookresearch/sam2) | Promptable image and video segmentation backend used by several systems above. |
| [nnInteractive](https://github.com/MIC-DKFZ/nnInteractive) | 3D interactive segmentation framework behind the nnInteractive Agent entry. |
| [MedSAM2](https://github.com/bowang-lab/MedSAM2) | Medical promptable segmentation and tracking model used as a backend by medical agents here. |
| [Seg-Zero](https://github.com/JIA-Lab-research/Seg-Zero) | Reasoning-chain segmentation with a separate mask decoder; no tool loop, so it is linked rather than curated as an agent. |
| [ThinkGeo](https://github.com/mbzuai-oryx/ThinkGeo) | Tool-augmented remote-sensing agent benchmark; not segmentation-scored. |

[↑ Back to browse](#browse)

## Maintenance

The list is kept by reading, not by running. For each candidate:

1. **Discovery.** Search GitHub and the awesome lists linked above, then follow paper and project links to their repositories and demos.
2. **Evidence.** Read the project's own README and, where the entry claims a loop, the source files that implement it — tool definitions, the agent step, the feedback handling, the evaluation script. Nothing is cloned, installed or executed.
3. **Record.** Write the entry, then store the full description, tags, status, verification date and evidence URLs in [data/resources.json](data/resources.json).

Status (`Active`, `Early`, `Paper only`, …) and the last-checked date live in that JSON record rather than in every table row, so the tables stay readable; entries that are deprecated or paper-only say so in their description. Re-checks update the date for the rows actually re-read, and changes are logged in [docs/research-notes.md](docs/research-notes.md). The current snapshot was last checked on **2026-11-05**.

## Open questions

- **Independent evaluation.** BIABench is the only independent benchmark here; most evidence for the agent systems is author-run.
- **Industrial inspection.** No agentic segmentation system with an inspectable tool loop was verified for this domain, so the section is intentionally absent rather than filled.
- **Licences.** Not verified uniformly. Some repositories have a README that conflicts with their metadata, and some have no root licence file at all.
- **Runtime verification.** Nothing here was installed or run, so no row claims "works"; a passing script is not the same as a good mask.
- **Tool and skill evaluation.** The MCP servers and agent skills have little third-party evaluation; their evidence is what the authors report.

## Contributing

The repository is private and not accepting outside contributions. Inclusion criteria, category rules, the table format, source requirements and the maintenance process are in [CONTRIBUTING.md](CONTRIBUTING.md); maintenance agents should read [AGENTS.md](AGENTS.md) first. In short: a row needs a canonical link, a role, one factual summary and tags, with the evidence recorded in [data/resources.json](data/resources.json), and unknown things stay `unknown`.

## Usage notice

**No licence has been chosen for this list.** It is a private compilation; whether it becomes public, and under which licence, has not been decided, so do not redistribute or reuse it yet. Every linked project keeps its own licence, which the reader must check before use. No third-party README, image, dataset or code is copied here, and no weights or datasets are included.

Nothing here is medical, safety or security advice, and no entry has been clinically evaluated.

---

**33 entries** · **5 embedded benchmarks** · **9 related resources** · machine-readable records in [data/resources.json](data/resources.json) · selection notes and rejected candidates in [docs/research-notes.md](docs/research-notes.md)
