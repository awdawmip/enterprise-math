# P025 补充 117 —— Joint-MAY Witness Complex

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-poset-observable-stage113`  
依赖：P025 补充 116；canonical A4 correspondence boundary  
硬阻断：`NONE`

## 1. Pointwise support 不是 uncertainty compression 的终点

补充 116 已证明，一个非空 admissible ideal family

\[
\mathcal F\subseteq J(P)
\]

对所有 pointwise MAY/MUST membership queries 可以 exact collapse 为

\[
(L,U),
\]

但这对 nested supports 会丢失 joint witness correlation。

Stage 117 寻找 existential **joint-MAY** query 的最粗自然对象：

> 是否存在一个 admissible exact ideal，同时包含 \(S\) 中全部 labels？

## 2. P025-D42 —— joint-MAY complex

定义

\[
\boxed{
\mathcal K_{\mathcal F}
:=
\{S\subseteq P:\exists I\in\mathcal F,\ S\subseteq I\}.
}
\]

等价地，

\[
\boxed{
\mathcal K_{\mathcal F}
=
\bigcup_{I\in\mathcal F}2^I.
}
\]

它对 subset inclusion 向下闭合，所以是一个 abstract simplicial complex。

对任意有限 label set \(S\)：

\[
\boxed{
S\text{ jointly MAY}
\iff
S\in\mathcal K_{\mathcal F}.
}
\]

因此 \(\mathcal K_{\mathcal F}\) 正是所有 existential joint-MAY queries 的 semantic signature。

## 3. P025-T261 —— maximal admissible ideals 是 exact generators

记

\[
\operatorname{Max}_{\subseteq}(\mathcal F)
\]

为按 inclusion 极大的 admissible ideals。

则

\[
\boxed{
\mathcal K_{\mathcal F}
=
\bigcup_{M\in\operatorname{Max}_{\subseteq}(\mathcal F)}2^M.
}
\]

每个 nonmaximal admissible ideal 都被某个 maximal ideal 包含，因此不会贡献新的 joint-MAY face。

反过来，\(\mathcal K_{\mathcal F}\) 的 maximal faces 恰好就是

\[
\boxed{
\operatorname{Max}_{\subseteq}(\mathcal F).
}
\]

所以 inclusion-antichain of maximal admissible ideals 是所有 joint-MAY futures 的 exact finite generator。

## 4. P025-T262 —— 所有 joint MAY/MUST queries 只需 `(L, Max(F))`

joint MUST 仍然简单：

\[
S\text{ jointly MUST}
\iff
S\subseteq L,
\qquad
L=\bigcap_{I\in\mathcal F}I.
\]

因此，对**所有 finite joint MAY 与 finite joint MUST membership queries**，exact semantic state 是

\[
\boxed{
\Sigma_{\rm joint}(\mathcal F)
=
\left(
L,
\operatorname{Max}_{\subseteq}(\mathcal F)
\right).
}
\]

它严格比 pointwise pair \((L,U)\) 更细，因为 maximal faces 记录哪些 labels 能在同一个 admissible exact state 中共同出现。

## 5. Nonmaximal exact states 仍可能完全不可见

joint MAY/MUST state 仍然不是 exact admissible family。

在三元素 antichain \(P=\{a,b,c\}\) 上，令

\[
\mathcal F_1
=
\{\{a,b,c\},\{a\},\{b\}\}
\]

以及

\[
\mathcal F_2
=
\{\{a,b,c\},\{a\},\{c\}\}.
\]

二者都有

\[
L=\varnothing,
\qquad
\operatorname{Max}_{\subseteq}(\mathcal F_i)
=
\{\{a,b,c\}\}.
\]

所以所有 joint MAY/MUST membership queries 都一致。但 exact-state future

> `\{b\}` 本身是否是 admissible exact state？

能区分二者。

因此

\[
\boxed{
\text{existential/universal joint support}
\neq
\text{exact family identity / witness multiplicity structure}.
}
\]

## 6. Precision-type ladder

poset pressure test 现在得到一条 exact progression：

\[
\boxed{
\begin{array}{ccl}
\text{exact membership} &\to& \text{one ideal boundary},\\
\text{pointwise MAY/MUST} &\to& (L,U),\\
\text{joint MAY/MUST} &\to& (L,\operatorname{Max}\mathcal F),\\
\text{exact witness identity/counts} &\to& \text{finer correspondence data}.
\end{array}}
\]

state type 会随 declared future language 改变；不存在一条 scalar precision axis 能完整排列这些层。

## 7. 与 A4 的关系

A4 已拥有 generic admissible-support 与 correspondence algebra。simplicial complexes、maximal faces、witness hypergraphs 都属于 prior mathematics。

所以 Stage 117 是 specialization / pressure test。可复用信息是：coarse multivalued state 往往可以比 full admissible family 更粗，但正确压缩取决于 future 到底询问 pointwise support、joint existential witness，还是 exact witness identity。

## 8. 可执行资产

新增：

- `src/enterprise_math/poset_joint_may_complex.py`；
- `tests/test_poset_joint_may_complex.py`。

executable layer 验证 maximal-face generation、exact joint-MAY faces、MUST intersection，以及 same-joint-signature / different-exact-family collision。

## 9. 下一前沿

对于 bounded-arity joint queries，full maximal ideals 可能仍然过精。下一自然对象是只保留到 arity \(k\) 的 truncated witness complex，其 state complexity 由 relevant hypergraph skeleton 控制，而不是 full admissible family。后续应直接与 A4 witness spectra 对照，而不是升级成另一套 generic correspondence theory。
