# P025 补充 111 —— Polynomial Observable Interaction-Order Theorem

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonlinear-observable-stage107`  
依赖：P025 补充 110  
硬阻断：`NONE`

## 1. 一般 polynomial observable

设

\[
P(r)=c_0+c_1r+\cdots+c_dr^d,
\qquad c_d\ne0,
\]

为 degree `d>=0` 的非零 polynomial。

定义 node-rank observable

\[
\boxed{\mathcal O_P:=\sum_jP(r_j).}
\]

threshold/node operation algebra 与 Stage109 common merged-rank generator 都保持不变。

## 2. P025-T254 —— universal upper bound `deg(P)+1`

每个 old-node selected rank 都是 candidate-row selection bits 的 affine function。与 `P` 复合后得到 degree 至多 `d` 的 Boolean polynomial。

每个 future-node term 形如

\[
y_jP\left(R_j+\sum_i x_iC_{ij}\right),
\]

所以 future selector `y_j` 最多再提高一阶。

因此

\[
\boxed{\deg\mathcal O_P(x,y)\le d+1.}
\]

所有 `d+2` 阶及以上 irreducible Boolean finite differences 恒为零。

当 `d=0` 时，candidate-threshold actions 不改变 constant observable，而 future node append 贡献 constant `c_0`，所以 worst-case order 为 `1`。

## 3. P025-T255 —— exact top coefficient

继续使用 exact P025 dyadic edge

\[
\rho_0=\frac1{22}<\frac{13}{22}=\rho_1.
\]

当 `d>=1` 时，在两者之间选择 `d` 个不同 rational candidate thresholds，不设 old thresholds。

old node 位于所有 candidates 下方，future node 位于所有 candidates 上方。于是 selected variables 上

\[
\mathcal O_P=P(0)+yP(x_1+\cdots+x_d).
\]

old constant `P(0)` 在任何 mixed action difference 下都会消失。

对 `d` 个 threshold variables 求差分会消掉所有低于 `d` 次的 polynomial terms，只留下 leading term

\[
\boxed{c_dd!}.
\]

最后对 future-column gate `y` 求差分，所以

\[
\boxed{
\Delta_{x_1}\cdots\Delta_{x_d}\Delta_y\mathcal O_P
=c_dd!\ne0.
}
\]

`d=0` 时，一阶 future-node difference 就是 `c_0`。

## 4. P025-T256 —— exact worst-case order

合并上下界：

\[
\boxed{\operatorname{ord}(\mathcal O_P)=\deg(P)+1}
\]

对每个非零 polynomial `P` 都在 worst case 精确成立。

因此 Stage110 的 moment theorem 只是这个 mother theorem 的特例。

## 5. lower-degree terms 不影响 top interaction

最高阶 coefficient 只由 leading coefficient 决定：

\[
\boxed{\text{top coefficient}=c_dd!.}
\]

lower-degree terms 可以显著改变 lower-order responses，也可能制造 state-relative cancellations，但无法改变 worst-case top order。

例如

\[
P(r)=5-3r+2r^3
\]

的 exact worst-case interaction order 为 `4`，top coefficient 为

\[
2\cdot3!=12.
\]

## 6. observable family 的后果

如果 declared observable family 包含 degree 无界的 polynomials，那么 required response-jet order 也无界，即使：

- operation algebra 固定；
- common merged-rank incidence generator 的类型固定。

所以若不同时限制 observable algebra，就无法给 operation system 配一个 universal finite jet order。

## 7. 架构后果

精确的 future-compatibility contract 不只要声明允许哪些 operations，还必须声明哪些 observable algebra 要保持可预测。

minimum response order 是

\[
\boxed{(\text{operation algebra},\text{observable algebra})}
\]

相对于 generator geometry 的共同性质，而不是 operations 单独的性质。

## 8. Prior-art / novelty 边界

polynomial degree、leading finite differences 与 `c_d d!` coefficient 都是 classical algebra。P025 不单独主张这些结论新颖。

项目侧结果是把这些 classical facts 精确部署为一族 arithmetic precision pressure tests：固定 operation system 与 incidence generator，只改变 observable。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_polynomial_rank_observable.py`；
- `tests/test_abc_polynomial_rank_observable.py`。

## 10. 下一前沿

worst-case degree 并不是每个 state 实际需要的 precision。Stage112 将用 `P` 在 node base old-threshold rank 上的 forward differences，以及该 node 实际跨过的 candidate-threshold 数，精确计算 local interaction order。