# T6 p13 order 9: signed split(1,8), first three negative-roster lengths

Date: 2026-11-23. Frozen scientific input `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. Research lane `chatgpt-research-onhour-enterprise-math-20260923`.

**Author-executed exact finite result:** For one positive vertical atom of q-order 1 and a negative vertical roster of total q-order 8 with **1, 2, or 3 named atoms**, no genuinely support-disjoint pair admits a twelve-dimensional q0 signed compensation satisfying six necessary 13-adic mixed congruences and the original both-side mass caps 2331.

A shared named vertical atom between the two sides is cancelled before the new-case search and remains part of previously excluded lower-order cases; it is not spuriously counted as a new admissible distinct shape. The full raw ordered pair universe is 81,432, with 5,328 common-atom pairs, so 76,104 disjoint cases were exactly searched.

| Negative q pattern | Raw ordered pairs | Already-cancellable pairs | Exact GS nodes | Ball leaves | Budget legal |
|---|---:|---:|---:|---:|---:|
| (8) | 144 | 0 | 366 | 0 | 0 |
| (1,7) | 1,728 | 144 | 4,086 | 0 | 0 |
| (2,6) | 1,728 | 0 | 4,473 | 0 | 0 |
| (3,5) | 1,728 | 0 | 4,437 | 0 | 0 |
| (4,4) | 936 | 0 | 2,452 | 1 | 0 |
| (1,1,6) | 11,232 | 1,728 | 24,344 | 0 | 0 |
| (1,2,5) | 20,736 | 1,728 | 48,106 | 1 | 0 |
| (1,3,4) | 20,736 | 1,728 | 48,318 | 1 | 0 |
| (2,2,4) | 11,232 | 0 | 28,817 | 0 | 0 |
| (2,3,3) | 11,232 | 0 | 28,410 | 0 | 0 |
| **Total** | **81,432** | **5,328** | **193,809** | **3** | **0** |

The three nonempty lattice-sphere leaves are fully recorded in the exact certificate. Their original signed masses are (3981,3716), (5302,2525), and (3228,4251); none meets the 2331-per-side bound.

The actual necessary congruences are
```
sum_{r=1}^{12} u_r r^{-j}
+ sum_{(q,r) in V_plus} (13q+r)^(-j)
- sum_{(q,r) in V_minus} (13q+r)^(-j)
 == 0 mod 13^j, j=1,...,6.
```
For vertical costs `c_plus,c_minus`, the weighted 12D q0 lattice sphere has squared radius `(2331-c_plus)^2+(2331-c_minus)^2`, strictly below `2*2331^2` and below the existing exact minimum Gram–Schmidt diagonal square. Full rational/integer enumeration examines the only two possible neighboring integers at each coordinate and checks the original two side masses after reconstruction. The frozen full denominator and sign/multiplicity semantics are preserved.

Evidence:
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN1TO3_AUTHOR_CERT_20261123_0900.json` @ `9509ae14b87f5edc5768c5002beb998476b7b35a`, blob `3f6140312a8b950e83d72233128e098a3b44fb36`;
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN1TO3_EXACT_REPLAY_20261123_0900.py` @ `40f4a45b75b437dca17d74f9d77afe23c50ab261`, blob `162eb32e0fd01d6e8942e4d010702931542b6706`;
- Previous complete p13 q9 split(0,9) author result: `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split0_9_complete_author_exclusion.md` @ `0423e5bc23e3d074e89e0e5c33818013e004c98f`.

The checker source was published and read back, but has **not** been separately rerun after publication; local exact author calculation was executed. This is **AUTHOR_EXACT_FINITE_EXECUTED / GITHUB_VERIFIED / UNREVIEWED / NOT_ADMITTED**, not a native Task Result, independent review or global (T_6) proof.

**Next minimal new finite domain:** p13 order9 signed split(1,8), negative-side vertical roster length **4**, with exact full named-roster enumeration and common-atom cancellation. Continue through lengths 5–8 and the remaining sign splits only after consuming existing Source evidence. The formal Source's separately delegated p17 q14 split(7,7) preflight remains unchanged. Historical Activity328 attribution is unresolved; do not borrow the old Researcher identity to append.
