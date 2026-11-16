# R474｜有限正系数 PF₃ 的无附加前提局部充要判据

日期：2026-11-02。结论：作者侧解析证明＋精确整数有限回归（UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING）。本结果修正 R473 的假设形式：该定理中的二阶严格正性原来被作为前提，现证明它对全部有限正系数 PF₃ 序列事实上**必然成立**。适用对象为一般有限正实序列的半无限 Toeplitz 矩阵，signed BRC 为应用场景；不涉及新的 X6 原生动力学证明。

## 主定理

设 n≥2，a₀,…,aₙ>0 为任意实数，其他下标 a_j=0，T_{i,j}=a_{j−i}（i,j≥0）。设

\[
D_{2,j}=a_j^2-a_{j-1}a_{j+1},\quad D_{3,j}=\det(a_{j+v-i})_{0\le i,v\le2}.
\]

则对所有 0≤j≤n 有如下**无预设严格二阶条件**的充要等价：

\[
\boxed{T\in PF_3 \ \Longleftrightarrow\ D_{2,j}>0\ \text{且}\ D_{3,j}\ge0\quad(0\le j\le n).}
\]

PF₃ 意味所有 1、2、3 阶有限 Toeplitz 子式非负。D₂,₀=a₀²、D₂,ₙ=aₙ²、D₃,₀=a₀³、D₃,ₙ=aₙ³ 均自动严格正；实际只需 1≤j≤n−1 的局部二、三阶检查，O(n) 个子式。

## 新增引理（严格 D₂ 是 PF₃ 必要条件）

PF₃ ⇒ D₂,j≥0，因为这些就是合法二阶相邻子式。如果内部存在零，选第一个 j∈{1,…,n−1} 满足 D₂,j=0。此时 D₂,j−1>0（起点 D₂,₀=a₀²>0）。

取前三行 0,1,2 与非连续列 j,j+1,n+1，对应三阶子式

\[
\begin{aligned}
M_j&=\det\begin{pmatrix}
a_j&a_{j+1}&0\\
a_{j-1}&a_j&a_n\\
a_{j-2}&a_{j-1}&a_{n-1}
\end{pmatrix}\\
&=a_{n-1}(a_j^2-a_{j-1}a_{j+1})-a_n(a_j a_{j-1}-a_{j+1}a_{j-2}).
\end{aligned}
\]

因 D₂,j=0 且所有 a 正，a_{j+1}=a_j²/a_{j−1}，直接代入得

\[
\boxed{M_j=-\frac{a_n a_j}{a_{j-1}}D_{2,j-1}<0.}
\]

与 PF₃ 矛盾。因此全部局部 D₂ 必须严格正；这个论证包含两侧有限支撑零边界。

## 充分性与承重依赖

在 D₂,j>0、D₃,j≥0 条件下，R473 已证明充分性：设 v_j=(a_j,a_{j−1},a_{j−2})ᵀ。内部正规化 x_j=a_{j−1}/a_j 严格上升；y_j=a_{j−2}/a_j。相邻割线斜率 h_j=(y_{j+1}−y_j)/(x_{j+1}−x_j) 从 D₃,j≥0 推出单调不降，故每个内部三列行列式 ≥0。右端 D₃,n−1≥0 等价于右边界斜率 a_{n−1}/a_n≥h_{n−1}，控制 v_{n+1}=(0,a_n,a_{n−1})ᵀ、v_{n+2}=(0,0,a_n)ᵀ；后续列为零。前两行的一、二阶子式也非负。R441-A 经 skew dual Jacobi–Trudi 与 Littlewood–Richardson 非负展开将连续首行普通子式推广到所有行选择的 Toeplitz 子式。因此充分性成立，新增必要性给出完整等价。经典 Schur/LR 索引归约仍属于后续独立审阅的数学依赖。

## 非严格二阶局部判据的显式反例族

n≥3、任意 q>0，令 a_j=q^j（0≤j≤n），支持外为零。直接代数计算：全部局部 D₂,j≥0 和 D₃,j≥0，内部均为零；但是

\[
\det T_{\{0,1,2\},\{1,2,n+1\}}
=\det\begin{pmatrix}q&q^2&0\\1&q&q^n\\0&1&q^{n-1}\end{pmatrix}
=-q^{n+1}<0.
\]

最小例子 a=(1,1,1,1) 的全部局部 D₂,D₃ 非负，但列 (1,2,4) 给 −1。因此把 D₂>0 改成 D₂≥0 而只检查邻接三阶子式，会漏掉真实非邻接负证；严格性是 PF₃ 真正的必要性质。

## 精确整数回归

R474_VERIFY.py 以任意精度整数完整枚举正整数序列：n=2,3,4,5 且每个 a_i∈{1,…,6}；n=6 且每个 a_i∈{1,…,4}，**总计72,328条**。针对通过严格局部判据的 162 条输入，枚举 R441-A 所列全部 m≤3 首行普通 Toeplitz 子式，均非负。对于满足弱局部判据但未满足严格判据的 185 条输入，逐条计算首个内部零 D₂ 引出的 M_j<0，且精确全列验证有负三阶子式：n=3,4,5,6 分别 6,36,105,38 条。对 n∈{3,4,7}, q∈{1,2,3} 的几何序列独立检查 M_1=−q^(n+1)。汇总分类流 SHA256 为 008dd99b505ffae0995d010ebc92340cdcc502e85df476389835d43b4ebb6c96；真实运行输出 R474_EXACT_PASS，机器数据见 R474_EVIDENCE.json。

一般任意正实数命题依据解析证明；整数枚举是范围明确的交叉检查，并非代替证明。

## 精确来源与可续接前沿

- R473（直接推论起点）：research_notes/r473_sharp_pf3_nonstrict_local_20261102_emr3/R473_PROOF.zh-CN.md；继承不可变提交 f7dce1c52cd9ecadefc50703b5f8634f45c4fb30。
- R441-A（必要的 Schur/LR 全行归约）：research_notes/r441_signed_brc_schur_lr_full_pf4_20261101_emr3/R441_PROOF.zh-CN.md。
- 既有 signed BRC 科学输入冻结于 R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f。BRC 复用类别：REUSE_APPLIED（signed scalar / Toeplitz observer，保留其有符号组合）；未把 signed 标量定理视为正 BRC 质量或原生 X6 保真。
- 下一研究单元：独立检查 R441-A 的 skew Schur 形状/索引映射与有限支撑边界，之后将无附加前提判据用于 R472 后续 s=249,…,256 的参数研究；允许系数为零的支撑分块另行探索。
- 2026-11-02 本轮 GitHub 账号 awdawmip，对 enterprise-math 显示 push=true。原生会话注册返回 STATIC_READONLY_SCOPE_DENIED（operation_sent=false），活跃任务查询返回 CONTROL_QUOTA；未形成原生 CLAIM/Result/Driver 接纳。P000 与 ACTIVE 世界观保持原状。
