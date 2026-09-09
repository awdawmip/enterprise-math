# Actual JT2 research assignment and scoped refusal

Driver: `EM-DVR-57CCCE`. Status: `ACTUAL_SELECTION_REFUSED; NO CLAIM OR ER`.

The same real researcher `EM-JT2-EF9380` and existing session `local:codex-agent:jt2-bounded-reference-review:20260909:EF9380` were observed RUNNING by the actual agent tool before this Driver posted Issue 240 ASSIGN `5603476128`. The researcher sent its own confirmation observed at `2026-09-09T14:24:12Z`. Its earlier inactive interval is not recorded as continuous liveness.

The actual assignment was created and last updated at `2026-09-09T14:24:07Z` by server actor `awdawmip / 30957095 / OWNER`. Its body SHA-256 is `b0a9195aa5513f75ccd7da2f246aeff14493f38260182a5ca045eb98347529a1`. It pins DA `DA-4EE3132EDE68C56B33EE`, AUTHORIZE `5602746982`, task `RS-EMW59A-JT2-QTF3-FIXED-POINT`, publication `TP2-C2C9DDEB2D65387D115E`, and only parent `EM-FREE-W59A-JT2-RAMANUJAN-LEGENDRE`.

## Actual canonical execution

The canonical CLI ran from clean, fully materialized main `d40aa672623d6fc82af4cbb60964e6a628267e62`, tree `232c88cee00c1d24d52af93de7c9e80e6b85e191`, using the unchanged generated request and 765 actual raw server comments. The raw export combines eight full pages (764 comments) with a complete two-comment incremental page since `2026-09-09T13:34:43Z`; entries are merged by actual server ID.

Started at `2026-09-09T14:26:51.731389+00:00`, it completed in `14.578` seconds with canonical CLI exit code `2`, `action=NO_DISPATCH`, `selection_status=BLOCKED`. Authority, exact publication/taskbook, parent, recipient and session bindings were validated. This is a real refusal, not a positive validation, CLAIM, execution authorization, Result or mathematical review.

The CLI reason says `assigned research target retains canonical state NEEDS_DISPATCH`. The precise source cause is `research_control_dispatch.py:548`: the accepted state is already `NEEDS_DISPATCH`, but the additional truthiness test on `state.get("hard_block")` rejects the existing mathematical target label `QTF3_FIXED_POINT_NORMALIZATION_SCALAR`.

At this same source revision, `tools/research_runtime_reducer.py:477-488` maps an unclaimed READY task to NEEDS_DISPATCH. A BLOCKED state with the complete four-field hard-block structure maps to BLOCKED. Its ordinary `select_state` accepts NEEDS_DISPATCH states. The new assigned route therefore adds a stricter interpretation of the retained mathematical label. This diagnosis does not itself authorize changing any code, task, proof, priority or claimant.

## Evidence and continuation

The exact server assignment readback, generated request and full execution receipt accompany this note. The gzip file contains the original uncompressed raw JSON bytes, with both hashes in the manifest. GitHub App metadata differs between single-comment and list endpoints; both raw responses were preserved, and all execution-relevant server fields were checked equal. App metadata was not treated as control authority.

Preserve the current ASSIGN and request. Repair the narrow control interpretation through the Owner's current control path, keep actual typed hard blocks and canonical non-dispatchable states closed, and run the same target against current canonical code and fresh server events. Do not edit the taskbook label, publish another ASSIGN merely to obtain a different outcome, fabricate a CLAIM, or present this failed run as positive. The six formal QTF3 outputs remain pending actual selection, prepare/CLAIM and runtime authorization. Already checked mathematical inputs remain unchanged.
