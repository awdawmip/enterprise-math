# P025 补充 147 —— Eventual completion 是 scheduler contract 的性质

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-fairness-stage147`

## 1. 设置

沿用 Stages 144–146 的 asynchronous helper-progress ideal system。合法状态是有限 helper dependency poset 的 ideal

\[
I\in J(P_{gate}).
\]

每个 helper 最多触发一次。任意 nonterminal ideal 都至少有一个 enabled helper：取其 complement 中的一个极小元素即可。

现在对同一个 completion proposition 比较三种 scheduler contracts。

## 2. MAY-complete

询问：

> 是否存在一条合法 scheduler execution，最终完成全部 helpers？

对任意 ideal `I`，不断选择任意一个 enabled helper。每次 firing 都严格扩大 ideal，而 helper 集有限，因此从任意状态都存在一条 completion execution：

\[
\boxed{\operatorname{MAY\_complete}(I)=\mathrm{true}\quad\forall I.}
\]

所以 MAY-completion future 只有一个 state class。

## 3. 无 fairness 时的 MUST-complete

现在允许 scheduler 无限 stutter/no-op，并且不施加任何 fairness requirement。

对任意 nonterminal ideal，都存在永远 stutter 的无限 execution，因此永远不完成；terminal ideal 则已经完成。所以

\[
\boxed{
\operatorname{MUST\_complete}_{unrestricted}(I)
\iff
I=P_{gate}.
}
\]

对应 future 精确有两个 classes：

1. terminal；
2. nonterminal。

所以同一个 nonterminal state 可以同时满足 `MAY=yes`、`MUST=no`。

## 4. Weak fairness 已经充分

假设 **weak fairness**：

> 某 helper action 一旦 enabled，并且之后持续 enabled，则最终必须触发。

任取 nonterminal ideal `I`。从 complement 中选一个极小 helper `h`。`h` 的全部 helper predecessors 已经属于 `I`，所以 `h` enabled。由于 completed helpers 单调增长，prerequisites 永远不会被移除，因此 `h` 会一直 enabled，直到它 firing。

weak fairness 因而强制 `h` 最终触发。remaining helper 数严格下降。对有限 remaining count 归纳，最终全部 helpers 完成。

所以

\[
\boxed{
\operatorname{MUST\_complete}_{weak\ fairness}(I)=\mathrm{true}
\quad\forall I.
}
\]

这个有限单调系统只需要 weak fairness，不需要 strong fairness。

## 5. 精确 quotient 翻转

合法 state space 与 observable proposition `eventually complete` 完全相同，只改变 scheduler contract：

\[
\boxed{
\begin{array}{c|c}
\text{future contract} & \#\text{truth-value classes}\\
\hline
\text{MAY completion} & 1\\
\text{MUST, unrestricted stutter} & 2\\
\text{MUST, weak fairness} & 1
\end{array}}
\]

因此 future quotient 无法从 state geometry 单独确定。

## 6. 对 Stage 146 的范围修正

Stage 146 的 endpoint-one-class 命题只有在明确声明 completion/liveness contract 后才成立，例如 weak fairness，或者显式 `run-to-saturation` operation。

若没有这种 contract，任意 asynchronous scheduling 下的 `eventual saturated endpoint` 并不是 total deterministic future observable。

## 7. 架构后果

future specification 至少需要三个逻辑上独立的部分：

1. state / transition legality；
2. path quantifier（`MAY`、`MUST` 或选定 deterministic scheduler）；
3. admissible infinite executions 上的 liveness / fairness assumption。

只改变后两项，就可以在 states 与 transitions 完全不变时改变 coarsest future-safe quotient。

## 8. 前人工作边界

MAY/MUST path semantics、weak fairness、liveness 与有限 well-founded progress 论证都属于经典 transition-system/concurrency theory。这里不主张 generic novelty。P025 提供 exact finite pressure-test instance，以及 precision architecture 所需的 scope correction。
