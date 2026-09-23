# CONTROL_PLANE_MAINTENANCE — hourly Research lane cross-lane routing repair

Date: 2026-09-23
Scope: control/recovery only; no mathematical acceptance, Result, review, CLAIM, OPEN, or task completion is asserted by this record.
Parent objective: preserve autonomous Enterprise Math execution while keeping `chatgpt-hourly-enterprise-math-20260921` maintenance-only and returning Research work to a separate lawful execution lane.

## Highest verified control frontier before repair

Current Enterprise Math main observed immediately before this record: `09e61ec3685b6466c9155920ef19b3bba98237b7`.

The current shared operations contract requires CONTROL_PLANE_MAINTENANCE to remain non-research and to recover unknown effects before replay. Existing issue #1501 remains the exact D=-24 continuation adapter blocker; no new `continuation_prepare`, CLAIM, OPEN, Result, or review was performed by maintenance in this repair.

## Recurrent cross-lane contamination found

Read-only ordinary-control `status` on the fixed maintenance conversation used request:

- conversation: `chatgpt-hourly-enterprise-math-20260921`
- request: `maint11-status-20260923-1415-01`
- bridge issue: `awdawmip/kimi-query-bridge#1138`

It exposed a Researcher session inside the maintenance-only conversation:

- session: `MCP-3f3660813110464db7110d237a53aa1f`
- execution/researcher: `EM-DIRECT-5293F1`
- role/mode: `RESEARCHER / TASK_RESEARCH`
- start request: `research-hourly-session-20260923-1330-r6`
- prior contribution IDs retained by the service: `EM-DIRECT-55C4FA`, `EM-DIRECT-A17886`, `EM-DIRECT-C7E2E3`

The original start request is bridge issue `#1106`; it used the maintenance conversation ID. This is a recurrence of the earlier cross-lane failure, not a lawful maintenance role transition.

## Safety classification before fence

Read-only `recovery_status` request `maint11-recovery-20260923-1418-01` / bridge issue `#1139` verified all of the following for the contaminated session:

- `execution_authorized=false`
- `source_authority_verified=false`
- `pending=[]`
- `runs=[]`
- `unopened_claims=[]`
- `unpublished_uploads=[]`
- `blocked_work=[]`
- `has_more=false`
- no relevant collection was truncated

Therefore this local session was classified `CORRUPT_OR_CONFLICTED / CROSS_LANE_LOCAL_SESSION_WITH_NO_EXECUTION_FRONTIER`. It was safe to fence without releasing another executor's claim or discarding unpublished work.

## Minimal root-cause repair

The existing scheduled automation titled `每小时研究任务` remained enabled and retained its existing schedule/frequency/phase/notification behavior. Only its prompt routing was changed.

It now fixes its ordinary-control logical conversation to:

`chatgpt-research-hourly-enterprise-math-20260923`

and explicitly forbids Researcher execution operations on:

`chatgpt-hourly-enterprise-math-20260921`.

The new Research conversation is a distinct stable execution lane, not an identity reset caused by context loss. It must create/recover its own lawful Researcher session and preserve contribution history through canonical continuation. No scheduler, GitHub Action, hosted cron, duplicate automation, or privilege expansion was introduced.

## Fence and readback

Maintenance then submitted exactly one `session_close` mutation for the contaminated session under request `maint11-close-crosslane-20260923-1421-01` / bridge issue `#1140`. The original request was polled to terminal state instead of being reissued.

Terminal native receipt:

- `closed=true`
- `role_authority_remaining=false`
- `historical_evidence_preserved=true`
- session: `MCP-3f3660813110464db7110d237a53aa1f`

Post-close read-only recovery request `maint11-recovery-postclose-20260923-1422-01` / bridge issue `#1141` verified:

- `session_state=CLOSED`
- `execution_authorized=false`
- `source_authority_verified=false`
- `pending=[]`
- `runs=[]`
- `unopened_claims=[]`
- `unpublished_uploads=[]`
- `blocked_work=[]`
- `has_more=false`

Maintenance-lane isolation is therefore `VERIFIED_COMPLETE` for this recurrence.

## Actual execution recovery versus control repair

Control repair: `VERIFIED_COMPLETE` for maintenance-lane isolation and routing-prompt root cause.

Actual TASK_RESEARCH recovery: `UNFINISHED / NOT_YET_PROVEN_BY_THIS_MAINTENANCE_RUN`. This repair does not claim that the newly separated hourly Research conversation has already registered a lawful Researcher session, won a CLAIM, or OPENed a run. That requires a later real execution-lane receipt and must not be fabricated by maintenance.

Scientific result from this maintenance unit: `NONE`.

## Remaining independent blocker

Issue `awdawmip/enterprise-math#1501` remains open. Current `control_plane/research_continuation.py` still treats an unresolved non-URL `last_progress_ref` such as stable review ID `DR-2EA60F5817976E662FA6` as a repository-relative path. The lawful Research lane has already hash-verified the unique exact immutable review artifact, but fresh typed continuation preparation still fails before native mutation with `CHAT_AUTHENTICATED_LAST_PROGRESS_ARTIFACT_REQUIRED`.

Do not repeat the same rejected `continuation_prepare` until the reviewed/deployed Source changes and a fresh continuation exposes an authenticated non-null `progress_reference_readback`. Acceptance remains: lawful Research lane continuation -> typed continuation_prepare -> explicit CLAIM -> explicit OPEN, with successful OPEN readback establishing execution. Issue #1500 remains a later, separate checkpoint lease-boundary concern and is not modified here.

## Next maintenance action / do not repeat

On the next maintenance round:

1. read this maintenance conversation's `recovery_status` first; if still closed/clean, do not reopen a Researcher/Driver session here;
2. verify whether the dedicated hourly Research lane has become discoverably active through its own lawful session/continuation receipts before calling execution recovered;
3. consume any reviewed/deployed change to #1501 exactly once and validate the affected Research path to its next real state;
4. do not repeat the fenced session_start, rejected continuation_prepare, already verified artifact reads, prior mathematics, or existing reviews.

No P000, source pin, mathematical scope, source-isolation, proof-strength, contribution-independence, or existing durable scientific frontier is changed by this control repair.
