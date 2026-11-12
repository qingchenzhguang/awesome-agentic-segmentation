<h1 align="center">Awesome Agentic Segmentation</h1>

<p align="center">
  <img src="https://img.shields.io/badge/%E4%BB%93%E5%BA%93-private-6e7781" alt="私有仓库">
  <img src="https://img.shields.io/badge/%E6%9D%A1%E7%9B%AE-33-0969da" alt="33 条">
  <img src="https://img.shields.io/badge/%E6%A0%B8%E9%AA%8C-2026--11--05-1a7f37" alt="核验 2026-11-05">
  <img src="https://img.shields.io/badge/%E8%AE%B8%E5%8F%AF%E8%AF%81-%E6%9C%AA%E9%80%89%E6%8B%A9-bf8700" alt="未选择许可证">
</p>

<p align="center">
  <a href="#overview">概览</a> &nbsp;·&nbsp;
  <a href="#design-space">设计空间</a> &nbsp;·&nbsp;
  <a href="#browse">浏览</a> &nbsp;·&nbsp;
  <a href="#start-here">从这里开始</a> &nbsp;·&nbsp;
  <a href="#agents--applications">Agent</a> &nbsp;·&nbsp;
  <a href="#harnesses--frameworks">框架</a> &nbsp;·&nbsp;
  <a href="#tools--integrations">工具</a> &nbsp;·&nbsp;
  <a href="#evaluation--benchmarks">评测</a> &nbsp;·&nbsp;
  <a href="#examples--tutorials">示例</a> &nbsp;·&nbsp;
  <a href="#papers--surveys">论文</a> &nbsp;·&nbsp;
  <a href="#related-resources">相关</a> &nbsp;·&nbsp;
  <a href="#open-questions">待解问题</a> &nbsp;·&nbsp;
  <a href="#usage-notice">使用声明</a>
</p>

![Agent 规划分割任务、调用视觉工具、检查返回的掩码并据此决定下一步](assets/hero.svg)

*Agent 规划分割任务、调用视觉工具、检查返回的掩码，并把看到的结果带入下一步——本清单关注的正是这个闭环。*

English: [README.md](README.md)

## Overview

*概览：范围、边界与核验方式。*

精选图像分割 Agent、运行框架、工具与相关资源。覆盖任务规划、视觉工具调用、掩码检查与迭代改进，以及可复用的集成、评估与工作流。

一个项目要同时满足三点才算在范围内：Agent **做出决定**（选哪个工具、加什么提示、是否停止），它**调用**分割工具并拿到产物，这个产物**反馈**到下一步动作。名字里有 "agent" 不构成 Agent 的证据。

本清单**不是**分割模型、数据集或论文的大全。模型后端只有 Agent 能调用时才出现，普通模型统一放在[相关资源](#related-resources)。工业检测是目标领域，目前没有经核验的条目，因此不摆空栏目。

每条都在 **2026-11-05** 通过阅读项目自身文档（部分条目另读源码）核验；没有克隆、安装或运行任何项目，也没有下载权重。作者的声明按声明记录。仓库为私有、尚未选择开源许可证、暂不接受外部贡献。

## Design space

*设计空间：五维受控标签。*

每条在五个维度上打标签。标签是受控词表而非自由文本，随着清单增长仍能保持稳定。

| 维度 | 取值 |
| :--- | :--- |
| **角色** | Agent 与应用 · 运行框架 · 工具 / 集成 · 基准 · 示例 · 论文 |
| **领域** | 自然图像 · 医学 · 遥感 · 显微成像 · 视频 |
| **提示形式** | 文本 · 点 · 框 · 掩码 · 交互 · 无提示 |
| **维度** | 2D · 3D · 视频 |
| **状态** | Active · Maintained · Early · Deprecated · Paper only |

`Active` 表示当前仍在开发；`Maintained` 表示可用但已安静数月；`Early` 表示产物存在但不完整、属于研究原型，或缺数据/权重；`Deprecated` 表示作者已指向别处；`Paper only` 表示没有公开代码，或代码明确未发布。每行的日期是最后一次只读核验时间，不代表项目今天仍能运行。

## Browse

*浏览：按角色进入。*

| 角色 | 收录内容 | 条目数 |
| :--- | :--- | :---: |
| [Agents & Applications](#agents--applications) | 会规划、调用分割工具、检查掩码并迭代的完整系统 | 13 |
| [Harnesses & Frameworks](#harnesses--frameworks) | 执行循环、代码生成与测试、预设、轨迹、预算、评测划分 | 2 |
| [Tools & Integrations](#tools--integrations) | Agent 可调用的后端、MCP 服务器、skill、插件与固定管线 | 10 |
| [Evaluation & Benchmarks](#evaluation--benchmarks) | 评估分割 Agent 的基准，以及收录项目自带的基准 | 1 + 5 |
| [Examples & Tutorials](#examples--tutorials) | 属于已收录项目的可运行示例 | 3 |
| [Papers & Surveys](#papers--surveys) | 直接关于分割 Agent、工具使用与反馈的研究 | 4 |
| [Related Resources](#related-resources) | 模型层、相邻 Agent 方向与不按分割计分的基准 | 9 |

## Start here

*从这里开始：按需求选择入口。*

| 我想…… | 从这里看 | 为什么 |
| :--- | :--- | :--- |
| 用一句话描述要分割的东西 | [VASA](https://github.com/Wayne2Wang/VASA)、[SAM 3 Agent notebook](https://github.com/facebookresearch/sam3/blob/main/examples/sam3_agent.ipynb) | 一个维护可编辑的工作掩码并支持 trace 回放，一个是官方有限轮 SAM 3 工具循环。两者都需要权重与 VLM 端点。 |
| 给编码 Agent 装上分割工具 | [nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent)、[SAM 3 Segmentation Skill](https://github.com/lillyguisnet/sam3-segmentation) | 3D 方向是 MCP 服务器加修正 skill；2D 照片方向是带复核表的分阶段 CLI skill。 |
| 做 3D 医学标注 | [nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent)、[agentic-segmentation harness](https://github.com/sameed-khan/agentic-segmentation) | 一个是工具集加基准，一个是带数据划分与轨迹的编码 Agent harness。 |
| 把医学请求路由到正确模型 | [MedSegAgent](https://github.com/uni-medical/MedSegAgent)、[MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent) | 前者做数据集级模型与标签路由，后者是训练出来的提示选择 Agent。 |
| 走出自然图像 | [GenCellAgent](https://github.com/yuxi120407/GenCELLAgent)、[ask-to-mask](https://github.com/janelia-cellmap/ask-to-mask)、[FarmSeeker](https://github.com/WithoutOcean/FarmSeeker) | 显微图像工具路由、VLM 评审迭代、遥感检索加 SAM 2.1 精修。 |
| 研究或自建 harness | [agentic-segmentation harness](https://github.com/sameed-khan/agentic-segmentation)、[BIABench](https://github.com/BIABench/BIABench) | 一个提供带版本的预设与轨迹，一个用结果分加过程分评 16 个任务。 |

## Agents & Applications

*Agent 与应用：会规划、调用工具并迭代的完整系统。*

会决定下一步做什么、调用分割或编辑工具、查看结果并继续的完整系统。

| 项目 | 实际提供的能力 | 状态 · 核验 |
| :--- | :--- | :--- |
| **[VASA](https://github.com/Wayne2Wang/VASA)** · [论文](https://arxiv.org/abs/2605.19410)<br><sub>`Natural images` · `Text` · `2D`</sub> | VLM 用 SAM 3 规划、构建并编辑一张持久工作掩码，审视它并从错误中恢复；每次运行都保存 trace 查看器与工具调用历史。 | `Early`<br>2026-11-05 |
| **[MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent)** · [论文](https://arxiv.org/abs/2602.03320)<br><sub>`Medical` · `Points` `Boxes` · `2D`</sub> | 用多轮强化学习训练的 Qwen3-VL，为医学分割器选择正负点、框或提前停止；附推理脚本与 RL 配方。 | `Early`<br>2026-11-05 |
| **[MedSegAgent](https://github.com/uni-medical/MedSegAgent)**<br><sub>`Medical` · `Text` · `3D`</sub> | AutoGen 流水线把自由文本请求路由到具体数据集的 nnU-Net 模型与标签 ID；TotalSegAgent 分支可真正执行分割并在查看器中展示。 | `Active`<br>2026-11-05 |
| **[SegAgent](https://github.com/aim-uofa/SegAgent)** · [论文](https://arxiv.org/abs/2503.08625)<br><sub>`Natural images` · `Text` `Interactive` · `2D`</sub> | 模仿标注轨迹的 MLLM：向交互式分割器发出一系列交互动作并逐步修整掩码；权重、代码与 HLMAT 数据均已发布。 | `Maintained`<br>2026-11-05 |
| **[VoxelSage](https://github.com/ZJUMAI/VoxelSage)** · [论文](https://arxiv.org/abs/2609.37648)<br><sub>`Medical` · `Text` `Interactive` · `3D`</sub> | 自托管腹部 CT 工作台：语言 Agent 通过 Skills 驱动分割（VISTA3D 或 TotalSegmentator）、测量、关键层面与 3D 重建。 | `Early`<br>2026-11-05 |
| **[GenCellAgent](https://github.com/yuxi120407/GenCELLAgent)**<br><sub>`Microscopy` · `Text` `Interactive` · `2D`</sub> | 免训练路由：在 Cellpose、µSAM、ERNet、MitoNet、LISA、SegGPT 之间按 plan–execute–evaluate 循环选择，带 VLM 评分、记忆与人工修正。 | `Early`<br>2026-11-05 |
| **[ask-to-mask](https://github.com/janelia-cellmap/ask-to-mask)**<br><sub>`Microscopy` · `Text` `Points` · `2D` `3D`</sub> | VLM 写提示、生成器出掩码、VLM 评审再迭代；配合 SAM 3 点提示与正交平面多数投票得到 3D 掩码。 | `Early`<br>2026-11-05 |
| **[FarmSeeker](https://github.com/WithoutOcean/FarmSeeker)**<br><sub>`Remote sensing` · `Text` `Masks` · `2D`</sub> | 找出含糊的耕地，检索额外时空影像、跨时相推理，并用 SAM 2.1 精修掩码；配套 GSFS-Bench。 | `Early`<br>2026-11-05 |
| **[Refer-Agent](https://github.com/iSEE-Laboratory/Refer-Agent)** · [论文](https://arxiv.org/abs/2602.03595)<br><sub>`Video` · `Text` · `Video`</sub> | 推理与反思 Agent 先构建并校验目标描述，再由 SAM 2 在视频中传播掩码。 | `Active`<br>2026-11-05 |
| **[Agentic-SAM](https://github.com/mdialameh/Agentic-SAM)**<br><sub>`Medical` · `Text` `Boxes` · `2D`</sub> | 用 LangGraph 编排 SAM 3、Medical-SAM3 与 MedSAM2，按框分割 PTMC、在 RFA 视频中逐帧跟踪并实时给出跟踪说明。 | `Early`<br>2026-11-05 |
| **[MMedAgent](https://github.com/Wangyixinxin/MMedAgent)** · [论文](https://aclanthology.org/2024.findings-emnlp.510/)<br><sub>`Medical` · `Text` `Boxes` · `2D`</sub> | 训练出来的工具选择 Agent，工具含 MedSAM 框提示分割与 Grounding DINO + MedSAM 文本提示分割，另有分类、VQA 与报告生成。 | `Maintained`<br>2026-11-05 |
| **[Change-Agent](https://github.com/Chen-Yang-Liu/Change-Agent)** · [论文](https://ieeexplore.ieee.org/document/10591792)<br><sub>`Remote sensing` · `Text` · `2D`</sub> | 基于 Lagent 的 Agent：对双时相影像运行多层级变化解译模型，返回变化掩码与描述，并回答后续问题。 | `Maintained`<br>2026-11-05 |
| **[LORE](https://github.com/nourhanb/LORE-Interactive-Agentic-Segmentation-Framework-)**<br><sub>`Medical` · `Interactive` · `3D`</sub> | 策略网络观察掩码、误差残差与几何描述，决定下一次修正（点击、框、涂鸦）或停止；已发布代码，未发布权重与数据。 | `Early`<br>2026-11-05 |

**说明。** `Change-Agent` 是这里最弱的一条：Agent 层只是把查询路由到固定的解译模型，不会检查掩码再重试。`MedSAM-Agent` 根目录没有许可证文件，SFT/RL 数据集仍标注为未发布。

## Harnesses & Frameworks

*运行框架：可复用的执行机制。*

可复用的执行机制：规划、代码生成与测试、预设、轨迹、预算、重试与评测划分。通用框架只有在仓库中能看到具体分割集成时才收录。

| 项目 | 实际提供的能力 | 状态 · 核验 |
| :--- | :--- | :--- |
| **[VisionAgent](https://github.com/landing-ai/vision-agent)**<br><sub>`Natural images` · `Text` · `2D`</sub> | 规划视觉任务、生成调用工具（含基于 SAM 2 的实例分割与视频跟踪）的 Python、执行测试并迭代；仓库简介已标注 deprecated。 | `Deprecated`<br>2026-11-05 |
| **[agentic-segmentation](https://github.com/sameed-khan/agentic-segmentation)**<br><sub>`Medical` · `Interactive` · `3D`</sub> | 通用编码 Agent 通过 `seg_*` 工具驱动 nnInteractive 做 3D MRI 肿瘤分割；带版本的预设、逐次轨迹、评测划分与实验日志。 | `Early`<br>2026-11-05 |

**说明。** `VisionAgent` 文档完整、工具清单真实，但不建议在已废弃的仓库上开展新工作。`agentic-segmentation` 默认分支是 `integrate`，较重的运行产物用 DVC 管理，README 把工作定位为调查研究而非产品。

## Tools & Integrations

*工具与集成：Agent 可调用的后端与接口。*

Agent 可以调用的后端、MCP 服务器、skill、插件与固定管线。这一节的重点是宿主（谁调用）与后端（谁计算）；包装器不是 Agent。

| 项目 | 实际提供的能力 | 状态 · 核验 |
| :--- | :--- | :--- |
| **[SAM 3](https://github.com/facebookresearch/sam3)**<br><sub>`Natural images` · `Text` `Points` `Boxes` · `2D`</sub> | Meta 的可提示概念模型，内置 Agent 包：MLLM 调用 `segment_phrase`、`examine_each_mask`、`select_masks`、`report_no_mask`。 | `Active`<br>2026-11-05 |
| **[nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent)** · [论文](https://arxiv.org/abs/2610.31080)<br><sub>`Medical` `Microscopy` · `Interactive` · `3D`</sub> | MCP 服务器加 Agent Skill：宿主 Agent 用涂鸦、框和点提示 nnInteractive，查看 3D 渲染，撤销并修正。 | `Active`<br>2026-11-05 |
| **[SAM 3 Segmentation Skill](https://github.com/lillyguisnet/sam3-segmentation)**<br><sub>`Natural images` · `Text` `Points` `Boxes` · `2D`</sub> | 把 SAM 3 封装成分阶段 CLI 命令——find、click、everything，再到 audit、select、review-sheets、refine、export——决策可撤销。 | `Early`<br>2026-11-05 |
| **[ComfyUI Segmentation Agent](https://github.com/adambarbato/ComfyUI-Segmentation-Agent)**<br><sub>`Natural images` · `Text` · `2D`</sub> | ComfyUI 节点：视觉 LLM 把角色描述拆成 SAM 3 短语，检查带编号的候选掩码并选定子集。 | `Early`<br>2026-11-05 |
| **[Grounded SAM 2](https://github.com/IDEA-Research/Grounded-SAM-2)**<br><sub>`Natural images` `Video` · `Text` · `2D` `Video`</sub> | 固定的 Grounding DINO 或 Florence-2 → SAM 2 管线，用于开放词表掩码与视频跟踪；没有反馈闭环。 | `Maintained`<br>2026-11-05 |
| **[proofreader-mcp](https://github.com/janelia-cellmap/proofreader-mcp)**<br><sub>`Microscopy` · `No prompt` · `3D`</sub> | MCP 服务器：按过合并、过分割、垃圾或误分类的可能程度排序，交给宿主 LLM 判断并记录人工结论；自身不跑模型。 | `Early`<br>2026-11-05 |
| **[gfm-mcp](https://github.com/yuyi1008688/gfm-mcp)**<br><sub>`Remote sensing` · `Text` · `2D`</sub> | 地理空间基础模型的 MCP 工具：建筑与水体分割、目标与变化检测、零样本分类与嵌入，可在 CPU 上跑。 | `Early`<br>2026-11-05 |
| **[MCP-Slicer](https://github.com/zhaoyouj/mcp-slicer)**<br><sub>`Medical` · `No prompt` · `3D`</sub> | 驱动 3D Slicer 的 MCP 服务器：列出 MRML 节点、在 Slicer 内执行 Python、截取切片与 3D 截图以闭环。 | `Active`<br>2026-11-05 |
| **[BioImage-Agent](https://github.com/llnl/bioimage-agent)**<br><sub>`Microscopy` · `No prompt` · `2D`</sub> | napari 插件：通过 MCP 暴露查看器，让外部 Agent 检查图像并从另一个进程调用 napari 公共 API。 | `Early`<br>2026-11-05 |
| **[MedMCP](https://github.com/medmcp/medmcp)**<br><sub>`Medical` · `Text` · `3D`</sub> | 本地部署的 Agent 工作台：本地模型规划、可安装工具栈计算、查看器显示分割叠加；默认数据不出本机。 | `Active`<br>2026-11-05 |

**说明。** `SAM 3` 权重需接受 Hugging Face 条款，仓库使用 Meta 自定义许可证。`SAM 3 Segmentation Skill` 按作者自述主要由 AI 编写。`ComfyUI Segmentation Agent` 的测试文件导入了仓库里不存在的类。`gfm-mcp` 为 GPL-3.0，部分嵌入工具需要代理访问 Google Earth Engine。`MedMCP` 声明未获临床使用许可。

## Evaluation & Benchmarks

*评测与基准：结果分与过程分要分开看。*

测什么很关键：脚本跑通、模型自评掩码、对照人工标注的准确率，是三件不同的事。

| 基准 | 测什么 | 状态 · 核验 |
| :--- | :--- | :--- |
| **[BIABench](https://github.com/BIABench/BIABench)** · [论文](https://arxiv.org/abs/2609.34274)<br><sub>`Microscopy` · `Text` · `2D`</sub> | 16 个源自已发表研究的真实生物图像分析任务，同时评结果与过程，统一 `run(instruction, input_dir, output_dir)` 接口。 | `Active`<br>2026-11-05 |

**已收录项目自带的基准**以交叉链接呈现、不重复计为条目，因为一个项目在本清单中只保留一行。

| 基准 | 所属项目 | 测什么 |
| :--- | :--- | :--- |
| [nnInteractive Agent benchmark](https://github.com/MIC-DKFZ/nninteractive-agent/blob/master/benchmark/README.md) | nnInteractive Agent | Claude Code 与 Codex 驱动 nnInteractive 在 14 个公开 CT、MRI、PET、micro-CT 影像、51 个目标上的平均 Dice。 |
| [HLMAT 评测](https://github.com/aim-uofa/SegAgent/blob/main/evaltools/eval.md) | SegAgent | 类人点击轨迹之后的掩码质量，用仓库自带 IoU 脚本计分。 |
| [MSTT-199 与 BEAMSTER 划分](https://github.com/sameed-khan/agentic-segmentation/tree/integrate/eval) | agentic-segmentation | 编码 Agent 在 3D MRI 上分割软组织肿瘤与脑转移，附逐次得分与轨迹。 |
| [GSFS-Bench](https://github.com/WithoutOcean/FarmSeeker) | FarmSeeker | 带推理—查询的耕地分割；核验时数据集尚未发布。 |
| [MedSegAgent 模型选择测试集](https://github.com/uni-medical/MedSegAgent/blob/main/evaluate.py) | MedSegAgent | 路由流水线的数据集命中率，不是掩码 Dice。 |

## Examples & Tutorials

*示例与教程：属于已收录项目的上手入口。*

可照着跑的示例。每条都属于上面已收录的项目，是上手入口，不是新项目。

| 示例 | 能得到什么 | 来源 · 核验 |
| :--- | :--- | :--- |
| **[SAM 3 Agent notebook](https://github.com/facebookresearch/sam3/blob/main/examples/sam3_agent.ipynb)**<br><sub>`Natural images` · `Text` · `2D`</sub> | 官方 Notebook：构建 SAM 3、接入 vLLM 部署的 Qwen3-VL、运行 `run_single_image_inference`，保存预测、掩码与 Agent 历史。 | SAM 3<br>2026-11-05 |
| **[VASA 演示与 trace 查看器](https://github.com/Wayne2Wang/VASA/tree/main/outputs)**<br><sub>`Natural images` · `Text` · `2D`</sub> | 三条已录制查询；打开 `trace.html` 即可回放规划、工具调用与掩码编辑，无需运行任何代码。 | VASA<br>2026-11-05 |
| **[nnInteractive Agent 网页演示](https://github.com/MIC-DKFZ/nninteractive-agent#web-demo)**<br><sub>`Medical` · `Interactive` · `3D`</sub> | 浏览器聊天界面套用同一套 MCP 工具与 skill，配合实时 2D/3D 视图，无需自备 Agent。 | nnInteractive Agent<br>2026-11-05 |

## Papers & Surveys

*论文：与分割 Agent 直接相关的研究。*

与分割 Agent 直接相关的研究。项目已在上文有行时，论文并入该行，不在此重复。

| 工作 | 贡献 | 状态 · 核验 |
| :--- | :--- | :--- |
| **[RSAgent](https://arxiv.org/abs/2512.24023)**<br><sub>`Natural images` · `Text` · `2D`</sub> | Agent 式 MLLM：多轮调用分割工具箱、观察视觉反馈并修正空间假设；核验时未找到公开代码仓库。 | `Paper only`<br>2026-11-05 |
| **[RSure-Agent](https://github.com/AIRS101/RSure-Agent)** · [论文](https://arxiv.org/abs/2610.04836)<br><sub>`Remote sensing` · `Text` · `2D`</sub> | 遥感 Agent：在复用工具观测前先校验，以减少误差传播；核心工具调用与校验代码仍标注为未发布。 | `Paper only`<br>2026-11-05 |
| **[VoxelPrompt](https://arxiv.org/abs/2410.08397)**<br><sub>`Medical` · `Text` · `3D`</sub> | 面向 3D 医学影像的视觉语言 Agent：向冻结的分割网络输出可执行指令；核验时未找到公开代码仓库。 | `Paper only`<br>2026-11-05 |
| **[SEER](https://github.com/Ztrura/SEER)** · [论文](https://arxiv.org/abs/2603.08215)<br><sub>`Medical` · `Text` · `3D`</sub> | 推理模型：把临床语言落到图像证据并输出可供分割骨干执行的目标规格；已发布权重、推理代码与评测划分。 | `Active`<br>2026-11-05 |

## Related Resources

*相关资源：有用但不在收录边界内。*

有用但不在收录边界内：模型层、相邻 Agent 方向，以及不按分割计分的基准。

| 资源 | 为什么外链 |
| :--- | :--- |
| [awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) | 传统的分割模型、数据集与工具索引——本清单刻意不收的模型层。 |
| [Awesome-Segment-Anything](https://github.com/liliu-avril/Awesome-Segment-Anything) | 可提示分割论文，含 SAM 系列与交互式分割。 |
| [awesome-medical-imaging-agents](https://github.com/Nanboy-Ronan/awesome-medical-imaging-agents) | 医学影像 Agent 的广泛索引，设有分割与标注专节。 |
| [Awesome-Multimodal-Agent](https://github.com/OpenEnvision/Awesome-Multimodal-Agent) | 多模态 Agent 论文，与工具调用型分割 Agent 相邻。 |
| [SAM 2](https://github.com/facebookresearch/sam2) | 可提示的图像与视频分割后端，上文多个系统在用。 |
| [nnInteractive](https://github.com/MIC-DKFZ/nnInteractive) | nnInteractive Agent 背后的 3D 交互式分割框架。 |
| [MedSAM2](https://github.com/bowang-lab/MedSAM2) | 医学可提示分割与跟踪模型，被上文医学 Agent 当作后端。 |
| [Seg-Zero](https://github.com/JIA-Lab-research/Seg-Zero) | 带独立掩码解码器的推理链分割；没有工具闭环，因此只作外链。 |
| [ThinkGeo](https://github.com/mbzuai-oryx/ThinkGeo) | 工具增强遥感 Agent 基准；不按分割质量计分。 |

## Open questions

*待解问题：仍未验证或仍缺证据的地方。*

- **独立评测。** BIABench 是本清单里唯一的独立基准；Agent 系统的证据大多由作者自己跑出。
- **工业检测。** 没有核验到具备可检查工具闭环的 Agent 系统，因此该栏目有意留空，而不是拿模型填充。
- **许可证。** 未逐项核验；有的仓库 README 与元数据冲突，有的根目录根本没有许可证文件。
- **运行验证。** 这里没有安装或运行任何项目，因此没有任何一行声称“可用”；脚本跑通不等于掩码质量好。
- **工具与 skill 评测。** MCP 服务器和 Agent skill 几乎没有第三方评测，证据来自作者自述。
- **Agent 的边界。** 基于模型的交互策略（LORE、SegAgent）贴近这条线；判断标准就是[概览](#overview)里的三条。

## Contributing

*参与贡献：私有阶段的收录与维护规则。*

仓库为私有、暂不接受外部贡献。收录标准、分类规则、表格格式、来源要求与维护流程见 [CONTRIBUTING.md](CONTRIBUTING.md)；维护 Agent 请先读 [AGENTS.md](AGENTS.md)。要点是：每行必须有规范链接、角色、一句事实性概述、状态、核验日期，以及 [data/resources.json](data/resources.json) 里的证据；不确定的内容保持 `unknown`。

## Usage notice

*使用声明：许可证与免责。*

**本清单尚未选择开源许可证。** 目前是私有汇编，是否公开、采用何种许可证均未决定，请勿转载或复用。每个被链接项目仍适用其自身许可证，使用前请自行确认。本仓库没有搬运第三方 README、图片、数据集或代码，也不包含权重与数据集。

本清单不构成医学、安全或合规建议，没有任何条目经过临床评估。核验日期记录的是一次只读检查，不是背书。

---

**33 条** · **5 个项目内基准** · **9 条相关资源** · 核验于 2026-11-05 · 结构化数据见 [data/resources.json](data/resources.json) · 筛选与被排除候选见 [docs/research-notes.md](docs/research-notes.md)
