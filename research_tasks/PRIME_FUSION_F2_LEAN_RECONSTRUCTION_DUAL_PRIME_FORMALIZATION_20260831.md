<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-FUSION-F2-LEAN-RECONSTRUCTION-DUAL-PRIME-FORMALIZATION",
  "title": "Prime Fusion F2 — Lean Reconstruction and Dual-Prime Formalization",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "PRIME_FUSION_T7_T8_ACCEPTED_MATHEMATICS_LEAN_FORMALIZED_NO_SORRY_WITH_PINNED_BUILD_PASS",
  "next_action": "Reuse the integrated F1 PrimeFusion modules to formalize only the Driver-accepted T7 idempotent reconstruction theorem and T8 dual-prime finite-quotient characterization at their accepted exact/strengthened scope, preserving canonical channel labels and negative controls, then run the pinned warnings-fatal EnterpriseMath build and axiom audit.",
  "dependencies": [
    "driver_reviews/PRIME_FUSION_F1_LEAN_FINITE_ALGEBRA_FORMALIZATION_DRIVER_REVIEW_20260825.md@blob:c50ecb08ba632ccd8bc37e98bc53dd6612d2232d",
    "driver_reviews/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_DRIVER_REVIEW_20260824.md@blob:e6a83670108f77c37676c098afc10c4ae2371e45",
    "EnterpriseMath/PrimeFusion/Channels.lean@blob:598579174c08d34204934fe0925c6cfa21141877",
    "EnterpriseMath/PrimeFusion/PointedRecovery.lean@blob:df40c37ebd99a8046e4c9f08ff705ea9205cf406",
    "EnterpriseMath/PrimeFusion.lean@blob:c361329898ea4358fadb63cd644cff1ed99c158d",
    "lean-toolchain@blob:c084c7fbe586b0276863b66f16d2955a43bc3fc6"
  ],
  "source_refs": [
    "driver_reviews/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_DRIVER_REVIEW_20260824.md@blob:e6a83670108f77c37676c098afc10c4ae2371e45",
    "driver_reviews/PRIME_FUSION_F1_LEAN_FINITE_ALGEBRA_FORMALIZATION_DRIVER_REVIEW_20260825.md@blob:c50ecb08ba632ccd8bc37e98bc53dd6612d2232d"
  ],
  "evidence_status": "T7_T8_DRIVER_ACCEPTED_MATHEMATICS / F1_LEAN_MAIN_AVAILABLE / NO_EXISTING_F2_FOUND / NO_NEW_MATHEMATICS",
  "tags": ["prime-fusion","F2","Lean","T7","T8","reconstruction","dual-prime","finite-quotient","no-sorry"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-FUSION-F2-LEAN-RECONSTRUCTION-DUAL-PRIME-FORMALIZATION",
  "parent_objective_id": "OBJ-PRIME-FUSION-MACHINE-CHECKED-THEOREM-PACKAGE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFF2",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-FUSION-F1-LEAN-FINITE-ALGEBRA-FORMALIZATION",
  "successor_gate": {
    "new_information_gap": "F1 is Lean-checked through T1-T6 and corrected T10/T11 interfaces, while the independently Driver-accepted T7 reconstruction theorem and T8 dual-prime finite-quotient characterization remain outside the proof-bearing Lean package.",
    "why_parent_result_does_not_close_it": "F1 explicitly deferred full T7/T8 and exported only interfaces such as the diagonal square pair, channel labels, idempotent split and pointed recovery. Written exact proofs and independent checkers do not establish Lean elaboration, API compatibility or axiom cleanliness for the later T7/T8 statements.",
    "discriminating_outcomes": [
      "T7 and T8 formalize at accepted exact/strengthened scope with no sorry/admit/custom axioms and the pinned full build passes",
      "Lean exposes an exact statement/API mismatch requiring Driver return without changing theorem strength",
      "a library representation obstruction is isolated while the accepted mathematics remains unchanged",
      "one strengthened convenience statement is too expensive or unnatural in Lean but the exact accepted source-strength theorem is formalizable and the distinction is recorded"
    ],
    "kill_condition": "Stop if completion requires weakening T7/T8, adding an unreviewed hypothesis, changing canonical Gaussian/Eisenstein channel attachment, treating finite computation as a general proof, introducing a custom axiom, or absorbing T9/T12-T15 as hidden scope expansion.",
    "alternative_route_or_free_exploration_considered": "Prime Fusion could remain at mixed written/Lean evidence strength, and unrelated free research remains available. Formalizing T7/T8 is preferred because the mathematics is already independently accepted and the current F1 API exposes the exact square/idempotent/channel interfaces needed, so this is a bounded proof-kernel gap rather than theorem rediscovery.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "F1 is already Driver-accepted and merged at its declared boundary. Reopening it would blur an audited finite-algebra slice with later reconstruction/field-characterization theorems; F2 preserves the accepted stage boundary and makes the new proof obligations independently falsifiable."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Prime Fusion F2 — Lean Reconstruction and Dual-Prime Formalization

Status: `READY / FORMALIZATION / NO NEW MATHEMATICS / T7-T8 ONLY`

## Mother question

Can the independently Driver-accepted T7 reconstruction theorem and T8 dual-prime finite-quotient characterization be represented at exact accepted strength in the repository-pinned Lean/mathlib environment, reusing the existing F1 PrimeFusion proof kernel without theorem weakening or new mathematical assumptions?

## Frozen inputs and scope

The mathematical authority is the Driver-accepted T4/T7/T8 exact-closure review. The proof-engineering baseline is the merged F1 PrimeFusion Lean package on current main.

This task contains **no new theorem-discovery authority**. If the written accepted mathematics and the proposed Lean statement diverge, return the mismatch; do not modify the mathematics to make Lean easier.

Reuse existing declarations whenever possible, especially:

- `N`, `C`, `u`, `v` and `diagonal_square_pair`;
- `primitive_channels_isCoprime`, `channel_gcd_exact`;
- `Hmodulus_eq_mul`, `pointedCRT` and fixed channel projections;
- `pointed_idempotent_partition`, `pointed_idempotent_channel_recovery`;
- current quotient/CRT interfaces.

Do not create a competing general algebra library unless exact current-tool coverage is first checked and a real capability gap is recorded.

The pinned Lean toolchain is `leanprover/lean4:v4.33.0-rc2`. Use current main's pinned mathlib resolution and the exact command `lake build --wfail -KCI EnterpriseMath` as the final build gate.

## Hard target and required outputs

Hard target:

`PRIME_FUSION_T7_T8_ACCEPTED_MATHEMATICS_LEAN_FORMALIZED_NO_SORRY_WITH_PINNED_BUILD_PASS`.

### F2-L01 — T7 universal idempotent split interface

Formalize a source-facing theorem for idempotent `e mod H` showing that

`N = gcd(e,H)`, `C = gcd(e-1,H)`

automatically satisfy `N*C=H` and `gcd(N,C)=1`, at the exact integer/natural typing that best composes with existing F1 lemmas.

Reuse/generalize the existing idempotent partition proof rather than reproving prime-power splitting through a new framework.

### F2-L02 — T7 exact reconstruction gate

Formalize the accepted reconstruction theorem: from the ordered channel data obtained from the idempotent split, if

`N > C`,
`U = 3*N - 2*C`,
`V = 2*C - N`

are perfect squares with the required parity/integrality conditions supplied or derived at exact accepted strength, reconstruct positive integer `a,b` with channels exactly `N,C`; derive primitivity from channel coprimality rather than adding it unnecessarily.

Separate the diagonal-allowed positive theorem from strict interiority. Strict interiority is exactly the extra `V>0` / `N<2*C` gate.

Retain exact negative controls for square-gate and orientation hypotheses. Finite controls are regression only.

### F2-L03 — T8 dual-prime arithmetic equivalence

Formalize the accepted algebraic equivalence on the strongest clean family supported by the Driver review:

`N,C both prime <=> H=N*C is a square-free semiprime`

with the necessary nonzero/distinctness/channel conditions stated transparently. Do not silently replace “distinct prime fields with canonical channel attachment” by an unordered abstract product that forgets Gaussian versus Eisenstein labels.

### F2-L04 — T8 quotient/field characterization

Connect the arithmetic dual-prime theorem to the existing fixed product/quotient projections so that, at accepted source strength, the two components are finite prime fields of orders `N` and `C`, and conversely the fixed channel quotient being the product of two distinct prime fields forces the dual-prime condition.

Abstract product isomorphism alone is insufficient to recover channel labels; the formal theorem must retain the fixed projections/central idempotent attachment or explicitly separate unordered and channel-labelled versions.

### F2-L05 — integration and proof integrity

Add only the minimal new module(s), preferably `Reconstruction.lean` and `DualPrime.lean` or an equally narrow split. Import them through `EnterpriseMath/PrimeFusion.lean` once coherent.

Run `#print axioms` for the new load-bearing declarations. Required:

- no `sorry`;
- no `admit`;
- no custom axioms;
- no theorem target commented out as a substitute for proof;
- finite `native_decide` only for bounded regressions, never unbounded theorem proof;
- `lake build --wfail -KCI EnterpriseMath` passes.

## Research value to preserve

Prime Fusion currently has an unusually strong evidence chain: independently accepted written mathematics plus a clean Lean F1 kernel. T7/T8 are the natural gap between those layers. Closing them would make reconstruction and the dual-prime finite-quotient characterization proof-kernel checkable while preserving the exact channel typing that distinguishes Prime Fusion from an unordered CRT-product slogan.

## Success, kill, and return criteria

Success requires a one-to-one declaration map for T7/T8, warnings-fatal full build success, axiom audit, exact negative/regression controls and a frozen Result under the current execution/result contracts.

Return for revision rather than weakening a theorem if Lean exposes an interface mismatch. A representation-only obstruction is a valid terminal result if isolated precisely.

Stop after T7/T8. Do not absorb T9 or T12-T15, publication claims, performance claims, distribution claims, or new Prime Fusion mathematics into F2.
