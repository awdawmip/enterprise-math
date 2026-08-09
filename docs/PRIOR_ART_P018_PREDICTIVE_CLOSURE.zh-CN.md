# 前人工作边界 —— P018 Predictive 与 Contextual Closure

状态：`PRIOR-ART NOTE`  
范围：future-observation equivalence、有限确定性状态可区分性、代数 congruence、syntactic/contextual congruence、quotient algebra、congruence refinement 与最小 exact quotient state

## 成熟邻域

有限确定性机器以及“如何通过 observable behavior 区分内部状态”的问题，在 Moore 的 sequential-machine 框架中已有经典来源；Nerode 的 automaton transformations 以及后续 Myhill–Nerode 谱系，则已经建立了 behavioral congruence 与 minimal quotient automata 的成熟语言。[SRC-MOORE-1956-SEQUENTIAL] [SRC-NERODE-1958-AUTOMATON]

多元运算的一般化属于经典 universal algebra。标准 congruence 与 quotient algebra 都是成熟工具；Burris 与 Sankappanavar 的教材提供了标准参考。[SRC-BURRIS-SANKAPPANAVAR-1981-UA]

更直接地，Słomiński 已研究“任意 equivalence relation 内所包含的最大 congruence”；Clark、Davey、Freese 与 Jackson 将同一对象表述为 syntactic congruence `Syn(theta)`，明确指出它是 `theta` 内最大的 algebra congruence，并发展了 term/context 判据。[SRC-SLOMINSKI-1974-GREATEST-CONGRUENCE] [SRC-CLARK-DAVEY-FREESE-JACKSON-2004-SYNTACTIC]

因此 P018 **不主张发明**：

- deterministic states 的 future-output / behavioral equivalence；
- 依据未来 observation 做 partition refinement；
- algebra congruence 与 quotient algebra；
- “识别关系与 operation compatible 时 quotient operation 才 well-defined”的一般判据；
- one-hole term / polynomial context 与 elementary translation 作为 congruence 判据；
- 任意 equivalence 内最大的 congruence；
- syntactic congruence 或 term-context indistinguishability；
- automata 理论意义上的 minimal equivalent finite-state realization；
- behaviorally / algebraically indistinguishable states 可以 quotient 的一般原则。

## 进取数论特有的研究接口

项目当前关注的问题更窄，且仍为 `NOVELTY_UNVERIFIED`：

> 给定一个 finite-precision observation，如果它的 kernel 并不对该 precision state 需要支持的 operations 闭合，能否把“恢复 exact operation closure 所需的最大 compatible refinement”写成完全有限的 integer/state 构造，同时给出显式停止界与信息量界，并与 P005 typed precision、P009 type-erasure warning、P010/P011 irreversibility observables 以及 P018 carry/defect calculus 精确接起来？

Supplement 18 把 unary deterministic 情形视为 adopted Moore/Nerode-style behavioral refinement。Supplement 19 则采用 universal-algebraic syntactic-congruence machinery，研究有限 finitary operation signature 下的 finite-precision 后果与 exact information accounting。

## 关于 carry 的重要边界

Universal algebra 回答的是：为了 exact operation descent，**哪些 state distinctions 必须保留**。它并不意味着所有高效实现或 transport law 都必须用同一种方式存储完整 refinement label。

对于 radix quotient addition，P018 另行研究 exact remainder/carry representation。“任意 exact addition 下完整 remainder 是最小 per-state detail”可以从 contextual distinguishability 推出；而 carry 本身仍是 operand detail 保留之后导出的 interaction / transport 项。这个区分既避免把普通 congruence theory 错标成新的 cocycle theory，也避免把 carry cocycle 机械推广到所有 operation signature。

## Claim discipline

即便 Enterprise Math 的组合最终证明有价值或 unusually compact，在完成专门 novelty review 之前也不提出历史优先权主张。从项目定义出发严格证明的定理可以标记 `PROVED`，但其 novelty status 仍单独保持 `NOVELTY_UNVERIFIED`。
