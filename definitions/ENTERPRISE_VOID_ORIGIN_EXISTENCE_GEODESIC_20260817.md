# 进取虚无起点、存在原点与全最短路径线段

Status: `ACTIVE / CANONICAL / FOUNDATIONAL_SUPERSESSION`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Supersedes the start-point convention in `definitions/ENTERPRISE_SEGMENT_ALL_SHORTEST_PATHS_20260817.md`.

## 1. Foundational freeze: start from void, not from the origin

The Enterprise coordinate space does not begin at a coordinate zero.

Freeze an external pre-coordinate state

`VOID_E = ∅`.

`VOID_E` is **not** a native coordinate, not a vertex of the ordinary native coordinate graph `G_E`, and is not the number `0`.

The native coordinate origin remains

`O_E = [+1] = [-1]`.

The first existence/generation step is

`VOID_E -> O_E`.

Thus the extended existence graph `G~_E` is obtained from the native coordinate adjacency graph `G_E` by adjoining exactly one external state `VOID_E` and exactly one generation edge from `VOID_E` to the glued origin `O_E`.

There is no edge from `VOID_E` directly to any other coordinate state.

Freeze:

`VOID_TO_ORIGIN_IS_FIRST_STEP`.

`NATIVE_ZERO_COORDINATE_EXISTS = false`.

## 2. Two distances, two types

For native coordinate states `P,Q in G_E`, keep the internal spatial/native adjacency distance

`d_E(P,Q) = minimum number of primitive native adjacency edges from P to Q inside G_E`.

For a native state `P`, define the existence length from void

`ELL_E(P) = d_(G~_E)(VOID_E,P)`.

Because every path from `VOID_E` to a native coordinate must first traverse `VOID_E -> O_E`,

`ELL_E(P) = 1 + d_E(O_E,P)`.

In particular

`ELL_E(O_E)=1`.

On one signed native axis,

`ELL_E(±n)=n` for every `n>=1`,

where `±1` is the glued origin state and `±n, n>=2` are ordinary signed native coordinates.

Thus native coordinate magnitude and existence length are aligned on the axes:

`ENTERPRISE_COORDINATE_MAGNITUDE(±n)=ELL_E(±n)=n`.

The former is a coordinate label/magnitude; the latter is a path-length theorem. Their equality on axes does not identify the two types globally unless separately proved.

## 3. Enterprise segment from void to a coordinate

The foundational Enterprise segment terminating at native coordinate `P` is the complete shortest-path family in the extended existence graph:

`SEG_E(P) = GEO_(G~_E)(VOID_E,P)`

`= { gamma : VOID_E -> P | |gamma| = ELL_E(P) }`.

Freeze:

`ALL_SHORTEST_VOID_TO_POINT_PATHS_ARE_THE_SEGMENT`.

Since `VOID_E -> O_E` is the unique first edge, removing that first edge gives a canonical bijection

`SEG_E(P) <-> GEO_E(O_E,P)`.

Therefore the previous all-shortest-path family from `O_E` remains the **spatial tail** of the segment, but it is no longer the full foundational segment.

## 4. Origin is the first occupied point-state

The statement

`ORIGIN = ±1`

now has a stronger structural meaning:

- `VOID_E` is non-coordinate / nonexistence;
- first step produces the first occupied coordinate state `O_E=±1`;
- subsequent primitive steps produce higher signed coordinate states.

There is still no native coordinate `0` between void and origin.

The sequence on one positive/negative axis is therefore

`VOID_E -> ±1 -> ±2 -> ±3 -> ...`.

## 5. Fixed existence-length endpoint sets

For integer `n>=1`, define

`EXISTENCE_SPHERE_E(n) = {P in G_E : ELL_E(P)=n}`.

Equivalently,

`EXISTENCE_SPHERE_E(n) = {P : d_E(O_E,P)=n-1}`.

Hence

`EXISTENCE_SPHERE_E(1)={O_E}`.

For `n>=2`, the endpoint set is the ordinary native graph-distance shell of internal radius `n-1`.

Whether this fixed-existence-length shell is the canonical Enterprise circle, its induced cycle structure, circumference law, and circle constant are theorem questions and must be re-derived under this start-point convention.

## 6. Consequence for square/root calibration

This foundation removes the previous apparent offset between axis coordinate magnitude and segment length:

`±n` has existence length `n`.

Therefore the already frozen algebraic/native square calibration

`ENTERPRISE_SQUARE(n)=n^2`

is no longer in tension with a segment-length convention that counted only `n-1` post-origin adjacency steps.

No new square formula is introduced here; this is a typing reconciliation.

## 7. Historical typing

`definitions/ENTERPRISE_SEGMENT_ALL_SHORTEST_PATHS_20260817.md` remains useful for its all-shortest-path ontology, but its statement that the foundational segment starts at `O_E` is superseded.

Retain from it:

- all shortest spatial paths are kept;
- no representative geodesic is selected;
- triangle/strip/packet representations are derived, not ontological primitives.

Replace its length/start convention by:

`SEG_E(P)=all shortest VOID_E-to-P paths`;

`ELL_E(P)=1+d_E(O_E,P)`.

Historical AK/AL/AI circle interpretations remain subject to exact re-audit. No result is protected from contradiction under the new foundation.
