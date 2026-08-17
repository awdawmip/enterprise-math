# R059D Stage AT-REISSUE2 — Origin-Diameter-One Circle Generation and Geodesic Family Refoundation

Task-ID: `RS-R059D-STAGE-AT-REISSUE2-ORIGIN-DIAMETER-ONE-CIRCLE-GENERATION`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r059d-stage-at-reissue2-origin-diameter-one-circle-generation`

## 0. Foundational inputs

Read first:

- `definitions/ENTERPRISE_ORIGIN_IS_DIAMETER_ONE_CIRCLE_20260817.md`
- `definitions/ENTERPRISE_VOID_ORIGIN_EXISTENCE_GEODESIC_20260817.md`
- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SEGMENT_ALL_SHORTEST_PATHS_20260817.md` only as the retained spatial-tail theorem;
- `driver_reviews/R059D_STAGE_AT_REISSUE_ORIGIN_DIAMETER_ONE_SUPERSESSION_20260817.md`.

The earlier AT and AT-REISSUE taskbooks are superseded and must not be executed canonically.

Freeze:

`VOID_E=∅` is external pre-coordinate nonexistence, not native coordinate `0`.

`VOID_E -> O_E=[+1]=[-1]` is the unique first existence step.

`CIRCLE_E(1)={O_E}`.

`DIAMETER_E(CIRCLE_E(1))=1`.

The base circle is not a classical diameter-zero/radius-zero point-circle.

The full segment terminating at native point `P` is the family of all shortest paths `VOID_E -> P`; all have the same unique first edge and then all shortest spatial tails `O_E -> P`.

## 1. Hard objective

Starting from the frozen diameter-one base circle, derive the strongest exact native theorem for:

1. complete void-to-point geodesic segment families;
2. fixed-existence-level endpoint sets;
3. generation of higher Enterprise circles from `CIRCLE_E(1)`;
4. Enterprise diameter for higher circles;
5. Enterprise radius, if independently meaningful;
6. circumference/perimeter;
7. any circle constant;
8. status of historical AK/AL/AI circle results.

Do not import classical `D=2R`, Euclidean equal-distance, standard pi, source angles, or historical circle membership.

## 2. Stage A — base-circle theorem and type firewall

Formalize the base case exactly:

`CIRCLE_E(1)={O_E}`

`DIAMETER_E(CIRCLE_E(1))=1`.

Prove/type-check:

- `VOID_E` is not an element of the circle;
- native zero remains nonexistent;
- the ordinary internal graph diameter of the singleton and `DIAMETER_E` are distinct typed quantities;
- D6 fixes the base circle;
- translation of the coordinate origin transports the base-circle state while the void generation edge reattaches to the translated origin.

Do not define Enterprise radius yet.

Output:

`R059D_STAGE_AT2_BASE_DIAMETER_ONE_CIRCLE_THEOREM.json`.

## 3. Stage B — augmented existence graph and all shortest segments

Re-prove under the current foundation:

`ELL_E(P)=1+d_E(O_E,P)`

and the canonical bijection

`SEG_E(P) <-> GEO_E(O_E,P)`

after deleting the unique first existence edge.

Using the zero-centered A2 chart only as an auxiliary incidence certificate, prove/refute

`d_E(O_E,P)=max(|a|,|b|,|a+b|)`

for decoded point `(a,b)`.

Then characterize **all** shortest spatial tails exactly, including multiplicity, D6/reversal, axis cases and tie/bisector cases.

No representative geodesic may be privileged.

Outputs:

- `R059D_STAGE_AT2_EXISTENCE_DISTANCE_THEOREM.json`
- `R059D_STAGE_AT2_ALL_SHORTEST_SEGMENTS_THEOREM.json`.

## 4. Stage C — geodesic footprint and equal-length local grammar

Define the segment footprint as the union of all shortest paths.

Re-audit local moves:

- fixed-endpoint `1->2` triangle detour;
- inverse `2->1` shortening;
- equal-length `2<->2` rhombus/order-exchange candidate;
- any other elementary geodesic-preserving move.

Prove the generating local grammar for the graph of shortest-path representatives if possible, and whether the representative graph is connected.

Output:

`R059D_STAGE_AT2_GEODESIC_FOOTPRINT_AND_FLIP_THEOREM.json`.

## 5. Stage D — existence layers generated from the base circle

For `n>=1`, define only as an existence-level endpoint set:

`LEVEL_E(n)={P:ELL_E(P)=n}`.

Freeze only

`LEVEL_E(1)=CIRCLE_E(1)={O_E}`.

For `n>=2`, derive:

- exact cardinality;
- D6 sector decomposition;
- induced native spatial adjacency;
- connected components;
- vertex degrees;
- whether it is a simple closed cycle;
- relation between `LEVEL_E(n)` and `LEVEL_E(n+1)` under outward existence generation.

Candidate to test, not assume:

`|LEVEL_E(n)|=6(n-1)` for `n>=2`.

Output:

`R059D_STAGE_AT2_EXISTENCE_LAYER_THEOREM.json`.

## 6. Stage E — higher-circle identification

The base case is already frozen as a circle. Determine whether the natural recursive/generated higher circle family is exactly

`CIRCLE_E(n)=LEVEL_E(n)`

for every `n>=1`.

A valid proof must explain why the same object type persists from the singleton base circle to later cyclic layers; mere cardinality matching is insufficient.

Required questions:

1. Does each level arise canonically from the preceding circle under native generation/adjacency?
2. For `n>=2`, is the induced endpoint graph a single D6 cycle?
3. Is any extra turn-selector needed?
4. Are there alternative equally native generated objects at the same existence scale?
5. Does `n=1` act as a genuine base object for the same recursive family rather than an exceptional naming convention?

Possible dispositions:

- `EXISTENCE_LEVELS_FORM_CANONICAL_ENTERPRISE_CIRCLE_FAMILY_FROM_DIAMETER_ONE_BASE`;
- `BASE_CIRCLE_FROZEN__HIGHER_LEVELS_REQUIRE_EXTRA_CIRCLE_AXIOM`;
- exact countertheorem.

Output:

`R059D_STAGE_AT2_CIRCLE_GENERATION_THEOREM.json`.

## 7. Stage F — Enterprise diameter law

Only after the higher-circle family is frozen, derive `DIAMETER_E` for every circle.

Do not define diameter as:

- maximum pairwise spatial graph distance;
- twice a presumed radius;
- coordinate magnitude by fiat;
- old AK/AL radius label.

Start from the frozen calibration

`DIAMETER_E(CIRCLE_E(1))=1`.

Test whether native generation forces

`DIAMETER_E(CIRCLE_E(n))=n`

for all `n>=1`, or another exact recurrence/law.

If multiple inequivalent diameter extensions of the base case satisfy all current native axioms, freeze underdetermination instead of selecting by historical fit.

Output:

`R059D_STAGE_AT2_DIAMETER_LAW.json`.

## 8. Stage G — Enterprise radius law, independently

Only after Stage F, ask whether an independent native radius exists.

Potential observables to audit include:

- spatial post-origin distance from `O_E` to level endpoints;
- existence length from `VOID_E`;
- another circle-internal/native center-to-boundary observable.

Do **not** impose

`DIAMETER_E=2*RADIUS_E`.

If a radius is canonical, derive the exact relation between `RADIUS_E` and `DIAMETER_E` including the base circle.

If no independent radius is needed or uniquely defined, say so explicitly.

Output:

`R059D_STAGE_AT2_RADIUS_DIAMETER_RELATION.json`.

## 9. Stage H — circumference/perimeter law

Only after the circle family is fixed, define its circumference/perimeter from native circle structure.

The `n=1` base circle requires a separately proved base value; do not silently assign zero or one by classical analogy.

For `n>=2`, if the circle is an induced simple cycle, derive its boundary-edge count exactly.

Candidate to test, not assume:

`PERIMETER_E(CIRCLE_E(n))=6(n-1)` for `n>=2`.

Then prove the recurrence/generation relation between consecutive circle perimeters.

Output:

`R059D_STAGE_AT2_CIRCUMFERENCE_THEOREM.json`.

## 10. Stage I — circle constant audit without classical denominator leakage

Do not define a circle constant until the Enterprise diameter and/or radius laws are proved.

Compute all meaningful native ratios separately, such as

`PERIMETER_E / DIAMETER_E`

and, only if a canonical radius exists,

`PERIMETER_E / (2*RADIUS_E)`

but do not assume these are identical or that either should be called `kappa_E`.

Determine whether there is:

- an exact constant at finite scale;
- only an asymptotic constant;
- a scale-dependent ratio;
- more than one typed ratio.

Historical `kappa_E^2=12` must be re-audited only after the new ratio typing is frozen.

Output:

`R059D_STAGE_AT2_CIRCLE_CONSTANT_AUDIT.json`.

## 11. Stage J — square/root and diameter-one base compatibility

Audit consistency with the frozen arithmetic calibration:

`ENTERPRISE_SQUARE(n)=n^2`

`ENTERPRISE_ROOT(n^2)=n`.

In particular determine whether the diameter-one base circle gives an independent reason for the `1` baseline or whether square/root remains separately founded by the unit quadrilateral.

Do not alter square/root unless an exact contradiction is found.

Output:

`R059D_STAGE_AT2_SQUARE_ROOT_CIRCLE_BASE_AUDIT.json`.

## 12. Stage K — historical supersession map

After all new theorems freeze, compare separately with:

- AP-REISSUE;
- AQ;
- AR;
- AS diagnostic result;
- AK fixed-length orbit;
- AL support frontier;
- AI `kappa_E^2=12`;
- AG/AH words and counts;
- old AT and AT-REISSUE task assumptions.

Classify each:

- `PRESERVED_AS_NATIVE`;
- `PRESERVED_WITH_REINDEXING`;
- `PRESERVED_AS_AUXILIARY_COMBINATORIAL_OBJECT`;
- `REQUIRES_REINTERPRETATION`;
- `SUPERSEDED_BY_ORIGIN_DIAMETER_ONE_CIRCLE_FOUNDATION`.

Do not delete correct combinatorics merely because its old circle typing fails.

Output:

`R059D_STAGE_AT2_HISTORICAL_SUPERSESSION_MAP.json`.

## 13. Deterministic validation

After proof statements freeze, validate at minimum:

- existence distances on large bounded boxes by independent BFS;
- all shortest-path multiplicities for bounded cases;
- local geodesic-move connectivity;
- existence levels through at least `n=257`;
- induced adjacency/cycle structure;
- circle generation recurrence;
- diameter/radius/perimeter formulas where proved;
- D6/reversal;
- no-native-zero and void-is-not-zero firewalls;
- exact comparison to historical circle objects;
- prior-stage immutability.

Proof dominates checker evidence.

## 14. Stop condition

Stop for Driver review. Do not consume a later stage automatically.
