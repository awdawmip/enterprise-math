# P025 补充 156 —— Dependency closure 是 expanding operation envelope 的 fixed point

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-state-support-stage155`

## 1. 从 static prerequisite state 到 executable interference

Stage 155 已证明：若只有 `Q` 中的 actions 可以 firing，则精确 static helper-state support

\[
R_Q=Q\cup\operatorname{Pred}(Q)
\]

足以承载全部 Q-only words。

现在改变 future operation envelope：把新暴露的 predecessor helpers 自身也升级成 executable actions。它们自己的 hidden predecessors 又可能影响 legality，因此上一轮 static state support 不再一定 self-contained。

## 2. 迭代 support growth

定义

\[
Q^{(0)}=Q
\]

并递归定义

\[
\boxed{
Q^{(t+1)}
=
Q^{(t)}\cup\operatorname{Pred}(Q^{(t)}).
}
\]

解释如下：

- 若精确只有 `Q^(t)` 中的 actions executable，而其他 helper statuses frozen，则 Stage155 说明 state support `Q^(t+1)` sufficient；
- 若这些新暴露的 state coordinates 随后也被升级成 executable actions，则下一层 `Q^(t+2)` 开始相关。

由于 helper DAG 有限，该序列最终稳定。

## 3. Fixed point 等于 dependency closure

到 fixed point `Q^*` 时，每个成员的全部 helper predecessors 都已经在集合中。所以 `Q^*` predecessor-closed，并且包含初始 `Q`。

反过来，任何包含 `Q` 的 predecessor-closed set 都必须包含递归产生的每一层。因此

\[
\boxed{
Q^*
=
\downarrow Q.
}
\]

所以 Stage153/154 的 autonomous action support，正是反复把 Stage155 state support 升级成 actions 后的 fixed point。

## 4. Promotion 会暴露新的 legality collision

若 `Q^(1)` 只作为 `Q^(0)` actions 的 state support，它是 sufficient 的。

一旦 `Q^(1)\Q^(0)` 中的新 helpers 也变成 executable，它们的 enabledness 就可能依赖 `Q^(2)\Q^(1)` 中的 predecessors。此时可以出现两个 global ideals 在整个 `Q^(1)` 上完全相同，却对某个 newly promoted action 给出不同 legality。

perfect 16-way compiler 的最高 pre-output helper 已出现这个现象：第一层 repair 只有三个 helper coordinates；把它的两个 child helpers 也升级成 actions 后，立刻暴露四个 hidden first-layer predecessors，迫使 support 扩成七个 helpers。

## 5. Perfect family 的精确增长

对 perfect balanced compiler 的一个最高 pre-output helper：

\[
\boxed{
\begin{array}{c|c}
k & |Q^{(t)}|\text{ until fixed point}\\
\hline
8 & 1,3\\
16 & 1,3,7\\
32 & 1,3,7,15
\end{array}}
\]

fixed point size 为

\[
\boxed{\frac{k}{2}-1,}
\]

与 Stage154 的 full dependency support 完全一致。

## 6. Precision 解释

dependency support 不应自动作为 initial state precision 一次性收取。它由 future 被允许操作什么逐层生成。

一个自然 staged picture 是

\[
\boxed{
\text{declared actions}
\to
\text{static prerequisite state}
\to
\text{promoted actions}
\to
\text{new hidden prerequisite state}
\to\cdots
\to
\downarrow Q.
}
\]

因此同一 dependency graph 在不同 future operation envelopes 下具有不同 precision cost。

## 7. 前人工作边界

dependency closure 与 DAG support 上的 fixed-point iteration 都是经典对象。这里不主张 generic novelty。P025 提供 exact future-operation interpretation 与 scalable support-growth witnesses。
