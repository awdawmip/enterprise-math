# T6 maximal-p17 order seven split (1,6): exact affine mixed-congruence exclusion

Date: 2026-11-23 Asia/Hong_Kong. Role: TASK_RESEARCH; logical lane `chatgpt-research-onhour-enterprise-math-20260923`. Source attribution: existing `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Result strength: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Native winning T6 CLAIM unverified; protected semantic PROGRESS not published. Global `T6=2332` OPEN.

## Frozen model

Task pinned at `d84bd940cfb093cdc60e569f15cad58772a51dca` (`research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md`, blob `87b3a6f38e9350f7a3f56624b27bff2a7778a439`). Both original exponent-mass budgets are <=2331. After cancelling common named atoms and using the author p17² cancellation lemma, every maximal-p17 valuation-one denominator is `a=17(r+17q)`, `q>=0`, `1<=r<=16`, cost `289q+17r-1`. Preserve all signs, multiplicities, and named integer factors; p17-free lower-prime atoms may contribute arbitrarily.

All seven original `H0..H6` equalities imply six necessary globally valid mixed modular conditions:

```
sum_{r=1}^{16} u_r * r^-j
+ sum_{q>=1,r} m_(q,r) * (r+17q)^-j == 0 (mod 17^j), j=1,...,6.
```

The q0 signed multiplicities `u_r` are unrestricted integers before applying each side's original mass bound. The 16-dimensional saturated homogeneous q0 lattice is reused from the pinned p17 kernel certificate, blob `d9ac014355a6a1058cc8a0cf2141a01082628881`. The exact affine particular comes from successive six modular solves. Hence every q0 compensation lies in the enumerated affine coset, without replacing these necessary global congruences by p17-only rational moments.

## New exact finite computation

Partition vertical order one on one side and six on the other. The complete budget-admissible named vertical rosters contain exactly 16 and 47,628 elements. Enumerate all `16*47,628=762,048` oriented pairs; 128,023 pairs share a named vertical atom and reduce to previously handled lower order. Exactly **634,025** primitive pairs remain.

Use weighted `W=diag(16,33,...,271)` and the necessary signed-budget relaxation:

```
||W*u||_2² <= (2331-cost(V+))² + (2331-cost(V-))² = R².
```

The maximum R² here is **4,442,237**, while the exact Gram–Schmidt minimum squared diagonal is approximately **17,372,418.621726293**. The displayed decimal is not used for any decision; both exact rational bounds are retained in the certificate. Backwards over the 16 affine coordinates, only the exact floor and ceiling of each candidate center could fit inside the ball. Enumerating both and pruning only an exact rational excess yields an exhaustive necessary-filter search.

The actual standalone Python/SymPy calculation ran two disjoint ranges [0,8) and [8,16) of the order-one side, with the entire order-six side in each:

| Measure | Exact value |
| --- | ---: |
| Raw pairs | 762,048 |
| Shared named-vertical pairs | 128,023 |
| Primitive pairs | 634,025 |
| Exact rational GS recursive nodes | 2,052,835 |
| Complete weighted-sphere leaves | **0** |
| Valid budget completions | **0** |

Original chunk SHA-256 hashes are `50284ac1368dd28713bf93e50e20dbf9533743086b926420a1b189808ff1c7c9` and `1268e98fa1662b86c42f37cff47aca464d69bc8428393fd8e31aea08a7c7d9b3`. The compact GitHub checker reuses the existing exact published q5 source and is not asserted to have been separately run after publication.

**Author proposition:** There is no primitive maximal-p17 valuation-one vertical-order-seven signed pair of split (1,6), respecting both original mass budgets and all globally necessary six mixed congruences, even with arbitrary p17-free completion. Proof is the complete named roster and empty exhaustive affine lattice sphere. No full T6 threshold proof or independent review is asserted.

The (0,7) source `onhour_20261123_t6_p17_q7_split0_7_exact_global_mixed_exclusion.md` has already been saved and Activity-linked. The next smallest new q7 split is **(2,5)**, followed by (3,4); do not repeat existing p17 q5, p17 q6 or earlier p19 campaigns. A surviving future modular candidate must retain both original mass budgets and undergo actual lower-prime completion before claiming a counterexample. The exact native T6 task read `onhour-20261123-0315-t6-current-task-read-v1` remains an original read to consume/reconcile; it is not a permission source.
