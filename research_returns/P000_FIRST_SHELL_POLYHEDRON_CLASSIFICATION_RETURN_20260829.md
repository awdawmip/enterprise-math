# P000 第一层 Cell 壳层多面体精确分类 — Research Return

Status: `SUCCESS / HARD_TARGET_CLOSED_AT_TYPED_CARRIER_STRENGTH / AWAITING_DRIVER_REVIEW`

Task: `RS-P000-FIRST-SHELL-POLYHEDRON-CLASSIFICATION`  
Publication: `TP2-8BAE9A40F7D298D7AD01`  
Researcher: `EM-P000SHELL-44B349`  
Claim: `chatgpt-p000shell-20260829-1014-c4ae60`

Hard target:

`P000_FIRST_NATIVE_LAYER_POLYHEDRON_AND_READOUTS_EXACTLY_CLASSIFIED`

## Executive conclusion

The candidate sentence “第一层是一个 14 面体” is **too strong and incorrectly typed**.

The exact result is:

1. `L1_NATIVE(c)` is the native adjacency-distance-1 support and is the correct default meaning of “一层”.
2. A declared ideal equal-sphere Barlow carrier gives 12 kissing centers around a carrier center.
3. Their center hull `HULL1` always has `V=12,E=24,F=14` and face multiset `8 triangles + 6 squares`, but there are exactly two local Barlow types:
   - cubic (`ABC/ACB` local stacking): cuboctahedron;
   - hexagonal (`ABA/ACA` local stacking): triangular orthobicupola / anticuboctahedron.
4. These two 14-faced hulls are not combinatorially the same.  Their edge/face incidence signatures are:
   - FCC/cubic: `(TT,TS,SS)=(0,24,0)`;
   - HCP/hexagonal: `(TT,TS,SS)=(3,18,3)`.
5. The center Voronoi cell is a different object.  In the same two Barlow local types it has `V=14,E=24,F=12`:
   - cubic: rhombic dodecahedron, 12 rhombi;
   - hexagonal: trapezo-rhombic dodecahedron, 6 rhombi + 6 isosceles trapezoids.
6. Thus, within ideal Barlow carriers, both
   - `FIRST_NEIGHBOR_CENTER_HULL_HAS_14_FACES`, and
   - `CENTER_VORONOI_CELL_HAS_12_FACES`
   are correct **carrier-level universal face-count statements**, but they describe dual, nonidentical objects and neither is by itself a native P000 theorem.
7. The naive `12 carrier directions / 2 = 6 native axes` inference fails even before native typing: the FCC shell is centrally symmetric and admits six Euclidean antipodal pairs, whereas the HCP shell is not centrally symmetric.  Therefore no Barlow-universal six-pair carrier structure exists.

## 1. Typed definitions

Let `C` be the P000 Cell state space and let `Adj_6` be the declared native adjacency relation when such a relation is part of the active six-dimensional model.

Define

`L1_NATIVE(c) := {x in C : Adj_6(c,x)}`,

or equivalently the graph-distance-one sphere when the native adjacency graph metric has been declared.

This is a native object.  It does not require Euclidean embedding, sphere packing, convexity, negative coordinate axes, or Voronoi geometry.

For a separately typed classical carrier realization `iota` by equal spheres of radius `r`, define the carrier kissing-center shell

`KISS1_iota(c) := {iota(x) : ||iota(x)-iota(c)|| = 2r}`

over the carrier center set in scope.

A statement that `KISS1_iota(c)` is the image of `L1_NATIVE(c)` requires an explicit adjacency/contact bridge.  P000 alone does not provide that bridge.

Define

`HULL1_iota(c) := conv(KISS1_iota(c)-iota(c))`.

This is a classical convex-hull readout.

Define the center Voronoi region

`VOR_iota(c) := {y : ||y-iota(c)|| <= ||y-iota(x)|| for every carrier center x}`.

This is a classical Dirichlet/Voronoi readout.

Therefore the default later meaning of “第一层” should be:

`NATIVE_ADJACENCY_DISTANCE_1`.

`KISS1`, `HULL1`, and `VOR` must be requested and typed explicitly as carrier readouts.

## 2. Exact coordinate certificate

Use integer certificate coordinates `p=(X,Y,Z)` and the Euclidean map

`Phi(X,Y,Z) = (X/2, Y/(2*sqrt(3)), Z*sqrt(6)/3)`.

Then

`12 ||Phi(p)-Phi(q)||^2 = 3 dX^2 + dY^2 + 8 dZ^2`.

Hence all shell-distance and hull-face tests reduce to exact integer arithmetic.

The common basal ring is

`R = {(2,0,0),(1,3,0),(-1,3,0),(-2,0,0),(-1,-3,0),(1,-3,0)}`.

The upper three neighbors are

`U = {(1,1,1),(-1,1,1),(0,-2,1)}`.

For the hexagonal local environment use

`D_h = {(1,1,-1),(-1,1,-1),(0,-2,-1)}`.

For the cubic local environment use

`D_c = {(0,2,-1),(-1,-1,-1),(1,-1,-1)}`.

Every listed point has carrier distance one from the center.

The deterministic checker enumerates every supporting coplanar vertex set, deduplicates maximal facets, recovers hull edges by the exact contact metric, and checks each face metric.

## 3. FCC / cubic local shell

For `R union U union D_c` the exact census is:

- shell vertices / kissing neighbors: `12`;
- hull edges: `24`;
- hull faces: `14`;
- face multiset: `8` equilateral triangles + `6` squares;
- Euler: `12 - 24 + 14 = 2`;
- face-edge incidence: `8*3 + 6*4 = 48 = 2*24`;
- every hull edge is triangle-square: `(TT,TS,SS)=(0,24,0)`;
- the vertex set is centrally symmetric.

This is exactly the cuboctahedron.

The edge-face incidence signature is already a complete separator from the HCP local shell below; no visual naming is used as proof.

## 4. HCP / hexagonal local shell

For `R union U union D_h` the exact census is again:

- shell vertices / kissing neighbors: `12`;
- hull edges: `24`;
- hull faces: `14`;
- face multiset: `8` equilateral triangles + `6` squares;
- Euler: `12 - 24 + 14 = 2`;
- face-edge incidence: `48 = 2*24`.

But the edge-face incidence signature is now

`(TT,TS,SS)=(3,18,3)`.

The shell is therefore not combinatorially equivalent to the cuboctahedron.  It is the triangular orthobicupola, also called the anticuboctahedron or twisted/pseudocuboctahedron in close-packing literature.

It is also not centrally symmetric: for example the negative of `(1,1,1)` is absent from the HCP shell.

So FCC and HCP share the same `f`-vector and the same face-size multiset, but not the same face-incidence structure and not the same Euclidean symmetry.

## 5. Arbitrary Barlow stacking: exact local classification

Let successive close-packed layer positions be labeled `A,B,C`, with consecutive labels unequal.

For a center in the middle layer, only two cases are possible:

1. the two neighboring layer labels are equal, e.g. `ABA`, `ACA`, `BAB`, ...;
   this is the hexagonal local type and gives the triangular orthobicupola;
2. the two neighboring layer labels are different, e.g. `ABC`, `ACB`, `BAC`, ...;
   because both differ from the middle label, they are the two other layer positions;
   this is the cubic local type and gives the cuboctahedron.

Therefore every ideal Barlow packing has exactly two possible first kissing-shell hull types, not a larger stacking-dependent family.

The strongest universal shell statement is:

`BARLOW_KISS1_COUNT = 12`

and

`BARLOW_HULL1_F_VECTOR = (12,24,14)`

with

`BARLOW_HULL1_FACE_MULTISET = 8 TRIANGLES + 6 SQUARES`.

The 14-face count is universal within this declared carrier class, but the polyhedron type is not unique.

## 6. Voronoi distinction and exact dual calculation

With the center at the origin and every kissing vector of unit norm, the 12 nearest-neighbor bisectors are

`v . x <= 1/2`.

In the rational dual coordinate `u = Phi^T x`, these become

`p . u <= 1/2`.

The checker intersects these exact rational halfspaces.  The resulting local Dirichlet cell is polar-dual, up to the fixed scale `1/2`, to the kissing-center hull.

### Cubic/FCC Voronoi cell

Exact census:

- `V=14,E=24,F=12`;
- Euler: `14-24+12=2`;
- face-edge incidence: `12*4=48=2*24`;
- all 12 faces are rhombi.

For every face, exact squared side lengths are

`(3/8,3/8,3/8,3/8)`

and squared diagonals are

`(1/2,1)`.

This is the rhombic dodecahedron.

### Hexagonal/HCP Voronoi cell

Exact census:

- `V=14,E=24,F=12`;
- Euler: `14-24+12=2`;
- face-edge incidence: `48`;
- 6 rhombi with the same metric signature as above;
- 6 isosceles trapezoids.

For every trapezoidal face, the exact sorted squared side lengths are

`(1/6,3/8,3/8,2/3)`,

the two squared diagonals are both

`17/24`,

and exactly one pair of opposite sides is parallel.

This is the trapezo-rhombic dodecahedron (also called the trapezoidal dodecahedron in some close-packing sources).

External source-checks agree with the exact certificate:

- M. Slavíček et al., “Periodic arrangements of closely packed spheres,” *ChemTexts* (2024), DOI `10.1007/s40828-024-00199-8`, describes the two 12-neighbor coordination polyhedra in close-packed stacking: cuboctahedron for cubic local environment and anticuboctahedron for hexagonal local environment, both with `12` vertices, `24` edges, `14` faces, `8` triangles and `6` squares.
- Conway and Sloane, “What Are All the Best Sphere Packings in Low Dimensions?”, *Discrete & Computational Geometry* 13 (1995), describe the two essential local surround types in Barlow packings.
- T. C. Hales and S. P. Ferguson, *The Kepler Conjecture: The Hales-Ferguson Proof* (Springer, 2011), introductory Voronoi-domain discussion, gives the two close-packing Voronoi types: rhombic dodecahedron for local cubic triples and trapezoidal dodecahedron for local hexagonal triples, each with 12 faces and 14 vertices.

The proof strength of this return does not depend on polyhedron-name lookup: the supplied exact checker independently reproduces the finite incidences and face metrics.

## 7. Six-axis P000 boundary

The carrier data do not derive the six native P000 axes.

The typed quantities are different:

- native axis count: fixed by P000 as `6`;
- native first layer: `L1_NATIVE`, determined by the active native adjacency;
- carrier kissing-neighbor count in ideal Barlow realization: `12`;
- carrier Euclidean direction relation: an embedding-dependent relation;
- three visible slice axes: a research-slice object, not a complete six-axis list.

A six-antipodal-pair decomposition exists for the FCC carrier shell because the exact vertex set is centrally symmetric.

It fails for the HCP carrier shell because the exact vertex set is not centrally symmetric.

Therefore even the carrier statement

`12 KISSING DIRECTIONS = 6 OPPOSITE DIRECTION PAIRS`

is not Barlow-universal.

Consequently no implication

`12 carrier neighbors -> 6 native axes`

is licensed.

If a future P000 model supplies a carrier bridge, that bridge must state explicitly what native relation each carrier direction or direction family represents.  Opposite Euclidean rays may not be imported as primitive native negative axes.

## 8. Rotation / shell consequence

For P000 Rubik/rotation/tomography work, the default first support layer should be

`L1_NATIVE(c)`,

not a carrier hull face set and not a Voronoi boundary.

Recommended typed carrier regression data, when a close-packed visualization is intentionally used, are:

`(stacking_local_type, KISS1, HULL1_f_vector, HULL1_face_incidence_signature, VOR_type)`.

In particular:

- `14` hull faces are a Barlow-carrier coarse invariant;
- the hull itself is a visualization/combinatorial control object, not a native invariant without a bridge;
- the incidence signature `(TT,TS,SS)` must be retained because it separates the two Barlow local types despite identical `(V,E,F)` and face-size counts;
- `12` Voronoi faces encode neighbor bisectors, not “twelve faces of the first native layer”;
- native rotation supports should be selected by native adjacency, as already required by the accepted P000 rotation/tomography review.

## 9. Deterministic certificate

Checker:

`scripts/check_p000_first_shell_polyhedron_classification.py`

Certificate:

`research_artifacts/P000_FIRST_SHELL_POLYHEDRON_CLASSIFICATION/exact_certificate_20260829.json`

The checker uses only Python standard-library exact integers and `fractions.Fraction`.

It verifies, independently for FCC and HCP inputs:

- all 12 neighbor radii;
- maximal supporting hull facets;
- exact regular triangle/square face metrics;
- `V,E,F`;
- Euler and face-edge incidence;
- triangle/square edge-adjacency signature;
- central symmetry or its failure;
- rational Voronoi vertices;
- Voronoi dual edges;
- rhombus/trapezoid face metric classification;
- all 12 admissible local Barlow triples and their exact two-type partition.

Local execution of the exact submitted checker completed without assertion failure.

## 10. Hard-target disposition

`SUCCESS`.

The task’s ambiguity is closed at the strongest justified strength:

- no unique classical polyhedron equals `L1_NATIVE`;
- an ideal Barlow carrier has a universal 14-face neighbor-center-hull count but two exact shell types;
- its center Voronoi region has a universal 12-face count but two exact Voronoi types;
- FCC/HCP equality at `V,E,F` level is strictly weaker than polyhedral equivalence;
- the 12-to-6 antipodal pairing is FCC-specific and fails in HCP;
- none of these carrier readouts is promoted to P000 native ontology.

Unresolved residue is deliberately narrow:

`CARRIER_TO_NATIVE_ADJACENCY_AND_AXIS_BRIDGE_NOT_YET_DEFINED`.

That is not a failure of this task; it is the exact boundary preventing an unjustified carrier-to-P000 promotion.

## Method harvest

`RESULT_ONLY`.

The exact finite checker is task-local certification machinery.  No new general Enterprise tool family is claimed; the existing finite-incidence/symmetry ideas are composed rather than promoted.

## Recommended Driver disposition

`ACCEPTED / FOLLOWUP_TASK` if the Driver agrees with the typed boundary.

A justified successor would define or constrain a genuine `L1_NATIVE <-> carrier contact` bridge for one explicit six-dimensional P000 model and test whether any carrier-derived direction relation survives rotation/slice transport.  It should retain both FCC and HCP shells as regression cases, with the HCP non-central-symmetry result as a no-overclaim guard.
