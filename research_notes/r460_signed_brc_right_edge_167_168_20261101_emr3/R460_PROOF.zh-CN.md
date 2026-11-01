# R460｜signed BRC 辅助标量：s=167、168 的无限参数正性与 r=191 的 PF₃ 拼接

日期：2026-11-01。状态：AUTHOR_SIDE_EXACT_SYMBOLIC_AND_INTEGER / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。

## 规范来源、角色和边界

输入固定于 GLOBAL_KNOWLEDGE_V1 main@6d5a467836a2b555a1997a110968aad3d66bd074、Enterprise Math main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419，数学前沿继承 R459 不可变提交 ceb9f50c412d5aee1f909220a2181cafffb9e0be（Draft PR #1708）。已读项目 P000、ACTIVE 世界观、可移植研究协议及 R459 输入；研究属于原始 signed BRC 的辅助标量读出，不断言原生 X6 支路、时间动力学或观察映射的全状态保真。

本轮 GitHub 认证账户 awdawmip 可以写入仓库；原生服务 em_status 的 research_authority_granted=false、active_jobs=5/5，DIRECTED_RESEARCH 定向路由 authority_granted=false。未声明活动已原生登记、正式 Owner、CLAIM、Result 或独立审阅资格。P000 和 ACTIVE 世界观原样保留。

## 研究对象

令 r=2k+1 为奇数，2≤s≤r，Catalan 数 C_k=(2k)!/[k!(k+1)!]，定义

\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},
\qquad B_s(k)=H(2k+1,s)/C_k.
\]

相邻 Toeplitz 二阶、三阶子式（列 j=r−s）为

\[
D_{2,s}=H(r,s)^2-H(r,s-1)H(r,s+1),
\]

\[
\begin{aligned}
D_{3,s}={}&H(r,s)^3-2H(r,s-1)H(r,s)H(r,s+1)\\
&+H(r,s-2)H(r,s+1)^2+H(r,s-1)^2H(r,s+2)\\
&-H(r,s-2)H(r,s)H(r,s+2).
\end{aligned}
\]

## 定理 A｜两个新位置的无限参数证书

对每个整数 s∈{167,168}，以及所有整数 k≥k₀=⌊(s+2)/2⌋，都有 D_{2,s}>0 且 D_{3,s}>0。

证明依赖 R452 的精确 E_s O_s R_s 恒等式，采用 u=k−k₀≥0、F=(2s+4)!。对 t=s−2,...,s+2 令 Q_t(u)=F B_t(k₀+u)∈ℤ[u]，并记 A=Q_s、B=Q_{s−1}、C=Q_{s+1}、D=Q_{s−2}、E=Q_{s+2}。于是

\[
P_{2,s}=A^2-BC,\quad
P_{3,s}=A^3-2ABC+DC^2+B^2E-DAE,
\]
\[
D_{2,s}=C_k^2P_{2,s}(u)/F^2,\qquad
D_{3,s}=C_k^3P_{3,s}(u)/F^3.
\]

R460_VERIFY.py 以任意精度整数逐一生成四个完整多项式，检验每个系数严格大于零，并独立确认 Desnanot–Jacobi 多项式恒等式

\[
A P_{3,s}=P_{2,s}^2-(B^2-DA)(C^2-AE).
\]

u≥0 时正系数保证多项式严格正，故结论覆盖无限多个 k，而非有限样本的经验外推。

| s | k₀ | deg P₂ | deg P₃ | 正整数系数总数 | 长度前缀系数流 SHA256 |
|---:|---:|---:|---:|---:|---|
| 167 | 84 | 668 | 1002 | 1672 | 93881acc78ac2348d7c01514697173fb265316f42d9d28b3d2061553de0d0e85 |
| 168 | 85 | 672 | 1008 | 1682 | b9d4e55210095c040bf24f21af1e7e1dec8c498bc3ec47da787ded79ca140adb |

**本轮共验证4个完整参数化多项式、3354个严格正系数和2项全多项式恒等式。** 对每个 s 在 k=k₀、k₀+1 与五个相邻 t，执行20次原始 signed 卷积与 EOR 值的精确相等检查，以及20次 Catalan 改写相等检查，均通过。有限交叉检查与无限参数正系数证书属于不同证据层。

## 定理 B｜新增 r=191 的 PF₃ 证明路径

以 a_j=H(r,r−j)（0≤j≤r−2，之外为零）定义半无限 Toeplitz 矩阵。根据前序作者侧 R447 左边缘 j≤22、R452—R459 右边缘 2≤s≤166 正性证书，本轮的 s=167、168 使 r=191 时 j≥23 的全部 s=r−j≤168 受证书覆盖；其余 j≤22 由 R447 覆盖。结合 R450 的相邻二阶、三阶子式正性充分判据，**在上述前序定理成立的条件下，T^(191)∈PF₃**。此拼接路线覆盖全部奇数 99≤r≤191，新增 r=191。

另外独立使用 R460_ROW_VERIFY.py 的正 Catalan 系数表示，对 r=191 的190个合法位置分别检查 a_j>0、D₂>0、D₃>0，合计 **570项精确整数判号全部通过**；8个 s 的原始 signed 与交替 Catalan 表示各作一次交叉核验，合计16项等式。该整行检查是固定 r 的证据，半无限 PF₃ 推论仍依赖 R450 的数学归约。

## 复现、作用范围、下一问题

运行：python R460_VERIFY.py 167 167；python R460_VERIFY.py 168 168；python R460_ROW_VERIFY.py。R460_EVIDENCE_ALL.json 保存系数摘要哈希、准确输入 pins、每次精确检查及 r=191 证据；哈希用于重现一致性，不表示外部数学审阅。全部计算仅使用 Python 任意精度整数。作者侧报告和文件写入均不授予研究状态机权限。

下一具体单元：检查 s=169、170 的多项式证书以验证 r=193；同时将 Turán 恒等式与 EOR 分解结合，寻找 k、s 同时增长下无需逐个 s 枚举的统一正性下界。出现非正多项式系数时，独立检查整数 k 上的真实子式符号，区分证书方法失效与反例。
