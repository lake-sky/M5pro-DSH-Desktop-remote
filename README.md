# use-person-model 工作区

本工作区为个人模型（use-person-model）的工作目录：承载创意项目与技术类书籍项目，并沉淀工作方法技能。

## 目录索引

| 目录 | 说明 |
| --- | --- |
| [creative-project/](creative-project/) | 创意项目区（含 novelist/ 小说家工作区，详见其 README） |
| [tech-books-project/](tech-books-project/) | 技术类书籍项目区（含《从零构建语言模型》，详见其 README） |
| [skills/](skills/) | 全局技能库：把实践中验证有效的工作方法沉淀成可复用 skill（详见其 README） |

## 命名规则

- **从现在起，所有目录必须使用英文命名**，采用 kebab-case（小写字母 + 连字符，如 `creative-project`、`novelist`）。
- 文件名可随内容语言而定，但目录名一律为英文。
- 每个目录（包括工作区根目录）都必须维护一份 `README.md`，说明该目录的用途与索引信息；目录内容变化后请及时更新对应 README。
- 例外：`skills/` 下每个技能子目录以 `SKILL.md` 作为入口文档（遵循 Agent Skills 规范），它即该目录的 README 等价物。

## 版本控制

- 本工作区为 git 仓库，分支 `main`，远程仓库 `origin` → `git@github.com:lake-sky/M5pro-DSH-Desktop-remote.git`（SSH）。`.DS_Store` 等系统文件已被忽略。
- **规则：每次本地 `git commit` 之后，必须同步执行 `git push` 推送到远程**，保持本地与远程一致，不积压未推送的提交。
- 目录结构变更与内容更新请随手提交（并随之推送）。
- 注意：DSH 沙箱内的网络出口可能不通（GitHub 通道被拦截时推送会失败）。此时先完成本地提交，并请用户在普通终端执行 `git push -u origin main` 兜底。
