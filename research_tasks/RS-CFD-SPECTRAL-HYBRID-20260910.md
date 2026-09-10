<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-SPECTRAL-HYBRID-20260910",
  "title": "Spectral hybrid evaluation and full-trajectory cost",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Full-trajectory 3D integration and support-aware fallback are not yet tested.",
  "next_action": "Verify the imported 3D probe hashes, add a no-pruning RK4 hybrid, and run held-out sparse and dense trajectories.",
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
    "spectral-hybrid"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-SPECTRAL-HYBRID-20260910",
  "parent_objective_id": "OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "CFD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
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

# Spectral hybrid evaluation and full-trajectory cost

## Mother question

Can a support-aware sparse/FFT nonlinear evaluator reduce total cost at matched accuracy, without silently discarding newly generated modes?

## Frozen inputs and scope

Periodic incompressible flow. Start from the attached 3D probe; the separate 2D CFD9R2K7 checkpoint is evidence only, not interchangeable code or a 3D theorem. Freeze FFT normalization, retained cube, de-aliasing, viscosity, precision and time integrator before comparison. Classical effective-model computation, not a native P000 fluid derivation. Keep signed/complex amplitudes, wavevector labels and declared observations distinct. No industrial acceleration, continuous-PDE certificate or novelty is assumed.

## Hard target and required outputs

Implement a no-pruning hybrid with complete generated outputs and density fallback; add full-trajectory tests and held-out seeds; report detection, allocation, nonlinear evaluation and total elapsed cost. Then expose a separate optional pruning interface, whose bounds are not confused with trajectory error. Provide a spectralDNS-compatible serial adapter and state whether the original host was actually run.

## Research value to preserve

Single-RHS gains exist but exact support fills rapidly; preserve the negative 2D full-trajectory result. A usable integration or a demonstrated cost obstruction is valuable.

## Success, kill, and return criteria

Pass a bounded implementation checkpoint only if hybrid and reference agree within declared numerical tolerances on all frozen tests and raw timings are retained. Speedup requires matched-accuracy total-cost evidence, not a kernel ratio. Stop a losing configuration and retain FFT fallback. Return code, cases, results, limitations and next unresolved unit.
