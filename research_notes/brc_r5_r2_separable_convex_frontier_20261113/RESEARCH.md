# Frozen BRC R5: radius-separator decomposition and conditional convex marginal merge

Date: 2026-11-13. Mode: TASK_RESEARCH scientific continuation, independent of formal CLAIM. Frozen scientific input: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Predecessor exact complete-budget study: Draft PR #2302, immutable commit `c3989b2846f81cdda694efa1bf1b043150a8169a`. This is a scalar certificate-event observer calculation, with the frozen joint certificate/branch provenance retained at the scientific input. It asserts no new X6-native observer quotient or mathematical acceptance.

## Theorem 1. Exact radius-separator factorization

Let `x[0]<...<x[N-1]` be strictly increasing real coordinates, and let `R>=0`. A set of centers S is a subset of the input indices. Define `d(b,S)=min_{s in S}|x[b]-x[s]|`. Minimize `J_R(K)=sum_b d(b,S)` among all `|S|=K` and `max_b d(b,S)<=R`, with infeasible K excluded.

Split the index set at every gap `x[i+1]-x[i]>R`, yielding consecutive nonempty blocks `B_1,...,B_m`. Let `J_j(k)` denote the same constrained minimum for block j, using its own coordinates, and `D_j` the minimum feasible number of centers in that block. Then

```
J_R(K) = min { sum_j J_j(k_j) : sum_j k_j=K, D_j<=k_j<=|B_j| }.
D_R = sum_j D_j.
```

**Proof.** For a point b in block B_j and a center s outside B_j, the intervening separating gap makes `|x[b]-x[s]|>R`. Thus, any globally radius-R feasible S must contain at least one center within distance R of b in its own B_j. For any such S, all within-block points are served at distance <=R by a within-block center, while every outside-block center is at distance >R, so their nearest-center distances are exactly those of `S∩B_j`. Conversely, a union of feasible within-block S_j is globally feasible and realizes the sum of local costs. Minimizing at fixed cardinality yields the displayed min-plus convolution, and minimizing feasible cardinality gives the additive D_R formula. This applies to arbitrary increasing real coordinates; no integrality is required. QED.

A single gap `>R` is sufficient for this factorization. A gap equal to R does not support this argument, because a center across the gap may serve at radius R. The theorem does not erase branch/composite structure: it factors only the specified scalar distance observer over a declared fixed-radius horizon.

## Theorem 2. Conditional exact marginal-gain merge

Suppose each local finite cost curve `J_j(D_j),...,J_j(|B_j|)` has non-increasing marginal improvements
`g_j(k)=J_j(k-1)-J_j(k)` for `k>D_j`, i.e. `g_j(k+1)<=g_j(k)`.
Start at `K_0=sum D_j`, `J_0=sum J_j(D_j)`. Repeatedly select the largest next unconsumed local marginal gain (breaking ties deterministically), subtract it from the cost, and advance that block by one center. After t steps the result is exactly `J_R(K_0+t)`.

**Proof.** Increasing a block's budget by a positions selects precisely the first a entries of its non-increasing gain sequence. The total cost reduction is their sum. The collection of the t largest available gains across all local sequences is prefix-closed up to tie-breaking that favors earlier elements of a given sequence, hence corresponds to a feasible allocation of t additional centers. Any other allocation selects t gains and has a sum no greater than the sum of the t largest gains. Therefore the greedy merge attains the minimum global cost at every total K. QED.

This second theorem is conditional; this run checks its premise for the 29 actual R5 blocks. It does not presume discrete convexity for arbitrary coordinate distributions. Once local curves are computed, a heap merges their marginals in `O((N-D_R) log m)` comparisons and `O(m)` heap storage, with exact integer costs. General min-plus convolution remains valid without the convexity condition.

## Frozen R5 numerical consequences

Reconstruct the original 15 signed integer atoms and the q=3,12,15 certificate wall families, retaining duplicate threshold multiplicities. There are exactly 953 distinct rational walls, 954 boundary event coordinates, and 1065 events. The wall multiplicity histogram is `{1:869,2:56,3:28}`. With R=2, exactly 28 gaps of 3 separate the scalar event-coordinate sequence into **29 independent blocks**.

Block lengths (in order):
`[19,14,7,7,13,8,18,12,13,6,7,18,7,21,20,5,36,15,19,23,20,12,38,26,22,36,17,24,471]`.

Minimum center requirements by block:
`[4,3,2,2,3,2,5,3,3,2,2,4,2,5,5,1,8,4,5,5,4,3,9,6,5,9,4,6,97]`, summing to `D_2=213`.

All 29 local optimal cost curves passed an exact non-increasing-marginals check. Full-sample direct DP, general min-plus component convolution, and conditional marginal heap merge agree for **all 742 budgets K=213,...,954**, including costs `J_2(213)=1070` and `J_2(351)=603`. The canonical newline-delimited K,J values have SHA-256 `1de18dc9b43790c9bcb66e5ba8a88532dfd2de9979ee4d936cef8a1704b3dab9`, `sum J=292961`, and `sum K*J=130909193`. The full direct radius-2 graph has 4383 directed edges; the 29 local graphs have 4137.

Independent small-input exhaustive validation: 21,844 array/radius pairs with length 1..7, gaps in {1,2,3,4}, radii in {0,1,2,3}. Among them, 20,616 have nontrivial radius separators. For each pair, direct enumeration of all nonempty center subsets agrees with the computed component convolution. The actual R5 sequence additionally checks the heap-merge condition and its 742 outputs.

Single non-warmed CPython process measurements (not repeated benchmarks): full fixed-radius DP 0.235634 s, component DP + min-plus convolution 0.079485 s, component DP + heap merge 0.060290 s. These timings measure only this Python scalar optimizer, not the original 2520-byte certificate seed's 28-coordinate/8192-query cold-start, RSS, or throughput.

## Reproduction and remaining questions

`VERIFY_R5_R2_COMPONENTS.py` uses only Python stdlib and exact `Fraction`/integer arithmetic; run `python VERIFY_R5_R2_COMPONENTS.py`. `EXACT_OUTPUT.json` records the actual test observation. All costs must be recomputed from the pinned atom coefficients, not from a repinned current tree. The R5 research ownership/CLAIM query is tracked separately; the artifact is a draft scientific note and not a new canonical Result.

Next useful experiments: isolate the 471-boundary block and test exact incremental-update sensitivity when one gap crosses the radius separation threshold; construct a witness or sufficient condition for discrete convexity of the local R2 cost curves. Independently perform the original full 28-coordinate prefix-query replay across alternative encodings, with exact output hashes and cold-start/peak RSS measurement.
