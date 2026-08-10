# P025 补充 126 —— Semantic Membership-Implication Poset

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonideal-boundary-stage125`  
依赖：P025 补充 125；A2/A4 future-state boundaries  
硬阻断：`NONE`

## 1. 修 relation，而不是先加 scalar precision

补充 125 已证明：若 exact states 违反 externally supplied poset 的 downward-closure law，该外部 order 就不能安全用于 query normalization。

但一个非空有限 exact-state family

\[
\Omega\subseteq2^P
\]

自身仍包含 membership implications。

## 2. P025-D49 —— semantic implication preorder

定义

\[
\boxed{x\preceq_\Omega y
\iff
\forall X\in\Omega,
\quad y\in X\Longrightarrow x\in X.}
\]

等价地，`y` 在 \(\Omega\) 上的 membership column 逐点小于等于 `x` 的 membership column。

该关系 reflexive 且 transitive，因此是 preorder。

## 3. P025-T275 —— every exact state 在 semantic order 下自动 downward closed

对每个 \(X\in\Omega\)，

\[
y\in X,\quad x\preceq_\Omega y
\Longrightarrow x\in X.
\]

所以每个 exact state 自动成为 semantic preorder 的 down-set。

external order 上失效的 closure law，被一张由实际 exact-state semantics 内生生成的 relation 恢复。

## 4. P025-T276 —— semantic preorder 的 maximality

令 \(R\) 为 \(P\) 上任意 binary relation，并假设 \(\Omega\) 中每个 exact state 都在 \(R\) 下 downward closed。则

\[
\boxed{R\subseteq\preceq_\Omega.}
\]

因为若 \(xRy\)，`R` 的 safety 就意味着每个包含 \(y\) 的 exact state 都包含 \(x\)，这正是 \(x\preceq_\Omega y\)。

因此 \(\preceq_\Omega\) 是**与全部 exact states 兼容的最大 membership-implication relation**。

这是 endogenous safe relation，而不是 externally imposed ontology。

## 5. Quotient always-coactive labels

定义

\[
\boxed{x\sim_\Omega y
\iff
x\preceq_\Omega y
\text{ and }
y\preceq_\Omega x.}
\]

则 `x,y` 在每个 exact state 上具有完全相同的 membership column。

quotient 掉 \(\sim_\Omega\) 后得到真正的 finite poset

\[
\boxed{P_\Omega:=P/{\sim_\Omega}.}
\]

每个 exact state 都投影成 \(P_\Omega\) 的 order ideal。

因此 arbitrary Boolean exact states 总能在**替换 relation geometry**后，表示成 semantic quotient poset 的 ideals。

## 6. Exact geometry 会改变

semantic poset 可以与 external order 完全不同。

### External chain 打开为 semantic antichain

令 external labels 满足 `a<b`，但 exact states 为

\[
\Omega=\{\{a\},\{b\}\}.
\]

在 \(\Omega\) 上二者互不蕴含，所以 semantic quotient 有两个 incomparable labels，

\[
\boxed{\operatorname{width}(P_\Omega)=2.}
\]

external width-one assumption 因而在 semantic level 上是错误的。

### Always-coactive labels collapse

若每个 exact state 中 `a` 与 `b` 总是同时出现或同时不出现，则

\[
a\sim_\Omega b
\]

二者压成一个 semantic coordinate。

因此 semantic geometry 相比 external label geometry 既可能变宽，也可能变小。

## 7. Unary safe geometry 仍不是 full query quotient

semantic implication poset 捕获全部**一元** membership implications，并重新保证 antichain normalization safe。

但它未必是 conjunction query 的 coarsest representation。受限 exact-state family 可能满足真正的 higher-order law，例如

\[
a\wedge b\Longleftrightarrow c,
\]

而任何一个 unary implication 都看不见这一事实。

因此

\[
\boxed{\text{semantic implication poset}\neq\text{full conjunctive closure in general}.}
\]

Stage 127 必须从 unary implication 升级到 exact-state family 诱导的 complete closure operator。

## 8. 架构结论

补充 125–126 给出新的 repair principle：

\[
\boxed{
\text{unsafe external relation}
\not\Rightarrow
\text{add scalar precision};
\quad
\text{first infer the safe semantic relation}.
}
\]

relation geometry 本身就是 task-relative state interface 的一部分。

## 9. 与 A2/A4 的关系

A2 拥有 safe future quotients，A4 拥有 arbitrary correspondence / support。Stage 126 是 specialization：Boolean correspondence 会诱导一张 largest unary implication preorder。应把它作为 diagnostic interface，而不是竞争性的 relation-algebra mother theorem。

## 10. Prior-art 边界

logical implication preorders、quotient preorders 与 membership-column equivalence 都是 elementary / standard formal-concept / order-theoretic ideas。这里不主张 generic novelty。

项目侧结果是它们对 P025 width-saturation boundary 的 exact repair。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/semantic_implication_poset.py`；
- `tests/test_semantic_implication_poset.py`。

executable layer 验证 reflexivity/transitivity、largest-safe-relation maximality、coactive labels 的 semantic quotient、exact-state idealhood，以及 external chain 打开为 semantic width two 的样本。

## 12. 下一前沿

Stage 127 应构造 \(\Omega\) 的 full conjunctive closure operator，证明两个 raw conjunctions 具有相同 future truth vector 当且仅当它们的 closures 相同，并把 semantic implication poset 精确定位为该 closure system 的 unary fragment。
