# P025 补充 142 —— Helper validity 相对于 future operation envelope

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-helper-cache-stage139`

## 1. Current correctness 与 future robustness

一个 stale helper 不一定会立刻破坏**当前** raw endpoint。它是否危险，取决于未来还允许执行哪些 raw operations。

对 sequential k-way compiler，helper `e_j` 在语义上证明 raw prefix

\[
P_j=\{a_1,\ldots,a_j\}.
\]

若每个当前为真的 helper 都满足

\[
\boxed{e_j\in T\Rightarrow P_j\subseteq\pi(T),}
\]

则称 internal state **prefix-valid**。

## 2. Stale state 可以当前 harmless

在四元 compiler 中取

\[
T=\{e_2\}.
\]

这个 helper 是 stale，因为 `a_1,a_2` absent。但当前 saturation 仍无法到达 `z`，因为 `a_3,a_4` 也 absent。所以当前 raw projection 仍然正确。

现在允许 future raw operation 加入

\[
\{a_3,a_4\}.
\]

stale `e_2` 会绕过缺失 prefix，生成 `e_3`，再生成 `z`；而 pure raw conjunction 仍缺少 `a_1,a_2`，因此 future 结果错误。

所以

\[
\boxed{
\text{current endpoint safety}\not\Rightarrow\text{future robustness}.
}
\]

## 3. 精确 robustness 定理

假设 raw projection 中 `z` 尚未为真。则 sequential-helper internal state 对**任意未来 monotone raw antecedent additions** 都保持 pure raw closure，当且仅当它 prefix-valid：

\[
\boxed{
\text{robust under all raw additions}
\iff
\forall j,\ e_j\Rightarrow(a_1\wedge\cdots\wedge a_j).
}
\]

### 充分性

若每个 retained helper 都证明其完整 raw prefix，那么每条 internal rule

\[
e_{j-1}a_j\Rightarrow e_j
\]

都会保持这一性质。因此最终能推出 `z` 就意味着全部 raw antecedents 已存在，精确匹配 pure raw closure。

### 必要性

若某个 `e_j` 已存在但 prefix 中仍缺少某个 antecedent，则未来加入全部 suffix antecedents `a_(j+1),...,a_k`，同时保持缺失 prefix 不变。helper chain 将到达 `z`，而 pure raw conjunction 仍为 false，所以该 state 不 robust。

如果 raw `z` 已经存在，那么对这个特定 raw-output future 而言 helper staleness 不可见，因为 helper rules 不会再添加其他 raw label。因此完整条件是

\[
\boxed{
z\in\pi(T)\quad\text{或}\quad\text{prefix-validity}.}
\]

## 4. Legality 是 operation-language-relative

同一个 internal state 因此可能：

- 对 future language `只读取当前 raw endpoint` 合法；
- 对更强 future language `允许以后任意增加 raw antecedents，再读取 endpoint` 非法。

所以 legality 不是 state representation 单独的属性，而是

\[
\boxed{
\text{internal state}
\times
\text{allowed future operations}
\times
\text{declared observables}
}
\]

之间的兼容关系。

## 5. 架构后果

Stage 138 的 admissible-state invariant 本身也必须按 future operation envelope 索引。future 变强时，即使 raw observable 与 internal coordinate set 完全不变，也可能必须强化 hidden-state validity invariant。

这是 P023/P024 future-compatible quotient 逻辑在 hidden-state 层的精确对应。

## 6. 前人工作边界

cache validity predicates、inductive invariants 与 input extensions 下的 robust safety 都是经典 verification 思想。这里不主张 generic novelty。P025 提供 exact iff 边界，以及 `currently harmless` 严格弱于 `safe for declared future` 的 counterexample。
