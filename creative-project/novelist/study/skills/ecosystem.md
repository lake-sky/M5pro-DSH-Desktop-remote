# Skill 概念与生态背景

> 调研日期：2026-10-02

## 1. 什么是 Agent Skill

「Skill（技能）」是给 AI Agent 的可复用能力单元，2025 年 10 月由 Anthropic 正式推出「Agent Skills」规范后迅速成为生态标准。一个 skill 通常是一个文件夹：

```text
my-skill/
├── SKILL.md          # 入口：frontmatter（name、description）+ 核心指令
├── references/       # 按需加载的参考资料（不占常驻上下文）
├── scripts/          # 确定性脚本（检查、统计、检索）
└── assets/           # 模板、样例等静态资源
```

关键设计思想：

- **渐进式加载（progressive disclosure）**：Agent 平时只看得到 `name` + `description`；任务匹配时才读 SKILL.md 正文；更深资料按需读 references/。上下文不被撑爆，这是所有成熟写作 skill 的共同底座。
- **确定性脚本兜底**：能用脚本判断的（字数、句式、结构）不交给模型猜，模型负责创作与读感判断。
- **一句话安装**：`npx skills add <owner/repo>`，或直接对 Agent 说「安装这个 skill https://github.com/...」。

## 2. skills.sh：公共技能目录

Vercel 运营的 [skills.sh](https://www.skills.sh) 是目前最大的公开 Agent Skills 目录，自称「The Open Agent Skills Ecosystem」：

- 安装方式统一为 `npx skills add <owner/repo>`。
- 支持的宿主 Agent 20 余个：Claude Code、Cursor、Codex、GitHub Copilot、Windsurf、Gemini、Cline、OpenCode、Zed、Roo、Kilo、Trae、Goose 等。
- 截至调研日，累计安装量约 154 万（All Time 榜单）。
- 榜首技能以**编程类**为主：`find-skills`（vercel-labs，370 万安装）、`grill-me` / `tdd` / `improve-codebase-architecture`（mattpocock）、`frontend-design`（anthropics 官方）、`video-edit` 等。
- 写作 / 创意类是其中的垂直品类，中文网文写作是 2026 年增长最快的分支之一。

## 3. 写小说 skill 在生态中的位置

- GitHub 上检索「novel + skill」可匹配 **726 个仓库**（2026-10 调研日），其中中文名网文写作类占多数。
- 宿主普遍多平台：Claude Code、Codex CLI、OpenCode、Cursor、Google Antigravity、Cline，以及通用 Web AI。
- 与写作 skill 相邻的品类：短剧/剧本（drama-skills）、小说改编游戏（novel-to-game）、小说改编视频解说、提示词转影片。
- 与 DeepSeek Harness 相关：zenstory-ai 组织提供 **oh-story-dsh**（DSH 社区插件，小说/短剧/游戏/视频解说工作台），可在本环境内直接体验其流程。

## 4. 为什么写作社区偏爱 skill 形态

| 需求 | skill 形态的对应 |
| --- | --- |
| 方法论很多（视角、对话、节奏、钩子……） | references/ 分文件按需加载 |
| 长篇上下文撑不住 | 文件当记忆 + 状态卡只读关键 |
| 质量要求可验证 | scripts/ 做确定性检查 |
| 作者各有习惯 | 偏好记忆文件跨会话学习 |
| 想跨工具用 | 同一份 skill 装进多个 Agent |

一句话：**skill 把「写作方法论」从聊天记录里解放出来，变成了可维护、可检索、可复用的资产**——这正是我们 study/ 目录要做的事，方向一致。
