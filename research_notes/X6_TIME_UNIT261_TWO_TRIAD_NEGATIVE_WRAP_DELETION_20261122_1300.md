# X6 Unit261 — Exact two-triad survival under deletion of A's negative wrap edge

Date: 2026-11-22 13:00 Asia/Hong_Kong. Task `RS-X6-NATIVE-TIME-DYNAMICS`, publication `TP2-91D4A7C2F63805BE21A3`, parent `PO-X6-UPPER-STRUCTURE-20260906`. Research-lane author `EM-X6-FB6990`, original SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Status `AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_PHYSICAL_EXECUTION`.

## Exact input, population and question

Preserve P000's signed six-axis Cell torsor at `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json` and the original immutable Unit245 compact certificate `enterprise-math@f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json` (blob `113d2102fe393bfd6f77bf7cca093b4cecf6796f`). The conditional graph has twelve signed OUTER Cells x0,...,x11 plus center P, one fixed directed ingress xi→P and egress P→xj, with even i,j. The two distinct complete labeled triads A,B occupy separate Cells, start at (x0,x2), and must return there with signed ring windings (-12,+12). Each event moves exactly one whole label into an empty target; Port steps have zero winding.

Unit260 proves that deleting the A-labeled negative boundary event x0→x11 from **all precontexts** excludes every possible finite solution for the 21 Port pairs i≥j. For the complementary 15 pairs i<j, Unit260 constructed only a single-triad bypass. The present question is whether an **actual two-label occupancy-compatible ordered BRC path** survives, and its exact additional primitive event cost.

## Main theorem: full conditional two-triad dichotomy

Delete only the event `A:x0→x11` in every BRC precontext; retain all other original graph transitions, including B's transitions. For the original two-triad return and winding target:

* All 21 even directed Port pairs i≥j are **unreachable at any finite length**, by Unit260's exact winding identity applied to A.
* All 15 pairs i<j are **reachable with both labeled triads and the original empty-target occupancy guard**. Their restricted shortest costs, compared with the previously proven unrestricted Unit245 costs, are:

| Ingress→egress | Original min | With A edge deleted | Extra |
|---|---:|---:|---:|
| 0→2 | 38 | 38 | 0 |
| 0→4 | 36 | 36 | 0 |
| 0→6 | 38 | 38 | 0 |
| 0→8 | 38 | 38 | 0 |
| 0→10 | 46 | 52 | 6 |
| 2→4 | 46 | 46 | 0 |
| 2→6 | 38 | 44 | 6 |
| 2→8 | 38 | 44 | 6 |
| 2→10 | 36 | 38 | 2 |
| 4→6 | 48 | 54 | 6 |
| 4→8 | 38 | 52 | 14 |
| 4→10 | 32 | 44 | 12 |
| 6→8 | 44 | 62 | 18 |
| 6→10 | 34 | 52 | 18 |
| 8→10 | 40 | 68 | 28 |

Five of fifteen costs are unchanged; ten increase by 2–28 events. This completes Unit260's 21/15 orientation split **at the original two-triad BRC occupancy level**, rather than the earlier A-only graph level.

## Proof, exact boundedness and executable witness

For each i<j, run FIFO breadth-first search on the same labeled four-register state (posA,posB,wA,wB) as Unit245. Each transition is an original directed OUTER or selected-center primitive event, subject to unoccupied destination and the single deletion `actor=A, source=x0, target=x11`. Parent pointers retain an ordered witness, and shortest-state distance/multiplicity accounting counts distinct chronological event histories without erasing labels or order.

All fifteen original joint goals were reached at length at most **68**. The verifier uses an integer winding bound |wA|,|wB|≤80; any path of length less than 68 has |wA|,|wB|<68 and therefore is inside the explored graph. The FIFO first-arrival distances are therefore the true **unbounded-winding shortest lengths**, not merely bounded-search guesses. The 15 encoded ordered witnesses recheck original source Cell, target vacancy, directed Port, signed winding, label identity and final return, including no deleted A edge. Both a Node typed-array solver and an independent Python tuple-state FIFO solver reproduce all 15 distances and shortest-history counts.

The executed Node audit made **3,608 integer assertions**, reached **540,585 total per-case BFS state discoveries**, and examined **1,831,584 candidate edges** (counts include each case's own initial state). The independently run Python audit passed all 15 (distance, shortest-history count) comparisons. These totals describe this new restricted model and are not the native Source execution counts.

## Signed primitive axis mapping for the actual Source request

Unit245 embeds x0=(1,0,0,0,0,0) and x11=(1,0,-1,0,0,0). Their difference is (0,0,-1,0,0,0). Thus this event is **-e2 in Unit256's explicitly zero-based e0,e1,e2 slice notation**, equivalently **-E_3 under P000's one-based E_1,...,E_6 axis convention**. Carry both the numerical vector and indexing convention in any true native admission call to avoid addressing the wrong physical axis.

## Native meaning and next action

The theorem is for the fixed **conditional directed BRC Cell graph**. Real Source must still supply a signed intact-triad transfer satisfying triadic closure, three token identities, vacancy, environmental evolution and observer time ordering. A refusal restricted to one precontext is not the global deletion analyzed here; use Unit258's contextual guards. A physical context-independent refusal of the A-labeled vector (0,0,-1,0,0,0) would exclude all 21 i≥j Port pairs in this benchmark, while the 15 i<j have explicit BRC-level bypass witnesses with measurable extra operation costs, pending individual physical admission.

Control: the original request `onhour-20261122-1157-x6-current-task-owner-read-v1` is **SUCCEEDED / error=null**, as-of 2026-11-22 04:06:15 UTC. Its Source state reports `owner=taskbook/unassigned`, `dispatch_state=NEEDS_DISPATCH`, no current winning lease, `execution_authorized=false`. This read is not a CLAIM. Prior terminal Source failures remain terminal and protected semantic PROGRESS is not invented. Original research lane and maintenance lane remain separated.
