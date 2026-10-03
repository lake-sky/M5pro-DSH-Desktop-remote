# 重点项目深度剖析

从 16+ 个公开项目中，按「机制可借鉴性」（而非 star 数）选出 7 个做深度剖析。材料来源为各仓库 README 与文件树，调研日期 2026-10-02。

## 对比总览

| 项目 | 定位 | 记忆机制 | 质量门禁 | 人机分工 |
| --- | --- | --- | --- | --- |
| oh-story | 网文全流程 skill 包（13 skill） | 文件系统 + `_tracking-state.json` 唯一真相 | 缺细纲拦截、句式 lint、字数口径 | AI 主导，人确认方向 |
| chinese-novelist | 从零生成整本小说 | 大纲/人物档案/写作计划 JSON + 偏好记忆 | 字数与连贯性自动校验，最多 3 轮重写 | AI 全自动，人做问答确认 |
| Chinese-WebNovel-Skill | 模块化写作 skill | 主 SKILL.md 路由 + 专项模块 + 本地语料 | 每章完稿必经 consistency_review | AI 主导，人给简介 |
| Novel-Control-Station | 长篇创作控制中枢 | 12 件文档真值层 + 动态状态回写 | 章节控制卡、审计日志、修订链 | AI 控盘，人定方向与结局 |
| novel-harness | 灵感陪练（反对直出） | RAG 知识包 + 项目文档 | 审稿 Agent + 去 AI 化模块 | 人主导，AI 陪练 |
| denova | 写作 + 游戏一体化平台 | 本地版本管理 + 资料库 | Agent 变更审阅可回滚 | 人主导，AI 助手 |
| padwriter | 节拍写作双端落地 | 节拍索引 + 人设/世界观文档 | 节拍对齐 | 人写，agent 维护后台资料 |

## 1. zenstory-ai/oh-story-claudecode（约 7.2k star）

**定位**：面向中文网文的 skill 包，把「扫榜选材 → 拆解爆款 → 搭大纲写正文 → 去 AI 味 → 生成封面」装进你正在用的编程 Agent。

**核心机制**：

- 13 个 skill 分工：`story-setup`（环境部署）、`story`（路由与作者习惯）、`story-long-write` / `story-short-write`（长/短篇写作）、`story-deslop`（去 AI 味）、`story-long-analyze` / `story-short-analyze`（拆文）、`story-long-scan` / `story-short-scan`（扫榜）、`story-import`（旧稿逆向导入）、`story-review`（多视角审稿）、`story-cover`（封面）、`browser-cdp`（浏览器抓数据）。
- 三层架构：① **文件系统当记忆**——设定、大纲、正文、追踪各自独立目录，对话只负责创作不负责记忆；② **7 个专业 Agent 分工**——story-architect（架构）、narrative-writer（正文）、consistency-checker（一致性）、character-designer、story-researcher、story-explorer、chapter-extractor；③ **8 个自动化 hook**，其中只有 `guard-outline-before-prose.sh` 是阻断性的：缺对应细纲就阻止创建正文。
- **续写状态卡**（`追踪/上下文.md`）：固定 7 栏、硬上限 12KB、不进正文 prompt，下一章只读这一份，压缩上下文也不丢伏笔。
- **「作者真相 / 读者已知」分开记账**——角色提前知道答案、伏笔写飞的主要来源被单列管理。
- **伏笔账本**带编号与优先级，如 `F016｜钟嘉嘉并非普通军报实习生…｜埋第7章｜回收章未定｜高`。
- 去 AI 味是**确定性 lint**：逐条匹配已知句式，命中的模式包括 `em-dash`（破折号滥用）、`not-is-comparison`（不是A而是B）、`negation-parade`（没有X，没有X）、`voice-contrast`（声音不大，却）、`cliche-density-tic`（仿佛/一丝/缓缓/微微密度过高），给出文件行号与改写方向。
- 适配 8 款宿主：Claude Code、Codex CLI、Google Antigravity、OpenCode、ZCode、OpenClaw、Reasonix，以及能读项目文件的通用 Web AI。
- 安装：`npx skills add zenstory-ai/oh-story-claudecode -y -g`。

**关键文件 / 知识资产**：`skills/` 下 13 个 `SKILL.md`（含 `story-long-write`、`story-deslop` 等）；各 skill 的 `references/` 按需加载，合计 100+ 份写作方法论；`docs/` 收录架构、知识体系、去 AI 味具体做法；`demo/` 提供拆文报告、续写工程、去 AI 味对照与封面样例。

**对文学小说家的可借鉴点**：①「作者真相 / 读者已知」分账机制，直接对治叙述者知道太多、伏笔失控；②「固定栏位 + 硬上限」的续写状态卡，可套用于长篇人物与线索管理；③去 AI 味句式清单可直接当自查表用。

## 2. [PenglongHuang/chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill)（约 3.3k star）

**定位**：从零生成 10–50 章完整中文小说的单 skill，核心卖点是「让 AI 把整本写完」，解决写作者半途而废的痛点。

**核心机制**：

- **三层递进式问答**：Layer 1 核心定位必答 3 问（题材创意、主角设定、核心冲突），Layer 2 深度定制可选 5 问（世界观、叙事视角、核心主题、读者定位、章节数量）；每题支持随机生成或「跳过」。
- **偏好记忆**：`user-preferences.json` 跨会话记录题材类型、叙事风格、章节倾向、文字密度，下次直接套用。
- **中断续写**：Phase 0 自动检测未完成项目，从断点继续。
- **三种写作模式**：串行（主 Agent 逐章，默认）、子 Agent 并行（追速度）、Agent Teams（大型长篇）。
- **Phase 0–4 管线**：初始化 → 三层问答 → 规划确认（7 列章节规划 + 人物档案 + 写作计划 JSON）→ 疯狂创作（每章 3000–5000 字，写前分析→撰写→润色去 AI 味→字数检查→更新摘要）→ 自动校验（字数与连贯性，不合格最多重写 3 轮）。
- **内置指南 8 篇**：章节写作、悬念钩子（13 种结尾钩子类型）、人物塑造、对话写作、情节结构、内容扩充、大纲模板、人物档案模板。
- 四条核心法则：展示而非讲述、冲突驱动剧情、悬念承上启下、开头即高潮。

**关键文件 / 知识资产**：`SKILL.md`；`references/flows/` 7 篇流程文档（phase0–4 + shared-infrastructure）；`references/guides/` 8 篇写作指南；`scripts/check_chapter_wordcount.py` 字数校验脚本。

**对文学小说家的可借鉴点**：① 13 种结尾钩子类型清单值得归档进素材库；②「写前分析 → 撰写 → 润色 → 校验」的单章闭环可直接借用；③ 偏好记忆文件的做法适合记录自己的文风偏好。

## 3. [Tomsawyerhu/Chinese-WebNovel-Skill](https://github.com/Tomsawyerhu/Chinese-WebNovel-Skill)（约 833 star）

**定位**：面向中文网文写作的 Codex skill，形态不是「一份很长的总 prompt」，而是**主 skill 路由 + 专项模块下沉 + 本地语料检索**的模块化设计。

**核心机制**：

- **四层结构**：`SKILL.md` 只保留全局原则与模块路由；`references/modules/` 每个高频问题拆成独立模块；`data/` + `analysis/` 提供本地小说语料与检索索引；`scripts/` + `templates` 提供检索脚本与模板。
- **10 个专项模块**：`concept_planning`（把一句简介压成题材/消费点/hook/premise/故事引擎）、`opening`、`volume_outline`、`plot_logic`、`character_consistency`、`transition`、`dialogue`、`chapter_ending`、`anti_ai_voice`、`consistency_review`。
- **模块五件套**：每个模块统一为 `README.md` + `tutorial.md` + `runtime.md` + `good_examples.md` + `bad_examples.md` + `source_index.md`。
- **三条链**：前置规划链（concept_planning → opening / volume_outline）→ 正文执行链（plot_logic → character_consistency → transition → dialogue → chapter_ending → anti_ai_voice）→ 完稿收口链（consistency_review，每章默认必过）。
- **优先级次序明确**：`plot_logic` 与 `character_consistency` 偏底层，先修因果与人物；`anti_ai_voice` 最后介入，避免把结构问题误判成文风问题。
- **本地语料检索**：`python3 scripts/search_corpus_examples.py --type '开头钩子' --tag '危机压身' --limit 5`，先匹配素材、再构思、再写作。

**关键文件 / 知识资产**：`references/modules/`（10 个模块）；`data/articles/` 原始语料；`analysis/excerpts.csv` 结构化摘录 + `imitation_index.md` 模仿索引；`references/webnovel_corpus_guide.md` 检索说明。

**对文学小说家的可借鉴点**：①「主文件短而稳、知识下沉到模块」的组织方式，正是我们 study/ 目录可以照搬的结构；②每个模块配正例 + 反例 + 来源索引，比单纯攒技巧更利于写作时调用；③「先诊断问题层级，再调用对应材料」的排障顺序。

## 4. [jingtai123/Novel-Control-Station-Skill](https://github.com/jingtai123/Novel-Control-Station-Skill)（约 416 star）

**定位**：面向中文长篇小说的「创作控制中枢」，把一次性生成升级成可控、可追踪、可持续推进的创作系统。作者用它在起点写了实际连载作品，是有实战验证的项目。

**核心机制**：

- **开书访谈与方向对齐**：先锁定题材、受众、主角设定与核心性格、创作长度、结局倾向、风格方向；悬疑/历史/群像/多线等复杂类型会继续派生问题。
- **先设计后正文**：大纲 + 核心人物档案 + 多线结构关系 + 关键冲突与阶段目标，用户确认后才进入正文。
- **12 件文档真值层**：项目总览、主题命题、世界观、人物圣经、关系图谱、主情节线、伏笔账本、章节路线图、动态状态文件、风格指南、`chapters/`、`control-cards/`、写作日志。
- **每章 8 项动态状态回写**：关键事件、人物状态变化、关系变化、情节线推进、伏笔状态、世界规则变更、情绪债务与未兑现承诺、下一章承接压力。
- **图式回忆只作临时控制视图**：吸收图结构管理角色/事件/伏笔的思路，但不起第二套真相源，标准项目文件始终是唯一真值层。
- **章节控制卡 + 标题体系闭环**：动笔前先明确「本章必须改变什么、推进哪条线、回归哪个债务、冲突是什么、结尾留什么余波」；只把人物从 A 送到 B 的章节被判为结构性疲软。
- **7 个风格模块按需加载**：幽默、悬念、推理、爱情、恐怖、奇幻、文学，先读 `core.md`，真的需要才展开更深文档，支持主风格 + 辅助风格协同。
- **三步真实性修订**：去抽象套话与工整句式 → 压低过度专业词与分析腔 → 恢复具体细节、人物声音、中文语感。
- **marathon 疯狂创作模式**：读文档 → 生成控制卡 → 起草正文 → 逻辑校验与重写 → 更新动态状态 → 写审计日志 → 自动进入下一章；Windows 下用 `codex-continue-novel.ps1` 交接，并强制校验「真的写回文件」而不是只打印正文。

**关键文件 / 知识资产**：`references/` 下 20+ 篇方法论文档，包括 `foundational-literary-principles.md`（基础文学原理）、`popular-fiction-common-laws.md`（通俗小说共通规律）、`genre-benchmark-rules.md`（类型标杆规则）、`chapter-architecture-rules.md`、`character-construction-methods.md`、`dialogue-writing-rules.md`、`epoch-and-people-resonance.md` 等；`references/style-modules/` 风格模块库。

**对文学小说家的可借鉴点**：① `references/` 里那批方法论（文学原理、人物构造、对话规则）与商业套路相对独立，值得优先精读；②「情绪债务与未兑现承诺」这一栏提醒作者对读者的承诺要记账；③ 只写位移不写变化的章节自查法。

## 5. [manhai934/novel-harness](https://github.com/manhai934/novel-harness)（约 129 star）

**定位**：面向老书虫转作者与已有作者的 AI 小说创作**陪练**。作者明确表态：现阶段 AI 不适合直出内容，网上说能直出的都靠人工精修，所以项目定位是陪练而非代笔。

**核心机制**：

- **人机分工写死**：AI 负责激发灵感、拆解章节、提供写作支架、检查问题、管理长篇上下文；作者负责选择方向、完成表达、人工精修、最终定稿。
- **空瓶分块陪写**：把一章拆成一块块可手动填充的「空瓶」，帮看得多写得少的人跨过卡文；只有明确要求才生成完整正文，且统一视为「待人工精修粗稿」。
- **默认不给正文**：只说「帮我写小说」时先进入开书规划；准备写某章时默认返回分块写作指引。
- **RAG 参考检索**：随项目自带知识包在 `.harness/knowledge/included/`，市场下载的进 `.harness/knowledge/remote/`，本地建索引供 Agent 检索。
- **测试版知识包市场**：本地 MCP 暴露 `list_knowledge_packs`、`install_knowledge_pack`、`rebuild_rag_index` 等工具，云端已有创意规划、设定框架、正文润色、玄幻、世情、知乎短篇、规则怪谈等 10 个知识包。
- **Studio Dashboard**：本地 `127.0.0.1:8765` 网页工作台，管理小说/章节/大纲/设定，右侧可实时问「下一段往哪写」或拆写作块，正文不上传远端。
- **多专项 Agent + 去 AI 化模块**：总编/规划/写作/审稿分工；`human-linguistics` 模块把工整、解释感重的 AI 文风调成更接近真人网文的口气。

**关键文件 / 知识资产**：`docs/` 下设计原则、架构、Agent 体系、创作管线、知识包说明；`rag/` 检索与 MCP 服务；`studio/` 工作台；`.harness/knowledge/` 知识包目录。

**对文学小说家的可借鉴点**：① 它的核心主张（AI 陪练、人定稿）与文学写作的诉求最接近；②「空瓶分块」是治疗卡文的具体方法，值得单独归档进技法；③ 知识包 + RAG 的思路，可以用在我们自己的素材库检索上。

## 6. [alfredxw/denova](https://github.com/alfredxw/denova)（约 850 star）

**定位**：不是 skill 包，而是一体化 AI 创作平台（Go + Node 桌面应用，Apache-2.0）：小说写作与 AI 角色扮演游戏并列为一级入口，内置 AI Agents、Skills、SubAgent 协作、自动化、图像生成与项目版本管理。

**核心机制**：

- **写作 + 游戏双入口**：写作侧重构思、设定、大纲、章节与进度；游戏侧重玩家行动、剧情分支、角色状态与故事线推进；资料库、方案预设、Skills、版本管理两者共享。
- **创作 Agent**：支持 Native / Codex / Claude Code 三种运行时，能读取项目内容、调用工具、直接修改文件；支持多会话、SubAgent 协作、任务暂停恢复。
- **资料库 + 方案预设**：统一管理角色、地点、势力、世界规则与叙事风格，同一份设定同时服务写作与游戏。
- **写作功能完整**：Markdown 与源码编辑、多文档 Tab、查找替换、大纲与章节细纲、进度追踪、正文评论、修改审阅、现有小说导入。
- **版本与恢复**：本地版本保存、差异查看、历史恢复，并且 Agent 对工作区的修改可审阅、可撤销。
- **图像与自动化**：生成章节插画、互动图像、书籍封面；按计划运行审阅、续写等任务。
- **跨平台**：中英双语、明暗主题、Windows/macOS/Linux，支持局域网访问、手机自适应与 PWA。

**关键文件 / 知识资产**：`web/` 前端与 `img/` 界面样例；`CHANGELOG.md` 记录数据兼容说明；内置 Skills 目录与方案预设。

**对文学小说家的可借鉴点**：①「资料库（角色/地点/势力/世界规则/叙事风格）统一管理」正是长篇最需要的设定层；②「Agent 改动可审阅可回滚」的机制对写作项目很关键——AI 改稿必须可撤销；③ 版本保存 + 差异对比，适合存放多稿版本。

## 7. [cheyann4399/padwriter](https://github.com/cheyann4399/padwriter)（约 98 star）

**定位**：节拍写作方法论的双端落地——安卓端 PadWriter 语音写作 App 与 Claude Code 端 `novel-manager` skill 共用同一套「节拍器理论」。

**核心机制**：

- **节拍器创作方法论**：往收件箱丢想法 → 生成卷级梗概 → 按节拍写正文。
- **后台自动化**：人设、世界观、节拍索引全部由 agent 后台自动维护，作者只管推进节拍。
- **语音优先**：安卓 App 用悬浮球手势（长按录音、松开处理）把口述转成文字，支持原汁原味 / 正式得体 / 简洁精炼三种润色风格，以及三级文字注入策略（直接设置文本 → 剪贴板粘贴 → 模拟逐字输入）。

**关键文件 / 知识资产**：`.claude/skills/novel-manager/` 写作技能；Releases 提供 APK 安装包。

**对文学小说家的可借鉴点**：①「先丢想法进收件箱，再整理成梗概，再落到节拍」符合创作直觉，可作为素材收集流程；②「节拍」这一概念是控制节奏的可操作抓手，值得与我们的技法笔记对照。

---

## 小结

- 论机制完整度，**oh-story** 与 **Novel-Control-Station** 最值得精读，两者都把「连续性」当作工程问题解决。
- 论写作观，**novel-harness** 的「人是作者、AI 是陪练」对我们最有参考价值；其空瓶分块法可直接试用。
- 论组织方式，**Chinese-WebNovel-Skill** 的「短主文件 + 专项模块 + 正反例」最适合我们的 study/ 目录借鉴。
- 论设定管理，**denova** 的资料库与版本回滚机制值得在自己的写作项目里复刻（本工作区已有 git，天然满足版本要求）。
