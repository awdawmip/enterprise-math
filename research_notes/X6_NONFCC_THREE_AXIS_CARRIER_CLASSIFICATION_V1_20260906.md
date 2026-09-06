# X6 non-FCC three-axis selections: native realization, FCC no-go, and global Euclidean obstruction

Status: `FREE_RESEARCH / EXACT CLASSIFICATION + NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-NONFCC-SLICE-REALIZATION`
Consumes:
- signed X6 spatial Foundation and centered three-axis subtorsors;
- `X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`;
- current FCC/K4 primary carrier definition.

## 1. Three distinct realization strengths

The 20 choices `S in C({1,...,6},3)` must be separated at three semantic strengths.

### Native X6 strength

Every selection is a signed centered `Z^3` affine subtorsor of X6. The triadic-rotation V1 theorem supplies every one of the 20 selections with:

- an intrinsic signed C6 frame cycle;
- two shortest BRC branches per C6 macro edge;
- an intrinsic OUTER 12-Cell native microcycle.

At this strength all 20 are in one `S6` orbit. There is no native STAR/FACE/PATH distinction.

### Current fixed FCC carrier strength

The current primary FCC carrier fixes six specific unoriented line families and only some 3-subsets can be oriented into an equal-unit Euclidean 120-degree triangular chart.

### Abstract isolated triangular-chart strength

Any native three-axis selection can be relabeled to one reference triangular chart by choosing an `S6` frame. This gives an isolated local carrier template, but not a simultaneous embedding of all six axes into the current FCC line atlas and not a canonical gluing between different selections.

These three strengths must not be conflated.

## 2. K4/FCC labels

Use the established correspondence

- `AB=L1=[(1,1,0)]`;
- `AC=L3=[(1,0,1)]`;
- `AD=L6=[(0,1,-1)]`;
- `BC=L5=[(0,1,1)]`;
- `BD=L4=[(1,0,-1)]`;
- `CD=L2=[(1,-1,0)]`.

Under the FCC-preserving `S4`, the 20 three-edge subsets split by their K4 graph type:

- 4 STAR triples;
- 4 FACE/triangle triples;
- 12 PATH triples.

This orbit split is carrier-atlas structure, not native X6 ontology.

## 3. Sign-gauge criterion for one FCC triple

Choose one representative vector `v_a` for each unoriented FCC line in a three-line set. Every vector has squared norm `2`.

Write

`d_ab = v_a dot v_b`.

A chart-local sign choice `s_a in {+1,-1}` changes the pairwise dot product to

`s_a s_b d_ab`.

To obtain three equal-length Euclidean 120-degree vectors, all three signed pairwise dots must equal `-1`.

The product of the three pairwise dots is sign-gauge invariant because

`(s1 s2)(s2 s3)(s3 s1)=1`.

Therefore a necessary condition is

`d_12 d_23 d_31 = -1`,

with no zero pair.

For the FCC line representatives this condition is also sufficient: solve two sign equations relative to one chosen sign; the invariant product forces the third. Exactly two solutions differ by global reversal.

## 4. Exact FCC classification

Direct exact dot-product classification gives:

### STAR

Every STAR triple has three nonzero raw pairwise dots with product `-1`.

Therefore each STAR admits exactly two chart-local sign gauges (global reversals) in which all pairwise dots are `-1`. Since the signed vectors have norm squared `2`, their Euclidean angles are 120 degrees and their sum is zero.

These are exactly the four already-established FCC triangular slices.

### FACE

Every FACE triple has nonzero pairwise dots whose product is `+1`.

The sign-gauge invariant therefore forbids making all three pairwise dots `-1`.

Example: `{AB,AC,BC}` has raw dots `(1,1,1)`.

Hence none of the four FACE selections is a current-FCC 120-degree triangular chart.

### PATH

Every PATH triple contains at least one pair of carrier vectors with dot product `0`.

A sign flip cannot change zero to `-1`.

Example: `{AB,AC,BD}` has one zero pair.

Hence none of the twelve PATH selections is a current-FCC 120-degree triangular chart.

Therefore:

`CURRENT_FCC_EQUAL_UNIT_120_CHARTS = EXACTLY_THE_4_STAR_SELECTIONS`.

The 16 non-STAR selections retain their native X6 C6/C12 realization but do not inherit the current FCC circle/gate/bisector carrier semantics.

## 5. All 20 admit an abstract isolated triangular template

Fix one reference STAR chart `S0`. For any native three-axis selection `S`, choose a permutation `g in S6` with `g(S)=S0` and transport the abstract triangular chart back along `g`.

Such a `g` always exists because `S6` is transitive on 3-subsets.

For fixed `S` and `S0`, the number of axis permutations mapping `S` to `S0` is

`3! * 3! = 36`:

- any bijection from the three selected axes to `S0`;
- any bijection of the complementary three axes.

Thus the local chart transport has a frame/torsor ambiguity. No one of the 36 choices is canonical from the native 3-subset alone.

This proves local template existence, not a new global carrier embedding.

## 6. Stronger theorem: no single Euclidean six-line carrier can realize all 20 native triads

Suppose, for contradiction, that six fixed unoriented lines in some real inner-product space admit unit representatives `v_1,...,v_6` such that **every** 3-subset can choose local signs making its three vectors pairwise Euclidean 120 degrees.

Every pair belongs to some 3-subset, so

`|v_i dot v_j| = 1/2`

for all `i != j`.

Let

`epsilon_ij = sign(v_i dot v_j) in {+1,-1}`.

For every triangle `{i,j,k}`, local orientability to three negative pairwise inner products forces the sign-gauge invariant

`epsilon_ij epsilon_jk epsilon_ki = -1`.

Choose vertex signs `s_i` using one reference vertex. The triangle condition then gauges every pair simultaneously to

`(s_i v_i) dot (s_j v_j) = -1/2`.

Hence the global Gram matrix would have diagonal `1` and every off-diagonal entry `-1/2`.

But for the all-ones coefficient vector `1=(1,...,1)`,

`1^T G 1 = 6 + 2*C(6,2)*(-1/2) = 6-15 = -9 < 0`.

A real Gram matrix must be positive semidefinite. Contradiction.

Therefore no ordinary real-inner-product carrier with six fixed line identities can realize all 20 native three-axis selections as equal-unit 120-degree triples, regardless of ambient Euclidean dimension.

The obstruction already appears for four or more globally coupled line identities; increasing Euclidean carrier dimension does not cure it.

## 7. Consequence for carrier research

The non-FCC problem cannot be solved by merely finding “a better high-dimensional Euclidean picture” with six fixed vectors and one global inner product.

Possible future routes must instead use at least one of:

- chart-dependent carrier frames/readouts;
- nontrivial transition data between local triangular charts;
- a non-Euclidean/non-single-Gram carrier semantics;
- a richer relational carrier that does not identify native `PERP_E` with one global classical angle matrix.

This conclusion supports, rather than modifies, the existing rule

`NATIVE_ENTERPRISE_ORTHOGONALITY != CARRIER_EUCLIDEAN_ANGLE_RELATION`.

## 8. Circle/gate/overlap typing

The current radius `1/sqrt(3)`, gap-free overlapping circles, triple carrier gates and Viète bisector/gate statements belong to the established FCC STAR carrier charts.

A separately chosen abstract triangular template may reproduce analogous classical formulas locally, but until a bridge/gluing theorem is supplied it must not inherit the identity or authority of the current FCC primary carrier.

Thus for the 16 non-STAR selections:

- native signed Z3 subtorsor: YES;
- intrinsic native C6/C12 path realization: YES;
- isolated abstract triangular chart after choosing a frame: YES;
- current fixed FCC six-line 120 chart: NO;
- current FCC circle/gate/bisector semantics: NO;
- one global ordinary Euclidean six-line carrier realizing all 20: IMPOSSIBLE.

## 9. Current frontier

This substantially closes the original 16-selection question. What remains is not native existence but **global chart gluing**:

1. choose the admissible class of chart-dependent carrier transitions;
2. determine the minimal transition/holonomy data needed to glue local triangular templates;
3. decide whether a richer non-Euclidean carrier is useful or whether local readouts are sufficient;
4. preserve common-depth and path provenance when moving between native and carrier layers.

No Foundation promotion or external novelty claim is made.
