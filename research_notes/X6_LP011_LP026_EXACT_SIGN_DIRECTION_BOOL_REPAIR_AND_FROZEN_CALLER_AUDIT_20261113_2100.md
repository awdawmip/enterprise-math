# X6 LP011/LP026 exact primitive direction repair and bounded frozen LP011/LP019 caller audit

Date: 2026-11-13 (21:00 Asia/Shanghai nominal research lane; actual source audit and commits during current turn).
Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`.
Research logical lane: `chatgpt-research-onhour-enterprise-math-20260923`; Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-bdd4acf9d96a8f1f0dfab4e9`, RUN `RUN-756de85b94c23b46b181f7b8`. The owner records are historical/current binding pointers, not standalone new authorization.
Frozen science pin: `59538f585d037d09ef687b28715c4bc1a3f9fe03` (P000 V5); historical comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Neither frozen science nor historical code changed.

## Genuine current execution-interface defect (LP011/LP026)
Original live `Spatial6.step(axis,direction)` in `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` (pre-fix blob `ac32f6d82a91db99297e587cf63b0df95cece514`, lines 46-50) and the current `Coord6.step` and `local_step` in `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py` (pre-fix blob `dd6dd7e74b83be09bb7545ee92357eda445c6ca3`, lines 88-95 and 140-148) accepted any direction comparing equal to +1 or -1. Python has `True == 1`, hence `True in (-1,1)`, so Boolean `True` crossed an input boundary declared to require an exact integer signed primitive direction.

Local exact-language witness checked both `True in (-1,1)` and `type(True) is not int`; the corrected predicate `type(direction) is int and direction in (-1,1)` rejects Boolean and integral-valued float impostors while retaining integers ±1. This is an argument-domain error, not an X6 theorem change. No other operation or sign count is redefined.

Three live source predicates were corrected with guarded GitHub blob-CAS and exact post-write readback:
- `x6_signed.py` commit `04de8c676c38e2242d4072a66efecdfd599f0c61`, new blob `0aab71a8d4f798cc07c53ca2e8f60b580ab0b87f`
- `x6_coordinate.py` commit `2e87546a2bdf7e51f0d9c2b911877bab07e3dba7`, new blob `34197857f513c1c46b11c3ca76492d8bbfd7b6a9`

Two **original project regression checkers**, not substitutes, were extended to reject `(True,False,0,2,-2)` at the relevant native and quotient directions:
- `check_x6_signed.py` commit `8b8ae20a1b28120acffa7efd9d16beb075ae7e06`, new blob `95b7693b645e32f6589ee768eab0ce3798ab7a79`
- `check_x6_coordinate.py` commit `3b47d947440208543c2df2f16dd5bf515ec76e4b`, new blob `8e7ff65c6ae54a97c3bfe781d7785d877ffb2b2f`

All four exact GitHub contents and blob IDs were read back successfully after publishing. **Validation scope: local isolated Python semantics witness PASS; full original project scripts are NOT YET EXECUTED on the modified dependency/source set.** Their execution and output remain an explicit scientific/engineering evidence debt, not a claimed regression pass.

## Bounded frozen-source historical caller trace

The immutable old repository tree was read at `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. This round inspected the complete content of the existing core `six_axis_foundation_v2_20260905` count-atlas, independent-reference, mutations, and vendor `atlas_brc.py`; six-axis V7/V16 signed/derived coordinate modules, admission/diagonal quotient scripts, and another 18 complete targeted historical `experiments/`, `scripts/`, and `tests/` files. The latter selected exact subset is:
`scripts/check_p000_first_shell_polyhedron_classification.py`,
`scripts/check_native_shell_grade_integer_allocation_foundation_audit.py`,
`scripts/check_p022_first_reentry_kernel_driver_audit.py`,
`scripts/check_p022_forced_midpoint_fallback_replay.py`,
`scripts/check_p022_franel_first_reentry_fixed_kernel_nonvanishing.py`,
`scripts/check_p022_observation_history_arithmetic_core.py`,
`scripts/check_free_research_agm_fcc_counter_visible_lift_no_go.py`,
`scripts/check_r043c4_native_interface_link_separator.py`,
`scripts/check_r043c5_global_pinch.py`,
`scripts/check_r043c6_rooted_successor.py`,
`tests/test_p006_signed.py`,
`tests/test_p022_geodesic_multiplicity.py`,
`tests/test_euler_native_bisector.py`,
`tests/test_euler_fcc_chirality.py`,
`tests/test_euler_fcc_chirality_connectivity.py`,
`tests/test_exact_arithmetic_brc_runtime.py`,
`experiments/brc_foundation_retrofit_check.py`,
`experiments/six_axis_foundation_v2_20260905/closure_addenda.py`.

The new 18-file subset had **zero relevant matches** under the explicit finite indicator search `dominant.axis|native.dominant|argmax|主导轴|正.*路径.*相消|signed.*cancel|cancel.*signed|signed.*brc|relative.*brc|native.*brc|pathsqrt|path.sqrt|can6|can3|rho\(|min.?zero|full.*signed.*path|BRC.*path` (case-insensitive). The core files were separately examined at function and operation level: `six_axis.py` defines chart-relative counts and full-depth reconstruction; `atlas_brc.py` counts positive BranchKey occurrence histograms and separately types frame/signed determinants; `x6_signed.py` and signed checker distinguish genuine signed native coordinates from positive min-zero BRC readout; `scripts/check_x6_foundation_admission.py` explicitly contrasts actual native signed reverse norm 1 with derived quotient section norm 5. Historical `brc_dominant_degeneracy_quotient_check.py` is a previously reviewed dominant-**weight** operator and is not double-counted.

This closes only these immutable filenames, semantics and exact search predicates; no original LP011 **native signed dominant-axis** mistaken argmax caller or LP019 **positive N-BRC signed cancellation** erroneous historical call site was established. The older 24 frozen definitions and seven old executable reviews remain previously completed cohorts; total 35 current-main consumer inspections remain the last previously reported cohort count (two original X6 checkers were touched here for a real repair, not mislabeled as fresh independent audit count). Historical culprit: `UNRESOLVED_PROVENANCE`. The 28 LP consumer/action dependency census and independent Driver `REQUEST_REVISION` are open.

## Immutable frontier and exact next action

Mother objective: identify and repair actual 28 LP current type/consumer errors, preserve frozen LP011/LP019 historical claims accurately, deliver a defensible residual caller inventory for independent Driver review.

New completed: three current signed-direction input guards corrected and four GitHub source/checker blobs read back; current exact 18-file frozen negative-search subset typed. Do not repeat old full G25 signed shell counts, PathSqrt 132-pair boundary, signed cover 516299 assertions, LP026 signed-BRC 59267 states, or the earlier full proof checks.

Current smallest unfinished evidence item: **execute the two modified original project checkers** against their exact current source imports, record actual stdout, exit status and verified source bytes; then evaluate real remaining LP011/LP019 historical caller links and LP28 downstream dependency names. Subsequent Native Source PROGRESS requires the current owner/CLAIM/RUN authorization; the separate original continuation read `onhour-20261113-2135-x6-current-continuation-v1` was QUEUED / WAIT_ORIGINAL at last observation; reconcile/read its original ID, no replay or new identity.

This author-side evidence is `SOURCE_PATCHED / FOCUSED_EXACT_PYTHON_SEMANTICS_PASS / ORIGINAL_REGRESSIONS_PENDING / UNREVIEWED / NOT_ADMITTED`.
