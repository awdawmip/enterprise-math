# 跨骨架帽矩的 Green 接续与真实锚点控制

日期：2026-11-24（Asia/Hong_Kong）。本稿属于本轮作者推导与作者核验；独立 Review 和正式 Result 由父研究线另行记录。

科学前驱：`enterprise-math@42e7aa4dbd01a6eb66e2f881c7cddcba72a3d775:research_notes/portable_direct/rh_directed_local_20261124_e7808f/directed_arithmetic/LOCAL_PRIME_DEFICIT_TRANSFER.md`；完整累计场前驱为该包保留的 `prior/riemann_cumulative_haar_20261123/joint_prefix/CUMULATIVE_FLUX_HAAR_ENERGY.md`。

整数下标继续表示固定原生 X6 轴 `c_*+nE_1` 上的辅助标量观察；P000 和 Heartbeat X6 基础保持原义。本稿的 Green 核用于有限标量插值，不把辅助二维图像或标量相消提升为原生空间定义。完整整数背景、合数、厚度、单位、真实端点和前史均保留。

## 1. 本轮增量

此前局部三点算子能够消去仿射前史，因此对每个 dyadic 块内部的三角亏缺作估计，仍留下骨架锚点。这一缺口可以用**跨过相邻块接缝的同类非负帽观察**接回：有限 Green 恒等式保留两个真实端点；对于完整参考道路，另外证明的无穷远归一化固定其线性模态。

采用交错整数节点

\[
a_{2j}=2^{j+1},\qquad a_{2j+1}=3\,2^j\quad(j\ge0),
\tag{1}
\]

即 `2,3,4,6,8,12,…`。每个相邻三点包

\[
p_k=(a_{k-1},a_k,a_{k+1}),\quad k\ge1,
\tag{2}
\]

都满足 `R=2L`，所以仍在上一轮局部定理的 `Y≤2X` 范围内。它们由两族组成：

\[
(X,3X/2,2X),\qquad (3X/2,2X,3X)
\tag{3}
\]

（`X` 为不小于 2 的 2 的幂）。后一族跨过旧 dyadic 骨架接缝。两族每个尺度各一包，未扩大成任意符号测试函数。

下文证明：若普通素数在这两族上的归一化正亏缺具有次幂上界，则真实参考骨架正锚点也具有平方根乘次幂上界。上一轮完整匹配误差随后把该结论传给实际厚度族。

## 2. 有限 Green 恒等式：两个真实端点完整保留

取任意严格递增的实节点

\[
a_0<a_1<\cdots<a_N,
\]

和任意真实节点值 `q_k=q(a_k)`。令 `F` 为这些值的分段仿射插值，并定义

\[
t_k=\frac{q_k-q_{k-1}}{a_k-a_{k-1}}
      -\frac{q_{k+1}-q_k}{a_{k+1}-a_k},\quad 1\le k<N.
\tag{4}
\]

定义两端真实割线与正核

\[
J_N(x)=\frac{a_N-x}{a_N-a_0}q_0+
       \frac{x-a_0}{a_N-a_0}q_N,
\]

\[
G_N(x,z)=\frac{(\min(x,z)-a_0)(a_N-\max(x,z))}{a_N-a_0}.
\tag{5}
\]

### 定理 1：带真实边界的精确重建

在整个 `[a0,aN]` 上，

\[
\boxed{F(x)=J_N(x)+\sum_{k=1}^{N-1}G_N(x,a_k)t_k.}
\tag{6}
\]

**证明。** 对固定 `z=a_k`，`G_N(·,z)` 在两个端点为零，在 `z` 左右的斜率差恰为 1，在其他节点的斜率差为零。因此 (6) 右端与 F 有相同的全部斜率跳跃；两者之差是全区间仿射函数，并在两个端点为零，故恒为零。所有系数都是精确有理数，当原节点为整数时无需数值微分。证毕。

因为 `G_N≥0`，直接得到

\[
F(x)\le J_N(x)+\sum_{k=1}^{N-1}G_N(x,a_k)(t_k)_+.
\tag{7}
\]

保留 `J_N` 的符号后再正化给出更精细的有限正部上界。式 (6) 中的全部 signed t 可以精确重建；(7) 是有向充分上界。任何有限窗口只拥有窗口内帽矩时，右端真实边界 `q_N` 仍须支付。

## 3. 无穷端点极限与单侧帽矩

令 `a_k→∞`，固定 j。若

\[
\frac{q(a_N)}{a_N}\longrightarrow \ell\quad(N\to\infty),
\tag{8}
\]

则

\[
J_N(a_j)\longrightarrow q(a_0)+(a_j-a_0)\ell,
\]

而对固定 k，

\[
G_N(a_j,a_k)\uparrow \min(a_j,a_k)-a_0.
\tag{9}
\]

若对这个固定 j 有

\[
\sum_{k\ge1}(\min(a_j,a_k)-a_0)(t_k)_+<\infty,
\tag{10}
\]

则

\[
\boxed{
q(a_j)\le q(a_0)+(a_j-a_0)\ell
 +\sum_{k\ge1}(\min(a_j,a_k)-a_0)(t_k)_+ .}
\tag{11}
\]

**证明。** 在 (7) 中令 `N→∞`。非负核的极限使用单调收敛；(8) 给出真实端点的极限。正负部不能互相替换，因而 (10) 只要求本来就进入上界的正部尾可和。若需要 signed 等式，则由 (6)、(8)、正部单调收敛和有限的左端，负部核和也收敛，从而

\[
q(a_j)=q(a_0)+(a_j-a_0)\ell+
\sum_{k\ge1}(\min(a_j,a_k)-a_0)t_k.
\tag{12}
\]

这里 signed 系列在上述条件下绝对收敛。证毕。

`ℓ` 是实际道路的渐近线性项；它不是可以任意选取或默认为零的规范。下一节对本研究的固定参考道路证明 `ℓ=0`。

## 4. 完整参考道路的无穷远归一化

保留原定义

\[
q^*(y)=y(1+\gamma-\log y)
 +\sum_{n\le y}(y/n-1)\Lambda(n),\quad y\ge1.
\tag{13}
\]

令 `ψ(t)=Σ_{n≤t}Λ(n)`，在整数点采用完整闭前缀；取积分时单点值不影响结果。使用已知无条件素数定理误差

\[
\psi(t)-t=O(t\exp(-c\sqrt{\log t}))\quad(c>0),
\tag{14}
\]

以及 `ζ(s)=1/(s−1)+γ+O(s−1)`。外部来源见第 8 节。这里只用这些标准事实确定参考道路的归一化；目标的平方根级帽亏缺没有由 (14) 获得。

### 引理 1

\[
\boxed{\frac{q^*(y)}y=-\int_y^\infty
                      \frac{\psi(t)-t}{t^2}\,dt\longrightarrow0.}
\tag{15}
\]

**证明。** 有限部分求和给

\[
\sum_{n\le y}\frac{\Lambda(n)}n
 =\frac{\psi(y)}y+\int_1^y\frac{\psi(t)}{t^2}\,dt.
\tag{16}
\]

由 (14)，`∫_1^∞(ψ(t)−t)t^(−2)dt` 绝对收敛。因此

\[
\sum_{n\le y}\frac{\Lambda(n)}n-\log y\longrightarrow L
 =1+\int_1^\infty\frac{\psi(t)-t}{t^2}\,dt.
\]

将 `S(y)=Σ_{n≤y}Λ(n)/n=log y+L+o(1)` 代入 `s>0` 的部分求和式

\[
-\frac{\zeta'(1+s)}{\zeta(1+s)}
 =s\int_1^\infty S(t)t^{-s-1}\,dt
 =\frac1s+L+o(1).
\]

余项 `s∫o(1)t^(−s−1)dt=o(1)` 由先固定尾起点、再令 `s↓0` 得到。与 Laurent 展开产生的 `1/s−γ+O(s)` 比较，得到 `L=−γ`，于是

\[
\int_1^\infty(\psi(t)-t)t^{-2}dt=-1-\gamma.
\]

再把 (16) 代入 (13)，即得 (15)。源自整数 prime-power 事件的每一项和完整 `−y log y` 背景都保留；该恒等式仅给同一道路的另一种表示。证毕。

这里不是把实际固定有限厚度 D 延长到无穷后假定同样归一化；本节只针对与窗口无关的参考道路 q*。

## 5. 两族普通素数亏缺同时控制骨架锚点

现在取 (1) 的交错节点。记

\[
L_k=a_{k-1},\ x_k=a_k,\ R_k=a_{k+1}=2L_k.
\]

每包的帽核 `φ_k` 和普通素数亏缺保持上一轮定义：

\[
\tau_k=\sum_{L_k<n<R_k}\frac{\phi_k(n)}n
 -\sum_{L_k<p<R_k\atop p\ \mathrm{prime}}
               \frac{\phi_k(p)}p\log p.
\tag{17}
\]

第一项仍包含所有整数。上一轮局部公式给

\[
t_k^*=\tau_k+K_k-Q_k,\qquad
0\le K_k\le\frac1{4L_k^2},\quad Q_k\ge0.
\tag{18}
\]

因此

\[
(t_k^*)_+\le(\tau_k)_++\frac1{4L_k^2}.
\tag{19}
\]

由于 `h_k=L_k`，本包的归一化根预算恰为

\[
\mathcal N_{L_k}(\tau_k)=\sqrt{L_k}(\tau_k)_+.
\tag{20}
\]

### 定理 2：显式的锚点支付

固定 `0<ε<1/2`。若存在有限 `Cε`，使所有 `k≥1` 满足

\[
\sqrt{L_k}(\tau_k)_+\le C_\varepsilon L_k^\varepsilon,
\tag{21}
\]

则全部交错锚点满足

\[
\boxed{
(q^*(a_j))_+\le(q^*(2))_++\frac34
 +D_\varepsilon C_\varepsilon a_j^{1/2+\varepsilon},}
\tag{22}
\]

其中

\[
D_\varepsilon=(3/2)^{1/2-\varepsilon}
 \left\{\frac1{1-(4/3)^{-1/2-\varepsilon}}
       +\frac1{(4/3)^{1/2-\varepsilon}-1}\right\}.
\tag{23}
\]

`q*(2)=2(1+γ−log2)`。特别地，若 (21) 对每个 `ε>0` 成立（只需取小于 `1/2` 的 ε），则

\[
\boxed{(q^*(a_j))_+\le a_j^{1/2+o(1)}.}
\tag{24}
\]

这里的 `a_j^{1/2+o(1)}` 表示对每个正 ε 有相应常数上界，包含有界或衰减的情形。

**证明。** 所有相邻节点比值都位于

\[
r=4/3\le a_k/a_{k-1}\le v=3/2.
\]

置 `p=1/2−ε>0`。由 (21)，

\[
(\tau_k)_+\le C_\varepsilon L_k^{-p}
             \le C_\varepsilon v^p a_k^{-p}.
\]

于是将 (11) 中的和分成 `k≤j` 与 `k>j`，有

\[
\begin{aligned}
\sum_{k\ge1}\min(a_j,a_k)(\tau_k)_+
&\le C_\varepsilon v^p
 \left(\sum_{k\le j}a_k^{1-p}
       +a_j\sum_{k>j}a_k^{-p}\right)\\
&\le C_\varepsilon v^p a_j^{1-p}
 \left(\frac1{1-r^{-(1-p)}}+\frac1{r^p-1}\right).
\end{aligned}
\tag{25}
\]

两个几何级数绝对收敛，所以 (10) 成立。背景修正可统一支付

\[
\sum_{k\ge1}\min(a_j,a_k)K_k
\le\frac v4\sum_{k\ge1}\frac1{L_k}
\le\frac{v}{4a_0(1-r^{-1})}=\frac34.
\tag{26}
\]

使用 (15) 的 `ℓ=0`、(19)、(25)—(26)，得到 (22)。高次素数幂 Q 带负号，给上界时无须为它支付。证毕。

### 有限截断后的显式尾成本

若 (21) 的上界用于 `k>M`，且 `j≤M`，则普通素数部分的未读取尾满足

\[
\boxed{
\sum_{k>M}(\min(a_j,a_k)-2)(\tau_k)_+
\le\frac{C_\varepsilon v^p a_j\,a_{M+1}^{-p}}
          {1-r^{-p}}.}
\tag{27}
\]

背景尾另可直接用 `Σ_{k>M}a_j/(4L_k²)` 支付。式 (27) 是在已证或明确假定尾亏缺界下的成本；有限采样本身不提供这个无界假设。

## 6. 回到有限窗口实际厚度族和真实骨架

对每个匹配窗口 `[A,B]`，设其完整实际道路 `q_B` 有已经证明的统一点值半径

\[
|q_B(y)-q^*(y)|\le\varepsilon_B y,
\qquad 1\le y\le B.
\tag{28}
\]

若 `ε_B sqrt(B)→0`，它就足以使下面的全部锚点匹配支付一致趋零；此接口不限制厚度个数或匹配阶。在窗口内的任何上述锚点都有

\[
\boxed{
\frac{q_B(a_j)_+}{\sqrt{a_j}}
\le\frac{q^*(a_j)_+}{\sqrt{a_j}}
  +\varepsilon_B\sqrt B.}
\tag{29}
\]

上一轮 `k≥c log B` 的完整前缀定理给实例 `ε_B=η_B/[c(c+1)]`，其中 `η_B=a_m(log B)^k`；`m=ceil(0.7 log B)` 的有理厚度族满足所需极限。本轮其他已经证明 (28) 的匹配族也可直接接入，包括缩小厚度而保持阶数固定的族。其具体半径由相应匹配分支证明。此处使用的都是窗口内完整实际道路的误差。

设真实块 `[X,2X]` 的端点正值满足

\[
q(X)_+/\sqrt X\le M,
\qquad q(2X)_+/\sqrt{2X}\le M.
\]

则两端真实割线 J 满足

\[
\frac{J(n)}n=
\frac{2X-n}{n}\frac{q(X)}X+
\frac{2(n-X)}n\frac{q(2X)}{2X}.
\tag{30}
\]

两个系数非负且和为 1，所以

\[
\boxed{\|J_+\|_{w,[X,2X]}
\le M\sqrt{(X+1)/X}.}
\tag{31}
\]

从而 (21) 的次幂版本与满足 `ε_B sqrt(B)→0` 的匹配支付，足以给 `[A,A^λ]` 内节点位于 (1) 的全部真实 dyadic 骨架次幂能量预算。块内部能量继续按原细余项和中粗层预算处理。

### 任意裁切端点的一包补接

若整数端点 n 不在 (1) 上，取包围它的相邻链节点 `u<n<v`。记 `h=v−u`，则 `u/3≤h≤u/2`。令 `p=(u,n,v)`，并令

\[
M=\max\{q^*(u)_+/\sqrt u,\ q^*(v)_+/\sqrt v\}.
\]

三点插值恒等式给 `q*(n)=J_uv(n)+[(n−u)(v−n)/h]t_p*`。平方根的凹性给 `J_uv(n)≤M sqrt(n)`；又因 `(n−u)(v−n)≤h²/4`，

\[
\boxed{\frac{q^*(n)_+}{\sqrt n}
\le M+\frac{\sqrt3}{4}\mathcal N_u(t_p^*)
\le M+\frac{\sqrt3}{4}
 \left(\mathcal N_u(\tau_p)+\frac1{16u^{3/2}}\right).}
\tag{31a}
\]

这里的 `𝓝_u` 是原定义用于这个单包的预算。第一个成本系数由
`[(n−u)(v−n)/h]/sqrt(n) · u/h^(3/2) ≤ u/(4sqrt(hn)) ≤ sqrt(3)/4`
得到；第二步使用同一 `t*=τ+K−Q` 和 `Q≥0`。因此任意裁切端点可通过一个准确的非负帽观察接入；窗口只有两个裁切端点时至多增加两包，并按 (29) 传回实际匹配族。该参考帽可跨出裁切窗口：上端 B 的右支撑满足 `v≤3B/2`，下端 A 的左支撑可低于 A。这是明确增加的普通素数测试；匹配转移只在原窗口内的端点 n 使用，无需评价窗口外的实际 `q_B(v)`。

## 7. 命题范围与接续意义

新增的是一个有向接合定理：**原中粗层帽亏缺问题，加上两族跨尺度粗帽的同阶亏缺问题，可以在同一普通素数正锥框架下同时承担内部预算和真实锚点控制。** 后一族含旧 dyadic 接缝，因而有意保留了先前局部块观察消去的信息。

使用本定理时，把 (3) 的准确几何加入原测试类，或证明既有测试类能控制它们。有限窗口式 (6) 支付两个真实端点；无穷版本借助 (15) 固定 q* 的线性项。

条件 (21) 在真实无界素数输入上仍待证明。本稿给出完整 Green 接合、同类帽对锚点的充分控制、背景成本、参考道路归一化与匹配转移。

## 8. 外部标准输入与复算

这里只引入两个外部标准事实，并从它们自行推导 (15)：

- K. S. Kedlaya, *Notes on analytic number theory*, Chapter 7, Theorem 7.7: `|ψ(x)−x|=O(x exp(−c sqrt(log x)))`. 原文使用 prime-power 点的半权约定；与完整闭前缀的差在整数点至多 `log x/2`，不改变本稿使用的误差界，且积分不受单点值影响。来源：<https://kskedlaya.org/ant/part-2-4.html>，2026-11-24 实际读取。
- NIST DLMF §25.2, equation 25.2.4 与 25.2.5：ζ 在 1 的 Laurent 展开与 `γ0=γ`。来源：<https://dlmf.nist.gov/25.2#E4>，2026-11-24 实际读取。Euler product 的对数导数在 `Re s>1` 绝对收敛，给本稿使用的 Mangoldt Dirichlet 级数。

`verify_anchor_green.py` 用 Python `Fraction` 对有理节点和值检查有限 Green 恒等式、逐点一侧支配和真实仿射边界。它不依靠浮点测试证明无穷结论；无穷结论由上面的解析论证承担。父分支另用原已保存实际节点做有限 Green 重建，避免重复道路点值查询。
