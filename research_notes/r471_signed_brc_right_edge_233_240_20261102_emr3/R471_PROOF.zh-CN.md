# R471｜signed BRC 辅助标量右缘 s=233–240：无限 k 正性证书与 PF₃ 条件拼接

日期：2026-11-02。成果性质：作者侧任意精度整数计算辅助证明；正式独立 Driver 审查与原生任务接纳尚待完成。

## 冻结来源与研究对象

科学输入沿用 R462 不可变提交 18783e01e3646c72b7aab3b16d3f565e83e6446f，原始 E/O/R 内核 R462_VERIFY_FROZEN_KERNEL.py Git blob 7c641c985b8c48ef3fb2ddcb2142e38ca0a4ccff。复用 R468_EXACT_KERNEL.py Git blob 9057a6c46814a06cea45bffc20fe6f44f370b0bb 的精确大整数多项式乘法（可选 GMP 加速），不改变冻结数学对象。接续 R470 发布提交 965891958485e9ef0a0d287842e49f2ecaf3e2a7。

本轮读取的行为规则快照为 GLOBAL_KNOWLEDGE_V1 main@b29cc9f16cf53151b9c0b175e9c6be31ff49711f、Enterprise Math main@5dd2761cf80f91a074013f5bb192d09626d3bd87。P000、ACTIVE 世界观、portable 协议和 current-normative-context 适用规则保持原义，P000/世界观未修改。本对象只属于 signed BRC 辅助标量模型，不推断原生 X6 物理动力学。

## 定理：八个 s 的全部合法 k

给定整数 k≥1，令 r=2k+1，2≤s≤r，并定义

\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\qquad
C_k=\frac{\binom{2k}{k}}{k+1}>0.
\]

对固定 r 设 a_j=H(r,r-j)（0≤j≤r−2），其余整数 j 处 a_j=0。令

\[
D_{2,j}=a_j^2-a_{j-1}a_{j+1},\quad
D_{3,j}=\det(a_{j+v-i})_{0\le i,v\le2}.
\]

**定理 R471：** 对每个固定整数 s∈{233,234,235,236,237,238,239,240}，以及全部整数 k≥k₀=⌊(s+2)/2⌋，记 r=2k+1，j=r−s，则 D₂,j>0、D₃,j>0。

**证明（精确整式证书）：** 固定 s，设 u=k−k₀≥0、F=(2s+4)!。冻结 R462 E/O/R 恒等式给出五个整数多项式

\[
Q_t(u)=F\,H(2k+1,t)/C_k\in\mathbb Z[u],
\qquad t=s-2,\ldots,s+2.
\]

记 A=Q_s，B=Q_(s−1)，C=Q_(s+1)，D=Q_(s−2)，E=Q_(s+2)。完整展开得到

\[
P_2=A^2-BC,\quad
P_3=A^3-2ABC+DC^2+B^2E-DAE.
\]

本轮实际完整计算每个 s 的 P₂、P₃；所有系数严格为正整数，次数分别为 4s、6s，八参数总共 (∑(10s+2))=18,936 个正系数。并逐 s 精确检查

\[
A P_3=P_2^2-(B^2-DA)(C^2-AE)
\]

这八个 Desnanot–Jacobi 完整整式恒等式。在每个 s 的 k=k₀、k=k₀+1，对 t=s−2,…,s+2 交叉检验原始 signed BRC 交替卷积与正 Catalan 表达式，各 80 次。每个系数流 SHA256 见 R471_EVIDENCE.json；冻结 R462 的 s_certificate() 定义完整的无歧义序列化方式。

因 u≥0 且 P₂、P₃ 全系数为正，P₂(u)、P₃(u)>0；由

\[
D_{2,j}=(C_k/F)^2P_2(u),\quad D_{3,j}=(C_k/F)^3P_3(u)
\]

和 C_k/F>0 即得结论。以上有限完整系数证书分别证明八个 s 对应无限多个合法 k。QED。

## 新增四个 r 的整行独立检验

在 r=257、259、261、263，用 Catalan 正式

\[
a_{r-s}=\binom{r+s}{2s}\sum_{q=0}^{\min((r-1)/2,\lfloor(s-1)/2\rfloor)}
\binom{s-1}{2q}4^q C_{(r-1)/2-q}
\quad(2\le s\le r)
\]

生成全部系数，检查各行所有 j=0,…,r−2 的 a_j、D₂,j、D₃,j，零填充边界包括在内。每类严格正值有 256+258+260+262=1,036 个，合计 **3,108 项精确整数符号判定通过**。另在每行八个 s 点交叉核验 32 项原始 signed 卷积和 32 项交替 Catalan 式。两份独立验证程序得到相同的系数流 SHA256 88b8ee876a98654ef9d2a1b4f70008026ea21125789e1bf36d567dc6e84fe0d3，子式流 SHA256 f510e8c99231f642f5e8fadb707e2bb5d1a0f6e6a5ae19174058e3e33d872742。

## 条件性 PF₃ 结论、权限与下一问题

既有作者侧左缘 j≤22、右缘 s≤232 已覆盖至 r=255；本轮拓展 s≤240，因奇数 r≤263 时 j≥23 蕴涵 s=r−j≤240，左右缘相邻 D₂、D₃ 的覆盖拼接成立。**在 R447、R450 以前作者侧引理及 R450 半无限 Toeplitz PF₃ 局部充分判据成立的前提下**，推出 T^(r)∈PF₃，所有奇数 99≤r≤263；本轮新增 257、259、261、263。完整 PF₃ 推导承重引理待独立审阅，本轮八组全 k 局部子式正性具备完整整式计算证书。

复现：将本目录的 R471_CERTIFY.py、R471_ROW_VERIFY.py、R471_INDEPENDENT_ROW.py 与已发布且 Git blob 固定的 R462_VERIFY_FROZEN_KERNEL.py、R468_EXACT_KERNEL.py 置于同一目录。逐 s 执行 python R471_CERTIFY.py 233 233 至 python R471_CERTIFY.py 240 240；另执行 python R471_ROW_VERIFY.py、python R471_INDEPENDENT_ROW.py。可按 R468 说明编译 R468_GMP_ACCELERATOR.c 得到可选精确加速库。无需浮点误差论证。

本轮 GitHub 身份 awdawmip、仓库 push=true；原生 em_session_start 返回 STATIC_READONLY_SCOPE_DENIED、operation_sent=false；活跃 Owner 查询返回 CONTROL_QUOTA；正式 CLAIM、Result 和独立 Driver 接纳均待处理。

下一研究单元：s=241–248 的精确整式系数证书；独立审查 R450 的局部到整体 PF₃ 判据；探索同时无界 s、k 的 Turán 解析正性结构。
