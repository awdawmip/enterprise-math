# X6 LP011/LP026: original modified checker execution certificate

Date: 2026-11-13 (Research on-hour lane). Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`. Publication: `TP2-B4A441B23DA3159232C2`.
Logical lane: `chatgpt-research-onhour-enterprise-math-20260923` (not the maintenance lane). Historical registered Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`; own previous CLAIM `MCP-bdd4acf9d96a8f1f0dfab4e9`, RUN `RUN-756de85b94c23b46b181f7b8`. These are provenance; a new Source write requires current authority.

## Exact source environment and provenance

Both **original modified project checkers** were executed unchanged, each against its complete original project Python imports (not substitutes). Source files were loaded via the authorized GitHub connector, placed into an isolated local directory preserving the repository-relative paths, and verified against Git's `blob <length>\\0<bytes>` SHA-1 object identity by `git hash-object`. The exact Git blobs matched the current GitHub main tree. Python interpreter: **Python 3.13.5**, GCC 14.2.0, standard library, ordinary assertions enabled. No network access or code execution occurred in the Source backend.

| Repo-relative file | Verified blob SHA-1 | SHA-256 |
|---|---|---|
| `experiments/x6_signed_native_spatial_v16_20260905/check_x6_signed.py` | `95b7693b645e32f6589ee768eab0ce3798ab7a79` | `4c41fb2b38db8281271c04dda941551407e07471bac0de7055aef270ca8d8031` |
| `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` | `0aab71a8d4f798cc07c53ca2e8f60b580ab0b87f` | `31509d902abaae19f5256817292d5fd1a3ff184105da6b5ba345138ab98b8237` |
| `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` | `300a96e3dc24bf6fff73743037a0347a8bc83176` | `6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4` |
| `experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py` | `8e7ff65c6ae54a97c3bfe781d7785d877ffb2b2f` | `925b9a5b5a1fc308099eaac0af2332da70fbabb8c45dd1b708771d180fe900dc` |
| `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py` | `34197857f513c1c46b11c3ca76492d8bbfd7b6a9` | `23cb0de87128448a1d74f7b569ea4b4fbbcdd223b77e6273e8409075dabc7934` |
| `experiments/six_axis_foundation_v2_20260905/six_axis.py` | `2a16d04bd6c5e6d50e0fdd20e455f854b71bdcf4` | `c83023a164ca115a4ba4e6bf370fc4c58aa2d082af3733307a873a2be5ec7609` |
| `experiments/six_axis_foundation_v2_20260905/vendor/atlas_brc.py` | `881a34d1919da64a85e6e06902ec3f23654a147e` | `9facc6512d2803db92a048b687620f17f7feb24f1fa7558e16e686817f775950` |

Commands: `PYTHONDONTWRITEBYTECODE=1 python experiments/x6_signed_native_spatial_v16_20260905/check_x6_signed.py` and `PYTHONDONTWRITEBYTECODE=1 python experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py`.
Both completed with exit code 0 and no stderr. Exact stdout follows.

### Original signed X6 native regression
```text
PASS_X6_SIGNED_NATIVE_SPATIAL_V16
checks= 56502
full_translation_group=Z^6
primitive_signed_neighbours=12
joint_positive_slice_kernel=Z*(1,1,1,1,1,1)
relative_observer=Z^6/Z*1
full_diagonal_norm_squared=6
length6_balanced_positive_paths_to_diagonal=720
full_positive_return_nontrivial=false
```
stdout SHA-256: `6136224518fb12e60437d1fb99f47e872795e4fe7007ecc34efe60ba0cc7fa71`.

### Original derived coordinate regression
```text
PASS_X6_NATIVE_COORDINATE_COMPLETION_V7
checks= 58999
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
stdout SHA-256: `f08a2b9a032c183ac27cc12eef44475af6245d32442ba5a491af5a9d40b37476`.

## Exact conclusion and bounds

The original repaired native checker covers **56,502 checks**; the original derived checker covers **58,999 checks**, including five and ten new invalid-direction test cases, respectively. The pre-modification derived count 58,989 is now 58,999. Both execute the same source and checker bytes as the live repository at the time of verification. Thus the previously explicit `ORIGINAL_REGRESSIONS_PENDING` debt for the 2026-11-13 boolean-direction patch is closed **for these two original scripts and dependency graph**. The result is an original Python regression execution certificate, not a formal theorem or independent Driver admission.

The frozen scientific P000 V5 pin is `59538f585d037d09ef687b28715c4bc1a3f9fe03`. No changes to that pin, the old historical pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, nor to the native benchmark conditions occurred.

## Precise continuation

Mother target remains the 28 LP current-consumer closure and frozen historical wrong-caller provenance of LP011 (native signed dominant axis) and LP019 (positive N-BRC versus signed cancellation), followed by an independent Driver `REQUEST_REVISION` verdict. The prior `G=25` shell/observer results and old cover 516299-assertion test are completed and must not be repeated.

The Source `onhour-20261113-2135-x6-current-continuation-v1` is SUCCEEDED; fresh `onhour-20261113-2203-own-x6-continuation-v1` and task read revalidated an as-of Source event collection. Their projections **do not grant execution authority**. Preserve historical SID/CLAIM/RUN and original request IDs; perform new Source native PROGRESS only following fresh winning claim/run authorization, and no reviewer identity borrowing.

Author-side status: `ORIGINAL_MODIFIED_REGRESSIONS_PASS / SOURCE_HASH_VERIFIED / UNREVIEWED / NOT_ADMITTED`.
