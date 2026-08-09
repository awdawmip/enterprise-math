# P025 补充 13 —— Absorption Floor 的三块 Derivative-Content 压缩

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 05–06  
Hard block：`NONE`

## 1. 动机

补充 05 已经给出精确 cross-prime formula：

\[
\eta_{\min}
=
\gcd_{\text{cross-block }p,q}
\frac{R e_p e_q}{g p q},
\]

其中 `R=rad(abc)`，`e_p=v_p(abc)`，`g` 是 raw additive row 的 content。

这个公式已经有限，但表面上仍需要保留全部 prime-pair data。本补充证明：如果 future observable 只是 `eta_min`，那么 `a,b,c` 三个 support blocks **各自内部的全部 prime coordinates 都可以精确坍缩成一个整数 content**。

于是完整 absorption floor 最终只需至多三个 block-pair integers 就能恢复。

## 2. P025-D04 —— Normalized block derivative content

对正整数 `n>1`，记

\[
R_n=\operatorname{rad}(n),
\qquad
m_n=\frac n{R_n}.
\]

prime-coordinate arithmetic derivative 为

\[
d_x(n)
=n\sum_{p\mid n}\frac{v_p(n)}p x_p.
\]

除以 compulsory multiplicity residual 后：

\[
\boxed{
\frac{d_x(n)}{m_n}
=
\sum_{p\mid n}
 v_p(n)\frac{R_n}{p}x_p.
}
\]

定义

\[
\boxed{
h(n)
=
\gcd_{p\mid n}
\left(
 v_p(n)\frac{R_n}{p}
\right).}
\]

对 unit block 定义

\[
h(1)=0.
\]

称 `h(n)` 为 **normalized block derivative content**。

## 3. P025-T36 —— 一个整数 ideal 就是完整 block image

对 `n>1`，当 local prime-coordinate vector `x` 遍历

\[
\mathbb Z^{\operatorname{supp}(n)}
\]

时，normalized derivative values 恰好组成

\[
\boxed{
\left\{
\frac{d_x(n)}{m_n}:x\right\}
=h(n)\mathbb Z.
}
\]

### 证明

normalized derivative 是一个整数线性形式，其 coefficient list 为

\[
\left\{
 v_p(n)R_n/p:p\mid n
\right\}.
\]

所有值都被它们的 gcd `h(n)` 整除；反过来，针对该 coefficient list 的 Bezout identity 给出一个整数 coordinate vector，使线性形式恰好取值 `h(n)`，再通过整数倍得到 `h(n)Z` 的全部元素。∎

### 解释

对任何只通过 normalized derivative value 观察一个 block 的 future language，完整 within-block prime-coordinate state 都能精确替换成 principal ideal generator `h(n)`。

这不是 approximation，而是 exact quotient。

## 4. P025-T37 —— Raw additive-row content 同样可以 block-compress

在 `n` 的 support block 内，raw additive-relation coefficients 为

\[
\frac{n v_p(n)}p
=
 m_n\left(v_p(n)\frac{R_n}p\right).
\]

因此 block content 为

\[
\boxed{m_n h(n).}
\]

对 primitive abc triple，完整 raw additive-row content 因而就是

\[
\boxed{
g
=
\gcd\bigl(
 m_a h(a),
 m_b h(b),
 m_c h(c)
\bigr),}
\]

其中 unit block 对 gcd 贡献零。

所以一旦 `h(a),h(b),h(c)` 已知，连形成 `alpha_hat` 所需的 normalization 也不再需要逐 prime coordinates。

## 5. P025-T38 —— 至多三个 block-pair generators 决定 `eta_min`

记

\[
R_a=\operatorname{rad}(a),
\quad
R_b=\operatorname{rad}(b),
\quad
R_c=\operatorname{rad}(c),
\]

以及

\[
h_a=h(a),
\quad
h_b=h(b),
\quad
h_c=h(c).
\]

对每一对非空 support blocks 定义

\[
\boxed{
E_{ab}=\frac{R_c h_a h_b}{g},
\qquad
E_{ac}=\frac{R_b h_a h_c}{g},
\qquad
E_{bc}=\frac{R_a h_b h_c}{g},
}
\]

若对应的 pair 中含有 empty/unit block，则该项不保留。

每个被保留的 `E_ij` 都是正整数，并且

\[
\boxed{
\eta_{\min}
=
\gcd(E_{ab},E_{ac},E_{bc})
}
\]

其中只对保留的正项取 gcd。

### 证明

固定一个 block pair，例如 `a,b`。补充 05 的 cross-prime terms 为

\[
K_{p,q}
=
\frac{R_aR_bR_c}{g}
\left(\frac{v_p(a)}p\right)
\left(\frac{v_q(b)}q\right).
\]

改写成

\[
K_{p,q}
=
\frac{R_c}{g}
\left(v_p(a)\frac{R_a}p\right)
\left(v_q(b)\frac{R_b}q\right).
\]

因为两个 index 独立变化，全部 `p|a,q|b` 项的 gcd 可分离为两个 block gcd 的乘积：

\[
\gcd_{p,q}K_{p,q}
=
\frac{R_c}{g}
\left(
\gcd_{p|a}v_p(a)R_a/p
\right)
\left(
\gcd_{q|b}v_q(b)R_b/q
\right),
\]

这正是

\[
E_{ab}=R_c h_a h_b/g.
\]

另外两个 block pairs 完全相同。于是对全部 cross-prime pairs 取 gcd，就等价于对至多三个 block-pair generators 取 gcd。∎

## 6. 压缩定理

合并 P025-T36–T38，精确 absorption floor 只依赖

\[
\boxed{
\Sigma_{\rm block}(a,b,c)
=
\bigl(
(R_a,m_a,h_a),
(R_b,m_b,h_b),
(R_c,m_c,h_c)
\bigr).
}
\]

一旦这个 state 已知，任何单独 prime-pair minor 都不再需要保存。

一般情况下，这比完整 prime-coordinate witness generator 严格更粗。

它对 `eta_min` 足够，但**不能**据此恢复完整 witness lattice、minimum witness radius `mu`、access radius `nu` 或完整 Pareto frontier；这些更丰富 future observables 仍依赖 prime-coordinate coefficients 的几何结构。

## 7. 例子

### `1+242=243`

unit block 为

\[
(R_a,m_a,h_a)=(1,1,0).
\]

对

\[
242=2\cdot11^2,
\]

有

\[
R_b=22,
\quad
m_b=11,
\]

normalized derivative coefficients 为

\[
11,\ 4,
\]

所以

\[
h_b=1.
\]

对

\[
243=3^5,
\]

有

\[
R_c=3,
\quad
m_c=81,
\quad
h_c=5.
\]

因此

\[
g=\gcd(0,11,405)=1,
\]

唯一保留的 block-pair generator 是

\[
E_{bc}=R_a h_b h_c=5.
\]

于是

\[
\boxed{\eta_{\min}=5.}
\]

对这个 observable 来说，内部 `(2,3)` 与 `(11,3)` 两种 prime pair 已经不再需要保存。

### `2+7=9`

\[
h_a=1,
\qquad
h_b=1,
\qquad
h_c=2,
\qquad
g=1.
\]

三个 block generators 为

\[
E_{ab}=3,
\qquad
E_{ac}=14,
\qquad
E_{bc}=4.
\]

所以

\[
\eta_{\min}=\gcd(3,14,4)=1.
\]

### `5+7=12`

这里

\[
h_a=h_b=1,
\qquad
h_c=2,
\qquad
g=1,
\]

因此

\[
(E_{ab},E_{ac},E_{bc})=(6,14,10)
\]

并得到

\[
\boxed{\eta_{\min}=2.}
\]

## 8. 与 second-order support closure 的关系

block content

\[
h(n)=\gcd_p v_p(n)R_n/p
\]

让 Stage 06 的 second-order phenomenon 更具体。

它的 prime factors 只能来自：

- 已经存在于 `R_n` 的 primes；
- valuation exponents `v_p(n)` 的 prime factors。

它无法从其它来源获得真正新的 prime label，因为它只是这些整数乘积的 gcd。

因此 block-compressed formula 与 second-order support-closure theorem 完全一致：

\[
\operatorname{supp}(\eta_{\min})
\subseteq
\operatorname{supp}(R)
\cup
\bigcup_p\operatorname{supp}(v_p(abc)).
\]

## 9. 架构含义

同一个 fine prime-coordinate state 现在出现两种截然不同的 exact compression：

### Arithmetic-floor language

若 future task 只询问 `eta_min`，则

\[
\boxed{
\text{prime-coordinate valuation state}
\to
\text{三个 block contents }h_a,h_b,h_c
\to
\eta_{\min}
}
\]

已经 exact。

### Geometric-access language

若 future task 需要 `mu`、`nu`、具体 witness 或 Pareto frontier，同样的 block compression 一般就过粗。

所以这又是 P023 principle 的具体实例：

> 合法的最粗精度不是一个数本身的永久固有属性，而是由必须保持 exact 的 future observable 决定。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_absorption_block.py`
  - normalized block derivative coefficients；
  - block image content `h(n)`；
  - raw additive block content `m(n)h(n)`；
  - 至多三个 block-pair absorption generators；
  - 对 `eta_min` 足够的 compact block state。
- `tests/test_abc_absorption_block.py`
  - exact block image examples；
  - raw additive content reconstruction；
  - 工作 absorption examples；
  - 对全部 `c<100` primitive triples 穷举验证 block formula 与 cross-prime formula 一致。

## 11. Prior-art discipline

一个整数线性形式的 image 是由 coefficients gcd 生成的 principal ideal，属于初等 Bezout algebra。独立 index 的 separable pair products 之 gcd 可以按 block gcd 分组，同样是初等算术。

P025 不主张这些代数 identity 本身是新数学。

项目侧真正的候选价值是：`abc` arithmetic-Wronskian absorption floor 可以拥有如此小的 exact precision state，而 witness-access geometry 不能同样压缩。这种 task-indexed compression 作为项目综合目前仍标记 `NOVELTY_UNVERIFIED`。

## 12. 下一前沿

不存在 hard block，继续：

1. 构造两个不同 fine triples，它们有相同 block absorption state，却有不同 access radius `nu`，直接证明 block compression 对 geometric-access language 不足；
2. 直接从 `(R_i,m_i,h_i)` 推导 local-prime obstruction formula，而不回到全部 exponent coordinates；
3. 测试 `h(n)` 在 multiplication 或 exponentiation 下是否存在有用 recursive precision structure；
4. 把 block derivative content 与 Pasten 的 lattice bases / norm bounds 做精确比较；
5. 检验其它 relation-conditioned witness systems 中是否也会出现类似 block-content compression。
