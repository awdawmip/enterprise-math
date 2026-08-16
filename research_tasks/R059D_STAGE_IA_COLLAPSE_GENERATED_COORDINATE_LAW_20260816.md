# R059D Stage IA — COLLAPSE-GENERATED COORDINATE LAW / UNIQUE TRACEABLE INTEGER CELL COORDINATES

Task-ID: `RS-R059D-STAGE-IA-COLLAPSE-GENERATED-COORDINATE-LAW`
Generation: `R059D`
Stage: `IA`
Status: `DRIVER_APPROVED_TASKBOOK`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Researcher-ID: `EM-R059D-C7A21`
Date: `2026-08-16`

## 0. Driver correction — one problem, not two

This task supersedes the separated-coordinate task

`RS-R059D-COORD-IA-MAIN-COORDINATE-UNIQUE-ADDRESS`.

The corrected scientific statement is:

> **The collapse mechanism is itself the coordinate-generation mechanism.**

Do not first choose a numerical coordinate system and then test collapse inside it.
Do not first solve collapse and later attach coordinates as an independent bookkeeping layer.

The object to identify is one law whose execution simultaneously:

1. receives the pre-collapse relational/count state of a crystal cell;
2. resolves noninteger / multibranch pre-collapse values into stored integers;
3. thereby assigns that cell its numerical coordinate;
4. gives the same stored coordinate whenever the same cell is reached through another legal history;
5. separates distinct cells sufficiently to serve as a unique address;
6. carries an exact derivation certificate showing how the coordinate was generated.

Coordinate generation is therefore the primary empirical/mathematical test of the collapse law.

## 1. What may exist before coordinates

A coordinate-free **cell identity scaffold** is allowed only so the experiment can know when two histories reach the same combinatorial cell.

Use the Stage-W-REISSUE2 A2/C6 scaffold `C[a,b]` (or an exactly equivalent coordinate-free naming of the same adjacency graph) strictly as:

- `CELL_ID`;
- adjacency incidence;
- path recoalescence oracle;
- cyclic/reflection/inversion action on cell identities.

It is NOT the stored numerical coordinate system.
Its `(a,b)` implementation labels are not physical or mathematical output coordinates.

This separation is mandatory because otherwise coordinate uniqueness would be proved by presupposing the target coordinate.

## 2. Frozen prior findings to consume, not redo

Preserve the following accepted R059D facts/negative controls:

### W first-round negative control

Homogeneous additive stored-coordinate increments trivialize the experiment toward `p=1` and are not native premises.

Do not assume:

- named direction has a fixed stored-coordinate increment everywhere;
- stored coordinate is path-sum of first-shell stored increments;
- stored coordinate map is a group homomorphism from CELL_ID scaffold.

### W REISSUE2

- `CELL_COORDINATES_ARE_INTEGER_ONLY`.
- Pre-collapse algebraic values such as radicals may exist, but are never stored coordinates.
- Same-cell path consistency and distinct-cell injectivity are legitimate atlas constraints.
- Multiple root orders / completion rules survived the tested atlas; square root was not uniquely selected.

### X

In the frozen cyclic/typed-reflection subcase, the pure-axis symmetric coordinate family can be written

`C_u(n)=(n,-a_n,-a_n)`

with

`a_0=0`, `a_1=1`, and `a_{n+1}-a_n in {0,1}`.

The jump positions were not identified by the frozen atlas constraints alone.

### Y/Z

Crossing/frontier counts are readouts, not yet coordinate-generating mechanisms. In particular, odd frontier size or square/triangular arithmetic must not be inserted as the collapse rule without an independent coupling proof.

### AA

Stage AA may remain frozen for Driver review, but its result is not a premise of Stage IA unless separately accepted and explicitly routed later.

## 3. Hard coordinate-generation observations

Freeze only the minimum observations already justified by the line:

- origin CELL_ID `O` stores `(0,0,0)`;
- one `+u` neighbor stores `(1,-1,-1)`;
- all stored coordinate components are integers.

Cyclic first-shell values

`+v -> (-1,1,-1)` and `+w -> (-1,-1,1)`

may be studied as an explicitly declared symmetry subcase, not silently as universal truth.

Negative-direction values are likewise derived/audited through the declared reflection/inversion semantics rather than assumed globally unless already frozen by the chosen subcase.

## 4. The coordinate generator is a collapse operator

Define a candidate coordinate-generating collapse mechanism abstractly as

`K : PRECOLLAPSE_STATE -> STORED_INTEGER_STATE`

where the stored integer state contains the triaxial coordinate

`Gamma(cell)=(U,V,W) in Z^3`.

`K` is not permitted to read the unknown target coordinate as input.

A candidate `K` may read only explicitly declared pre-coordinate information, such as:

- CELL_ID-local adjacency type;
- exact path/event count ledgers that are proved cell-state admissible;
- current legal pre-collapse algebraic values;
- a finite declared internal collapse state if such state is independently justified;
- already generated neighboring stored states only when the update rule is noncircular and replayable.

Every theorem-critical input to `K` must be typed.

## 5. Coordinate-generation law requirements

A successful collapse law must satisfy all of the following simultaneously.

### IA-C1 — TOTAL GENERATION

Every cell in the declared tested atlas receives at least one legal stored integer triple.

### IA-C2 — SAME-CELL CONFLUENCE

If histories `P` and `Q` reach the same CELL_ID, collapse replay must give the same final stored coordinate:

`Gamma_P(cell)=Gamma_Q(cell)`.

If `K` has internal state, the final state relevant to future coordinate generation must also be confluent or its nonconfluence must be proved observationally irrelevant.

### IA-C3 — DISTINCT-CELL SEPARATION

Within the declared chart, distinct CELL_IDs must not collapse to the same stored coordinate unless the candidate explicitly proposes a noninjective coordinate ontology. The primary target is injective addressing.

### IA-C4 — LOCAL REPLAYABILITY

The coordinate must be reproducible from the frozen pre-coordinate evidence and collapse rule. No per-cell arbitrary lookup table is allowed as a positive mechanism.

### IA-C5 — SYMMETRY COVARIANCE

Cyclic/reflection/inversion transformations that are declared on the CELL_ID scaffold must induce corresponding typed transformations of generated coordinates. The law may not privilege an axis name unless the input state itself breaks that symmetry.

### IA-C6 — INTEGER STORAGE

Only integer triples are stored. Algebraic/radical values remain pre-collapse evidence.

### IA-C7 — EXTENSION CONSISTENCY

A coordinate assignment accepted at radius `r` must remain unchanged when the atlas is extended to radius `r+1`. A rule that repeatedly rewrites already frozen coordinates as the search radius grows is not a stable coordinate-generation law.

### IA-C8 — TRACE CERTIFICATE

For each generated cell coordinate preserve an exact certificate:

`CELL_ID -> admitted histories/evidence -> precollapse state -> legal integer branch set -> eliminated branches with reasons -> selected branch -> stored coordinate`.

Traceability is part of the coordinate law, not optional logging.

## 6. No arbitrary staircase as an answer

Stage X proved that an arbitrary binary staircase can satisfy the earlier coordinate atlas constraints.

Therefore Stage IA MUST distinguish:

- `GLOBAL_ASSIGNMENT_EXISTS`;
- `UNIFORM_COLLAPSE_GENERATOR_EXISTS`.

A table that says independently for every `n` whether `a_{n+1}-a_n=0` or `1` is not by itself a collapse mechanism.

The positive target is a rule that computes the branch from pre-coordinate state.

At minimum test whether the surviving families can be realized by:

1. memoryless deterministic local collapse;
2. finite-state deterministic collapse with explicitly bounded state;
3. state derived solely from native relational/count evidence;
4. rules requiring an external preprogrammed jump schedule.

Classify family 4 as `COORDINATE_ASSIGNMENT_WITHOUT_NATIVE_GENERATOR`, not success.

## 7. Reuse the event-count ledger, but do not assume a root law

Use the Stage-W-REISSUE2 elementary event ledger as one admissible source of pre-collapse information:

- direct signed counts `D_i`;
- transverse count balances;
- split nonnegative transverse counts when needed.

Do not assume square root, cube root, floor, ceiling, nearest, midpoint, parity alternation, or a frontier formula as the native collapse law.

A small predeclared candidate registry may contain these only as controls/comparators.

The researcher may derive a new candidate only from an explicit relational/count invariant identified before scoring that candidate.

## 8. Stage IA-0 — rebuild the coordinate problem as constraint + generator

Construct an atlas of CELL_IDs with enough multi-path cells and pure-axis depth to expose generator behavior.

Minimum:

- complete CELL_ID radius 4;
- pure-axis rays through at least `n=64` if cheap;
- all shortest path words for radius <=4;
- selected nonshortest reversal/loop paths;
- exact cyclic/reflection images.

For every cell, store all pre-coordinate evidence independently of the unknown coordinate.

## 9. Stage IA-1 — pure-axis coordinate generation

In the cyclic symmetric subcase, study

`Gamma(+u^n)=(n,-a_n,-a_n)`

only as a derived coordinate form.

Reconfirm the frozen binary-step admissibility without redoing Stage X as discovery work, then ask the new question:

> Which binary branch sequences are actually generated by one uniform collapse mechanism from the available pre-coordinate state?

For every candidate mechanism report:

- exact input signature at each `n`;
- whether two different `n` can have the same input signature but require different branch decisions;
- minimal internal state needed to reproduce the sequence;
- whether the rule is axis-covariant;
- whether the rule is genuinely predictive rather than a coded lookup table.

## 10. Stage IA-2 — mixed-cell global coordinate generation

Propagate each surviving collapse generator to off-axis cells.

Mandatory cell families include:

- `+u,+v` and reordered path;
- `+u,+w` and reordered path;
- `+u,-v`;
- `+u,+u,+v`;
- cyclic images;
- cells with three or more distinct shortest histories;
- paths with inserted exact reversal loops.

Require one generated coordinate per CELL_ID across every history.

Do not repair a conflict by choosing a preferred path.

## 11. Stage IA-3 — coordinate uniqueness as a law-selection test

For the bounded atlas, enumerate all collapse generators within the predeclared rule class that satisfy IA-C1..IA-C8.

The primary scientific question is not merely whether at least one coordinate assignment exists.

It is:

`How many inequivalent coordinate-generating collapse laws survive?`

Freeze one of:

- `UNIQUE_COLLAPSE_COORDINATE_GENERATOR_WITHIN_DECLARED_CLASS`;
- `FINITE_MULTIPLE_COLLAPSE_COORDINATE_GENERATORS_SURVIVE`;
- `INFINITE_OR_PARAMETRIC_GENERATOR_FAMILY_SURVIVES`;
- `NO_GENERATOR_IN_DECLARED_CLASS`.

If multiple generators survive, identify the smallest exact witness where they assign different coordinates to the same CELL_ID.

## 12. Stage IA-4 — information insufficiency / missing observable theorem

If the current native state cannot determine a unique generator, do not add a formula by taste.

Instead prove as strong a non-identifiability statement as possible.

Preferred form:

> Two different deterministic collapse-coordinate generators consume exactly the same currently frozen pre-coordinate observables on all states in a declared class, satisfy all frozen symmetries/consistency laws, yet assign different legal coordinates somewhere.

Then characterize what *kind* of additional information could distinguish them, for example:

- one additional relational local-state bit;
- finite memory of a declared event type;
- cross-axis coupling invariant;
- refinement/precision relation;
- another independently derived native observable.

Do not name a preferred missing observable unless the evidence supports it.

This is a successful Stage-IA result if exact: it tells us what the coordinate-generating collapse law still lacks.

## 13. Stage IA-5 — traceable coordinate registry

If a unique or preferred-by-proof generator is obtained, freeze for each tested CELL_ID:

- generated integer coordinate;
- collapse certificate;
- predecessor evidence;
- all legal histories tested;
- symmetry images;
- exact replay digest.

Verify that extending the atlas does not alter earlier coordinates.

If uniqueness is not obtained, freeze the multibranch coordinate registry instead; never choose one branch silently.

## 14. Critical anti-circularity controls

The checker must reject at least:

- `MAIN_COORDINATE_PREASSIGNED_BEFORE_COLLAPSE`;
- `A2_CELL_ID_LABEL_USED_AS_NUMERICAL_COORDINATE`;
- `LAMBDA_QUOTIENT_ADDRESS_USED_TO_SELECT_COLLAPSE_BRANCH`;
- `HOMOGENEOUS_STORED_INCREMENT_ASSUMED`;
- `PATH_SUM_OF_FIRST_SHELL_COORDINATES_ASSUMED`;
- `ARBITRARY_BINARY_STAIRCASE_CALLED_COLLAPSE_LAW`;
- `PER_CELL_LOOKUP_TABLE_CALLED_NATIVE_GENERATOR`;
- `PREFERRED_PATH_USED_TO_HIDE_NONCONFLUENCE`;
- `SQUARE_ROOT_ASSUMED`;
- `FLOOR_OR_CEILING_ASSUMED`;
- `ODD_FRONTIER_COUNT_ASSUMED_TO_DRIVE_COORDINATE`;
- `COORDINATE_COLLISION_IGNORED`;
- `ATLAS_EXTENSION_REWRITES_PRIOR_COORDINATES`;
- `FLOATING_POINT_STORED_COORDINATE`;
- `EUCLIDEAN_METRIC_USED_TO_BREAK_BRANCH_TIE`.

## 15. Required artifacts

Freeze at least:

1. `R059D_STAGE_IA_CELL_ID_VS_COORDINATE_SEMANTICS.json`
2. `R059D_STAGE_IA_COLLAPSE_COORDINATE_OPERATOR_PROTOCOL.json`
3. `R059D_STAGE_IA_PRECOORDINATE_EVIDENCE_LEDGER.json`
4. `R059D_STAGE_IA_PURE_AXIS_GENERATOR_ANALYSIS.json`
5. `R059D_STAGE_IA_MIXED_CELL_GENERATION_ATLAS.json`
6. `R059D_STAGE_IA_PATH_CONFLUENCE_CERTIFICATE.json`
7. `R059D_STAGE_IA_COORDINATE_INJECTIVITY_CERTIFICATE.json`
8. `R059D_STAGE_IA_GENERATOR_IDENTIFIABILITY_LEDGER.json`
9. `R059D_STAGE_IA_MISSING_OBSERVABLE_CERTIFICATE.json` if non-identifiability remains
10. `R059D_STAGE_IA_TRACEABLE_COORDINATE_REGISTRY.json`
11. `R059D_STAGE_IA_EXTENSION_STABILITY_RESULTS.json`
12. `R059D_STAGE_IA_SEMANTIC_CLAIM_LEDGER.json`
13. deterministic checker output
14. frozen Stage-IA checkpoint.

## 16. Required return

Return:

- the exact distinction between CELL_ID and generated coordinate;
- collapse operator input/output typing;
- pure-axis generator classification;
- mixed-cell path-confluence result;
- coordinate injectivity result;
- number/class of surviving coordinate-generating collapse laws;
- smallest disagreement witness if multiple survive;
- exact missing-observable characterization if unique generation is impossible;
- traceable coordinate registry / multibranch registry;
- artifact hashes;
- checkpoint SHA256;
- owner head / Draft PR if published.

Final scientific disposition must be one of:

- `COLLAPSE_GENERATED_COORDINATE_LAW_IDENTIFIED`;
- `COLLAPSE_GENERATED_COORDINATE_LAW_IDENTIFIED_WITHIN_DECLARED_CLASS_ONLY`;
- `COORDINATE_GENERATION_NONIDENTIFIABLE_WITH_CURRENT_NATIVE_STATE`;
- `CURRENT_COLLAPSE_CLASS_INCONSISTENT_WITH_UNIQUE_COORDINATES`;
- `SEMANTIC_HARD_STOP` with exact gate.

Then stop for Driver review.

Do not resume Stage AA/BRC threshold work until this coordinate-generating collapse checkpoint has been reviewed.
