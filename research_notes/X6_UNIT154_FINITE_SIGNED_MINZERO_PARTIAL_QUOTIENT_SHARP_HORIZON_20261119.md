# X6 Unit154 — finite signed min-zero observer: sharp partial-operation horizon

Date: 2026-11-19. Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, mother `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Research lane `chatgpt-research-onhour-enterprise-math-20260923`. Source exposure: frozen historical `fd2bcff10ca6e147348b6c1236027fc0d2877df3`; unchanged signed X6 scientific baseline `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Author material: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. No historical module or R063 benchmark was executed in this unit.

## Exact question and actual historical interface

The frozen `src/enterprise_math/partial_operation_quotient.py` (blob `d1f86491ce07279c058a4c99f40cabb1f96da0de`) explicitly requires classwise agreement on *definedness* and target class (`partial_operation_descends`, lines 127–159), refines by named enabled/target behavior (`partial_family_refinement_step`, lines 175–196), and provides horizon signatures (`partial_family_horizon_partition`, lines 296–315). Its frozen direct test `tests/test_partial_operation_quotient.py` (blob `0a36a62a8676df260b6d1dec18923545603c4202`, lines 99–168) asserts that disabled actions cannot be replaced by identity. It imports the operation-word enumerator from `src/enterprise_math/operation_quotient.py` (blob `758a65de02a434446936cd7e37b2ae604eade863`). This actual historical test-to-implementation edge was not among Unit153's 15 inspected source files.

The research question is whether the signed three-axis **relative/min-zero observer** remains an operation-compatible quotient if a finite simulation window turns the otherwise total native signed steps into partial operations. This is an *explicitly truncated computational state space*, not a new P000 boundary or a full native-X6 claim.

## Exact theorem (all integer radii)

For integer `R >= 1`, let `S_R=[-R,R]^3∩Z³` be a selected signed three-axis slice (embedded as `(z_0,z_1,z_2,0,0,0)` when six-axis notation is required), `D=(1,1,1)`, and
`sigma(z)=z-min(z_0,z_1,z_2)D`.
Declare six *labeled partial operations* `T_{i,s}(z)=z+s e_i`, defined exactly when the target remains in `S_R` (`i=0,1,2`, `s=±1`). Observe `sigma` after every completely defined operation word; whether a word is defined is itself observable, as required by the frozen partial-operation contract.

Let `P_R(h)` be the partition of `S_R` by identical `(definedness, sigma(final state))` for **every** named word of length at most `h` (including the empty word). Then, for every integer `0<=h<=R`,

```text
#P_R(h) = (2R+1)^3 - [2(R-h)]^3.
```

At `h>=R` every class is a singleton. Thus the **exact worst-case minimal finite horizon** needed to reconstruct the full native signed state from the min-zero observation and legality-sensitive future words is `R`, not a constant independent of the truncation radius. The same proof with exponent `m` holds for an explicitly selected `m`-axis signed-coordinate cube and its diagonal quotient; the project-relevant executed case here is the three-axis slice, not a replacement of six-dimensional P000 space.

## Proof

1. `sigma(x)=sigma(y)` iff `y=x+kD` for some integer `k`. For any pair with different initial observer values, the empty word distinguishes them.
2. Put `r=R-h` and define the inner cube `I=[-r,r]^3`. Every operation word of length `<=h` stays inside `S_R` when begun at any `x∈I`. For `x,y∈I` with the same min-zero observation, the same word translates both by the same native displacement, so every resulting min-zero observation is still identical. Hence points in `I` are grouped exactly by their original diagonal-shift observer fiber.
3. Conversely take `x≠y` with `sigma(x)=sigma(y)`, say `x_i<y_i` for all three coordinates (the offset is a common nonzero integer). If at least one lies outside `I`, some coordinate (indeed the same coordinate index can be used) crosses a lower or upper boundary within `h` steps from one member before the other. Concretely if `x_i<-r`, the word `(-e_i)^{R+x_i+1}` is disabled from `x` but fully allowed from `y`, and has length `<=h`. Otherwise if `y_i>r`, the word `(+e_i)^{R-y_i+1}` is disabled from `y` but allowed from `x`, likewise of length `<=h`. If either of the pair lies outside the inner cube, one of these alternatives holds. Such pairs have distinct future signatures.
4. So every outer-cube point is a singleton, while inner-cube states are grouped by diagonal observer fibers. There are `(2r+1)^3-(2r)^3` such inner observer classes because min-zero representatives have nonnegative coordinates at most `2r` with at least one zero. Therefore
```text
#P_R(h) = ((2R+1)^3-(2r+1)^3)+((2r+1)^3-(2r)^3)
        = (2R+1)^3-(2(R-h))^3.
```
5. At `h=R`, the partition is discrete. For the lower bound, `x=(-1,-1,-1)`, `y=(0,0,0)` share the same observer and every word of length `<=R-1` is legal from both, with identical min-zero outputs; `(-e_0)^R` is illegal from `x` but legal from `y`. Hence `R` is sharp.

## Reproducible exact finite check

An independently written, standalone integer refinement checker (not the historical module) exhausts `R=1..5` and proves agreement with the stated closed form at **every horizon**. Class counts for successive horizons are:
- R1 (27 states): 19,27,27
- R2 (125 states): 61,117,125,125
- R3 (343 states): 127,279,335,343,343
- R4 (729 states): 217,513,665,721,729,729
- R5 (1331 states): 331,819,1115,1267,1323,1331,1331.

Python normal, `-O` and `-OO` all returned the exact same JSON bytes, SHA-256 `faa025fcff50e1d3461822a3009cd0de970fb49bcbbbf3d8ee3a7087666bd80d`. See `research_checks/X6_UNIT154_FINITE_MINZERO_PARTIAL_QUOTIENT_CHECK_20261119.py` and `research_checks/X6_UNIT154_FINITE_MINZERO_PARTIAL_QUOTIENT_RESULTS_20261119.json`. The finite checks corroborate a separately complete all-R proof; neither automatically supplies independent review.

## Typed 28-LP/R062 consequence and limits

On **unbounded** signed `Z³`, all labeled native translations are total and min-zero diagonal equivalence is preserved: fixed labels descend, consistent with Unit152's full-state lift. On the explicitly **truncated** signed cube, the same nominal steps become partial and their domain legality reveals the erased common depth. The historical `partial_operation_quotient.py` API correctly keeps the definedness bit; using the total-operation quotient interface or silently substituting “disabled = identity” would not preserve the finite run. If one needs an exact finite truncation of the native Cell simulation, the lossless chart `(sigma,h)` or the stage-R discrete quotient is sufficient. The finite truncation may be an implementation choice; it is not a postulated physical boundary nor evidence for a historical LP011/LP019 bad caller.

This creates one new precisely pinned, historically frozen P023 partial-operation *consumer* for the 28-LP crosswalk. It does **not** resolve the alleged LP011 spatial-argmax or LP019 positive-natural-BRC subtraction original caller; those remain `UNRESOLVED_PROVENANCE`. The original Unit50 fixed-sector R063 benchmark remains already author-executed; independent Driver review/any explicitly required corroboration is outstanding. Unit153 native Source published at `66101af89083af7d19e12a4ea1bf89b73cc6e6b7`; Units149–152 own author materials remain preserved with separate missing native associations after the original failed Unit149 rate-limit request.

Do not re-run completed mathematics, retry failed/unknown native writes, amend original frozen inputs, self-review, or change scheduler/notifications.
