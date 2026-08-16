# R059D COORD-IA — MAIN COORDINATE / UNIQUE TRACEABLE CELL ADDRESS FOUNDATION

Task-ID: `RS-R059D-COORD-IA-MAIN-COORDINATE-UNIQUE-ADDRESS`
Generation: `R059D-COORD`
Stage: `IA`
Status: `DRIVER_APPROVED_TASKBOOK`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Researcher-ID: `EM-R059D-C7A21`
Date: `2026-08-16`

## 0. Driver pivot

Coordinate foundation is now higher priority than continuing BRC threshold fitting.

R059D Stage AA has independently reached a frozen researcher checkpoint and is not modified by this task. Do not consume Stage-AA conclusions as premises for coordinate construction. Coordinate IA is a foundation subprogram intended to freeze how every lattice/cell receives an exact, unique, computable and traceable address before later BRC/collapse claims rely on coordinates.

The task is not to infer Euclidean length, angle, area, or root-collapse behavior.

## 1. Existing authoritative carrier

Use the current project-level three-axis plane carrier from `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`:

`Lambda = {(x,y,z) in Z^3 : x+y+z=0}`

with generator steps

`u=(1,-1,0)`
`v=(0,1,-1)`
`w=(-1,0,1)`

and

`u+v+w=0`.

Six directed local steps:

`{+u,-u,+v,-v,+w,-w}`.

This is an integer algebraic carrier. Do not attach inherited Euclidean metric semantics.

## 2. Scientific question

Freeze an exact addressing law answering all of the following:

1. Given any finite transition history from a chosen chart origin, how is the cell coordinate computed using integer arithmetic only?
2. Why do different histories that reach the same carrier cell yield the same coordinate readout?
3. Why can two distinct carrier cells not receive the same coordinate inside one frozen chart?
4. How can the coordinate be reversed into a valid canonical generation certificate?
5. What chart metadata is mathematically necessary for absolute uniqueness?
6. How are coordinate equality and raw path-history equality kept distinct?
7. How can the address be serialized exactly and replayed without floating point or geometric embedding?

## 3. Raw channel-count quotient

For a path/history P, define signed net channel counts

`n(P)=(a,b,c) in Z^3`,

where each component is positive-step count minus negative-step count for the corresponding channel family.

Because `u+v+w=0`, raw count triples are not unique cell coordinates:

`(a,b,c) ~ (a+t,b+t,c+t)` for every integer t.

Freeze the quotient

`Q = Z^3 / <(1,1,1)>`.

Mandatory theorem target:

The map

`Phi([a,b,c]) = a*u + b*v + c*w`

is a bijection from Q onto Lambda.

In explicit integer coordinates:

`Phi([a,b,c]) = (a-c, b-a, c-b)`.

Prove exactly:

- well-definedness under common shift;
- kernel exactly `<(1,1,1)>`;
- surjectivity onto every `(x,y,z)` with `x+y+z=0`;
- injectivity on quotient classes.

This quotient is the primary algebraic explanation of why multiple paths/count descriptions may recoalesce to one cell.

## 4. Main coordinate

Within one frozen chart, define the main coordinate of a cell as the unique

`COORD(cell)=(x,y,z) in Lambda`.

Transition update is exact integer addition:

`COORD(next)=COORD(current)+delta(step)`

with `delta` one of the six frozen generators.

The chart origin has

`COORD(O)=(0,0,0)`.

Mandatory path-readout theorem:

For every history P from O,

`COORD(endpoint(P)) = sum delta(step_i) = Phi([n(P)])`.

Do not identify histories merely because their coordinates agree. Raw history equality remains ordered-history equality wherever previously frozen.

## 5. Gauge / anchor impossibility and chart header

Prove or explicitly certify the following obstruction:

A homogeneous infinite carrier with translation and D6/C6-type symmetries cannot internally select one unique absolute origin and one unique oriented frame from symmetry alone.

Therefore an absolute address must carry a declared chart/gauge header.

Freeze at least:

`CHART = (carrier_id, precision_layer_id, origin_anchor_id, frame_id)`.

The origin anchor is provenance, not a geometric center.

The frame labels are addressing metadata. They do not imply a physically preferred axis unless a separate theorem establishes one.

Mandatory address form:

`CELL_ADDRESS = (CHART_ID, x, y, z)` with `x+y+z=0`.

Within a fixed chart, exact tuple equality is the primary identity test. Hashes may be checksums only and must not replace exact tuple identity.

## 6. Canonical trace certificate

Coordinate uniqueness alone is not enough; every address must be reproducibly generable.

Construct a canonical quotient representative for each class `[a,b,c]` by common-shift normalization, preferred target:

`NF([a,b,c])=(A,B,C)` such that

- `A,B,C >= 0`;
- `min(A,B,C)=0`;
- `(A,B,C)` is in the same diagonal-shift class.

Prove existence and uniqueness.

Then freeze a deterministic serialization-only channel order (for example `u < v < w`) and define a canonical generation certificate using `A` copies of `+u`, then `B` copies of `+v`, then `C` copies of `+w`, or an exactly equivalent deterministic certificate.

Important semantic guard:

The canonical certificate is an addressing/provenance normal form. It does not become the unique native history and does not erase other histories reaching the same cell.

The researcher may find a more symmetric deterministic certificate, but any arbitrary ordering choice must be typed as implementation/addressing metadata rather than native geometric preference.

## 7. Exact reverse computation

Given `(CHART_ID,x,y,z)` with `x+y+z=0`, provide an integer-only algorithm to recover:

- the quotient class `[a,b,c]`;
- its canonical normal form `NF`;
- a valid canonical generation certificate;
- all six neighboring addresses.

No floating point is permitted.

## 8. Traceability requirements

For every tested cell address, deterministic replay must verify:

`origin -> canonical certificate -> coordinate -> exact same address`.

For every tested arbitrary legal history P:

`history -> net channel counts -> quotient class -> coordinate`.

For two histories P,Q ending at the same cell, record:

`COORD(P)=COORD(Q)` while preserving whether `P=Q` as raw ordered histories.

For closed carrier cycles, verify exact coordinate return to zero displacement.

## 9. Required local algebra regressions

At minimum include:

1. origin;
2. six one-step neighbors;
3. `u+v+w=0` triangular closure;
4. step followed by inverse;
5. commuting reorderings `u+v=v+u` as coordinate readouts;
6. multiple histories to the same cell;
7. distinct cells with distinct coordinates;
8. negative-direction histories;
9. common-shift raw count triples mapping to the same coordinate;
10. canonical NF invariance under choice of raw representative;
11. cyclic channel relabeling covariance;
12. reflection/inversion covariance;
13. deterministic replay for a declared bounded atlas, preferably all canonical cells generated within transition count <= 6 or another explicit finite bound.

## 10. Relationship to older R059D coordinate experiments

Do not silently inherit Stage-W homogeneous stored-coordinate formulas as the main coordinate ontology.

In particular, the older conditional W0 stored map

`(a-b-c,-a+b-c,-a-b+c)`

was an experiment-specific homogeneous stored-coordinate model and later nonhomogeneous work showed that stored-coordinate homogeneity was not forced.

COORD-IA instead derives the main address from the current project carrier `Lambda` and the exact path-count quotient. Record old W/W-reissue coordinate models as conditional historical models, not the primary address unless an explicit equivalence theorem is proved.

## 11. Semantic firewall

Do not use as premises:

- Euclidean length/norm;
- angle/trigonometry;
- area/volume;
- square-root/root-order collapse;
- BRC threshold formulas;
- Stage-AA frontier coupling;
- shortest-path uniqueness;
- canonical history = native history;
- arbitrary origin/frame = naturally preferred origin/frame.

Allowed:

- exact integer addition/subtraction;
- quotient groups / equivalence classes;
- finite words and signed channel counts;
- declared chart/gauge metadata;
- carrier automorphisms;
- exact deterministic normal forms.

## 12. Required artifacts

Freeze at least:

1. `R059D_COORD_IA_CARRIER_AND_CHART_PROTOCOL.json`
2. `R059D_COORD_IA_PATH_COUNT_QUOTIENT.json`
3. `R059D_COORD_IA_MAIN_COORDINATE_MAP.json`
4. `R059D_COORD_IA_UNIQUENESS_BIJECTION_PROOF.json`
5. `R059D_COORD_IA_GAUGE_ANCHOR_OBSTRUCTION.json`
6. `R059D_COORD_IA_CANONICAL_NORMAL_FORM.json`
7. `R059D_COORD_IA_TRACE_CERTIFICATE_PROTOCOL.json`
8. `R059D_COORD_IA_NEIGHBOR_GENERATION_PROTOCOL.json`
9. `R059D_COORD_IA_AUTOMORPHISM_COVARIANCE.json`
10. `R059D_COORD_IA_REGRESSION_RESULTS.json`
11. `R059D_COORD_IA_SEMANTIC_CLAIM_LEDGER.json`
12. deterministic checker output
13. `R059D_COORD_IA_MAIN_COORDINATE_CHECKPOINT.json`

## 13. Checker hard negatives

Reject at minimum:

- `RAW_COUNT_TRIPLE_IS_UNIQUE_COORDINATE`;
- `COMMON_SHIFT_CHANGES_CELL`;
- `COORD_EQUALITY_IMPLIES_RAW_HISTORY_EQUALITY`;
- `HOMOGENEOUS_CARRIER_HAS_INTRINSIC_UNIQUE_ORIGIN`;
- `HOMOGENEOUS_CARRIER_HAS_INTRINSIC_UNIQUE_ORIENTED_FRAME`;
- `HASH_IS_PRIMARY_CELL_IDENTITY`;
- `FLOATING_POINT_REQUIRED_FOR_COORDINATE`;
- `OLD_STAGE_W_STORED_MAP_SILENTLY_PROMOTED_TO_MAIN_COORDINATE`;
- `EUCLIDEAN_METRIC_USED_FOR_ADDRESSING`;
- `BRC_COLLAPSE_USED_TO_DEFINE_COORDINATE`.

## 14. Required return / stop

Return:

- exact coordinate construction;
- quotient-bijection theorem status;
- chart/gauge obstruction status;
- canonical normal form and reverse algorithm;
- bounded deterministic replay summary;
- artifact hashes;
- checkpoint SHA256;
- owner head / Draft PR if published;
- one of:
  - `MAIN_COORDINATE_UNIQUE_TRACEABLE_FOUNDATION_PROVED`
  - `MAIN_COORDINATE_REQUIRES_REVISED_CARRIER_RELATION`
  - `SEMANTIC_HARD_STOP` with exact gate.

Then stop for Driver review. Do not enter Coordinate IB without authorization.
