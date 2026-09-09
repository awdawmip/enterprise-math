<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-DRIVER-HODGE-H0O-REVISION-REVIEW-ROUTING",
  "title": "Driver Hodge H0O revision result review and routing",
  "kind": "GOVERNANCE",
  "owner": "driver/governance/hodge-h0o-revision-review-routing",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "H0O generation 2 is the current same-TaskID theorem-preserving contract-alignment revision. The original conservation identity is preserved, while the original hard target remains unestablished unless one of its three terminal alternatives is actually proved.",
  "next_action": "Refresh H0O generation 2 and its exact result/review state. If no revised Result exists, preserve the generation-2 research entrypoint. When a revised Result appears, verify the six retained obligations, the three terminal alternatives, the preserved conservation theorem, and the unresolved-residue ledger before issuing any Driver disposition or later route.",
  "dependencies": [
    "TP2-853EE36ED78FF34CC992",
    "DR-59B956C38543808B4146",
    "RR-FB3CF77C4F611FDED79B"
  ],
  "source_refs": [
    "git:awdawmip/enterprise-math@c16084e34d5e1e0392ab5dd6684891aa039a772a:research_task_records/RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3/TP2-853EE36ED78FF34CC992.json",
    "git:awdawmip/enterprise-math@c16084e34d5e1e0392ab5dd6684891aa039a772a:research_tasks/HODGE_H0O_CONTRACT_ALIGNMENT_REVISION_20260908.md",
    "git:awdawmip/enterprise-math@c16084e34d5e1e0392ab5dd6684891aa039a772a:research_result_reviews/RR-FB3CF77C4F611FDED79B/DR-59B956C38543808B4146.json"
  ],
  "evidence_status": "H0O_GEN2_ACTIVE_CLAIMABLE / ORIGINAL_THEOREM_PRESERVED / ORIGINAL_HARD_TARGET_OPEN",
  "last_progress_ref": "git:awdawmip/enterprise-math@c16084e34d5e1e0392ab5dd6684891aa039a772a:research_task_records/RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3/TP2-853EE36ED78FF34CC992.json",
  "last_progress_at": "2026-09-09T10:06:00+00:00",
  "hard_block": "AWAIT_REVISED_H0O_RESULT_OR_NEW_CONTROL_EVIDENCE",
  "tags": [
    "Driver",
    "HODGE",
    "H0O",
    "review",
    "routing",
    "revision",
    "exact-set"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-DRIVER-HODGE-H0O-REVISION-REVIEW-ROUTING",
  "parent_objective_id": "HODGE_SPECIAL_OPEN_FRONTIER_ALGEBRAICITY_MECHANISM",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "DRV-HODGE-H0O",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Driver Hodge H0O revision result review and routing

Status: `READY / DRIVER-PUBLISHED GOVERNANCE`

## Mother question

How should a successor Driver carry the H0O line from the current generation-2 theorem-preserving revision through exact review and routing without discarding the valid seed-conservation theorem, repeating the old search, or treating contract correction as proof of the unchanged hard target?

## Frozen inputs and scope

The current research publication is `RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3 / TP2-853EE36ED78FF34CC992`. It supersedes generation 1 only as the current executable definition of the same Task-ID. Preserve the original nonsplit `[-3]` target, the H0N separator `Pi_W`, the Poincare-polarization pure codimension-three family, and the proved identity relating exceptional source support to exceptional output.

The prior Driver disposition `DR-59B956C38543808B4146` is a theorem-preserving `REQUEST_REVISION`. It does not reject the conservation identity. It records that the submitted Result did not establish any of the original terminal alternatives: an actual nonzero exceptional output, a whole-family zero-projection theorem, or exact target-side non-instantiability of the declared family.

This governance task performs no Hodge proof itself and grants no theorem strength. It must consume the current generation-2 Result when one exists and must not replace the unchanged research hard target with a bookkeeping-only success.

## Hard target and required outputs

Hard target: `HODGE_H0O_REVISION_RESULT_EXACTLY_REVIEWED_AND_PARENT_ROUTE_TYPED`.

Required Driver outputs:

1. Refresh the exact current H0O generation-2 publication and its Result/review set before acting.
2. If no revised Result is frozen, preserve `TP2-853EE36ED78FF34CC992` as the research entrypoint and return `WAITING_ON_H0O_GEN2_RESEARCH`.
3. When a revised Result appears, verify that it preserves the six original obligations and separately accounts for all three original terminal alternatives.
4. Preserve the proved conservation identity at exactly its demonstrated strength; do not convert absence of an exceptional source cycle into universal zero projection or family non-instantiability.
5. If the corrected Result is only a partial or negative boundary, keep the unchanged H0O hard target and parent Hodge objective open with a nonempty residue.
6. If a genuine original terminal theorem is supplied, review it independently at its exact hypotheses before deciding task closure or a later research route.
7. Persist the resulting review/follow-up authority and update the durable line handoff with the smallest unfinished unit.

## Research value to preserve

H0O contains real reusable mathematics but previously mixed that theorem with an overstrong completion label. The line must preserve the exact exceptional-component conservation law while preventing future Drivers from consuming unsupported closure. A durable governance task makes the distinction recoverable without re-reading the whole Hodge history.

## Success, kill, and return criteria

Success requires an exact Driver disposition for the current generation-2 Result when available, correct preservation of the theorem/hard-target boundary, and a durable next route. If no Result exists, the valid terminal state for this control pass is `WAITING_ON_H0O_GEN2_RESEARCH`.

Kill any attempt to revive generation 1 as the executable task, to treat contract alignment alone as mathematical completion, to infer non-algebraicity or H1, or to open a broader kernel/correspondence search without a separately justified research task. This governance task closes only when no unresolved Driver action remains for H0O and control has been handed to a later routed unit.
