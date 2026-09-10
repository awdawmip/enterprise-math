<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-TRAJECTORY-VERIFY-20260910",
  "title": "Independent trajectory and benchmark verification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "No independent complete-solver comparison or trajectory certificate is available.",
  "next_action": "Freeze an independent validation matrix and check imported source/result identities before rerunning only verification-required cases.",
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
    "trajectory-verify"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-TRAJECTORY-VERIFY-20260910",
  "parent_objective_id": "OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "CFD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "REPLAY",
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

# Independent trajectory and benchmark verification

## Mother question

Do the sparse, dense and hybrid implementations compute the declared finite dynamics, and do any cost gains survive complete trajectories?

## Frozen inputs and scope

Independent reviewer must not be the main implementation author. Distinguish the attached 3D microbenchmark from CFD9R2K7 2D data. Freeze input seeds, time horizon, hardware metadata, precision and error metrics. Classical effective-model computation, not a native P000 fluid derivation. Keep signed/complex amplitudes, wavevector labels and declared observations distinct. No industrial acceleration, continuous-PDE certificate or novelty is assumed.

## Hard target and required outputs

Reproduce invariants and analytical cases; test support growth, conjugacy, divergence, energy behavior, timestep refinement and dense fallback. Compare with an actual pinned public solver when dependencies permit. Classify finite-map, trajectory and PDE claims separately.

## Research value to preserve

Prevents single-RHS improvements or floating agreement from being promoted to solver/PDE guarantees.

## Success, kill, and return criteria

Report every failure and all end-to-end costs. A verification pass is scoped to frozen cases; no universal or physical claim follows. Return an independent report with exact source hashes and unresolved certificate obligations.
