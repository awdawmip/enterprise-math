# R061 Stage 1 — Native Object Typing Theorem

Task-ID: `RS-R061-STAGE1-NATIVE-LINE-TRACE-FIBER-ORIGIN-AFFINE-REALIZATION`  
Taskbook source: `4183c1300994e61f5a4443aea8487438a7210cc6`  
Stage 0 frozen head: `e6657ce00382d52acda319f0108b787a03e9d5f2`  
Researcher-ID: `EM-R061S1-4183C1`

## Status

`NATIVE_OBJECT_TYPING_COMPLETE = true`.

The current foundation is geometrically consistent but **undertyped** at one place: the same raw integer tuple was being used both as a native coordinate/vector address and as an integer label for a circle-cell center even though the native number axes pass through triple-intersection vertices and never through cell centers.

The minimal correction is a type split. No metric, radius, axis, sector, cell carrier, or Pythagorean law is changed.

## 1. Four primitive object types

Fix a native right sector `S_ij` with positive axes `E_i,E_j`.

### 1.1 Coordinate vertex

`V_ij(a,b)` is the triple-intersection coordinate vertex with native component address `(a,b)` in the sector chart.

Carrier presentation only:

`V_ij(a,b)=O_E+a t_i+b t_j`.

Special case:

`V_ij(0,0)=O_E`.

The axis tick vertices are `V_ij(n,0)` and `V_ij(0,n)`.

### 1.2 Circle cell and its center

`C_ij(a,b)` is the circle cell in the sector-local affine center chart whose center is the unique sector-anchor center translated by `a t_i+b t_j`.

Its center is denoted `ctr(C_ij(a,b))`.

A cell is identified by its center, but the cell and its center remain typed objects.

### 1.3 Native line identity

For multiplicities `(a,b)` define

`T_{a,b}^{(ij)}=[X_i^a X_j^b]`

under component-preserving commutations `X_i X_j ~ X_j X_i`.

This records the native positive-axis component identity of the segment. It is not merely a carrier endpoint.

### 1.4 Native line-path representative

A line-path representative is a single-cell trajectory

`Sigma_O^(ij) ; w`

where `w` is a linearization of `T_{a,b}^{(ij)}`.

At every discrete trajectory state exactly one circle cell is occupied.

## 2. Exact endpoint type

The native line endpoint is neither an untyped coordinate vertex nor an untyped cell center alone.

Freeze the Stage 1 typing:

`END_E^(ij)(a,b) := ( V_ij(a,b), C_ij(a,b) )`.

Thus:

- the **coordinate/vector component endpoint** `V_ij(a,b)` owns the native length law;
- the **terminal cell** `C_ij(a,b)` owns the terminal discrete trajectory state;
- the pair records the incidence bridge between the algebraic/coordinate line and its circle-cell realization.

Therefore the taskbook question has the exact answer:

`IS_NATIVE_LINE_ENDPOINT_A_COORDINATE_VERTEX_OR_A_CELL_CENTER_OR_A_TYPED_PAIR?`

Answer:

`NATIVE_LINE_ENDPOINT = TYPED_PAIR(COORDINATE_VERTEX, TERMINAL_CIRCLE_CELL)`.

## 3. Native length ownership

For the typed endpoint

`END_E^(ij)(a,b)=(V_ij(a,b),C_ij(a,b))`,

define its native line length through the frozen sector component law:

`L_E(END_E^(ij)(a,b))^2 := a^2+b^2`.

This does not measure the carrier distance from `O_E` to the cell center and does not count graph jumps.

In particular:

`L_E(END_E^(12)(3,4))=5`.

## 4. Why the raw tuple needed a type tag

The foundation simultaneously freezes:

- `O_E=(0,0,0)` as a triple-intersection vertex;
- `O_E` is not a cell center;
- cell centers carry integer sector addresses;
- native number axes never pass through cell centers.

Hence the raw tuple `(a,b,0)` cannot, without a type tag, mean one and the same physical object in both statements.

Stage 1 resolves this without deleting either integer structure:

`VADDR_ij(a,b)` and `CADDR_ij(a,b)` are two typed copies of the same integer semigroup `N_0^2`.

They are linked by the affine incidence map derived in the companion anchor theorem, but they are not identified as physical points.

In particular:

`VADDR_ij(0,0)=O_E`,

while

`CADDR_ij(0,0)=C_ij(0,0) != O_E`.

This is a typing correction, not a numerical offset correction.

## 5. Incidence diagram

For one sector:

`O_E = V_ij(0,0)`

`  --Sigma_O^(ij)--> C_ij(0,0)`

`  --native component address (a,b)--> V_ij(a,b)`

and for a trace linearization `w` with prefix counts `(p_k,q_k)`:

`C_ij(0,0) -> C_ij(p_1,q_1) -> ... -> C_ij(a,b)`.

The terminal relation is

`C_ij(a,b) INCIDENT_TO V_ij(a,b)`.

Thus the line identity, coordinate endpoint, and cell trajectory are connected but not collapsed.

## 6. N=0 boundary case

`T_{0,0}` has one empty linearization.

Its line identity has zero native length at `V_ij(0,0)=O_E`.

Its native discrete realization support is typed as the incidence event

`Sigma_O^(ij): O_E -> C_ij(0,0)`

followed by zero center-to-center transitions.

No fictitious cell at the origin is introduced.

For a fixed sector there is one sector-anchor branch. Globally the origin has three incident cells and hence three sector-typed support branches.

## 7. Axis gluing

A positive native axis is shared by two sector charts.

The **line identity** on that physical axis is deduplicated by `(axis label, radial component)`.

The two adjacent sectors have distinct sector-anchor cells, so their two cell trajectories are not duplicates and are both retained as chart-local realizations of the same global axis line identity.

This is not a simultaneous multi-cell state: they are separate trajectories.

## 8. Theorem

With the typed split above:

1. origin, coordinate vertices, centers, cells, line identities, and paths are disjoint types;
2. native length is never assigned to graph jump count or carrier center distance;
3. a line path never acts directly on `O_E` by a center-transition generator;
4. every line path terminates at a cell incident to its coordinate endpoint vertex;
5. the raw integer tuple ambiguity is removed without changing any frozen geometry.

Therefore:

`NATIVE_OBJECT_TYPING_COMPLETE = true`.
