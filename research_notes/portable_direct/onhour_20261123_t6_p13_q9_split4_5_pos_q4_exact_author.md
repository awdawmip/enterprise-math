# T6 maximal p13, q-order9 signed split(4,5): complete positive (4) finite exclusion

2026-11-23. Frozen scientific input: awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca.
Mother task: RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND. Portable author mathematics only; not Native PROGRESS/Result.

## Exact statement
Assume the original H0,...,H6 shapes, both original exponent side masses at most 2331, the saved cancellation of higher 13-valuations, and the saved saturated q0 lattice.
For maximal prime 13, valuation-one vertical order9 split(4,5), when the positive side contains exactly one named q4 vertical atom (4,r) (1<=r<=12), there is no admissible disjoint-support collision with any negative q-order5 named roster. Shared named vertical atoms reduce to previously handled lower-order units.

## Exhaustive integer/rational search
Each vertical named atom (q,r) denotes full denominator 13*(13q+r) and exponent cost 13*(13q+r)-1; q0 costs 13r-1. Negative q5 partitions and their residue multisets were enumerated without replacement of named atoms by totals.
| Negative q partition | Raw pairs | Shared canceled | Exact GS recursion nodes | Sphere leaves |
|---|---:|---:|---:|---:|
| (5) | 144 | 0 | 373 | 0 |
| (1,4) | 1728 | 144 | 3701 | 0 |
| (2,3) | 1728 | 0 | 3975 | 0 |
| (1,1,3) | 11232 | 0 | 25440 | 0 |
| (1,2,2) | 11232 | 0 | 25346 | 0 |
| (1,1,1,2) | 52416 | 0 | 115508 | 0 |
| (1,1,1,1,1) | 52416 | 0 | 112536 | 0 |
| **All** | **130,896** | **144** | **286,879** | **0** |

The negative side has 10,908 distinct canonical named rosters. SHA256 for newline-separated Python str(negative_roster), iterated by ascending partition length, nondecreasing q tuple and residue multiset, is 8923ff59c75c4efc039018e9a280ad37742021ab20d09ffdba514e858c38699d.
All 130,752 disjoint pairs have exact vertical mass within side bounds. Necessary equations for j=1..6:
sum_{r=1}^{12} u_r*r^(-j) + (13*4+rpos)^(-j) - sum_{(q,r) in negative}(13q+r)^(-j) = 0 modulo 13^j.
Build the saturated 12D q0 integer congruence lattice, index 13^21, and reconstruct the weighted q0 vector with costs 13r-1.
Budget admissibility implies squared weighted norm <= (2331-cpos)^2+(2331-cneg)^2 <= 10867122. Its exact smallest weighted Gram-Schmidt diagonal squared is
78577530278042129705264382752517501995032553011464356025 / 4243983974238642688103181306691645151538473248349 > 10867122.
Each projected coordinate has at most the two neighboring integers that may enter the ball. Descending exact rational recursion tested all such points. None entered the ball, so the full finite subcase is excluded.

## Scope and continuation
Exact author computation was executed locally with Python Fraction/SymPy, using the same 12D q0 matrix and affine congruences as the earlier q9 p13 checked cases. Source-boundary: this is author evidence, not independent review; no claim of global T6 closure. This finite scope does not cover other positive patterns of q-order4. Exact statistic file: research_checks/T6_P13_Q9_SPLIT4_5_POS_Q4_AUTHOR_EXACT_CERT_20261123_1058.json.
Next: q-order9 split(4,5) positive (1,3), all negative q5 named rosters, while preserving full original side costs, six mixed congruences, and named composite atoms. Native Source p17 q14 work is independently delegated.
Status: AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. Original logical Research lane retained; current winning native CLAIM unverified.
