<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-E001-IMPULSE-V2",
  "title": "E001 emergent impulse/rebound continuation",
  "kind": "RESEARCH",
  "owner": "engineering/e001-material-impulse-v2",
  "base_state": "HANDOFF_READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Continue finite impulse/momentum material dynamics after the canonical wall and pair slices without hard-coded velocity reversal.",
  "next_action": "Driver: verify the frozen E001 current-hold passivity-budget return and standalone checker; if accepted, consume the exact distinction between static material passivity, schedule-specific sampling passivity, and schedule-independent passivity when deciding the next owner architecture (schedule restriction vs endpoint/chord-aware work vs explicit correction state). Do not re-own contact-network quotient mathematics.",
  "dependencies": [
    {
      "target": "canonical pair impulse result",
      "action": "CONSUME",
      "satisfied": true
    }
  ],
  "source_refs": [
    "PR #190",
    "engineering/e001-material-impulse-v2"
  ],
  "evidence_status": "LEGACY_CONTROL_MIGRATED_HANDOFF_READY",
  "last_progress_ref": "PR #974 / 220baa23270edd203beb6ab0882f22fdb7571180",
  "last_progress_at": "2026-08-30T13:44:46+00:00",
  "hard_block": null,
  "tags": [
    "E001",
    "impulse",
    "legacy-control-migration",
    "momentum",
    "precision",
    "rebound",
    "v2-cutover"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-E001-IMPULSE-V2",
  "parent_objective_id": "LEGACY_CONTROL_CUTOVER_RS_E001_IMPULSE_V2",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "E001",
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

# RS-E001-IMPULSE-V2 — V2 Task Preservation

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
