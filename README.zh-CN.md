# Awesome Agentic Segmentation（中文）

> 精选图像分割 Agent、运行框架、工具与相关资源。
>
> 覆盖任务规划、视觉工具调用、掩码检查与迭代改进，以及可复用的集成、评估与工作流，横跨多个影像领域。

**English: [README.md](README.md)**

本清单关注的是**真正会做分割这件事**的系统：它们会决定调用哪个工具、检查返回的掩码，并据此改变下一步动作。一个项目不会因为名字里有 "agent" 就被收录；收录依据是它的文档或代码里能看到「决策—工具调用—反馈」这条链路，或者它本身就是支撑这类系统运行的组件。

本清单**不是**分割模型、数据集或论文的大全。模型后端只有在 Agent 能调用它时才出现，普通模型统一放到 [Related Resources](#related-resources)（相关资源）。覆盖面上，本清单追求跨领域而非单领域深挖：自然图像、医学影像、遥感与显微成像均有条目；工业检测是目标领域，但目前还没有经过核验的条目，因此不摆空栏目。

**仓库状态**：私有、第一版、尚未选择开源许可证。下列每条都在 **2026-11-05** 通过阅读项目自身文档（部分条目另读源码）核验。核验过程中没有克隆、安装或运行任何项目，也没有下载模型权重。作者的声明按声明记录，不等同于本清单验证过的结果。收录标准、被排除的候选与未核验项见 [docs/research-notes.md](docs/research-notes.md)。

## 目录

- [从这里开始](#从这里开始)
- [Agents & Applications](#agents--applications)
- [Harnesses & Frameworks](#harnesses--frameworks)
- [Tools & Integrations](#tools--integrations)
- [Evaluation & Benchmarks](#evaluation--benchmarks)
- [Examples & Tutorials](#examples--tutorials)
- [Papers & Surveys](#papers--surveys)
- [Related Resources](#related-resources)
- [参与贡献](#参与贡献)
- [许可证与使用声明](#许可证与使用声明)

## 图例

标签是小规模受控词表，不是自由文本。每条从下列三组取值；当系统确实同时覆盖两种形态时（例如既有 2D 切片也有 3D 体数据），同一组可以出现两个值。

- **领域** —— `Natural images`（自然图像）、`Medical`（医学）、`Remote sensing`（遥感）、`Microscopy`（显微成像）、`Video`（视频）
- **提示形式** —— `Text`（文本）、`Points`（点）、`Boxes`（框）、`Masks`（掩码）、`Interactive`（交互）、`No prompt`（无提示）
- **维度** —— `2D`、`3D`、`Video`

状态含义：

| 状态 | 含义 |
| --- | --- |
| `Active` | 已核验代码与文档，项目当前看起来仍在开发且可用。 |
| `Maintained` | 可用且有文档，但核验前数月没有活动。 |
| `Early` | 产物存在，但明确不完整、属于研究原型，或缺少已发布的数据/权重。 |
| `Deprecated` | 作者已指向别处，不建议新项目使用。 |
| `Paper only` | 找到了论文，但没有公开代码，或代码明确未发布。 |
| `Unverified` | 本版未使用；留给完全无法核验的条目。 |

「核验日期」是最后一次只读检查的日期，不代表项目现在仍可运行，也不是安全性或临床性审查。

## 从这里开始

这个领域还很年轻，术语也不统一。三个可用的入口：

**1. 「用一句话描述我要分割的东西」。**
先看 [VASA](https://github.com/Wayne2Wang/VASA)，它维护一张工作掩码，通过规划、审视与错误恢复反复修改；或者看官方 [SAM 3 Agent notebook](https://github.com/facebookresearch/sam3/blob/main/examples/sam3_agent.ipynb)，它演示 MLLM 在有限轮数内调用 SAM 3 工具。两者都需要模型权重与 VLM 端点，都无法在普通笔记本 CPU 上跑。

**2. 「给我的编码 Agent 装上分割工具」。**
[nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent) 是本清单里最完整的例子：MCP 服务器、带修正手册的 skill、以 3D 渲染作为反馈，并附带 14 个体数据的 Agent 基准。二维照片方向，[SAM 3 Segmentation Skill](https://github.com/lillyguisnet/sam3-segmentation) 把复核表、可撤销决策与 COCO 导出打包成 skill。

**3. 「我想研究或自己搭 harness」。**
[agentic-segmentation harness](https://github.com/sameed-khan/agentic-segmentation) 记录了带版本的预设、逐次运行轨迹与评测划分；[BIABench](https://github.com/BIABench/BIABench) 对 16 个生物图像任务同时评结果与过程。看 [VisionAgent](https://github.com/landing-ai/vision-agent) 之前请先读[运行框架](#harnesses--frameworks)一节的说明：它文档完整，但仓库简介已标注 deprecated。

**如果只有十分钟**，先读[论文](#papers--surveys)一节里的四条 `Paper only`，再读[工具与集成](#tools--integrations)，它们说明了这个领域目前的两条路线：训练出来的 Agent 模型，或者「外部 Agent + MCP/Skill 工具」。

## Agents & Applications

*Agent 与应用：完成多步分割的完整系统。*

能完成多步分割的完整系统：决定下一步做什么、调用分割或编辑工具、查看结果、继续。每条都写明 Agent 决定什么、调用哪些工具、反馈来自哪里。

- **[VASA](https://github.com/Wayne2Wang/VASA)** — 免训练的视觉编排 Agent，用 VLM 协调 SAM 3 完成开放式即席分割：规划、掩码编辑、审视与错误恢复围绕一张可持续检查、可编辑的工作掩码展开，每次运行都保存 trace 查看器和工具调用历史。
  <sub>`Natural images` · `Text` · `2D` · 状态 `Early` · 核验 2026-11-05 · [论文](https://arxiv.org/abs/2605.19410)</sub>

- **[MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent)** — 用多轮强化学习训练的 Qwen3-VL Agent，为医学分割器（MedSAM2、SAM 2.1 或 IMISNet）选择正负点、边界框或提前停止，仓库提供单图与批量推理脚本以及 RL 训练配方。
  <sub>`Medical` · `Points` `Boxes` · `2D` · 状态 `Early` · 核验 2026-11-05 · [论文](https://arxiv.org/abs/2602.03320)</sub>

- **[MedSegAgent](https://github.com/uni-medical/MedSegAgent)** — 基于 AutoGen 的多智能体流水线，用由粗到细的查询过滤把自由文本的医学分割请求映射到具体数据集的 nnU-Net 模型与标签 ID；TotalSegAgent 分支另外提供可运行的 CT/MR 分割服务与网页查看器。
  <sub>`Medical` · `Text` · `3D` · 状态 `Active` · 核验 2026-11-05</sub>

- **[SegAgent](https://github.com/aim-uofa/SegAgent)** — 模仿人类标注轨迹训练的 MLLM：它向交互式分割器发出一系列交互动作，用多步构建并修整掩码；模型权重、推理代码与 HLMAT 轨迹数据集均已发布。
  <sub>`Natural images` · `Text` `Interactive` · `2D` · 状态 `Maintained` · 核验 2026-11-05 · [论文](https://arxiv.org/abs/2503.08625)</sub>

- **[VoxelSage](https://github.com/ZJUMAI/VoxelSage)** — 自托管的腹部 CT 工作台：自然语言 Agent 通过技能接口驱动分割（VISTA3D 或 TotalSegmentator）、定量测量、关键层面选择与交互式 3D 重建，并提供 Web 界面与 Skills API。
  <sub>`Medical` · `Text` `Interactive` · `3D` · 状态 `Early` · 核验 2026-11-05 · [论文](https://arxiv.org/abs/2609.37648)</sub>

- **[GenCellAgent](https://github.com/yuxi120407/GenCELLAgent)** — 面向细胞显微图像的免训练多智能体系统：按图像在 Cellpose、µSAM、ERNet、MitoNet、LISA、SegGPT 等专用或通用分割器之间路由，采用 plan–execute–evaluate 循环，并带 VLM 质量评分、人工修正与配置记忆。
  <sub>`Microscopy` · `Text` `Interactive` · `2D` · 状态 `Early` · 核验 2026-11-05</sub>

- **[ask-to-mask](https://github.com/janelia-cellmap/ask-to-mask)** — 电子显微镜细胞器分割，带 Agent 式精修闭环：视觉语言模型写提示词、生成器出掩码、VLM 评审再迭代；配合 SAM 3 点提示与正交平面多数投票得到 3D 掩码。
  <sub>`Microscopy` · `Text` `Points` · `2D` `3D` · 状态 `Early` · 核验 2026-11-05</sub>

- **[FarmSeeker](https://github.com/WithoutOcean/FarmSeeker)** — 遥感耕地分割 Agent：先找出含糊区域，再检索额外的时空影像、跨时相推理，并用 SAM 2.1 精修掩码；配套的 GSFS-Bench 被描述为支持「推理—查询」的全球尺度耕地分割基准。
  <sub>`Remote sensing` · `Text` `Masks` · `2D` · 状态 `Early` · 核验 2026-11-05</sub>

- **[Refer-Agent](https://github.com/iSEE-Laboratory/Refer-Agent)** — 指代视频目标分割的协作式多智能体系统：推理与反思阶段先构建并校验目标描述，再由 SAM 2 在视频中传播掩码。
  <sub>`Video` · `Text` · `Video` · 状态 `Active` · 核验 2026-11-05 · [论文](https://arxiv.org/abs/2602.03595)</sub>

- **[Agentic-SAM](https://github.com/mdialameh/Agentic-SAM)** — 本地超声助手：用 LangGraph 编排 SAM 3、Medical-SAM3 与 MedSAM2，按用户框分割 PTMC、在 RFA 视频中逐帧跟踪，并实时给出跟踪状态说明。
  <sub>`Medical` · `Text` `Boxes` · `2D` · 状态 `Early` · 核验 2026-11-05</sub>

- **[MMedAgent](https://github.com/Wangyixinxin/MMedAgent)** — 多模态医学 Agent，经训练学会选择并调用专用工具，包括 MedSAM 的框提示分割与 Grounding DINO + MedSAM 的文本提示分割，覆盖 MRI、CT、X 光、组织学与大体病理等模态。
  <sub>`Medical` · `Text` `Boxes` · `2D` · 状态 `Maintained` · 核验 2026-11-05 · [论文](https://aclanthology.org/2024.findings-emnlp.510/)</sub>

- **[Change-Agent](https://github.com/Chen-Yang-Liu/Change-Agent)** — 基于 Lagent 的双时相遥感 LLM Agent：调用多层级变化解译模型得到变化掩码与描述，再就变化回答后续问题。
  <sub>`Remote sensing` · `Text` · `2D` · 状态 `Maintained` · 核验 2026-11-05 · [论文](https://ieeexplore.ieee.org/document/10591792)</sub>

  <sub>说明：其 Agent 层是在固定变化解译模型之上的 LLM 工具路由，不会检查掩码再重试，因此比上面几条更弱地符合「Agent」标准。</sub>

- **[LORE](https://github.com/nourhanb/LORE-Interactive-Agentic-Segmentation-Framework-)** — 面向 3D 肿瘤分割的交互式 Agent 框架：策略网络观察当前掩码、误差残差与几何描述，决定请求哪种修正（点击、框、涂鸦）以及何时停止；已发布 Agent 代码，未发布数据与权重。
  <sub>`Medical` · `Interactive` · `3D` · 状态 `Early` · 核验 2026-11-05</sub>

## Harnesses & Frameworks

*运行框架：可复用的执行机制。*

可复用的执行机制：规划、工具编排、代码生成与测试、预算、轨迹、重试、带版本的预设、评测划分。通用 Agent 框架只有在仓库里能看到具体的分割集成时才收录——下面两条都满足。

- **[VisionAgent](https://github.com/landing-ai/vision-agent)** — 把视觉任务规划成计划、生成可运行的 Python 代码并调用大量工具（含基于 SAM 2 的实例分割与视频跟踪），随后执行测试并迭代直到通过；仓库简介现已标明该项目被 LandingAI 的 Agentic Document Extraction 取代（deprecated）。
  <sub>`Natural images` · `Text` · `2D` · 状态 `Deprecated` · 核验 2026-11-05</sub>

  <sub>说明：deprecated 写在 GitHub 仓库简介里，README 本身没有提。工具清单是真实的（`agentic_sam2_instance_segmentation`、`florence2_sam2_*`、`sam2` 等），但不建议在其上开展新工作。</sub>

- **[agentic-segmentation（编码 Agent harness）](https://github.com/sameed-khan/agentic-segmentation)** — 研究型 harness：通用编码 Agent 通过一组 `seg_*` 工具驱动 nnInteractive 完成 3D MRI 肿瘤分割；仓库包含带版本的 harness 预设、逐次运行记录、评测数据划分与可复现实验日志。
  <sub>`Medical` · `Interactive` · `3D` · 状态 `Early` · 核验 2026-11-05</sub>

  <sub>说明：默认分支是 `integrate`；较重的运行产物用 DVC 管理；README 把工作定位为「编码 Agent 能否驱动 3D 交互式分割工具」的调查研究，而不是产品。</sub>

## Tools & Integrations

*工具与集成：Agent 可以调用的后端、MCP、skill 与固定管线。*

Agent 可以调用的后端、MCP 服务器、skill、插件、适配器与固定管线。每条都说明宿主（谁调用）与后端（谁计算）。包装器不等于 Agent，本栏目也不作此暗示。

- **[SAM 3](https://github.com/facebookresearch/sam3)** — Meta 的可提示概念分割模型，随仓库提供推理与微调代码，并内置 Agent 包：多模态 LLM 在有限轮数内调用 `segment_phrase`、`examine_each_mask`、`select_masks`、`report_no_mask` 等工具。
  <sub>`Natural images` · `Text` `Points` `Boxes` · `2D` · 状态 `Active` · 核验 2026-11-05</sub>

  <sub>说明：权重需要接受 Hugging Face 访问条款；仓库使用 Meta 自定义许可证（GitHub 标记为 NOASSERTION）。</sub>

- **[nnInteractive Agent](https://github.com/MIC-DKFZ/nninteractive-agent)** — MCP 服务器加 Agent Skill：让宿主 Agent（Claude Code、Codex 或其他 MCP 客户端）用涂鸦、框和点提示 nnInteractive、查看 3D 渲染、撤销与修正；另附网页演示和 Agent 基准。
  <sub>`Medical` `Microscopy` · `Interactive` · `3D` · 状态 `Active` · 核验 2026-11-05 · [论文](https://arxiv.org/abs/2610.31080)</sub>

  <sub>说明：决策由宿主 Agent 做出；本包提供工具、带修正手册的 skill 与验证指引，并把 `python` 工具列为安全面，提供三档权限。</sub>

- **[SAM 3 Segmentation Skill](https://github.com/lillyguisnet/sam3-segmentation)** — 把 SAM 3 封装成分阶段 CLI 命令的 Agent Skill（`find`、`click`、`everything`，再到 `audit`、`select`、`review-sheets`、`refine`、`export`），让宿主 Agent 复核候选、记录可撤销决策并导出 PNG 或 COCO RLE 掩码。
  <sub>`Natural images` · `Text` `Points` `Boxes` · `2D` · 状态 `Early` · 核验 2026-11-05</sub>

  <sub>说明：需要 NVIDIA GPU 与已获授权的 SAM 3 访问；作者声明主要由 AI 编写、未经充分人工检查，且输出是候选而非已验证掩码。</sub>

- **[ComfyUI Segmentation Agent](https://github.com/adambarbato/ComfyUI-Segmentation-Agent)** — ComfyUI 节点：让视觉 LLM 把角色描述拆成若干 SAM 3 短语，把带编号的候选掩码回传模型，循环直到模型选定子集。
  <sub>`Natural images` · `Text` · `2D` · 状态 `Early` · 核验 2026-11-05</sub>

  <sub>说明：仓库中的测试文件引用了不存在的类，按现状发布的测试套件看起来是失效的。</sub>

- **[Grounded SAM 2](https://github.com/IDEA-Research/Grounded-SAM-2)** — 把 Grounding DINO 或 Florence-2 与 SAM 2 串起来的演示管线，用于开放词表图像掩码与视频目标跟踪；它是固定管线而非 Agent，但常被 Agent 系统当作分割后端。
  <sub>`Natural images` `Video` · `Text` · `2D` `Video` · 状态 `Maintained` · 核验 2026-11-05</sub>

  <sub>说明：没有反馈闭环——文本进检测器、框进 SAM 2、掩码返回。README 中部分功能标注为仍在开发。</sub>

- **[proofreader-mcp](https://github.com/janelia-cellmap/proofreader-mcp)** — 面向分割对象图像化校对的 MCP 服务器：把每个对象的截图作为资源，按可能出现过合并、过分割、垃圾或误分类的程度排序交给宿主 LLM 判断，并记录人工结论；自身不跑任何模型。
  <sub>`Microscopy` · `No prompt` · `3D` · 状态 `Early` · 核验 2026-11-05</sub>

- **[gfm-mcp](https://github.com/yuyi1008688/gfm-mcp)** — 把地理空间基础模型推理封装成 MCP 工具（建筑物提取、水体分割、目标检测、变化检测、零样本场景分类与嵌入），使 LLM Agent 能在 CPU 上调用遥感分割。
  <sub>`Remote sensing` · `Text` · `2D` · 状态 `Early` · 核验 2026-11-05</sub>

  <sub>说明：中文文档优先；GPL-3.0；部分嵌入工具需要代理访问 Google Earth Engine。</sub>

- **[MCP-Slicer](https://github.com/zhaoyouj/mcp-slicer)** — 让客户端操控 3D Slicer 的 MCP 服务器：列出 MRML 节点、在 Slicer 环境内执行 Python、截取切片与 3D 视图，为 ReAct 式循环提供视觉反馈。
  <sub>`Medical` · `No prompt` · `3D` · 状态 `Active` · 核验 2026-11-05</sub>

  <sub>说明：分割能力通过 Slicer 模块与 Python 工具触达，没有专门的分割工具。</sub>

- **[BioImage-Agent（napari MCP）](https://github.com/llnl/bioimage-agent)** — napari 插件，通过 socket 服务器把查看器以 MCP 暴露出去，让外部 Agent 能检查图像并从另一个进程调用 napari 的公共 API。
  <sub>`Microscopy` · `No prompt` · `2D` · 状态 `Early` · 核验 2026-11-05</sub>

  <sub>说明：只负责查看器控制；分割发生在 Agent 可能调用的其他 napari 插件里。</sub>

- **[MedMCP](https://github.com/medmcp/medmcp)** — 本地部署的医学影像 Agent 工作台：本地模型规划任务、可安装的工具栈执行计算、查看器显示图像与分割叠加结果；默认情况下数据不出本机。
  <sub>`Medical` · `Text` · `3D` · 状态 `Active` · 核验 2026-11-05</sub>

  <sub>说明：README 注明仍在积极开发，且未获临床使用许可。</sub>

## Evaluation & Benchmarks

*评测与基准：测的是什么。*

测的是什么很关键：脚本跑通、模型自评掩码、对照人工标注的准确率，是三件不同的事。本栏目每条都说明自己属于哪一种。

- **[BIABench](https://github.com/BIABench/BIABench)** — 包含 16 个源自已发表研究的真实生物图像分析任务的基准，同时给结果分与过程分；为 Claude Code、Codex、DeepSeek Harness 等编码 Agent 提供适配器，统一 `run(instruction, input_dir, output_dir)` 接口。
  <sub>`Microscopy` · `Text` · `2D` · 状态 `Active` · 核验 2026-11-05 · [论文](https://arxiv.org/abs/2609.34274)</sub>

  <sub>说明：任务中包含核分割；由于结果与过程分开计分，「跑通」本身不等于质量达标。</sub>

**已收录项目自带的基准**（交叉链接，不重复计为独立条目——一个项目在本清单中只保留一个主条目）：

- [nnInteractive Agent benchmark](https://github.com/MIC-DKFZ/nninteractive-agent/blob/master/benchmark/README.md)
  —— Claude Code 与 Codex 驱动 nnInteractive 在 14 个公开 CT、MRI、PET 与 micro-CT 影像、51 个目标上的平均 Dice，并对比单击提示与纯文本 3D 模型。
- [HLMAT 评测](https://github.com/aim-uofa/SegAgent/blob/main/evaltools/eval.md) —— 按类人点击轨迹得到的掩码质量，用仓库自带 IoU 脚本计算。
- [MSTT-199 与 BEAMSTER 划分](https://github.com/sameed-khan/agentic-segmentation/tree/integrate/eval)
  —— 编码 Agent 在 3D MRI 上分割软组织肿瘤与脑转移，附逐次得分与轨迹。
- [GSFS-Bench](https://github.com/WithoutOcean/FarmSeeker) —— 带推理—查询的耕地分割；核验时数据集尚未发布。
- [MedSegAgent 模型选择测试集](https://github.com/uni-medical/MedSegAgent/blob/main/evaluate.py)
  —— 路由流水线的数据集命中率，不是掩码 Dice。

## Examples & Tutorials

*示例与教程：上手入口。*

可照着跑的示例。每一条都属于上面已收录的项目，放在这里只是作为上手入口，不单独计为新项目。

- **[SAM 3 Agent notebook](https://github.com/facebookresearch/sam3/blob/main/examples/sam3_agent.ipynb)** — 官方 Notebook，端到端运行 SAM 3 Agent：构建 SAM 3、接入 vLLM 部署的 Qwen3-VL，对文本查询调用 `run_single_image_inference`，输出预测、渲染掩码与 Agent 历史。
  <sub>`Natural images` · `Text` · `2D` · 来自 SAM 3 · 核验 2026-11-05</sub>

- **[VASA 演示与 trace 查看器](https://github.com/Wayne2Wang/VASA/tree/main/outputs)** — 示例图片上的三条现成查询及录制结果；直接打开 `trace.html` 就能逐步回放规划、工具调用与掩码编辑，无需运行任何代码。
  <sub>`Natural images` · `Text` · `2D` · 来自 VASA · 核验 2026-11-05</sub>

- **[nnInteractive Agent 网页演示](https://github.com/MIC-DKFZ/nninteractive-agent#web-demo)** — 浏览器演示：把同一套 MCP 工具与 skill 放在聊天界面之后，配合实时 2D/3D 视图，向没有安装 Agent 的人展示 Agent 驱动的 3D 标注。
  <sub>`Medical` · `Interactive` · `3D` · 来自 nnInteractive Agent · 核验 2026-11-05</sub>

## Papers & Surveys

*论文：与分割 Agent 直接相关的研究。*

与分割 Agent 直接相关的研究。若项目已在上文有条目，论文链接并入该条目，不在此重复。以下每条都标明实际发布了什么。

- **[RSAgent](https://arxiv.org/abs/2512.24023)** — 面向文本引导分割的 Agent 式多模态 LLM：多轮调用分割工具箱、观察视觉反馈并修正空间假设；先冷启动 SFT 再做 Agent 强化学习。核验时未找到公开代码仓库。
  <sub>`Natural images` · `Text` · `2D` · 状态 `Paper only` · 核验 2026-11-05</sub>

- **[RSure-Agent](https://github.com/AIRS101/RSure-Agent)** — 遥感 Agent：在后续推理前先校验工具返回的观测，以减少误差传播。仓库已发布项目页、演示视频与论文，但核心工具调用与校验代码仍标注为未发布。
  <sub>`Remote sensing` · `Text` · `2D` · 状态 `Paper only` · 核验 2026-11-05 · [论文](https://arxiv.org/abs/2610.04836)</sub>

- **[VoxelPrompt](https://arxiv.org/abs/2410.08397)** — 面向 3D 医学影像的视觉语言 Agent：向冻结的分割网络输出可执行指令，端到端把语言提示落到体数据任务上。核验时未找到公开代码仓库。
  <sub>`Medical` · `Text` · `3D` · 状态 `Paper only` · 核验 2026-11-05</sub>

- **[SEER](https://github.com/Ztrura/SEER)** — 面向自由文本 3D 医学分割的视觉语言推理模型：把临床语言落到图像证据上，并输出可供分割骨干执行的目标规格；已发布权重、推理代码与评测划分。
  <sub>`Medical` · `Text` · `3D` · 状态 `Active` · 核验 2026-11-05 · [论文](https://arxiv.org/abs/2603.08215)</sub>

  <sub>说明：推理是单轮的——它产出规格而非与工具反复迭代，因此归为研究而非 Agent 系统。</sub>

## Related Resources

*相关资源：有用但不作为核心条目收录的链接。*

有用但不作为核心条目收录的链接：模型层、相邻的 Agent 方向，以及不按分割计分的基准。

- [awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) —— 传统的分割模型、数据集与工具索引；适合查阅本清单刻意不收的模型层。
- [Awesome-Segment-Anything](https://github.com/liliu-avril/Awesome-Segment-Anything) —— 可提示分割的论文汇总，含 SAM 系列与交互式分割工作。
- [awesome-medical-imaging-agents](https://github.com/Nanboy-Ronan/awesome-medical-imaging-agents) —— 医学影像 Agent 的广泛索引，设有分割与标注代理专节。
- [Awesome-Multimodal-Agent](https://github.com/OpenEnvision/Awesome-Multimodal-Agent) —— 多模态 Agent 论文汇总，与工具调用型分割 Agent 相邻。
- [SAM 2](https://github.com/facebookresearch/sam2) —— 可提示的图像与视频分割后端，上文多个 Agent 系统都在使用。
- [nnInteractive](https://github.com/MIC-DKFZ/nnInteractive) —— nnInteractive Agent 条目背后的 3D 交互式分割框架。
- [MedSAM2](https://github.com/bowang-lab/MedSAM2) —— 医学可提示分割与跟踪模型，被本清单中的医学 Agent 当作后端。
- [Seg-Zero](https://github.com/JIA-Lab-research/Seg-Zero) —— 带独立掩码解码器的推理链分割模型；没有工具调用闭环，因此仅作外链而非 Agent 收录。
- [ThinkGeo](https://github.com/mbzuai-oryx/ThinkGeo) —— 工具增强遥感 Agent 的基准；不按分割质量计分，因此仅作外链而非分割基准收录。

## 参与贡献

本仓库目前为私有，暂不接受外部贡献。收录标准、分类规则、条目格式、来源要求与维护流程见 [CONTRIBUTING.md](CONTRIBUTING.md)（英文）。要点是：每条必须有规范链接、分类、一句事实性描述、状态、核验日期与至少一条证据链接；结论必须来自项目自身仓库或论文并注明出处，不确定的内容保持 `unknown`。

维护 Agent 请先读 [AGENTS.md](AGENTS.md)。

## 许可证与使用声明

**本清单尚未选择开源许可证。** 当前仍处于私有整理阶段，是否公开以及采用何种许可证由所有者另行决定，目前尚未作出决定。在该决定公布前，请勿转载或复用本汇编。

本清单链接的每个项目仍适用其自身许可证，使用前请自行确认。条目描述是简短的事实性概括并附原始链接；本仓库没有整段搬运第三方 README、图片、数据集或代码。模型权重与数据集不包含在仓库内，且通常受各自条款限制。

本清单不构成医学、安全或合规建议，没有任何条目经过临床评估。核验日期记录的是一次只读检查，不代表背书。

---

共 **33 条**，分布于六个栏目；另有 **5 个**项目内基准与 **9 条**相关资源。最近一次核验：2026-11-05。结构化数据见 [data/resources.json](data/resources.json)；筛选依据、被排除的候选与待核验项见 [docs/research-notes.md](docs/research-notes.md)。
