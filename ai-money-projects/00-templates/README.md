# 00 — 项目模板库 (templates)

这里存放**所有项目都应复用的标准化模板**。新建项目时，把对应模板复制到项目目录、改名填字即可。

> 原则：**模板只为「过程记录」服务**。项目的最终产物（代码、内容、设计稿、课程包）放在项目目录的 `/code` 或 `/content` 子目录下，不属于模板范畴。

## 模板清单

| 文件 | 用途 | 对应阶段 |
| --- | --- | --- |
| [project-readme-template.md](project-readme-template.md) | 项目总览 README（必填） | 全周期 |
| [discovery-template.md](discovery-template.md) | 机会发现 | 立项前 |
| [research-template.md](research-template.md) | 调研 | 立项前 |
| [plan-template.md](plan-template.md) | 计划与里程碑 | 立项 |
| [build-template.md](build-template.md) | 研发流水账 | MVP 阶段 |
| [launch-template.md](launch-template.md) | 上线 Checklist | 发布前 1 周 |
| [operate-template.md](operate-template.md) | 运营与变现 | 上线后 |
| [review-template.md](review-template.md) | 复盘 | 项目结束 |

## 推荐工作流

1. **复制 `project-readme-template.md` → 项目目录 `README.md`**，先填好「状态、目标用户、价值主张、关键指标」四块。
2. 立项前依次完成 `01-discovery.md` `02-research.md` `03-plan.md`。
3. 开发期每天往 `04-build.md` 里追加 1 条（哪怕只写 3 行）。
4. 上线前过一遍 `05-launch.md` 的 Checklist。
5. 上线后每周更新 `06-operate.md`，每月汇总。
6. 项目结束 / 阶段切换时填 `07-review.md`，并把可复用方法抽到 `../../skills/`。

## 新建项目一键命令

```bash
# 在 ai-money-projects/<分类>/ 下创建新项目骨架
cd ai-money-projects
NEW=01-content-creation/your-project-name
mkdir -p "$NEW"/{assets,content}
cp 00-templates/project-readme-template.md "$NEW/README.md"
cp 00-templates/discovery-template.md  "$NEW/01-discovery.md"
cp 00-templates/research-template.md   "$NEW/02-research.md"
cp 00-templates/plan-template.md       "$NEW/03-plan.md"
cp 00-templates/build-template.md      "$NEW/04-build.md"
cp 00-templates/launch-template.md     "$NEW/05-launch.md"
cp 00-templates/operate-template.md    "$NEW/06-operate.md"
cp 00-templates/review-template.md     "$NEW/07-review.md"
```
