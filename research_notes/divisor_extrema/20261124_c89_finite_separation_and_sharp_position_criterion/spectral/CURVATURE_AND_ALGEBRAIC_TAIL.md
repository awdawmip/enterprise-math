# C89：跨支径向曲率与有限分离的全局代数误差

## 1. 对象与结论

本文仍以原整数安排 `2 ≤ w ≤ v ≤ c` 的原读数 `H(0,1)` 为研究对象。
连续源坐标 `X=(v/c,w/c)`、谱和半代数集合用于其渐近计数，均为辅助读数表示。

沿用 C88 的三个库存 `c,c+A,c+B`，假设

\[
1\le A<B=o(c),\qquad B/c^{1/3}\to\infty,
\quad A/B\to0,
\]

\[
D=\sqrt{c/B},\qquad
p_*={7\over4}\log_2c+{1\over2}\log_2(c/B),\qquad
L_c=2^{p-p_*}\to L>0,\qquad A/D\to\tau<\infty.
\]

记 `F=(G,B₁)`，源域 `Δ={0<y<x<1}`。C88 定义的全宏观纤维相位筛选量为

\[
Q_\tau(X)=\int_{-1}^1(1-|d_0|)
\mathbf1\{\exists Y\ne X:F(Y)=F(X),\ 
|d_0-(L\tau/2)(B_2(Y)-B_2(X))|<1\}\,dd_0.
\tag{1}
\]

不存在其他宏观原像时令其为零。以下只在 C82 的正规有限纤维满测集上使用此定义；
零面积例外集的值不影响积分。

**全局代数率。** 存在只依赖原谱的常数 `C>0`、`η>0`，使对所有 `L,τ>0`

\[
\boxed{R_\tau(L):=2\int_\Delta Q_\tau(X)\,dX
\le C\min\{1,(L\tau)^{-\eta}\}.}
\tag{2}
\]

因此 C88 原点一致的有限分离夹逼可量化为

\[
\boxed{
\Phi_0(L)-C\min\{1,(L\tau)^{-\eta}\}
\le \liminf_c\inf_\alpha V_c^{\rm full}(\alpha)
\le \limsup_c\sup_\alpha V_c^{\rm full}(\alpha)
\le\Phi_0(L).}
\tag{3}
\]

式 (3) 是每组固定极限参数 `L,τ` 的库存极限结论。本文没有对原库存 `c`
的误差给出速率；`η` 是由一个有限代数消元多项式确定的正指数，本文未计算其
具体数值，也未声称它是最优指数。相位加权的 C89 改进界若用 `Wτ≤Qτ`，同样满足 (2)。

此外，原谱的非退化折叠给出常数 `c₀>0`，使

\[
\boxed{R_\tau(L)\ge c_0\min\{1,(L\tau)^{-1}\}.}
\tag{4}
\]

这是几何相位筛选量的下界，不把相位窗口中有实际整数竞争者作为前提或结论。

## 2. 同一前两谱纤维上的准确曲率公式

本节重用 C84 `BRANCH_TRANSITION.md` §3 已证明的公式；该文的 `q` 就是这里
的 `N`。以下保留短推导以便本篇自含核查，不将该恒等式计作 C89 新成果。

在固定符号的正谱内部，采用已有坐标

\[
\mathcal A=4x^{15/4},\qquad d=4(y/x)^{9/4},\qquad
m={7\over16}\mathcal A^4d,
\]

\[
G=C_*\frac{\mathcal A^{19/5}d^{14/3}
|\mathcal A-1||d-1|}{(1+m)(1+m\mathcal A)},
\]

\[
h={1\over\mathcal A-1}+5-4{m\over1+m}
-5{m\mathcal A\over1+m\mathcal A},\qquad
B_1=-{15\over4}hG.
\]

这里用 `𝒜` 区分谱坐标与中间库存增量 `A`。置

\[
u={m\over1+m},\quad v={m\mathcal A\over1+m\mathcal A},
\quad N={\mathcal A\over(\mathcal A-1)^2}
+16u(1-u)+25v(1-v).
\tag{5}
\]

径向算子 `E=x∂x+y∂y` 满足

\[
E={15\over4}\mathcal A\partial_{\mathcal A},\qquad
\mathcal A h_{\mathcal A}=-N,
\qquad EG=\left({15\over4}h-{3\over4}\right)G.
\]

代入已有恒等式 `B₂=−(E+7/4)B₁`，逐项得到

\[
\boxed{\frac{B_2}{G}
={225\over16}(h^2-N)+{15\over4}h.}
\tag{6}
\]

所以对同一 `F=(G,B₁)` 纤维内的两个正谱点，`G,h` 均相等，进而

\[
\boxed{B_2(Y)-B_2(X)
=-{225\over16}G(X)\{N(Y)-N(X)\}.}
\tag{7}
\]

这给出 C88 有限偏移的另一准确写法：

\[
h_{XY}=-{225L\tau\over32}G(X)\{N(Y)-N(X)\}.
\tag{8}
\]

曲率 `N` 保留各逆支的标签；式 (7) 并未把多个逆支合并成一个状态。

## 3. 最近跨支谱差是半代数函数

在 C82 的正规有限纤维满测集合上定义

\[
\delta(X)=\min\left(1,
\min_{Y\ne X,\ F(Y)=F(X)}|B_2(Y)-B_2(X)|\right),
\tag{9}
\]

空内层最小值按 `+∞` 处理。在所去掉的半代数零面积集合上可定义 `δ=0`。
这样 `0≤δ≤1`，且 C82 三谱几乎处处单原像定理给出 `δ>0` 几乎处处。

源域、谱、正规性及纤维关系都是半代数的。分数幂由正根变量表示，绝对值由
有限符号分片表示。式 (9) 的图可以用“存在一个达到该最小值的逆支，且没有
更小的逆支”，加上空纤维、截断和例外集条款，写成实多项式的一阶公式。
实闭域消元定理遂使它成为半代数图。这里使用的只是投影/消元封闭性，参见
S. Basu, *Algorithms in Real Algebraic Geometry: A Survey*, Theorem 2.1：
<https://www.math.purdue.edu/~sbasu/raag_survey2011_final-sep4-2014.pdf>。

以下给出所需测度估计的完整初等部分，避免把“半代数”本身当作未经说明的速率。

### 引理：正几乎处处的半代数函数具有幂次小值界

设 `Ω⊂R²` 有界，`f:Ω→[0,1]` 半代数，且 `f>0` 几乎处处。则存在 `C,η>0`
满足

\[
|\{X\in\Omega:0<f(X)\le\varepsilon\}|
\le C\varepsilon^\eta\qquad(0<\varepsilon\le1).
\tag{10}
\]

**证明。** 取 `f` 图的一个有限多项式符号公式，删去恒零和常数多项式。
图上每一点至少使其中一个多项式为零：否则全部符号在一个三维开邻域中
保持不变，那个开邻域就会包含于函数图，与单值性矛盾。因此某个非零多项式
`P(X,t)` 在整张图上为零。把它的最高公因子 `t^k` 除去，得

\[
P(X,t)=t^k\widetilde P(X,t),\qquad
p(X):=\widetilde P(X,0)\not\equiv0.
\]

当 `f(X)>0` 时仍有 `Ṕ(X,f(X))=0`。在包含 `Ω` 的固定闭矩形与 `0≤t≤1`
上，多项式的 `t` 导数有统一上界 `M`，所以

\[
0<f(X)\le\varepsilon\quad\Longrightarrow\quad
|p(X)|=|\widetilde P(X,0)-\widetilde P(X,f(X))|
\le M\varepsilon.
\tag{11}
\]

若 `p` 为非零常数，则充分小的 `ε` 下集合为空，其余 `ε` 调整常数即可。
否则令 `n=deg p≥1`，选择单位方向 `e`，使最高次齐次项 `p_n(e)=a≠0`。
在正交坐标 `X=se+re⊥` 中，每条固定 `r` 的切片上，`p` 是首项系数为同一个
常数 `a` 的 `n` 次一元多项式。将其在复数域分解成 `a∏(s−z_j)`。
若 `|p|≤Mε`，至少一个因子满足

\[
|s-z_j|\le(M\varepsilon/|a|)^{1/n}.
\]

每个这样的复圆盘在实轴上的投影长度不超过两倍半径，故整条切片上小值集
长度至多 `2n(Mε/|a|)^{1/n}`。对有界的 `r` 区间积分就得到 (10)，可取
`η=1/n`。这同时说明指数可由消元后的多项式确定，而没有执行消元不等于
已经知道它的数值。证毕。

## 4. 从小值界回到原库存唯一率

式 (1) 若非零，则存在某个逆支满足

\[
\left|{L\tau\over2}(B_2(Y)-B_2(X))\right|<2.
\]

当 `Lτ>4` 时，这给

\[
Q_\tau(X)\le\mathbf1\{\delta(X)<4/(L\tau)\}.
\tag{12}
\]

对 (9) 应用 (10)，零集没有面积，得到 (2)；其余 `Lτ≤4` 用 `0≤Rτ≤1`
并增大同一个常数覆盖。C88 已证

\[
\limsup_c\sup_\alpha(V_c^{\rm near}-V_c^{\rm full})\le R_\tau(L),
\qquad V_c^{\rm near}\to\Phi_0(L)
\]

原点一致，因而 (3) 直接成立。这一步没有给不同逆支的格点指定概率独立性。

## 5. 折叠给出相位筛选量的反向界

C82 `FIBER_STRUCTURE.md` 证明存在正谱内部的非退化折叠。取一小段紧折叠弧，
用参数 Morse 坐标 `(s,t)` 将 `F` 写成可逆目标变换后的
`(s,M(s)−t²)`。源换元的 Jacobian 在该紧片上有正下界，且 `B₂(s,t)` 光滑。
因此 `(s,t)` 与 `(s,−t)` 是同纤维的两个源点，并且

\[
|B_2(s,t)-B_2(s,-t)|\le C_1|t|
\tag{13}
\]

在整片上一致成立。对 `|t|≤min(t₀,1/(C₁Lτ))`，此竞争支的偏移绝对值
至多 `1/2`；C88 的准确函数 `q(h)=1−h²/2` 在这一区间至少为 `7/8`。
于是对该源条带积分即得 (4)，常数只由所选固定折叠片和原谱决定。

本文的 (2) 与 (4) 夹住相位必要条件的全局消退速度。实际全库存唯一率的
有限 `τ` 极限仍涉及耦合整数格；式 (3) 正是本篇无需解决该联合分布即可取得的
原问题结论。

## 6. 来源与证明强度

- C82, `CROSS_PHASE.md`：三谱几乎处处单原像、半代数例外集和有限纤维。
- C82, `FIBER_STRUCTURE.md`：非退化折叠与完整纤维结构。
- C82, `HIGH_PRECISION.md`：谱归一及 `N,T` 的已知表达。
- C84, `BRANCH_TRANSITION.md` §3：本篇 (6)–(7) 的既有曲率与跨支谱差公式；
  科学提交 `01f50954ee37548372464c68a311f7df2dba0632`，路径
  `research_notes/divisor_extrema/20261119_c84_precision_design_and_branch_filter/BRANCH_TRANSITION.md`。
- C88, `critical/FINITE_SEPARATION_BRANCH_FILTER.md`：有限分离偏移、`Qτ` 和全库存夹逼。
- Basu 上引 Theorem 2.1：仅用于实多项式公式的消元封闭性；小值测度引理已在本文证明。

新增代数速率及折叠下界均为手推证明，曲率恒等式重用 C84。本文未报告数值指数、
原库存误差率或外部同行审查。
