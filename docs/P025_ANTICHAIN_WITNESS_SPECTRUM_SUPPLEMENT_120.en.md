# P025 Supplement 120 — Antichain Witness Spectrum and Width Saturation

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-poset-observable-stage113`  
Depends on: P025 Supplements 113–119; canonical A4 witness-spectrum boundary  
Hard block: `NONE`

## 1. Combine state-side and operation-side collapses

Supplement 118 truncates joint-MAY precision by raw witness arity. Supplement 119 shows that raw required sets are themselves overprecise: every joint query is equivalent to its maximal-antichain normal form.

Stage 120 combines those two collapses.

## 2. P025-D46 — antichain witness spectrum

Let \(\mathcal F\subseteq J(P)\) be nonempty and fix a raw arity cap \(k\ge1\).

Define

\[
\boxed{
\mathcal W_k(\mathcal F)
:=
\{A\subseteq P:
A\text{ antichain},\ |A|\le k,\ \exists I\in\mathcal F\text{ with }A\subseteq I\}.
}
\]

For every raw joint query \(S\) with \(|S|\le k\),

\[
\boxed{
S\text{ jointly MAY}
\iff
\alpha(S)\in\mathcal W_k(\mathcal F),
}
\]

where \(\alpha(S)=\operatorname{Max}_P(S)\).

So \(\mathcal W_k\) is the exact bounded-arity joint-MAY signature **after operation normalization**.

## 3. Dominance closure and maximal generators

Order antichains by

\[
A\preceq B
\iff
\downarrow A\subseteq\downarrow B.
\]

If \(B\) is jointly MAY and \(A\preceq B\), then \(A\) is jointly MAY. Therefore \(\mathcal W_k\) is downward closed under dominance.

Let

\[
\boxed{
G_k:=\operatorname{Max}_{\preceq}\mathcal W_k.
}
\]

Then \(G_k\) regenerates the entire bounded spectrum:

\[
\boxed{
A\in\mathcal W_k
\iff
\exists G\in G_k:\ A\preceq G.
}
\]

Thus the correct bounded correlation state is a dominance-antichain of antichain generators, not a raw table of subset queries.

## 4. P025-T265 — width saturation

Every antichain in \(P\) has size at most

\[
w:=\operatorname{width}(P).
\]

Therefore

\[
\boxed{
\mathcal W_k(\mathcal F)
=
\mathcal W_{\min(k,w)}(\mathcal F).
}
\]

In particular,

\[
\boxed{
k\ge w\Longrightarrow\mathcal W_k=\mathcal W_w.}
\]

So increasing raw witness arity beyond the poset width cannot create new joint-membership semantics.

This is an exact **precision horizon** determined by relation geometry.

## 5. P025-T266 — chain collapse of all joint correlation

If \(P\) is a chain, then \(w(P)=1\). Hence every nonempty joint query is equivalent to one maximal label.

Therefore pointwise MAY/MUST support already determines **all finite joint MAY/MUST membership queries**:

\[
\boxed{
\operatorname{width}(P)=1
\Longrightarrow
(L,U)\text{ is complete for all joint membership futures}.
}
\]

So the Stage-116 correlation deficit can genuinely appear only when

\[
\boxed{\operatorname{width}(P)\ge2.}
\]

Branching observation geometry is not just a quantitative cost increase; it is the exact genesis condition for higher-arity membership correlation.

## 6. Full-arity recovery

Once \(k\ge w(P)\), the dominance-maximal witness generators agree with the boundaries of the inclusion-maximal admissible ideals:

\[
\boxed{
G_k
=
\{\partial M:M\in\operatorname{Max}_{\subseteq}(\mathcal F)\}.
}
\]

Thus Stage 120 recovers Supplement 117 after first quotienting raw queries by the poset law.

On an ambient antichain, dominance reduces to ordinary subset inclusion and Stage 120 reduces exactly to the hypergraph/simplicial skeleton of Supplement 118.

## 7. Precision-genesis hierarchy

The combined result gives a sharper architecture:

\[
\boxed{
\begin{array}{ccl}
\text{poset width }1
&\Rightarrow&
\text{pointwise support closes all joint membership};\\
\text{poset width }w>1
&\Rightarrow&
\text{correlation may appear up to essential arity }w;\\
k\ge w
&\Rightarrow&
\text{witness-arity refinement saturates}.
\end{array}}
\]

Thus correlation precision is controlled jointly by:

1. the declared raw query cap \(k\);
2. the ambient relation width \(w(P)\);
3. the realized admissible witness spectrum \(G_k\).

No one scalar precision level captures these three resources.

## 8. Relation to A2/A4

A2 owns generic declared-future quotients. A4 owns generic multivalued support and witness spectra. Stage 120 is a pressure-test specialization showing that **relation geometry can impose a finite witness-arity horizon before any A4-specific counting or witness identity data are considered**.

It should be consumed as evidence for separating:

\[
\boxed{
\text{raw operation arity}
\neq
\text{essential relation arity}
\neq
\text{realized witness-spectrum complexity}.
}
\]

## 9. Prior-art discipline

Poset width, antichain dominance, simplicial complexes and maximal-face representations are classical. No generic novelty claim is made.

Project-side contribution is the exact synthesis as a future-precision pressure test and the explicit width-saturation boundary. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added:

- `src/enterprise_math/poset_antichain_witness_spectrum.py`;
- `tests/test_poset_antichain_witness_spectrum.py`.

The executable layer verifies chain saturation at arity one, strict width-two refinement, antichain recovery of raw hypergraph semantics, and full-spectrum recovery from maximal admissible-ideal boundaries.

## 11. Natural generation boundary

Supplements 113–120 now form one coherent result family:

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

This is a natural freeze point. Any next generation should leave the pure ideal-membership model and test either witness identity/count multiplicity, non-ideal correspondences, or composition of several partial-order observation systems.
