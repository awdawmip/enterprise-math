# T6 maximal p13: vertical order8 signed split (0,8), author exact global-mixed exclusion

Date: 2026-11-23 (Asia/Hong_Kong), research conversation `chatgpt-research-onhour-enterprise-math-20260923`. Frozen task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`, original `H_0,...,H_6` and each-side exponent mass cap 2331.

## Statement

**Within the p13 valuation-one vertical total order8, split (0,8), no original integer exponent shape collision with identical `H_0,...,H_6` and both exponent masses ≤2331 is possible**, assuming the previously saved complete p13 higher-valuation cancellation and saturated q0 lattice lemmas. This is a complete **author** exact finite census of this one signed split; other p13 order8 splits remain unresolved. The original lower-prime-only denominators remain allowed.

Preserve named atom `(q,r)` with denominator `13(13q+r)` and cost `169q+13r-1`, the signed q0 vector on `13r`, and all six necessary mixed congruences `sum u_r*r^(-j) - sum_(q,r in V-) (13q+r)^(-j) ≡ 0 mod 13^j`, `j=1..6`. The original q0 12D saturated lattice has index `13^21` and exact Gram–Schmidt minimum diagonal-square greater than `2*2331^2`, so floor/ceil exact-coordinate branching exhausts every vector within the necessary two-side radius.

## Exhaustive computation

The complete order8 negative-side canonical named roster comprises **521,235** multisets. Five disjoint sorted-roster slices cover indices [0,10000), [10000,160000), [160000,310000), [310000,460000), [460000,521235).

| Ordered index range | Raw configurations | Vertical over budget | Exact GS recursion nodes | Relaxed leaves | Budget-valid |
|---|---:|---:|---:|---:|---:|
| [0,10000) | 10,000 | 0 | 28,876 | 0 | 0 |
| [10000,160000) | 150,000 | 94 | 421,062 | 1 | 0 |
| [160000,310000) | 150,000 | 143 | 422,030 | 1 | 0 |
| [310000,460000) | 150,000 | 931 | 414,371 | 2 | 0 |
| [460000,521235) | 61,235 | 928 | 168,868 | 2 | 0 |
| **Total** | **521,235** | **2,096** | **1,455,207** | **6** | **0** |

All six relaxed candidate vectors satisfy the exact six modular conditions. Their respective actual exponent side mass pairs are (4877,4115), (3537,3767), (1698,6003), (2287,5866), (6553,1763), (1988,4855); none meets both 2331 caps. The certificate contains every named original atom, signed q0 vector, exact squared radius/norm, source-order digest and segment counts.

The local calculation used exact Python `Fraction` plus SymPy integer LLL and cached each `(q,r)` atom's 12 coordinate values; **no float comparison was used for membership or congruence**. The matching slower GitHub replay checker `research_checks/T6_P13_Q8_BOUNDED_AUTHOR_AFFINE_CHECK_20261123.py` has been published, but not separately rerun after publication. Scope: `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`. Original T6 global threshold still OPEN.

## Next scientific question

At a fresh canonical Source check, consume any already-saved p13 q8 successor before starting the lowest other admissible split **(1,7)**, preserving genuine modular survivors for lower-prime completion. Use q0 lattice, full six mixed p13-adic digits, original named atoms and true separate masses. There is no established current winning native CLAIM for this lane, so no protected semantic PROGRESS or Result is asserted.
