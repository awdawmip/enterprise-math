# Foundation Steward Control-Plane Addendum

Status: `ACTIVE / CONTROL-PLANE PRECEDENCE ADDENDUM / V2`
Effective: `2026-11-13`
Classification: `NO_NEW_MATHEMATICS`

This addendum changes no mathematical Foundation content, theorem status, Steward authority, or backflow classification. It only fixes post-cutover control routing for Foundation Steward work.

## 1. Authority precedence

For task publication, execution handoff, live dispatch and tool-reuse resolution, use:

- `control_plane/current_control_authority.json`;
- `research_task_publication_contract_v2.json`;
- `research_dispatch_contract.json`;
- `tool_invocation_policy.json`.

Any older Steward/architecture prose that still names `research_task_records/<task-id>/<publication-id>.json`, `tools/research_task_records.py`, `research_runtime_policy_v2.json` as a new-task definition surface, or `tools/research_dispatch.py` as the complete live entrypoint is compatibility wording only.

## 2. Foundation question to research execution

A genuine unresolved mathematical question exposed by Steward work may be investigated, corrected or related to prior results by the Steward itself. An FQ/backflow record is useful optional support, not permission to start or continue mathematics.

Only when choosing to publish a separately executable shared research task, the control path is:

`VERIFIED RESEARCH NEED (OPTIONAL FQ)`

`-> V2 TASKBOOK`

`-> tools/research_task_records.py prepare`

`-> IMMUTABLE V2 PUBLICATION RECORD`

`-> research_control_dispatch.py`

`-> Issue #240 CLAIM / OWNER SCOPE`

`-> RESEARCHER EXECUTION`.

Do not create or modify `research_runtime_policy_v2.json` to publish the new task. Do not use the V1 shared registry as post-cutover task authority.

## 3. Steward task publication

When the Steward itself publishes a governance task, use the same immutable V2 transaction as Researcher and Driver publication.

`STEWARD-ID` is publisher provenance only. It does not auto-grant task execution ownership, theorem truth, Working Truth, Foundation promotion, or research-review authority beyond the Steward contract.

## 4. Dispatch

Canonical live dispatch is `research_control_dispatch.py`.

`tools/research_dispatch.py` is the ordinary fresh selector and cannot by itself conclude `NO_DISPATCH` while a valid owner may be stale-recoverable.

Freeze:

`STALE_SESSION + VALID_OWNER_CLAIM -> ADOPT_SAME_CLAIM`.

`FRESH_SELECTOR_EMPTY + OWNER_LIVENESS_UNKNOWN -> VERIFY_SESSION_LIVENESS`.

## 5. Tool integrity

Before accepting shared reusable machinery, Steward must run coverage/dedup at the timing defined by `tool_invocation_policy.json`, then resolve every relevant match through the reuse-resolution state machine.

`COVERAGE_LOOKUP != TOOL_USE`.

A matched mathematical interface may be `REUSE_APPLIED`; an executable result is `REUSE_EXECUTED` only if the existing implementation was actually run. If the current chat environment cannot run an adequate implementation, record `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE`; do not convert environment limitations into a new mathematical tool family.

## 6. Research boundary

The Steward may pursue a newly exposed mathematical problem, compare later results with old questions, and correct or generalize prior material when useful. Depth, method, order and handoff are research judgments; no FQ, Packet, classification, fixed stage or return-to-stewardship ceremony is required. Mark conjectures and unreviewed conclusions honestly. Lean/formalization is optional, not a default requirement.

This freedom does not activate another role, transfer a live CLAIM, or grant review/Working Truth/Foundation authority. Shared operational writes still use the writer's actual identity, current authorization and canonical ownership/CAS. GitHub remains the scientific source of record.
