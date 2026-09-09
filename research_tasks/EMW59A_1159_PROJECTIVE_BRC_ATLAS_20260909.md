<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "EM-FREE-W59A-ISSUE1159-WALLIS-SINE-ROTATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-EMW59A-1159-PROJECTIVE-BRC-ATLAS",
  "title": "Issue 1159 projective spectral factors and BRC rotation-atlas integration",
  "frontier": "The later free-research branch compresses complement-paired primitive spectral roots into projective factors and proposes an oriented rational BRC rotation chart, spectral quotient/root-block compression, formal-group division-polynomial behavior, primitive Jacobian quotients, conductor/complement identities, Galois traces, and Ramanujan-sum formulas. These claims have not yet been integrated with the current primitive BRC semantic layer or audited for which parts are native versus effective.",
  "next_action": "Read the state-machine handoff and the projective conductor/Ramanujan trace notes, reconstruct the exact projective factor definitions and complement action, then test whether the oriented BRC chart and division-polynomial structure are derivable from admissible finite rotation primitives or only provide an effective arithmetic atlas.",
  "dependencies": [],
  "source_refs": [
    "research_notes/EM_FREE_W59A_ISSUE1159_STATE_MACHINE_HANDOFF_20260909.md",
    "research-branch:free/1159-internal-phase-euler-w59a@9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c",
    "research_notes/PROJECTIVE_SPECTRAL_CONDUCTOR_AND_COMPLEMENT_SHEETS_20260905.md",
    "research_notes/RAMANUJAN_SUMS_AS_PROJECTIVE_SPECTRAL_GALOIS_TRACES_20260905.md",
    "research-commit:e98bb1b8dca13b3556e56b0eabfdffaac9beb36c",
    "research-commit:d5c3274743f1e4eee66f3685e56bf3c0d5a516a7",
    "research-commit:fe0871e6ff11563dd961c064c373b99020978c7a"
  ],
  "evidence_status": "FREE_RESEARCH_1159_DURABLE_HANDOFF_20260909",
  "last_progress_ref": "research_notes/EM_FREE_W59A_ISSUE1159_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:59:00+08:00",
  "hard_block": "PROJECTIVE_SPECTRAL_TO_BRC_SEMANTIC_INTEGRATION",
  "tags": ["EM-FREE-W59A", "issue-1159", "projective-spectrum", "BRC", "rotation-atlas", "formal-group", "Galois-trace"],
  "registry_key": "RS-EMW59A-1159-PROJECTIVE-BRC-ATLAS",
  "identity_lane": "RW59BRC",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# Issue 1159 projective spectral factors and BRC rotation-atlas integration

Status: `READY / FREE-RESEARCH INTEGRATION`

## Mother question

Do the projective primitive factors extracted from the finite Dirichlet rotation spectrum provide a genuine admissible finite rotation atlas for BRC-type primitive geometry, or are the rational chart, formal-group, conductor, and trace structures only effective arithmetic coordinates on a different carrier?

## Frozen inputs and scope

Read the #1159 state-machine handoff first. Use the pinned internal-phase branch and preserve the latest conductor correction: for odd `d>1`, the corrected complement-sheet midpoint value is `|Omega_d(4)|=1`.

Consume the finite spectral algebra already established or under separate arithmetic audit; do not reclassify its roots as primitive BRC states merely because the formulas look rotational. The central task is semantic admissibility as well as algebraic correctness.

The projective spectral Galois and Ramanujan-trace formulas are theorem-candidates to rederive. Classical cyclotomic and formal-group language may be used as compatibility or effective-coordinate language after the carrier map has been typed.

## Hard target and required outputs

Hard target: `PROJECTIVE_SPECTRAL_TO_BRC_SEMANTIC_INTEGRATION`.

Deliver a typed integration theorem, obstruction, or split result covering:

1. Define the projective primitive factor `Omega_d`, its complement pairing, degree, denominator/conductor labels, and exact relation to the oriented primitive spectral factors.
2. Recheck the complement-sheet field identity and discriminant/midpoint consequences, including all parity and prime-power edge cases.
3. Reconstruct the oriented rational BRC rotation chart and the spectral quotient/root-block compression from the pinned research generations. State exactly which finite data are being quotiented or identified.
4. Analyze the proposed formal-group/division-polynomial behavior of the decimation family and determine whether it is an intrinsic algebraic law of the spectral carrier or an effective chart identity.
5. Audit the primitive Jacobian/binomial-completion claims and determine the precise geometric or algebraic object, if any, represented by those quotients.
6. Independently verify the native Galois/conductor action needed for the proposed projective trace basis and the Ramanujan-sum formula.
7. Compare the resulting object with the current primitive BRC/rotation substrate at the correct semantic layer. Identify the exact map if admissible; otherwise give a no-go showing which primitive relation cannot be preserved.
8. If a reusable chart or invariant survives, extract it through existing method/tool families after a coverage check rather than creating a duplicate mechanism.

## Research value to preserve

This is the bridge from a successful finite spectral arithmetic program back toward the project's primitive rotation geometry. A positive result would turn projective spectral factors into a reusable rational atlas; a negative result is equally important because it prevents an effective cyclotomic-looking coordinate system from being mistaken for native BRC semantics.

The conductor and Ramanujan-trace structures also offer unusually sharp arithmetic invariants for testing any proposed carrier map.

## Success, kill, and return criteria

Success is an exact typed bridge identifying which projective spectral structures survive as admissible BRC rotation data, with all algebraic identities independently checked and the corrected conductor law preserved.

Kill any route that equates two carriers merely from matching spectra, matching Galois groups, or a shared polynomial recurrence. Matching observables are evidence for a bridge, not a proof of carrier identity.

If no native bridge exists, return the strongest effective atlas theorem plus the first primitive relation or semantic requirement that obstructs native identification.