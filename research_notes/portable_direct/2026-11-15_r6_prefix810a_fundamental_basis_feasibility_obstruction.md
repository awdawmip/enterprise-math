# PREFIX-810A — Fundamental-cycle Z-bases can fail as feasible bounded-fiber move sets

Date: 2026-11-15, Asia/Shanghai. Research6 independent BRC named-source supplementary result to PREFIX-810 and PREFIX-809; frozen scientific input f42f2906d77f24085c123f3ccfe9667d41caa96d unchanged. Historical Activity: RA-63E1066C3056A93898BE8E18 (EM-DIRECT-4660FF). No shared X6 CLAIM acquired.

## 1. Exact obstruction, even for a complete positive-capacity 2x3 support

Let G=K_{2,3}, with all six named source edges having capacity 1. Use row-major order (00,01,02,10,11,12), row demands (1,1), and column demands (0,1,1).

Exactly two feasible tables exist:

A=(0,0,1,0,1,0)
B=(0,1,0,0,0,1).

Both have the stipulated margins. Since column 0 has demand zero, its edges 00 and 10 are fixed at zero in every feasible state. The row-major greedy spanning forest of the complete support contains edges 00,01,02,10; the fundamental cycle vectors for chords 11 and 12 are

g1=(+1,-1,0,-1,+1,0)
g2=(+1,0,-1,-1,0,+1).

Each of +g1,-g1,+g2,-g2 necessarily changes one or both column-0 edges, so none is an admissible move from either A or B. Consequently, the graph of feasible tables using this **fixed fundamental-cycle basis** has two isolated vertices.

Nevertheless,

B-A=(0,+1,-1,0,-1,+1)=g2-g1.

This is a feasible single 4-cycle switch on columns 1 and 2. Thus the fundamental cycles span the **integer circulation module**, as PREFIX-810 proved, yet their individual unit moves are not a universal feasible-connectivity family at fixed capacities and margins. The counterexample is explicit and exhaustive, not a runtime/solver obstruction.

An adaptive choice of forest after excluding the two fixed zero edges does recover the 4-cycle in this particular example.

## 2. Stronger obstruction to the simple fixed-edge-removal repair

On 3x3 row-major edges (00,01,02,10,11,12,20,21,22), assign capacities

K=(0,1,1,1,1,1,1,1,1)

and margins R=(1,1,2), S=(1,1,2). The **complete** four-table fiber is:

A=(0,0,1,0,0,1,1,1,0)
B=(0,0,1,0,1,0,1,0,1)
C=(0,0,1,1,0,0,0,1,1)
D=(0,1,0,0,0,1,1,0,1).

All eight positive-capacity edges vary across these four tables. Therefore removing edges constant over the *entire fiber* removes only 00, whose original capacity was already zero.

Choose the resulting variable-graph row-major greedy spanning forest. Its three fundamental cycle moves are

g1=(0,1,-1,0,-1,1,0,0,0),
g2=(0,0,0,1,-1,0,-1,1,0),
g3=(0,1,-1,1,-1,0,-1,0,1).

From A, neither sign of any one g_i gives another of the four feasible tables. Hence this **face-adaptive greedy fundamental basis** still leaves A isolated.

For perspective, the eight-edge variable graph has exactly 36 spanning forests, of which 30 give connected move graphs on this four-table fiber and six do not. Forest selection, not merely deletion of globally fixed edges, affects bounded-fiber connectivity.

The claim proved here is that a particular fixed/adaptively selected fundamental Z-basis can fail. It is not a claim that every spanning-forest basis must fail for the witness, or that feasible cycle connectivity is impossible. PREFIX-809's full simple-cycle moves still connect the fiber.

## 3. Exact exhaustive regression

The accompanying program PREFIX810A_R6_BASIS_FEASIBILITY_CHECK.py imports the immutable PREFIX-810 cycle-basis/fiber enumerators, enumerates every full source table and margin fiber in the declared finite domains, constructs the chosen signed fundamental cycle basis on (a) every positive-capacity edge and (b) each actual fiber's varying-edge support, and runs exact finite graph reachability on ± unit basis moves. No approximate arithmetic or random sampling is involved.

| Family | Capacity patterns | Fibers | Complete source tables | Fibers with >=2 tables | Fixed-basis disconnected fibers | Face-adaptive basis disconnected fibers |
|---|---:|---:|---:|---:|---:|---:|
| 2x3, K in {0,1,2} | 729 | 39,366 | 46,656 | 5,776 | 640 | 0 |
| 3x3, K in {0,1} | 512 | 17,840 | 19,683 | 1,457 | 312 | 20 |
| **Total** | **1,241** | **57,206** | **66,339** | **7,233** | **952** | **20** |

All checks passed, including the two explicit witnesses and enumeration of the 36 spanning forests in the 3x3 witness (30 connected, six disconnected). Result file: PREFIX810A_R6_BASIS_FEASIBILITY_RESULTS.json. The counts concern the deterministic row-major greedy basis rule and the declared capacity domains, not the fraction of all possible bases in an unrestricted class.

## 4. Next unit and native-scope handling

A feasible *Markov move set* requires more than an integral kernel basis. The next discriminating problem is to find conditions on capacities/margins/support that guarantee a selected family of fundamental or chordless cycles is both sign-feasible and connected, using PREFIX-807/808 residual cuts to detect blocked moves without enumerating every table. Compare adaptive forest selection, all simple cycles, and bounded-fiber feasible-move caching as three distinct algorithms.

These are exact BRC auxiliary source-count results. P000 Heartbeat World native X6, signed Cell/Link/Port provenance, and separately typed time are unchanged; a full native dynamics correspondence needs its own admitted map and event permission.

Status: AUTHOR_PROVED / EXACT_EXHAUSTIVE_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
