# X6 Unit262 — Sharp decorated-return overhead for both 28-event directed-Port optima

Date: 2026-11-22 14:00 Asia/Hong_Kong. Task: `RS-X6-NATIVE-TIME-DYNAMICS` / publication `TP2-91D4A7C2F63805BE21A3` / mother objective `PO-X6-UPPER-STRUCTURE-20260906`. Original TASK_RESEARCH author `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_SOURCE_EXECUTION**.

## Input and type boundary

Freeze P000 `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; consume the original Unit245 immutable 36-case directed-center-Port certificate `enterprise-math@f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json` (blob SHA1 `113d2102fe393bfd6f77bf7cca093b4cecf6796f`), and Unit261's two-label occupancy model. Previously established signed ordered-frame formula comes from `research_notes/X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md`, where `R_can` cyclically permutes the three ordered axis labels and reverses all three signs; `R_can^3` is a sign reversal and `R_can^6=1`.

Consider **one explicitly declared decorated extension** of the existing conditional BRC model: each whole-triad event of label T updates that label's signed ordered internal frame by `R_can` and leaves the other triad's frame untouched. A separate global event-phase register `g in C12` advances by +1 for **every** event. Spatial Cells, signed ring winding, directed center Port, distinct label identities, whole-triad atomicity and empty-target occupancy remain exactly the frozen Unit245 conditions. Require both spatial returns and original winding target `W_A=-12, W_B=+12`. Optional stronger return predicates: each triad's full signed frame returns; additionally `g` returns. This is a declared test coupling, **not** a claim that Source has admitted those frame or clock updates.

## New sharp theorem

For each of the two original 28-event optimal Port configurations, `(i,j)=(6,0),(8,2)`, the three nested minimum lengths are exactly:

```text
spatial + winding return                         28
spatial + winding + both labeled C6 frame return 30
spatial + winding + both frames + global C12     36
```

Proof of lower bounds: the original Unit245 exhaustive BFS proves the spatial-winding optimum is 28. For any ordered signed frame with three distinct axis labels and nonzero signs, the action `R_can` has exact order 6: steps 1–2 change the ordered axes, step 3 reverses every sign, and step 6 is the first identity. A complete frame return therefore requires each label's count `n_A,n_B` divisible by 6, hence total `N=n_A+n_B` divisible by 6; the smallest such `N >=28` is 30. Return of the independent global C12 phase requires `N` divisible by 12; the smallest such `N>=28` is 36. These are true lower bounds in the explicitly declared decorated graph, not merely lower bounds for one chosen witness.

Proof of attainability: Unit245 supplies the two complete 28-event strings, encoded as one character per event (uppercase A/lowercase B; destination 0..11 or center 12). For `(6,0)`, the original sequence has `(n_A,n_B)=(16,12)`; prepend the legal 2-event A bounce `LA` (A:x0→x11→x0) once for length 30, four times for length 36. For `(8,2)`, the original sequence has `(12,16)`; prepend the legal 2-event B bounce `dc` (B:x2→x3→x2) once or four times. Both bounce targets are vacant initially. The complete resulting traces retain **all** original chronological event labels and exact six-axis signed primitive moves, directed center Port restriction, vacancy and `(-12,+12)` winding, while restoring the relevant internal frame and phase registers. Thus the lower bounds are attained.

| Directed center Port | Original 28 counts (A,B) | 30-event counts | 36-event counts |
|---|---|---|---|
| x6→P→x0 | (16,12) | (18,12) | (24,12) |
| x8→P→x2 | (12,16) | (12,18) | (12,24) |

Reproduction strings:

```text
(6,0) N=28: LKJIHGMALKJIHGMdefghijklabAc
(6,0) N=30: LALKJIHGMALKJIHGMdefghijklabAc
(6,0) N=36: LALALALALKJIHGMALKJIHGMdefghijklabAc
(8,2) N=28: LKJdefghimIHGFEDCBAcdefghimc
(8,2) N=30: dcLKJdefghimIHGFEDCBAcdefghimc
(8,2) N=36: dcdcdcdcLKJdefghimIHGFEDCBAcdefghimc
```

A V8 exact replay made **605 assertions, zero failures**: per-event signed native coordinate displacement has exactly one unit axis support; directed-Port/OUTER adjacency, label identity, vacancy, signed winding and final spatial positions are checked. It also performs the internal `R_can` updates, checks the individual frame returns and global C12 closure. The script and complete event certificate are saved beside this note.

## Experiment consequence and unresolved Source obligation

Under the stated model, the 28-event original witness is spatially closed but **not** fully internally closed. Merely demanding frame closure needs 30 events; demanding an additional globally returning C12 phase needs 36. These are different physical observables and therefore cannot be merged into a generic '28-event return' statement.

For prefixed-bounce traces, the original Unit251–252 measurement indices after events 3 and 7 move to events **5 and 9** at length 30, and to **11 and 15** at length 36. Equal C24/C3 numerical sensor values require a separately proved clock/frame-independent observation law; their values are not inferred merely from spatial return.

The exact next native Source experiment remains: test the intact triad's signed displacement `(0,0,-1,0,0,0) = -E_3` from x0 to x11 with actual three force-token identities, `TRIADIC_CLOSURE_E`, occupancy, environment update and chronological observer; then test whether an actual whole-triad move advances `R_can` and/or a global C12 phase. Without those Source admissions, the 28/30/36 statement is an exact **conditional** decorated BRC theorem, not execution of the original native benchmark or physical C24/C3 sensors. Existing R063 remains separate.

Control/source boundary: the last successful original Task read as of 2026-11-22 04:06:15 UTC had `owner=taskbook/unassigned`, `dispatch_state=NEEDS_DISPATCH`, `execution_authorized=false`. Previous Source continuation failures were terminal and are not reissued. Protected Native semantic PROGRESS remains pending genuine current ownership and write authorization; GitHub author science is not a CLAIM or project Result.
