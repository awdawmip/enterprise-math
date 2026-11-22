# X6 Unit263 — Full local C12 return versus per-move C6 frame return

Date/observation: 2026-11-22 14:56 Asia/Hong_Kong. Parent: `PO-X6-UPPER-STRUCTURE-20260906`, Task `RS-X6-NATIVE-TIME-DYNAMICS`, publication `TP2-91D4A7C2F63805BE21A3`. Research-lane continuity reference: `chatgpt-research-onhour-enterprise-math-20260923`; prior source owner `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034` (historical provenance, NOT current execution authorization). Classification: **conditional mathematical result, exact local computation executed, UNREVIEWED / NOT_ADMITTED / NO_NATIVE_SOURCE_EXECUTION**.

## Frozen sources and specific open target

- Task science remains pinned to `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json` (ACTIVE_LOCKED V5, time orders changes and is not spatial).
- Original directed two-labeled-triad BRC 36-case input: `enterprise-math@f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json`.
- Prior Unit262 conditional coupling: `research_notes/X6_TIME_UNIT262_DECORATED_TRIAD_FRAME_C6_AND_GLOBAL_C12_CLOSURE_20261122_1400.md`, proof @ `a3618f61227b13618958067b3514092dcafc7c7b`.
- The earlier *distinct local transition* is `research_notes/X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md`, full ordered signed 960-frame carrier and SHELL/CLOSURE deterministic map (FREE research / NOT_FOUNDATION). This is used as a **declared possible event coupling**, not an admitted physical transition.
- Source-native intact signed triad movement `A:x0→x11`, displacement `(0,0,-1,0,0,0)` (P000 one-based `-E_3`), with three force-token identities, occupancy, environment and chronological observer, remains unexecuted.

## Exact competing event couplings

Let `F` denote an ordered signed triad frame, with distinct native-axis labels, independent signs, and `R_can` the corrected rotation:
`R_can((i0,i1,i2),(s0,s1,s2))=((i1,i2,i0),(-s0,-s1,-s2))`.
It has **exact order six** on all 960 frames.

Unit262 assumed H6: every full-triad move of label T performs `R_can` on that label's frame, and a separate global event register `g∈C12` advances at every event. Under H6 it correctly found minima `28/30/36` for spatial-only / frame-closed / frame+global-phase-closed returns.

The existing local Cell-fiber source supplies another deterministic map H12:
`F_loc(frame,SHELL)=(frame,CLOSURE)` and
`F_loc(frame,CLOSURE)=(R_can(frame),SHELL)`.
**For this unit only**, assume each whole-triad *movement event* applies `F_loc` once to that moving label; the other label's fiber stays fixed. This coupling is distinct from H6. After `n` own moves, the full ordered frame *and* local mode return precisely when `12 | n`. The global independent `g∈C12` still advances once per event. No assertion here identifies H12 with the real Source physical transition.

## Sharp new theorem and its difference from Unit262

For either original 28-event directed Port pair `(6,0)` or `(8,2)`, both labeled triads begin with arbitrary full ordered signed frames and local modes; preserve original signed outer winding `W_A=-12, W_B=+12`, directed Port and unoccupied-target guard. Under H12:
- spatial plus winding return has minimum **28** (original Unit245);
- spatial, winding plus return of **both full local 1920-state C12 fibers** has minimum **36**;
- adding return of global independent C12 event register also has minimum **36**.

Proof: `F_loc²(frame,m)=(R_can(frame),m)`; since `R_can` has exact order six on every full ordered signed frame, `F_loc` has exact order twelve on each of the 1920 states, yielding 160 length-12 cycles. Both labeled fibers return only if `12|n_A` and `12|n_B`. Thus `12|N=n_A+n_B`. The original spatial lower bound is `N≥28`, hence `N≥36`. Unit262 already constructed two valid 36-event originals with counts `(n_A,n_B)=(24,12)` and `(12,24)`, respectively. Replaying them under `F_loc` returns both fibers and, as `36≡0 mod12`, the global register. So **36 is attained**, not only bounded. This lower bound is for all paths in the declared coupled BRC model; the witnesses are original occupancy/signed-winding histories.

The 30-event H6 frame-closed paths have counts `(18,12)` and `(12,18)`. Under H12 the moving 18-event triad ends in its starting local mode but with frame `R_can^9=R_can^3`, i.e. all three signs reversed. Thus those paths are **not** full local-fiber returns. This identifies a concrete observer/type distinction, not a contradiction between the two correctly scoped conditional models.

| Directed Port | original 28 (nA,nB; local full return) | prefixed 30 (nA,nB; local full return) | prefixed 36 (nA,nB; local full return) |
|---|---|---|---|
| x6→P→x0 | (16,12; no) | (18,12; no) | (24,12; yes) |
| x8→P→x2 | (12,16; no) | (12,18; no) | (12,24; yes) |

## Independent exact finite check and original-event scope

A local Python exact implementation exercised all `960×2=1920` local fiber states, advancing each through 12 steps and checking that the **only first positive return is step 12**: `23,040` state-step assertions, zero failures. It separately replayed all six original Unit262 28/30/36 routes under both the original two-label BRC vacancy/winding constraints and the H12 fiber law, reproducing the displayed counts/returns. Machine-readable route results and reproducible script are saved in `research_checks/` under this unit. This is a complete test of the *finite proposed coupled graph*, not physical Source admission.

## Smallest discriminating native observation — unchanged original object

Before choosing the H6-derived 30-event return or H12-derived 36-event return for an actual benchmark, the existing authorized Source executor must first attempt the genuine intact-triad signed displacement `A:x0→x11`, `Δ=(0,0,-1,0,0,0)` (one-based `-E3`) and record whether the move is admitted with three actual force-token IDs, triadic closure, vacancy, environment response, precise event order and the **pre/post full ordered signed frame plus SHELL/CLOSURE if defined**.

If initial local mode is SHELL and both models are operationally defined, the **first admitted event** distinguishes their frame readouts: H6 predicts frame `R_can(frame_0)`, while H12 predicts unchanged frame and mode CLOSURE. If that first event is unavailable, collect an actually admitted two-step return at an allowable state, not a simulated substitute. For H12, two own events predict `R_can(frame_0)` and restored SHELL; for H6, two predict `R_can²(frame_0)`. If the actual Source exposes neither frame nor mode observer, the distinction is *not identifiable from that observation* and cannot be decided from terminal Cell/winding alone.

**Native benchmark remains unchanged:** original 28-event BRC task, independent real C24/C3 in-trace sensors at the original event locations, and separate original R063 object under #2416. A modified 36-event coupled witness cannot count as completing the original 28-event physical test.

## Control and continuation

Last verified Source owner read (2026-11-22 04:06:15 UTC) reported `NEEDS_DISPATCH`, unassigned and `execution_authorized=false`; later fresh Task read `onhour-20261122-1500-x6-task-current-read-v1` is pending as recorded in this cycle and must be consumed by original request ID, not resubmitted. The earlier historic CLAIM/RUN are not current authorization. Protected native semantic PROGRESS remains unpublished for Units233–263. Existing engineering support #2903 continues to own Source continuation/claim repair; no new scheduler/owner identity is created. Reuse Units245–262 unchanged, and require actual signed triad Source admission + independent sensor evidence before native completion.

**Status:** AUTHOR_PROVED (conditional H12); EXACT_FINITE_CHECK_EXECUTED; UNREVIEWED; NOT_ADMITTED; NO_NATIVE_PHYSICAL_MOVEMENT; NO_NATIVE_C24_C3_SENSOR.
