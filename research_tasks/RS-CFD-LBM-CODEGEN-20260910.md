<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-LBM-CODEGEN-20260910",
  "title": "LBM structure-preserving code-generation feasibility",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "No confirmed missing transformation or performance gap.",
  "next_action": "Pin a current lbmpy example and inspect its generated collision/streaming code and bottleneck.",
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
    "lbm-codegen"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-LBM-CODEGEN-20260910",
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

# LBM structure-preserving code-generation feasibility

## Mother question

Is there a cost-relevant collision/streaming optimization beyond current lbmpy generation that preserves required moments and boundary behavior?

## Frozen inputs and scope

One declared velocity stencil and collision model; inspect existing symbolic simplification, generated kernels and memory traffic. Integer grids alone establish no special fit with Enterprise Math. Classical effective-model computation, not a native P000 fluid derivation. Keep signed/complex amplitudes, wavevector labels and declared observations distinct. No industrial acceleration, continuous-PDE certificate or novelty is assumed.

## Hard target and required outputs

Profile arithmetic and bandwidth, identify a missing legal transformation or return no gap, and compare generated kernels with existing optimizations under identical precision and boundary tests.

## Research value to preserve

A bounded negative result avoids an expensive route based only on surface similarities.

## Success, kill, and return criteria

Kill the route when memory traffic dominates and proposed algebra does not lower total cost, or when moment/boundary regressions appear. Return a documented capability map and one falsifiable candidate at most.
