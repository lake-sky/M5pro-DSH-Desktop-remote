# 写小说 Skill 项目全景

> 调研日期：2026-10-02。star 数为当日快照。搜索口径：GitHub 仓库名/描述含 novel + skill，按 star 排序取前 18；同类另补若干。

## 1. 全流程写作 skill 包（直接产出正文/整本书）

| 项目 | star | 创建 | 定位 | 特点速览 |
| --- | --- | --- | --- | --- |
| [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) | 7200 | 2026-04 | 网文全流程 skill 包（MIT） | 扫榜→拆文→写作→去AI味→封面，13 个 skill；文件系统当记忆；7 Agent + 8 hook；支持 8 款 Agent；姊妹项目见 §5 |
| [PenglongHuang/chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill) | 3268 | 2026-01 | 从零生成 10–50 章完整中文小说（MIT） | 三层递进问答、偏好记忆、中断续写、三种写作模式、自动校验重写 |
| [alfredxw/denova](https://github.com/alfredxw/denova) | 850 | 2026-05 | 小说写作 + AI RPG 一体化平台（Apache-2.0，Go/Node 桌面端） | 内置 Agents + Skills + SubAgent 协作 + 版本管理 + 图像生成；写作/游戏双入口 |
| [Tomsawyerhu/Chinese-WebNovel-Skill](https://github.com/Tomsawyerhu/Chinese-WebNovel-Skill) | 833 | 2026-04 | 中文网文写作 skill（Codex 为主） | 主 skill 路由 + 10 个专项模块 + 本地语料检索，模块化设计最典型 |
| [zenstory-ai/novel-to-game](https://github.com/zenstory-ai/novel-to-game) | 820 | 2026-07 | 小说改编游戏（source-grounded） | 引用式设计文档 + 可运行构建 + 证据化 QA，3 个浏览器可玩示例 |
| [leenbj/novel-creator-skill](https://github.com/leenbj/novel-creator-skill) | 661 | 2026-02 | AI 长篇小说创作系统 | 文件级长期记忆的 Smart State 模式，主打百万字级持续创作 |
| [Shanyin-ai/Story-to-game](https://github.com/Shanyin-ai/Story-to-game) | 460 | 2026-05 | 分支叙事游戏工具包 | HTML 交互故事启动器 + 小说/剧本/大纲转可玩 JSON 的 skill |
| [jingtai123/Novel-Control-Station-Skill](https://github.com/jingtai123/Novel-Control-Station-Skill) | 416 | 2026-03 | 中文长篇「创作控制中枢」（MIT） | 文档驱动 + 连续性引擎；12 件真值文档；疯狂创作模式；起点有实际连载 |
| [wordflowlab/novel-writer-skills](https://github.com/wordflowlab/novel-writer-skills) | 262 | 2025-10 | skill + slash command 写小说探索 | 较早的形态实验 |
| [lornshrimp/Lorn.NovelWriteSkills](https://github.com/lornshrimp/Lorn.NovelWriteSkills) | 224 | 2026-04 | 长篇网文 AI 写作资产库 | 题材设计→大纲→章节→审阅润色→多平台改写→质量门禁→分发落盘 |
| [FlickeringLamp/ai-novelist](https://github.com/FlickeringLamp/ai-novelist) | 224 | 2025-06 | AI 写作 vibe coding 尝试 | function calling + RAG + MCP + skills + 人在回路，「小 cursor」式 |
| [dama-cyber/Distilled-Novel-Toolbox](https://github.com/dama-cyber/Distilled-Novel-Toolbox) | 192 | 2026-05 | 小说写作 skills 工具箱 | 「蒸馏」型工具集 |
| [Supreme-Ultimate/novel-to-script-team](https://github.com/Supreme-Ultimate/novel-to-script-team) | 174 | 2026-03 | 小说改编影视流水线 | 多 Agent 多 Skill 完整流水线 |
| [zy-zmc/tianming-skill](https://github.com/zy-zmc/tianming-skill) | 150 | 2026-05 | 「天命」AI 长篇小说协同创作 | 模块化提示词工程系统 |
| [jiaw-Zh/long-novel-writer](https://github.com/jiaw-Zh/long-novel-writer) | 91 | 2026-05 | 长篇小说生成 SKILL | 用 codex 蒸馏自 AI_NovelGenerator，优化记忆系统 |

## 2. 陪练 / 工作台型（人主导，AI 辅助）

| 项目 | star | 创建 | 定位 | 特点速览 |
| --- | --- | --- | --- | --- |
| [manhai934/novel-harness](https://github.com/manhai934/novel-harness) | 129 | 2026-05 | AI 写作「灵感陪练」 | 明确反对 AI 直出；空瓶分块陪写 + 审稿 + RAG 知识包 + Studio 网页工作台 + 多专项 Agent |
| [cheyann4399/padwriter](https://github.com/cheyann4399/padwriter) | 98 | 2026-05 | 节拍写作双端落地 | 安卓语音写作 App + novel-manager skill 共用「节拍器理论」；人设/世界观/节拍索引 agent 自动维护 |

## 3. 相邻品类（改编 / 视频化）

| 项目 | star | 创建 | 说明 |
| --- | --- | --- | --- |
| [woyin2024/lengyi-seedance2.5-prompt](https://github.com/woyin2024/lengyi-seedance2.5-prompt) | 109 | 2026-07 | 把想法/小说片段变成 30 秒影片的提示词 skill（Seedance 2.5） |

## 4. 观察

1. **时间线**：最早的写作 skill 出现在 2025 年中（FlickeringLamp 2025-06、wordflowlab 2025-10），2026 年 1–5 月集中爆发，与 Agent Skills 规范普及、中文网文 AI 写作讨论（知乎/贴吧/linux.do）互相助推。
2. **分化**：一派追求「全自动跑完整本」（oh-story、Control-Station、chinese-novelist），一派回归「人是作者」陪练定位（novel-harness）。前者上限高、返工风险大；后者落地稳、依赖人的投入。
3. **平台外溢**：写作 → 短剧 → 游戏 → 视频解说的改编链已经成体系（zenstory-ai 一个组织就覆盖了四条线）。
4. **star 与质量不能画等号**：高 star 多来自传播与完整度，方法论深度反而要看 references/ 文档。下文深度剖析按「机制可借鉴性」选项目，不完全按 star。
