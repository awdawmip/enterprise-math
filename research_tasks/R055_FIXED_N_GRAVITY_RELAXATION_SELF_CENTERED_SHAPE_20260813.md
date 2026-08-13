<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R055-FIXED-N-GRAVITY-RELAXATION-SELF-CENTERED-SHAPE",
  "title": "R055 — Fixed-N Gravity Relaxation and Self-Centered Shape Formation",
  "kind": "MATHEMATICAL_RESEARCH",
  "owner": "program/self-centered-lattice-shape-formation",
  "base_state": "NEW_MOTHER_QUESTION_PARALLEL_TO_R054",
  "priority": "P0",
  "leverage": "EMERGENT_CENTER / FIXED_MASS_RELAXATION / LIMIT_SHAPE / ROUNDNESS_WITHOUT_CIRCLE_TARGET",
  "frontier": "Hold the number of equal-mass triangular-lattice cells fixed, allow only frozen admissible boundary rearrangements, recompute the centroid after every accepted move, and determine whether the resulting self-centered relaxation selects a unique disk-like shape, a hexagonal/Wulff-like shape, multiple metastable attractors, or another limit class without using classical circle or pi in the optimization target.",
  "next_action": "Freeze the relaxation/move/initial-state protocols before any trajectory, prove the exact centroid-pairwise moment identity and strict-descent termination, exhaust small N, run multi-start local-slide and nonlocal-relocation controls on construction N, freeze theorem/counterexample status, then open strict holdout N and only afterward compare frozen terminal shapes with Euclidean disks and regular hexagons.",
  "dependencies": [
    {
      "target": "research_inputs/R055_FIXED_N_GRAVITY_RELAXATION_SELF_CENTERED_SHAPE_PACKET_20260813.md @ 73e48ac77f403dc468cdea3458e14d10130386e0",
      "action": "CONSUME_AS_FROZEN_PROBLEM_PACKET",
      "satisfied": true
    },
    {
      "target": "R053/R054 calibration line",
      "action": "KEEP_SEPARATE; USE ONLY AS MOTIVATION THAT EXTERNAL TEACHER-CENTER CLUSTERS DO NOT TEST FIXED-N SELF-ORGANIZATION",
      "satisfied": true
    }
  ],
  "evidence_status": "FIXED_N_SELF_CENTERING_AND_DISCRETE_LIMIT_SHAPE_RESEARCH",
  "hard_block": null,
  "tags": [
    "R055",
    "triangular-lattice",
    "fixed-N",
    "centroid",
    "gravity-relaxation",
    "boundary-slide",
    "moment-of-inertia",
    "limit-shape",
    "metastability",
    "roundness"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R055",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R055 — Fixed-N Gravity Relaxation and Self-Centered Shape Formation

Status: `READY / P0 / NEW MOTHER QUESTION / NO PI OR CIRCLE TARGET DURING RELAXATION / NOT CANONICAL`

## 0. Mother question

R053/R054 study how an externally generated teacher-circle boundary can be collapsed. R055 asks an earlier and more structural question:

> If the same number `N` of equal-mass cells is allowed to rearrange on the triangular lattice while preserving connectivity and topology, and the center of mass is recomputed after every accepted boundary move, what shape does the system select by itself?

Do **not** start from a Euclidean circle. Do **not** use classical `pi`, radius, circumference, teacher center or tangent to choose a move.

The intended chain is

`fixed N -> lattice rearrangement -> centroid feedback -> terminal cluster -> emergent center/shape -> post-freeze external comparison`.

A valid negative answer is valuable: the dynamics may have multiple attractors, lattice-anisotropic terminal states, local traps, or a non-circular limit shape.

## 1. Frozen packet

Consume exactly:

`research_inputs/R055_FIXED_N_GRAVITY_RELAXATION_SELF_CENTERED_SHAPE_PACKET_20260813.md`

Packet source:

`73e48ac77f403dc468cdea3458e14d10130386e0`

The packet fixes the substrate, equal masses, fixed-N regimes, move classes, objective separation, initial-state families, holdout N, adversarial controls and interpretation boundary.

Do not silently alter them after trajectories are observed.

## 2. Stage 0 — freeze protocols before relaxation

Before running any construction trajectory, create and freeze:

- `R055_RELAXATION_PROTOCOL.json`;
- `R055_MOVE_ENERGY_REGISTRY.json`;
- `R055_INITIAL_STATE_REGISTRY.json`.

The protocol must restate the exact machine-level definitions of:

- lattice basis and axial norm;
- connected/hole-free cluster predicate;
- occupied boundary and exterior frontier;
- equal cell mass;
- centroid recomputation;
- exact integer gravity-compaction energy `G(C)`;
- D1 local boundary slide;
- D2 global boundary relocation reference;
- strict descent and tie-break;
- construction/holdout N;
- deterministic initial-shape generators and seeds;
- exact stopping condition;
- diagnostic definitions `P_edge`, `A2`, radial-squared dispersion and directional imbalance;
- explicit absence of circle/pi from move selection.

Return, before any construction relaxation:

`R055_RELAXATION_PROTOCOL_SHA256`

`R055_MOVE_ENERGY_REGISTRY_SHA256`

`R055_INITIAL_STATE_REGISTRY_SHA256`

## 3. Stage A — exact identities and small-N exhaustive truth

First prove/check the exact identity

`I2(C) = (1/N) sum_{x<y} ||x-y||^2`

and therefore that `G(C)=N I2(C)` is an exact integer on the triangular lattice under the packet's normalization.

Derive an exact formula for `Delta G` under one cell replacement `u -> v` if possible.

Prove strict-descent termination for D1 and D2 on the finite fixed-N state quotient.

Then exhaust all connected hole-free clusters modulo translation+D6 for `N=1..12` where computationally feasible.

For each N return:

- number of state classes;
- exact global `G` minimizer class(es);
- exact global `P_edge` minimizer class(es);
- whether the two minimizer sets coincide;
- all D1 local minima of `G` where feasible;
- basin sizes under each frozen tie-break;
- centroid classes of global/local minima;
- `A2`, radial-squared dispersion and directional imbalance of each relevant minimizer.

Do not generalize small-N enumeration to all N without theorem.

## 4. Stage B — fixed-N gravity relaxation on construction sizes

Use exactly the construction N from the packet:

`[19,31,37,53,61,79,91,113,127,151,169,199,217]`.

For every N, run all frozen initial-state families under D1 primary strict descent.

After each accepted move:

1. update the cluster;
2. recompute the centroid from all N cells;
3. recompute exact `G` or exact incremental equivalent;
4. verify strict decrease;
5. recompute the legal move set from the new shape/center state.

Record trajectories and terminal states exactly enough to reproduce every accepted step.

Then run D2 as a reference on the same initial/terminal states to answer whether D1 is merely stuck in local minima.

No D2 result may be relabeled as a local physical sliding law.

## 5. Stage C — attractor and path-dependence classification

For every construction N classify:

- whether all initial-state families reach one translation+D6 class;
- whether alternative frozen tie-breaks change the terminal class;
- whether D1 and D2 agree;
- whether centroid final classes agree;
- whether terminal `G` values are equal despite shape nonuniqueness;
- whether there are multiple metastable attractors.

Use the exact status vocabulary from the packet:

- `D1_LOCAL_MINIMUM`;
- `D2_RELOCATION_MINIMUM`;
- `GLOBAL_G_MINIMUM` only when proved;
- `MULTIPLE_ATTRACTORS`;
- `UNIQUE_ATTRACTOR_OBSERVED` only as bounded evidence unless proved.

Actively search for the smallest N that falsifies uniqueness/path-independence if such a counterexample exists.

## 6. Stage D — objective separation

Do **not** assume compactness, boundary minimization and roundness are the same problem.

Compare at least:

1. gravity-moment minimizers/terminal states under `G`;
2. raw lattice-boundary minimizers under `P_edge` where exact or well-certified;
3. second-moment isotropy `A2`;
4. radial-squared boundary dispersion;
5. six-direction boundary imbalance.

Report whether lowering `G` monotonically improves any of the other diagnostics. Counterexamples are important.

In particular, test the hypothesis that `P_edge` optimization is driven toward a lattice-anisotropic hexagonal/Wulff shape while `G` optimization may favor a more isotropic disk-like shape.

Do not declare that hypothesis true from images alone.

## 7. Stage E — theorem/counterexample freeze before holdout

Before opening strict holdout N, freeze:

`R055_THEOREM_COUNTEREXAMPLE_LEDGER.json`

and return:

`R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256`.

The ledger must distinguish:

- `PROVED`;
- `EXACT_EXHAUSTIVE_SMALL_N`;
- `BOUNDED_MULTI_START_OBSERVATION`;
- `COUNTEREXAMPLE`;
- `OPEN`.

At minimum give explicit status for:

- strict-descent termination;
- exact centroid/pairwise identity;
- D1 local-minimum versus D2 minimum equivalence;
- initial-condition independence;
- tie-break independence;
- uniqueness of terminal shape;
- uniqueness of centroid class;
- asymptotic isotropy/roundness;
- gravity-minimum versus perimeter-minimum equivalence;
- any proposed disk/hexagonal limit shape.

## 8. Stage F — strict holdout N

Only after the protocol/registry/theorem-ledger hashes are frozen, open the strict holdout sizes:

`[43,67,103,139,181,241,301]`.

Run the already-frozen initial families, moves, tie-breaks, objectives and diagnostics without changes.

Return:

`R055_HOLDOUT_RESULTS.json`.

Report whether construction-era claims about attractor uniqueness, D1/D2 agreement, centroid classes, anisotropy trends or objective separation survive.

Any change to move rules or objective after holdout is a new generation.

## 9. Stage G — post-freeze external circle/hexagon comparison

Only now may ordinary Euclidean comparison models be opened.

For each frozen terminal shape compare, without refitting the relaxation:

- equal-area Euclidean disk centered at the final centroid;
- best aligned/rescaled regular hexagon;
- relevant raw `P_edge` minimizer/control.

Use multiple diagnostics rather than one circularity scalar. At minimum include:

- normalized radial deviation;
- symmetric-difference or occupancy-area discrepancy where implemented;
- second-moment comparison;
- boundary directional anisotropy;
- a Hausdorff-style boundary discrepancy if robustly defined.

Classical `pi` may appear only inside external disk/circularity comparison formulas in this stage.

No post-freeze comparison result may be used to alter the primary gravity rule.

Return:

`R055_EXTERNAL_SHAPE_COMPARISON.json`.

## 10. Stage H — asymptotic attack

If construction/holdout data suggest a stable limit shape, actively attempt a theorem or a counterexample.

Promising proof routes include exact exchange inequalities, lattice-point moment minimization, discrete symmetrization/rearrangement, comparison of rescaled occupancy measures, and bounds separating bulk moment from boundary anisotropy.

For any limit-shape claim return one of:

- `LIMIT_SHAPE_PROVED`;
- `SUBSEQUENCE_OR_CENTER_CLASS_LIMIT_PROVED`;
- `LIMIT_SHAPE_COUNTEREXAMPLE_FOUND`;
- `OPEN_WITH_BOUNDED_EVIDENCE`.

Do not fit a curve to finite N and call it an asymptotic theorem.

A particularly valuable result would be either:

`FIXED_N_GRAVITY_RELAXATION_SELECTS_DISKLIKE_LIMIT`

or a rigorous negative such as

`LOCAL_SLIDE_METASTABILITY_PREVENTS_UNIQUE_SHAPE`

or

`LATTICE_ANISOTROPY_SURVIVES_GRAVITY_RELAXATION`.

## 11. Mandatory negative controls

Execute every packet adversarial control, especially:

- cell count preservation;
- lattice-site preservation;
- connectivity and hole-free preservation;
- centroid recomputation after every accepted move;
- no privileged initial center;
- no circle/pi in energy or move selection;
- perimeter minimum not relabeled as roundness;
- gravity minimum not relabeled as a circle by definition;
- multiple initial conditions and tie-breaks;
- D1 local minima not promoted to global minima;
- D2 not mislabeled as local sliding;
- no all-N theorem from small-N enumeration;
- no asymptotic theorem from finite large-N pictures;
- no post-hoc combined objective.

## 12. Required artifacts

Return every artifact listed in the frozen packet, including:

- report;
- frozen protocols/registries;
- small-N exhaustive atlas;
- relaxation trajectories;
- terminal-shape atlas;
- centroid-dynamics atlas;
- objective comparison;
- strict holdout results;
- external shape comparison;
- theorem/counterexample ledger;
- adversarial and exact-check results;
- final manifest;
- checker/tests.

At final checkpoint return:

`R055_ARTIFACT_MANIFEST_SHA256`.

## 13. Interpretation boundary

The task is testing one explicit lattice relaxation model, not asserting that the physical universe uses that lattice or that physical gravity is quadratic.

The central success criterion is narrower and stronger:

> determine whether a fixed number of equal-mass cells plus a local boundary-rearrangement law can jointly produce an emergent center and a reproducible compact shape without a circle being supplied as the target.

If the answer is no because of metastability, anisotropy or nonuniqueness, freeze the obstruction rather than repairing it post hoc.

## 14. Advancement vector

Before task:

- fixed-N self-centered relaxation: `0% -> 55%` target;
- emergent-center dynamics: `10% -> 55%` target;
- multi-attractor/path-dependence classification: `0% -> 45%` target;
- circle-free roundness diagnostics: `0% -> 45%` target;
- limit-shape theorem surface: `0% -> 30%` target.

Advancement vector:

`fixed-N-relaxation +55 / centroid-dynamics +45 / attractor-classification +45 / roundness-diagnostics +45 / limit-shape +30`.

End state remains `NOT_CANONICAL` pending Driver review.