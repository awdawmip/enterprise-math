<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-1195-SELECTOR-INTERVAL-HEIGHT-CERT",
  "title": "1195: Exact Finite Selector Interval and Height Certificate — Closed by CP17",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Issue #1195 comment 5540958862 already supplies the rigorous four-term rank-5 interval recovery certificate that CP16 had left open. The prior generation of this task was published from a stale CP16-only recovery frontier and has no remaining research unit.",
  "next_action": "No research execution remains under this task. Consume comment 5540958862 as the completed interval certificate and use it only as an input to later selector/class-field or mixed-place identification work.",
  "dependencies": [],
  "source_refs": [
    "research_notes/1195_research_handoff_index_20260909.md",
    "research_notes/1195_research_handoff_postcp16_20260909.md",
    "issue:1195#issuecomment-5540958862"
  ],
  "evidence_status": "VERIFIED_COMPLETE_BY_DURABLE_ISSUE_CHECKPOINT",
  "last_progress_ref": "issue:1195#issuecomment-5540958862",
  "last_progress_at": "2026-09-09T01:05:00+08:00",
  "hard_block": null,
  "tags": ["1195","selector","interval-certificate","height","completed"],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-1195-SELECTOR-INTERVAL-HEIGHT-CERT",
  "parent_objective_id": "EM-PI-POWER-SPECTRAL-SELECTOR",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R1195C",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
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

# 1195: Exact Finite Selector Interval and Height Certificate — Closed by CP17

Status: `VERIFIED COMPLETE / TERMINAL CAPTURE / PUBLISHED_REGISTERED`

## 0. Mother question

Is there any remaining research work under the CP16 request for a rigorous finite interval/height certificate for a rank-5 selector, or has that exact last mile already been completed in durable #1195 state?

## 1. Frozen inputs and scope

Read the post-CP16 reconciliation handoff and Issue #1195 comment `5540958862`. That checkpoint explicitly states `RIGOROUS FINITE INTERVAL CERTIFICATE / exact rational interval arithmetic` and closes the four-term `n=0,1,2,3` last mile left by CP16.

This terminal capture exists only to prevent a stale state-machine task from re-dispatching already completed work. It does not reopen the certificate, request a stronger theorem, or create a new numerical benchmark.

## 2. Hard target and required outputs

Hard target: `CONFIRM_CP17_CONSUMPTION_AND_NO_REPLAY`.

The durable completion already provides the required output. A future reader should:

1. consume `5540958862` as the exact finite interval certificate;
2. preserve CP16's asymptotic height-identification theorem as its parent result;
3. avoid rerunning the four-term intervalization unless an independently evidenced integrity defect is found;
4. route any genuinely new question to a distinct successor task rather than relabeling this completed unit.

## 3. Research value to preserve

Closing this stale task protects the research graph from duplicate execution and preserves the exact distinction between a recovered-but-outdated conversational frontier and current durable authority. The interval certificate remains an important dependency for later finite selector and adelic identification work, but it is no longer an open research problem.

## 4. Success, kill, and return criteria

Success is the terminal state itself: no new researcher should claim this task. The certificate is already verified complete in the durable issue checkpoint.

Kill any attempt to restart the CP16 last mile merely because an older handoff or publication said it was open. If future evidence reveals a genuine defect in `5540958862`, open a new narrowly scoped integrity/revision task with that evidence rather than reactivating this one.