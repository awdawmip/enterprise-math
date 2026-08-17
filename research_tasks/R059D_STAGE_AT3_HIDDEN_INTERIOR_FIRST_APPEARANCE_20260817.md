# R059D Stage AT3-HI — Hidden Interior First Appearance Under Perimeter Trace

Task-ID: `RS-R059D-STAGE-AT3-HI-HIDDEN-INTERIOR-FIRST-APPEARANCE`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r059d-stage-at3-hi-hidden-interior-first-appearance`

This is a focused parallel diagnostic to AT-REISSUE3. It does not consume the next main-stage letter and must not assume AT3's four-invariant laws before they are proved.

## 0. Current frozen foundation

Read first:

- `definitions/ENTERPRISE_INITIAL_CIRCLE_ALL_UNIT_INVARIANTS_20260817.md`
- `definitions/ENTERPRISE_VOID_ORIGIN_EXISTENCE_GEODESIC_20260817.md`
- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SEGMENT_ALL_SHORTEST_PATHS_20260817.md` as the retained all-shortest-path spatial-tail structure.

Freeze:

`VOID_E=∅` is external pre-coordinate nonexistence, not native coordinate `0`.

`VOID_E -> O_E=[+1]=[-1]` is the unique first existence step.

`CIRCLE_E(1)={O_E}` and

`R_E(1)=D_E(1)=P_E(1)=A_E(1)=1`.

The four unit values are co-primitive calibrations. No classical circle formula is allowed as a primary definition.

For a native endpoint `P`, the Enterprise segment is the family of all shortest paths `VOID_E -> P`.

## 1. User target

The user rejects the naive assumption that area can continue indefinitely as a simple cumulative sum of successive perimeter counts.

The hard target is to determine the **first circle level at which genuinely hidden interior native points occur**: points that belong to the circle's native interior/generation carrier but are not traversed by the perimeter, especially points that enter the interior without ever having belonged to any earlier perimeter trace.

Do not assume such a level exists. An exact no-hidden-point theorem is a valid outcome.

## 2. Three trace/interior notions — mandatory

The stage must distinguish the following objects.

### 2.1 Current perimeter trace

For each candidate/generated circle level `n`, let `PERIMETER_PATH_FAMILY_E(n)` be **all** native closed perimeter traversals admitted by the independently justified circle-generation/turn rules available under the frozen foundation.

No preferred clockwise path may be selected if several equally lawful paths exist.

Define

`TRACE_E(n) = union of all native vertices visited by every admitted perimeter path in the family`.

Also record separately:

- `TRACE_EDGE_E(n)` = union of traversed native edges;
- path multiplicity/provenance;
- whether all admitted perimeter paths have identical vertex support.

If no perimeter-path family can yet be defined without circularity, freeze `PERIMETER_TRACE_UNDERDEFINED` and continue with every noncircular candidate trace separately rather than inventing one.

### 2.2 Native interior/generation carrier

Define the circle interior without Euclidean containment and without using an area formula as an oracle.

Mandatory candidate to audit first:

`GEODESIC_HULL_E(B) = union of all vertices occurring on all shortest VOID_E -> P segments for P in boundary/perimeter endpoint set B`.

Test whether this is the correct native generated interior carrier under the current all-shortest-path segment foundation.

Also audit any strictly more intrinsic carrier forced by the circle-generation rule, such as enclosed native cells/packets generated between successive perimeter traces.

Freeze the accepted object as `INTERIOR_E(n)` only after proving:

- D6 covariance;
- nesting or exact failure of nesting;
- compatibility with `INTERIOR_E(1)={O_E}`;
- no Euclidean/source-circle leakage;
- no use of `AREA_E(n)` to define membership.

If more than one inequivalent interior carrier survives, preserve all and report robustness/nonrobustness of first hidden appearance.

### 2.3 Hidden and fresh-hidden points

Define the current hidden interior set

`HIDDEN_E(n) = INTERIOR_E(n) \ TRACE_E(n)`.

This may become trivially nonempty merely because earlier circles are contained inside later circles. Therefore the principal object is the **fresh/lifetime-hidden** set.

Let

`TRACE_HISTORY_E(n) = union_{1<=k<=n} TRACE_E(k)`.

Define

`FRESH_HIDDEN_E(n) = INTERIOR_E(n) \ (INTERIOR_E(n-1) union TRACE_HISTORY_E(n))`

for `n>=2`, with the obvious base convention at `n=1`.

Interpretation: a point first enters the accepted interior by level `n`, but has never been traversed by any perimeter through level `n`.

Also define the cumulative lifetime-hidden set

`LIFETIME_HIDDEN_E(n) = INTERIOR_E(n) \ TRACE_HISTORY_E(n)`.

These three sets must never be conflated.

## 3. Primary theorem target

Find the exact minimum

`n_* = min{n>=1 : FRESH_HIDDEN_E(n) != empty}`

if it exists.

For the first nonempty level, output:

1. exact native coordinates/states of every first hidden point;
2. auxiliary A2 labels only as computation certificates;
3. D6 orbit decomposition;
4. multiplicity / number of shortest segments passing through each point;
5. exact reason no legal perimeter path visits it;
6. exact reason it nevertheless belongs to the interior carrier;
7. whether it is a vertex phenomenon, cell phenomenon, packet phenomenon, or mixed.

If `FRESH_HIDDEN_E(n)=empty` for every level in a proved infinite family, prove the exact no-hidden theorem instead.

## 4. First-appearance mechanism

Do not stop at the first integer.

Classify how hidden points are born. Candidate mechanisms to test include:

- `PERIMETER_SKIP`: the perimeter turn jumps around a native point that remains in the generated hull;
- `GEODESIC_INTERLEAVING`: multiple shortest segment families create an interior junction never exposed on a boundary trace;
- `CELL_FILL`: a new enclosed cell/packet contributes an interior native point before that point can occur on a perimeter;
- `PATH_MERGER`: several perimeter/segment branches merge and bury a point;
- `HISTORICAL_REINDEXING_ARTIFACT`: apparent hiddenness disappears after correct void-first / initial-circle indexing;
- an exact stronger mechanism discovered by the Researcher.

For the true first mechanism, provide a minimal local configuration certificate.

## 5. Relation to the naive cumulative-area count

The stage must explicitly test the naive recurrence

`A_naive(n) = A_naive(n-1) + P_trace_count(n)`

with base `A_naive(1)=1`, but only as a **counting diagnostic**, not as the definition of native area.

Determine the first level, if any, at which fresh hidden interior contributions force a discrepancy between:

- cumulative perimeter-visited support;
- accepted interior support cardinality / cell-packet count;
- any independently derived `AREA_E(n)` available after the interior object is frozen.

Do not assert `AREA_E = number of vertices` unless separately proved.

A hidden-point theorem may exist even if numeric area remains underdefined.

## 6. Exhaustive census and proof scope

Mandatory exact census:

- levels `n=1..64` exhaustively;
- extend to at least `n=256` if compressed formulas permit;
- if no first hidden point is found, derive a structural theorem rather than merely reporting a finite search.

For every level record:

- perimeter trace vertex count;
- perimeter trace edge count;
- interior carrier vertex/cell/packet counts by type;
- `|HIDDEN_E(n)|`;
- `|FRESH_HIDDEN_E(n)|`;
- `|LIFETIME_HIDDEN_E(n)|`;
- D6 orbit counts;
- whether each hidden set is connected/disconnected under native adjacency;
- first-generation level of every lifetime-hidden point in the finite census.

## 7. Robustness across all admissible perimeter paths

Because earlier research freezes `ALL_ADMISSIBLE_REACHABLE_PATHS_ARE_VALID`, hiddenness must be quantified carefully.

For a point `x`, distinguish:

- `NEVER_TRACED`: no admissible perimeter path at any level up to n visits x;
- `SOMETIMES_TRACED`: at least one admissible perimeter path visits x and at least one does not;
- `ALWAYS_TRACED`: every admissible perimeter realization at the relevant level visits x.

The principal first-hidden theorem must use `NEVER_TRACED` unless a different quantifier is explicitly justified.

If the first-appearance level depends on perimeter-path choice, freeze that nonuniqueness rather than selecting a favorable path.

## 8. Classical/source leakage firewall

Primary construction may not use:

- Euclidean inside/outside tests;
- source angles or standard pi;
- `D=2R`, `P=2*pi*R`, `A=pi*R^2`;
- AK `tau` or historical N/frontier membership as an oracle;
- AL A8 as an interior or boundary selector;
- previously guessed formulas `P=6(n-1)` or `A=1+3n(n-1)` as membership definitions.

Those formulas may only be compared post hoc after native sets are frozen.

## 9. Historical comparison arm

Only after the first-hidden theorem freezes, compare with historical AP/AK/AL/AQ/AR/AS objects.

Ask specifically whether the first hidden interior point is:

- absent from the historical N perimeter;
- present in an old support carrier;
- generated by all-shortest-path segment footprints;
- related to earlier UP/DOWN or escape-branch competition;
- a new phenomenon created only by the initial all-unit circle foundation.

No historical result is protected from exact contradiction.

## 10. Required artifacts

At minimum produce:

- `research_results/R059D_STAGE_AT3_HI/R059D_STAGE_AT3_HI_TRACE_DEFINITION.json`
- `research_results/R059D_STAGE_AT3_HI/R059D_STAGE_AT3_HI_INTERIOR_DEFINITION.json`
- `research_results/R059D_STAGE_AT3_HI/R059D_STAGE_AT3_HI_FIRST_APPEARANCE_THEOREM.json`
- `research_results/R059D_STAGE_AT3_HI/R059D_STAGE_AT3_HI_HIDDEN_CENSUS.json`
- `research_results/R059D_STAGE_AT3_HI/R059D_STAGE_AT3_HI_MECHANISM_CLASSIFICATION.json`
- `research_results/R059D_STAGE_AT3_HI/R059D_STAGE_AT3_HI_AREA_RECURRENCE_AUDIT.json`
- `research_results/R059D_STAGE_AT3_HI/R059D_STAGE_AT3_HI_PROOF.md`
- deterministic checker + checker output
- artifact manifest
- frozen checkpoint
- final report.

## 11. Preferred terminal dispositions

Use the strongest exact result, including:

1. `FIRST_FRESH_HIDDEN_INTERIOR_LEVEL_PROVED__N_STAR_<N>`
2. `HIDDEN_INTERIOR_EXISTS_BUT_FIRST_LEVEL_DEPENDS_ON_ADMISSIBLE_PERIMETER_REALIZATION`
3. `CURRENT_HIDDEN_NONEMPTY_FROM_EARLY_LEVEL_BUT_FRESH_HIDDEN_FIRST_APPEARS_LATER`
4. `NO_FRESH_HIDDEN_INTERIOR_POINTS__EVERY_INTERIOR_POINT_IS_PERIMETER_TRACED_AT_SOME_GENERATION`
5. `INTERIOR_OR_PERIMETER_TRACE_UNDERDEFINED_UNDER_CURRENT_FOUNDATION`
6. an exact stronger theorem.

## 12. Validation

After proof statements freeze, independently validate:

- all levels through at least 64;
- first-appearance minimality by exhaustive replay below `n_*`;
- D6 covariance;
- all perimeter-path quantifiers;
- geodesic-hull membership;
- hidden/lifetime/fresh set identities;
- no-native-zero / void-is-not-zero firewall;
- no classical membership leakage;
- prior-stage immutability by Git compare.

Proof dominates checker evidence.

## 13. Stop condition

Stop for Driver review after the focused hidden-interior theorem is frozen.

Do not modify or consume the AT3 main owner branch.
Do not automatically open a later stage.
