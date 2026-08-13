<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R053-TRIANGULAR-PACKING-PI-SUPERVISED-BOUNDARY-COLLAPSE",
  "title": "R053 — Pi-Supervised Triangular-Packing Boundary Collapse: Circumference and Tangency",
  "kind": "CALIBRATED_MATHEMATICAL_RESEARCH",
  "owner": "program/pi-supervised-crystal-boundary",
  "base_state": "NEW_MOTHER_QUESTION",
  "priority": "P0",
  "leverage": "NATIVE_CIRCUMFERENCE / LOCAL_COLLAPSE_CREDIT / SCALE_DEPENDENT_PI / TANGENT_RECOVERY",
  "frontier": "Use classical pi as an explicit teacher signal to learn a compact local collapse algebra on the planar triangular/hexagonal densest packing, then freeze that algebra and test whether it independently defines circumference, recovers tangent direction, and exhibits scale-stable pi readouts on unseen crystal circles.",
  "next_action": "Freeze the lattice/teacher/split protocol, enumerate local boundary microclusters and exact collapse candidates, train local credit under classical circumference supervision, freeze one inference policy before holdout, then evaluate circumference, tangent recovery, and scale oscillation without refitting.",
  "dependencies": [
    {"target":"research_inputs/R053_TRIANGULAR_PACKING_PI_SUPERVISED_COLLAPSE_PACKET_20260813.md @ 468178137f84d85dfa8fd52fdc4ddfb64224d175","action":"CONSUME_AS_PROBLEM_PACKET","satisfied":true},
    {"target":"FOUNDATIONAL_LOGIC / calibration separation","action":"CONSUME_AS_LAYER_DISCIPLINE_ONLY","satisfied":true}
  ],
  "evidence_status": "CLASSICAL_PI_SUPERVISED_INVERSE_COLLAPSE_RESEARCH",
  "hard_block": null,
  "tags": ["R053","triangular-lattice","hex-cells","pi-supervision","collapse","circumference","tangent","scale"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "NEW_RESEARCHER_ID_REQUIRED",
  "identity_lane": "R053",
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242","review_state":"PASS","temporary_overrides":["CLASSICAL_PI_IS_EXPLICITLY_ALLOWED_AS_TEACHER_SIGNAL"]}
}
-->

# R053 — Pi-Supervised Triangular-Packing Boundary Collapse

Status: `READY / P0 / NEW MOTHER QUESTION / CLASSICAL PI SUPERVISION EXPLICITLY ALLOWED / NOT CANONICAL`

Researcher identity will be supplied by the Driver relay.

## 0. Problem statement

This task deliberately changes the role of classical `π`.

Do **not** try to rediscover π blindly.

Traditional Euclidean π is the teacher signal. We know where the classical circumference lies and use that success to assign credit to competing local collapse modes of a discrete crystal boundary.

The intended chain is:

`classical circumference target -> local collapse credit -> frozen collapse algebra -> Enterprise-Math circumference -> inferred tangent field -> scale-dependent pi readout`.

The research question is:

> On a two-dimensional densest equal-cell packing, can one learn a radius-independent, phase-robust, local algebraic collapse rule whose frozen application to unseen crystal-circle boundaries reproduces classical circumference and thereby reveals the effective tangent direction of the ideal circle from the local organization of the real discrete boundary?

This task is **calibration/inverse reconstruction**, not a foundational proof that classical π is native.

## 1. Exact input packet

Consume:

`research_inputs/R053_TRIANGULAR_PACKING_PI_SUPERVISED_COLLAPSE_PACKET_20260813.md`

Exact source:

`468178137f84d85dfa8fd52fdc4ddfb64224d175`

The packet's teacher/student separation is authoritative.

R052/R052B mathematical content is not required. Do not import their pi-role definitions as the collapse answer. This is a new mother question.

## 2. Explicitly allowed teacher mathematics

On the **teacher side**, classical Euclidean mathematics is allowed from the beginning:

- circle;
- center;
- radius;
- Euclidean distance;
- diameter;
- classical symbolic `π`;
- target circumference `2πR`;
- high-precision numerical evaluation of π for optimization/scoring;
- classical circle tangent, but only for post-policy validation as specified below.

This allowance is intentional.

On the **student side after policy freeze**, the rule must not call any of those global teacher quantities except the already-formed discrete crystal boundary itself.

## 3. Fixed student substrate — planar densest packing only

Use only the planar triangular lattice / regular-hexagonal Voronoi packing from the packet.

Do not broaden this task to:

- square grids;
- arbitrary planar graphs;
- 3D FCC/HCP;
- variable cell sizes;
- rotated multi-scale Nollm geometry;
- continuum PDEs.

Keep the physical cell scale symbolic as `ell_0`. No claim that a minimum universe-cell size is presently known is allowed.

Prefer exact axial/Eisenstein coordinates and exact algebraic arithmetic. Floating point may be used for optimization diagnostics and high-precision target comparison, but the discrete boundary and candidate local geometry should be represented exactly where possible.

## 4. Stage 0 — freeze lattice, teacher-circle generation, splits and scoring

Before fitting or ranking any collapse policy, create and freeze:

`R053_LATTICE_TARGET_PROTOCOL.json`

It must specify at least:

1. exact lattice basis and normalization;
2. exact Voronoi hex-cell geometry;
3. exact teacher-circle clusterization rule `C(R,c)`;
4. boundary extraction rule and exposed-edge orientation convention;
5. tie handling for cell centers exactly on the teacher circle;
6. deterministic finite set of center phases `c` in one fundamental lattice cell;
7. construction/training radii;
8. validation radii/phases used for model/policy selection;
9. strictly held-out radii/phases opened only after policy freeze;
10. larger extrapolation radii, if computationally feasible;
11. maximum local microcluster radius/window `K` or a finite search bound;
12. primary circumference loss;
13. secondary reporting metrics;
14. exact policy-complexity accounting rule;
15. target-π numerical precision policy;
16. a requirement to repeat decisive policy ranking at higher precision to exclude target-rounding artifacts;
17. explicit statement that classical tangent labels are **not** used in collapse training or policy selection;
18. explicit statement that the held-out set is not used to redesign the collapse library or local features.

The primary training target must be based on classical circumference, for example through

`pi_hat(R,c)=P_policy(R,c)/(2R)`

and a declared loss against classical `π`.

The exact aggregation may be squared, absolute, robust, scale-weighted, or multiobjective, but it must be frozen before fitting and must not silently overweight one handpicked radius.

Return:

`R053_LATTICE_TARGET_PROTOCOL_SHA256`

before Stage A/B scoring begins.

## 5. Stage A — enumerate the real crystal boundary and local microcluster types

For every construction circle, produce the exact union of included hex crystal cells and its exposed cyclic boundary.

Represent the raw boundary at minimum by:

- cyclic exposed-edge word in six lattice directions;
- boundary vertex sequence;
- adjacent boundary-cell identities;
- local turn sequence;
- exact local anchor coordinates.

Enumerate local boundary microcluster types up to the frozen bound `K`.

Canonicalize by translation and, where appropriate, the dihedral symmetry `D6`, while retaining the transformation needed to recover the actual oriented direction in the original boundary.

For each local type record:

- type ID;
- minimal representative patch;
- boundary edge word;
- adjacent-cell pattern;
- occurrence count by construction radius and center phase;
- symmetry orbit size;
- whether the type appears at convex, flat-like, or concave discrete boundary locations, if this is internally definable;
- whether it is unseen in some construction strata.

Do not use held-out-circle occurrences to design a special case.

Freeze:

`R053_BOUNDARY_MICROCLUSTER_CATALOG.json`

## 6. Stage B — finite collapse hypothesis library

Generate a serious finite library of local collapse modes.

A collapse mode acts on a bounded local crystal-boundary patch and returns an exact effective segment or short effective chain.

Every collapse mode must declare:

- collapse ID;
- supported microcluster type(s);
- exact local anchors consumed;
- exact effective segment vector(s);
- exact effective length expression;
- effective tangent-direction class;
- raw boundary support consumed;
- whether orientation reversal changes the output;
- 60-degree rotation equivariance rule;
- composability constraints;
- overlap exclusion;
- fallback behavior when no specialized collapse applies;
- parameter count.

Candidate anchors may be constructed from local boundary vertices, exposed-edge midpoints, boundary-cell centers, contact points, and other local algebraic anchors declared in the foundation packet.

### Critical anti-hardcode rule

No candidate effective length or direction may contain a free continuous constant chosen to equal, approximate, encode, or algebraically hide `π`, `2π`, `4π`, or a radius-specific correction.

Classical π may choose **among** local algebraic collapse modes through credit assignment; it may not be inserted as the local output constant itself.

A collapse family may contain discrete/hierarchical choices, but every inference-time choice must eventually be a function only of the bounded local student state and frozen policy.

Include at least useful baselines such as:

- raw exposed-edge perimeter/no collapse;
- simple fixed local collapse(s);
- any natural chord/anchor baseline supported by the exact cell geometry.

Freeze:

`R053_COLLAPSE_HYPOTHESIS_LIBRARY.json`

and return:

`R053_COLLAPSE_LIBRARY_SHA256`

before fitting Stage C.

## 7. Stage C — π-supervised credit assignment and policy learning

Now use classical π directly.

The goal is to assign local credit to competing collapse modes according to their contribution to the global circumference target over the construction circles.

A learned policy should conceptually have the form

`local boundary state -> collapse mode`

or an equivalent finite grammar/energy/parser whose inference depends only on local discrete state plus previously frozen parsing state.

### Required credit accounting

Create:

`R053_COLLAPSE_CREDIT_LEDGER.json`

For every serious `(microcluster type, collapse mode)` pair record where meaningful:

- number of construction occurrences;
- contexts/scales/phases in which it was tested;
- positive/negative credit;
- exact credit definition;
- counterfactual or ablation comparison used;
- order-dependence, if any;
- variance/stability across radii;
- variance/stability across center phases;
- whether credit reverses sign in different contexts;
- interactions with neighboring collapse choices;
- whether the mode survives into the frozen policy.

Credit may be computed by exact counterfactuals, dynamic programming, coordinate optimization, Shapley-style attribution, or another explicit method, but the method must be reproducible and its limitations recorded.

### Closed-boundary parsing requirement

The frozen rule must cover the raw cyclic boundary exactly once in the accounting sense used for perimeter. It may not double-count overlapping raw support.

If parsing/segmentation has multiple optima or depends on a starting edge, this must be resolved by a frozen invariant rule or explicitly recorded as an ambiguity/failure.

### No tangent supervision during training

Do not use the classical tangent field to choose collapse modes.

The only geometric teacher objective for the main policy is classical circumference / π plus the frozen complexity or regularization terms declared in Stage 0.

The tangent direction must later emerge from the selected collapse geometry.

### Freeze before holdout

Use construction data to fit and validation data to choose among policies if the frozen protocol allows it.

Before opening the strict holdout set, freeze:

`R053_COLLAPSE_POLICY.json`

including:

- complete local rule/grammar;
- parser/segmentation rule;
- fallback rule;
- all learned discrete choices/weights;
- total parameter/lookup-table complexity;
- training and validation performance;
- exact inference contract stating that π, R, circle center and teacher geometry are not inputs.

Return:

`R053_COLLAPSE_POLICY_SHA256`

before Stage D.

## 8. Stage D — frozen-policy holdout circumference test

Open the strict held-out radii and center phases only after the policy hash is frozen.

For each held-out teacher circle:

1. build the crystal cluster from the frozen lattice protocol;
2. expose its raw boundary;
3. apply the frozen collapse policy **without π or teacher geometry as inference inputs**;
4. obtain `Per_EM`;
5. then evaluate
   `pi_EM(R,c)=Per_EM/(2R)`
   against classical π.

No refitting or policy mutation is allowed.

Report at minimum:

- signed error;
- absolute error;
- relative circumference error;
- center-phase variation;
- radius variation;
- comparison with frozen baselines;
- unseen microcluster rate and fallback usage;
- worst held-out cases;
- whether construction gains survive scale extrapolation.

Return:

`R053_HOLDOUT_CIRCUMFERENCE_RESULTS.json`

A policy that fits training circles but fails held-out radii/phases is a valid negative result.

## 9. Stage E — infer and validate the local tangent direction

Only after `R053_COLLAPSE_POLICY_SHA256` is frozen, use the winning/frozen collapse geometry to define the Enterprise-Math local tangent field.

For every accepted collapsed microcluster, derive the effective tangent direction from its frozen output segment/vector. Do not insert a new learned tangent parameter.

Then compare the inferred tangent field against the classical teacher-circle tangent field.

The tangent comparison is validation, not training.

Create:

`R053_TANGENT_RECOVERY_ATLAS.json`

It must include:

- mapping from raw local crystal type to frozen effective tangent direction;
- location/anchor convention for associating a collapsed patch with a teacher-circle point;
- tangent misalignment metric;
- results by radius;
- results by center phase;
- results by microcluster type;
- whether lower circumference error correlates with improved tangent alignment;
- counterexamples where circumference is globally good but local tangent is wrong;
- any local type whose tangent remains ambiguous after credit training.

A particularly valuable result is:

`GLOBAL_PI_CREDIT_RECOVERS_LOCAL_TANGENT_WITHOUT_TANGENT_SUPERVISION`.

But do not claim it unless the frozen-policy holdout evidence supports it.

## 10. Stage F — define the student-side circumference algebra

Extract the final rule into a clean algebraic definition independent of the training loop.

Return:

`R053_CIRCUMFERENCE_COLLAPSE_ALGEBRA.json`

It must state:

- the student input type;
- the local microcluster equivalence classes;
- the accepted collapse operation(s);
- exact length and direction outputs;
- cyclic boundary parsing/composition;
- perimeter aggregation;
- symmetry/equivariance properties;
- any proved invariance theorem;
- any ambiguity/dependency still present;
- exact definition of `Per_EM(C)` after policy freeze.

The objective is that a later program can compute `Per_EM` for a new crystal cluster **without knowing that π was the historical teacher**.

This is the point where the task earns a native notion of circumference.

## 11. Stage G — scale-dependent π, oscillation and precision horizon

With the frozen circumference rule, evaluate a broad radius range larger than the construction scale where feasible.

Define:

`pi_EM(R,c)=Per_EM(C(R,c))/(2R)`.

Study:

- whether finite-radius values differ;
- signed oscillation around classical π;
- center-phase dependence;
- lattice-anisotropy signatures;
- mean bias by scale;
- max/min envelope by scale;
- possible periodic/quasiperiodic shell effects;
- empirical or theorem-level decay rate of the envelope;
- whether the rule converges, stabilizes to a band, or retains systematic bias.

Keep `ell_0` symbolic and translate only at the end:

`R_physical = R * ell_0`.

Return:

`R053_SCALE_PI_OSCILLATION.json`

`R053_PRECISION_HORIZON.json`

For every claimed precision horizon, label it one of:

- `PROVED_FOR_ALL_LARGER_SCALES`;
- `PROVED_UNDER_DECLARED_SUBSEQUENCE_OR_PHASE_CLASS`;
- `BOUNDED_EXHAUSTIVE_OBSERVATION_ONLY`;
- `EMPIRICAL_CONJECTURE_ONLY`.

Do not turn a finite computed range into an asymptotic theorem.

## 12. Strong theorem / discovery targets

Valuable outcomes include any of the following:

- a finite local collapse grammar with strong held-out π performance;
- a small subset of boundary microcluster types receiving most of the circumference correction credit;
- a proof that certain local collapse modes are always harmful/helpful under the frozen loss;
- D6-equivariant collapse classification;
- a closed-boundary parsing invariance theorem;
- an exact algebraic circumference definition after training;
- local tangent recovery from π-only global supervision;
- a scale/phase oscillation law for `pi_EM`;
- an error bound of order `O(ell_0/R)` or another justified asymptotic rate;
- a proof that no bounded-local policy of the tested class can remove a certain anisotropy/bias;
- a demonstration that one needs a larger local neighborhood to distinguish two boundary organizations with opposite credit.

Negative results are first-class.

## 13. Required adversarial attacks

At minimum attack and record:

- `PI_HARDCODED_IN_LOCAL_COLLAPSE_OUTPUT`
- `PI_USED_AT_INFERENCE_AFTER_POLICY_FREEZE`
- `RADIUS_SPECIFIC_PARAMETER_OR_LOOKUP`
- `CENTER_PHASE_SPECIFIC_PARAMETER_OR_LOOKUP`
- `GLOBAL_CIRCLE_CENTER_USED_AS_STUDENT_FEATURE`
- `GLOBAL_RADIUS_USED_AS_STUDENT_FEATURE`
- `CLASSICAL_TANGENT_USED_DURING_POLICY_TRAINING`
- `HOLDOUT_USED_TO_REDARY_COLLAPSE_LIBRARY`
- `HOLDOUT_RETRAIN_OR_POSTHOC_POLICY_PATCH`
- `ONE_RADIUS_OR_ONE_PHASE_OVERFIT`
- `CYCLIC_START_DEPENDENCE`
- `OVERLAPPING_COLLAPSES_DOUBLE_COUNTED`
- `BOUNDARY_SUPPORT_LEFT_UNACCOUNTED`
- `D6_SYMMETRY_BROKEN_WITHOUT_DECLARATION`
- `RAW_HEX_EDGE_LENGTH_MISTAKEN_FOR_LEARNED_CIRCUMFERENCE`
- `TEACHER_2PIR_COPIED_DIRECTLY_AS_STUDENT_OUTPUT`
- `TARGET_PI_PRECISION_CHANGES_POLICY_RANKING`
- `POLICY_COMPLEXITY_EXPLOSION_MEMORIZES_TRAINING_CIRCLES`
- `UNSEEN_MICROCLUSTER_HAS_NO_FROZEN_FALLBACK`
- `FINITE_SCALE_NUMERICS_PRESENTED_AS_ASYMPTOTIC_THEOREM`
- `MINIMUM_UNIVERSE_CELL_SIZE_CLAIMED_WITHOUT_PHYSICAL_EVIDENCE`

## 14. Exact computation requirements

Where practical use exact integer/algebraic arithmetic for:

- lattice membership;
- cell-neighbor relations;
- exposed-boundary extraction;
- microcluster canonicalization;
- local anchor geometry;
- candidate collapse segment vectors;
- combinatorial parsing/checks.

For π scoring use explicit arbitrary precision. Record the precision. Re-run decisive construction/validation ranking at materially higher precision and confirm whether the selected policy changes.

If it changes, do not freeze a winner until the ranking ambiguity is understood.

Provide exact checker/tests for:

- lattice boundary correctness on small known clusters;
- D6 canonicalization/equivariance;
- no-overlap/exact-cover parsing;
- inference-time teacher-feature absence;
- policy hash immutability;
- holdout no-refit;
- reproducible perimeter totals on small fixtures.

## 15. Required artifacts

Return at least:

- `R053_REPORT.md`
- `R053_LATTICE_TARGET_PROTOCOL.json`
- `R053_BOUNDARY_MICROCLUSTER_CATALOG.json`
- `R053_COLLAPSE_HYPOTHESIS_LIBRARY.json`
- `R053_COLLAPSE_CREDIT_LEDGER.json`
- `R053_COLLAPSE_POLICY.json`
- `R053_CONSTRUCTION_RESULTS.json`
- `R053_VALIDATION_RESULTS.json`
- `R053_HOLDOUT_CIRCUMFERENCE_RESULTS.json`
- `R053_TANGENT_RECOVERY_ATLAS.json`
- `R053_CIRCUMFERENCE_COLLAPSE_ALGEBRA.json`
- `R053_SCALE_PI_OSCILLATION.json`
- `R053_PRECISION_HORIZON.json`
- `R053_ADVERSARIAL_TEST_RESULTS.json`
- `R053_EXACT_CHECK_RESULTS.json`
- `R053_ARTIFACT_MANIFEST.json`
- checker/tests.

Freeze and report at minimum:

- `R053_LATTICE_TARGET_PROTOCOL_SHA256`
- `R053_COLLAPSE_LIBRARY_SHA256`
- `R053_COLLAPSE_POLICY_SHA256`
- `R053_ARTIFACT_MANIFEST_SHA256`

## 16. Interpretation discipline

If the frozen policy performs well, the allowed claim is approximately:

> Classical circular success can supervise a compact local collapse algebra on a triangular crystal boundary, and the frozen algebra then defines an independent discrete circumference/tangent readout on unseen clusters.

Do not automatically claim:

- the triangular lattice is physically real;
- the learned collapse is the unique physical law;
- classical circumference has been fundamentally derived;
- the universe has a known cell size;
- every finite-scale circle has the same pi readout.

The target is to learn **how the edge organizes and collapses**, not to re-label `2πR` as a native formula.

## 17. Module estimate / advancement vector

Before task:

- planar crystal-circle boundary representation: `0% -> 45%` target;
- local collapse credit algebra: `0% -> 45%` target;
- native circumference definition: `0% -> 35%` target;
- tangent recovery: `0% -> 30%` target;
- scale-dependent pi / precision horizon: `0% -> 25%` target.

Advancement vector:

`boundary-organization +45 / collapse-credit +45 / circumference +35 / tangent +30 / scale-pi +25`.

End state remains `NOT_CANONICAL` pending Driver review.
