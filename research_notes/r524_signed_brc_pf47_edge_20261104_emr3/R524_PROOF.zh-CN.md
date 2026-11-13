# R524 — signed BRC 辅助标量四十七阶 Toeplitz 子式：全正整数参数符号分类与阶数生成函数

日期：2026-11-04。冻结科学输入 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f；前沿 R523@56a79af2628cd4fd7f0b2b2c4b85ea31b505b1e7。状态 AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED。

## 条件定理 A — m=47 的全正整数参数

设整数 $k\ge1$、$r=2k+1$、$C_k=\binom{2k}{k}/(k+1)>0$，并定义

$$H_k(t)=\binom{r+t}{2t}[x^r](1-x)(1+x)^{2t}(1+x^2)^{r-t}\quad(2\le t\le r),$$

其余整数 $t$ 上取零。令 $D_m(k)=\det(H_k(3+i-j))_{0\le i,j<m}$，$D_0=1$。沿用冻结 R452/R462 的关键引理：每个固定整数 $t\ge2$ 的 $p_t(k)=H_k(t)/C_k$ 在正整数上等于次数不超过 $2t$ 的有理多项式。

在此前提下，**$D_{47}(k)>0$ 当 $1\le k\le7$ 或任意整数 $k\ge21$；$D_{47}(k)<0$ 当 $8\le k\le20$**。相应奇数参数 $r$ 从 **43** 起永久严格为正，正整数域无零点。结合 R523 的结论，得到 $D_{46}(8)>0>D_{47}(8)$，以及 $D_{46}(k)<0<D_{47}(k)$ 对所有 $21\le k\le55$ 成立。

## 精确多项式证书及无限尾部证明

Toeplitz–Hessenberg 展开给出 $f_0=1$ 以及

$$f_m=\sum_{a=1}^{m}(-1)^{a-1}p_{a+2}p_2^{a-1}f_{m-a},\qquad f_m=D_m/C_k^m.$$

由冻结引理归纳 $\deg f_m\le6m$，于是 $\deg f_{47}\le282$。取对 $k\ge1$ 严格正的

$$G(k)=[k(k+1)(2k+1)(2k+3)]^{47}(k+2),\qquad\deg G=189.$$

对 $k=1,\ldots,94$ 精确求 $f_{47}(k)/G(k)$ 的约分分母最小公倍数 $L>0$，令 $\delta_j=\Delta^j[L f_{47}/G](1)$，$0\le j<94$。定义 $S(k)=\sum_{j=0}^{93}\delta_j\binom{k-1}{j}$，故 $\deg(GS)\le189+93=282$。

JavaScript BigInt 在 **283 个互异整数点 $k=1,\ldots,283$** 逐点检查

$$L D_{47}(k)=C_k^{47}G(k)S(k).$$

除以正的 $C_k^{47}$，等号两边是次数不超过282的有理多项式，因而是恒等式。完整 $L$、94项 $\delta_j$、尾部差分和有限点 $S(k)$ 均见 R524_EVIDENCE.json。

证书显示 $S(1),\ldots,S(7)>0$，$S(8),\ldots,S(20)<0$；以 $k=21$ 为原点，**全部94个** $\varepsilon_j=\Delta^j S(21)$ **严格为正**。对任意整数 $u\ge0$，

$$S(21+u)=\sum_{j=0}^{93}\varepsilon_j\binom{u}{j}>0,$$

因为二项式系数非负且 $\varepsilon_0>0$。结合 $L,G,C_k>0$ 得全正整数符号结论。该证明为依赖冻结固定 $t$ 多项式引理的精确计算辅助证明。

## 定理 B — 固定参数的有理阶数生成函数

固定任意整数 $k\ge1$，记 $p=H_k(2)>0$、$h_a=H_k(a+2)$，定义

$$A_k(z)=\sum_{a=1}^{r-2}(-1)^{a-1}h_a p^{a-1}z^a.$$

在形式幂级数环 $\mathbb Z[[z]]$ 中，

$$\boxed{\sum_{m\ge0}D_m(k)z^m=\frac{1}{1-A_k(z)}.}$$

证明：同一 Toeplitz–Hessenberg 首行展开对原始行列式直接给出 $D_0=1$ 与 $D_m=\sum_{a=1}^m(-1)^{a-1}h_ap^{a-1}D_{m-a}$；$h_a=0$ 当 $a>r-2$。乘以 $z^m$ 求和即得公式。$h_{r-2}=H_k(r)=\binom{2r}{r}-\binom{2r}{r-1}=C_r>0$，$p>0$ 可由 ballot–Catalan 表达式验证，故分母次数恰为 $r-2=2k-1$。分子为1，不发生约分；这是固定 $k$ 下该序列的最小线性递推阶数。

此结构把逐个 $m$ 的符号转换转化为有限分母及其代数极点问题。跨参数的主导根排序尚需单独证明。

## 原始 signed BRC 核验、范围与下一步

R524_VERIFY.js 返回 R524_EXACT_JS_PASS：283项整点多项式恒等式、20项原始47×47 Bareiss 行列式和940项原始有符号系数／ballot–Catalan 对照。作者侧独立的 Python/SymPy Berkowitz 从原始有符号矩阵计算 $k=1,\ldots,21,55,56$ 共23项，包括两处换号边界7/8、20/21；另有1081项公式交叉检查，R524_INDEPENDENT_PASS。运算均为精确整数；正式独立 Driver 数学审阅及原生 CLAIM/Result 尚未完成。

对象为冻结 R462 的 **signed BRC 辅助 Toeplitz 标量模型**。没有把标量证明提升为原生 X6 物理动力学或残差归因，也没有修改 P000 或 ACTIVE 世界观。

下一科学问题：固定 $k=7,8,20,21$，对 $1-A_k(z)$ 进行精确代数根与主导极点分析；另可接续 $m=48$ 的全正整数符号分类（次数上界288、96项 Newton 差分、289点精确恒等式）。
