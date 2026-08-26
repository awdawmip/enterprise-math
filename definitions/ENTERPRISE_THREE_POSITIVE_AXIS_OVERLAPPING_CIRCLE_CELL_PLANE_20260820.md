# 进取平面重基：三正轴整数圆心格、半径 1/sqrt(3) 的重叠圆 Cell 覆盖

Status: `ACTIVE / CANONICAL / FOUNDATIONAL_CORRECTION`
Date: `2026-08-20`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

This file is the corrected current foundation. It keeps the three-positive-axis overlapping circle-cell carrier with nearest center spacing 1 and cell radius `1/sqrt(3)`, but corrects the native angular/metric semantics: in Enterprise geometry the `120 degree` sector between adjacent positive axes is the native right angle. Therefore the former Euclidean-carrier quadratic form `a^2+b^2+c^2-ab-bc-ca` is not the native Enterprise Pythagorean metric.

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

## 2. Integer center carrier and three positive directions

Cell centers form the same gap-free triangular carrier arrangement. Normalize nearest-neighbor center spacing to

`D_CENTER = 1`.

Freeze:

`NEAREST_CELL_CENTER_DISTANCE = 1`.

Let the three positive native axis rays be `E_1,E_2,E_3`. In the planar carrier presentation their directions occur successively at `120 degree` separation.

The earlier statement

`e_1+e_2+e_3=0`

was a relation of a classical planar vector presentation of the three carrier directions. It is **not** a native Enterprise vector identity and must not be used to define native length, opposite directions, or primitive native-point coordinate equivalence.

Freeze:

`CARRIER_DIRECTION_RELATION != NATIVE_VECTOR_RELATION`.

`NO_PRIMITIVE_NATIVE_POINT_DIAGONAL_SHIFT_QUOTIENT`.

This prohibition is typed at the primitive native point/address layer. It does not prohibit the separately typed derived G1 endpoint/displacement quotient frozen in `ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md`.

No native negative axes are required. The three positive rays themselves partition the plane into three native sectors.

Freeze:

`ENTERPRISE_NATIVE_AXES = THREE_POSITIVE_RAYS`.

`NO_NATIVE_NEGATIVE_AXES_REQUIRED`.

## 3. Three positive integer coordinates are sector coordinates

Use nonnegative integer triples

`(a,b,c) in N_0^3`

with canonical condition

`min(a,b,c)=0`.

At the primitive native point/address layer, this is **not** a quotient by common diagonal shift. It is a sector typing rule.

The separately typed derived displacement section `A_D` uses the same underlying min-zero tuple set as a representation, but this representation-level coincidence does not identify the semantic types `A_D` and `A_E`.

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

`(a,b,c) IS_NOT_EQUIVALENT_TO (a+k,b+k,c+k) AS_PRIMITIVE_NATIVE_POINT_ADDRESS`.

`A_E != A_D AS_SEMANTIC_TYPES`.

Cell centers carry integer addresses in this sector atlas. Because the geometric origin is a triple-intersection vertex rather than a center, the center lattice is an affine carrier relative to the origin; integer address does not mean that a center lies on a number axis.

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

## 8. Native Pythagorean metric

Inside each native right sector, the two bounding positive axes are Enterprise-orthogonal. Therefore the native Pythagorean law is primitive:

For `P=(a,b,0)` in `S_12`,

`L_E(P)^2 = a^2+b^2`.

For `P=(0,b,c)` in `S_23`,

`L_E(P)^2 = b^2+c^2`.

For `P=(a,0,c)` in `S_31`,

`L_E(P)^2 = a^2+c^2`.

Because every canonical native address has at least one zero component, these three cases combine into

`L_E(a,b,c)^2 = a^2+b^2+c^2`, for `min(a,b,c)=0`.

Freeze:

`NATIVE_SECTOR_PYTHAGOREAN_LAW = a^2+b^2` on each active two-axis sector.

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

The origin-based native norm in each sector is now fixed by the Pythagorean law above.

For arbitrary point-to-point displacement across different sectors, do not identify primitive native point addresses by common diagonal shift, and do not use the separately typed derived G1 displacement quotient to infer a global symmetric metric or to subtract primitive three-component point coordinates as though the three sectors formed one linear Euclidean basis.

The current R061 Stage-2 chart transition/decoder may be interpreted through the separately typed derived displacement quotient, but its directed gauge remains the accepted native line gauge and the historical diagonal-invariant quadratic is not restored as native length.

Freeze:

`CROSS_SECTOR_POINT_TO_POINT_METRIC = REQUIRES_EXPLICIT_NATIVE_CHART_TRANSITION`.

`DERIVED_G1_DISPLACEMENT_QUOTIENT != PRIMITIVE_POINT_COORDINATE_QUOTIENT`.

This does not alter the sector-local Pythagorean theorem.

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
- `(a,b,c)~(a+k,b+k,c+k)` as primitive native coordinate equivalence;
- the claim that the three native 120-degree axis pairs are not Enterprise-orthogonal;
- native metric `a^2+b^2+c^2-ab-bc-ca`;
- using classical carrier angle to decide native Pythagorean orthogonality.

The separately typed derived G1 displacement quotient does not revive any item in this superseded primitive/native list.

## 12. Canonical summary

Freeze:

`ORIGIN = 0 = TRIPLE CELL INTERSECTION`.

`CELL = CIRCLE WITH INTEGER-ADDRESSED CENTER`.

`NEAREST CENTER SPACING = 1`.

`CELL RADIUS = 1/sqrt(3)`.

`NEIGHBOR CELLS OVERLAP`.

`ALL CELLS COVER THE PLANE WITHOUT GAPS`.

`THREE POSITIVE AXES ONLY`.

`THREE POSITIVE AXES CUT THE PLANE INTO THREE 120-DEGREE NATIVE RIGHT SECTORS`.

`ENTERPRISE RIGHT ANGLE = 120 DEGREES`.

`THREE-COORDINATE ADDRESS = GLUED TWO-AXIS SECTOR CHART, NOT PRIMITIVE DIAGONAL-SHIFT QUOTIENT`.

`A_E = PRIMITIVE_CURRENT_NATIVE_POINT_OR_SECTOR_ADDRESS_TYPE`.

`A_D = SEPARATELY_TYPED_DERIVED_G1_DISPLACEMENT_SECTION`.

`A_E != A_D AS_SEMANTIC_TYPES`.

`CELL CENTERS HAVE NONNEGATIVE INTEGER SECTOR ADDRESSES`.

`NATIVE PYTHAGOREAN LENGTH^2 = SUM OF SQUARES OF THE TWO ACTIVE AXIS COORDINATES`.

`(3,4,0) HAS NATIVE LENGTH 5`.
