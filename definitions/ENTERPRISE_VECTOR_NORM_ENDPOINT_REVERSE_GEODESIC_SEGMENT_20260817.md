# 进取线段重基：固定累计向量模长，先定端点 cell，再反向取全部最短路径

Status: `ACTIVE / CANONICAL / FOUNDATIONAL_SUPERSESSION`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Depends on:
- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_INITIAL_CIRCLE_ALL_UNIT_INVARIANTS_20260817.md`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`
Supersedes as foundational radius/segment semantics:
- `ELL_E(P)=1+d_E(O_E,P)` as the definition of circle radius / segment length;
- `EXISTENCE_SPHERE_E(n)={P:d_E(O_E,P)=n-1}` as the canonical higher-circle endpoint rule;
- the use of shortest-jump depth to generate higher circle levels.

## 1. Foundational correction

The previous geodesic-shell route inverted the logical order. It used shortest-jump count to define the length/radius first, then declared the endpoints at that graph distance to be the fixed-length shell.

Freeze the corrected order:

`VECTOR_LENGTH -> ENDPOINT_CELLS -> REVERSE_SHORTEST_PATH_FIBERS`.

A fixed Enterprise segment/circle scale is determined first by a **native cumulative vector length**, not by primitive jump count.

Shortest paths remain important, but only after the endpoint cell is known: they are the complete minimal realizations of the already-selected endpoint, not the observable that selects the endpoint radius.

Freeze:

`GRAPH_JUMP_COUNT_DOES_NOT_DEFINE_ENTERPRISE_RADIUS`.

`SHORTEST_PATHS_REALIZE_A_VECTOR_SELECTED_ENDPOINT`.

## 2. Critical non-collapse: accumulate vectors first, take norm second

Let a native spatial path after the origin carry primitive directed displacement vectors

`Delta V_1, Delta V_2, ..., Delta V_k`.

The radius observable must not be the scalar sum

`sum_i ||Delta V_i||_E`.

If all primitive steps have the same unit scalar length, that scalar sum collapses back to jump count and reproduces the rejected shell model.

Instead the path carries a cumulative/resultant vector state

`V_cum(k) = V_base ⊕ Delta V_1 ⊕ ... ⊕ Delta V_k`,

where `V_base` is the native base/vector state associated with the initial circle/origin and `⊕` is the Enterprise-native vector composition law.

The quantity held fixed is

`R_VEC(k) = ||V_cum(k)||_E`.

Freeze the ordering:

`COMPOSE_VECTORS_FIRST__MEASURE_RESULTANT_SECOND`.

Do not substitute a classical Euclidean norm or a scalar path-length sum.

## 3. Initial unit circle calibration retained

The initial circle remains

`CIRCLE_E(1)={O_E}`

with

`R_E(1)=D_E(1)=P_E(1)=A_E(1)=1`.

The vector-radius foundation must reduce to

`||V_base||_E = 1`

in the exact native sense eventually derived.

The algebraic representation of `V_base`, `⊕`, and `||.||_E` beyond this base calibration is not inserted by fiat here. It is a theorem problem.

## 4. Vector norm is native and currently underived

A valid Enterprise vector-length observable must be derived from native structure, not imported from the compatibility plane.

At minimum it must be audited against:

- three native axes and six directions;
- `ENTERPRISE_ORTHOGONAL` axis semantics;
- signed-origin/no-zero rules;
- D6 covariance;
- sign/reversal covariance;
- axis calibration;
- `ENTERPRISE_SQUARE(n)=n^2` without assuming a classical Pythagorean sum;
- the initial-circle unit calibration.

Do not assume

`sqrt(x^2+y^2)`,

`sqrt(x^2+y^2+z^2)`,

`max(|a|,|b|,|a+b|)`,

or any historical BRC/source norm as the native vector norm.

Those may be tested only as candidates/certificates.

## 5. Forward vector-radius endpoint generation

For a target native vector length `rho>=1`, run all admissible native vector-accumulation paths from the initial state and retain every cell reached with cumulative vector norm exactly `rho` under the frozen vector law.

Define, once the vector law is proved well-typed,

`END_VEC_E(rho) = { P : some admissible cumulative vector realization reaches cell P with ||V_cum||_E = rho }`.

If the cumulative vector attached to a cell is path-independent, prove it and reduce this to a pointwise level set.

If different admissible paths to the same cell can carry inequivalent cumulative vector states, do not select one: preserve the full fiber and type `END_VEC_E(rho)` set-valuedly.

The forward generation step may use many jumps. The number of jumps used to reach `P` is provenance, not the fixed radius.

## 6. Reverse shortest-path realization fiber

After an endpoint cell `P in END_VEC_E(rho)` has been selected by vector norm, define its realization fiber by reversing the question:

`GEO_REV_E(P) = { gamma : VOID_E -> P | gamma uses the minimum admissible primitive jump count among paths to P }`.

Equivalently after deleting the unique `VOID_E -> O_E` prefix, retain all minimum-jump spatial tails from `O_E` to `P`.

Freeze:

`ALL_REVERSE_SHORTEST_REALIZATIONS_ARE_RETAINED`.

No representative shortest path is privileged.

But also freeze:

`MIN_JUMP_COUNT(P) != VECTOR_RADIUS(P)` unless a later theorem proves equality on a declared subset.

## 7. New segment ontology

For target vector radius `rho` and endpoint `P in END_VEC_E(rho)`, the Enterprise segment state is the endpoint-selected realization fiber

`SEG_VEC_E(rho,P) = (rho, P, GEO_REV_E(P))`.

The family of all segments of vector length `rho` is

`SEG_VEC_E(rho) = { SEG_VEC_E(rho,P) : P in END_VEC_E(rho) }`.

Thus the endpoint cell and its vector-length class are primary; the shortest path family is secondary realization structure.

This supersedes the prior identification

`segment length = shortest path length`.

## 8. Circle/perimeter consequence reopened

A higher Enterprise circle may now be generated only after the vector-radius endpoint set is known.

Candidate higher-circle support:

`CIRCLE_SUPPORT_VEC_E(rho) = END_VEC_E(rho)`.

Whether this endpoint support admits one or many native perimeter traversals, whether it is connected, and what its perimeter is are theorem questions.

Do not replace `END_VEC_E(rho)` by a graph-distance shell merely because the latter is easy to enumerate.

## 9. Interior and hidden-point consequence

The AT3-HI negative theorem for the simple graph shell remains correct for that rejected candidate arm:

`graph-distance shell + geodesic hull -> every vertex is perimeter-traced at birth`.

It no longer constrains the vector-radius circle in the same way.

Under vector-radius generation, a native cell may satisfy an interior/generation criterion while never belonging to any exact vector-norm perimeter endpoint set. Therefore the canonical fresh-hidden question is reopened from first principles.

No claim that such a point must exist is frozen here; it must be found or ruled out under the derived vector law.

## 10. What survives from the void-first foundation

Retain:

- `VOID_E=∅` is external pre-coordinate nonexistence, not native `0`;
- `VOID_E -> O_E=±1` is the unique first existence transition;
- graph distance `d_E` is a valid combinatorial/min-jump observable;
- all shortest realizations to a fixed endpoint are retained;
- signed-origin and negative-coordinate rules;
- initial circle `(R,D,P,A)=(1,1,1,1)`.

Supersede:

- `ELL_E=1+d_E` as the geometric segment radius/length;
- fixed graph-distance existence shells as canonical higher circles.

`ELL_E` may remain as an external existence-depth / minimum-transition count if needed, but it is no longer the radius observable.

## 11. Canonical summary

Freeze:

`RADIUS_IS_VECTOR_NORM_NOT_JUMP_COUNT`.

`COMPOSE_VECTORS_FIRST__MEASURE_RESULTANT_SECOND`.

`VECTOR_NORM_SELECTS_ENDPOINT_CELLS`.

`REVERSE_MIN_JUMP_SEARCH_RETURNS_ALL_SHORTEST_REALIZATIONS`.

`SHORTEST_PATH_LENGTH_IS_NOT_SEGMENT_LENGTH`.

`GRAPH_DISTANCE_SHELL_IS_NOT_CANONICAL_CIRCLE_BY_DEFINITION`.

The exact native vector composition/norm law and its first hidden-interior consequences are the next research target.
