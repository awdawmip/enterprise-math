# 一般稳定厚度组合的正卷积核与 Laplace 误差界

Date: 2026-11-21 (Asia/Hong_Kong)
Researcher-ID: EM-DIRECT-B5750A / TASK_RESEARCH
Task context: RS-RH-METHOD-TRANSFER-20261121
Status: AUTHOR_PROVED_KERNEL_AND_ERROR_BOUNDS; ARITHMETIC_WINDOW_ENERGY_OPEN.

## 1. 对象、来源和本稿范围

沿用冻结项目科学输入 `enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7` 与上轮已保存的稳定厚度桥 `enterprise-math@cc8e2eec9e281ac2649341ec44a270c49bed6d38:research_notes/portable_direct/rh_adaptive_window_20261121_b5750a/`。

完整道路为 R_a(n)=∏_(p|n)(1−p^(−a))。本稿保留所有 n≥2 和全部不同素因子子集；n=1 的修复端口另列。可在选定 Cell 锚点上以 n↦c_*+nE_1 索引道路。以下概率空间是计算同一标量核的辅助表示，不是对整数算术的随机独立性假设，也不是 X6 的新增空间轴或实际时间动力学。原生状态及允许的其它未来观察继续保留。

独立指数变量之和的密度和部分分式表达属于既有概率工具，参见 George P. Yanev, *Exponential and Hypoexponential Distributions: Some Characterizations* (2020), https://arxiv.org/abs/2012.08498 ，以及 *Sum of independent exponentials*, https://people.maths.bris.ac.uk/~mb13434/sumexp.pdf 。下文给出本任务需要的自足证明；贡献在于识别它与一般厚度外推权完全相同，并推导完整道路的符号、误差和参数代价。

## 2. 正负外推权恰好形成一个生存函数

令 m≥2，a_0,…,a_(m−1) 为不同正数，

\[
\nu_j=\prod_{k\ne j}\frac{a_k}{a_k-a_j},\qquad
D(n)=\sum_j\nu_jR_{a_j}(n)/a_j\quad(n\ge2).
\]

令 X_j 相互独立、密度 a_j e^(−a_j t) (t≥0)，T=ΣX_j。定义

\[
S(t)=\sum_j\nu_j e^{-a_jt},\qquad
\Psi(t)=\sum_j\frac{\nu_j}{a_j}(1-e^{-a_jt}),\qquad
I(t)=t-\Psi(t).
\]

**定理 1。** 对 t≥0，

\[
\boxed{S(t)=\Pr(T>t),\quad
\Psi(t)=\mathbb E\min(t,T),\quad
I(t)=\mathbb E(t-T)_+.}
\tag{1}
\]

因此 0≤Ψ≤t，Ψ 严格递增、凹；I≥0 且凸，I'=Pr(T≤t)，I''=f_T≥0。

**证明。** 卷积密度的 Laplace 变换为

\[
\mathcal L_T(z)=\prod_j\frac{a_j}{a_j+z}.
\]

在各简单极点 −a_j 处计算留数，得到有理恒等式

\[
\prod_j\frac{a_j}{a_j+z}
=\sum_j\frac{\nu_j a_j}{a_j+z}.
\]

故密度为 f_T(t)=Σν_j a_j e^(−a_jt)，积分到无穷得到生存函数 S(t)。也可直接按指数卷积归纳证明同一公式，不需要把含负系数的表达当作概率公理。对生存函数积分给 Ψ，再用 min(t,T)+(t−T)_+=t 得 I。□

同一恒等式给出

\[
\boxed{\Psi(\infty)=\sum_j\nu_j/a_j
=\mathbb ET=\sum_j1/a_j.}
\tag{2}
\]

这正是上轮 n=1 需要减去的端口。完整修复后 D(1)=0；本文其余和从 n=2 开始。

等距节点 a_j=(j+1)h 时，S(t)=1−(1−e^(−ht))^m，恢复上轮已证正核。这次 (1) 同时覆盖非等距、切比雪夫及任意不同正厚度。

## 3. 完整因子层的符号

设 n≥2 有 r 个不同素因子，ell_i=log p_i。用 Δ_ell f(t)=f(t+ell)−f(t)，Möbius 恒等式给

\[
\boxed{D(n)=-\sum_{d\mid n}\mu(d)\Psi(\log d),\qquad
D(n)-\Lambda(n)=(-1)^r\Delta_{\ell_1}\cdots\Delta_{\ell_r}I(0).}
\tag{3}
\]

所以素数幂层为 D(n)=Ψ(log p)∈(0,log p)，双素因子层为

\[
\boxed{D(n)=\int_0^{\ell_1}\int_0^{\ell_2}f_T(u+v)\,du\,dv>0.}
\tag{4}
\]

更一般地，r≥2 时

\[
D(n)=(-1)^r\int_{\prod_i[0,\ell_i]}
f_T^{(r-2)}(u_1+\cdots+u_r)\,d\boldsymbol u.
\tag{5}
\]

### 显式的三因子、四因子符号范围

令 A=max a_j。卷积在单纯形上换元，令 V 在 {v_i≥0,Σv_i=1} 上均匀分布，B=Σa_iV_i∈[min a_i,A]，得到

\[
f_T(t)=\frac{\prod_j a_j}{(m-1)!}t^{m-1}
\mathbb E e^{-tB}.
\tag{6}
\]

此处单纯形在 v_1,…,v_(m−1) 坐标测度下的体积为 1/(m−1)!；V 使用其归一化的均匀概率测度。等式也由卷积积分直接成立。

对 t>0 求导：

\[
f_T'(t)=\frac{\prod a_j}{(m-1)!}t^{m-2}
\mathbb E\big[e^{-tB}(m-1-tB)\big].
\]

故当 A log(rad n)≤m−1 时，r=3 的 D(n)≤0。

再求一次导数，方括号变为

\[
(m-1)(m-2)-2(m-1)tB+(tB)^2.
\]

其较小根为 m−1−√(m−1)。因此 m≥3 且

\[
A\log\operatorname{rad}n\le m-1-\sqrt{m-1}
\]

时，r=4 的 D(n)≥0。

**推论。** 上轮 A=1/2、m=ceil(log Z)、log Z≥10 的稳定组合，在所有 n≤Z 上同时具有：素数幂 D>0 且低于 Λ；双因子 D>0；三因子 D≤0；四因子 D≥0。理由是 A log Z≤m/2，而 m/2≤m−1−√(m−1) 对 m≥7 成立。各结论只涉及其声明因子层；更高层保留 (5)，不预设统一符号。

## 4. 一般节点的正积分误差与有限 Laplace 界

从正密度积分可得

\[
I(t)=\Big(\prod a_j\Big)
\int_{x_j\ge0,\,\sum x_j\le t}
(t-\sum x_j)e^{-\sum a_jx_j}\,d\boldsymbol x.
\tag{7}
\]

因此若 b=min a_j，

\[
e^{-At}\frac{(\prod a_j)t^{m+1}}{(m+1)!}
\le I(t)\le\frac{(\prod a_j)t^{m+1}}{(m+1)!}.
\tag{8}
\]

上界是正单纯形体积计算，不受正负权求差的数值抵消影响。上界中不可直接插入 e^(−bt)：积分内 Σx_j 可以小于 t。

另对任意 σ>0，使用 x_+≤e^(σx)/(eσ)，有

\[
\boxed{I(t)\le\frac{e^{\sigma t}}{e\sigma}
\prod_j\frac{a_j}{a_j+\sigma}.}
\tag{9}
\]

由 (3) 对非空因子子集求和得

\[
\boxed{|D(n)-\Lambda(n)|
\le\frac{\mathcal L_T(\sigma)}{e\sigma}
\left[\prod_{p\mid n}(1+p^\sigma)-1\right]
\le\frac{2^{\omega(n)}-1}{e\sigma}
e^{\sigma\log n}\mathcal L_T(\sigma).}
\tag{10}
\]

本式是一种新的可选误差上界；上轮插值余项可同时使用，两者取较小者。I 的正核并不使完整多因子误差同号。

在本项目使用的 1/2≤θ<1 范围内，令 L=log Z，r_*(Z)=max_(2≤n≤Z)ω(n)。r_* 可由连续素数的累积乘积精确确定，因为 r 个不同素因子的最小乘积是第 r 个 primorial。也可用 r!≤Z 给不依赖素数筛的较粗上界。定义

\[
\eta_Z(\sigma)=\frac{2^{r_*(Z)}-1}{e\sigma}
e^{\sigma L}\mathcal L_T(\sigma).
\]

若

\[
\boxed{\eta_Z(\sigma)L e^{(1-\theta)L}\le\frac12,}
\tag{11}
\]

则对全部 1≤y≤Z 有 |G_combo(y)−G(y)|≤y^theta/2。证明是 |D−Λ|≤η_Z 和 Σ_(2≤n≤y)(y/n−1)≤y log y；y∈[1,2) 两者相同。所有前史保留。

## 5. 切比雪夫组合的 Laplace 乘积可直接算

沿用给定 K>1、s=arcosh K、d=m−1、t=s/d，

\[
b/A=\tanh^2(t/2),\quad
\Delta=(A-b)/2,\quad
a_j=\Delta[\cosh t-\cos(j\pi/d)].
\]

令 u>t 满足 cosh u=cosh t+σ/Δ。上一轮节点乘积恒等式在平移 σ 后给

\[
\boxed{\mathcal L_T(\sigma)
=\frac{\sinh t\,\sinh s}{\sinh u\,\sinh(du)}.}
\tag{12}
\]

它计算的是正乘积，可以在对数域稳定求值；不需要先累加 m 个交错指数项。输入仍有 m 个实际厚度通道，(12) 的短公式只减少这个误差上界的计算成本。

从同一节点多项式的对数导数，另得精确单位端口

\[
\boxed{\sum_j\frac1{a_j}
=\frac{\coth t+d\coth s}{A\tanh(t/2)}.}
\tag{13}
\]

当 A 固定、m 增长时，这个端口为 Θ(m²/A)，并非逐项粗估得到的 O(m³/A)。原始输入独立误差的上界仍可沿用 K/b；两者用途不同。

## 6. 可证明的更宽厚度设计及其真实代价

给定 θ∈[1/2,1)、K>1，置 τ=1−θ>0、s=arcosh K。令 L→∞，选整数 m=m(L) 使 m/L→∞，取

\[
b=B/L^2,\qquad
A=b/\tanh^2[s/(2(m-1))],
\quad 0<B<\frac{s^2}{4\tau}.
\tag{14}
\]

使用上述切比雪夫节点和权重，则归一化权重绝对和恒为 K，而且当 L 充分大时，(11) 成立，从而整个 y≤e^L 窗口具有同样的半单位桥。

**证明。** 固定 σ>0。由 (14)，A~4B(m−1)²/(s²L²)，所以 A→∞，t→0，u→0，并且

\[
\frac{(m-1)u}{L}\longrightarrow s\sqrt{\sigma/B}.
\]

同时 sinh t/sinh u 的对数为 −log L+O(1)，故 (12) 给

\[
\frac1L\log\mathcal L_T(\sigma)
\longrightarrow -s\sqrt{\sigma/B}.
\]

由 r!≤e^L，得到 r_*(e^L)=o(L)：对 r≥4，log(r!)≥(r/2)log(r/2)，排除 r≥εL 的任意固定 ε>0。将其代入 (11)，其左侧的对数除以 L 的极限为

\[
\tau+\sigma-s\sqrt{\sigma/B}.
\]

选择 σ=s²/(4B)，此值为 τ−s²/(4B)<0，得到结论。也可在设计接近阈值时固定 σ=τ。□

例如 K=3、θ=1/2 时，允许 B 逼近 (arcosh3)²/2；上轮固定 A=1/2、m~L 的 bL² 极限是 (arcosh3)²/8。这里较大的最薄厚度常数以 m/L→∞ 和增大的最大厚度 A 为代价，未宣称通道总成本更优或全体节点均趋零。该设计不接用仅小 a 成立的 Q_a≤Ca 前提。

有限参数表用 (11) 的实际左侧计算，作为高精度非区间参数探索。一般命题由上述证明承担；同目录脚本明确区分精确有理恒等式、正积分核对和浮点参数案例。

## 7. 对正部窗口目标的作用

本稿把“交错厚度权如何仍保有正结构”落实为 (1)，把误差压缩落实为可算的正 Laplace 乘积 (9)–(12)，并为二至四因子层给出明确符号范围。它可用于选择厚度、验证误差及分解后续正部源工作。

完整道路上的 D_n 与 q_n+ 的相关仍需算术证明。辅助指数变量的独立性来自计算核的构造，不提供整数残差相互独立、随机相位抵消或任意远窗口能量界。
