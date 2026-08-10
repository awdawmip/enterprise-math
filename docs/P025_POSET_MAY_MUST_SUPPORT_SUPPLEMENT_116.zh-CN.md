# P025 补充 116 —— Poset MAY/MUST Support

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-poset-observable-stage113`  
依赖：P025 补充 113–115；canonical A4 admissible-support boundary  
硬阻断：`NONE`

## 1. 离开 single-valued ideal 世界

补充 113–115 都假设一个 coarse state 决定一个 exact order ideal。Stage 116 移除这个假设。

令

\[
\varnothing\ne\mathcal F\subseteq J(P)
\]

表示同一个 coarse state 下仍然 admissible 的 exact ideals family。

pointwise membership 此时自然分裂成两个 future languages：

- `MUST(p)`：每个 admissible ideal 都包含 \(p\)；
- `MAY(p)`：至少一个 admissible ideal 包含 \(p\)。

## 2. P025-T260 —— exact pointwise MAY/MUST state

定义

\[
\boxed{
L(\mathcal F):=\bigcap_{I\in\mathcal F}I,
\qquad
U(\mathcal F):=\bigcup_{I\in\mathcal F}I.
}
\]

order ideals 对任意 intersection 与 union 都闭合，因此

\[
\boxed{L(\mathcal F)\subseteq U(\mathcal F),\qquad L,U\in J(P).}
\]

对每个 label \(p\in P\)：

\[
\boxed{\operatorname{MUST}(p)\iff p\in L,}
\]

以及

\[
\boxed{\operatorname{MAY}(p)\iff p\in U.}
\]

因此，两个 admissible families 对**所有 pointwise MAY/MUST membership queries** 给出完全相同答案，当且仅当它们具有相同 nested ideal pair

\[
\boxed{(L,U).}
\]

这就是该 declared pointwise language 的 coarsest semantic state。

## 3. Exact boundary representation

由补充 113–114，每个 ideal 都可由其 maximal antichain boundary 精确表示，所以 nested pair 可以写成

\[
\boxed{(\partial L,\partial U).}
\]

因此 pointwise uncertainty 不需要保存整个 family \(\mathcal F\)，只需要两个 nested support envelopes。

每个 label 只有三种 pointwise 状态：

\[
\boxed{
\begin{cases}
\text{MUST},&p\in L,\\
\text{MAY but not MUST},&p\in U\setminus L,\\
\text{IMPOSSIBLE},&p\notin U.
\end{cases}}
\]

## 4. P025-C41 —— identical MAY/MUST supports 可以隐藏 joint correlation

取二元素 antichain

\[
P=\{a,b\}.
\]

考虑

\[
\mathcal F_1=\big\{\{a\},\{b\}\big\}
\]

与

\[
\mathcal F_2=\big\{\varnothing,\{a,b\}\big\}.
\]

二者都有

\[
L=\varnothing,
\qquad
U=\{a,b\}.
\]

所以 pointwise MAY/MUST signature 完全相同：

\[
a:\text{MAY},
\qquad
b:\text{MAY}.
\]

但 joint future

> 是否存在一个 admissible exact state，使 \(a,b\) 同时成立？

能把它们分开：

\[
\mathcal F_1:\text{NO},
\qquad
\mathcal F_2:\text{YES}.
\]

因此

\[
\boxed{
\text{pointwise support envelopes}
\neq
\text{joint witness/correlation state}.
}
\]

这就是 A4 correspondence information 真正开始必要的精确位置。

## 5. 与 A4 的关系

A4 已拥有 finite multivalued relations、MAY/MUST support、witness spectra 与 correspondence structure。Stage 116 因此**不**主张一个新的 generic MAY/MUST theorem。

它在 P025 中承担的是 pressure test：给出 exact transition

\[
\boxed{
\text{single ideal}
\to
\text{admissible ideal family}
\to
(L,U)
\to
\text{joint-correlation deficit}.
}
\]

反例证明：当 future language 开始询问 joint witness 时，A4 不能被两个 ordinary support sets 替代。

## 6. Precision hierarchy

在这个 finite-poset specialization 中，declared future 形成严格层级：

1. selected exact membership on \(Q\)：一个 query ideal \(I\cap Q\)；
2. pointwise MAY/MUST uncertainty：nested pair \((L,U)\)；
3. joint MAY/MUST/witness queries：必须增加 \(\mathcal F\) 的 correlation / correspondence information。

所以 future language 增强时，不只是保留信息量增加，**state type 本身也会改变**：

\[
\boxed{
\text{ideal boundary}
\longrightarrow
\text{two support boundaries}
\longrightarrow
\text{relation/correspondence state}.
}
\]

## 7. Prior-art 边界

union/intersection envelopes、MAY/MUST semantics 与 relational witness information 都是标准 set/lattice/relation concepts。这里不主张一般理论新颖。

项目侧结果是 P025 future-precision pressure test 中的 exact finite transition 与 counterexample。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 8. 可执行资产

新增：

- `src/enterprise_math/poset_may_must_support.py`；
- `tests/test_poset_may_must_support.py`。

executable layer 验证 MAY/MUST envelopes 的 ideal closure、pointwise status、singleton exact-state recovery，以及 same-support / different-joint-witness 的 exact collision。

## 9. 下一前沿

下一问题是：究竟需要多少 correlation information？完整保存 \(\mathcal F\) 通常仍然过精。对 declared joint-query family，应继续寻找 coarsest correlation signature：pairwise co-activation、bounded-arity witness hyperedges，或者只有当 future language 真正要求时才保留 full admissible correspondence。
