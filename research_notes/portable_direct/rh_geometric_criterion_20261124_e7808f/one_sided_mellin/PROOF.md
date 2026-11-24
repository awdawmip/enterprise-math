# 完整参考道路的单侧 Mellin 接口与能量增长指数

研究身份：EM-DIRECT-E7808F / TASK_RESEARCH。活动：RA-0B92AAF774CA466C1C1BC38B。

本稿为本轮共同作者的解析推导，不是独立 Review，不登记新的 formal Result。科学基础与原道路约定沿用当前项目冻结；原道路仍保留完整 \(D,\kappa,\gamma\)，以及 \(c=\mu_{\rm Mob}*(D-\kappa)\)、\(c(1)=-2\log2\)。本文的 \(Q=q^*\) 是保持背景、Euler 常数与完整前缀起点的辅助参考道路；不能把 \(Q\) 与固定匹配阶的实际道路无条件互换。\(Q\) 仍是指定 X6 原生整数轴上的辅助标量读出。

## 1. 定义、量词与结论

令 \(\Lambda\) 为包含所有素数幂的 von Mangoldt 函数，\(\gamma\) 为 Euler 常数。对所有实数 \(x\ge1\)，定义

\[
Q(x)=x(1+\gamma-\log x)
 +\sum_{2\le n\le x}\left(\frac xn-1\right)\Lambda(n).                 \tag{1.1}
\]

新出现的整数项在 \(x=n\) 处等于零，因此这里没有半权端点问题，\(Q\) 在整个 \([1,\infty)\) 连续。写

\[
S_\pm(X)=\sum_{n=X}^{2X}\frac{Q(n)_\pm^2}{n^2},\qquad X\in\mathbb N,
\quad f_+=\max(f,0),\quad f_-=\max(-f,0).                              \tag{1.2}
\]

“有次幂上界”始终指以下单向量词，不包含任何下界：

\[
\forall\varepsilon>0\ \exists C_\varepsilon<\infty,\ X_\varepsilon
\quad\forall X\in\mathbb N,\ X\ge X_\varepsilon:
\quad S_\pm(X)\le C_\varepsilon X^\varepsilon.                          \tag{1.3}
\]

也可以仅要求 \(X=2^j\)：任意 \([X,2X]\) 都包含在两个相邻的二进块之并中，反向限制显然成立，所以两种上界量词等价。注意：这里每个二进块内仍包含**全部整数点**，不是仅取二进端点。

记所有非平凡零点（按重数）为 \(\rho=\beta+i\tau\)，并令

\[
\Theta=\sup_\rho\Re\rho\in[1/2,1].                                    \tag{1.4}
\]

本文证明：

1. 对正部与负部分别有精确指数律

\[
\boxed{\displaystyle
\limsup_{X\to\infty}\frac{\log S_\pm(X)}{\log X}=2\Theta-1.}             \tag{1.5}
\]

这里可以取全部整数 \(X\)，也可以仅取 \(X=2^j\)，并约定 \(\log0=-\infty\)。没有假设最右零点达到上确界。

2. 以下各条件分别与 RH 等价：正部满足 (1.3)；负部满足 (1.3)；正部能量有统一常数上界；负部能量有统一常数上界。

3. 无条件有下列绝对收敛的平滑显式公式，对每个实数 \(x\ge1\) 有效：

\[
\boxed{Q(x)=\log(2\pi)+\sum_\rho\frac{x^\rho}{\rho(1-\rho)}
       -\sum_{j\ge1}\frac{x^{-2j}}{2j(2j+1)}.}                          \tag{1.6}
\]

特别地，\(Q(x)=O(x^\Theta)\) 且 \(Q(x)=o(x)\)。在 RH 条件下，

\[
\boxed{|Q(x)|\le C_0\sqrt x+\log(2\pi),\qquad
C_0=2+\gamma-\log(4\pi).}                                             \tag{1.7}
\]

以上是判据、指数识别与条件性反向估计，不是证明 RH，也没有由有限样本推出无界估计。

## 2. Mellin 恒等式、实轴正则性与零点极点

由 \(\Lambda(n)\le\log n\)，定义直接给出 \(Q(x)=O(x\log^2(2x))\)。故在 \(\Re s>1\) 上绝对收敛并可交换和与积分。逐项核为

\[
\int_n^\infty(x/n-1)x^{-s-1}\,dx=\frac{n^{-s}}{s(s-1)}.
\]

结合 \(\sum\Lambda(n)n^{-s}=-\zeta'(s)/\zeta(s)\)，得到

\[
F(s):=\int_1^\infty Q(x)x^{-s-1}\,dx
=\frac{1+\gamma}{s-1}-\frac1{(s-1)^2}
-\frac{\zeta'(s)}{s(s-1)\zeta(s)}.                                    \tag{2.1}
\]

所用 Euler 乘积及 Dirichlet 级数是标准外部输入，见主来源 [S1]。由 Laurent 展开 [S2]

\[
\frac{\zeta'}\zeta(s)=-\frac1{s-1}+\gamma+O(s-1),
\]

得到

\[
-\frac{\zeta'/\zeta(s)}{s(s-1)}
=\frac1{(s-1)^2}-\frac{1+\gamma}{s-1}+O(1).
\]

所以 \(s=1\) 是 \(F\) 的可去点。完整背景与正确的 \(\gamma\) 正是在这里同时消去二阶和一阶极点。

对实数 \(0<s<1\)，交错级数

\[
\eta(s)=\sum_{n\ge1}(-1)^{n-1}n^{-s}
=\sum_{j\ge1}\big((2j-1)^{-s}-(2j)^{-s}\big)>0
\]

且 \(\zeta(s)=\eta(s)/(1-2^{1-s})<0\)。对实数 \(s>1\)，Euler 乘积给出非零。因此，延拓后的 \(F\) 在**每个正实数点的某个复邻域内全纯**。这个结论不要求 RH；它也没有断言整个右半平面无复极点。

若 \(\rho\) 是重数为 \(m_\rho\) 的非平凡零点，则 (2.1) 在 \(\rho\) 的留数为

\[
\operatorname{Res}_{s=\rho}F(s)
=-\frac{m_\rho}{\rho(\rho-1)}
=\frac{m_\rho}{\rho(1-\rho)}\ne0.                                    \tag{2.2}
\]

因此任何非平凡零点都不能被道路核消去。非平凡零点所在带及函数方程的对称性见 [S3]、[S4]。

## 3. 非负 Mellin 变换的 Landau 引理：自足证明

**引理 3.1。** 设 \(h\ge0\) 局部可积于 \([1,\infty)\)，其 Mellin 积分

\[
L(s)=\int_1^\infty h(x)x^{-s-1}\,dx
\]

具有有限实收敛横坐标 \(\sigma_c\)。则由 \(\Re s>\sigma_c\) 定义的全纯函数不能跨过实点 \(\sigma_c\) 全纯延拓。

**证明。** 假设在 \(|s-\sigma_c|<R\) 存在与原函数一致的全纯延拓。取 \(s_0=\sigma_c+R/4\)。它的 Taylor 级数至少在 \(|s-s_0|<R/2\) 内收敛，因为该圆盘包含在上述延拓圆盘内。令 \(r=3R/8\)，于是 \(s_0-r=\sigma_c-R/8<\sigma_c\)。

在 \(s_0>\sigma_c\) 可由留出一个正实裕量而逐次求导，得到

\[
(-1)^jL^{(j)}(s_0)
=\int_1^\infty h(x)(\log x)^j x^{-s_0-1}\,dx\ge0.
\]

在 Taylor 圆盘内代入 \(s_0-r\)，全部级数项非负且总和有限。单调收敛定理给出

\[
\begin{aligned}
L(s_0-r)
&=\sum_{j\ge0}\frac{r^j}{j!}
  \int_1^\infty h(x)(\log x)^j x^{-s_0-1}\,dx\\
&=\int_1^\infty h(x)x^{-s_0-1}
  \sum_{j\ge0}\frac{(r\log x)^j}{j!}\,dx\\
&=\int_1^\infty h(x)x^{-(s_0-r)-1}\,dx<\infty.
\end{aligned}
\]

这与 \(s_0-r<\sigma_c\) 矛盾。证毕。

**引理 3.2（单侧延拓）。** 设实函数 \(f\) 局部可积且至多为多项式增长，其 Mellin 变换 \(H\) 初始定义于某个右半平面。设 \(H\) 有到 \(\Re s>\alpha\) 的亚纯延拓，并在每个实点 \(s>\alpha\) 附近全纯。若

\[
\int_1^\infty f_+(x)x^{-\sigma-1}\,dx<\infty
\quad\text{对每个实数 }\sigma>\alpha,                                 \tag{3.1}
\]

则 \(H\) 在整个 \(\Re s>\alpha\) 全纯。把正部与负部互换，结论不变。

**证明。** 正部积分给出 \(H_+\) 在 \(\Re s>\alpha\) 的全纯函数。负部因多项式增长有有限上界的收敛横坐标 \(\sigma_-\)，也可能为 \(-\infty\)。若 \(\sigma_->\alpha\)，则在 \(\Re s>\sigma_-\) 上，亚纯函数唯一性给出

\[
H_-=H_+-H.
\]

这个等式首先在共同的初始半平面成立，继而在上述连通半平面成立，且那里 \(H\) 的所有表面极点均可去。因为 \(H_+\) 与 \(H\) 在实点 \(\sigma_-\) 附近全纯，上式使 \(H_-\) 跨过该点全纯延拓，违背引理 3.1。因此 \(\sigma_-\le\alpha\)。两部分积分在 \(\Re s>\alpha\) 均全纯，其差就是 \(H\)。证毕。

这里的实轴正则性不可省略。特别是给道路加上 \(cx\) 后，Mellin 变换会新增 (c/(s-1))；不能再在跨越 1 的论证中套用本引理。

## 4. 从整数单侧能量到连续 Mellin 积分

在每个开单元 \((n,n+1)\)，源和是仿射的，因此

\[
Q''(x)=-1/x.
\]

令 \(I_n\) 为端值 (Q(n),Q(n+1)) 的线性插值。二阶导数的插值余项（也可由二阶 Green 核直接积分）给出

\[
0\le Q(x)-I_n(x)\le\frac{(x-n)(n+1-x)}{2n}
\le\frac1{8n}.                                                       \tag{4.1}
\]

这个误差与区间里有无素数幂无关；新源项在整数处保持连续。正部满足

\[
Q(x)_+\le(1-u)Q(n)_++uQ(n+1)_++1/(8n),\quad u=x-n,
\]

负部满足相同不等式且可以去掉最后误差。由 \((a+b)^2\le2a^2+2b^2\)、凸性、\(x\ge n\) 以及 \((n+1)^2/n^2\le4\)，合并所有细单元得

\[
\boxed{\int_X^{2X}\frac{Q(x)_\pm^2}{x^2}\,dx
\le5S_\pm(X)+\frac1{32X^3}.}                                        \tag{4.2}
\]

若 \(S_\pm(X)\le C X^r\)，其中 \(r>-1\)，则对任意 \(\sigma>(r+1)/2\)，Cauchy–Schwarz 给出

\[
\begin{aligned}
\int_X^{2X}Q(x)_\pm x^{-\sigma-1}\,dx
&\le\left(\int_X^{2X}\frac{Q(x)_\pm^2}{x^2}\,dx\right)^{1/2}
\left(\int_X^{2X}x^{-2\sigma}\,dx\right)^{1/2}\\
&\ll_{\sigma,C,r} X^{(r+1)/2-\sigma}.
\end{aligned}                                                       \tag{4.3}
\]

沿 \(X=2^j\) 求和收敛。所以只用全体整数点上的单侧能量，就能得到相应连续正部或负部 Mellin 积分的收敛。这里没有把整数点当作连续函数，也没有漏掉单元曲率误差。

由 (1.3)，对任何 \(\sigma>1/2\) 可取 \(0<\varepsilon<2\sigma-1\)，从而 (4.3) 给出 (3.1)，其中 \(\alpha=1/2\)。引理 3.2 使 \(F\) 在 \(\Re s>1/2\) 全纯，(2.2) 排除该半平面内的零点，再用函数方程对称性即得 RH。这已经完成单侧判据的困难方向，不依赖显式公式。

## 5. 平滑显式公式的严证

为避免未经说明地移动无穷轮廓，本节用已确立的 Hadamard 乘积与 Mellin 唯一性。只用到以下外部标准解析事实：

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\xi(s)=\xi(1-s),                                                     \tag{5.1}
\]

以及 \(\xi\) 的一阶 Hadamard 乘积和 \(\sum_\rho|\rho|^{-2}<\infty\)。这些事实的主来源分别是 [S3] 与作者托管的研究论文 [S5]，后者的 §7、公式 (32)–(34) 明确给出所需形式。由乘积逐项对数求导，局部一致且绝对收敛的组合是

\[
H(s):=\frac{\xi'}\xi(s)
=b+\sum_\rho\left(\frac1{s-\rho}+\frac1\rho\right),
\qquad b=H(0).                                                       \tag{5.2}
\]

每个括号内两项必须保留在一起，它是 \(O_s(|\rho|^{-2})\)；本稿不重排单独的 \(1/\rho\) 条件级数。

由 (5.1) 对数求导，以及 [S2] 的 Laurent 展开、[S6] 的 \(\psi(1/2)=-\gamma-2\log2\)，有

\[
H(1)=1+\gamma/2-\tfrac12\log(4\pi),\qquad
b=-H(1)=-1-\gamma/2+\tfrac12\log(4\pi).
\]

在 (5.2) 代入 1，并与 0 的值相减，得到绝对收敛的恒等式

\[
\boxed{\sum_\rho\frac1{\rho(1-\rho)}=-2b
=2+\gamma-\log(4\pi)=C_0.}                                         \tag{5.3}
\]

非平凡零点没有实零点，且只有有限多个零点在任意紧集内；于是

\[
A_0:=\sum_\rho\frac1{|\rho(1-\rho)|}<\infty.                          \tag{5.4}
\]

设 (U(x)) 为 (1.6) 右侧。零点和与平凡零点和在每个紧区间 \([1,M]\) 绝对一致收敛，故 \(U\) 连续。并且 \(|U(x)|\le A_0x+\log(2\pi)\)。当 \(\Re s>1\) 时，可以绝对交换 Mellin 积分与两组级数，得到

\[
\widehat U(s)=\frac{\log(2\pi)}s
+\sum_\rho\frac1{\rho(1-\rho)(s-\rho)}
-\sum_{j\ge1}\frac1{2j(2j+1)(s+2j)}.                                \tag{5.5}
\]

下面逐项计算，证明它恰等于 (2.1)。记

\[
T_0=\sum_{j\ge1}\frac1{2j(2j+1)}=1-\log2.
\]

零点部分由代数恒等式给出

\[
s(s-1)\sum_\rho\frac1{\rho(1-\rho)(s-\rho)}
=sC_0-H(s)+b.                                                        \tag{5.6}
\]

平凡零点部分则由 [S7] 的 digamma 部分分式得到

\[
\begin{aligned}
-s(s-1)\sum_{j\ge1}\frac1{2j(2j+1)(s+2j)}
&=-sT_0+\sum_{j\ge1}\left(\frac1{2j}-\frac1{s+2j}\right)\\
&=-sT_0+\tfrac12\bigl(\psi(1+s/2)+\gamma\bigr).                       \tag{5.7}
\end{aligned}
\]

再代入

\[
H(s)=\frac1s+\frac1{s-1}-\tfrac12\log\pi
 +\tfrac12\psi(s/2)+\frac{\zeta'}\zeta(s),
\quad \psi(1+s/2)=\psi(s/2)+2/s,
\]

并用 \(C_0=2+\gamma-\log4\pi\) 与上述 \(b,T_0\)，各项精确整理为

\[
s(s-1)\widehat U(s)
=s(1+\gamma)-1-\frac1{s-1}-\frac{\zeta'}\zeta(s)
=s(s-1)F(s).                                                        \tag{5.8}
\]

因此 (U,Q) 在初始半平面有相同 Mellin 变换。

这里可直接用以下唯一性论证。取固定实数 \(c>2\)，令
\(w(u)=(Q(1/u)-U(1/u))u^{c-1}\)，则 \(w\in L^1(0,1)\)。在 \(s=c+n\) 处的 Mellin 等式表示 \(\int_0^1 w(u)u^n\,du=0\) 对所有整数 \(n\ge0\) 成立。多项式在 \(C[0,1]\) 中稠密，故相应有限符号测度为零，\(w=0\) 几乎处处。连续性进一步给出 \(Q=U\) 处处。于是 (1.6) 对所有实数 \(x\ge1\) 成立，包括素数幂和 \(x=1\)。

端点校准也直接核对：在 \(x=1\)，(1.6) 的右侧为

\[
\log(2\pi)+C_0-(1-\log2)=1+\gamma=Q(1).                              \tag{5.9}
\]

## 6. 无条件增长、RH 常数界与精确能量指数

由 (1.6)、(5.4) 和 \(\Re\rho\le\Theta\)，

\[
|Q(x)|\le A_0x^\Theta+\log(2\pi).                                   \tag{6.1}
\]

又因每个非平凡零点严格满足 \(\Re\rho<1\)，(5.4) 允许对 \(Q(x)/x\) 的零点级数用支配收敛，从而无条件得到

\[
\boxed{Q(x)=o(x).}                                                   \tag{6.2}
\]

这一步即使 \(\Theta=1\) 也成立，并没有假设统一的零点实部间隙。

在 RH 下，每个 \(\rho(1-\rho)=1/4+\tau^2>0\)，所以 (5.3) 给出 \(A_0=C_0\)。另外

\[
0\le\sum_{j\ge1}\frac{x^{-2j}}{2j(2j+1)}\le1-\log2<\log(2\pi).
\]

这就证明 (1.7)，其常数 \(C_0\approx0.0461914179\)。例如对任一单侧，

\[
\begin{aligned}
S_\pm(X)\le{}&C_0^2(\log2+X^{-1})\\
&+2C_0\log(2\pi)\bigl((2-\sqrt2)X^{-1/2}+X^{-3/2}\bigr)\\
&+(\log(2\pi))^2\bigl((2X)^{-1}+X^{-2}\bigr).
\end{aligned}                                                       \tag{6.3}
\]

这里只是把 (1.7) 平方后用单调函数的和积比较；特别有统一常数上界，并有 \(\limsup S_\pm(X)\le C_0^2\log2\)。所以 §4 的必要方向加上本节反向，证明了 §1 的 RH 等价陈述。

为证 (1.5)，(6.1) 先给出上界

\[
\limsup\frac{\log S_\pm(X)}{\log X}\le2\Theta-1.
\]

若某一单侧的左边 \(r\) 严格小于 \(2\Theta-1\)，选取

\[
\max(r,-1)<r'<2\Theta-1,\qquad \alpha=(r'+1)/2\in(0,\Theta).
\]

由 limsup 定义，充分大时 \(S_\pm(X)\le X^{r'}\)。§4 给出该单侧 Mellin 积分在所有实 \(\sigma>\alpha\) 收敛。§2 的实轴正则性与引理 3.2 遂使 \(F\) 在 \(\Re s>\alpha\) 全纯。然而 \(\alpha<\Theta\) 保证至少有某个零点 \(\Re\rho>\alpha\)，由 (2.2) 它产生不可去极点，矛盾。

整个反证仅用二进块时也完全成立，所以两种窗口量词具有相同精确指数。这是 limsup 指数，不是每一窗口都有相应幂下界，也不是声称最右零点存在。

同一论证还得到整数端点的单侧指数律

\[
\limsup_{n\to\infty}\frac{\log Q(n)_\pm}{\log n}=\Theta.               \tag{6.4}
\]

上界由 (6.1) 给出；若一侧有严格小于 \(\Theta\) 的指数，(4.1) 把该整数逐点上界传到连续道路，再直接得到这一侧在某个 \(\alpha<\Theta\) 右侧的 Mellin 收敛，重复同一矛盾即可。再次约定 \(\log0=-\infty\)。

## 7. 骨架和校准的接口边界

上述结果保留了完整真实端点。对于 \(J_X\)，即连接 (Q(X),Q(2X)) 的真实割线，RH 与 (1.7) 立即给出 \(\sum_{X\le n\le2X}(J_X(n))_+^2/n^2=O(1)\)。反向不能仅从“窗口正能量小”就未经证明地读出每个端点为 \(O(\sqrt X)\)：直接取一个样本最多给出 \(Q(X)_+\le X\sqrt{S_+(X)}\)。

若窗口左端遍历**全部大整数**，则 (6.4) 与 (6.1) 可以另行证明骨架能量具有指数 \(2\Theta-1\)：固定 \(0<\varepsilon<1\)，沿 \(H=Q(X)_+\ge X^{\Theta-\varepsilon}\) 的整数序列，另一端值满足 \(Q(2X)\ge-CX^\Theta\)。在长度至少常数倍

\[
X\frac{H}{H+CX^\Theta}
\]

的初始子段上，割线仍至少为 (H/2)。该长度趋于无穷，于是离散求和给出骨架正能量至少为常数倍

\[
\frac{H^3}{X(H+CX^\Theta)}\gg X^{2\Theta-1-3\varepsilon}.
\]

上界由 (6.1) 给出。因此全部整数窗口的骨架正能量也有同一指数；其负部同理。**此证明没有自动覆盖只观察 \(X=2^j\) 的骨架端点序列**，后者不是 §4 的全部整数块能量，可能涉及采样频率问题。本稿不声明该稀疏端点条件等价。

最后，由 (6.2)，若把校准改为 \(Q_c(x)=Q(x)+cx\)，则所有三角矩完全不变，但当 \(c>0\) 时

\[
\sum_{n=X}^{2X}\frac{Q_c(n)_+^2}{n^2}\sim c^2X,
\]

当 \(c<0\) 时其正部能量最终为零。负部情形互换。只有 \(c=0\) 保留本文的单侧能量指数律。这说明三角抵消与骨架校准必须同时保留，不能因为三角矩消去仿射项就删除真实 \(\gamma\) 或锚点。

## 8. 接回匹配道路时应支付什么

此前已经证明的全部匹配阶核允许在每个有限窗口使用一个真正定义好的匹配族 \(D_B\)，在背景、\(\gamma\) 与前缀一致时支付

\[
\|q_B-Q\|_{w,[A,B]}\le\varepsilon_B.
\]

正部映射为 1-Lipschitz，故

\[
\big|\|(q_B)_+\|_w-\|Q_+\|_w\big|\le\varepsilon_B,
\quad
\big|\|(q_B)_-\|_w-\|Q_-\|_w\big|\le\varepsilon_B.                    \tag{8.1}
\]

这给出窗口族之间的严格迁移接口。它不能把固定 \(m=11\) 的已算样本外推到任意大窗口；也不能把不同 \(B\) 的道路伪装成同一固定无限道路。完整背景与前缀的相同条件是 (8.1) 所接误差估计的前提，本文没有删去该条件。

## 9. 主来源、核验性质与复用

以下来源均在本轮实际打开读取。本文的 Landau 引理、整数曲率桥、单侧判据、指数律与由 Hadamard 乘积推得 (1.6) 的整理是本稿给出的证明；引用只承担明确列出的标准解析输入。

- [S1] NIST DLMF §27.4，Euler 乘积与 von Mangoldt Dirichlet 级数：<https://dlmf.nist.gov/27.4>。
- [S2] NIST DLMF §25.2，解析延拓、交错级数与 Laurent 展开：<https://dlmf.nist.gov/25.2>。
- [S3] NIST DLMF §25.4，完成函数定义及函数方程：<https://dlmf.nist.gov/25.4>。
- [S4] NIST DLMF §25.10，零点所在区域及对称性：<https://dlmf.nist.gov/25.10>。
- [S5] E. A. Kudryavtseva, F. Saidak, P. Zvengrowski, *Riemann and his zeta function*, Morfismos 9(2), 2005, pp. 1–48；作者托管全文，§7 公式 (32)–(34)：<https://home.uncg.edu/~f_saidak/Morfismos2005.pdf>。
- [S6] NIST DLMF §5.4，digamma 特值：<https://dlmf.nist.gov/5.4>。
- [S7] NIST DLMF §5.7，digamma 的部分分式：<https://dlmf.nist.gov/5.7>。

随附核验程序只核验有限代数整理、端点常数及有限实单元插值误差。它不通过截断零点和“验证” RH，不把数值闭合充当本文无界定理的证明。作者交叉核对与独立 Review 状态严格分开。
