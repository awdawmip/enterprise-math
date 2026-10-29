# R346｜BRC Newton 内区 TP₂：第301条无界差分带的精确证书

日期：2026-10-28（Asia/Shanghai）。
状态：**AUTHOR_SIDE_EXACT / CONDITIONAL_ON_R330 / DRIVER_UNREVIEWED / NOT_ADMITTED**。

账户规则读取：`awdawmip/chatgpt-global-knowledge main@0e5f9a101ea9ad5e9538ed90af71323400ba2180`；项目基准读取：`awdawmip/enterprise-math@6cd52f7b1794a4a5a8d4585dc6f6fcf561eefc19`；沿用 R345 作者侧前沿：`5e043110d76e7a61fa561cc4776ea16870439a15`。

## 1. 数学对象与约束

研究对象是 R345 的**完整十二项带符号 K/J 有序六边 BRC 辅助组合递推**，初值 `B_0(t)=1+t`。保留所有本次抽取度数内的正负项。原始分支数量、符号与乘积保留在 K/J 系数；观察范围只包含 BRC 组合系数抽取、整数差分与行列式；允许未来操作是其精确代数延拓。此辅助模型不等于心跳世界原生六维 X6 Cell 动力学；本结论不作 X6 物理归因。P000、ACTIVE 世界观与联合关系保全约束未变动。

定义

\[
D_{q,k}=\sum_{v=0}^{k}(-1)^{k-v}\binom{k}{v}2^{q-v}[t^q]B_{q+v}(t),\quad 0\le k\le q,
\]

\[
M_{q,k}=D_{q,k}D_{q+1,k+1}-D_{q,k+1}D_{q+1,k}.
\]

**载重前提：** R330 尚待独立复核的全指标命题：对所有整数 `r,u≥0`，`D_{r+u,u}=5^uH_r(u)`，`H_r\in\mathbb Q[u]` 且 `\deg H_r\le r`。

定义 `L_r(v)=5^rH_r(v)` 与

\[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1).
\]

将 `q=r+k` 代入定义，准确得到

\[
M_{r+k,k}=5^{2k+1-2r}Q_r(k-1),\qquad r\ge1,\ k\ge1.
\]

由 R330 有 `\deg Q_r\le 2r`。令 `t_{r,i}=\Delta^iQ_r(0)`，`0\le i\le2r`，则 Newton 插值给出

\[
Q_r(v)=\sum_{i=0}^{2r}t_{r,i}\binom vi,\qquad v\in\mathbb Z_{\ge0}.
\]

所以对固定 `r` 完整证明所有 `t_{r,i}>0`，便可推出所有 `k\ge1` 的 `M_{r+k,k}>0`。

## 2. 本轮精确证书

重新执行原始十二项 K/J 带符号递推，计算 `B_s,0\le s\le908`，保留幂次 `0,\ldots,605`；构造 `H_0,\ldots,H_{302}` 并检查 `\Delta^{r+1}H_r(0)=0`、全部 `H_r` 的 Newton 系数严格正、`\Delta^rH_r(0)=6^r`，其中 `0\le r\le302`。额外节点检查属于有限验证，不代替 R330 全指标引理。

精确生成 `Q_{301}(0),\ldots,Q_{301}(602)`，求其 **603个完整 Newton 系数**：

- 全部603项严格正；0项非正。
- 全部系数中的最小值在 `i=0`。
- 603项规范文本 `301,i,decimal_difference\n` 的 SHA256：`242f508cdf355e238c7052d3e7bb66b71754d5e474c85e617328210f951c4484`。
- 从头重算 `r=1\ldots300` 的旧90,600项，SHA256：`5f897213f1bc399a6f649b7a9bb3932a1d670cbae4eb7baa98a08eee96c9b384`（与R345一致）。
- 旧 `r=256\ldots300` 摘要：`5835f388f9a78bbcde8bff10a4ff5bfa85364794a8658084efb48526d5fbb136`（与R345一致）。
- 全部 `r=1\ldots301` 共91,203项 SHA256：`0890ffe6433ce6a8edbcca77c94fd05e854628ef2ec4ffca7143d413c6cf6515`。

最高阶系数同时满足精确恒等式

\[
t_{301,602}=30^{602}\operatorname{Cat}_{301}
=\frac{30^{602}}{302}\binom{602}{301}>0.
\]

其推导为 `\Delta^rH_r(0)=6^r` 给出 `L_r` 最高幂系数 `30^r/r!`，在 `Q_r` 中相减得到 Catalan 因子；本轮亦由整数计算复核。

## 3. 本轮新增条件定理

结合 R345 的300条带，基于 R330 载重前提，得到

\[
\boxed{M_{q,k}>0,\quad k\ge1,\quad 1\le q-k\le301.}
\]

依照 R341 的合法矩形比值望远镜及上述域内 `D` 的正性，进一步得

\[
\boxed{D_{q,k}D_{p,\ell}-D_{q,\ell}D_{p,k}>0,
\quad1\le k<\ell\le q<p,\quad p-k\le302.}
\]

“无界”特指每个固定余阶差分带内的 `k` 可无限增长；`r,k` 同时增长的全二维内区 TP₂ 仍为开放目标。

## 4. 复现、精确范围与交接

运行 `python R346_verify.py`。执行仅使用 Python 任意精度整数和 `Fraction`，不使用浮点判断；已执行本地原件 `R346_verify.py` 的 SHA256：
`b7a0e0be716cef2f5b1c6ec49b87c74084c38d379277ab26fbd9b9e0fab486a4`。

完整本地机器证据 `R346_EVIDENCE.json` SHA256：
`78cca14b8051fba5295a610bcea78fb890fbeb293baf1f635dd9439213093dba`；存档摘要 `R346_SUMMARY.json`。复用来源 `research_notes/r345_unbounded_interior_tp2_corank300_20261028_emr3/R345_VERIFY.py`（R345 commit：`5e043110d76e7a61fa561cc4776ea16870439a15`）。本轮生成代码独立复现该原始 K/J 约定并重算 R345 历史摘要。

下一独立研究单元：`r=302` 所需 `H_{303}`、`Q_{302}` 共605项完整 Newton 差分；另需独立审查 R330 全指标有理抽取与次数界，尝试证明同时控制 `r,k` 的统一正锥条件。

权限：GitHub 实际登录 `awdawmip`；本轮原生任务读取 `CONTROL_QUOTA`、原生 session 创建 `STATIC_READONLY_SCOPE_DENIED`（`operation_sent=false`）；原生活跃 owner/CLAIM 未获权威确认，无 Source Result 与独立 Driver 接纳。
