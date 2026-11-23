# T6 p13 maximal-prime qorder10 split(0,10): all seven-atom negative rosters excluded at author finite strength

Date: 2026-11-23. Mother Task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`, frozen scientific input `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. Preserve the full named integer denominators `13(13q+r)`, signs, multiplicities, two independent exponent mass caps `M_+,M_- <=2331`, the original `H_0,...,H_6` observers, and the previous high-valuation cancellation and saturated q0 lattice proof.

## Exact finite result

A length-seven negative vertical roster of total order 10 has **exactly three** nondecreasing q-patterns:

| Negative q-pattern | Named rosters | Vertical mass over budget | Exact 12D GS searches | Exact recursion nodes | Relaxed sphere points | Original mass-valid |
|---|---:|---:|---:|---:|---:|---:|
| (1,1,1,1,1,1,4) — previously complete | 148,512 | 52,803 | 95,709 | 262,167 | 2 | 0 |
| **(1,1,1,1,1,2,3) — newly complete** | **628,992** | **219,694** | **409,298** | **1,120,050** | **7** | **0** |
| **(1,1,1,1,2,2,2) — newly complete** | **496,860** | **172,809** | **324,051** | **890,511** | **4** | **0** |
| **All length seven** | **1,274,364** | **445,306** | **829,058** | **2,272,728** | **13** | **0** |

All new finite enumerations are complete over non-overlapping canonical index segments; interrupted unbounded attempts were not counted. The new two patterns were executed by this author using exact SymPy `Matrix` and `Fraction` arithmetic, with explicit named roster indices and SHA256 digest for each complete chunk. Every sphere point was separately checked with exact original two-sided masses and all six congruences; all 11 new relaxed points violate at least one original side mass cap.

For each q0 signed vector `u=(u_1,...,u_{12})`, necessary mixed congruences from the original observers are

```
sum_(r=1..12) u_r*r^(-j) - sum_(q,r in negative) (13q+r)^(-j)
     == 0 modulo 13^j, j=1,...,6.
```

The saturated q0 lattice has index `13^21`, and its minimal exact Gram–Schmidt diagonal square is

```
78577530278042129705264382752517501995032553011464356025
/4243983974238642688103181306691645151538473248349
```

greater than the maximum necessary weighted square radius `2*2331^2=10867122`. Exact two-nearest-integer recursive enumeration consequently covers every q0 point that can survive both original budget bounds. The 13 relaxed finite sphere points (including the two in the previous author certificate) are preserved with their actual signed integer values.

## Durable evidence

- Existing first seven-atom partition certificate: `research_checks/T6_P13_Q10_SPLIT0_10_NEG_LEN7_PATTERN1111114_AUTHOR_CERT_20261123.json`; unchanged and reused.
- New seven-atom partition `(1,1,1,1,1,2,3)`: `research_checks/T6_P13_Q10_SPLIT0_10_NEG_LEN7_PATTERN1111123_AUTHOR_EXACT_CERT_20261123.json`. Four non-overlapping ranges `[0,5000)`, `[5000,150000)`, `[150000,400000)`, `[400000,628992)`, and exact seven relaxed witness vectors.
- New partition `(1,1,1,1,2,2,2)`: `research_checks/T6_P13_Q10_SPLIT0_10_NEG_LEN7_PATTERN1111222_AUTHOR_EXACT_CERT_20261123.json`. Five non-overlapping ranges `[0,5000)`, `[5000,100000)`, `[100000,200000)`, `[200000,350000)`, `[350000,496860)`, and exact four witness vectors.
- Source-published replay wrappers `research_checks/T6_P13_Q10_SPLIT0_10_NEG_LEN7_PATTERN1111123_EXACT_REPLAY_20261123.py`, `research_checks/T6_P13_Q10_SPLIT0_10_NEG_LEN7_PATTERN1111222_EXACT_REPLAY_20261123.py`. Their original author code was executed locally. **These published compact wrappers have not been separately executed after publication; no independent review is asserted.**

Previous qorder10 split(0,10) negative lengths 1–6 were already author-excluded at their exact scope: 1,217,658 named rosters, of which 106,674 exceed the vertical-only mass cap and 1,110,984 received exact GS search, with 3,055,111 exact nodes and 17 relaxed sphere points, 0 original mass-valid. Combining the existing and new finite scopes yields **2,492,022** length1–7 named rosters excluded at author finite strength, **551,980** vertical-only budget failures, **1,940,042** exact GS searches, **5,327,839** exact recursion nodes, and **30** relaxed sphere points (all budget-invalid).

## Research frontier and provenance correction

A direct GitHub tree/immutable-note comparison located an **earlier already-published** full p13 qorder9 split(4,5) positive `(1,1,1,1)` author closure, at `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split45_pos1111_full_exact_author_closure.md` (commit `fae5aa69f087624bf457e75e1876a8f28f5e360e`), with the same total and six relaxed witnesses. The fresh q9 rerun in this Research lane reproduced those data under a different nonoverlapping slicing, **not a new independent mathematical discovery or an independent referee review**. The actual newly completed science in this turn is the two formerly unvisited p13 qorder10 length-seven q-patterns above. Preserve prior author provenance and do not double-count q9.

Next smallest unfinished p13 qorder10 split(0,10) scope is **negative length8**, beginning q-pattern `(1,1,1,1,1,1,1,3)` (seven q1 atoms, one q3 atom; 381,888 named rosters), then pattern `(1,1,1,1,1,1,2,2)` (965,328), length9 `(1,1,1,1,1,1,1,1,2)` (906,984), and length10 ten q1 atoms (352,716). All remain to be checked using original two caps and congruences. Other qorder10 signed splits, higher p13 orders, lower-prime/H0 completion and global `T_6=2332` remain open.

**Status:** `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`. The Native Source p17 q14 delegated preflight, actual author/Activity, current winning CLAIM, semantic PROGRESS and Result have separate authority and are not changed by this portable GitHub publication.
