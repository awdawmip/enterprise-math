# P000 Enterprise Geometry — FCC Primary Coordinate Carrier

Status: `ACTIVE / PRIMARY CARRIER READOUT / P000-BOUND / CENTERED-SLICE-ALIGNED`
Original date: `2026-08-29`
Updated: `2026-09-05`
Steward: `EM-STW-C31A7F / FOUNDATION_STEWARD`

## 1. Governing selection

Freeze:

`P000_PRIMARY_COORDINATE_CARRIER = FCC_CUBIC_BARLOW`.

`P000_PRIMARY_FIRST_SHELL_CARRIER_HULL = CUBOCTAHEDRON`.

`P000_PRIMARY_CARRIER_VORONOI = RHOMBIC_DODECAHEDRON`.

`HCP_HEXAGONAL_BARLOW = SECONDARY_REGRESSION_CARRIER`.

This remains a **classical carrier/readout convention downstream of P000 and X6**. It is not native Cell identity and does not reduce the six-dimensional native ontology to classical three-dimensional FCC space.

## 2. Six carrier line families

Use the six unoriented FCC nearest-neighbor line families

`L1=[(1,1,0)]`, `L2=[(1,-1,0)]`,

`L3=[(1,0,1)]`, `L4=[(1,0,-1)]`,

`L5=[(0,1,1)]`, `L6=[(0,1,-1)]`,

where `[v]={v,-v}` is a classical carrier line family.

The count six is a compatibility property, not a derivation of native dimension.

## 3. Four overlapping STAR slice types

The established close-packed triangular STAR atlas is

`S_A={L1,L3,L6}`,

`S_B={L1,L4,L5}`,

`S_C={L2,L3,L5}`,

`S_D={L2,L4,L6}`.

Each carrier line family occurs in two STAR slices, giving

`4*3/2=6`.

Chart-local representatives in one STAR slice can be oriented as equal unit vectors `u_i,u_j,u_k` with pairwise Euclidean `120 degrees` and

`u_i+u_j+u_k=0`.

The chart-local sign is a carrier orientation choice. Native primitive direction typing remains the P000 signed domain `+/-E_a`.

## 4. Centered native slice -> STAR carrier projection

The 2026-09-05 centered-slice rebase closes the **local STAR-slice coordinate bridge**.

For selected native axes `S={i,j,k}` and a chosen native Cell anchor `c_*`, the native slice is

`X_S(c_*) = c_* + Z e_i + Z e_j + Z e_k`

with raw signed coordinate `x in Z^3` and Cell-center zero `(0,0,0)`.

The corresponding STAR carrier-center readout is

`pi_S(x)=x_i u_i+x_j u_j+x_k u_k`.

Since `u_i+u_j+u_k=0`,

`ker(pi_S)=Z*(1,1,1)`.

An exact axial carrier coordinate is

`(x_i-x_k, x_j-x_k)`.

Freeze:

`CENTERED_NATIVE_STAR_SLICE = Z3_SIGNED_CELL_COORDINATES`.

`STAR_CARRIER_CENTER_READOUT = Z3/Z(1,1,1)`.

`STAR_CARRIER_KERNEL != NATIVE_COORDINATE_EQUIVALENCE`.

`MIN_ZERO_TRIPLE = CANONICAL_CARRIER/RELATIVE SECTION`.

`MIN_ZERO_TRIPLE + COMMON_DEPTH = LOSSLESS_NATIVE_SLICE_COORDINATE`.

The local bridge is exact at this coordinate/readout strength. The **complete global bridge** from arbitrary signed X6 states, rotations, all six line families, chart orientations, the sixteen non-STAR coordinate selections, channels and time-dependent carrier data remains open.

## 5. Carrier circle-footprint geometry

On each STAR carrier plane, normalize nearest carrier-center spacing to `1`.

The historical circle construction is retained as a footprint/readout decoration with

`R_CARRIER=1/sqrt(3)`.

At this radius:

- neighboring carrier circles overlap;
- every circle-boundary intersection is a triple incidence;
- the footprint circles cover the classical triangular carrier plane without gaps.

The old triple-boundary point is now typed as a carrier incidence vertex `V_E`, not the native coordinate origin.

Freeze:

`CARRIER_CIRCLE_FOOTPRINT != NATIVE_CELL_IDENTITY`.

`CARRIER_TRIPLE_INCIDENCE_VERTEX != NATIVE_CELL_ZERO`.

`NATIVE_SLICE_ZERO = CHOSEN_CELL_CENTER`.

## 6. Native/carrier metric separation

For raw native slice displacement `x=(a,b,c)`,

`L_E(x)^2=a^2+b^2+c^2`.

The classical STAR carrier Euclidean quadratic is

`Q_car(x)=a^2+b^2+c^2-ab-bc-ca`.

The latter is diagonal-shift invariant; the former is not.

Thus carrier-center identity cannot determine native length without common depth.

Witness:

`(3,4,0)` and `(4,5,1)` have the same carrier center and `Q_car=13`, while their native squared lengths are `25` and `42`.

Freeze:

`CARRIER_EUCLIDEAN_LENGTH != NATIVE_ENTERPRISE_LENGTH`.

`CARRIER_CENTER_EQUALITY != NATIVE_CELL_EQUALITY`.

## 7. Carrier triangle holonomy

For the selected triple let

`H_S=(1,1,1)`.

Then

`pi_S(H_S)=0`

but natively

`H_S!=0`, `L_E(H_S)^2=3`.

Therefore a three-positive-step carrier triangle is a carrier return with hidden native common-depth displacement, not a native Cell return.

Freeze:

`CARRIER_TRIANGLE_RETURN != NATIVE_CELL_RETURN`.

This is a mandatory observer-preservation witness for BRC/path work.

## 8. Coordinate transport and rotation

Current transport pattern:

`NATIVE X6 CELL TRANSLATION -> PRESERVE NATIVE AXIS LABELS`.

`NATIVE/CARRIER ROTATION -> PERMUTE AXIS FAMILIES AND SLICE CHARTS WITH TYPE PRESERVATION`.

`SELECT CENTERED NATIVE Z3 SLICE -> OPTIONAL STAR CARRIER PROJECTION`.

`CARRIER PROJECTION -> RETAIN COMMON DEPTH WHEN FUTURE OPERATIONS REQUIRE NATIVE STATE`.

The exact finite native axis-permutation skeleton is `S6`; the FCC atlas-preserving subgroup remains `S4`.

## 9. HCP regression role

HCP remains a regression carrier. Its noncentral first shell prevents silently deriving native axis count by `12/2` and requires explicit layer/basis state when appropriate.

Freeze:

`HCP_REGRESSION_GUARD = NO_SILENT_12_TO_6_NATIVE_AXIS_DERIVATION`.

## 10. Authority

Local centered STAR-slice coordinate/readout semantics are controlled by

`ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`.

Full native spatial identity remains controlled by

`ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`.

FCC remains the preferred classical carrier/readout, never the native ontology.
