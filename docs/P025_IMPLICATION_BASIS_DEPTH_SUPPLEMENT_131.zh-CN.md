# P025 补充 131 —— Implication basis 的存储量与推导深度

状态：`PROVED_WIP + EXECUTABLE_CHECKED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-closure-basis-stage130`

## 1. 为什么补充 130 还不是终点

完整 rooted-circuit table 是直接且单轮完备的，但允许 iterative forward chaining 后，一些 rooted circuits 会变成全局冗余规则。

例如 closure law

\[
a\Rightarrow c\Rightarrow b,
\]

对应 rooted circuits

\[
a\Rightarrow c,\qquad c\Rightarrow b,\qquad a\Rightarrow b.
\]

删除 `a -> b` 后，semantic closure 不变，因为它可以通过 `c` 用两轮重建。

因此，“某个 root 的 minimal premise”和“全局不可删除 implication rule”是不同概念。

## 2. Basis 语义

有限 single-head implication basis `B` 由规则

\[
A\Rightarrow b
\]

组成。从 seed `S` 出发，每一轮并行触发所有当前 enabled rules，直到不再增加标签，记最终结果为 `cl_B(S)`。

若对所有 `S subseteq P` 都有

\[
\operatorname{cl}_B(S)=\operatorname{cl}_\Omega(S),
\]

则称 `B` 对目标 closure sound and complete。

对 complete basis 定义 worst-case parallel derivation depth

\[
d(B)=\max_{S\subseteq P}
\min\{t:\text{到第 }t\text{ 轮已达到 }cl_\Omega(S)\}.
\]

存储成本可以用 rule count 或 total premise literals 衡量。它们是 representation costs，而不是 semantic state dimension。

## 3. Chain family：精确可扩展分离

设

\[
x_0\Rightarrow x_1\Rightarrow\cdots\Rightarrow x_n.
\]

exact closed states 是空集以及所有 suffixes

\[
\{x_i,x_{i+1},\ldots,x_n\}.
\]

### 完整 rooted-circuit table

任意 `i<j` 都给出 rooted circuit

\[
x_i\Rightarrow x_j.
\]

所以 direct table 有

\[
\boxed{\binom{n+1}{2}}
\]

条规则，并且任意 seed 一轮闭合：

\[
\boxed{d=1}.
\]

### Adjacent/Hasse basis

只保留

\[
x_i\Rightarrow x_{i+1},\qquad0\le i<n.
\]

它只有

\[
\boxed{n}
\]

条规则，仍然 sound and complete；但从 `{x_0}` 出发精确需要 `n` 轮：

\[
\boxed{d=n}.
\]

在 single-head implication 表示中，这些相邻 consequence 对 minimum-rule chain representation 是不可绕开的，因此 adjacent basis 实现自然的 minimum-storage 极端。

## 4. 精确有限 Pareto 样本

对四个标签 `x0,x1,x2,x3`，三个显式 complete bases 给出

\[
\boxed{(\#\text{rules},d)=(3,3),(4,2),(6,1)}.
\]

中间 basis 是 adjacent basis 再加 shortcut `x0 -> x2`。

因此，同一个 semantic closure 可以拥有真正不同的 relation-law coordinate charts，并承担不同 execution cost。

## 5. 架构后果

若不先声明 future runtime 允许执行什么，就不应给一个 closure law 指派单一 scalar `relation precision`。

至少三个资源必须分开：

1. semantic closure / state information；
2. 被保存的 implication-law size；
3. 为重建 future consequences 所需的 derivation / operation depth。

完整 circuit table 付出更多存储，以换取 one-round lookup；更小的 iterative basis 减少存储，但需要更多 future computation。

这是此前 P025 chart/update Pareto 边界在 relation-law 层的对应物。

## 6. 前人工作边界

Horn bases、transitive reduction、forward chaining、derivation depth 与 shortcut tradeoff 都是经典对象，这里不主张 generic novelty。项目侧价值是把这组 tradeoff 精确放入 future-relative precision accounting 中。
