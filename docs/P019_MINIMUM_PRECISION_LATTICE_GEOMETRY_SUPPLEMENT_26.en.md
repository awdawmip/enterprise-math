# P019 Supplement 26 — Observation-Aware Future Languages and Minimum Exact Relation Precision

Status: `RESEARCH WIP / EXACT LINEAR OBSERVATION + DYNAMICS SOLVER`

## 1. Why dynamics alone are insufficient

Supplement 25 solves minimum exact partitions for integer affine dynamics. A future language also contains questions/observations. Even when dynamics ignore a hidden relation, a future query that directly asks for that relation makes the current quotient too coarse.

Minimum exact relation state must therefore be determined jointly by future operations and future observations.

## 2. Exact linear observations

For

\[
\lambda(c)=w^Tc+b,
\]

an exact coarse score exists iff

\[
\boxed{w^T=\bar w^TA.}
\]

The affine constant `b` adds no distinguishability requirement.

## 3. P019-X96 — Block-constant coefficient criterion

For a coordinate partition matrix `A`, a linear score descends iff

\[
\boxed{w_i=w_j}
\]

whenever fine coordinates `i,j` lie in the same coarse block. The common block coefficient is the coarse coefficient.

## 4. P019-X97 — Coarsest observation refinement

For a family of score vectors `w^(1),...,w^(r)`, assign each fine coordinate its coefficient signature

\[
\sigma_O(i)=(w_i^{(1)},...,w_i^{(r)}).
\]

Split only within current blocks by unequal signatures. The result is the coarsest refinement preserving every declared exact linear score.

## 5. Hidden internal relation queries automatically demand refinement

For unit capacities, `Z_01=c_0-c_1` has coefficient vector `(1,-1,0,...)`. If coordinates 0 and 1 are currently merged, their coefficients differ, so X96 forces a split. Asking for an internalized relation is itself a refinement demand; no separate manual precision request is required.

Conversely, coarse-block relations have coefficients constant inside each current block and do not force meaningless singleton refinement.

## 6. P019-X98 — Minimum exact partition for operations plus observations

First refine the initial partition by observation signatures, obtaining `Pi_O`. Then run Supplement 25's stable matrix refinement starting from `Pi_O`. The resulting `Pi_*` is the coarsest refinement preserving every declared linear observation and every declared affine dynamics.

Any exact common refinement must first refine `Pi_O`, then by Supplement 25's coarsest theorem must refine `Pi_*`.

## 7. Branch predicates

If a piecewise future rule chooses branches by a deterministic function of an exact linear score `w^Tc+b`, then making that score quotient-readable is sufficient to make branch identity quotient-readable. This is exact for branch-identity-sensitive languages. It may be stronger than necessary when hidden branches happen to have identical coarse outputs, so no universal minimality claim is made for arbitrary output-only piecewise maps.

## 8. P019-X99 — Relation precision rank cost

If the current partition has `ell_0` blocks and the minimum exact partition has `ell_*`, the necessary increase in fixed-total relation dimension is

\[
\boxed{\Delta d=\ell_*-\ell_0.}
\]

The Refinement Forest restores a present state using exactly the same number of independent internal weighted relations. Thus `Delta d` is an intrinsic integer minimum exact relation-refinement rank cost. It is not an execution-time or bit-length metric.

## 9. Task-derived precision

The workflow becomes:

1. declare the future operation/observation language;
2. synthesize the coarsest exact partition;
3. read the minimum required relation-rank refinement from `ell_*-ell_0`;
4. expose only that relation detail.

Required precision is therefore derived from future distinguishability rather than selected heuristically in advance.

## 10. Implementation

Added `src/enterprise_math/linear_observation_quotient.py` and `tests/test_linear_observation_quotient.py`, including block-constant checks, observation-only refinement, hidden relation queries, coarse relation non-overrefinement, joint operation+observation synthesis, brute-force common-coarsest checks over all four-coordinate candidate partitions, and affine constants.

## 11. Prior-art boundary

Observable congruence, behavioral equivalence, minimal realization, and partition-refinement methods are established neighboring tools. P019 makes no general priority claim. The project-specific connection is the pipeline

\[
\boxed{
\text{future language}
\to
\text{minimum partition precision}
\to
\text{weighted relation state}
\to
\text{exact refinement rank cost}.
}
\]

## 12. Next steps

1. combine `Delta d` with the relation quantum `g` from Supplement 24 as a two-coordinate precision cost;
2. support modular/congruence observations that can admit coarser quotients than exact-score preservation;
3. handle output-equivalent predicate-controlled affine dynamics without requiring hidden branch identity;
4. connect the solver to P018 adaptive precision selection;
5. feed actual P021 witness queries in as observations to determine which relation degrees causal composition truly requires.
