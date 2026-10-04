# manuscript（正文）

本书正文，一章一文件。文件名与 [outline.md](../outline.md) 的章号严格一一对应。

## 命名约定

| 部分 | 文件名格式 | 示例 |
| --- | --- | --- |
| 第一部分 | `chNN-英文短名.md` | `ch01-getting-started.md` |
| 第二部分 | `chNN-英文短名.md` | `ch10-business-definition.md` |
| 附录 | `appendix-X-英文短名.md` | `appendix-a-glossary.md` |

## 写作要求

每章按 **[章节模板 v1.0（已锁定）](../chapter-template.md)** 撰写：**本章目标 / 实操步骤 / 坑点与解法 / 验收标准**。

- 长度预算：单章正文 8–12KB（约 150–250 行）。
- 单章坑点不超过 8 条；超出部分移入本目录的 `pitfalls-chNN.md`，正文只留汇总表。
- 坑点编号全书唯一（`P-###`）、**只增不改**，并在第一部分末章（排错手册）按现象登记索引。
- 预期输出必须标 `【实测】`（附硬件与版本）或 `【示意】`（写明非实测值）。
- 引用上游项目的命令必须与实测通过的 commit / 版本号一起出现。
- 图引用 `figures/` 中的文件，编号形如 `图 3-1`；代码引用 `code/chNN-*/`。
- 正文只放关键代码片段，完整脚本一律放 `code/`。

## 索引

| 文件 | 对应章节 | 状态 |
| --- | --- | --- |
| [ch01-getting-started.md](ch01-getting-started.md) | 第 1 章 开局：选路、硬件与预算 | 样章（四段式模板已验证） |
| [appendix-a-glossary.md](appendix-a-glossary.md) | 附录 A 术语表 | 初稿 |
| [appendix-b-hardware-cost.md](appendix-b-hardware-cost.md) | 附录 B 硬件与成本对照表 | 初稿 |
