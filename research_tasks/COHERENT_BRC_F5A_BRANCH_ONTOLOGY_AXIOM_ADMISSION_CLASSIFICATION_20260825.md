<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F5A-BRANCH-ONTOLOGY-AXIOM-ADMISSION-CLASSIFICATION",
  "title": "Coherent-BRC F5A — Branch Ontology Axiom Admission Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "BRANCH_TO_OLD_SUPPORT_FAITHFULNESS_AXIOM_ADMISSION_STATUS_CLASSIFIED",
  "next_action": "Classify the minimal typed branch-to-old-support faithfulness rule, its consistency and conservativity, and whether it should be admitted as a new axiom before any rank-two continuation is authorized.",
  "dependencies": [
    "research_inputs/CBRC_F5A_BRANCH_ONTOLOGY_AXIOM_ADMISSION_PACKET_20260825.md@b904a86aa24ed35564956181a7c1309074a782ea",
    "driver_reviews/CBRC_F5R_INDEPENDENT_FORGETFUL_BRANCH_SEMANTICS_DRIVER_REVIEW_20260825.md@6e40f56745c405042ad2216d1f62b110312ffb83"
  ],
  "source_refs": [
    "research_inputs/CBRC_F5A_BRANCH_ONTOLOGY_AXIOM_ADMISSION_PACKET_20260825.md@b904a86aa24ed35564956181a7c1309074a782ea",
    "definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md@6ec0d73a19e28ec586c59a97d24f5798c9119771",
    "definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@b631242db84c5bd3640e6dc554b19a1d04d464f3"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED_AXIOM_ADMISSION_AUDIT",
  "tags": ["CBRC","F5A","axiom-admission","branch-ontology","refinement","forgetful-map","conservativity"],
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF5A"
}
-->

# Coherent-BRC F5A — Branch Ontology Axiom Admission Classification

Task-ID:

`RS-CBRC-F5A-BRANCH-ONTOLOGY-AXIOM-ADMISSION-CLASSIFICATION`

Driver:

`EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Intended owner branch:

`research/cbrc-f5a-branch-ontology-axiom-admission`

## 0. Driver routing

F5R is accepted with the exact result:

`F5R_NEW_AXIOM_REQUIRED`.

Current BRC/path/refinement semantics permit a nonzero retained enriched branch with zero old projection. Therefore the per-branch condition

`pi(x)!=0 and pi(y)!=0`

cannot be promoted as a derived theorem.

F5A does not search for a carrier. It decides whether a narrowly typed branch ontology rule is mathematically coherent, conservative, minimal and worthy of admission as a **new axiom**.

Do not optimize for admission. Rejection, narrowing, deferral or model-relative status are valid completions.

## 1. Hard target

`BRANCH_TO_OLD_SUPPORT_FAITHFULNESS_AXIOM_ADMISSION_STATUS_CLASSIFIED`.

Choose exactly one primary verdict:

- `F5A_ADMIT_MINIMAL_TYPED_BRANCH_FAITHFULNESS_AXIOM`;
- `F5A_ADMIT_RESTRICTED_ELEMENTARY_RULE_ONLY`;
- `F5A_MODEL_RELATIVE_EXTENSION_NOT_FOUNDATION_AXIOM`;
- `F5A_DEFER_AXIOM_UNDERDETERMINED`;
- `F5A_REJECT_AXIOM_OVERSTRONG_OR_INCONSISTENT`;
- `F5A_NO_ADMISSIBLE_RULE_CLOSES_THE_LOOPHOLE`;
- `F5A_TARGET_LEAK_INVALID`.

No verdict automatically changes Foundation. Driver review is required after freeze.

## 2. Publication-liveness gate — before mathematics

Before any mathematical analysis:

1. allocate a fresh Researcher-ID;
2. create/push owner branch
   `research/cbrc-f5a-branch-ontology-axiom-admission`;
3. commit/push
   `evidence/cbrc_f5a_execution_stamp.json`
   recording Researcher-ID, task ID, exact taskbook source, owner branch, exact mathematical source refs, `phase=STARTED_BEFORE_MATH`, and `admission_verdict=null`;
4. verify the remote branch resolves to that stamp commit.

If the gate fails, stop without mathematics.

## 3. Mathematical whitelist

Before raw freeze, read/use only:

1. `research_inputs/CBRC_F5A_BRANCH_ONTOLOGY_AXIOM_ADMISSION_PACKET_20260825.md@b904a86aa24ed35564956181a7c1309074a782ea`;
2. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md@6ec0d73a19e28ec586c59a97d24f5798c9119771`;
3. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@b631242db84c5bd3640e6dc554b19a1d04d464f3`;
4. `driver_reviews/CBRC_F5R_INDEPENDENT_FORGETFUL_BRANCH_SEMANTICS_DRIVER_REVIEW_20260825.md@6e40f56745c405042ad2216d1f62b110312ffb83` only as the accepted semantic boundary.

Repository/governance files may be used only for execution procedure.

## 4. Firewall

Do not read/use before raw freeze:

- downstream coherent-BRC/wave free research;
- R063/R064/R065/FQ mathematics;
- external quantum mechanics, quantum walks, Hilbert spaces, Born rules, path integrals, gauge theory or wave equations;
- any preselected rank-two, complex or quadratic carrier;
- phase groups, norms, inner products, positive quadratic forms or square laws;
- Hadamard/Fourier/splitter targets.

Do not admit or reject a rule because it helps or obstructs a desired downstream carrier.

## 5. Q1 — exact candidate lattice

Starting from A0–A4 in the frozen input, define an exact implication/strictness lattice among:

- elementary two-branch projection nondegeneracy;
- typed branch-to-old-support faithfulness;
- descendant-family faithfulness;
- global support-reflecting retraction;
- leafwise faithfulness at arbitrary finite refinement depth;
- every necessary strictly intermediate rule discovered.

Required:

1. precise domains and quantifiers;
2. proof of every implication;
3. smallest exact countermodel for every failed converse;
4. distinction between arbitrary carrier states and states typed as active retained branches;
5. distinction between nonempty witness support and nonzero signed aggregate.

Deliver:

`F5A_BRANCH_FAITHFULNESS_AXIOM_LATTICE_CLASSIFIED`.

## 6. Q2 — consistency with canonical BRC operations

For each serious admission candidate, test consistency with:

- concrete Path-formal branching;
- natural-number augmentation;
- signed completion and old signed cancellation;
- two individually faithful branches recoalescing to signed aggregate zero;
- same-terminal recoalescence;
- marker erasure;
- typed composition/concatenation;
- translation covariance;
- minimal `(1,1)` commuting diamond;
- fixed-trace path families.

The rule must not silently turn final cancellation into impossibility. Pre-collapse branch faithfulness and post-recoalescence aggregate support are different predicates.

Deliver:

`F5A_CANONICAL_BRC_CONSISTENCY_CLASSIFIED`.

## 7. Q3 — composition and refinement closure

Determine whether elementary faithfulness propagates automatically to arbitrary finite refinement trees.

Classify exactly:

- whether A0 implies A4;
- whether additional functorial/inductive data are required;
- whether a faithful parent may refine into a projection-zero child while the descendant family remains faithful;
- behavior under repeated splitting and branch regrouping;
- dependence on serialization order and marker relabeling;
- whether descendant-family faithfulness is stable under tree contraction/expansion.

Give theorem-level necessary and sufficient closure conditions, not only depth-bounded examples.

Deliver:

`F5A_REFINEMENT_COMPOSITION_CLOSURE_CLASSIFIED`.

## 8. Q4 — minimal F4-loophole closure

Using the accepted F5R countermodel only as an independence witness, determine the weakest candidate that excludes the pure-enrichment elementary branch pattern

`(nonzero old projection, zero old projection)`

while preserving kernel enrichment attached to old-supported branches.

Required:

- prove that the selected candidate closes the elementary F4 loophole;
- prove that every strictly weaker candidate fails, with exact countermodel;
- show whether global support reflection is unnecessarily strong;
- state whether hidden kernel states may still exist off the active-branch type;
- state whether two faithful branches may carry opposite signed projections and cancel later.

Deliver:

`F5A_MINIMAL_LOOPHOLE_CLOSING_RULE_CLASSIFIED`.

## 9. Q5 — conservativity and ontology cost

For every candidate surviving Q1–Q4, determine whether adjoining it:

- changes any existing canonical Boolean/N/Path-formal theorem;
- forbids any existing canonical path witness;
- changes path counts or typed terminals;
- merely restricts which enriched states may be declared active branches;
- requires adding a new branch-to-witness map/data structure;
- requires noncanonical choices;
- is invariant under authorized relabeling and translation;
- creates obligations on future coefficient enrichments.

Produce exact extension models showing consistency when claimed. If a rule cannot be interpreted without extra structure, specify that structure and classify whether it is data, law or axiom.

Deliver:

`F5A_CONSERVATIVITY_AND_ONTOLOGY_COST_CLASSIFIED`.

## 10. Q6 — admission verdict and conditional rank statement

Based only on Q1–Q5, decide whether any candidate should be:

- admitted as a minimal typed axiom;
- admitted only for elementary refinement events;
- retained as a model-relative optional extension;
- deferred;
- rejected.

If and only if a rule forcing both elementary projections nonzero is recommended for admission, state the F4 consequence only as a separate conditional theorem:

`GLOBAL_ZERO_SEPARATION + ADMITTED_BRANCH_FAITHFULNESS => torsion_free_rank(C) >= 2`.

Do not construct or classify rank-two carriers.

Deliver:

`BRANCH_TO_OLD_SUPPORT_FAITHFULNESS_AXIOM_ADMISSION_STATUS_CLASSIFIED`.

## 11. Mandatory ablations

At minimum ablate one at a time:

1. the active-branch type restriction;
2. concrete-witness support data;
3. nonzero signed projection;
4. leafwise closure;
5. descendant-family closure;
6. total old-coordinate conservation;
7. signed cancellation compatibility;
8. translation/relabeling covariance;
9. composition/refinement functoriality.

For each, record whether loophole closure, conservativity, cancellation, or interpretability fails.

## 12. Deterministic checker

Required path:

`scripts/cbrc_f5a_validate_branch_ontology_axiom_admission.py`

Minimum coverage:

- exact finite refinement trees through depth at least `4`;
- A0–A4 implication/countermodel witnesses;
- the accepted F5R kernel-branch countermodel;
- candidate-true signed branches with later exact cancellation;
- minimal `(1,1)` two-witness fiber;
- tree contraction/expansion checks;
- marker relabeling and translation invariance on finite typed toys;
- all mandatory ablations;
- zero theorem/model mismatches.

Enumeration is evidence only. General semantic implications and closure claims require proof.

## 13. Materialization checkpoints

### Checkpoint A

After candidate-lattice and minimality theorems stabilize, push drafts of:

- `research_reports/CBRC_F5A_BRANCH_ONTOLOGY_AXIOM_ADMISSION_RETURN_20260825.md`;
- `research_reports/CBRC_F5A_AXIOM_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`.

### Checkpoint B

Before final verdict, push:

- `research_reports/CBRC_F5A_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`;
- `scripts/cbrc_f5a_validate_branch_ontology_axiom_admission.py`.

Run the exact pushed checker and record byte identity, result and digest.

### Checkpoint C

Push final manifest:

`evidence/cbrc_f5a_branch_ontology_axiom_admission_manifest.json`.

Verify the remote branch after every checkpoint.

## 14. Required artifacts

1. `evidence/cbrc_f5a_execution_stamp.json`;
2. `research_reports/CBRC_F5A_BRANCH_ONTOLOGY_AXIOM_ADMISSION_RETURN_20260825.md`;
3. `research_reports/CBRC_F5A_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`;
4. `research_reports/CBRC_F5A_AXIOM_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`;
5. `scripts/cbrc_f5a_validate_branch_ontology_axiom_admission.py`;
6. `evidence/cbrc_f5a_branch_ontology_axiom_admission_manifest.json`.

## 15. Hard acceptance gate

Driver acceptance requires:

`F5A_BRANCH_FAITHFULNESS_AXIOM_LATTICE_CLASSIFIED`;

`F5A_CANONICAL_BRC_CONSISTENCY_CLASSIFIED`;

`F5A_REFINEMENT_COMPOSITION_CLOSURE_CLASSIFIED`;

`F5A_MINIMAL_LOOPHOLE_CLOSING_RULE_CLASSIFIED`;

`F5A_CONSERVATIVITY_AND_ONTOLOGY_COST_CLASSIFIED`;

`BRANCH_TO_OLD_SUPPORT_FAITHFULNESS_AXIOM_ADMISSION_STATUS_CLASSIFIED`;

`TARGET_LEAK_AUDIT_PASS`;

plus publication-liveness checkpoints and deterministic checker evidence.

## 16. Freeze / stop

Freeze on the owner branch and report owner head, artifact SHA-256s, checker digest/result, clean-tree status and primary verdict.

Stop after freeze. Do not open F6, construct rank-two carriers, compare downstream wave structures or promote Foundation axioms without Driver review.

---

Driver issue note:

`F5R PROVES THE BRANCH CONDITION IS NEW; CLASSIFY THE MINIMAL TYPED AXIOM AND ITS ADMISSION COST BEFORE ANY RANK-TWO CONTINUATION.`