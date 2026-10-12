# /content — 已发布与待发布的内容产物

本目录与"过程文档"分离，专门存放**已经发布**或**待发布**的内容本身。

> 规则：
> - 入库前用脚本自动脱敏（脚本：`../code/scripts/scrub.py`，待建）。
> - 每份内容用 `YYYY-MM-DD__<slug>.md` 命名。
> - 文件第一行固定为 frontmatter：发布状态、handle、impressions、engagement。
> - **真实收入截图 / 隐私数据 → `../assets/screenshots/`**，不在此留底。

## 目录约定

| 子目录 | 用途 |
| --- | --- |
| `posts/` | 单条推文（≤ 280 字） |
| `threads/` | 长 thread（多帖带顺序） |
| `long-form/` | 长文（> 1k 字，X Articles 或博客同步） |
| `repurposed/` | 从其他渠道（中文公众号、博客）二次分发到 X 的版本 |

## 文件命名

```text
YYYY-MM-DD__<slug>.md
# 示例：2025-10-15__ai-tools-i-paid-for.md
```

## frontmatter 模板

```yaml
---
status: draft | scheduled | published | killed
date: YYYY-MM-DD
handle: @yourhandle
impressions: 0
likes: 0
reposts: 0
replies: 0
bookmarks: 0
profile_clicks: 0
affiliate_clicks: 0
revenue_usd: 0.00
notes: |
  创作时灵感、数据来源、特别决策
---
```

## 当前内容数

- posts: 0
- threads: 0
- long-form: 0
- repurposed: 0

> 项目 M0 阶段，尚未发布任何内容；首发 5 条见 `../05-launch.md`。
