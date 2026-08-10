# P025 Supplement 113 — Poset Observation Boundary

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-poset-observable-stage113`  
Depends on: P025 Supplements 109–112; canonical A2 future-signature discipline  
Hard block: `NONE`

## 1. Why Stage 113 changes the geometry

Stages 109–112 exploit one labelled total order of thresholds. At each node, the active threshold set is therefore a prefix, so one scalar merged rank reconstructs the entire incidence column.

Stage 113 removes exactly that hypothesis. Let

\[
(P,\le)
\]

be a finite partially ordered declared-observation family. A semantically admissible active set is an order ideal

\[
I\subseteq P,
\qquad
x\in I,\ y\le x\Longrightarrow y\in I.
\]

The question is what replaces one scalar rank when declared observables are genuinely incomparable.

## 2. P025-T253 — rank completeness iff the observation poset is a chain

Consider the cardinality observable

\[
q_{\rm rank}(I)=|I|
\]

on the finite ideal lattice \(J(P)\).

Then

\[
\boxed{
|I|\text{ distinguishes all order ideals}
\iff
P\text{ is a chain}.
}
\]

### Proof

If \(P\) is a chain with \(n\) elements, it has exactly one ideal of every size

\[
0,1,\ldots,n,
\]

so cardinality is complete.

Conversely, choose a linear extension of any non-chain finite poset. Its prefixes already give \(n+1\) distinct ideals. Because the poset is not a chain, choose incomparable elements \(x,y\) with \(x\) preceding \(y\) in the extension. The principal ideal \(\downarrow y\) contains \(y\) but not \(x\), so it cannot equal any extension prefix containing \(y\). Hence the poset has more than \(n+1\) ideals. Since ideal cardinalities take only the \(n+1\) values \(0,\ldots,n\), two distinct ideals have the same cardinality.

Thus the scalar merged-rank normal form is complete for full membership semantics exactly in the total-order case.

## 3. Minimal exact collision

Take the two-element antichain

\[
P=\{a,b\},
\qquad a\parallel b.
\]

Then

\[
I_a=\{a\},
\qquad
I_b=\{b\}
\]

satisfy

\[
|I_a|=|I_b|=1
\]

but answer the membership future `is a active?` differently.

So equal merged rank does not imply semantic equality once the declared observation geometry ceases to be a chain.

## 4. P025-T254 — maximal-antichain boundary is an exact state

For any finite ideal \(I\), define

\[
\boxed{\partial I:=\operatorname{Max}(I).}
\]

Then \(\partial I\) is an antichain and

\[
\boxed{I=\downarrow\partial I.}
\]

Moreover \(\partial I\) is unique. Hence finite order ideals and finite antichains are in bijection:

\[
\boxed{J(P)\cong \mathcal A(P)}
\]

as state sets via ideal ↔ maximal boundary.

This is classical finite-poset mathematics. The P025 pressure-test conclusion is narrower: when the total-order rank coordinate fails, the exact replacement state for full ideal-membership semantics is a labelled antichain boundary, not another scalar precision level.

## 5. Monotone node paths

Suppose node states grow monotonically:

\[
I_0\subseteq I_1\subseteq\cdots\subseteq I_h.
\]

Writing

\[
A_j=\partial I_j,
\]

the path can be represented entirely by antichain boundaries with the dominance order

\[
A\preceq B
\iff
\downarrow A\subseteq\downarrow B.
\]

Equivalently, every element of \(A\) lies below at least one element of \(B\).

Thus the total-order scalar rank path generalizes to a path in the antichain/ideal lattice.

## 6. Relation to A3/A4

This result does **not** identify A3 relation state or A4 admissible support with a poset ideal.

It gives a pressure-test boundary:

- total-order observation incidence → scalar prefix/rank coordinate is exact;
- partial-order observation incidence → scalar rank can be false;
- full membership semantics → relation-aware labelled boundary data are required.

A4 already owns finite multivalued support/correspondence algebra. Stage 113 should therefore be consumed as evidence that branching observation geometry naturally produces support/boundary states, not as a competing A4 mother theorem.

## 7. Prior-art discipline

Order ideals, antichains, linear extensions, and the ideal–antichain bijection are standard poset theory. P025 claims no novelty for those facts.

Project-side contribution is the exact boundary of the Stage109 merged-rank compiler and its use as a future-precision pressure test. Historical novelty of the synthesis remains `NOVELTY_UNVERIFIED`.

## 8. Executable assets

Added:

- `src/enterprise_math/poset_observation_boundary.py`;
- `tests/test_poset_observation_boundary.py`.

The executable layer checks finite-poset validity, ideal enumeration, rank completeness, exact equal-rank collisions, maximal-boundary reconstruction, antichain enumeration, and monotone boundary dominance.

## 9. Next frontier

1. compute the exact worst-case boundary storage in terms of poset width;
2. prove the antichain-boundary path representation is tight under full membership futures;
3. study future languages that query only selected observables and therefore permit coarser-than-full-boundary states;
4. connect the resulting MAY/MUST or membership projections to A4 without collapsing multivalued relations into one ideal;
5. identify the correct analogue of Stage112 state-relative precision when the local observation boundary has several incomparable directions.
