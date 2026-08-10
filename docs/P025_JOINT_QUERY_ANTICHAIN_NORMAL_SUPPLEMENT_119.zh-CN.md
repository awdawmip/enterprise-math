# P025 补充 119 —— Antichain Normal Form for Joint Queries

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-poset-observable-stage113`  
依赖：P025 补充 113–118  
硬阻断：`NONE`

## 1. Raw query arity 不等于 semantic arity

补充 118 用 raw set size \(|S|\) 衡量 bounded joint-MAY future。但 ideal semantics 内部带有 order redundancy：若一个 required label 位于另一个 required label 之下，同时要求二者并不比只要求较大的那个更强。

Stage 119 因此先 quotient **query language 自身**，再讨论需要多少 state precision。

## 2. P025-D44 —— maximal-antichain query normal form

对有限 required label set

\[
S\subseteq P,
\]

定义

\[
\boxed{
\alpha(S):=\operatorname{Max}_P(S).
}
\]

因为每个 exact state \(I\) 都是 order ideal，

\[
\boxed{
S\subseteq I
\iff
\downarrow S\subseteq I
\iff
\alpha(S)\subseteq I.
}
\]

所以每个 joint membership query 都与其 maximal required labels 构成的 antichain 语义等价。

## 3. P025-T264 —— exact operation quotient

对 joint MAY 或 joint MUST membership semantics，两个 raw required sets operation-equivalent 当且仅当

\[
\boxed{
S\sim T
\iff
\alpha(S)=\alpha(T).
}
\]

等价地，

\[
\downarrow S=\downarrow T.
\]

因此 coarsest natural query representation 不是 raw subset / raw label list，而是一个 labelled antichain normal form。

这是直接发生在 operation-language 侧的 quotient；exact state representation 可以完全不变。

## 4. P025-D45 —— essential arity

定义 semantic / essential arity

\[
\boxed{e(S):=|\alpha(S)|.}
\]

则

\[
\boxed{e(S)\le\operatorname{width}(P).}
\]

若 declared future 允许 raw size 至多 \(k\) 的 queries，则 worst-case essential arity 精确为

\[
\boxed{
\min\{k,\operatorname{width}(P)\}.
}
\]

上界来自 \(\alpha(S)\) 是 antichain 且 \(|\alpha(S)|\le|S|\)；tightness 由取一个大小为 \(\min(k,w(P))\) 的 antichain 得到。

## 5. Exact extremes

### Chain

若 \(P\) 是 chain，每个非空 joint query 都 collapse 为唯一最大 label：

\[
\boxed{e(S)=1.}
\]

因此任意长 raw conjunction 的 semantic arity 都只有 1。

### Antichain

若 \(P\) 自身就是 antichain，则

\[
\alpha(S)=S,
\]

没有任何 arity compression。

它们是两个极端几何。

## 6. Query-class count

raw arity 不超过 \(k\) 的 queries，其 semantic equivalence classes 与 \(P\) 中大小不超过 \(k\) 的 antichains 一一对应。

所以 operation-language state count 是

\[
\boxed{
N_{\rm query}(k)
=
\#\{A\subseteq P:A\text{ antichain},\ |A|\le k\}.
}
\]

它可能远小于

\[
\sum_{j=0}^{k}\binom{|P|}{j}.
\]

对 chain，只要 \(k\ge1\)，总数始终只有 \(1+|P|\)；对 antichain 则完全没有 reduction。

## 7. 与 Stage 106 的关系

Stage 106 已证明：future semantics 增强时，可以只细化 **operation quotient** 而不细化 state quotient。

Stage 119 给出互补方向：在任何 state refinement 之前，relation geometry 本身就可能让 raw operation language 过精。被支配的 required labels 会在 ideal law 下自动 collapse。

因此 future precision 至少存在两个独立的 reduction axes：

\[
\boxed{
\text{state quotient}
\quad\text{与}\quad
\text{operation/query quotient}.
}
\]

二者都不能从 raw syntax 直接推断。

## 8. 与 A4 的关系

A4 拥有 witness / correspondence semantics。Stage 119 不替代 A4 witness spectra。它只说明：当 witnesses 是 declared poset 的 ideals 时，在查询任何 MAY/MUST support object 之前，应先把 joint-query syntax 规范成 antichain。

因此 A4 实际看到的 effective witness arity 可以从 raw \(k\) 降到至多 \(\min(k,w(P))\)。

## 9. Prior-art 边界

down-closures、maximal antichains 与 dominated constraints redundancy 都是经典 poset facts。这里不主张一般数学新颖。

项目侧结果是 exact operation-language precision reading，以及它与 P025/A2/A4 future-quotient hierarchy 的集成。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

新增：

- `src/enterprise_math/poset_joint_query_normal.py`；
- `tests/test_poset_joint_query_normal.py`。

executable layer 验证 chain collapse、antichain non-collapse、dominated raw queries 的 exact future equivalence、ideal-membership reconstruction，以及 worst-case essential-arity law。

## 11. 下一前沿

下一步应把 Stage 118 与 Stage 119 合并：bounded raw arity \(k\) 真正诱导的 witness skeleton 应由 antichain query classes 索引，而不是 arbitrary subsets。relevant precision resource 应联合依赖 query cap \(k\)、poset width，以及 admissible family 实际实现的 antichain spectrum。
