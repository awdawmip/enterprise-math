# P025 补充 146 —— Asynchronous helper progress 的 task-relative quotients

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-helper-cache-stage139`

## 1. 设置与 fairness 边界

固定 Stage 144 的 asynchronous helper-progress system，假设全部 raw antecedents 已存在，而 output `z` 尚未触发。合法 pre-output runtime state 是 helper dependency poset 的 ideal

\[
I\in J(P_{gate}).
\]

本补充比较**同一个** ideal state space 上不同 declared futures 所需的 quotient。

只要讨论 eventual saturated raw endpoint，就显式假设 scheduler 具有足够的 eventual-completion / fairness：所有为了 saturation 所需、持续 enabled 的 helper 最终都会被触发。没有这类 liveness 条件时，asynchronous scheduler 可以永久 stutter，此时 `eventual saturated endpoint` 甚至不是一个 total future observable。Stage 147 将单独研究这一 liveness contract。

## 2. Endpoint-only future

在 eventual completion 假设下，任意 pre-output ideal 最终都会到达同一个 saturated helper state，随后得到同一个 raw output `z`。

所以对 future language

> 只返回最终 saturated raw endpoint，

全部 pre-output helper ideals 都等价：

\[
\boxed{N_{endpoint}=1.}
\]

Stages 144–145 中巨大的 ideal lattice 对这个 endpoint-only query 不贡献额外 state precision。

## 3. Remaining-helper-work future

如果 future 只问

> 所有 helpers 完成以前还剩多少次 helper firing？

则每个 helper 最多触发一次，每个 asynchronous action 精确完成一个 helper。设 helper 总数为 `m`，则

\[
\boxed{R(I)=m-|I|.}
\]

因此 ideal cardinality 是 sufficient 且 exact 的。沿任一 linear extension，`0,...,m` 的每个 cardinality 都会出现，所以 quotient 精确有

\[
\boxed{m+1}
\]

个 classes。

这就是 ideal lattice 的 scalar rank quotient。

## 4. Enabled-action future 打破 rank

现在把 future 强化为询问

> 下一步哪些带标签的 helper actions enabled？

对 ideal `I`，

\[
\operatorname{En}(I)
=
\{h\notin I:\operatorname{Pred}(h)\subseteq I\}.
\]

相同 cardinality 不决定这个 labelled enabled set。

在四元 balanced compiler 中，两个 first-layer helpers 彼此 incomparable。ideals

\[
I_1=\{h_1\},
\qquad
I_2=\{h_2\}
\]

大小都为一，因此 remaining-work count 相同，但

\[
\operatorname{En}(I_1)=\{h_2\},
\qquad
\operatorname{En}(I_2)=\{h_1\}.
\]

所以

\[
\boxed{|I|\text{ 对 labelled next-action semantics 不 sufficient}.}
\]

scheduler-facing future 会重新强迫 labelled support geometry 出现。

## 5. Exact-progress future

如果 future 要求 exact completed-helper identity、exact internal trace continuation，或者任何能够区分全部 ideals 的语言，就必须保留 full ideal state。state count 为

\[
\boxed{|J(P_{gate})|},
\]

并可使用 Stage 144 的 antichain-boundary compression 作为 coordinate chart。

## 6. Precision ladder

对完全相同的 raw state、compiler 与 asynchronous legal state space，declared future 给出精确层级

\[
\boxed{
1
\quad\to\quad
m+1
\quad\to\quad
\text{enabled-action quotient}
\quad\to\quad
|J(P_{gate})|.
}
\]

前两层分别对应 endpoint 与 remaining-work semantics；第三层依赖 labelled action support，可以严格细于 rank；第四层是 exact progress identity。

因此“存在很多合法 runtime states”本身并不意味着 observation precision 必须同样细。

## 7. 架构后果

Stage 144 证明 scheduler freedom 生成 ideal lattice；Stage 146 进一步证明 future language 决定其中多少结构必须保持可见。

同一个 runtime 可以具有：

- endpoint-only semantics 下的完全 collapse；
- amount-of-work semantics 下的 scalar rank；
- action legality 下的 labelled relation/support state；
- exact progress 下的 full ideal/antichain state。

这是 A2/P023/P024 future-relative precision 在 concurrency 场景中的直接 specialization。

## 8. 前人工作边界

order-ideal rank、enabled-event sets 与 asynchronous configurations 都属于经典 concurrency/order theory。这里不主张 generic novelty。P025 提供 exact task ladder 与 fairness/liveness scope warning。
