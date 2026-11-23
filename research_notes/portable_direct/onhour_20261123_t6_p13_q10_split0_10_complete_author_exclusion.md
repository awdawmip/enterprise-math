# T6 / maximal-p13 valuation-one: vertical order 10, signed split (0,10), complete finite exclusion

Date: 2026-11-23 (Asia/Hong_Kong).
Research lane: `chatgpt-research-onhour-enterprise-math-20260923`.
Task: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND` (`T6=2332` global target OPEN).
Input pin: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`.
Evidence strength: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.
This is independently preservable *portable* author science, not a protected Native semantic PROGRESS or an independent nonauthor review; current native Source owns the separate p17 q14 delegated preflight.

## Proposition and proof scope

Assume the previously saved p13 higher-valuation cancellation lemma and the full saturated 12-coordinate q0 congruence lattice. Let the only remaining valuation-one p13 vertical atoms have signed decomposition `(0,10)`: ten negative named denominators `13(13q+r)` where `1<=r<=12`, `q>=1`, and the vertical orders sum to ten. Each original side has nonnegative exponent mass at most 2331. Keep the original signed multiplicities, every named denominator, and the necessary readouts from original `H0..H6`.

**Conclusion:** No such configuration satisfies simultaneously the six global mixed congruences `j=1..6` and both original side mass budgets. This excludes the entire `p13, v13=1, q10, split(0,10)` family under the stated prior lemmas. Lower-prime completion and other q10 signed splits remain separate parts of the global target.

For `u=(u_1,...,u_12)`, let `w_r=13r-1`. For any negative vertical roster `V_-`, the necessary congruences are

```
sum_{r=1..12} u_r*r^(-j) - sum_{(q,r) in V_-}(13q+r)^(-j) == 0 (mod 13^j), j=1,...,6.
```

Its source-correct integer coset is `u = x(V_-) + Lambda`, where `Lambda` has exact index `13^21`. Use the previously checked saturated basis, weight it with `diag(w_r)` and take an exact rational Gram–Schmidt reduction. Its minimum diagonal square is

```
78577530278042129705264382752517501995032553011464356025
/4243983974238642688103181306691645151538473248349
```

which exceeds `2*(2331)^2 = 10,867,122`. For the vertical original exponent cost `C_- = sum(169q+13r-1)`, any legal q0 compensation obeys

```
||W u||_2^2 <= 2331^2 + (2331-C_-)^2.
```

If `C_->2331`, the roster is immediately excluded. Otherwise the bound is less than the minimum Gram–Schmidt diagonal square. Express the weighted coset in the integral reduced basis and enumerate from the highest coefficient to the lowest. At each coordinate `D_i>radius`, so an admissible integer can only be `floor(-center)` or that integer plus one. Exact rational inequality checks at all 12 levels cover the complete necessary ball. Every ball leaf is evaluated with exact original signs, named multiplicities, modular residues and *both* budgets. A mere relaxed ball leaf is not a collision.

## Complete roster enumeration

The earlier author continuation already preserved **2,873,910** fully checked q10 (0,10) rosters, covering negative vertical lengths 1-7 plus the length-8 pattern `11111113` at their original author-evidence strength. This new calculation checked all remaining three disjoint pattern families, with original residue multiset ordering:

| New negative q pattern | Named rosters | Vertical overbudget | Exact affine GS cases | GS nodes | Relaxed leaves | Both budgets legal |
|---|---:|---:|---:|---:|---:|---:|
| `11111122` (6 q1, 2 q2) | 965,328 | 566,325 | 399,003 | 1,091,320 | 5 | **0** |
| `111111112` (8 q1, 1 q2) | 906,984 | 665,129 | 241,855 | 659,133 | 0 | **0** |
| `1111111111` (10 q1) | 352,716 | 297,274 | 55,442 | 151,394 | 2 | **0** |
| **New total** | **2,225,028** | **1,528,403** | **696,300** | **1,901,847** | **7** | **0** |

Both the local exhaustive exact checker and a separately implemented direct vertical-integer-mass enumeration agree on the `gs_searches` counts in all three new families. The seven ball witnesses were each checked again with all six original moduli; all have mass overrun on at least one original side. The fully partitioned source index intervals and order digests are recorded in the three published machine certificates.

Combining existing author-scoped evidence with today's three checked families:

| Full q10 split (0,10) count | Value |
|---|---:|
| Total named vertical rosters | **5,098,938** |
| Vertical overbudget | 2,303,241 |
| Exact GS examined | 2,795,697 |
| Exact GS recursive nodes | 7,664,115 |
| Relaxed sphere leaves | 40 |
| Legal original two-sided candidates | **0** |

The exact totals for overbudget and GS cases are obtained by adding the preserved earlier baseline (774,838 overbudget / 2,099,072 GS) to the new evidence; the value of `2,303,241` and `2,795,697` should be cross-checked with the machine records before treating this aggregate as a validated statistic. The mathematical exclusion itself uses the separate complete family proofs, not this display sum.

## Exact research artifacts

- `research_checks/T6_P13_Q10_SPLIT0_10_PATTERN11111122_FULL_AUTHOR_EXACT_CERT_20261123.json` — 965,328 checked configurations, 5 complete signed witnesses, five exhaustive interval digests.
- `research_checks/T6_P13_Q10_SPLIT0_10_PATTERN111111112_FULL_AUTHOR_EXACT_CERT_20261123.json` — 906,984 checked configurations, 0 relaxed leaves, three interval digests.
- `research_checks/T6_P13_Q10_SPLIT0_10_PATTERN1111111111_FULL_AUTHOR_EXACT_CERT_20261123.json` — 352,716 checked configurations, 2 complete signed witnesses.
- `research_checks/T6_P13_Q10_SPLIT0_10_PATTERN11111122_EXACT_REPLAY_20261123.py` and `research_checks/T6_P13_Q10_SPLIT0_10_FINAL_TWO_PATTERNS_EXACT_REPLAY_20261123.py` — published exact replay wrappers; not independently rerun after GitHub publication. Actual author work was executed locally with equivalent exact integer/rational procedures.

## Remaining T6 frontier

The q10 `(0,10)` signed split is closed at author finite-search strength. Next examine q10 `(1,9)` with positive vertical q1 named atoms, preserving common-atom cancellation, both side budgets, the full q0 lattice and all six mixed congruences. Where a true admissible necessary solution appears, retain the full q0 and vertical integer witness for subsequent lower-prime/H0 testing. Source's separate p17 q14 preflight and all historical Result/Activity authors remain untouched. Existing Research Activity 328 attribution is unresolved, so this scientific publication creates neither that Activity event nor a Native CLAIM/Result.
