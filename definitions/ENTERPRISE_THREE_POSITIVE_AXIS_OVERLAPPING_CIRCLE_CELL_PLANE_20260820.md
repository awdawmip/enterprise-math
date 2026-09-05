# Legacy three-positive-axis overlapping-circle slice — current retyping notice

Status: `SUPERSEDED_AS_NATIVE_SLICE / RETAINED_AS_CARRIER-READOUT PROVENANCE`
Original date: `2026-08-20`
Retyped: `2026-09-05`
Steward: `EM-STW-C31A7F / FOUNDATION_STEWARD`

The original generation at this path treated a three-positive-axis overlapping-circle construction as the primitive native point/Cell geometry, placed the native origin at a triple circle-boundary intersection, and used nonnegative min-zero triples as primitive native addresses.

Those native-coordinate/origin claims are superseded by the direct-user X6 unification:

`definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`.

Current authority is:

`X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)`

and for selected `S={i,j,k}` with chosen Cell anchor `c_*`:

`X_S(c_*) = c_* + Z e_i + Z e_j + Z e_k`.

Therefore the native three-axis slice uses signed raw coordinates `Z^3`, and `(0,0,0)` is the chosen **Cell center** anchor.

## Surviving carrier calculations

The following calculations from the original file remain exact after retyping them as properties of the classical triangular/FCC STAR-slice carrier readout:

- nearest carrier-center spacing `1`;
- circular carrier-footprint radius `1/sqrt(3)`;
- neighboring footprint circles overlap with positive area;
- every footprint-circle boundary intersection is a triple incidence at this radius;
- radius `1/sqrt(3)` is the exact covering radius of the unit triangular center lattice, so the footprint cover of the classical carrier plane is gap-free;
- three chart-local carrier line representatives can be oriented at pairwise Euclidean `120 degrees` with sum zero.

These do **not** identify a native Cell with a classical circle. The circle is a carrier footprint/readout attached to a native Cell state.

## Current type corrections

Freeze:

`LEGACY_TRIPLE_BOUNDARY_ORIGIN -> CARRIER_TRIPLE_INCIDENCE_VERTEX V_E`.

`V_E != NATIVE_CELL`.

`V_E != NATIVE_COORDINATE_ZERO`.

`NATIVE_SLICE_ZERO = CHOSEN_CELL_CENTER`.

`LEGACY_THREE_POSITIVE_RAYS_ONLY = SUPERSEDED_AT_NATIVE_LAYER`.

`NATIVE_SELECTED_AXIS_DIRECTIONS = +/-E_i,+/-E_j,+/-E_k`.

`LEGACY_MIN_ZERO_A_E = RELATIVE/CARRIER OBSERVER SECTION, NOT NATIVE CELL IDENTITY`.

`LOSSLESS_NATIVE_SLICE_COORDINATE = (can3(x), min(x))`.

`CARRIER_CIRCLE_FOOTPRINT != NATIVE_CELL_IDENTITY`.

`CARRIER_GAP_FREE_COVER != CONTINUUM_NATIVE_SPACE_ONTOLOGY`.

## Metric correction

For raw signed native slice displacement `d in Z^3`, current native squared length is

`L_E(d)^2=sum d_i^2`.

The historical `(3,4,0)` value `5` survives when `(3,4,0)` is the **raw native displacement**. It is not a function of the min-zero carrier address alone.

The classical planar carrier quadratic

`Q_car(a,b,c)=a^2+b^2+c^2-ab-bc-ca`

is retained only as carrier Euclidean geometry.

For example `(3,4,0)` and `(4,5,1)` have the same carrier center, but native squared lengths `25` and `42` respectively.

## Provenance

The complete original text and its historical proofs remain recoverable in Git history at pre-rebase revisions. Current work must use the 2026-09-05 centered-slice rebase for native semantics and consult this path only as a compatibility/provenance pointer.
