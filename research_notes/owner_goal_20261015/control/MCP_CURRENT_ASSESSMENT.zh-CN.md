# MCP 状态核对

地址：https://em.181131.xyz/gateway/v1/enterprise-math/mcp 。

2026-10-15 本轮实测：`em_context_manifest` 与 `em_status` 均成功返回，版本 `0.6.11`，直连传输 `DIRECT_HTTPS_STREAMABLE_HTTP`。源码同步在运行，仓库同步错误和控制同步错误均为 null，读到了独立审核成功后的 Source `456c6f38e9c3a310d9a809fcea1b1128320c5ab2`。已实际完成 Result 和独立审核的原生写入及 GitHub 全文回读；没有服务器离线的证据。

已确认过的问题：

- 并发更新 Source main 导致一次 `SOURCE_MAIN_CAS_RETRY_LIMIT`。协调串行写入后，同一研究运行恢复并成功冻结 Result；独立审核也已成功。
- GitHub 桥接存在排队，以及旧评论状态滞后的现象。有原生请求已成功，但旧评论仍停留在 OUTCOME_UNKNOWN 的实际例子；应读取原请求的 Native receipt。延迟的具体服务器原因尚未确定。
- 当前连接凭据是静态只读；直写遭拒属于权限配置，不能据此判定服务器故障。已获授权的写入通过项目既有 GitHub 控制桥接完成。

此次状态里控制快照为 `ON_DEMAND_REFRESH_PENDING`、`full_snapshot_verified=false`。这是本次捕获的状态，不能据此承诺所有功能均健康，也不能单独推断离线。

Johor 信息只来自历史 README：[不可变来源](https://github.com/awdawmip/em-research-mcp/blob/228c94e37d707f1ab86ee404ee5eaf9adb6c5fec/README.md#L30)。原文：

> Overseas endpoint: `https://em.181131.xyz/gateway/v1/enterprise-math/mcp`.
> The Johor Bahru application became the sole writer on 2026-10-04 at 16:23:40 UTC.
> Shanghai is stopped and disabled. The old VM, original state and history remain retained.

实际服务器位置和主机运维日志未验证；此前据此追问 Johor 运维连接的推断已撤回。

2026-10-15 20:03 UTC 附近再次只读检查：`em_status` 成功返回，仍为 `0.6.11` 与上述正确地址。Source pin 已到 `13af89a60fbff9aa7447febb543e53d5efbd4bf6`；源码同步运行，仓库与控制同步错误仍为 null。控制快照仍报告 `ON_DEMAND_REFRESH_PENDING`、`full_snapshot_verified=false`，不据此作全部功能健康承诺。新研究的实际 prepare、claim、open 也均已有成功回执。

2026-10-15 20:38:01 UTC 再次直接读取成功：地址与版本不变，Source 已同步至 `b46c77b64f5f42ed98a14f94dda29d4e2dc2cfac`；同步运行，仓库／控制错误为 null，`reviewed_code_gate_passed=true`，仍未作全量快照健康认证。本轮多项真实 Native 证据发布和非终局检查点均已成功并全文核验。

响应慢问题有更精确的实测：Public129 原生任务查询创建于 20:26:18 UTC，20:29:28 记录仍为 RUNNING，20:30:04 成功，创建到成功约 227 秒。这包含排队和上游等待，并非已测得的 CPU 时间；具体耗时原因未定位。因此当前可确认服务可用，也确实存在部分请求耗时较长的问题，不能把所有延迟都归为旧评论滞后。

本地原始证据：`MCP_STATUS_ACTUAL_DIRECT_READ_20261015T1834Z.json`、`MCP_STATUS_ACTUAL_DIRECT_READ_20261015T2003Z.json` 与 `MCP_DIRECT_STATUS_AND_PUBLIC129_ORIGINAL_20261015T203801Z.json`。本报告是控制状态说明，不授予数学、研究执行或服务器运维权限。
