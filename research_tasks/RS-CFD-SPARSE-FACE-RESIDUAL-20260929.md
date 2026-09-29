<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-SPARSE-FACE-RESIDUAL-20260929",
  "title": "守恒输运的稀疏格面残差与按需补偿",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Full face carry improves profile accuracy and exact conservation but is slower; a sparse/block/deferred version with charged bounds is untested.",
  "next_action": "Consume the pinned transport pilot; state one candidate residual compression law and its finite-horizon observer budget before implementation.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@3b79d9b7128c824826d86f68bcb55ba7ab7533a0:research_notes/cfd_pilots/20260928_8F8257D1/CHECKPOINT.md",
    "google-drive:file:10D_lLzJnFhh9ZS8dTnTt3fl8v6vw3Rr1;zip_sha256:e1f14eb7349a3bb4d4202c0d40e04dba6817f71df425ff21f0904ae11ee8784d",
    "awdawmip/enterprise-math@eeeda974bd72c5eab1efc81ccac6c276479bfbdf:research_tasks/RS-CFD-ROUNDING-ENVELOPE-20260910.md"
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
  "registry_key": "RS-CFD-SPARSE-FACE-RESIDUAL-20260929",
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
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 守恒输运：稀疏格面残差、按块补偿与成本边界

## Mother question

Can a conservative quantized transport update retain less face-residual state or process it less frequently than the full-carry pilot, while keeping a declared finite-horizon profile/observable error and reducing measured total resources? Determine when location, orientation and time association are indispensable, rather than assuming one global leftover is sufficient.

This is a new finite-volume compensation branch under the existing CFD acceleration objective. The earlier RS-CFD-ROUNDING-ENVELOPE-20260910 concerns outward-rounded Fourier-tail pruning, not this spatial integer flux-carry update. The direct-chat pilot is source provenance, not an invented completed formal parent task.

## Frozen inputs and scope

The directly requested 2026-09-28 pilot is preserved at:
`awdawmip/enterprise-math@3b79d9b7128c824826d86f68bcb55ba7ab7533a0:research_notes/cfd_pilots/20260928_8F8257D1/CHECKPOINT.md`.
Checkpoint SHA256: `d8f52593b355adc20c24e3838ed2a0cadc62b41aff548a1e76ebc4352855020e`.
The 35-file reproducibility ZIP is Drive file `10D_lLzJnFhh9ZS8dTnTt3fl8v6vw3Rr1`, SHA256 `e1f14eb7349a3bb4d4202c0d40e04dba6817f71df425ff21f0904ae11ee8784d`.
Its status remains FINITE_AUTHOR_EXPERIMENT / NOT_ADMITTED / EXTERNAL_ENGINEERING_MODEL. This task does not reinterpret those calculations as native dynamics or independent validation.

Begin with the pilot's periodic positive-density first-order upwind model, Courant number 1/8, common quantized initial data and shared oriented face flux. Preserve full-carry equations f_i=floor((q_i+rho_i)/8), rho_i'=(q_i+rho_i) mod 8, q_i'=q_i+f_(i-1)-f_i, with rho_i in {0,...,7}. Conservation is algebraic before overflow; explicitly establish integer width bounds, positivity and the meanings of delayed/aggregated records.

Retain 512 cells/4096 steps and 8192 cells/65536 steps (one transit), the short-time control and at least one predeclared longer horizon plus a sharp-profile stress case. Use the same discretization and initial state for FP64, FP32, no-carry integer, full-carry integer and candidate variants. Report quantization/roundoff errors relative to the same-discretization reference separately from continuum/discretization error. The pilot's first-order diffusion error is not cured by more accurate carry accounting.

Prototype sparse active faces, block summaries or threshold-triggered processing only after declaring what is lost and how its future observable effect is bounded. Label every outstanding record by sufficient face/block, orientation and time information. BRC-positive mass cannot stand in for signed oriented flux; any claimed BRC reuse must match a typed existing law rather than use the name as a correctness argument.

## Hard target and required outputs

1. Derive a finite-horizon conservation and propagated-error contract for at least one specified compression/deferred-update variant, or give an exact collision/counterexample showing that its proposed retained state is insufficient. State whether the bound controls the full field, regional flux/mean, or another fixed observer, and how horizon changes invalidate it.
2. Implement a fallback to a faithful update when the budget is exhausted. Freeze a budget grid and calibration/held-out profiles before measurements; do not tune to evaluation answers. Include a total-only residual control and full-carry reference. Test exact small states with rational/integer arithmetic, overflow boundaries, activation/deactivation, threshold crossings and block boundaries.
3. Measure the resource/error Pareto comparison over the declared horizons, using at least seven shuffled warmed timing repetitions for compiled kernels. Count residual map/index/flags, unpacking, scans, activation tests, bound evaluation, fallback, allocation and communication when used. Separate persistent state, working arrays and process peak memory; neither logical bit count nor kernel-only timing is whole-solver cost.
4. Save raw outputs, per-run timing and error/conservation/positivity logs, proof or counterexample, implementation/checker and restart instructions. Audit prior art before any novelty claim; extend existing compensation/error-feedback methods where adequate rather than replacing them by terminology.

## Research value to preserve

The full-transit pilot had exact integer mass conservation for both carry and no-carry, but at coarse quantum the profile errors were about 0.281% and 17.29%. At 8192 cells, full carry reached relative L2 error 8.71734603e-6 versus FP32 1.30295792e-3, yet took 140.168 ms versus FP64 88.170 ms and FP32 43.066 ms. This task must solve the state/processing overhead or identify a useful accuracy niche; it must not recast that slower result as an acceleration. Full carry used 5 persistent bytes/cell, not 5 bytes of total process memory.

## Success, kill, and return criteria

A constructive result must exactly conserve integer mass within proved width limits, respect declared positivity and every held-out finite-horizon error budget, and improve at least one total resource at matched accuracy relative to the appropriate full-carry/conventional baseline while reporting all tradeoffs. Lower memory with higher runtime may be a useful bounded result, not a speedup. Better roundoff with unchanged dominant discretization error is not a proportional gain in physical accuracy.

Reject a proposed compression if identical retained state leads to distinguishable allowed future observations beyond budget, if bound cost erases its claimed economy, or if it hides a dense scan under a sparse label. Exact negative results and a measured non-benefit region satisfy the research return. Do not silently raise budgets, change the target output or discard failed variants after seeing results. No turbulent-closure or general fluid-physics claim follows from this scalar model.
