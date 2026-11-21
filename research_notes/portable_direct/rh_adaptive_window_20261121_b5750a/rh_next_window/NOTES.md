# 完整道路的窗口准则：有界权重与匹配厚度下的整数等价

Date: 2026-11-21 (Asia/Hong_Kong)
Contribution: same-author-team continuation; no new identity, CLAIM, remote write or independent Project Review.
Status: AUTHOR_PROVED_DISCRETE_WINDOW_EQUIVALENCE; UNBOUNDED_WINDOW_ENERGY_ESTIMATE_OPEN.

## 1. 原生对象、观察范围和抽象输入

沿用项目全部整数道路 `R_a(n)=prod_(p|n)(1-p^(-a))`。在一个固定窗口 `[Y,Z]` 内，厚度族和实权重固定，权重和为1。定义

\[
D_n=\sum_jw_j\frac{R_{a_j}(n)}{a_j},\qquad
F(y)=\sum_{2\le n\le y}D_n(y/n-1)-y\log y+(1+\gamma)y.
\]

所以 `F=sum_j w_j G_(a_j)`，并保留截至当前观察位置的全部整数及合数质量。另一个窗口可选择另一组厚度或权重。`Y,Z,a_j,w_j,D_n` 是已有算术观察量的参数/读出，不增加 X6 空间轴；下面的标量递推不被解释成完整原生联合状态的无损编码。

本稿复用科学快照 `enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7` 的 P000/X6、联合观察保真、残差保真及完整道路定义，接续本轮 `rh_continuation_window_phase/NOTES.md` 的整数单元曲率证书。

为了覆盖等距多厚度外推和父会话的其它节点设计，主定理只要求以下**逐整数误差接口**：

\[
\boxed{
|D_n-\Lambda(n)|\le\eta\le\tfrac12
\quad(2\le n\le\lfloor Z\rfloor).
}\tag{H}
\]

这里只使用 `Lambda(n)>=0` 和 `Lambda(n)<=log n`。没有引入素数分布估计、RH 或无限尾收敛假设。

等距 m 阶外推具有

\[
D_n=\frac1h\sum_{j=1}^m\frac{(-1)^{j+1}}j\binom mjR_{jh}(n),
\quad |D_n-\Lambda(n)|\le\frac{h^m(\log n)^{m+1}}{m+1}.
\]

若 `Z=Y^lambda`、`Y>=e`，采用匹配步长

\[
h_Y=\left(\frac{m+1}{2}\right)^{1/m}
\frac{Y^{-\lambda(1-\theta)/m}}{(\lambda\log Y)^{1+2/m}},
\]

则

\[
\eta\le\frac{Y^{-\lambda(1-\theta)}}{2\lambda\log Y}<\tfrac12.
\]

因此该族满足(H)，且常数与阶数、权重绝对和无关。其它节点族只需提供同一(H)接口即可使用以下定理。端点数值求值误差仍需按其实际权重传播，数学常数统一不表示浮点计算成本统一。

## 2. 保留前史端口的精确递推

令 `q_N=F(N)`，并定义

\[
A_N=\sum_{2\le n\le N}\frac{D_n}n,
\qquad B_N=\sum_{2\le n\le N}D_n.
\]

有

\[
\boxed{q_N=N(A_N+1+\gamma-\log N)-B_N,}
\]

\[
A_N=A_{N-1}+D_N/N,\qquad B_N=B_{N-1}+D_N.
\]

直接相减得到

\[
q_{N+1}-q_N=A_N+(1+\gamma)
-[(N+1)\log(N+1)-N\log N].
\]

再相减便有

\[
\boxed{
q_{N+1}-2q_N+q_{N-1}=\frac{D_N-\kappa_N}{N}\quad(N\ge2),
}\tag{1}
\]

其中

\[
\kappa_N=N[(N+1)\log(N+1)-2N\log N+(N-1)\log(N-1)].
\]

固定的原点条件是

\[
q_1=1+\gamma,
\qquad q_2=2(1+\gamma-\log2).
\]

这些初值和全部节点输入 `D_N` 决定此标量观察量。等价的有限 Green 表示为

\[
q_N=q_1+(N-1)(q_2-q_1)
+\sum_{n=2}^{N-1}(N-n)\frac{D_n-\kappa_n}{n}.
\]

它把待研究量写成有固定初值的节点残差累计，所有带符号相关性保留在求和中。在窗口左端重新归零会改变问题。若后续允许晚选厚度权重，应保留各厚度自己的 `A_N,B_N`，或另证合并表示对该未来操作语言安全。

### 2.1 中心化背景的精确离散系数

用 `f''(x)=1/x` 的三角积分式并合并正负 t，

\[
\kappa_N
=2\int_0^1\frac{1-t}{1-t^2/N^2}\,dt
=\sum_{k=0}^{\infty}\frac{N^{-2k}}{(k+1)(2k+1)}.
\]

于是，对 `N>=2`，

\[
\boxed{
1+\frac1{6N^2}\le\kappa_N
\le1+\frac1{6(N^2-1)}.
}\tag{2}
\]

这是中心化项的精确离散修正，不能在等式(1)中直接把它替换为1而不保留余项。

## 3. 匹配误差排除了任意窄的正端点尖峰

由(H)、`Lambda>=0` 和(2)，

\[
D_N-\kappa_N\ge-\tfrac12-1-\frac1{6(N^2-1)}>-2,
\]

故

\[
\boxed{q_{N-1}+q_{N+1}\ge2q_N-\frac2N.}\tag{3}
\]

因此每个内点至少有一个邻点满足

\[
q_{N\pm1}\ge q_N-\frac1N.
\]

这条节点形状约束是连续正部能量与整数正部平方和之间反向比较的依据。对任意带符号端点数据，反向比较并不成立：一个正端点可以被两个极深的负端点夹住，导致插值正区间很窄。(H)正好提供了这里所需的统一控制。

## 4. 整数核心窗口的双边比较

先取整数 `3<=A<B`，`B>=A+2`。固定 `theta>0`，记

\[
p=2\theta+1,
\quad E_{A,B}=\int_A^B(F(y)_+)^2y^{-p}\,dy,
\]

\[
S_{A,B}=\sum_{N=A}^B((q_N)_+)^2N^{-p},
\qquad S^\circ_{A,B}=\sum_{N=A+1}^{B-1}((q_N)_+)^2N^{-p}.
\]

定义明确常数

\[
U_{\theta,A}=\tfrac12[1+(1+1/A)^p],
\quad C_{\theta,A}=\sqrt2\,(1+1/(A+1))^{p/2},
\]

\[
R_{\theta,A,B}=\left(\sum_{N=A+1}^{B-1}N^{-p-2}\right)^{1/2}
\le\frac{A^{-\theta-1}}{\sqrt{2\theta+2}},
\]

\[
\varepsilon_{\theta,A}\le
\frac{1+1/A}{8\sqrt{2\theta+2}}A^{-\theta-1}.
\]

则有

\[
\boxed{
\sqrt{S^\circ_{A,B}}
\le C_{\theta,A}\sqrt{E_{A,B}}+R_{\theta,A,B},
}\tag{4}
\]

\[
\boxed{
\sqrt{E_{A,B}}
\le\sqrt{U_{\theta,A}}\sqrt{S_{A,B}}
+\varepsilon_{\theta,A}.
}\tag{5}
\]

这些常数不依赖厚度、阶数、模态数或权重范数。上界(5)只需固定单元曲率；反向界(4)使用(H)。

### 4.1 上界证明

令 L 是整数端点插值。在 `[N,N+1]` 上，由正部的凸性及平方的凸性，

\[
L(y)_+^2\le(N+1-y)((q_N)_+)^2+(y-N)((q_{N+1})_+)^2.
\]

用 `y^(-p)<=N^(-p)` 积分，再合并相邻单元，每个内部节点的总系数至多

\[
\tfrac12[N^{-p}+(N-1)^{-p}]
\le U_{\theta,A}N^{-p}.
\]

两边界节点也满足同一上界。因此 `E_+(L)<=U S`。在每个单元上 `F''=-1/y`，故上轮的曲率证书给
`||F_+||<=||L_+||+epsilon`，即(5)。

### 4.2 反向界证明

对每个内部 N，选择(3)保证的邻点。如果 `q_N>1/N`，对应整条相邻单元上有

\[
L(y)_+\ge q_N-1/N.
\]

该单元的权不小于 `(N+1)^(-p)`。每个单元最多被其两个端点选择，所以

\[
\sum_{N=A+1}^{B-1}(q_N-1/N)_+^2(N+1)^{-p}
\le2E_+(L)\le2E_{A,B}.
\]

再用 `(q_N)_+<=(q_N-1/N)_++1/N` 的加权 Minkowski 不等式，以及
`N^(-p)<=(1+1/(A+1))^p(N+1)^(-p)`，得到(4)。

保留实际端点项

\[
T_{A,B}=((q_A)_+)^2A^{-p}+((q_B)_+)^2B^{-p},
\]

还得到

\[
\boxed{
\sqrt{S_{A,B}}
\le C_{\theta,A}\sqrt{E_{A,B}}+R_{\theta,A,B}+\sqrt{T_{A,B}}.
}\tag{6}
\]

端点项没有被隐去。

## 5. 任意实数幂窗口与纯整数准则

设 `1/2<=theta<1`、`lambda>1`，令 `Z=Y^lambda`、`A=ceil Y`、`B=floor Z`，Y 足够大以保证 `A>=3,B>=A+2`。

(H)还给出一个不依赖素数分布的初等上界。利用 `D_n<=log n+1/2` 与 `sum_(n=2)^floor(y)1/n<=log y`，

\[
F(y)\le y[(\log y)^2-\tfrac12\log y+(1+\gamma)]
\le y[(\log y)^2+2].
\]

于是

\[
\boxed{F(y)_+\le y[(\log y)^2+2].}\tag{7}
\]

由此，(6)中的端点项满足

\[
T_{A,B}\le A^{1-2\theta}[(\log A)^2+2]^2
+B^{1-2\theta}[(\log B)^2+2]^2.
\]

而被整数核心遗漏的两个长度小于1的边界片段，其正部能量之和不超过

\[
\begin{aligned}
T_{\mathrm{frag}}={}&(A-Y)Y^{1-2\theta}[(\log A)^2+2]^2\\
&+(Z-B)B^{1-2\theta}[(\log Z)^2+2]^2.
\end{aligned}\tag{8}
\]

所以

\[
E_{A,B}\le E_{Y,Z}
\le\left(\sqrt{U_{\theta,A}}\sqrt{S_{A,B}}+\varepsilon_{\theta,A}\right)^2
+T_{\mathrm{frag}}.
\]

当 `theta>1/2` 时，以上显式边界界均趋于0；当 `theta=1/2` 时，它们至多是对数的四次多项式，仍为次幂。

### 定理：匹配窗口条件的整数等价式

对每个 Y 使用满足(H)的固定系数组合 `F_Y`，定义

\[
\boxed{
\mathscr S_\theta(Y)
=\sum_{N=\lceil Y\rceil}^{\lfloor Y^\lambda\rfloor}
\frac{(F_Y(N)_+)^2}{N^{2\theta+1}}.
}\tag{9}
\]

在上述固定 `theta>=1/2,lambda>1` 范围，以下两条条件等价：

\[
\forall\alpha>0\ \forall Y_0\ \exists Y\ge Y_0:
\quad E_+(F_Y;Y,Y^\lambda)\le Y^\alpha,
\]

\[
\boxed{
\forall\alpha>0\ \forall Y_0\ \exists Y\ge Y_0:
\quad\mathscr S_\theta(Y)\le Y^\alpha.
}\tag{10}
\]

证明：分别使用(5)、(6)及(8)。给定目标指数 beta，使用另一条件的指数 `alpha=beta/2`，提高有限起点后，把有界比较常数、平方交叉项、衰减余项及对数多项式边界项吸收到 `Y^beta`。无须把Y限制为整数或平方数，也没有交换厚度极限与无穷尾。

因此，在本轮已经建立的道路到固定外部 G 的匹配误差桥之后，真正剩下的研究目标可以写成(10)这个**纯整数加权正部平方和**。完整实数窗口被等价处理，全部前史和合数贡献仍保留在 `F_Y(N)` 中。

本稿没有证明(10)。有限窗口试算只能验证具体窗口、递推与证书，不能取代其中任意远窗口的量词。

## 6. 可复算检验与证据范围

`verify_discrete_window.py` 采用70位 mpmath，核对小范围匹配厚度窗口中的：

- 全道路端点直接求和与二阶递推的一致性；
- `kappa_N` 的严格理论上下界和匹配误差接口；
- 连续正部积分与整数平方和的双边比较；
- 整数窗口以及具有非整数边界的窗口。

结果保存在 `discrete_window_results.json`。它是非区间浮点交叉核对；一般定理由上述证明支持。本稿没有重跑上轮的严格有理反例或大批旧实验。

## 7. 直接由完整道路得到的有界权重版本

还有一个不需要先比较 `D_n` 与 `Lambda(n)` 的版本，尤其适合父会话系数绝对和保持为3的节点设计。

对任何 `a>0,n>=2`，选任意素因子 p，其余道路因子均不超过1，因此

\[
0<R_a(n)/a\le(1-p^{-a})/a\le\log p\le\log n.
\]

若 `sum w_j=1` 且 `sum |w_j|<=K`，令

\[
P=(K+1)/2,\qquad M=(K-1)/2,
\]

则直接有

\[
\boxed{-M\log n\le D_n\le P\log n.}\tag{11}
\]

节点递推(1)于是保证至少一个邻点满足

\[
q_{N\pm1}\ge q_N-\delta_N,
\qquad \delta_N=\frac{1+M\log N}{N}.
\]

将 §4.2 中的 `1/N` 换成 `delta_N`，同一证明给出

\[
\sqrt{S^\circ_{A,B}}
\le C_{\theta,A}\sqrt{E_{A,B}}+R_{K,\theta,A,B},
\]

其中

\[
R_{K,\theta,A,B}^2
=\sum_{N=A+1}^{B-1}\frac{(1+M\log N)^2}{N^{2\theta+3}}.
\]

令 `r=2theta+2`，利用被积函数在 `t>=3` 上递减并积分，有明确界

\[
\boxed{
R_{K,\theta,A,B}^2
\le\frac{A^{-2\theta-2}}{r}
\left[(1+M\log A)^2+
\frac{2M(1+M\log A)}r+\frac{2M^2}{r^2}\right].
}\tag{12}
\]

端点与边界片段使用

\[
\boxed{F(y)_+\le y[P(\log y)^2+2]}\tag{13}
\]

替换(7)，其余证明不变。

特别地，对整个 `sum |w_j|<=3` 的族，统一取 `P=2,M=1` 即可。双边比较的主常数仍是 `C_(theta,A),U_(theta,A)`，而附加范数余量是

\[
O_\theta((1+\log A)A^{-\theta-1}),
\]

与厚度、节点数、阶数无关。对 `theta>=1/2`、固定 `lambda>1`，边界项仍为次幂，故 §5 的连续窗口条件与整数条件(10)仍然等价。

此处研究的是完整道路组合本身。若它同时满足父会话已证明的到固定外部 G 的匹配误差界，就可把(10)接入既有零点接口；本节不会单凭有限窗口离散化生成那条误差桥或无限尺度估计。

若 K 随 Y 快速增长，(12)、(13)会保留这种成本；不能未经检查就继续宣称余项次幂。匹配条件(H)提供另一条与 K 无关的控制，所以其较小的余项仍有独立用途。
