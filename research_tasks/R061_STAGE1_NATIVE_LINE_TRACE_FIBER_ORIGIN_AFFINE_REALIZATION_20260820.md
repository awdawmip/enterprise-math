# R061 Stage 1 — Native Line Trace Fiber / Origin-Affine Realization

Task-ID: `RS-R061-STAGE1-NATIVE-LINE-TRACE-FIBER-ORIGIN-AFFINE-REALIZATION`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r061-stage1-native-line-trace-realization`

## 0. Read first / frozen inputs

Read first:

1. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md` from current `main`;
2. `driver_reviews/R061_STAGE0_LINE_FORMULA_VALIDATION_DRIVER_REVIEW_20260820.md`;
3. frozen Stage 0 owner result at commit `e6657ce00382d52acda319f0108b787a03e9d5f2`, especially:
   - `research_results/R061_STAGE0/R061_STAGE0_ENTERPRISE_LINE_FORMULA_VALIDATION_PROOF.md`;
   - `R061_STAGE0_ORIGIN_AFFINE_OFFSET_AUDIT.md`;
   - `R061_STAGE0_THIRD_AXIS_COMPLETENESS_AUDIT.md`;
   - `R061_STAGE0_NONCOMMUTATIVE_PATH_LIFT_THEOREM.md`;
   - `R061_STAGE0_COUNTEREXAMPLES.json`.

Freeze from Stage 0:

`D_N={(a,b)>=0:a^2+b^2=N}` is exact.

`Sh_{a,b}(X_i,X_j)=[u^a v^b](uX_i+vX_j)^(a+b)` is exactly the finite free-word fiber with `a` copies of `X_i`, `b` copies of `X_j`.

Do not re-prove these except for regression checks.

Freeze current native geometry:

- `ENTERPRISE_RIGHT_ANGLE = 120_DEGREES`;
- inside each native right sector, `L_E^2=a^2+b^2`;
- `L_E(3,4,0)=5`;
- three positive native axes only;
- circle-cell center carrier nearest-neighbor spacing `1`;
- circle-cell carrier radius `1/sqrt(3)`;
- gap-free pairwise-overlapping circle-cell cover;
- origin `O_E=0` is a triple circle-boundary intersection, not a cell center and not a cell;
- instantaneous native state is exactly one circle cell;
- graph jump count is not native line length;
- carrier translation relations are not native Enterprise vector identities.

## 1. Hard objective

Derive or falsify an exact native realization map from the validated formal line lift to the overlapping circle-cell plane.

The hard target is:

`NATIVE_LINE_PATH_FIBER_IS_EXACTLY_TYPED_AND_ALGEBRAICALLY_GENERABLE`.

Do **not** assume that:

- every endpoint path is a line path;
- every minimum-jump path is a line path;
- every shuffle is automatically a native path from the origin;
- the trace-class hypothesis is true;
- `Pi_cell=identity`;
- one guessed affine `+1/-1` correction resolves the origin.

The stage must distinguish at least four objects:

1. `LINE_IDENTITY` — the algebraic object representing one Enterprise line segment;
2. `LINE_PATH_REPRESENTATIVE` — one discrete single-cell trajectory realizing that line identity;
3. `ENDPOINT_PATH` — any valid cell trajectory with the same endpoint;
4. `MIN_JUMP_ENDPOINT_PATH` — any graph-geodesic endpoint realization.

A central question is whether

`LINE_PATH_FIBER` is a strict subset of `ENDPOINT_PATH_FIBER`.

## 2. Exact typing of origin, coordinate vertices, centers, and endpoints

The current foundation uses both triple-intersection coordinate vertices and integer-addressed circle-cell centers. Stage 0 showed that a center-transition word cannot act directly on `O_E`.

Produce a complete typed incidence diagram for one sector `S_ij`:

- origin triple vertex `O_E`;
- the three circle cells incident to `O_E`;
- their circle centers;
- native positive axes through triple-intersection vertices;
- integer axis tick vertices;
- integer-addressed cell centers;
- the object denoted by a native coordinate `(a,b,0)`;
- the object whose native length is `sqrt(a^2+b^2)`;
- the object at which a line path is considered to terminate.

You must answer explicitly:

`IS_NATIVE_LINE_ENDPOINT_A_COORDINATE_VERTEX_OR_A_CELL_CENTER_OR_A_TYPED_PAIR?`

If the current foundation is internally undertyped, provide the **minimal correction** preserving all user-frozen geometry.

Output:

`research_results/R061_STAGE1/R061_STAGE1_NATIVE_OBJECT_TYPING_THEOREM.md`

and machine-readable incidence data.

## 3. Derive the origin-incidence operator, do not guess it

Stage 0 introduced the schematic requirement

`Sigma_O : O_E -> one incident cell`.

Derive the exact native start semantics from the radius `1/sqrt(3)` overlapping-circle incidence.

Requirements:

- list the exactly three incident cells at the origin;
- derive their center-address relationship to the sector charts;
- determine whether a line in sector `S_ij` admits one, two, or three initial cell branches;
- no arbitrary tie-break;
- preserve symmetry/cyclic covariance;
- if the correct native path begins at a coordinate vertex event rather than a cell state, type that explicitly instead of forcing a fictitious cell at `O_E`.

Determine the exact affine equation connecting:

`formal component count -> native cell/vertex endpoint address`.

No guessed `+1`, `-1`, or half-step correction is permitted.

Output:

`R061_STAGE1_ORIGIN_INCIDENCE_AFFINE_ANCHOR_THEOREM.md`.

## 4. Trace-class candidate for native straightness

Test the following candidate, but do not assume it.

For a sector pair `(i,j)` define the formal commutation trace

`T_{a,b}^{(ij)} = [X_i^a X_j^b]`

under the equivalence relation generated by

`X_i X_j ~ X_j X_i`.

Its linearizations are exactly

`Lin(T_{a,b}^{(ij)}) = Sh_{a,b}(X_i,X_j)`.

Candidate semantics:

`ONE_NATIVE_LINE_IDENTITY = ONE_TRACE_CLASS`;

`NATIVE_LINE_PATHS = NATIVE_REALIZATIONS_OF_ALL_TRACE_LINEARIZATIONS`.

This candidate would explain why `(3,4)` has many paths while still being one length-5 line identity.

Audit whether the commutation relation has a native geometric meaning, e.g. local commuting squares/diamonds in the overlapping cell incidence, rather than being only a formal endpoint-count identity.

Mandatory tests:

- local `X_i X_j` vs `X_j X_i` endpoint agreement;
- single-cell state validity for both orders;
- whether the two paths bound/represent the same native straight micro-segment;
- composition under concatenation;
- scaling `(a,b)->(ka,kb)`;
- reversal at the carrier-transition level without creating native negative axes;
- cyclic covariance across all three `120 degree` right sectors.

Output:

`R061_STAGE1_TRACE_LINE_CANDIDATE_AUDIT.md`.

## 5. Classify the Stage 0 third-direction counterexample

The exact carrier fact remains:

for a selected start center, `X_i X_j` and one reverse-third-family nearest-center move can reach the same carrier center in the smallest `(1,1)` witness.

Stage 1 must classify that reverse-third path as one of:

- `SAME_LINE_TRACE_REPRESENTATIVE`;
- `SAME_ENDPOINT_DIFFERENT_LINE`;
- `CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE`;
- another explicitly defined native class.

Do not decide by jump count.

The decision must follow from the native line identity/straightness law derived in this stage.

Then generalize to arbitrary `(a,b)` and determine whether third-family moves ever belong to the same line fiber.

Output:

`R061_STAGE1_THIRD_DIRECTION_LINE_IDENTITY_CLASSIFICATION.md`.

## 6. Competing line-path classes — mandatory falsification matrix

Compare at least these candidates:

### C0 — FREE_SHUFFLE

All words in `Sh_{a,b}(X_i,X_j)`.

### C1 — TRACE_LINEARIZATIONS_WITH_NATIVE_INCIDENCE

Only those shuffle linearizations that survive the exact origin/cell incidence map.

### C2 — ALL_MINIMUM_JUMP_ENDPOINT_PATHS

All graph-geodesic cell paths to the same endpoint.

### C3 — ALL_SIMPLE_ENDPOINT_PATHS_WITHIN_SECTOR

All non-self-repeating admissible paths staying in the sector carrier.

### C4 — BALANCED_DIGITAL_LINE_SUBFIBER

A stricter balanced-prefix/Christoffel/Sturmian-style subset if native straightness forces one. Do not import a classical algorithm as truth; test only as a candidate.

### C5 — ANY_OTHER_NATIVE_CLASS FORCED BY INCIDENCE

If the geometry forces a different exact class, derive it.

For each candidate evaluate:

- exact algebraic generability from `(a,b)`;
- finite canonical definition;
- endpoint correctness;
- origin typing;
- single-cell admissibility;
- sector confinement;
- cyclic covariance;
- scaling covariance;
- concatenation behavior;
- reversal behavior;
- third-direction classification;
- compatibility with `3-4-5` multipath intuition;
- no use of jump count as native length.

Output a machine-readable candidate matrix.

## 7. Native line formula target

If one candidate survives, derive a corrected native formula of the form

`LINE_E^(ij)(N) = disjoint_union_{a^2+b^2=N} Realize_E(T_{a,b}^{(ij)})`

or a rigorously justified replacement.

`Realize_E` must include every required typing operation, including any origin incidence or affine chart map.

The formula must answer for `N=25`:

- which coordinate branches are generated;
- which nondegenerate branch represents `3-4-5`;
- exactly how many native line-path representatives the `(3,4)` branch has;
- the explicit path IDs or compressed exact representation;
- why omitted same-endpoint routes are not members of the same line fiber.

If no candidate survives, freeze the minimal impossibility result instead of inventing a tie-break.

## 8. Mandatory exact examples

At minimum audit:

- `N=0`;
- `N=1`;
- `N=2`, branch `(1,1)`;
- `N=5`, branch `(1,2)` / `(2,1)` where applicable;
- `N=25`, `(3,4)` and `(4,3)`;
- `N=65`, multiple coordinate decompositions;
- `N=169`, `289`, `625`, `841`, `4225`;
- scaled triples `(6,8,10)`, `(9,12,15)`, `(10,24,26)`, `(16,30,34)`, `(40,42,58)`.

Also test nonrepresentable `N` values.

## 9. Deterministic validation

After the structural definition is fixed, build a deterministic checker.

Minimum computational requirements:

- explicit native replay for all surviving candidate paths with `a+b<=18`;
- exact compressed counting/automaton checks through `a+b<=256` where meaningful;
- all three sectors;
- all origin-incidence branches;
- no float dependence for combinatorial decisions;
- preserve exact counterexamples for every rejected candidate;
- regression check Stage 0 coordinate/shuffle hashes;
- detect duplicate physical trajectories under chart gluing;
- detect any path containing a non-neighbor cell transition;
- detect any accidental simultaneous multi-cell state.

Proof/typing dominates checker evidence.

## 10. Acceptance gates

The stage passes only if all required gates for the selected native class are true:

1. `NATIVE_OBJECT_TYPING_COMPLETE`;
2. `ORIGIN_INCIDENCE_EXACT`;
3. `AFFINE_ADDRESS_ANCHOR_EXACT`;
4. `LINE_IDENTITY_DEFINED_INDEPENDENTLY_OF_ENDPOINT_ONLY`;
5. `LINE_PATH_CLASS_FINITE_AND_CANONICAL`;
6. `LINE_PATHS_SINGLE_CELL_ADMISSIBLE`;
7. `SAME_ENDPOINT_VS_SAME_LINE_CLASSIFIED`;
8. `THIRD_DIRECTION_COUNTEREXAMPLE_RESOLVED_BY_TYPING_NOT_BY_PATCH`;
9. `THREE_SECTOR_COVARIANCE_PASS`;
10. `SCALING_AND_CONCATENATION_AUDIT_PASS`;
11. `N25_3_4_5_NATIVE_PATH_FIBER_EXACT`;
12. `NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE`;
13. `DETERMINISTIC_VALIDATION_PASS`.

If the trace candidate fails but another exact native class passes, report that result.

If no class passes, set

`NATIVE_LINE_PATH_FIBER_DERIVABLE_FROM_CURRENT_FOUNDATION = false`

and preserve the minimal obstruction.

## 11. Stop condition

Stop for Driver review after Stage 1.

Do not open Stage 2 automatically from the researcher branch.
