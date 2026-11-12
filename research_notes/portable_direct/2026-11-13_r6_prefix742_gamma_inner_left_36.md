# PREFIX-742-R6 — 36 additional whole-grid BRC–Gamma exclusions

Date: 2026-11-13 (Asia/Shanghai). Objective: PREFIX-675. Predecessor: PREFIX-741.
Frozen scientific pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## New theorem

Let `T_p,T_z` be independent Gamma clocks defined by the frozen 189-level BRC stopped-survivor recurrence; let `Y=max(T_p,T_z)`, `mu=E[Y]`, `M2=E[Y²]`, `W=M2-mu²`, and `V_q(p,z)=q²W(p,z)-q mu(p,z)`. Fix `e=(0,73/500)` and the closed grid cell `R_ij=[i/384,(i+1)/384]×[j/384,(j+1)/384]`.

For **every real q ≥ 2**, every `(p,z)` in any of the 18 closed cells

`(i,j)∈{17,18,19}×{40,41,42,43,44,45}`

and every cell obtained by transposing its coordinates, we prove

`V_q(e)-V_q(p,z) > q²/2 > 0`.

Thus these **36 entire continuous cells** exclude any global maximizer of the frozen auxiliary Gamma objective.

## Certificate and proof

The integer survivor kernel uses 189 levels and has 9,529 nonzero coefficient positions. Normalized Bernstein coefficients `w[n,k]/C(n,k)` are symmetric and nondecreasing toward the central index. Therefore the Gamma-clock survival tails and the two moments of their independent maximum are coordinatewise nondecreasing.

For any closed subrectangle `Q=[a,c]×[b,d]`, set `L=mu(a,b)`, `H=M2(c,d)`, and `t=1/q∈(0,1/2]`. Then `mu(p,z)≥L≥0`, `M2(p,z)≤H`, and
```
[V_q(e)-V_q(p,z)]/q²
≥ W(e) - H + L² - t*(mu(e)-L).
```
The last expression is affine in `t`, so the smaller of its values at `0` and `1/2` is a universal lower bound. Split each 384-grid cell into four closed 768-grid subrectangles; take the minimum of their two exact rational endpoint bounds.

All 18 selected cells passed the exact integer/`Fraction` checks. The table reports `floor(10^6 * lower_bound)` for the new witness and, for an exact collision test, the original PREFIX-712 witness `e0=(0,3/20)` with one unsplit 384-grid cell.

| j | i=17 new / old | i=18 new / old | i=19 new / old |
|---:|---:|---:|---:|
| 40 | 60540908 / -36126720 | 66009435 / -31222595 | 71447256 / -26393026 |
| 41 | 47648822 / -51039437 | 53255568 / -45952258 | 58861163 / -40908053 |
| 42 | 35162669 / -65559205 | 40875269 / -60322849 | 46614521 / -55099571 |
| 43 | 23129965 / -79633855 | 28917394 / -74280971 | 34757418 / -68913085 |
| 44 | 11594040 / -93215419 | 17426771 / -87777259 | 23336092 / -82297935 |
| 45 | 593841 / -106260360 | 6443978 / -100766628 | 12392685 / -95207569 |

The smallest **floor** of the new exact lower bounds equals `593841`; hence every bound is ≥ `593841/1000000 > 1/2`, establishing the strict theorem. The original PREFIX-712 comparator has negative bound for each of the 18 cells, so none passes its original sufficient certificate. Exchangeability proves the transposed 18 cells.

## Union and scope

Every new cell has one index in `{17,18,19}` and the other in `[40,45]`. This support is disjoint from the original PREFIX-713/716/718 certified sets (whose recorded maximum coordinate minima are respectively 128, 79, 79, 110). Later PREFIX-729–741 author additions cover central cells with both indices ≥30, the PREFIX-741 inner strip with lower index ≥20, or transverse cells with upper index ≥70. Therefore the 36 new cells are disjoint from all these authored additions. The original PREFIX-712 full-cell predicate was explicitly rerun as above.

Relative to PREFIX-741's author-level union, the exact incremental count is
```
141720 + 36 = 141756
141756 / 147456 = 11813 / 12288 = 96.13444010416666...%
147456 - 141756 = 5700
```
This is a provenance-conditioned author-level union update, not an independent acceptance of all upstream certificates. A full independent union audit remains separate.

## Actual verification

A standalone Python 3 standard-library implementation rebuilt the 189-row integer kernel, checked 9,529 positions, symmetric/unimodal Bernstein ratios, and both existing `emu` and `eW` numerator SHA256 regressions. It performed all 18 exact 2×2 split-cell calculations and 18 original-witness full-cell tests; it returned `ALL_CHECKS_PASS PREFIX742-R6 18+18=36`. No floating-point inequalities occur in the proof. The checked source, source-dependent compact replay, exact computed evidence, and run log are separate artifacts.

The arithmetic establishes the auxiliary Gamma exclusion on the defined cell family for all real `q≥2`; independent theorem review, complete upstream union audit, task admission and native Claim/Result/Review remain separate operations.

## Next question

Explore `j=46` and beyond for `i=17..19`, or use a tighter 4×4 enclosure for the weakest cell `(17,45)`. Independently execute the compact repository-native replay and audit the entire older union before any promotion.
