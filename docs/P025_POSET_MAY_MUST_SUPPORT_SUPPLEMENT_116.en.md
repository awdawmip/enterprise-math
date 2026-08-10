# P025 Supplement 116 — Poset MAY/MUST Support

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-poset-observable-stage113`  
Depends on: P025 Supplements 113–115; canonical A4 admissible-support boundary  
Hard block: `NONE`

## 1. Leaving the single-valued ideal world

Supplements 113–115 assumed that one coarse state determines one exact order ideal. Stage 116 removes that assumption.

Let

\[
\varnothing\ne\mathcal F\subseteq J(P)
\]

be the family of exact ideals still admissible under one coarse state.

Pointwise membership now naturally splits into two future languages:

- `MUST(p)`: every admissible ideal contains \(p\);
- `MAY(p)`: at least one admissible ideal contains \(p\).

## 2. P025-T260 — exact pointwise MAY/MUST state

Define

\[
\boxed{
L(\mathcal F):=\bigcap_{I\in\mathcal F}I,
\qquad
U(\mathcal F):=\bigcup_{I\in\mathcal F}I.
}
\]

Arbitrary intersections and unions of order ideals are order ideals, so

\[
\boxed{L(\mathcal F)\subseteq U(\mathcal F),\qquad L,U\in J(P).}
\]

For every label \(p\in P\):

\[
\boxed{
\operatorname{MUST}(p)\iff p\in L,
}
\]

and

\[
\boxed{
\operatorname{MAY}(p)\iff p\in U.
}
\]

Therefore two admissible families have identical answers to **all pointwise MAY/MUST membership queries** iff they have the same nested ideal pair

\[
\boxed{(L,U).}
\]

This is the coarsest semantic state for that declared pointwise language.

## 3. Exact boundary representation

By Supplements 113–114, each of the two ideals is represented exactly by its maximal antichain boundary:

\[
\boxed{
(\partial L,\partial U).
}
\]

Thus pointwise uncertainty does not require storing the whole family \(\mathcal F\). It requires two nested support envelopes.

The three pointwise statuses are

\[
\boxed{
\begin{cases}
\text{MUST},&p\in L,\\
\text{MAY but not MUST},&p\in U\setminus L,\\
\text{IMPOSSIBLE},&p\notin U.
\end{cases}}
\]

## 4. P025-C41 — identical MAY/MUST supports can hide joint correlation

Take the two-element antichain

\[
P=\{a,b\}.
\]

Consider

\[
\mathcal F_1=\big\{\{a\},\{b\}\big\}
\]

and

\[
\mathcal F_2=\big\{\varnothing,\{a,b\}\big\}.
\]

Both have

\[
L=\varnothing,
\qquad
U=\{a,b\}.
\]

Hence their pointwise MAY/MUST signatures are identical:

\[
a:\text{MAY},
\qquad
b:\text{MAY}.
\]

But the joint future

> MAY \(a\) and \(b\) hold simultaneously in one admissible exact state?

separates them:

\[
\mathcal F_1:\text{NO},
\qquad
\mathcal F_2:\text{YES}.
\]

Therefore

\[
\boxed{
\text{pointwise support envelopes}
\neq
\text{joint witness/correlation state}.
}
\]

This is the precise point where A4 correspondence information becomes necessary.

## 5. Relation to A4

A4 already owns finite multivalued relations, MAY/MUST support, witness spectra and correspondence structure. Stage 116 therefore does **not** claim a new generic MAY/MUST theorem.

Its role is a P025 pressure test showing the exact transition:

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

The counterexample demonstrates why A4 cannot be replaced by two ordinary support sets when the future language asks joint witness questions.

## 6. Precision hierarchy

For this finite poset specialization, declared futures produce a strict hierarchy:

1. selected exact membership on \(Q\): one query ideal \(I\cap Q\);
2. pointwise MAY/MUST uncertainty: nested pair \((L,U)\);
3. joint MAY/MUST/witness questions: require additional correlation/correspondence information about \(\mathcal F\).

Thus increasing the future language can change not only the amount of state retained but its **type**:

\[
\boxed{
\text{ideal boundary}
\longrightarrow
\text{two support boundaries}
\longrightarrow
\text{relation/correspondence state}.
}
\]

## 7. Prior-art discipline

Union/intersection envelopes, MAY/MUST semantics and relational witness information are standard set/lattice/relation concepts. No generic novelty claim is made.

The project-side result is the exact finite transition and counterexample inside the P025 future-precision pressure test. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 8. Executable assets

Added:

- `src/enterprise_math/poset_may_must_support.py`;
- `tests/test_poset_may_must_support.py`.

The executable layer verifies ideal closure of MAY/MUST envelopes, pointwise status, singleton exact-state recovery, and an exact same-support/different-joint-witness collision.

## 9. Next frontier

The next question is how much correlation information is actually required. Full storage of \(\mathcal F\) is generally excessive. For a declared family of joint queries, we should derive the coarsest correlation signature: pairwise co-activation, bounded-arity witness hyperedges, or the full admissible correspondence only when the future language truly asks for it.
