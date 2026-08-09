# 前人工作边界 —— P018 Predictive Dynamic Closure

状态：`PRIOR-ART NOTE`  
范围：future-observation equivalence、有限确定性状态可区分性、congruence refinement 与最小 dynamically closed quotient

## 成熟邻域

有限确定性机器以及“如何通过 observable behavior 区分内部状态”的问题，在 Moore 的 sequential-machine 框架中已有经典来源；Nerode 的 automaton transformations 以及后续 Myhill–Nerode 谱系，则已经建立了 behavioral congruence 与 minimal quotient automata 的成熟语言。[SRC-MOORE-1956-SEQUENTIAL] [SRC-NERODE-1958-AUTOMATON]

因此 P018 **不主张发明**：

- deterministic states 的 future-output / behavioral equivalence；
- 依据未来 observation 做 partition refinement；
- congruence-compatible quotient dynamics；
- automata 理论意义上的 minimal equivalent finite-state realization；
- behaviorally indistinguishable states 可以 quotient 的一般原则。

## 进取数论特有的研究接口

项目当前关注的问题更窄，且仍为 `NOVELTY_UNVERIFIED`：

> 给定一个显式 finite-precision observation，如果其 kernel 不 dynamically closed，能否把“恢复 exact dynamic closure 所需的最粗 refinement”写成完全有限的 integer/state 构造，并进一步与 P005 typed precision lattice、P009 type-erasure warning、P010 deterministic kernel irreversibility、P011 collision spectra，以及 P018 carry/defect calculus 精确接起来？

Supplement 18 把 classical automata machinery 视为 adopted prior art，只研究这一具体接口。

## Claim discipline

即便 Enterprise Math 的组合最终证明有价值或 unusually compact，在完成专门 novelty review 之前也不提出历史优先权主张。从项目定义出发严格证明的定理可以标记 `PROVED`，但其 novelty status 仍单独保持 `NOVELTY_UNVERIFIED`。
