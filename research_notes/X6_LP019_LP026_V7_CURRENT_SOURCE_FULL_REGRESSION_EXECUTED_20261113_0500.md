# X6 LP019 / LP026 — patched V7 complete original regression, actual current-source execution

Date of execution: 2026-11-13, on-hour TASK_RESEARCH lane. Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication: `TP2-B4A441B23DA3159232C2`. Researcher: `EM-X6-FB6990`, session: `MCP-082892eb480e45dea6d4b9fcc0491034`; frozen science remains the task's P000 V5 / signed-X6 baseline at `59538f585d037d09ef687b28715c4bc1a3f9fe03`.

## Executed object and exact inputs

The previously repaired *original* checker `experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py` was **actually executed**, importing its original current-source `Coord6`, `six_axis`/vendor atlas and signed `signed_brc`. The files below were read via the authenticated GitHub connector from `awdawmip/enterprise-math` current `main`, written byte-for-byte into the same repository-relative local directory structure, and each local Git blob hash matched the connector-returned actual blob SHA-1:

| Exact original module path | Git blob SHA-1 | SHA-256 of executed local bytes |
|---|---|---|
| `experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py` | `88f102979cd27909960eced1de2c4c5a7b78709d` | `5ddade93f7e12b27eb57917049dee90aaa406839029b8d0f7d6670da249d2179` |
| `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py` | `dd6dd7e74b83be09bb7545ee92357eda445c6ca3` | `e00a139c3ab4343d529607d20b5d36d4ebd4867b97ed8d06e5a8e1f3e35d4c39` |
| `experiments/six_axis_foundation_v2_20260905/six_axis.py` | `2a16d04bd6c5e6d50e0fdd20e455f854b71bdcf4` | `c83023a164ca115a4ba4e6bf370fc4c58aa2d082af3733307a873a2be5ec7609` |
| `experiments/six_axis_foundation_v2_20260905/vendor/atlas_brc.py` | `881a34d1919da64a85e6e06902ec3f23654a147e` | `9facc6512d2803db92a048b687620f17f7feb24f1fa7558e16e686817f775950` |
| `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` | `300a96e3dc24bf6fff73743037a0347a8bc83176` | `6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4` |

Host: Python 3.13.5, POSIX isolated working directory `/mnt/data/em_runtime`, repository-relative imports. Command (working directory is the temporary source tree root):

```bash
python experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py
```

## Actual stdout and exact regression certificate

```text
PASS_X6_NATIVE_COORDINATE_COMPLETION_V7
checks= 58989
v2_raw_lifts_cross_checked=4096
native_three_axis_selections=20
hidden_kernel_per_slice=Z^3
chart_roundtrips= 80
axis_permutation_skeleton=S6 (720 elements)
fcc_preserving_subgroup=S4 (24 elements); slice types 4+4+12
derived_section_reverse_axis_norm_squared=5; native_signed_reverse_axis_norm_squared=1; local_projection_reverse_norm_squared=2
return_6=720; return_12=7484400
return_type=positive_min_zero_relative; signed_native_return_6=19920
```

Original stdout UTF-8 SHA-256: `67ba1446566130aee0d7ae0fe412cb631708ea0b49fb40616744acab4ce90553`; exit status: 0 (all assertions completed). `checks=58989` is the **script's own test-count readout**. The checker tests 4,096 raw lifts, explicit integer signed native depth reconstruction, native and relative norm distinctions, 20 three-axis slices, S6/S4 symmetries, actual old-V2 chart reconstruction, exact positive-branch BRC endpoint recurrence and signed BRC return comparisons. Counts from the old pre-patch 50,771-check run were previously completed and are distinct; this run uses the *patched* current modules.

Typed mathematical readout: the 720 six-positive words return only to min-zero `Coord6` quotient zero while reaching signed native displacement `D=(1,1,1,1,1,1)`, native squared norm 6; the signed six-axis length-six zero-return BRC is `19,920`. A unit negative signed step has native squared norm 1, while its min-zero `Coord6` section has squared norm 5. The explicit integer common-depth lift is exercised by the actual original V7 program.

## Task significance, remaining exact obligations, provenance

This resolves the previously recorded `NOT_RUN` deficit for the **modified original V7 checker** and closes the affected executable consumer acceptance check. It supplies an author-run source import/integer regression certificate, not an independently reviewed Result or repository-wide downstream call-site audit. The 28-LP crosswalk remains the parent task's dependency ledger. LP011 historical native argmax bad-caller attribution, LP019 historical signed-cancellation bad-caller attribution, other active downstream consumers and Driver `REQUEST_REVISION` remain open.

Do not repeat: the old original checker regression, this patched full V7 regression, prior LP019 FCC carrier-only return count 48, LP026 norm-range families, and LP028 signed-chart exact certificates.

Next smallest scientific action: read exact current callers that take `Coord6.norm_squared`, `positive_return_count`, min-zero `can3`, R061/R062 and PathSqrt outputs as native X6 quantities; for a demonstrated violation, preserve caller path/line/argument type, run the minimal signed-depth/provenance correction against the original modules, and update the 28-LP consumer ledger. Do not infer a bad historical caller from an ambiguous string match.

Evidence scope: `AUTHOR_EXECUTED_CURRENT_SOURCE_REGRESSION / EXACT_INTEGER_CHECK_PASS / UNREVIEWED / NOT_ADMITTED`. No P000, frozen theorem or scheduler state changed.
