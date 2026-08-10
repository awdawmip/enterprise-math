# P025 补充 134 —— Chain implication law 的精确存储/深度端点

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-closure-basis-stage130`

## 1. Chain closure

固定 labels

\[
x_0,x_1,\ldots,x_n
\]

以及 semantic closure law

\[
x_0\Rightarrow x_1\Rightarrow\cdots\Rightarrow x_n.
\]

等价地，

\[
cl(\{x_i\})=\{x_i,x_{i+1},\ldots,x_n\}.
\]

exact closed states 是空状态与所有 suffixes。

## 2. Minimum-rule 下界

任意 sound complete single-head implication basis 至少需要

\[
\boxed{n}
\]

条规则。

因为对每个 `j=1,...,n`，从 seed `{x_{j-1}}` 出发最终必须生成缺失标签 `x_j`。只有 root/head 为 `x_j` 的规则能够加入该标签，所以每个 `x_j` 至少需要一条不同的 rooted rule。

Adjacent basis

\[
x_{j-1}\Rightarrow x_j,
\qquad1\le j\le n
\]

恰有 `n` 条规则，因此下界 sharp。

## 3. Minimum-rule basis 的唯一性

设一个 complete basis 恰好只有 `n` 条规则。则对每个 `x_j, j>=1`，它恰好有一条 root 为 `x_j` 的规则。

用从后向前的归纳证明这条唯一规则只能是

\[
\boxed{x_{j-1}\Rightarrow x_j.}
\]

对 `j=n`，从 seed `{x_{n-1}}` 出发，在 `x_n` 出现之前不存在任何其他 later label。唯一 root 为 `x_n` 的规则 premise 必须包含于 `{x_{n-1}}`。空 premise 不 sound，因为 `x_n` 不是 mandatory，因此 premise 只能是 `{x_{n-1}}`。

假设对 roots `x_{j+1},...,x_n` 已证明它们都是 adjacent tail rules。则从 `{x_{j-1}}` 出发，在 `x_j` 出现以前，这些 tail rules 都无法触发，因为它们最终都依赖 `x_j` 启动。此时唯一可用 label 仍是 `x_{j-1}`，所以 root 为 `x_j` 的唯一规则只能是 `{x_{j-1}} -> x_j`。

因此 adjacent/Hasse basis 是**唯一 minimum-rule single-head basis**。

## 4. Minimum storage 下被强制的 derivation depth

从 seed `{x_0}` 出发，唯一 minimum basis 每轮精确增加一个 chain level。因此

\[
\boxed{d_{\min\text{-storage}}=n.}
\]

在这个 family 上，minimum rule count 与 minimum derivation depth 无法同时实现。

## 5. One-round 端点

由 Stage 133，任何 one-round complete basis 都必须包含全部 rooted circuits。对该 chain，每个 `i<j` 都给出 circuit

\[
x_i\Rightarrow x_j.
\]

所以唯一 inclusion-minimal one-round representation 有

\[
\boxed{\binom{n+1}{2}}
\]

条规则，depth 为一。

因此两个精确资源端点为

\[
\boxed{
(\#\text{rules},d)
=
(n,n)
\quad\text{和}\quad
\left(\binom{n+1}{2},1\right).
}
\]

`n=3` 时，Stage 131 还给出两端之间的 complete 中间点 `(4,2)`，夹在 `(3,3)` 与 `(6,1)` 之间。

## 6. 无界分离

随 `n` 增长，

\[
\frac{\binom{n+1}{2}}n=\frac{n+1}{2},
\]

而 minimum-storage basis 的 depth 是 `n` 而不是一。

因此，为 direct closure 支付的 storage overhead 与为 minimum storage 支付的 computation depth 都可以无界增长。

## 7. 架构后果

即使 semantic closure 与 rule formalism 都已固定，relation-law precision 仍有真正的 storage/execution frontier。紧凑 law representation 可以语义完全精确但计算更深；direct representation 可以计算浅却存储显著更大。

这既不是 state precision，也不是 query-generator precision，而是独立的 **law-representation/runtime** 资源对。

## 8. 前人工作边界

chain 的 transitive closure/reduction 与 shortcut-depth tradeoff 都是经典对象。项目不主张 generic novelty。该 family 只用于严格证明：单一 scalar `relation precision` 无法同时代表 stored law size 与允许的 future derivation depth。
