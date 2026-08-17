# R059D Stage AT-REISSUE3 — Initial Unit Circle and Four-Invariant Native Generation

Task-ID: `RS-R059D-STAGE-AT-REISSUE3-INITIAL-UNIT-CIRCLE-FOUR-INVARIANT-GENERATION`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r059d-stage-at-reissue3-initial-unit-circle-four-invariant-generation`

## 0. Foundational inputs

Read first:

- `definitions/ENTERPRISE_INITIAL_CIRCLE_ALL_UNIT_INVARIANTS_20260817.md`
- `definitions/ENTERPRISE_VOID_ORIGIN_EXISTENCE_GEODESIC_20260817.md`
- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SEGMENT_ALL_SHORTEST_PATHS_20260817.md` only as retained spatial-tail structure;
- `driver_reviews/R059D_STAGE_AT_REISSUE2_INITIAL_UNIT_CIRCLE_SUPERSESSION_20260817.md`.

Earlier AT, AT-REISSUE and AT-REISSUE2 taskbooks are superseded and must not be executed canonically.

Freeze the current base state:

`VOID_E=∅` is external pre-coordinate nonexistence, not native coordinate `0`.

`VOID_E -> O_E=[+1]=[-1]` is the unique first existence step.

`CIRCLE_E(1)={O_E}`.

And simultaneously:

`RADIUS_E(CIRCLE_E(1))=1`

`DIAMETER_E(CIRCLE_E(1))=1`

`PERIMETER_E(CIRCLE_E(1))=1`

`AREA_E(CIRCLE_E(1))=1`.

These four ones are co-primitive Enterprise calibrations. None is derived from another by a classical formula.

The full Enterprise segment terminating at native coordinate `P` is the family of **all shortest paths** `VOID_E -> P`.

## 1. Hard objective

Starting from the normalized initial circle `(R,D,P,A)=(1,1,1,1)`, derive the strongest exact Enterprise-native theorem for:

1. the void-first existence/geodesic hierarchy;
2. whether higher existence levels form one canonical circle family;
3. native radius propagation;
4. native diameter propagation;
5. native perimeter/circumference propagation;
6. native area propagation;
7. relations, if any, among the four invariants;
8. square/root compatibility;
9. historical R059D circle status.

The four higher invariant laws must be derived independently before cross-relations are asserted.

## 2. Mandatory classical-formula firewall

Primary definitions/proofs may not assume:

- `D=2R`;
- `P=pi*D`;
- `P=2*pi*R`;
- `A=pi*R^2`;
- Euclidean equal-distance circle membership;
- source angle/trigonometry/standard pi;
- AK `tau` or `SEG_E(r)` orbit membership;
- AL A8 frontier maximality;
- historical `kappa_E` as a target.

The arithmetic identity `ENTERPRISE_SQUARE(n)=n^2` remains frozen, but may not be used to define higher circle area without an independent geometric theorem.

No historical result is protected from exact contradiction.

## 3. Stage A — existence graph, distance, and all-shortest-path segment theorem

Re-establish the current segment carrier under the all-unit base-circle foundation.

For native `P`, prove:

`ELL_E(P)=1+d_E(O_E,P)`.

The first existence edge `VOID_E -> O_E` is unique, and deleting it gives a canonical bijection

`SEG_E(P) <-> GEO_E(O_E,P)`.

Using the zero-centered A2 chart only as an auxiliary incidence certificate through `ENC_SIGNED/DEC_SIGNED`, prove or refute

`d_E(O_E,P)=max(|a|,|b|,|a+b|)`

for decoded `(a,b)`.

Characterize **all** shortest spatial tails exactly: admissible step directions, path-word condition, multiplicity, D6/reversal, axis/tie cases.

No representative shortest path may be privileged.

Outputs:

- `R059D_STAGE_AT3_EXISTENCE_DISTANCE_THEOREM.json`
- `R059D_STAGE_AT3_ALL_SHORTEST_SEGMENTS_THEOREM.json`.

## 4. Stage B — initial circle and higher existence-layer generation

For `n>=1`, define only the existence level

`LEVEL_E(n)={P:ELL_E(P)=n}`.

Freeze:

`LEVEL_E(1)=CIRCLE_E(1)={O_E}`.

For `n>=2`, derive exactly:

- cardinality of `LEVEL_E(n)`;
- D6 decomposition;
- induced native adjacency;
- connected components and vertex degrees;
- relation between `LEVEL_E(n)` and `LEVEL_E(n+1)` under native outward generation;
- whether every level is a simple closed endpoint cycle;
- whether the family is recursively generated from the initial circle without an extra selector.

Only if justified, freeze

`CIRCLE_E(n)=LEVEL_E(n)`.

A valid proof must explain why the singleton initial circle and later cyclic levels are members of one Enterprise circle family rather than merely sharing an index.

Output:

`R059D_STAGE_AT3_CIRCLE_GENERATION_THEOREM.json`.

## 5. Stage C — native radius law, independently from diameter

The base calibration is

`RADIUS_E(CIRCLE_E(1))=1`.

Derive the higher radius law from Enterprise-native structure only.

Audit candidate meanings separately:

- existence generation level from `VOID_E`;
- fixed-origin shortest-segment length;
- another intrinsic center-to-circle observable derived from the generated circle family.

Do not use diameter or perimeter to define radius.

Test, but do not assume:

`RADIUS_E(CIRCLE_E(n))=n`.

If several inequivalent radius extensions survive, freeze underdetermination.

Output:

`R059D_STAGE_AT3_RADIUS_LAW.json`.

## 6. Stage D — native diameter law, independently from radius

The base calibration is

`DIAMETER_E(CIRCLE_E(1))=1`.

Derive a higher-circle diameter law without using `2*RADIUS_E`.

Audit possible native meanings, including generation span, antipodal/native crossing structure, and any circle-internal incidence observable justified by Stage B.

Do not define diameter as ordinary singleton/pairwise graph diameter by fiat.

Test, but do not assume:

`DIAMETER_E(CIRCLE_E(n))=n`.

Output:

`R059D_STAGE_AT3_DIAMETER_LAW.json`.

## 7. Stage E — native perimeter/circumference law, independently

The base calibration is

`PERIMETER_E(CIRCLE_E(1))=1`.

For higher circles, derive perimeter from the intrinsic generated circle structure, not from radius/diameter and not from pi.

If `CIRCLE_E(n)` for `n>=2` is an induced cycle, distinguish carefully:

- raw boundary-edge count of the visible level cycle;
- Enterprise perimeter invariant propagated from the base value one.

Do not assume these are the same typed object until proved.

Derive the exact recurrence from circle `n` to circle `n+1` if one exists.

Output:

`R059D_STAGE_AT3_PERIMETER_LAW.json`.

## 8. Stage F — native area law, independently

The base calibration is

`AREA_E(CIRCLE_E(1))=1`.

Derive higher area from an Enterprise-native interior/generation construction.

Audit possible native area carriers, such as:

- generated enclosed native cells/normalized cell packets;
- cumulative layer contribution from the initial circle;
- another incidence-based interior measure proved compatible with the frozen unit quadrilateral.

Mandatory:

- no Euclidean area;
- no `pi*R^2`;
- no use of `n^2` merely because `ENTERPRISE_SQUARE(n)=n^2`;
- exact compatibility with `AREA_E(CIRCLE_E(1))=1`;
- D6 invariance;
- a proved recurrence or closed form if available.

Test, but do not assume:

`AREA_E(CIRCLE_E(n))=n^2`.

Output:

`R059D_STAGE_AT3_AREA_LAW.json`.

## 9. Stage G — cross-invariant relation audit

Only after Stages C–F are independently frozen, compare the four laws.

Determine exactly whether Enterprise-native relations emerge among

`R_E(n), D_E(n), P_E(n), A_E(n)`.

Possible valid outcomes include:

- one or more exact algebraic relations;
- recurrence-only relations;
- asymptotic ratios;
- scale-dependent ratios;
- no nontrivial relation beyond the shared base normalization.

Explicitly test rather than assume whether any analogue of

`D=2R`, `P/D=constant`, `A/R^2=constant`

exists.

If a circle constant is defined, state its exact type and denominator. Do not recycle the historical symbol `kappa_E` unless the new invariant relation justifies it.

Output:

`R059D_STAGE_AT3_FOUR_INVARIANT_RELATION_AUDIT.json`.

## 10. Stage H — square/root compatibility

Audit the relation between the circle hierarchy and the frozen arithmetic laws

`ENTERPRISE_SQUARE(n)=n^2`

`ENTERPRISE_ROOT(n^2)=n`.

The base identity

`AREA_E(CIRCLE_E(1))=1=1^2`

is only a calibration coincidence until a general theorem is proved.

If Stage F independently yields `AREA_E(CIRCLE_E(n))=n^2`, prove the resulting geometric interpretation and update typing. Otherwise preserve square/root independently.

Also recheck the unit quadrilateral `AREA_E=4` and `PERIMETER_E=4` for compatibility with the circle foundation without conflating square and circle objects.

Output:

`R059D_STAGE_AT3_SQUARE_ROOT_CIRCLE_COMPATIBILITY.json`.

## 11. Stage I — turn/path-family theorem

If Stage B gives a canonical higher circle cycle, define turning at the **whole segment-family** level:

endpoint `P` carries all shortest `VOID_E -> P` paths.

Moving to an adjacent circle endpoint replaces the entire geodesic family with the next one; no representative path is selected.

Determine:

- clockwise/counterclockwise native orientations;
- minimal return period;
- overlap of adjacent segment footprints;
- equal-length local geodesic deformations (`2<->2` etc.);
- reduction to the accepted one-step AR cycle after proper retyping.

Output:

`R059D_STAGE_AT3_SEGMENT_FAMILY_TURN_THEOREM.json`.

## 12. Stage J — historical supersession map

After the new circle/invariant laws freeze, compare separately with:

- AP-REISSUE;
- AQ;
- AR;
- AS diagnostic result;
- AK fixed-length orbit;
- AL support frontier;
- AI `kappa_E^2=12`;
- AG/AH count/word identities;
- old AT / AT-REISSUE / AT-REISSUE2 assumptions.

Classify each:

- `PRESERVED_AS_NATIVE`;
- `PRESERVED_WITH_REINDEXING`;
- `PRESERVED_AS_AUXILIARY_COMBINATORIAL_OBJECT`;
- `REQUIRES_REINTERPRETATION`;
- `SUPERSEDED_BY_INITIAL_ALL_UNIT_CIRCLE_FOUNDATION`.

Correct combinatorics must not be deleted merely because its old geometric typing fails.

Output:

`R059D_STAGE_AT3_HISTORICAL_SUPERSESSION_MAP.json`.

## 13. Deterministic validation

After proof statements freeze, validate at minimum:

- distance theorem by independent BFS on large boxes;
- shortest-path multiplicities;
- existence levels/circle adjacency through at least `n=257`;
- D6/reversal;
- independently computed radius/diameter/perimeter/area recurrences where claimed;
- base normalization `(R,D,P,A)=(1,1,1,1)`;
- no classical-formula leakage;
- no-native-zero / void-is-not-zero firewall;
- historical comparison;
- prior-stage immutability.

Proof dominates checker evidence.

## 14. Stop condition

Stop for Driver review. Do not consume a later stage automatically.
