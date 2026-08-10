# P025 Supplement 115 — Task-Relative Poset Query Projection

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-poset-observable-stage113`  
Depends on: P025 Supplements 113–114; canonical A2 declared-future signature discipline  
Hard block: `NONE`

## 1. Full boundary is not always the right future state

Supplements 113–114 identify the maximal antichain boundary of an ambient ideal as the exact state for **full labelled membership** on a finite observation poset \(P\).

But a declared future language may query only a subset

\[
Q\subseteq P.
\]

Keeping the whole ambient boundary would then be unnecessarily precise.

## 2. P025-T257 — exact query projection

For an ambient ideal \(I\in J(P)\), define

\[
\boxed{
\pi_Q(I):=I\cap Q.
}
\]

Equip \(Q\) with the induced order from \(P\). Then \(I\cap Q\) is an order ideal of the induced poset \(Q\).

For the declared future consisting of all labelled membership queries

> is \(q\) active?

for every \(q\in Q\), two ambient ideals are future-equivalent exactly when

\[
\boxed{
I\sim_Q J
\iff
I\cap Q=J\cap Q.
}
\]

Thus \(\pi_Q\) is the coarsest semantic state for that declared membership language.

## 3. P025-T258 — every induced query ideal is realizable

The signature image is not merely a subset of \(J(Q)\). It is all of it:

\[
\boxed{
\pi_Q(J(P))=J(Q).
}
\]

Indeed, let \(K\in J(Q)\) and let \(A=\operatorname{Max}_Q(K)\). Then the ambient down-closure

\[
I:=\downarrow_P A
\]

satisfies

\[
I\cap Q=K.
\]

Therefore the exact query-state space is the ideal lattice of the induced query poset.

## 4. P025-T259 — task-relative boundary cost

By Supplement 114 applied to the induced query poset,

\[
\boxed{
\max_{I\in J(P)}
\left|
\operatorname{Max}_Q(I\cap Q)
\right|
=
\operatorname{width}(Q).
}
\]

The relevant precision-support cost is therefore controlled by the **query width**, not the ambient width.

In particular,

\[
\boxed{
\operatorname{width}(Q)=1
\Longrightarrow
\text{a scalar query rank is complete},
}
\]

even when \(P\) itself has large width.

## 5. Exact compression examples

### Diamond ambient poset

Let

\[
a<b<d,
\qquad
a<c<d,
\qquad b\parallel c.
\]

The ambient poset has width two. Full membership therefore needs a boundary that can contain both \(b\) and \(c\).

But for the declared query chain

\[
Q=\{a,d\},
\]

we have

\[
\operatorname{width}(Q)=1,
\]

and the query signature has only three states:

\[
\varnothing,
\{a\},
\{a,d\}.
\]

So a width-two ambient state collapses exactly to scalar rank for this future language.

### Wide antichain ambient poset

If \(P\) is an \(n\)-element antichain, it has \(2^n\) ideals and width \(n\). If the future asks only one label \(q\), then \(Q=\{q\}\) has only two ideal states and width one.

This is an arbitrarily large task-relative collapse.

## 6. Precision amount and support geometry are both future-relative

Supplements 107–112 showed that the observable algebra can change required state precision. Supplements 113–115 add a second effect: the future language can change the **shape of the support geometry** itself.

The correct object is therefore not a global scalar `precision level`. At minimum, one must distinguish:

\[
\boxed{
\text{ambient relation geometry}
\quad\text{from}\quad
\text{declared-query geometry}.
}
\]

The query poset may have smaller width, fewer ideal states, and a different antichain boundary than the ambient poset.

## 7. Relation to A2 and A4

A2 already owns the generic statement that a declared future language determines a future signature and therefore a task-relative quotient. Stage 115 is a **specialization/pressure test**, not a competing mother theorem.

A4 owns multivalued support/correspondence algebra. Stage 115 does not assert that every A4 support is an order ideal. It shows that when a declared observation family *does* have monotone poset semantics, task-relative support restriction is naturally an induced-ideal quotient with width controlled by the queried subposet.

## 8. Prior-art discipline

Restriction of order ideals to induced subposets and antichain boundaries are classical finite-poset facts. No generic novelty claim is made.

Project-side contribution is the exact task-relative precision reading and its executable connection to the previous P025 rank-path failure boundary. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/poset_query_projection.py`;
- `tests/test_poset_query_projection.py`.

The executable layer verifies exact query projection, surjectivity onto the induced ideal lattice, query-width cost, scalar recovery on a chain query inside a wider ambient poset, and strict reduction of a full boundary to a smaller query boundary.

## 10. Next frontier

The next unresolved layer is multivalued uncertainty. If a coarse state no longer determines one ideal but a **family of admissible ideals**, then full membership splits into MAY and MUST semantics. That is exactly where A4 correspondence algebra should enter. The next P025 pressure test should therefore stop pretending the state is single-valued and derive the minimal MAY/MUST boundary representation for a family of admissible ideals.
