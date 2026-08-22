<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GS-FQ009-ORIENTATION-TORSOR-ATLAS-STEWARD-VERIFICATION",
  "title": "FQ-20260822-009 Foundation Steward Verification — Orientation Torsor and Positive Atlas",
  "kind": "GOVERNANCE",
  "owner": "maintenance/fq009-orientation-torsor-atlas-steward-verification",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Steward verification of an answered Foundation question proposing to derive the positive three-axis atlas from an oriented origin triangle and typed carrier normal-form decoder.",
  "next_action": "Verify exact source alignment, minimality, torsor typing and no-quotient leakage against the current Foundation; accept the smallest safe refoundation, retain only part of it, require narrowing, or reject.",
  "dependencies": [
    "FQ-20260822-009 answered Foundation entry",
    "QRF-R3 independent verification return",
    "current native origin/cell/three-axis Foundation"
  ],
  "source_refs": [
    "Issue #164 FQ-20260822-009 / comment 5379130082",
    "research/qrf-r3-independent-foundation-verification:research_outputs/QRF_R3_INDEPENDENT_FOUNDATION_VERIFICATION_20260822.md@blob:43bd231209d15d071eb15b39c73e7bfdbabac984",
    "research/qrf-r3-independent-foundation-verification:research_outputs/qrf_r3_independent_foundation_verification.py@blob:e57c9f0004f992794d246a840237fe500a83afde",
    "awdawmip/enterprise-math@41a1bbdf23831f9ad2af160df4a6bd5603f22547:definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md"
  ],
  "foundation_questions": [
    "FQ-20260822-009"
  ],
  "evidence_status": "ANSWERED_READY_FOR_STEWARD_VERIFICATION",
  "last_progress_ref": "Issue #164 comment 5379130082",
  "last_progress_at": "2026-08-22T16:00:00+08:00",
  "hard_block": null,
  "tags": [
    "foundation-steward",
    "fq009",
    "qrf-r3",
    "orientation-torsor",
    "positive-atlas",
    "governance-verification"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "FQ009",
  "origin_kind": "FOUNDATION_QUESTION",
  "origin_foundation_question_id": "FQ-20260822-009",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9cb0f9abbec5b946fb67557c2ef8e7d371df3e5aa059d409da1192a55cf0eac2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# FQ-20260822-009 Foundation Steward Verification — Orientation Torsor and Positive Atlas

Status: `READY / DRIVER_APPROVED / STEWARD_VERIFICATION`

## 0. Task-local mother question

Does the answered FQ-20260822-009 justify replacing part of the current primitive declaration

`three positive native rays + canonical min-zero address atlas`

by the weaker typed package

`origin elementary carrier triangle + one selected orientation-torsor element + carrier translation + min-zero normal-form decoding`,

while preserving the current native metric, right-angle, cell and no-native-quotient boundaries exactly?

The task is verification and classification. Do not accept a refoundation merely because the orientation theorem is correct; verify that the proposed primitive package is actually aligned with the exact current Enterprise origin/cell carrier and does not smuggle back a forbidden native equivalence.

## 1. Frozen task-local inputs and scope

Use as evidence, not authority:

- the FQ-20260822-009 answered entry;
- the QRF-R3 independent verification report and its executable pressure tests.

Use the current canonical native Foundation as authority for:

- `O_E=0` as a triple cell-boundary intersection;
- the three neighboring origin-incident cell centers and triangular carrier structure;
- three positive native rays;
- canonical addresses `A_E={(a,b,c) in N_0^3:min(a,b,c)=0}`;
- `NO_NATIVE_DIAGONAL_SHIFT_QUOTIENT`;
- carrier relations being distinct from native vector identities;
- the existing native `120 degree` right-angle and sector-local scalar law.

The candidate datum must be typed as an element `o in Or(T)` of the two-sheet orientation torsor of the unlabeled elementary triangle, not as a detached Boolean with intrinsically named `0/1` values.

Do not use QRF-R2, Gaussian/C4 algebra, R063 holonomy, path collapse, or a Euclidean clockwise convention as premises for acceptance.

## 2. Required Steward verification outputs

### A. Exact current-source alignment of the origin triangle

Verify from the current Foundation that the three cells incident at the native origin determine exactly the elementary carrier triangle required by the returned construction.

Answer explicitly:

- whether that triangle is canonically identifiable from the current origin/cell incidence data;
- whether any existing accepted datum already selects one cyclic orientation sheet;
- whether the current classical carrier embedding contributes only presentation information or already carries an accepted native chirality.

If an accepted current native datum already selects a sheet, the new orientation datum is redundant and the candidate must be narrowed.

### B. Orientation torsor obstruction and typing

Independently verify:

`Aut(T) ~= S3`,

with the two cyclic orientations forming the quotient torsor

`S3/A3 ~= C2`,

and no full-automorphism-fixed orientation section from bare unlabeled incidence plus the frozen translation structure.

Check that the proposed primitive is exactly one selected torsor element and does not require a distinguished base edge, first vertex, absolute axis ordering, metric orientation or extra sign datum.

### C. Sufficiency and minimality for the positive atlas

Verify that one orientation element canonically orients the three boundary translation classes cyclically and generates the three positive direction families by nonnegative iteration.

Check equivariance under cyclic gauge relabeling and the exact reflection behavior between the two orientation sheets.

Distinguish the unlabeled cyclic three-direction object from a serialized tuple `(E1,E2,E3)`. Absolute axis names must remain gauge unless the current Foundation independently supplies more structure.

### D. Min-zero decoder and no-native-quotient audit

Verify the returned carrier theorem:

`ker(Phi)=Z(1,1,1)`

for the coefficient presentation of the three directed carrier translations, and verify existence and uniqueness of the min-zero normal form obtained by subtracting the common minimum.

Then audit the semantic layer strictly:

- diagonal equivalence may exist only among carrier coefficient presentations;
- the decoder may select one unique min-zero representative;
- native address equality inside `A_E` remains literal componentwise/function equality;
- no statement may install `(a,b,c)~(a+k,b+k,c+k)` as native ontology.

If the proof cannot be stated without reintroducing a native quotient, reject the decoder part.

### E. Exact refoundation boundary

Determine what, if anything, may become derived from the accepted package.

At minimum distinguish:

1. selection of the three positive direction families;
2. gauge-labeled serialization of the three channels;
3. carrier-to-native min-zero decoding;
4. the native `120 degree` right-angle law;
5. the sector-local quadratic scalar law;
6. circle-cell radius/overlap structure;
7. path/provenance fibers.

QRF-R3 by itself does not derive items 4 through 7. A positive verdict must not silently claim otherwise.

If full atlas+decoder acceptance is too strong but the orientation result is sound, state the smallest surviving refoundation and keep the rest primitive.

### F. Minimal Foundation-delta classification

If accepted, state the exact minimal Foundation rewrite needed to replace only the justified primitive declarations while preserving all existing metric, cell, coordinate-equality and path boundaries.

List the exact current Foundation surfaces that would require consistency edits. Do not perform those edits in this task.

## 3. Verdict taxonomy, acceptance bar, and stop conditions

Return exactly one leading verdict:

- `ACCEPT_FQ009_MINIMAL_ORIENTATION_TORSOR_REFOUNDATION`
- `ACCEPT_FQ009_ORIENTATION_ONLY_KEEP_ADDRESS_PRIMITIVE`
- `NEEDS_NARROWER_FQ009`
- `REJECT_FQ009_FOUNDATION_CHANGE`

`ACCEPT_FQ009_MINIMAL_ORIENTATION_TORSOR_REFOUNDATION` requires all of the following:

1. the origin elementary triangle is canonically available from current accepted origin/cell incidence;
2. no accepted current native datum already selects an orientation sheet;
3. one orientation-torsor element is necessary and sufficient for the positive three-direction atlas without hidden base/order/metric structure;
4. the min-zero decoder is theorem-level correct and cleanly confined to carrier representation;
5. native diagonal quotient leakage is absent;
6. the proposed refoundation leaves current metric/right-angle/cell/path laws untouched except where an exact derivation is independently verified.

Return `ACCEPT_FQ009_ORIENTATION_ONLY_KEEP_ADDRESS_PRIMITIVE` if the orientation-torsor derivation of the positive rays is sound but the min-zero decoder should remain carrier/implementation structure rather than a Foundation derivation of native addresses.

Return `NEEDS_NARROWER_FQ009` if one or more theorem statements are sound but the current source does not yet type the origin triangle, translation carrier or orientation datum strongly enough for a safe Foundation replacement.

Return `REJECT_FQ009_FOUNDATION_CHANGE` if the bit/torsor is redundant, insufficient without hidden structure, dependent on a metric embedding, or if the decoder reinstates the forbidden native diagonal quotient.

Stop once one verdict is justified by the smallest decisive evidence. The return must contain the verified minimal primitive package, the exact no-go/minimality statement, the representation-versus-ontology boundary, exact current-source comparison, and a bounded change recommendation.