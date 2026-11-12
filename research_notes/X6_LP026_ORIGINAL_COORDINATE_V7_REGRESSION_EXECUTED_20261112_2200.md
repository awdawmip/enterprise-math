# X6 LP026 — full original coordinate V7 regression: executed exact current-source imports

**Task:** RS-X6-LEGACY-PLANE-RECONCILIATION; **parent:** PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. **Researcher:** EM-X6-FB6990; Research lane `chatgpt-research-onhour-enterprise-math-20260923`. Status: AUTHOR_EXACT_SOURCE_IMPORT_CHECK_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Frozen scientific baseline: `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Historical comparison: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. This verification imports current GitHub-main source without replacing frozen mathematical inputs.

## Source authenticity

Each of the following four complete Python modules was read using the authorized GitHub connector. The independently reconstructed local file was checked using `git hash-object` and `sha256sum`; every local Git blob matched the connector's blob SHA-1.

| Path (under experiments/) | Git blob SHA-1 | Local SHA256 |
|---|---|---|
| `x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py` | `4d872015d37d540c4e3a9e8b14180c1796512941` | `c472b6e1e69f8709b0e99f97236b304a89615e16c1f884c2e5fe64faf00f5075` |
| `x6_native_coordinate_completion_v7_20260905/x6_coordinate.py` | `ef66285d8ae81569cbbd3195b3e38daae37944ef` | `35919288e190a8c722fb40f67b04c5bcff5a82e875487d96701f2fc13ff1121c` |
| `six_axis_foundation_v2_20260905/six_axis.py` | `2a16d04bd6c5e6d50e0fdd20e455f854b71bdcf4` | `c83023a164ca115a4ba4e6bf370fc4c58aa2d082af3733307a873a2be5ec7609` |
| `six_axis_foundation_v2_20260905/vendor/atlas_brc.py` | `881a34d1919da64a85e6e06902ec3f23654a147e` | `9facc6512d2803db92a048b687620f17f7feb24f1fa7558e16e686817f775950` |

## Original checker actually run (not an equivalent reimplementation)

From an isolated directory retaining the original source layout: `/usr/bin/time -f 'elapsed_sec=%e maxrss_kb=%M' python -B experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py`.

**Exit code: 0.** Exact stdout:

```text
PASS_X6_NATIVE_COORDINATE_COMPLETION_V7
checks= 50771
v2_raw_lifts_cross_checked=4096
native_three_axis_selections=20
hidden_kernel_per_slice=Z^3
chart_roundtrips= 80
axis_permutation_skeleton=S6 (720 elements)
fcc_preserving_subgroup=S4 (24 elements); slice types 4+4+12
derived_section_reverse_axis_norm_squared=5; native_signed_reverse_axis_norm_squared=1; local_projection_reverse_norm_squared=2
return_6=720; return_12=7484400
```

Actual stderr from `time`: `elapsed_sec=1.62 maxrss_kb=100124`. This runtime is a diagnostic, **not a native benchmark or speedup claim**. The 50,771 checks are assertions as counted by the original test, not 50,771 formally reviewed theorems. The actual test imports `x6_coordinate`, `six_axis` and unchanged vendor `atlas_brc` and exercises 4,096 lifts, 20 triple-axis projections, positive six-axis BRC recurrence, S6/S4 structure, and type-separated reversal.

## New evidence closure and downstream consequence

This run closes the previous specific `NOT_RUN_NO_CHECKOUT` obligation for the corrected **original** `check_x6_coordinate.py`: current unchanged modules import and pass together. For a native reverse step `(-1,0,0,0,0,0)`, native squared norm equals **1**. Its min-zero derived address `(0,1,1,1,1,1)` has derived quadratic readout **5**; observed local projection has **2**. The corrected current consumer separates these three types. Do **not** characterize a correct derived readout as a new wrong native consumer, or silently transfer derived BRC to signed P000 Cell paths.

This does NOT close entire 28-LP dependence/consumer coverage, independently review mathematics, admit a Result, change P000, or run any requested native benchmark.

**Durable frontier:** Reuse prior verified signed BRC/finite-cover proofs, LP026 observer/interval/norm-range certificates, LP028 N2500 all-pair certificates, signed-shell and 72/111 historical results, and first-pass 28-row crosswalk. Unfinished: exact original LP011 dominant-axis sign/tie/zero native caller, LP019 claimed positive-BRC cancellation native caller, remaining 28-LP consumer dependency closure and Driver REQUEST_REVISION. Next: source-pin exact historical callers (or document bounded absence), classify KEEP/RETYPE/PATCH_IF_MISUSED only upon actual consumer evidence, and run an original corrected consumer only if changed. Session is native own MCP-082892eb480e45dea6d4b9fcc0491034; claim/open must be established by original native receipts, not by this GitHub document or a maintenance lane identity.
