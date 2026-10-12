# /code — 自动化与工具栈

本目录存放本项目用到的**所有可复用的代码、prompt、自动化工作流与数据**，按"X.com 自媒体运营"这一场景组织。

## 目录约定

| 子目录 | 用途 | 是否入库 |
| --- | --- | --- |
| `scripts/` | 一次性或周期性运行的 Python / Shell 脚本 | ✅（真实密钥用环境变量注入） |
| `prompts/` | 验证有效的 prompt 模板（一份 .md = 一份 prompt） | ✅ |
| `workflows/` | n8n / Make / Coze 工作流的 JSON 导出 | ✅ |
| `data/` | 抓回来的原始数据（trending、metrics、competitor） | ✅（CSV/JSON，已脱敏） |
| `AI-COLLAB-SOP.md` | AI 协作总 SOP（项目灵魂） | ✅ |
| `CONTENT-CALENDAR.md` | 选题 + 排程速查表 | ✅ |

## 真实密钥管理

**任何包含 API key / OAuth token / Stripe secret 的文件禁止入库。**
约定做法：

- 代码里用 `os.environ.get("X_API_KEY")` 读取。
- 本地密钥放 `~/.config/x-com-ai-builders/.env`（已加入 `.gitignore`）。
- 模板 `.env.example` 入库，仅占位。
- 共享给协作者时用 1Password / Bitwarden。

## 待建文件（M1 内补齐）

- [ ] `scripts/scrape_trending.py` — 抓 X trending hashtags + 对标账号最新高互动帖
- [ ] `scripts/weekly_metrics.py` — 每周日自动统计 impressions / engagement / followers
- [ ] `scripts/compliance_check.py` — 帖子合规自动检查（FTC、字符、敏感词）
- [ ] `prompts/cover-prompt.md` — 配图 prompt 模板
- [ ] `prompts/thread-outline.md` — 长 thread 大纲 prompt
- [ ] `prompts/native-rewrite.md` — AI 味 → native speaker 改写 prompt
- [ ] `workflows/weekly-report.json` — n8n 周报工作流

## 升级日志

- 2025-10-12：建立目录与 SOP 文档。
