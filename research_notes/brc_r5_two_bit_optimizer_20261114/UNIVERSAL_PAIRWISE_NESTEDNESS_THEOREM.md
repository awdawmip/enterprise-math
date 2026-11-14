# Frozen R5: universal pairwise nested optimal-center sets

**Date:** 2026-11-14  
**Frozen scientific input:** `435e77af0d180eac32bd1f9c4c464bc4010b7551`  
**Status:** author-side exact finite theorem, computed certificate PASS, independent mathematical review `NOT_REVIEWED`.  
**Scope:** the derived, one-dimensional, radius-two, 954-event, indexed-center covering observer; **not** native X6/BRC state equivalence.

## Exact definitions and theorem

The frozen 954 indexed event coordinates are reconstructed by `research_notes/brc_r5_exact_cost_spectrum_20261114/VERIFY_R5_COST_SPECTRA.py`. Let `B` be any subset of the 28 originally length-three gaps. The modified coordinates shorten each selected gap to length two without changing any event index. For any center-index subset `S`, define
`C_B(S)=sum_t min_{s in S}|x_t^(B)-x_s^(B)|`;
require nearest-center radius at most two. Write `J_B(K)` for the minimum cost among feasible size-K subsets and `Opt_B(K)` for the **set of all** minimizers.

**Theorem.** For **every** subset `B⊆{0,...,27}` and **every integer** `292≤K≤953`, there exist indexed center sets `S∈Opt_B(K)` and `U∈Opt_B(K+1)` such that `S⊂U`.

Equivalently, if the optimal-pair deletion distance is
`ρ_B(K)=min{|S\\U|:S∈Opt_B(K),U∈Opt_B(K+1)}`,
then `ρ_B(K)=0` and the minimum symmetric difference is one, for all `2^28=268435456` closure backgrounds and all 662 transitions `K=292,...,953`.

**Quantifier warning:** this is `forall B forall K exists S exists U`, **not** `forall B exists one nested global chain (S_292⊂S_293⊂...⊂S_954)`, and not an assertion that every optimal K-center solution extends optimally. Distinct transitions may require distinct selected `S`.

## Exact finite dynamic-programming certificate in the no-closure model

Fix an increasing integer coordinate sequence `x=(x_0,...,x_(n-1))`, radius 2. A feasible ordered center path `S={j_1<...<j_K}` decomposes uniquely into a left prefix, the adjacent-center gaps, and a right suffix. Define the cost of a center-to-center segment
`e(i,j)=sum_(i<t<j)min(x_t-x_i,x_j-x_t)`,
defined only when all its interior event distances are at most two. The left prefix cost is `p(j)=sum_(t<j)(x_j-x_t)` when `x_j-x_0≤2`, and the right suffix cost is `q(j)=sum_(t>j)(x_t-x_j)` when `x_(n-1)-x_j≤2`. Every feasible center subset has **exactly one** increasing center path; nearest center values between consecutive selected centers depend only on those two centers.

For a fixed feasible center set, inserting one new center `h` changes precisely one of these three types of cost segments. Define its **best gain**
`g(S)=max_(h not in S)[C(S)-C(S∪{h})]`.
For an interior segment, the gain is
`g(i,j)=max_(i<h<j) [e(i,j)-e(i,h)-e(h,j)]`,
with zero if there is no interior available center. The analogous prefix/suffix gains arise by splitting their one-center segment at an inserted center. All gains and costs are exact integers.

The paired dynamic programming state for each path length `k` and rightmost center `j` retains: (1) the **minimum** feasible path cost `F_k(j)`; (2) the **maximum one-insertion gain** `G_k(j)` among all paths attaining that minimum cost. The path transition from `i` to `j` uses candidate cost `F_k(i)+e(i,j)`. For a winning minimum-cost predecessor, its best insertion gain is
`max(G_k(i),g(i,j))`;
on ties, take the **maximum** of these gains. Left prefixes initialize the recurrence and eligible right suffixes finalize it, again maximizing insertion gain only among globally optimal K-center paths. Thus the exact output `H(K)` equals
`max_{S∈Opt_empty(K)} g(S)`.
The min-cost component equals the independent predecessor source `optimum_counts_spectrum` at each K.

Executing this exact recurrence on the frozen 954 coordinates gives the **complete** gain spectrum

| K transition | Number of transitions | Exact `H(K)` | Exact `J_empty(K)-J_empty(K+1)` |
|---|---:|---:|---:|
| 292→293 through 314→315 | 23 | 3 | 3 |
| 315→316 through 350→351 | 36 | 2 | 2 |
| 351→352 through 953→954 | 603 | 1 | 1 |
| **Total** | **662** | | |

For each of these 662 transitions there is a **globally optimal** K-center set `S` attaining `H(K)`, and an insertion `h` such that
`C_empty(S∪{h}) = J_empty(K)-H(K) = J_empty(K+1)`.
The new `K+1`-set remains feasible and is optimal by equality of costs. Hence a nested optimum pair exists in the no-closure instance at each K.

## Transfer to all 2^28 closure patterns

The prior exact high-budget monotone sandwich theorem in the same Draft PR #2379 establishes for every `B` and `K≥214`:

```
J_B(K) = J_empty(K)
Opt_empty(K) ⊆ Opt_B(K).
```

This is valid because closing an inter-block gap from three to two leaves the feasibility and cost of **any previously feasible original indexed-center subset** unchanged: each event already has an own-block center within radius two; across a shortened gap the best newly reachable opposite-block center can be at distance two, never better than the existing nearest distance. The previously computed optimal objective levels at the two endpoints therefore match for all closure backgrounds.

For any of the **original** nested optimum pairs `S⊂U` from the previous section, both sets remain feasible **with the same costs** after arbitrary gap closures. Since their costs equal the closure-independent global optimum at their respective cardinalities, they both lie in `Opt_B`. Therefore the same nested pair works in **every** closure background for its K, establishing the claimed universal pairwise theorem. This is a finite exact transfer argument, not a probabilistic extrapolation or a claim that all 268 million patterns were individually enumerated.

## Actual computation, artifacts, and limits

`VERIFY_R5_UNIVERSAL_NESTEDNESS.py` reconstructs the 954 frozen coordinates and directly computes the optimal-insertion-gain DP, checks all 662 adjacent original-budget transitions, independently compares its min-cost levels to the previous exact path-count DP, and computes all 662 transitions under each of the four effective two-bit closure cases (`none`, `15`, `17`, `both`). It also checks the full gain DP against exhaustive indexed-center subset enumeration on 240 small seeded integer-coordinate inputs, 3–8 events each, with exact integer semantics. Execution returned `PASS_R5_ALL_CLOSURE_PAIRWISE_NESTEDNESS`; the generated summary is in `EXACT_NESTEDNESS_CERTIFICATE.json`. The mathematical all-background conclusion follows from the proved transfer lemma, not random tests.

Source modules inherited from the same Draft PR are `VERIFY_R5_COST_SPECTRA.py` and `VERIFY_R5_OPTIMAL_WITNESSES.py`, at the exact frozen R5 derived science input. The local run used a faithful reconstruction of their code; original remotely posted imported bytes have not been separately independently re-executed in this turn. Independent review remains `NOT_REVIEWED`; no formal Task/CLAIM, Result or X6-state theorem is inferred.

**Next frontiers:** classify `ρ_B(K)` below K292, first the cost-invariant but potentially optimizer-sensitive range K214..291, then the low-budget K207..213 feasible cases. A separate native 2,520-byte certificate, 28-coordinate, 8,192-prefix-query performance experiment remains open.
