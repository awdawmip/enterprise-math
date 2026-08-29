# P000 Enterprise Geometry — FCC Primary Coordinate Carrier

Status: `ACTIVE / PRIMARY COORDINATE CARRIER CONVENTION / P000-BOUND / USER-DIRECTED DRIVER SELECTION`
Date: `2026-08-29`
Authority: `Driver review DR pending immutable record / direct user criterion = coordinate continuity + rotation`

## 1. Governing selection

Freeze:

`P000_PRIMARY_COORDINATE_CARRIER = FCC_CUBIC_BARLOW`.

`P000_PRIMARY_FIRST_SHELL_CARRIER_HULL = CUBOCTAHEDRON`.

`P000_PRIMARY_CARRIER_VORONOI = RHOMBIC_DODECAHEDRON`.

`HCP_HEXAGONAL_BARLOW = SECONDARY_REGRESSION_CARRIER`.

This is a **carrier coordinate convention downstream of P000**. It does not replace the P000 six-dimensional native ontology with classical three-dimensional FCC space.

## 2. Why FCC is selected

The selection criterion is

`DISCRETE_COORDINATE_CONTINUITY + ROTATION_CLOSURE`.

Here discrete coordinate continuity means that axis-family labels can be transported from Cell to Cell without changing coordinate rules or adding an unobserved stacking/sublattice phase variable.

FCC is selected because:

1. its center set is translation-homogeneous as one Bravais carrier;
2. its first contact shell is centrally symmetric;
3. its 12 contact rays define six stable unoriented carrier line families;
4. the cubic/octahedral rotation symmetry permutes the same line/slice incidence structure;
5. its close-packed triangular sections provide exact carrier `120 degree` three-line charts compatible with the established three-axis Enterprise slice;
6. no `AB` stacking-state bit is needed to keep the coordinate frame consistent under ordinary carrier translations.

HCP remains mathematically valid as a close-packed carrier, but its first shell is not centrally symmetric and its `ABAB...` stacking requires additional layer/basis state for a globally uniform coordinate-frame transport. Therefore it is not the default coordinate carrier.

## 3. Six FCC carrier line families

Use the six unoriented nearest-neighbor line families

`L1=[(1,1,0)]`,

`L2=[(1,-1,0)]`,

`L3=[(1,0,1)]`,

`L4=[(1,0,-1)]`,

`L5=[(0,1,1)]`,

`L6=[(0,1,-1)]`,

where `[v]={v,-v}` is an **unoriented classical carrier line family**.

These are a carrier realization for six native axis labels; they do not derive the native axis count.

Freeze:

`NATIVE_AXIS_COUNT=6` comes from P000.

`FCC_LINE_FAMILY_COUNT=6` is a compatibility property of the selected carrier.

`FCC_LINE_FAMILY_COUNT != DERIVATION_OF_NATIVE_DIMENSION`.

## 4. Four overlapping 120-degree slice charts

At the line-family level the FCC close-packed triangular atlas contains four three-line slice types:

`S_A={L1,L3,L6}`,

`S_B={L1,L4,L5}`,

`S_C={L2,L3,L5}`,

`S_D={L2,L4,L6}`.

For each slice, choose chart-local orientations of its three carrier lines so that their representatives have equal norm, pairwise Euclidean angle `120 degree`, and carrier sum zero.

The chart-local sign is an implementation/readout orientation. It is **not** a primitive native negative axis.

Incidence:

- 4 slice types;
- 3 line families per slice;
- 2 slice incidences per line family;
- `4*3/2=6` unique carrier line families.

This overlapping atlas is preferred to a decomposition into two disconnected three-axis blocks because rotation can transport between overlapping slices while preserving shared axis-family identity.

## 5. Native-to-carrier typing

The native six-dimensional state must remain distinct from its classical carrier readout.

Freeze:

`NATIVE_6D_STATE -> FCC_CARRIER_READOUT`.

`FCC_CARRIER_READOUT_IS_NOT_NATIVE_IDENTITY`.

`CARRIER_DIRECTION_RELATION != NATIVE_VECTOR_RELATION`.

`CARRIER_KERNEL != NATIVE_COORDINATE_EQUIVALENCE`.

`CLASSICAL_CARRIER_DIMENSION != NATIVE_SPATIAL_DIMENSION`.

Therefore classical linear dependence among the six FCC line families cannot reduce P000 from six dimensions.

## 6. Coordinate transport semantics

The default coordinate transport rule is:

`CELL_TRANSLATION -> PRESERVE_GLOBAL_LINE_FAMILY_LABELS`.

`CARRIER_ROTATION -> PERMUTE_LINE_FAMILIES_AND_SLICE_CHARTS`.

`SLICE_SELECTION -> ORIENT_THREE_LOCAL_LINE_REPRESENTATIVES_FOR_120_DEGREE_CHART`.

`OBSERVATION -> READ_SELECTED_SLICE_ONLY`.

The global native positive-axis address calculus and exact bridge `E_i <-> L_j + chart orientation/transition` remain to be completed by the axis-mixing/bridge research route. Until that bridge is proved, do not identify a native positive ray with a Euclidean opposite-pair quotient.

## 7. HCP regression role

HCP is retained as a mandatory regression carrier because its first shell is not centrally symmetric.

Any future theorem that accidentally derives six native axes from `12/2`, assumes every close-packed carrier has six antipodal contact pairs, or erases stacking/basis state must fail the HCP regression.

Freeze:

`HCP_REGRESSION_GUARD = NO_SILENT_12_TO_6_CARRIER_DERIVATION`.

## 8. Research consequence

The current preferred P000 coordinate route is:

`FULL_6D_NATIVE_CELL_STATE`

`-> FCC_SIX_LINE_ROTATIONAL_ATLAS`

`-> ROTATE / TRANSPORT SLICE INCIDENCE`

`-> SELECT 3-AXIS 120-DEGREE SLICE`

`-> OBSERVE`

`-> TIME-ORDER RELATIONAL CHANGE`.

FCC is therefore the default **coordinate carrier**, while P000 remains the native dimensional foundation and rotation remains the primary geometric operation.
