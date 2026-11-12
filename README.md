<h1 align="center">Awesome Agentic Segmentation</h1>

<p align="center">
  <img src="https://img.shields.io/badge/repository-private-6e7781" alt="Private repository">
  <img src="https://img.shields.io/badge/entries-33-0969da" alt="33 entries">
  <img src="https://img.shields.io/badge/verified-2026--11--05-1a7f37" alt="Verified 2026-11-05">
  <img src="https://img.shields.io/badge/license-not%20chosen-bf8700" alt="No licence chosen">
</p>

<p align="center">
  <a href="#overview">Overview</a> &nbsp;·&nbsp;
  <a href="#design-space">Design space</a> &nbsp;·&nbsp;
  <a href="#browse">Browse</a> &nbsp;·&nbsp;
  <a href="#start-here">Start here</a> &nbsp;·&nbsp;
  <a href="#agents--applications">Agents</a> &nbsp;·&nbsp;
  <a href="#harnesses--frameworks">Harnesses</a> &nbsp;·&nbsp;
  <a href="#tools--integrations">Tools</a> &nbsp;·&nbsp;
  <a href="#evaluation--benchmarks">Evaluation</a> &nbsp;·&nbsp;
  <a href="#examples--tutorials">Examples</a> &nbsp;·&nbsp;
  <a href="#papers--surveys">Papers</a> &nbsp;·&nbsp;
  <a href="#related-resources">Related</a> &nbsp;·&nbsp;
  <a href="#open-questions">Open questions</a> &nbsp;·&nbsp;
  <a href="#contributing">Contributing</a> &nbsp;·&nbsp;
  <a href="#usage-notice">Usage</a>
</p>

![Agents plan a segmentation task, call vision tools, inspect the returned masks and refine](assets/hero.svg)

*Agents plan a segmentation task, call vision tools, inspect the returned mask and feed what they see into the next step — the loop this list is about.*

## Overview

A curated list of agents, harnesses, tools and resources for **agentic image segmentation**. Explore systems that plan segmentation tasks, use vision tools, inspect masks and refine results, plus the reusable integrations, evaluation resources and workflows around them. Chinese: [README.zh-CN.md](README.zh-CN.md).

A repository is in scope when all three hold: an agent **decides** something (which tool, which prompt, whether to stop), it **calls** a segmentation tool whose artifact it receives, and that artifact **feeds back** into the next action. A name containing "agent" is not evidence of agency.

What this list is **not**: a catalogue of segmentation models, datasets or papers. Model backends appear only where an agent can call them; plain models are linked from [Related Resources](#related-resources). Industrial inspection is a target domain with no verified entry yet, so no placeholder is shipped for it.

Every entry was checked by reading the project's own documentation and, where marked, its source files on **2026-11-05**. Nothing was cloned, installed or run, and no weights were downloaded. Author claims are reported as claims. The repository is private, has no open-source licence, and is not accepting contributions yet.

## Design space

Each entry is labelled on five dimensions. The labels are a controlled vocabulary rather than free text, so they stay stable as the list grows.

| Dimension | Options |
| :--- | :--- |
| **Role** | Agent & application · Harness · Tool / integration · Benchmark · Example · Paper |
| **Domain** | Natural images · Medical · Remote sensing · Microscopy · Video |
| **Prompt** | Text · Points · Boxes · Masks · Interactive · No prompt |
| **Dimensionality** | 2D · 3D · Video |
| **Status** | Active · Maintained · Early · Deprecated · Paper only |

`Active` means development appears current; `Maintained` means usable but quiet for months; `Early` means the artifact exists but is incomplete, a research prototype, or missing released data or weights; `Deprecated` means the owner now points elsewhere; `Paper only` means no public code was found or the code is explicitly unreleased. The date in each row is the last read-only verification, not a promise that the project still runs today.

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
| Work on 3D medical annotation | [nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent), [agentic-segmentation harness](https://github.com/sameed-khan/agentic-segmentation) | Tools and a benchmark for one; a documented coding-agent harness with splits and traces for the other. |
| Route medical requests to the right model | [MedSegAgent](https://github.com/uni-medical/MedSegAgent), [MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent) | Model and label routing at dataset level; a trained agent choosing prompts for a medical segmenter. |
| Go beyond natural images | [GenCellAgent](https://github.com/yuxi120407/GenCELLAgent), [ask-to-mask](https://github.com/janelia-cellmap/ask-to-mask), [FarmSeeker](https://github.com/WithoutOcean/FarmSeeker) | Microscopy tool routing, VLM-critique refinement, and remote-sensing retrieval plus SAM 2.1 refinement. |
| Study or build the harness | [agentic-segmentation harness](https://github.com/sameed-khan/agentic-segmentation), [BIABench](https://github.com/BIABench/BIABench) | Versioned presets and traces; 16 tasks scored on both outcome and process. |

## Agents & Applications

Complete systems that decide what to do next, call a segmenter or an editor, look at the result and continue.

| Project | What it provides | Status · verified |
| :--- | :--- | :--- |
| **[VASA](https://github.com/Wayne2Wang/VASA)** · [paper](https://arxiv.org/abs/2605.19410)<br><sub>`Natural images` · `Text` · `2D`</sub> | A VLM plans, builds and edits one persistent working mask with SAM 3, scrutinises it and recovers from errors; every run saves a trace viewer and the tool-call history. | `Early`<br>2026-11-05 |
| **[MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent)** · [paper](https://arxiv.org/abs/2602.03320)<br><sub>`Medical` · `Points` `Boxes` · `2D`</sub> | Qwen3-VL trained with multi-turn RL to choose positive/negative points, boxes or an early stop for a medical segmenter; ships inference scripts and an RL recipe. | `Early`<br>2026-11-05 |
| **[MedSegAgent](https://github.com/uni-medical/MedSegAgent)**<br><sub>`Medical` · `Text` · `3D`</sub> | AutoGen pipeline that routes a free-text request to dataset-specific nnU-Net models and label IDs; a TotalSegAgent branch runs the segmentation and shows it in a viewer. | `Active`<br>2026-11-05 |
| **[SegAgent](https://github.com/aim-uofa/SegAgent)** · [paper](https://arxiv.org/abs/2503.08625)<br><sub>`Natural images` · `Text` `Interactive` · `2D`</sub> | MLLM trained to imitate annotator trajectories: it issues a sequence of interactions to an interactive segmentor and refines the mask; weights, code and HLMAT data are released. | `Maintained`<br>2026-11-05 |
| **[VoxelSage](https://github.com/ZJUMAI/VoxelSage)** · [paper](https://arxiv.org/abs/2609.37648)<br><sub>`Medical` · `Text` `Interactive` · `3D`</sub> | Self-hosted abdominal CT workspace where a language agent drives segmentation (VISTA3D or TotalSegmentator), measurements, key slices and 3D reconstruction through Skills. | `Early`<br>2026-11-05 |
| **[GenCellAgent](https://github.com/yuxi120407/GenCELLAgent)**<br><sub>`Microscopy` · `Text` `Interactive` · `2D`</sub> | Training-free router across Cellpose, µSAM, ERNet, MitoNet, LISA and SegGPT in a plan–execute–evaluate loop with VLM scoring, memory and human corrections. | `Early`<br>2026-11-05 |
| **[ask-to-mask](https://github.com/janelia-cellmap/ask-to-mask)**<br><sub>`Microscopy` · `Text` `Points` · `2D` `3D`</sub> | A VLM writes the prompt, a generator draws the mask and a VLM critic refines it; SAM 3 point prompts with majority voting over orthogonal planes produce 3D masks. | `Early`<br>2026-11-05 |
| **[FarmSeeker](https://github.com/WithoutOcean/FarmSeeker)**<br><sub>`Remote sensing` · `Text` `Masks` · `2D`</sub> | Detects ambiguous farmland, retrieves extra spatio-temporal imagery, reasons across dates and refines the mask with SAM 2.1; GSFS-Bench accompanies it. | `Early`<br>2026-11-05 |
| **[Refer-Agent](https://github.com/iSEE-Laboratory/Refer-Agent)** · [paper](https://arxiv.org/abs/2602.03595)<br><sub>`Video` · `Text` · `Video`</sub> | Reasoning and reflection agents build and check the target description before SAM 2 propagates masks through the video. | `Active`<br>2026-11-05 |
| **[Agentic-SAM](https://github.com/mdialameh/Agentic-SAM)**<br><sub>`Medical` · `Text` `Boxes` · `2D`</sub> | LangGraph tools over SAM 3, Medical-SAM3 and MedSAM2 for box-prompted PTMC segmentation, frame-by-frame RFA video tracking and live tracking notes. | `Early`<br>2026-11-05 |
| **[MMedAgent](https://github.com/Wangyixinxin/MMedAgent)** · [paper](https://aclanthology.org/2024.findings-emnlp.510/)<br><sub>`Medical` · `Text` `Boxes` · `2D`</sub> | Trained tool selector whose tools include MedSAM box prompts and Grounding DINO + MedSAM text prompts, alongside classification, VQA and report generation. | `Maintained`<br>2026-11-05 |
| **[Change-Agent](https://github.com/Chen-Yang-Liu/Change-Agent)** · [paper](https://ieeexplore.ieee.org/document/10591792)<br><sub>`Remote sensing` · `Text` · `2D`</sub> | Lagent agent that runs a multi-level change-interpretation model on bi-temporal images, returns change masks and descriptions, and answers follow-up questions. | `Maintained`<br>2026-11-05 |
| **[LORE](https://github.com/nourhanb/LORE-Interactive-Agentic-Segmentation-Framework-)**<br><sub>`Medical` · `Interactive` · `3D`</sub> | A policy observes the mask, error residuals and shape descriptors, then chooses the next correction (click, box, scribble) or stops; code released, weights and data not. | `Early`<br>2026-11-05 |

**Notes.** `Change-Agent` is the weakest fit here: its agent layer routes queries to a fixed interpretation model and does not inspect masks and retry. `MedSAM-Agent` has no root licence file, and its SFT/RL datasets are still listed as unreleased.

## Harnesses & Frameworks

Reusable execution machinery: planning, code generation and tests, presets, traces, budgets, retries and evaluation splits. A general framework is listed only when the repository shows a concrete segmentation integration.

| Project | What it provides | Status · verified |
| :--- | :--- | :--- |
| **[VisionAgent](https://github.com/landing-ai/vision-agent)**<br><sub>`Natural images` · `Text` · `2D`</sub> | Plans a vision task, generates Python that calls tools including SAM 2 instance segmentation and video tracking, tests the code and iterates; the repository description marks it deprecated. | `Deprecated`<br>2026-11-05 |
| **[agentic-segmentation](https://github.com/sameed-khan/agentic-segmentation)**<br><sub>`Medical` · `Interactive` · `3D`</sub> | A general coding agent drives nnInteractive through `seg_*` tools for 3D MRI tumours; versioned presets, per-run traces, evaluation splits and an experiment log. | `Early`<br>2026-11-05 |

**Notes.** `VisionAgent` is documented and its tool inventory is real, but new work should not start from a deprecated repository. The `agentic-segmentation` default branch is `integrate`, heavy run artifacts are tracked with DVC, and its README frames the work as an investigation rather than a product.

## Tools & Integrations

Backends, MCP servers, skills, plugins and fixed pipelines an agent can call. The host (who calls) and the backend (who computes) are the point of this section; a wrapper is not an agent.

| Project | What it provides | Status · verified |
| :--- | :--- | :--- |
| **[SAM 3](https://github.com/facebookresearch/sam3)**<br><sub>`Natural images` · `Text` `Points` `Boxes` · `2D`</sub> | Meta's promptable concept model, with a bundled agent package in which an MLLM calls `segment_phrase`, `examine_each_mask`, `select_masks` and `report_no_mask`. | `Active`<br>2026-11-05 |
| **[nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent)** · [paper](https://arxiv.org/abs/2610.31080)<br><sub>`Medical` `Microscopy` · `Interactive` · `3D`</sub> | MCP server plus agent skill: the host agent prompts nnInteractive with scribbles, boxes and points, inspects 3D renders, undoes and corrects. | `Active`<br>2026-11-05 |
| **[SAM 3 Segmentation Skill](https://github.com/lillyguisnet/sam3-segmentation)**<br><sub>`Natural images` · `Text` `Points` `Boxes` · `2D`</sub> | Skill wrapping SAM 3 in staged CLI commands — find, click, everything, then audit, select, review-sheets, refine and export — with reversible review decisions. | `Early`<br>2026-11-05 |
| **[ComfyUI Segmentation Agent](https://github.com/adambarbato/ComfyUI-Segmentation-Agent)**<br><sub>`Natural images` · `Text` · `2D`</sub> | ComfyUI node where a vision LLM splits a character description into SAM 3 phrases, inspects numbered mask candidates and accepts a subset. | `Early`<br>2026-11-05 |
| **[Grounded SAM 2](https://github.com/IDEA-Research/Grounded-SAM-2)**<br><sub>`Natural images` `Video` · `Text` · `2D` `Video`</sub> | Fixed Grounding DINO or Florence-2 → SAM 2 pipelines for open-vocabulary masks and video tracking; a backend, with no feedback loop. | `Maintained`<br>2026-11-05 |
| **[proofreader-mcp](https://github.com/janelia-cellmap/proofreader-mcp)**<br><sub>`Microscopy` · `No prompt` · `3D`</sub> | MCP server that ranks likely overmerge, oversegment, junk or misclassified objects for the host LLM and records human verdicts; it runs no model. | `Early`<br>2026-11-05 |
| **[gfm-mcp](https://github.com/yuyi1008688/gfm-mcp)**<br><sub>`Remote sensing` · `Text` · `2D`</sub> | MCP tools for geospatial foundation models: building and water segmentation, object and change detection, zero-shot classification and embeddings, on CPU. | `Early`<br>2026-11-05 |
| **[MCP-Slicer](https://github.com/zhaoyouj/mcp-slicer)**<br><sub>`Medical` · `No prompt` · `3D`</sub> | MCP server driving 3D Slicer: list MRML nodes, run Python in Slicer and capture slice and 3D screenshots to close a ReAct loop. | `Active`<br>2026-11-05 |
| **[BioImage-Agent](https://github.com/llnl/bioimage-agent)**<br><sub>`Microscopy` · `No prompt` · `2D`</sub> | napari plugin exposing the viewer over MCP so external agents can inspect images and call napari's public API from another process. | `Early`<br>2026-11-05 |
| **[MedMCP](https://github.com/medmcp/medmcp)**<br><sub>`Medical` · `Text` · `3D`</sub> | On-premise agentic workspace: a locally served model plans, installable tool stacks compute and a viewer shows segmentation overlays; data stays local by default. | `Active`<br>2026-11-05 |

**Notes.** `SAM 3` weights need Hugging Face access acceptance and the repository uses a custom Meta licence. `SAM 3 Segmentation Skill` was largely written by an AI, by the author's own statement. `ComfyUI Segmentation Agent` ships a test file that imports a class the repository does not define. `gfm-mcp` is GPL-3.0 and some embedding tools need a proxy for Google Earth Engine. `MedMCP` states it is not licensed for clinical use.

## Evaluation & Benchmarks

What is measured matters: a script that runs, a model judging its own mask and accuracy against human annotation are three different things.

| Benchmark | What it measures | Status · verified |
| :--- | :--- | :--- |
| **[BIABench](https://github.com/BIABench/BIABench)** · [paper](https://arxiv.org/abs/2609.34274)<br><sub>`Microscopy` · `Text` · `2D`</sub> | 16 real bioimage-analysis tasks reconstructed from published studies, scored on both the produced result and the analysis process, behind one `run(instruction, input_dir, output_dir)` interface. | `Active`<br>2026-11-05 |

**Benchmarks released inside listed projects** are cross-linked rather than duplicated as entries, because a project keeps one canonical row in this list.

| Benchmark | Hosted in | What it measures |
| :--- | :--- | :--- |
| [nnInteractive Agent benchmark](https://github.com/MIC-DKFZ/nninteractive-agent/blob/master/benchmark/README.md) | nnInteractive Agent | Mean Dice of Claude Code and Codex driving nnInteractive on 14 public CT, MRI, PET and micro-CT images and 51 targets. |
| [HLMAT evaluation](https://github.com/aim-uofa/SegAgent/blob/main/evaltools/eval.md) | SegAgent | Mask quality after human-like click trajectories, scored with the repository's IoU script. |
| [MSTT-199 and BEAMSTER splits](https://github.com/sameed-khan/agentic-segmentation/tree/integrate/eval) | agentic-segmentation | Coding-agent segmentation of soft-tissue tumours and brain metastases in 3D MRI, with per-run scores and trajectories. |
| [GSFS-Bench](https://github.com/WithoutOcean/FarmSeeker) | FarmSeeker | Farmland segmentation with reasoning-and-querying; dataset not yet released at verification time. |
| [MedSegAgent model-selection test set](https://github.com/uni-medical/MedSegAgent/blob/main/evaluate.py) | MedSegAgent | Dataset-level hit rate of the routing pipeline, not mask Dice. |

## Examples & Tutorials

Runnable walkthroughs. Each belongs to a project already listed above; it is a way in, not a separate project.

| Example | What you get | Source · verified |
| :--- | :--- | :--- |
| **[SAM 3 Agent notebook](https://github.com/facebookresearch/sam3/blob/main/examples/sam3_agent.ipynb)**<br><sub>`Natural images` · `Text` · `2D`</sub> | Official notebook: builds SAM 3, calls a vLLM-served Qwen3-VL, runs `run_single_image_inference` and saves the prediction, mask and agent history. | SAM 3<br>2026-11-05 |
| **[VASA demo and trace viewer](https://github.com/Wayne2Wang/VASA/tree/main/outputs)**<br><sub>`Natural images` · `Text` · `2D`</sub> | Three recorded queries; opening `trace.html` replays planning, tool calls and mask edits without running anything. | VASA<br>2026-11-05 |
| **[nnInteractive Agent web demo](https://github.com/MIC-DKFZ/nninteractive-agent#web-demo)**<br><sub>`Medical` · `Interactive` · `3D`</sub> | Browser chat over the same MCP tools and skill, with live 2D/3D views for people without an agent installed. | nnInteractive Agent<br>2026-11-05 |

## Papers & Surveys

Research that directly informs segmentation agents. Where a project already has a row above, its paper is linked from that row instead of appearing here again.

| Work | What it contributes | Status · verified |
| :--- | :--- | :--- |
| **[RSAgent](https://arxiv.org/abs/2512.24023)**<br><sub>`Natural images` · `Text` · `2D`</sub> | Agentic MLLM that queries a segmentation toolbox, observes visual feedback and revises its spatial hypothesis over multiple turns; no public code repository was found. | `Paper only`<br>2026-11-05 |
| **[RSure-Agent](https://github.com/AIRS101/RSure-Agent)** · [paper](https://arxiv.org/abs/2610.04836)<br><sub>`Remote sensing` · `Text` · `2D`</sub> | Remote-sensing agent that verifies tool observations before reusing them; the core tool-calling and verification code is still listed as unreleased. | `Paper only`<br>2026-11-05 |
| **[VoxelPrompt](https://arxiv.org/abs/2410.08397)**<br><sub>`Medical` · `Text` · `3D`</sub> | Vision-language agent that emits executable instructions to a frozen segmentation network for 3D medical images; no public code repository was found. | `Paper only`<br>2026-11-05 |
| **[SEER](https://github.com/Ztrura/SEER)** · [paper](https://arxiv.org/abs/2603.08215)<br><sub>`Medical` · `Text` · `3D`</sub> | Reasoning model that grounds clinical language and emits an executable target specification for a segmentation backbone; checkpoints, inference code and an evaluation split are released. | `Active`<br>2026-11-05 |

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

## Open questions

- **Independent evaluation.** BIABench is the only independent benchmark in this list; most evidence for the agent systems is author-run.
- **Industrial inspection.** No agentic segmentation system with an inspectable tool loop was verified for this domain, so the section is intentionally absent rather than filled.
- **Licences.** Not verified uniformly. Some repositories have a README that conflicts with their metadata, and some have no root licence file at all.
- **Runtime verification.** Nothing here was installed or run, so no row claims "works"; a passing script is not the same as a good mask.
- **Tool and skill evaluation.** The MCP servers and agent skills have little third-party evaluation; their evidence is what the authors report.
- **The agentic boundary.** Model-based interaction policies (LORE, SegAgent) sit close to the line; the three criteria in [Overview](#overview) are the tie-breaker.

## Contributing

The repository is private and not accepting outside contributions. Inclusion criteria, category rules, the table format, source requirements and the maintenance process are in [CONTRIBUTING.md](CONTRIBUTING.md); maintenance agents should read [AGENTS.md](AGENTS.md) first. In short: a row needs a canonical link, a role, one factual summary, a status, a verification date and an evidence URL in [data/resources.json](data/resources.json), and unknown things stay `unknown`.

## Usage notice

**No licence has been chosen for this list.** It is a private compilation; whether it becomes public, and under which licence, has not been decided, so do not redistribute or reuse it yet. Every linked project keeps its own licence, which the reader must check before use. No third-party README, image, dataset or code is copied here, and no weights or datasets are included.

Nothing here is medical, safety or security advice, and no entry has been clinically evaluated. Verification dates record a read-only check, not an endorsement.

---

**33 entries** · **5 embedded benchmarks** · **9 related resources** · verified 2026-11-05 · machine-readable records in [data/resources.json](data/resources.json) · selection notes and rejected candidates in [docs/research-notes.md](docs/research-notes.md)
