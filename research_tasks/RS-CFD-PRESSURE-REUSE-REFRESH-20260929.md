<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-PRESSURE-REUSE-REFRESH-20260929",
  "title": "缓变压力方程的计算复用、热启动与误差触发刷新",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Fixed-operator reuse is measured; the validity and total cost of reuse under coefficient drift are untested.",
  "next_action": "Consume the pinned pilot and existing pressure task; freeze matched operator-drift/held-out sequences and a true-residual/QoI acceptance test.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@3b79d9b7128c824826d86f68bcb55ba7ab7533a0:research_notes/cfd_pilots/20260928_8F8257D1/CHECKPOINT.md",
    "google-drive:file:10D_lLzJnFhh9ZS8dTnTt3fl8v6vw3Rr1;zip_sha256:e1f14eb7349a3bb4d4202c0d40e04dba6817f71df425ff21f0904ae11ee8784d",
    "awdawmip/enterprise-math@eeeda974bd72c5eab1efc81ccac6c276479bfbdf:research_tasks/RS-CFD-PRESSURE-GAMG-20260910.md"
  ],
  "evidence_status": "FINITE_PILOT_NOT_ADMITTED;NEW_TASK_UNEXECUTED",
  "last_progress_ref": "awdawmip/enterprise-math@3b79d9b7128c824826d86f68bcb55ba7ab7533a0:research_notes/cfd_pilots/20260928_8F8257D1/CHECKPOINT.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "CFD",
    "direct-user-20260929",
    "residual-faithful-engineering"
  ],
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-PRESSURE-REUSE-REFRESH-20260929",
  "parent_objective_id": "OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "CFD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-CFD-PRESSURE-GAMG-20260910",
  "successor_gate": {
    "new_information_gap": "Operator drift may invalidate reused factors, preconditioners and adjoints; no costed refresh rule has been demonstrated.",
    "why_parent_result_does_not_close_it": "The parent publication asks about repeated-geometry condensation; no parent completion is assumed. The new direct-chat pilot measures fixed A only.",
    "discriminating_outcomes": [
      "Equal-accuracy net benefit under bounded drift with charged refresh cost",
      "No benefit because refresh/certification dominates",
      "Accuracy failure or exact invalidity witness for a reuse shortcut"
    ],
    "kill_condition": "Accepted inaccurate solves or consistent total-cost non-benefit terminate that variant, with evidence retained.",
    "alternative_route_or_free_exploration_considered": "Fresh tuned solves, fixed refresh, warm starts and GAMG/interface work remain alternatives; none requires a new geometry or native dynamics premise.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Isolates drift/refresh as a bounded independently assignable gap without editing the existing condensation task or assuming its owner/result."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 缓变压力方程：计算复用、热启动与误差触发刷新

## Mother question

For a sequence A_j p_j=b_j with fixed mesh and boundary conditions but slowly or abruptly changing positive coefficients, when can old factorization/preconditioner/initial-solution information be reused at lower total cost while retaining declared pressure-output accuracy? Construct an error-triggered refresh rule, or locate its measurable failure boundary.

This is a bounded continuation of RS-CFD-PRESSURE-GAMG-20260910, not a replacement of its owner or a claim that its condensation/GAMG target is complete. The older task studies a reusable interface for repeated geometry; this task isolates operator drift and refresh economics using a newly available finite pilot.

## Frozen inputs and scope

The directly requested 2026-09-28 pilot is preserved at:
`awdawmip/enterprise-math@3b79d9b7128c824826d86f68bcb55ba7ab7533a0:research_notes/cfd_pilots/20260928_8F8257D1/CHECKPOINT.md`.
Checkpoint SHA256: `d8f52593b355adc20c24e3838ed2a0cadc62b41aff548a1e76ebc4352855020e`.
The 35-file reproducibility ZIP is Drive file `10D_lLzJnFhh9ZS8dTnTt3fl8v6vw3Rr1`, SHA256 `e1f14eb7349a3bb4d4202c0d40e04dba6817f71df425ff21f0904ae11ee8784d`.
Its status remains FINITE_AUTHOR_EXPERIMENT / NOT_ADMITTED / EXTERNAL_ENGINEERING_MODEL. This task does not reinterpret those calculations as native dynamics or independent validation.

Use the pilot's two-dimensional SPD -div(k grad p) discretization with zero Dirichlet boundary and the difference of two regional pressure averages as the initial quantity of interest. Start with 48x48 and 96x96; add one larger predeclared size if resources permit. Freeze one fixed-operator control, smooth coefficient-drift sequences, and an abrupt local-change stress sequence before timing. Keep positivity, coefficient bounds, initial conditions and sequence lengths explicit. Preserve the fixed-matrix sparse-LU gain and the failed calibrated rtol=3e-4 (42/48) observation; neither establishes a safe reuse rule for a changed operator.

Same-discretization acceptance is |J(p)-J(p_hat)|<=1e-4 and ||b-A p_hat||_2/||b||_2<=1e-3 for every held-out solve; define a nonzero absolute scale for zero RHS before running. Exact manufactured/reference solutions belong only to evaluation, never the online trigger. Distinguish the true algebraic residual from an estimated/preconditioned residual. These tests are not full-flow divergence, time-integration or continuum-error certificates.

Read the existing pressure task and relevant reusable solver interfaces rather than renaming their methods. Classical signed linear algebra is the declared engineering carrier; a positive-weight total alone supplies no cancellation, SPD or inverse bound. Use project residual/observer typing only with its actual interface; no native arithmetic execution is asserted here.

## Hard target and required outputs

1. A written reuse contract identifying retained state, validity horizon, operator change, online error indicator, rebuild decision and fallback. An old factorization may be an approximate inverse/preconditioner for the new system, never silently treated as the exact new solve. Prove any claimed bound with stated coercivity assumptions; distinguish exact-arithmetic laws, outward-rounded certificates and heuristic floating estimates.
2. An implementation and frozen benchmark comparing rebuild-every-solve, fixed-interval refresh, the error-triggered rule, and warm starts. Retain a tuned conventional preconditioned solver and the fixed-operator reuse control; compare against the existing GAMG route where a compatible implementation is actually available, otherwise delimit that missing comparison. Record all cases rather than only beneficial drifts.
3. Separate calibration from new held-out sequences, predeclare parameters and practical benefit criterion, then run at least five shuffled timing repetitions. Charge setup, factorization/preconditioner construction, adjoint/error checks, updates, data conversion, fallbacks and rejected attempts. Report amortized and one-shot cost, full peak-memory measurement where available, and unresolved memory coverage. Compilation and common reference-generation costs must be separate, not silently omitted or charged to only one method.
4. Per-solve accuracy/trigger/rebuild logs, raw timings, independent checker code or independently implemented small-case arithmetic, source versions and a restartable result packet. Preserve all pilot artifacts; rerun only the integrity checks and matched controls actually needed by the new experiment.

## Research value to preserve

The pilot's fixed 96x96 variable-coefficient 48-load LU reuse measured 0.057502 s versus 0.404582 s for its conservative PCG control, with 7272968 factor bytes; it did not test operator drift. Goal stopping measured 0.374502 s and is a reliability candidate, not a demonstrated major accelerator. The new information sought is the costed validity boundary of reuse, not another presentation of fixed-matrix amortization.

## Success, kill, and return criteria

Return either a reproducible equal-accuracy net benefit on the preregistered drift family, or a cost/accuracy failure map showing why reuse is not advantageous. A positive result must satisfy both tolerances on every held-out solve and include certification/refresh/fallback cost. A speed advantage against a deliberately over-solved reference alone is insufficient.

Reject any method that returns an inaccurate accepted solve, conceals a rebuild, depends on an exact answer online, or transfers fixed-operator correctness to a changed operator without a bound. Stop expanding a tested variant when total overhead consistently removes its advantage; preserve the negative evidence. A local mathematical bound or finite experiment does not establish industrial/general asymptotic acceleration. Finish with the smallest specifically evidenced next gap, not an automatic unbounded sequel.
