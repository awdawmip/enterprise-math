<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-ROUNDING-ENVELOPE-20260910",
  "title": "Low-cost outward-rounded pruning envelopes",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Existing exact Fraction construction is too expensive for the demonstrated use.",
  "next_action": "Identify reusable interval primitives and implement the smallest dimension-typed nonnegative envelope with an exact reference checker.",
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
    "rounding-envelope"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-ROUNDING-ENVELOPE-20260910",
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

# Low-cost outward-rounded pruning envelopes

## Mother question

Can the finite-map tail bound be evaluated conservatively at a cost low enough for use inside a solver?

## Frozen inputs and scope

Use declared finite Fourier operators and exact binary64 inputs. Keep 2D scalar-vorticity and 3D vector-velocity estimates separate. Establish each dimension-specific inequality before implementation; handle zero, subnormal, overflow and nonfinite inputs. Classical effective-model computation, not a native P000 fluid derivation. Keep signed/complex amplitudes, wavevector labels and declared observations distinct. No industrial acceleration, continuous-PDE certificate or novelty is assumed.

## Hard target and required outputs

Implement outward-rounded nonnegative reductions, retain exact-rational reference checks, and report enclosure validity, tightness and total construction cost over adversarial and held-out data. Explicitly exclude floating-kernel, time-discretization and unresolved-mode errors unless separately bounded.

## Research value to preserve

The saved 2D rational envelope took about 18.83 ms, more than its FFT reference; this is a concrete bottleneck, not a need for a renamed arbitrary-precision library.

## Success, kill, and return criteria

Accept only enclosures that dominate exact-rational evaluations in regression tests and follow a documented arithmetic proof. Reject unsafe arithmetic shortcuts. Return failing cases even if the result is no useful cost reduction.
