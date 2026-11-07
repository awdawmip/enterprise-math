# R472｜signed BRC 辅助标量右缘 s=241–248：无限 k 正性与 PF₃ 条件性拼接

日期：2026-11-02。作者侧精确整数计算机辅助证明；完整 PF₃ 拼接依赖先前 R447、R450 的未独立审查引理。研究对象仅为 signed BRC **辅助标量** Toeplitz 序列，不作原生 X6/物理动力学归因。

## 冻结来源与精确对象

本轮科学输入沿用 R462 不可变提交 18783e01e3646c72b7aab3b16d3f565e83e6446f；所用 R462 E/O/R 数学内核的 Git blob 为 7c641c985b8c48ef3fb2ddcb2142e38ca0a4ccff，R468 仅提高精确整数多项式乘法效率，其数学内核 Git blob 为 9057a6c46814a06cea45bffc20fe6f44f370b0bb。最后已验证前沿为 R471 Git 提交 c8128da3cf4308afb6a9da3594cfd4c9ce8921cc。

对整数 k≥1，r=2k+1，2≤s≤r，令

$$
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s}.
$$

定义 a_j=H(r,r-j)（0≤j≤r−2），其他整数 j 置零。置

$$
D_{2,j}=a_j^2-a_{j-1}a_{j+1},\qquad
D_{3,j}=\det(a_{j+v-i})_{0\le i,v\le2}.
$$

## 精确证书定理

**R472 定理。** 对每个固定整数 s∈{241,…,248} 及每个整数 k≥k₀=⌊(s+2)/2⌋，取 r=2k+1、j=r−s，则

$$
D_{2,j}>0,\qquad D_{3,j}>0.
$$

**证明。** 置 u=k−k₀≥0，F=(2s+4)!，C_k=(2k)!/(k!(k+1)!)>0。依冻结 E/O/R 恒等式，在整数多项式环构造

$$
Q_t(u)=F H(2k+1,t)/C_k\in\mathbb Z[u],
\quad t=s-2,s-1,s,s+1,s+2.
$$

令 A=Q_s、B=Q_(s−1)、C=Q_(s+1)、D=Q_(s−2)、E=Q_(s+2)，定义

$$
P_2=A^2-BC,\quad
P_3=A^3-2ABC+DC^2+B^2E-DAE.
$$

对八个 s，冻结数学内核与精确乘法器实际计算所有系数并逐项检验严格为正。每个 s 的次数分别为 deg(P₂)=4s、deg(P₃)=6s，待检查正系数数目为 10s+2；八组总计 19,576 项。另逐 s 在 Z[u] 中核对完整 Desnanot–Jacobi 恒等式

$$
A P_3=P_2^2-(B^2-DA)(C^2-AE),
$$

并对 k=k₀,k₀+1 及五个 t 值各做 H 的原始 signed BRC 卷积与独立正 Catalan 表达式交叉核验，各80次。八组系数流SHA256保存在 R472_EVIDENCE.json；可运行 R472_CERTIFY.py 重算全部系数、判号、恒等式与核验。由于 u≥0 且 P₂、P₃ 的每项系数严格正，得到 P₂(u),P₃(u)>0。于是

$$
D_{2,j}=(C_k/F)^2P_2(u)>0,\quad
D_{3,j}=(C_k/F)^3P_3(u)>0.
$$

证毕。证明使用冻结的 E/O/R 与 H 同一性；对此原有解析恒等式的独立审查属于单列的承重依赖。

## 新增四个 r 的整行独立验证

对 r=265,267,269,271，另由 Catalan 整数式

$$
a_{r-s}=\binom{r+s}{2s}
\sum_{q=0}^{\min((r-1)/2,\lfloor(s-1)/2\rfloor)}
\binom{s-1}{2q}4^q C_{(r-1)/2-q}
$$

直接计算每行 j=0,…,r−2 的 a_j、D₂,j、D₃,j，均为严格正整数。每种量各264+266+268+270=1,068项，三种共3,204项。两份独立整行程序的系数流 SHA256 同为 a77d791685011a4d813f68ef1cbafe15295929ff5d9718f8f32017d504f49bcf，子式流 SHA256 同为 fda0320d5ad40eab04885fd051b43c016feea4b3c150ff6c311dfac4e9bdf2c8；各另做32次 raw 与32次交替 Catalan 等式检查。完整机器证据见同目录两个 ROW_EVIDENCE JSON。

## 条件性 PF₃ 拼接与下一问题

依旧作者侧 R447 左缘 j≤22、R471 以前已覆盖的右缘 s≤240，现增至 s≤248。对于奇数 r≤271，若 j≥23 则 s=r−j≤248。结合 R450 对零边界以及半无限 Toeplitz 的局部正性→PF₃ 充分判据，获得**以该旧判据及既有左右缘引理成立为条件**的拼接结论：

$$
T^{(r)}\in PF_3,\qquad r=99,101,\ldots,271.
$$

相对 R471 新增 r=265,267,269,271。其正式数学接纳需独立审查 R447/R450；本轮八组无限 k 正性与四个有限 r 整行判号有可复算的精确整数证书。

下一独立研究单元：检验 s=249,…,256；并列优先问题是独立审查 R450 的零边界到半无限 PF₃ 承重步骤，及寻求 s、k 同时无界时的统一 Turán 下界。若新的系数法出现非正系数，应直接测试合法 k 的真实子式符号，区分证书形式与数学反例。

## 可复现环境与实际权限

从同一 GitHub PR 分支复制 R468 目录下已发布的 R462_VERIFY_FROZEN_KERNEL.py、R468_EXACT_KERNEL.py 与可选的 R468_GMP_ACCELERATOR.c 到本目录。Python 使用任意精度整数；可选先用 gcc -O3 -shared -fPIC R468_GMP_ACCELERATOR.c -o R468_GMP_ACCELERATOR.so -lgmp 编译加速，然后执行 Python R472_CERTIFY.py 241 248、R472_ROW_VERIFY.py、R472_INDEPENDENT_ROW.py。每个 s 可独立运行并汇总；本轮八个 s 已分别运行并严格 PASS。

本轮 GitHub 认证用户为 awdawmip 且可向仓库推送。原生新研究会话因 STATIC_READONLY_SCOPE_DENIED 未建立；owner 列表调用返回 CONTROL_QUOTA。成果仅作为 Draft PR 作者侧研究材料，未提交原生 CLAIM/Result，Driver 未审查。P000 与 ACTIVE 世界观保持原样。
