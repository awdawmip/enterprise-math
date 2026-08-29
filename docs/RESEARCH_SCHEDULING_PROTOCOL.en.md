# Enterprise Math Research Scheduling Protocol

Status: `ACTIVE / CANONICAL SCHEDULING CONTRACT`  
Effective: 2026-08-29  
Scope: all L1 core owners, L2 program owners, L3 bridges/probes, and L4 integration replays.

This protocol resolves scheduling ambiguity while preserving one operational priority: **research is the hot path; GitHub is sparse coordination and durable provenance, not per-step telemetry.**

## 1. Primary invariant: research is parallel, canonical promotion is serialized

Enterprise Math separates two different activities:

- **research/discovery**: new proofs, counterexamples, constructions, tools, experiments, and specializations;
- **canonical promotion**: semantic ownership audit, numbering, bilingual replay, reference/lineage registration, final repository gates, and merge to `main`.

Research/discovery is parallel by default. Canonical promotion is serialized only where repository consistency requires it.

A dependency needed for canonical ownership or later integration is **not automatically a dependency of ongoing research**.

## 2. `defer` is not a blocker

The words `defer`, `consume from`, `owner moved`, `audit against`, `replay after`, `depends on owner`, or equivalent routing language mean:

> do not duplicate or prematurely promote the mother theorem here.

They do **not** mean:

> stop this research line until another branch finishes.

A route continues with every question that can be stated and tested without the missing result. It may use an already proved upstream theorem, keep a downstream statement conditional, construct examples/counterexamples, derive specializations, or isolate the exact missing lemma.

## 3. Only an explicit `HARD_BLOCK` may stop a route

A route may wait only if all of the following are recorded:

```text
HARD_BLOCK:
  missing_object: <exact theorem/data/experiment/artifact>
  owner: <route or external source>
  necessity: <why no meaningful independent next step exists>
  unblock_condition: <precise condition that resumes work>
```

If any field is absent, the condition is not a hard block.

`HARD_BLOCK` must be exceptional. If a route can continue by proving a conditional theorem, searching for a counterexample, weakening assumptions, building an executable oracle, testing a special case, or attacking a different open frontier, it is not blocked.

Governance, registry publication, scheduler state, CI, review, identity registration, moving `main`, or a pending workflow is never by itself a mathematical `HARD_BLOCK`.

## 4. L1/L2/L3 owners may always create new mathematics

- L1 core owner: new reusable mother theorems are allowed and expected.
- L2 program owner: new program-specific mathematics, applications, counterexamples, and candidate generalizations are allowed and expected.
- L3 bridge/probe: new mathematics is allowed within the bridge's declared question.
- L4 integration replay: **NO NEW MATHEMATICS**.

A replay manifest on an L1/L2/L3 owner branch containing

`no_new_mathematics_during_replay = true`

applies only to the identified replay slice or replay operation. It must never freeze the owner branch as a whole.

If a new theorem is discovered while moving one replay slice, record it on the appropriate L1/L2/L3 research frontier; do not smuggle it into the L4 transport commit.

## 5. Moving `main` is not a research blocker

Repeatedly rebuilding the same validated result every time `main` advances creates integration livelock.

Use this rule instead:

1. freeze the proved semantic payload by source commit/blob/theorem identity;
2. continue unrelated research normally;
3. create or refresh the L4 integration replay when promotion is actually ready;
4. perform one final combination gate against the then-current `main` before merge;
5. if `main` moved only by unrelated changes, do not create a new research generation or restart the proof;
6. restart research only when the new `main` introduces a genuine semantic conflict or invalidates an assumption.

Thus the requirement is **final-state compatibility**, not continuous chase of every intermediate `main` head.

## 6. Relay action classes

Every new cross-route Relay entry should classify its requested downstream action as exactly one of:

- `INFORM` — useful context; no action required before continuing;
- `CONSUME` — reuse this result rather than duplicating it;
- `TEST` — pressure-test or seek a bridge/counterexample when convenient to that route;
- `HARD_DEPENDENCY` — the downstream route truly cannot continue on its declared frontier without this result.

Only `HARD_DEPENDENCY` may create a `HARD_BLOCK`, and the downstream route must still record the four `HARD_BLOCK` fields itself.

Absence of an acknowledgement does not block the upstream route.

## 7. Route state is a semantic checkpoint, not a heartbeat tax

An active owner should be able to reconstruct:

```text
frontier: <current mathematical question>
hard_block: NONE | <HARD_BLOCK record>
last_durable_progress: <commit/return/checkpoint/Relay result when one exists>
shared_surface_seen: <relevant canonical snapshot when one was actually needed>
```

This is a recoverability property, not a requirement to write or refresh the record on every step.

Freeze:

`ROUTINE_RESEARCH_STEP -> NO_GOVERNANCE_WRITE_REQUIRED`.

`NO_NEW_DURABLE_PROGRESS -> NO_HEARTBEAT_REQUIRED_BY_DEFAULT`.

`PENDING_CI_OR_REVIEW -> CONTINUE_INDEPENDENT_SAFE_WORK; DO_NOT_POLL_AS_PROGRESS`.

A `HEARTBEAT` event remains a legacy compatibility mechanism for a genuinely needed owner-lease renewal when no semantic progress event exists. It is **not** a periodic research obligation and must never be used as owner-scope session-liveness evidence.

## 8. Recovery-aware live dispatch and conversation handoff

Canonical live scheduling/control routing is:

`research_control_dispatch.py`.

It composes stale-owner recovery before fresh selection over:

- immutable post-cutover task publications: `research_task_records/<task-id>/<publication-id>.json`;
- frozen legacy task definitions only: `research_scheduler.json`;
- recovery-aware live router: `research_control_dispatch.py`;
- ordinary merged fresh selector/reducer: `tools/research_dispatch.py`;
- active-cohort fresh lane selector: `tools/research_lane_dispatch.py`;
- live runtime coordination: Research Dispatch Board Issue #240;
- result/review overlays: `research_result_records/` and `research_result_reviews/`.

`tools/research_dispatch.py` remains the canonical **task-definition / ordinary fresh-selection** reducer. It does not own stale-session adoption and cannot by itself produce a global `NO_DISPATCH` verdict.

Freeze:

`STALE_SESSION + VALID_OWNER_CLAIM -> ADOPT_EXISTING_WINNING_CLAIM_WITHOUT_NEW_CLAIM`.

`FRESH_SELECTOR_EMPTY + VALID_OWNER_UNKNOWN_LIVENESS -> VERIFY_SESSION_LIVENESS`.

`FRESH_SELECTOR_MISS != NO_DISPATCH`.

`tools/research_scheduler.py` remains a **legacy event-reduction/config-validation primitive**. It is not post-cutover task-definition authority.

The scheduler coordinates **who continues which frontier**. It does not decide whether a theorem is proved, canonical, novel, or ready for promotion.

### 8.1 Task existence and states

For post-cutover work:

`TASKBOOK_FILE != OFFICIAL_TASK`.

`IMMUTABLE_PUBLICATION_RECORD_CREATED -> OFFICIAL_TASK_EXISTS`.

The ordinary merged dispatch view derives runtime states including:

`NEEDS_DISPATCH`, `LEASED`, `AWAITING_REVIEW`, `BLOCKED`, `COMPLETE`, and `DORMANT`.

Historical task-state names such as `READY`, `HANDOFF_READY`, `CLAIMED`, `IN_PROGRESS`, `DONE`, and `SUPERSEDED` remain compatible inputs/derived details.

A frozen return awaiting Driver review is `AWAITING_REVIEW`, not a researcher-dispatchable task. A terminal reviewed result is `COMPLETE`.

### 8.2 One CLAIM, not a pre-claim GitHub transaction chain

For a new registered execution, the **single Issue #240 `CLAIM` comment is the execution authorization envelope**. It carries or resolves:

- exact task ID and current `publication_id`;
- claim ID;
- Researcher-ID or deterministic derivation inputs;
- theorem owner;
- execution branch and exact base commit;
- allowed output paths/prefixes;
- owner lease duration.

Freeze:

`VALIDATE_CURRENT_PUBLICATION -> CREATE_OR_VERIFY_BRANCH -> ONE_CLAIM -> RESEARCH`.

No separate pre-claim execution-record commit, PR, merge, CI wait, or second GitHub comment is required.

An immutable execution record may be materialized later for durable provenance and batched with the first genuine research checkpoint or final return.

### 8.3 Server-authenticated Issue #240 events

A live registered runtime event is one Issue #240 comment. Authentication reuses that same comment; it does **not** add a second write.

Canonical live-event envelope is derived from GitHub server metadata:

- `comment_id` — event ordering authority;
- `user.login` — authenticated GitHub author provenance;
- `created_at` — event/lease clock authority;
- `updated_at` — edit detection;
- SHA-256 of the exact comment body — payload pin.

The JSON body's `actor` and `at` fields are descriptive provenance only. They are not authentication or clock authority.

Freeze:

`SERVER_COMMENT_ID > BODY_DECLARED_ORDER`.

`SERVER_CREATED_AT > BODY_DECLARED_AT`.

`EDITED_EVENT_COMMENT -> NOT_RUNTIME_AUTHORITY`.

If an event needs correction, append a new correction/superseding event. Do not edit an earlier scheduler event to rewrite history.

Bare V1 event objects remain available only for explicit historical replay/unit-test compatibility. They are not live authority for an immutably registered task.

### 8.4 Claims, owner lease, and owner-scope session liveness

A `CLAIM` is a temporary task-ownership lease, not permanent ownership and not proof that the exact winning owner scope remains active.

`OWNER_LEASE != OWNER_SCOPE_SESSION_LIVENESS`.

`CONVERSATION_ACTIVITY != OWNER_SCOPE_SESSION_LIVENESS`.

- `PROGRESS` may renew the owner lease and record a real checkpoint;
- `HEARTBEAT` may renew the owner lease only when actually needed, but is not periodic by default and is not session-liveness evidence;
- owner-scope session liveness is refreshed only by an independently verified `TASK_RESEARCH_RESPONSE` or `DURABLE_EXECUTION_PROGRESS` bound to the exact current winning `claim_id` and task/lane scope;
- Control-plane, Driver, Steward, FREE, unrelated-task/lane, generic chat, and CI/status activity do not refresh a suspended Researcher claim;
- `HANDOFF` releases the claim deliberately and states one concrete `next_action`;
- an expired owner claim returns to a dispatchable recovery state under the compatibility reducer;
- a second valid claim cannot preempt a live lease;
- stale owner-scope session recovery adopts a still-valid winning claim after durable-frontier verification rather than waiting for the owner lease to expire.

### 8.5 New-conversation automatic routing

A current explicit user task always overrides automatic selection.

If a new Enterprise Math task-research conversation has no user-selected task and automatic dispatch is applicable, it must:

1. read the current Common Surface and this protocol;
2. invoke `research_control_dispatch.py` as the top-level route, supplying exact owner-scope liveness observations when independently available;
3. if the action is `ADOPT_OWNER_CLAIM`, verify the durable frontier and adopt the **same** winning claim without creating a second claim;
4. if the action is `VERIFY_SESSION_LIVENESS`, resolve exact owner-scope activity before inferring that no task exists;
5. only when the action is `CLAIM_NEW_OWNER`, accept the task/lane selected through the subordinate fresh selector and post one valid server-backed `CLAIM` before substantive task-specific research begins;
6. refresh only the selected task's materially relevant source/taskbook/branch dependencies before proving anything new.

Do **not** infer `NO_TASK` / `NO_DISPATCH` merely because a direct `tools/research_dispatch.py` fresh-selection call returns no candidate. Do not preload the whole repository, poll CI, chase moving `main`, or repeatedly re-read Issue #240 after the claim unless a real coordination boundary requires it.

The live-claim race is resolved by the first valid GitHub comment in server comment-ID order.

### 8.6 Session exit and result contract

A research session should leave a recoverable durable frontier at a meaningful boundary, but it must not manufacture GitHub writes merely because a turn is ending.

When an unfinished task genuinely needs transfer to another executor, post `HANDOFF` with:

- task ID and current claim ID;
- last meaningful durable progress reference;
- one concrete next action;
- `hard_block = NONE` unless the full exceptional block record is justified.

If the same conversation is simply continuing and no transfer is needed, no HANDOFF is required.

Use result freeze when the declared research execution has reached its return boundary. For a registered task, `DONE` is accepted only through the canonical result/review lifecycle; a bare DONE statement does not self-close the task.

No downstream ACK is required for handoff.

### 8.7 Control-plane consistency

`branch_governance_overrides.json` remains the theorem/owner registry. New task existence comes from immutable task publications; the frozen scheduler file is only a legacy baseline. Foundation task links resolve through the canonical merged dispatch view.

Historical branch ledgers and old scheduler rows remain provenance/snapshots, not live new-task publication authority.

CI, review, L4 replay, or moving `main` may affect evidence/promotion status, but they do not silently mutate research into `BLOCKED`.

## 9. Interaction-budget invariant

The control plane must not become the dominant research workload.

Between genuine semantic checkpoints, the default budget is:

- governance-only repository writes: **0**;
- CI polling: **0**;
- review polling: **0**;
- moving-main chase: **0**;
- mandatory scheduler heartbeat: **0**.

Allowed sparse boundaries include task publication, one claim, genuine durable research checkpoint when useful, frozen return, Driver review/disposition, and final integration/promotion.

If a future rule requires extra GitHub operations, it must show why the information cannot be carried by an already-required semantic-boundary artifact/event. Otherwise the extra operation is a control-plane regression.

## 10. Relationship to Architecture v2

This protocol preserves Architecture v2's theorem ownership and non-destructive replay rules. It changes only the mistaken scheduling interpretation:

> ownership is unique; knowledge is shared; research remains parallel; control persistence remains sparse.

The A0–A5 ownership axis prevents duplicate mother theorems. It must not become a serial dependency chain or a GitHub-polling loop.
