# 进取平面重基：三正轴整数圆心格、半径 1/sqrt(3) 的重叠圆 Cell 覆盖

Status: `ACTIVE / CANONICAL / FOUNDATIONAL_CORRECTION`
Date: `2026-08-20`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Refoundation integration: `FQ-20260822-008 + FQ-20260822-009 / EM-DVR-ZX1UEJ`

This file is the corrected current foundation. It keeps the three-positive-axis overlapping circle-cell carrier with nearest center spacing 1 and cell radius `1/sqrt(3)`, but corrects the native angular/metric semantics: in Enterprise geometry the `120 degree` sector between adjacent positive axes is the native right angle. Therefore the former Euclidean-carrier quadratic form `a^2+b^2+c^2-ab-bc-ca` is not the native Enterprise Pythagorean metric.

The 2026-08-22 refoundation integration changes only two primitive/derived boundaries while preserving the same native model class:

1. the three positive direction families are generated from the unordered elementary origin-center triangle plus one selected orientation-torsor element;
2. within each already-typed two-channel sector, the global sum-of-squares scalar law is derived from one-dimensional square calibration plus local transverse scalar independence.

The canonical native address atlas remains declared/primitive: the carrier min-zero normal form is not promoted into an absolute native address derivation.

## 1. Native origin and object types

The native Enterprise plane origin is

`O_E = 0`.

Every native cell is a circle/disk carrier with a distinguished center.

Freeze:

`ENTERPRISE_NATIVE_ORIGIN = 0`.

`ENTERPRISE_CELL = CIRCLE_CELL`.

`CELL_IDENTITY_IS_BY_CELL_CENTER`.

The origin is not a cell center and is not itself a cell. It is a triple boundary-intersection vertex of three neighboring circle cells.

Freeze:

`ORIGIN_IS_TRIPLE_CELL_INTERSECTION`.

`ORIGIN_IS_NOT_CELL_CENTER`.

`ORIGIN_IS_NOT_A_CELL`.

Strictly distinguish:

1. `CELL_CENTER` — discrete integer-addressed center state;
2. `CIRCLE_CELL` — the closed circular carrier around that center;
3. `COORDINATE_VERTEX` — a triple boundary-intersection event of three cells.

## 2. Integer center carrier and oriented generation of the three positive directions

Cell centers form the same gap-free triangular carrier arrangement. Normalize nearest-neighbor center spacing to

`D_CENTER = 1`.

Freeze:

`NEAREST_CELL_CENTER_DISTANCE = 1`.

Because the origin is the common boundary point of exactly three neighboring origin-incident cells, their three centers canonically determine an **unordered elementary carrier triangle** `T`.

Freeze:

`ORIGIN_INCIDENT_CENTER_TRIANGLE = UNORDERED_ELEMENTARY_TRIANGLE_T`.

Bare incidence plus the triangular translation carrier does not select a cyclic orientation of `T`. Its automorphism group is

`Aut(T) ~= S3`,

and the two cyclic orientations form the two-sheet torsor

`Or(T) ~= S3/A3 ~= C2`.

Select one primitive orientation element

`o in Or(T)`.

This is a torsor element, not a detached Boolean whose literal `0/1` labels have intrinsic native meaning.

Freeze:

`NATIVE_ORIENTATION_DATUM = o in Or(T)`.

Orient the three boundary translation classes of `T` cyclically according to `o`. Their translation classes generate the three positive carrier direction families. The three native axis rays are the rays from `O_E` parallel, in the carrier presentation, to those three positive direction families.

Freeze:

`THREE_POSITIVE_DIRECTION_FAMILIES = DERIVED_FROM_ORIENTED_ORIGIN_TRIANGLE`.

`ENTERPRISE_NATIVE_AXES = THREE_POSITIVE_RAYS`.

The names `E_1,E_2,E_3` are cyclic gauge labels for these three derived positive direction families. The orientation datum does not choose an absolute first axis, base edge, or first vertex.

After choosing `o`, the residual automorphism group preserving the oriented triangle is

`Aut(T,o)=A3 ~= C3`.

Freeze:

`ABSOLUTE_AXIS_LABELS_ARE_GAUGE`.

`RESIDUAL_ORIENTED_TRIANGLE_AUTOMORPHISM = A3 ~= C3`.

In the planar carrier presentation the three positive directions occur successively at `120 degree` separation. The orientation refoundation does **not** derive the native right-angle or scalar law from that carrier angle; those semantic layers are stated separately below.

The carrier boundary translations satisfy the classical presentation relation corresponding to one cyclic triangle traversal, often serialized as

`e_1+e_2+e_3=0`.

This is a relation of a classical planar/translation carrier presentation. It is **not** a native Enterprise vector identity and must not be used to define native length, opposite directions, or coordinate equivalence.

Freeze:

`CARRIER_DIRECTION_RELATION != NATIVE_VECTOR_RELATION`.

`NO_NATIVE_DIAGONAL_SHIFT_QUOTIENT`.

No native negative axes are required. The three positive rays themselves partition the plane into three native sectors.

Freeze:

`NO_NATIVE_NEGATIVE_AXES_REQUIRED`.

## 3. Three positive integer coordinates are primitive sector coordinates, not a carrier quotient

Use nonnegative integer triples

`(a,b,c) in N_0^3`

with canonical condition

`min(a,b,c)=0`.

This is **not** a quotient by common diagonal shift. It is a native sector typing/address rule.

Define the three native sectors:

- `S_12 = {(a,b,0): a,b >= 0}`;
- `S_23 = {(0,b,c): b,c >= 0}`;
- `S_31 = {(a,0,c): a,c >= 0}`.

For an interior point/cell center of one sector exactly one component is zero. On a positive axis two components are zero. At the origin all three components are zero.

Thus

`A_E = {(a,b,c) in N_0^3 : min(a,b,c)=0}`

is the glued union of three two-axis positive coordinate charts.

Freeze:

`THREE_POSITIVE_COORDINATES = THREE_GLUED_TWO_AXIS_SECTOR_CHARTS`.

`NATIVE_ADDRESS_ATLAS = DECLARED_PRIMITIVE_SECTOR_ATTACHMENT`.

`(a,b,c) IS_NOT_EQUIVALENT_TO (a+k,b+k,c+k)`.

The oriented triangle does not by itself derive the absolute attachment of these addresses to cell centers. The reason is structural: after choosing `o`, the residual `A3 ~= C3` symmetry still cyclically permutes the three oriented-triangle roles, while the geometric origin is not itself a center. Hence the center carrier is affine relative to the origin and an absolute address attachment requires more than a carrier displacement normal form.

At the carrier-presentation layer only, if the three oriented boundary translation classes are serialized as `e_1,e_2,e_3`, the coefficient map has kernel

`ker(Phi)=Z(1,1,1)`.

Subtracting the common minimum from an integer coefficient triple therefore gives a unique min-zero **carrier displacement normal form**. This theorem is permitted only as carrier representation/decoding mathematics.

Freeze:

`CARRIER_MIN_ZERO_NORMAL_FORM != NATIVE_ABSOLUTE_ADDRESS_DERIVATION`.

`CARRIER_DIAGONAL_KERNEL != NATIVE_DIAGONAL_EQUIVALENCE`.

Cell centers carry the declared integer addresses in this sector atlas. Because the geometric origin is a triple-intersection vertex rather than a center, the center lattice is an affine carrier relative to the origin; integer address does not mean that a center lies on a number axis.

## 4. Cell radius

Every circle cell has the same carrier radius

`R_CELL = 1/sqrt(3)`.

Freeze:

`ENTERPRISE_CELL_RADIUS = 1/sqrt(3)`.

With nearest center spacing 1, this is the critical radius at which the three cells centered at the vertices of every elementary unit center triangle meet at one common boundary point.

## 5. Pairwise overlap and exact triple intersections

For neighboring centers,

`D_CENTER = 1 < 2/sqrt(3)`.

Therefore neighboring circle cells overlap with positive area.

Freeze:

`NEIGHBORING_CELLS_OVERLAP_WITH_POSITIVE_AREA`.

At `R_CELL=1/sqrt(3)`, every elementary three-center triangle has one common triple boundary-intersection point. The next nonzero center separation is too large for non-neighbor circles to intersect. Hence every circle-boundary crossing in the carrier occurs as a three-cell intersection rather than as an isolated two-cell crossing.

Freeze:

`EVERY_CELL_BOUNDARY_INTERSECTION_IS_TRIPLE`.

## 6. Gap-free dense-discrete cover

At nearest center spacing 1, radius `1/sqrt(3)` is exactly the covering threshold of this triangular center carrier. Therefore

`UNION_ALL_ENTERPRISE_CELLS = ENTERPRISE_PLANE`.

Freeze:

`NO_GEOMETRIC_GAPS_BETWEEN_CELLS`.

`DENSE_DISCRETE = DISCRETE_INTEGER_CENTER_ADDRESSES + GAP_FREE_OVERLAPPING_CIRCLE_CELLS`.

At the critical radius, three neighboring cells have a common set consisting of a single triple-intersection point rather than a positive-area three-cell overlap region.

## 7. Native right angle is 120 degrees

This is the highest angular correction.

The three positive native axes divide one full turn into three equal sectors. Each sector has carrier opening `120 degrees`, and this is the native Enterprise right angle.

Freeze:

`ENTERPRISE_RIGHT_ANGLE = 120_DEGREES`.

Equivalently:

`E_1 PERP_E E_2`,

`E_2 PERP_E E_3`,

`E_3 PERP_E E_1`,

where `PERP_E` is Enterprise orthogonality, not classical Euclidean orthogonality of the carrier drawing.

Thus the Enterprise plane has three native right sectors per full turn rather than four classical 90-degree quadrants.

The three native number axes remain the three positive rays from `O_E`, parallel in the carrier presentation to the three center-center direction families. Their ticks are

`0,1,2,3,...`

at native unit spacing.

Freeze:

`NATIVE_AXIS_TICKS_ARE_NONNEGATIVE_INTEGERS`.

`NATIVE_AXIS_UNIT_LENGTH = 1`.

`NATIVE_NUMBER_AXIS_NEVER_PASSES_THROUGH_CELL_CENTER`.

The orientation-torsor refoundation in Section 2 does not derive this `120 degree` native-right-angle declaration.

## 8. Native sector scalar: axis calibration + transverse independence

Inside each native right sector, let

`Q_ij = L_E^2`

be the scalar on the two active nonnegative integer coordinates of sector `S_ij`.

The current sector scalar primitive is factored into two independent pieces.

### Primitive A — one-dimensional square calibration

Along either active native axis,

`Q_ij(n,0)=n^2`,

`Q_ij(0,n)=n^2`,

for every `n in N_0`.

Freeze:

`NATIVE_AXIS_SCALAR_CALIBRATION = n^2`.

### Primitive B — local transverse scalar independence

For every elementary plaquette of the two-channel sector,

`Q_ij(a+1,b+1)-Q_ij(a+1,b)-Q_ij(a,b+1)+Q_ij(a,b)=0`.

Equivalently, the marginal scalar increment of one active channel is invariant under the transverse channel background.

Freeze:

`NATIVE_SECTOR_TRANSVERSE_INTERACTION = 0`.

`TRANSVERSE_INDEPENDENCE_IS_SECTOR_PRODUCT_RELATIVE`.

This is not invariant under arbitrary channel-mixing coordinate transformations. The current native sectors already preserve the two active channel foliations; no stronger coordinate-free claim is made.

### Derived theorem — sector sum of squares

On a connected two-channel sector, zero mixed second difference implies additive separation. Combining that theorem with the two axis calibrations gives:

For `P=(a,b,0)` in `S_12`,

`L_E(P)^2 = a^2+b^2`.

For `P=(0,b,c)` in `S_23`,

`L_E(P)^2 = b^2+c^2`.

For `P=(a,0,c)` in `S_31`,

`L_E(P)^2 = a^2+c^2`.

Because every canonical native address has at least one zero component, these three cases combine into

`L_E(a,b,c)^2 = a^2+b^2+c^2`, for `min(a,b,c)=0`.

Freeze:

`NATIVE_SECTOR_SUM_OF_SQUARES = DERIVED_THEOREM`.

`NATIVE_ORIGIN_LENGTH_SQUARED = a^2+b^2+c^2` for canonical sector addresses.

Example:

`(3,4,0)` lies in the native right sector `S_12` and has

`L_E(3,4,0)=5`.

Thus the classical integer triple `3,4,5` maps directly into the Enterprise plane, but its right angle is the native `120 degree` angle between the two positive sector axes.

The former carrier-induced quadratic form

`a^2+b^2+c^2-ab-bc-ca`

is superseded as the **native Enterprise metric**. It may still describe distances in a classical planar carrier presentation, but it does not define Enterprise length or Enterprise orthogonality.

Freeze:

`CARRIER_EUCLIDEAN_LENGTH != NATIVE_ENTERPRISE_LENGTH`.

## 9. Global distance and chart transition status

The origin-based native norm in each sector is fixed by the derived sum-of-squares theorem above from the accepted sector primitives.

For arbitrary point-to-point displacement across different sectors, do not reintroduce the deleted diagonal-shift quotient and do not automatically subtract global three-component coordinates as though the three sectors formed one linear Euclidean basis.

Freeze:

`CROSS_SECTOR_POINT_TO_POINT_METRIC = REQUIRES_EXPLICIT_NATIVE_CHART_TRANSITION`.

This is the next metric/gluing question; it does not alter the sector-local sum-of-squares theorem.

## 10. Discrete cell-state principle

The instantaneous geometric state remains one circle cell identified by one cell-center address.

Freeze:

`ROTATING_SEGMENT_NATIVE_STATE = ONE_CIRCLE_CELL_PER_TRAJECTORY_STEP`.

Triple-intersection vertices are transition/incidence events between cells, not simultaneous multi-cell states.

If several cell trajectories are admissible, retain multiple single-cell trajectories rather than a multi-cell instantaneous state.

## 11. Superseded metric/address claims

Superseded as current native foundation:

- signed-origin-one / no-native-zero ontology;
- origin-circle ontology;
- first cell radius = 1;
- tangent close packing;
- gap-center origin;
- three bisector-axis lines / six signed native axes;
- `e_1+e_2+e_3=0` as a native vector identity;
- `-e_1=e_2+e_3` and cyclic variants as native vector identities;
- `(a,b,c)~(a+k,b+k,c+k)` as native coordinate equivalence;
- the claim that the three native 120-degree axis pairs are not Enterprise-orthogonal;
- native metric `a^2+b^2+c^2-ab-bc-ca`;
- using classical carrier angle to decide native Pythagorean orthogonality;
- treating the global sector formula `a^2+b^2` as the sole primitive scalar statement rather than the derived consequence of axis calibration plus transverse independence;
- treating the carrier diagonal kernel/min-zero displacement normal form as an absolute native address quotient or derivation.

## 12. Canonical summary

Freeze:

`ORIGIN = 0 = TRIPLE CELL INTERSECTION`.

`CELL = CIRCLE WITH INTEGER-ADDRESSED CENTER`.

`NEAREST CENTER SPACING = 1`.

`CELL RADIUS = 1/sqrt(3)`.

`NEIGHBOR CELLS OVERLAP`.

`ALL CELLS COVER THE PLANE WITHOUT GAPS`.

`ORIGIN-INCIDENT CELL CENTERS = UNORDERED ELEMENTARY TRIANGLE T`.

`NATIVE CHIRAL DATUM = ONE ELEMENT o OF Or(T) ~= C2`.

`THREE POSITIVE DIRECTION FAMILIES = DERIVED FROM (T,o) + CARRIER TRANSLATION`.

`ABSOLUTE AXIS LABELS = CYCLIC GAUGE; Aut(T,o)=A3 ~= C3`.

`THREE POSITIVE AXES CUT THE PLANE INTO THREE 120-DEGREE NATIVE RIGHT SECTORS`.

`ENTERPRISE RIGHT ANGLE = 120 DEGREES`.

`THREE-COORDINATE ADDRESS = PRIMITIVE GLUED TWO-AXIS SECTOR ATTACHMENT, NOT DIAGONAL-SHIFT QUOTIENT`.

`CARRIER MIN-ZERO NORMAL FORM != ABSOLUTE NATIVE ADDRESS DERIVATION`.

`CELL CENTERS HAVE NONNEGATIVE INTEGER SECTOR ADDRESSES`.

`NATIVE AXIS SCALAR CALIBRATION = n^2`.

`NATIVE SECTOR TRANSVERSE INTERACTION = 0`.

`NATIVE SECTOR SUM-OF-SQUARES = DERIVED`.

`(3,4,0) HAS NATIVE LENGTH 5`.
