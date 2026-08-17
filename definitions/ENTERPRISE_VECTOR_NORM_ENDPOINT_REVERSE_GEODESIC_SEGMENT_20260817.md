# 进取线段重基：象限内代数向量模先定端点，再反向取全部最短路径

Status: `ACTIVE / CANONICAL / FOUNDATIONAL_SUPERSESSION`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Depends on:
- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_INITIAL_CIRCLE_ALL_UNIT_INVARIANTS_20260817.md`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`
- `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`
Supersedes as foundational radius/segment semantics:
- `ELL_E(P)=1+d_E(O_E,P)` as the definition of circle radius / segment length;
- `EXISTENCE_SPHERE_E(n)={P:d_E(O_E,P)=n-1}` as the canonical higher-circle endpoint rule;
- the use of shortest-jump depth to generate higher circle levels.

## 1. Foundational correction

The previous geodesic-shell route inverted the logical order. It used shortest-jump count to define length/radius first and then declared the graph shell to be the fixed-length endpoint set.

Freeze the corrected order:

`VECTOR_LENGTH -> ENDPOINT_CELLS -> REVERSE_SHORTEST_PATH_FIBERS`.

A fixed Enterprise segment/circle scale is determined first by a cumulative/resultant vector length, not by primitive jump count.

Shortest paths remain important only after an endpoint cell is selected: they are the complete minimum-jump realizations of that endpoint.

Freeze:

`GRAPH_JUMP_COUNT_DOES_NOT_DEFINE_ENTERPRISE_RADIUS`.

`SHORTEST_PATHS_REALIZE_A_VECTOR_SELECTED_ENDPOINT`.

## 2. Accumulate vectors first; never sum scalar edge lengths as radius

Let a path carry directed displacement vectors

`Delta V_1, Delta V_2, ..., Delta V_k`.

Do not define the radius by

`sum_i ||Delta V_i||_E`.

When primitive steps have common unit scalar length, that scalar sum collapses to jump count and reproduces the rejected shell model.

Instead compose the displacement vectors algebraically in the currently valid coordinate chamber:

`V_cum = V_base + Delta V_1 + ... + Delta V_k`.

Then measure the resultant vector.

Freeze:

`COMPOSE_VECTORS_FIRST__MEASURE_RESULTANT_SECOND`.

## 3. Quadrant/chamber-local algebraic vector norm is canonical

The previous warning that the square-root-of-sum-of-squares formula had to be rediscovered was too strong.

Current Enterprise axes are already frozen as pairwise `ENTERPRISE_ORTHOGONAL`. Together with the frozen arithmetic laws

`ENTERPRISE_SQUARE(t)=t^2`

and

`ENTERPRISE_ROOT(t^2)=t`,

the vector-length formula is accepted as an **algebraic norm inside one currently operable sign chamber / quadrant**.

Let

`V = v_1 e_1 + v_2 e_2 + v_3 e_3`

be an Enterprise vector expressed in one fixed admissible sign chamber, with `e_i` the three native orthogonal axis directions. Then

`||V||_E = ENTERPRISE_ROOT(v_1^2 + v_2^2 + v_3^2)`.

Equivalently,

`||V||_E = sqrt(v_1^2 + v_2^2 + v_3^2)`

as an algebraic formula.

If a local calculation has only two active components, the third vector-algebra component is zero and the same law reduces to

`sqrt(x^2+y^2)`.

This use of scalar/vector-algebra zero does **not** create native coordinate `0`. A zero vector component means only that the vector has no component along that algebraic basis direction.

Freeze:

`VECTOR_ALGEBRA_ZERO_COMPONENT != NATIVE_COORDINATE_ZERO`.

`QUADRANT_LOCAL_PYTHAGOREAN_VECTOR_NORM = ACCEPTED_ALGEBRAIC_LAW`.

This is not a claim that the Enterprise plane is globally Euclidean. It is a claim that, inside a fixed operable algebraic sign domain, orthogonal vector components combine by square, sum, and Enterprise root.

## 4. Current quadrant restriction is structural, not a bug in the formula

At present the Enterprise plane does **not** have a frozen coordinate-operation law that carries one raw coordinate expression continuously across a sign/quadrant boundary.

Therefore the algebraic norm formula is applied only inside one fixed sign-consistent chart/chamber.

When a path or endpoint analysis reaches a chamber boundary:

1. stop the current coordinate arithmetic at the boundary;
2. pass to an adjacent valid sign chart/chamber;
3. re-express the vector there;
4. continue with the same algebraic norm law in the new chamber.

Do not perform a single raw-coordinate calculation that crosses a sign boundary as if the present coordinate algebra were globally chart-free.

Freeze:

`CURRENT_ENTERPRISE_COORDINATE_OPERATIONS_ARE_CHAMBER_LOCAL`.

`CROSS_CHAMBER_GEOMETRY_REQUIRES_CHART_TRANSITION`.

The word “quadrant” here denotes an Enterprise algebraic sign chamber; it is not assumed to mean the four classical Cartesian quadrants.

This is consistent with the guiding principle:

`ENTERPRISE_GEOMETRY_IS_CLOSER_TO_ALGEBRA_THAN_TO_CLASSICAL_CONTINUOUS_GEOMETRY`.

## 5. Initial unit circle calibration

The initial circle remains

`CIRCLE_E(1)={O_E}`

with

`R_E(1)=D_E(1)=P_E(1)=A_E(1)=1`.

The exact embedding of the unique void-to-origin unit generation into the chamber-local vector representation must preserve the base norm one.

Do not identify the raw native coordinate tuple `(±1,±1,±1)` with a three-component displacement vector by fiat. Native point coordinates and vector-algebra components are distinct typed objects.

Freeze:

`POINT_COORDINATE_TUPLE != VECTOR_COMPONENT_TUPLE` unless an explicit chart map is given.

This avoids the false inference that the origin vector norm is `sqrt(3)` merely because a three-axis point representative can be written `(±1,±1,±1)`.

## 6. Forward vector-radius endpoint generation

For target vector length `rho>=1`, generate admissible cumulative vectors **within each valid algebraic chamber** and retain every native cell reached with resultant norm `rho`.

Write chamberwise:

`END_VEC_E(rho;Q) = { P : an admissible Q-local vector accumulation reaches P with ||V_cum||_E=rho }`.

The global candidate endpoint support is obtained only by the justified union/gluing of the chamber-local supports along common axis/boundary states:

`END_VEC_E(rho) = GLUE_Q END_VEC_E(rho;Q)`.

Do not obtain global support by a single cross-quadrant coordinate calculation.

If several chamber representations of the same boundary cell occur, retain the full provenance and prove their compatibility.

The number of primitive jumps used to reach `P` is provenance, not the fixed radius.

## 7. Reverse shortest-path realization fiber

After an endpoint cell `P in END_VEC_E(rho)` is selected by vector norm, reverse the problem:

`GEO_REV_E(P) = { gamma : VOID_E -> P | gamma has minimum admissible primitive jump count among paths to P }`.

Equivalently, after deleting the unique `VOID_E -> O_E` prefix, retain every minimum-jump spatial tail from `O_E` to `P`.

Freeze:

`ALL_REVERSE_SHORTEST_REALIZATIONS_ARE_RETAINED`.

`MIN_JUMP_COUNT(P) != VECTOR_RADIUS(P)` in general.

No representative shortest path is privileged.

## 8. New segment ontology

For vector radius `rho` and endpoint `P in END_VEC_E(rho)`, define

`SEG_VEC_E(rho,P) = (rho, P, GEO_REV_E(P))`.

The complete fixed-length segment family is

`SEG_VEC_E(rho) = {SEG_VEC_E(rho,P): P in END_VEC_E(rho)}`.

Thus:

- vector length is primary;
- endpoint cell is selected by vector algebra;
- shortest-path family is the secondary realization fiber.

This supersedes

`segment length = shortest path length`.

## 9. Circle/perimeter consequence reopened

A higher Enterprise circle may be generated only after `END_VEC_E(rho)` is known.

Candidate support:

`CIRCLE_SUPPORT_VEC_E(rho)=END_VEC_E(rho)`.

Whether the glued support is connected, whether it has one or many legal perimeter traversals, and how perimeter/area propagate are theorem questions.

Do not replace it by a graph-distance shell merely because that shell is easy to enumerate.

## 10. Hidden-interior consequence

The AT3-HI theorem remains exact for the rejected graph-shell candidate:

`graph-distance shell + geodesic hull -> every vertex is perimeter-traced at birth`.

That negative theorem no longer constrains the vector-radius support.

Because exact vector-norm levels need not coincide with minimum-jump shells, a cell can in principle become interior without ever lying on any prior exact vector-norm perimeter support.

The canonical fresh-hidden question is therefore reopened.

No claim that such a point must exist is frozen here.

## 11. What survives

Preserve:

- `VOID_E=∅` external pre-coordinate nonexistence;
- `VOID_E -> O_E=±1` unique first existence transition;
- no native coordinate zero;
- signed negative coordinates;
- initial circle `(R,D,P,A)=(1,1,1,1)`;
- graph distance/minimum jump count as a combinatorial observable;
- all shortest paths to a fixed endpoint as reverse realization structure;
- `ENTERPRISE_SQUARE(n)=n^2` and Enterprise root;
- three pairwise `ENTERPRISE_ORTHOGONAL` native axes.

Supersede:

- `ELL_E=1+d_E` as geometric segment radius/length;
- graph-distance shells as canonical higher circles;
- the claim that the algebraic square-root-of-sum-of-squares vector norm is unavailable.

## 12. Canonical summary

Freeze:

`RADIUS_IS_RESULTANT_VECTOR_NORM_NOT_JUMP_COUNT`.

`VECTOR_NORM_WITHIN_A_VALID_CHAMBER = sqrt(sum of squared orthogonal vector components)`.

`CURRENT_COORDINATE_ARITHMETIC_CANNOT_CROSS_CHAMBERS_WITHOUT_RECHARTING`.

`VECTOR_NORM_SELECTS_ENDPOINT_CELLS`.

`REVERSE_MIN_JUMP_SEARCH_RETURNS_ALL_SHORTEST_REALIZATIONS`.

`SHORTEST_PATH_LENGTH_IS_NOT_SEGMENT_LENGTH`.

`GRAPH_DISTANCE_SHELL_IS_NOT_CANONICAL_CIRCLE_BY_DEFINITION`.
