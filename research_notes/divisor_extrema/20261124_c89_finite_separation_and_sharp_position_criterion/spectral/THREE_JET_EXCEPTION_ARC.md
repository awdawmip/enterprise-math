# C89：三项库存谱确有不同正规原像——一维例外族的存在

## 1. 新结论

沿用原安排的连续归一谱

\[
F=(G,B_1),\qquad B_1=-(E+3/4)G,
\qquad B_2=-(E+7/4)B_1.
\]

C82 已证明 `(G,B₁,B₂)` 在整个可行源域中几乎处处单原像，并将可能的不同
原像限制在至多一维的半代数例外集。本篇证明这个例外集确实包含一维部分。

**定理。** 存在无穷多对不同源点 `X≠Y`，两点均位于

\[
0<\mathcal A<1,\qquad 0<d<1,
\quad \mathcal A=4x^{15/4},\ d=4(y/x)^{9/4},
\]

且均为 `F` 的正规点，使

\[
\boxed{G(X)=G(Y)>0,\quad B_1(X)=B_1(Y),\quad B_2(X)=B_2(Y).}
\tag{1}
\]

满足 (1) 的有序配对中存在一维半代数子集，其源投影包含有正长度的正规
解析弧。这些配对可任意接近左侧的非退化折叠曲线。

更具体地，可在一段紧折叠弧上选统一的 Morse 坐标 `(h,t)`，使对每个足够小的
`t>0`，至少有一个 `h=h_t` 满足 (1)，其配对正是 `(h_t,t)` 与 `(h_t,−t)`。

本结论关于原谱的连续宏观原像。整数安排的准确有限读数碰撞仍须用原整数
读数判定；本文不从 (1) 推出任一有限库存出现整数碰撞。

## 2. 所需已知结构与曲率坐标

为免与库存增量混淆，用 `𝒜` 表示谱坐标。令

\[
m=k\mathcal A^4d,\qquad k={7\over16},\qquad
u={m\over1+m},\qquad v={m\mathcal A\over1+m\mathcal A},
\]

\[
\nu(\mathcal A,d)={G\over C_*}
=\frac{\mathcal A^{19/5}d^{14/3}(1-\mathcal A)(1-d)}
{(1+m)(1+m\mathcal A)},
\]

\[
h={1\over\mathcal A-1}+5-4u-5v,
\qquad B_1=-{15\over4}hG,
\]

\[
T=4u(1-u)+5v(1-v),\qquad
N={\mathcal A\over(\mathcal A-1)^2}+16u(1-u)+25v(1-v).
\tag{2}
\]

C81–C82 在左侧 `0<𝒜<1` 已证明：

- `h𝒜=−N/𝒜<0`，`hd=−T/d<0`；对每个 `h<4`、`0<d≤4`，有唯一解析解
  `𝒜=a_h(d)`。
- 沿固定 `h`，`ν(a_h(d),d)` 在 `0<d<1` 有唯一内部峰值。
  记峰的位置为 `d_*(h)`、`𝒜_*(h)=a_h(d_*(h))`，峰值为 `M(h)>0`。
- 峰非退化；`νdd|h<0`。折叠曲线随 `h` 解析，且

\[
{8\over11}<d_*(h)\le{20\over23}.
\tag{3}
\]

C84 `BRANCH_TRANSITION.md` §3 已证明的曲率恒等式（其 `q` 就是本篇 `N`，
短推导重列于 `CURVATURE_AND_ALGEBRAIC_TAIL.md` §2）是

\[
\frac{B_2}{G}={225\over16}(h^2-N)+{15\over4}h.
\tag{4}
\]

所以本问题等价于：在同一 `(ν,h)` 的折叠两侧找到相同的 `N`。

沿固定 `h` 对 `log d` 求导，记

\[
\mathcal D=d\partial_d-{\mathcal A T\over N}\partial_{\mathcal A}.
\tag{5}
\]

这是因为 `d a'_h(d)=−𝒜T/N`。故

\[
\dot N:=\mathcal DN
=dN_d-{\mathcal A T\over N}N_{\mathcal A}.
\tag{6}
\]

## 3. 折叠曲线两端的曲率导数符号相反

下面的所有展开对 (3) 中的紧 `d` 区间一致，故可以直接用于随 `h` 变化的峰。

### 3.1 当 h 从下方趋于 4

由于 `u,v≥0`，

\[
h\le5+{1\over\mathcal A-1}
=4-{\mathcal A\over1-\mathcal A},
\]

所以沿折叠 `h↑4` 时必有 `𝒜_*→0`。在 `𝒜→0` 时，由 (2)

\[
T=4k\mathcal A^4d+O(\mathcal A^5),\qquad
N=\mathcal A+O(\mathcal A^2),
\]

\[
dN_d=16k\mathcal A^4d+O(\mathcal A^5),\qquad
N_{\mathcal A}=1+O(\mathcal A).
\]

于是

\[
{\mathcal A T\over N}N_{\mathcal A}
=4k\mathcal A^4d+O(\mathcal A^5),
\]

\[
\boxed{\dot N=12k\mathcal A^4d+O(\mathcal A^5)
={21\over4}\mathcal A^4d+O(\mathcal A^5)>0}
\tag{7}
\]

对充分接近 4 的 `h<4` 成立。这里 (3) 给 `d≥8/11`，因此首项的正性有统一
裕量。也可从已知折叠方程看出 `d_*→14/17`，但符号证明不需要这个极限。

### 3.2 当 h 趋于负无穷

式 (2) 中 `5−4u−5v` 有界，故 `h→−∞` 迫使 `𝒜_*→1−`。写
`ε=1−𝒜`。由 (3)，`T` 与 `S=16u(1−u)+25v(1−v)` 及其固定阶导数在这段
区域中一致有界，而且

\[
T(1,d)={9kd\over(1+kd)^2}>0
\]

在 (3) 中有一致的正下界。准确地，

\[
N={\mathcal A\over\varepsilon^2}+S,
\qquad N_{\mathcal A}={1+\mathcal A\over\varepsilon^3}+S_{\mathcal A},
\]

\[
{\mathcal A T\over N}=T\varepsilon^2+O(\varepsilon^4),
\qquad dN_d=O(1).
\]

代入 (6)，得到

\[
\boxed{\dot N=-{2T(1,d)\over\varepsilon}+O(1)<0}
\tag{8}
\]

对充分负的 `h` 成立。

因此可固定两个有限数

\[
h_-<h_+<4,
\]

使折叠点上的 `Ṅ(h_-)<0<Ṅ(h_+)`。

## 4. 同一折叠的两支曲率必在中间相遇

在紧参数区间 `I=[h_-,h_+]` 上，非退化峰与其正谱边距均有统一裕量。
定义

\[
t=\operatorname{sgn}(d-d_*(h))
\sqrt{M(h)-\nu(a_h(d),d)}.
\tag{9}
\]

在足够小且对整个 `I` 统一的邻域中，(9) 是保持 `d` 方向的解析坐标，且

\[
\nu=M(h)-t^2,
\qquad \partial_t d>0.
\tag{10}
\]

例如令
`M−ν=(d−d_*)²r(h,d)`，由峰的非退化性，`r` 在邻域中解析且严格为正；
则 (9) 就是 `t=(d−d_*)√r(h,d)`。紧性给统一正下界和统一逆函数邻域。

记源逆换元为 `X(h,t)`，并设 `Ñ(h,t)=N(X(h,t))`。相同 `h`、相反 `t`
的两点由 (10) 具有相同 `ν,h`，即相同的 `G,B₁`。置

\[
K(h,t)=
\begin{cases}
\displaystyle{\widetilde N(h,t)-\widetilde N(h,-t)\over2t},&t\ne0,\\[6pt]
\partial_t\widetilde N(h,0),&t=0.
\end{cases}
\tag{11}
\]

这是 `(h,t)` 的解析函数，并对 `t` 为偶函数。在折叠线上，

\[
K(h,0)={\dot N\over d}\,\partial_t d.
\tag{12}
\]

因为 `d>0`、`∂td>0`，(7)–(8) 给

\[
K(h_-,0)<0<K(h_+,0).
\]

连续性保证存在 `t₀>0`，使这两个严格符号同时保持于 `0≤t≤t₀`。
再缩小 `t₀`，保证 `M(h)−t²>0`。对任意固定 `0<t<t₀`，由 `h` 的介值定理，
存在 `h_t∈(h_-,h_+)` 使

\[
K(h_t,t)=0.
\]

所以 `N(X(h_t,t))=N(X(h_t,−t))`，(4) 遂给 (1)。因 `t≠0`，两个源点不同，
且在 Morse 形式下前两谱的 Jacobian 非零，所以它们都是 `F` 的正规源点。

取 `t→0` 的任意序列，再从紧区间 `I` 选收敛子列，即得这些真实三谱配对
趋近折叠上某个 `K(h,0)=0` 的点。

## 5. 一维半代数正规弧

上述曲率、峰、配对和正根坐标都是半代数的；局部解析逆图同样是原半代数
关系的有限分支。集合

\[
Z=\{(h,t):h_-<h<h_+,\ 0<t<t_0,\ K(h,t)=0\}
\]

的 `t` 投影包含整个 `(0,t₀)`，故其半代数维数至少为一。
另一方面 C82 已证不同源点共享三谱的源集合维数至多为一；这里
`(h,t)↦X(h,t)` 是解析微分同胚，因此 `dim Z≤1`。于是 `dim Z=1`。

这里使用半代数集合的有限 Nash 分层定理；可直接参见 Aizenbud–Gourevitch,
*De-Rham theorem and Shapiro lemma for Schwartz functions on Nash manifolds*,
Theorem A.2.2（文内第 21 页），及其 Remark 2.3.20（第 9 页）的实解析性说明：
<https://www.wisdom.weizmann.ac.il/~dimagur/RhamShap.pdf>。
半代数一维集合的有限 Nash 分片含有至少一段非平凡解析弧。限制到它的一个
紧子弧，并避开有限个分片端点，可令整个子弧满足 `t≥t₁>0`。其源投影为
有正长度的正规解析弧，配对支也正规且与源保持正距离。所有相关坐标和
Jacobians 在这条紧子弧上有统一界。

这一步只用于把已在 §4 逐 `t` 构造的配对集合写成标准的弧形式；定理中的
“每个小 `t` 有一对”已由介值定理独立证明。

## 6. 有限 Gamma 连续延拓中的三库存准确碰撞

本节仍将落点视为实变量，使用 C77–C79 已建立的 Gamma 连续延拓。库存本身
取真实整数。结论是这张连续延拓图上的准确相等，不加入整数落点条件。

**推论。** 对任意整数序列

\[
1\le A_c<B_c=o(c),
\tag{13}
\]

充分大 `c` 时，存在两对不同的实落点 `(v_c,w_c)`、`(v'_c,w'_c)`，均在
`2<w<v<c` 内，使其 Gamma 连续延拓的准确原读数在三个库存
`c,c+A_c,c+B_c` 上分别完全相等。两对归一落点均保持在固定内部紧集上，
且彼此的归一距离有正下界。

**证明。** 固定 §4 的一个足够小 `t_*>0`，使

\[
K(h_-,t_*)<0<K(h_+,t_*).
\tag{14}
\]

令 `X_±(h)=X(h,±t_*)`，`h∈I`。两条源路径均正规，彼此具有统一正距离，
且共享同一个目标路径

\[
Z(h)=F(X_+(h))=F(X_-(h)).
\]

置 `z_c=B_c/c`、`θ_c=A_c/B_c∈(0,1)`，使用 C88 的准确有限谱

\[
\mathcal G_c(t,X)=c^{3/4}\{g(c(1+t);cX)-1\},
\]

\[
U_c=\mathcal G_c(0,\cdot),\qquad
P_c={\mathcal G_c(z_c,\cdot)-U_c\over z_c},
\]

\[
Q_c={2\{\theta_c\mathcal G_c(z_c,\cdot)
+(1-\theta_c)U_c-\mathcal G_c(\theta_c z_c,\cdot)\}
\over\theta_c(1-\theta_c)z_c^2}.
\tag{15}
\]

在上述固定内部紧图上，已知有限谱与库存/源联合导数展开给

\[
(U_c,P_c)\longrightarrow(G,B_1)\quad\hbox{于 }C^1,
\qquad Q_c\longrightarrow B_2\quad\hbox{一致}.
\tag{16}
\]

第二个收敛对全部 `0<θ_c<1` 一致：C88 的插值误差积分将 (15) 写成
`∂_t²𝒢_c` 的一个质量为一的非负平均，采样参数落在 `[0,z_c]`。
因此 (13) 足够，并不需要舍入临界极限中较强的 `B_c/c^{1/3}→∞`。

用参数隐函数定理，沿紧目标路径 `Z(h)` 的两个正规逆图在 (16) 的扰动下
保持；有限局部图由同一原逆支附近的唯一性拼接。因此存在连续路径
`X_{±,c}(h)`，一致趋于 `X_±(h)`，且准确满足

\[
(U_c,P_c)(X_{+,c}(h))=(U_c,P_c)(X_{-,c}(h))=Z(h).
\tag{17}
\]

定义

\[
r_c(h)=Q_c(X_{+,c}(h))-Q_c(X_{-,c}(h)).
\]

它一致趋于

\[
r(h)=B_2(X_+(h))-B_2(X_-(h))
=-{225\over16}G(X_+(h))\,2t_*K(h,t_*).
\]

由 (14)，`r(h_-)>0>r(h_+)`，故充分大 `c` 时 `r_c` 在两端仍有相反严格
符号。介值定理给 `h_c∈I` 使 `r_c(h_c)=0`。连同 (17)，两个源点具有
完全相同的 `U_c,P_c,Q_c`。式 (15) 是三个库存准确读数的可逆线性重组，
因为 `0<θ_c<1`、`z_c>0`；故三个原读数逐个完全相同。

两条源路径所在紧集远离源域边界，且源对的归一距离有统一正下界。
因此乘回 `c` 后满足所述实落点范围并仍然不同。证毕。

## 7. 对有限分离筛选的直接含义

在第 5 节紧正规弧的一小邻域，可以固定一个解析配对支 `Y=T(X)`，
满足 `F(T(X))=F(X)`。令

\[
f(X)=B_2(T(X))-B_2(X).
\]

该函数在弧上为零，并在邻域中具有统一 Lipschitz 常数。弧可用一片管状坐标
`(s,z)` 表示，其中 `z=0` 是弧，源面积密度有正下界，且

\[
|f(s,z)|\le C|z|.
\tag{18}
\]

因此宽度为常数乘 `min(1,(Lτ)^{-1})` 的条带中，总有这条远支满足
`|(Lτ/2)f|≤1/2`，其 C88 相位允许概率至少为 `7/8`。由于这里 `J>0`
还有统一正下界，源支的近距唯一概率不会因逼近折叠而消失。

具体地，若 C89 的相位加权损失上界写成

\[
W_\tau(X)=\int_{-1}^1(1-|d_0|)
F_2\left({L^2J(X)\over1-|d_0|}\right)
\mathbf1\{\exists j:\ |d_0-h_j(X)|<1\}\,dd_0,
\]

则固定 `L>0` 后，可以直接只积分 `d₀∈[−1/4,1/4]`。当 `|h_j|≤1/2` 时这段
全部满足允许条件；固定紧管上若 `a=L²J∈[a_min,a_max]`，则
`a/(1−|d₀|)∈[a_min,4a_max/3]`。`F₂` 的连续正性给统一正下界，
配合 `1−|d₀|≥3/4` 及 (18)，得到常数 `c_L>0` 使

\[
\boxed{2\int_\Delta W_\tau(X)\,dX
\ge c_L\min\{1,\tau^{-1}\}.}
\tag{19}
\]

式 (19) 是现有相位保证下界与端点值之间的缺口下界；它不等同于原整数
唯一率实际缺口的下界。取得真实缺口仍需要耦合整数格中的竞争者信息。

## 8. 来源与证明强度

- C82 `FIBER_STRUCTURE.md`：左支全域单峰、解析折叠、非退化二阶项。
- C82 `HIGH_PRECISION.md`：折叠范围 `8/11<d≤20/23`、`N,T` 表达。
- C82 `CROSS_PHASE.md`：三谱不同原像的源集合维数至多一。
- C84 `BRANCH_TRANSITION.md` §3：准确曲率恒等式 (4)；科学提交
  `01f50954ee37548372464c68a311f7df2dba0632`，路径
  `research_notes/divisor_extrema/20261119_c84_precision_design_and_branch_filter/BRANCH_TRANSITION.md`。
  本轮 `CURVATURE_AND_ALGEBRAIC_TAIL.md` §2 重列短推导供核查。
- C88 `critical/FINITE_SEPARATION_BRANCH_FILTER.md` §1：准确有限差商及对
  `0<θ<1` 一致的二阶谱收敛；§6 的正规有限逆图延拓。

新增结果为 (7)–(8) 的两端符号、(11)–(12) 的介值构造、真实三谱正规配对族
及其正规弧、有限 Gamma 连续延拓稳定性推论。证明为完整手推分析论证；探索过程中曾用浮点值定位符号，
最终证明完全依赖所列准确恒等式和一致渐近展开，不以那些浮点值为证据。
