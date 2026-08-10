# P025 补充 132 —— Query generator arity 与 relation-law arity 互不可比

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-closure-basis-stage130`

## 1. 两种不同的 arity 资源

对有限 exact-state family `Omega`，记 `cl=cl_Omega`。

Stage 128 的 **query-generator horizon** 为

\[
g(\Omega)
=
\max_{C\in\operatorname{Fix}(cl)}
\min\{|S|:cl(S)=C\}.
\]

它衡量：为了表示某个 conjunction-semantic class，最坏情况下必须保留多少个 raw query labels。

Stage 130 的 **direct relation-law horizon** 为

\[
h_{\rm circ}(\Omega)
=
\max\{|A|:(A,b)\text{ 是 rooted minimal implication}\}.
\]

它衡量 one-round circuit presentation 中不可约 direct implication 的最大 premise arity。

两者回答的是不同问题，不存在普遍大小关系。

## 2. `g` 可任意大而 `h_circ=0`

设 `P` 有 `w` 个 labels，并取 exact-state universe

\[
\Omega=2^P.
\]

则对任意 `S`，

\[
cl(S)=S,
\]

即 identity closure。于是不存在 `b notin A` 的任何非平凡 implication `A -> b`，因此

\[
\boxed{h_{\rm circ}(\Omega)=0.}
\]

但 closed class `P` 在 identity closure 下只能由 `P` 自身生成，所以

\[
\boxed{g(\Omega)=|P|=w.}
\]

因此 `g-h_circ` 可以任意大。

## 3. Relation-law arity 也可以大于 query-generator arity

取

\[
\Omega=\{\{a\},\{b\},\{a,b,c\}\}.
\]

其 closed classes 为

\[
\varnothing,\quad \{a\},\quad \{b\},\quad \{a,b,c\}.
\]

它们分别可由

\[
\varnothing,\quad\{a\},\quad\{b\},\quad\{c\}
\]

生成，所以

\[
\boxed{g(\Omega)=1.}
\]

但 closure 中存在不可约 binary circuit

\[
\boxed{\{a,b\}\Rightarrow c,}
\]

所以

\[
\boxed{h_{\rm circ}(\Omega)=2.}
\]

因此一般也不存在 `h_circ <= g`。

## 4. 互不可比定理

在所有有限 exact-state families 上，两者不存在任一方向的普遍不等式：

\[
\boxed{
g(\Omega)\not\le h_{\rm circ}(\Omega),
\qquad
h_{\rm circ}(\Omega)\not\le g(\Omega).
}
\]

必须分别记录：

1. **query-state arity** —— 命名一个 future-equivalence class 需要多少 labels；
2. **relation-law arity** —— 一个不可约 implication 最多需要多少 antecedent labels 共同出现。

任何一方都不能作为另一方的代理。

## 5. 架构后果

当前 precision architecture 因此又多出一条必须永久保持的分离：

- semantic state / closure class；
- query-generator arity；
- relation-law storage 与 premise arity；
- execution / derivation depth。

一个系统可以几乎没有 relation law，却有昂贵 query（identity closure）；也可以拥有非常便宜的 query normal form，却存在真正 higher-order relation law（`a AND b -> c` 样本）。

## 6. 前人工作边界

closure generators、implicational dimension、Horn premise arity 等都属于经典 closure-system/FCA/Horn 理论。P025 不主张其一般原创性。项目侧可复用的是由 exact counterexamples 支撑的 precision-resource 分离。
