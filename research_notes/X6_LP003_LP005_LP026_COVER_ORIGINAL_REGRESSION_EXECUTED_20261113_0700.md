# X6 LP003/LP005/LP026 — original cover regression executed (2026-11-13)

- Parent task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`.
- Research identity: `EM-X6-FB6990`, session `MCP-082892eb480e45dea6d4b9fcc0491034`; scientific-author execution; NOT independent review, Result, or Foundation promotion.
- Evidence class: **ORIGINAL PROJECT CHECKER EXECUTED ON EXACT SOURCE BLOBS**. Repository `awdawmip/enterprise-math`, current main read at `b79bb035d97dfed8137f8dcd2ba581c070d90d28`. The four GitHub connector source bodies were materialized in the isolated Python runtime with the original relative import layout. Each local file was compared with the GitHub-supplied **Git blob SHA-1**, and all four matched exactly. No rewritten substitute algorithms were supplied.
- Runtime: Python 3.13.5, process exit code 0, approximate wall time 21.49 s; peak resident memory 96,016 KiB. This measures this execution environment, not an algorithm benchmark.

## Exact source integrity

| File (relative repository path) | Verified Git blob SHA-1 | Local SHA-256 |
|---|---|---|
| `experiments/x6_native_coordinate_completion_v7_20260905/check_x6_cover.py` | `65778c6ccb44eb9bb15c0123ac51423dd10c8686` | `1f899365ddec7a15e0da7817c699ea8b79550479fb26f30767950f25e25f555e` |
| `experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py` | `171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd` | `ece5961a7a3ef4596079a77b8f2cf409a2548fda02384372da3a1235243d7861` |
| `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py` | `dd6dd7e74b83be09bb7545ee92357eda445c6ca3` | `e00a139c3ab4343d529607d20b5d36d4ebd4867b97ed8d06e5a8e1f3e35d4c39` |
| `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` | `ac32f6d82a91db99297e587cf63b0df95cece514` | `e48b6f2133edc588fde98b1b0f02ce27fecda915b152b7901300898920d52b8e` |

## Exact invocation and complete stdout

Run from the preserved project-relative working directory:

```sh
python experiments/x6_native_coordinate_completion_v7_20260905/check_x6_cover.py
```

```text
PASS_X6_CELL_COVER_CLASSIFICATION_V13_V14
checks= 516299
tested_moduli=0..8
m=1=>quotient_cover_coordinate_complete_only; current_P000_signed_native_m=0
m>1=>cyclic_common_depth_fibre
m=0=>integer_common_depth_fibre; P000_native_signed_step_crossfile=PASS
native_m0_states= 15625 ; native_m0_steps= 187500
```

The checked assertion count is reproducible from the checker loops: 125000 triple-composition associativity cases; 400 coordinate/depth assertions; 58 diagonal-loop assertions (including first returns); 205 `m=1` quotient identity checks; 15625 native initial-state comparisons; 375000 actual `CoverState.step` versus `Spatial6.step` comparisons and native squared-norm comparisons; 4 rejection checks for finite-modulus native lifting; 2 explicit diagonal-collision assertions. Sum: **516299**.

**Mathematical interpretation.** For a signed displacement `z` with `h=min(z)`, let `r=z-h(1,...,1)`; `CoverState(Coord6(r), h, 0)` retains exactly `z` and its signed six-axis primitive transitions on the complete finite domain `[-2,2]^6` (15,625 states and 187,500 transitions). The same code's finite-modulus covers deliberately do not claim native Cell identity. The checker also tests the existing associative cover composition and diagonal returns for the listed finite moduli, not their untested universal generality.

## Frontier and attribution

- **VERIFIED_COMPLETE:** Previous outstanding original patched `check_x6_cover.py` project regression is now executed, source-integrity-verified and recorded. The earlier independent 390625-assertion reference certificate is additional evidence, not a substitute for this run.
- **DO NOT REPEAT:** `check_x6_coordinate.py` original 58989 checks already passed; LP028 60-chart N=2500 and LP019 FCC 48-vs-0 certificates; historical 72 and signed 30/846; LP026 V12 78125 checks. Do not use this test to claim closure of unrelated consumers.
- **STILL OPEN:** complete claim-level 28-LP downstream dependency ledger, exact historical wrong-caller attribution for LP011 native sign/tie and LP019 positive-count/signed-cancellation, and independent Driver `REQUEST_REVISION` re-evaluation. No assertion of universal correctness from finite regression.
- **NEXT EXACT ACTION:** resume current Research lane using original session/claim/run after fresh Source authorization, inspect actual remaining downstream call sites from the existing 820 heuristic candidates, and identify/reproduce any genuine native/observer mismatch; checkpoint this report with immutable GitHub source reference.
- **Source status:** GitHub-authored execution certificate; Source canonical PROGRESS and native checkpoint are separate write effects and require their own original request receipts. No Result/freeze/review claimed.
