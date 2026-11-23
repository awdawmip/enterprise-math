# T6 p13 q-order9: signed split(2,7), positive q-pattern (1,1) complete exact exclusion

Date: 2026-11-23. Scientific pin: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. This is author-executed exact finite science, `UNREVIEWED / NOT_ADMITTED`.

## Complete original domain and result

The positive vertical side has **two** q=1 atoms with any unordered named residue multiset in 1..12, yielding C(13,2)=78 possibilities. The negative vertical side has q-order7, any length1..7, all nondecreasing q partitions and canonical named residue multisets (153,960 negative configurations). Both sides retain actual composite denominator 13(13q+r), sign, multiplicity, and exponent masses <=2331; original H_0,...,H_6 equality implies the six exact mixed congruences. For this **entire positive length-two subcase**, no original-budget candidate exists.

The prior exact saturated p13 q0 lattice (index 13^21) encodes the q0 signed vector. For each negative configuration and each positive multiset, enumerate exact rational Gram–Schmidt nearest integer branches within
`R^2=(2331-c_plus)^2+(2331-c_minus)^2`,
where `c_plus=336+13(r1+r2)` and `c_minus=169*7+13*sum(negative residues)-length`. Here `R^2 <= 5,167,457`, while the exact minimum GS diagonal-square exceeds 18,515,039, making the two nearest integer branches per coordinate exhaustive.

| Negative length | Negative rosters | Raw signed pairs | Common-name canceled | Exact GS nodes | Sphere leaves | Both budgets valid |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 12 | 936 | 0 | 2,293 | 0 | 0 |
| 2 | 432 | 33,696 | 1,728 | 75,818 | 0 | 0 |
| 3 | 4,536 | 353,808 | 51,912 | 698,270 | 0 | 0 |
| 4 | 19,968 | 1,557,504 | 417,024 | 2,586,438 | 3 | 0 |
| 5 | 44,772 | 3,492,216 | 1,381,536 | 4,709,721 | 8 | 0 |
| 6 | 52,416 | 4,088,448 | 2,070,432 | 4,435,902 | 0 | 0 |
| 7 | 31,824 | 2,482,272 | 1,493,856 | 2,143,448 | 3 | 0 |
| **Total** | **153,960** | **12,008,880** | **5,416,488** | **14,651,890** | **14** | **0** |

All 6,592,392 disjoint pairs were covered by six exact nonoverlapping canonical negative-roster index ranges: [0,10000), [10000,30000), [30000,60000), [60000,90000), [90000,120000), [120000,153960). The same-name cases cancel to previously closed p13 q-order7, and none of the other disjoint cases violates the vertical-only cap. Fourteen exact affine-sphere leaves were found. All fourteen have been separately checked using exact integer side masses and inverse-power congruences modulo 13^j for j=1,...,6; each violates at least one full-side cap. Full signed vectors, named atoms and both masses are in the JSON certificate.

Complete negative roster stream SHA256, using lines `length q1 r1 q2 r2 ...\n` in canonical enumeration order:
`a551554e8c631814caee26fb6471150f01f044f38f0bf35e96503d25e21901f9`.
The author ran six segment-specific GMP exact rational C++17 searches and verified all 14 survivors independently in Python. Published exact Python replay: `research_checks/T6_P13_Q9_SPLIT2_7_POS_Q1Q1_AUTHOR_REPLAY_20261123_1026.py`; full post-publication Python replay remains unexecuted.

## Consequence and smallest next unit

The other positive q-order2 partition is the **single q2 atom**. Its previously published full negative q7 enumeration gave 1,847,520 raw pairs, six budget-invalid affine leaves, and no legal pair. Hence together these two positive partitions exhaust the maximal-p13 valuation-one signed **order9 split(2,7)**, under the saved higher valuation cancellation and saturated q0 lattice dependencies. Orders/splits (0,9),(1,8),(2,7) are thus author-excluded, while signed (3,6),(4,5), lower-prime completion and global T6=2332 remain open.

Next research: signed q-order9 split(3,6) smallest as-yet-unexecuted positive/negative q partitions; maintain exact original side caps and full named p13 carrier. Formal Native p17 q14(7,7) preflight remains independently owned. This p13 portable proof is neither Native PROGRESS nor formal Result/review.
