# R004 精度起源——补充 24：certificate 的 backward semantic liveness

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + P023_RECURSIVE_SPECIALIZATION`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_23.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 23 已给出 typed certificate composition 与 safe demotion 规则。下一问题是：在 staged future program 中，一个 strong certificate distinction 究竟要保持多久。本补充证明不需要新的 minimization theory：certificate state 自己就是另一个有限 carrier，可以再次使用 P023 future-safe quotient 原理。

## 1. Deterministic staged certificate program

考虑 staged deterministic program

`C_0 --f_0--> C_1 --f_1--> ... --f_(n-1)--> C_n`。

reference implementation 先取各 certificate carrier 相同有限大小。每个位置 i 有 typed observation `o_i`，表示剩余程序在该点真正需要暴露的语义。

从后向前定义 complete suffix signature：

`Sigma_n(c)=o_n(c)`，

`Sigma_i(c)=(o_i(c),Sigma_(i+1)(f_i(c)))`。

令

`Theta_i=ker Sigma_i`。

则 `C_i/Theta_i` 正好是该程序位置上供整个剩余 suffix 使用的**唯一最粗 exact certificate quotient**。

这就是 P023 已有 deterministic future-signature construction 在 certificate carrier 上的递归使用，不是新 mother theorem。

## 2. 不存完整 suffix word 的 backward recurrence

设 `P_(i+1)` 为 `Theta_(i+1)` classes。位置 i 的两个 certificate states c,c' 可以合并，当且仅当

`o_i(c)=o_i(c')`

且

`f_i(c),f_i(c')`

落在同一个 `P_(i+1)` class。

因此最小 partition 可通过单步 backward recurrence 计算：

`P_i=ker(c |-> (o_i(c),[f_i(c)]_(P_(i+1))))`。

不需要显式 materialize 指数长度的 suffix word。

## 3. Exact erasure gate

若 compiler 考虑候选 certificate erasure

`e_i:C_i->D_i`，

它在位置 i 安全，当且仅当 e_i collapse 的每一对 states 对剩余 suffix 都不可区分：

`ker e_i subseteq Theta_i`。

等价地，e_i induced partition 必须 refine `P_i`。

若 gate 失败，存在 exact counterexample pair

`e_i(c)=e_i(c')`

但

`Sigma_i(c)!=Sigma_i(c')`。

compiler 可以直接返回该 pair，解释“为什么现在还不能降级”。

## 4. Semantic last use

certificate distinction 在位置 i **live**，当且仅当 erase 它会合并某一对仍被 `Theta_i` 区分的 states。

因此 strong certificate 不能因为“以后某个时刻 weaker type 已经够用”就从程序开始处直接降级。正确做法是保留到最后一次 future-sensitive use，之后立即 collapse。

最小例子：certificate state 是 `{0,1,2}` 中的 witness count。在 exact-count observation 之前，suffix partition 必须 discrete；最后一次 exact-count use 之后，如果剩余 future 只问 MAY/nonzero support，suffix partition 就变成

`{{0},{1,2}}`。

所以 COUNT -> MAY 的正确 demotion point 正好是最后一个 count-sensitive use 之后。

同一规则适用于 richer certificates：

- future extension/composition 还需要 module presentation 时继续保留；若以后只问 resource mass，可降成 exponent profile；
- future exterior-field replacement 仍依赖 A3 projective direction 时继续保留 direction；若以后只做 capacity budget，可降成 rank/profile；
- future composition 仍使用 witness identity 时保留 labels；所有 label-sensitive stages 结束后才降成 MAY。

## 5. 没有新信息就不能 semantic resurrection

若 erasure e 已把两个具有不同剩余 suffix signature 的 certificate states 合并，那么任何只接收 `e(c)` 的 deterministic downstream computation 在两种情况中得到完全相同输入，无法恢复原 distinction。

这不是独立 novelty claim，而是 future-safe quotient / factorization 的普通 no-resurrection 内容。

以后若出现 stronger certificate，只能因为某一步真的注入了新 side information，或提供了 explicit reconstruction witness。automatic demotion 永远不能授权 automatic upward lift。

## 6. Forward world synthesis / backward certificate liveness

Representation Compiler 现在出现一个有用的方向分工。

### Forward

从 exact world state 与 declared future language 出发，做 stabilization/refinement，得到 minimal safe carrier。

### Backward

从 terminal/staged future requirements 出发，把 suffix distinctions 向前驱位置 pull back，决定每个 program point 仍然 live 的 certificate structure。

二者不是竞争算法，而是同一 future-compatibility principle 在不同 carrier 上的两次使用。

## 7. Validation

Independent exhaustive checks 使用三状态 certificate carrier 与全部 deterministic two-stage programs：

- stage functions 共 `27^2` 对；
- set-partition-valued observations 共 `5^3` 组；
- 总计 **91,125** 条完整 staged programs。

每个 program point 上，backward recurrence partition 与 literal complete suffix signatures 产生的 partition 完全一致。

随后在每个位置测试全部 candidate erasure partitions，共 **1,366,875** 个 erasure checks；

`ker e subseteq Theta_i`

与 literal suffix-signature safety 逐例完全等价，0 mismatch。

这些是 finite exact WIP checks，不是 fresh full-repository CI 或 canonical-main claims。

## 8. Ownership 与下一 frontier

Generic future-safe quotient / suffix indistinguishability 仍归 P023。R004 当前只增加 certificate-state recursive compiler specialization、explicit last-use semantics 与 staged witness extraction。

下一步要把 backward liveness 与 generator obstruction clutter 真正接起来：每个 program point 的 live suffix quotient 都会诱导 primitive generators 上的 monotone **suffix adequacy predicate**。真正困难的是：suffix 不断缩短时，minimal generator cuts 是否能增量更新，从而产生 dynamic instruction-retirement schedule，而不是每个位置重新枚举完整 cut hypergraph。
