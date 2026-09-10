<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-CANCELLATION-GROUPS-20260910",
  "title": "Cancellation-preserving Fourier defect groups",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "No cheap validated cancellation-preserving grouping bound is established.",
  "next_action": "Freeze the output observer and compare legal output-fiber grouping with deliberately unsafe equal-shell compression.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@13a7cdc9dfac3b7f6d7120f7b020733d7c91f964:research_notes/CFD9R2K7/cfd_public_algorithm_probe_20260910.json",
    "spectralDNS/spectralDNS:spectralDNS/solvers/NS.py@blob:6a11909d1e2c1d529d382952c4c9d77e7073645c",
    "research_notes/CFD-B1F673/prior_3d/probe.py"
  ],
  "evidence_status": "EXPLORATORY_INPUTS_NOT_INDEPENDENTLY_REVIEWED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "CFD",
    "user-directed-20260910",
    "cancellation-groups"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-CANCELLATION-GROUPS-20260910",
  "parent_objective_id": "OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "CFD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Cancellation-preserving Fourier defect groups

## Mother question

Which branch groupings yield tighter affordable defect bounds without losing phase, output direction or future-operation information?

## Frozen inputs and scope

Finite retained Fourier operators; preserve p+q, vector projection and conjugacy. Equal frequency lengths alone do not identify 3D modes. Positive branch-mass theorems do not prove signed cancellation. Classical effective-model computation, not a native P000 fluid derivation. Keep signed/complex amplitudes, wavevector labels and declared observations distinct. No industrial acceleration, continuous-PDE certificate or novelty is assumed.

## Hard target and required outputs

Define admissible grouping keys, prove the grouping law, build an independent checker and compare termwise, grouped and exact finite defects including grouping cost. Include direction and opposite-phase counterexamples.

## Research value to preserve

Triangle-inequality bounds can be too loose; tighter valid groups may make conservative pruning usable.

## Success, kill, and return criteria

Pass only with a precise observer/future-operation domain and tests against exact finite sums. Kill a quotient that merges inequivalent outputs or a grouping whose complete cost defeats its purpose. Return a theorem/proof candidate or an explicit obstruction.
