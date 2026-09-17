<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GV-CFD-HOST-INDEPENDENT-REVIEW-20260917",
  "title": "CFD Driver review of native-host correctness, independence and total cost",
  "kind": "GOVERNANCE",
  "owner": "governance",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The 2026-09-16 native-host checkpoint reports successful author tests but has no independently accepted solver-wide or general acceleration conclusion.",
  "next_action": "After frozen host implementation and independent-verification evidence are available, bind the exact Results and issue separate correctness, performance, scope and continuation dispositions.",
  "dependencies": [
    {
      "task_id": "RS-CFD-SPECTRAL-HYBRID-20260910",
      "required_artifact": "A frozen Result or current task-approved return bound to the 2026-09-16 native-host implementation and raw source/result bytes."
    },
    {
      "task_id": "RS-CFD-TRAJECTORY-VERIFY-20260910",
      "required_artifact": "A source-pinned independent verifier Result, including failures and total-cost accounting, produced by an executor distinct from the implementation author."
    }
  ],
  "source_refs": [
    "awdawmip/enterprise-math@20255478397fc475ec0584da0cf4311dd17bcc82:research_notes/CFD9R2K7/host_20260916/checkpoint_summary.json",
    "research_notes/CFD-B1F673/prior_chat_bundle_20260910/README.md",
    "research_artifacts/CFD_DRIVER_NEXT_STEPS_20260917/dossier.md",
    "research_artifacts/CFD_DRIVER_NEXT_STEPS_20260917/review_ledger.json",
    "research_tasks/RS-CFD-SPECTRAL-HYBRID-20260910.md",
    "research_tasks/RS-CFD-ROUNDING-ENVELOPE-20260910.md",
    "research_tasks/RS-CFD-CANCELLATION-GROUPS-20260910.md",
    "research_tasks/RS-CFD-TRAJECTORY-VERIFY-20260910.md",
    "research_tasks/RS-CFD-ROM-ITHACA-20260910.md",
    "research_tasks/RS-CFD-AMR-BASILISK-20260910.md",
    "research_tasks/RS-CFD-PRESSURE-GAMG-20260910.md",
    "research_tasks/RS-CFD-LBM-CODEGEN-20260910.md",
    "research_tasks/RS-CFD-TRAJECTORY-CERTIFICATION-20260910.md",
    "research_tasks/RS-CFD-PRIOR-ART-AUDIT-20260910.md"
  ],
  "evidence_status": "SOURCE_BACKED_NEXT_STEP_PUBLICATION_NOT_RESULT_ACCEPTANCE",
  "last_progress_ref": "awdawmip/enterprise-math@20255478397fc475ec0584da0cf4311dd17bcc82:research_notes/CFD9R2K7/host_20260916/checkpoint_summary.json",
  "last_progress_at": "2026-09-16T03:06:34.100093+00:00",
  "hard_block": {
    "missing_objects": [
      "A frozen Result or current task-approved return bound to the 2026-09-16 native-host implementation and raw source/result bytes.",
      "A source-pinned independent verifier Result, including failures and total-cost accounting, produced by an executor distinct from the implementation author."
    ],
    "owner": "GV-CFD-PERSISTENT-LINE-DRIVER-20260917",
    "unblock_condition": "Exact current prerequisite artifacts and a source-backed typed release for this publication; a taskbook or author PASS is insufficient."
  },
  "tags": [
    "CFD",
    "user-directed-20260917",
    "driver-handoff"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "GV-CFD-HOST-INDEPENDENT-REVIEW-20260917",
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
    "policy_digest": "sha256:98ee2981553fb4eeaf5bd8599513719ee2ac987fae875e9c5daf8a3e2156f3cf",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# CFD native-host independent Driver review

## Mother question

What exact correctness and cost claims survive independent examination of the actual native-host implementation, and which, if any, justify the separate closed-support research hypothesis?

## Frozen inputs and scope

Review the implementation pinned at 20255478397fc475ec0584da0cf4311dd17bcc82 and raw results identified by that checkpoint, not merely the older standalone probe. Require the current frozen implementation return and the independent RS-CFD-TRAJECTORY-VERIFY-20260910 evidence. The task is BLOCKED on those artifacts; publication does not satisfy them. An input may be a properly recorded negative or incomplete result, not only PASS.

The reported host scope is one MPI process, grids 16 and 32, 3/2 dealiasing with native Nyquist handling, 12 RK4 steps per trajectory, and default/upstream-Numba variants. Preserve the distinction between modified pressure and physical pressure, setup/calibration versus warmup/install/disk-I/O exclusions, and cross-runner versus within-run comparisons. Check the actual report rather than treating these summary fields as sufficient proof.

Execution requires an activated CFD-scoped Driver. A self-review by the implementation author is not the independent verification input. This is review of a classical effective model, not P000 foundation work.

## Hard target and required outputs

Produce a source-bound review packet that separately answers:

1. Are normalization, de-aliasing, conjugate pairing, new output modes, mean/Nyquist treatment, raw Vortex pressure input and single projection consistent with the pinned host?
2. Do the independent checks reproduce both velocity and pressure observations, time refinement and sparse-to-dense fallback on held-out and stress cases?
3. What full compute costs were measured, including detection, planning, calibration and final readout? Are all exclusions and both favorable and unfavorable cases retained?
4. Does any claimed gain extend beyond analytically special invariant flows? Random-case near-parity is not a general acceleration result.
5. Are the exact arithmetic support-invariance argument, floating implementation behavior and external CFD validity kept distinct?
6. Give an exact ACCEPT-at-declared-strength, REQUEST_REVISION, REJECT or INSUFFICIENT_EVIDENCE disposition, with current source/result pins, missing objects and one concrete follow-up.
7. Decide whether RS-CFD-EXACT-SUPPORT-SELECTOR-20260917 may proceed at its frozen scope after its separate antecedent requirement, or should remain blocked/parked. A positive host verdict alone does not prove novelty or authorize any stronger model.

## Research value to preserve

This gate separates useful verified engineering from optimistic interpretation of a microbenchmark. A scope-limited or negative verdict is a valid outcome and should make the next decision clearer.

## Success, kill, and return criteria

SUCCESS is a reproducible, independently supported and exactly bound Driver disposition, not necessarily a positive performance verdict. Reject general speedup language unsupported by matched-accuracy complete-cost comparisons. Request a specific revision rather than relaxing pressure, support or independence checks to obtain acceptance. Keep all unresolved continuous-PDE and physical-validation claims outside the verdict.
