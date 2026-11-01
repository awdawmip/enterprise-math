# R468｜signed BRC 辅助标量右缘 s=209–216 的无限参数正性证书与条件性 PF₃ 拼接

日期：2026-11-02。状态：AUTHOR_SIDE_EXACT_SYMBOLIC_AND_INTEGER / DRIVER_UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。

## 固定规范、科学对象与命题

本轮读取同一 GLOBAL_KNOWLEDGE_V1 canonical main@5cef4755fe796ca26a3014112791967d8d5ad6cc；Enterprise Math main@3c5f59dd53d611b617195753254f2a8791073557。科学输入保持冻结 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f；接续 R467@9c555bc4e8b5bc071e9fc48794350230a676fa4d。P000、ACTIVE 世界观未修改。所有结论针对 signed BRC 辅助标量模型，并未将其当作原生 X6 动力学。

对奇数 r=2k+1 与 2≤s≤r 定义

\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad C_k=\frac{\binom{2k}{k}}{k+1}>0.
\]

定义 a_j=H(r,r-j)（0≤j≤r−2；其余位置补零）。令 D_{2,j}=a_j^2-a_{j-1}a_{j+1}，D_{3,j}=\det(a_{j+v-i})_{i,v=0}^{2}。

**R468 定参数无限 k 命题**：对于每个固定整数 209≤s≤216，对全部整数 k≥k₀=⌊(s+2)/2⌋，取 j=2k+1−s，均有 D_{2,j}>0 与 D_{3,j}>0。

## 可复算的有限符号证书与论证

沿用 R462 的 E/O/R 精确代数恒等式，令 u=k−k₀≥0、F=(2s+4)!，并令 Q_t(u)=F H(2k+1,t)/C_k∈ℤ[u]（t=s−2,…,s+2）。设 A=Q_s、B=Q_{s−1}、C=Q_{s+1}、D=Q_{s−2}、E=Q_{s+2}。

直接按 Toeplitz 行列式展开：

\[
P_2=A^2-BC,\quad P_3=A^3-2ABC+DC^2+B^2E-DAE.
\]

冻结数学内核与本轮精确整数卷积程序在每个 s=209,…,216 上完整展开 P₂ 与 P₃；得到 deg(P₂)=4s、deg(P₃)=6s，**每一个整数系数严格为正**。八个 s 共16个多项式、17,016个严格正系数。由于 u≥0，P₂(u)>0、P₃(u)>0；且 D₂=C_k²P₂/F²、D₃=C_k³P₃/F³，故定参数命题对所有合法 k 成立，而不只是有限整数点测试。

为防止仅依赖同一行列式展开，对每个 s 精确核验完整 Desnanot–Jacobi 多项式恒等式
\[
A P_3=P_2^2-(B^2-DA)(C^2-AE).
\]
共8次。另在 k=k₀,k₀+1 与五个 t=s−2,…,s+2 的80组输入上，分别对照原始 signed 系数卷积及正 Catalan 求和（各80次），全通过。R468_EVIDENCE_ALL.json 给出每个 s 的次数、严格正系数数目和系数流 SHA256。R468_CERTIFY.py 是实际执行的定参数检查入口。

## 条件性 PF₃ 拼接推进至 r=239

复用此前 R447 作者侧左缘 0≤j≤22，以及 R452–R467 右缘 2≤s≤208；本轮增加 209≤s≤216。对所有奇数 99≤r≤239，j≥23 时 s=r−j≤216，因此左右覆盖全部相邻位置。若采用尚待独立审查的 R450 局部充分判据及此前作者侧依赖，得到**条件性**半无限 T^(r)∈PF₃，r=99,101,…,239；相比 R467 新增 r=233,235,237,239。

另外，R468_ROW_VERIFY.py 使用另一套正 Catalan 整数表达式直接构造 r=233,235,237,239 的完整零延拓行，对全部 940 个系数、940 个二阶相邻子式、940 个三阶相邻子式共2,820项精确整数做严格正性检查，并完成32项原始卷积及32项交替 Catalan 等式对照。两套整数流 SHA256 分别为 bdd913270590e0c4793d6be5c2ea94435d447dde71b71210fc5a409919100d29 和 f54e747ff1276b587868155b63ce7153b8e18ef3e5121a12c239de4f55a6866d，逐行位数及结果在 R468_ROW_EVIDENCE.json。

## 计算工具改进与精确验证

本轮将 R462 中计算 R 多项式时重复的线性因子乘积预先组织成 prefix/suffix 递推；E、O、R 采用平衡树乘法。多项式系数仍处于 ℤ[u]，未改变冻结数学定义。采用可处理负系数的平衡 Kronecker 整数打包，令位宽 w=bit_length((Σ|a_i|)(Σ|b_j|))+2，并以平衡位元解包；因为 |(ab)_n|≤(Σ|a_i|)(Σ|b_j|)<2^(w−1)，每一个整数系数都能无歧义恢复。可选 GCC/GMP 仅优化大整数乘法，纯 Python 退化路径也为精确整数运算。

实际验证：400项随机小尺寸多项式卷积与常规整数卷积一致；100项随机有符号大整数 GMP 与 Python 对照一致；s=175 的既有 R463 精确系数流哈希回归为 5a68b3d2ced114ee7744e5a75b8553717314a3d0ea1b5b497b0739ba09847239，与 R463 一致。八个新 s 各自完成原始卷积核验、完整正系数判号和 Desnanot–Jacobi 恒等式。冻结 R462 数学源码复制为 R462_VERIFY_FROZEN_KERNEL.py；当前目录中的 R468_EXACT_KERNEL.py、R468_CERTIFY.py、R468_ROW_VERIFY.py、R468_GMP_ACCELERATOR.c 可完整复现。

运行：在该研究目录下，可选使用 gcc -O3 -shared -fPIC R468_GMP_ACCELERATOR.c -o R468_GMP_ACCELERATOR.so -lgmp；然后依次执行 python R468_EXACT_KERNEL.py、python R468_CERTIFY.py 209 216、python R468_ROW_VERIFY.py。无 GMP 编译模块时自动使用 Python 原生大整数，正确性不变但明显变慢。

## 当前权属与后续问题

GitHub 认证身份 awdawmip 具有仓库 push 权限。原生研究服务的 em_session_start 返回 STATIC_READONLY_SCOPE_DENIED / operation_sent=false；活跃 Owner 查询返回 CONTROL_QUOTA。因此当前研究属于可回读的作者侧材料，尚无正式 CLAIM、Result、独立 Driver Review 或 Foundation 接纳。

下一科学单元：检查 s=217–224 对应精确多项式证书；同时针对 R447/R450 作者侧依赖开展独立定义与行列式充分性核查，并沿 E/O/R–Turán 凝聚寻找 s、k 同时无界增长时的统一正性论证。若某个正系数证书失败，先检验合法 k 下真实子式的符号，再判断是证书方法局限还是数学反例。
