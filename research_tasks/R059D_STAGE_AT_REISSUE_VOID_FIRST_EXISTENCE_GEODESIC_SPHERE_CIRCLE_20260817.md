# R059D Stage AT-REISSUE — Void-First Existence Geodesic Segment and Spatial Circle Re-foundation

Task-ID: `RS-R059D-STAGE-AT-REISSUE-VOID-FIRST-EXISTENCE-GEODESIC-SPHERE-CIRCLE`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`
Owner branch after taskbook freeze:

`research/r059d-stage-at-reissue-void-first-existence-geodesic-sphere`

## 0. Foundational supersession

Read first:

- `definitions/ENTERPRISE_VOID_ORIGIN_EXISTENCE_GEODESIC_20260817.md`
- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SEGMENT_ALL_SHORTEST_PATHS_20260817.md` only as the retained spatial-tail theorem;
- `driver_reviews/R059D_STAGE_AS_DRIVER_REVIEW_VOID_START_SUPERSESSION_20260817.md`.

The previous AT taskbook is `SUPERSEDED / DO NOT EXECUTE` because it began the full segment at the origin.

Freeze the current foundation:

`VOID_E = ∅` is an external pre-coordinate state, not native coordinate `0`.

`VOID_E -> O_E=±1` is the unique first existence step.

For native point `P`:

`ELL_E(P)=d_(G~_E)(VOID_E,P)=1+d_E(O_E,P)`.

The full Enterprise segment is

`SEG_E(P)=all shortest paths VOID_E -> P`.

Every shortest path has the same unique first edge `VOID_E -> O_E`; deleting it gives the complete spatial geodesic family `GEO_E(O_E,P)`.

Freeze:

`ALL_SHORTEST_VOID_TO_POINT_PATHS_ARE_THE_SEGMENT`.

## 1. Hard objective

Derive the exact consequences of the void-first segment foundation for:

1. existence length;
2. post-origin spatial graph distance;
3. complete shortest-path families;
4. local geodesic deformation;
5. fixed-existence-length endpoint sets;
6. spatial circle/turn closure;
7. circumference/radius typing;
8. historical R059D circle status.

No historical circle theorem is protected from exact contradiction.

## 2. Mandatory type split: existence length versus spatial radius

Use two symbols and never conflate them:

`n = ELL_E(P)` = total existence length from `VOID_E`, with `n>=1`;

`r = d_E(O_E,P)` = post-origin spatial adjacency radius, with `r>=0`.

They satisfy exactly

`n=r+1`.

The origin has

`n=1`, `r=0`.

A one-post-origin-step endpoint `±2` has

`n=2`, `r=1`.

On a signed native axis prove

`ELL_E(±m)=m` for native coordinate magnitude `m>=1`.

Required output:

`R059D_STAGE_ATR_EXISTENCE_SPATIAL_LENGTH_TYPING.json`.

## 3. Stage A — augmented existence graph theorem

Construct the extended graph `G~_E` by adjoining exactly one external state `VOID_E` and one edge `VOID_E--O_E` to the native vertex graph `G_E`.

Prove:

1. `VOID_E` is not a native coordinate and is not `0`;
2. every path from `VOID_E` to a native state passes through `O_E` first;
3. `ELL_E(P)=1+d_E(O_E,P)`;
4. shortest `VOID_E->P` paths are in canonical bijection with shortest `O_E->P` spatial tails;
5. path multiplicities are unchanged by the void prefix;
6. D6 acts trivially on the unique existence edge and natively on the spatial tail;
7. translation typing is explicit: if the geometric origin is translated, the void generation edge attaches to the translated origin, not to an absolute coordinate.

Output:

`R059D_STAGE_ATR_AUGMENTED_EXISTENCE_GRAPH_THEOREM.json`.

## 4. Stage B — exact native spatial distance theorem

Prove the native vertex graph distance independently of the old circle.

Using the zero-centered A2 chart only as an auxiliary certificate through `DEC_SIGNED/ENC_SIGNED`, test/prove

`d_E(O_E,P)=max(|a|,|b|,|a+b|)`

for decoded auxiliary point `(a,b)`.

Require:

- lower bound;
- explicit shortest-path construction;
- D6 invariance;
- exact axis calibration;
- no native-zero leakage.

Then combine with Stage A to derive the existence-length closed form

`ELL_E(P)=1+max(|a|,|b|,|a+b|)`

as an auxiliary certificate, never as a native coordinate ontology.

Output:

`R059D_STAGE_ATR_SPATIAL_DISTANCE_THEOREM.json`.

## 5. Stage C — characterize ALL void-to-point shortest paths

Because the first edge is unique, characterize the spatial tail family `GEO_E(O_E,P)` exactly and then prefix `VOID_E->O_E`.

For each D6 sector derive:

- allowable shortest-path step directions;
- necessary and sufficient step-word condition;
- spatial length `r`;
- total existence length `n=r+1`;
- exact path multiplicity;
- axis and bisector special cases;
- reversal and D6 transport.

No single geodesic may be privileged.

Output:

`R059D_STAGE_ATR_ALL_SHORTEST_PATHS_THEOREM.json`.

## 6. Stage D — derived segment footprint and local deformation

Define the segment's spatial footprint as the union of all spatial geodesic tails. The void edge is a unique ontological prefix and carries no triangular spatial cell.

Prove the exact local geodesic deformation grammar.

Mandatory tests:

1. fixed-subpath `1->2` triangular detour is non-geodesic and exits the segment family;
2. `2->1` removes a non-geodesic detour rather than turning a fixed-length segment;
3. classify all elementary equal-length replacements between shortest paths;
4. prove/refute `2<->2` rhombus step-order exchange as the generating local move;
5. prove/refute connectivity of the graph of shortest path representatives under equal-length local moves.

Output:

`R059D_STAGE_ATR_GEODESIC_DEFORMATION_THEOREM.json`.

## 7. Stage E — fixed existence-length endpoint sets

For `n>=1`, define

`EXISTENCE_SPHERE_E(n)={P:ELL_E(P)=n}`.

Prove exactly

`EXISTENCE_SPHERE_E(n)={P:d_E(O_E,P)=n-1}`.

Then determine:

- `n=1` case exactly;
- cardinality for every `n>=2`;
- D6 sector decomposition;
- induced **spatial** native adjacency graph among endpoints;
- whether it is a single simple cycle for `n>=2`;
- ball cardinality under existence-length indexing.

Candidate to test, not assume:

`|EXISTENCE_SPHERE_E(1)|=1`,

`|EXISTENCE_SPHERE_E(n)|=6(n-1)` for `n>=2`.

Output:

`R059D_STAGE_ATR_FIXED_EXISTENCE_SPHERE_THEOREM.json`.

## 8. Stage F — circle center and radius typing

The void state is not a spatial point. Therefore if Stage E gives a closed endpoint cycle, determine carefully what the circle's geometric center and radius are.

Mandatory distinction:

- total segment existence length: `n`;
- spatial circle center: `O_E` unless an exact theorem says otherwise;
- spatial radius: `r=n-1` measured by native spatial adjacency after the existence edge.

Do not call `VOID_E` the geometric center merely because the full segment starts there.

Determine whether the canonical fixed-segment endpoint cycle should be typed as

`CIRCLE_E(n)` = endpoints of total existence-length n segments,

with spatial radius parameter `r=n-1`.

Output:

`R059D_STAGE_ATR_CIRCLE_CENTER_RADIUS_TYPING.json`.

## 9. Stage G — intrinsic turn closure of the whole path family

If the induced spatial adjacency on `EXISTENCE_SPHERE_E(n)` is cyclic, define turn intrinsically by adjacent endpoint states.

At endpoint `P`, the segment state is the entire void-prefixed geodesic family.

Determine:

- whether exactly two turn orientations survive;
- whether no individual shortest path representative must be chosen;
- whether the endpoint cycle closes canonically;
- minimal period;
- overlap/deformation relation of neighboring geodesic families;
- reduction at `n=2` to the old AR one-post-origin-step six-cycle after retyping.

Output:

`R059D_STAGE_ATR_GEODESIC_FAMILY_TURN_CLOSURE.json`.

## 10. Stage H — circumference and constant, with two denominators separated

Only if Stage F/G canonically identify the spatial endpoint cycle as the Enterprise circle, define circumference as spatial boundary-edge count.

If Stage E yields

`C_E(n)=6(n-1)` for `n>=2`, derive both ratios separately:

### Spatial circle ratio

Using `r=n-1`:

`C_E/(2r)=3` exactly.

### Existence-length ratio

Using total segment length `n`:

`C_E/(2n)=3(n-1)/n`, which is not constant at finite n but tends to `3`.

Do not conflate these.

If canonical, define the appropriate Enterprise circle constant only after deciding which radius type belongs to circle geometry. Preferred typing to test is spatial radius about `O_E`, not void-distance.

If this yields `kappa_E=3`, explicitly re-audit historical `kappa_E^2=12` as a native circle constant.

Output:

`R059D_STAGE_ATR_CIRCUMFERENCE_RADIUS_CONSTANT_AUDIT.json`.

## 11. Stage I — coordinate magnitude, existence length, and square calibration

Audit the new alignment on axes:

`COORD_MAG(±n)=ELL_E(±n)=n`.

Determine exactly what this does and does not imply for:

- `ENTERPRISE_SQUARE(n)=n^2`;
- the unit quadrilateral calibration;
- spatial adjacency side counts `n-1`;
- area/perimeter typing.

Do not rederive square from a graph-distance area assumption unless independently justified. The purpose is type reconciliation, not changing the frozen square formula by fiat.

Output:

`R059D_STAGE_ATR_SQUARE_LENGTH_TYPING_AUDIT.json`.

## 12. Stage J — historical supersession map

After all primary theorems freeze, compare with:

- AR one-step stateful cycles;
- AK fixed-length turn orbit;
- AL support frontier;
- AI `kappa_E^2=12`;
- AG/AH words/counts;
- AQ cell escape;
- old AT origin-start taskbook.

Classify each as:

- `PRESERVED_AS_NATIVE`;
- `PRESERVED_WITH_LENGTH_REINDEXING`;
- `PRESERVED_AS_AUXILIARY_COMBINATORIAL_OBJECT`;
- `REQUIRES_REINTERPRETATION`;
- `SUPERSEDED_BY_VOID_FIRST_GEODESIC_FOUNDATION`.

Find the first exact divergence where applicable.

Output:

`R059D_STAGE_ATR_HISTORICAL_SUPERSESSION_MAP.json`.

## 13. Validation

After theorem statements freeze, validate at minimum:

- augmented graph identity;
- native distance by independent BFS;
- shortest-path enumeration;
- geodesic local-move connectivity for bounded cases;
- existence spheres through `n>=257`;
- induced cycle adjacency;
- D6/reversal;
- no-native-zero / void-is-not-zero firewall;
- exact historical comparisons;
- prior-stage immutability.

Proof dominates checker evidence.

## 14. Stop condition

Stop for Driver review. Do not consume a later stage automatically.
