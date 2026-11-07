# R481 — signed BRC 固定右缘 PF₄ 的渐近符号分类与任意固定阶内部正性

日期：2026-11-02。状态：AUTHOR_SIDE_ANALYTIC_AND_EXACT / DRIVER_UNREVIEWED / NOT_ADMITTED。冻结科学输入：R462@18783e01e3646c72b7aab3b16d3f565e83e6446f；接续 R479@752ed68bd6404267d036761cc412846969f1ec21、R480@a281c82aae5b8f0bbd33a734610c5ad28136a9b9。对象是 signed BRC 来源的辅助标量，保留 P000、ACTIVE 世界观及原生 X6 的独立类型。

## 1. 精确对象与固定右缘极限

对 k≥1、r=2k+1、2≤s≤r，沿用冻结模型

\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s}.
\]

在 s<2、s>r 时置 H(r,s)=0。令 \(C_k=\binom{2k}{k}/(k+1)>0\)。R479 已从原始系数推导可重验的式子

\[
H(2k+1,s)=\binom{2k+1+s}{2s}
\sum_{q=0}^{\lfloor(s-1)/2\rfloor}\binom{s-1}{2q}4^q C_{k-q}.\tag{1}
\]

设 \(a_{r,j}=H(r,r-j)\)。相邻 m 阶 Toeplitz 子式定义为

\[
D_{m,r-s}^{(r)}
=\det(a_{r,r-s+v-i})_{0\le i,v<m}
=\det(H(r,s+i-v))_{0\le i,v<m}.\tag{2}
\]

对固定 t≥2，\(C_{k-q}/C_k\to4^{-q}\)，偶位二项和 \(\sum_q\binom{t-1}{2q}=2^{t-2}\)。因此

\[
\frac{H(r,t)}{C_k r^{2t}}\longrightarrow A_t,\qquad
A_t=\begin{cases}\frac{2^{t-2}}{(2t)!},&t\ge2,\\0,&t<2.\end{cases}\tag{3}
\]

固定 s≥2、m≥1。每个矩阵元素中的 \(r^{2(s+i-v)}=r^{2s}r^{2i}r^{-2v}\) 按行、列提取，行列指数总和抵消。零指标保持为零。逐项取极限得到**精确归一化**：

\[
\boxed{\lim_{\substack{k\to\infty\\r=2k+1}}
\frac{D_{m,r-s}^{(r)}}{C_k^m r^{2ms}}
=L_m(s):=\det(A_{s+i-v})_{0\le i,v<m}.}\tag{4}
\]

该极限使用有限个固定索引系数，无须整体 PF₃ 判据。

## 2. 定理 A：任意固定阶数的内部右缘最终正性

**定理。** 对任意固定整数 m≥1、s≥m+1，有 \(L_m(s)>0\)。因此存在整数 K(m,s)，使全部 k≥K(m,s) 且 r=2k+1≥s 满足 \(D_{m,r-s}^{(r)}>0\)。

**证明。** 此时最小指标 s−(m−1)≥2，故所有 A 指标都有 \(A_t=c_t/4\)，其中 \(c_t=2^t/(2t)!\) (t≥0)。于是

\[
L_m(s)=4^{-m}\det(c_{s+i-v})_{0\le i,v<m}.
\]

Weierstrass 双曲余弦乘积给出

\[
\sum_{t\ge0}c_tz^t=\cosh\sqrt{2z}
=\prod_{n=0}^\infty(1+\lambda_nz),
\quad \lambda_n=\frac{8}{\pi^2(2n+1)^2}>0.\tag{5}
\]

由于 \(\sum_n\lambda_n<\infty\)，有 \(c_t=e_t(\lambda_0,\lambda_1,\ldots)\)，即第 t 个初等对称函数。矩阵转置及**对偶 Jacobi–Trudi 恒等式**给出矩形分拆 \((m^s)\) 的 Schur 函数

\[
\det(c_{s+i-v})_{0\le i,v<m}
=s_{(m^s)}(\lambda_0,\lambda_1,\ldots).\tag{6}
\]

Schur 函数按半标准 Young 表展开为非负单项式之和。第 i 行（1≤i≤s）全部填 i 的表合法，贡献 \(\lambda_0^m\lambda_1^m\cdots\lambda_{s-1}^m>0\)。取任何 N≥s 个变量，该正项已经出现；N→∞ 保持严格正性。故 \(L_m(s)>0\)，再由式 (4) 推出所述阈值存在性，证毕。

这一结论适用于每个固定 m 的无限参数族，右缘 s≥m+1。

## 3. 定理 B：四阶固定右缘的完整渐近符号分类

**定理。** 对全部固定整数 s≥2，

\[
\boxed{L_4(3)<0,\quad L_4(2)>0,\quad L_4(s)>0\ \ (s\ge4).}\tag{7}
\]

**证明。** 对 s≥5，定理 A (m=4) 直接给出严格正。对可能受到 s<2 截断影响的 s=2,3,4，将式 (4) 的四阶有理数行列式完全展开得到：

\[
\begin{aligned}
L_4(2)&=\frac{1}{331776}>0,\\
L_4(3)&=-\frac{31}{144850083840000}<0,\\
L_4(4)&=\frac{50137}{32884851013926912000000}>0.
\end{aligned}\tag{8}
\]

于是对每个固定 s≥2，所有充分大的奇数 r 的 \(D_{4,r-s}^{(r)}\) 具有相应严格符号。阈值允许依赖 s；本定理是固定 s 的逐点分类。R479 对唯一渐近负的固定位置 s=3 还有精确阈值：全部 k≥49 时 \(D_{4,r-3}^{(r)}<0\)。

## 4. 精确复现、来源与范围

同目录 R481_VERIFY.py 用 Python 标准库、Fraction、任意精度整数，以两个独立表达式完成250项原始 signed 系数卷积与 Catalan 式 (1) 逐项相等检查（2≤k≤21、2≤s≤min(r,15)）。对 s=2,…,30 计算极限常数，核对三个精确有理数及 s≥5 的矩阵恒等式与正号。另对 k=4,…,100、2≤s≤min(12,r)，直接完成1,063项原始整数四阶行列式检查，全部符合 s=3、k≥49 为负、其余被检项目为正。输出 R481_EXACT_PASS，摘要在 R481_EVIDENCE.json；一般无限参数结论依靠第1–3节解析推导，不以有限枚举代替证明。

科学类型为 signed BRC 辅助标量 Toeplitz；本轮结果是直接行列式结论，不依赖 R441-A/R474 的全局 PF₃ 归约，不改变原生 X6。保留 frozen R462 科学 pin 与 R479/R480 的来源关系，正式 Source 接纳、Owner 身份及独立 Driver 审核分别按实际权限处理。

下一最小问题：为 m=4、s≥4 给出**可计算**的 K(m,s)，检验有限 k 上是否有隐藏的四阶负性；研究 s 随 r 共同增长时的符号过渡带，并另线改进 R480 的对数增长左缘窗口。
