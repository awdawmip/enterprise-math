<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GV-CFD-PERSISTENT-LINE-DRIVER-20260917",
  "title": "CFD persistent line Driver: recovery, dispatch, review and handoff",
  "kind": "GOVERNANCE",
  "owner": "governance",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Ten CFD research publications exist. Actual serial host integration has an author-tested checkpoint dated 2026-09-16, but independent acceptance and a durable line-level review/decision loop are not established by that checkpoint.",
  "next_action": "Confirm active delegated CFD Driver scope, reconcile current task generations and execution owners, then route the 2026-09-16 host packet to the existing independent verification task and maintain the attached dossier.",
  "dependencies": [],
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
  "hard_block": null,
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
  "registry_key": "GV-CFD-PERSISTENT-LINE-DRIVER-20260917",
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

# CFD persistent line Driver

## Mother question

How should an explicitly activated CFD line Driver carry the existing ten-task program from the verified host implementation checkpoint to independent review and evidence-based next-step decisions without duplicating completed work or losing the negative performance evidence?

## Frozen inputs and scope

The parent objective is OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910. This is a governance task for an activated, appropriately delegated RESEARCH_DRIVER; its publication is not that activation. The source packet is the 2026-09-16 host checkpoint pinned in the metadata and its linked raw results. The earlier e40e530 checkpoint is historical input, not the highest implementation frontier.

Preserve the classical effective-model scope: serial spectralDNS/shenfun/FFTW, frozen upstream revision, finite grids, no support pruning, native pressure/diffusion and RK4. Author tests are not independent acceptance. P000 premises are unchanged and no native fluid derivation is claimed. A different reviewer must evaluate the implementation; role relabeling of its author does not establish independence.

The existing research tasks remain the work owners. In particular, RS-CFD-TRAJECTORY-VERIFY-20260910 owns independent replication and RS-CFD-PRIOR-ART-AUDIT-20260910 owns antecedent classification. This task coordinates them rather than duplicating their technical outputs. Inspect any newer immutable Result and current owner before selecting work.

## Hard target and required outputs

1. Verify the current primary-task owner, pending Results and published generation from source; record exactly which units are complete, unfinished, conflicting or unknown. Missing historical transport evidence is not a new execution authorization.
2. Preserve and verify the host evidence packet, then arrange independent review through RS-CFD-TRAJECTORY-VERIFY-20260910; require exact source/result pins and separate implementation author, independent verifier and decision maker.
3. Maintain research_artifacts/CFD_DRIVER_NEXT_STEPS_20260917/dossier.md and research_artifacts/CFD_DRIVER_NEXT_STEPS_20260917/review_ledger.json with current state, completed work, remaining work, exact artifact locations, active scope and replacement conditions.
4. Carry GV-CFD-HOST-INDEPENDENT-REVIEW-20260917 to a terminal scope-limited verdict after its inputs are actually available. Capture a rejected or insufficient-evidence verdict as faithfully as a positive result.
5. Keep RS-CFD-EXACT-SUPPORT-SELECTOR-20260917 blocked until its verification and antecedent conditions are satisfied. Preserve rounding, cancellation and finite-trajectory certification as separate obligations.
6. Route the ROM, AMR, pressure and LBM feasibility work using the existing tasks, public baselines and demonstrable subproblems. Record the allocation basis rather than prescribing an arbitrary parallel-worker count.
7. Return a machine-readable decision ledger with exact Result/review/follow-up identifiers once they exist; never fill them with invented identifiers merely to complete the table.

## Research value to preserve

A replacement Driver must be able to continue from this dossier without access to this conversation. Preserve full-cost negative evidence on general random fields, the limited positive invariant-subspace examples, pressure-interface correctness, and all unresolved mathematical/engineering bridges.

## Success, kill, and return criteria

SUCCESS for the first bounded handoff is a reconciled evidence map, an explicit independent-review route, and one source-backed next action per existing workstream with ownership and input readiness recorded. Persistent responsibility continues through a recorded replacement or a separately justified parent-level disposition.

Do not mark the line complete because tasks were published, a source file was written, or one test suite passed. If an owner conflict or missing activation prevents execution, report the exact missing authority and preserve all independent, publication-safe work. Do not restart the completed native-host integration from scratch.
