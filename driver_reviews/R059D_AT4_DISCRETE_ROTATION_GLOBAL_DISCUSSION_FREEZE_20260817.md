# R059D AT4 — Discrete Rotation Global Discussion Freeze

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-17`
Status: `ACTIVE_FOUNDATION_SNAPSHOT / NO_TASK_EXECUTION_UNTIL_EXPLICIT_RESUME`

This document freezes the latest discussion before any further research task is executed. It is a foundation/control-plane snapshot, not a research taskbook.

## 1. Discrete ontology

Enterprise geometry is a discrete system. A rotating fixed-vector-length segment must occupy exactly one native cell at each discrete trajectory step.

Freeze:

`ROTATING_SEGMENT_NATIVE_STATE = ONE_NATIVE_CELL_PER_STEP`.

An algebraic shell point or exact edge crossing is not a native rotating state. It is a certificate that a transition boundary has been reached.

Freeze:

`ALGEBRAIC_CROSSING = TRANSITION_CERTIFICATE_NOT_NATIVE_STATE`.

The set of cells incident to a crossed edge is an admissibility/support set, not a simultaneous native state.

Freeze:

`INCIDENT_CELL_SET = ADMISSIBILITY_SUPPORT_NOT_SIMULTANEOUS_STATE`.

## 2. State versus support versus trajectory

Three objects must never be conflated:

1. instantaneous state: one cell `C_k`;
2. one oriented trajectory: `C_0 -> C_1 -> ...`;
3. support union: the set of all cells visited by one trajectory or by all legitimate trajectories.

Freeze:

`INSTANTANEOUS_STATE != TRAJECTORY_SUPPORT_UNION`.

`PERIMETER_SUPPORT_UNION != SIMULTANEOUS_CELL_STATE`.

If more than one transition is equally legitimate, preserve all resulting trajectories, but every trajectory remains cell-single-valued.

Freeze:

`ALL_LEGITIMATE_PATHS_RETAINED = BRANCHING_OF_SINGLE_CELL_TRAJECTORIES`.

`ALL_LEGITIMATE_PATHS_RETAINED != MULTI_CELL_INSTANTANEOUS_STATE`.

## 3. Correct algebraic-collapse question

The previous comparison of PRE/DOWN versus POST/UP at edge endpoints was typed at the wrong level.

For an oriented shell crossing a shared edge between two cells, define:

- `CELL_PRE`: cell occupied immediately before crossing;
- `CELL_POST`: cell entered immediately after crossing.

The native collapse question is cell-level:

`CELL_PRE vs CELL_POST vs a stronger oriented-cell transition law`.

Do not substitute the two vertices of the crossed edge for the two cells.

Freeze:

`ENDPOINT_PRE_POST = DIAGNOSTIC_ONLY`.

`NATIVE_COLLAPSE_DIRECTION_IS_CELL_LEVEL`.

## 4. Orientation is part of the state

A rotation state must carry enough orientation/sweep information to distinguish the two traversals.

Minimum current candidate:

`S=(rho,C,epsilon)`

where `rho` is fixed vector radius, `C` is the unique current cell, and `epsilon` is orientation.

If incoming edge, previous cell, or another finite-memory datum is required at vertex events, extend the state minimally and prove necessity.

For any deterministic regime, reversal must satisfy:

`T_(-epsilon)=T_epsilon^{-1}`.

## 5. Algebraic vector foundation retained

Within one valid Enterprise algebraic chamber:

`||V||_E = sqrt(v_1^2+v_2^2+v_3^2)`

and in a two-active-component sector:

`q=x^2+y^2`.

Current coordinate arithmetic is chamber-local. Cross-chamber geometry requires explicit recharting and gluing.

Vector-algebra zero components are not native coordinate zero.

Radius remains resultant vector norm, not primitive jump count.

Reverse shortest paths remain realization fibers after cell selection, not radius/collapse generators.

## 6. What survives from AT4-S1

The exact q-range calculation for the cell `D(1,1)` survives:

`q(D(1,1))=[9/2,8]`.

Therefore:

`4 < q(D(1,1)) < 9`.

No exact integer-radius algebraic arc at radii 1, 2, or 3 intersects `D(1,1)`, while the radius-3 algebraic disk fully contains it.

Freeze:

`D(1,1)_IS_A_ROBUST_HIDDEN_WITNESS_BY_R3 = true`.

This witness is independent of whether a crossing chooses CELL_PRE or CELL_POST, because the exact arcs themselves do not enter the cell.

## 7. What is reopened

The previous proof that radius 3 is the *first* hidden radius used historical perimeter trace defined by retaining all incident cells of exact crossings. That support can strictly exceed a true single-cell trajectory trace.

Therefore the minimality claim is reopened.

Freeze:

`FIRST_SECTOR_HIDDEN_RADIUS <= 3`.

`FIRST_SECTOR_HIDDEN_RADIUS_EQUALS_3 = OPEN`.

Radii 1 and 2 must be reconsidered only after the discrete one-cell rotation law is settled.

## 8. Consequence for perimeter history

Historical perimeter trace must be generated from cells actually selected along legitimate discrete trajectories.

It may not be defined by:

- every cell geometrically incident to every exact crossing;
- PRE/POST edge vertices;
- nearest endpoint in squared norm.

After trajectories are defined, one may separately form the support union over one trajectory or all legitimate trajectories. This support union is a derived historical object.

## 9. Relation to earlier results

AT3-HI remains exact for the rejected graph-distance-shell model: every vertex is traced at birth there, so no fresh/lifetime-hidden vertex occurs.

AT4-S1 remains useful for:

- exact chamber-local algebraic q-ranges;
- exact arc/cell incidence certificates;
- the robust `D(1,1)` radius-3 hidden witness;
- the negative result that endpoint PRE/POST/NEAREST proxies do not define native cell collapse.

Supersede only the statement that `EXACT_CROSSING + ALL_INCIDENT_CELLS` is itself a native instantaneous rotating state.

## 10. Control-plane pause

Freeze:

`NO_NEW_TASKBOOK_NOW = true`.

`NO_TASK_EXECUTION_UNTIL_EXPLICIT_USER_RESUME = true`.

A previously created S1R taskbook/owner branch may remain in repository history, but it is not to be treated as an instruction to execute while this pause is active.

The next research question, when explicitly resumed, is to derive the oriented single-cell transition/collapse law and then recompute historical perimeter and the first hidden radius.
