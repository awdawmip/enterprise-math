# LP019/LP026 — actual V7 executable consumer: explicit signed-native lift and return-type repair
Date: 2026-11-13 (Asia/Hong_Kong). Status: AUTHOR_PROVED / EXACT_INDEPENDENT_CHECK_EXECUTED / CURRENT_SOURCE_PATCHED / ORIGINAL_REGRESSION_NOT_RERUN / UNREVIEWED / NOT_ADMITTED.
Parent Task: RS-X6-LEGACY-PLANE-RECONCILIATION; publication TP2-B4A441B23DA3159232C2. Research lane: EM-X6-FB6990 / MCP-082892eb480e45dea6d4b9fcc0491034. Frozen P000 V5 scientific input remains pinned at 59538f585d037d09ef687b28715c4bc1a3f9fe03; pre-rebase comparison fd2bcff10ca6e147348b6c1236027fc0d2877df3.

## Actual still-live code consumer and defect
Current-main `experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py` (original current blob 4d872015d37d540c4e3a9e8b14180c1796512941) tested six positive steps on `Coord6` as a "loop", tested `positive_return_count(6)==720`, and printed unqualified `return_6=720`. The exact computation is valid only in the historical **derived min-zero quotient**; signed native `Z^6` moves by `D=(1,1,1,1,1,1)`, not by zero. The same source previously distinguished derived reverse-axis norm 5 from signed native norm 1, but did not preserve the depth witness through the executable `Coord6` interface. This is a located executable-label/consumer type leak rather than a newly attributed 2026-08 historical LP019 signed-cancellation bug.

## Precise mathematical result and typed API
For any `z in Z^6`, let `h=min_i z_i`, `r_i=z_i-h`. Then `min r=0`, `z=r+hD`, and conversely every min-zero nonnegative `r` and integer `h` give one exact signed native displacement. Therefore:
`G(z)=sum_i (r_i+h)^2 = Q(r)+2h*sum_i r_i+6h^2`.
This is an unconditional integer identity on the six signed axes. `Q(r)=sum r_i^2` without the explicit depth is a derived-section quadratic, not a depth-free native norm.

`Coord6.signed_native_lift(common_depth: int)` now reconstructs the exact six native integers and explicitly rejects a noninteger common depth. Existing derived `Coord6` and `brc_endpoint_multiplicity` remain unchanged mathematically. Their docstrings now state their observation type. For `r=0`, depths `h=0` and `h=1` yield distinct native endpoints `0` and `D` with native squared norms `0` and `6`, while `Coord6` and its positive relative return merge them.

For six positive labeled axis steps, exactly 6!=720 orderings terminate at native `D`; none terminate at native zero. Separately the current signed twelve-direction BRC kernel has `N_6(0)=19920`; this prior Source-verified count is reused, not presented as new discovery.

## Actual current-main edits with immutable readback
1. `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py`: original blob ef66285d8ae81569cbbd3195b3e38daae37944ef; CAS commit a8675ff8a9e38534a633f123dc2642a9fc94a8ce; new blob dd6dd7e74b83be09bb7545ee92357eda445c6ca3. Implemented explicit `signed_native_lift`, corrected derived `norm_squared`, positive-BRC endpoint and return docstrings.
2. `experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py`: original blob 4d872015d37d540c4e3a9e8b14180c1796512941; CAS commit c39545e96e2831b11d9a01aa46e0211ff1c6a047; new blob 88f102979cd27909960eced1de2c4c5a7b78709d. Added explicit native lift and squared norm assertions over the 4096 raw nonnegative lifts, native -axis restoration for six axes, actual six-positive-step diagonal displacement check, and signed `endpoint_multiplicity(6,0)=19920` vs derived positive `positive_return_count(6)=720`. Preserved the historical output string for compatibility, added an explicit return-type output.
Both exact files were fetched from their resulting immutable commits and byte-compared against the written text.

## Executed evidence and boundaries
Independently executed exact Python integer enumeration of all 5^6=15625 signed displacements `z in [-2,2]^6`, each with two assertions on `can6(z)`, `h=min(z)`, reconstructed `z` and native norm. **31,250 assertions PASS**. The six-positive-path endpoint/relative-return witness was also asserted. The elementary identity above supplies the full unbounded proof; the finite test checks the independent implementation.

The patched original `check_x6_coordinate.py` full import/regression **was not executed on this host** (the current source tree is only accessible through the GitHub connector here). Its added assertions are durable code requiring the normal executable checkout test. Do not replace that test with the independent 31,250 checks; do not repeat the previous unchanged 50,771-check certificate as if it covered this newly modified checker.

## Source/ownership and next executable obligations
Original `onhour-20261113-0329-own-x6-v9v11v13v14-progress-publish` finished SUCCEEDED with canonical Source publication at commit 0bf475cea9a43dc90c6b11d5aacc7f2dca7c36bd. Current Research lane's `onhour-20261113-0355-own-x6-run-resume` returned SUCCEEDED with RUN-1e81bbcb1938961eb41db249 generation 3 revision 3, same winning CLAIM MCP-9ce362c91287345702dd387d. New `onhour-20261113-0355-own-x6-continuation` requires original-receipt reconciliation until terminal.

Next: run the now-patched *original* complete `check_x6_coordinate.py` with its actual `six_axis`, vendor `atlas_brc` and `signed_brc` dependencies; check stdout against newly typed expectations. Then trace additional current consumers importing `positive_return_count` or `Coord6.norm_squared` and amend the 28-LP ledger only on actual call-site evidence. The purported historical native LP011 argmax and LP019 positive/sign-cancellation wrong-call sources remain UNRESOLVED_PROVENANCE. Research Activity #2187 historical readback compatibility and independent Driver REQUEST_REVISION remain open. Native formal checkpoint must carry the full current verified frontier and exact request status; GitHub files alone do not claim Source admission.
