# X6 Unit66 — Three-sector overlap and signed-shell BRC inclusion–exclusion

Date 2026-11-16. Mother `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`; author lane `chatgpt-research-onhour-enterprise-math-20260923`. Status **AUTHOR-PROVED / EXACT FINITE EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Frozen types and exact historical source

P000 V5 signed native six-axis Cell torsor at source pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical source pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Fix a genuine native Cell start and a selected three-axis signed `Z^3` subtorsor. Each of the three *named* positive two-generator sectors `S12,S23,S31` is a restricted chart on this subtorsor; the old `Sigma_O^(ij)` carrier incidence is not native Cell identity.

Actually read historical `driver_reviews/R061_STAGE1R_NATIVE_LINE_TRACE_FINAL_ACCEPTANCE_20260821.md` blob `adae46be77ae4cad4bacc36c1dccd6a0e6abf1a` lines 73–79: one named `G=25` sector has four ordered pair branches and positive path mass `1+35+35+1=72`. Historical R062 `driver_reviews/R062_STAGE0_BRC_MULTIPATH_ENRICHMENT_BRIDGE_DRIVER_REVIEW_20260821.md` blob `d46593b6c2c257d5ff43f653ab32eb0385b238dd` lines 137–160 separates positive multiplicity from Boolean support. Current signed `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` blob `97ab1403ab04b4fa80034625fb1b2e3ed115e59b` gives signed selected `G=25` shell `(30,846)`. This unit retrospectively *derives* the three-chart min-zero subtotal `(9,213)`; it does not assert that an original historic document called that subtotal the full native shell.

## Exact all-radius theorem

For every integer `g>=1`, set `s(g)=1` if `g` is a perfect square, else 0. Define `R2(g)` = number of nonnegative ordered pairs `(a,b)` with `a²+b²=g`; `W2(g)` = sum of their `binom(a+b,a)` natural signed-step shuffle masses. Let `E(g),W(g)` count respectively distinct nonnegative **at-most-two-support** triples and their shortest-path positive BRC mass in the union of all three named positive charts. Let `Q(g),V(g)` count respectively strictly positive three-support triples `a²+b²+c²=g` and sum of their natural multinomial BRC masses. Let `S(g),B(g)` count all signed triples and their shortest-path natural BRC mass on `Z³` at norm-square `g`.

**For all positive integers g:**

```text
E(g)=3 R2(g) - 3 s(g)       W(g)=3 W2(g) - 3 s(g)
S(g)=4 E(g) - 6 s(g) + 8 Q(g)
B(g)=4 W(g) - 6 s(g) + 8 V(g).
```

**Proof.** Summing three named positive two-generator charts counts every support-two triple once and every axial triple twice; exactly three positive axial endpoints exist when and only when `g` is square, all with BRC mass 1. This proves the first pair of formulas. Four independent signs lift every positive two-support triple into signed native points with unchanged factorial/multinomial path mass. Axial profiles have only two signed lifts rather than four, so the three axes yield an overcount of `6s(g)`. Every strictly positive three-support triple was entirely absent from the two-axis charts; it has exactly eight sign lifts, each with unchanged multinomial mass. Disjointness by support completes the proof for every `g>=1`, with no floating-point approximation or assumption of primitive diagonal segments.

The theorem preserves exact native Cell starting point, signed primitive axis identity and natural path-word multiplicity, versus positive chart and carrier incidence.

## Exact tested examples

| g | Fixed positive sector (R2,W2) | Distinct three-chart minzero (E,W) | Strict positive support-three (Q,V) | Full signed Z3 (S,B) |
|---:|---:|---:|---:|---:|
| 1 | (2,2) | (3,3) | (0,0) | (6,6) |
| 3 | (0,0) | (0,0) | (1,6) | (8,48) |
| 25 | (4,72) | (9,213) | (0,0) | (30,846) |
| 50 | (3,268) | (9,804) | (6,166320) | (84,1333776) |
| 65 | (4,678) | (12,2034) | (6,216216) | (96,1737864) |

In particular, `g=50` has **1,330,560** signed natural shortest-path words from genuinely three-support profiles alone. At `g=3`, the two-generator sector observer is empty although signed native has 8 endpoints and 48 natural shortest-path words. At `g=25` the three typed totals 72, 213, 846 are simultaneously valid for their different populations.

## Independent computation and scope

An independent integer enumerator `research_checks/X6_LEGACY_3SECTOR_SIGNED_SHELL_OVERLAP_UNIT66_20261116.py` enumerated all `[-22,22]^3` signed triples, all `[0,22]^3` positive/nonnegative triples and all `[0,22]^2` pairs, filtering `1<=g<=512`. For any such g every coordinate magnitude is bounded by `floor(sqrt(512))=22`; coverage is exhaustive on exactly this finite domain. Natural BRC weights computed with integer factorials. Four predicted endpoint/mass identities agreed with independently enumerated values for **all 512** shells, zero failures. Actual standard Python, `-O`, `-OO` executions exited 0 with identical stdout SHA256 `9b86adc643d9153d95e77005beda50a32039f1e033f3762acbd6e24a6a91c014`. Machine-readable witness: `research_checks/X6_LEGACY_3SECTOR_SIGNED_SHELL_OVERLAP_UNIT66_RESULTS_20261116.json`. Original R061/R062/R063 benchmark was **not** rerun.

LP015/LP017/LP018/LP019 disposition: `PRESERVE_OBSERVER_THREE_SECTOR_UNION / PRESERVE_PATH_BRC / RETYPE_NATIVE_SIGNED`. This derivation locates precise reviewed historical **antecedents**, rather than an alleged historical misuse. The exact alleged LP011 wrong native signed-axis argmax caller and LP019 positive N-BRC subtraction caller remain `UNRESOLVED_PROVENANCE`; Unit65's scoped review excluded R063 Stage3 PR #574 from the latter. Continue bounded downstream actual callers and independent Driver `REQUEST_REVISION`. No P000 modification, no old PR modified, no native mathematical acceptance claimed.
