# 多厚度道路读出：全阶误差、窗口增厚与相位成本

Date: 2026-11-21 (Asia/Hong_Kong)
Author collaboration: /root/rh_multithickness under the current RH method-transfer continuation.
Status: AUTHOR_DERIVED_SCALAR_READOUT_LEMMAS; not an independent Project Review, not an RH proof.

## 0. 研究对象、前提与归属

本稿在项目既有 P000 / 心跳世界原生 X6 前提下，研究完整整数道路的一个带符号标量读出。道路输入保留全部整数、不同素因子联合层、厚度标签及原点端口。积分与导数是已声明的有效数学读出工具，厚度参数不被解释为额外空间轴或完整物理时间。

这里在不同厚度下对道路读出作线性组合，不把相反标量符号视为联合状态消失，也不由某个阶数的接触消去推断合数方向冗余。后续若改用其他观察量或未来操作，必须重新保留所需联合信息。

沿用冻结项目源 enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7 中：

- research_notes/COMPOSITE_ROAD_RH_PENETRATION_JET_HIERARCHY_20260906.md：全阶接触层及 R'_0(n)=Λ(n)。
- research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md：完整道路、单位背景及正道路能量。
- p000_reality_foundation.json、definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json、definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json、definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json：世界与观察者类型保持。

沿用上一轮已发布证明 enterprise-math@d020e8a51defa2a0e45cd8a9150330805627155c:research_notes/portable_direct/rh_method_transfer_20261121_b5750a/FULL_ROAD_WINDOW_BRIDGE.md 的 G、完整幂窗口及 Landau 接口。外部接口固定到 CocoSgt/riemann-hypothesis-lean@7cbf7a0c32fca1badf05931879a37c3f8a2b03b4 的 CharFamily / lemmaL，本文不重建整个 Lean 工程。

前向差分、插值、Rolle 与 Peano 核是标准分析工具；本稿不主张其为新发现。此次新增交付是它们对完整道路的明确常数、端口修正、有限窗口桥接及资源代价。

## 1. 所有正厚度上的统一导数界

对 n≥2 记不同素因子为 p_1,...,p_r，l_i=log p_i，L_n=Σ_i l_i=log rad(n)。道路为

\[
R_a(n)=\prod_{i=1}^r(1-e^{-a l_i}),\quad a\ge0.
\]

**引理 1。** 对每个整数 k≥1 和全部 a≥0，

\[
\boxed{|\partial_a^k R_a(n)|\le L_n^k\le(\log n)^k.}
\]

证明：对 f_i(a)=1-e^{-a l_i}，有 |f_i(a)|≤1；当 q≥1 时，|f_i^(q)(a)|=l_i^q e^{-a l_i}≤l_i^q。Leibniz 公式给

\[
|R_a^{(k)}(n)|
\le\sum_{k_1+\cdots+k_r=k}\frac{k!}{k_1!\cdots k_r!}
\prod_i l_i^{k_i}
=(l_1+\cdots+l_r)^k.
\]

这是有限乘积恒等式与逐项界，对全部 a≥0 有效。□

该界不需要把所有非素数幂项删除；对每个 n，其全部联合素因子仍在乘积中。

## 2. m 阶前向导数读出及单位端口

令 m≥1 为整数，h>0。定义

\[
v_{m,j}=(-1)^{j+1}\binom mj,\qquad
w_{m,j}=\frac{v_{m,j}}j,\qquad
H_m=\sum_{j=1}^m\frac1j.
\]

对 n≥2 设

\[
\boxed{D_{m,h}(n)=\frac1h\sum_{j=1}^m w_{m,j}R_{jh}(n).}
\]

这是在 0,h,...,mh 上插值后对原点求导：若 P 是 f 在这些节点上的 m 次插值多项式，则

\[
P'(0)=\frac1h\left[-H_m f(0)+\sum_{j=1}^m w_{m,j}f(jh)\right].
\]

n≥2 时 R_0(n)=0，故上面的 D 正是 P'(0)。系数可直接对 Lagrange 基函数求导取得，或核对其对次数 0,...,m 的单项式精确。

**原点端口必须显式保留。** n=1 时 R_a(1)=1，对所有厚度成立，而目标 Λ(1)=0。若直接套用只含正厚度的 D，则

\[
D^{\rm uncorrected}_{m,h}(1)=H_m/h.
\]

完整人口上的正确读出是

\[
\boxed{
\widehat D_{m,h}(n)=\frac1h
\left[\sum_{j=1}^m w_{m,j}R_{jh}(n)-H_m R_0(n)\right],
\quad R_0(n)=\mathbf 1_{n=1}.
}
\]

因此 \widehat D(1)=0，而 n≥2 时 \widehat D=D。之后的平滑和均从 n=2 开始；若改从 n=1 开始，必须保留上式修正。

## 3. 精确余项常数

**定理 2。** 对 n≥2，有某个 ξ∈(0,mh) 满足

\[
D_{m,h}(n)-\Lambda(n)
=(-1)^{m+1}\frac{h^m}{m+1}R^{(m+1)}_\xi(n).
\]

故

\[
\boxed{|D_{m,h}(n)-\Lambda(n)|
\le\frac{h^m}{m+1}L_n^{m+1}.}
\]

证明：一般取 f∈C^(m+1)[0,mh]、插值多项式 P，并设

\[
\omega(x)=x\prod_{j=1}^m(x-jh),\quad
K=\frac{f'(0)-P'(0)}{\omega'(0)}.
\]

函数 f-P-Kω 在 0 有二重零点，并在 h,...,mh 为零。反复 Rolle 定理给出某个 ξ∈(0,mh)，使其 m+1 阶导数为零。因此 K=f^(m+1)(ξ)/(m+1)!。又 ω'(0)=(-1)^m m!h^m，故

\[
f'(0)-P'(0)=(-1)^m\frac{h^m}{m+1}f^{(m+1)}(\xi).
\]

代入 f=R_·(n)、f'(0)=Λ(n)，再应用引理 1。□

若把最大厚度记作 A=mh，则

\[
\boxed{|D_{m,A/m}(n)-\Lambda(n)|
\le \frac{A^m}{m^m(m+1)}L_n^{m+1}.}
\]

特别地，两厚度读出为

\[
D_{2,A/2}(n)=\frac{4R_{A/2}(n)-R_A(n)}A,
\qquad
\boxed{|D_{2,A/2}(n)-\Lambda(n)|\le\frac{A^2}{12}L_n^3.}
\]

### 3.1 显式 Peano 核

对于固定 m,h，误差也有精确积分表示

\[
D_{m,h}(n)-\Lambda(n)
=\int_0^{mh}K_{m,h}(t)\partial_t^{m+1}R_t(n)\,dt,
\]

\[
\boxed{K_{m,h}(t)=\frac1{h\,m!}
\sum_{j=1}^m w_{m,j}(jh-t)_+^m.}
\]

这是带积分余项的 Taylor 公式逐项代入；1 至 m 次矩消去全部低阶余项。该核具有固定符号

\[
(-1)^{m+1}K_{m,h}(t)\ge0,
\qquad
\int_0^{mh}|K_{m,h}(t)|dt=\frac{h^m}{m+1}.
\]

符号可由上面的 Rolle 余项定理严格推出：将任意连续非负函数 g 作为 f^(m+1)，误差必有符号 (-1)^(m+1)。若核在某段有相反符号，取非负 g 支持于该段即可矛盾。总质量用单项式 x^(m+1) 或直接积分核求得。

m=2、A=2h 时，核在 [0,A] 的显式式子是

\[
K_{2,A/2}(t)=
\begin{cases}
-t+\dfrac{3t^2}{2A},&0\le t\le A/2,\\
-\dfrac{(A-t)^2}{2A},&A/2\le t\le A.
\end{cases}
\]

其全程非正，绝对积分为 A²/12。

### 3.2 常数的渐近饱和

若 n=p^k、l=log p，则有完全显式的误差

\[
\boxed{l-D_{m,h}(p^k)=\int_0^l(1-e^{-hu})^m\,du.}
\]

证明：把 D 当作 l 的函数，求导得到

\[
\partial_lD=\sum_{j=1}^m v_{m,j}e^{-jhl}
=1-(1-e^{-hl})^m,
\]

再使用 D(l=0)=0。于是

\[
\lim_{h\downarrow0}
\frac{l-D_{m,h}(p^k)}{h^m l^{m+1}}=\frac1{m+1}.
\]

因此引理的 L_n 版本常数，在素数幂的小厚度极限已经达到，不能在相同全体对象与归一化下统一缩小。

## 4. 完整道路平滑读出与中心项

沿用上一轮

\[
\mathscr G_a(y)=\frac1a\sum_{2\le n\le y}R_a(n)(y/n-1)
-y\log y+(1+\gamma)y.
\]

定义新读出

\[
\mathscr G^{[m]}_h(y)=\sum_{2\le n\le y}D_{m,h}(n)(y/n-1)
-y\log y+(1+\gamma)y.
\]

由于 Σ_j v_(m,j)=1，有精确关系

\[
\boxed{\mathscr G^{[m]}_h(y)=\sum_{j=1}^m v_{m,j}\mathscr G_{jh}(y).}
\]

两厚度情形就是 2 mathscr G_(A/2)-mathscr G_A。中心项完整保留一次。

同样，若 S_a(t)=Σ_(n≤t)R_a(n)，则新未中心化读出满足

\[
\sum_{2\le n\le y}D_{m,h}(n)(y/n-1)
=\frac yh\sum_{j=1}^m w_{m,j}
\int_1^y(S_{jh}(t)-1)t^{-2}\,dt.
\]

这里每个 S_(jh)-1 的单位扣除与 §2 的 H_m/h 端口修正相同。

**定理 3。** 对 y≥2，

\[
|\mathscr G^{[m]}_h(y)-G(y)|
\le\frac{h^m}{m+1}
\sum_{2\le n\le y}L_n^{m+1}(y/n-1)
\le\boxed{\frac{h^m}{m+1}y(\log y)^{m+2}}.
\]

第一式直接应用定理 2 与非负 ramp；第二式使用 L_n≤log y、y/n-1≤y/n、Σ_(n=2)^floor(y)1/n≤log y。所有和都保留有限窗口中的完整整数人口。

## 5. 完整幂窗口的增厚选择

固定整数 m≥1、0<θ<1、λ>1。令

\[
h_Y^*=\left(\frac{m+1}{2}\right)^{1/m}
\frac{Y^{-\lambda(1-\theta)/m}}
{(\lambda\log Y)^{1+2/m}},\qquad Y\ge e.
\]

可直接使用 h_Y=h_Y^*；若后续接口要求最大道路厚度不超过 1/2，则取

\[
\boxed{h_Y=\min\{1/(2m),h_Y^*\}.}
\]

定理 3 对全正厚度有效，截帽只是提供兼容的小厚度范围。对固定 m，当 Y 足够大时截帽自动失效。无论是否截帽，在整个 [Y,Y^λ] 上都有

\[
\boxed{|\mathscr G^{[m]}_{h_Y}(y)-G(y)|\le\tfrac12y^\theta.}
\]

证明：h_Y^m≤((m+1)/2)Y^(-λ(1-θ))/(λ logY)^(m+2)，且 y^(1-θ)(log y)^(m+2) 在窗口右端取最大值。代入即可。

最大厚度 A_Y=m h_Y^* 的未截帽公式为

\[
A_Y=m\left(\frac{m+1}{2}\right)^{1/m}
\frac{Y^{-\lambda(1-\theta)/m}}
{(\lambda\log Y)^{1+2/m}}.
\]

m=1 恢复上一轮选择；m=2 得到

\[
\boxed{A_Y=\sqrt6\,
\frac{Y^{-\lambda(1-\theta)/2}}{(\lambda\log Y)^2}.}
\]

对于相同窗口误差预算，两厚度最大厚度与原单厚度之比为

\[
\sqrt6\,Y^{\lambda(1-\theta)/2}(\lambda\log Y),
\]

对固定参数趋向无穷。它改善的是此标量读出的近似误差与厚度折衷；它本身不证明新读出的能量更小。

### 5.1 对实际 WindowHyp 的条件能量转移

定义

\[
\mathscr E^{[m]}_\theta(Y)=
\int_Y^{Y^\lambda}
(\mathscr G^{[m]}_{h_Y}(y)_+)^2y^{-2\theta-1}\,dy.
\]

若

\[
\forall\alpha>0\ \forall Y_0\ge e\ \exists Y\ge Y_0:
\quad\mathscr E^{[m]}_\theta(Y)\le Y^\alpha,
\]

则上一轮完整的 Cauchy–Schwarz 论证原样适用：取

\[
R(y)=(\mathscr G^{[m]}_{h_Y}(y))_++y^\theta,
\]

即可得到外部实际 WindowHyp，并在采用该外部 Landau 定理的前提下推出 Re(s)>θ 的非零性。这里传入解析定理的仍是固定 G；带符号的多厚度读出只承担有限窗口近似，不替代外部正权重角色族。

此条件能量界尚未证明。本稿没有从更高的逼近阶数推出 RH。

## 6. 系数放大与单侧能量边界

### 6.1 两种输入精度的成本

若归一化输入 X_j=R_(jh)/(jh) 的误差均不超过 η，则

\[
D_{m,h}=\sum_j v_{m,j}X_j,
\qquad
|\delta D|\le(2^m-1)\eta.
\]

同样的放大常数适用于已经中心化的 mathscr G_(jh)。这是精确的 l1 算子范数：允许输入误差独立取权重相反的符号即可达到。

若原始 R_(jh) 的绝对误差均不超过 η，则

\[
|\delta D|\le\frac{A_m}{h}\eta,
\quad
A_m=\sum_{j=1}^m\frac{\binom mj}{j}
=\sum_{j=1}^m\frac{2^j-1}{j}.
\]

最后一个恒等式由积分 ((1+x)^m-1)/x、代换 u=1+x 后展开几何级数取得。并且

\[
A_m\ge(2^m-1)/m.
\]

m=2、最大厚度 A=2h 时，原始道路误差放大为 5η/A；归一化读出误差放大为 3η。升阶需要计入精度与相关性成本。

### 6.2 旧正部能量不足以直接控制新正部

对任何实数族 g_j，有

\[
\left(\sum_j v_{m,j}g_j\right)_+
\le\sum_{j\text{ odd}}\binom mj(g_j)_+
+\sum_{j\text{ even}}\binom mj(g_j)_-.
\]

因此若采用逐项三角估计，偶数厚度输入需要负部信息。仅知道所有 (g_j)_+ 的能量，不能普遍控制组合正部。例如 m=2、g_1=0、g_2=-M，两个输入正部均为零，但 2g_1-g_2=M。

这个代数反例说明某种一般不等式不存在，并不声称真实道路会实现任意指定 g_j。实际研究应直接控制组合的相关能量，或保留足够的两侧交叉信息。

此外新 D 是带符号的标量读出，并不是另一个正道路质量。既有全阶接触公式表明，对具有恰好 m+1 个不同素因子的 n，

\[
D_{m,h}(n)=(-1)^{m+1}m!h^m\prod_{p\mid n}\log p+O_n(h^{m+1}).
\]

例如 m=2、n=30 时，小厚度下 D 为负，而每一个输入道路 R_h(30)、R_(2h)(30) 仍严格为正。全部联合层作为输入保留；它们在所声明读出中的标量组合不等于原生状态删除。

## 7. 与全尾中心常数的兼容消去

以下供全尾能量路线使用；精确尾恒等式由相应协作稿独立建立。设

\[
c(a)=1/\zeta(1+a),\qquad
d(a)=(\gamma-1)c(a)+c'(a)-1.
\]

由 ζ 在 1 的 Laurent 展开，c 在 0 可去奇点并且

\[
c(0)=0,\ c'(0)=1,\ c''(0)=-2\gamma;
\qquad d(0)=0,\ d'(0)=-(1+\gamma).
\]

它们在 0 附近是实解析函数。因而同一个前向导数定理给出

\[
\left|\sum_jv_{m,j}\left(\frac{c(jh)}{jh}-1\right)\right|
\le\frac{h^m}{m+1}\sup_{0\le t\le mh}|c^{(m+1)}(t)|,
\]

\[
\left|\sum_jv_{m,j}\left(\frac{d(jh)}{jh}+1+\gamma\right)\right|
\le\frac{h^m}{m+1}\sup_{0\le t\le mh}|d^{(m+1)}(t)|.
\]

对固定 m、小 h，两项均为 O_m(h^m)。所以如果尾表示中的显式漂移正是这两个系数乘 y logy、y，升阶后漂移为 O_m(h^m y logy)，并没有遗留一个未经消去的 O(h)y 主项。

这个固定阶结论不自动提供 m→∞ 时导数上确界的统一控制。把 m 随窗口增加、从局部 Q_a 假设推出全部窗口结论，需要另行跟踪这些常数以及 2^m-1 的输入放大。

## 8. 验证与保留前沿

verify_multithickness.py / multithickness_results.json 检查：

- Fraction 精确权重矩、Peano 核质量相关矩与有限核符号采样；
- 通过除数展开独立计算道路导数，与乘积导数上界比较；
- 全整数有限样本上的外推误差及单位端口；
- 素数幂精确积分误差和常数渐近饱和；
- 全人口有限平滑、归一化组合恒等式和完整窗口内的误差样本。

数值部分使用 mpmath 90 位高精度，非区间算术；一般结论由本稿证明支持。有限样本不会推出全局能量上界。没有重复上一轮已完成的全部实验，也未重新运行外部 Lean 工程。

可接手的精确问题是：在厚度增厚带来的收益与带符号权重成本之间，证明多厚度正部窗口能量、或从真实的跨厚度相关性得到足够估计。固定有限阶可以分别选择；任何依赖 m 增长的推论都应把常数与资源预算写清。
