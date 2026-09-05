# Enterprise X6 centered three-axis native slice rebase

Status: `ACTIVE / FOUNDATION / P000-V5-BOUND / X6-SIGNED-SLICE / DIRECT-USER-REBASE`
Date: `2026-09-05`
Steward: `EM-STW-C31A7F / FOUNDATION_STEWARD`
Authority: direct user instruction to unify the three-axis cut plane with the full six-axis Cell-center geometry and to recompute the earlier cut-plane calculations from the signed X6 foundation.
Parent foundation: `ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`.
Observer guard: `ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`.

## 1. Purpose and controlling correction

The full signed X6 Cell-center torsor is the native spatial identity layer. A three-axis slice is therefore not a second ontology with a different kind of origin.

For every selected native-axis triple `S={i,j,k}` and chosen spatial Cell anchor `c_*`, define the centered native slice

`X_S(c_*) := c_* + Z e_i + Z e_j + Z e_k`.

Its exact raw slice coordinate is

`x=(x_i,x_j,x_k) in Z^3`,

with the same Cell anchor as zero:

`coord^S_{c_*}(c_*)=(0,0,0)`.

Freeze:

`THREE_AXIS_NATIVE_SLICE = CENTERED_AFFINE_SUBTORSOR_OF_X6`.

`THREE_AXIS_NATIVE_SLICE_COORDINATES = SIGNED_Z3`.

`THREE_AXIS_NATIVE_SLICE_ZERO = CHOSEN_CELL_CENTER`.

`SLICE_CELL_ZERO = FULL_X6_CELL_ANCHOR_RESTRICTED_TO_S`.

There is no native spatial hole at coordinate zero.

## 2. Three different objects that must not be conflated

The rebase separates:

1. `NATIVE_CELL` — one spatial Cell state in X6;
2. `CELL_COORDINATE_ZERO` — the chosen native Cell anchor used to coordinatize the torsor/slice;
3. `CARRIER_TRIPLE_INCIDENCE_VERTEX` — a point where three classical circular carrier footprints meet.

The third object was historically called the Enterprise origin `O_E`. That use is superseded for native spatial coordinates. In current typing write such a carrier incidence vertex as `V_E` (or an explicitly indexed `V_E(C_a,C_b,C_c)`).

Freeze:

`CELL_COORDINATE_ZERO = NATIVE_CELL_ANCHOR`.

`CARRIER_TRIPLE_INCIDENCE_VERTEX != NATIVE_CELL`.

`CARRIER_TRIPLE_INCIDENCE_VERTEX != NATIVE_COORDINATE_ZERO`.

`LEGACY_O_E_AS_TRIPLE_BOUNDARY_INTERSECTION = RETYPED_TO_CARRIER_INCIDENCE_VERTEX_V_E`.

A carrier drawing may of course choose an arbitrary plotting origin, but that plotting choice has no authority over native Cell identity.

## 3. Exact embedding into full X6

For ordered `S=(i,j,k)`, define

`J_S: Z^3 -> Z^6`

by placing `(x_i,x_j,x_k)` in components `i,j,k` and putting zero in the three omitted components. Relative to the same anchor,

`coord_{c_*}(P)=J_S(x)` for `P in X_S(c_*)`.

Thus slice membership means the three omitted **relative coordinates are exactly zero**. This differs from merely observing three components of an arbitrary full X6 state.

Freeze:

`NATIVE_SLICE_MEMBERSHIP != SELECTED_SLICE_OBSERVATION_OF_ARBITRARY_X6_STATE`.

`P in X_S(c_*) -> OMITTED_RELATIVE_COMPONENTS_OF_P = 0`.

`Obs_S(z)` for arbitrary `z in Z^6` remains a lower-information observer and does not assert slice membership.

## 4. Signed primitive adjacency and no axis fissure

The primitive coordinate neighbors inside the selected slice are

`x -> x +/- e_i`,

`x -> x +/- e_j`,

`x -> x +/- e_k`.

Hence every selected native axis is a two-sided integer Cell chain

`...,-2,-1,0,1,2,...`

through the Cell anchor.

Freeze:

`THREE_AXIS_SLICE_PRIMITIVE_NEIGHBOR_COUNT = 6_DIRECTED`.

`SLICE_AXIS_TICKS = Z`.

`ZERO_TICK_IS_A_LEGAL_NATIVE_CELL_STATE = TRUE`.

`REMOVE_ZERO_CELL_FROM_AXIS = TYPE_ERROR`.

The full X6 still has twelve directed primitive coordinate neighbors; the centered slice simply retains the six belonging to its selected three axes.

## 5. Native metric recomputation

For `P,Q in X_S(c_*)`, let raw signed slice displacement be

`d=coord^S(Q)-coord^S(P)=(d_i,d_j,d_k) in Z^3`.

The X6 component rule restricts exactly to

`d_S(P,Q)^2 = d_i^2+d_j^2+d_k^2`.

Therefore

`d_S(P,Q)=d_S(Q,P)`

and signed reversal sends `d -> -d` without changing length.

Freeze:

`CENTERED_SLICE_NATIVE_DISTANCE_SQUARED = SUM_OF_THREE_SIGNED_COMPONENT_SQUARES`.

`CENTERED_SLICE_NATIVE_DISTANCE_IS_SYMMETRIC = TRUE`.

`L_E(+e_a)=L_E(-e_a)=1` for every selected axis `a`.

This is the restriction of the full X6 metric, not a newly selected scalarization.

### Recomputed 3-4-5 witness

For raw native displacement

`d=(3,4,0)`,

`L_E(d)^2=3^2+4^2=25`, so `L_E(d)=5`.

The reverse displacement is

`-d=(-3,-4,0)`

and also has squared native length `25`.

Thus the old reversal value `17` is not a native signed-slice length; it came from applying a positive/min-zero re-decoding observer to the reverse displacement.

## 6. Relative min-zero observer and exact repair coordinate

For raw slice coordinate `x=(x_i,x_j,x_k)` define

`h_S(x)=min(x_i,x_j,x_k)`

and

`r_S(x)=can3(x)=x-h_S(x)*(1,1,1)`.

Then

`r_S(x) in N_0^3`, `min(r_S)=0`,

and the decomposition

`x = r_S(x)+h_S(x)*(1,1,1)`

is unique.

Hence

`Z^3 <-> A3_REL x Z`,

where

`A3_REL := {(a,b,c) in N_0^3 : min(a,b,c)=0}`.

Freeze:

`MIN_ZERO_TRIPLE = RELATIVE_SLICE_OBSERVER_ADDRESS`.

`MIN_ZERO_TRIPLE_ALONE != NATIVE_CELL_IDENTITY`.

`LOSSLESS_THREE_AXIS_SLICE_CHART = (MIN_ZERO_RESIDUAL, INTEGER_COMMON_DEPTH)`.

The historical tuple set called `A_E` is retained only as a compatibility representation of this min-zero observer/carrier-center address. It is no longer the primitive native Cell address.

### Distance from repaired coordinates

If

`P <-> (r,h)` and `Q <-> (s,k)`,

then with `Delta h=k-h`,

`d_S(P,Q)^2 = sum_{a in S} (s_a-r_a+Delta h)^2`.

Dropping `Delta h` is therefore not safe for native distance.

## 7. Recomputed triangular/FCC carrier projection

For each established FCC/K4 STAR slice choose three chart-local classical carrier vectors

`u_i,u_j,u_k`

with

`|u_i|=|u_j|=|u_k|=1`,

pairwise Euclidean angle `120 degrees`, and

`u_i+u_j+u_k=0`.

Define the classical planar carrier readout

`pi_S(x)=x_i u_i+x_j u_j+x_k u_k`.

This is a **readout/projection**, not native identity.

Its exact kernel is

`ker(pi_S)=Z*(1,1,1)`.

Equivalently, after choosing `(u_i,u_j)` as carrier generators and using `u_k=-u_i-u_j`, an exact axial carrier coordinate is

`carrier_S(x)=(x_i-x_k, x_j-x_k) in Z^2`.

Therefore

`pi_S(x)=pi_S(y) <=> y-x = n*(1,1,1)` for some `n in Z`.

Freeze:

`FCC_SLICE_CARRIER_CENTER_IDENTITY = Z^3 / Z(1,1,1)`.

`FCC_SLICE_CARRIER_KERNEL != NATIVE_COORDINATE_EQUIVALENCE`.

`MIN_ZERO_RESIDUAL = CANONICAL_SECTION_OF_CARRIER_CENTER_QUOTIENT`.

This is the exact three-axis local form of the global observer-preservation issue already present in X6.

## 8. Carrier Euclidean distance is not native Enterprise distance

For a raw triple `x=(a,b,c)`, the classical planar carrier squared distance from the carrier origin is

`Q_car(x)=a^2+b^2+c^2-ab-bc-ca`.

It is diagonal-shift invariant and therefore depends only on `pi_S(x)`.

By contrast, native Enterprise squared length is

`L_E(x)^2=a^2+b^2+c^2`,

which is not diagonal-shift invariant.

Recomputed witness:

- `x=(3,4,0)` has native `L_E^2=25` and carrier `Q_car=13`;
- `x'=(4,5,1)=x+(1,1,1)` has the **same carrier center** and the same `Q_car=13`, but native `L_E^2=42`.

Freeze:

`CARRIER_CENTER_ADDRESS_ALONE_CANNOT_DETERMINE_NATIVE_LENGTH`.

`CARRIER_EUCLIDEAN_DISTANCE != NATIVE_ENTERPRISE_DISTANCE`.

`COMMON_DEPTH_IS_REQUIRED_FOR_NATIVE_METRIC_WHEN_STARTING_FROM_MIN_ZERO_CARRIER_ADDRESS`.

## 9. Recomputed circle-footprint geometry

The earlier circle construction survives as a property of the classical triangular carrier readout, not as the ontology of a native Cell.

Normalize nearest carrier-center spacing to

`D_CARRIER_CENTER=1`.

For an elementary equilateral carrier triangle of side `1`, its circumradius is

`R_CARRIER=1/sqrt(3)`.

Thus every native Cell read out at one carrier center may be decorated by a circular carrier footprint of radius `1/sqrt(3)`.

Freeze:

`CARRIER_CIRCLE_FOOTPRINT_RADIUS = 1/sqrt(3)`.

`CARRIER_CIRCLE_FOOTPRINT != NATIVE_CELL_IDENTITY`.

### Neighbor overlap

`1 < 2/sqrt(3)`,

so neighboring carrier circles overlap with positive area.

### Triple boundary intersections

For two neighboring centers separated by `1`, the two equal-radius circle intersections lie at squared perpendicular offset

`R_CARRIER^2-(1/2)^2 = 1/3-1/4 = 1/12`.

They are exactly the circumcenters of the two elementary equilateral carrier triangles adjacent to that center-center edge. Each is therefore also at distance `1/sqrt(3)` from the corresponding third nearest center.

The next nonzero triangular-lattice center separation has squared distance `3`, while

`(2R_CARRIER)^2=4/3`.

Hence non-neighbor carrier circles do not intersect. Every boundary intersection in this radius-`1/sqrt(3)` carrier construction is consequently a three-circle incidence.

Freeze:

`EVERY_CARRIER_CIRCLE_BOUNDARY_INTERSECTION_IS_TRIPLE = TRUE`.

These points are `V_E` incidence vertices, not native coordinate zeros.

### Gap-free carrier cover

The Voronoi vertices of the unit triangular center lattice are the same elementary-triangle circumcenters, at distance `1/sqrt(3)` from the nearest centers. Therefore radius `1/sqrt(3)` is the exact covering radius.

Freeze:

`UNION_OF_CARRIER_CIRCLE_FOOTPRINTS = CLASSICAL_SLICE_CARRIER_PLANE`.

`CARRIER_COVER_IS_GAP_FREE = TRUE`.

This statement is about the classical readout plane. It is not a claim that a continuum of points constitutes the native discrete X6 space.

## 10. Recomputed meaning of the old triple-intersection origin

The former `O_E` construction is retained only as carrier relation data:

`V_E(C_a,C_b,C_c) in boundary(F_a) cap boundary(F_b) cap boundary(F_c)`.

It is useful as an incidence/transition/relational vertex between carrier footprints.

It is no longer used to create a type-changing start map of the form

`O_E -> first Cell`.

A native path starts at an actual native Cell and proceeds by primitive signed Cell-to-Cell steps.

Freeze:

`NATIVE_PATH_START = NATIVE_CELL`.

`NO_SPECIAL_ORIGIN_TO_FIRST_CELL_INCIDENCE_STEP_REQUIRED`.

`TRIPLE_INCIDENCE_VERTEX = RELATION_READOUT_NOT_SPATIAL_CELL_STATE`.

## 11. Carrier triangle closure becomes native hidden displacement

Let

`H_S=e_i+e_j+e_k`, represented in the raw slice as `(1,1,1)`.

Because `u_i+u_j+u_k=0`,

`pi_S(H_S)=0`.

But in native X6,

`H_S != 0`,

`L_E(H_S)^2=3`,

and `N_min(H_S)=3`.

Therefore an ordered three-step path using each selected positive axis once is a **closed triangle in the carrier readout but not a native spatial return**.

Freeze:

`CARRIER_TRIANGLE_RETURN != NATIVE_CELL_RETURN`.

`CARRIER_TRIANGLE_HOLONOMY = NONZERO_NATIVE_COMMON_DEPTH_STEP H_S`.

For integer `n`,

`L_E(nH_S)^2=3n^2`.

For `n>0`, the number of shortest native path words to `nH_S` is

`(3n)!/(n!)^3`.

This is an explicit BRC witness that a carrier endpoint quotient cannot erase native path/state information.

## 12. Signed native path and BRC recomputation

For raw signed slice displacement

`d=(d_i,d_j,d_k)`,

the X6 formulas restrict to

`N_min(d)=|d_i|+|d_j|+|d_k|`,

`L_E(d)^2=d_i^2+d_j^2+d_k^2`,

and for `d != 0`,

`PRIMITIVE_STRAIGHT <=> support_size(d)=1 <=> N_min(d)=L_E(d)`.

If more than one component is nonzero, the displacement is a composite native path/readout under P000.

The exact shortest-path N-BRC multiplicity is

`B_min(d)=N_min(d)!/(|d_i|! |d_j|! |d_k|!)`.

Freeze:

`CENTERED_SLICE_BRC_USES_RAW_SIGNED_DISPLACEMENT_BEFORE_MIN_ZERO_PROJECTION`.

`SIGNED_REVERSAL_PRESERVES_SHORTEST_PATH_MULTIPLICITY`.

### Recomputed 3-4-5 path count

For `(3,4,0)`,

`N_min=7`, `B_min=7!/(3!4!)=35`.

For the native reverse `(-3,-4,0)`, the same values hold:

`N_min=7`, `B_min=35`.

The historical positive/min-zero reverse decode `(1,0,4)` has only `5` shortest positive words and squared component readout `17`; both are observer artifacts, not the native reverse of `(3,4,0)`.

### Recomputed squared-length-25 shell

In the full signed centered three-axis slice, the integer solutions of

`d_i^2+d_j^2+d_k^2=25`

are exactly:

- 6 signed axis endpoints, permutations of `(±5,0,0)`;
- 24 signed two-axis endpoints, permutations/signs of `(±4,±3,0)`.

Hence there are `30` raw native displacement endpoints at squared length `25`.

The 6 axis endpoints each have one shortest path. The 24 support-two endpoints each have `35` shortest paths. Therefore the full signed-shell shortest-path count is

`6 + 24*35 = 846`.

The historical one-positive-sector subtotal

`1+35+35+1=72`

remains correct only for the four nonnegative `S_ij` representatives `(0,5),(3,4),(4,3),(5,0)` with the third raw component fixed to zero. It is not the complete signed native slice shell.

Freeze:

`OLD_N25_72 = POSITIVE_SECTOR_SUBSET_COUNT_NOT_FULL_NATIVE_SLICE_COUNT`.

`FULL_SIGNED_THREE_AXIS_N25_ENDPOINT_COUNT = 30`.

`FULL_SIGNED_THREE_AXIS_N25_SHORTEST_BRC_COUNT = 846`.

## 13. Positive-only residual + path-length repair

For a path using only the three selected positive native axes, let exact raw endpoint be

`n in N_0^3`, `m=sum_i n_i`.

If only the min-zero carrier residual `r=can3(n)` and path length `m` are retained, the omitted common depth is

`k=(m-sum_i r_i)/3`

when this is a nonnegative integer, and

`n=r+k*(1,1,1)`.

Thus a carrier triangle path with endpoint `n=(1,1,1)` has

`r=(0,0,0)`, `m=3`, `k=1`.

The carrier endpoint alone says “return”; carrier endpoint plus path length reconstructs the hidden positive common depth in this restricted positive-only setting.

This reconstruction does not make the carrier endpoint quotient globally safe for signed paths, arbitrary future operations, provenance, or full X6 state.

## 14. Retyping of legacy R061/R062 slice results

The following older formulas are preserved only at their valid lower-information strength.

### Positive shuffle counts survive

For raw positive displacement `(a,b,0)` with `a,b>=0`, the number of shortest words in the two selected positive generators remains

`binom(a+b,a)`.

Thus the historical `3,4` count `35` is retained exactly.

### Old “native line” terminology is narrowed

Under current P000, a primitive straight segment has support on exactly one native axis. Therefore a support-two object such as `(3,4,0)` is not a new primitive straight direction. It is a composite native displacement with a BRC path fiber.

Freeze:

`LEGACY_SUPPORT_TWO_NATIVE_LINE_IDENTITY = RETYPED_TO_COMPOSITE_NATIVE_DISPLACEMENT_TRACE`.

### Directed min-zero gauge is observer-only

The historical decoder

`can3(d)`

and its sum-of-squares value remain a valid positive/min-zero **observer gauge**, but they are not the native signed point-to-point metric.

Freeze:

`LEGACY_DIRECTED_MIN_ZERO_GAUGE = CARRIER_RELATIVE_OBSERVER_GAUGE`.

`LEGACY_DIRECTED_GAUGE_ASYMMETRY != NATIVE_SIGNED_DISTANCE_ASYMMETRY`.

### Bidirectional length spectrum is no longer needed as native metric repair

At native signed slice strength,

`d_S(P,Q)=d_S(Q,P)`

already holds. Historical bidirectional spectra may be retained as observer diagnostics of the positive/min-zero decoder, not as the native orientation-free length object.

### BRC bridge survives with richer typing

The enrichment order

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`

remains valid, but the skeleton must now retain signed raw native components and must distinguish native endpoint from carrier endpoint. In particular, carrier recoalescence at `H_S` does not imply native recoalescence.

## 15. Rotation and slice covariance

Any axis permutation in the X6 `S6` skeleton transports the centered slice construction:

`S -> sigma(S)`,

`X_S(c_*) -> X_{sigma(S)}(sigma(c_*))`.

For the FCC/K4 carrier-atlas subgroup, the four established STAR selections retain their close-packed triangular carrier realization. The current rebase changes their origin/type semantics, not their carrier incidence combinatorics.

Freeze:

`CENTERED_SLICE_REBASE_IS_AXIS_PERMUTATION_COVARIANT`.

`FCC_STAR_SLICE_COMBINATORICS_SURVIVE`.

`FCC_CARRIER_PROJECTION_REMAINS_LOWER_INFORMATION_THAN_NATIVE_SLICE`.

## 16. Recalculation ledger

| Earlier item | Recomputed status |
| --- | --- |
| origin is triple circle boundary intersection | **superseded as native origin**; retained as carrier incidence vertex `V_E` |
| origin is not a Cell | **superseded for native coordinates**; slice coordinate zero is a chosen Cell |
| three positive rays only | **superseded at native layer**; selected axes have primitive signed directions `+/-E_i` |
| min-zero `N_0^3` is primitive Cell address | **superseded**; it is a carrier/relative observer section |
| nearest carrier-center spacing `1` | **retained** |
| carrier circle radius `1/sqrt(3)` | **retained, retyped as carrier footprint** |
| neighboring circles overlap | **retained at carrier layer** |
| every circle-boundary crossing is triple | **retained at carrier layer** |
| circle footprints cover carrier plane without gaps | **retained at carrier layer** |
| native right angle `120°` | **retained by P000** |
| `(3,4,0)` native length `5` | **retained only when `(3,4,0)` is raw signed native displacement** |
| reverse `(3,4,0)` has squared gauge `17` | **superseded as native length**; true native reverse squared length is `25` |
| unit reverse length squared `2` | **superseded as native length**; true native reverse squared length is `1` |
| directed native metric/gauge | **superseded at native layer** by symmetric signed component metric; retained as observer gauge |
| N=25 one-sector path total `72` | **retained as positive-sector subset** |
| full signed native N=25 shell | **recomputed: 30 endpoints, 846 shortest paths** |
| three-positive-step carrier triangle returns | **carrier return only**; native endpoint is `H_S`, norm squared `3`, BRC multiplicity `6` |

## 17. Machine invariants

Freeze the following for machine/checker use:

`CENTERED_THREE_AXIS_SLICE_FOUNDATION=ACTIVE`.

`CENTERED_THREE_AXIS_SLICE_PARENT=X6_NATIVE_SPATIAL`.

`CENTERED_THREE_AXIS_SLICE_COORDINATE_CARRIER=Z^3`.

`CENTERED_THREE_AXIS_SLICE_ZERO=CHOSEN_NATIVE_CELL_ANCHOR`.

`CENTERED_THREE_AXIS_SLICE_ZERO_IS_CELL=true`.

`CENTERED_THREE_AXIS_SLICE_PRIMITIVE_DIRECTION_DOMAIN=SIGNED_SELECTED_NATIVE_AXES`.

`CENTERED_THREE_AXIS_SLICE_NATIVE_DISTANCE_SQUARED=SUM_OF_THREE_SIGNED_COMPONENT_SQUARES`.

`CENTERED_THREE_AXIS_SLICE_NATIVE_DISTANCE_SYMMETRIC=true`.

`THREE_AXIS_MIN_ZERO_ADDRESS=RELATIVE_CARRIER_OBSERVER_NOT_NATIVE_IDENTITY`.

`THREE_AXIS_MIN_ZERO_LOSSLESS_REPAIR=INTEGER_COMMON_DEPTH`.

`FCC_STAR_SLICE_CARRIER_KERNEL=Z(1,1,1)`.

`CARRIER_TRIPLE_INCIDENCE_VERTEX!=NATIVE_COORDINATE_ZERO`.

`CARRIER_CIRCLE_RADIUS=1/sqrt(3)`.

`CARRIER_CIRCLE_COVER_GAP_FREE=true`.

`CARRIER_BOUNDARY_INTERSECTIONS_TRIPLE=true`.

`CARRIER_TRIANGLE_RETURN!=NATIVE_RETURN`.

`RAW_SIGNED_DISPLACEMENT_REQUIRED_BEFORE_NATIVE_LENGTH_OR_BRC_COLLAPSE=true`.

`LEGACY_POSITIVE_MIN_ZERO_REVERSAL_ASYMMETRY=OBSERVER_ARTIFACT_NOT_NATIVE_METRIC`.

`FULL_SIGNED_THREE_AXIS_N25_ENDPOINT_COUNT=30`.

`FULL_SIGNED_THREE_AXIS_N25_SHORTEST_BRC_COUNT=846`.

## 18. Supersession and compatibility

This definition supersedes the native-coordinate/origin/metric interpretation of:

- `ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`;
- `ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md` where it calls support-two traces primitive/native straight lines;
- `ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` as a native point-to-point metric/gauge;
- `ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md` as the repair for native reversal asymmetry;
- `ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` only where its transition skeleton assumes the old non-Cell origin or positive/min-zero native ontology.

Exact carrier geometry, positive-sector combinatorics, trace-word counts and BRC projections survive only at the explicitly retyped strengths stated above.

Git history retains the older generations as provenance. Current work must start from the centered signed slice and descend to the carrier/min-zero observer only with explicit type labels.
