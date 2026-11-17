# X6 Unit94 — Source-exact strict signed direction successor and frozen-pin-safe integration

**2026-11-17. AUTHOR-SOURCE-EXECUTED / INTEGER-EXACT / UNREVIEWED / NOT_ADMITTED.**
Mother objective: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; Task `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`.
Frozen inputs retained: P000 `59538f585d037d09ef687b28715c4bc1a3f9fe03`, legacy corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, signed primitive BRC Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`.

## Implemented code

The original `experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py` remains **byte-for-byte unchanged**, Git blob `171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd`. The separate, explicitly opt-in source version `experiments/x6_native_coordinate_completion_v7_20260905/x6_cover_strict_v2.py` is Git blob `d38c2d0fa3fed306afeb387ce60f7f2d9bd52f68`, committed at `60159728c51356c87e98df3af6dca7408d874546`. It is an exact source copy of the original with a document-header source-version notice and one guard change in `CoverState.step`:

```python
if type(axis) is not int or axis not in AXES or type(direction) is not int or direction not in (-1,1):
    raise ValueError("invalid native axis step")
```

This is an implemented versioned successor, **not an in-place replacement of the frozen source**. Importers of `x6_cover` continue using their old class and semantics until explicitly migrated and re-pinned.

The test `research_checks/X6_UNIT94_STRICT_COVER_SUCCESSOR_NATIVE_SOURCE_CHECK_20261117.py` (Git blob `804774b0825afdb09fc995669b804418a6cfb121`) imports the untouched frozen module alongside the new source module. Both were executed against the actual complete `x6_coordinate.py` Source bytes, Git blob `9738543aace13f8a72af577e9ad8964c5fd40de8`. All three modules' local bytes were checked against the corresponding observed Git blob SHA-1 before comparison.

## Exact mathematical and operational boundary

For every exact integer `direction` in `(-1,+1)`, the old and new source step bodies are identical after their input guards; therefore **all** such steps preserve the same transition over any six-axis min-zero state and every integer cover modulus `m>=0`, including paths obtained by composition of valid steps. In particular:

`step_m(kappa_m(z),i,eps) = kappa_m(z+eps*e_i)` for all signed integral `z`, named axis `i`, and exact integer sign `eps`.

The frozen source accepts `direction=True` as `+1`, while the new source raises `ValueError`. The successor rejects Boolean, floating point and other non-exact integer sign inputs directly. The old source's `direction=1.0` happens to be rejected subsequently by `Coord6/canonical`, whereas the new guard rejects it at the operation boundary. This distinguishes an actual Boolean acceptance defect from merely changing the exception location for floats.

The independent source-level checker performed **43,740 actual comparison steps** across `{-1,0,1}^6` (729 states), cover moduli `0..4`, six axes and two exact integer directions. It also checked the full/native `m=0` signed lift, malformed direction inputs and five two-loop diagonal transitions. CPython normal/`-O`/`-OO` produced the same JSON bytes, SHA256 `a9ed4e4babe0f7044e6e2c744f9523f05cbfcb7a7335b9e9336c30265e1c5386`, no failures. Exact machine certificate: `research_checks/X6_UNIT94_STRICT_COVER_SUCCESSOR_RESULTS_20261117.json` at Git blob `387951a4af761c2495d22cedac03dc25dfd47b6b`.

This is original **source-code execution** for the two cover modules and the complete coordinate dependency within a partial local project tree. The entire original `check_x6_cover.py`, R063/Helly native benchmark and original LP026 full importer were **not executed**; they remain separate frozen evidence/validation requirements.

## Pin and current consumer boundary

The existing `research_checks/X6_LP026_CURRENT_COVER_FAST_G_NATIVE_BRC_IMPORT_20261112_ONHOUR.py` at Git blob `346be279c42a1a44a7ecfae01256cb92e3109f00` pins old `x6_cover.py=171baf1...` and `x6_coordinate.py=dd6dd7e74b83be09bb7545ee92357eda445c6ca3`. The latter differs from **current main** `x6_coordinate.py=9738543aace13f8a72af577e9ad8964c5fd40de8` by actual Git blob readback. Thus running that historical `PINS` gate directly against current `main` would fail **before import**; this is a static pin comparison, not a reported execution or a defect in that original frozen run.

An active downstream migration must explicitly choose and pin the intended coordinate/source commit, import `x6_cover_strict_v2.CoverState`, and run the original LP026 algorithm/consumer's full exact regression on a coherent dependency set. Do not silently edit the frozen `x6_cover.py`, overwrite an old pin or call the new version a successful native benchmark. The new source is ready for opt-in integration but no existing importer was migrated this unit.

## Parent continuation and source-identity boundary

Unit94 is an implemented, executable correction for a real current reusable input-type boundary; it does not establish a malformed LP026 caller or an earlier LP011/LP019 wrong historical caller. The original historical `file:line` attribution, remaining 28-LP consumer graph, independent Driver `REQUEST_REVISION` and original-run Native semantic PROGRESS remain open.

Original researcher provenance: logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, Researcher-ID `EM-X6-FB6990`, Activity `RA-5E3FE1E761E4963EC461A892`, historical CLAIM `MCP-579c8e23625448582b421831`, RUN `RUN-fb25028676f9692ab1bacaee`. Exact continuation original receipt `onhour-20261117-1211-x6-own-exact-cont-r11` was SUCCEEDED/read-only with `execution_authorized=false`; no claim, run or Native semantic write was made from an unrelated Sites or maintenance identity. New GitHub authorship records are not independent scientific review/admission.

Next scientific action: source-owner and downstream pin-aware LP026 opt-in integration test, or exact LP011/LP019 historical caller provenance if the canonical source owner retains the frozen importer; use the first genuinely executable current consumer route. Maintain original source pins and do not rerun completed full native benchmark.
