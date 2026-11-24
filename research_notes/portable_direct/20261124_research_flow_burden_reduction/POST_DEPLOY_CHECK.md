# 后端部署后的独立复查 — 2026-11-24

Progress-Event-ID: `20261124T073902Z-backend-deployment-verified-f52de59801bc`
At: `2026-11-24T15:39:02+08:00`
Role: `CONTROL_PLANE_MAINTENANCE`
Status: `BACKEND_DEPLOYMENT_VERIFIED`

## 结论

用户通知部署完成后，重新读取真实运行版本并走查既有会话、已有任务、固定成果和速记本。上次的“后端等待部署”已完成；原会话恢复空页问题在同一真实会话上消失。新提交的精确任务读取成功，原任务状态、归属及固定任务书核验一致。

本轮没有改动运行代码或增加 CI。研究身份、CLAIM、任务和生产笔记均沿用既有记录。

## 部署源与真实运行版本

- 实际 release：`6e1b2fd7f0954ec375156e799e89d76c26abb2b2`，父提交为原部署 `b6c33838c05b8442b225a6c019773fb026e18607`，保留既有速记本集成。
- 实际读回 runtime：`e294ccd6841b84ea7d9fc18802b4654fa4eae400d9681f6672f37814ea5c9c8e`。
- 网关实际 build：`em-sites-gateway-20261124-light-read-r1`。
- release 三处实现与此前补丁对应：轻身份直接省去合同构造；恢复请求按真实 SID 绑定过滤后分页；精确 task 不再无条件预取 Activity 全根。

来源：[部署记录](https://github.com/awdawmip/em-research-mcp/blob/1ee30bae732f7517639f13a5dd841d57c2c4985e/docs/evidence/research-flow-20261124/REPORT.md)、[实际 release](https://github.com/awdawmip/em-research-mcp/commit/6e1b2fd7f0954ec375156e799e89d76c26abb2b2)。部署记录的 runtime 与本轮 live 回执一致，未把 MCP main 当作运行 release。

## 实际流程检查

| 环节 | 本轮结果 |
|---|---|
| 轻身份 | 成功；3,431 字符；`source_snapshot_read=false`，按需合同定位仍在。 |
| 完整合同 | 成功，四项 Driver 合同完整可读。 |
| 旧会话恢复 | 返回自己的原登记 `paper-k4-pell-p008-revision-20261113-f52de59801bc`，`SUCCEEDED`；SID 与原登记回执一致。 |
| 分页结束 | 本会话实际只有一条绑定请求，`has_more_requests=false`、`next_cursor=null`。旧空页及外会话游标消失。 |
| 已有成果 | 原请求 `flow-reduction-20261124-f52de59801bc-artifact-v1` 仍成功；元数据、正文页和完整哈希与部署前一致。 |
| RH 固定来源 | `4d63cb…` 报告 L1–L32 精确对应，解析响应与部署前一致。 |
| X6 当前笔记 | `X6.R90.near-directions.sharp-port.20261123.routing.v9` 仍为 current，4,823 字符，内容与部署前一致。 |

此次历史会话没有下一页，未人为制造分页；部署记录另有真实 Driver 会话的续页验收，本地真实解析器用例也覆盖多页与同时间戳。历史会话恢复仍为元数据读取，`execution_authorized=false`、`credentials_included=false`。

## 新发起的已有 C78 任务读取

原请求：`flow-postdeploy-20261124-0733-f52de59801bc-task-v1`。
任务：`RS-C78-EFFECTIVE-RATIONAL-IDENTIFICATION-20261123`。

该请求从 QUEUED/RUNNING 到 `SUCCEEDED`，没有重发。实际入场 Source 为 `a88e3e001275269cae93c40d77e6984b1ef2970f`，完成时 Source 和事件 Issue 均未变化；收集 1,774 条事件。publication 为 `TP2-9B877E4C74293B30F2EF`，状态 `READY / NEEDS_DISPATCH`，owner 为 `taskbook/unassigned`，claim 为空。

另从上述固定 Source 读取 [任务书](https://github.com/awdawmip/enterprise-math/blob/a88e3e001275269cae93c40d77e6984b1ef2970f/research_tasks/RS-C78-EFFECTIVE-RATIONAL-IDENTIFICATION-20261123.md)，其正文与 native 返回逐字相同，blob 均为 `02a01c65498dd423eb0625ef64b83bb9f903f6c8`。publication、任务书 blob、状态和归属也与上次该任务的核验记录一致。

本次总完成耗时约 **82 秒**，观察器阶段累计为 81.78 秒：

| 阶段 | 本轮累计墙钟时间 |
|---|---:|
| Source 材料准备 | 41.42 秒 |
| 原生任务读取与状态计算 | 38.68 秒 |
| 事件整理 | 1.27 秒 |
| 非运行等待 | 0.013 秒 |

其他阶段合计约 0.40 秒。阶段时间来自终态 `progress.timing.completed_phase_seconds`，计量为墙钟时间。当前性能负担主要落在材料准备和原生状态计算，并非本次排队。

部署记录中另一个任务实际初始选入 5,600 个路径，其中 Activity 44 个，后续按需追加为 0；该计数来自 server 观察 `inv-sbj35k0je9`。本轮 C78 正常成功回执没有公开初始 selected/Activity 计数，故不把前一任务的 44 当成本次计数。实际运行源码已确认包含 Activity 按需读取修复。

## 剩余事项

旧 X6 v1 仍只提供 `current=false` 和向后的 `revises`，没有直接指向当前继任版本的入口。该能力不在这次部署补丁内；按已知当前 ID 接续正常。

本次单任务读取仍约 82 秒，下一次性能改进应依据上述两段实际开销定位。恢复、RH source、X6 note 的一次并发读取批次也出现约 12–14 秒样本；该批次含并发和排队影响，未将它解释为独立性能结论。

本轮不新增研究工作流。原部署交接已完成，后续不应仅因早期文档中的“尚未部署”再次部署同一补丁。完整指标见同目录 `POST_DEPLOY_METRICS.json`；恢复与速记本逐项比较摘要见 `POST_DEPLOY_FLOW.json`。
