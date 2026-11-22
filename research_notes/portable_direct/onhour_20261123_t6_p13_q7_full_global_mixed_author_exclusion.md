# T6 maximal-p13 vertical order7 — full global-mixed exact author exclusion

Date: 2026-11-23 (Asia/Hong_Kong), Research lane `chatgpt-research-onhour-enterprise-math-20260923`. Mother task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`, frozen mass cap **2331 per side**, original exact BRC observers `H_0,...,H_6`.

## Statement and conclusion

**Author finite proposition (dependency-conditional):** Assuming the already-recorded maximal-p13 valuation≥2 cancellation and saturated 12-dimensional q0 congruence lattice, there is **no** pair of distinct original exponent shapes whose largest prime is 13, with each side exponent mass ≤2331, equal `H_0,...,H_6`, and valuation-one p13 vertical total order exactly **7**. This result covers *every* split of order7 and allows arbitrary p13-free lower-prime denominators. It is `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`; global T6=2332 is still **OPEN**.

For a valuation-one atom labelled `(q,r)`, `q>=1,1<=r<=12`, retain its actual denominator `13(13q+r)` and exponent cost `169q+13r-1`. The q0 signed vector `u_r` uses denominator `13r`, weight `13r-1`. From all six exact original shape-moment equalities, for `j=1,...,6` the mixed congruences
```
sum_{r=1..12} u_r*r^(-j) + sum_{(q,r) in V+}(13q+r)^(-j)
 - sum_{(q,r) in V-}(13q+r)^(-j) ≡ 0 (mod 13^j)
```
are necessary, regardless of the smaller-prime atoms. The saturated lattice has index `13^21` and exact Gram–Schmidt minimum squared diagonal `18,515,039.35...` (the exact rational is in the prior q0 proof); the two-side budget enforces radius squared ≤`2*2331^2=10,867,122`. Since radius squared is strictly smaller than every GS diagonal square, at any recursion coordinate only floor/ceil of the negative exact center can survive; exhaustive exact Fraction recursion and signed budget checking close the finite domain. Vertical states are canonical named and multiplicity-preserving; common opposite-side vertical atoms are canceled to an already-lower order rather than counted as new primitive outcomes.

## Results: complete four-way partition

| Split | Original named pairs | Removed common support | Primitive pairs | Exact GS nodes | Sphere leaves | Both caps valid |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (0,7) prior certified | 153,960 | 0 | 153,960 | 447,638 | 2 | **0** |
| (1,6) prior certified | 511,368 | 130,896 | 380,472 | 1,005,734 | 6 | **0** |
| (2,5) prior [0,15) plus new [15,90) | 981,720 | 336,960 | 644,760 | 1,610,793 | 4 | **0** |
| (3,4) new [0,100),[100,310),[310,520) | 1,318,200 | 504,336 | 813,864 | 1,972,315 | 5 | **0** |
| **Total all order7** | **2,965,248** | **972,192** | **1,993,056** | **5,036,480** | **17** | **0** |

The prior `(2,5)` [0,15) has 163,620 raw / 99,400 primitive pairs, 254,294 exact GS nodes and 1 over-budget relaxed leaf. This run computed only [15,90), including 818,100 raw / 545,360 primitive pairs, 1,356,499 exact GS nodes, 3 over-budget leaves. The new (3,4) three slices cover all 520 ordered first-side states against the complete 2,535 second-side states. All 8 new relaxed leaves have exact signed vectors, named atoms, true side masses, norms and radius bounds in the companion JSON. Each of all 17 all-order7 leaves violates at least one side's 2331 budget; no eligible lower-prime completion can restore that excluded q0 mass.

## Execution, exactness, reproducibility and provenance

A locally executed exact SymPy/Fraction implementation reproduced the same published `T6_P13_Q7_BOUNDED_AUTHOR_AFFINE_CHECK_20261123.py` arithmetic, with the expensive fixed LLL basis and 84 atom-to-lattice coordinate vectors cached once, preserving source enumeration order; it did not use floating point for inclusion or modular checks. Four new disjoint slices completed; their raw ordered-pair SHA-256, exact counts and eight leaf certificates are stored in the companion certificate. The published earlier parameterized checker supports exact reruns of the same slices and was read for this run, but **was not independently reexecuted** after this publication. This author result is not an independent review.

Original partial provenance: `research_notes/portable_direct/onhour_20261123_t6_p13_q7_two_complete_splits_and_partial2_5_author.md`, blob `a120072c0f088eb97b6656b2bbda02d4ce395ea9`; corresponding first15 certificate blob `92af990d76e900fe7afa817fac910855f1209da6`. No previously completed range was represented as new research.

## Next scientific frontier and native boundaries

The new exact unresolved maximal-p13 scientific unit is **valuation-one vertical order8**, beginning with the lowest canonical admissible split, subject to a fresh Source check for another already-saved author or owner. Apply the same exact mixed congruences and each side's full exponent mass cap; retain lower-prime completions if true kernels survive. Higher orders and the remaining lower-prime layers remain open. A prior historical Source Task snapshot showed `NEEDS_DISPATCH` and no winning T6 CLAIM. Without a fresh authenticated claimant, this GitHub author proof and Research Activity are **portable** and do not constitute Native semantic PROGRESS, formal Result, freeze, review or theorem admission.
