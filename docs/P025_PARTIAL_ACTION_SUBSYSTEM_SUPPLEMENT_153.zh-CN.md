# P025 补充 153 —— Predecessor-closed helper actions 构成精确 partial subsystem

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-fairness-stage147`

## 1. 设置

设 `P_gate` 为 helper dependency poset，`I` 为合法 ideal，并令

\[
Q\subseteq P_{gate}
\]

为 declared labelled helper-action family。

每个 `q in Q` 都是 partial action：

\[
F_q(I)=I\cup\{q\}
\]

当 `q` enabled 时定义，否则 undefined。

问题是 projected state

\[
\pi_Q(I)=I\cap Q
\]

什么时候能承载这些 actions 生成的完整 legality-sensitive future language？

## 2. Predecessor-closed action family

假设 `Q` 是 `P_gate` 的 order ideal：每个 declared action 的全部 helper ancestors 也都 declared/visible。

Stage 152 已给出当前 enabledness factorization：

\[
q\text{ 在 }I\text{ 中 enabled}
\iff
q\text{ 在 }I\cap Q\text{ 中 enabled}.
\]

当 action enabled 时，

\[
\pi_Q(F_q(I))
=
(I\cup\{q\})\cap Q
=
(I\cap Q)\cup\{q\}.
\]

因此 partial maps 精确满足

\[
\boxed{
\pi_Q\circ F_q
=
F_q^Q\circ\pi_Q,
}
\]

并且 enabledness/domain membership 也完全一致。

## 3. 全部 action words 因子化

因为每一个 generator partial operation 都与 projection 交换且保持 legality，对 word length 归纳可得：

- 一个 declared `Q`-word 在 global ideal `I` 上可执行，当且仅当它在 projected ideal `I\cap Q` 上可执行；
- 若可执行，最终 projected state 精确等于 induced subsystem 中执行该 word 的结果；
- 每个 prefix 的 legality decision 也完全一致。

所以

\[
\boxed{
I\mapsto I\cap Q
\text{ 对完整 legality-sensitive }Q\text{-word future sufficient}.
}
\]

## 4. 当前 enabledness 已经 future-complete

在 induced poset `Q` 内应用 Stage151，`I\cap Q` 的 labelled enabled frontier 可以精确重建 projected ideal。

因此当 `Q` predecessor-closed 时，**当前 visible enabledness signature** 已经决定所有 declared helper action words 的未来行为：

\[
\boxed{
\text{current }Q\text{-enabled frontier}
\Longleftrightarrow
I\cap Q
\Longrightarrow
\text{all }Q\text{-action futures}.
}
\]

不再需要额外 history/refinement coordinate。

## 5. 非 closed support 在长度一就失败

若 `Q` 不 predecessor-closed，hidden predecessors 可以在 `I\cap Q` 不变时改变 visible action 是否 enabled。Stage152 的八元例 `Q={h5}` 已给出精确 witness。

所以 projection 在 **word length one** 就可能无法尊重 declared generator。若不补入 hidden dependency state/support，更深 future closure 无法把这个 projected subsystem 修好。

## 6. Operation-language support closure

对这个 helper system，一个自然 self-contained action language 不是任意 syntactic set `Q`，而是 dependency-closed support：

\[
\boxed{Q\leadsto\downarrow Q.}
\]

这种 support closure 是 operation language 自身的 semantic cost。

## 7. 与 P023/Foundation 的关系

这是 canonical legality-sensitive partial-operation quotient 的具体 specialization：domain membership 本身属于 future behavior，必须和 enabled targets 一起通过 quotient 因子化。

这里 dependency closure 给出了特别简单的 sufficient state，而且全部 labelled current enabledness 已经恢复它。

## 8. 前人工作边界

projected transition systems、partial-map homomorphisms、dependency closure 与 word-level induction 都属于经典对象。这里不主张 generic novelty。P025 提供 exact helper-system specialization 与 scope boundary。
