# 进取向量半径与离散旋转：当前理论总纲

Status: `ACTIVE / CANONICAL / THEORY_SYNTHESIS`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

This file freezes the current theoretical synthesis only. It is not a research taskbook.

## 1. Three-layer ontology

Current Enterprise geometry separates three different layers:

1. **algebraic vector layer** — resultant vectors, square/root and fixed vector norm;
2. **discrete geometric layer** — native cells and cell-by-cell rotation states;
3. **combinatorial realization layer** — minimum-jump/reverse-geodesic path families after a cell has already been selected.

Freeze the order:

`ALGEBRAIC VECTOR LENGTH -> DISCRETE CELL STATE/TRAJECTORY -> REVERSE MIN-JUMP REALIZATION`.

No later layer may be used to redefine an earlier one.

## 2. Native coordinate and vector algebra are different typed objects

The native coordinate origin remains

`O_E=[+1]=[-1]`.

Native coordinate `0` does not exist.

`VOID_E=∅` is an external pre-coordinate state and `VOID_E -> O_E` is the first existence transition.

The initial circle remains

`CIRCLE_E(1)={O_E}`

with

`RADIUS_E=DIAMETER_E=PERIMETER_E=AREA_E=1`.

A native point tuple such as `(±1,±1,±1)` is not automatically a vector-component tuple.

Freeze:

`NATIVE_POINT_COORDINATES != VECTOR_COMPONENTS`.

A chamber-local chart/map is required to associate a native state/cell with algebraic vector components.

Vector algebra may contain zero scalar components. Such a zero only means zero component along one vector basis direction.

Freeze:

`VECTOR_COMPONENT_ZERO != NATIVE_COORDINATE_ZERO`.

## 3. Enterprise vector-length formula

The three native axes are frozen pairwise `ENTERPRISE_ORTHOGONAL`.

Together with

`ENTERPRISE_SQUARE(t)=t^2`

and Enterprise root, the vector norm is frozen inside one valid algebraic sign chamber:

`V=v_1 e_1+v_2 e_2+v_3 e_3`,

`||V||_E = sqrt(v_1^2+v_2^2+v_3^2)`.

For a two-active-component local sector:

`||V||_E=sqrt(x^2+y^2)`.

Equivalently, the squared norm is the algebraic quantity

`q(V)=||V||_E^2=v_1^2+v_2^2+v_3^2`.

Freeze:

`QUADRANT_LOCAL_PYTHAGOREAN_VECTOR_NORM = CANONICAL_ALGEBRAIC_LAW`.

This does not identify the whole Enterprise plane with one global Euclidean Cartesian chart. The formula is an algebraic law on valid orthogonal vector components.

## 4. Resultant first, norm second

For a path carrying directed algebraic increments `Delta V_i`, do not define radius by

`sum_i ||Delta V_i||_E`.

That scalar sum would collapse back toward jump count.

Instead compose vectors first:

`V_k = V_base + sum_(i=1)^k Delta V_i`

inside the current valid chamber/chart, then measure the resultant:

`R_k = ||V_k||_E`.

Freeze:

`COMPOSE_VECTORS_FIRST__MEASURE_RESULTANT_SECOND`.

`RADIUS_IS_RESULTANT_VECTOR_NORM_NOT_JUMP_COUNT`.

The exact point/cell-to-vector chart map, including the representation of the initial unit state `V_base`, must preserve

`||V_base||_E=1`.

Do not infer `sqrt(3)` for the origin from the native point notation `(±1,±1,±1)`.

## 5. Chamber-local operation domain

Current coordinate/vector arithmetic is not globally cross-sign/chamber.

Inside one valid Enterprise algebraic chamber the vector formula is fully usable.

When a geometric object reaches a sign/chamber boundary:

1. stop the raw coordinate calculation in the current chart;
2. identify the shared native boundary/axis state;
3. rechart into the adjacent chamber;
4. continue with the same algebraic norm law there;
5. obtain a global object by gluing the local descriptions.

Freeze:

`CURRENT_NATIVE_COORDINATE_ARITHMETIC_IS_CHAMBER_LOCAL`.

`CROSS_CHAMBER_GEOMETRY = GLUED_LOCAL_ALGEBRA`.

This is the current precise meaning of the guiding principle

`ENTERPRISE_GEOMETRY_IS_CLOSER_TO_ALGEBRA`.

## 6. Fixed radius is an algebraic level before it is a discrete trajectory

For fixed vector radius `rho`, the chamber-local ideal shell is

`SIGMA_E(Q,rho)={V in Q: ||V||_E=rho}`.

Equivalently,

`q(V)=rho^2`.

In a two-component sector:

`x^2+y^2=rho^2`.

This algebraic shell determines where a fixed-vector-length object would meet the discrete carrier. It does not itself define a native instantaneous state.

Freeze:

`ALGEBRAIC_SHELL = LENGTH_CONSTRAINT_AND_TRANSITION_GUIDE`.

## 7. Enterprise rotation is discrete and cell-valued

Enterprise geometry is discrete. A rotating fixed-length segment occupies exactly one native cell at each trajectory step.

Freeze:

`ROTATING_SEGMENT_NATIVE_STATE = ONE_NATIVE_CELL_PER_STEP`.

An exact algebraic edge crossing is only a transition certificate.

`ALGEBRAIC_CROSSING != NATIVE_STATE`.

The set of cells incident to a crossed edge is an admissibility/support set.

`INCIDENT_CELL_SET != SIMULTANEOUS_NATIVE_STATE`.

Three objects must remain distinct:

- instantaneous state: one cell `C_k`;
- trajectory: `C_0 -> C_1 -> ...`;
- support union: all cells visited along one or many legitimate trajectories.

Freeze:

`INSTANTANEOUS_STATE != TRAJECTORY_SUPPORT`.

## 8. Ambiguity means branching trajectories, not a multivalued state

If a local event admits two equally legitimate cell choices, preserve both possibilities as two trajectories:

`... -> C_a -> ...`

and

`... -> C_b -> ...`.

Every trajectory remains single-valued at every step.

Freeze:

`ALL_LEGITIMATE_PATHS_RETAINED = BRANCHING_OF_SINGLE_CELL_TRAJECTORIES`.

`ALL_LEGITIMATE_PATHS_RETAINED != MULTI_CELL_INSTANTANEOUS_STATE`.

This is the discrete analogue of retaining all legitimate realizations without conflating them into one state.

## 9. Correct algebraic-collapse question is cell-level

For an oriented algebraic shell crossing a shared edge between two native cells, define:

- `CELL_PRE`: cell occupied immediately before the crossing;
- `CELL_POST`: cell entered immediately after the crossing.

The native collapse/rotation question is

`CELL_PRE vs CELL_POST vs a stronger oriented-cell rule`.

The previously studied PRE/DOWN and POST/UP **edge vertices** were only endpoint diagnostics and do not answer this cell-level question.

Freeze:

`NATIVE_COLLAPSE_DIRECTION_IS_CELL_LEVEL`.

A minimum rotation state is currently typed as

`S=(rho,C,epsilon)`

where `rho` is fixed vector radius, `C` is the unique current cell, and `epsilon` is orientation.

If a vertex event requires incoming-edge/previous-cell memory, add the minimum finite memory needed and prove it.

Any deterministic transition law should satisfy reversal:

`T_(-epsilon)=T_epsilon^{-1}`.

No canonical CELL_PRE/CELL_POST selection law is currently frozen.

## 10. Reverse shortest paths are secondary realizations

Only after vector/cell semantics select a target cell `C` may graph distance be used to find all minimum-jump realizations from `VOID_E` to `C`.

Retain all minimizers.

Freeze:

`REVERSE_SHORTEST_PATHS_REALIZE_SELECTED_CELLS`.

`MIN_JUMP_COUNT != VECTOR_RADIUS` in general.

Thus shortest paths remain important but are downstream of vector length and discrete cell selection.

## 11. Hidden-interior mechanism from algebraic square gaps

The graph-distance-shell model forced every vertex to be perimeter-traced at birth and therefore could not create fresh hidden vertices.

The vector-radius model does not have that obstruction.

A native cell `C` has an algebraic squared-norm interval

`q(C)=[q_min(C),q_max(C)]`.

If an entire cell interval lies strictly between consecutive admitted integer squared radii,

`m^2 < q_min(C) <= q_max(C) < (m+1)^2`,

then the cell can become part of a later interior without any exact integer-radius algebraic shell intersecting it.

The current exact chamber-local witness is

`D(1,1)` with

`q(D(1,1))=[9/2,8]`.

Hence

`4 < 9/2 <= q <= 8 < 9`.

It is fully contained by the radius-3 algebraic disk while exact integer-radius arcs 1,2,3 do not intersect it.

Freeze:

`D(1,1)_IS_A_ROBUST_HIDDEN_WITNESS_BY_R3 = true`.

However, the previous radius-3 minimality proof used the union of all incident cells as perimeter history. Under one-cell rotation semantics that history may overcount.

Therefore only

`FIRST_SECTOR_HIDDEN_RADIUS <= 3`

is currently safe.

`FIRST_SECTOR_HIDDEN_RADIUS_EQUALS_3` remains open until the discrete rotation law is fixed.

## 12. Current conceptual summary

The present Enterprise line/circle picture is:

`ALGEBRA chooses the length level`;

`DISCRETE CELL DYNAMICS chooses the actual rotating state`;

`COMBINATORIAL GEODESICS realize the chosen cell afterwards`.

Equivalently:

`VECTOR NORM -> CELL ROTATION -> REVERSE SHORTEST-PATH FIBER`.

This is the current theory-level synthesis and supersedes any interpretation in which graph jump count defines radius or an exact continuous crossing itself serves as the native rotating state.
