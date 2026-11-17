# X6 Unit95 — Exact opt-in integration of strict CoverState into a real LP026 signed-BRC consumer

**2026-11-17 · AUTHOR-SOURCE-EXECUTED / INTEGER-EXACT / UNREVIEWED / NOT_ADMITTED.** Mother goal `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`, task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Frozen scientific pins retained (P000 `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical source `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, signed BRC `300a96e3dc24bf6fff73743037a0347a8bc83176`).

## Exact source and observed divergence

The existing full LP026 source consumer `research_checks/X6_LP026_CURRENT_COVER_FAST_G_NATIVE_BRC_IMPORT_20261112_ONHOUR.py` is retained **unchanged**, Git blob `346be279c42a1a44a7ecfae01256cb92e3109f00`. Its pinned coordinate dependency is `dd6dd7e74b83be09bb7545ee92357eda445c6ca3`. Current main `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py` instead has Git blob `9738543aace13f8a72af577e9ad8964c5fd40de8`. Consequently, the historical script executed against *current* main fails its source pin preflight **before imports**. That is not an original frozen experimental failure and is not a reason to silently update the original script.

Unit94 provided an opt-in strict version of the previously frozen `CoverState`: `experiments/x6_native_coordinate_completion_v7_20260905/x6_cover_strict_v2.py`, Git blob `d38c2d0fa3fed306afeb387ce60f7f2d9bd52f68`. Its exact typed input guard rejects `direction=True`, while retaining all valid integer `+1/-1` native transitions. Frozen `x6_cover.py` remains blob `171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd`.

## Unit95 actually executed

A distinct, explicit opt-in consumer `research_checks/X6_UNIT95_STRICT_COVER_LP026_OPT_IN_IMPORT_20261117.py` was created and verified, Git blob `4104b0b011b4ea8d72db2eb12a23f946a6792bfe`, immutable commit `a473be615309aded72452fa7aab39ae7c10b84e9`. It preserves the prior consumer's exact LP026 mathematical checks but substitutes the precise current coordinate pin and `x6_cover_strict_v2.CoverState` import. Its 18 original Python `assert` sites were converted to always-on `require` checks so optimization (`-O/-OO`) does not silently skip scientific assertions. The separate test adds an actual Boolean rejection check. Signed native BRC source remains blob `300a96e3dc24bf6fff73743037a0347a8bc83176`; fast native norm recovery stays blob `496764aa8ebdb19bb03b7d40b82128a82be0ed84`.

**Actual local execution** reconstructed exact Git blob bytes for the four main modules and this new consumer, then ran CPython ordinary, `-O`, `-OO`. All three executions passed, produced byte-identical stdout (SHA256 `319ae30d1c60eb91c2258a42cc7caa86c9156ed254f6bb58cf72c24fc8a8952b`) and retained the following original consumer's outputs:

| Check / output | Exact count or witness |
|---|---:|
| Signed native BRC endpoint multiplicity, word lengths 0–6 | 10,364 |
| Cover-state projection checks, moduli 0–5 | 59,267 |
| Source-level signed step transition checks, lengths 0–5 | 281,472 |
| Fast native quadratic recovery observer checks | 59,267 |
| Ambiguous quadratic observer classes | 2,355 |
| Relative section norm differs from uniquely recovered native norm | 49,834 |
| Reverse single-axis section/native squared norms | 5 / 1 |
| Length-9 two lifts: same native norm 21, different BRC multiplicities | 10,080 / 7,560 |
| Boolean direction `True` at strict CoverState boundary | Rejected |

This validation is a real imported-module end-to-end LP026 scientific consumer for the **new opt-in pinned source set**. Neither the original historical consumer's successful execution under *its own original old pins*, nor a re-execution of full frozen R063/Helly native benchmark is claimed. Machine certificate: `research_checks/X6_UNIT95_STRICT_COVER_LP026_OPT_IN_RESULTS_20261117.json` (Git blob `9150fa03566a079e60d12816f2679fa9aa09c89b`).

## Exact mathematical/observer scope

The native population is all named length-`n` signed six-axis BRC paths with 12 primitive directions, counted by nonnegative integer multiplicity; the finite-depth cover observer is `(rho(z),min(z) mod m)`, with modulus zero retaining exact common depth. A cover class can carry multiple native signed endpoints or squared norms, and an observer's section norm is not a substitute for native squared norm. Fast recovery is checked against native endpoint enumeration, with ambiguity retained rather than arbitrarily selecting a lift.

The `True` input is a *source interface type defect*, not an observed error in the LP026 legal integer-sign consumer; all its passed source steps use named axes and integer `-1/+1`. This versioned integration gives an executable corrective implementation without disturbing the archived pin. It does not by itself resolve historical LP011 wrong argmax or LP019 alleged positive BRC signed cancellation `file:line` attribution, nor settle remaining 28-LP dependency closure.

## Durable identity and control continuation

The real Research-lane provenance is logical conversation `chatgpt-research-onhour-enterprise-math-20260923`, Researcher-ID `EM-X6-FB6990`, original SID `MCP-082892eb480e45dea6d4b9fcc0491034`, original CLAIM `MCP-579c8e23625448582b421831`, original RUN `RUN-fb25028676f9692ab1bacaee`, original Activity `RA-5E3FE1E761E4963EC461A892`. The prior native exact continuation request `onhour-20261117-1211-x6-own-exact-cont-r11` has SUCCEEDED/read-only with `execution_authorized=false`; this Unit made **no unauthorized CLAIM/open/Native PROGRESS** and did not use the control-maintenance lane or D25 identity.

Parent goal remains OPEN. Next independent scientific action: locate original precise LP011/LP019 historical source calls and complete the downstream 28-LP typed consumer graph, assessing native signed BRC, cover/section and PathSqrt as distinct interfaces. Unit94/95 versioned-source validation is completed; do not repeat it absent input changes. Source publication is author evidence, not independent Driver review or mathematical admission.
