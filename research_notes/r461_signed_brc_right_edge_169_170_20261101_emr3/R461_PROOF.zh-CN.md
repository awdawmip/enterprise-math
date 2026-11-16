# R461｜signed BRC 辅助标量：s=169、170 的无限参数正性与 r=193 的 PF₃ 拼接
日期：2026-11-01。状态：AUTHOR_SIDE_EXACT_SYMBOLIC_AND_INTEGER / DRIVER_UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTRATION_DENIED。

## 来源与精确命题
本轮读取 GLOBAL_KNOWLEDGE_V1 canonical main `beb40a3fa89e97eabaed8a3f92b0c84bc03c9ba7`，Enterprise Math canonical main `e3298b14b8f868adb468085cc15c695aff11b6ef`；科学输入承继 R460 不可变提交 `a7d14cfe3f01dd784bcadcbab555240bd882e2b1`。沿用 R452 的精确 EOR 因子分解、R447 左缘与 R450 的 PF₃ 局部归约；后两项仍是作者侧依赖，未被本轮独立数学审查。

对于奇数 r=2k+1 和 2≤s≤r，令
`H(r,s)=binom(r+s,2s) [t^r](1−t)(1+t)^(2s)(1+t²)^(r−s)`，
`a_j=H(r,r−j)`（0≤j≤r−2，支持外补零），
`D₂,j=a_j²−a_(j−1)a_(j+1)`，`D₃,j=det(a_(j+v−i))_(i,v=0,1,2)`。

**定理 A：** 对每个 s∈{169,170} 与所有整数 k≥floor((s+2)/2)，均有 `D₂,r−s>0`、`D₃,r−s>0`。

## 证明与实际精确证书
令 `C_k=binom(2k,k)/(k+1)`，`B_t(k)=H(2k+1,t)/C_k`。根据 R452 已证明的全 t 整系数多项式恒等式：
`(2t)! B_t(k)=E_t(k) O_t(k) R_t(k)`，
`E_t=∏_(v=0)^(t−1) 2(k+1−floor(t/2)+v)`，
`O_t=∏_(v=0)^floor(t/2)(2k+2v+1)`，
`R_t=Σ_(q=0)^floor((t−1)/2) binom(t−1,2q) 2^q ∏_(v=q)^(floor((t−1)/2)−1)(2k−2v−1) ∏_(d=0)^(q−1)(k+1−d)`。
取 `k₀=floor((s+2)/2)`、`u=k−k₀≥0`、`F=(2s+4)!`，定义 `Q_t(u)=F B_t(k₀+u)∈Z[u]`（t=s−2,...,s+2）。设 A=Q_s、B=Q_(s−1)、C=Q_(s+1)、D=Q_(s−2)、E=Q_(s+2)，则
`P₂=A²−BC`；
`P₃=A³−2ABC+DC²+B²E−DAE`。
严格关系：`D₂,r−s=C_k² P₂(u)/F²`，`D₃,r−s=C_k³ P₃(u)/F³`。因此只需两个 Z[u] 多项式的全部系数严格为正。

实际执行任意精度整数源码 `R461_VERIFY.py`，对 s=169（k₀=85）得到 deg P₂=676、deg P₃=1014，共1692项严格正系数，系数流 SHA256 `aa9a7596202359a9b192e9f9748424261adf4cbfaba7a1e13b9c068c1650a07a`；对 s=170（k₀=86）得到次数680和1020，共1702项严格正系数，SHA256 `e7fcbb577161feceac4be438e941c0d913bc1970f560f03f377123ab006072bd`。合计4个完整多项式、**3394个严格正系数**。另精确验证两个全多项式 Desnanot–Jacobi 恒等式
`A P₃=P₂²−(B²−DA)(C²−AE)`，
以及20项原始 signed 卷积、20项 Catalan 表达式的边界交叉等式。因 P₂、P₃ 的每项系数严格正，u≥0 时 P₂、P₃ 严格正，从而证明全部无限多个合法 k。哈希是可重现的计算一致性凭据。

## r=193 的完整拼接
对于 r=193（k=96），j≤22 由 R447 左缘证书覆盖；j≥23 则 s=193−j≤170，由 R452—R461 右缘证书覆盖；全部合法 j∈[0,191] 的二、三阶相邻子式正。在 R450 的局部充分判据与此前作者侧依赖成立的条件下，得 `T^(193)∈PF₃`，双端拼接链延伸至奇数 r=99,101,...,193。

此外独立执行 `R461_ROW_VERIFY.py`，对 r=193 的192个系数、192个 D₂、192个 D₃ 进行**576项全整数严格正性检查**，并核对8项原始 signed 卷积和8项交替 Catalan 等式；全部通过。该整行证书是固定 r 的证据，PF₃ 推论依赖 R450 的数学归约。

## 模型边界、复现与后续
此结果为 signed BRC 的辅助标量读出，没有宣告原生 X6 联合状态、时间动力学、切片或观察保真对应。P000 与 ACTIVE 世界观未修改。复现命令：
`python R461_VERIFY.py 169 169`
`python R461_VERIFY.py 170 170`
`python R461_ROW_VERIFY.py`
在本轮原生执行会话登记中，服务以 `STATIC_READONLY_SCOPE_DENIED` 拒绝（`operation_sent=false`），因此仅归档作者侧成果，没有 CLAIM、Result 或独立 Driver 审查。
**下一单元：** 检查 s=171,172 的完整正系数证书，以拼接 r=195；并尝试对 s,k 同时无界增长证明统一 Turán 正性不等式。
