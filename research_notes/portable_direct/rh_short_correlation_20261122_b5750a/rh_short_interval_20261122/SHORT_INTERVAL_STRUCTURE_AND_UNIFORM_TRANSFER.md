# 真实系数的短区间结构与全部窗口的一致转移

Researcher-ID: `EM-DIRECT-B5750A / TASK_RESEARCH`  
Research-Activity-ID: `RA-60C6D083A81B19084A74C5BA`  
Date: 2026-11-22 UTC  
Status: 作者证明的精确恒等式、无条件截断界及一致稳定界；临界算术消失仍未证明。

科学输入冻结于 `enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7`。本稿沿用完整道路、全部整数与合数人口、单位、全部厚度标签、原点背景和真实前史。以下的 Möbius 逆、带符号和以及 `Lambda` 都是已声明的辅助标量观察；没有以辅助参考替换原生 P000 道路，也没有把带符号相消解释为 BRC 正质量消灭。本稿属于同作者推导，不构成独立 Project Review。保存和控制记录由父任务处理。

## 1. 输入与这次实际推进的部分

直接使用的既有作者结果为：

- `rh_integer_kernel/POSITIVE_KERNEL_AND_LAPLACE_BOUND.md` 的正卷积核、完整因子恒等式及单纯形误差界；
- `rh_joint_variance/JOINT_VARIANCE_GROWTH.md` 的真实系数结构；
- `rh_triangle_arithmetic_20261122/TRIANGLE_KERNEL_AND_PHASE_COMMUTATION.md` 的三角整除核与短区间 `C_0,C_1` 接口；
- `riemann_adaptive_window_20261121/rh_next_root/CHEBYSHEV_THICKNESS_BRIDGE.md` 的式 (11)，以及 `rh_correlation_rational/NOTES.md` 的有理节点乘积界；
- `riemann_triangle_correlation_20261122/REPORT.md` 中使用真实端点的骨架和分层能量读出。

新增结论有四个：真实 `c` 相对参考 `c*` 的误差恰为 `mu(n) I(log n)`；背景 `epsilon=kappa-1` 有精确总质量及可量化的短区间卷积尾；整个 `c` 向量相对参考的 `ell^1` 误差随稳定族绝对趋零；原道路的全部三角层、同一真实骨架和完整前史的加权正能量都能一致转移。因此有限厚度近似本身不再是这些读出的未知算术部分。

## 2. 有限厚度误差只出现于平方自由系数

取不同正厚度 `a_1,...,a_m`，使用重新精确计算的原点 Lagrange 权

\[
\nu_j=\prod_{k\ne j}\frac{a_k}{a_k-a_j},\qquad
\Psi(t)=\sum_j\frac{\nu_j}{a_j}(1-e^{-a_jt}),\qquad I(t)=t-\Psi(t).
\]

既有正核证明给出 `I(t)=E(t-T)_+`，其中 `T` 是这些率的独立指数变量之和。这仅是同一确定性标量核的辅助表示。特别地，`I(0)=0`、`I` 非负递增，且

\[
0\le I(t)\le C_{\boldsymbol a}t^{m+1},\qquad
C_{\boldsymbol a}=\frac{\prod_j a_j}{(m+1)!}.
\tag{1}
\]

记 `1` 为恒一算术函数，`delta_1` 为 Dirichlet 卷积单位。完整道路，包括已修复的 `D(1)=0`，满足

\[
D=1*(-\mu\Psi(\log)),\qquad
\Lambda=1*(-\mu\log),\qquad c=\mu*(D-\kappa).
\]

定义辅助参考 `c*=mu*(Lambda-kappa)`。对全部整数 `n>=1`，精确有

\[
\boxed{c(n)=-\mu(n)\Psi(\log n)-(\mu*\kappa)(n),\qquad
c^*(n)=-\mu(n)\log n-(\mu*\kappa)(n),}
\tag{2}
\]

\[
\boxed{c(n)-c^*(n)=\mu(n)I(\log n).}
\tag{3}
\]

证明只需对两个完整道路施加 `mu*`，并用 `mu*1=delta_1`。没有逐素数截断或交换无限和。

因此：

- 含平方因子的 `n` 上，`c(n)=c*(n)` 精确成立。这些系数仍在完整人口内；它们是背景卷积的真实贡献，并非被删去。
- 平方自由 `n>=2` 上，误差具有 `mu(n)` 的符号；既有真实系数符号公式还表明它把参考系数的绝对值减小 `I(log n)`。
- 单位保持 `c(1)=c*(1)=-2 log 2`，不是 `-1`。
- `mu*(D-Lambda)` 不需要用 `eta tau(n)` 估计；它已经由式 (3) 精确化简。

同时

\[
D(n)-\Lambda(n)=\sum_{d\mid n}\mu(d)I(\log d).
\tag{4}
\]

式 (4) 并不保证多因子道路误差同号。

## 3. 背景曲率的精确质量与尾界

对 `n>=1` 置

\[
\kappa_n=n\{(n+1)\log(n+1)-2n\log n+(n-1)\log(n-1)\},
\quad\epsilon_n=\kappa_n-1,
\]

其中 `0 log 0=0`，故 `epsilon_1=2 log 2-1=:c_0`。直接展开 `log(1+z)`、`log(1-z)` 并在 `n=1` 取单调极限，得到正项级数

\[
\boxed{\epsilon_n=\sum_{r=1}^{\infty}
\frac{n^{-2r}}{(r+1)(2r+1)},\qquad
0<\epsilon_n\le\frac{c_0}{n^2}.}
\tag{5}
\]

令 `g(n)=n log n`。对 `n Delta^2 g(n)` 有限求和后，所有内部项抵消。因此

\[
\boxed{\sum_{n=1}^{N}\epsilon_n
=N(N+1)\log(1+1/N)-N.}
\tag{6}
\]

令 `N` 趋于无穷，得到精确质量

\[
\boxed{\sum_{n\ge1}\epsilon_n=\frac12,\qquad
\sum_{n\ge2}\epsilon_n=\frac32-2\log2.}
\tag{7}
\]

尾质量也有正积分而非仅有渐近式：

\[
\boxed{R_N:=\sum_{n>N}\epsilon_n
=N+\frac12-N(N+1)\log(1+1/N)
=\int_0^1\frac{t(1-t)}{N+t}\,dt.}
\tag{8}
\]

最后一个等式由多项式除法直接积分验证。因此，对 `N>=1`，

\[
\frac1{6(N+1)}\le R_N\le\frac1{6N},\qquad
R_N\ge\frac1{6N}-\frac1{12N^2},\qquad
\sum_{n>N}\frac{\epsilon_n}{n^j}\le\frac1{6N(N+1)^j}\quad(j\ge0).
\tag{9}
\]

较细下界使用 `1/(N+t)>=1/N-t/N^2`。

由 `mu*kappa=delta_1+mu*epsilon`，式 (2) 变为

\[
\boxed{c(n)=-\mu(n)\log n-\delta_{n1}
-(\mu*\epsilon)(n)+\mu(n)I(\log n).}
\tag{10}
\]

绝对可和的是 `epsilon` 本身。`mu*epsilon` 是保留全部除数的 Dirichlet 卷积，不能据此删掉。一个合法但较粗的点态后果为

\[
|(\mu*\epsilon)(n)|\le\sum_{k\mid n}\epsilon_k\le\frac12.
\tag{11}
\]

故 `n>=2` 时 `|c*(n)+mu(n)log n|<=1/2`；含平方因子的真实 `c(n)` 也满足此界。既有 `beta(n)<=c_0` 对该背景还给出更强常数。本稿的短区间分析继续保留式 (10) 中的实际卷积。

## 4. 两个真实短区间矩的精确归约

对实数 `0<=U<V` 和 `j=0,1`，定义

\[
C_j(U,V)=\sum_{U<n\le V}\frac{c(n)}{n^j},\quad
L_j(U,V)=\sum_{U<n\le V}\frac{\mu(n)\log n}{n^j},\quad
M_j(u,v)=\sum_{u<r\le v}\frac{\mu(r)}{r^j}.
\]

原三角接口中的 `C_j(U,V;H)` 恰为本节 `C_j(max(U,H),V)`，若下端不小于上端则为零。有限交换除数和给出

\[
\boxed{
C_j(U,V)=-L_j(U,V)-\mathbf1_{U<1\le V}
-\sum_{k\le V}\frac{\epsilon_k}{k^j}M_j(U/k,V/k)
+\sum_{U<n\le V}\frac{\mu(n)I(\log n)}{n^j}.}
\tag{12}
\]

这里没有独立性假设，也没有把不同 `k` 的联合和换成随机量。`k=1` 的背景项恰为 `epsilon_1 M_j(U,V)`；`k>=2` 的其余实际除数项仍全部保留。

### 4.1 背景高除数尾可无条件支付

设 `U>0`、`h=V-U`、整数 `K>=1`，把式 (12) 中背景和截到 `k<=K`。余项记为 `T_{j,K}`。区间内 `n=kr` 有 `n^{-j}<=U^{-j}`，而其中 `r` 的个数至多 `h/k+1`，也至多 `V/k`。由式 (9)，

\[
\boxed{|T_{j,K}|\le\frac1{U^j}
\min\left\{\frac{V}{6K(K+1)},
\frac{h}{6K(K+1)}+\frac1{6K}\right\}.}
\tag{13}
\]

若 `K>=floor V`，余项精确为零；此时可直接使用零而不使用式 (13) 的上界。

特别地，`h>=1` 时取 `K=ceil sqrt(h)`，背景高除数尾至多

\[
|T_{j,K}|\le U^{-j}\left(\frac16+\frac1{6K}\right).
\tag{14}
\]

这使短区间背景的高除数部分成为有界误差。未解决的部分是主项 `L_j` 及明确的有限组低 `k` Möbius 和；不是一个未量化的无限背景尾。式 (13) 在系数层有效，尚未宣称把它逐项代入三角外层 `k` 求和后可免费丢弃所有累计成本；外层仍按既有精确核联合计算。

### 4.2 局部 Möbius 前缀到底需要控制什么

记

\[
\mathcal M(u,v)=\sup_{u\le t\le v}
\left|\sum_{u<r\le t}\mu(r)\right|.
\]

分部求和给出，对 `U>=1`，

\[
L_0(U,V)=\log V\,M_0(U,V)
-\int_U^V\frac{M_0(U,t)}t\,dt,
\]

\[
|L_0(U,V)|\le[\log V+\log(V/U)]\mathcal M(U,V).
\tag{15}
\]

当 `U>=e` 时，`log t/t` 非负递减，故

\[
|L_1(U,V)|\le\frac{\log U}{U}\mathcal M(U,V).
\tag{16}
\]

离散分部求和同样给出完整背景的确定性界

\[
\left|\sum_{k\le V}\frac{\epsilon_k}{k^j}M_j(U/k,V/k)\right|
\le\sum_{k\le V}\frac{\epsilon_k}{\max(k,U)^j}
\mathcal M(U/k,V/k),\quad j=0,1.
\tag{17}
\]

这里使用第一项实际整数至少为 `max(1,U/k)`；没有在 `U/k<1` 的区域使用错误的连续积分下端。

例如，**如果另行证明**本次所需的全部膨缩区间同时满足
`mathcal M(u,v)<=A sqrt(v-u+1)`，则式 (17) 至多

\[
\frac{A}{U^j}\left(\sqrt h\sum_k\frac{\epsilon_k}{\sqrt k}
+\sum_k\epsilon_k\right)
\le\frac{A}{2U^j}(\sqrt h+1).
\tag{18}
\]

这是精确说明背景如何继承一个已证明的局部界；本稿没有证明这个局部平方根假设。单点道路的符号、完整周期方差或有限窗口样本，都不能代替它。实际三角问题还可从联合核获得较逐区间绝对值更强的控制；本节没有将这种可能性排除。

## 5. 整个真实 `c` 向量与参考的误差绝对趋零

定义 `eta_Z=C_a(log Z)^{m+1}`。既有插值余项和式 (1) 同时给出

\[
\max_{n\le Z}|D(n)-\Lambda(n)|\le\eta_Z,
\qquad \max_{n\le Z}I(\log n)\le\eta_Z.
\tag{19}
\]

式 (3) 立刻给出有限向量的确定性界

\[
\boxed{\sum_{n\le Z}|c(n)-c^*(n)|
=\sum_{n\le Z}|\mu(n)|I(\log n)\le Z\eta_Z.}
\tag{20}
\]

因此对所有短区间同时成立

\[
|C_0(U,V)-C_0^*(U,V)|\le\eta_V(\lfloor V\rfloor-\lfloor U\rfloor),
\]

\[
|C_1(U,V)-C_1^*(U,V)|\le\eta_V\sum_{U<n\le V}\frac1n.
\tag{21}
\]

对稳定有理节点族取 `Z>=e^10`、`m=ceil(log Z)`。旧理想节点的道路误差常数是 `128/(3 log Z)`，有理化将节点乘积最多乘 `64/63`。因此直接复核得

\[
\boxed{\eta_Z\le\frac{K_0}{\log Z}\rho^m,
\qquad K_0=\frac{8192}{189},\quad \rho=\frac e8.}
\tag{22}
\]

置 `beta=log 8-1>1`，则 `rho^m<=Z^{-beta}`，所以

\[
\boxed{\sum_{n\le Z}|c_Z(n)-c^*(n)|
\le\frac{K_0Z^{1-\beta}}{\log Z}\longrightarrow0.}
\tag{23}
\]

这里 `c_Z` 使用由终端 `Z` 一次选定、对全部 `n<=Z` 共用的同一厚度族；没有逐 `n` 或逐区间重选参数。式 (23) 是全部短区间与线性读出系数绝对值具有共同固定上界的整个族的一致稳定，不是关于未匹配范围 `n>Z` 的声明。每条真实厚度通道和有限精确误差仍在原生状态内。

## 6. 三角层的误差从道路源直接支付

设整数包 `p=(L,x,R)` 满足 `X<=L<x<R<=Y<=2X`，长度 `h=R-L`，高度一三角帽为 `Phi_p`。原道路与辅助参考使用相同仿射背景、单位及完整前史。写

\[
e_n=D_n-\Lambda(n),\quad f_n=(\kappa_n-D_n)/n,
\quad f_n^*=(\kappa_n-\Lambda(n))/n.
\]

由三点读出，

\[
\boxed{t_p-t_p^*=-\sum_{L<n<R}\frac{\Phi_p(n)e_n}{n}.}
\tag{24}
\]

记 `K_{1,p}=sum Phi_p(n)/n`。整数三角帽精确满足 `sum Phi_p(n)=h/2`，故

\[
|t_p-t_p^*|\le\eta_R\mathcal K_{1,p}
\le\frac{\eta_Rh}{2X}.
\tag{25}
\]

取同层内部互不交的全部实际包，最长长度 `delta`，总长度不大于 `b=Y-X<=X`。定义上一轮使用的归一化层根

\[
\mathcal N_{X,\ell}(t)=
\left(\frac1{X^2}\sum_{p\in\ell}h_p^3(t_p)_+^2\right)^{1/2}.
\]

因为 `z->z_+` 为 1-Lipschitz，Minkowski 不等式与 `sum h_p^5<=delta^4 b` 给出

\[
\boxed{|\mathcal N_{X,\ell}(t)-\mathcal N_{X,\ell}(t^*)|
\le\frac{\eta_Y}{2X^2}\left(\sum_{p\in\ell}h_p^5\right)^{1/2}
\le\frac{\eta_Y\sqrt b\,\delta^2}{2X^2}.}
\tag{26}
\]

完整最粗块的右端至多 `eta_Y sqrt X/2`。这是所有包及所有层同时成立的确定性界；无须先证明任何 Möbius 消失。

还可将所有层的诊断以平方和一起比较。一个整点二叉消元树在长 `b` 的块上最多有 `b-1` 个内部包，且每包长度不大于 `b`，所以 `sum_all p h_p^5<=b^6`。对任意块分解及任意这类树，令

\[
\mathcal N_{\mathrm{all}}(t)=
\left(\sum_{[X,Y]}\frac1{X^2}
\sum_{p\text{ in the block}}h_p^3(t_p)_+^2\right)^{1/2}.
\]

则

\[
|\mathcal N_{\mathrm{all}}(t)-\mathcal N_{\mathrm{all}}(t^*)|
\le\frac{\eta_B}{2}\left(\sum_{[X,Y]}b^2\right)^{1/2}
\le\frac{\eta_B(B-A)}2\longrightarrow0.
\tag{27}
\]

此处平方汇总仅用于一致稳定的陈述。它不是把原证明所需的逐层正部分预算换成新的充分条件；若选用逐层根的总和，仍须按原有树结构支付该总和。

## 7. 真实骨架与完整前史不会额外放大误差

原观察量为 `q(y)=sum_(2<=n<=y) D_n(y/n-1)-y log y+(1+gamma)y`，其中 `D_1=0`。令 `q*` 在相同规范下把辅助读出中的 `D` 换成 `Lambda`，但保留全部前史、单位和完全相同的仿射项。于是对所有实数 `y>=1`，

\[
\boxed{E(y):=q(y)-q^*(y)
=\sum_{2\le n\le y}e_n(y/n-1).}
\tag{28}
\]

由 `sum_{2<=n<=y}1/n<=log y`，在同一终端族 `B` 内，

\[
|E(y)|\le\eta_B y\log y\le K_0\rho^m y
\quad(1\le y\le B).
\tag{29}
\]

因此完整前史在整个窗口的点态上界亦为 `K_0 B rho^m<=K_0 B^{1-beta}->0`。

对整数窗口 `[A,B]`，设

\[
\|v\|_w^2=\sum_{n=A}^{B}\frac{|v(n)|^2}{n^2}.
\]

则

\[
\boxed{\|q-q^*\|_w\le K_0\rho^m\sqrt{B-A+1}.}
\tag{30}
\]

取任意保留真实端点的共同整点骨架 `Pi`，记其线性插值为 `J_Pi`。在相邻骨架端点 `u,v` 间，插值权非负且加权端点恰为 `n`。所以式 (29) 逐点蕴含

\[
|J_\Pi E(n)|\le K_0\rho^m n,
\qquad
\boxed{\|J_\Pi q-J_\Pi q^*\|_w
\le K_0\rho^m\sqrt{B-A+1}.}
\tag{31}
\]

这个界对所有合法共同骨架一致；包括根据真实数据选择骨架之后再固定同一个骨架进行比较。它不比较两套独立重选、端点不同的骨架。

设 `S(v)=sum (v(n)_+)^2/n^2`。正部分的非扩张性给出

\[
\boxed{|\sqrt{S(q)}-\sqrt{S(q^*)}|\le\|E\|_w,\qquad
|\sqrt{S(J_\Pi q)}-\sqrt{S(J_\Pi q^*)}|
\le\|J_\Pi E\|_w.}
\tag{32}
\]

由 `beta>1`，右端最多为 `K_0 B^{1/2-beta}`，随终端增大趋零。这使真实族与参考族相应能量根的趋零结论等价；它并没有证明任一方已经趋零。此前完整前史里可能较大的仿射量不会在式 (31) 中被偷偷重置。

## 8. 背景局部曲率可付，但骨架上的仿射前史仍须保留

为辨明剩余阻力，可进一步把参考局部源写成

\[
\frac{\kappa_n-\Lambda(n)}n
=\frac{1-\Lambda(n)}n+\frac{\epsilon_n}n.
\]

这是辅助分解。由式 (5)，`epsilon_n/n<=c_0/X^3` 于块内成立。因此与第 6 节同样计算，背景非恒定曲率对某层归一化根的影响至多

\[
\boxed{\frac{c_0\sqrt b\,\delta^2}{2X^4}
\le\frac{c_0}{2X^{3/2}}.}
\tag{33}
\]

它在所有中粗层上均无条件可付。不过，不能据此从完整骨架删去 `epsilon` 的前史。为直接看见这一点，保留单位的完整背景势为

\[
\mathcal B(N)=\sum_{n\le N}\epsilon_n(N/n-1).
\]

再一次有限望远镜求和给出

\[
\sum_{n\le N}\frac{\epsilon_n}n
=(N+1)\log(N+1)-N\log N-H_N,
\quad\sum_{n\ge1}\frac{\epsilon_n}n=1-\gamma.
\tag{34}
\]

与式 (6) 合并后，

\[
\boxed{\mathcal B(N)=N(\log N-H_N+1)
=(1-\gamma)N-\frac12+r_N,}
\]

\[
r_N=\sum_{n>N}\epsilon_n(1-N/n),\qquad
0<r_N\le R_N\le\frac1{6N}.
\tag{35}
\]

完整背景有确定的线性项和常数项；仅其消去仿射后的余项很小。式 (35) 特意含 `n=1` 的 `epsilon_1(N-1)`。直接的单位端口校验是

\[
\sum_{n=1}^{N}\kappa_n(N/n-1)=N\log N,
\quad
q(N)=\sum_{n=1}^{N}(D_n-\kappa_n)(N/n-1)+(1+\gamma)N.
\tag{36}
\]

因为 `D_1=0`，第一种原道路写法中的 `D` 前缀从 `2` 开始，而背景的完整恒等式从 `1` 开始；两者并不冲突。若把单位背景端口另列，就必须同步保留该项，不能移除后沿用相同骨架和端点值。

## 9. 已分离的成本与仍然开放的算术部分

在由终端 `B` 选择的一般稳定有理族内，已经证明：

- 有限厚度误差对整个 `c` 向量的 `ell^1` 成本为 `O(B^{1-beta}/log B)`；所有短区间同时稳定。
- 它对原三角包、全部分层诊断、真实共同骨架和完整前史的正能量都有显式统一界。
- `epsilon` 的短区间高除数卷积尾能用式 (13) 无条件支付；其局部三角曲率更由式 (33) 支付。
- `epsilon` 的真实完整前史具有式 (35) 的确定仿射项。该项仍在原始道路和骨架内。

剩余的中粗尺度问题被具体压到参考联合算术读出：带对数的 Möbius 短区间和、有限组由 `epsilon_k` 加权的膨缩 Möbius 和，以及它们经过真实三角整除核后的联合符号。可以继续利用核级相消改善逐项绝对值，但本稿尚未得到足以封闭临界窗口能量的算术估计。正核身份、绝对可和背景和参数稳定并不自行提供该估计，也不证明黎曼猜想。

本轮兄弟任务 `rh_reference_certificate_20261122` 对既有完整道路缓存、全部实际 38 包、相同真实骨架及少量直接正核样点进行严格区间复算。其有限结果支持本稿恒等式的实现核对；本稿的一般结论依据上述证明，不依据样本外推。
