# 随阶数增长的背景控制与条件能量传递

Date: 2026-11-21 (Asia/Hong_Kong)
Researcher: EM-DIRECT-B5750A / TASK_RESEARCH
Status: AUTHOR_PROVED_UNIFORM_INTERPOLATION_BOUNDS; ROAD_ENERGY_PREMISE_EXPLICIT.

本稿接续 CHEBYSHEV_THICKNESS_BRIDGE.md。节点权重ν的总和为1、绝对和为3，m=ceil(logZ)，最小节点b=Θ((logZ)^−2)。这里把最大厚度选为固定 A≤1/8，以得到背景系数的统一复分析余界。这个常数选择与前稿A=1/2的直接误差桥分别成立。

对象仍为心跳世界X6上的完整道路标量读出，保留全部整数/合数输入、厚度标签、原点及边界端口；复分析只用于该读出系数。科学前提沿用项目@9fc068244e4f1117f1e75df5eb0285c6697d21d7，前轮尾恒等式见@824b102adf7095090c43c5f2112e42334fdd32e4的CENTERED_TAIL_AND_WINDOW_ENERGY.md。

## 1. 一个无条件的解析邻域

设

\[
f(a)=a\zeta(1+a),\qquad g(a)=1/f(a),\qquad f(0)=g(0)=1.
\]

对Re s>1，Abel求和给

\[
\zeta(s)=s\int_1^\infty\lfloor x\rfloor x^{-s-1}\,dx
=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.
\]

后一积分对Re s>0绝对收敛，给出该区域的解析延拓。代入s=1+a：

\[
f(a)=1+a-a(1+a)\int_1^\infty\{x\}x^{-2-a}\,dx.
\]

于是对0<R<1、|a|≤R，

\[
\boxed{|f(a)-1|\le R+\frac{R(1+R)}{1-R}
=\frac{2R}{1-R}.}
\tag{1}
\]

取R=3/10得到|f−1|≤6/7<1，所以g在该闭圆盘邻域内解析，且|g|≤7。取ρ=1/4得到|g|≤3；以半径R−ρ=1/20使用Cauchy导数估计，则

\[
\boxed{|g(a)|\le3,\quad |g'(a)|\le140
\quad(|a|\le1/4).}
\tag{2}
\]

这里没有使用RH或关于临界带的零点假设；不消失来自(1)的直接局部估计。

## 2. 两个背景系数的统一界

前轮定义c_a=1/ζ(1+a)=ag(a)，κ_a=(γ−1)c_a+c'_a−1，并写

\[
\mathscr G_a(y)=y[b(a)\log y+d(a)]
-y\int_y^\infty U_a(t)a^{-1}t^{-2}\,dt,
\]

其中

\[
b(a)=g(a)-1,
\quad d(a)=1+\gamma+(\gamma-1)g(a)+\frac{g(a)-1}{a}+g'(a).
\]

从ζ在1处的Laurent常数得到g'(0)=−γ，故b(0)=d(0)=0。由于(g(a)−1)/a=∫_0^1g'(ta)dt，由(2)及0<γ<1，有

\[
|d(a)|\le2+3+140+140=285<300\qquad(|a|\le\rho).
\tag{3}
\]

对在|z|≤ρ解析、绝对值≤M的函数q，以正节点a_j≤A<ρ外推至0，留数公式给

\[
q(0)-\sum_j\nu_jq(a_j)
=\frac1{2\pi i}\int_{|z|=\rho}
\frac{q(z)}z\frac{\prod_j(-a_j)}{\prod_j(z-a_j)}\,dz.
\]

因此

\[
\boxed{\left|q(0)-\sum_j\nu_jq(a_j)\right|
\le M\frac{\prod_ja_j}{(\rho-A)^m}.}
\tag{4}
\]

取前稿K=3的切比雪夫节点，写q_m=(∏a_j)/A^m。A≤ρ/2=1/8时，A/(ρ−A)≤1；于是

\[
\boxed{|b_{\boldsymbol a}|\le3q_m,\qquad
|d_{\boldsymbol a}|\le300q_m,\qquad
q_m\le\frac{32}{(m-1)4^m}.}
\tag{5}
\]

这里b_a组合用g(0)=1及Σν=1，d_a组合用d(0)=0。所有常数显式，可以用于m随窗口增长。

## 3. 条件道路能量的精确传递成本

本节明确假设：存在C>0、a_0>0，使项目原始道路能量

\[
\mathcal Q_a=c_a^2+\int_1^\infty U_a(t)^2t^{-2}\,dt\le Ca
\quad(0<a\le a_0).
\tag{H}
\]

项目已把(H)列为RH等价强条件；本稿不证明(H)，本节作用是核对从这个既有接口到窗口接口的统一代价。

选固定0<A≤min(1/8,a_0)，节点最小值b，定义归一化完整残差

\[
J(t)=\sum_j\frac{\nu_j}{a_j}U_{a_j}(t).
\]

Minkowski及(H)给

\[
\left(\int_1^\infty J(t)^2t^{-2}\,dt\right)^{1/2}
\le\sqrt C\sum_j\frac{|\nu_j|}{\sqrt{a_j}}
\le3\sqrt{C/b}.
\tag{6}
\]

对1/2≤θ<1，t≥Y有t^(−2θ−1)≤Y^(1−2θ)t^(−2)。前轮已证加权Hardy不等式因此给

\[
\boxed{\int_Y^\infty y^{1-2\theta}
\left(\int_y^\infty J(t)t^{-2}\,dt\right)^2dy
\le\frac{9C}{b(1-\theta)^2}Y^{1-2\theta}.}
\tag{7}
\]

令L=logZ≥10、m=ceilL；漂移项的窗口能量由(5)界为

\[
E_{\rm drift}\le
\left[\frac{32(3L+300)}{(m-1)4^m}\right]^2
A_\theta(Y,Z),
\qquad A_\theta(Y,Z)=\frac{Z^{2-2\theta}-Y^{2-2\theta}}{2-2\theta}.
\tag{8}
\]

完整平方上界当然也是正部平方的上界。合并(7)–(8)：

\[
\boxed{E_+(\mathscr G_{\boldsymbol a};Y,Z)
\le\frac{18C}{b(1-\theta)^2}Y^{1-2\theta}
+2\left[\frac{32(3L+300)}{(m-1)4^m}\right]^2A_\theta(Y,Z).}
\tag{9}
\]

对固定λ>1、Z=Y^λ，b=Θ_A((logZ)^−2)、m=ceil(logZ)，所以

\[
E_+\ll_{C,A,\theta,\lambda}
(\log Y)^2Y^{1-2\theta}
+Z^{2-2\theta-2\log4}.
\tag{10}
\]

对每个固定θ>1/2，(10)趋于0；θ=1/2时也是次幂增长。固定m桥中的额外θ阈值在这个明确前提下消失。该结论属于接口传递的改进，未改变(H)的未证状态。

## 4. 与有限窗口研究的分工

无条件部分(1)–(5)完成自适应阶数的背景误差估计。条件部分(6)–(10)量化已有强道路能量输入的代价。实际有限窗口仍可直接使用无需ζ背景的完整道路端点公式和真实正部积分，保留内部量与右端通量的相关抵消；本轮tail分支研究的正部凸性与均值/方差分解正用于这个方向。

数值核对只检验所声明参数的系数与恒等式；普遍界由上述证明承担。数学作者核对、正式Result与项目独立Review分别记录。
