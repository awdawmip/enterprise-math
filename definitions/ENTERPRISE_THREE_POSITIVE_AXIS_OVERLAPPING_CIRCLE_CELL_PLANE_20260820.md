# 进取平面重基：三正轴整数圆心格、半径 1/sqrt(3) 的重叠圆 Cell 覆盖

Status: `ACTIVE / CANONICAL / FOUNDATIONAL_SUPERSESSION`
Date: `2026-08-20`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

This file supersedes the 2026-08-18 triple-intersection draft where the first cell radius and origin-to-center distance were both normalized to 1 and the native axes were described as bisectors. The current construction instead normalizes nearest-neighbor cell-center spacing to 1, takes every circle-cell radius to be `1/sqrt(3)`, and uses three positive native axes parallel to the three nearest-neighbor center-center directions.

## 1. Native origin and object types

The native Enterprise plane origin is

`O_E = 0`.

Freeze:

`ENTERPRISE_NATIVE_ORIGIN = 0`.

Every native cell is a circle/disk carrier with a distinguished center.

Freeze:

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

## 2. Integer center lattice and primitive spacing

Cell centers form a planar triangular lattice. Normalize nearest-neighbor center spacing to

`D_CENTER = 1`.

Freeze:

`NEAREST_CELL_CENTER_DISTANCE = 1`.

Let `e_1,e_2,e_3` be the three positive primitive center-lattice directions, each of length 1, separated pairwise by 120 degrees and satisfying

`e_1 + e_2 + e_3 = 0`.

The full six geometric neighbor directions are obtained from the three positive directions because

`-e_1 = e_2+e_3`,

`-e_2 = e_3+e_1`,

`-e_3 = e_1+e_2`.

No native negative axis is required.

Freeze:

`ENTERPRISE_NATIVE_AXES = THREE_POSITIVE_AXES`.

`ENTERPRISE_PRIMITIVE_AXIS_DIRECTIONS = {e_1,e_2,e_3}`.

`NO_NATIVE_NEGATIVE_AXES_REQUIRED`.

## 3. Nonnegative integer three-axis addressing

Use nonnegative integer triples as algebraic addresses:

`(a,b,c) in N_0^3`.

Because `e_1+e_2+e_3=0`, addresses are equivalent under common diagonal shift:

`(a,b,c) ~ (a+k,b+k,c+k)`.

Choose the canonical representative by

`min(a,b,c)=0`.

Thus the native three-axis address space is

`A_E = { (a,b,c) in N_0^3 : min(a,b,c)=0 }`.

This stores all directions without negative coordinates.

Examples of the six unit geometric directions in canonical nonnegative form:

- `+e_1 = (1,0,0)`;
- `+e_2 = (0,1,0)`;
- `+e_3 = (0,0,1)`;
- `-e_1 = (0,1,1)`;
- `-e_2 = (1,0,1)`;
- `-e_3 = (1,1,0)`.

Cell centers carry integer lattice addresses. Because the geometric origin is a triple-intersection vertex rather than a center, the center lattice is an affine coset relative to the origin. Therefore distinguish:

`INTEGER_CELL_ADDRESS != CLAIM_THAT_CELL_CENTER_LIES_ON_A_NATIVE_AXIS`.

A fixed affine embedding maps integer cell addresses to their circle centers.

## 4. Cell radius

Every circle cell has the same radius

`R_CELL = 1/sqrt(3)`.

Freeze:

`ENTERPRISE_CELL_RADIUS = 1/sqrt(3)`.

This value is forced by the normalization `D_CENTER=1` together with the requirement that the three cells centered at the vertices of every elementary unit equilateral triangle meet at its circumcenter.

For an equilateral triangle of side 1, the circumradius is exactly

`1/sqrt(3)`.

Hence every elementary center triangle determines one triple cell-intersection vertex.

## 5. Pairwise overlap and exact triple intersections

For neighboring centers `C_i,C_j`,

`dist(C_i,C_j)=1 < 2/sqrt(3)`.

Therefore neighboring circle cells overlap with positive area.

Freeze:

`NEIGHBORING_CELLS_OVERLAP_WITH_POSITIVE_AREA`.

The next possible nonzero center distance in the triangular lattice is `sqrt(3)`, and

`sqrt(3) > 2/sqrt(3)`.

Therefore only nearest-neighbor circle cells intersect.

Each nearest-neighbor pair belongs to exactly two elementary unit equilateral center triangles, one on each side of the shared center-center edge. Their two circle-boundary intersection points are precisely the two circumcenters of those triangles. At each such point a unique third neighboring circle cell also passes through the point.

Thus every circle-boundary intersection is a triple intersection:

`EVERY_CELL_BOUNDARY_INTERSECTION_IS_TRIPLE`.

No four-cell boundary intersection occurs in the generic lattice geometry.

## 6. Gap-free dense-discrete cover

The triangular lattice with nearest-neighbor spacing 1 has covering radius exactly `1/sqrt(3)`.

Since `R_CELL=1/sqrt(3)`, the union of all circle cells covers the entire plane:

`UNION_ALL_ENTERPRISE_CELLS = ENTERPRISE_PLANE`.

There are no uncovered void/gap regions.

Freeze:

`NO_GEOMETRIC_GAPS_BETWEEN_CELLS`.

`DENSE_DISCRETE` is to be understood here as:

`DISCRETE_INTEGER_CENTER_LATTICE + GAP_FREE_OVERLAPPING_CELL_COVER`.

It does not mean that the set of cell centers is topologically dense.

At the critical radius `1/sqrt(3)`, three neighboring cells have a common set consisting of a single triple-intersection point rather than a positive-area triple-overlap region.

## 7. Three positive number axes

The three native number axes are the three positive rays from `O_E` parallel to the three families of nearest-neighbor center-center lines.

They are not the center rays and not the angular bisectors used in the superseded 2026-08-18 draft.

Freeze:

`NATIVE_NUMBER_AXES_ARE_PARALLEL_TO_CENTER_CENTER_DIRECTIONS`.

`NATIVE_NUMBER_AXES = THREE_POSITIVE_RAYS_FROM_ORIGIN`.

The three positive axis directions are separated by 120 degrees and satisfy the same relation

`e_1+e_2+e_3=0`.

The axes pass through the same-orientation sublattice of triple-intersection vertices at unit spacing:

`0,1,2,3,...`.

Freeze:

`NATIVE_AXIS_TICKS_ARE_NONNEGATIVE_INTEGERS`.

`NATIVE_AXIS_UNIT_LENGTH = 1`.

Because the origin is a triangle circumcenter and the axes are parallel to center-center lines, these axis rays do not pass through cell centers.

Freeze:

`NATIVE_NUMBER_AXIS_NEVER_PASSES_THROUGH_CELL_CENTER`.

## 8. Native three-axis metric

The native three axes are not pairwise orthogonal. Their Gram relations are

`||e_i||^2 = 1`,

`<e_i,e_j> = -1/2` for `i != j`.

Therefore for a displacement represented by any triple `(a,b,c)` modulo common diagonal shift,

`V = a e_1 + b e_2 + c e_3`,

the native squared length is

`Q_E(a,b,c) = a^2+b^2+c^2-ab-bc-ca`.

Equivalently,

`Q_E(a,b,c) = 1/2 * ((a-b)^2 + (b-c)^2 + (c-a)^2)`.

This quadratic form is invariant under

`(a,b,c) -> (a+k,b+k,c+k)`.

Freeze:

`NATIVE_THREE_AXIS_LENGTH_SQUARED = a^2+b^2+c^2-ab-bc-ca`.

`NATIVE_THREE_AXIS_LENGTH = sqrt(Q_E)`.

This supersedes direct use of `sqrt(a^2+b^2+c^2)` on native three-axis addresses. The ordinary square-sum-root formula remains applicable only to separately chosen pairwise-orthogonal components.

For two cell-center integer addresses `P,Q`, compute the raw address difference, add a common diagonal shift if desired to restore a nonnegative canonical representative, and evaluate the same `Q_E`; common diagonal normalization does not change the length.

## 9. Discrete cell-state principle

The instantaneous geometric state remains one circle cell identified by one cell-center address.

Freeze:

`ROTATING_SEGMENT_NATIVE_STATE = ONE_CIRCLE_CELL_PER_TRAJECTORY_STEP`.

Triple-intersection vertices are transition/incidence events between cells, not simultaneous multi-cell states.

If several cell trajectories are admissible, retain multiple single-cell trajectories rather than a multi-cell instantaneous state.

## 10. Superseded coordinate foundations

Superseded as current native foundation:

- signed-origin-one / no-native-zero ontology;
- origin-circle ontology;
- first cell radius = 1;
- origin-to-first-center distance = 1;
- tangent close packing;
- gap-center origin;
- three bisector-axis lines / six signed native axes;
- treating the three native axes as pairwise orthogonal components;
- direct native-axis norm `sqrt(a^2+b^2+c^2)`.

Historical computations remain archived and require explicit retyping before reuse.

## 11. Canonical summary

Freeze:

`ORIGIN = 0 = TRIPLE CELL INTERSECTION`.

`CELL = CIRCLE WITH INTEGER-ADDRESSED CENTER`.

`NEAREST CENTER SPACING = 1`.

`CELL RADIUS = 1/sqrt(3)`.

`NEIGHBOR CELLS OVERLAP`.

`EVERY BOUNDARY INTERSECTION IS A THREE-CELL INTERSECTION`.

`ALL CELLS TOGETHER COVER THE PLANE WITHOUT GAPS`.

`THREE POSITIVE AXES ONLY`.

`AXES ARE PARALLEL TO CENTER-CENTER DIRECTIONS`.

`AXIS TICKS ARE 0,1,2,... WITH UNIT SPACING`.

`CELL CENTERS HAVE INTEGER ADDRESSES`.

`NONNEGATIVE THREE-AXIS ADDRESSES ARE CANONICALIZED BY min(a,b,c)=0`.

`NATIVE LENGTH^2 = a^2+b^2+c^2-ab-bc-ca`.
