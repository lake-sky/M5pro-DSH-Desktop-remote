# 06 — AI Agent / 自动化 (ai-agents)

搭建 Agent（或组合多个 agent）替客户（或替自己）完成**重复性、可被规则化**的工作。
典型方向：
- 客服 Agent（接单、回答、退款、跟进）
- 销售 Agent（线索挖掘、邮件外联、CRM 同步）
- 运营 Agent（社媒自动发布、内容审核、A/B 实验）
- 交易 / 监控 Agent（数据抓取、异常告警、量化脚本）
- 办公自动化 Agent（周报、PPT 整理、知识库问答）

## 分类下的项目索引

> 状态图例：💡 idea · 🔍 research · 🛠 building · 🚀 launched · 💰 profitable · 🧊 on-hold · ❌ killed · 📦 archived

| 项目名 | 一句话 | 部署形态 | 状态 | 创建 | 最近更新 |
| --- | --- | --- | --- | --- | --- |
| _（暂无）_ | — | — | — | — | — |

## 子目录约定

- 命名 `agent-作用对象`，例如 `agent-shopify-cs` `agent-bilibili-auto-publisher`。
- 代码放 `code/`，配置（n8n / Coze / Dify 工作流 JSON、prompt、secrets 模板）放 `code/configs/`，**真实密钥不入库**。
- 跑批日志、抓取数据、对外可公开的产物放 `assets/`。

## 共享经验（待沉淀）

- Agent 设计模式（ReAct / Plan-and-Execute / Reflection）汇总 → `../../skills/`。
- 评估（Eval）与护栏（Guardrail）模板。
- 计费模式：按调用量 / 按时长 / 按结果佣金。

## 风险红线

- 涉及真实交易、金融、外联的 Agent 必须有**人工审核开关**与**速率限制**。
- 涉及抓取与账号操作的 Agent 必须确认平台 ToS 合规。
- 任何 Agent 不得代替用户做不可逆操作而无人确认。
