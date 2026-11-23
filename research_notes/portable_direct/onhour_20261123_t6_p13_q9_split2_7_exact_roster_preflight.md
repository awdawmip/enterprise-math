# T6 p13 order9 signed split(2,7): exact roster and common-atom preflight

2026-11-23. Frozen Task science: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. Mother target T6=2332 remains OPEN. The signed split(1,8) complete author-level exclusion was checkpointed in `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split1_8_all_negative_lengths_author_exact_exclusion.md`.

## Exact input census

For total positive vertical q-order2, the complete named roster is either one atom `(2,r)` (12 possibilities) or two `(1,r)` with weakly increasing residue (multiset `C(13,2)=78` possibilities). Thus exactly 90 positive rosters. For negative q-order7, all 15 nondecreasing integer q partitions are covered, with independent nondecreasing residues in each equal-q block. The total is 153,960 negative rosters, yielding **13,856,400 signed raw pairs**.

Both standalone vertical side budgets automatically pass here: for any negative q-order7 with `L<=7` named atoms and residue sum `R<=12L`, its exact original exponent cost is `13*13*7+13R-L=1183+13R-L<=1183+155L<=2268<2331`; positive q-order2 has at most two atoms and total cost at most 648. This only concerns vertical costs; the final q0 signed side costs remain to be checked by exact GS completion.

Shared named vertical atoms cancel into previously handled lower-order cases. Fix a negative roster; let `d_1` count distinct negative residues with q=1 and `d_2` distinct negative residues with q=2. Of 90 positive rosters, precisely

```
common_count = d_2 + [78 - binom(13-d_1,2)]
```

share a named atom: the first term covers the 12 q2 singleton choices and the second term covers q1 two-residue multisets not completely outside the negative q1 support. The q2 and two-q1 types are disjoint. Applying this exact formula across all 153,960 named negative rosters gives 5,547,384 pairs with common named support, and **8,309,016 genuinely disjoint signed pairs** needing mixed congruence/affine search.

| Negative q pattern | Negative rosters | Raw pairs | Shared-atom pairs | Disjoint pairs |
|---|---:|---:|---:|---:|
| 1111111 | 31,824 | 2,864,160 | 1,493,856 | 1,370,304 |
| 111112 | 52,416 | 4,717,440 | 2,122,848 | 2,594,592 |
| 11113 | 16,380 | 1,474,200 | 567,216 | 906,984 |
| 11122 | 28,392 | 2,555,280 | 866,736 | 1,688,544 |
| 1114 | 4,368 | 393,120 | 125,280 | 267,840 |
| 1123 | 11,232 | 1,010,880 | 250,560 | 760,320 |
| 115 | 936 | 84,240 | 19,944 | 64,296 |
| 1222 | 4,368 | 393,120 | 63,648 | 329,472 |
| 124 | 1,728 | 155,520 | 22,464 | 133,056 |
| 133 | 936 | 84,240 | 11,232 | 73,008 |
| 16 | 144 | 12,960 | 1,728 | 11,232 |
| 223 | 936 | 84,240 | 1,728 | 82,512 |
| 25 | 144 | 12,960 | 144 | 12,816 |
| 34 | 144 | 12,960 | 0 | 12,960 |
| 7 | 12 | 1,080 | 0 | 1,080 |
| **TOTAL** | **153,960** | **13,856,400** | **5,547,384** | **8,309,016** |

These numbers were produced by the exact standalone checker `research_checks/T6_P13_Q9_SPLIT2_7_EXACT_ROSTER_PREFLIGHT_20261123.py` using integer partitions, residue multiset enumeration and the above complement count, without floating-point arithmetic.

## Next exact mathematical unit

This is a completed **input census and cancellation normalization**, not an exclusion of the signed (2,7) split. Next execute exact mod-13^j and saturated 12D q0 affine search, beginning with negative q-partition `(7)` (12 negative named rosters × 90 positive named rosters = 1080 signed raw pairs; no shared atoms), or the next least costly disjoint partition as fits actual computation. Retain separate original side costs and full named pos/neg residues, signed integer q0 vectors and all witnesses. The recorded 8,309,016 disjoint pairs are the exact full remainder, permitting rigorously disjoint chunk boundaries.

Status: `AUTHOR_EXACT_INTEGER_PREFLIGHT_EXECUTED / UNREVIEWED / NOT_ADMITTED`. No native claim or official Progress/Result is asserted.
