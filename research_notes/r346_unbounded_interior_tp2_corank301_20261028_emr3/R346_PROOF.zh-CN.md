# R346｜BRC Newton 内区 TP₂ 第301条无界差分带：完整精确整数证书

日期：2026-10-28（Asia/Shanghai）。研究状态：AUTHOR_SIDE_EXACT / R330_CONDITIONAL / DRIVER_UNREVIEWED / NOT_ADMITTED。
固定知识读取：`awdawmip/chatgpt-global-knowledge main@0e5f9a101ea9ad5e9538ed90af71323400ba2180`；项目当前源读取：`awdawmip/enterprise-math@6cd52f7b1794a4a5a8d4585dc6f6fcf561eefc19`；复用 R345 不可变数学前沿 `5e043110d76e7a61fa561cc4776ea16870439a15`。

## 对象、范围与语义

本研究对象为 R345 原始**十二项有符号 K/J 递推的有序六边 BRC 辅助组合模型**，初始条件 `B_0(t)=1+t`。保留所有所需次数内的有符号高次项。人口为该辅助组合模型的完整标号递推，分支符号与 multiplicity 保留在系数中；观察量为系数抽取和有限差分；未来操作限定为下述整数差分、行列式及 Newton 插值。此一维指标是辅助模型的代数参数，不是独立的原生空间方向；没有建立向 P000 原生 X6 六维 Cell 动力学的对应，不作物理推论。P000、ACTIVE 世界观、联合关系保全规则均保持不变。

记
[
D_{q,k}=sum_{v=0}^k(-1)^{k-v}inom{k}{v}2^{q-v}[t^q]B_{q+v}(t),quad0le kle q,
]
[
M_{q,k}=D_{q,k}D_{q+1,k+1}-D_{q,k+1}D_{q+1,k}.
]

**明确的尚待独立复核前提（R330）**：对于一切整数 `r,u≥0`，`D_{r+u,u}=5^uH_r(u)`，其中 `H_r∈Q[u]` 且 `deg H_r≤r`。

令 `L_r(v)=5^rH_r(v)`，并按 R344/R345 定义
[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1).
]
直接按 `r=q-k` 代入可得对所有 `k≥1,r≥1`
[
M_{r+k,k}=5^{2k+1-2r}Q_r(k-1).
]
R330 给出 `deg Q_r≤2r`。故完整系数
[
t_{r,i}=Delta^iQ_r(0)quad(0le ile2r)
]
的严格正性，借 Newton 恒等式
[
Q_r(v)=sum_{i=0}^{2r}t_{r,i}inom vi
]
便能证明全部非负整数 `v` 上的严格正性。

## 新增 R346 证书

从原始十二项 K/J 递推重新计算 `B_s,0≤s≤908`，保留指数 `0…605`；构建 `H_0,…,H_{302}`，各自逐点计算 `u=0,…,r+1`，检验 `Δ^{r+1}H_r(0)=0`、全部 `r+1` 项 Newton 系数正且最高项 `Δ^rH_r(0)=6^r`。这些额外节点是有限核对，不取代 R330 的无限次数定理。

以全部整数 Newton 系数算出 `Q_{301}(0),…,Q_{301}(602)`，计算完整603项前向差分，**603项全部严格正；零/负项0；精确差分的最小项在 i=0**。

新增603项规范行 `301,i,decimal_integer\n` 的 SHA256 为：

`242f508cdf355e238c7052d3e7bb66b71754d5e474c85e617328210f951c4484`。

全部 `r=1…300` 的90,600项旧证书从本次原始递推独立重建，SHA256：

`5f897213f1bc399a6f649b7a9bb3932a1d670cbae4eb7baa98a08eee96c9b384`（与R345一致）。

其中 `r=256…300` 的摘要仍为
`5835f388f9a78bbcde8bff10a4ff5bfa85364794a8658084efb48526d5fbb136`（与R345一致）。

全部 `r=1…301` 共 `91,203` 项系数规范序列的SHA256为
`0890ffe6433ce6a8edbcca77c94fd05e854628ef2ec4ffca7143d413c6cf6515`。

最高项另满足
[
t_{301,602}=30^{602}operatorname{Cat}_{301}>0,
quad operatorname{Cat}_{301}=rac1{302}inom{602}{301}.
]
最高项恒等式由首项 `Δ^rH_r(0)=6^r` 及最高幂系数比较推得，并与精确计算一致。

## 条件结论与推广

继承 R345 的300条差分带，并加入第301条，得到**计算辅助、以 R330 为前提的作者侧结论**
[
oxed{M_{q,k}>0,quad kge1,quad1le q-kle301.}
]
由于已验证需要的 `H_0…H_{302}` Newton 正性，同一薄楔内 `D` 各元素均正；由相邻TP₂的正比值望远镜公式，得
[
oxed{D_{q,k}D_{p,ell}-D_{q,ell}D_{p,k}>0,
quad1le k<ellle q<p, p-kle302.}
]
该结论的无限指标为沿固定余阶差分带的 `k`，不是 `r,k` 同时无界的全二维猜想。

## 精确复验、可移植交接、来源

本轮本地实际执行程序为 `R346_verify.py`，仅用 Python 整数与 Fraction；机器摘要为 `R346_SUMMARY.json`；完整输出数据在本轮交付材料 `R346_EVIDENCE.json`，其 SHA256 为
`78cca14b8051fba5295a610bcea78fb890fbeb293baf1f635dd9439213093dba`。
本轮本地源 SHA256 `b7a0e0be716cef2f5b1c6ec49b87c74084c38d379277ab26fbd9b9e0fab486a4`。复验使用：
`python R346_verify.py`，运行后比较 `R346_SUMMARY.json` 中的SHA及603项正性。
源算法源于不可变 R345 GitHub 文件 `research_notes/r345_unbounded_interior_tp2_corank300_20261028_emr3/R345_VERIFY.py`，本轮在同一K/J定义下另写完整重验程序并重算旧90,600项摘要。

**接续问题**：计算 `r=302` 时 `H_{303}`、完整 `Q_{302}` 的605项系数；以及优先独立复核 R330 的全指标有理抽取与多项式次数界。出现 Newton 非正项时区别正锥证书失效与实际二阶子式变负。固定审查义务：独立 Driver 审查、数学原生接纳与 X6 桥接均仍待办理。

**权限记录**：本轮 GitHub 登录 `awdawmip`；原生 `em_control_tasks` 查询返回 `CONTROL_QUOTA`，`em_session_start` 返回 `STATIC_READONLY_SCOPE_DENIED, operation_sent=false`，活跃 Owner 未取得权威确认，未申请或冒领CLAIM/Result。
