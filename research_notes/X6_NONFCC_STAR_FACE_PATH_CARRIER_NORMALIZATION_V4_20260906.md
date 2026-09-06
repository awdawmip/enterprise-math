# X6 non-FCC carrier V4: STAR/FACE/PATH rank classification and A6 rotation-normalized realization

Status: `FREE_RESEARCH / EXACT CARRIER CLASSIFICATION + NORMALIZATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NONFCC-SLICE-REALIZATION`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`;
- intrinsic signed-C6/C12 realization on all 20 three-axis selections;
- `X6_ORIENTATION_PRESERVING_CHART_A6_UNIFICATION_V3_20260906.md`.
Checker: `experiments/x6_nonfcc_carrier_v4_20260906/check_nonfcc_carrier_classification.py`.

## 1. Question and strength split

All `C(6,3)=20` native three-axis coordinate selections already have intrinsic signed-X6 C6/C12 Cell-path dynamics. Only four K4 STAR selections have the currently frozen FCC triangular/circle carrier realization.

The open question has two different strengths:

1. **direct fixed-FCC realization**: keep the global FCC line-family assignment fixed and ask whether the selected three line families themselves form the existing planar 120-degree triangular carrier;
2. **rotation-normalized realization**: first apply an allowed native orientation-preserving frame transport that sends the selected chart to a STAR chart, then use the established STAR FCC carrier readout.

These are not equivalent and must not be conflated.

## 2. Fixed FCC six-line representatives

Use K4 edge labels

`AB, AC, AD, BC, BD, CD`

for the six FCC nearest-neighbor line families, with one convenient unoriented carrier representative set

`AB=(1,1,0)`,
`AC=(1,0,1)`,
`AD=(0,1,-1)`,
`BC=(0,1,1)`,
`BD=(1,0,-1)`,
`CD=(1,-1,0)`.

Every vector has carrier Euclidean squared norm 2. Sign changes only select the opposite ray of the same carrier line family; they do not create a native negative-axis identity.

This carrier Euclidean Gram data is an implementation/readout object, not the native Enterprise metric. Native selected axes remain pairwise `PERP_E` with 120-degree Enterprise right angle by P000 regardless of the following carrier classification.

## 3. The 20 triples have exactly three K4 combinatorial types

A three-edge subset of K4 has exactly one of three degree patterns:

- `STAR`: `(3,1,1,1)` — three edges incident to one vertex;
- `FACE`: `(2,2,2,0)` — a K4 triangle face;
- `PATH`: `(2,2,1,1)` — a three-edge spanning path.

Counts are exactly

`4 STAR + 4 FACE + 12 PATH = 20`.

The established FCC/K4 `S4` atlas preserves these three types and has exactly these orbit sizes.

## 4. Exact fixed-carrier rank theorem

For a selected triple `S`, let `M_S` be the 3x3 matrix whose columns are the three fixed FCC line-family representatives and let

`G_S=M_S^T M_S`.

Exhaustive exact calculation gives:

### STAR

For all 4 STAR triples:

`rank(M_S)=2`,

`det(G_S)=0`.

There are exactly two simultaneous ray-orientation choices giving

`v_i dot v_j = -1`

for all three pairs. Since `||v_i||^2=2`, this is pairwise carrier Euclidean 120 degrees. The two choices differ by reversing all three carrier rays.

Thus the STAR triples are exactly the fixed FCC triples realizing the existing planar triangular 120-degree carrier.

### FACE

For all 4 FACE triples:

`rank(M_S)=3`,

`det(G_S)=4`.

All three pairwise carrier dots are nonzero `+/-1`. Their product is always `+1`.

Changing carrier ray signs multiplies the three pairwise dots by factors whose total product is 1, so this product sign is invariant. But three simultaneous 120-degree pairwise dots would have product

`(-1)^3=-1`.

Therefore no ray orientation makes a FACE triple pairwise carrier-120.

### PATH

For all 12 PATH triples:

`rank(M_S)=3`,

`det(G_S)=4`.

Each PATH contains one pair of opposite/disjoint K4 edges. The corresponding FCC carrier line representatives have dot product 0. Sign changes cannot alter zero.

Therefore no PATH triple can be pairwise carrier-120 under the fixed global FCC line-family realization.

Hence:

`DIRECT_FIXED_FCC_TRIANGULAR_120_REALIZATION <=> CHART_TYPE=STAR`.

Exactly 4 of 20 charts satisfy it.

## 5. What the no-go does and does not say

The 16 FACE/PATH selections are **not** carrierless and are not invalid native slices.

They have:

- exact native X6 coordinate meaning;
- intrinsic signed-C6/C12 Cell-path rotation realization;
- a perfectly valid fixed global FCC line-family readout;
- rank-3 rather than rank-2 FCC carrier geometry.

The no-go says only that they cannot reuse the existing **planar triangular overlapping-circle STAR carrier semantics without changing frame/readout**.

In particular, carrier rank 3 does not imply native dimension 3 and carrier Euclidean 90/60/120 angles do not redefine P000 native orthogonality.

## 6. A6 transitivity gives a positive rotation-normalized realization

The current all-20 chart theorem gives the orientation-preserving positive-axis transport group `A6`, order 360.

`A6` acts transitively on the 20 three-axis subsets. Fix one reference STAR chart, for example

`S_*={AB,AC,AD}`.

For every chart `S` there exists `g in A6` with

`g(S)=S_*`.

Therefore every native three-axis chart admits the typed composite observer

`native chart S`

`-- A6 frame transport g -->`

`reference STAR chart S_*`

`-- established FCC STAR readout -->`

`triangular 120-degree/circle carrier`.

Call this an **A6 rotation-normalized STAR carrier realization**.

It is a rotated/readout realization, not evidence that the original fixed FCC line families of a FACE/PATH chart were already coplanar STAR lines.

## 7. Exact normalization ambiguity

For a fixed source chart `S` and fixed target STAR set `S_*`, the number of even axis permutations satisfying

`g(S)=S_*`

is

`|Stab_{A6}(S_*)| = 360/20 = 18`.

Thus an unoriented chart-to-STAR normalization has an 18-element frame fiber.

If the chart retains one of its two cyclic orientations and the target STAR cyclic orientation is fixed, the number of compatible A6 lifts is

`360/40 = 9`.

If the three visible source axes are matched to the three target STAR slots individually, only the hidden complement can vary. Exactly three A6 lifts remain.

So the hierarchy is

`unoriented selected set: 18 lifts`,

`cyclically oriented chart: 9 lifts`,

`fully ordered visible slots: 3 lifts`.

The final 3-fold residual acts only on the hidden complementary axes from the current local observer's perspective, but it may be visible to later full-frame operations.

## 8. Connection with chart-path holonomy

The all-20 even-lift chart connection gives one constructive way to choose a normalizing `g`: pick a path in the Johnson graph `J(6,3)` from `S` to `S_*` and multiply its even chart lifts.

The connection is not globally flat. Four-axis chart triangles carry nontrivial double-transposition A6 holonomy.

Therefore different normalization paths can produce different members of the 18/9/3 lift fiber even when the local source and target charts agree.

This is not a bug. It is exactly the frame/provenance information that a local carrier observer erases.

Consequently:

`LOCAL_ROTATION_NORMALIZED_FCC_READOUT != FULL_A6_FRAME_STATE`.

Any future operation that depends on full frame transport must retain the chosen A6 lift or equivalent holonomy memory.

## 9. Relation between S4 and A6

The K4/FCC atlas-preserving subgroup `S4` acts on the six K4 edges by even permutations and lies inside `A6`.

Under this `S4`, the 20 charts split into the carrier-type orbits

`4 STAR + 4 FACE + 12 PATH`.

Under full orientation-preserving native chart transport `A6`, all 20 charts lie in one orbit.

Thus STAR/FACE/PATH is a property of the **fixed FCC carrier frame**, not an intrinsic partition of native X6 three-axis charts.

This precisely explains why a native A6 rotation can carry a non-STAR chart to a STAR carrier chart without contradiction.

## 10. Current non-FCC task closure

Closed at this stage:

- all 20 native three-axis selections already have intrinsic signed-C6/C12 Cell-path realization;
- exact fixed-FCC carrier classification `4 STAR / 4 FACE / 12 PATH`;
- STAR iff rank-2 and directly orientable as the existing carrier 120-degree triangle;
- FACE/PATH fixed-FCC rank-3 obstructions;
- positive A6 rotation-normalized STAR carrier realization for every chart;
- exact 18/9/3 normalization-lift ambiguity;
- interpretation of route dependence as A6 chart holonomy.

Remaining carrier questions are now narrower:

1. whether FACE/PATH rank-3 fixed-FCC configurations have useful native-calibrated carrier semantics of their own rather than merely normalized STAR readouts;
2. whether a physical law selects a canonical A6 normalization path/frame or keeps the holonomy as state;
3. how the circle/gate footprint should be transported through the normalization without mistyping it as native Cell identity;
4. application-specific observer safety when collapsing the 18/9/3 lift fibers.

No Foundation promotion or external novelty claim is made.
