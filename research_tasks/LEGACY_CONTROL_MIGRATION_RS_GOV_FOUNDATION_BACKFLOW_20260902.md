<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GOV-FOUNDATION-BACKFLOW",
  "title": "Foundation backflow verification and canonicalization",
  "kind": "GOVERNANCE",
  "owner": "governance",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Close the research-to-Foundation loop for returned FQs and mature Feedback Packets: independently verify scope/evidence, build minimal latest-main integration for accepted results, and complete post-merge propagation without becoming the theorem research owner.",
  "next_action": "Treat FQ-20260809-004 as a closed regression example. For the next ANSWERED FQ or mature Foundation Feedback Packet, independently verify the returned evidence and weakest scope, accept or reject the minimal interface, integrate accepted governance/Foundation surfaces through current-main L4, and only mark CANONICALIZED after merge and propagation.",
  "dependencies": [
    {
      "target": "canonical FQ-20260809-004 result / PR #268",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "canonical shared-surface promotion gate / PR #282",
      "action": "CONSUME",
      "satisfied": true
    }
  ],
  "source_refs": [
    "Issue #164",
    "Issue #82",
    "foundation_backflow.json",
    "docs/FOUNDATION_BACKFLOW_LOOP.en.md",
    "PR #282"
  ],
  "evidence_status": "LEGACY_CONTROL_MIGRATED_READY",
  "last_progress_ref": "FQ-20260809-004 canonical / PR #282",
  "last_progress_at": "2026-08-09T23:28:00+08:00",
  "hard_block": null,
  "tags": [
    "backflow",
    "canonicalization",
    "foundation",
    "governance",
    "legacy-control-migration",
    "v2-cutover",
    "verification"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GOV-FOUNDATION-BACKFLOW",
  "parent_objective_id": "LEGACY_CONTROL_CUTOVER_RS_GOV_FOUNDATION_BACKFLOW",
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
    "legacy_runtime_state": "READY",
    "legacy_dispatch_state": "NEEDS_DISPATCH",
    "legacy_claim_id": null
  }
}
-->

# RS-GOV-FOUNDATION-BACKFLOW — V2 Task Preservation

Status: `PUBLISHED_REGISTERED / CONTROL_MIGRATION / READY`

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
