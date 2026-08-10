# P025 Supplement 121 — Witness-Count Zeta Inversion

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-witness-count-stage121`  
Depends on: P025 Supplements 117–120; canonical A4 witness-spectrum boundary  
Hard block: `NONE`

## 1. From existence to multiplicity

Supplements 117–120 ask whether a joint witness exists. Stage 121 strengthens the future language: how many exact witnesses realize a required label set?

Let `P` be a finite observation poset and let exact witness states be order ideals `I in J(P)`. Allow a nonnegative integer multiplicity

\[
w:J(P)\to\mathbf N.
\]

The ordinary set-family case is the special case `w(I) in {0,1}`.

## 2. P025-D47 — witness-count response

For a required label set `S subseteq P`, define

\[
\boxed{
c(S):=\sum_{I\supseteq S}w(I).
}
\]

Because every exact witness is an ideal,

\[
\boxed{
c(S)=c(\downarrow S)=c(\alpha(S)),}
\]

where

\[
\alpha(S)=\operatorname{Max}_P(S).
\]

Thus the Stage-119 antichain operation quotient survives unchanged under counting semantics.

## 3. P025-T267 — upper-zeta transform

For every ideal `K in J(P)`,

\[
\boxed{
c(K)=\sum_{I\in J(P):\ K\subseteq I}w(I).}
\]

This is exactly the upper zeta transform of the multiplicity function on the finite ideal lattice `J(P)`.

Hence the entire count future is an incidence-algebra coordinate chart on witness multiplicity state.

## 4. P025-T268 — exact inversion

Order ideals by decreasing cardinality. Then

\[
\boxed{
w(K)=c(K)-\sum_{I\supsetneq K}w(I).}
\]

The right side uses only multiplicities of strict supersets, already recovered at earlier descending steps.

Therefore the full ideal-count table determines the exact multiplicity function uniquely:

\[
\boxed{
(c(K))_{K\in J(P)}
\Longleftrightarrow
(w(I))_{I\in J(P)}.
}
\]

This is ordinary Möbius inversion on `J(P)`, implemented without needing an explicit closed formula for the Möbius function.

## 5. Exact-family recovery

If `w` is Boolean, then

\[
\mathcal F=\{I:w(I)=1\}
\]

is recovered exactly from the count table.

Thus witness counts restore information that existential joint-MAY semantics deliberately discards. In Supplement 117, nonmaximal admissible ideals can be invisible to all existential support queries; in Stage 121 they reappear through their contribution to the zeta counts.

## 6. Count semantics still uses antichain query normal forms

The stronger observable does not undo the operation-side collapse. A raw conjunction such as

\[
\{x_1,\ldots,x_m\}
\]

first reduces to the maximal incomparable requirements `alpha(S)` and only then evaluates a count.

Hence witness identity precision and raw query syntax remain distinct resources:

\[
\boxed{
\text{stronger state observable}
\not\Rightarrow
\text{undo query quotient}.
}
\]

## 7. Prior-art discipline

Finite-poset zeta transforms, incidence algebras and Möbius inversion are classical prior mathematics. P025 claims no generic novelty for them.

The project-side result is the exact placement of witness-count semantics inside the existing P025/A2/A4 precision hierarchy and its executable compatibility with the antichain operation quotient. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 8. Executable assets

Added:

- `src/enterprise_math/poset_witness_count_zeta.py`;
- `tests/test_poset_witness_count_zeta.py`.

The executable layer verifies zeta transformation, exact descending inversion, Boolean-family recovery, total count at the empty query, and equality of counts for raw queries with the same maximal-antichain normal form.

## 9. Next frontier

Supplement 120 proves existential joint-membership semantics saturate at poset width. Stage 122 asks whether exact count reconstruction has the same horizon and whether that horizon is sharp. The parity split of the Boolean lattice gives a natural candidate lower-bound construction.
