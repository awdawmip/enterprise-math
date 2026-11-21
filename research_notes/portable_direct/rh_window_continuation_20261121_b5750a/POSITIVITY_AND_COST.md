# 正厚度混合的偏差下界与两厚度外推的精确代价

Date: 2026-11-21 (Asia/Hong_Kong)
Researcher: EM-DIRECT-B5750A / TASK_RESEARCH
Task context: RS-RH-METHOD-TRANSFER-20261121
Status: AUTHOR_PROVED_SCALAR_OBSERVER_RESULTS; Project Review not performed.

## 1. 对象与观察者范围

沿用项目完整道路

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}),\quad R_a(1)=1,
\qquad F_a(n)=R_a(n)/a\quad(n\ge2).
\]

项目一阶 jet 是 \(R'_0(n)=\Lambda(n)\)。本稿只比较有限厚度的标量读出如何逼近这一已定义观察量，不删除完整道路输入，也不把带符号标量抵消解释为联合状态消失。

科学输入固定为 enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7 的 penetration-jet 与 positive-road-energy 记录；P000/X6、联合关系观察者保持和残差保真前提保留。静态索引可在选定原生 Cell 锚点 c_* 的 X6 中写作 n↦c_*+nE_1，其他原生坐标在此索引切片固定；整数及其因子联合数据、厚度和幅度都是类型化读出字段。该索引不宣称覆盖完整空间状态。下列范数是读出/扰动范数。

## 2. 正权重混合不能优于所用最薄观察量的素数幂偏差

设 \(a_1,\ldots,a_r>0\)、\(\alpha_j\ge0\)、\(\sum_j\alpha_j=1\)，定义

\[
P(n)=\sum_j\alpha_j F_{a_j}(n),\qquad b=\min_j a_j.
\]

**定理 1。** 对每个素数幂 \(n=p^k\)，记 \(L=\log p\)，有

\[
0<P(p^k)\le F_b(p^k)<L,
\]

\[
\boxed{L-P(p^k)\ge L-\frac{1-e^{-bL}}b.}
\]

证明：

\[
F_a(p^k)=\int_0^L e^{-au}\,du
\]

对 a 严格递减且严格小于 L。凸组合至多等于所用最薄厚度的值。若所有正权重都放在厚度 b 上，等号成立。□

进一步，若 \(\max_j a_jL\le1\)，则

\[
\boxed{L-P(p^k)\ge\frac{L^2}{3}\sum_j\alpha_j a_j
\ge\frac{bL^2}{3}.}
\]

因为对 \(0\le t\le1\)，
\(t-(1-e^{-t})\ge t^2/2-t^3/6\ge t^2/3\)。逐项应用再求和即可。

**确切含义。** 如果所有采样厚度均至少为 \(\kappa a\)，其中 \(\kappa>0\) 不随 a 变，则正归一化混合在固定素数幂上仍有 \(\Omega(a)\) 偏差。获得更高阶精度，需要使用相应更薄的正厚度，或引入带符号的外推。这里的下界仅针对已定义的正凸组合族。

## 3. 任意两厚度的二阶外推

令 \(0<b<a\)。定义

\[
\boxed{D_{a,b}(n)=\frac{aF_b(n)-bF_a(n)}{a-b}.}
\]

其两个权重为 \(a/(a-b)\) 与 \(-b/(a-b)\)，总和为 1。该式是 R 在节点 0,b,a 上的二次插值多项式在 0 的导数。

**定理 2。** 对全部 \(n\ge2\)，

\[
\boxed{|D_{a,b}(n)-\Lambda(n)|\le\frac{ab}{6}(\log\operatorname{rad}n)^3.}
\]

证明：插值导数余项给出某个 \(\xi\in(0,a)\)，使

\[
D_{a,b}(n)-R'_0(n)=-\frac{ab}{6}R'''_\xi(n).
\]

对有限乘积使用 Leibniz 和 multinomial 恒等式，得到 \(|R'''_\xi(n)|\le(\sum_{p\mid n}\log p)^3\)。□

系数在素数幂上渐近精确。固定 \(r=b/a\in(0,1)\) 且 \(a\to0\)，

\[
\Lambda(p^k)-D_{a,b}(p^k)
=\frac{ab}{6}(\log p)^3+O_r(a^3(\log p)^4).
\]

对上轮完整道路平滑观察量 \(\mathscr G_a(y)\)，定义

\[
\mathscr G_{a,b}(y)
=\frac{a\mathscr G_b(y)-b\mathscr G_a(y)}{a-b}.
\]

中心项保留一次，完整整数和保持不变，并有

\[
\boxed{|\mathscr G_{a,b}(y)-G(y)|\le\frac{ab}{6}y(\log y)^4.}
\]

因此固定 \(0<\theta<1,\lambda>1\)，只要

\[
ab\le L_Y:=\frac{3Y^{-\lambda(1-\theta)}}{(\lambda\log Y)^4},
\]

就有整个 \([Y,Y^\lambda]\) 上误差不超过 \(y^\theta/2\)。

## 4. 厚度收益与扰动放大的精确二参数关系

若对两个已归一化读出的误差分别满足 \(|\delta F_b|,|\delta F_a|\le\eta\)，则

\[
|\delta D_{a,b}|\le\frac{a+b}{a-b}\eta.
\]

取误差分别为 \(+\eta,-\eta\) 达到等号。因此其 \(\ell_\infty\to|\cdot|\) 扰动放大因子精确为

\[
\boxed{A(r)=\frac{1+r}{1-r},\qquad r=b/a.}
\]

这是读出误差传播的最坏情形，不是假定真实道路误差之间相互独立。

**定理 3。** 给定允许的放大上限 \(K>1\)、正预算 \(L>0\) 和约束 \(ab\le L\)，在上述两节点族中，能够使用的最大最小厚度为

\[
\boxed{b_{\max}=\sqrt{L\frac{K-1}{K+1}}.}
\]

它在

\[
r=\frac{K-1}{K+1},\qquad
a=\sqrt{L\frac{K+1}{K-1}},\qquad
b=\sqrt{L\frac{K-1}{K+1}}
\]

处取得。证明：\(A(r)\le K\) 等价于 \(r\le(K-1)/(K+1)\)，而 \(b^2=rab\le rL\)。同时令两约束取等即可。□

例如 \(K=3\) 给出 \(r=1/2\)，即本轮的等距两厚度公式。它是在这一特定误差预算和两节点族中，最大化所用最小厚度的选择。需要限制最大厚度的应用，应再与该应用的厚度上限共同取交；窗口渐近时上述厚度自动趋于零。

## 5. 正部能量的附加信息

提高精度所需的负权重改变了正部问题。对于一般读出 f,g，\((2f-g)_+\) 无法只由 \(f_+,g_+\) 控制。此次窗口分支进一步给出了实际完整道路在 \([25,125]\)、厚度 1/10 与 1/5 上的严格有理证书，见 [窗口主稿](rh_continuation_window_phase/NOTES.md)。

一种保留缺失信息的精确接口是选定参考厚度 b，写

\[
\mathscr G_{a,b}=\mathscr G_b+\Delta_{a,b},
\qquad
\Delta_{a,b}=\frac{b}{a-b}(\mathscr G_b-\mathscr G_a).
\]

于是对任意正测度的加权 L² 范数，

\[
\|\mathscr G_{a,b,+}\|_2
\le\|\mathscr G_{b,+}\|_2+\|\Delta_{a,b,+}\|_2.
\]

两厚度之差的中心项恰好消去，在每个整数单元上是线性函数；本轮有限窗口证书可精确积分其正部。这个差是需要保留的跨厚度联合观察方向。

## 6. 结论状态

本文证明了正凸组合的偏差下界、一般两厚度误差和精确扰动/厚度权衡。完整道路的跨尺度窗口能量上界仍是研究目标。证明是作者推导；一般插值与误差传播工具不主张新颖性，项目审阅及正式 Result 状态另据真实记录。
