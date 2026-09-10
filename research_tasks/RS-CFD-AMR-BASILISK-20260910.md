<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-AMR-BASILISK-20260910",
  "title": "Basilisk observable-driven adaptation feasibility",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "No demonstrated observer-sensitive improvement over the public baseline.",
  "next_action": "Pin one Basilisk example and its current adaptation rule; identify what the chosen output needs that local wavelet error omits.",
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
    "amr-basilisk"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-AMR-BASILISK-20260910",
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

# Basilisk observable-driven adaptation feasibility

## Mother question

Can a target-observable error indicator improve mesh allocation beyond the existing wavelet-adaptation baseline?

## Frozen inputs and scope

One public incompressible-flow example and a fixed global observable. Existing wavelet adaptation is prior machinery, not a new contribution. Classical effective-model computation, not a native P000 fluid derivation. Keep signed/complex amplitudes, wavevector labels and declared observations distinct. No industrial acceleration, continuous-PDE certificate or novelty is assumed.

## Hard target and required outputs

Compare a proposed observer-sensitive indicator with existing wavelet criteria using the same accuracy target. Preserve boundary and conservation behavior; count indicator, refinement and solve costs.

## Research value to preserve

Connects retained local information to an actual global output rather than merely reducing cell count.

## Success, kill, and return criteria

Return a bounded go/no-go result, counterexample or clearly stated missing stability estimate. Do not claim an indicator is a rigorous bound without propagation analysis.
