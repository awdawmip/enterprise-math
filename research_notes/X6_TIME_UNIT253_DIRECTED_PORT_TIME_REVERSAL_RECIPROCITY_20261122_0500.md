# X6 Native Time — Unit253: sharp directed-Port time-reversal reciprocity and operational chirality cost

Date: 2026-11-22 05:00 Asia/Hong_Kong. Task `RS-X6-NATIVE-TIME-DYNAMICS`, publication `TP2-91D4A7C2F63805BE21A3`, parent `PO-X6-UPPER-STRUCTURE-20260906`.
Scientific status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED / NO_PHYSICAL_NATIVE_EXECUTION**. Research lane: `chatgpt-research-onhour-enterprise-math-20260923`; historical legitimate author `EM-X6-FB6990` / SID `MCP-082892eb480e45dea6d4b9fcc0491034`. A past claim is not current execution authority.

## Immutable sources and declared graph
Frozen P000 `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. The established OUTER local C12 primitive Cell lift is the cycle `x_{2r}=P+a_r, x_{2r+1}=P+a_r+a_{r+1}`, with `(a_0,...,a_5)=(e1,e2,e3,-e1,-e2,-e3)`; signed original steps are exactly `x_k->x_{k±1}`. A center spoke is geometrically an ordinary signed one-axis edge only at the six even ring indices. Treat the passage of an intact force triad through this edge, and the empty-target serial occupancy guard, as the **conditional transition law already stated in Unit245**, not as Source-confirmed physical dynamics.

Consume without recomputing the original Unit245 certificate at `f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json`, Git blob `113d2102fe393bfd6f77bf7cca093b4cecf6796f`: 36 sharp FIFO-BFS minima for two labelled intact triads A,B starting and ending `(x0,x2)`, with exactly one directed center ingress `x_i->P` and one directed egress `P->x_j` and initial/terminal `L_A=-12, L_B=+12`. Each native event changes at most one integer signed OUTER winding counter by 1; spokes contribute 0.

## Theorem 253A — exact signed chronological reversal
For each ordered ingress/egress pair `(i,j)∈E×E, E={0,2,4,6,8,10}`, let `N_{-+}(i,j)` be the minimum number of permitted serial movements from the initial two-label state back to itself with `(L_A,L_B)=(-12,+12)`. Let `N_{+-}(i,j)` be the corresponding minimum with `(+12,-12)`, using the **same** initial Cell positions and the same directed Port pair. Then
```
                  N_{+-}(i,j) = N_{-+}(j,i)
```
with equality of exact integer minimum cost, not merely an inequality.

**Proof.** Take any legal path of length n for `(i,j)`. Reverse all chronological transitions, keeping labelled triads intact. Since all original C12 ring edges are bidirectional, each reversed ring step is a legal signed primitive with the opposite signed winding increment. A source/target occupancy exclusion remains legal under reverse traversal: its old source is vacated by that event, so the reversed target is vacant. Every original `x_i->P` becomes `P->x_i`; every `P->x_j` becomes `x_j->P`. Consequently the reversed path is legal precisely for the swapped pair `(j,i)`. Initial and final labelled positions coincide, and the counter vector negates. This is an involution on all finite admissible histories and preserves event count, individual triad labels and the **full reversed ordered BRC source/target ledger**. Apply it to each shortest path and reverse the inequality to obtain equality. It does not erase BRC history and does not identify time with an additional spatial axis.

This theorem is the graph-level **reversal-with-Port-swap** law. It does not assert a physically time-reversible world, or that reversing a Port without changing the Port permission is physically possible.

## Theorem 253B — complete sharp reversed-goal cost spectrum
Rows and columns are `i,j=0,2,4,6,8,10`. The exact transposed spectrum for the reverse winding target is

| ingress i / egress j | 0 | 2 | 4 | 6 | 8 | 10 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 30 | 38 | 32 | 28 | 30 | 36 |
| 2 | 38 | 30 | 36 | 30 | 28 | 32 |
| 4 | 36 | 46 | 32 | 40 | 34 | 32 |
| 6 | 38 | 38 | 48 | 36 | 44 | 38 |
| 8 | 38 | 38 | 38 | 44 | 36 | 48 |
| 10 | 46 | 36 | 32 | 34 | 40 | 32 |

For a **fixed directed Port pair**, define the operational chirality cost difference
`D(i,j)=N_{+-}(i,j)-N_{-+}(i,j)=N_{-+}(j,i)-N_{-+}(i,j)`.
Then `D(j,i)=-D(i,j)`; precisely 24 of the 36 ordered pairs have nonzero cost difference, 12 have zero difference, and `max|D|=10` events. The complete frequency spectrum is `D∈{-10,-8,-4,0,4,8,10}` with multiplicities `{4,4,4,12,4,4,4}`. Specifically the original 28-event minima at `(6,0)`, `(8,2)` for `(-12,+12)` require **38 events** for `(+12,-12)` while those two directed Ports remain unchanged. In the reversed target the global minimum 28 instead moves to `(0,6)`, `(2,8)`.

This finite asymmetry is exactly attributable to **fixed orientation-dependent resource permissions**, not a measured physical arrow of time. It is distinguishable by retaining the sign of the ordered event and each Port's direction; unsigned endpoint-only observers would collapse the relevant difference.

## Independent exact computation and complete lower-bound lease
A separate, actually executed pure-Python FIFO breadth-first search builds every one of the 36 **reverse target** state graphs independently of transposing the old result. Its state is `(cell_A,cell_B,L_A,L_B)`, with 13 Cells and `cell_A != cell_B`; transition alphabet includes the two signed ring neighbours of each Cell and only `x_i->P, P->x_j`, moving one labelled triad at a time. The generator forbids occupied targets. The target is exactly `(x0,x2,+12,-12)`.

The search limits `|L_A|,|L_B|≤48` and `depth≤48`. This is **complete for global minimum certification**: by reversing an existing original witness for the swapped Port, every instance has an admissible history of at most 48 events; no strictly shorter history can ever reach an absolute ring counter larger than 48 because a single event alters it by at most one. Thus no discarded state can conceal a better candidate. FIFO first-goal depth is the minimum.

Executed original Python checker: 36 independent search instances, **761,846 total state discoveries across these instances**, 36/36 matching exact transpose comparisons, zero mismatches. Inputs are the frozen C12 signed graph and the original immutable Unit245 cost matrix, not any physical sensor sample. The complete checker and JSON certificate are stored alongside this note.

## Source evidence still required
Source-qualified signed whole-triad Port permissions, transition/environment response, real ordered Cell/Port receipts, and an independent calibrated C24 precision observer remain unverified. The already designed Unit251–252 intermediate C24/C3 measurements on the original Unit245 traces remain a candidate native experiment and are not replaced by this reverse-cost theorem. The separate R063 six-file native benchmark remains the responsibility of `RS-X6-LEGACY-PLANE-RECONCILIATION`.

Next genuine discriminating experiment: if a real Source-authorized directed center Port pair is known, measure its existence/guard and validate the **asymmetric two-target cost/feasibility** on the same original signed Cell ledger. If the Source forbids any passage, record the actual rejecting guard. Preserve the original 36 certificate routes and C24 measurement plans. No live own CLAIM is established by this note; protected semantic PROGRESS, independent review and Result admission remain outstanding. Support issue #2903 covers the existing control failure, without duplicate claim/registration.
