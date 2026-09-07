# Research Scheduling Protocol V2

Status: `ACTIVE / CURRENT ONLY`

Task definitions are immutable V2 publications. `research_control_dispatch.py` first resolves stale-owner recovery, then delegates fresh task selection to `tools/research_dispatch.py` or active-cohort lane selection to `tools/research_lane_dispatch.py`.

Issue #240 mutations require an authenticated, unedited GitHub server comment envelope from an authorized actor. `tools/research_runtime_reducer.py` is a pure reducer; it owns no task table and no mathematical authority.

Selection order is defined in `research_runtime_policy_v2.json`. Owner lease and conversation liveness are independent. A valid stale owner is adopted after durable-frontier verification; a second claim is not created.

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
