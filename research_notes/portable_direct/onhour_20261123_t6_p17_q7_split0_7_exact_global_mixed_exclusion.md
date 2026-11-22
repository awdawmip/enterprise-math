# T6 maximal p17 valuation-one / q7 split(0,7): exact global mixed-congruence exclusion

Date 2026-11-23 Asia/Hong_Kong. Research lane `chatgpt-research-onhour-enterprise-math-20260923`. Author-source attribution: existing `EM-X6-FB6990`, public session `MCP-082892eb480e45dea6d4b9fcc0491034`. Scientific status **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Parent T6 objective OPEN. No current winning T6 CLAIM or native semantic PROGRESS asserted.

Frozen input: `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md` at `d84bd940cfb093cdc60e569f15cad58772a51dca` (blob `87b3a6f38e9350f7a3f56624b27bff2a7778a439`). Both exponent-mass budgets are at most 2331; full named denominator `a=e+1`, repeated atom counts, signed sides, q0 alphabet `r=1..16`, and the original seven observers `H0..H6` are preserved.

## Proposition

After the previously authored cancellation of all p17 valuation >=2 atoms and of shared named atoms, **there is no primitive maximal-p17 valuation-one vertical-order-seven pair of side orders (0,7) satisfying all six globally necessary mixed 17-adic reciprocal congruences**, even with unrestricted lower-prime completion.

Write each p17 valuation-one denominator as `17(r+17q)`, with integer `q>=0` and `1<=r<=16`, cost `289q+17r-1`. Let `u_r` be q0 signed occurrence count and `m_{q,r}` the vertical signed count. Full original H0..H6 equality implies, for `j=1..6`,

```
sum_r u_r * inv(r^j, 17^j)
+ sum_{q>=1,r} m_(q,r) * inv((r+17q)^j, 17^j)
== 0 (mod 17^j).
```

No rational equality of the p17 sub-block alone is assumed; p17-free atoms remain arbitrary.

## Exhaustive domain and search

The zero-order side has exactly one empty vertical roster. For the order-seven side, all partitions of `q=7` into positive integers, all named residue multisets and repetitions, and every configuration with vertical-side cost at most 2331 were enumerated. Exactly **8,697** complete order-seven vertical rosters exist. No same-name vertical cancellation is possible against the empty side.

The homogeneous q0 lattice uses the saturated 16x16 basis `U` of pinned `research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json` (blob `d9ac014355a6a1058cc8a0cf2141a01082628881`), with determinant absolute value `17^21`. The affine particular solutions are constructed by sequential exact mixed-modular lifting, and every q0 solution lies in one affine coset of U.

Set `W=diag(16,33,...,271)` and let `c_-` be the order-seven vertical mass. The signed mass budgets imply the necessary exact squared-ball inequality

```
||W u||_2^2 <= 2331^2 + (2331-c_-)^2 = R^2.
```

Across all order-seven rosters, maximum `R^2 = 5,518,825`; the exact minimum Gram–Schmidt diagonal square of `UW` is approximately `17,372,418.62`, with its exact rational value recorded in the certificate. Thus every candidate affine integer coefficient must be one of the floor/ceiling pair at each reversed GS coordinate. Enumerating these exact choices and pruning only proven excess partial squared norms is exhaustive.

The standalone exact Python/SymPy implementation actually executed every one of the **8,697** configurations, visiting **40,799** GS recursion nodes, producing **zero full sphere leaves** and therefore **zero budget-valid q0 solutions**. One complete local results JSON is identified by SHA-256 `ea1c7cdd5077cc650f30c1f9fe611038ab937e9cbd878967b3caef162e007b1b`. The compact repository reproducer extends the existing published q5 solver to q=6,7 atoms without changing its lattice; it has not been separately executed after publication.

Hence the proposition follows by complete finite enumeration and a rigorous necessary spherical relaxation. No low-prime completion or hidden unvisited signed q0 coordinate can restore the required congruences.

## Scope, provenance, continuation

The existing activity contained q6 split(2,4) and split(3,3) author reports by the time this run inspected its full tail. The independent local re-computation of those same ranges is **corroboration, not a newly completed unique science unit**. Its newly saved combined auxiliary artifacts are not another independent review and are not counted twice in Research Activity.

This q7 (0,7) unit is the next separate scientific increment. Next: compute the q7 split (1,6) under the same frozen budget and global mixed congruences, using actual full order-six roster and precise signed q0 affine enumeration. If any complete sphere lattice point survives, check original two budgets and preserve its full named factor identities for subsequent low-prime completion. Do not rerun q5/q6 or p19.

Control read `onhour-20261123-0315-t6-current-task-read-v1` was observed WAITING_RESOURCE/GITHUB_PRIMARY_RATE_LIMIT with automatic original-request resume. The older `onhour-20261123-0105-t6-current-source-cont-v1` is SUCCEEDED but not current ownership authorization. Neither source evidence nor GitHub publication grants native CLAIM/Result or independent mathematical acceptance.
