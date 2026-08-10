# P025 补充 138 —— Auxiliary-state compilation 必须携带 legality invariant

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-closure-basis-stage130`

## 1. Helper compiler 真正保持的是什么

设 `X_raw` 是 Stage 136 pure k-way conjunction 的 raw label state space，`X_ext` 是加入 helper labels 后的扩展空间。记

\[
\iota:X_{raw}\to X_{ext}
\]

为把所有 helpers 初始化为 absent 的 embedding，记

\[
\pi:X_{ext}\to X_{raw}
\]

为删除全部 helper coordinates 的 projection。

设 `F_ext^*` 表示扩展 helper rules 的饱和 forward chaining。compiler 满足

\[
\boxed{
\pi\bigl(F_{ext}^*(\iota(S))\bigr)
=
cl_{raw}(S)
\qquad\forall S\subseteq X_{raw}.
}
\]

这才是正确的 raw-semantic simulation statement。

## 2. 它不是整个 internal state space 上的 homomorphism

更强的命题

\[
\pi(F_{ext}^*(T))=cl_{raw}(\pi(T))
\qquad\forall T\in X_{ext}
\]

是假的。

对 sequential helper compiler，最后一条规则为

\[
e_{k-1}a_k\Rightarrow z.
\]

人为初始化

\[
T=\{e_{k-1},a_k\}.
\]

内部 forward chaining 会生成 `z`，因此

\[
\pi(F_{ext}^*(T))=\{a_k,z\}.
\]

但

\[
\pi(T)=\{a_k\},
\]

pure raw k-way conjunction 不会由单个 antecedent 触发：

\[
cl_{raw}(\{a_k\})=\{a_k\}.
\]

所以

\[
\boxed{
\pi(F_{ext}^*(T))\ne cl_{raw}(\pi(T)).
}
\]

## 3. 正确的 compiler contract

auxiliary-state compilation 因此不只需要 output projection，还必须声明 admissible internal-state discipline，例如：

1. raw initialization 时 helpers 全部 absent；
2. helpers 只能通过 declared internal rules 生成；
3. 只有从合法 raw embeddings 可达的 internal states，才参与 raw semantic equivalence 的声明。

等价地，correctness 是一个**受限 simulation/refinement property**，而不是 unrestricted extended state system 与 raw system 的全空间相等。

## 4. Precision 后果

auxiliary state 有两种完全不同的含义：

- **合法 derived scratch/cache state** —— 在 reachability invariant 下只是 implementation detail；
- **自由 observable state coordinate** —— 会扩大 semantic state space，并可能改变 raw futures。

两者不能混为一谈。

所以 Stage 136 的 law-compiler resource vector 还必须加入 legality coordinate：

\[
\boxed{
(\text{premise arity},
\text{derivation depth},
\text{auxiliary-state dimension},
\text{admissible internal-state invariant}).
}
\]

最后一项在没有另外声明复杂度度量时是定性资源。

## 5. 与 partial-operation / future legality 的关系

这一结构与现有 Foundation/P023 的结论同构：enabledness 与 legal domain 本身属于 future-observable structure；hidden-state representation 只有在合法状态 contract 被保持时才安全。本补充只是一个有限 specialization / pressure test，不主张新的 generic simulation theorem。

## 6. 前人工作边界

simulation relations、refinement mappings、hidden-state initialization 与 invariant-restricted implementation correctness 都是标准 transition-system / program-verification 思想。P025 不主张 generic novelty。项目侧结果是一个 exact counterexample：它阻止把 auxiliary-state dimension 当成无需合法性成本的自由 precision trade。
