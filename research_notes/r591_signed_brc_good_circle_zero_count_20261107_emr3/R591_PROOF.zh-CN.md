# R591｜辅助整函数的显式好圆周与增长窗口零点计数

日期：2026-11-07；状态：AUTHOR_SIDE_ANALYTIC_PROOF，独立数学 Driver 审阅待完成。

## 来源与模型

冻结科学输入：R462 @ 18783e01e3646c72b7aab3b16d3f565e83e6446f。沿用 R590 @ 88406fcfe23c2c23c2c27887b87613f8dcd6031a 对辅助 Toeplitz–Hessenberg 标量观察者的原始定义：

\[
F_k(z)=\sum_{j=0}^{2k-1}(-1)^j\frac{H_k(j+2)}{H_k(2)k^{2j}}z^j,\quad
F(z)=24\sum_{j\ge0}\frac{(-8z)^j}{(2j+4)!},\quad F(0)=1.
\]

原始 Catalan 数求和定义 H_k、冻结支路和基函数来源均在 R590 证明文件。该文件已经证明：对每个固定 0<a<1/8，

\[
\sup_{|z|\le a(\log k)^2}|F_k(z)-F(z)|
=O_a(k^{-1+\sqrt{8a}}\log k).\tag{R590}
\]

本文只研究辅助标量整函数的零点；原生六轴/十二条带符号 BRC 支路及联合观察仍保持冻结来源和 P000 的类型要求。

## 定理 A：每个倍增环带都有可量化的好圆周

对任何实数 R≥1，存在实数 rho∈(R,2R)，满足

\[
\boxed{\min_{|z|=\rho}|F(z)|\ge\exp(-144\sqrt R)>0.}\tag{A}
\]

**证明。** 写 N_F(r) 为 F 在闭盘 |z|≤r 中的零点个数（计重数）。从 Taylor 级数直接得到

\[
M_F(r)\le24\sum_{j\ge0}\frac{(8r)^j}{(2j)!}
=24\cosh\sqrt{8r}\le24e^{\sqrt{8r}}.
\]

由于 F(0)=1，Jensen 公式对 r≥1 给出

\[
N_F(r)\log2\le\log M_F(2r)\le\log24+4\sqrt r
\le8\sqrt r,\qquad
\boxed{N_F(r)\le12\sqrt r.}\tag{1}
\]

F 的增长阶≤1/2，故由 Hadamard 分解，且 F(0)=1，

\[
F(z)=\prod_{\zeta:F(\zeta)=0}(1-z/\zeta).\tag{2}
\]

所有根逐重计数。由 (1) 可知 Σ_\zeta |\zeta|^{-1}<∞，因此是收敛的零阶典范乘积，没有非恒定指数因子。

对每个零点写 u_\zeta=|\zeta|，并对 rho∈[R,2R] 记

\[
L(\rho)=\sum_\zeta\log|1-\rho/u_\zeta|.
\]

除去可数个 rho=u_\zeta 的位置，反三角不等式逐因子给出

\[
\log|F(z)|\ge L(\rho)\quad\text{对所有 }|z|=\rho.\tag{3}
\]

按 u_\zeta 的大小积分估计：

（i）u<R/2 时，rho/u≥2，因此 log|1-rho/u|≥0。

（ii）R/2≤u≤4R，令 v=u/R∈[1/2,4]、x=rho/R，则

\[
\frac1R\int_R^{2R}\log|1-\rho/u|\,d\rho
=\int_1^2\log|x-v|\,dx-\log v
\ge-2-\log4>-4.\tag{4}
\]

理由是区间上负对数部分的积分最多为 ∫_{-1}^{1}(-log|y|)dy=2。
由 (1)，u≤4R 的零点不超过 N_F(4R)≤24√R 个，故它们平均贡献≥-96√R。

（iii）u>4R，则 rho/u≤1/2，因 log(1-t)≥-2t（0≤t≤1/2），每项平均贡献≥-4R/u。利用 (1) 的计数上界及 Stieltjes 分部积分，

\[
\sum_{u_\zeta>4R}u_\zeta^{-1}
\le\int_{4R}^{\infty}\frac{N_F(t)}{t^2}dt
\le12\int_{4R}^{\infty}t^{-3/2}dt
=\frac{12}{\sqrt R}.\tag{5}
\]

所以远零点贡献≥-48√R。乘积的局部收敛与上述积分界保证 L 可积（有限个对数奇点具有可积性）。结合 (3)–(5) 得

\[
\frac1R\int_R^{2R}L(\rho)\,d\rho\ge-144\sqrt R.
\]

从而存在内点 rho 使 L(rho)≥-144√R，对所有 |z|=rho 代回 (3) 即得 A。证毕。

## 定理 B：无条件的对数平方增长窗口零点匹配

取**显式常数 c=1/40000**。对所有充分大的整数 k，存在

\[
\boxed{\rho_k\in(c(\log k)^2,2c(\log k)^2)}
\]

满足 F_k、F 在 |z|<rho_k 内的复零点数**严格相等**（计重数）。该圆周还满足

\[
\min_{|z|=\rho_k}|F(z)|\ge k^{-0.72},\quad
\sup_{|z|\le\rho_k}|F_k(z)-F(z)|=O(k^{-0.98}\log k).\tag{6}
\]

**证明。** 取 R_k=c(log k)^2，充分大 k 时 R_k≥1。定理 A 提供 rho_k 与下界

\[
e^{-144\sqrt{R_k}}=k^{-144/200}=k^{-0.72}.
\]

在 (R590) 中置 a=2c=1/20000<1/8，对 |z|≤2R_k 得

\[
\sup|F_k-F|
=O_{2c}(k^{-1+\sqrt{16c}}\log k)
=O(k^{-0.98}\log k).
\]

两者比值为 O(k^{-0.26}log k)→0，故充分大 k 时整个选定圆周满足 |F_k-F|<|F|。由 Rouché 定理精确匹配圆盘中的零点数。证毕。

**推论 C：一个逐渐增大的零点集合得到匹配。** F 有无限个非零 Taylor 系数，因此不是多项式。F 的增长阶≤1/2；若只有有限零点，Hadamard 分解将使其成为常数倍多项式，矛盾。因此 F 有无限多根。rho_k→∞，结合 (1) 与定理 B，

\[
\boxed{N_{F_k}(\rho_k)=N_F(\rho_k)\to\infty,\qquad
N_{F_k}(\rho_k)\le12\sqrt{2c}\log k=O(\log k).}
\]

这是一项存在性的圆周选择定理，不要求事先固定 rho_k 的数值。

## 独立有限精确证书

R591_VERIFY.py 使用原始 Catalan H_k 求和、整数与 Fraction 构造 F_k，采用精确有理数计算圆周上界：

\[
\sup_{|z|=r}|F_k-F|\le
\sum_{j=0}^{2k-1}|a_{k,j}-a_j|r^j+\sum_{j\ge2k}a_jr^j;
\quad
\min_{|z|=r}|F|\ge1-\sum_{j\ge1}a_jr^j.
\]

用相邻项比值的严格几何级数上界控制两个无限尾项。对 k=8、16、32、64 与 r=1、2 的八组输入，均严格通过有理数版 Rouché 判据，证明所涉有限圆盘双方都无零点。R591_EVIDENCE.txt 保存真实程序输出；无限窗口结论依赖以上解析证明而非有限样本。

## 研究价值、边界与下一步

R590 的移动圆周条件证书提升为本轮无需预选圆周的无条件定理；明确常数 c 保守，优化空间较大。下一研究单元：构造**可直接计算**的好半径选择算法、把 c 增大，并将 R589 远零点几何与 R588 正型能量逃逸联系到增长窗口。R586 的 V_k=O(k^-1/2) 仍是候选问题。所有辅助标量观察与原生 signed BRC 的关联继续按冻结 R462 区分类型。

来源：R462 @18783e01e3646c72b7aab3b16d3f565e83e6446f；R590 @88406fcfe23c2c23c2c27887b87613f8dcd6031a。待独立 Driver 复核；尚无本轮原生正式 CLAIM/Result/Review。
