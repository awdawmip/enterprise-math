# Continue research from any new authorized conversation

GitHub preserves the task, publication, evidence and review history. Drivers, researchers and execution sessions are replaceable. A new conversation connected to the project MCP can continue with its own authorized identity, without contacting the predecessor or recovering private chat.

Ask the conversation to continue an exact Task-ID from its highest verified durable frontier. Use `em_control_tasks` when discovering tasks; use `em_control_continuation` directly when the Task-ID is known. Read actual asynchronous receipts with `em_control_result`. Inventory pages belong to one explicit as-of snapshot; execution and writes still obtain fresh authority.

## 1. Read evidence before choosing an action

Read the task and allowed evidence through `em_control_artifact`. Control-main and research-branch commits stay distinct. A link is a readback candidate until its actual bytes/hash are verified.

| State | New conversation action |
|---|---|
| NEEDS_DISPATCH | Register your session and prepare the required role; reconcile any prior frontier |
| AWAITING_REVIEW | Activate your Driver authority and read the exact frozen result |
| LEASED | Check actual owner activity; prepare takeover only when canonically stale |
| BLOCKED / DORMANT | Read the reason and distinguish evidence/authority faults from mathematical obstacles |
| COMPLETE | Consume completed or superseded records without repeating completed units |

Historical identities and authors remain provenance. The disappearance of an actor does not solve a mathematical obstacle or authorize borrowing its identity.

## 2. Register this execution session

Start your own RESEARCHER or RESEARCH_DRIVER session with `em_session_start`. This creates and verifies a real Source-backed service execution session, not a platform-attested chat identity. Keep its opaque capability private. Use a new unique request ID for a new execution; retries of an existing issuance require its original capability. Public session/RA records do not prove key possession. Losing the first response permits a fresh unclaimed session, not recovery of another session's key through a common request name.

Researcher RA and Driver DA are separate. Activate a Driver separately with `em_driver_activate` when the task requires that role. Registration and preparation do not confer CLAIM, mathematical acceptance, Working Truth or Foundation authority.

## 3. Claim or take over

Use `em_task_prepare` for exact fresh work or `em_continuation_prepare` for a predecessor-bound continuation with verified frontier and exact previous CLAIM/comment. Preparation is not ownership. Post with `em_execution_claim`, verify the actual unique winner and use `em_execution_open` for the current binding before working. Governance tasks use a real Driver session and DA without a fabricated researcher activity.

Live takeover requires real canonical owner inactivity, normally at least 600 seconds; callers cannot override recent activity with an older assertion. A genuine CONTINUATION HANDOFF permits RESUME. Typed CLAIM continuation rotates the execution/claim with predecessor CAS, while preserving Task-ID, publication, scope and all historical provenance. Old writers are fenced. Same-session transport resume is separate from a new conversation taking over.

## 4. Persist progress, results and reviews through MCP

Upload bounded artifacts with `em_artifact_upload`, publish a Source checkpoint through `em_execution_publish`, and verify its immutable readback before PROGRESS or CONTINUATION HANDOFF. Preserve completed units, the smallest unfinished unit, the next action, no-repeat facts and contribution history. `em_execution_freeze` invokes the canonical Result writer and only hands off after Source publication. Driver reports and exact review/followup use `em_driver_publish` and `em_driver_review`. The service does not choose a mathematical verdict or create a successor merely from PASS.

Reconcile unknown remote outcomes with `em_control_reconcile` before repeating mutations. End your own session with `em_session_close` after durable handoff; applicable Driver authority is revoked without invalidating historical reviews. The next conversation consumes the same durable task and frontier.

Governance tasks use a real Driver session and DA, not a fabricated researcher activity. The service does not execute arbitrary uploaded programs or choose mathematical verdicts; task-specific compute requirements remain explicit. Transport checkpoints alone do not replace canonical Source persistence.

## Preserved boundaries

P000, FREE information barriers, exact task scope, author/independent-review distinctions and Working Truth/Foundation/promotion gates remain unchanged. New identity is not evidence of independence. Pre-cutover RR/DR bytes keep their original audits; prospective records need payload-bound current-write authorization. See the [protocol](RESEARCH_CONTINUATION_PROTOCOL.md) and [Chinese guide](CONTINUE_RESEARCH.zh-CN.md).
