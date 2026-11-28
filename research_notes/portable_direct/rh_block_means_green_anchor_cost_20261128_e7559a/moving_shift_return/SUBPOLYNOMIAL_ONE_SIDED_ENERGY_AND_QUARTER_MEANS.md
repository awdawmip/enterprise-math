# 单侧次多项式能量判据与四分之一次方规模块均值的带锚点接合

第9轮，统一作者 **EM-DIRECT-E7559A / TASK_RESEARCH**，Activity **RA-D2F111EA1C0D4B1DBEFBC1B4**。这是作者解析接合，不是 independent Review 或 formal Result；本节不增加有限算例。

保持 P000 / Heartbeat X6 固定原生轴的辅助标量观察。完整参考道路为

\[
q^*(y)=y(1+\gamma-\log y)
+\sum_{n\le y}(y/n-1)\Lambda(n),\qquad y\ge1.
\tag{0.1}
\]

以下 `T(B)=B^{o(1)}` 的精确含义始终是：对于每个 `ε>0`，存在有限常数 `C_ε`，使所有充分大 B 均有 `T(B)≤C_εB^ε`。它不是某个未指明稀疏子列上的条件。

## 1. 单独一侧的次多项式完整能量已经等价于 RH

定义闭整数前缀

\[
S_\pm(q^*;B)=\sum_{1\le n\le B}\frac{q^*(n)_\pm^2}{n^2}.
\]

**定理 1。** 对一个预先固定的符号 `+` 或 `−`，分别有

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\forall\varepsilon>0,\ S_\pm(q^*;B)\ll_\varepsilon B^\varepsilon.
}
\tag{1.1}
\]

证明以下取正侧；负侧交换两个非负 Mellin 变换即可。第8轮已经证明 RH 蕴含 `S_+(q*;B)=O(log B)`，故只需加强其逆向输入。

### 1.1 整数到连续道路的完整支付

在每个单位开区间 `(n,n+1)` 内，全部源核均为仿射，故准确有

\[
(q^*)''(y)=-1/y.
\]

令 `0≤t≤1`。真实背景曲率给

\[
q^*(n+t)=(1-t)q^*(n)+tq^*(n+1)+R_n(t),
\qquad 0\le R_n(t)\le\frac{t(1-t)}{2n}\le\frac1{8n}.
\tag{1.2}
\]

上界可由比较二阶导数证明；差函数在两端为零。先对两个端点取正部，再用凸性及 `(a+b)²≤2a²+2b²`，得到

\[
\int_n^{n+1}\frac{q^*(y)_+^2}{y^2}\,dy
\le\frac{q^*(n)_+^2+q^*(n+1)_+^2}{n^2}
+\frac1{32n^4}.
\tag{1.3}
\]

由于 `(n+1)²/n²≤4`、`Σ_{n≥1}n^{-4}≤4/3`，对任意实 `T≥1`，置 `N=ceil T`，可得

\[
\boxed{
\int_1^T\frac{q^*(y)_+^2}{y^2}\,dy
\le5S_+(q^*;N)+\frac1{24}.}
\tag{1.4}
\]

完整背景没有被替换成分段仿射道路；它的单位曲率费用已经显示支付。负侧也可使用相同充分界。

### 1.2 任意小指数使单侧 Mellin 在整个右半临界面收敛

假设 (1.1) 右侧。任取 `σ>1/2`，选择

\[
0<\varepsilon<2\sigma-1.
\]

由 (1.4)，对 `X=2^k` 的每个 dyadic 实区间，Cauchy–Schwarz 给

\[
\begin{aligned}
\int_X^{2X}q^*(y)_+y^{-\sigma-1}\,dy
&\le
\left(\int_X^{2X}\frac{q^*(y)_+^2}{y^2}\,dy\right)^{1/2}
\left(\int_X^{2X}y^{-2\sigma}\,dy\right)^{1/2}\\
&\ll_{\sigma,\varepsilon}X^{1/2-\sigma+\varepsilon/2}.
\end{aligned}
\tag{1.5}
\]

指数严格为负，所以 dyadic 求和收敛。在任意紧子集 `Re s≥σ_0>1/2` 上，统一选 `ε<2σ_0−1` 即有局部一致支配。因此

\[
P(s)=\int_1^\infty q^*(y)_+y^{-s-1}\,dy
\]

在 `Re s>1/2` 绝对收敛且全纯。这里只控制一个固定正指数并不够；需要对每个正指数成立的量词。

### 1.3 非负 Landau 接续排除右半临界面的零点

原完整道路初等地满足 `q*(y)=O(y(1+log²y))`。故负部 Mellin

\[
N(s)=\int_1^\infty q^*(y)_-y^{-s-1}\,dy
\]

至少在 `Re s>1` 收敛。在该半平面，第8轮的准确式为

\[
P(s)-N(s)=\widehat q^*(s)
=\frac{1+\gamma}{s-1}-\frac1{(s-1)^2}
-\frac{\zeta'(s)/\zeta(s)}{s(s-1)}.
\tag{1.6}
\]

右侧在每个实 `s>1/2` 处局部全纯：`s=1` 的主部准确相消，正实区间没有非平凡零点。这些事实及非负 Mellin 的 Landau 边界奇点引理均已在第8轮证明和核对。

若 N 的收敛横坐标 `σ_c>1/2`，则 `N=P−qhat*` 在实点 `σ_c` 给出解析延拓，与该非负边界引理矛盾。所以 N 也在整个 `Re s>1/2` 收敛全纯，继而 `qhat*=P−N` 在该半平面全纯。

但每个实部大于 `1/2` 的非平凡零点 ρ，重数 `m_ρ`，在 (1.6) 中产生非零留数

\[
-\frac{m_\rho}{\rho(\rho-1)}\ne0.
\]

因此不存在这种零点，再由反射对称推出 RH。无需最右实部被取得、零点简单性或频率线性独立性。定理得证。

## 2. 原道路、普通素数 Green 项和真实割线的准确接合

取 `X=2^k`、`k≥1`。令 `J_k^*` 为真实端点 `(X,q*(X))`、`(2X,q*(2X))` 的完整割线，并定义其闭窗口正根能量

\[
A_k=\left(\sum_{n=X}^{2X}\frac{(J_k^*(n))_+^2}{n^2}\right)^{1/2}.
\tag{2.1}
\]

令 `g_n=n log n`，内部整数上的真实背景离散曲率为

\[
\kappa_m=m(g_{m+1}-2g_m+g_{m-1}).
\]

单位三角积分准确给

\[
\kappa_m-1
=2\int_0^1\frac{(1-t)t^2}{m^2-t^2}\,dt,
\qquad
0\le\kappa_m-1\le\frac1{6(m^2-1)}.
\tag{2.2}
\]

对 `[X,2X]` 的离散 Dirichlet Green 核 G，定义

\[
U_c(n)=\sum_{X<m<2X}G(n,m)\frac{c_m}{m}.
\]

原完整道路的整数二阶差为

\[
\Delta^2q^*(m)=\frac{\Lambda(m)-\kappa_m}{m}.
\]

因此在**全整数网格**上准确有

\[
q^*(n)=J_k^*(n)+U_b(n)+U_{\kappa-1}(n)-U_{\mathrm{pp}}(n),
\tag{2.3}
\]

其中

\[
b_m=1-\mathbf1_{\{m\ \mathrm{prime}\}}\log m\le1,
\quad
\mathrm{pp}_m=\sum_{p^j=m,\ j\ge2}\log p\ge0.
\]

高次素数幂项 `U_pp≥0`，在这个控制原道路正部的方向可以直接保留有利符号。完整前史仍在真实割线 `J_k*` 中，没有丢弃。

背景费用可直接显示。因为内部 `m≥X+1`，(2.2) 给 `(κ_m−1)/m≤1/(6X³)`；又有

\[
\sum_{X<m<2X}G(n,m)=\frac{(n-X)(2X-n)}2.
\]

故

\[
0\le U_{\kappa-1}(n)\le\frac1{48X},
\qquad
\boxed{\|U_{\kappa-1}\|_w\le\frac{\sqrt{X-1}}{48X^2}.}
\tag{2.4}
\]

两端该 Green 项为零，所以这里已准确支付完整闭窗口。

## 3. 四分之一次方规模的块均值，加真实正锚点，等价于 RH

取

\[
r_k=2^{\lfloor3k/4\rfloor},\qquad
M_k=X/r_k=2^{\lceil k/4\rceil}.
\tag{3.1}
\]

由完整整数普通素数累计误差 `F(n)=n−theta(n)` 定义

\[
w_i=\frac1{r_k}\sum_{v=0}^{r_k-1}F(X+ir_k+v),
\quad 0\le i<M_k,
\]

\[
C_k^+=\max_{\substack{d=2^j\\1\le d<M_k}}
\frac1{Xd}\sum_{i=0}^{M_k-1-d}(w_{i+d}-w_i)_+^2.
\tag{3.2}
\]

这个 C 正是本轮 `green_cutoff/COARSE_BLOCK_MEANS_TO_ORIGINAL_GREEN.md` 的统计：局部累计与全局 F 仅差一个公共常数，块均值差不变。将该稿 (1.1) 用于 (2.3)，得到明确接合

\[
\boxed{\begin{aligned}
\|(q^*)_+\|_{w,[X,2X]}
\le{}&A_k+
\sqrt{\frac{C_k^+}{12}(1-r_k/X)(1-X^{-2})}\\
&+\frac{r_k^2\sqrt{X-1}}{2X^2}
+\frac{\sqrt{X-1}}{48X^2}\\
\le{}&A_k+\sqrt{C_k^+/12}+\frac12+\frac1{48X^{3/2}}.
\end{aligned}}
\tag{3.3}
\]

使用的是全整数网格，所以左边是真正完整道路在全部闭整数点上的能量。最后一步准确使用 `r_k≤X^{3/4}`。

**定理 2。** 对上述固定选定的 `r_k`、真实割线以及真实普通素数统计，

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\forall\varepsilon>0,\quad
A_k+C_k^+\ll_\varepsilon2^{\varepsilon k}.
}
\tag{3.4}
\]

等价地，可以把右侧写成 `max{1,A_k,sqrt(C_k^+)}=2^{o(k)}`；因为所有正指数均可任意选择，开平方、平方不改变这个增长类。

**逆向证明。** 由 (3.3)，若 `A_k,C_k^+≪_η2^{ηk}`，则完整闭块的正根能量 `≪_η2^{ηk}`，正平方能量 `≪_η2^{2ηk}`。对于任意给定 `ε>0`，取 `η=ε/2`，对 `k≤floor(log₂B)` 的完整闭块求和，并支付单独的 `n=1`，得到

\[
S_+(q^*;B)\ll_\varepsilon B^\varepsilon.
\]

末块允许完整延到 `2^{k+1}`；非负性使这种覆盖成为充分上界。相邻块重复的端点没有被错误抵消。定理 1 随即推出 RH。

**正向证明。** RH 下，第8轮的绝对收敛规范零点展开给 `|q*(y)|≤C sqrt y`。由于平方根为凹函数，真实端点割线满足 `|J_k*(n)|≤C sqrt n`，故

\[
A_k^2\le C^2\sum_{n=X}^{2X}\frac1n=O(1).
\tag{3.5}
\]

另一方面，RH 下前驱的全中心二幂长度统计满足 `K_k^+≪k²`。本轮 Jensen 方向对当前 `r_k` 同样适用，给 `C_k^+≤K_k^+≪k²`。两者共同蕴含 (3.4) 右侧。证毕。

## 4. 结论的边界

新判据联合使用每个二幂窗口约 `X^{1/4}` 个连续块均值，以及两个真正完整参考道路端点所形成的正割线预算。它没有把四分之一次方规模的块均值**单独**宣布为 RH 等价条件，也没有证明真实锚点的所需无条件上界。

均值的取得仍依赖完整整数源聚合，真实端点仍包含完整前史。这里的观察规模不等于端到端计算复杂度。若接合的是随窗口变化的实际匹配道路，返回参考道路的完整匹配误差和端点误差须另按本轮相应接合式支付。

本稿只新增解析连接；未重跑前驱证书，未增加 ζ 零点、道路点值或素数筛计算。依赖是第8轮 `return_energy/LOGARITHMIC_RETURN_ENERGY.md` 的单侧 Landau 论证和 RH 均值、第8轮全中心统计上界，以及本轮 `block_means`、`green_cutoff` 两项已给定作者定理。
