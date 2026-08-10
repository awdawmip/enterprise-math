# P025 补充 157 —— Operation-support growth 是 reverse dependency-ball geometry

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-state-support-stage155`

## 1. Predecessor expansion 就是 metric growth

Stage 156 定义

\[
Q^{(0)}=Q,
\qquad
Q^{(t+1)}=Q^{(t)}\cup\operatorname{Pred}(Q^{(t)}).
\]

这精确等于在 dependency graph 上从 consumer action 向 prerequisite helper 反向走的 breadth-first growth。

对 helper `x in down(Q)`，定义 reverse dependency distance

\[
d_Q(x)
=
\min\{\text{从 }x\text{ 沿 helper-dependency edges 正向到某个 }q\in Q\text{ 的边数}\}.
\]

则

\[
\boxed{
Q^{(t)}
=
\{x\in\downarrow Q:d_Q(x)\le t\}.
}
\]

所以 Stage156 的 support-growth layers 就是这个有向 dependency distance 的 exact closed balls。

## 2. 精确 support horizon

定义

\[
H_{supp}(Q)
=
\min\{t:Q^{(t)}=\downarrow Q\}.
\]

由 ball identity，

\[
\boxed{
H_{supp}(Q)
=
\max_{x\in\downarrow Q}d_Q(x).
}
\]

因此，为了暴露全部 dependency support 所需的 operation-promotion rounds，就是 declared action set 的 reverse eccentricity。

## 3. Perfect balanced family

对 perfect `k=2^d` compiler 的一个最高 pre-output helper action，dependency subtree 的 helper height 为

\[
d-1.
\]

action 本身距离 0，第一层 hidden helpers 距离 1，最底 helper layer 距离 `d-2`。所以

\[
\boxed{
H_{supp}=d-2=\log_2k-2.
}
\]

reverse shells 大小为

\[
1,2,4,\ldots,2^{d-2},
\]

balls 大小为

\[
\boxed{
|Q^{(t)}|=2^{t+1}-1,
\qquad
0\le t\le d-2.
}
\]

这精确重现 Stage156 的 `1->3`、`1->3->7`、`1->3->7->15` 等序列。

## 4. 两种等价语义

同一个整数 `H_supp` 有两个解释：

1. **operation-language horizon** —— 当前 exposed prerequisite state 还能被升级成 executable actions 多少轮才闭合；
2. **relation-geometry horizon** —— declared action set 到其 hidden helper support 的最大 reverse dependency distance。

所以 future-language closure process 可以被直接表示成有限 relation geometry。

## 5. 边界

horizon/depth 不等于 support cardinality。branching 会让只增加一层 dependency distance 时突然暴露大量新 helper coordinates。Stage 158 将分离 support radius 与 support volume。

## 6. 前人工作边界

breadth-first search、graph distance、eccentricity 与 dependency DAG depth 都属于经典对象。这里不主张 generic novelty。P025 提供 future-operation support promotion 与 dependency-ball geometry 在当前 precision architecture 中的 exact equivalence。
