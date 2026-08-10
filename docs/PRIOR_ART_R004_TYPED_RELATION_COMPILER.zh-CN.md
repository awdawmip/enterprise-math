# 先行工作——R004 typed relation 与 mixed dispatcher

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED / CORRECTED`

本文约束补充 13–14 的 novelty 边界。一般 stable-partition、congruence、weighted/semiring transition 与 fixed-point refinement 都属于成熟先行数学。R004 当前只保留 typed Enterprise Math placement、精确有限 specializations、纠错/counterexample package 与 P023/A3/A4 interface reduction。

## 1. Coalgebraic partition refinement 与 modular system combination 是 prior art

Wißmann、Dorsch、Milius、Schröder 已给出 generic coalgebraic partition refinement，覆盖 relational、weighted、deterministic、probabilistic、color-refinement systems，并允许 modular combination of system types [SRC-WISSMANN-DORSCH-MILIUS-SCHROEDER-2018-COALGEBRAIC-REFINEMENT]。

Deifel、Milius、Schröder、Wißmann 又在 weighted / weighted-tree-automata setting 下细化这一 generic 方法，包括 cancellative 与 non-cancellative monoid weights [SRC-DEIFEL-MILIUS-SCHROEDER-WISSMANN-2018-WEIGHTED-REFINEMENT]。

因此 R004 不把 generic mixed partition-refinement algorithm、modular transition-type compiler、behavioural minimization 或其 complexity theory 当成新发明。

## 2. Weighted / semiring transition semantics 是 prior art

Miculan 与 Peressotti 研究 semiring/commutative-monoid weighted labelled transition systems 与 weighted bisimulation [SRC-MICULAN-PERESSOTTI-2013-WEIGHTED-BISIMULATION]。

所以 monoid block aggregation、Boolean reachability、path-count semantics、semiring relation composition 都处在成熟 weighted-transition 数学范围内。R004 的 semiring quotient 计算只是 finite descent certificate，不宣称新的 abstract algebraic structure。

## 3. Monoid-weighted balanced partition 与 stable lattice 有直接 prior art

Sequeira、Aguiar、Hespanha 使用 commutative-monoid matrices 研究 weighted coupled-cell networks、invariant synchrony/balanced partitions 和 coarsest invariant refinement [SRC-SEQUEIRA-AGUIAR-HESPANHA-2021-MONOID-NETWORKS]。

Kamei 与 Cock 计算 balanced equivalence relations 及其 complete-lattice structure [SRC-KAMEI-COCK-2012-BALANCED-LATTICE]。

因此 stable relation partitions 存在 closure/refinement operator，以及 lattice combination 可能需要 re-stabilization，都不是 Enterprise Math 的 generic novelty。

## 4. Congruence 与 fixed-point machinery 是成熟数学

固定一个 total algebra 时，compatible equivalence relations 就是 congruences，而 congruences 对 intersection 封闭。因此补充 14 的 fixed-operation-family observation meet law 是标准 universal algebra。

有限 monotone/idempotent closure operators、fair/chaotic fixed-point iteration、worklist convergence 也都是成熟 order-theoretic / program-analysis patterns。R004 不宣称 abstract least-common-fixed-point mechanism 的历史原创性。

Partial-algebra congruence / quotient theory 同样已有先行工作。R004 的 one-bottom totalization 只作为“definedness + output class”的 quotient-compatibility encoding；不宣称 one-point extension 可以保留任意 partial algebra 的全部 algebraic laws。

## 5. 对补充 13 第一版边界的纠正

补充 13 第一版把“operation raw meet”与“relation stabilization”对照得过强。正确边界是：

- **固定 operation family、改变 observations**：compatible-congruence closure 保留 raw observation intersection；
- **不同 operation families**：分别 closure 后仍可能 cross-activate，必须求 common fixed point；
- **固定 quotient-relative relation channel**：甚至两个 stable partitions 的 raw common refinement 都可能不 stable。

补充 14 给出 4-state different-operation counterexample 与任意长度 two-operation ping-pong family，因此这次纠正有 theorem/counterexample 支撑，不是措辞调整。

## 6. 当前 project-local WIP additions

R004 只保留下列 project-local package：

1. MAY / COUNT / LABEL-SET typed semantics 与 semantic factor-order certificates；
2. equal-cardinality 但不可比较的 typed safe partitions，否定 scalar class count 作为完整 precision coordinate；
3. relation/relation 与 operation/operation finite activation-cascade witnesses；
4. 把 P023/A3/A4 owner semantic closures 组织成 least common fixed-point dispatcher；
5. 把 legality 编码为 tagged quotient-compatibility obligation；
6. 把 semiring relation quotient map 用作 finite composition/path syntax 的 generator-level descent certificate；
7. finite-generator-basis architecture：编译 generators，再证明 algebraic closure，而不是枚举全部 future expressions；
8. executable finite examples 内继续保持 integer/fractionless internal state。

这套 Enterprise Math packaging 的 historical novelty 仍为 `NOVELTY_UNVERIFIED`。
