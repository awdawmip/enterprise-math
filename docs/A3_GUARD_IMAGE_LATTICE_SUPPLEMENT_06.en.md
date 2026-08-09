# A3 Guard-Image Lattice Supplement 06 — Canonical Modulus Refinement and the Rank-One Minimum Task-Precision Frontier

Status: `RESEARCH WIP / EXACT COARSEST MODULUS REFINEMENT + COMPLETE STATE-LOCAL MINIMUM-RANK SOLVER`

## 1. Goal

Supplement 05 showed that a rank-one hidden guard can be refined by a finite-index residue restriction so that a dangerous branch becomes unreachable without making the guards fully visible.

We now solve the complete state-local optimization problem:

> Given a parent partition, the current coarse fiber's base guard scores, and one fixed parent-level branch-effect language, what is the minimum relation-rank refinement needed for exactness over **all partition refinements**?

The answer is not merely optimal inside a hand-picked candidate family.

## 2. A3-G22 — Hidden integer labels of fine coordinates

Assume the parent guard image is

\[
W(K_P)=\mathbb Z h.
\]

Inside every parent block `B`, fix an anchor `a`. For each `i in B`,

\[
W_i-W_a\in\mathbb Z h,
\]

so there is a unique integer

\[
\boxed{\lambda_i\in\mathbb Z}
\]

such that

\[
\boxed{W_i-W_a=\lambda_i h.}
\]

Set `lambda_a=0`.

Changing the anchor translates all labels in that parent block by one common integer, so label differences and equality modulo `q` are anchor-independent.

## 3. A3-G23 — Canonical Modulus Refinement Theorem

Fix an integer

\[
q\ge1.
\]

Inside each parent block, group coordinates by

\[
\boxed{\lambda_i\bmod q}
\]

and call the resulting refinement

\[
\boxed{R_q.}
\]

If `i,j` remain in one child block, then `lambda_i-lambda_j` is divisible by `q`, so

\[
W_i-W_j=(\lambda_i-\lambda_j)h\in q\mathbb Z h.
\]

Therefore

\[
\boxed{W(K_{R_q})\subseteq q\mathbb Z h.}
\]

Conversely, suppose a refinement `R` satisfies

\[
W(K_R)\subseteq q\mathbb Z h.
\]

Any two coordinates in one `R` block then satisfy

\[
W_i-W_j\in q\mathbb Z h,
\]

hence

\[
\lambda_i\equiv\lambda_j\pmod q.
\]

Thus every `R` block lies inside one `R_q` residue block:

\[
\boxed{R\preceq R_q.}
\]

So `R_q` is the unique coarsest refinement forcing the child image inside `q` times the parent image.

## 4. Exact-image preservation

If some refinement `R` actually has

\[
\boxed{W(K_R)=q\mathbb Z h,}
\]

then `R` refines `R_q`, giving

\[
q\mathbb Z h=W(K_R)\subseteq W(K_{R_q}).
\]

The previous containment gives the reverse inclusion, hence

\[
\boxed{W(K_{R_q})=q\mathbb Z h.}
\]

Therefore any arbitrary refinement realizing rank-one image index `q` has a canonical replacement that is no finer and realizes exactly the same hidden score lattice.

## 5. A3-G24 — Finite modulus visibility bound

For each parent block define its label span

\[
D_B=\max_{i\in B}\lambda_i-\min_{i\in B}\lambda_i
\]

and let

\[
\boxed{D=1+\max_B D_B.}
\]

If `q>=D`, unequal labels cannot be congruent modulo `q`. Hence all such modulus refinements stabilize to the same label-equality partition

\[
\boxed{R_q=R_{vis}.}
\]

Inside every block of `R_vis`, all guard coefficient differences vanish, so

\[
\boxed{W(K_{R_{vis}})=0.}
\]

Thus every nonzero rank-one child image index appears in the finite range

\[
\boxed{1\le q<D.}
\]

## 6. A3-G25 — Complete minimum state-local rank-one task precision

Fix:

- a parent partition `P` with `rank W(K_P)=1`;
- the current fine state / current parent-fiber base guard scores `g`;
- a fixed **parent-level future effect language**
  \[
  E:\{F,T\}^r\to\mathcal Y.
  \]

Refinement is used only as internal precision; the declared effect being tested remains the same parent-level effect `E`.

For any refinement `R`:

- if its child hidden rank is zero, the current child fiber has one guard pattern and is branch-deterministic;
- if its child rank remains one, write
  \[
  W(K_R)=q\mathbb Z h.
  \]
  Its current score coset is exactly
  \[
  g+q\mathbb Z h,
  \]
  and exactness depends only on whether `E` is constant over the branch patterns reachable in that coset.

By G23–G24, every safe refinement has a canonical replacement `R_q` (or the guard-visible `R_vis`) that is no finer and has the same current hidden score coset. Therefore it is sufficient and complete to check

\[
\boxed{q=1,2,\ldots,D.}
\]

For each `R_q`:

1. compute its actual child guard-image rank / step;
2. compute the current reachable patterns with the exact rank-one sweep;
3. apply the reachable-effect erasure criterion from Supplement 04;
4. record the relation-rank gain
   \[
   \Delta d_q=|R_q|-|P|.
   \]

Then

\[
\boxed{
\Delta d_{min}
=\min_{q:\,R_q\text{ safe}}(|R_q|-|P|)
}
\]

is the minimum state-local task-exact relation-rank gain over **all partition refinements**.

## 7. Minimum cost can be unique while the minimum partition is not

Define the minimum frontier

\[
\mathcal F_{min}
=\{R_q:R_q\text{ safe},\ |R_q|-|P|=\Delta d_{min}\}.
\]

This frontier can contain incomparable partitions.

Take hidden labels

\[
(0,1,3).
\]

Modulo `2`, the residues `(0,1,1)` give

\[
R_2=\{\{0\},\{1,2\}\}.
\]

Modulo `3`, the residues `(0,1,0)` give

\[
R_3=\{\{0,2\},\{1\}\}.
\]

These partitions are incomparable and both have relation-rank gain `1`.

With base scores `(1,-1)`, parent direction `(1,-1)`, and a branch-effect language in which only `(T,T)` has a different effect, both refined fibers eliminate `(T,T)` and are task-exact.

A complete three-coordinate partition oracle confirms

\[
\boxed{\mathcal F_{min}=\{R_2,R_3\}.}
\]

Hence one must distinguish

\[
\boxed{\text{minimum precision cost}}
\]

from

\[
\boxed{\text{minimum precision frontier}.}
\]

The cost may be unique while the representation choices form an antichain.

## 8. Relation to A2/P023 and frontier structures

General minimal future-compatible states remain an A2/P023 mother problem.

A3 contributes a concrete arithmetic specialization:

- minimum cost is integer relation-rank gain;
- minimum states are an antichain of canonical modulus partitions;
- hidden lattice subgroup/residue structure determines which branch behaviors disappear.

This is `COMPOSABLE_INDEPENDENT` with recent A4/support antichain/frontier results. Similar terminology is not a proof that the two theories are the same; a theorem-level bridge is still required.

## 9. Implementation

Added:

- `src/enterprise_math/rank_one_guard_modulus.py`;
- `tests/test_rank_one_guard_modulus.py`;
- `src/enterprise_math/rank_one_task_precision.py`;
- `tests/test_rank_one_task_precision.py`.

Key APIs:

- `rank_one_guard_labels`;
- `rank_one_modulus_refinement`;
- `rank_one_modulus_visibility_bound`;
- `minimum_rank_one_task_precision`.

Tests include hidden-label reconstruction, the canonical modulus theorem checked against all small partitions, visibility stabilization, the strict task-versus-guard precision example, complete minimum-rank agreement with a partition oracle, and the incomparable `(0,1,3)` minimum frontier.

## 10. Current boundary

This theorem is **state-local and uses one fixed parent-level effect language**.

It does not yet solve:

- refinements whose declared future output language itself becomes finer;
- one common coarse program that must be exact over many parent coarse states;
- minimum partition synthesis for rank-two/higher hidden images.

These require separate proofs.

## 11. Next

1. combine the minimum frontier with relation quantum and guard-image index in a typed precision certificate;
2. develop the rank-two analogue using finite-index hidden sublattices and rank drops;
3. solve common-safe refinements over multiple parent coarse states;
4. relay the strict task-precision separation to P018/A2;
5. investigate a theorem-level connection between A3 minimum-partition antichains and the finite frontier tools appearing in P023/A4.
