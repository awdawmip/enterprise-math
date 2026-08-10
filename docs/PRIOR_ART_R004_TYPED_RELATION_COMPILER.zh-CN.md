# R004 typed relation compiler —— prior art 边界

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

本说明限制 Supplement 13 的 novelty claim。一般 stable-partition / weighted-bisimulation 数学属于 prior art。R004 只研究 typed Enterprise Math compiler 的放置方式、有限 exact specializations，以及 total-operation 与 quotient-relative relation 在组合任务上的分界。

## 1. Coalgebraic partition refinement 是 prior art

Wißmann、Dorsch、Milius、Schröder 给出了 generic coalgebraic partition refinement，可覆盖 classical relational systems、weighted systems、deterministic automata、Markov/Segala 类系统和 color refinement [SRC-WISSMANN-DORSCH-MILIUS-SCHROEDER-2018-COALGEBRAIC-REFINEMENT]。

Deifel、Milius、Schröder、Wißmann 又对 weighted / weighted-tree-automata 情形推进了 generic method，包括 cancellative 与 non-cancellative monoid weights [SRC-DEIFEL-MILIUS-SCHROEDER-WISSMANN-2018-WEIGHTED-REFINEMENT]。

因此 R004 不主张 generic partition refinement、behavioural minimization 或 monoid-weighted refinement algorithm 为项目发明。

## 2. Weighted transition / bisimulation semantics 是 prior art

Miculan 与 Peressotti 研究了 transition weights 取值于 commutative monoid 的 weighted labelled transition systems，并发展 weighted bisimulation machinery [SRC-MICULAN-PERESSOTTI-2013-WEIGHTED-BISIMULATION]。

因此 `source -> aggregate of weights into an equivalence block` 属于成熟 weighted-transition semantics 家族。

## 3. Monoid-weighted balanced network partition 是直接 prior art

Sequeira、Aguiar、Hespanha 使用 commutative-monoid matrices 描述 weighted coupled-cell networks，把 invariant synchrony / balanced-partition 结果推广到 weighted setting，并给出 coarsest invariant refinement algorithm [SRC-SEQUEIRA-AGUIAR-HESPANHA-2021-MONOID-NETWORKS]。

这一方向与 R004 finite block-aggregate implementation 很接近，所以项目不能把“commutative monoid relation compiler”包装成新的 abstract mathematics。

## 4. Balanced-equivalence lattice 是 prior art

Kamei 与 Cock 计算 coupled-cell networks 的 balanced equivalence relations，并明确描述其 hierarchy 为 complete lattice [SRC-KAMEI-COCK-2012-BALANCED-LATTICE]。

因此 stable/balanced equivalences 形成 lattice、stable meet 可能需要 closure/refinement 而不是朴素 set-partition intersection，并不是 Enterprise Math 新数学。

## 5. Total-operation congruence intersection 是成熟代数

total algebra 的 compatible equivalence relations 是 congruences，任意 congruence intersection 仍是 congruence。R004 的 `raw meet` 对照只消费这一标准事实，并把 mother operation-quotient interface 留给 A2/P023。

## 6. 当前 project-local package

R004 Supplement 13 只把以下 package 作为项目级 WIP：

1. 在既有 future-language compiler 中把 relation semantics 明确类型化为 MAY、witness COUNT、witness LABEL-SET 及其 products；
2. 用 monoid factor map 作为一个 semantic quotient 必然 refine 另一个的 exact sufficient certificate；
3. 给出同 class count 但 COUNT/LABEL-SET partitions 不可比较的例子，证明 scalar class count 不是完整 relation-precision coordinate；
4. 区分 total-operation composition（congruence raw meet）与 quotient-relative relation aggregation（stabilize raw meet）；
5. 给出 3-state two-channel semantic-activation cascade 与 5-state same-channel raw-meet failure，并做 bounded minimality checks；
6. 把 generic mother mathematics 回流 P023/A4，不建立重复基础层。

这套 exact packaging 与所选 finite witnesses 的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。
