# P025 补充 115 —— Task-Relative Poset Query Projection

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-poset-observable-stage113`  
依赖：P025 补充 113–114；canonical A2 declared-future signature discipline  
硬阻断：`NONE`

## 1. Full boundary 并不总是正确 future state

补充 113–114 已确定：对有限 observation poset \(P\) 的**完整 labelled membership**，ambient ideal 的 maximal antichain boundary 是 exact state。

但 declared future language 可能只查询一个子集

\[
Q\subseteq P.
\]

此时保留整个 ambient boundary 就是过精。

## 2. P025-T257 —— exact query projection

对 ambient ideal \(I\in J(P)\)，定义

\[
\boxed{
\pi_Q(I):=I\cap Q.
}
\]

令 \(Q\) 继承 \(P\) 的 induced order。则 \(I\cap Q\) 是 induced poset \(Q\) 的 order ideal。

对 declared future

> 对每个 \(q\in Q\)，询问 `q 是否 active？`

两个 ambient ideals future-equivalent 当且仅当

\[
\boxed{
I\sim_QJ
\iff
I\cap Q=J\cap Q.
}
\]

因此 \(\pi_Q\) 就是该 declared membership language 的 coarsest semantic state。

## 3. P025-T258 —— 每个 induced query ideal 都可实现

signature image 不只是 \(J(Q)\) 的一个子集，而是全部：

\[
\boxed{
\pi_Q(J(P))=J(Q).
}
\]

事实上，任取 \(K\in J(Q)\)，令

\[
A=\operatorname{Max}_Q(K).
\]

其 ambient down-closure

\[
I:=\downarrow_PA
\]

满足

\[
I\cap Q=K.
\]

所以 exact query-state space 就是 induced query poset 的 ideal lattice。

## 4. P025-T259 —— task-relative boundary cost

把补充 114 施加到 induced query poset，得到

\[
\boxed{
\max_{I\in J(P)}
\left|
\operatorname{Max}_Q(I\cap Q)
\right|
=
\operatorname{width}(Q).
}
\]

因此 relevant precision-support cost 由 **query width** 控制，而不是 ambient width。

特别地，

\[
\boxed{
\operatorname{width}(Q)=1
\Longrightarrow
\text{scalar query rank 完备},
}
\]

即便 ambient \(P\) 自己的 width 很大。

## 5. Exact compression examples

### Diamond ambient poset

令

\[
a<b<d,
\qquad a<c<d,
\qquad b\parallel c.
\]

ambient poset width 为 2。full membership 因此可能需要同时包含 \(b,c\) 的 boundary。

但对 declared query chain

\[
Q=\{a,d\},
\]

有

\[
\operatorname{width}(Q)=1,
\]

query signature 只有三个状态：

\[
\varnothing,
\{a\},
\{a,d\}.
\]

所以 width-two ambient state 在这个 future language 下可以 exact collapse 回 scalar rank。

### Wide antichain ambient poset

若 \(P\) 是含 \(n\) 个元素的 antichain，则它有 \(2^n\) 个 ideals，width 为 \(n\)。若 future 只问一个 label \(q\)，则 \(Q=\{q\}\) 只有两个 ideal states，width 为 1。

这给出可任意放大的 task-relative collapse。

## 6. Precision amount 与 support geometry 都是 future-relative

补充 107–112 已证明 observable algebra 会改变 required state precision。补充 113–115 又增加第二种效应：future language 会改变 **support geometry 的形状本身**。

因此正确对象不应是一条 global scalar `precision level`。至少必须区分：

\[
\boxed{
\text{ambient relation geometry}
\quad\text{与}\quad
\text{declared-query geometry}.
}
\]

query poset 可能具有更小 width、更少 ideal states，以及不同的 antichain boundary。

## 7. 与 A2、A4 的关系

A2 已拥有 generic mother statement：declared future language 决定 future signature，从而决定 task-relative quotient。Stage 115 是它的**specialization / pressure test**，不是竞争性 mother theorem。

A4 拥有 multivalued support / correspondence algebra。Stage 115 不主张每个 A4 support 都是 order ideal。它只说明：当 declared observation family 本身具有 monotone poset semantics 时，task-relative support restriction 自然成为 induced-ideal quotient，其 width 由 queried subposet 控制。

## 8. Prior-art 边界

order ideal 对 induced subposet 的 restriction 与 antichain boundary 都是经典 finite-poset facts。这里不主张一般理论新颖。

项目侧贡献是 exact task-relative precision reading，以及它与此前 P025 rank-path failure boundary 的 executable 连接。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 9. 可执行资产

新增：

- `src/enterprise_math/poset_query_projection.py`；
- `tests/test_poset_query_projection.py`。

executable layer 验证 exact query projection、到 induced ideal lattice 的 surjectivity、query-width cost、宽 ambient poset 内 chain query 的 scalar recovery，以及 full boundary 到更小 query boundary 的严格缩减。

## 10. 下一前沿

下一层是 multivalued uncertainty。如果 coarse state 不再决定一个 ideal，而只决定一**族 admissible ideals**，那么 full membership 会自然分裂成 MAY 与 MUST semantics。这正是 A4 correspondence algebra 应进入的位置。下一步 P025 pressure test 应停止假设 state single-valued，并推导 admissible-ideal family 的 minimal MAY/MUST boundary representation。
