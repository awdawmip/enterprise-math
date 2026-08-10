# R004 精度宇宙生成 —— Supplement 05：isotropic divisor-grid expansion 与 finite macro crossover

状态：`PROVED_WIP + EXECUTABLE_CHECKED + CANDIDATE_PHYSICAL_INTERPRETATION`  
Parent：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_04.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

Supplement 04 找到了 canonical arithmetic scale-axis rank，但也暴露了第一版 prime-product geometry candidate 的弱点：直接把 prime-power 数值当成 spatial side lengths，通常会得到不相等的全局 axis lengths。

本补充把 geometry 移到 divisor lattice 本身。intrinsic coordinates 取 prime **exponents**，而不是 prime-power magnitudes。只要 active exponents 相等，得到的 geometry 就精确 axis-symmetric。

## 1. Divisor lattice 是 exact finite exponent grid

令

\[
\lambda=\prod_{i=1}^D p_i^{a_i}.
\]

`lambda` 的每个 positive divisor 都有唯一表示

\[
d=\prod_{i=1}^D p_i^{e_i},
\qquad
0\le e_i\le a_i.
\]

因此 divisor set 与 finite integer box 精确双射：

\[
\boxed{
X_\lambda
=\prod_{i=1}^D\{0,1,\ldots,a_i\}.
}
\]

若两个 divisor states 恰有一个 exponent 改变 `+1` 或 `-1`，就在它们之间连 edge。这正是 divisor lattice 的 Hasse graph，也是 side lengths `a_i+1` 的 path Cartesian product。

于是

\[
\boxed{|X_\lambda|=\prod_i(a_i+1)=\tau(\lambda),}
\]

\[
\boxed{
|E_\lambda|
=\sum_i a_i\prod_{j\ne i}(a_j+1),
}
\]

而 intrinsic graph diameter 为

\[
\boxed{\operatorname{diam}(X_\lambda)=\sum_i a_i.}
\]

shortest-path metric 就是 exponent coordinates 上成熟的 `L1` distance。以上都属于标准有限 divisor-lattice / graph 数学。

## 2. Precision one 真的是一个点

当

\[
\lambda=1
\]

时，没有 active prime factors，因此也没有 exponent coordinates。divisor grid 就是 singleton

\[
X_1=\{()\}.
\]

其 arithmetic rank 为 0，只有一个 vertex，没有 edge，diameter 为 0。

关键在于，未来的 `D` 并没有藏在 `1` 的 factorization 里。后续 rank-opening event 必须真正引入新的 prime support。这保留了 R004 的强边界：precision-one pregeometry 不能偷偷带着一个已经展开的 hidden coordinate carrier。

## 3. Isotropic genesis family

取一个 squarefree post-genesis support

\[
P=p_1p_2\cdots p_D.
\]

考虑 refinement sequence

\[
\boxed{\lambda_a=P^a,\qquad a=0,1,2,\ldots.}
\]

在 `a>=1` 时，每个 active prime exponent 都等于 `a`。因此

\[
X_{P^a}
\cong
\{0,1,\ldots,a\}^D.
\]

exact profile 为

\[
\boxed{
|V_a|=(a+1)^D,
}
\]

\[
\boxed{
|E_a|=D\,a\,(a+1)^{D-1},
}
\]

\[
\boxed{
\operatorname{diam}(X_{P^a})=Da.
}
\]

对于 `D=3`：

| level `a` | scale | grid | vertices | diameter |
| --- | --- | --- | ---: | ---: |
| 0 | `1` | point | 1 | 0 |
| 1 | `P` | `2x2x2` | 8 | 3 |
| 2 | `P^2` | `3x3x3` | 27 | 6 |
| 3 | `P^3` | `4x4x4` | 64 | 9 |

因此第一次 support-opening event 之后，可以得到一个 dimension 固定、但持续 finite expansion 的 grid candidate。

## 4. Prime-label independence

设 `P`、`Q` 都是 squarefree，而且拥有同样数量 `D` 的 prime factors。在同一 level `a`，`P^a` 与 `Q^a` 的 divisor exponent grids 都精确等于

\[
\{0,\ldots,a\}^D.
\]

忽略 arithmetic prime labels 后，用 exponent vector identity map 就得到 graph isomorphism。

因此所有只依赖 unlabeled exponent grid 的 graph observables——vertex count、edge count、diameter、shell/ball structure、finite distance spectrum——都只依赖 `(D,a)`，不依赖 `P` 里究竟是哪几个 primes。

所以 candidate 不再需要回答“为什么偏偏是 `2,3,5`？”真正未解决的问题变成

\[
\boxed{
\text{为什么第一次 support-opening event 的 rank 恰好是 }D=3?
}
\]

## 5. Exact nested expansion

geometry 不是每一层独立重建。

level `a` 的 states 是

\[
0\le e_i\le a.
\]

它们精确构成 level `a+1`

\[
0\le e_i\le a+1
\]

states 的子集。而且所有 old Hasse edges 原样保留，两个 old states 之间不会凭空新增 edge。因此

\[
\boxed{
X_{P^a}
\text{ 是 }
X_{P^{a+1}}
\text{ 的 induced subgraph}.}
\]

Expansion 只增加新的 outer exponent layers。

## 6. 用 gcd 做 canonical coarsening

若 `c|f`，并且 `d|f` 是 fine scale 上的 divisor-state，定义

\[
\boxed{
\Gamma_{f\to c}(d)=\gcd(d,c).
}
\]

这会精确删除 coarse scale 不存在的 prime exponents，并把保留的 exponents clamp 到 coarse maxima。

若

\[
c\mid m\mid f,
\]

则标准 gcd absorption 给出

\[
\boxed{
\Gamma_{m\to c}(\Gamma_{f\to m}(d))
=
\Gamma_{f\to c}(d).
}
\]

因此 divisor-grid coarsening 沿 nested scales path independent。

在 isotropic sequence 中，从 `P^(a+1)` coarsen 到 `P^a`，就是把所有 exponent `a+1` clamp 到 `a`。

## 7. Rank opening / contraction 与普通 precision change 不同

prime-axis rank 仍然是 support size

\[
D_{\mathrm{scale}}(\lambda)=\omega(\lambda).
\]

一次 refinement `mu=lambda*r` 满足

\[
\boxed{
D_{\mathrm{scale}}(\mu)-D_{\mathrm{scale}}(\lambda)
=
|\operatorname{supp}(r)\setminus\operatorname{supp}(\lambda)|.
}
\]

因此提高已有 prime exponent 会提高 precision，但不会打开新的 candidate dimension。

反向结论同样重要。coarsening 可以明显降低 precision，却完全不降低 rank。例如

\[
180\to60\to30
\]

始终保持 support `{2,3,5}` 与 rank `3`。而

\[
30\to6\to2\to1
\]

的 rank sequence 是

\[
3\to2\to1\to0.
\]

所以

\[
\boxed{
\text{precision contraction}
\not\Rightarrow
\text{dimension/rank contraction}.
}
\]

未来若把 black-hole-like region 解释成 local precision contraction，就必须证明 coarse dynamics 真正删除了 prime support；只降低 exponent 不够。

## 8. Path-independent rank accounting

由于 refinement 中 support 只做 set union，任意 divisibility path 从 `1` 到 final scale `lambda` 的所有 rank-opening increments 总和都等于

\[
\boxed{\omega(\lambda).}
\]

不同 factorization schedule 可以一次打开多个 new primes，也可以逐个打开，但总量与 path 无关。

反过来，任意 descending divisor path 从 `lambda` 回到 `1`，若在某 prime 最终完全消失的 step 记一次 loss，则总 lost support axes 同样是

\[
\boxed{\omega(\lambda).}
\]

这是 R004 “opening/contraction loop” 当前最干净的数学版本。它只是 scale lattice 上的 rank potential，不构成 cosmological genesis 与 black-hole physics 互为物理对偶的证据。

## 9. Exact finite distance spectrum

对一条 `n` vertices 的 path，定义 ordered-pair distance polynomial

\[
A_n(z)
=n+2\sum_{s=1}^{n-1}(n-s)z^s.
\]

`z^s` 的 coefficient 就是 path distance 为 `s` 的 ordered coordinate pairs 数量。

对 side lengths 为 `n_1,...,n_D` 的 rectangular product grid，exact ordered `L1` pair-distance spectrum 就是

\[
\boxed{
\prod_{i=1}^D A_{n_i}(z)
}
\]

的 coefficient sequence。

因为 coordinate distances 相加、独立 coordinate-pair counts 相乘，所以结论直接成立。R004 executable 只用 finite integer convolution 计算该 polynomial product。

三维 binary cube 的 ordered spectrum 为

\[
(8,24,24,8),
\]

unordered distinct-pair spectrum 为

\[
(0,12,12,4).
\]

## 10. Geometry-driven quantum-to-classical toy crossover

threshold-record bridge 定义

\[
\eta(x,y;d_{\mathrm{rec}})
=
\frac{\max(d_{\mathrm{rec}}-d_G(x,y),0)}{d_{\mathrm{rec}}}.
\]

因此

\[
\eta=0
\iff
 d_G(x,y)\ge d_{\mathrm{rec}}.
\]

在一维 path `P_N` 上，distance 至少为 `d` 的 unordered distinct pairs 数量精确为

\[
\boxed{
Z(N,d)=
\begin{cases}
0,&N\le d,\\
(N-d)(N-d+1)/2,&N>d.
\end{cases}
}
\]

因为 distance 为 `s` 的 unordered pairs 恰好有 `N-s` 个。

固定 positive `d` 时，fraction

\[
Z(N,d)/\binom N2
\]

随 `N` 不下降；可以直接用 exact finite difference 检验，不需要 infinite-size limit。

当 `d=3`，`N=3,4,5,8,16` 时 zero-overlap fractions 精确为

\[
0,\quad 1/6,\quad 3/10,\quad 15/28,\quad 91/120.
\]

通过前述 distance polynomial，同一计算可以推广到 product grids。

对 record resolution `2` 的 three-dimensional isotropic grids，side lengths `1,2,3,4,5` 得到 exact zero-overlap pair fractions

\[
\boxed{
0,\quad 4/7,\quad 11/13,\quad 13/14,\quad 149/155.
}
\]

由于 equal-rank squarefree supports 在 unlabeled exponent grid 上完全相同，这整条 record-crossover sequence 也与具体 prime labels 无关。

这第一次给出一个 exact finite candidate mechanism：geometry expansion 本身会让越来越多 state pairs 落入 complete record distinguishability 区域。它仍只是 toy，因为 threshold-record law 与 physical record resolution 还没有从真实 apparatus/environment interaction 中推导出来。

## 11. 当前最强 R004 candidate

目前最经济的 construction 是：

1. precision one 是 `lambda=1`：一个 divisor state，rank 0；
2. 一次 genesis event 引入 rank `D` 的 squarefree support `P`；
3. 后续 isotropic refinement 使用 `lambda_a=P^a`；
4. divisor Hasse graph 是 nested expanding grid `{0,...,a}^D`；
5. geometry 通过 graph distance 控制 toy environment-record overlap；
6. zero-overlap fraction 可由 finite distance polynomial 精确计算；
7. Bell-locality 与 measurement-independence 仍是独立 causal requirements，不能用 observable no-signalling 代替。

这个 construction 已经消掉了 earlier R004 toys 中多个任意选择，但还有一个决定性问题完全未解决：

> 什么 finite causal law 决定 genesis rank `D`？为什么 physical selected value 恰好是 3，同时还要复现 quantum Bell correlations 与 observed large-scale symmetries？

这比最初的“precision increase creates space”已经窄得多，也更适合真正研究与证伪。
