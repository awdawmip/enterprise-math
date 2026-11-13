# X6 LP011/LP026: original S6-patched project regressions — exact byte-certified execution

Date: 2026-11-14. Mother Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`.
Scope: **original main-backed Python checkers and all their actual imports**, after the S6 Boolean-axis-index repair. Author-side evidence only: `EXECUTED_EXACT / SOURCE_HASH_VERIFIED / UNREVIEWED / NOT_ADMITTED`.
Research logical lane: `chatgpt-research-onhour-enterprise-math-20260923`; maintenance logical lane is separate. Prior Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. No current CLAIM or Native PROGRESS is asserted by this GitHub author-side evidence.

## Exact immutable scientific and current-source scope

Frozen P000 V5 input pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Neither was modified.
The following seven **current** GitHub main file bodies were fetched using the authorized GitHub connector, reconstructed in an isolated local directory at their original relative paths, and each independently checked with Git's `blob <decimal byte length>\\0<raw file bytes>` SHA-1 convention. The observed on-disk Git blob exactly matched the actual remote connector blob for **every** file:

| Original file (all under `experiments/`) | Git blob SHA-1 | SHA-256 of exact file bytes |
|---|---|---|
| `x6_signed_native_spatial_v16_20260905/check_x6_signed.py` | `83c5ed026c41360696019f2a1d92d3db41910295` | `258cdc9ec68eeca2c0ecfaeec3b10ad4af1bbe7019b4efd7edb2751fe1cbafcf` |
| `x6_signed_native_spatial_v16_20260905/x6_signed.py` | `405d9bc752bbf45582f2d0a6d9f91bff9cc5f89e` | `3ff8e757a2752267b450c587ccc978b3c531abc6ff33f4babf2b3c49ab9b8d56` |
| `x6_signed_native_spatial_v16_20260905/signed_brc.py` | `300a96e3dc24bf6fff73743037a0347a8bc83176` | `6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4` |
| `x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py` | `d562df4cedf3aa54fd3ca5db5ee0d17ff873a752` | `9ce8118883da86627472055460c7ed1081c9f9eb8fffc2bd04e6f71f164225e0` |
| `x6_native_coordinate_completion_v7_20260905/x6_coordinate.py` | `9738543aace13f8a72af577e9ad8964c5fd40de8` | `6387655807c8c537fa56a5d43fa91a66d20782ecc74d943cc241b78bb45e979b` |
| `six_axis_foundation_v2_20260905/six_axis.py` | `2a16d04bd6c5e6d50e0fdd20e455f854b71bdcf4` | `c83023a164ca115a4ba4e6bf370fc4c58aa2d082af3733307a873a2be5ec7609` |
| `six_axis_foundation_v2_20260905/vendor/atlas_brc.py` | `881a34d1919da64a85e6e06902ec3f23654a147e` | `9facc6512d2803db92a048b687620f17f7feb24f1fa7558e16e686817f775950` |

Execution interpreter: Python 3.13.5, GCC 14.2.0, default assertions enabled, standard library, `PYTHONDONTWRITEBYTECODE` / `-B` equivalent. No Source-server code execution; this is local exact-blob original-script execution.

## Original current checker 1: signed native X6

Command: `python -B experiments/x6_signed_native_spatial_v16_20260905/check_x6_signed.py`
Exit code: **0**; stderr: empty. stdout SHA-256: `a06827e782fe12e451b7b95f6cadc260f89558bd5dc6e080d61d474b381b7c39`.

```text
PASS_X6_SIGNED_NATIVE_SPATIAL_V16
checks= 56510
full_translation_group=Z^6
primitive_signed_neighbours=12
joint_positive_slice_kernel=Z*(1,1,1,1,1,1)
relative_observer=Z^6/Z*1
full_diagonal_norm_squared=6
length6_balanced_positive_paths_to_diagonal=720
full_positive_return_nontrivial=false
```

This is the **post-S6-patch** original checker: previous post-direction-patch 56,502 checks plus 8 original-checker invalid-permutation cases. Its tests retain signed primitive adjacency, all 720 native S6 permutations, chart lifts, diagonal quotient and positive N-BRC type separation.

## Original current checker 2: derived X6 coordinates

Command: `python -B experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py`
Exit code: **0**; stderr: empty. stdout SHA-256: `ff557d61e7e96f0d5598a947087d7db5e6bee87658efe3a3e2a2a3b46aa354ff`.

```text
PASS_X6_NATIVE_COORDINATE_COMPLETION_V7
checks= 59003
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

This is the **post-S6-patch** original checker: previous 58,999 checks plus 4 invalid-permutation checks. It executes the unchanged V2 atlas dependency (4,096 complete raw lifts), S6/S4 consumers, min-zero chart reconstruction, exact signed native lift and the original positive BRC dynamic endpoint recurrence.

**Combined exact original checks: 56,510 + 59,003 = 115,513, both exit 0, no stderr, no failed assertions.** This closes the narrowly stated `ORIGINAL_REGRESSIONS_PENDING` item attached to the 2026-11-13 23:00 S6 Boolean-permutation repair. It is not a native benchmark replacement, an admission of the entire X6 task, a new P000 theorem, or a claim that LP011/LP019 historical wrong callers have been found.

## Continuation checkpoint

Highest retained science (do not redo): previous full native-cover 516,299 original assertions; LP026 native BRC/cover 59,267 norm checks; G25 five-orbit 7,812 signed endpoint shell and 1,440 double relative-observer fibres; G3 20 first `(rho,BRC)` collision pairs; R063 fixed pair chart 132 globally singleton observer endpoints; and the original pre-S6 direction-patch 115,501 original assertions. This report adds only the **new current S6 regression 115,513**.

Current unfinished mother unit: exact old LP011 **native signed dominant-axis argmax** caller provenance, LP019 **positive N-BRC versus signed cancellation** wrong caller provenance, and genuine 28-LP downstream dependency closure for independent Driver `REQUEST_REVISION`. Do not infer these purported old errors from the corrected S6 input-domain bug. The 2026-11-13 original `onhour-20261113-2340-x6-exact-continuation-v1` returned `SUCCEEDED` but `execution_authorized=false`, requiring typed continuation with original owner and frontier. Source session recovery lists existing runs and uploader pointers; this read-only projection is not a winning CLAIM.

Next exact action: inspect remaining frozen executable/consumer provenance at the task's historical SHA and actual current import/call sites. Publish the above author-side certificate under current authorized Research lane only when a real CLAIM/open permits Native semantic PROGRESS. Preserve Researcher SID and all pending original request IDs without replay or identity substitution.

Author status: `EXACT_ORIGINAL_REGRESSIONS_PASS / GITHUB_AUTHOR_EVIDENCE / UNREVIEWED / NOT_ADMITTED / NATIVE_SEMANTIC_CHECKPOINT_PENDING_AUTHORITY`.
