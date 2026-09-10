<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-ROM-ITHACA-20260910",
  "title": "ITHACA-FV output-aware reduced-model feasibility",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "No selected example, held-out output test or cost model exists.",
  "next_action": "Inspect one current incompressible ITHACA-FV example and freeze a single observable and baseline.",
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
    "rom-ithaca"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-ROM-ITHACA-20260910",
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

# ITHACA-FV output-aware reduced-model feasibility

## Mother question

Can output-aware mode retention improve a repeated incompressible-flow design calculation compared with existing POD-Galerkin and DEIM baselines?

## Frozen inputs and scope

One simple single-phase geometry and fixed parameter range; choose a pressure-drop or flow observable. Treat existing ITHACA-FV algorithms as baselines; no native-P000 or universal reduced-model claim. Classical effective-model computation, not a native P000 fluid derivation. Keep signed/complex amplitudes, wavevector labels and declared observations distinct. No industrial acceleration, continuous-PDE certificate or novelty is assumed.

## Hard target and required outputs

Pin a public example, document full/reduced interfaces, run a bounded held-out comparison and propose an error-triggered enrichment/fallback rule. Include training/snapshot and online costs.

## Research value to preserve

Repeated related simulations may benefit even when one unrestricted solve does not.

## Success, kill, and return criteria

Stop after the bounded feasibility comparison if no useful accuracy/cost window appears. Do not substitute a generic dimension reduction claim for measured output quality. Return a reproducible go/no-go report.
