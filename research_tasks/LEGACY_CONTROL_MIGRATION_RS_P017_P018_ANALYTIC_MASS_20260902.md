<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P017-P018-ANALYTIC-MASS",
  "title": "P017/P018 analytic core-mass control",
  "kind": "RESEARCH",
  "owner": "bridge/p017-p018-hard-core-v2",
  "base_state": "SUPERSEDED",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Control the surviving global core mass after exact anchor/singular normalization rather than stacking more fixed CRT layers.",
  "next_action": "Do not redispatch the old analytic-mass task as written. Its Euler/core-mass layer was developed in later P017×P018 work; any new analytic continuation must be justified from the latest exact weighted-boundary residue.",
  "dependencies": [
    {
      "target": "canonical/relayed P018 cubic channel contraction",
      "action": "CONSUME",
      "satisfied": true
    }
  ],
  "source_refs": [
    "PR #170",
    "bridge/p017-p018-hard-core-v2"
  ],
  "evidence_status": "LEGACY_CONTROL_MIGRATED_SUPERSEDED",
  "last_progress_ref": "PR #170",
  "last_progress_at": "2026-08-24T02:06:30+00:00",
  "hard_block": null,
  "tags": [
    "Euler-product",
    "P017",
    "P018",
    "analytic",
    "legacy-control-migration",
    "sieve",
    "v2-cutover"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P017-P018-ANALYTIC-MASS",
  "parent_objective_id": "LEGACY_CONTROL_CUTOVER_RS_P017_P018_ANALYTIC_MASS",
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

# RS-P017-P018-ANALYTIC-MASS — V2 Task Preservation

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
