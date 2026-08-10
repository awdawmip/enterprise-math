# P025 补充 143 —— Helper provenance 在 runtime 单向，在 saturation 变为双向

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-helper-cache-stage139`

## 1. Global validity 可以局部化

Stage 142 对 sequential compiler 的 future-robust validity 条件为

\[
e_j\Rightarrow(a_1\wedge\cdots\wedge a_j).
\]

由于 helper `e_j` 递归构造，这个高 arity 条件精确等价于 local provenance laws：

\[
\boxed{e_2\Rightarrow a_1,\quad e_2\Rightarrow a_2,}
\]

以及对 `j>=3`，

\[
\boxed{e_j\Rightarrow e_{j-1},\quad e_j\Rightarrow a_j.}
\]

沿 helper chain 向下归纳即可恢复完整 raw prefix；反过来 global prefix condition 也立即推出每一条 local dependency。

所以 auxiliary topology 不只局部化 forward computation law，也局部化 cache-validity law。

## 2. 所有合法 reachable states 都 provenance-sound

helpers 初始 absent，并且只能通过

\[
a_1a_2\Rightarrow e_2,
\qquad
 e_{j-1}a_j\Rightarrow e_j
\]

生成。raw 与 helper labels 一旦出现就保持单调。因此任何合法 reachable transient state 中出现的 helper，都必然同时携带自己的 prerequisites。

所以每个合法 reachable state 都满足上述 local provenance implications。

## 3. Runtime 中反方向可以失败

执行过程中 converse 不一定成立。

例如 raw seed

\[
\{a_1,a_2,a_3\}
\]

在第一轮后已经有 `e_2`，但 `e_3` 还没生成。因此

\[
e_2\wedge a_3
\]

为真，而

\[
e_3
\]

仍为假。

所以 runtime legality 只要求

\[
\boxed{
e_j\Rightarrow(e_{j-1}\wedge a_j),
}
\]

而不要求 converse。

## 4. Saturation 加入 cache completeness

到达合法 saturated endpoint 后，所有 enabled helper rules 都已经触发。因此对 helpers 有

\[
\boxed{
e_2\iff(a_1\wedge a_2),
}
\]

以及

\[
\boxed{
e_j\iff(e_{j-1}\wedge a_j)
\qquad(j\ge3).
}
\]

等价地，endpoint cache 同时满足：

- **sound**：每个被保存的 helper 都有合法 provenance；
- **complete**：每个已经满足 local prerequisites 的位置都 materialize 了 helper。

## 5. Relation-law phase transition

同一批 internal coordinates 在不同 future phases 下服从不同的 exact relation type：

- transient/runtime state：单向 provenance implication；
- saturated endpoint state：local biconditional / cache equality。

这不是矛盾，因为 saturation 本身就是额外的 future condition。

## 6. Precision 后果

helper tree 同时购买了两种局部化：

1. high-arity forward computation 被编译成 low-arity local rules；
2. global validity certificate 被编译成 low-arity local provenance rules。

但代价仍然是 auxiliary state 加 lifecycle/runtime contract。若不说明 state 是 transient 还是 saturated，就不能完整指定这些 coordinates 所服从的 law。

## 7. 前人工作边界

data provenance、inductive invariants、materialized views 与 fixpoint completion 都是标准对象。这里不主张 generic novelty。P025 提供的是当前 precision architecture 内的 exact phase-dependent law boundary。
