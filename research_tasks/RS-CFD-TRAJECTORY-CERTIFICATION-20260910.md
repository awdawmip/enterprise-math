<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-TRAJECTORY-CERTIFICATION-20260910",
  "title": "CFD finite-trajectory error certification from local defects",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The CFD line has finite-map defect bounds and floating trajectory agreement, but no rigorous finite-time propagation certificate separating approximation, time-discretization, rounding, and truncation contributions.",
  "next_action": "Freeze one finite-dimensional three-dimensional Galerkin system, time horizon, norm and observable set, then derive the first explicit local-defect-to-trajectory stability inequality from the verified finite-map interfaces.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@13a7cdc9dfac3b7f6d7120f7b020733d7c91f964:research_notes/CFD9R2K7/cfd_public_algorithm_probe_20260910.json",
    "awdawmip/enterprise-math@e40e5303234c5e8bd725528aad9bff9edf0c059d:research_notes/CFD-B1F673/main/summary.json",
    "research_notes/CFD-B1F673/prior_3d/probe.py",
    "research_notes/CFD-B1F673/prior_chat_bundle_20260910/README.md",
    "research_notes/CFD-B1F673/prior_chat_bundle_20260910/prior_local_main_results.json",
    "research_notes/CFD-B1F673/prior_chat_bundle_20260910/prior_taskset_manifest.json",
    "research_notes/CFD-B1F673/prior_chat_bundle_20260910/RAW_VORTEX_INTERFACE.md",
    "research_tasks/RS-CFD-SPECTRAL-HYBRID-20260910.md",
    "research_tasks/RS-CFD-ROUNDING-ENVELOPE-20260910.md",
    "research_tasks/RS-CFD-CANCELLATION-GROUPS-20260910.md",
    "research_tasks/RS-CFD-TRAJECTORY-VERIFY-20260910.md"
  ],
  "evidence_status": "EXPLORATORY_INPUTS_NOT_INDEPENDENTLY_REVIEWED",
  "last_progress_ref": "awdawmip/enterprise-math@e40e5303234c5e8bd725528aad9bff9edf0c059d:research_notes/CFD-B1F673/main/summary.json",
  "last_progress_at": "2026-09-10T09:00:00+00:00",
  "hard_block": null,
  "tags": [
    "CFD",
    "user-directed-20260910",
    "trajectory-certification",
    "error-propagation"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-TRAJECTORY-CERTIFICATION-20260910",
  "parent_objective_id": "OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "CFD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-CFD-SPECTRAL-HYBRID-20260910",
  "successor_gate": {
    "new_information_gap": "No rigorous map currently converts local approximation, arithmetic and time-stepping defects into a finite-time trajectory or declared-output error budget.",
    "why_parent_result_does_not_close_it": "The parent hybrid task measures and cross-checks the same finite dynamics without pruning; its current source explicitly does not provide a continuous-PDE certificate or a rigorous multi-step defect propagation theorem.",
    "discriminating_outcomes": [
      "A finite-dimensional Galerkin a-posteriori trajectory bound with explicit computable constants and a checker.",
      "A scoped obstruction showing the available stability constants or certificate cost are too loose for useful acceptance at the frozen horizon."
    ],
    "kill_condition": "Kill any useful-certification claim if the required error accounts cannot be separated, the needed stability constants cannot be computed at the frozen scope, or the bound is provably too loose to distinguish acceptance from fallback.",
    "alternative_route_or_free_exploration_considered": "The existing independent trajectory-verification task tests empirical reproducibility and benchmark behavior; it does not replace mathematical propagation of certified local defects.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Keeping certification separate prevents performance tuning from weakening proof obligations and lets the certificate line be reviewed or closed independently even if the acceleration line succeeds or fails."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# CFD finite-trajectory error certification from local defects

Status: `READY / PUBLISHED_REGISTERED / FINITE-DYNAMICS CERTIFICATION`

## Mother question

For one frozen finite-dimensional three-dimensional incompressible Fourier-Galerkin dynamics and a declared finite time horizon, can computable local defects be propagated into a rigorous bound on the full trajectory or selected observables at a cost low enough to guide accept, refine, or fallback decisions?

## Frozen inputs and scope

Work first with the finite Galerkin ordinary differential system actually evaluated by the CFD spectral line. This is a classical effective-model calculation and not a derivation of native P000 fluid dynamics. Preserve integer wavevector addresses, vector components, complex amplitudes, conjugate pairing, projection information, time ordering, and every distinction required by the declared observer.

Keep four error accounts distinct: approximation or support truncation, floating or interval arithmetic, time discretization, and unresolved continuous-PDE/model error. The first three may be bounded in this task. The fourth remains outside the conclusion unless an additional theorem is supplied. Positive-mass BRC results do not by themselves certify signed or phase cancellation; any compression must preserve the signed or complex carrier needed by the future operations.

Use the existing hybrid, rounding, cancellation, and independent verification sources as inputs without treating their exploratory numerical agreement as a theorem.

## Hard target and required outputs

Produce one reproducible finite-dynamics certificate package containing:

1. an explicit stability or defect-propagation inequality for the frozen Galerkin system and norm;
2. computable constants or interval enclosures for the chosen horizon, with the dependence on viscosity, retained modes and solution-size bounds stated;
3. a time-discretization account that can be combined with the local nonlinear-evaluation defect without double counting;
4. a rounding or outward-enclosure account adequate for the checker;
5. an accept/refine/fallback rule whose mathematical guarantee is exactly the proved finite-dynamics bound;
6. at least one independently checkable successful case and one stress or failure case showing when the certificate becomes too loose.

Report separately the mathematical bound, its observed numerical slack, and the cost of constructing and checking it.

## Research value to preserve

A successful certificate would make sparse or approximate CFD computation auditable rather than heuristic. A negative result is also valuable if it identifies the stability constant, norm choice, cancellation loss, or certificate overhead that prevents useful finite-time guarantees. This separation is important because empirical trajectory agreement and fast single-step kernels do not establish a reusable error budget.

## Success, kill, and return criteria

SUCCESS requires an explicit finite-time error statement, a reproducible checker, exact scope boundaries, and complete accounting of certificate cost.

KILL any claim that local residual smallness alone controls the trajectory when the required stability hypothesis has not been established. Do not convert a finite-dimensional certificate into a continuous Navier-Stokes regularity, discretization-convergence, physical-model, or industrial-validity statement.

If a useful bound cannot be obtained at the frozen horizon, return the sharpest verified obstruction and the smallest next mathematical quantity whose improvement could change that conclusion.
