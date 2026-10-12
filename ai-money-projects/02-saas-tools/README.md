# 02 — AI SaaS 工具 (saas-tools)

自建可对外提供服务的 SaaS，按**月订阅 / 按量付费 / 团队席位**等模式收费。
技术栈通常包含：前端 + 后端 API + 数据库 + 计费（Stripe / Creem）+ 第三方 AI API 包装。

## 分类下的项目索引

> 状态图例：💡 idea · 🔍 research · 🛠 building · 🚀 launched · 💰 profitable · 🧊 on-hold · ❌ killed · 📦 archived

| 项目名 | 一句话 | 定价 | 状态 | 创建 | 最近更新 |
| --- | --- | --- | --- | --- | --- |
| _（暂无）_ | — | — | — | — | — |

## 子目录约定

- 推荐命名 `<产品定位>-<目标人群>`，例如 `cold-email-ai-for-saas` `image-bg-remover-api`。
- 计费、隐私、用户协议等合规文档统一放在项目 `assets/legal/` 下。

## 共享经验（待沉淀）

- 常见坑：API 成本失控 → 引入缓存、限流、模型分级路由。
- 上 Stripe / Creem 流程笔记沉淀到 `../../skills/`。
- 部署模板（Vercel + Cloudflare + D1 / Neon）抽取为 skill。
