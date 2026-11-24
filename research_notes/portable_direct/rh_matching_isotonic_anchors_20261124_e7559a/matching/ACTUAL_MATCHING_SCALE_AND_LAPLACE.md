# 实际厚度误差的正卷积结构与缩尺度匹配族

日期：2026-11-24（Asia/Hong_Kong）。本轮作者统筹 `EM-DIRECT-E7559A / TASK_RESEARCH`，Activity `RA-D2F111EA1C0D4B1DBEFBC1B4`；原作者 E7808F、B5750A 的贡献保留。作者工作内推导与核验；不是独立 Review。继承的科学对象是 `enterprise-math@42e7aa4dbd01a6eb66e2f881c7cddcba72a3d775` 中 `research_notes/portable_direct/rh_directed_local_20261124_e7808f` 的完整道路。这里研究同一个辅助标量读出，不变更 P000、Heartbeat X6 状态或 BRC 正质量。全部整数、单位约定、合数关系、完整前史、背景和真实端点保留。

## 1. 本轮的两个实质增量

1. 当前任务对厚度没有正的统一下限。若允许整个厚度尺度随终点 B 缩小，则 **一个厚度已经足以使完整窗口匹配误差趋零**：取 `a_B=1/B`，权重为 1。写 `L=log B`、`C=4log2`，利用实际源的乘法支撑平均得到

\[
\boxed{\|q_B-q^*\|_{w,[A,B]}
\le\frac{\sqrt{B-A+1}}{2B}
\left[L(L+C)+(L+C)^2e^{(L+C)/B}\right]
=O\!\left(\frac{(\log B)^2}{\sqrt B}\right)\longrightarrow0.}
\tag{1.1}
\]

同一界适用于任意包含真实两端点的节点插值。第 2.2 节先给出只用逐点源界的 `(log B)^3/(2sqrt B)` 简单证明，第 2.4 节利用完整乘法支撑省去一个对数。所需输入分母 B、归一化因子 B 和求值精度成本在第 3 节列明。

2. 若保留上轮宽度固定为 `θ=1/2` 的有理 Chebyshev 型节点族，利用实际误差的正卷积结构，可把已证充分阶数从 `ceil(0.7 log B)` 降到 `ceil(0.56 log B)`。新的完整窗口上界是

\[
\boxed{\|q-q^*\|_w
\le \frac{32000}{961e}
B^{9/10-(14/25)\log5}\longrightarrow0,}
\tag{1.2}
\]

其中系数也可写为 `(2048/961)·125/(8e)`，指数约为 `−0.00128523096`。取 `m=ceil(0.6 log B)` 时指数为 `−0.06566274746`，有更大的衰减余量。常数没有优化。

第一项改变整个厚度尺度；第二项维持原来的固定宽度节点设计。两项都不以逐整数误差包络的最坏核下界代替实际族的可行性。

## 2. 一个厚度的完整无界族

对整数 `B≥2`，定义

\[
a_B=1/B,\qquad D_{B,1}=0,
\qquad D_{B,n}=\frac1{a_B}\prod_{p\mid n}(1-p^{-a_B})\quad(n\ge2).
\tag{2.1}
\]

每个 B 对应一条完整道路；`D_{B,n}` 在全部整数上有定义。`q_B` 仍采用同一 `γ`、同一背景以及从 1 开始的完整前缀。参考道路只将 D 换为 Λ。

### 2.1 逐整数误差与符号

上轮的直接厚度插值定理在 `m=1` 时直接给出

\[
\boxed{|D_{B,n}-\Lambda(n)|\le\frac{(\log n)^2}{2B}
\quad(2\le n\le B).}
\tag{2.2}
\]

这一特殊族还可独立作初等验证。设 `r=ω(n)`、`L=log rad(n)≤log B`。

- `r=1` 时 `n=p^j`，由 `0<u−1+e^{−u}≤u²/2`（u>0）得
  `0<Λ(n)−D_{B,n}≤a_B(log p)²/2`。
- `r≥2` 时 `Λ(n)=0`、`D_{B,n}>0`。由 `1−e^{−u}≤u` 与算术几何平均，
  \[
  D_{B,n}\le a_B^{r-1}\prod_{p\mid n}\log p
  \le a_B^{r-1}(L/r)^r
  =a_BL^2\frac{(a_BL)^{r-2}}{r^r}
  \le a_BL^2/4,
  \]
  因为 `a_BL≤log B/B<1`。

因此此族的真实误差在素数幂处严格为负，在具有至少两个不同素因子的整数处严格为正。单位误差为零。这里没有把完整整数源改成单侧误差。

### 2.2 完整道路、真实端点与任意插值

完整前缀差恰为

\[
q_B(y)-q^*(y)=\sum_{n=2}^y(y/n-1)(D_{B,n}-\Lambda(n)).
\tag{2.3}
\]

对整数 `2≤y≤B`，用 `Σ_{n=2}^y1/n≤∫_1^y dt/t=log y` 得

\[
|q_B(y)-q^*(y)|
\le\frac{(\log y)^2}{2B}\,y\sum_{n=2}^y\frac1n
\le\frac{y(\log y)^3}{2B}.
\tag{2.4}
\]

`y=1` 的两条道路相等。对全部节点有 `|q_B(y)−q*(y)|≤C_B y`，其中 `C_B=(log B)^3/(2B)`。分段仿射插值的非负重心权准确再现 y，所以任意网格 Π（含真实端点）满足

\[
|I_\Pi(q_B-q^*)(n)|\le C_B n.
\]

逐点除以 n、平方求和即得简单界

\[
\boxed{\|q_B-q^*\|_w,\ \|I_\Pi(q_B-q^*)\|_w
\le\frac{(\log B)^3}{2B}\sqrt{B-A+1}
\le\frac{(\log B)^3}{2\sqrt B}.}
\tag{2.4a}
\]

正部映射在每一点为 1-Lipschitz，故两条道路正部根能量之差亦受同一上界控制。

源误差还有

\[
\varepsilon_B\sqrt B
\le\frac{(\log B)^2}{2\sqrt B}\longrightarrow0.
\tag{2.5}
\]

因此该族满足前驱普通素数局部亏缺归约所需的匹配成本趋零条件。普通素数亏缺和 q* 的真实骨架仍是相应的算术问题。

### 2.3 固定数量与缩尺度的普遍交换

固定整数 `m≥1`，取整数 `Q_B≥1`，令

\[
a_{j,B}=j/Q_B,\qquad
v_j=(-1)^{j-1}\binom mj\quad(1\le j\le m).
\tag{2.6}
\]

这些就是 0 处的 Lagrange 权，精确满足 `Σv_j=1`、`Σv_ja_{j,B}^r=0`（1≤r<m），总变差为 `2^m−1`。直接插值系数为

\[
\frac{\prod_ja_{j,B}}{(m+1)!}=\frac1{(m+1)Q_B^m}.
\]

同一完整前缀估计给

\[
\boxed{\|q_B-q^*\|_{w,[A,B]}
\le\frac{(\log B)^{m+2}}{(m+1)Q_B^m}\sqrt{B-A+1}.}
\tag{2.7}
\]

若 `Q_B=ceil(B^r)`、固定 `r>0` 且 `mr>1/2`，右侧趋零。若要求所有厚度≤θ，只需取 B 大到 `m/Q_B≤θ`。`m=1,Q_B=B` 在全部 `B≥2` 已满足 θ=1/2。

上轮核分类中的 `k=Ω(log B)` 是“除去逐整数包络系数后，归一化前缀核有统一常数”的充要尺度。式 (2.7) 允许包络系数本身随 B 更快变小，故固定 k 完全相容。这里得到的是实际厚度族的充分构造，没有声称最优精度成本。

### 2.4 完整乘法支撑平均再省去一个对数

本小节对任意 a>0 的单厚度源成立。设

\[
S(y)=\sum_{n\le y}\frac{\Lambda(n)}n,
\qquad e_n=D_a(n)-\Lambda(n).
\]

素数幂部分由第 2.1 节有

\[
\sum_{\substack{n\le y\\\omega(n)=1}}\frac{|e_n|}n
\le\frac a2\sum_{n\le y}\frac{\Lambda(n)\log n}n
\le\frac a2(\log y)S(y).
\tag{2.8}
\]

对 r≥2，令 `Λ^{*r}` 为 Λ 的 r 重 Dirichlet 卷积。如果 `ω(n)=r`，每个非零卷积项的 r 个因子都必须是素数幂，且恰好各承担一个不同素因子，因此

\[
\Lambda^{*r}(n)=r!\prod_{p\mid n}\log p,
\qquad
0<D_a(n)\le\frac{a^{r-1}}{r!}\Lambda^{*r}(n).
\]

全部这些量非负。把满足 `ω(n)=r` 的求和扩到所有 n，再把有序乘积的 `n_1\cdots n_r≤y` 条件扩到各 `n_i≤y`，便有

\[
\sum_{\substack{n\le y\\\omega(n)\ge2}}\frac{D_a(n)}n
\le\sum_{r\ge2}\frac{a^{r-1}}{r!}S(y)^r
=\frac{e^{aS(y)}-1-aS(y)}a.
\tag{2.9}
\]

原源的合数支撑通过其 r 个不同素因子的联合乘积进入这个界；没有将合数误差默认为零。结合 (2.8)—(2.9) 及 `e^u−1−u≤u²e^u/2` 得

\[
\boxed{\sum_{n\le y}\frac{|e_n|}n
\le\frac a2\left[(\log y)S(y)+S(y)^2e^{aS(y)}\right].}
\tag{2.10}
\]

完整前缀权满足 `0≤y/n−1≤y/n`，所以 (2.10) 的右端乘以 y 即控制道路差的绝对值。

前驱已证初等 Chebyshev 界 `ψ(y)≤Cy`，`C=4log2`（见其 `ARITHMETIC_FINE_REMAINDER_BOUNDS.md` §3）。使用完整整除恒等式

\[
\log(y!)=\sum_{d\le y}\Lambda(d)\lfloor y/d\rfloor
\ge yS(y)-\psi(y)
\]

得到 `S(y)≤log y+C`。对 `a=1/B`、`y≤B`，(2.10) 给出共同的线性道路上界

\[
|q_B(y)-q^*(y)|\le
\frac y{2B}\left[L(L+C)+(L+C)^2e^{(L+C)/B}\right].
\tag{2.11}
\]

它经任意真实端点插值保持，除以 n 后平方求和得到 (1.1)。对 B→∞，显示括号为 `2L²(1+o(1))`。当 B≥16 时，`C≤L` 且 `exp((L+C)/B)≤sqrt2<3/2`，还可采用更简洁的

\[
\boxed{\|q_B-q^*\|_w,\ \|I_\Pi(q_B-q^*)\|_w
\le \frac{4(\log B)^2}{B}\sqrt{B-A+1}
\le\frac{4(\log B)^2}{\sqrt B}.}
\tag{2.12}
\]

这是上界中的实际算术平均改进。素数定理、RH、短区间下界及随机性均未被用作假设。

## 3. 缩尺度成本：输入位数、稳定求值与完整人口

`a_B=1/B` 是精确有理数，分子分母直接表示需要 `O(log B)` 位，匹配权为 1。原定义有 `1/a_B=B` 的归一化因子。若直接计算 `1−exp(−u)` 后再除以 a，需要支付小差的精度。

一个等价的稳定表示是

\[
E(u)=\int_0^1e^{-ut}\,dt=
\begin{cases}(1-e^{-u})/u,&u>0,\\1,&u=0,\end{cases}
\]

\[
\boxed{D_a(n)=a^{r-1}\left(\prod_{p\mid n}\log p\right)
\left(\prod_{p\mid n}E(a\log p)\right).}
\tag{3.1}
\]

这是完整正乘积恒等式；r 与全部不同素因子仍保留。对本族 `0≤a log p≤log B/B<1`，E 的交错幂级数或正积分可以作有向区间计算，避免将两个接近 1 的浮点数相减作为唯一求值方法。

例如若仍用直接乘积，在各 `1−p^{-a}` 因子上给出误差 δ、将有效区间截到 [0,1]，r 个因子乘积的误差至多 rδ。归一化后误差至多 `Brδ`。取 `δ≤1/(B²r)` 可使单个 D 的误差≤1/B；所需分数位数为 `2log₂B+O(log log B)`。再按完整前缀支付，这部分数值根误差≤`(log B)/sqrt B`。这是一个充分精度预算，不是计算复杂度最优结论。

素因子取得、所有 n 的源生成、背景和前缀计算仍有各自成本。一个厚度的结论是匹配样本数量与尺度/精度之间的交换，不是端到端运行时间或素数筛的次线性声明。

## 4. 实际匹配误差的正卷积表示

本节适用于任意 m 个互异正厚度 a_j，使用其**真实 0 处** Lagrange 权

\[
v_j=\prod_{i\ne j}\frac{a_i}{a_i-a_j}.
\]

定义

\[
F(t)=\sum_jv_j\frac{1-e^{-a_jt}}{a_j},\qquad I(t)=t-F(t),\quad t\ge0.
\tag{4.1}
\]

令 `k_a` 为 m 个非负、质量为 1 的函数 `a_j exp(−a_jt)1_{t≥0}` 的卷积。部分分式恒等式

\[
\prod_j\frac{a_j}{s+a_j}
=\sum_j\frac{a_jv_j}{s+a_j}
\tag{4.2}
\]

可直接把两侧乘以 `Π(s+a_j)` 后在 `s=−a_j` 检查；两边所得多项式次数≤m−1，因此 m 个互异点已确定它们相等。由有限指数卷积（或对卷积逐项积分的 Laplace 变换）得

\[
k_a(t)=\sum_ja_jv_je^{-a_jt},\qquad
\int_t^\infty k_a(u)du=\sum_jv_je^{-a_jt}.
\]

于是

\[
I'(t)=1-\sum_jv_je^{-a_jt}=\int_0^t k_a(u)du,
\]

\[
\boxed{I(t)=\int_0^t(t-u)k_a(u)du\ge0.}
\tag{4.3}
\]

所有 m 均成立，特别 m=1 时 `k_a(t)=a exp(−at)`，没有端点异常。这是辅助解析正卷积，也可等价写为 `E[(t−S)_+]`；概率解释不构成原源的随机性假设。

对任意 `s>0`，标量不等式 `x_+≤e^{sx}/(es)` 给出

\[
\boxed{I(t)\le\frac{e^{st}}{es}H_a(s),
\qquad H_a(s):=\prod_j\frac{a_j}{a_j+s}.}
\tag{4.4}
\]

因为卷积的带权积分等于各因子带权积分之积，式 (4.4) 不需要在正负 Lagrange 权上逐项取绝对值。

## 5. 全整数 Möbius 接合与完整道路核

对 n>1，`Σ_{d|n}μ(d)=0` 且 `−Σ_{d|n}μ(d)log d=Λ(n)`，所以

\[
D_n=-\sum_{d\mid n}\mu(d)F(\log d),\qquad
\boxed{e_n=D_n-\Lambda(n)=\sum_{d\mid n}\mu(d)I(\log d).}
\tag{5.1}
\]

`e_1=I(0)=0`。这里真实背景、κ 和 `c=μ*(D−κ)` 没有改动；(5.1) 仅是两条同背景道路的源差恒等式。

令

\[
K_d(y)=\sum_{1\le r\le y/d}(y/(dr)-1)
=\frac ydH_{\lfloor y/d\rfloor}-\lfloor y/d\rfloor\ge0.
\]

有限换序给出

\[
\boxed{q(y)-q^*(y)=\sum_{d\le y}\mu(d)I(\log d)K_d(y).}
\tag{5.2}
\]

单位 d=1 的 I 值为零，d=y 的 K 值为零。现在才对 (5.2) 取绝对值，使用 `|μ(d)|≤1` 和 (4.4)：

\[
|q(y)-q^*(y)|\le\frac{H_a(s)}{es}
\sum_{d=2}^y d^sK_d(y).
\tag{5.3}
\]

### 5.1 无额外除数数目或窗口对数的求和

固定 `0<s≤1`。函数 `g_s(t)=t^{s-1}(1-t)` 在 (0,1] 上非负递减。对任意实数 M≥1，右端点矩形给

\[
\sum_{d=1}^{\lfloor M\rfloor}d^s(M/d-1)
\le M^{s+1}\int_0^1g_s(t)dt
=\frac{M^{s+1}}{s(s+1)}.
\tag{5.4}
\]

因此

\[
\sum_{d=2}^y d^sK_d(y)
\le\sum_{r=1}^{\infty}\frac{(y/r)^{s+1}}{s(s+1)}
=\frac{y^{s+1}\zeta(s+1)}{s(s+1)}.
\]

外层 r 实际仅到 floor(y/2)；扩展为正收敛级数只用于上界。得到

\[
\boxed{|q(y)-q^*(y)|
\le\frac{H_a(s)\zeta(s+1)}{es^2(s+1)}y^{s+1}
\le\frac{H_a(s)}{es^3}y^{s+1}.}
\tag{5.5}
\]

末步使用初等界 `ζ(s+1)≤1+1/s`。没有把 (5.1) 中的除数和直接省略；它在完整共同前缀中经 (5.4) 支付。

记 `C_s=H_a(s)/(es³)`。对 `y≤B`，(5.5) 给 `|q(y)−q*(y)|≤C_s B^s y`。因此

\[
\boxed{\|q-q^*\|_{w,[A,B]},\quad
\|I_\Pi(q-q^*)\|_{w,[A,B]}
\le C_s B^s\sqrt{B-A+1}.}
\tag{5.6}
\]

这里 Π 可以任意，但含真实两端点；插值保持的是线性上界 `C_s B^s y`，没有把凸函数 y^(s+1) 的割线误认为位于曲线下方。

### 5.2 可直接用于旧固定点表的有理半径

取 s=1 时，`H_a(1)` 对有理厚度是精确有理数，

\[
\boxed{|q(y)-q^*(y)|\le\frac{H_a(1)\zeta(2)}{2e}y^2.}
\tag{5.7}
\]

以 `Z_N=Σ_{j=1}^N1/j²+1/N>ζ(2)` 和 `E_M=Σ_{j=0}^M1/j!<e` 替换，可得到纯有理安全半径 `H_a(1) Z_N y²/(2E_M)`。它可与上轮所有已证半径逐点取小；不读取实际 q 样本来选定半径，也不需要新增厚度指数查询。

## 6. 固定宽度有理 Chebyshev 族的新阶数

沿用上轮构造：T_m 根 z_j、`b_j=θ(1+z_j)/2`、实际有理 `|a_j−b_j|≤θ/(128m³)`。已有根间隔证明给 `b_j≥θ/(4m²)`，故 `|a_j/b_j−1|≤1/(32m)`。

对 s>0，逐因子比较与 Bernoulli 不等式给

\[
\frac{H_a(s)}{H_b(s)}
\le\left(\frac{1+1/(32m)}{1-1/(32m)}\right)^m
\le(32/31)^2.
\tag{6.1}
\]

Chebyshev 多项式的首项系数、根对称性及 `T_m(−1)=(−1)^m` 给

\[
\prod_jb_j=2(\theta/4)^m,
\quad \prod_j(s+b_j)=2(\theta/4)^mT_m(1+2s/\theta),
\]

\[
H_b(s)=1/T_m(1+2s/\theta).
\]

置 `z=1+2s/θ>1`、`r=z+sqrt(z²−1)>1`。由递推直接验证 `T_m(z)=(r^m+r^(−m))/2`，于是

\[
\boxed{H_a(s)\le\frac{2048}{961}r^{-m}.}
\tag{6.2}
\]

取 `m=ceil(c log B)`，(5.6) 推出

\[
\boxed{\|q-q^*\|_w,\ \|I_\Pi(q-q^*)\|_w
\le\frac{2048}{961es^3}
B^{1/2+s-c\log r}.}
\tag{6.3}
\]

所以明确的充分条件为 `c log r−s>1/2`。对 θ=1/2、s=2/5，有 `z=13/5`、`sqrt(z²−1)=12/5`、r=5。选择 `c=14/25` 时

\[
\frac{14}{25}\log5-\frac9{10}
=0.001285230963096209776425226606\ldots>0.
\tag{6.4}
\]

这给出 (1.2)。取 c=3/5 时，衰减指数为 `(3/5)log5−9/10=0.06566274746046022476045559993571258…`。

固定宽度族的原有节点位数 `O(log m)`、单权重位数 `O(m log m)`、全部权重直接表示 `O(m²log m)`、权重总变差 `<4m` 继续适用；节点实际有理权重新精确计算，0 处权与 z 坐标下 −1 处权一致。

## 7. 普通素数层归约的匹配条件也可满足

固定宽度族还需要逐整数误差，而不仅是道路误差。由 (5.1)、(4.4)，对 `n≤B` 和 `0<s<1`，

\[
|e_n|\le\frac{H_a(s)}{es}\prod_{p\mid n}(1+p^s)
\le\frac{H_a(s)}{es}n^s
\exp\!\left(\sum_{p\mid n}p^{-s}\right).
\]

若 `r_n=ω(n)≤log B/log2`，将不同素数递增排序，粗下界第 i 个素数≥i+1 给

\[
\sum_{p\mid n}p^{-s}
\le\sum_{i=1}^{r_n}(i+1)^{-s}
\le\frac{(r_n+1)^{1-s}}{1-s}.
\]

于是当 (6.3) 的指数严格为负时，统一有

\[
\varepsilon_B\sqrt B
\le O\!\left(B^{1/2+s-c\log r}
\exp\bigl(O((\log B)^{1-s})\bigr)\right)\longrightarrow0.
\tag{7.1}
\]

其中小于任意正幂的因子是显式除数支持成本，未被抹去。因此 0.56 阶族同样可以接入前驱普通素数层归约；该渐近界的有限起效阈值可能较大。单厚度族的 (2.5) 更直接。

## 8. 核验与当前范围

`verify_actual_matching.py` 复用前驱 m=1,…,16 的有理节点，精确检查 16 个 (4.2) 多项式恒等式、0 处权、136 个匹配矩及 32 个有理 Laplace 界；以有理 atanh 级数认证 (6.4) 的正性。另对 m=1,…,12 精确检查 78 个缩尺度匹配矩。取 `B=256,a=1/256`，有向区间核对 255 个源符号与半径、256 个 Möbius 源恒等式、256 个完整前缀恒等式、512 个完整前缀上界，以及各 256 个乘法支撑平均的源界和道路界。输出 `actual_matching_certificate.json`。数学全参数结论由上述解析证明承担。

同轮 anchor 分支作者已交叉核对 §§2–7 的符号、卷积密度、0 处权、完整前缀求和、Chebyshev 扰动及参数条件，确认没有遗漏除数数目或窗口对数成本。这项核对属于共同作者工作。本文 `ε_B` 指源误差；与其他证明中的道路归一化误差记号须区分。

本轮没有为未知的普通素数统一亏缺估计或 q* 真实骨架上界补入假设。匹配部分已提供两种明确可行的无界族，后续可以按尺度与精度成本选择。

### 前置来源

- 上轮 `matching_order/PROOF.md`：有理 Chebyshev 节点隔离、根间距、有理扰动、精确权和表示长度。
- 上轮 `matching_transfer/ALL_ORDER_MATCHING_KERNEL.md`：一般源包络核的精确范围，固定 11 厚度混号证据。
- 前驱 `prior/riemann_cumulative_haar_20261123/dependencies/ARITHMETIC_FINE_REMAINDER_BOUNDS.md` §1：直接厚度插值误差。
- 同前驱 `prefix_compute/PAIRED_PREFIX_ORACLE.md` §§2–4：完整道路、单位与背景、共同前缀公式。

