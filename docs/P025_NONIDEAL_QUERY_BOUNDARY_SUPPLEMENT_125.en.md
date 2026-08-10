# P025 Supplement 125 — Exact Ideal-Law Boundary for Query Normalization

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-nonideal-boundary-stage125`  
Depends on: P025 Supplements 119–124  
Hard block: `NONE`

## 1. Question

Stages 119–124 use the poset law

\[
S\subseteq I
\iff
\operatorname{Max}_P(S)\subseteq I
\]

for exact states `I` that are order ideals. Stage 125 removes the ideal assumption while keeping the same ambient poset labels.

The goal is to identify whether poset width alone causes query-arity saturation.

## 2. P025-T274 — exact iff boundary

Let `X subseteq P` be an arbitrary Boolean exact state. The following are equivalent:

1. `X` is an order ideal of `P`;
2. for every required set `S subseteq P`,
   \[
   \boxed{
   S\subseteq X
   \iff
   \operatorname{Max}_P(S)\subseteq X;
   }
   \]
3. whenever `x<=y` and `y in X`, then `x in X`.

The equivalence of (1) and (3) is the definition of downward closure. `(1)->(2)` is the Stage-119 normalization theorem.

For `(2)->(3)`, take a comparable pair `x<y` and the raw query

\[
S=\{x,y\}.
\]

Its maximal antichain is

\[
\operatorname{Max}(S)=\{y\}.
\]

If `y in X`, condition (2) forces `{x,y} subseteq X`, hence `x in X`.

Therefore

\[
\boxed{
\text{maximal-antichain query normalization is universally safe}
\iff
\text{the exact state obeys the ideal law}.
}
\]

## 3. Minimal width-one failure

Take the two-element chain

\[
a<b,
\qquad
\operatorname{width}(P)=1,
\]

but allow the non-ideal exact state

\[
X=\{b\}.
\]

Then

\[
\{a,b\}\nsubseteq X
\]

while

\[
\operatorname{Max}(\{a,b\})=\{b\}\subseteq X.
\]

So the width-one saturation statement fails immediately once downward closure is removed.

Hence

\[
\boxed{
\text{poset width alone is not the source of Stage-120 saturation}.
}
\]

The real source is **order relation + exact-state closure under that relation**.

## 4. Pairwise defect certificate

If `X` is not an ideal, there exists a pair

\[
x<y,
\qquad
y\in X,
\qquad x\notin X.
\]

That one pair is already an exact certificate that antichain query normalization fails:

\[
\{x,y\}\not\subseteq X,
\qquad
\{y\}\subseteq X.
\]

Thus failure of the ideal law never requires a high-arity counterexample; it is witnessed at arity two.

## 5. Architectural consequence

The Stage-120 width horizon has a hidden legality condition. It should be read as

\[
\boxed{
\text{relation geometry}
+
\text{state closure under that relation}
\Longrightarrow
\text{arity collapse bounded by width}.
}
\]

A label order that is merely present in metadata does not license operation-language collapse.

This is parallel to FQ-006 partial-operation legality: structural compression is safe only when the relevant legality/closure condition is preserved.

## 6. Relation to A2/A4

A2 owns safe declared-future quotients. A4 owns arbitrary finite correspondences. Stage 125 is a negative-boundary specialization showing that an A4 correspondence cannot inherit Stage-120 poset-width conclusions merely because its labels happen to carry an external partial order.

The exact-state fibers themselves must respect that order.

## 7. Prior-art discipline

Order ideals and downward closure are elementary poset theory. No generic novelty claim is made.

The project-side result is the exact hypothesis boundary for the earlier P025 precision compiler and its executable minimal counterexample. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 8. Executable assets

Added:

- `src/enterprise_math/nonideal_query_boundary.py`;
- `tests/test_nonideal_query_boundary.py`.

The executable layer verifies the iff boundary, the width-one chain counterexample, pairwise defect certificates, and valid ideal boundary cases.

## 9. Next frontier

If an externally supplied order is unsafe, a family of exact states still induces its own implication relation: `x` is semantically below `y` when every exact state containing `y` also contains `x`. Stage 126 derives that maximal safe preorder and its quotient poset.
