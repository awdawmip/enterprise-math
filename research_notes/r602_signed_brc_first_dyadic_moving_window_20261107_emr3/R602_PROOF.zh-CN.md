# R602 — 首个跨越半径 13 的 dyadic 增长窗口：显式误差及复零点匹配证书

2026-11-07 · AUTHOR_SIDE_EXACT_ANALYTIC_CERTIFICATE · DRIVER_UNREVIEWED · NOT_ADMITTED

## 科学范围与冻结源

母目标：冻结 signed BRC 十二支路的增长逆谱与全谱正型能量 V_k 规律。冻结科学输入为 R462 @18783e01e3646c72b7aab3b16d3f565e83e6446f；本研究仅处理它的 Toeplitz–Hessenberg **辅助标量观察者**，保持原生 X6、符号、分支、联合关系、相位、路径与 provenance 的独立类型。承重作者侧来源：R590 @研究目录 research_notes/r590_signed_brc_moving_disk_20261107_emr3，R600 @468d87978cb4b4ba2ebb1530b0e3a004ff5e648b，R601 @03810fd313161818d66298f92dd6f5860e1ee21c，R593 首对非实根圆盘计数。

设 k 是整数 ≥2，d=2k−1，精确 Catalan 辅助多项式
\[
 F_k(z)=\sum_{j=0}^{d}(-1)^j a_{k,j}z^j,\qquad
 F(z)=\sum_{j\ge0}(-1)^j a_jz^j,\quad
 a_j=\frac{24\cdot8^j}{(2j+4)!}.
\]
其中 a_{k,j} 是 R590 原始 H_k 定义的系数，不改变冻结输入。令
\[
 k=2^{42}=4398046511104,\quad c=\frac1{64},\quad
 \rho_k=c(\log k)^2,\quad R=14,\quad X=R+\frac18=\frac{113}{8},\quad L=64.
\]

## 定理 A：第一个跨越 13 的 dyadic 窗口

严格有
\[
 13<\rho_k<14,\quad
 \rho_{2^{41}}=\frac{(41\log2)^2}{64}<13.
\]
所以在固定 c=1/64、k 取 2^n、n≥1 的族中，k=2^42 是第一个满足 \(\rho_k>13\) 的参数。

证明：从恒等式 \(\log2=2\sum_{m\ge0}3^{-(2m+1)}/(2m+1)\)，截断和几何尾界给出
\[
 \frac{56}{81}<\log2<\frac{25}{36}.
\]
于是只需验证三条完全有理数不等式：
\((42\cdot56/81)^2>64\cdot13\)、
\((42\cdot25/36)^2<64\cdot14\)、
\((41\cdot25/36)^2<64\cdot13\)。
前两个推出 rho_k 在 (13,14)，第三个及 n↦rho_{2^n} 的单调性证得最小 dyadic 指数。

## 定理 B：固定有限 k 的显式整圆盘误差

在整个闭圆盘 \(|z|\le113/8\) 上，
\[
 \boxed{\sup_{|z|\le113/8}|F_k(z)-F(z)|\le U<\frac1{6720}},
\]
其中 U 是下面两个明确有理数之和，且只需要有限阶乘与整数幂：
\[
 S=\frac{3L}{2k}+\frac{L(L+1)(L+5)}{12k^2},\quad
 B=\frac{3(L+1)}{2(2k-L)},\quad E=S+B,
\]
\[
 U_{\rm low}=24\cdot3^{11}\frac{E}{1-E},\qquad
 U_{\rm tail}=24\bigl[1+21(k+1)(2k+1)\bigr]
 \frac{100}{99}\frac{113^{65}}{130!},\qquad
 U=U_{\rm low}+U_{\rm tail}.
\]
脚本以精确 Fraction 验证 \(0<E<1,\ U<1/6720\)。近似值 U≈0.000139927733，仅作阅读展示。

**解析证明。** R590 的原始 Catalan 公式精确给出（0≤j≤d）
\[
 \frac{a_{k,j}}{a_j}=
 P_{k,j} W_{k,j},\quad
 P_{k,j}=\prod_{h=1}^{j}
 \left(1+\frac{h+3}{2k}\right)\left(1-\frac h{2k}\right),
\]
\[
 W_{k,j}=2^{-j}\sum_{q=0}^{\lfloor(j+1)/2\rfloor}
 {j+1\choose2q}\,R_{k,q},\quad
 R_{k,q}=\prod_{h=0}^{q-1}
 \left(1+\frac3{2(k-h)-1}\right).
\]
对 0≤j≤L=64，每对乘积是 \(1+x_h\)，
\(x_h=3/(2k)-h(h+3)/(4k^2)>0\)（因 \(6k>L(L+3)\)），
故 \(1\le P_{k,j}\le e^S\)。
若 \(q\le (L+1)/2\)，每个递推分母 \(2(k-h)-1\ge2k-L\)，于是
\[
 1\le R_{k,q}\le
 \exp\left[\frac{3q}{2k-L}\right]
 \le e^{B}.
\]
偶二项式权重满足 \(2^{-j}\sum_q{j+1\choose 2q}=1\)，
故 \(1\le W_{k,j}\le e^B\)，进而 \(0\le a_{k,j}/a_j-1\le e^E-1\le E/(1-E)\)。

低阶误差由
\[
 \sum_{j=0}^{L}a_j X^j
 \le24\sum_{j\ge0}\frac{(8X)^j}{(2j)!}
 =24\cosh\sqrt{113}
 <24e^{11}<24\cdot3^{11}
\]
控制，因此不超过 \(U_{\rm low}\)。

高阶对每个 \(j>L\) 复用 R590 已证全阶包络
\(a_{k,j}\le21(k+1)(2k+1)a_j\)，以及
\(a_j X^j\le24b_j,\ b_j=113^j/(2j)!\)。
由于 \(b_{j+1}/b_j=113/[(2j+2)(2j+1)]<1/100\) 对所有 j≥65 成立，
\[
 \sum_{j>L}a_j X^j+\sum_{L<j\le d}a_{k,j}X^j
 \le 24[1+21(k+1)(2k+1)]\frac{100}{99} b_{65}
 =U_{\rm tail}.
\]
三角不等式对整个闭圆盘给出 \(\sup|F_k-F|\le U\)，
精确有理数验证 \(U<1/6720\) 完成证明。

注：上面的 Catalan 递推上界显式使用分母 \(2k-L\)，与 R590 概括渐近式中的宽松统一常数无关；本证书是对固定巨大整数 k 的直接有限证明，不假定一个未写出的 big-O 阈值。

## 定理 C：增长窗口的首对复根及全部极限根的显式匹配

由 R601 作者侧统一局部 Rouché 定理（其导数与间距前提来自 R600），取 \(R=14\)、
\(\eta=U\)。因 \(\sqrt{14}<4\)，
\[
 \eta<\frac1{6720}<\frac1{48\cdot56}
 <\frac1{48\cdot14^{3/2}},
\quad
 \delta=6\cdot14^{3/2}\eta<336U<\frac1{20}.
\]
因此每个 F-零点 \(|\zeta|\le14\) 在开圆盘 \(B(\zeta,1/20)\)
内匹配一个唯一的简单 \(F_k\) 零点；匹配圆盘两两不交，
共轭结构保留。尤其 R593 在 \(|z|<13\) 严格计数得到的首对非实
共轭 F-零点，因 \(13<\rho_k<14\)，现有对应的两个 \(F_k\) 简单根，
位移均严格小于 1/20。R601 还给出匹配集合的二次虚部读出扰动界，
可代入这个新 δ 数值。

这里的结论是所有极限根 \(|\zeta|\le14\) 的**单向匹配**；
若要证明半径 14 内 \(F_k\) 没有额外根，需独立好圆周计数。并且
这只是辅助标量观察谱：原生十二支路、全谱 V_k 尾能量仍作为母问题继续研究。

## 验证边界及下一问题

实际执行 R602_VERIFY.py；用整数、Fraction、factorial 对 log 窗口、
低阶 E、全阶尾界和 \(U<1/6720\)、\(336U<1/20\)
作精确比较。原始终止标记 R602_ALL_EXACT_CERTIFICATES_PASS；
运行记录在 R602_EVIDENCE.txt。无限根存在性及 Rouché 结论依赖
上述分析及 R600/R601 的作者侧证明，并未被有限计算代替。

下一问题：在 \(\rho_k\in(13,14)\) 与邻近的可认证半径上，
结合 R591 的好圆周方法构造 \(F_k\) 无遗漏零点计数；优化低阶
\(\sum a_jX^j\) 的精确估计，将首个可认证 k 降低多个数量级；
再结合根对计数推进增长能量求和及全谱谱尾。
