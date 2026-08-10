# P025 补充 118 —— Bounded-Arity Witness Skeleton

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-poset-observable-stage113`  
依赖：P025 补充 117；canonical A4 witness-spectrum boundary  
硬阻断：`NONE`

## 1. Full joint-MAY 仍可能过精

补充 117 已证明：所有 existential joint-MAY queries 可以由 joint-MAY complex

\[
\mathcal K_{\mathcal F}
\]

或者其 maximal faces 精确编码。

但 declared future language 可能只询问某个 bounded arity

\[
1\le k\le|P|
\]

以内的 joint witnesses。此时保留所有 high-arity witness faces 就是过精。

## 2. P025-D43 —— truncated witness complex

定义 arity-\(k\) truncation

\[
\boxed{
\mathcal K_{\mathcal F}^{(\le k)}
:=
\{S\in\mathcal K_{\mathcal F}:|S|\le k\}.
}
\]

对 declared future

\[
S\text{ 是否 jointly MAY？},
\qquad |S|\le k,
\]

这个 truncated complex 就是 exact semantic signature。

## 3. P025-T263 —— maximal truncated faces 是 exact generators

令

\[
\boxed{
H_k
:=
\operatorname{Max}_{\subseteq}
\mathcal K_{\mathcal F}^{(\le k)}.
}
\]

则

\[
\boxed{
\mathcal K_{\mathcal F}^{(\le k)}
=
\bigcup_{F\in H_k}2^F.
}
\]

因此 \(H_k\) 是所有 arity 不超过 \(k\) 的 joint-MAY queries 的 exact finite generator。

## 4. Exact arity ladder

该结构在 pointwise support 与 full joint complex 之间连续插值。

### `k=1`

\[
H_1
\]

就是 singleton MAY labels 的集合，等价于 ordinary MAY support \(U\)。

### `k=2`

\[
H_2
\]

是 pairwise co-activation graph 的 maximal edge / vertex data。它能区分 pointwise support 完全相同但 pairwise coexistence 不同的 coarse states。

### 一般 `k`

\[
H_k
\]

是 bounded-rank witness hypergraph / simplicial skeleton。

### full arity

当

\[
k=|P|
\]

时恢复

\[
\boxed{
H_{|P|}=\operatorname{Max}_{\subseteq}(\mathcal F).
}
\]

## 5. Strict arity separation

在三元素 antichain \(\{a,b,c\}\) 上，令

\[
\mathcal F
=
\{\{a,b\},\{a,c\},\{b,c\}\}.
\]

每个 singleton 都 MAY，每个 pair 都 jointly MAY。因此 `k=2` future 看不到任何缺失 pair。

但

\[
\{a,b,c\}
\]

并不 jointly MAY。所以 `k=3` language 严格比 `k=2` 更细。

因此 pairwise witness information 一般不能 collapse 成 arbitrary joint witness information。

## 6. Worst-case state count 边界

若 ambient poset 是 \(n\)-元素 antichain，则任意 subset 都是 ideal，任意 simplicial witness complex 都可以出现。因此 maximal truncated faces 数量在 worst case 可达到标准 Sperner-layer 尺度

\[
\boxed{
\binom{n}{\min(k,\lfloor n/2\rfloor)}
}.
\]

这是 prior combinatorics，不是新的 P025 theorem。它的架构含义是：bounded witness arity 是真实的 precision resource；即使 label universe 不变，增大 \(k\) 也可能大幅增加 required correlation state。

## 7. 与 A4 的关系

A4 已拥有 generic witness spectra 与 multivalued correspondence。Stage 118 应作为 specialization / pressure test：

\[
\boxed{
\text{declared witness arity}
\Longrightarrow
\text{required hypergraph skeleton depth}.
}
\]

它给出一个 exact 例子：future-language complexity 改变的是 **relation state 的 arity**，而不只是 scalar observation 的精细程度。

## 8. Prior-art 边界

simplicial complexes、hypergraph skeletons、maximal faces 与 Sperner bounds 都是经典数学。这里不主张一般理论新颖。

项目侧结果是 P025/A4 pressure test 中的 exact future-relative witness-arity compiler。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 9. 可执行资产

新增：

- `src/enterprise_math/poset_bounded_witness_skeleton.py`；
- `tests/test_poset_bounded_witness_skeleton.py`。

executable layer 验证 `k=1` MAY-support reduction、pairwise correlation、full-arity recovery、maximal-face regeneration，以及 strict `k=2` vs `k=3` separation。

## 10. 下一前沿

下一问题是 poset order 本身能否降低 witness arity。对 ideal states，一个 required label set \(S\) 与它的 down-closure \(\downarrow S\) 有相同 joint-MAY truth。因此被其他 labels 支配的元素可能是语义冗余。正确 local joint-query complexity 可能由 required set 的 antichain width / maximal generator count 决定，而不是 raw arity \(|S|\)。Stage 119 应把这个 antichain reduction 精确推出来。
