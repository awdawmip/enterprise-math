# X6 Unit123 — R063 original residue: exact first failure of named-step N-BRC prediction

**Research date:** 2026-11-18. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`; author `EM-X6-FB6990`, original Research conversation `chatgpt-research-onhour-enterprise-math-20260923`. **Status:** AUTHOR-PROVED / EXACT FINITE PYTHON EXECUTED / UNREVIEWED / NOT_ADMITTED. No original C3/C4 benchmark executed in this unit.

## Exact original input and typed object

Historical immutable scientific source: `awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3:experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py`, Git blob `643b2bac659a445891dcb5588b647972977104e0`. Its `sector_ball` (source lines 77–82) enumerates `(a,b,0)` for `a,b>=0` and `a²+b²<=R²`; its `residue` (85–88) returns `(a mod m,b mod m)`, and `check_spatial` (101–132) tests this fixed-positive sector. The third coordinate is fixed **only in that chart**.

Keep the frozen P000 V5 signed `Z^6` native Cell directions at `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Embed the positive ordered pair `(a,b)` along two *explicitly named* native axes with chosen positive signs and a Cell anchor, so the native primitive `+e_2` below is an allowed operation in this particular chart, with the new point allowed outside the initial finite-radius input ball.

For an integer `m>=1` and any integer radius `R>=0`, define
```
P_R = {(a,b) in N_0² : a²+b² <= R²},
r_m(a,b) = (a mod m, b mod m),
G(a,b) = a²+b²,
L(a,b) = a+b,
B(a,b) = binom(a+b,a)  [nonnegative natural N-BRC shortest-word mass].
Q_m(a,b) = (r_m(a,b), G(a,b), L(a,b), B(a,b)).
U_2(a,b) = (a,b+1), a named primitive positive step.
```

## Sharp theorem: first operation-aware ambiguity is exactly R=m

For **every positive integer m**, `Q_m` determines `B(U_2(z))` for all `z in P_R` whenever `R<m`, but cannot determine it for all `z in P_m`:

```
R_first_failure_of_next_B_under_U2(m) = m.
```

The first ambiguity survives *even after giving the observer its current native squared norm, shortest signed primitive length and exact current N-BRC count*. Explicit witness:
```
x=(m,0), y=(0,m).
r_m(x)=r_m(y)=(0,0)
G(x)=G(y)=m²
L(x)=L(y)=m
B(x)=B(y)=1
B(U_2(x))=B(m,1)=m+1
B(U_2(y))=B(0,m+1)=1
G(U_2(x))=m²+1; G(U_2(y))=(m+1)².
```
The same discrepancy occurs for the other named positive step `U_1`, with the two B outcomes exchanged.

**Proof of minimality:** For `R<m`, each coordinate of a point of `P_R` lies in `[0,m-1]`, so `r_m` is injective and any desired native/chart function is determinable from it. At `R=m`, a pair of distinct points with equal residues must differ by at least `m` in one coordinate. The disk bound forces that coordinate to be either `0` or `m`, with the complementary coordinate zero at the `m` endpoint. Consequently the sole nontrivial residue fiber is exactly `{(0,0),(0,m),(m,0)}`. Their current B masses are all 1. The two axial nonzero points have identical `Q_m`, but the displayed operation gives different next N-BRC masses. This proves the lower bound and attaining witness for every `m>=1`. QED.

**Comparison with completed Unit116:** Unit116 established the *static* first loss of current natural BRC under `r_m` at `R=m+1`. Unit123 proves the *dynamic*, named-step N-BRC loss at `R=m`, even when `G,L,B` of the current point are supplied. One full radius separates these two precise failure boundaries.

## Executed exact evidence

The new independent Python source `research_checks/X6_UNIT123_R063_OPERATION_AWARE_RESIDUE_SHARP_THRESHOLD_20261118.py` uses the historical declared `sector_ball/residue` formulas unchanged in a self-contained script and checks each `m=1,...,100`. For each m it exhausts every point of `P_(m-1)` and `P_m`, proves the exact three-point first residue fiber in the finite enumeration, groups by the full `Q_m`, finds exactly the one two-axial ambiguous augmented fiber at `R=m`, and checks both named positive-step N-BRC outputs. The general proof above establishes all `m>=1`.

Actual CPython ordinary, `-O` and `-OO` executions each exited 0 and emitted byte-identical compact JSON, SHA256 `aa32b4b122d40c8dea4a74704b89d7a4520573f210324edbf902b883366324c9`. Across all 100 moduli the checks examined **262,595** below-threshold and **270,549** at-threshold chart points. The `m=20` witness has present B=1 versus 1 and next B=21 versus 1; `m=100` has next B=101 versus 1. The maximal tested absolute difference is 100 and multiplicative ratio 101.

Original-source Git blob `643b2bac...` remains unchanged; no six-blob R063 C3/C4 512/512 program was rerun. Original source module integration is not claimed by this independent Unit123 checker. The source is tied to precisely the original fixed-positive R063 reader and named native step under the typed embedding.

- Executed checker: `research_checks/X6_UNIT123_R063_OPERATION_AWARE_RESIDUE_SHARP_THRESHOLD_20261118.py`, Git blob `9baefcacd8d93ce3c39b0c4f07fa7bbde6761bfa`, source commit `1e2a9966bf3c9452165b99820b65ff25d24d379a`.
- Exact test certificate: `research_checks/X6_UNIT123_R063_OPERATION_AWARE_SHARP_THRESHOLD_RESULTS_20261118.json`, Git blob `691c419224190292b03ffbcd1b69174e266f809c`, source commit `9ec7974007d333d45bf14add54074f99c8c300d5`.

## Mother-task type correction and next precise obligation

**LP019/LP023/LP028:** A fixed-positive PathSqrt/R063 modulo endpoint reader can retain current BRC while losing the information needed for a future *named* native step. Any consumer that predicts signed or embedded primitive-step N-BRC must carry native axis/start/sign and enough raw endpoint state, or certify the specific transition is constant on each relevant residue fiber. Current audited typed adapters already retain native labels; Unit123 does not attribute an unobserved wrong current caller.

**Open parent deliverables:** finish the 28-LP actual current-consumer dependency map and historical exact offender provenance for LP011/LP019, with honest `UNRESOLVED_PROVENANCE` where no executable wrong caller was located; consume the independent Driver `REQUEST_REVISION`; seek independent authorized verification/admission for R063 original six-blob 512/512 author-side run in Issue #2416. Existing Unit118 native import integration is complete by Unit122 and is not repeated. Scientific frozen inputs and maintenance-lane identity remain unchanged.
