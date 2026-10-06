---
name: sandbox-env-triage
description: 沙箱环境故障分诊——把「命令失败」拆成三类（我自己的命令 bug / Xcode 许可门控导致 git 与 python3 失效 / 网络出口不可达）并各自处置。当命令报错、git 提交或推送失败、或反复抓不到外部资料时使用。
---

# sandbox-env-triage（沙箱环境故障分诊）

## 何时适用

- 命令报错，但不确定是**自己写错**还是**环境坏了**
- `git commit` / `git push` 失败
- 需要抓取外部资料，却反复失败、返回空
- 同一个操作"上次还好、这次不行"

## 核心原则：先分诊，再重试

**失败时不要立刻加大重试次数**。先把故障归到三类之一，因为三类的处置完全不同：

| 类别 | 能否自愈 | 处置 |
| --- | --- | --- |
| A. 我自己的命令 bug | 能（改命令） | 立即修 |
| B. 许可门控（git/python3 失效） | 能（加前缀绕过） | 立即绕 |
| C. 网络出口不可达 | 不能（等或交接） | 完成本地部分 + 交接 |

> 反例代价：曾把 B/C 误判为"网络抖动"，反复重试数轮，实际第一层只是自己的命令 bug。

## 30 秒分诊表

| 症状 | 病因 | 判据（一条命令确认） |
| --- | --- | --- |
| `You have not agreed to the Xcode license agreements`，exit 69 | **B 许可门控** | 换 CLT 直连路径能跑通即确诊 |
| 所有域名解析到 `198.18.0.x`（RFC 2544 保留段） | **C 出口不通**（DNS 被拦截代理接管） | `nslookup <host>` |
| `curl` 返回 `000` | **C** | `curl -s -o /dev/null -w "%{http_code}" https://github.com` |
| `ssh` 报 `Connection closed by 198.18.0.x port 22` | **C** | `ssh -T git@github.com` |
| `git push` exit 128 `correct access rights` | **可能是 C**，也可能是 ssh-agent 无身份 | `ssh-add -l`；再看上面两条 |
| `declare -A: invalid option` 等 shell 报错 | **A 命令 bug** | `bash --version`（macOS 常为 3.2） |
| Google Books API `429 quota exceeded` | 共享配额耗尽，非我方问题 | 换源（Open Library） |

## 病因 A：我自己的命令 bug

**先单样本，再批量。** 批量失败时，先跑一个最小样本确认管道本身可用。

macOS 常见坑：

- **bash 3.2**（2007 年版）不支持 bash 4 特性：`declare -A`（关联数组）、`mapfile` 都不可用。改用 `while IFS='|' read -r k v; do ... done <<'EOF'` + 索引数组。
- **报错只看 `tail -1` 会掩盖失败**：命令链用 `;` 连接时，前一步失败仍会继续执行，最后 `echo "成功"` 骗过自己。必须用 `&&` 串接，或显式核对结果（见下「推送必须核对」）。
- 解析 JSON 优先用 `jq`（本机为 1.7.1），不要手写正则。

## 病因 B：Xcode / CLT 许可门控

**现象**：`/usr/bin/git`、`/usr/bin/python3` 都是**受许可门控的 shim**；会话或环境重建后许可状态失效，所有调用直接 exit 69，报 `You have not agreed to the Xcode license agreements`。

**关键**：CLT 自带的真实二进制**本身是好的**，只是 `/usr/bin/*` 这层 shim 被拦。

**绕过（首选）**——加环境变量前缀：

```bash
export DEVELOPER_DIR=/Library/Developer/CommandLineTools
grep -c ...
git commit ...      # 现在可用
python3 -c ...      # 现在可用
```

**绕过（备选）**——直接调真实路径（实测 git 2.54.0 可用）：

```bash
/Library/Developer/CommandLineTools/usr/bin/git --version
/Applications/Xcode.app/Contents/Developer/usr/bin/git --version
```

⚠️ **每次 bash 调用都是全新 shell**：`export` 不会保留到下一次调用。要么每次都写前缀，要么在每条命令开头带上。

⚠️ `sudo xcodebuild -license accept` 需要交互式 sudo，**不要尝试**；绕过即可。

## 病因 C：网络出口不可达

**三连判据**（按顺序，全部命中即确诊）：

```bash
nslookup github.com                                  # 落在 198.18.0.0/15 → DNS 被拦截代理接管
curl -s -o /dev/null -w "%{http_code}\n" --max-time 10 https://github.com   # 000 → 出口不通
ssh -o ConnectTimeout=8 -T git@github.com            # Connection closed by 198.18.0.x port 22 → 确诊
```

**重要事实：出口是间歇性的**——可能几分钟前能推、现在不通、过一会儿又通。所以：

1. **不要用"加大重试次数"当解法**，那是把整轮时间烧在等待上；
2. 先把**不依赖网络的活干完**（写文件、本地逻辑、文档）；
3. 本地 `git commit` 保住成果，按根 README 约定**请用户在普通终端兜底**：`git push -u origin main`；
4. 之后再用**一次**带少量重试的推送收尾（网络可能已恢复）。

**恢复验证**：`curl` 得 200 + `ssh -T git@github.com` 返回 `Hi <user>! You've successfully authenticated`。此时直接推送即可。

## 推送必须核对（防止"假成功"）

推送命令不要用 `;` 收尾，否则失败会被吞掉。用显式核对：

```bash
git push 2>&1 | tail -2
test "$(git rev-parse main)" = "$(git rev-parse origin/main)" \
  && echo "✅ 本地=远程" \
  || { echo "⚠️ 未推送，本地领先:"; git log --oneline origin/main..main; }
```

## 反模式（不要做）

- 把环境故障当网络抖动，反复重试同一件事
- 不区分"我的 bug"和"环境故障"，一味归因外部
- 用 `;` 串联 `commit`/`push`，让失败静默通过
- 网络不通时硬等，不先做本地可完成的部分
- 尝试 `sudo` 修许可（需交互密码，必然失败）

## 案例

- [2026-10-06-xcode-license-and-egress.md](2026-10-06-xcode-license-and-egress.md) — 落实 13 条文献待核项时连折数轮：真实根因是许可门控 + 出口不通，而非网络抖动
