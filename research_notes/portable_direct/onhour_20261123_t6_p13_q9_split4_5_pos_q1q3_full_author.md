# T6 p13 q-order 9: complete exact positive (1,3) against all negative q5 rosters

Date 2026-11-23. Frozen science awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca; mother RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND.

## Finite statement
For maximal prime 13 and valuation one, signed q-order 9 split(4,5), take exactly two positive vertical named atoms with q values (1,3), residues r1,r3 independently in 1..12. Let the negative vertical side be any named q-order5 multiset. Under the original H0,...,H6 equality and original mass caps (<=2331 separately on both sides), and using the previously recorded higher-13-valuation cancellation and saturated q0 congruence lattice, **no such support-disjoint signed configuration exists**. Shared named atoms cancel into earlier lower-order cases.

## Exact exhaustive search
Full denominator is 13*(13q+r), integer exponent cost 13*(13q+r)-1, q0 weights 13r-1. All 10,908 q5 named negative rosters and all 12^2=144 positive residue pairs were covered.
| Negative q-pattern | Raw ordered-sign pairs | Shared canceled | Exact GS recursion nodes | Ball leaves |
|---|---:|---:|---:|---:|
| (5) | 1728 | 0 | 4027 | 0 |
| (1,4) | 20736 | 1728 | 42792 | 0 |
| (2,3) | 20736 | 1728 | 42676 | 0 |
| (1,1,3) | 134784 | 30240 | 229543 | 1 |
| (1,2,2) | 134784 | 11232 | 271111 | 1 |
| (1,1,1,2) | 628992 | 134784 | 1052921 | 1 |
| (1,1,1,1,1) | 628992 | 196560 | 899053 | 0 |
| **TOTAL** | **1,570,752** | **376,272** | **2,542,123** | **3** |

Disjoint-support pairs: 1,194,480. Zero had both original side masses <=2331. The three exact affine-ball points are fully represented by the certificate's named positive/negative atoms and signed q0 vectors, with original mass pairs (3289,4693), (3642,3768), (3291,4452). All six exact modulo-13^j equalities were asserted at each ball leaf, j=1..6.

Completeness: Every named q partition is nondecreasing and equal-q residues are enumerated as multisets. The signed q0 lattice is the previously saved saturated 12D lattice of index 13^21. For each (positive,negative) vertical roster, the six congruences define one affine q0 coset; exact weighted Gram–Schmidt coordinates are enumerated by descending two-neighbor recursion. The original side budgets imply weighted affine squared radius <=2*(2331)^2=10,867,122, strictly below the inherited least GS diagonal square 78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349. Thus there is no unvisited q0 point under the original budget.

The execution first completed all negative lengths1..3 in one exact run. The negative patterns (1,1,1,2) and (1,1,1,1,1) were then each exhausted by five disjoint roster index intervals [0,1000),[1000,2000),[2000,3000),[3000,4000),[4000,4368). No interval overlapped, and no length/pattern was silently omitted. The negative-roster order and SHA256 match the earlier 10,908-roster q5 universe: 8923ff59c75c4efc039018e9a280ad37742021ab20d09ffdba514e858c38699d.

Exact author certificate: research_checks/T6_P13_Q9_SPLIT4_5_POS_Q1Q3_FULL_AUTHOR_CERT_20261123_1106.json. Compact replay checker: research_checks/T6_P13_Q9_SPLIT4_5_POS_Q1Q3_REPLAY_20261123_1106.py. The raw local run used exact Python Fraction/SymPy; the published compact checker has not been independently executed after publication.

Scientific strength: AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. This excludes the stated positive (1,3) subfamily only. Native Source separately delegates p17 q14 with its own owner and no present native semantic PROGRESS from this portable result.
Next minimal unit: p13 q-order9 split(4,5), positive (2,2), all q5 negative rosters; later positive (1,1,2),(1,1,1,1), and global lower-prime completion.
