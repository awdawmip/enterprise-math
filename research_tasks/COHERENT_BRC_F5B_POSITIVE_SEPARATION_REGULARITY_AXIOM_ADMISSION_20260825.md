<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F5B-POSITIVE-SEPARATION-REGULARITY-AXIOM-ADMISSION",
  "title": "Coherent-BRC F5B — Positive-Separation Regularity Axiom Admission",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "POSITIVE_SEPARATION_REGULARITY_AXIOM_ADMISSION_STATUS_CLASSIFIED",
  "next_action": "Classify the minimal positive-separation regularity needed for the F4 rank-one obstruction, decide its working-extension admission status, and only then state any conditional rank lower bound with the admitted F5AR elementary branch axiom.",
  "dependencies": [
    "research_inputs/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_PACKET_20260825.md@1cdfb6b1f8fb0806507c9a4ce72278461246034b",
    "driver_reviews/CBRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_DRIVER_REVIEW_20260825.md@0c983a5c98456a4d9c4b6be29b9a988631984842"
  ],
  "source_refs": [
    "research_inputs/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_PACKET_20260825.md@1cdfb6b1f8fb0806507c9a4ce72278461246034b",
    "driver_reviews/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_DRIVER_REVIEW_20260823.md@54fefbc20ad485ce3a7cab95ca6146f6c711b7c1",
    "driver_reviews/CBRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_DRIVER_REVIEW_20260825.md@0c983a5c98456a4d9c4b6be29b9a988631984842"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED_REGULARITY_ADMISSION",
  "tags": ["CBRC","F5B","axiom-admission","positive-separation","regularity","rank-lower-bound","working-extension"],
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF5B"
}
-->

# Coherent-BRC F5B — Positive-Separation Regularity Axiom Admission

Task-ID:

`RS-CBRC-F5B-POSITIVE-SEPARATION-REGULARITY-AXIOM-ADMISSION`

Driver:

`EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Intended owner branch:

`research/cbrc-f5b-positive-separation-regularity-axiom-admission`

## 0. Driver routing

F5AR is accepted with scope narrowing:

`A0 = ELEMENTARY_OLD_REFINING_BRANCH_PROJECTION_NONDEGENERACY`

is admitted only as a Coherent-BRC **working-extension axiom**, not native Foundation truth.

The rank-two lower bound is still not available because the F4 free-block obstruction also relies on a positive-separation regularity. F4 classified `GLOBAL_ZERO_SEPARATION` mathematically but did not admit it as Foundation or working-extension truth.

F5B is the final known admission gate before any rank-two carrier search can be considered.

Do not optimize for rank lift. A weaker admission, model-relative status, deferral or rejection are all valid completions.

## 1. Hard target

`POSITIVE_SEPARATION_REGULARITY_AXIOM_ADMISSION_STATUS_CLASSIFIED`.

Choose exactly one primary verdict:

- `F5B_ADMIT_GLOBAL_ZERO_SEPARATION`;
- `F5B_ADMIT_RESTRICTED_FREE_FIBER_POSITIVITY_ONLY`;
- `F5B_ADMIT_ENVELOPE_ZERO_SEPARATION_ONLY`;
- `F5B_MODEL_RELATIVE_REGULARITY_NOT_WORKING_AXIOM`;
- `F5B_DEFER_REGULARITY_UNDERDETERMINED`;
- `F5B_REJECT_POSITIVE_SEPARATION_OVERSTRONG`;
- `F5B_NO_ADMISSIBLE_POSITIVITY_RULE_CLOSES_RANK_ONE`;
- `F5B_TARGET_LEAK_INVALID`.

No verdict automatically changes native Foundation.

## 2. Publication-liveness gate — before mathematics

Before reading any mathematical source:

1. allocate a fresh Researcher-ID;
2. verify remote owner branch
   `research/cbrc-f5b-positive-separation-regularity-axiom-admission` exists;
3. commit/push
   `evidence/cbrc_f5b_execution_stamp.json`
   containing at minimum:
   - Researcher-ID;
   - task ID;
   - exact taskbook source commit;
   - owner branch;
   - exact mathematical source refs;
   - `phase = STARTED_BEFORE_MATH`;
   - `admission_verdict = null`;
   - `math_source_read_before_stamp = false`;
4. verify remote owner branch resolves to the stamp commit.

If this gate fails, stop without mathematics.

## 3. Mathematical whitelist

Before raw freeze read/use only:

1. `research_inputs/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_PACKET_20260825.md@1cdfb6b1f8fb0806507c9a4ce72278461246034b`;
2. `driver_reviews/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_DRIVER_REVIEW_20260823.md@54fefbc20ad485ce3a7cab95ca6146f6c711b7c1`;
3. `driver_reviews/CBRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_DRIVER_REVIEW_20260825.md@0c983a5c98456a4d9c4b6be29b9a988631984842`.

The taskbook is specification, not an additional mathematical source.

Repository/governance files may be read only for execution procedure.

## 4. Firewall

Do not read/use before raw freeze:

- downstream coherent-BRC/wave free research;
- R063/R064/R065/FQ mathematics;
- external quantum mechanics, Hilbert spaces, Born rules, quantum walks, path integrals, gauge theory or wave equations;
- rank-two carrier proposals;
- complex/quadratic integer carriers;
- finite phase groups;
- norms, inner products, quadratic forms, p-norms or square laws;
- Hadamard/Fourier/splitter targets;
- any F6 candidate answer.

No admission/rejection may be based on resemblance to a desired downstream model.

## 5. Q1 — candidate lattice

Using P0–P5 from the frozen packet, classify every implication and strict failed converse among:

- P0 global coefficient zero separation;
- P1 free-coordinate-fiber positivity;
- P2 envelope zero separation;
- P3 finite-copy nondegeneracy;
- P4 active-branch scalar positivity;
- P5 elementary-split-output positivity;
- every necessary intermediate rule discovered.

Required:

1. exact domains/quantifiers;
2. proof of all implications;
3. smallest exact countermodel for every failed converse;
4. exact classification of P1 versus P2 for finite torsion and, if useful, without finiteness;
5. distinction between pointwise coefficient positivity and envelope positivity.

Deliver:

`F5B_POSITIVE_SEPARATION_REGULARITY_LATTICE_CLASSIFIED`.

## 6. Q2 — minimal F4 free-block obstruction regularity

Determine the weakest exact regularity sufficient for the arbitrary torsion-free-rank-one free-block no-go mechanism reviewed in F4.

Required:

- identify the exact positivity statement used at the contradiction step;
- prove sufficiency for arbitrary finite torsion and arbitrary non-signed-permutation `A in GL_2(Z)` at the accepted F4 scope;
- prove every strictly weaker serious candidate fails, with exact rank-one countermodel;
- separate theorem proof from bounded checker regression.

Deliver:

`F5B_MINIMAL_FREE_BLOCK_OBSTRUCTION_REGULARITY_CLASSIFIED`.

## 7. Q3 — rank-one closure together with admitted A0

Combine only after Q2 is frozen:

- the minimal admitted/considered positivity regularity;
- the accepted F4 conclusion that rank-one survivors under the obstruction have signed-permutation free quotient;
- admitted F5AR A0 requiring both elementary old-refining output projections nonzero.

Classify whether these together exclude every issued-scope torsion-free-rank-one balanced reversible conserving model.

If yes, state the lower bound only as a theorem of the explicit working extension.

If not, give the smallest remaining loophole.

Deliver:

`F5B_WORKING_EXTENSION_RANK_ONE_CLOSURE_CLASSIFIED`.

## 8. Q4 — conservativity / intrinsic formulation

For each serious candidate surviving Q1–Q3, determine:

- whether pure-kernel states with zero free coordinate remain legal;
- whether exact signed cancellation remains legal;
- whether canonical Path/N/Boolean BRC objects change;
- whether a choice of splitting `C ~= Z e ⊕ T` is required;
- whether the condition can be stated intrinsically using the canonical retraction `pi:C->Ze`;
- whether finite torsion is essential;
- whether future coefficient enrichments must satisfy new scalar-separation obligations.

Prefer a formulation in terms of `pi(z)` or a canonically defined finite fiber when possible; do not introduce noncanonical coordinates merely for convenience.

Deliver:

`F5B_POSITIVE_SEPARATION_CONSERVATIVITY_AND_ONTOLOGY_COST_CLASSIFIED`.

## 9. Q5 — admission verdict

Decide whether the minimum serious regularity should be:

- admitted to the Coherent-BRC working extension;
- admitted only in a restricted free-fiber/envelope form;
- retained as model-relative;
- deferred;
- rejected.

Do not promote it to native Foundation truth.

If a working-extension rule is admitted and Q3 proves rank-one closure, state only:

`A0 + ADMITTED_POSITIVE_SEPARATION + BALANCED_REVERSIBLE_CONSERVATION => torsion_free_rank(C) >= 2`.

Status must be explicitly:

`WORKING_EXTENSION_THEOREM`.

No rank-two carrier may be constructed or classified.

Deliver:

`POSITIVE_SEPARATION_REGULARITY_AXIOM_ADMISSION_STATUS_CLASSIFIED`.

## 10. Mandatory ablations

At minimum ablate one at a time:

1. finiteness of torsion fiber;
2. positivity on pure-kernel states;
3. positivity on all nonzero free-coordinate fibers;
4. finite-copy nondegeneracy;
5. active-branch positivity;
6. elementary-output positivity;
7. fixed scalar law / no step-dependent rescaling;
8. exact marked conservation;
9. A0 branch projection nondegeneracy.

For each, record whether the free-block obstruction, rank-one closure, conservativity or interpretability fails.

## 11. Deterministic checker

Required path:

`scripts/cbrc_f5b_validate_positive_separation_regularity_admission.py`

Minimum coverage:

- finite torsion fibers for multiple nonisomorphic groups;
- P0–P5 implication/countermodel witnesses;
- exact periodic weak-scalar rank-one survivor from the F4 boundary when sufficient positivity is removed;
- exact F4 torsion-mediated survivor when A0 is removed;
- admitted A0 plus candidate positivity on the elementary split;
- bounded `GL_2(Z)` regression against the arbitrary theorem, never used as proof;
- all mandatory ablations;
- zero theorem/model mismatches.

General infinite/rank-one claims require proof in the report.

## 12. Materialization checkpoints

### Checkpoint A

After lattice/minimality theorems stabilize, push drafts of:

- `research_reports/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_RETURN_20260825.md`;
- `research_reports/CBRC_F5B_REGULARITY_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`.

### Checkpoint B

Before final verdict, push:

- `research_reports/CBRC_F5B_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`;
- `scripts/cbrc_f5b_validate_positive_separation_regularity_admission.py`.

Run the exact pushed checker and record byte identity, result and digest.

### Checkpoint C

Push final manifest:

`evidence/cbrc_f5b_positive_separation_regularity_admission_manifest.json`.

Verify the remote branch after every checkpoint.

## 13. Required artifacts

1. `evidence/cbrc_f5b_execution_stamp.json`;
2. `research_reports/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_RETURN_20260825.md`;
3. `research_reports/CBRC_F5B_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`;
4. `research_reports/CBRC_F5B_REGULARITY_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`;
5. `scripts/cbrc_f5b_validate_positive_separation_regularity_admission.py`;
6. `evidence/cbrc_f5b_positive_separation_regularity_admission_manifest.json`.

## 14. Hard acceptance gate

Driver acceptance requires:

`F5B_POSITIVE_SEPARATION_REGULARITY_LATTICE_CLASSIFIED`;

`F5B_MINIMAL_FREE_BLOCK_OBSTRUCTION_REGULARITY_CLASSIFIED`;

`F5B_WORKING_EXTENSION_RANK_ONE_CLOSURE_CLASSIFIED`;

`F5B_POSITIVE_SEPARATION_CONSERVATIVITY_AND_ONTOLOGY_COST_CLASSIFIED`;

`POSITIVE_SEPARATION_REGULARITY_AXIOM_ADMISSION_STATUS_CLASSIFIED`;

`TARGET_LEAK_AUDIT_PASS`;

plus publication-liveness checkpoints and deterministic checker evidence.

## 15. Freeze / stop

Freeze on owner branch and report owner head, artifact SHA-256s, checker digest/result, clean-tree status and primary verdict.

Stop after freeze. Do not open F6, construct rank-two carriers, compare downstream wave structures or promote native Foundation axioms without Driver review.

---

Driver issue note:

`F5AR ADMITS ONLY ELEMENTARY BRANCH PROJECTION NONDEGENERACY; NOW FIND THE MINIMAL POSITIVE-SEPARATION REGULARITY BEFORE ANY RANK-TWO CONTINUATION.`
