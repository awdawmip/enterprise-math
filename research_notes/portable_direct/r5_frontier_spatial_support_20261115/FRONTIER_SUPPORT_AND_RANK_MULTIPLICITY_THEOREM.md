# R5: sharp geometric support bound for offline recourse frontiers

Date: 2026-11-15. Frozen science: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Model: the derived 954-event, one-dimensional, **strictly increasing integer-coordinate**, radius-two, indexed-center observer. The theorem below also applies to arbitrary strictly increasing integer samples and an arbitrary integer radius; it is a theorem of that observer type, not a native X6 statement. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Theorem (sharp spatial support bound)

Let `z[0]<...<z[n-1]` be integers, let `rho>=0` be an integer radius, and consider a feasible indexed-center set. Its centers are increasing event indices. Fix an event-index cut `j`. A *crossing consecutive-center arc* is `i -> q` with `i<=j<q`, where the two centers are consecutive in some feasible full center selection. Let `T_j` be the set of possible tails `i` of such arcs, allowing all feasible selections (hence also all optimal selections).

**For every `j`, `|T_j| <= 2*rho+1`. This bound is sharp.** In the R5 radius-two observer, at most **five different original event indices** can occur as the spatial tails of the old-DAG frontier at a fixed event-index cutoff. This statement concerns event indices, *not* the number of rank-labeled vertices: one index may be present at several optimizer path ranks.

To localize the support, define `t(j)=max {t<j: z[t]<z[j]-rho}` when this set is nonempty, and

```
A_j = {i<=j: z[j]-rho <= z[i] <= z[j]}
      UNION
      {i<=t(j): z[t(j)]-rho <= z[i] <= z[t(j)]}
```

with the second set empty when `t(j)` is absent. Then `T_j subset A_j`, `|A_j|<=2*rho+2`, and when `|A_j|=2*rho+2`, its leftmost candidate **cannot** be a crossing tail.

**Proof.** Every event strictly between consecutive selected centers `i<q` is covered by either `i` or `q`: centers outside this ordered pair are farther from the intervening event than one of its endpoints. If `i>t(j)`, the maximality of `t(j)` gives `z[i]>=z[j]-rho`, so `i` lies in the first band. If `i<=t(j)`, then `t(j)` is between `i` and `q` (or equals `i`). Since `z[q]>=z[j]>z[t(j)]+rho`, it cannot be covered by `q`; therefore `z[i]>=z[t(j)]-rho`. This proves the inclusion. Distinct integer positions give at most `rho+1` candidates in each band. If both bands contain `rho+1` event positions, they include `z[t(j)]-rho` and `z[j]-rho`. The former candidate center cannot pair with any `q>j`: the event at `z[j]-rho` is at distance `z[j]-z[t(j)]>rho` from it and at distance at least `rho+1` from any `q>j`. Thus at most `2*rho+1` candidates survive. If `t(j)` does not exist, the first band alone suffices. QED.

**Sharpness.** Let event coordinates be all integers `0,...,2*rho+1`; choose `j=2*rho` and `q=2*rho+1`. Each `i=0,...,2*rho` can be followed by `q`: every intermediate event is within radius `rho` of one endpoint. All `2*rho+1` tails occur. For `rho=2`, the small witness is `0,...,5` with cut `j=4`, tails `0,...,4`.

## Rank-labeled frontier and Pareto consequence

For an old globally-optimal center-path DAG with fixed center count `K`, let `V_K(j)` consist of its rank-labeled vertices `(i,r)` with `i<=j` and an optimal outgoing edge `(i,r)->(q,r+1)` with `q>j`. Define `d_K(j)=max_i |{r:(i,r) in V_K(j)}|` (zero if empty) and `W_K(j)=|V_K(j)|`. The proven geometric result gives

```
W_K(j) <= (2*rho+1)*d_K(j)   (in particular W_K(j)<=5*d_K(j) for rho=2).
```

Thus path-rank multiplicity, rather than unlimited spatial lookback, controls the width exponent in the existing Pareto bound `A(j,h)<=(h+2)^(W_K(j)-1)` for `W_K(j)>=1`. For a uniformly bounded rank multiplicity `d`, the exponent is bounded by `(2*rho+1)*d-1`. This is a **conditional parameterized complexity bound**, not a universal constant-width result: rank multiplicity may vary with input and K.

## Exact R5 verification, with source scope

The frozen generator yields 954 events, 28 original gap-three positions and strictly increasing integer coordinates. Its original gap histogram is `{1:869,2:56,3:28}`; closing any gap-three position reduces it to two. Therefore every effective closure sample has adjacent gaps in `{1,2,3}`. On such samples any consecutive-center arc spanning more than seven units would leave an event uncovered: the first event beyond `z[i]+2` occurs by `z[i]+5` and is then at distance greater than two from the far endpoint. The finite checker may safely stop at coordinate span seven.

Locally executed `VERIFY_R5_FRONTIER_SPATIAL_SUPPORT.py`: exhaustive `3^9=19,683` ten-event coordinate-gap sequences; 32 effective R5 closure masks; all admissible crossing arcs for each cut; membership in `A_j` and the bound five; equality witness. Output: `PASS_R5_FRONTIER_SPATIAL_SUPPORT`, observed max tail count five and max raw two-band size six. Exact output bytes: 4,047; SHA-256 `abab60f2343666ca6175405aeea7b0a0018a68485368ca91b95d4b9c2e3f5e8e`.

Locally executed independent `VERIFY_R5_OPTIMAL_FRONTIER_RANK_AUDIT.py`: integer weighted-prefix/suffix optimization over all 954 events, K=214..221 and all 32 effective masks (256 optimizer instances); for every event cutoff, reconstruct optimal rank-labeled vertices and their crossing optimal edges. Output: `PASS_R5_OPTIMAL_FRONTIER_RANK_AUDIT`. Largest global frontier width = **19**; largest distinct spatial tails = **5**; largest per-tail rank multiplicity = **5**. Full 74,571-byte output SHA-256: `ea83a3345d64b70c528f9843771ba9cd4ca6abec75bf3717dd67953140dd01f0`. One maximum-width example: K=217, effective mask 2, event cutoff 187, W=19.

The observed `W=19` is independently recalculated here across all 256 effective optimizer instances and every event-index cutoff. Extension from the five effective variables to all 28 original closure bits uses the previously saved optimizer-family support theorem; it is not a new independent proof of that support theorem.

Files `VERIFY_R5_FRONTIER_SPATIAL_SUPPORT.py` and `VERIFY_R5_OPTIMAL_FRONTIER_RANK_AUDIT.py` reproduce the calculation. Exact emitted JSON may be regenerated by these saved programs; the original local output is retained as conversation evidence. The proof above is independent of the finite checks. No native X6 transition, physical calibration, or full original recourse minimax theorem is claimed by this result.

## Next mathematical target

Derive a useful bound on the **rank diversity** `d_K(j)` from radius-two coverage, excess center budget, and optimal-cost constraints; determine when `d_K(j)` can grow with K. This focuses the formerly undifferentiated frontier-width problem on an exact residual: multiple compatible optimizer path ranks for the same spatial event index. Separately audit common-anchor factorization and the offline max-plus state-update recurrence, retaining the existing independent-review status.

Provenance: pre-existing Draft PR #2427 and frozen pin above, particularly `OFFLINE_MAXMIN_EXACT_RECOURSE_THEOREM.md`, `VERIFY_R5_OFFLINE_MAXMIN_RECOURSE.py`, and `PARETO_FRONTIER_PARAMETRIC_BOUND_AND_BACKGROUND_REVERSALS.md`. Research Activity historically `RA-33C87C2B703418F0706695E9`; current formal Task/CLAIM not established. This file is an independent author-side GitHub proof/evidence publication, not a protected runtime progress mutation.
