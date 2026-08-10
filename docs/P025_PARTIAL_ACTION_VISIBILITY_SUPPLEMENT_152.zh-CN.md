# P025 补充 152 —— Partial action visibility 需要 dependency-closed support

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-fairness-stage147`

## 1. Partial action language

设 `P_gate` 为 helper dependency poset，

\[
I\in J(P_{gate})
\]

为 exact completed-helper state，并且只暴露一部分带标签 helper actions

\[
Q\subseteq P_{gate}.
\]

可见的当前 legality signature 为

\[
E_Q(I)=\operatorname{En}_{P_{gate}}(I)\cap Q.
\]

问题是：它什么时候能成为 projected visible progress

\[
I_Q=I\cap Q
\]

的干净 observable？

## 2. Predecessor-closed 充分条件

假设 `Q` 本身是 `P_gate` 的 order ideal：每个 visible helper 的所有 helper ancestors 也都 visible。

此时 `I_Q` 是 induced poset `Q` 的 ideal，而且每个 visible helper 的全部 prerequisites 都在 `Q` 内。所以 helper `q` 的 global enabledness 只依赖 `I_Q`。

更精确地，

\[
\boxed{
\operatorname{En}_{P_{gate}}(I)\cap Q
=
\operatorname{En}_{Q}(I\cap Q).
}
\]

对 induced poset `Q` 使用 Stage151，右侧又精确重建 `I\cap Q`。所以

\[
\boxed{
Q\text{ predecessor-closed}
\Longrightarrow
E_Q\text{ 是 projected progress }I\cap Q\text{ 的 exact coordinate}.
}
\]

`Q` 外部的 hidden helpers 无法再影响 visible action legality。

## 3. 非 closed action set 会泄漏 hidden dependency state

若 `Q` 漏掉 helper predecessors，上面的 factorization 可以失败。

在 balanced 八元 compiler 中，`h5` 依赖 hidden helpers `h1,h2`。取

\[
Q=\{h_5\}.
\]

考虑两个 visible projection 都为空的合法 ideals：

- 没有 helper 完成时，`h5` disabled；
- `h1,h2` 已完成时，`h5` enabled。

所以

\[
\boxed{
I\cap Q=J\cap Q
\quad\not\Rightarrow\quad
E_Q(I)=E_Q(J).
}
\]

visible action legality 会暴露 visible projected state 中没有保存的 hidden predecessor progress。

## 4. Enabledness 也可能无法恢复 visible progress

反方向也会失败。仍取 `Q={h5}`：

- hidden predecessors 尚未完成时，`h5` absent 且 disabled；
- `h5` 自身已完成以后，它也 disabled。

两个状态的 visible enabled signature 都为空，但 visible progress projection 分别为 `empty` 与 `{h5}`。因此

\[
\boxed{
E_Q(I)=E_Q(J)
\quad\not\Rightarrow\quad
I\cap Q=J\cap Q.
}
\]

所以 arbitrary partial action set 不会自动形成自洽的 state subsystem。

## 5. Operation-support closure principle

若要把一组 helper actions 当作 autonomous future language，一个稳健做法是先沿 dependency 做闭包：

\[
Q\leadsto\downarrow Q.
\]

在 predecessor-closed support 上，当前 labelled enabledness 与 projected progress 精确匹配；若不 closed，则必须额外保留 hidden-state information，或者接受另一种更粗 semantics。

这是此前 state-support closure 在 operation-language 一侧的对应物。

## 6. 架构后果

现在需要记录的不只是 declared actions 是哪些，还包括**解释这些 actions 所需要的 relation support**。

一个 syntactically 很小的 action language，可能具有更大的 semantic dependency footprint。因此

\[
\boxed{
\text{raw action count}
\neq
\text{semantic operation-support size}.
}
\]

## 7. 前人工作边界

dependency closure、projected transition systems 与 hidden-predecessor effects 都属于经典 systems/order theory。这里不主张 generic novelty。P025 提供 exact finite action-visibility boundary 与 future-precision interpretation。
