# C88：任意缓慢移动的真实库存设计

## 1. 对象与新桥接

原安排仍为 `2≤w≤v≤c`，共 `binom(c,2)` 条；读取原来的
`H(0,1)`，额外因子 5 放在第一次 23 更新之前。三个库存为

\[
c,\qquad c+A,\qquad c+B,\qquad 1\le A<B=o(c).
\]

记

\[
\theta=A/B,\quad D=\sqrt{c/B},\quad
p_*(c,B)=\frac74\log_2c+\frac12\log_2(c/B),\quad
L_c=2^{p-p_*}.
\]

本轮 `bridge/GENERAL_MOVING_POSITION.md` 首先证明统一跟踪：若

\[
R_c=\frac{A(B-A)}{\sqrt{cB}}\to\infty,
\qquad B=o(c),\qquad 0<L_-\le L_c\le L_+<\infty,
\]

则 `sup_α|V_c(α)−Φ_(A/B)(L_c)|→0`，不要求位置比例收敛。
这也覆盖任何固定实数内点：取 `A=⌊θB⌋` 即可，无需固定有理分母。
其端点特例 `bridge/MOVING_ENDPOINT_BRIDGE.md` 证明：若

\[
\theta\longrightarrow0,\qquad A/D\longrightarrow\infty,
\qquad L_c\longrightarrow L\in(0,\infty),
\tag{1}
\]

则原全库存、全部整数对手的唯一率一致于三个舍入格原点趋于

\[
\Phi_0(L)=2\int_\Delta F_0(L^2J(X))\,dX.
\tag{2}
\]

这里 `Δ={0<y<x<1}`、`J=|det d(G,B₁)|` 为 C82 的原谱对象。
`F₀` 是 C85 已定义的独立三相位端点函数。新的内容是 (1)–(2)
的真实整数库存实现，而不是重新定义或重新发现 `F₀`。

若仅有 `0<L₋≤L_c≤L₊<∞`，同一定理和紧性给

\[
\sup_{\alpha\in\mathbb T^3}|V_c(\alpha)-\Phi_0(L_c)|\to0.
\tag{3}
\]

因此整数位数取整无需假装 `L_c` 沿全部整数库存收敛。

## 2. 中间间距可任意缓慢增长

**构造定理。** 对任何整数序列 `A(c)→∞`、`A=o(√c)`，取

\[
\boxed{B(c)=\lfloor c/A(c)\rfloor.}
\tag{4}
\]

则 (1) 的两个位置条件成立，且

\[
\frac Bc\sim\frac1A\to0,\qquad
D\sim\sqrt A,\qquad
\frac AD\sim\sqrt A\to\infty,\qquad
\theta\sim\frac{A^2}{c}\to0.
\]

证明只有这些等价式；由于 `A=o(√c)`，最终确有 `A<B`，取整的相对误差
趋零。对应的每次临界读取位数为

\[
\boxed{p_*(c,B)=\frac74\log_2c+\frac12\log_2A+o(1).}
\tag{5}
\]

例如 `A=⌈log₂log₂c⌉`，仍在该定理内。第一个库存增加量无需任何固定正幂
`c^ε`。条件 `A→∞` 是这个构造的适用条件；本篇没有证明它是所有可能实现的
必要条件。

更一般，任何整数 `A→∞`、`A=o(c)` 也可搭配合适的外间距。令
`h=min(A,√(c/A))`、`B=⌊c/h⌋`，则 `h→∞`、`A/B→0`，
并且 `A/D∼A/√h≥√A→∞`。式 (4) 是更简单的慢增长特例。

## 3. 幂次设计区域

若 `A∼c^α`、`B∼c^β`，其中 `0<α<β<1`，则桥接的充分条件准确化为

\[
\boxed{2\alpha+\beta>1.}
\tag{6}
\]

这是本轮已证定理覆盖的幂次区域；等号以及反向不等式并未被宣布为
唯一识别率的充要分界。对应

\[
\theta\sim c^{\alpha-\beta},\quad
A/D\sim c^{\alpha+(\beta-1)/2},\quad
p_*=(9/4-\beta/2)\log_2c+o(1).
\]

| 中间间距 A | 最外间距 B | A/D | 每次临界位数 p_* |
|---|---|---|---|
| `⌈c^(1/4)⌉` | `⌈c^(3/4)⌉` | `∼c^(1/8)` | `(15/8)log₂c+o(1)` |
| `⌈c^(1/5)⌉` | `⌈c^(4/5)⌉` | `∼c^(1/10)` | `(37/20)log₂c+o(1)` |
| 任意 `A→∞, A=o(√c)` | `⌊c/A⌋` | `∼√A` | `(7/4)log₂c+(1/2)log₂A+o(1)` |

## 4. 真正增添信息，而非重复同一准确值

C85 的准确关系为

\[
F_0(a)=2\int_0^1\ell F_2(a/\ell)\,d\ell.
\tag{7}
\]

`F₂` 非减、连续，且对每个正参数严格小于一、在无穷远趋一。因此
`F₂(a/ℓ)≥F₂(a)`，并在一段正长度的 `ℓ` 区间严格大于它，故

\[
\boxed{F_0(a)>F_2(a)\qquad(a>0).}
\tag{8}
\]

在同样的首末库存、同样的位数和首末格原点下，记只读首末的全库存唯一率
为 `V_c^(02)`。两端的真实唯一率至多其近距唯一率；C82 给出后者的极限
`Φ₂(L)=2∫_ΔF₂(L²J)`。于是对每个固定 `L>0`，

\[
\liminf_c\inf_\alpha\{V_c^{(3)}(\alpha)-V_c^{(02)}(\alpha_0,\alpha_2)\}
\ge 2\int_\Delta[F_0(L^2J)-F_2(L^2J)]\,dX>0.
\tag{9}
\]

最后的严格性只用 `J>0` 几乎处处及 (8)。即使中间位置比例趋零，这次
真实读取仍挽回正比例安排。式 (9) 不需要先知道两端全竞争者唯一率是否收敛。

在 `a≥1` 的辅助局部范围，C82 的两读数闭式代入 (7) 给出

\[
F_0(a)=1-\frac7{2\pi^2a},\qquad
F_0(a)-F_2(a)=\frac7{4\pi^2a},\qquad
\frac{1-F_0(a)}{1-F_2(a)}=\frac23.
\tag{10}
\]

这个 `2/3` 不可直接积分为全库存高倍率系数比：小 `J` 的尾层仍参与主项。

## 5. 端点高精度系数现可由原库存达到

令 `I₂=∫₀∞[1−F₂(t²⁰)]dt`，C85 已证 `I₀=(40/41)I₂`；
C87 已证 `Iθ>I₀` 对每个固定 `0<θ<1` 成立。C82 的尾层转移给

\[
1-\Phi_0(L)\sim W\frac{40}{41}I_2L^{-1/10},\qquad
1-\Phi_\theta(L)\sim WI_\theta L^{-1/10}.
\tag{11}
\]

因此本轮移动设计实现了 C87 中只能由内点逼近的最小主系数。比较任何固定
内点设计与满足 (1) 的移动设计，先取库存极限，再令 `L→∞`，移动设计严格更好。
低倍率方向则相反：

\[
\Phi_0(L)=C_{\rm end}M_2L^4+O(L^6),\qquad
\Phi_\theta(L)\sim\kappa_3M_{3/2}
\sqrt{\theta(1-\theta)/2}\,L^3.
\tag{12}
\]

这里 `M_r=2∫_ΔJ^r`、`C_end=2∫₀∞F₂(s)s⁻³ds>0`。
所以对任意固定内点，两条连续极限曲线至少相交一次。
没有证明交点唯一，也没有从 (11) 推出任意联动发散的 `L_c` 都服从该渐近。

## 6. 证明与来源边界

新增桥接见本轮 `bridge/MOVING_ENDPOINT_BRIDGE.md` 与
`bridge/GENERAL_MOVING_POSITION.md`；有限 `A/D` 的残余
分支筛选见 `critical/FINITE_SEPARATION_BRANCH_FILTER.md`。式 (4)–(6)、
真实实验增益 (9) 和实现结论由桥接及列明前件推出。
端点积分、小倍率系数和 `40/41` 来自 C85 `endpoint/ENDPOINT_LIMIT.md`；
严格高倍率位置排序来自 C87 `positions/GLOBAL_POSITION_THEOREM.md`。
本篇不把辅助读数格当作原生空间，也不删去原路径的整数标签或分支身份。
