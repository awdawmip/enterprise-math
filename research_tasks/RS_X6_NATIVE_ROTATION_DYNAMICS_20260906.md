<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-X6-NATIVE-ROTATION-DYNAMICS",
  "title": "Native X6 rotation dynamics beyond static axis permutations",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "X6 spatial Cell identity, signed adjacency, S6 axis-permutation skeleton and restricted FCC C6/C12 microtraces are closed, but complete native rotation remains undefined as a Cell/path dynamics rather than a static relabeling.",
  "next_action": "Define the intrinsic signed C6 generator on an arbitrary oriented three-axis selection, compute the group generated over all triads, and lift each macrostep to the exact BRC Cell-path fiber while preserving provenance under composition.",
  "dependencies": [
    {"target":"P000 V5 + ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905","action":"CONSUME","satisfied":true},
    {"target":"VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905","action":"CONSUME","satisfied":true},
    {"target":"VIETE_PHASE_REFINEMENT_VS_PRECISION_PROSTATE_CLOCK_20260905","action":"CONSUME","satisfied":true}
  ],
  "source_refs": [
    "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json",
    "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md",
    "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md",
    "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"
  ],
  "evidence_status": "SPATIAL_FOUNDATION_CLOSED_ROTATION_DYNAMICS_OPEN",
  "last_progress_ref": "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
  "last_progress_at": "2026-09-05T11:53:48Z",
  "hard_block": null,
  "tags": ["X6","rotation","C6","C12","BRC","triadic","path-provenance"],
  "claim_lease_minutes": 120,
  "created_by_role": "FREE_RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-X6-NATIVE-ROTATION-DYNAMICS",
  "parent_objective_id": "PO-X6-UPPER-STRUCTURE-20260906",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "X6U",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": null,
  "successor_gate": "DIRECT_USER_UPPER_STRUCTURE_ATTACK_AFTER_X6_SPATIAL_FOUNDATION_CLOSED",
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:fbe51ab884e1267b7bb6de0de598ad5504fd0d67d1570475115a9a16a6ec4ca0","review_state":"PASS","temporary_overrides":[]}
}
-->

# RS-X6-NATIVE-ROTATION-DYNAMICS

Status: `PUBLISHED_REGISTERED / CLAIMABLE / DIRECT_USER_DIRECTION`

## Mother question

What is a native rotation in signed Cell-centered X6 when rotation must be realized as typed Cell/path dynamics rather than identified with a static coordinate relabeling or a carrier fixed-radius curve?

## Hard target

1. Separate static signed-frame isometries, positive-axis label permutations, observer rotations, and physical Cell trajectory dynamics.
2. Derive exact local triadic/C6 generators on arbitrary oriented three-axis selections and classify their full six-axis generated group.
3. Lift macro rotations to Path-formal/N/Weighted-BRC fibers. Prove which quotients are operation-safe under repeated composition.
4. Reconcile local `C3`, signed `C6`, native `C12` outer microcycle, half-turn, reversal and current principal root lineage in one typed hierarchy.
5. Determine the minimum memory/state required for an atlas-wide rotation successor; preserve branch bit, incoming phase, frame and time variables unless a factorization theorem removes them.
6. Return either a complete native rotation dynamics, a maximal exact restricted dynamics, or a sharp obstruction explaining the missing native relation.

## Hard boundaries

- `S6` by itself is not the answer; it is the current positive-axis relabeling skeleton.
- A signed lattice isometry is not automatically a physical rotation law.
- No primitive Cell microstep preserves exact nonzero native radius.
- Shortest-path choice is not globally safe unless future composition is proved insensitive to the discarded paths.
- Do not use classical 90-degree orientation or determinant sign as native angular semantics without a separate Enterprise definition.
