# T6 maximal p17 valuation-one order9 exact finite exclusion

Author research 2026-11-23. Research logical lane chatgpt-research-onhour-enterprise-math-20260923. Researcher EM-X6-FB6990; public session MCP-082892eb480e45dea6d4b9fcc0491034. Evidence AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. Global T6=2332 remains OPEN. No claimed T6 winning native CLAIM or semantic PROGRESS.

Frozen science: awdawmip/enterprise-math research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md, commit d84bd940cfb093cdc60e569f15cad58772a51dca (blob 87b3a6f38e9350f7a3f56624b27bff2a7778a439). Each signed exponent-shape side mass <=2331, full named denominators, signs/multiplicities and equality of H0..H6.

For p17 valuation-one atom (q,r), q>=1 and 1<=r<=16, denominator 17(r+17q), mass 289q+17r-1. Any side with vertical order >=9 costs at least 9*289+16=2617 >2331. Therefore the only possible total-order9 splits, up to side exchange, are (1,8),(2,7),(3,6),(4,5). With signed q0 variables u_1..u_16, global H1..H6 equality imposes the exact necessary congruences: for each j=1..6, sum(u_r * r^(-j)) + sum(m_(q,r) * (r+17q)^(-j)) == 0 modulo 17^j. The lower-prime denominators are unrestricted and do not affect these necessary conditions.

## Fully executed signed finite search, integer arithmetic
| Split | Raw roster pairs | Shared named vertical support | Primitive pairs | Corrected interval recursion nodes | Complete outward sphere leaves |
|---|---:|---:|---:|---:|---:|
| (1,8) | 16 | 0 | 16 | 48 | 0 |
| (2,7) | 1,321,944 | 243,838 | 1,078,106 | 2,527,035 | 0 |
| (3,6) | 51,819,264 | 17,889,480 | 33,929,784 | 61,318,004 | 0 |
| (4,5) | 194,058,400 | 84,995,374 | 109,063,026 | 164,410,949 | 0 |
| TOTAL | **247,199,624** | **103,128,692** | **144,070,932** | **228,256,036** | **0** |

Side roster counts for orders1..8: 16,152,1088,6460,30040,47628,8697,1. Every pair in every split was actually executed with the fixed signed 128-bit integer interval checker; the largest (4,5) run examined 194,058,400 raw pairs, all 6460 left rosters, 30040 right, finishing in about 17 seconds with ~7.5 MiB memory. There is no unvisited tail.

## Exact completeness

Reuse the already pinned saturated 16D integer signed q0 homogeneous lattice U from research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json, blob d9ac014355a6a1058cc8a0cf2141a01082628881, with |det U|=17^21 and full reciprocal-modular kernel index 17^21. A complete particular modular lift plus U describes every possible integer signed q0 vector. W=diag(16,33,...,271). The original separate side budget constraints imply the necessary weighted ball inequality norm(Wu)^2 <= (2331-Cpositive)^2+(2331-Cnegative)^2.

The exact Gram-Schmidt squared minimum of the weighted basis is 8350069911612335617606677214061177705401058080646556447012234889468081355909 / 480650972868542992444263969893692042421717754534280313801217347854273 > 17,372,418. The maximum q9 split radius squared is 4,104,685. Thus any solution coefficient lies within one integer of its exact conditional negative GS center. At fixed point S=2^32, outward floor/ceil intervals are maintained for the exact initial affine residue and every GS coupling; a branch is rejected only when the signed-int128 exact lower-bound energy exceeds R^2 S^2. The corrected recursion propagates original c_i+n_i into subsequent coordinates (not the conditional full GS center). Every leaf from this conservative search is absent, hence the true exact sphere is empty.

Executed local Python/SymPy generator produced deterministic SHA-256:
order1 8b3910304571b914d946b12776c13a7d67339fa2c9cff64868e3104ac5945ea7;
order2 6df0ade311609510d60f964e2d74899f5cecef1305ac3bd30353c22665ac346f;
order3 532819f8ded2b425ffe14e5220c8434436cbec1c6dff54a190573cda68d9d9cb;
order4 2f3656fa0b7a9b693926453a399658f0fe3f8d7b3669c38fd4050445f44c387b;
order5 c8f35cf3b4fad727df83fb427eebdab35e57d79bbe96e0c0bc9beaf9cca3b97d;
order6 55ad7b048c042f476c6891efc90cb6963a431291d92e55aed8c7889c983677d3;
order7 9239e2dece6f7b56ddfa7dc12bd072848fe044e2b2594195e7d0a373cc15d95b;
order8 5eb581b31376f57e9da74d4fb8bd3669e76f0b829ea20df9b79872ef8219de39;
GS intervals 4c9fc59b470752c01440db46cdacec6e5c41737d05d74522f8c1dfeb1229169b.

Published code: research_checks/T6_P17_Q9_INTERVAL_GENERATOR_20261123.py and corrected generalized research_checks/T6_P17_Q8_INTERVAL_EXHAUSTIVE_CHECK_20261123.cpp. Publish-and-readback of the code succeeded; newly published reproducer has NOT independently been executed since publication. The actual local code and generator equivalent were fully executed and original run output retained; independent review pending.

**Scoped result:** no primitive maximal-p17 valuation-one vertical-order9 signed shapes within both mass budgets can satisfy all globally necessary mixed 17-adic conditions; low-prime completion cannot rescue these absent modular solutions. Next primitive order10 splits (2,8),(3,7),(4,6),(5,5) must be checked; splits (0,10),(1,9) violate at least one side budget. Higher p17 order, p13 and smaller primes, and whole T6 remain unfinished.
