# R346｜第301条无界 BRC Newton 内区 TP₂ 余阶带交接

## 本轮证明范围

2026-10-28 Asia/Shanghai，在 R345 完整十二项有符号 K/J 辅助模型上，独立精确重建 \(r=1,\ldots,301\) 的 \(\Delta^i Q_r(0)\)。
新增 \(r=301\) 的603项系数严格正，旧 \(r\le300\) 的90,600项摘要与 R345 全部相符。
在尚待独立审查的 R330 有理抽取及次数界成立时，得 \(M_{q,k}>0\) 对所有 \(k\ge1,1\le q-k\le301\)；
由 R341 的正比值传播，非相邻内区合法子式在 \(p-k\le302\) 上正。
该成果仅属于原始 BRC 辅助组合模型，尚未对应到原生 X6 动力学。

## 必需材料

- 证明：本目录 `R346_PROOF.zh-CN.md`。
- 本轮实际运行、与本地源 Git Blob 一致的代码：`R346_verify.py`。
- 已执行精确整数/Fraction摘要：`R346_SUMMARY.json`。新增603项SHA256：`242f508cdf355e238c7052d3e7bb66b71754d5e474c85e617328210f951c4484`。
- 完整本地执行证据 SHA256：`78cca14b8051fba5295a610bcea78fb890fbeb293baf1f635dd9439213093dba`。本目录保存摘要，完整执行工件交付见研究轮次附件。
- 源前沿 R345：GitHub commit `5e043110d76e7a61fa561cc4776ea16870439a15`；GLOBAL_KNOWLEDGE_V1 固定读取 `main@0e5f9a101ea9ad5e9538ed90af71323400ba2180`。

## 研究及权限状态

`AUTHOR_SIDE_EXACT / CONDITIONAL_ON_R330 / GITHUB_READBACK_VERIFIED / OWNER_UNVERIFIED / DRIVER_UNREVIEWED / NOT_ADMITTED`。
GitHub 用户 `awdawmip` 可用于作者侧仓库持久化。
原生 `em_control_tasks` -> `CONTROL_QUOTA`，`em_session_start` -> `STATIC_READONLY_SCOPE_DENIED`（operation_sent=false）；本轮未生成/借用原生 Task CLAIM。
P000、ACTIVE 世界观保持原样。

## 下一任务（保持用户原父研究目标开放）

计算 \(r=302\) 所需 \(H_{303}\)、\(Q_{302}\) 的605个完整 Newton 差分；条件证书不得外推到未验的 \(r\ge302\)。
并以真正独立的数学推导检查 R330 全指标有理抽取及 \(\deg H_r\le r\) 引理，尝试非有限差分检查的证明或反例。
正系数证书失败时区分充分条件失败和实际内区 \(M_{q,k}\) 变号。
