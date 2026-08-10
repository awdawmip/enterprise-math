# 先行工作——R004 typed generator basis

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

补充 15 研究的是：完整 typed Representation Compiler 已经生成 target safe carrier 之后，怎样寻找 task-relative generator basis。generic minimum generating set、semigroup rank、hitting set/set cover、term generation、semiring generation 都属于成熟先行数学。

## 1. 有限 semigroup rank / minimum generating set 是 prior art

Gray 研究有限 semigroup 的最小 generator 数，并把结果应用到自然 transformation-semigroup families [SRC-GRAY-2013-FINITE-SEMIGROUP-RANK]。

Araújo、Bentz、Mitchell、Schneider 进一步研究稳定一个有限 partition 的 transformation semigroup，并求其 rank / minimum generating-set size [SRC-ARAUJO-BENTZ-MITCHELL-SCHNEIDER-2014-PARTITION-SEMIGROUP-RANK]。

因此 R004 不把 minimum transformation generating set、semigroup rank、partition-stabilising transformation semigroup 等概念当成新发明。

## 2. Hitting set 与 algebraic generation 是 generic priors

“从 generators 中选最小子集去命中全部 forbidden objects”直接就是有限 hitting-set/set-cover 形式。generic exact/approximate algorithms 与 complexity theory 都是成熟组合数学/计算机科学，不属于当前 novelty claim。

同样，判断 quotient operation 是否属于某 transformation monoid，或者 relation matrix 是否属于某 generated semiring subalgebra，都属于普通 algebraic generation。补充 15 只是把这些成熟对象作为 Enterprise Math compiler 内的 reconstruction certificates。

## 3. 当前 project-local WIP additions

R004 只保留以下组合包：

1. 完整 compiler 得到 `Q*` 后，用“命中 `Q*` 与 initial observation 之间所有严格更粗 forbidden partitions”精确刻画 carrier-preserving generator subset；
2. 用 pairwise-merge no-go 证明 basis synthesis 是 global partition-structural，而不是局部 pair 检查；
3. 区分 carrier basis 与 semantic reconstruction basis；
4. 证明 coarsening-natural reconstruction criterion：遗漏 typed generator 在 quotient 上可重建会推出 carrier redundancy；
5. 分别 specialize 到 unary operation-term/transformation-monoid generation、semiring relation generation、semantic factor map；
6. 给出完全整数的 inclusion-minimal/private-world 与 generator-disjoint packing certificates；
7. 延续 R004 既有边界：class/basis cardinality 只是 derived statistic，不是完整 typed-precision coordinate。

这套 Enterprise Math placement 与选定有限 reduction/counterexample package 的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。
