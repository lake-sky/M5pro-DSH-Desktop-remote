# skills（全局技能）

本工作区（个人模型 use-person-model）的**工作方法技能库**：把实践中踩过的坑、验证有效的做法，沉淀成可复用的 skill，供后续会话直接遵循。

> 与 [creative-project/novelist/study/skills/](../creative-project/novelist/study/skills/) 的区别：那里是**内容**调研（研究别人写小说的 skill）；这里是**方法**沉淀（我自己该怎么干活）。

## 索引

| Skill | 作用 |
| --- | --- |
| [long-task-resilience/](long-task-resilience/SKILL.md) | 长任务与大输出韧性：避免模型流式超时、分段落盘、断点续做 |

## 约定

- 每个 skill 一个子目录，以 `SKILL.md` 作为入口文档（即该目录的 README）；格式遵循 Agent Skills 规范（frontmatter 含 `name` 与 `description`）。
- 事故案例与 skill 同目录，命名 `YYYY-MM-DD-<摘要>.md`，作为该 skill 的证据来源。
- 目录一律英文 kebab-case 命名，规则见 [根 README](../README.md)。
- 若后续接入用户级全局 skill 机制，本目录下的 `SKILL.md` 可直接注册引用（规范一致）。

## 现有技能速查

| 场景 | 用哪个 |
| --- | --- |
| 要写大文件（>4KB）或单轮输出很多内容 | `long-task-resilience` |
| 任务中途报错/超时后要接着干 | `long-task-resilience`（恢复流程） |
