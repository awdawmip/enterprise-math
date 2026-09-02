<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P025-WITNESS-PRECISION",
  "title": "P025 bounded-witness precision mother-theorem test",
  "kind": "RESEARCH",
  "owner": "program/p025-abc-support-collapse",
  "base_state": "SUPERSEDED",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine whether coarse state plus a relation-conditioned bounded admissible witness family gives a precision theorem genuinely distinct from exact minimal repair and ordinary A4 support.",
  "next_action": "Do not redispatch the 2026-08-09 bounded-witness mother-theorem task. P025 subsequently advanced through witness-radius, support, future-relative precision, scheduler/action-support and Stage-160 Pareto results. Any continuation must begin from the latest Stage-160 successor gate.",
  "dependencies": [
    {
      "target": "A2/P023 exact descent/minimal repair",
      "action": "TEST",
      "satisfied": true
    },
    {
      "target": "A4 admissible support",
      "action": "TEST",
      "satisfied": true
    }
  ],
  "source_refs": [
    "PR #216",
    "Issue #211",
    "Research Relay #82"
  ],
  "evidence_status": "LEGACY_CONTROL_MIGRATED_SUPERSEDED",
  "last_progress_ref": "PR #216",
  "last_progress_at": "2026-08-24T02:06:51+00:00",
  "hard_block": null,
  "tags": [
    "A2",
    "A4",
    "P025",
    "abc",
    "legacy-control-migration",
    "precision",
    "v2-cutover",
    "witness"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P025-WITNESS-PRECISION",
  "parent_objective_id": "LEGACY_CONTROL_CUTOVER_RS_P025_WITNESS_PRECISION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P025",
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
    "legacy_runtime_state": "SUPERSEDED",
    "legacy_dispatch_state": "COMPLETE",
    "legacy_claim_id": null
  }
}
-->

# RS-P025-WITNESS-PRECISION — V2 Task Preservation

Status: `PUBLISHED_REGISTERED / CONTROL_MIGRATION / SUPERSEDED`

## Mother question

Can this exact task be represented on the immutable V2 task surface without changing its mathematical meaning or durable frontier?

## Frozen inputs and scope

The exact source definition, task metadata, frontier, references, owner boundary, and durable state are frozen in the accompanying metadata and migration record. They are not expanded or reinterpreted in this preservation body.

This preservation envelope adds no theorem, counterexample, novelty conclusion, priority elevation, truth status, or execution ownership.

## Hard target and required outputs

Preserve the verified terminal outcome as immutable nonclaimable history. This generation cannot authorize a new execution.

## Research value to preserve

Preserve the exact identity, lineage, accumulated evidence, durable frontier, and next executable action without replaying completed work.

## Success, kill, and return criteria

The V2 record preserves task identity and terminal state, remains nonclaimable, and creates no owner or execution event.

Return the immutable V2 publication record and its migration-manifest row after repository integrity checks pass. Mathematical execution and review remain separate actions.
