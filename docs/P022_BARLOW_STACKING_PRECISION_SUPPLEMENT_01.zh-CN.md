# P022 Barlow 堆垛精度补充 01 —— 精确 shell 公式与 drift 控制的测地增长

状态：`ACTIVE RESEARCH NOTE / EXACT INTEGER FINITE FORMULA + ASYMPTOTIC THEOREM / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：`P022_BARLOW_STACKING_PRECISION.*`  
边界：本文中的有限组合结论已证明；Barlow-specific geodesic-growth 公式的历史优先性尚未完成专项审计

## 1. 从 target-layer precision 推进到 whole-shell geometry

主 Barlow note 已证明：完整 root-to-one-target-layer distance+count language 只依赖目标层长度

\[
q=|k|
\]

与 prefix imbalance

\[
\delta_k.
\]

记

\[
d_k=|\delta_k|,
\qquad
c_k=\frac{q-d_k}{2}.
\]

则 mandatory vertical witness polynomial 具有 normal form

\[
P_k=(A+3)^{c_k}B_{\pm}^{d_k}.
\]

但一个 radius `n` 的完整 graph shell 会同时读取

\[
-n\le k\le n
\]

的所有 target layers。

因此 whole-shell 的正确有限状态不是单个 final imbalance，而是

\[
(d_{-n},\ldots,d_0,\ldots,d_n).
\]

下面先求出该 trajectory 中每一个坐标对 shell 的精确贡献。

## 2. triangular norm 上的 exposed-face counting

triangular graph norm 为

\[
h(q,r)=\max(|q|,|r|,|q+r|).
\]

其 radius shell 有六个 facets 和六个 corners。

给定非负 Laurent polynomial `P`，考虑

\[
P A^t,
\qquad t>0,
\]

其中

\[
A=x+x^{-1}+y+y^{-1}+xy^{-1}+x^{-1}y.
\]

落在 `supp(P)` 外 triangular distance 恰好为 `t` 的 coefficients，正是 Minkowski 扩张后的 outer boundary。

固定一个 facet normal。要落在这个 exposed facet：

- `P` 中选择的 exponent 必须位于对应 exposed face；
- `A` 的每一个 factor 都必须从该 normal 的两个 maximizing primitive steps 中选一个。

所以该 facet 上 coefficient mass 为

\[
F(P)\,2^t.
\]

相邻两个 facets 在一个 corner 相交。固定 corner 时，每个 `A` factor 只有一个同时 maximizing 的 primitive step，所以 overlap mass 就是 `P` 的对应 corner mass `C(P)`。

每个 outer-boundary point 要么属于一个 facet，要么属于两个相邻 facets 的交点，因此 inclusion-exclusion 给出精确恒等式

\[
\boxed{
\operatorname{Bd}_t(P)
=2^t\sum_{f=1}^{6}F_f(P)
-\sum_{v=1}^{6}C_v(P).
}
\]

这不是 asymptotic approximation，而是 coefficient identity。

## 3. Barlow normal form 的 face/corner masses

对 `A+3`，constant term 在所有非零 exposed directions 上都处于内部，因此 exposed faces 与 `A` 完全相同：

- 每个 facet mass = `2`；
- 每个 corner mass = `1`。

对 `B_+` 或 `B_-`：

- 六个 facets 中三个的 face mass 是 `1`；
- 另外三个是 `2`；
- 六个 corner masses 全部是 `1`。

product 的 exposed face 由各 factor 的 exposed face 相加，所以 face masses 相乘。于是对

\[
P_k=(A+3)^cB_\pm^d
\]

有

\[
\sum_fF_f(P_k)
=3\cdot2^c(1+2^d),
\]

并且

\[
\sum_vC_v(P_k)=6.
\]

因此所有 `t>0` 都满足

\[
\boxed{
\operatorname{Bd}_t(P_k)
=3\cdot2^{c+t}(1+2^d)-6.
}
\]

stacking prefix 对该结果的全部影响只剩下 `(c,d)`，也就是 `(q,|delta_k|)`。

## 4. P022-BG01 —— target layer 对 radius-`n` shell 的精确贡献

设 shell radius 为 `n`，target layer 为 `k`，并记

\[
q=|k|\le n,
\qquad
d=|\delta_k|,
\qquad
c=(q-d)/2.
\]

### 极端层 `q=n`

长度为 `n` 的 geodesic 不可能再包含 layer 内 step。每个 interface 有三个选择，因此所有 monotone vertical words 共

\[
\boxed{
L_n(k)=3^n
\qquad(q=n).
}
\]

### 非极端层 `q<n`

令

\[
t=n-q>0.
\]

Section 3 的 boundary mass 先统计 vertical 与 horizontal subsequences 内部的有序选择；再从总共 `n` 个位置中选择 `t` 个 layer 内 steps：

\[
\binom nt=\binom nq.
\]

所以

\[
\boxed{
L_n(k)
=\binom nq
\left(
3\cdot2^{c+n-q}(1+2^d)-6
\right),
\qquad q<n.
}
\]

等价地，

\[
\boxed{
L_n(k)=\binom nq
\left[
3\cdot2^n
\left(
2^{-(q+d)/2}+2^{-(q-d)/2}
\right)-6
\right].
}
\]

至此不再需要枚举该 target layer 上的 shell endpoints。

## 5. P022-BG02 —— 任意 Barlow prefix 的 exact whole-shell formula

只要知道 radius `n` 内各 target layers 的 prefix imbalance，就有

\[
\boxed{
T(n)=\sum_{k=-n}^{n}L_n(k).
}
\]

所以 whole-shell shortest-path total 只依赖有限 absolute prefix-imbalance trajectory：

\[
\boxed{
(|\delta_{-n}|,\ldots,|\delta_n|).
}
\]

imbalance sign 在这里进一步被擦掉，因为整个水平 layer 求和后 triangular lattice 具有 reflection symmetry。

这比 target-endpoint theorem 又多一层合法压缩：

- 固定 target layer 的 coordinate-sensitive endpoint queries 需要 signed `delta_k`；
- 只问该 target layer 对 shell-total 的贡献时，只需要 `|delta_k|`；
- 询问完整 radius-`n` shell 时，只需要所涉 layers 的 absolute imbalance trajectory。

reference tests 对 period length 不超过 4 的全部 ± patterns，在 radius 5 内逐 target layer 检查 BG01，而不是只检查最终 whole-shell sum。

## 6. 周期 drift

现在假设 stacking 周期为

\[
L\ge1,
\]

一个周期的 signed drift 为

\[
D=\sum_{j=0}^{L-1}\sigma_j.
\]

定义绝对 rational drift density

\[
\boxed{
\mu=\frac{|D|}{L}\in[0,1].
}
\]

规范状态仍可只保存整数 `(|D|,L)`，不要求浮点除法。

对 upward target `q=mL+r`，周期性给出

\[
\delta_q=mD+\delta_r.
\]

`delta_r` 只来自有限 period remainder，因此有界。向下 prefixes 同样只有一个有限 reversed phase。因此存在只依赖该 stacking period 的有限常数 `C`，使所有 signed target layers 都满足

\[
\boxed{
\left|
|\delta_k|-\mu|k|
\right|\le C.
}
\]

所以 absolute imbalance = linear drift + bounded periodic phase。

## 7. P022-BG03 —— 周期 whole-shell geodesic growth 只由 drift density 决定

当 `q<n` 时，BG01 写成

\[
L_n(k)=\binom nq
\left[
3\cdot2^n
\left(
2^{-(q+d_k)/2}+2^{-(q-d_k)/2}
\right)-6
\right].
\]

因为 `d_k>=0`，括号中第二个指数项更大。周期性又给出

\[
d_k=\mu q+O(1).
\]

因此存在只依赖有限 period 的正整数常数界 `c_1,c_2`，使所有非极端层在充分大的 shell 上满足

\[
 c_1\binom nq2^n
 2^{-q(1-\mu)/2}
\le
L_n(k)
\le
 c_2\binom nq2^n
 2^{-q(1-\mu)/2}.
\]

`-6` 不会破坏 lower bound：`q<n` 时未修正 boundary factor 至少为 `4`，所以

\[
3F-6\ge\frac32F.
\]

令

\[
a=2^{-(1-\mu)/2}.
\]

对 target-layer heights 求和，在固定 multiplicative constants 内就是

\[
2^n\sum_{q=0}^{n-1}\binom nqa^q.
\]

而

\[
\sum_{q=0}^{n-1}\binom nqa^q
=(1+a)^n-a^n.
\]

两个 extreme layers 总共只有

\[
2\cdot3^n,
\]

而

\[
2(1+a)\ge2+\sqrt2>3,
\]

所以它们在指数尺度上严格次要。

因此

\[
\boxed{
T(n)=\Theta\!\left(\lambda(\mu)^n\right)
}
\]

其中

\[
\boxed{
\lambda(\mu)
=2(1+a)
=2+2^{(1+\mu)/2}.}
\]

等价地，

\[
\boxed{
\lim_{n\to\infty}T(n)^{1/n}
=2+2^{(1+\mu)/2}.}
\]

所以得到严格结论：**任意周期 Barlow stacking 的 shell-total geodesic multiplicity 指数增长率，只依赖 absolute period drift density `|D|/L`，与 period 内 literal interface order 无关。**

但 finite shells 仍可不同，因为 bounded prefix phase 在取 limit 以前仍然可见。

## 8. 增长常数的 integer-first 代数表达

无需把 growth constant 存成 float。

由

\[
\mu=|D|/L
\]

有

\[
\lambda-2=2^{(L+|D|)/(2L)}.
\]

取整数幂 `2L`：

\[
\boxed{
(\lambda-2)^{2L}=2^{L+|D|}.}
\]

所以规范的 exact growth descriptor 可以只保存整数对

\[
\boxed{(2L,\ 2^{L+|D|})}
\]

以及“选取大于 2 的正实根”这一解释。

这与进取数论的 integer-first state discipline 完全兼容。

## 9. 特例

### FCC-type constant drift

`L=1`、`|D|=1`，故

\[
\mu=1,
\qquad
\lambda=4.
\]

integer equation：

\[
(\lambda-2)^2=4.
\]

与此前

\[
T_{FCC}(n)
=6\cdot4^n+8\cdot3^n-24\cdot2^n+12
\]

一致。

### HCP alternating stacking

`L=2`、`D=0`，所以

\[
\mu=0,
\qquad
\lambda=2+\sqrt2.
\]

integer equation：

\[
(\lambda-2)^4=4.
\]

与上一份 HCP recurrence 完全一致。

### 所有 zero-drift periodic Barlow stackings

只要

\[
D=0,
\]

无论 period length 和内部 order 如何，

\[
\boxed{
\lambda=2+\sqrt2.}
\]

所以 HCP 在 asymptotic geodesic-growth exponent 层并不唯一；它仍可由 finite multiplicity spectrum 和 prefix phase 与其他 zero-drift stackings 区分。

### 中间 drift

period `(-,-,+)`：

\[
L=3,\quad |D|=1,\quad\mu=1/3,
\]

故

\[
\lambda=2+2^{2/3},
\]

integer equation 为

\[
(\lambda-2)^6=16.
\]

period `(-,-,-,+)`：

\[
L=4,\quad |D|=2,\quad\mu=1/2,
\]

故

\[
\lambda=2+2^{3/4},
\]

integer equation 为

\[
(\lambda-2)^8=64.
\]

因此 close-packed family 在 zero-drift 与 constant-drift 两个极端之间形成一族严格有序的 algebraic geodesic-growth rates，由 rational drift density 参数化。

## 10. 精度含义

同一条 literal stacking history，在不同 query language 下对应不同的 exact state：

### 一个指定 target layer

需要

\[
\delta_k.
\]

### 某指定 layer 对 whole horizontal shell 的贡献

只需要

\[
|\delta_k|.
\]

因为对整个 layer 求和后 reflection 会擦掉 sign。

### radius `n` 的完整 finite graph shell

需要

\[
(|\delta_{-n}|,\ldots,|\delta_n|).
\]

### 一个周期 stacking 的 exponential growth rate

状态进一步坍缩到

\[
\boxed{(|D|,L)}
\]

或等价 rational drift density `|D|/L`。

所以同一 stacking word 存在一个合法压缩阶梯：

\[
\text{word}
\to
\text{prefix imbalance trajectory}
\to
\text{selected imbalances}
\to
\text{absolute imbalance trajectory}
\to
\text{period drift density},
\]

但**每一步都只能在对应 future language 已经同步变弱的情况下成立。**

这是目前 P023/P024 future-language precision 原理在 intrinsic geometry 中最清楚的 concrete example 之一。

## 11. 已证明与未证明的边界

本文证明：

- BG01 exact target-layer shell contribution；
- BG02 exact whole-shell sum；
- periodic drift 的 bounded-phase 公式；
- BG03 exact exponential rate；
- growth rate 只依赖 drift density。

本文没有证明或主张：

- drift density 相同的两个 stackings 有相同 finite shells；
- 它们有相同完整 multiplicity spectra；
- 某个 growth rate 在物理上更优；
- 本 Barlow geodesic-growth formula 历史上一定新颖。

事实上 finite-shell equality 一般是假的：不同 zero-drift periods 可以共享相同 asymptotic rate，同时在有限 radius 下拥有不同 shell totals 与 spectra。

## 12. executable assets

新增：

- `src/enterprise_math/p022_barlow_growth.py`；
- `tests/test_p022_barlow_growth.py`。

测试逐 target layer 检查 BG01：period length 不超过 4 的全部 ± patterns、radius 不超过 5；随后检查 radius 6 的 whole-shell formula、FCC/HCP 特化，以及 equal-drift / different-finite-shell 反例。
