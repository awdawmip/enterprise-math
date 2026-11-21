# X6 native time — Unit244: single bidirectional centre Port suffices, sharp six-position event-cost spectrum

Date: 2026-11-21 Asia/Hong_Kong. Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

Task RS-X6-NATIVE-TIME-DYNAMICS; publication TP2-91D4A7C2F63805BE21A3; parent PO-X6-UPPER-STRUCTURE-20260906; original on-hour Researcher EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034 (historical attribution, no current live CLAIM).

## Frozen X6 object and the exact question

Use the frozen awdawmip/enterprise-math science pin a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json, with full native six signed axes and a chosen relative three-axis slice. P is the existing chart-relative centre Cell. The twelve original OUTER Cells are

\[
x_{2r}=P+a_r,\quad x_{2r+1}=P+a_r+a_{r+1},\qquad
(a_0,\ldots,a_5)=(e_1,e_2,e_3,-e_1,-e_2,-e_3).
\]

Retain all 24 signed directed original OUTER ring edges. Choose **exactly one** centre spoke position p from {0,2,4,6,8,10} and enable only the two directed signed primitive edges x_p→P and P→x_p. All events move an intact labeled force triad atomically, serially, only from an occupied source to an unoccupied destination. All tokens, native Cell identities, Port signs and chronological BRC event order remain explicit. Actual physical Port permission is a **conditional assumption**, not established by P000.

Two triads start at A=x0, B=x2. They must return to these exact Cells and attain signed **original OUTER ring** increments L_A=-12, L_B=+12. Spoke edges contribute zero ring increment while remaining genuine primitive events. Let N(p) be the shortest admissible history.

## Unit244 theorem: exact shortest native event counts

| Only available bidirectional centre Port | N(p) | Ring primitive events | Signed centre primitives | BFS states discovered until first goal |
|---|---:|---:|---:|---:|
| x0↔P | 30 | 28 | 2 | 1541 |
| x2↔P | 30 | 28 | 2 | 1584 |
| x4↔P | 32 | 30 | 2 | 1681 |
| x6↔P | 36 | 34 | 2 | 2077 |
| x8↔P | 36 | 34 | 2 | 2122 |
| x10↔P | 32 | 30 | 2 | 1720 |

Thus a *single* bidirectional native centre-spoke Port is sufficient, conditionally, to permit two original frozen OUTER full loops of opposite sign under one-Cell exclusion. The event-time cost depends on the spoke's relative location. Unit243's all-spokes graph achieves 28; restricting the native Port interface incurs 2–8 extra genuine primitive events. This is an exact conditional resource/clock discrimination, not a substituted native benchmark.

### An explicit 30-event schedule for p=0

P denotes Cell 12. The exact source-adjacent BRC sequence is:

1. A: x0→x1.
2. B: x2→x3→x4→x5→x6→x7→x8→x9→x10→x11→x0 (ten consecutive +ring primitives).
3. B: x0→P (one signed centre primitive).
4. A: x1→x0→x11→x10→x9→x8→x7→x6→x5→x4→x3→x2→x1→x0→x11 (fourteen -ring primitives).
5. B: P→x0 (signed centre primitive), B: x0→x1, A: x11→x0, B: x1→x2.

The event counts are 1+10+1+14+1+3=30. A has fourteen negative and two positive ring moves, giving -12; B has twelve positive ring moves, giving +12; both return to initial signed six-axis Cell coordinates. Every destination is unoccupied at every step. For each of the other five spoke positions, a full exact labeled, signed-axis event ledger is in the machine certificate below.

## Exact finite proof of sharpness and correction of a tempting register bound

The full state is (Cell_A,Cell_B,L_A,L_B) with distinct occupied Cells and integer signed OUTER ring counters. Each enabled move changes one Cell and exactly one counter by 0 or ±1. Breadth-first search enumerates all serial interleavings from (0,2,0,0) to (0,2,-12,+12) separately for all six p, with the occupancy guard and exactly the source-defined 13 six-axis Cell coordinates. The registered search bounds the counters by |L_A|,|L_B|≤36. Since each proved shortest history has at most 36 primitive steps, a shorter history cannot visit a counter with magnitude above 36. Therefore the cut state set contains **all possible shorter witnesses** and cannot create a spurious shortest claim. FIFO BFS returns the exact minimum; independently implemented Python BFS agreed on all six counts.

A preliminary narrower cutoff |L|≤12 incorrectly gives 32 instead of 30 for p=0 and p=2 because some required intermediate histories retrace beyond endpoint winding magnitudes. The actual proof uses bound 36, tied to the length horizon. This is an explicit correction to the observer truncation, not a new physical axiom. All selected 13 Cell coordinates, signed primitive link displacement, serial exclusion, final integer ring winding and full BRC sequences are verified by the executable.

**Actual executed source, 0 assertion failures**: research_checks/X6_TIME_UNIT244_SINGLE_CENTER_PORTAL_EXACT_CHECK_20261121.js, commit 3f7a6f30e5bec68a1a6922efe97644defc330dd2, Git blob dd26afa386e0e1ce1a3589becdf1140416e6b0b5.

**Full exact certificate (six complete paths and BFS statistics)**: research_checks/X6_TIME_UNIT244_SINGLE_CENTER_PORTAL_EXACT_RESULTS_20261121.json, commit e6b82e7208228ab105ae956dd379ffb961af779d, Git blob ffef1c8ab0d89b15f92b39b3ac556573611116f7.

## Immediate native experiment and evidence boundary

Unit242's ring-only common-winding obstruction remains exact under its original graph. Unit243's 28-event all-spoke construction remains exact. This unit identifies a **weaker explicit Port availability test**: one of the six signed centre links must be available in both orientations for whole-triad movement, in addition to every original OUTER signed ring link and exact resource guard. The actual Source-admitted triadic Cell/Link/Port transition law, environmental response, and independent before/after C12/C24 precision-fibre readout are still missing. If the real Port law allows only one direction, test the corresponding directed graph rather than assume bidirectionality.

R063 six-file Native benchmark belongs to independent Task RS-X6-LEGACY-PLANE-RECONCILIATION. Units233–243 source artifacts and Activity244 have been consumed without recomputation. Native semantic PROGRESS Units233–244 requires an actual current winning own CLAIM; backend #2903 remains unverified for recovery. No Driver review or Result admission asserted.
