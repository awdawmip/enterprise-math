# R059D Stage AD — TRIANGULAR COVERAGE BRC CIRCLE RESOLVE

Task-ID: `RS-R059D-STAGE-AD-TRIANGULAR-COVERAGE-BRC-CIRCLE-RESOLVE`
Generation: `R059D`
Stage: `AD`
Status: `DRIVER_APPROVED_TASKBOOK`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Researcher-ID: `EM-R059D-3F7C42`
Date: `2026-08-17`

## 0. Mission

Construct and compare exact discrete BRC bridge candidates that map a fixed-length circular source object in the **垂直坐标系** (`ORTHOGONAL_COORDINATE_SYSTEM`) into a closed boundary/orbit in the **进取坐标系** (`ENTERPRISE_COORDINATE_SYSTEM`).

The central route is:

`ORTHOGONAL_FIXED_LENGTH_ORBIT`
`-> TRIANGULAR_CELL_COVERAGE_FIELD`
`-> FRONTIER / SOFT_STATE`
`-> RESOLVE_RULE`
`-> ENTERPRISE_BINARY_OCCUPANCY`
`-> CLOSED_ENTERPRISE_BOUNDARY`
`-> ROTATING_SEGMENT_ENDPOINT_ORBIT_CANDIDATE`.

This stage is inspired by computer-graphics anti-aliasing and rasterization, especially:

- subcell / multisample coverage;
- triangular-pixel coverage;
- error accumulation / error diffusion ideas analogous to Wu/Bresenham-style rasterization;
- triangle edge-function / incremental rasterization ideas.

These are conceptual inspirations only. Do not copy a graphics algorithm and rename it BRC.

The scientific question is:

> Can a finite-resolution coverage + resolve mechanism produce a deterministic, symmetric, closed, precision-stable Enterprise-coordinate representation of a fixed-length rotating segment without directly inserting the target lattice path?

## 0.1 Module completion estimate

Before Stage AD:

- Enterprise coordinate-system definition: `~95%` for the present plane carrier;
- BRC source/target bridge semantics: `~30%`;
- native Enterprise circle generator: `~5%` (definition by fixed-length orbit only; no update law);
- triangular coverage bridge: `0%` frozen;
- residual-based resolve rule: `0%` frozen;
- cross-precision circle consistency: `0%` established.

Target after Stage AD:

- Enterprise coordinate-system definition: unchanged;
- BRC bridge semantics: `50–70%` on the planar fixed-length-orbit problem;
- native Enterprise circle generator: `30–60%` depending on closure and uniqueness results;
- triangular coverage bridge: `70–100%` as a tested prototype;
- residual-based resolve rule: `50–100%` depending on gate performance;
- cross-precision consistency: `20–60%` diagnostic/provisional.

Progress vector:

`enterprise-coordinate +0 / brc-bridge +30 / circle-generator +40 / coverage-resolve +70 / precision-consistency +35 / physics +0`

Do not expand into six-dimensional world dynamics, physical force laws, π calibration, or continuum-field physics in this stage.

---

## 1. Frozen terminology and authority

Read and obey:

- `PROJECT_DEFINITION.zh-CN.md`
- `PROJECT_DEFINITION.md`
- `project_definition.json`
- `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`
- `definitions/enterprise_coordinate_system_and_brc_bridge.json`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_20260816.md`

Terminology:

- `ENTERPRISE_COORDINATE_SYSTEM` = 进取坐标系;
- `ORTHOGONAL_COORDINATE_SYSTEM` = 垂直坐标系;
- `CLASSICAL_2D_COMPATIBILITY_VIEW` = 经典二维兼容图示;
- `BRC_COLLAPSE_BRIDGE` = the bridge relation/algorithm from source coordinate semantics to target coordinate semantics.

Do not use deprecated informal visualization terminology for the Enterprise coordinate system.

Historical R059D W/X/Y/Z/AA and Stage AC artifacts remain immutable.

Stage AC is not an area theorem for this task. Its useful combinatorial constructions may be inspected only after the Stage AD native data structures are defined, and any reused count must be retyped explicitly.

---

## 2. What “circle” means in this stage

Do not begin from an Enterprise circle equation.

Source-side fixed-length orbit:

- choose center `O`;
- choose a source-system segment of fixed source length `r`;
- fix one endpoint at `O`;
- allow the free endpoint to range through all source directions while preserving source length `r`.

The source orbit is the teacher object:

`ORTHOGONAL_FIXED_LENGTH_ORBIT(O,r)`.

For source-side exact classification only, the standard compatibility identity

`x^2 + y^2 = r^2`

is allowed.

This identity belongs exclusively to the `ORTHOGONAL_COORDINATE_SYSTEM` / compatibility side.

It is forbidden to declare

`x^2+y^2=r^2`

or its triangular-chart rewrite to be the native Enterprise length law.

The Stage AD target is not “prove the classical circle equation.”

The Stage AD target is to discover/test a discrete resolve mechanism that converts the source fixed-length orbit into an Enterprise-coordinate closed boundary/orbit.

---

## 3. Common comparison frame

Use one fixed `CLASSICAL_2D_COMPATIBILITY_VIEW` only as a bridge-computation frame.

Freeze:

- source `+x` aligned with Enterprise `+u`;
- Enterprise adjacent axis direction shown at the frozen `60°` compatibility direction;
- source `+y` remains the classical orthogonal `90°` direction.

The two coordinate systems are therefore distinct charts over the same comparison plane.

The common comparison frame is an implementation/bridge layer. It does not reduce the Enterprise plane to two native dimensions.

A triangular implementation chart may be used for exact computation.

If the chart uses lattice indices `(a,b)` with compatibility embedding

`X=a+b/2`,

`Y=(sqrt(3)/2)b`,

then the source Euclidean squared-distance teacher evaluates as

`X^2+Y^2 = a^2 + a b + b^2`.

This identity may be used only to classify source-side sample positions relative to the source circle.

Hard rule:

`A2/EISENSTEIN_QUADRATIC_FORM_AS_ENTERPRISE_NATIVE_METRIC = false`.

---

## 4. Triangular cells and coverage field

Build the Enterprise triangular cell complex in the compatibility frame.

Each elementary triangle must have:

- stable `CELL_ID`;
- orientation tag `UP/DOWN` or equivalent neutral relational tag;
- exact vertices in rational/triangular coordinates;
- adjacency to neighboring elementary triangles;
- parent coarse cell under declared refinement, where applicable.

For each source circle `(O,r)` and each coverage precision layer `s`, compute an exact or integer-rational approximation to the disk coverage of each triangular cell:

`C_s(tau) = covered_subsamples(tau) / total_subsamples(tau)`.

Required:

`0 <= C_s(tau) <= 1`.

Preferred implementation:

- deterministic barycentric / triangular subdivision;
- integer/rational arithmetic;
- no floating-point dependency in the theorem/checker path.

A sub-sample may be classified inside the source disk using exact scaled integer comparison against the source teacher circle.

Store integer pair:

`covered_subsamples : total_subsamples`

as primary data.

Do not store only decimal coverage.

Required coverage precision levels at minimum:

`s in {4,8,16,32}`

or an equivalent monotone subdivision sequence.

Use `s=64` where computationally cheap.

---

## 5. Frontier and soft-state definition

For each `(r,s)`, classify cells:

- `FULL_IN`: coverage = 1;
- `FULL_OUT`: coverage = 0;
- `FRONTIER`: `0 < coverage < 1`.

The frontier is the primary anti-aliased bridge object.

Record:

- all frontier `CELL_ID`s;
- coverage rational for each;
- adjacency among frontier cells;
- six-sector / reflection images;
- connected components;
- local source-inside/source-outside neighboring states.

Do not yet call the frontier itself the Enterprise circle.

The frontier is a soft-state boundary carrier that must be resolved.

---

## 6. Three required resolve arms

All arms must receive the same source circle and the same coverage field.

### Arm N — `NEAREST_CELL_BASELINE`

A compatibility baseline only.

Resolve cell state using a single representative sample, preferably the deterministic cell centroid or another pre-frozen representative.

This arm may use the source teacher classification at that representative point.

It is not expected to be the final BRC rule.

Its purpose is to quantify what is gained by coverage and residual memory.

### Arm C — `COVERAGE_THRESHOLD`

Resolve independently by a frozen threshold:

`B(tau)=1 iff C_s(tau) >= theta`.

Freeze `theta=1/2` before reading performance.

Do not retune threshold by radius or sector.

Optional additional thresholds may be tested only as secondary controls and must be predeclared.

### Arm R — `ACCUMULATED_RESIDUAL_RESOLVE`

Construct an error-preserving resolver inspired by anti-aliased line/circle rasterization.

The core requirement is:

> fractional coverage not selected at one local step must remain as explicit residual state and influence later binary decisions.

A candidate minimal form is allowed:

`e_{k+1} = e_k + c_k - b_k`

with

- `c_k` = rational soft coverage contribution;
- `b_k in {0,1}` = resolved decision;
- `e_k` = retained residual.

But this exact recurrence is a candidate, not a mandatory final form.

The researcher may test other deterministic local residual recurrences if they are predeclared before scoring and do not import the target path.

The resolver must expose every signed residual update.

No hidden state.

---

## 7. Ordering problem for residual resolve

Residual algorithms require an update order. Order dependence is a scientific issue, not an implementation detail.

Test at least:

1. sector scan from `+u` anchor toward the adjacent Enterprise axis;
2. reversed sector scan;
3. a symmetry-derived mirrored scan;
4. if cheap, at least one alternative native frontier traversal order.

Required outputs:

- whether resolved occupancy is identical;
- whether final boundary is identical;
- whether only traversal orientation reverses;
- whether residual trace differs while endpoint set remains invariant.

If Arm R depends materially on arbitrary scan order, report:

`ORDER_DEPENDENT_RESOLVE`.

Do not silently choose the order that best matches the source circle.

---

## 8. Radius registry

Primary exact radius registry:

`r = 1..24`.

If cheap, extend through `r=64`.

Required discriminator radii include:

`1,2,3,4,5,8,13,21`.

The registry must be frozen before final scoring.

Do not remove difficult radii.

---

## 9. One-sector-first protocol

The first development domain is one adjacent Enterprise-axis sector, from the `+u` anchor direction to its adjacent Enterprise-axis direction in the compatibility view.

Develop and debug all three resolver arms on this single `60°` sector first.

Required one-sector gates:

- anchor cell/state is deterministic;
- terminal adjacent-axis state is deterministic;
- frontier between anchors is connected or exact failure is reported;
- resolver produces no impossible jumps across nonadjacent target cells;
- reverse traversal reproduces the same endpoint set if the rule claims reversibility;
- mirror sector gives the symmetry-transformed result.

Only after the one-sector gates are stable may the construction be propagated around all six sectors.

---

## 10. Full-circle construction

Construct six sector images using the frozen Enterprise-axis symmetry.

Do not independently optimize each sector.

One resolver rule must propagate to all sectors.

The full resolved boundary must be audited for:

### 10.1 Closure

- exactly closed boundary;
- no open endpoints;
- no gaps between sectors;
- no duplicated disconnected loops unless explicitly explained.

### 10.2 Connectivity

Preferred target:

`ONE_CONNECTED_BOUNDARY_COMPONENT`.

If small radii naturally create a different topology, record exact radius and mechanism.

### 10.3 Six-sector symmetry

Audit exact D6/cyclic-reflection compatibility of the resolved Enterprise boundary.

### 10.4 Inversion symmetry

Opposite directions must map consistently under global sign inversion.

### 10.5 Locality

Consecutive boundary states must be locally adjacent under the declared target adjacency rule.

No teleporting raster path.

---

## 11. Fixed-length interpretation gate

Stage AD does not yet assume a final native Enterprise distance formula.

Therefore do not certify fixed length by secretly evaluating a target-side Euclidean norm.

Instead use a typed bridge statement:

A resolved boundary state is `SOURCE_LENGTH_COMPATIBLE(r,s)` if its corresponding triangular cell/frontier carrier intersects or is selected from the soft coverage generated by the source fixed-length orbit of radius `r` at precision `s`.

Audit:

- every selected target boundary state has declared source-orbit provenance;
- no selected state is created without source coverage/frontier support unless the resolver's residual rule explicitly permits a local compensation step and that step is logged;
- compensation steps must return bounded cumulative coverage error.

A native Enterprise equal-length theorem remains a later target unless it falls out without importing a metric premise.

---

## 12. Coverage conservation / resolve error

For every resolver arm and sector/full circle, record exact coverage discrepancy.

At minimum:

`E_total = sum_tau (B(tau) - C_s(tau))`

over the declared resolve domain.

Also record prefix/cumulative error for ordered resolvers.

For residual Arm R, search for exact bounded-error structure such as

`|E_prefix(k)| <= constant`

or a sharper native bound.

Do not force a specific bound.

If a simple invariant is discovered, prove it symbolically from the recurrence.

This is a major target because a bounded residual may explain the historical BRC staircase jump timing.

---

## 13. Cross-precision tests

Keep two precision concepts typed separately:

1. `COVERAGE_SAMPLING_PRECISION` — subcell numerical coverage resolution;
2. `NATIVE_SPATIAL_REFINEMENT` — actual refinement of the Enterprise triangular cell complex.

### 13.1 Coverage sampling convergence

For fixed native lattice and radius, compare `s=4,8,16,32,(64)`.

Require exact tables of:

- frontier changes;
- resolved-boundary changes;
- residual changes;
- stabilization radius/precision if observed.

### 13.2 Native spatial refinement control

For selected radii, refine the triangular lattice by integer factors, preferably

`h in {2,3,4}`.

Scale the source radius accordingly in the common comparison frame.

Resolve at fine scale, then coarse-grain deterministically back to the base lattice.

Compare with direct base-lattice resolution.

Do not assume exact equality.

Return one of:

- `EXACT_CROSS_PRECISION_CONSISTENCY`;
- `BOUNDED_CROSS_PRECISION_DIFFERENCE`;
- `CROSS_PRECISION_INCONSISTENT`.

Record exact mismatch cells.

---

## 14. Circle/orbit extraction

From the resolved binary disk/boundary, derive a canonical boundary walk.

Start from the frozen `+u` anchor and traverse one orientation.

Record:

`ENTERPRISE_CIRCLE_ORBIT_CANDIDATE(r,s,resolver)`

as a sequence of target boundary states/cells.

For every state record:

- state/CELL_ID;
- predecessor/successor;
- sector id;
- coverage provenance;
- residual before/after if applicable;
- source teacher radius;
- precision layer;
- symmetry images.

The boundary walk is a candidate free-endpoint orbit for a fixed-length rotating segment.

Do not call it the final native circle theorem unless all required gates pass and no unresolved arbitrary choices remain.

---

## 15. Relationship to historical R059D staircase/frontier work

Only after Stage AD resolver data are independently generated, compare against historical R059D results.

Required questions:

1. Does the resolved boundary produce a binary staircase naturally?
2. Can historical `a_{n+1}-a_n in {0,1}` behavior be reinterpreted as a raster/resolve jump word?
3. Does `frontier` correspond to the current soft coverage frontier?
4. Does an explicit residual state supply the previously missing jump discriminator?
5. Do old reflection/orbit counts predict anything after the new residual state is included?
6. Is there an exact bridge theorem, or only a qualitative analogy?

Historical results may not be edited or retroactively strengthened.

---

## 16. Graphics-algorithm inspiration firewall

Allowed inspirations:

- coverage masks;
- multisampling;
- triangular cell coverage;
- signed/accumulated local error;
- incremental edge tests;
- deterministic raster traversal.

Forbidden shortcuts:

- copy a standard circle rasterizer and declare it native BRC;
- use a precomputed classical circle pixel path as the target sequence;
- choose threshold/scan order per radius after seeing target fit;
- use anti-alias opacity as if it were physical probability;
- infer a native Enterprise metric from the source-side Euclidean teacher without a proof.

Keep:

`GRAPHICS_METHOD = INSPIRATION / CONTROL`

not

`GRAPHICS_METHOD = PROOF_OF_ENTERPRISE_ONTOLOGY`.

---

## 17. Deterministic scoring and comparison

Do not rank methods by a single visual similarity score.

For each arm report a gate vector:

- `ANCHOR_PASS`
- `SECTOR_CONNECTIVITY_PASS`
- `FULL_CLOSURE_PASS`
- `ONE_COMPONENT_PASS`
- `D6_SYMMETRY_PASS`
- `INVERSION_PASS`
- `LOCALITY_PASS`
- `ORDER_INDEPENDENCE_STATUS`
- `COVERAGE_ERROR_BOUND_STATUS`
- `SAMPLING_PRECISION_STABILITY_STATUS`
- `NATIVE_REFINEMENT_CONSISTENCY_STATUS`
- `SOURCE_PROVENANCE_PASS`

Retain all failures.

If Arm R is best on some gates and worse on others, report the vector; do not collapse to one winner score unless a later Driver stage defines a decision functional.

---

## 18. Required artifacts

Freeze at least:

1. `R059D_STAGE_AD_SOURCE_CIRCLE_TEACHER_PROTOCOL.json`
2. `R059D_STAGE_AD_TRIANGULAR_CELL_COMPLEX.json`
3. `R059D_STAGE_AD_COVERAGE_PROTOCOL.json`
4. `R059D_STAGE_AD_COVERAGE_FIELD_REGISTRY.json`
5. `R059D_STAGE_AD_FRONTIER_REGISTRY.json`
6. `R059D_STAGE_AD_NEAREST_CELL_RESOLVER.json`
7. `R059D_STAGE_AD_COVERAGE_THRESHOLD_RESOLVER.json`
8. `R059D_STAGE_AD_ACCUMULATED_RESIDUAL_RESOLVER.json`
9. `R059D_STAGE_AD_RESIDUAL_TRACE_REGISTRY.json`
10. `R059D_STAGE_AD_ONE_SECTOR_AUDIT.json`
11. `R059D_STAGE_AD_FULL_CIRCLE_BOUNDARY_REGISTRY.json`
12. `R059D_STAGE_AD_D6_CLOSURE_SYMMETRY_AUDIT.json`
13. `R059D_STAGE_AD_COVERAGE_ERROR_LEDGER.json`
14. `R059D_STAGE_AD_COVERAGE_PRECISION_AUDIT.json`
15. `R059D_STAGE_AD_NATIVE_REFINEMENT_AUDIT.json`
16. `R059D_STAGE_AD_CIRCLE_ORBIT_CANDIDATES.json`
17. `R059D_STAGE_AD_HISTORICAL_STAIRCASE_BRIDGE_LEDGER.json`
18. `R059D_STAGE_AD_RESOLVER_GATE_MATRIX.json`
19. deterministic checker source
20. deterministic checker output
21. report
22. manifest
23. frozen checkpoint

All artifacts under:

`research_results/R059D_STAGE_AD/`.

---

## 19. Checker hard negatives

Checker must reject at minimum:

- `CLASSICAL_CIRCLE_PATH_USED_AS_TARGET_LOOKUP`;
- `SOURCE_EUCLIDEAN_METRIC_PROMOTED_TO_ENTERPRISE_NATIVE_METRIC`;
- `A2_RANK2_PROMOTED_TO_ENTERPRISE_PLANE_DIMENSION`;
- `FLOAT_ONLY_COVERAGE_WITHOUT_EXACT_REPLAY`;
- `RADIUS_SPECIFIC_THRESHOLD_TUNING`;
- `RADIUS_SPECIFIC_SCAN_ORDER_TUNING`;
- `DISCONNECTED_BOUNDARY_IGNORED`;
- `SECTOR_GAP_IGNORED`;
- `D6_ASYMMETRY_IGNORED`;
- `NONLOCAL_BOUNDARY_JUMP_IGNORED`;
- `RESIDUAL_STATE_HIDDEN`;
- `ORDER_DEPENDENCE_HIDDEN`;
- `CROSS_PRECISION_MISMATCH_HIDDEN`;
- `ANTI_ALIAS_ALPHA_CALLED_PHYSICAL_PROBABILITY`;
- `HISTORICAL_R059D_ARTIFACT_MUTATED`;
- `VISUAL_MATCH_PROMOTED_TO_THEOREM`.

---

## 20. Required disposition

Return exactly one primary disposition:

- `TRIANGULAR_COVERAGE_BRC_CIRCLE_RESOLVE_CANDIDATE_ESTABLISHED`
- `ACCUMULATED_RESIDUAL_RESOLVE_PASSES_PRIMARY_CIRCLE_GATES`
- `COVERAGE_BRIDGE_ESTABLISHED__RESOLVE_RULE_UNDERDETERMINED`
- `NO_TESTED_RESOLVE_RULE_PASSES_CIRCLE_GATES`
- `SOURCE_TARGET_OVERLAY_REQUIRES_ADDITIONAL_BRIDGE_STRUCTURE`
- `SEMANTIC_HARD_STOP`

Also report separately:

- `COVERAGE_FIELD_STATUS`
- `FRONTIER_STATUS`
- `NEAREST_CELL_STATUS`
- `COVERAGE_THRESHOLD_STATUS`
- `ACCUMULATED_RESIDUAL_STATUS`
- `FULL_CIRCLE_CLOSURE_STATUS`
- `D6_SYMMETRY_STATUS`
- `ORDER_DEPENDENCE_STATUS`
- `CROSS_PRECISION_STATUS`
- `HISTORICAL_BRC_BRIDGE_STATUS`

Then stop for Driver review.

---

## 21. Git / ownership discipline

Work only on:

`research/r059d-stage-ad-triangular-coverage-circle-bridge`

Researcher identity:

`EM-R059D-3F7C42`.

Do not modify frozen prior-stage artifacts.

Checkpoint policy:

- checkpoint after source teacher + triangular coverage field are frozen;
- checkpoint after the three resolver implementations and one-sector audit;
- checkpoint after full-circle closure/symmetry audit;
- checkpoint after precision/refinement audit;
- final checkpoint for report/manifest/checker.

At completion provide exact:

- branch head SHA;
- frozen parent/taskbook source SHA;
- checker digest;
- checkpoint digest;
- manifest digest.

Do not merge to `main` without Driver review.
