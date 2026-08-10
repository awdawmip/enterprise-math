# P025 补充 112 —— State-Relative Forward-Difference Jet

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonlinear-observable-stage107`  
依赖：P025 补充 111  
硬阻断：`NONE`

## 1. worst-case degree 不是 realized precision

Stage111 已证明 worst-case theorem

\[
\operatorname{ord}(\mathcal O_P)=\deg(P)+1.
\]

但这不意味着每个 node、每个 state 都需要同样高的 order。

realized local interaction 还取决于：

1. polynomial observable `P`；
2. node 对 always-selected old thresholds 的 base rank；
3. 该 node 实际跨过多少 candidate thresholds。

Stage112 精确计算这一依赖。

## 2. local future-node model

固定一个 future node。

令

\[
R\ge0
\]

为它相对 old thresholds 的 base rank，并假设它恰跨过 `c` 个 candidate thresholds。

把这些 crossed candidates 重标后，selected rank 为

\[
R+x_1+\cdots+x_c.
\]

再乘 future-node selector `y`，该 node 的贡献为

\[
\boxed{yP(R+x_1+\cdots+x_c).}
\]

## 3. P025-T257 —— local coefficients 就是 forward differences

任取 `k` 个不同 crossed candidate variables，monomial

\[
yx_{i_1}\cdots x_{i_k}
\]

的 coefficient 精确等于 `P` 在 `R` 上的 `k` 阶 forward difference：

\[
\boxed{
\Delta^kP(R)
=
\sum_{t=0}^{k}(-1)^{k-t}\binom{k}{t}P(R+t).
}
\]

它与具体选择哪 `k` 个 crossed candidate labels 无关；局部只取决于数量，因为每个 selected threshold 都让 rank 增加 1。

`k=0` 时 coefficient 就是

\[
\Delta^0P(R)=P(R),
\]

对应只有 future-node selector `y` 的一阶项。

## 4. P025-D51 —— realized local action order

若非空，定义

\[
k_*:=\max\{0\le k\le c:\Delta^kP(R)\ne0\}.
\]

则该 node 的 realized action-interaction order 为

\[
\boxed{k_*+1.}
\]

若

\[
\Delta^kP(R)=0
\qquad
\forall\,0\le k\le c,
\]

则该 node 对 declared observable 在所有 locally available candidate selections 下都完全 invisible，realized order 定义为 `0`。

又因为 `k>deg(P)` 时 `Delta^kP=0`，universal local cap 为

\[
\boxed{1+\min(c,\deg P).}
\]

但 finite-difference cancellation 可以让实际 order 严格更低。

## 5. P025-CE45 —— exact cancellation boundary

取

\[
\boxed{P(r)=r(r-1)=r^2-r.}
\]

在 base rank

\[
R=0
\]

处：

\[
P(0)=0,
\]

\[
\Delta P(0)=P(1)-P(0)=0,
\]

但

\[
\boxed{\Delta^2P(0)=2.}
\]

因此：

### 只跨一个 candidate

当 `c=1` 时，可用的 `k=0,1` differences 全部为零，future node 对 observable 完全 invisible：

\[
\boxed{\text{realized order}=0.}
\]

### 同时跨两个 candidates

当 `c=2` 时，nonzero second difference 可被访问，gated future response 立即达到

\[
\boxed{\text{realized order}=3.}
\]

所以同一个 degree-two observable 可以仅因 local crossed-candidate geometry 改变，就从 zero response 直接跳到 cubic response。

## 6. exact P025 arithmetic realization

仍使用 `(q,p,m)=(3,41,2)` 的 exact dyadic edge

\[
\frac1{22}<\frac{13}{22}.
\]

不设 old thresholds，因此 future node base rank `R=0`。

- 在两 pressures 之间放 1 个 candidate threshold：`c=1`，对 `P(r)=r(r-1)` realized order 为 `0`；
- 在同一区间放 2 个不同 candidates：`c=2`，realized order 为 `3`。

所以 cancellation boundary 在同一个 arithmetic transition 内精确实现。

## 7. base rank 也会改变 order

同一个 polynomial 在

\[
R=1
\]

时：

\[
P(1)=0,
\qquad
\Delta P(1)=P(2)-P(1)=2.
\]

所以只跨一个 candidate 时 realized order 已变成

\[
\boxed{2.}
\]

observable 与 crossed-candidate count 都没变，只改变 base old-threshold rank，就改变了 required precision。

## 8. state-relative precision law

Stage112 因而把 coarse worst-case rule

\[
\deg(P)+1
\]

替换成 exact local rule

\[
\boxed{
\operatorname{ord}_{\rm local}(P;R,c)
=
1+\max\{k\le c:\Delta^kP(R)\ne0\},
}
\]

当所有 available differences 都为零时取值 `0`。

required local response order 由

\[
\boxed{(\text{observable},\text{current base state},\text{available action geometry})}
\]

共同决定。

## 9. 架构后果

precision system 不应在所有位置均匀实例化 observable 的 worst-case order。

observable degree 只决定 ceiling；实际 state 只应激活那些：

- 在 current base rank 上 nonzero；
- 同时又被 candidate-action geometry 可达

的 forward-difference orders。

这是一个 exact algebraic **precision genesis by local future distinguishability** 模型。

## 10. Prior-art / novelty 边界

polynomial forward differences 与 local cancellation 都是 classical discrete calculus。P025 不单独主张这些结论新颖。

项目侧结果是把它们精确编译成 arithmetic threshold/node pressure-test geometry 上的 state-relative precision law。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_local_observable_jet.py`；
- `tests/test_abc_local_observable_jet.py`。

## 12. generation boundary

Stages107–112 已形成完整链条：

1. 改变 observable 可以强迫 state refinement；
2. quadratic observable 把 closure order 从二阶提高到三阶；
3. high-order response 仍来自 low-dimensional common rank generator；
4. rank moments 实现任意 finite interaction order；
5. 任意 polynomial observable worst-case order 为 `deg(P)+1`；
6. realized order 则由 forward differences 与 reachable geometry 在 local state 上决定。

这里是自然 freeze point。下一 generation 应转向 non-polynomial observables 或 non-total-order relation geometries。