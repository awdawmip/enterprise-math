<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P017-GLOBAL-CAPACITY",
  "title": "P017 signed-core global capacity pressure test",
  "kind": "RESEARCH",
  "owner": "program/p017-legendre",
  "base_state": "SUPERSEDED",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Turn signed full-core collision/discriminant geometry and shared P018 channel constraints into a quantitative subterminal or global capacity statement, or close that route with a rigorous negative boundary.",
  "next_action": "Do not redispatch the 2026-08-09 broad capacity task. If P017/P018 resumes, start from the latest frozen P017×P018 weighted-boundary/Walsh-L2 resume frontier and require a current successor gate.",
  "dependencies": [
    {
      "target": "canonical P018 quotient/root-channel results",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "Research Relay #82 current P017/P018 entries",
      "action": "INFORM",
      "satisfied": true
    }
  ],
  "source_refs": [
    "PR #191",
    "PR #170",
    "program/p017-legendre",
    "Research Relay #82"
  ],
  "evidence_status": "LEGACY_CONTROL_MIGRATED_SUPERSEDED",
  "last_progress_ref": "PR #191",
  "last_progress_at": "2026-08-24T02:06:18+00:00",
  "hard_block": null,
  "tags": [
    "Legendre",
    "P017",
    "capacity",
    "collision",
    "global-coupling",
    "legacy-control-migration",
    "v2-cutover"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P017-GLOBAL-CAPACITY",
  "parent_objective_id": "LEGACY_CONTROL_CUTOVER_RS_P017_GLOBAL_CAPACITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P017",
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

# RS-P017-GLOBAL-CAPACITY — V2 Task Preservation

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
