# R39 exact verification evidence

Date: 2026-11-10. Frozen scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Executed with Python Fraction / integer isqrt / integer Euclidean Floor Sum. Every shared S_z(L,J) was evaluated on both exact rational enclosure endpoints, required equal, and every nonempty selected source was checked for its correct owner at both endpoints. Two short windows were additionally checked by direct enumeration. All eleven cases matched the independent R38/R36 per-arc Floor Sum last-source oracle.

Operation unit: one shifted Floor Sum S_z(L,J) per distinct (L,z), excluding two-endpoint certification overhead. The independent oracle uses two shifted sums per arc-count query.

| Case | m | Labels tested | Independent shifted sums | Shared shifted sums | Reduction |
|---|---:|---:|---:|---:|---:|
| near-third mixed, 45 narrow | 257 | 45 | 2490 | 1230 | 50.6% |
| near-third | 21 | 21 | 1162 | 884 | 23.9% |
| near-fifth | 31 | 31 | 1920 | 1369 | 28.7% |
| near-seventh | 50 | 50 | 3094 | 2340 | 24.4% |
| near-third short | 21 | 21 | 106 | 85 | 19.8% |
| near-fifth short | 31 | 31 | 156 | 125 | 19.9% |
| near-third 10^15 origin | 21 | 21 | 1718 | 925 | 46.2% |
| mixed small m | 16 | 16 | 886 | 281 | 68.3% |
| mixed m32 | 32 | 32 | 1772 | 574 | 67.6% |
| mixed m128 | 128 | 128 | 7084 | 2104 | 70.3% |
| near-fifth mixed m128 | 128 | 128 | 7082 | 1996 | 71.8% |

Mixed m257 case: theta=1/3+sqrt(2)/1000, J=10^9, N=10^8. 45 narrow arcs handled in R39 and 212 wide arcs retain the R38 lanes. For like-for-like interval certification, R39's 1,230 distinct shifts require 2,460 actual rational-endpoint Floor Sum recurrences, against 4,980 for a non-cached per-arc endpoint-certified selector. Full numeric and source input tuples are reproduced in VERIFY_R39.py. The 11-case local full certificate records every returned owner-labelled source and all query metrics.

Observed verdict: PASS_R39_SHARED_ENDPOINT_FLOOR_SUM_EXACT_WITH_11_ORACLE_CHECKS.
Complete local certificate digest SHA-256: c8ffa3fbf39c4e47593c98e8d1bfe41333e4fca0d3a0ccfeb8f7c3b1ea848cc4.

This is author-side exact regression evidence and a hand-proved shared-count theorem. No claim of full 10^12-horizon S23 recalculation, formal proof assistant check, or independent reviewer approval.
