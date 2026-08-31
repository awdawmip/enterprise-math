<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GS-FQ010-N2-SCALE-ROLE-STEWARD-DISPOSITION",
  "title": "FQ-20260823-010 Foundation Steward Disposition — Relation Readout and Squared Line-Scale Role",
  "kind": "GOVERNANCE",
  "owner": "maintenance/fq010-n2-scale-role-steward-disposition",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "CRITICAL",
  "frontier": "FOUNDATION_STEWARD_REVIEW_OF_FQ010_N2_SCALE_ROLE_AND_SOURCE_DISPOSITION",
  "next_action": "Using the frozen R065 and FQ010 packets, decide exactly one source-level semantic disposition for the canonical relation readout |[R_type]| and its possible squared-line-scale role, while preserving realization-class typing and forbidding source mutation before the residual N2 role is explicitly classified.",
  "dependencies": [
    "driver_reviews/R065_PHASEA_PRIMITIVE_INTRINSIC_FINITE_READOUT_DRIVER_REVIEW_20260822.md@18f429470bcb5b7df41c46dad2c5a29964629a09",
    "driver_reviews/FQ010_LINE_SCALE_SEMANTIC_ADMISSION_COMPARATIVE_REFOUNDATION_DRIVER_REVIEW_20260823.md@1dd81fcb6282c1b00ff9675ef256a50d4d198bda",
    "projects/enterprise-math/FOUNDATION_COMPONENT_RELATION_LINE_SCALE_READOUT.md@main"
  ],
  "source_refs": [
    "research/fq010-line-scale-semantic-admission",
    "driver_reviews/R065_PHASEA_PRIMITIVE_INTRINSIC_FINITE_READOUT_DRIVER_REVIEW_20260822.md@18f429470bcb5b7df41c46dad2c5a29964629a09",
    "driver_reviews/FQ010_LINE_SCALE_SEMANTIC_ADMISSION_COMPARATIVE_REFOUNDATION_DRIVER_REVIEW_20260823.md@1dd81fcb6282c1b00ff9675ef256a50d4d198bda",
    "projects/enterprise-math/FOUNDATION_COMPONENT_RELATION_LINE_SCALE_READOUT.md@main"
  ],
  "foundation_questions": [
    "FQ-20260823-010"
  ],
  "evidence_status": "ANSWERED_READY_FOR_STEWARD_SEMANTIC_DISPOSITION",
  "last_progress_ref": "driver_reviews/FQ010_LINE_SCALE_SEMANTIC_ADMISSION_COMPARATIVE_REFOUNDATION_DRIVER_REVIEW_20260823.md@1dd81fcb6282c1b00ff9675ef256a50d4d198bda",
  "last_progress_at": "2026-08-23T20:10:00+08:00",
  "hard_block": null,
  "tags": [
    "foundation-steward",
    "fq010",
    "relation-first",
    "n2-readout",
    "line-scale",
    "semantic-disposition"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "FQ010",
  "origin_kind": "FOUNDATION_QUESTION",
  "origin_foundation_question_id": "FQ-20260823-010",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": "RS-FQ010-LINE-SCALE-SEMANTIC-ADMISSION-COMPARATIVE-REFOUNDATION",
  "successor_gate": "EXPLICIT_STEWARD_DISPOSITION_REQUIRED_BEFORE_FOUNDATION_SOURCE_MUTATION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# FQ-20260823-010 Foundation Steward Disposition — Relation Readout and Squared Line-Scale Role

Status: `READY / DRIVER_APPROVED / STEWARD_SEMANTIC_DISPOSITION`

Hard target:

`FOUNDATION_STEWARD_REVIEW_OF_FQ010_N2_SCALE_ROLE_AND_SOURCE_DISPOSITION`

Intended owner branch:

`maintenance/fq010-n2-scale-role-steward-disposition`

## 0. Task-local mother question

The mathematical comparison is closed. The remaining question is semantic and source-authoritative:

> Given that the typed component-partition relation isomorphism class is structurally stronger than its scalar cardinality, and that
>
> `Q_R = |[R_type]| = sum_c n_c^2`
>
> is a canonical available readout, what exact role—if any—should the current Foundation assign to that scalar as squared native line scale?

This is not a new theorem-search task. Do not rerun blind discovery, seek another scalar, or re-prove the already-reviewed equivalence.

## 1. Frozen accepted evidence

Use the following as frozen evidence:

1. R065 independently reconstructed the same-component/type equivalence structure from the blind primitive packet.
2. Relation-level clean independent replication is achieved.
3. Relation-cardinality lies inside the blind definability envelope, but primitive scalar uniqueness is false.
4. FQ010 established exact scalar-strength equivalence between the two-component relation-pair cardinality and the current FQ008 scalar readout.
5. The relation isomorphism class is strictly stronger than its scalar cardinality.
6. The accepted N0 object is the typed finite realization / component-partition relation isomorphism class, not the concrete token names or indices used by a finite-reasoning implementation.
7. The role declaration

   `SQUARED_NATIVE_LINE_SCALE := |[R_type]|`

   is not forced by N0 or by the scalar-equivalence theorem.
8. FQ008 axis-square calibration plus transverse independence remains an exact scalar characterization/calibration layer.

Do not rewrite the post-freeze equality as though R065 had selected the scalar or its geometric role.

## 2. Required semantic-layer ledger

The Steward return must explicitly separate these layers:

### N0 — structural object

`[R_type]`, the typed component-partition relation isomorphism class derived from component multiplicity/type content.

### N1 — canonical scalar readout

`Q_R := |[R_type]| = sum_c n_c^2`.

The availability and formula of this readout are theorem-level facts.

### N2 — role assignment

Whether `Q_R` is declared to be squared native line scale.

This is the residual semantic decision. It must not be hidden inside notation, calibration language, or a source edit.

### N3 — derived scalar characterization

The exact relation, if retained or admitted, between the chosen scale role and FQ008 axis-square plus transverse-independence laws.

For every layer state whether it is:

- canonical Foundation object;
- theorem-derived readout;
- explicit semantic declaration/calibration;
- implementation carrier only.

## 3. Exactly three admissible leading dispositions

Return exactly one of the following:

### A. `ADMIT_FQ010_N2_RELATION_CARDINALITY_AS_SQUARED_LINE_SCALE`

Explicitly declare

`SQUARED_NATIVE_LINE_SCALE := |[R_type]|`.

Requirements:

- explain why this semantic declaration improves the Foundation interface rather than merely changing notation;
- retain the N0/N1/N2 distinction in canonical prose;
- reclassify FQ008 axis-square plus transverse independence as derived characterization/calibration theorems at their existing sector-local scope;
- identify the smallest fresh current-main source integration needed;
- do not promote concrete token realization, token indices, or an arbitrary scalarization rule.

### B. `RETAIN_FQ010_HYBRID_RELATION_FIRST_WITH_SEPARATE_SCALAR_ADMISSION`

Preserve `[R_type]` as the deeper structural refoundation and retain FQ008 as the scalar admission/calibration interface.

Requirements:

- state that the relation-first result has explanatory/ontological compression without eliminating the N2 semantic selection;
- define the exact interface between the relation theorem card and the scalar Foundation section;
- prohibit wording that makes the scalar role appear uniquely forced by the relation;
- specify whether any source edit is required beyond routing/clarification.

### C. `DECLINE_FQ010_N2_SCALE_ROLE_RETAIN_FQ008_SCALAR_FIRST_INTERFACE`

Keep FQ008 scalar-first as the Foundation interface and register the relation route only as explanatory refoundation / derived theorem structure.

Requirements:

- give the exact semantic reason the N2 role is declined despite theorem-level scalar equivalence;
- retain the valid relation theorem and implementation-carrier boundary;
- state that declining the role does not refute R065 or FQ010 mathematics.

No fourth blended verdict is permitted. Any needed scope restriction must be expressed inside one of these three dispositions.

## 4. Realization-class and invariance audit

The return must verify:

- the accepted structural carrier is an isomorphism class, not a named token set;
- relation-cardinality survives allowed relabeling;
- the semantic role does not depend on token ordering, token names, or a privileged finite presentation;
- no carrier Euclidean metric, cross-sector point-to-point metric, angle, measure, curvature, or projection law is silently imported;
- any claim about line scale remains exactly at the presently authorized native scope.

If this typing cannot be stated without ambiguity, do not authorize canonical source mutation.

## 5. Source-disposition requirements

The Steward return must include an exact source plan:

1. whether a Foundation source change is authorized;
2. the minimum canonical files that would change;
3. the theorem/definition/calibration status of each proposed edit;
4. the disposition of stale PR `#587`, whose FQ008 scalar section predates FQ010;
5. whether FQ009 orientation-torsor content may be preserved separately;
6. the exact kill condition for a future integration PR.

Freeze:

`NO_EXPLICIT_N2_ROLE_CLASSIFICATION -> NO_CANONICAL_SCALAR_SOURCE_MUTATION`.

Any authorized source integration must be rebuilt from current main. Do not revive PR `#587` mechanically.

## 6. Non-goals and negative boundaries

This task must not:

- invent a new scalar or repeat blind scalar search;
- upgrade the concrete `U(n)` token realization to global N0;
- claim that relation-cardinality uniquely forces geometric meaning;
- introduce a new symmetric cross-sector distance;
- alter path/provenance fibers;
- import Gaussian, Eisenstein, Euclidean, conformal, Voronoi, Hodge, or factorization semantics;
- perform the canonical source integration itself;
- treat theorem equivalence alone as sufficient reason for a Foundation rewrite.

## 7. Required output

Produce one bounded Steward record:

`foundation_reviews/FQ010_N2_SCALE_ROLE_AND_SOURCE_DISPOSITION_20260823.md`

It must contain:

1. leading disposition;
2. N0/N1/N2/N3 semantic-layer ledger;
3. realization-class invariance audit;
4. exact source delta authorization or prohibition;
5. PR `#587` disposition;
6. negative boundary;
7. successor gate.

Stop once the semantic disposition is frozen. A later source integration, if authorized, is a separate `NO_NEW_MATHEMATICS` maintenance task.
