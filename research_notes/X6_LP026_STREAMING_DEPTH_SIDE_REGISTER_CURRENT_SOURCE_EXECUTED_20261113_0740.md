# X6 LP026 — sharp streaming depth-side register, executed against corrected live Source

Date 2026-11-13. Mother task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Nonblind current TASK_RESEARCH author-side execution `EM-X6-FB6990`; **original Driver mathematical result remains Driver-owned and untouched**.

## Specific actual current-source consumer compatibility issue

Historical Driver-written source-import checker at `research_checks/X6_LP026_SHARP_STREAMING_DEPTH_SIDE_REGISTER_SOURCE_IMPORT_20261112_DRIVER.py` (Git blob `5f4c279813087e774e471bc9d96cb7b156a38630`) pins its coordinate and cover modules to historical blobs `ef66285d8ae81569cbbd3195b3e38daae37944ef` and `3f7d9e62a4dd66e7888a69ff87276b283c891aac`. After the native/relative depth typing repair those are **not the current modules**, so a direct present-main execution fails the source guard before the science.

Preserve the historical Driver file and its frozen exact-source meaning. A new separate Researcher current-source checker `research_checks/X6_LP026_SHARP_STREAMING_DEPTH_CURRENT_SOURCE_RECHECK_20261113_0730.py` changes only those two import SHA pins to the genuine current module blobs `dd6dd7e74b83be09bb7545ee92357eda445c6ca3` and `171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd`. Its signed BRC module stays pinned at `300a96e3dc24bf6fff73743037a0347a8bc83176`. The mathematical code, predicates, finite-horizon loops and imported-source calls are unchanged.

The **exact new checker bytes**, Git blob SHA-1 `d5fbfe60878106846e0e94f4e4a5f2aa2761a620`, were executed in Python 3.13.5 using locally materialized connector-read exact dependency blobs and produced process exit 0, PASS. GitHub new checker committed at `74a768e0fd15734a58f3f6301fe0a5c1db081955`, exact blob readback verified. This is not a rerun of the old frozen Driver-source pin on old dependencies.

## Complete stdout from this run

```text
PASS_X6_LP026_SHARP_STREAMING_DEPTH_SOURCE_IMPORT
source_git_blob_sha1_pins {'experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py': 'dd6dd7e74b83be09bb7545ee92357eda445c6ca3', 'experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py': '171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd', 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py': '300a96e3dc24bf6fff73743037a0347a8bc83176'}
moduli_1_to_6_horizons_0_to_6 42
actual_source_CoverState_step_checks 425376
actual_source_signed_BRC_comparisons 27690
cover_ball_fiber_groups_checked 82723
```

Local process wall time about 29.30 seconds, RSS 104,908 KiB (not an algorithm speed comparison).

## Exact limited evidence and scientific implication

For every cover modulus `m in {1,...,6}` and horizon `H in {0,...,6}`, the original checker constructs all signed native words through horizon, compares the exact encoded finite-depth cover-with-register word distributions to the original signed native distribution, checks real imported `CoverState.step` on **425,376** transitions, imported signed BRC on **27,690** length-appropriate cases, all 82,723 accumulated cover-ball fibre groups, and exact sharp register capacity `1+floor(H/(3m))`.

The observed sharp finite-horizon register result remains compatible with the updated native Cell/relative cover code for these 42 declared cases. The test preserves the distinction between original native `z in Z^6`, finite-m cover residue, auxiliary register state and signed path multiplicity; no collapse of full native identity is claimed for finite-m alone. The original Driver theorem and any wider proof retain their historical claim and admission scope.

## Continuation

- Already completed earlier this turn: original `check_x6_cover.py` 516,299 PASS; LP026 live native-cover/norm/BRC integration 59,267 cover states, 281,472 steps PASS, its stale source pins repaired.
- Next scientific front: remaining 28-LP actual current downstream dependency and exact historical LP011/LP019 wrong-call provenance; Driver `REQUEST_REVISION` re-evaluation remains. Do not rerun already completed regressions without an altered relevant premise.
- Native Researcher session `MCP-082892eb480e45dea6d4b9fcc0491034`, own CLAIM `MCP-9ce362c91287345702dd387d`, run `RUN-1e81bbcb1938961eb41db249` are continuing under separate native Source authorization; GitHub persistence and formal native checkpoint/Source PROGRESS are distinct.
