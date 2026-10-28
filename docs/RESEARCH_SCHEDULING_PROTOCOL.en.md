# Research Scheduling Protocol V2

Status: `ACTIVE / CURRENT ONLY`

Scheduled conversations follow the [autonomous execution and recovery protocol](AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md): reconcile unknown effects, restore existing verified work, then dispatch fresh work. A completed control subflow does not complete the parent research objective.

Task definitions are immutable V2 publications. At a new research-unit boundary, `research_control_dispatch.py` ranks eligible fresh tasks, cohort lanes and verified stale-owner successor candidates together. Active exact-owner sessions remain protected. Recovery still preserves the exact predecessor/frontier and requires the existing authenticated successor CLAIM/CAS; selecting a target grants no execution authority.

Issue #240 mutations require an authenticated, unedited GitHub server comment envelope from an authorized actor. `tools/research_runtime_reducer.py` is a pure reducer; it owns no task table and no mathematical authority.

Selection weights are configured in `research_runtime_policy_v2.json`: initially P0/P1/P2/P3 = 40/30/20/10. These are initial engineering defaults, not numbers specified by the user. `tools/research_fair_selection.py` reconstructs weighted service credits from reducer-accepted CLAIMs and availability transitions in the shared authenticated event snapshot. Each successful claim accrues the currently available classes' normalized weights and charges one unit to its actual winner. Absent classes accrue no debt, so their shares can be borrowed without a later repayment wave. A handoff or expired lease followed by a new successful claim counts; failed attempts, retries of the same claim ID, HEARTBEAT, PROGRESS and reading/renewing an existing owner do not.

Within a priority, explicit `parent_task_id` chains identify directions and receive equal available-direction service; missing links fall back to exact task IDs. Names and identity-ID stems are never fuzzy-clustered. Within a direction, fewer successful claims and then older progress break ties. Leverage and HANDOFF state do not grant unconditional precedence. Explicit priority filters and exact source-authorized assignments retain their existing scope.

This is an advisory weighted selector, not an atomic global quota or a new refusal gate. Existing per-task/lane CLAIM and predecessor CAS still decide actual ownership. Concurrent terminals may select from one old snapshot and successfully claim different tasks; every accepted winner is charged on the next snapshot, and later choices compensate. There is no strict promise of 4/3/2/1 in every ten concurrent claims. Refresh normal canonical state after a race; no new lock, poller or background service is required.

Historical accounting is limited to the authenticated current-publication/lane replay already admitted by the canonical reducer. An older publication's filtered-out claims cannot be asserted valid from its task name. Missing availability/history/parent metadata is reported in `fair_selection` and falls back to currently visible tasks; historical dependency or publication changes without retained transitions cannot establish exact past eligibility. Raw events, scientific conclusions, publication authority and old task records are unchanged. Owner lease and conversation liveness remain independent; claim expiry releases ownership but does not automatically execute or resume a job.

## Registered HANDOFF intent

HANDOFF terminality is machine-explicit. Natural-language `next_action`, `summary`, and `progress_ref` are descriptive evidence only and never decide whether the owner is returning work for Driver review or handing it to another researcher.

For authenticated registered Issue #240 HANDOFF events at or after the audited compatibility boundary `2026-09-07T02:20:00Z` (GitHub server `created_at`), a producer must use one of these structural forms:

- researcher continuation: `handoff_scope: CONTINUATION`;
- frozen return awaiting Driver review: `handoff_scope: FROZEN_RETURN_AWAITING_DRIVER_REVIEW`;
- frozen return with an immutable result: a nonempty `result_id`;
- legacy-compatible frozen return: exact `terminal_scope: RESEARCH_RETURN_FROZEN_AWAITING_DRIVER_REVIEW`.

The compatibility boundary was selected only after replaying the complete Issue #240 stream for that interval. Before enforcement there were exactly two HANDOFFs at or after the boundary: one structurally ambiguous PCF return and one already-structured P021 frozen return; there was no plain researcher-to-researcher continuation to reinterpret.

`terminal_candidate` remains a historical reducer-compatibility marker for pre-boundary events. New registered producers must not use it as the sole terminal marker.

A post-boundary HANDOFF with missing, malformed, unknown, or contradictory structural scope fails closed. In particular, `CONTINUATION` cannot coexist with a frozen-return marker. A structurally ambiguous HANDOFF does not release a task into fresh dispatch. Its provisional blocking authority exists only when the rejected event belonged to the claim that was actually live at the authenticated server event time; a wrong or ghost `claim_id` cannot block a task.

Corrections are append-only. While the original owner lease remains valid, append a new structurally valid HANDOFF using the same live claim. Do not edit the old Issue #240 comment.

The same live-claim provenance rule applies to a registered `DONE` rejected for lacking a frozen Result plus terminal Driver review: a bogus or non-live claim cannot acquire task-blocking authority merely by emitting a terminal-looking event.

Freeze:

`HANDOFF_TEXT != TERMINAL_AUTHORITY`.

`POST_BOUNDARY_REGISTERED_HANDOFF -> EXPLICIT_MACHINE_SCOPE`.

`AMBIGUOUS_HANDOFF != FRESH_REDISPATCH`.

`WRONG_OR_GHOST_CLAIM_TERMINAL_EVENT != BLOCKING_AUTHORITY`.
