# P025 补充 121 —— Witness-Count Zeta Inversion

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-witness-count-stage121`  
依赖：P025 补充 117–120；canonical A4 witness-spectrum boundary  
硬阻断：`NONE`

## 1. 从 existence 提升到 multiplicity

补充 117–120 询问 joint witness 是否存在。Stage 121 增强 future language：有多少 exact witnesses 能实现一个 required label set？

令 `P` 为有限 observation poset，exact witness states 是 order ideals `I in J(P)`。允许每个 ideal 带一个非负整数 multiplicity

\[
w:J(P)\to\mathbf N.
\]

普通 set-family 情形就是 `w(I) in {0,1}` 的特例。

## 2. P025-D47 —— witness-count response

对 required label set `S subseteq P`，定义

\[
\boxed{
c(S):=\sum_{I\supseteq S}w(I).
}
\]

因为每个 exact witness 都是 ideal，

\[
\boxed{c(S)=c(\downarrow S)=c(\alpha(S)),}
\]

其中

\[
\alpha(S)=\operatorname{Max}_P(S).
\]

所以 Stage 119 的 antichain operation quotient 在 counting semantics 下原封不动成立。

## 3. P025-T267 —— upper-zeta transform

对每个 ideal `K in J(P)`，

\[
\boxed{c(K)=\sum_{I\in J(P):K\subseteq I}w(I).}
\]

这正是有限 ideal lattice `J(P)` 上 multiplicity function 的 upper zeta transform。

因此整个 count future 是 witness multiplicity state 的 incidence-algebra coordinate chart。

## 4. P025-T268 —— exact inversion

按 cardinality 从大到小排列 ideals，则

\[
\boxed{w(K)=c(K)-\sum_{I\supsetneq K}w(I).}
\]

右侧只用 strict supersets 的 multiplicities，而它们在 descending process 中已经先恢复。

所以 full ideal-count table 唯一决定 exact multiplicity function：

\[
\boxed{(c(K))_{K\in J(P)}\Longleftrightarrow(w(I))_{I\in J(P)}.}
\]

这就是 `J(P)` 上的普通 Möbius inversion；实现层不需要显式闭式 Möbius function。

## 5. Exact-family recovery

若 `w` 是 Boolean，则

\[
\mathcal F=\{I:w(I)=1\}
\]

可由 count table 精确恢复。

因此 witness counts 恢复了 existential joint-MAY semantics 主动丢掉的信息。补充 117 中 nonmaximal admissible ideals 对所有 existential support queries 都可能不可见；Stage 121 中它们会通过 zeta counts 重新出现。

## 6. Count semantics 仍使用 antichain query normal form

更强的 observable 并不会撤销 operation-side collapse。一个 raw conjunction

\[
\{x_1,\ldots,x_m\}
\]

仍先压成 maximal incomparable requirements `alpha(S)`，再计算 count。

因此 witness identity precision 与 raw query syntax 仍是不同资源：

\[
\boxed{\text{stronger state observable}\not\Rightarrow\text{undo query quotient}.}
\]

## 7. Prior-art 边界

finite-poset zeta transforms、incidence algebras 与 Möbius inversion 都是经典 prior mathematics。P025 不主张其 generic novelty。

项目侧结果是 witness-count semantics 在既有 P025/A2/A4 precision hierarchy 中的 exact 定位，以及它与 antichain operation quotient 的 executable compatibility。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 8. 可执行资产

新增：

- `src/enterprise_math/poset_witness_count_zeta.py`；
- `tests/test_poset_witness_count_zeta.py`。

executable layer 验证 zeta transformation、exact descending inversion、Boolean-family recovery、empty query 的 total count，以及具有相同 maximal-antichain normal form 的 raw queries count 相等。

## 9. 下一前沿

补充 120 已证明 existential joint-membership semantics 在 poset width 处饱和。Stage 122 要判断 exact count reconstruction 是否具有同样 horizon，以及该 horizon 是否 sharp。Boolean lattice 的 parity split 是天然 lower-bound construction。
