# Foundation Steward Control-Plane Addendum

Status: `ACTIVE / CONTROL-PLANE PRECEDENCE ADDENDUM / V1`
Effective: `2026-08-28`
Classification: `NO_NEW_MATHEMATICS`

This addendum changes no mathematical Foundation content, theorem status, Steward authority, or backflow classification. It only fixes post-cutover control routing for Foundation Steward work.

## 1. Authority precedence

For task publication, execution handoff, live dispatch and tool-reuse resolution, use:

- `control_plane/current_control_authority.json`;
- `research_task_publication_contract_v2.json`;
- `research_dispatch_contract.json`;
- `tool_invocation_policy.json`.

Any older Steward/architecture prose that still names `research_task_registry.json`, `tools/research_task_registry.py`, `research_scheduler.json` as a new-task definition surface, or `tools/research_dispatch.py` as the complete live entrypoint is compatibility wording only.

## 2. Foundation question to research execution

A genuine unresolved mathematical question exposed by Steward work is still minimized and recorded through the Foundation Problem Set/backflow process.

When that question needs an executable research task, the control path is:

`FQ / VERIFIED RESEARCH NEED`

`-> V2 TASKBOOK`

`-> tools/research_task_records.py prepare`

`-> IMMUTABLE V2 PUBLICATION RECORD`

`-> research_control_dispatch.py`

`-> Issue #240 CLAIM / OWNER SCOPE`

`-> RESEARCHER EXECUTION`.

Do not create or modify `research_scheduler.json` to publish the new task. Do not use the V1 shared registry as post-cutover task authority.

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

This addendum does not permit the Steward to solve a newly exposed unresolved research problem by default. The existing rule remains:

`VERIFY DISCREPANCY -> MINIMIZE -> PUBLISH/HANDOFF V2 RESEARCH TASK WHEN NEEDED -> RETURN TO STEWARDSHIP`.
