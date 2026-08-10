# P025 Supplement 114 — Poset Boundary Width

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-poset-observable-stage113`  
Depends on: P025 Supplement 113  
Hard block: `NONE`

## 1. From failure to exact replacement cost

Supplement 113 proves that scalar ideal cardinality is complete for full membership futures exactly when the observation poset is a chain. The exact replacement state is the maximal antichain boundary

\[
\partial I=\operatorname{Max}(I).
\]

Stage 114 asks how large that boundary must become in the worst case.

## 2. P025-T255 — exact width law

Let \(P\) be a finite poset and let \(w(P)\) denote its width, the maximum size of an antichain.

Then

\[
\boxed{
\max_{I\in J(P)}|\partial I|
=
 w(P).
}
\]

### Proof

Every \(\partial I\) is an antichain, so

\[
|\partial I|\le w(P).
\]

Conversely, let \(A\) be a maximum antichain. The down-closure

\[
I_A:=\downarrow A
\]

is an order ideal and, because \(A\) is an antichain,

\[
\operatorname{Max}(I_A)=A.
\]

Hence the upper bound is attained.

Therefore the worst-case number of labelled boundary generators required for full ideal-membership semantics is exactly the poset width.

## 3. Total-order recovery

A finite poset has width one iff it is a chain. Hence

\[
\boxed{
 w(P)=1
\iff
\text{Stage109 scalar prefix/rank geometry applies globally}.
}
\]

The previous one-coordinate merged-rank path is therefore the width-one boundary calculus.

## 4. P025-T256 — monotone ideal paths are dominance-monotone antichain paths

Let

\[
I_0\subseteq I_1\subseteq\cdots\subseteq I_h
\]

be a monotone path of order ideals and define

\[
A_j:=\partial I_j.
\]

Then

\[
\boxed{
A_0\preceq A_1\preceq\cdots\preceq A_h,
}
\]

where

\[
A\preceq B
\iff
\downarrow A\subseteq\downarrow B.
\]

Conversely every such dominance-monotone antichain path reconstructs a unique monotone ideal path by down-closure.

Thus the full ideal history can be stored as a path of boundaries of size at most \(w(P)\) per node, not as the full incidence matrix.

## 5. The boundary labels are semantic

Boundary *size* is not enough. Already on a two-element antichain,

\[
\{a\}
\quad\text{and}\quad
\{b\}
\]

have the same boundary size but answer labelled membership queries differently.

So the correct replacement for scalar rank is not a new scalar such as `boundary width used`; it is a labelled antichain state whose worst-case support size is controlled by \(w(P)\).

## 6. Relation to A4 support

A4 owns finite multivalued support/correspondence algebra. Stage 114 should not be read as reducing an A4 relation to a poset antichain.

The reusable pressure test is only:

- chain observation family → one prefix boundary coordinate;
- width-\(w\) partial observation family → up to \(w\) incomparable labelled boundary generators may be necessary;
- support/cardinality alone cannot replace labels for full membership futures.

This is evidence for a general foundation distinction between **precision amount** and **precision support geometry**.

## 7. Prior-art discipline

Poset width, antichains, order ideals, and the ideal–antichain correspondence are classical. No generic novelty claim is made.

The project-side result is their exact use as the failure/replacement calculus for the P025 merged-rank future-state compiler. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 8. Executable assets

Added:

- `src/enterprise_math/poset_boundary_width.py`;
- `tests/test_poset_boundary_width.py`.

The executable layer checks the width identity, tight witnesses, total-order recovery, boundary-path round trips, and the negative boundary that equal boundary cardinality is not semantic equality.

## 9. Next frontier

The next question is task-relative: full membership queries require the full ideal boundary, but a declared future language may inspect only a subset or quotient of poset elements. We therefore need the coarsest boundary projection sufficient for a declared query family, not the whole antichain by default.
