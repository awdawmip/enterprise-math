# P025 补充 113 —— Poset Observation Boundary

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-poset-observable-stage113`  
依赖：P025 补充 109–112；canonical A2 future-signature discipline  
硬阻断：`NONE`

## 1. 为什么 Stage 113 改变了几何

Stage 109–112 依赖一条带标签的 threshold 总序。每个 node 上的 active threshold set 因而都是一个 prefix，所以一个 scalar merged rank 就能恢复整列 incidence。

Stage 113 只移除这个假设。令

\[
(P,\le)
\]

为一个有限偏序的 declared-observation family。语义允许的 active set 取为 order ideal：

\[
I\subseteq P,
\qquad
x\in I,\ y\le x\Longrightarrow y\in I.
\]

问题是：当 declared observables 真正出现不可比较方向时，什么对象替代单一 rank？

## 2. P025-T253 —— rank 完备当且仅当 observation poset 是 chain

在有限 ideal lattice \(J(P)\) 上考虑 cardinality observable

\[
q_{\rm rank}(I)=|I|.
\]

则

\[
\boxed{
|I|\text{ 能区分所有 order ideals}
\iff
P\text{ 是一条 chain}.
}
\]

### 证明

若 \(P\) 是含 \(n\) 个元素的 chain，则每个大小

\[
0,1,\ldots,n
\]

都恰有一个 ideal，所以 cardinality 完备。

反之，取任意非 chain 有限 poset 的一个 linear extension。它的所有 prefixes 已经给出 \(n+1\) 个不同 ideals。因为 poset 不是 chain，可选两个不可比较元素 \(x,y\)，且 \(x\) 在 extension 中先于 \(y\)。principal ideal \(\downarrow y\) 包含 \(y\) 却不包含 \(x\)，所以它不可能等于任何包含 \(y\) 的 extension prefix。于是 ideal 总数严格大于 \(n+1\)。而 ideal cardinality 只能取 \(0,\ldots,n\) 共 \(n+1\) 个值，因此必有两个不同 ideals 具有相同大小。

所以，对完整 membership semantics 而言，scalar merged-rank normal form 完备的精确条件就是 observation geometry 为 total order。

## 3. 最小 exact collision

取二元素 antichain

\[
P=\{a,b\},
\qquad a\parallel b.
\]

则

\[
I_a=\{a\},
\qquad
I_b=\{b\}
\]

满足

\[
|I_a|=|I_b|=1,
\]

但对 future query `a 是否 active？` 给出不同答案。

因此 declared observation geometry 一旦不再是 chain，equal merged rank 就不再推出 semantic equality。

## 4. P025-T254 —— maximal-antichain boundary 是 exact state

对任意有限 ideal \(I\)，定义

\[
\boxed{\partial I:=\operatorname{Max}(I).}
\]

则 \(\partial I\) 是 antichain，并且

\[
\boxed{I=\downarrow\partial I.}
\]

而且 \(\partial I\) 唯一。因此有限 order ideals 与 finite antichains 构成一一对应：

\[
\boxed{J(P)\cong\mathcal A(P)}.
\]

这是经典有限偏序理论。P025 这里只保留更窄的 pressure-test 结论：当 total-order rank coordinate 失效后，对完整 ideal-membership semantics 的 exact replacement state 是一个**带标签 antichain boundary**，而不是另一条 scalar precision level。

## 5. Monotone node path

若 node states 单调增长：

\[
I_0\subseteq I_1\subseteq\cdots\subseteq I_h,
\]

写

\[
A_j=\partial I_j,
\]

则整条路径可以仅由 antichain boundaries 表示，并使用 dominance order

\[
A\preceq B
\iff
\downarrow A\subseteq\downarrow B.
\]

等价地，\(A\) 中每个元素都位于 \(B\) 中某个元素之下。

因此 total-order 的 scalar rank path 一般化为 antichain / ideal lattice 中的一条路径。

## 6. 与 A3/A4 的关系

本结果**不**把 A3 relation state 或 A4 admissible support 等同于一个 poset ideal。

它给出的是一条 pressure-test 边界：

- total-order observation incidence → scalar prefix/rank coordinate exact；
- partial-order observation incidence → scalar rank 可以失效；
- full membership semantics → 必须保留 relation-aware labelled boundary data。

A4 已经拥有 finite multivalued support / correspondence algebra。因此 Stage 113 应作为“branching observation geometry 自然产生 support/boundary state”的证据被消费，而不是另造一个与 A4 竞争的 mother theorem。

## 7. Prior-art 边界

order ideals、antichains、linear extensions 与 ideal–antichain bijection 都是标准 poset theory。

P025 不主张这些一般事实新颖。项目侧结果是：它们给出了 Stage109 merged-rank compiler 的精确失效边界，并成为 future-precision pressure test。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 8. 可执行资产

新增：

- `src/enterprise_math/poset_observation_boundary.py`；
- `tests/test_poset_observation_boundary.py`。

executable layer 检查 finite-poset validity、ideal enumeration、rank completeness、exact equal-rank collision、maximal-boundary reconstruction、antichain enumeration 与 monotone boundary dominance。

## 9. 下一前沿

1. 用 poset width 精确计算 worst-case boundary storage；
2. 证明 full membership future 下 antichain-boundary path representation 的 tightness；
3. 研究只询问 selected observables 的 future language，此时可能允许比 full boundary 更粗的 state；
4. 把 resulting MAY/MUST 或 membership projections 与 A4 对接，但不把 multivalued relation 偷换成一个 ideal；
5. 找到 Stage112 state-relative precision 在多条 incomparable observation directions 下的正确 analogue。
