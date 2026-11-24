# R5 — One all-closed shortest-path sweep recovers 256 exact closure-count observers

Date: 2026-11-16. Scientific input is frozen at `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Status: **AUTHOR_PROVED / EXACT_INTEGER_FINITE_CHECKED / NOT_REVIEWED**.
Role/ownership: independent portable research, historical attribution `EM-DIRECT-B78E55` only; no current R5 CLAIM or Result/Review is claimed.

## The open problem addressed

For the derived radius-two, integer-indexed 954-event nearest-center observer, earlier work reconstructs 28 possible length-three gap closures and proves that the complete high-budget optimizer families depend on eight effective closure bits, in the order
`U=(3,8,9,10,15,17,25,27)`.
At all budgets `K>=214`, previous source-backed proofs establish constant optimum cost across the closure masks and a principal-filter (least enabling mask) description of indexed optimal-center sets.

The immediately preceding kernel theorem shows a common weighted predecessor DAG of 4,383 arcs plus exactly 16 optional arcs (two for each effective bit); terminal and initial costs are mask-invariant. Its verifier checks all 256 resulting predecessor graphs, with the original fixed science source. Here we remove the need to solve the optimization DP independently for each of the 256 masks.

## New general theorem: requirement-mask shortest-path cohort transform

Let `G_b` be finite weighted, directed acyclic source-to-terminal path graphs obtained from a full graph `G_1` by retaining all unconditional edges and only conditional edges with bit-label sets contained in `b ⊆ {1,...,q}`. Edge weights and initial/terminal costs do not depend on `b`. A counted path has exactly `K` selected center vertices. Define its requirement set `R(p)` as the **union** of all its conditional edge-label sets, and its total cost `c(p)`.

Suppose for a specified `K` every submask has the same finite optimal cost:
`D_b(K)=D_1(K)=D(K)`.
Write `A_T(K)` for the number of complete `G_1` paths with exactly `K` centers, total cost `D(K)`, and requirement set `T`.

Then **for every closure mask**:

```text
N_b(K) = sum_{T subseteq b} A_T(K).
A_T(K) >= 0 is an exact integer.
```

Proof: any path in `G_b` is exactly a path in `G_1` with `R(p)⊆b`. All retained paths preserve their costs, and the common optimal cost equals `D(K)`. Thus the mask-b optimum family is precisely the full-graph global-optimum paths whose requirements are contained in b. Partition that family by the *unique* requirement set `T`. Conversely, every counted full-optimum path with `T⊆b` is available and is still optimal in `G_b`. The partition is disjoint, establishing the formula. Inverting the subset-zeta transform gives the signed Möbius formula; the path partition directly proves that the resulting coefficients are nonnegative integers.

### Single-sweep computation and proof of recurrence

For each number of centers `k` and final center `j`, compute the full-graph minimum prefix cost `d[k,j]`. Alongside it retain an exact coefficient dictionary `P[k,j][T]` counting full-graph paths attaining `d[k,j]` with union requirement set `T`.

Initialize the valid one-center states with one empty-requirement path, `P[1,j][∅]=1`.
For each full predecessor edge `i -> j` with fixed weight `w` and required bit mask `r`, compute `v=d[k-1,i]+w`. If `v<d[k,j]`, replace the target cost and reset its cohort dictionary. If `v=d[k,j]`, accumulate

```text
P[k,j][T OR r] += P[k-1,i][T] .
```

This is the tie-count shortest-path recurrence over the idempotent Boolean-support semiring for requirement masks: a bit used twice is still required once. By induction on k every full-graph minimum prefix path is counted once, and no losing prefix contributes. Combine only minimum-cost terminal states with invariant suffix costs to obtain `A_T(K)`, then apply the exact integer subset-zeta transform in `q·2^q` integer additions per requested K. Rolling k-layers need no past layer storage.

The all-closed cost recurrence is computed **once**; no mask-dependent optimization recurrence is needed to recover any `N_b(K)` where the common-cost premise holds. For other models or budgets with varying optimal costs, retain a full cost-sensitive path-state representation instead; this stated theorem uses its common-cost hypothesis.

## New exact run: four budgets × all 256 masks

The executable `R5_PATH_REQUIREMENT_DP_20261116.py` rebuilds the frozen 15-coefficient source from all 32,767 nonempty subsets and asserts pools `(538,298,229)`, 954 events, endpoint 1065, 28 length-three cuts. It independently reconstructs the baseline, eight one-bit, and full eight-bit kernels; asserts the 4,383+16 edge decomposition and invariant initial/terminal costs. It performs one full-closed cost/cohort sweep to K294. At K214,223,291,294 it computes the exact nonnegative cohorts and all 256 subset-zeta counts.

| K | Minimum cost | Positive exact requirement-mask cohorts | Effective cut support |
|---|---:|---:|---|
| 214 | 1064 | 20 | 3, 8, 9, 10, 27 |
| 223 | 1020 | 4 | 25, 27 |
| 291 | 748 | 3 | 25, 27 |
| 294 | 738 | 4 | 15, 17 |

The all-closed counts are, respectively:

```text
K214: 4573020854769248525038387200000
K223: 209661782760358268989540757667840000
K291: 10211420035936236257356176949248
K294: 342162737216429487140162764800
```

The three-count signatures `(N_b(214),N_b(223),N_b(294))` are distinct for all 256 masks. For the established bit-optimal three-query plan `(214,291,294)`, total returned integer bit lengths range from **298 to 305** over the 256 masks. This independently reproduces the earlier 305-bit worst case.

The program's built-in independent fixed-mask DP checks eight masks `0,1,2,16,64,128,170,255`, all four K values, against the new cohort method. A **separate full direct-DP comparison** then recomputed every mask at each of the four budgets: **1,024/1,024** min-cost and exact-count matches, zero mismatches. All arithmetic is integer or `Fraction`, and all 31 recorded nonzero cohorts reproduce their 256 count values by zeta expansion.

## Observed resource accounting

For the specific standard-library Python program and local execution environment:

- Single full-graph DP sweep: 293 layer updates; 608,177 eligible predecessor comparisons on the cohort-propagation pass, of which 343,400 are tight-cost edges.
- Exact cohort additions: **785,396**; largest total nonzero cohort entries in a sampled rolling layer: **2,167** (the naive dense upper bound for one layer is 954×256).
- Single-sweep script, **including eight direct-mask cross-checks**: **1.179 seconds** observed.
- Separate 256-mask × four-budget full direct-DP validation: **30.116 seconds** observed.

Both timings are implementation measurements, not hardware-independent complexity bounds. The independent baseline rebuilds mask-specific predecessor graphs. They quantify an observed reduction in repeated full-DP work; the exact result is the one-sweep cohort theorem and the 1,024-value agreement, rather than a universal speedup assertion.

The complete compact result `EXACT_PATH_REQUIREMENT_COHORTS_20261116.json` contains each exact nonzero `A_T(K)`, all 256 count values at each K, real run counters and both evidence digests. Source code local SHA256 `799b905ae4332f862a5a528a3da4fb4f8059277260175ef7e43c9e6b95ff020f`; full *augmented* local JSON SHA256 `be9bec976746bf3cf007b8d0d01b652d3a0173315d0ca6a6b22a642c65e6fc91`. The repository JSON is a normalized certificate projection of that run, not a byte-for-byte copy of the augmented stdout.

## Source lineage and boundaries

- Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
- Complete optimal-family principal-filter and cost constancy: `research_notes/portable_direct/r5_global_optimizer_tomography_20261114/RESEARCH.md`.
- Eight-switch DAG theorem and 256-kernel check: `research_notes/portable_direct/r5_eight_switch_kernel_20261116/RESEARCH.md`.
- Exact fused per-mask DP comparator: `research_notes/portable_direct/r5_fused_three_count_dp_20261116/VERIFY_R5_FUSED_DP.py`.
- This result concerns **only the derived indexed-event observer**. Native six-axis space, third slice coordinate, BRC path provenance, and future-operation residuals remain separate typed questions. There is no formal R5 task ownership or independent review conferred by this author-side GitHub output.

## Next discriminating unit

Extend the polynomial cohort sweep to every K=214..314 with no extra per-mask DP, compare all breakpoint supports and exact counts to the prior 29-endpoint spectra, and identify whether cohort supports can be compressed into a small transfer automaton for faster multi-budget queries. Separately retain the original center-replacement-distance frontier K214..291.
