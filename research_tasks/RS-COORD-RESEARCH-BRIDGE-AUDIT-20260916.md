<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-COORD-RESEARCH-BRIDGE-AUDIT-20260916",
  "title": "既有研究的坐标依赖审计：只修受影响桥接引理，不重开母题",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Task-level triage is available, but theorem-level source-to-address dependency closure and several old return/review bindings remain unresolved.",
  "next_action": "Consume the current task-state inventory and exact old returns; build a statement-to-input-to-observer dependency ledger before proposing any reproof.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:coordinate_address_contract.json",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:COORDINATE_ADDRESS_CONVENTION.zh-CN.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:EnterpriseMath/CellAddress/ThreeRegionSlice.lean",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/RS_X6_LEGACY_PLANE_RECONCILIATION_20260905.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/P000_FCC_NATIVE_COORDINATE_BRIDGE_ROTATION_ATLAS_SYNTHESIZED_V3_20260829.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_CERTIFICATE_20260909.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/HODGE_H0O_CONTRACT_ALIGNMENT_REVISION_20260908.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/RH_BRC_COUNT_CENTERED_CARRY_CLOSURE_20260909.md"
  ],
  "evidence_status": "SCOPED_SLICE_PROOF_COMPLETE_DELTA_UNFINISHED",
  "last_progress_ref": "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
  "hard_block": null,
  "tags": [
    "coordinate-address",
    "nonnegative",
    "representation-only"
  ],
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-COORD-RESEARCH-BRIDGE-AUDIT-20260916",
  "parent_objective_id": "OBJ-CELL-NONNEGATIVE-COORDINATE-MIGRATION-20260916",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "COORD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "related_existing_tasks": [
    "RS-X6-LEGACY-PLANE-RECONCILIATION",
    "RS-P000-FCC-NATIVE-COORDINATE-BRIDGE-ROTATION-ATLAS",
    "RS-RB-CM24-SOURCE-EXPOSED-EXACT-MAP-CERTIFICATE",
    "RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3",
    "RH-BRC-CARRY-CLOSURE-20260909"
  ],
  "lineage_rationale": "New address-representation delta under the explicit user request; does not revise or restart the related tasks with their different frozen mathematical targets.",
  "policy_review": {
    "temporary_overrides": [],
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:98ee2981553fb4eeaf5bd8599513719ee2ac987fae875e9c5daf8a3e2156f3cf",
    "review_state": "PASS"
  }
}
-->

# 既有研究的坐标依赖审计：只修受影响桥接引理，不重开母题

## Mother question

Which specific old bridge lemmas or executable observations actually depend on the changed final Cell-address convention?

## Frozen inputs and scope

The exact source snapshot is d2984d1a0c5c8221ee103084dd3da68dd039dfaa. The verified three-region slice proof is consumed unchanged (SHA256 2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02). Only final addresses change; native cell population, six axis labels, signed internal displacements, existing adjacency, decoded metric and ordered path data are retained.

This is a source-exposed post-20260913 representation audit, not a repetition of the frozen 20260905 legacy-plane task. RS-X6-LEGACY-PLANE-RECONCILIATION has a durable return but lacks valid terminal review binding; recover its evidence rather than redo its mathematics. The FCC atlas return awaits review. A3 shell alignment was rejected and already has its own revision. Accepted RB exact-map and shell-allocation results retain only their accepted strength. Preserve every blind-source restriction; this exposed auditor is not a new blind replicator.

## Hard target and required outputs

For each exact statement touched in X6/FCC,A3,Viète,BRC,Hodge,RB/Ramanujan and RH native bridges, return source pin,actual coordinate type,dependent operator,the unchanged transport lemma or counterexample,and disposition KEEP/ADAPT/RECOMPUTE/REPROVE/REVIEW_ONLY/UNKNOWN. Keep pure scalar,algebraic-cycle and analytic estimates unchanged when no Cell-address dependency exists. Do not infer RH or Hodge proof from recoding. Recover missing legacy return evidence into a review-ready packet without inventing acceptance. Record overlapping RH-road task pairs as owner decisions, not automatic cancellation. Outputs: research_artifacts/COORD_RESEARCH_BRIDGE_AUDIT_20260916/.

## Research value to preserve

This supplies precise research rework rather than a global restart, preserves accepted results and prevents closed or rejected work from being misreported as new success.

## Success, kill, and return criteria

Success is a source-bound impact ledger and minimal exact repairs/counterexamples for impacted bridges. Insufficient source yields UNKNOWN, not a claim that a theorem is invalid. Review-only gaps produce evidence handoff, not a new mathematical result or automatic status change.
