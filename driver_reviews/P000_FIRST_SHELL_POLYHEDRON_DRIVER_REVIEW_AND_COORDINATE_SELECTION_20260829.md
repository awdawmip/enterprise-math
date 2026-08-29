# P000 第一层多面体分类 — Driver Review 与主坐标载体选择

Status: `DRIVER_FINAL / ACCEPTED / FCC_PRIMARY_COORDINATE_CARRIER_SELECTED / HCP_REGRESSION_ONLY / NO_P000_AXIS_DERIVATION`

Result: `RR-73C4AC1CB16F08C64FC4`  
Task: `RS-P000-FIRST-SHELL-POLYHEDRON-CLASSIFICATION`  
Publication: `TP2-8BAE9A40F7D298D7AD01`  
Driver: `EM-DVR-7C31A8`

## 1. Driver verdict

`ACCEPTED`.

The research hard target is closed at the exact strength stated by the return:

`TYPED IDEAL-BARLOW CARRIER CLASSIFICATION`.

The accepted result is:

- native first layer defaults to `L1_NATIVE = native adjacency distance 1`;
- ideal Barlow carrier kissing shell has 12 neighbors;
- carrier neighbor-center hull has `V=12,E=24,F=14`, with two exact local types;
- carrier Voronoi cell has `V=14,E=24,F=12`, also with two exact local types;
- FCC and HCP cannot be identified merely from equal face counts;
- the carrier data do not derive the six native P000 axes.

No classical carrier polyhedron is promoted to P000 ontology by this review.

## 2. Decisive audit

### FCC / cubic local type

Accepted exact shell data:

`HULL1_FCC = cuboctahedron`.

`(V,E,F)=(12,24,14)`.

`FACE_MULTISET = 8 triangles + 6 squares`.

`(TT,TS,SS)=(0,24,0)`.

The shell is centrally symmetric.

Accepted Voronoi readout:

`VOR_FCC = rhombic dodecahedron` with `(V,E,F)=(14,24,12)`.

### HCP / hexagonal local type

Accepted exact shell data:

`HULL1_HCP = triangular orthobicupola / anticuboctahedron`.

`(V,E,F)=(12,24,14)`.

`FACE_MULTISET = 8 triangles + 6 squares`.

`(TT,TS,SS)=(3,18,3)`.

The shell is not centrally symmetric.

Accepted Voronoi readout:

`VOR_HCP = trapezo-rhombic dodecahedron` with `(V,E,F)=(14,24,12)` and `6 rhombi + 6 isosceles trapezoids`.

### Barlow boundary

The 14-face `HULL1` count is universal only in the declared ideal Barlow carrier class. The polyhedron type is not unique. Likewise the 12-face Voronoi count is carrier-level and does not identify the native first layer.

## 3. User-directed coordinate-system selection criterion

The current user direction requires selecting one carrier as the working coordinate system according to:

`COORDINATE_CONTINUITY + ROTATION`.

Because P000 geometry is discrete, `coordinate continuity` is not continuum topology. For this decision it means:

1. **translation-frame continuity** — moving from one Cell center to an adjacent center must permit the same axis-family labels to be transported without introducing a hidden stacking/sublattice phase variable;
2. **slice continuity** — the existing three-axis `120 degree` geometry must occur as a coherent close-packed slice of the chosen carrier and be transportable to neighboring compatible slices;
3. **rotation closure** — repeated legal carrier rotations must act on one fixed finite axis/slice incidence structure rather than changing the coordinate rule itself;
4. **six-axis compatibility** — P000's six native axis labels should admit one stable six-family carrier readout. This is a compatibility criterion only, never a derivation of six dimensions from the carrier.

## 4. Selection: FCC is the primary coordinate carrier

Freeze the project coordinate convention:

`P000_PRIMARY_COORDINATE_CARRIER = FCC_CUBIC_BARLOW`.

`P000_PRIMARY_FIRST_SHELL_CARRIER_HULL = CUBOCTAHEDRON`.

`P000_PRIMARY_CARRIER_VORONOI = RHOMBIC_DODECAHEDRON`.

`HCP_HEXAGONAL_BARLOW = SECONDARY_REGRESSION_CARRIER`.

This is a coordinate/carrier selection downstream of P000. It is not a claim that physical reality is a classical three-dimensional FCC lattice.

### 4.1 Why FCC wins on coordinate continuity

FCC centers form one translation-homogeneous Bravais carrier. A single local nearest-neighbor direction-family labeling can therefore be propagated throughout the carrier by translations without an additional `A/B` layer-state bit.

HCP carries an `ABAB...` stacking phase. Pure translational coordinate transport does not identify the two basis positions without retaining extra sublattice/layer information. For a primary coordinate carrier this is an avoidable frame-state discontinuity.

Therefore:

`FCC_COORDINATE_TRANSPORT_REQUIRES_NO_STACKING_PHASE`.

`HCP_COORDINATE_TRANSPORT_REQUIRES_STACKING/BASIS_STATE`.

### 4.2 Why FCC wins on rotation

The FCC first shell is centrally symmetric. Its 12 carrier contact rays form six stable **unoriented carrier line families**. The orientation-preserving cubic/octahedral rotational symmetry acts on the same shell and permutes these line families without changing the carrier type.

HCP's first shell is not centrally symmetric. Its 12 contact rays do not admit a local Barlow-universal decomposition into six opposite pairs. A six-family coordinate readout based on the local shell would therefore require extra choices that are not preserved by the HCP local geometry itself.

Freeze the typing boundary:

`FCC_SIX_LINE_FAMILIES = CARRIER_COORDINATE_COMPATIBILITY_STRUCTURE`.

`FCC_SIX_LINE_FAMILIES != PROOF_OF_P000_SIX_NATIVE_AXES`.

P000 supplies the six native dimensions independently; FCC is selected because it can carry those six labels continuously and rotationally.

## 5. FCC six-line rotational atlas

A convenient exact integer presentation of the six FCC nearest-neighbor line families is

`L1=[(1,1,0)]`,

`L2=[(1,-1,0)]`,

`L3=[(1,0,1)]`,

`L4=[(1,0,-1)]`,

`L5=[(0,1,1)]`,

`L6=[(0,1,-1)]`,

where `[v]={v,-v}` is an **unoriented classical carrier line family**.

These six families are the six unique lines determined by the 12 FCC first-shell contact rays.

The close-packed triangular carrier has four three-line `120 degree` slice types, represented at the line-family level by

`S_A={L1,L3,L6}`,

`S_B={L1,L4,L5}`,

`S_C={L2,L3,L5}`,

`S_D={L2,L4,L6}`.

For each slice, one can choose chart-local carrier orientations of its three lines so the three vectors have equal norm, pairwise Euclidean angle `120 degree`, and carrier sum zero. The chart-local sign choice is a carrier presentation device; it does **not** create primitive native negative axes.

Combinatorially:

- there are 4 triangular `120 degree` slice types;
- each slice uses 3 carrier line families;
- each line family belongs to exactly 2 slice types;
- hence the incidence count is `4*3/2=6` line families.

This `4 slices / 6 shared axes` incidence is selected as the primary FCC rotational coordinate atlas for subsequent P000 geometry work.

## 6. Coordinate readout boundary

The native spatial state remains six-dimensional. A classical FCC carrier readout may map native axis/path data into a lower-dimensional visual carrier, but the carrier map is not allowed to identify native states merely because their classical readouts coincide.

Freeze:

`NATIVE_6D_STATE -> FCC_CARRIER_READOUT`.

`FCC_CARRIER_READOUT_IS_NOT_NATIVE_IDENTITY`.

`CARRIER_LINEAR_RELATION != NATIVE_VECTOR_RELATION`.

`CARRIER_PROJECTION_DIMENSION != NATIVE_SPATIAL_DIMENSION`.

Therefore no classical relation among the FCC direction vectors may reduce the P000 dimension count.

## 7. Consequence for rotation research

The chosen default route is now:

`6D NATIVE CELL STATE -> FCC SIX-LINE CARRIER ATLAS -> ROTATE/PERMUTE AXIS-SLICE INCIDENCE -> SELECT 3-AXIS 120 DEGREE SLICE -> OBSERVE`.

The current axis-mixing programme should use the FCC carrier as the **default rotational coordinate carrier** while retaining HCP as a mandatory regression case proving that carrier-specific antipodal symmetry must not be confused with P000 native truth.

The next exact unresolved object is the bridge from native positive axes `E_1,...,E_6` to the six FCC carrier line families plus chart-orientation/transition data. That bridge must preserve native typing and must not quotient the six-dimensional native state by the classical carrier kernel.

## 8. Final disposition

`ACCEPTED / FOLLOWUP_TASK`.

The finite first-shell classification is closed. FCC is selected by user-directed Driver decision as the **primary coordinate carrier** because it gives the strongest discrete coordinate continuity and rotation closure. HCP is retained as a secondary regression/contrast carrier.

No derived carrier choice changes or weakens P000.
