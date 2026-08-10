# P025 补充 120 —— Antichain Witness Spectrum and Width Saturation

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-poset-observable-stage113`  
依赖：P025 补充 113–119；canonical A4 witness-spectrum boundary  
硬阻断：`NONE`

## 1. 合并 state-side 与 operation-side collapse

补充 118 按 raw witness arity 截断 joint-MAY precision；补充 119 又证明 raw required sets 自身仍然过精：每个 joint query 都等价于其 maximal-antichain normal form。

Stage 120 把这两个 collapse 合在一起。

## 2. P025-D46 —— antichain witness spectrum

令 \(\mathcal F\subseteq J(P)\) 非空，并固定 raw arity cap \(k\ge1\)。定义

\[
\boxed{
\mathcal W_k(\mathcal F)
:=
\{A\subseteq P:
A\text{ antichain},\ |A|\le k,\ \exists I\in\mathcal F\text{ with }A\subseteq I\}.
}
\]

对任意 raw joint query \(S\) 且 \(|S|\le k\)，有

\[
\boxed{
S\text{ jointly MAY}
\iff
\alpha(S)\in\mathcal W_k(\mathcal F),
}
\]

其中 \(\alpha(S)=\operatorname{Max}_P(S)\)。

所以 \(\mathcal W_k\) 是 **operation normalization 之后** bounded-arity joint-MAY 的 exact semantic signature。

## 3. Dominance closure 与 maximal generators

在 antichains 上定义

\[
A\preceq B
\iff
\downarrow A\subseteq\downarrow B.
\]

若 \(B\) jointly MAY 且 \(A\preceq B\)，则 \(A\) 也 jointly MAY。因此 \(\mathcal W_k\) 对 dominance 向下闭合。

令

\[
\boxed{
G_k:=\operatorname{Max}_{\preceq}\mathcal W_k.
}
\]

则 \(G_k\) 能恢复整个 bounded spectrum：

\[
\boxed{
A\in\mathcal W_k
\iff
\exists G\in G_k:\ A\preceq G.
}
\]

因此正确的 bounded correlation state 是一组 dominance-antichain generators，而不是 raw subset-query table。

## 4. P025-T265 —— width saturation

\(P\) 中任意 antichain 大小都不超过

\[
w:=\operatorname{width}(P).
\]

所以

\[
\boxed{
\mathcal W_k(\mathcal F)
=
\mathcal W_{\min(k,w)}(\mathcal F).
}
\]

特别地，

\[
\boxed{k\ge w\Longrightarrow\mathcal W_k=\mathcal W_w.}
\]

因此 raw witness arity 一旦超过 poset width，就不再产生任何新的 joint-membership semantics。

这是一个由 relation geometry 决定的 exact **precision horizon**。

## 5. P025-T266 —— chain 上所有 joint correlation collapse

若 \(P\) 是 chain，则 \(w(P)=1\)。每个非空 joint query 都等价于唯一 maximal label。

因此 pointwise MAY/MUST support 已经决定**所有 finite joint MAY/MUST membership queries**：

\[
\boxed{
\operatorname{width}(P)=1
\Longrightarrow
(L,U)\text{ 对所有 joint membership future 完备}.
}
\]

所以 Stage 116 的 correlation deficit 真正能够出生的必要条件是

\[
\boxed{\operatorname{width}(P)\ge2.}
\]

branching observation geometry 不只是一个 quantitative cost increase，而是 higher-arity membership correlation 的 exact genesis condition。

## 6. Full-arity recovery

当 \(k\ge w(P)\) 后，dominance-maximal witness generators 与 inclusion-maximal admissible ideals 的 boundaries 一致：

\[
\boxed{
G_k
=
\{\partial M:M\in\operatorname{Max}_{\subseteq}(\mathcal F)\}.
}
\]

所以 Stage 120 在先对 raw query 做 poset quotient 后，重新得到补充 117。

若 ambient poset 本身是 antichain，则 dominance 就是 ordinary subset inclusion，Stage 120 精确退化为补充 118 的 hypergraph / simplicial skeleton。

## 7. Precision-genesis hierarchy

组合结果给出更精确的架构：

\[
\boxed{
\begin{array}{ccl}
\text{poset width }1
&\Rightarrow&
\text{pointwise support 关闭全部 joint membership};\\
\text{poset width }w>1
&\Rightarrow&
\text{correlation 最多出生到 essential arity }w;\\
k\ge w
&\Rightarrow&
\text{witness-arity refinement 饱和}.
\end{array}}
\]

因此 correlation precision 由三个量联合决定：

1. declared raw query cap \(k\)；
2. ambient relation width \(w(P)\)；
3. realized admissible witness spectrum \(G_k\)。

不存在一个 scalar precision level 能同时表示这三类资源。

## 8. 与 A2/A4 的关系

A2 拥有 generic declared-future quotient；A4 拥有 generic multivalued support 与 witness spectra。Stage 120 是 pressure-test specialization：它说明 **relation geometry 可以在任何 A4-specific counting / witness identity 信息进入之前，先强制产生一个 finite witness-arity horizon**。

应当把它作为以下区分的证据：

\[
\boxed{
\text{raw operation arity}
\neq
\text{essential relation arity}
\neq
\text{realized witness-spectrum complexity}.
}
\]

## 9. Prior-art 边界

poset width、antichain dominance、simplicial complexes 与 maximal-face representations 都是经典数学。这里不主张 generic novelty。

项目侧贡献是把它们 exact 合成为 future-precision pressure test，并明确 width-saturation boundary。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

新增：

- `src/enterprise_math/poset_antichain_witness_spectrum.py`；
- `tests/test_poset_antichain_witness_spectrum.py`。

executable layer 验证 chain 在 arity one 即饱和、width-two 的严格 refinement、antichain geometry 下 raw hypergraph semantics 的恢复，以及 full-spectrum 从 maximal admissible-ideal boundaries 的恢复。

## 11. Natural generation boundary

补充 113–120 已形成一个完整结果族：

\[
\boxed{
\text{rank-path failure}
\to
\text{antichain boundary}
\to
\text{width cost}
\to
\text{task-relative query width}
\to
\text{MAY/MUST envelopes}
\to
\text{joint witness complex}
\to
\text{bounded arity}
\to
\text{antichain query quotient}
\to
\text{width saturation}.
}
\]

这里是自然 freeze point。下一 generation 应离开 pure ideal-membership model，去测试 witness identity/count multiplicity、non-ideal correspondences，或者多个 partial-order observation systems 的 composition。
