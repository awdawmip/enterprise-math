# P025 Supplement 117 — Joint-MAY Witness Complex

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-poset-observable-stage113`  
Depends on: P025 Supplement 116; canonical A4 correspondence boundary  
Hard block: `NONE`

## 1. Pointwise support is not the end of uncertainty compression

Supplement 116 proves that a nonempty admissible ideal family

\[
\mathcal F\subseteq J(P)
\]

is compressed exactly to

\[
(L,U)
\]

for all pointwise MAY/MUST membership queries, but this pair loses joint witness correlation.

Stage 117 asks for the coarsest natural object for existential **joint-MAY** queries

> is there one admissible exact ideal containing every label in \(S\)?

## 2. P025-D42 — joint-MAY complex

Define

\[
\boxed{
\mathcal K_{\mathcal F}
:=
\{S\subseteq P:\exists I\in\mathcal F,\ S\subseteq I\}.
}
\]

Equivalently,

\[
\boxed{
\mathcal K_{\mathcal F}
=
\bigcup_{I\in\mathcal F}2^I.
}
\]

This is downward closed under subset inclusion, hence an abstract simplicial complex.

For every finite label set \(S\),

\[
\boxed{
S\text{ is jointly MAY}
\iff
S\in\mathcal K_{\mathcal F}.
}
\]

So \(\mathcal K_{\mathcal F}\) is exactly the semantic signature for all existential joint-MAY queries.

## 3. P025-T261 — maximal admissible ideals are the exact generators

Let

\[
\operatorname{Max}_{\subseteq}(\mathcal F)
\]

be the inclusion-maximal admissible ideals.

Then

\[
\boxed{
\mathcal K_{\mathcal F}
=
\bigcup_{M\in\operatorname{Max}_{\subseteq}(\mathcal F)}2^M.
}
\]

Every nonmaximal admissible ideal is contained in a maximal one and contributes no new joint-MAY face.

Conversely, the maximal faces of \(\mathcal K_{\mathcal F}\) are exactly

\[
\boxed{
\operatorname{Max}_{\subseteq}(\mathcal F).
}
\]

Therefore the inclusion-antichain of maximal admissible ideals is an exact finite generator for all joint-MAY futures.

## 4. P025-T262 — all joint MAY/MUST queries need `(L, Max(F))`

Joint MUST remains simple:

\[
S\text{ is jointly MUST}
\iff
S\subseteq L,
\qquad
L=\bigcap_{I\in\mathcal F}I.
\]

Hence the exact semantic state for **all finite joint MAY and all finite joint MUST membership queries** is

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

This is strictly richer than the pointwise pair \((L,U)\), because the maximal faces encode which labels can coexist in one admissible exact state.

## 5. Nonmaximal exact states can still be invisible

The joint MAY/MUST state is not the exact admissible family.

On the three-element antichain \(P=\{a,b,c\}\), let

\[
\mathcal F_1
=
\{\{a,b,c\},\{a\},\{b\}\}
\]

and

\[
\mathcal F_2
=
\{\{a,b,c\},\{a\},\{c\}\}.
\]

Both satisfy

\[
L=\varnothing,
\qquad
\operatorname{Max}_{\subseteq}(\mathcal F_i)
=
\{\{a,b,c\}\}.
\]

Therefore every joint MAY/MUST membership query agrees. Yet the exact-state future

> is \(\{b\}\) itself an admissible exact state?

separates the two families.

Thus

\[
\boxed{
\text{existential/universal joint support}
\neq
\text{exact family identity / witness multiplicity structure}.
}
\]

## 6. Precision-type ladder

The poset pressure test now gives the exact progression

\[
\boxed{
\begin{array}{ccl}
\text{exact membership} &\to& \text{one ideal boundary},\\
\text{pointwise MAY/MUST} &\to& (L,U),\\
\text{joint MAY/MUST} &\to& (L,\operatorname{Max}\mathcal F),\\
\text{exact witness identity/counts} &\to& \text{finer correspondence data}.
\end{array}}
\]

The state type changes with the declared future language; there is no single scalar precision axis covering these levels.

## 7. Relation to A4

A4 already owns generic admissible-support and correspondence algebra. Simplicial complexes, maximal faces and witness hypergraphs are prior mathematics.

Stage 117 is therefore a specialization/pressure test. Its reusable message is that a coarse multivalued state can often be compressed below the full admissible family, but the correct compression depends sharply on whether the future asks pointwise support, joint existential witnesses, or exact witness identity.

## 8. Executable assets

Added:

- `src/enterprise_math/poset_joint_may_complex.py`;
- `tests/test_poset_joint_may_complex.py`.

The executable layer verifies maximal-face generation, exact joint-MAY faces, MUST intersection, and a same-joint-signature/different-exact-family collision.

## 9. Next frontier

For bounded-arity joint queries, full maximal ideals may still be overprecise. The natural next object is the truncated witness complex up to arity \(k\), with state complexity controlled by the relevant hypergraph skeleton rather than the full admissible family. This should be compared directly with A4 witness spectra rather than promoted as a new generic correspondence theory.
