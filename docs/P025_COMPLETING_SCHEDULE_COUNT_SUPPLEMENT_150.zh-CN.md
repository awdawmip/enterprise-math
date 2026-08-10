# P025 补充 150 —— Completing trace 数就是 linear-extension 数

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-fairness-stage147`

## 1. 从 fairness 到 complete firing words

Stage 149 已把当前有限单调 helper system 的 weakly fair executions 精确识别为 eventually completing executions。现在忽略 completion 以后的 terminal stutter，只记录有限 labelled helper firing word。

任何 complete firing word 都必须尊重全部 helper dependencies；反过来，任何尊重 dependency order 的 total ordering 都是一条合法 complete firing word。因此

\[
\boxed{
\{\text{complete helper firing words}\}
=
\{\text{linear extensions of }P_{gate}\}.
}
\]

所以完整 fair/completing trace precision 本质上是 order-extension 问题。

## 2. Perfect binary tree recurrence

设 `T_h` 为高度 `h` 的 perfect binary gate tree 的 helper/gate dependency poset，其中包含 subtree root。internal gates 数为

\[
n_h=2^h-1.
\]

令 `L_h` 为其 linear extension 数。

当 `h=1` 时只有一个 gate：

\[
\boxed{L_1=1.}
\]

当 `h>=2` 时，root 必须最后 firing。此前分别选择左右 child subtree 的一个 linear extension，再在保持各自内部顺序的前提下任意交织两条 words。每个 child 有 `n_(h-1)` 个 gates，所以

\[
\boxed{
L_h
=
\binom{2n_{h-1}}{n_{h-1}}
L_{h-1}^2.
}
\]

## 3. 完整 pre-output helper schedules

对 perfect `k=2^d` conjunction compiler，在 output `z` firing 以前，helper poset 就是 `z` 的两个高度 `d-1` child gate trees 的 disjoint union。

complete helper firing words 数与 `L_d` 的 interleaving 表达完全相同，因此

\[
\boxed{
N_{trace}(2^d)=L_d.
}
\]

精确前几项为

\[
\boxed{
N_{trace}(4)=2,
\quad
N_{trace}(8)=80,
\quad
N_{trace}(16)=21{,}964{,}800.
}
\]

## 4. Endpoint、state 与 trace 是不同资源

对同一个 perfect compiler 比较三个量：

\[
\begin{array}{c|c|c|c}
k & \text{endpoint classes} & \text{async progress states} & \text{complete labelled traces}\\
\hline
4 & 1 & 4 & 2\\
8 & 1 & 25 & 80\\
16 & 1 & 676 & 21{,}964{,}800
\end{array}
\]

这些数字无法用一个单一 `precision` 顺序理解：endpoint classes 强烈 quotient state；progress states 记录当前 configuration；trace words 则记录全部合法 ordering history。

尤其，一个相对不算大的 finite state space 可以承载数量巨大得多的 complete histories。

## 5. Operation-word precision 再次出现

Stages 105–106 已在 dyadic threshold setting 中区分 endpoint word quotient 与 trace word quotient。这里同一分离以 concurrency 形式再次出现：

- endpoint future 忘掉全部 firing order；
- progress state 只记当前 ideal；
- trace future 记住哪一个 linear-extension path 导致 completion。

因此 scheduler history 是 operation-word precision resource，而不自动等于 state-coordinate requirement。

## 6. 前人工作边界

poset linear extensions 与独立 subtrees 的 interleaving count 都属于经典 enumerative order theory。这里不主张 generic novelty。P025 提供 exact helper-compiler specialization，以及 endpoint/state/trace precision separation。
