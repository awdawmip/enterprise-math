# R059D Stage AT — Geodesic Path-Family Segment and Fixed-Length Sphere Circle Refoundation

Task-ID: `RS-R059D-STAGE-AT-GEODESIC-PATH-FAMILY-SEGMENT-FIXED-LENGTH-SPHERE-CIRCLE-REFOUNDATION`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`
Owner branch after taskbook freeze:

`research/r059d-stage-at-geodesic-segment-fixed-length-sphere`

## 0. Foundational input and reason for this stage

Read first:

- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SEGMENT_ALL_SHORTEST_PATHS_20260817.md`
- `driver_reviews/R059D_STAGE_AS_DRIVER_REVIEW_20260817.md`
- AS report only as the accepted weaker-axiom underdetermination diagnosis.

Freeze the new foundational segment semantics:

`SEG_E(O,P) = GEO_E(O,P) = { all native shortest paths from O to P }`

`L_E(O,P) = d_E(O,P)`.

`+1 ≡ -1 ≡ O_E`; native coordinate `0` does not exist.

This stage is allowed to overturn historical AK/AL/AI native-circle interpretations if the new segment foundation gives an exact contradiction. Do not preserve old circle formulas by adding ad hoc axioms.

## 1. Hard objective

Determine the exact consequences of the all-shortest-path segment definition for:

1. native graph distance;
2. the complete geodesic path family to every coordinate;
3. local path deformation grammar;
4. fixed-length endpoint sets;
5. intrinsic endpoint adjacency/turn closure;
6. circumference and any circle constant;
7. the status of historical R059D circle results.

The primary object is the full path family, never a chosen representative path.

## 2. Stage A — native vertex graph and exact graph distance

Define the native primitive vertex-adjacency graph entirely from Enterprise incidence and signed-origin semantics.

Prove an exact graph-distance theorem for every native point `P`.

The accepted zero-centered A2 chart may be used only as an auxiliary computation certificate through `DEC_SIGNED/ENC_SIGNED`; it may not become the native ontology.

If `P` decodes to auxiliary `(a,b)`, explicitly test/prove the candidate certificate

`d_E(O,P) = max(|a|, |b|, |a+b|)`.

Do not assume it merely because it is familiar from an A2/hex graph.

Required:

- proof by lower bound + explicit path construction;
- D6 invariance;
- signed-origin translation typing;
- exact axis calibration `d_E(O,±n)=n-1` in native one-axis notation;
- no native zero leakage.

Output:

`R059D_STAGE_AT_NATIVE_GRAPH_DISTANCE_THEOREM.json`.

## 3. Stage B — characterize ALL shortest paths

For every endpoint `P`, characterize

`GEO_E(O,P)`

exactly.

In each fundamental sector derive:

- admissible primitive step directions in a shortest path;
- necessary and sufficient condition for a step word to be geodesic;
- path length;
- exact path multiplicity;
- D6/reversal transport to all sectors.

Where the auxiliary endpoint can be written with two nonnegative sector coordinates whose sum is `r`, test/prove whether path multiplicity is the appropriate binomial coefficient and whether every ordering of the two primitive step types is valid.

Special cases:

- axis endpoint: one shortest path;
- first non-axis endpoints: enumerate all shortest paths explicitly;
- bisectors/ties: retain every path.

No probability is intrinsic. Multiplicity is provenance only unless a measure is separately introduced.

Output:

`R059D_STAGE_AT_ALL_SHORTEST_PATHS_THEOREM.json`.

## 4. Stage C — canonical segment footprint / geodesic interval

Define the segment footprint only from the full geodesic family:

`VERT_SEG(O,P) = union of all geodesic vertices`

`EDGE_SEG(O,P) = union of all geodesic edges`.

Determine the exact finite subcomplex/interval generated between `O` and `P`.

Questions:

- Is the footprint a chain on axes and a 2D geodesic corridor off-axis?
- What is its vertex/edge/triangle count?
- Is it convex in the native graph-geodesic sense?
- Is every footprint vertex itself on some shortest prefix/suffix decomposition?
- How do footprints change when the endpoint moves to an adjacent equal-length point?

This stage supersedes any need to select terminal-side versus edgewise-side carriers as the line itself.

Output:

`R059D_STAGE_AT_GEODESIC_SEGMENT_FOOTPRINT.json`.

## 5. Stage D — local geodesic deformation grammar

Re-audit AS triangle flips under the new shortest-path definition.

Mandatory tests:

1. For fixed subpath endpoints connected by a primitive edge, does `1->2` necessarily increase length and therefore leave the shortest-path family?
2. Does `2->1` shorten a non-geodesic detour rather than represent a fixed-length line motion?
3. What are the elementary moves connecting two different shortest paths with the same endpoints?
4. Test the candidate `2<->2` rhombus / adjacent-step-order swap as the primitive geodesic-preserving move.
5. Prove whether the graph whose vertices are shortest paths and whose edges are elementary geodesic-preserving flips is connected.

If true, this provides a canonical internal dynamics among all representations of the same segment without choosing one path.

Output:

`R059D_STAGE_AT_GEODESIC_FLIP_GRAMMAR.json`.

## 6. Stage E — fixed-length endpoint sphere

For every integer `r>=1`, define

`SPHERE_E(r) = { P : d_E(O,P)=r }`.

This follows from the segment definition and is not imported from an old circle.

Prove exactly:

- cardinality of `SPHERE_E(r)`;
- D6 orbit/sector decomposition;
- induced native adjacency graph on `SPHERE_E(r)`;
- degree of each sphere vertex within the induced graph;
- whether the induced graph is one simple cycle;
- its minimal cycle length/perimeter if cyclic;
- ball cardinality `BALL_E(r)={P:d_E<=r}` as a supporting check.

Preferred candidate to test, not assume:

`|SPHERE_E(r)| = 6r`

and induced sphere adjacency is a simple `6r`-cycle.

Output:

`R059D_STAGE_AT_FIXED_LENGTH_SPHERE_THEOREM.json`.

## 7. Stage F — fixed-length turn of the whole segment family

If Stage E gives a canonical cyclic adjacency on `SPHERE_E(r)`, define the turn operation at endpoint level from that intrinsic adjacency, not from AK `tau`.

At each endpoint `P`, the line segment is the entire `GEO_E(O,P)` family. Turning to adjacent sphere endpoint `Q` means replacing the whole geodesic family by `GEO_E(O,Q)`.

Determine:

- whether clockwise/counterclockwise are the only two side choices;
- whether all endpoint states close after the sphere cycle length;
- whether any path representative must be chosen (preferred answer: no);
- how neighboring segment footprints overlap and differ;
- whether AR's two one-step side cycles are exactly the `r=1` reduction of this endpoint-sphere turn.

Output:

`R059D_STAGE_AT_GEODESIC_SEGMENT_TURN_THEOREM.json`.

## 8. Stage G — circle definition audit

Test the foundational implication:

`fixed endpoint O + fixed segment length r + all allowed endpoint positions`

`=> SPHERE_E(r)`.

If the induced sphere graph is a simple closed D6 cycle, determine whether this is now the canonical Enterprise circle under the new segment foundation.

Do not add curvature/frontier axioms merely to preserve the historical N circle.

Possible dispositions:

- `GEODESIC_FIXED_LENGTH_SPHERE_IS_CANONICAL_ENTERPRISE_CIRCLE`;
- `FIXED_LENGTH_SPHERE_EXISTS_BUT_NEEDS_AN_INDEPENDENT_TURN_ADMISSIBILITY_AXIOM`;
- exact countertheorem.

Output:

`R059D_STAGE_AT_CIRCLE_FOUNDATION_THEOREM.json`.

## 9. Stage H — circumference and constant

Only if Stage G canonically identifies the sphere cycle as the circle, define its circumference as native boundary-edge count and derive the exact law.

If `C_E(r)=6r`, then derive rather than assume:

`kappa_E = lim C_E(r)/(2r) = 3`

and

`kappa_E^2 = 9`.

If that theorem holds, explicitly mark historical `kappa_E^2=12` as superseded **as a native circle constant under the new segment foundation**, while retaining historical algebraic identities as results about the old N/frontier object where valid.

If the new sphere cycle is not canonical, do not manufacture a constant.

Output:

`R059D_STAGE_AT_CIRCUMFERENCE_CONSTANT_AUDIT.json`.

## 10. Stage I — exact historical comparison / supersession map

Only after Stages A–H freeze, compare with:

- AR radius-1 cycle;
- AK fixed-length turn orbit;
- AL support frontier;
- AI `kappa_E^2=12`;
- AG/AH combinatorial words/counts;
- AQ outward-geodesic cell object.

Find the first radius at which the new geodesic sphere endpoint cycle differs from the historical N/AL endpoint cycle, if any.

Classify each historical result separately:

- `PRESERVED_AS_NATIVE`;
- `PRESERVED_AS_AUXILIARY_COMBINATORIAL_OBJECT`;
- `REQUIRES_REINTERPRETATION`;
- `SUPERSEDED_BY_GEODESIC_SEGMENT_FOUNDATION`.

Do not globally delete correct combinatorics merely because its old circle typing fails.

Output:

`R059D_STAGE_AT_HISTORICAL_SUPERSESSION_MAP.json`.

## 11. Validation

After theorem statements are fixed, validate at minimum:

- distance formula on large bounded boxes through independent BFS;
- exact shortest-path enumeration for small/medium radii;
- multiplicity formulas;
- geodesic-flip connectivity for bounded cases;
- sphere/ball counts at least through `r=256`;
- induced sphere adjacency and cycle checks;
- D6/reversal covariance;
- signed-origin/no-native-zero firewall;
- exact comparison to historical N/AL cycles through a range large enough to expose first divergence;
- prior-stage immutability by Git compare.

Proof dominates checker evidence.

## 12. Stop condition

Stop for Driver review. Do not consume a later stage automatically.
