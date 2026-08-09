# A3 Guard-Image Lattice Supplement 05 — Rank-One Residue Refinement and Task Precision Below Guard Visibility

Status: `RESEARCH WIP / EXACT SUBLATTICE REFINEMENT LAW + STRICT PRECISION-SEPARATION EXAMPLE`

## 1. Problem

If the actually reachable branch effects in a coarse fiber are not unique, the current quotient is not exact for that declared future language.

A direct but potentially excessive repair is to refine until every guard itself is exactly readable from the refined coarse state.

That is not always necessary.

For a rank-one hidden guard lattice, partition refinement can decrease the hidden lattice by finite index without decreasing its rank. The refined child fiber then keeps only one residue class of the parent arithmetic-line parameter, and a branch pattern responsible for effect ambiguity may disappear without making the guards visible.

## 2. A3-G19 — Rank-one guard-image refinement subgroup law

Let `R` refine a parent partition `P`. Then

\[
K_R\subseteq K_P
\]

and therefore

\[
W(K_R)\subseteq W(K_P).
\]

If the parent image has rank one, write its canonical step as

\[
W(K_P)=\mathbb Z h.
\]

The child rank cannot increase.

- If it drops to zero, the guards are fully visible on the refined partition.
- If it remains one, every subgroup of `Z h` has the form

\[
\boxed{W(K_R)=q\mathbb Z h,\qquad q\in\mathbb N_{>0}.}
\]

With canonical first-nonzero-positive steps,

\[
\boxed{h_R=q h_P}
\]

and

\[
\boxed{q=[W(K_P):W(K_R)].}
\]

Thus refinement can make hidden variation arithmetically sparser without exposing the guard family.

## 3. A3-G20 — A refined child fiber is one parent-parameter residue class

The parent score set is

\[
g+t h,\qquad t\in\mathbb Z.
\]

If the child image is `q Z h`, each child fiber corresponds to

\[
\boxed{t\equiv a\pmod q.}
\]

Writing `t=a+qn`, the child scores are

\[
\boxed{(g+a h)+n(qh).}
\]

Hence the child reachability problem is still the exact rank-one sweep from Supplement 01, with shifted base and enlarged step.

## 4. Three-slot example

Take three fine coordinates and two guards

\[
w^{(1)}=(0,1,2),
\qquad
w^{(2)}=(0,-1,-2).
\]

For the parent partition

\[
P=\{\{0,1,2\}\},
\]

the within-block coefficient differences generate

\[
\boxed{W(K_P)=\mathbb Z(1,-1).}
\]

At fine state

\[
c=(0,1,0),
\]

the base scores are

\[
g=(1,-1).
\]

The parent score line

\[
(1+t,-1-t)
\]

realizes exactly

\[
\boxed{(F,T),\ (T,T),\ (T,F)}.
\]

The `(T,T)` pattern occurs at `t=-1`, where both scores are zero.

## 5. One intermediate refinement deletes the dangerous pattern

Refine only to

\[
R=\{\{0,2\},\{1\}\}.
\]

The remaining hidden within-block direction is `e_2-e_0`, whose guard image is `(2,-2)`. Hence

\[
\boxed{W(K_R)=2\mathbb Z(1,-1).}
\]

The hidden rank is still one: the guards are not visible.

The child fiber containing the current fine state restricts the parent parameter to

\[
\boxed{t\equiv0\pmod2.}
\]

and its scores are

\[
(1+2n,-1-2n).
\]

Therefore

\[
\boxed{R_y=\{(F,T),(T,F)\}}
\]

and `(T,T)` is impossible.

## 6. A3-G21 — Task-exact precision can be strictly below guard-visible precision

Assign the same declared coarse effect `E` to `(F,T)` and `(T,F)`, a different effect `E'` to `(T,T)`, and anything to unreachable `(F,F)`.

- The parent is not exact because `(T,T)` is reachable.
- The intermediate refinement is exact because only the two `E` patterns remain reachable.
- Exact observation of both guards requires singleton precision because the fine coefficient signatures `(0,0)`, `(1,-1)`, `(2,-2)` are all distinct.

Thus

\[
\boxed{
\text{minimum precision for the declared branch-output task}
<
\text{minimum precision for exact guard identity}.
}
\]

This is a strict integer example, not a heuristic comparison.

## 7. Relation-rank cost

With unit fine capacities:

- parent `P` has relation rank `0`;
- task-exact `R` has relation rank `1`;
- singleton guard-visible precision has relation rank `2`.

Hence

\[
\boxed{\Delta d_{task}=1<2=\Delta d_{guard}.}
\]

This gives a concrete nontrivial benefit to future-language-derived precision.

## 8. Two-dimensional precision profile

The same example also shows that neither relation rank nor relation quantum alone is sufficient.

- parent capacity pattern `(3)` has relation quantum `g=3`;
- intermediate `(2,1)` has `g=1`;
- singleton `(1,1,1)` also has `g=1`.

The intermediate refinement already reaches the same structural relation quantum as the singleton state while retaining only one independent relation degree instead of two, and the declared task is already exact.

Therefore precision needs at least rank and quantum coordinates, while guard reachability can additionally depend on lattice coset/orientation. It should not be collapsed prematurely to one scalar.

## 9. Implementation

Added:

- `src/enterprise_math/rank_one_guard_refinement.py`;
- `tests/test_rank_one_guard_refinement.py`.

The regression suite preserves the three-slot example and verifies parent step `(1,-1)`, child step `(2,-2)`, image index `2`, unsafe parent, safe rank-one child, singleton guard visibility, and rank gains `1` versus `2`.

## 10. Meaning for P018 and A2

This result constrains precision refinement:

> **do not equate future safety with making every predicate explicitly visible.**

Sometimes less retained relation detail only needs to shrink the hidden fiber to a sparser residue class, eliminating future coarse-output ambiguity while leaving the predicate hidden.

For A2/P023 this is an arithmetic A3 specialization of general future-compatible quotient semantics. For P018 it is a direct pressure test showing that task precision can be strictly lower than full observable visibility.

## 11. Next

1. classify which partition refinements produce which rank-one image indices `q`;
2. solve the minimum image-index / relation-rank refinement that makes a declared effect language exact;
3. extend the idea to rank two, where refinement produces a finite-index sublattice or a rank drop and integer residues delete arrangement cells;
4. form task-precision certificates from `(relation rank, relation quantum, guard-image index/coset)` without arbitrary scalar weighting;
5. relay the result to P018/P023 so downstream work does not assume guard visibility is the minimum precision requirement.
