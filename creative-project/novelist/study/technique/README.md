# technique（技法）

写作手法的方法论库：把「怎么写得更好」变成**可执行的检查项**，而不是装饰性建议。

> **与相邻目录的分工**
> - [material/](../material/)（待建）存**原料**：场景、引文、轶事、灵感片段
> - `technique/`（本目录）存**做法**：结构、人物、对话、钩子、自查清单
> - [publishing/](../../publishing/) 存**发表规则**：平台、合同、合规——商业规则不进本目录

## 来源与许可

初稿蒸馏自三个 **MIT 许可**的开源项目（生态调研见 [../skills/](../skills/)）：

| 来源项目 | 许可 | 锁定版本（commit / 日期） | 本目录主要取用 |
| --- | --- | --- | --- |
| [chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill) | MIT | `cb6c3e7` / 2026-09-06 | 章节写法、钩子、情节结构、人物、对话、内容扩充 |
| [Novel-Control-Station-Skill](https://github.com/jingtai123/Novel-Control-Station-Skill) | MIT | `68d14aa` / 2026-03-29 | 基础文学原理、通俗小说共性规律、人物构造、对话规则 |
| [oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) | MIT | `87f2e7e` / 2026-10-03 | 去 AI 味 lint 清单 |

> **摘编纪律**：MIT 允许摘编与再分发，但必须**注明出处**。本目录只提炼**做法**，不整段搬运原文；具体条目注明来源。
> **版本锁定**：三仓库均为 2026-10-06 浅克隆（`--depth 1`），上表 commit 是本目录摘编所依据的版本。上游更新后若发现内容对不上，**先回退到该 commit 再核对**——这能排除大半「文档变了」的问题。

## 索引

| 文件 | 内容 |
| --- | --- |
| [principles.md](principles.md) | 地基：基础文学原理 10 条 + 通俗小说共性规律 10 条（含「拒绝信号」） |
| [chapter-craft.md](chapter-craft.md) | 章节写法：前 20% 决定生死、十种强力开头、**中文文学技法**、连贯性与新名词首现管理 |
| [hooks.md](hooks.md) | 钩子十三式 + 章首引子七式 + 五禁忌 + 强度分级 + 跨章悬念弧编排 |
| [plot-structures.md](plot-structures.md) | 情节结构：三幕 / 英雄之旅 / 类型结构 / 多线收敛 / 短篇快速结构 / 单章模板 |
| [character-and-dialogue.md](character-and-dialogue.md) | 人物构造（压力建模、五阶段弧光、漂移警报）+ 对话规则 |
| [stuck-and-expansion.md](stuck-and-expansion.md) | 卡文诊断 + 六个扩充技巧（子弹时间、内心展开、次要情节）+ 分题材富矿 |
| [ai-flavor-checklist.md](ai-flavor-checklist.md) | AI 味自查：10 种模式 + 四条核心规则 + 结尾/对话改写范例 |

> ★ [chapter-craft.md](chapter-craft.md) 的「中文文学技法」一节（白描 / 留白 / 意象营造 / 草蛇灰线 / 蒙太奇剪辑）与 [author-styles/](../author-styles/) 直接互补：**那边是「某位作家怎么用」，这边是「这些手法的操作要点」**。建议对照读。

## 使用方式

技法库**只有在写作时被调用才有价值**。建议三个调用点：

1. **动笔前**：用 `principles.md` 末尾的「拒绝信号」过一遍设定与大纲；
2. **每章写完**：用 `ai-flavor-checklist.md` 自查一遍；
3. **卡文时**：查 `stuck-and-expansion.md`。

## 命名规则

- 目录一律英文 kebab-case，规则见[根 README](../../../README.md)。
