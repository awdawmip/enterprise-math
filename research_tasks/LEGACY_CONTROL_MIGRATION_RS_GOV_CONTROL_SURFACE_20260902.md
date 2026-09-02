<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GOV-CONTROL-SURFACE",
  "title": "Research control-surface reconciliation",
  "kind": "GOVERNANCE",
  "owner": "governance",
  "base_state": "HANDOFF_READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Keep scheduler task coverage, owner registry, common surface, stale ledgers, and live PR generations mutually consistent without turning governance into a research blocker.",
  "next_action": "SECOND REVIEW TASK: independently audit retirement candidates using fresh current main, exact branch head, source PR/tag/lineage and branch-owned assets. Do not rely on first-pass labels as proof. Priority: (1) completed operational refs and registered ABSORBED/PROVENANCE refs; (2) named RETIRE_REVIEW_PENDING branches; (3) after canonical promotion, PROMOTION_READY branches. For each branch return APPROVE_RETIRE, REJECT_RETIRE, HARVEST_REQUIRED, or KEEP_ACTIVE. Only APPROVE_RETIRE authorizes later lifecycle mutation, stale-PR closure, and ref deletion. Do not poll CI or chase moving main.",
  "dependencies": [],
  "source_refs": [
    "Issue #240",
    "branch_governance_overrides.json",
    "docs/RESEARCH_BRANCH_LEDGER.en.md"
  ],
  "evidence_status": "LEGACY_CONTROL_MIGRATED_HANDOFF_READY",
  "last_progress_ref": "main@c69998189e6c69d08dd82d2b1e1fe91875fda9d1 / docs/BRANCH_COMPRESSION_AUDIT_20260811.md / branch_retirement_review_20260811.json",
  "last_progress_at": "2026-08-10T17:24:45+00:00",
  "hard_block": null,
  "tags": [
    "governance",
    "ledger",
    "legacy-control-migration",
    "owner-registry",
    "scheduler",
    "v2-cutover"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GOV-CONTROL-SURFACE",
  "parent_objective_id": "LEGACY_CONTROL_CUTOVER_RS_GOV_CONTROL_SURFACE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GOV",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "migration_source": {
    "archive_branch": "archive/legacy-control-plane-pre-v2-20260902",
    "source_commit": "ce629e24e5af59128e25af87075c6622413684e0",
    "legacy_runtime_state": "HANDOFF_READY",
    "legacy_dispatch_state": "NEEDS_DISPATCH",
    "legacy_claim_id": null
  }
}
-->

# RS-GOV-CONTROL-SURFACE — V2 Task Preservation

Status: `PUBLISHED_REGISTERED / CONTROL_MIGRATION / HANDOFF_READY`

## Mother question

Can this exact task be represented on the immutable V2 task surface without changing its mathematical meaning or durable frontier?

## Frozen inputs and scope

The exact source definition, task metadata, frontier, references, owner boundary, and durable state are frozen in the accompanying metadata and migration record. They are not expanded or reinterpreted in this preservation body.

This preservation envelope adds no theorem, counterexample, novelty conclusion, priority elevation, truth status, or execution ownership.

## Hard target and required outputs

Preserve the verified durable frontier as a claimable V2 generation without changing mathematical scope or creating an owner event.

## Research value to preserve

Preserve the exact identity, lineage, accumulated evidence, durable frontier, and next executable action without replaying completed work.

## Success, kill, and return criteria

The V2 record preserves task identity, owner boundary, priority class, frontier, and next action while creating no synthetic execution ownership.

Return the immutable V2 publication record and its migration-manifest row after repository integrity checks pass. Mathematical execution and review remain separate actions.
