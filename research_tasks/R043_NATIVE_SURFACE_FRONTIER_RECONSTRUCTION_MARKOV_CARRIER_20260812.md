<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043-NATIVE-SURFACE-FRONTIER-RECONSTRUCTION-MARKOV-CARRIER",
  "title": "R043 Native Surface Frontier Reconstruction and Minimal Markov Carrier",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "DONE",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "HISTORICAL TASK COMPLETED: stationary native slot-cut carrier K_partial proved; global forgetful-map injectivity pi:K_partial->G0 left as successor question.",
  "next_action": "DO NOT REDISPATCH THIS TASK. Continue only through the separately reviewed R043-C1 slot-completion / G0-injectivity successor task.",
  "dependencies": [],
  "source_refs": [
    "research_artifacts/R043_native_surface_frontier/CHECKPOINT.md",
    "research_artifacts/R043_native_surface_frontier/RESULTS.json",
    "research_artifacts/R043_native_surface_frontier/frontier_reconstruction.py",
    "historical execution record: #532 / EM-R043-8C2F71"
  ],
  "evidence_status": "DONE_RETURNED_ON_532 / STATIONARY_SLOT_CUT_POSITIVE / G0_GLOBAL_INJECTIVITY_OPEN",
  "last_progress_ref": "Driver correction 2026-08-24 after recovery of historical execution #532",
  "last_progress_at": "2026-08-24T13:02:00+08:00",
  "hard_block": null,
  "tags": ["R043","native-surface","historical-task","done","slot-cut","G0"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R043",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-R041-NATIVE-SURFACE-HORIZON-QUOTIENT-CALCULUS",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "HISTORICAL_DONE_NOT_DISPATCHABLE",
    "temporary_overrides": []
  }
}
-->

# R043 — Native Surface Frontier Reconstruction and Minimal Markov Carrier

Status: `DONE / RETURNED / HISTORICAL / DO NOT REDISPATCH`

This task was executed before the 2026-08-24 orphan-maintenance sweep, outside the Issue #240 runtime event channel. Its completed research checkpoint is frozen in `research_artifacts/R043_native_surface_frontier/` and historical execution record #532 under Researcher-ID `EM-R043-8C2F71`.

The original task text remains recoverable in Git history at the pre-correction taskbook generations. This current file is intentionally a dispatch-safety archival stub so the historical task cannot be mistaken for an unclaimed READY item.

## Retained result boundary

R043 established a fixed-form stationary native slot-cut carrier `K_partial`: current coherently embedded frontier plus the inward occupied contact slots of each frontier cell. For the declared addition-only surface dynamics, this carrier updates exactly without storing explicit `L1`, deeper exterior layers, or deep-interior provenance.

The checkpoint also found no weighted-current-frontier `G0` collision through the complete frozen `N<=8` FCC/HCP atlases and no action-rooted closure split through parent `N<=7`, but did **not** prove global `G0` sufficiency.

The exact unresolved residue is the forgetful-map question

`pi: K_partial -> G0`.

The next permitted research object is therefore a separate continuation that attacks native slot-completion / embedding rigidity and global injectivity of `pi`; this historical R043 task must not be re-run.
