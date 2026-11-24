# X6 R184 — Complete exclusion of the next four rank-two root classes

2026-11-25. EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Independent informed static BRC auxiliary-weight research, following R183@a4ab91536a86d7391206d0bc278c7f193fddb46a. Historical lane provenance EM-DIRECT-AE5AD5; current own execution binding not established. X6 read r2-20261125-0610-x6-current-read SUCCEEDED, observed 2026-11-24T22:10:26.205669Z, Source d24ac7095284c82616190e2d45381b3cd6965382: NO_CANONICAL_PUBLICATION_DIRECTORY, execution_authorized=false, native_operational_view_evaluated=false. No CLAIM or owner mutation. Activity linkage pending.

## Frozen scope and result
Port 10, 1,935 unoriented directions, six pair BRC observers, positive auxiliary weights (17t,B,22t,D), exact best item and full strict 3/2 near-direction set; preserve the R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f pins inherited from R183. P000 V5, ACTIVE worldview and joint-relation observer preservation apply. This is an auxiliary coefficient chart, not a native spatial object.

Read the exact R183 replay bank at 51dc01c0ff3020830688353e6c8772a94d3f80a3 and the R182 177-class side census at 6945e591116377f9386c7419b6ce31a2b9e8a146. Excluding the 33 already solved census IDs leaves 144 rows; select all four with minimum single-child event-list size 9. Results:

| class | child | supports | distinct interior events | strata | feasible |
|---|---|---:|---:|---:|---:|
|810|+|31|9|19|0|
|1495|+|29|9|19|0|
|1559|-|25|9|19|19|
|3587|+|28|9|19|0|
|1559 (opposite)|+|29|10|21|0|

The 76 first-child and 21 opposite-child exact tests cover all strata of the respective child; 97 tests total. Class 1559 is the discriminating example: its smaller child is feasible everywhere in the relaxation, while its opposite child is infeasible everywhere. Thus all four root classes are excluded, not merely sampled directions.

The R182 single-child event sufficiency theorem gives constant Boolean feasibility on each child's ternary sign stratum. For rank-two roots r=alpha*u+beta*v, alpha,beta>0, each varying event x crosses at beta/alpha=abs(x.u)/abs(x.v). Coalesce, sort via integer cross-products, and take each exact event ray and each intervening open interval representative (positive sum). Each representative was checked against the original strict sign masks and the expected support count. Clip the real support components first, then retain extreme endpoints and run the inherited fixed-endpoint capacity relaxation at remaining depth five. Geometry uses BigInt and support masks are exact integers with at most 31 supports. This is the same necessary relaxation as R183, not an exact adaptive full-depth tree solver. No new direction scoring. A failed child across all its strata suffices for a root exclusion; passing a child does not construct a tree.

Remaining original classes: 232-4=228, comprising 140 rank two and 88 rank three. Cumulative excluded 4021/4249. The global depth remains 6 <= D_linear <= 7, subject to inherited proofs.

## Executed evidence and reproduction
- 6bfdddedb516032743a729e36f96c4cdc8857715:research_notes/portable_direct/x6_r184_rank_two_next_replay.cjs — standalone Node.js BigInt reproduction, frozen bank and selected census rows embedded. Function implements the R183 recurrence; it was executed in the JavaScript tool runtime, not claimed as an independently tested Node.js run.
- 5fe5ae5a116de9e2aa94fb32cef2566be6c48ab4:research_notes/portable_direct/x6_r184_rank_two_next_replay.json — all 97 stratum representatives, Boolean results and excluded IDs.
Both contents were read back from their returned immutable commits and matched exactly.

## Next
Do not repeat classes 810,1495,1559,3587 or prior exclusions. Next smaller-child size-ten rows are 892,1273,1340,3056,3453,3910. For any partial feasible carrier, intersect the opposite-child strata rather than assuming a full-root survivor. The rank-three polygon refinement remains unexecuted. Activity association and independent mathematical review pending.
