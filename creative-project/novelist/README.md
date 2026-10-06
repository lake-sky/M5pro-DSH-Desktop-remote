# novelist（小说家）

小说家的工作区，存放小说作品及其大纲、人物设定等创作资料。

工作区按「向内 / 向外」两条线组织：**怎么写好**（`study/`）与**怎么发出去**（`publishing/`）。

## 索引

| 文件 / 目录 | 说明 |
| --- | --- |
| [works/](works/) | **作品区**：一部作品一个独立目录（含正文、大纲、人物、草稿、笔记与版本记录） |
| [study/](study/) | 研习区（向内）：素材、技法、古今著名作者的文法、类型史、AI 写小说 skill 调研 |
| [publishing/](publishing/) | 发表与运营（向外）：平台选择、签约条款、AI 合规、数据指标 |
| （内容添加后请在此登记） | |

## 现状提示

截至 2026-10-06：

| 线 | 状态 |
| --- | --- |
| **研究**（`study/`） | author-styles 10 位、technique 7 篇、sci-fi-history 3 篇、skills 调研 4 篇；`material/` 待建 |
| **发表**（`publishing/`） | 5 篇：平台矩阵、发表路径、合同要点、数据指标、AI 合规 |
| **创作**（`works/`） | 1 部作品（《三分钟》v0.1，约 900 字）← **这是最需要增长的数字** |

下一步的重点不是再加研究目录，而是**把 900 字变成一篇完整的短篇**（路径见 [publishing/strategy.md](publishing/strategy.md) 的阶段 0）。

## 命名规则

- 目录一律英文命名（kebab-case），规则见 [根 README](../README.md)。
- 每部作品统一放 `works/<类型>-<序号>-<英文短名>/`，作品内部再按 `outline.md` / `characters.md` / `chapters/` / `drafts/` / `notes.md` 组织。
- **不要把这些目录平铺在 `novelist/` 下**——多部作品会互相混淆，改稿也容易丢历史。完整约定与**版本规划**见 [works/README.md](works/README.md)。
