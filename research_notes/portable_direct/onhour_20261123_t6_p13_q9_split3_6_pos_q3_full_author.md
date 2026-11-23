# T6 p13 q-order9 signed split(3,6), positive single q3: exact exclusion

Date 2026-11-23. Frozen T6 Task: `enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. Result status: `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

Positive side is exactly one (q,r)=(3,r), r in 1..12; negative side consists of all 42,614 canonical q-order6 named rosters, length1..6, including all composite denominators and repeated atoms. Both original signed-side exponent masses are at most 2331. Previously proved p13 high-valuation cancellation and the exact saturated 12D q0 lattice are reused. The six necessary congruences come directly from H_0,...,H_6 equality, with mod 13^j, j=1..6.

The positive vertical mass is `506+13*r` (minimum 519). The smallest negative vertical mass is 1026, so the necessary weighted affine radius-squared is at most **4,986,369**. The existing exact smallest GS diagonal square exceeds 18,515,039. Every possible admissible lattice point is therefore covered by the two-nearest-integer exact rational recursion.

| Negative length | Negative rosters | Raw signed pairs | Common atom canceled | GS recursion nodes | Sphere leaves |
|---|---:|---:|---:|---:|---:|
| 1 | 12 | 144 | 0 | 358 | 0 |
| 2 | 366 | 4,392 | 144 | 10,092 | 0 |
| 3 | 3,028 | 36,336 | 1,728 | 80,178 | 0 |
| 4 | 10,452 | 125,424 | 4,368 | 274,188 | 0 |
| 5 | 16,380 | 196,560 | 0 | 436,957 | 0 |
| 6 | 12,376 | 148,512 | 0 | 323,968 | 0 |
| **Total** | **42,614** | **511,368** | **6,240** | **1,125,741** | **0** |

After shared-name cancellation to prior smaller q-order, all 505,128 disjoint signed pairs were tested; none failed the vertical-only budget and none had a q0 affine ball leaf. The complete negative roster SHA256 from canonical `length q1 r1 ...\n` lines is `2903878eca1eca25658a941fde216136f568e3cdeb38db6c1a892738f546f356`.

Certificate: `research_checks/T6_P13_Q9_SPLIT3_6_POS_Q3_AUTHOR_EXACT_CERT_20261123_1026.json`. Python replay checker reuses the previously committed saturated q0 lattice: `research_checks/T6_P13_Q9_SPLIT3_6_POS_Q3_AUTHOR_REPLAY_20261123_1026.py`. The local GMP exact rational author computation completed; the published Python checker has not been rerun in full.

Conclusion: the entire signed split(3,6) **positive length-one q3** subcase is excluded. Positive q=(1,2) or q=(1,1,1) remain unexecuted, followed by split(4,5), lower prime completion, and global T6=2332. Formal Native T6 p17 q14 preflight and author/owner review remain independent.
