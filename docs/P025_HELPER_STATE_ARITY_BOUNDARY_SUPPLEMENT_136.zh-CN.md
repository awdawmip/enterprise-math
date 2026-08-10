# P025 补充 136 —— Premise arity、derivation depth 与 auxiliary state 是三个独立资源

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-closure-basis-stage130`

## 1. Pure k-way raw closure

固定 raw labels

\[
a_1,\ldots,a_k,z,
\qquad k\ge2,
\]

并令唯一非平凡 semantic consequence 为

\[
\boxed{
a_1\wedge\cdots\wedge a_k\Rightarrow z.
}
\]

等价地，exact states 是所有 subsets，但排除“包含全部 `a_i` 却不包含 `z`”的那些状态。

## 2. Fixed-alphabet 定理

对这个 closure，完整 rooted-circuit table 恰好只有一条非平凡 circuit：

\[
\boxed{
\{a_1,\ldots,a_k\}\Rightarrow z.
}
\]

不存在以任何 antecedent `a_i` 为 root 的 sound 非平凡规则，因为 closure 从不生成 raw antecedents。任何加入 `z` 的 sound rule，其 premise 必须已经在语义上强迫 `z`；又因为 `z` 不能出现在自己的 premise 中，所以 premise 必须包含全部 raw antecedents。

因此在**固定 raw alphabet** 上，任意 sound complete single-head implication basis 都必须包含一条 premise arity 为 `k` 的规则。

允许更多 forward-chaining rounds 也没有帮助：在 `z` 出现以前，没有任何新的 semantic label 可以被生成并充当中间 consequence。

所以

\[
\boxed{
\text{fixed alphabet}\quad\Longrightarrow\quad
\text{对任意 derivation-depth budget，required max premise arity}=k.
}
\]

## 3. Auxiliary-state compilation

现在把 internal alphabet 扩展为额外包含 helper labels

\[
e_2,\ldots,e_{k-1},
\]

并使用 Stage 135 的 binary chain

\[
a_1a_2\Rightarrow e_2,
\quad
 e_{j-1}a_j\Rightarrow e_j,
\quad
 e_{k-1}a_k\Rightarrow z.
\]

从任何只含 raw labels 的 seed 出发，在扩展系统中 forward chaining，再投影回 raw alphabet，得到的结果**精确等于上面的 pure k-way closure**。

内部资源为

\[
\boxed{
\#\text{helpers}=k-2,
\qquad
\max\text{ premise arity}=2,
\qquad
\text{raw-seed depth}=k-1.
}
\]

因此 binary compilation 确实可能，但它购买的是 auxiliary state 加 derivation depth。

## 4. 对 Stage 135 的正确解释

Stage 135 不能被读成：

> 只要增加 depth，就总能降低 relation-law arity。

正确表述是：

> 当 runtime 被允许引入并保留合适的 intermediate state 时，高 arity direct law 有时可以编译成更低 arity 的 iterative laws。

若没有 auxiliary semantic/scratch coordinates，一些高 arity laws 在任意 depth 下仍保持不可约的高 arity。

## 5. 三轴 law compiler

relation-law representation 至少具有资源向量

\[
\boxed{
(\text{max premise arity},
\text{derivation depth},
\text{auxiliary-state dimension}).
}
\]

它们独立于 raw semantic closure 本身。compiler 可以在保持 declared raw future language 投影不变的前提下，在这个资源 frontier 上移动。

这也进一步区分了 **semantic state precision** 与 **internal computational state**：implementation 保存 helper labels，并不意味着这些 helpers 必须暴露成用户层 observable。

## 6. 前人工作边界

auxiliary gates、Tseitin-style/intermediate variables、Horn compilation 以及 circuit depth/arity tradeoff 都是经典对象。这里不主张 generic novelty。项目侧结果是精确的假设边界：它阻止对 Stage 135 作错误推广，并把三个资源明确纳入 precision accounting。
