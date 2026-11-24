# 全正厚度的完整道路匹配尺度与非微扰主项

日期：2026-11-24（Asia/Hong_Kong）。作者统筹沿用 `EM-DIRECT-E7559A / TASK_RESEARCH`，Activity `RA-D2F111EA1C0D4B1DBEFBC1B4`。科学前驱为 `enterprise-math@791cf72261f1b705181b77f892e920a9bb0537c0:research_notes/portable_direct/rh_native_residual_growth_20261124_e7559a`，尤其 `matching/SHARP_SINGLE_THICKNESS_BIAS.md`。本稿为作者推导与核验，不是独立 Review。

全部对象继续是 P000 / Heartbeat X6 固定原生轴上的辅助标量观察。原完整背景、单位、合数关系、前史和真实端点保持；本稿只分析实际单厚度族的匹配尺度。

## 1. 主结果：去掉厚度参数的先验限制

仍令

\[
D_a(1)=0,\qquad
D_a(n)=\frac1a\prod_{p\mid n}(1-p^{-a})\quad(n\ge2),\qquad a>0,
\]

q_a 与 q* 使用原来的同一完整背景，源分别为 D_a 与 Λ。记

\[
g(a)=\frac1{\zeta(1+a)},\qquad
d(a)=\frac{g(a)}a,\qquad
\Delta(a)=1-d(a).
\tag{1.1}
\]

这里 Δ(a) 是本稿的单厚度平均质量亏损系数，与原累计场中的 δ_n 区分。

### 定理 1.1：全参数一致根渐近

设整数 B→∞、1≤A=A(B)≤B，且 A/B→0。不要求 A→∞。令 Π 遍历 [A,B] 上包含两个真实端点的全部整数节点网格。则

\[
\boxed{
\sup_{a>0}\left|
\frac{\|q_a-q^*\|_{w,[A,B]}}
{\Delta(a)\sqrt B\log B}-1\right|\longrightarrow0,
}\tag{1.2}
\]

并且有更强的网格一致式

\[
\boxed{
\sup_{\substack{a>0\\\Pi}}
\left|
\frac{\|I_\Pi(q_a-q^*)\|_{w,[A,B]}}
{\Delta(a)\sqrt B\log B}-1\right|\longrightarrow0.
}\tag{1.3}
\]

因此对任意正数列 a_B，没有附加小参数制度，

\[
\boxed{
\|q_{a_B}-q^*\|_{w,[A,B]}\to0
\iff a_B\sqrt B\log B\to0.
}\tag{1.4}
\]

任意真实端点插值具有同一充要条件。原先 `a_B(log B)^2→0` 的充分参数制度在这里被移除；厚度趋零本身成为匹配趋零的必要推论。

### 定理 1.2：完整道路差的统一主形状

\[
\boxed{
\sup_{a>0}\left|
\frac{q_a(y)-q^*(y)}{-\Delta(a)y\log y}-1\right|\longrightarrow0
\quad(y\to\infty).
}\tag{1.5}
\]

从而存在 Y_0，使所有 a>0、y≥Y_0 都有 q_a(y)<q*(y)。这是完整累计道路差的最终符号，源误差在素数幂与多素因子整数上仍然异号。Y_0 在本稿中没有优化或给出数值。

## 2. 精确 Dirichlet 接口与单位扣除

先定义含单位的乘法函数

\[
f_a(n)=\sum_{d\mid n}\mu(d)d^{-a}
=\prod_{p\mid n}(1-p^{-a}),\qquad f_a(1)=1.
\]

于是对所有 n，准确地有

\[
D_a(n)=\frac{f_a(n)-\mathbf1_{n=1}}a.
\]

在 Re s>1 由绝对收敛换序得到

\[
\boxed{
\sum_{n\ge1}\frac{D_a(n)}{n^s}
=\frac1a\left(\frac{\zeta(s)}{\zeta(s+a)}-1\right).
}\tag{2.1}
\]

`−1/a` 不可省略：它准确编码 D_a(1)=0。对完整道路的 Mellin 积分，源部分还乘以 `1/[s(s−1)]`，因此该单位项对道路的常数和线性项都有实际贡献。

定义

\[
C(a)=1+\gamma+(\gamma-1)\frac{g(a)}a+
\frac{g'(a)-1}a.
\tag{2.2}
\]

第 3 节将证明，对某些绝对正常数 c、C_1，有统一估计

\[
\boxed{
\frac{q_a(y)}y=-\Delta(a)\log y+C(a)+
\begin{cases}
O(a^{-1}e^{-c\sqrt{\log y}}),&0<a\le1/2,\\
O(a^{-1}y^{-1/2}),&a\ge1/2.
\end{cases}
}\tag{2.3}
\]

大 O 的隐含常数不依赖 a 或 y≥2。小 a 端的 `1/a` 是本条非微扰表示的余项尺度；后续用原微扰估计接合，不把它误用到任意快趋零的 a。

### 系数的基本性质

因为 `ζ(1+a)>∫_1^∞t^(-1-a)dt=1/a`，故

\[
0<\Delta(a)<1\quad(a>0).
\]

Laurent 展开给

\[
g(a)=a-\gamma a^2+(\gamma^2+\gamma_1)a^3+O(a^4),
\]

从而

\[
\Delta(a)=\gamma a+O(a^2),\qquad
C(a)=(\gamma+2\gamma^2+3\gamma_1)a+O(a^2).
\tag{2.4}
\]

特别地存在常数 c_0,C_0'>0，使全部 a>0 满足

\[
\boxed{
c_0\min(a,1)\le\Delta(a)\le C_0'\min(a,1),
\qquad |C(a)|\le C_0'\Delta(a).
}\tag{2.5}
\]

证明：小 a 由 (2.4)；紧区间用连续性与严格正性；a→∞ 时 g(a)→1、g′(a)→0，故 Δ(a)→1、C(a)→1+γ。对 a≥1/2，g′ 的有界性也可直接由绝对级数 `g′(a)=−Σ μ(n)logn/n^(1+a)` 得到。这里 (2.5) 的第二式确保即使 Δ(a)logB 趋零，常数项仍比主项小一个 logB；仅有 C(a)=O(1) 不够。

## 3. 全正厚度的均值与道路余项

### 3.1 使用的无条件算术输入

使用有效 Mertens 界

\[
M(x):=\sum_{n\le x}\mu(n)=O(xe^{-c_1\sqrt{\log x}}).
\tag{3.1}
\]

这是本稿新增使用的标准无条件输入。实际核对了 Lee–Leong, *New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function*, arXiv:2208.06141v5，Theorem 1.1 的经典型 M(x) 界。其 `x(logx)exp(−η√logx)` 形式缩小 η 后给出 (3.1)，有限初段吸收入隐含常数。本稿不使用文中更强的零点区域或数值阈值作实际计算证书。

原参考道路还沿用前驱已由有效素数定理证明的

\[
q^*(y)/y=O(e^{-c_2\sqrt{\log y}}).
\tag{3.2}
\]

### 3.2 对 0≤a≤1/2 的加权 Möbius 和

令 `M_a(t)=Σ_(n≤t) μ(n)n^(-a)`。部分求和给

\[
M_a(t)=t^{-a}M(t)+a\int_1^t M(u)u^{-a-1}du.
\]

将积分分成 `[1,√t]` 和 `[√t,t]`，前段用 |M(u)|≤u，后段用 (3.1)，并用 `1−a≥1/2`，得某个 c_3>0 下

\[
|M_a(t)|\ll t^{1-a}e^{-c_3\sqrt{\log t}}
\quad(0\le a\le1/2),
\tag{3.3}
\]

常数统一。再次部分求和，使用 `t^(-a)≤N^(-a)` 及
`∫_(logN)^∞exp(−c√u)du≪exp(−c′√logN)`，得

\[
\left|g(a)-\sum_{d\le N}\frac{\mu(d)}{d^{1+a}}\right|
\ll N^{-a}e^{-c_4\sqrt{\log N}}
\quad(0<a\le1/2).
\tag{3.4}
\]

### 3.3 双曲线恒等式保留全部整数

记 H_a(y)=Σ_(n≤y)f_a(n)，N=floor√y。精确有限恒等式为

\[
H_a(y)=\sum_{d\le N}\mu(d)d^{-a}\lfloor y/d\rfloor
+\sum_{r\le N}M_a(y/r)-N M_a(N).
\tag{3.5}
\]

第一项替换 floor 后的误差不超过 N；其主项由 (3.4) 为 `yg(a)+O(ye^(−c√logy))`。其余各项由 (3.3) 以及

\[
\sum_{r\le N}r^{a-1}\le N^a(1+\log N)
\]

控制在相同误差尺度内。缩小正常数吸收有限次对数，得到

\[
\boxed{H_a(y)=yg(a)+O(ye^{-c_5\sqrt{\log y}})
\quad(0<a\le1/2).}\tag{3.6}
\]

若 a≥1/2，直接在
`H_a(y)=Σ_(d≤y) μ(d)d^(-a)floor(y/d)`
中支付 floor 与绝对尾，得

\[
|H_a(y)-yg(a)|
\le\sum_{d\le y}d^{-a}+y\sum_{d>y}d^{-1-a}
\ll\sqrt y
\quad(a\ge1/2).
\tag{3.7}
\]

于是完整累计源满足

\[
S_a(y):=\sum_{n\le y}D_a(n)
=yd(a)-\frac1a+
\begin{cases}
O(ye^{-c_5\sqrt{\log y}}/a),&0<a\le1/2,\\
O(\sqrt y/a),&a\ge1/2.
\end{cases}
\tag{3.8}
\]

单位扣除在这里仍精确保留。

### 3.4 完整道路常数的识别

完整有限部分求和给

\[
\frac1y\sum_{n\le y}(y/n-1)D_a(n)
=\int_1^y\frac{S_a(t)}{t^2}dt.
\]

由 (3.8)，固定 a>0 时 `∫_1^∞[S_a(t)−d(a)t]t^(-2)dt` 绝对收敛。其尾分别为
`O(a^(-1)e^(−c√logy))` 与 `O(a^(-1)y^(-1/2))`，其中精确单位项产生的 `1/(ay)` 包含在这些界内。

另一方面，(2.1) 在 s=1+z 处展开为

\[
\frac{d(a)}z+\frac{\gamma g(a)+g'(a)-1}a+O_a(z).
\]

利用 `ΣD_an^(-s)=s∫_1^∞S_a(t)t^(-s-1)dt` 比较常数，得上述道路积分常数为

\[
\frac{(\gamma-1)g(a)+g'(a)-1}a.
\]

加上原背景 `1+γ−logy`，即为 (2.3)。这一步识别常数而不改变任何真实端点。

## 4. 统一拼接与完整匹配的充要尺度

置 L=logB。将参数分成两个区间。

### 4.1 微小厚度 0<a≤L^(-3)

前驱的首阶支撑平均余项给，在全部 y≤B 上，

\[
q_a(y)-q^*(y)
=aT_b(y)+O(a^2L^3y),
\]

且前驱首阶主项给 `T_b(y)/y=−γlogy+O(1)`，包括 y=1 时吸收入常数。因此

\[
q_a(y)-q^*(y)=-\gamma a\,y\log y+O((a+a^2L^3)y).
\tag{4.1}
\]

误差是共同线性半径，经过任意真实端点插值仍成立。除以 `aL` 后的相对半径为
`O(L^(-1)+aL²)=O(L^(-1))`。又 Δ(a)/(γa)=1+O(a)，故可以统一替换主系数为 Δ(a)。

### 4.2 其余厚度 a>L^(-3)

取整数 Y=floor√B。对全部节点 y≥Y，(2.3)、(3.2) 以及 (2.5) 给

\[
q_a(y)-q^*(y)
=-\Delta(a)y\log y+C(a)y+r_a(y),
\]

\[
|r_a(y)|/y
\ll
\begin{cases}
a^{-1}e^{-c_6\sqrt L},&a\le1/2,\\
a^{-1}B^{-1/4}+e^{-c_6\sqrt L},&a\ge1/2.
\end{cases}
\tag{4.2}
\]

除以 Δ(a)L，右端统一趋零。例如中间参数段可用 `a^(-2)≤L^6`，故得到 `O(L^5e^(−c_6√L))`。

较小节点不能直接使用 (4.2)。初等地 `D_a(n)≤1/a`、`Σ_(n≤y)Λ(n)/n≤logy+4log2`，因此全部 y≤B 上

\[
|r_a(y)|\ll (1+a^{-1})Ly.
\tag{4.3}
\]

下面的插值引理保证这些小节点不会通过一个很长的单元造成未支付的误差。

### 引理 4.1：小节点误差的统一插值支付

设网格节点上的误差 z(y) 仅在 y≤Y 可能非零，且 |z(y)|≤My，Y为正整数。则

\[
\boxed{\|I_\Pi z\|_{w,[A,B]}^2\le2M^2Y.}\tag{4.4}
\]

证明：对 n≤Y，非负重心权再现 n，故 |I_Πz(n)|≤Mn，这部分至多 M²Y。对 n>Y，至多只有最后一个小节点与第一个大节点之间的单元非零；其值绝对值≤MY。用 `Σ_(n>Y)n^(-2)≤1/Y`，另一部分至多 M²Y。闭端点已按 n≤Y、n>Y 分开计数。证毕。

将 r_a 按节点是否≤Y 分成两部分。大节点部分由 (4.2) 的共同线性半径支付；小节点部分由 (4.3)—(4.4) 支付为

\[
O((1+a^{-1})LB^{1/4}).
\]

相对于 Δ(a)√B L，它至多为 `O(B^(-1/4)L^6)`，统一趋零。C(a)y 的根支付则由 (2.5) 至多 `O(Δ(a)√B)`，小于主项一个 L。

### 4.3 主形状与任意网格

由 ylogy 的凸性及所有节点≤B，

\[
\log n\le\frac{I_\Pi(y\log y)(n)}n\le\log B.
\]

A/B→0 给

\[
\sum_{n=A}^B(\log n)^2\sim B(\log B)^2,
\qquad (B-A+1)(\log B)^2\sim B(\log B)^2.
\]

因此该主形状的根范数对全部 Π 一致渐近于 √B logB。结合两个厚度区间的统一小余项，证明 (1.2)—(1.3)。在 y=B 处使用相同分区，但不需要小节点引理，得到 (1.5)。

最后由 (2.5)，若 Δ(a_B)√B logB→0，则 Δ(a_B)→0，从而 a_B→0；此时 Δ(a_B)∼γa_B。反向直接成立。因此 (1.4) 是全部正单厚度族上的充要结论。

## 5. 过渡区与范围

- 若 `a_B√B logB→u∈[0,∞)`，则完整根误差趋于 γu，所有真实端点插值一致；u=0 是精确匹配趋零区。
- 若 a_B→0 而 `a_B√B logB→∞`，则根误差渐近 γa_B√B logB 并发散。此结论现在覆盖慢于任何预定对数幂的厚度收缩。
- 若 a_B→a_0>0，则根误差渐近 Δ(a_0)√B logB。
- 若 a_B→∞，则 Δ(a_B)→1，根误差渐近 √B logB。
- 对每个固定 a>0，(2.3) 说明 q_a(y)/y∼−Δ(a)logy，因而其正部最终为零。这是固定厚度道路的背景质量偏差；它不满足趋零匹配条件，不能作为参考道路的无界正能量上界。

这里得到的必要性只属于实际单厚度正参数族；多厚度的有符号匹配仍有不同的消矩结构，不能据此宣称全部厚度设计的最优复杂度。

## 6. 证据与来源

伴随 `verify_uniform_thickness_identities.py` 采用精确分数，检查正整数厚度的乘积/除数源恒等式、单位扣除、双曲线有限和、完整道路核换序及小节点插值支付。它不以有限数据证明无界参数渐近。

另有 `explore_uniform_thickness.py`，用明确标记的双精度源与高精度主项系数观察多个厚度制度和多种节点网格；输出是探索记录，未提升为严格区间证书。

标准输入于2026-11-24实际读取：

- Ethan Simpson Lee and Nicol Leong, *New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function*, arXiv:2208.06141v5, Theorem 1.1（经典型有效 Mertens 界）：<https://arxiv.org/html/2208.06141v5>；实际另打开了PDF <https://arxiv.org/pdf/2208.06141>。这里只使用已说明的渐近衰减，不使用未复核的数值常数。
- NIST DLMF §25.2（ζ 的 Laurent 展开和 Stieltjes 常数约定），与前驱已读来源相同：<https://dlmf.nist.gov/25.2>。
- 原 q*/y 的有效余项与首阶 T_b 主项复用明确前驱证明；它们的有效素数定理输入来自 Kedlaya 解析数论讲义第7章。

本稿使用这些无条件已知输入，未假设RH。得到的是完整匹配的统一参数分类，参考道路与真实中粗层的无界次幂控制保持其原有开放状态。
