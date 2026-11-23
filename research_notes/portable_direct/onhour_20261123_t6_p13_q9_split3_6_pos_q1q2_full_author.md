# T6 maximal p13 q-order 9 signed split (3,6): positive q-pattern (1,2) full exact author exclusion

Date 2026-11-23. Frozen source `enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

In original H0...H6 two-side exponent-shape problem, each side has exponent mass at most 2331, with integer composite denominators and multiplicities retained. For maximal prime13 and 13-valuation1, consider vertical q-order split (3,6). The positive side consists of two named atoms with q=(1,2), residues r1,r2 independently in 1..12 (144 possibilities). The negative side is any named q-order6 multiset of length1..6: 42,614 canonical rosters. The high-valuation p13 cancellation theorem and exact saturated 12D q0 congruence lattice are retained.

The six necessary mixed congruences are
```
sum_r u_r*r^(-j) + (13+r1)^(-j)+(26+r2)^(-j)
  - sum_(q,r in negative) (13q+r)^(-j)=0 mod 13^j, j=1,...,6.
```
The exact original vertical masses are c_plus=505+13(r1+r2) and c_minus=169*6+13*sum(negative residues)-negative_length. Every legal q0 lift has weighted norm-square at most R²=(2331-c_plus)²+(2331-c_minus)² <= 4,943,025, smaller than the least exact GS diagonal square (about 18,515,039.35). Hence exact two-nearest integer Gram–Schmidt recursion is exhaustive.

| Negative length | Negative rosters | Raw pairs | Shared name canceled | GS nodes | Sphere leaves | Both budgets legal |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 12 | 1,728 | 0 | 3,999 | 0 | 0 |
| 2 | 366 | 52,704 | 3,456 | 112,626 | 1 | 0 |
| 3 | 3,028 | 436,032 | 71,712 | 814,390 | 1 | 0 |
| 4 | 10,452 | 1,505,088 | 383,616 | 2,451,038 | 3 | 0 |
| 5 | 16,380 | 2,358,720 | 773,136 | 3,390,343 | 0 | 0 |
| 6 | 12,376 | 1,782,144 | 628,992 | 2,416,581 | 2 | 0 |
| **Total** | **42,614** | **6,136,416** | **1,860,912** | **9,188,977** | **7** | **0** |

All 4,275,504 disjoint pairs were searched, with zero vertical-only budget rejects. Nine disjoint, complete negative-roster index ranges [0,5000),...,[40000,42614) were executed. All seven sphere leaves were independently checked using Python integer exact original masses and the six inverse-power congruences; none satisfied both side 2331 caps. The source roster SHA256 (`length q1 r1 ...\n`) is `2903878eca1eca25658a941fde216136f568e3cdeb38db6c1a892738f546f356`.

The exact checker and all seven complete signed vectors are committed in `research_checks/T6_P13_Q9_SPLIT3_6_POS_Q1Q2_AUTHOR_REPLAY_20261123_1026.py` and `research_checks/T6_P13_Q9_SPLIT3_6_POS_Q1Q2_AUTHOR_EXACT_CERT_20261123_1026.json`. Author computation used GMP exact rational arithmetic, published full Python replay is not yet rerun.

**Conclusion:** complete p13 q-order9 signed (3,6) positive q-pattern(1,2) is author-excluded. Alongside the separately completed single q3 positive case, one positive pattern (1,1,1) remains. A full p13 layer/global T6 conclusion is not claimed. Native formal Source p17 q14 (7,7) preflight is independently owned; Source admission and nonauthor review are pending.
