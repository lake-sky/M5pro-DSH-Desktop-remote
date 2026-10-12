# x-com-ai-builders — 在 X.com 上以"AI Builder"人设做自媒体运营

> **状态**：💡 idea
> **所属分类**：[../../](../)
> **创建日期**：2025-10-12
> **最近更新**：2025-10-12
> **负责人**：自己（创作/审核） + DSH AI 助手（调研/草稿/数据/翻译）

## 一、目标用户

- **主要人群**：
  - **海外独立开发者 / 副业搞 SaaS 的人**（indie hackers、bootstrap founders）——他们天天刷 X 看 build-in-public、工具评测、AI 工作流。
  - **AI 重度用户 / 早期采用者**——产品经理、设计师、研究员，关注新模型/新工具的实操经验。
  - **中文区出海的 AI 创作者**——他们想了解 X 上什么内容能火、什么变现方式有效。
- **典型场景**：
  - 通勤时刷 X，看 1-2 条"AI + 实战"的短帖 → 收藏 → 点击主页。
  - 决定是否 follow / 订阅 newsletter。
  - 点进 affiliate 链接或 Gumroad 产品页下单。
- **痛点强度**：中度。X 上"AI 教学"内容已极度饱和，但**有真实 build-in-public 经验、且诚实不端**的账号依然稀缺；用户痛的是"看了 100 条都没看到真东西"。

## 二、价值主张

> 为 **想用 AI 工具做出可变现产品/内容的海外创作者**，
> 在 **X.com 这个公开、短平快、强算法的阵地** 上，
> 做 **"我用 AI 做了什么、赚了多少、踩了什么坑"** 的真实 build-in-public 连载，
> 从而获得 **关注者增长 → 联盟佣金/付费产品/咨询/SaaS 订阅** 的复利收益。

## 三、关键指标

- **北极星指标**：**过去 28 天从 X 引流到任意变现落地页（affiliate / Gumroad / 自建 SaaS）的净收入 USD**。
- **副指标 1**：followers 净增（按月，看势能）；目标 90 天破 1k、180 天破 5k。
- **副指标 2**：单帖平均 impressions 与"放大帖"（10k+ impressions）占比。
- **副指标 3**：每条长 thread 带来的 profile clicks、bookmark 率、follow 转化率。
- **副指标 4**（滞后）：置顶帖 / pinned newsletter 链接的 CTR。

## 四、技术/工具栈

- **AI 写作**：Claude / GPT-4o（草稿、润色、英文母语化），DeepSeek（中文底稿）
- **AI 视觉**：Midjourney v7 / Flux（封面、推文配图、profile 头图）
- **AI 数据**：X API（v2 Basic/Pro） + 自建 Python 脚本（统计 / 监控 / 自动点赞同类账号）
- **调度**：Buffer / Hypefury（发布），n8n（自动化抓取 trending + AI 摘要）
- **变现链路**：
  - Affiliate：AdsPower、Perplexity Pro、Comet、Notion、Beehiiv、域名商
  - 数字产品：自建 Gumroad / Lemon Squeezy 店铺
  - 长期：自有 SaaS 站或付费 newsletter
- **资产/品牌**：Notion 主页、ConvertKit / Beehiiv 收件人、Stripe / Wise 收款
- **复盘**：本仓库的 `06-operate.md` + 简单 Python 报表（`code/scripts/`）

## 五、目录结构

```text
x-com-ai-builders/
├── README.md            # 本文件
├── 01-discovery.md      # 机会发现（为什么是 X，不是别的）
├── 02-research.md       # 选题/竞品/算法/合规调研
├── 03-plan.md           # 90 天 MVP 计划
├── 04-build.md          # 创作流水账（按周）
├── 05-launch.md         # 上线 Checklist + 首发 5 条内容
├── 06-operate.md        # 周报 / 月度财务 / 增长实验
├── 07-review.md         # 季度复盘
├── /assets              # 品牌资料、截图、合同/财务
│   ├── /brand
│   ├── /finance
│   └── /screenshots
├── /code                # 自动化代码
│   ├── /scripts         # 抓取 / 统计 / 发帖
│   ├── /prompts         # 沉淀的 prompt 库
│   ├── /workflows       # n8n / Make 工作流 JSON
│   └── /data            # 抓回来的原始数据（CSV/JSON）
└── /content             # 内容产物（与"过程文档"分离）
    ├── /posts           # 单条推文（<=280 字）
    ├── /threads         # 长串（带顺序编号）
    ├── /long-form       # 完整长文（>1k 字，可同步到博客）
    └── /repurposed      # 从其他渠道二次分发来的版本
```

## 六、关键链接

- **线上地址 / Demo**：<https://x.com/>(待填 handle)
- **代码仓库**：本仓库 `x-com-ai-builders/`
- **数据看板**：<待搭建>（计划：Notion 仪表盘 + 本地 SQLite + 自动周报邮件）
- **协作文档**：本目录 7 份 markdown
- **竞品/参考**：见 `02-research.md`

## 七、当前进展摘要

- 2025-10-12：项目立项，目录骨架与全流程模板就位；状态 `💡 idea` 即将转入 `🔍 research`。
- 2025-10-12：开始系统性调研 30 个 AI Builder 类账号（资料来源见 `02-research.md`）。
- 2025-10-12：注册/激活 X 账号，完成 bio + 头图 + 置顶帖 v1 草稿。

## 八、风险与下一步

- **最大风险**：
  1. **算法/政策变化**（X 推流规则 6 个月一改，账号被限流后恢复极难）。
  2. **人设一致性崩塌**——AI 自动发太多"营销味"内容会掉粉。
  3. **变现链路距离**——X 离钱远，affiliate 转化天然低（行业 0.5–2%）。
- **下一步 1 周内必须做的事**：
  1. 完成 `02-research.md`：列出 30 个对标账号、20 个高互动选题、5 条变现路径。
  2. 完成 `03-plan.md`：敲定 90 天里程碑、首月 30 条内容选题。
  3. 准备好"AI + 人类"协作 SOP：哪一步由 AI 出、哪一步必须人审。
