# A3 Guard-Image Lattice Supplement 08 — Finite-Workload Common Precision and the Failure of Naive Local-Optimum Composition

Status: `RESEARCH WIP / COMPLETE RANK-ONE/TWO FINITE-WORKLOAD SOLVER + STRICT LOCAL/SHARED GAP`

## 1. From one state to one shared coarse program

Supplements 06 and 07 give complete **state-local** minimum task precision for rank-one and rank-two hidden guard images. They fix one parent coarse fiber / one current fine state and ask for the least refinement needed to make the declared branch-effect language exact at that state.

A deployed coarse program usually has to serve more than one state.

Let a finite workload be

\[
\mathcal Y=\{y_1,\ldots,y_N\},
\]

with corresponding base guard-score vectors

\[
g^{(1)},\ldots,g^{(N)}.
\]

We now require one **common partition refinement** that is exact for every workload state under one fixed parent-level branch-effect language `E`.

## 2. A3-G31 — Finite-workload safe refinement

For a candidate refinement `R`, let its child hidden image be `L_R`. At workload state `a`, the child score coset is

\[
g^{(a)}+L_R.
\]

Let the reachable threshold patterns there be `R_a(R)`. The refinement is safe for the whole workload iff

\[
\boxed{
E|_{R_a(R)}\text{ is constant for every }a=1,\ldots,N.
}
\]

Equivalently,

\[
\boxed{\max_a a_E(y_a;R)=1.}
\]

This is the finite conjunction of the state-local reachable-effect criterion.

## 3. A3-G32 — Canonical replacement remains valid for a workload

Supplements 06 and 07 show that any refinement `R` with hidden image `L_R` has a unique canonical replacement `R_can(L_R)` that is no finer and has exactly the same child hidden image.

For every fixed workload fine state, its base score is unchanged, so

\[
g^{(a)}+W(K_R)=g^{(a)}+W(K_{R_{can}}).
\]

Thus every workload state's reachable pattern set and effect ambiguity are identical under `R` and its canonical replacement.

Hence

\[
\boxed{
R\text{ workload-safe}
\Longrightarrow
R_{can}(L_R)\text{ workload-safe and no finer}.
}
\]

The common minimum solver therefore searches canonical hidden-image states rather than Bell-number raw partitions.

## 4. Complete rank-one workload solver

For a rank-one parent image `Z h`, the canonical candidates are the finite modulus refinements

\[
R_1,\ldots,R_D
\]

from Supplement 06.

For each `R_q`, run the exact rank-one reachable-effect checker on every workload state. Keep only candidates safe for all states and minimize

\[
\boxed{
\Delta d_{work}
=\min_{q:\,R_q\text{ safe for all states}}
(|R_q|-|P|).
}
\]

All candidates attaining that cost form the finite-workload minimum frontier.

## 5. Complete rank-two workload solver

For a rank-two parent image, enumerate the complete finite family of partition-realizable hidden subgroups

\[
M_1,\ldots,M_s\le\mathbb Z^2
\]

from Supplement 07.

For each canonical `R_(M_i)` and every workload state:

- hidden rank zero: one current pattern;
- hidden rank one: exact switch sweep;
- hidden rank two: exact rank-two integer halfplane reachability.

Keep only subgroups safe for all states and minimize

\[
\boxed{
\Delta d_{work}
=\min_{i:\,R_{M_i}\text{ workload-safe}}
(|R_{M_i}|-|P|).
}
\]

By G32 this is complete over all partition refinements.

## 6. A3-G33 — Workload lower bound and a strict gap

Any common-safe refinement is individually safe for every state, so

\[
\boxed{
\Delta d_{work}
\ge
\max_{y\in\mathcal Y}\Delta d_{min}(y).
}
\]

Equality need not hold.

### Rank-one strict example

Use hidden labels

\[
(0,1,3),
\]

parent direction

\[
h=(1,-1),
\]

and a branch-effect language in which only `(T,T)` differs from `(F,T)` and `(T,F)`.

Take two states

\[
g^{(1)}=(-3,3),
\qquad
g^{(2)}=(-2,2).
\]

For state 1, the dangerous `(T,T)` zero crossing occurs at parent parameter `t=3`. Modulus `2` removes it, while modulus `3` preserves it. The state therefore has a rank-gain-one minimum partition

\[
\{\{0\},\{1,2\}\}.
\]

For state 2, the dangerous crossing occurs at `t=2`. Modulus `3` removes it, while modulus `2` preserves it. Its rank-gain-one minimum uses the incomparable partition

\[
\{\{0,2\},\{1\}\}.
\]

No single rank-gain-one refinement is safe for both states. The common workload requires the label-visible singleton refinement, giving

\[
\boxed{
\Delta d_{min}(y_1)=1,
\quad
\Delta d_{min}(y_2)=1,
\quad
\Delta d_{work}=2.
}
\]

Thus

\[
\boxed{
\Delta d_{work}>
\max_y\Delta d_{min}(y).
}
\]

State-local optima cannot simply be selected independently and reused as a shared precision policy.

## 7. Rank-two strict workload example

Use the four-slot guards from Supplement 07,

\[
w^{(1)}=(0,1,2,0),
\qquad
w^{(2)}=(0,1,2,1),
\]

and assign a different effect only to `(T,F)`.

For state

\[
g^{(1)}=(1,1),
\]

the diagonal hidden subgroup `Z(1,1)` makes `(T,F)` unreachable and is safe at relation-rank gain `1`.

For state

\[
g^{(2)}=(2,0),
\]

the same diagonal coset still reaches `(T,F)`, so the rank-gain-one refinement fails.

A common safe refinement uses the horizontal subgroup

\[
\mathbb Z(1,0),
\]

whose canonical partition is

\[
\boxed{\{\{0\},\{1,3\},\{2\}\}.}
\]

Its relation-rank gain is `2`, so rank two also exhibits

\[
\boxed{\text{one-state cost }1<\text{two-state common cost }2.}
\]

## 8. Complete partition oracles

The regression suite enumerates all parent refinements for:

- the rank-one three-coordinate example;
- the rank-two four-coordinate example.

For each partition and every workload state, it directly computes hidden rank, reachable patterns, and branch effects.

In both examples the common solver's minimum cost and full minimum partition frontier exactly match the Bell-partition oracle.

## 9. Implementation

Added:

- `src/enterprise_math/guard_workload_precision.py`;
- `tests/test_guard_workload_precision.py`.

Main APIs:

- `minimum_rank_one_workload_precision`;
- `minimum_rank_two_workload_precision`;
- `WorkloadPrecisionCandidate`;
- `WorkloadPrecisionResult`.

The result records the common minimum relation-rank gain, every minimum common-safe candidate, workload size, and canonical search-state count.

## 10. Three precision levels must remain distinct

The project now has explicit examples showing

\[
\boxed{
\text{state-local minimum}
\neq
\text{finite-workload minimum}
\neq
\text{global all-state program minimum}.
}
\]

The first two levels have complete rank-one/rank-two solvers.

The third level cannot be approximated conceptually by sampling more workload states; it requires a symbolic argument over the infinite coarse-state lattice.

## 11. Next

1. decide symbolically whether a fixed refinement induces one exact coarse effect over **all coarse states**;
2. decompose base-score variation into a coarse-readable score lattice plus the hidden image lattice instead of enumerating states;
3. derive the rank-one global periodic/residue coarse program first;
4. relay the strict finite-workload gap to P018/P023 so adaptive precision distinguishes per-state from shared-model costs;
5. run the first cross-route workload from an actual A4 staged-support or P021 predicate family.
