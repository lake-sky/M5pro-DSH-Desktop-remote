# skills（Skill 研究）

对开源社区「AI 写小说 skill」的调研区。记录生态背景、项目全景与深度剖析，并把其中有价值的方法论提炼进 study/ 的素材、技法、文法。

> 调研日期：2026-10-02。数据来源为 GitHub 公开仓库（README 与文件树），star 数会随时间变化，以链接为准。

## 索引

| 文件 | 内容 |
| --- | --- |
| [ecosystem.md](ecosystem.md) | Skill 概念与生态背景（Agent Skills 规范、skills.sh 目录、安装与宿主） |
| [projects.md](projects.md) | 写小说 skill 全景：16 个公开项目一览表（按类别分组） |
| [deep-dives.md](deep-dives.md) | 7 个重点项目深度剖析（架构、机制、关键文件） |
| [takeaways.md](takeaways.md) | 十条共性模式 + 对我们 novelist/study 的启示与行动项 |

## 快速结论

- 写小说 skill 的主战场是**长篇网文连载**，核心痛点是**连续性**：人设漂移、伏笔遗忘、文风同质化、越写越像评论文。
- 成熟项目收敛到同一套机制：**文档驱动（文件系统当记忆）+ 流程门禁 + 动态状态回写 + 去 AI 味 + 拆文库/语料检索**。
- 最热门是 [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode)（约 7.2k star），覆盖扫榜→拆文→写作→去 AI 味→封面的全流程，且有 DeepSeek Harness 社区插件版（oh-story-dsh）。
- 另一派是「陪练」定位（如 novel-harness）：主张 AI 现阶段不宜直出正文，人负责定稿。
- 对我们最有用的不是照搬 skill，而是把它们的**方法论文档**（写作指南、名家规律、去 AI 味规则）消化进 `technique/` 与 `author-styles/`。

## 命名规则

- 目录一律英文 kebab-case 命名，规则见 [根 README](../../README.md)。
