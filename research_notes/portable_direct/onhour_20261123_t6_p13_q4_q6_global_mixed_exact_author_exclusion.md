# T6 maximal-p13 valuation-one orders 4–6: exact global mixed-congruence exclusion (author calculation)

Date: 2026-11-23 Asia/Hong_Kong. Mother task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`; original research lane `chatgpt-research-onhour-enterprise-math-20260923`, author EM-X6-FB6990, original SID MCP-082892eb480e45dea6d4b9fcc0491034. Scope **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**, no winning native T6 CLAIM or protected PROGRESS asserted.

## Exact model and proof dependency

Frozen task input is `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md` @ d84bd940cfb093cdc60e569f15cad58772a51dca. For a signed, cancellation-normalized pair of exponent shapes with **each side mass ≤2331**, retain all named integer denominators, repeated atoms and distinct signs. Consume the previously saved author p13 valuation≥2 cancellation lemma and the exact saturated 12-dimensional p13 q0 lattice, determinant 13^21 and Fraction Gram–Schmidt minimum diagonal square >18,515,039.35. These are dependencies, not independent new reviews.

The valuation-one p13 q0 atom is denominator 13r (1≤r≤12), weight 13r−1. Each vertical atom (q,r), q≥1, has denominator 13(13q+r), exponent weight 169q+13r−1. For j=1,...,6 the full original H0,...,H6 equalities yield the *globally necessary*, lower-prime-safe congruences
```
 sum_{r=1}^{12} u_r r^(-j)
 + sum_{(q,r) in V+} (13q+r)^(-j)
 - sum_{(q,r) in V-} (13q+r)^(-j) = 0 (mod 13^j).
```
The signed q0 affine coset is formed from the published exact particular solutions and saturated q0 integer lattice. Both side budgets give the safe necessary weighted sphere ||Wu||²≤(2331−M+)²+(2331−M−)². Its radius is always smaller than the minimum exact Gram–Schmidt diagonal, so nearest floor/ceil recursion enumerates *every* possible lattice point. At a leaf calculate actual signed q0 side masses, not only total mass or sphere distance. Any overlapping named vertical atom is cancellable and belongs to a previously handled lower order, hence this census covers all **primitive** configurations.

## Executed exact finite enumeration

| Order/split | Raw | Common-support cancelled | Primitive evaluated | Fraction GS recursion nodes | Relaxed sphere leaves | Original-budget valid |
|---|---:|---:|---:|---:|---:|---:|
| q4 (0,4) | 2,535 | 0 | 2,535 | 8,803 | 1 | 0 |
| q4 (1,3) | 6,240 | 1,080 | 5,160 | 16,765 | 0 | 0 |
| q4 (2,2) | 4,005 | 792 | 3,213 | 10,450 | 0 | 0 |
| q5 (0,5) | 10,908 | 0 | 10,908 | 34,393 | 0 | 0 |
| q5 (1,4) | 30,420 | 6,240 | 24,180 | 72,758 | 0 | 0 |
| q5 (2,3) | 46,800 | 12,312 | 34,488 | 100,595 | 1 | 0 |
| q6 (0,6) | 42,614 | 0 | 42,614 | 130,186 | 0 | 0 |
| q6 (1,5) | 130,896 | 30,420 | 100,476 | 281,443 | 2 | 0 |
| q6 (2,4) | 228,150 | 70,020 | 158,130 | 423,495 | 1 | 0 |
| q6 (3,3) | 134,940 | 44,496 | 90,444 | 239,594 | 2 | 0 |
| **Total** | **637,508** | **165,360** | **472,148** | **1,318,482** | **7** | **0** |

All seven relaxed candidates satisfy the six exact modular congruences but fail at least one genuine per-side mass limit. See accompanying compact certificate for signed values, masses, four independent bounded local run fingerprints, full roster coverage counts, and source. In particular q4's unique sphere leaf has side masses 3689/4897 and q5's has 4028/4151.

Original standalone Python/SymPy/Fraction scripts were run for q4, q5, q6 split(0,6)/(1,5)/(2,4) and q6 split(3,3), separately, with a second modular-and-side-mass validation pass for every leaf. A derived replay checker, `research_checks/T6_P13_Q4_Q6_AUTHOR_AFFINE_RECHECK_20261123.py`, is published to rerun each order in-place against previously published q0–q2 source; **this compact derived checker has not independently been rerun post-publication**, and no nonauthor review or Native Result is claimed.

Consequently p13 valuation-one vertical orders 4, 5, 6 are excluded at author exact finite scope under the original full global necessary p13-adic conditions, **conditional on the already-saved higher-valuation cancellation lemma and q0 lattice correctness**. q0–q3 retain their prior scopes. Neither p13's remaining q7+ orders nor p13-free lower-prime completion is resolved. Global T6=2332 remains OPEN.

Next smallest scientific unit: p13 valuation-one vertical order7 canonical splits (0,7),(1,6),(2,5),(3,4). Preserve exact per-side cap, 13-adic mixed conditions and named overlap/cancellation, reuse the existing saturated lattice and partial lower-order certificates, and checkpoint any complete split before a resource limit. Controller: original pending continuation request `onhour-20261123-0431-t6-own-exact-continuation-v1` now SUCCEEDED, native execution_authorized=false; no claimed T6 owner.
