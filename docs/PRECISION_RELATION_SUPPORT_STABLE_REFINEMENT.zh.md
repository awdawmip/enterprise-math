# Relation-Support Stable Refinement 与 Terminal Support Trace 的分界

状态：`RESEARCH BRIDGE / NONCANONICAL`

对 deterministic total / partial actions，“让 operation 在 quotient 上 descend”与“保留所有 future output traces”自然会导向同一个稳定 refinement。对真正 multivalued 的 A4 relation，这两个 semantic requirement 会分开。

本文把这个边界精确化。

## 1. Support-level relation descent

设 X 是有限 state set，`E_0` 是 initial observation equivalence，`{R_a}` 是有限 labelled relation family。

相对于当前 equivalence E，对 source x 定义 quotient-support image：

`B_a^E(x)={ [y]_E : x R_a y }`。

空集合必须原样保留，表示 action a 从 x 没有 admissible target。

当对每个 action a 都满足

`x E y -> B_a^E(x)=B_a^E(y)`

时，称 relation family 对 E **support-stable**。

此时 fine relation 才能直接 descend 成 quotient classes 之间的 relation：一个 source quotient class 的 successor quotient-class set 不依赖 representative。

## 2. Coarsest support-stable refinement

从 `E_0` 开始，在每个 current block 内按

`(B_a^E(x))_a`

继续 split，并反复迭代。

每个 strict round 至少拆开一个 finite block，因此有限终止。

fixed point `E_*` 上，每个 declared relation 都 support-stable。

而且 `E_*` 是 `E_0` 内唯一最大的 support-stable equivalence。

证明与 operation congruence refinement 同类：若 F 已经 refine `E_0` 且对全部 relations stable，则归纳可得 F refine 每一轮 E。因为 F-equivalent states 具有相同的 F-target-class sets，而每个 F-class 都包含在 current E-class 内，所以映射到 E-class 后的 target-set 也一致。最终 F 必 refine fixed point。

这是标准 labelled-transition-system / bisimulation-style partition refinement。

## 3. Total 与 partial deterministic specialization

若每个 source 在 action a 下恰有一个 target：

`B_a^E(x)={ [u_a(x)]_E }`。

refinement 精确退化为 ordinary total-operation congruence refinement。

若每个 source 只有 0 或 1 个 target，则 support 只有两种形式：

`empty`

或

`{target block}`。

这些 support 的相等性正好等价于 FQ-006 的两条要求：

- definedness 一致；
- enabled 时 target quotient class 一致。

所以 total 与 deterministic-partial semantic repair 都是 relation-support stability 的 singleton / empty special cases。

## 4. Terminal observed-support trace semantics 更弱

另一个 future language 可以不暴露 quotient successor classes 本身，只问：

> 对每一个 literal action word w，最终能够到达哪些 observation labels？

这就是 A4 powerset / Boolean-semimodule route 编译的 support-trace language。

若两个 sources 对所有 literal words 都有相同 terminal observed support，就称其 trace-equivalent。

Support-stability 一定推出这种 trace equivalence：对 stable-equivalent sources，可归纳证明任意 word 后到达的 E-class sets 相同，而 E 又 refine initial observation。

因此：

`relation-support-stable precision`

必然细于或等于

`terminal observed-support trace precision`。

但在 multivalued relation 下，反向一般失败。

## 5. 六状态 choice-timing witness

取六个 states：

`p,q,r,s,t,z`，

并让 present observation 完全 constant。

Relation a 表示两种不同的 nondeterministic choice timing：

`p -> r`，

`q -> {s,t}`。

随后：

`r --b--> z`, `r --c--> z`，

`s --b--> z`，

`t --c--> z`。

这就是经典结构：

`p = a.(b+c)`

versus

`q = a.b + a.c`。

在 initial constant partition 上，p/q 都只表现为 action a 有一个 nonempty support 指向同一个 coarse block。

第一轮 support-stability refinement 会拆开 r,s,t,z，因为它们对 b/c 的 enabled support sets 不同。等这些 behavioural classes 出现后，relation a 才暴露：

`B_a(p)={ [r] }`

而

`B_a(q)={ [s],[t] }`，

所以第二轮继续把 p/q 拆开。

## 6. 但所有 terminal support traces 永远合并 p/q

由于 observation constant，terminal observed support 只记录最终 support 是 empty 还是 nonempty。

p 与 q 拥有完全相同的 relevant literal traces：

- a 都 reachable；
- `ab` 都 reachable；
- `ac` 都 reachable；
- fixture 中其他 continuations 的 empty / nonempty 结果也完全一致。

选择 b 或 c 以后，另一个 alternative 已经无法再对**同一个 predecessor branch**查询。因此 terminal language 忘记了 nondeterministic choice 到底发生在 a 之前还是之后。

Boolean-semimodule support compiler 在 exact fixed point 仍然保持 `{p,q}` 合并，而 relation-support stability 会将它们拆开。

这里丢失的是 branching correlation / choice timing，而不是 terminal reachability。

## 7. 这是 future-language difference，不是 contradiction

两个 quotients 回答的是不同问题。

### Trace/support future language

Observable object：

`word -> terminal observation labels 的 union`。

任何不能由一个 word 联合读取的 branching structure 都被有意忘掉。

### Relation-operation language

Observable / executable object：

`source quotient class -> successor quotient classes 的 set`。

若要在 coarse world 中直接运行 multivalued relation，就必须保留 successor behavioural types 与 branching structure 的关联。

因此 relation-stable quotient 合理地可能比 P023 terminal-support quotient 更细。

若不先声明 future operation / observation language，就不存在一个无条件唯一的“最小 relation precision”。

## 8. 与 A4 witness precision 的关系

Support-stability 仍然只保留：**哪些 quotient target classes 出现**。

它仍然忘记：

- 同一 quotient class 内多个 raw targets 的 multiplicity；
- literal path identity；
- target class 内的 provenance/source label；
- aggregate support 存活时到底哪条 branch died；
- per-branch cost / history。

若 future theory 能重新读取这些区别，那么即使 support-bisimulation 也太粗，必须进一步 enrich A4 witness state。

因此存在 task-relative hierarchy：

`terminal observed support trace`

`<= relation target-class support / bisimulation-like state`

`<= richer witness/provenance state`，

而且两个不等号都可能严格。

## 9. Semantic-precision consequence

Partial-operation 路线表明：增加 operation capability 有时可以通过 canonical state splitting 修复。

Multivalued relation 进一步说明：到底需要 split 到哪里，取决于**collapse 后所谓“执行 relation”究竟要求什么 interface**。

若只要求 terminal support traces，可能需要更少 state；若要求 quotient relation 的 target-class support 本身 well-defined，则必须保留更多 branching structure。

所以 semantic capability requirement 不能只写“preserve relation futures”，而必须明确 operation interface。

## 10. Prior-art boundary

Bisimulation、trace equivalence、labelled transition systems、nondeterministic automata 与 partition refinement 都是标准既有数学 / CS。A4 保留 raw correspondence / witness ownership；P023/A2 保留 declared future-signature 与 precision ownership。

这里的项目价值是明确 precision routing：

> **multivalued relation descent 必须保留 successor branching structure，因此可能严格需要比 terminal observed-support trace 更细的 state。**