# Enterprise Math Research Scheduling Protocol

Status: `ACTIVE / CANONICAL SCHEDULING CONTRACT / V2`  
Effective: 2026-08-24  
Scope: all L1 core owners, L2 program owners, L3 bridges/probes, L4 integration replays, and shared Driver review work.

This protocol resolves ambiguity created during Architecture v2 migration and later task/review growth. Where older migration notes, replay manifests, branch ledgers, Relay wording, or static scheduler rows can be read as requiring one research line to wait for another or as privately assigning work to one conversation, this protocol controls the scheduling interpretation.

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

## 7. Route heartbeat

Every active owner should be able to state:

```text
frontier: <current mathematical question>
hard_block: NONE | <HARD_BLOCK record>
last_progress: <commit/PR/Relay result>
shared_surface_seen: <main SHA or common-surface revision>
```

If `hard_block = NONE`, the route should continue research rather than waiting for another conversation, branch, review, or replay.

## 8. Unified task/review state machine and conversation handoff

The route heartbeat is made executable by:

- `research_scheduler.json` / `tools/research_scheduler.py` for the legacy task-state reducer;
- `research_work_state_machine.json` / `tools/research_work_state.py` for task publication, safe generic claiming and Driver review state;
- the append-only Research Dispatch Board Issue #240 as the shared event log.

The control plane coordinates **who executes which selected task and who reviews which return**. It does not decide whether a theorem is proved, canonical, novel, or ready for promotion.

Freeze:

`USER != MANUAL_TASK_OR_REVIEW_MESSAGE_BUS`.

### 8.1 Task states and publication generations

The durable task frontier retains the legacy states:

`BACKLOG -> READY -> CLAIMED -> IN_PROGRESS -> HANDOFF_READY -> DONE`

with two exceptional exits:

- `BLOCKED` — only after a complete four-field `HARD_BLOCK`;
- `SUPERSEDED` — the task frontier has been replaced by another explicit task.

But a static `READY` row is no longer sufficient by itself for generic automatic claiming.

For a newly approved or re-reviewed taskbook:

`TASKBOOK_DISPATCH_PASS -> SAME_TURN_TASK_PUBLISH`.

`TASK_PUBLISH` records an immutable `taskbook_ref=path@commit`, issuing Driver-ID and current routing fields. The latest valid publication is the current task generation. Runtime DONE/SUPERSEDE/claim events from an older generation of the same task id remain provenance and do not mutate the new generation.

Generic claim eligibility is limited to:

1. current published task generations; and
2. legacy tasks with reducer-accepted runtime execution history that genuinely need continuation/handoff recovery.

Untouched historical static `READY`/`HANDOFF_READY` entries remain visible as provenance but do not silently re-enter the generic queue.

### 8.2 Claims are renewable leases

A `CLAIM` is a temporary execution lease, not permanent ownership. Its default duration is declared by the task/scheduler contract.

- `PROGRESS` renews the lease and records a real checkpoint;
- `HEARTBEAT` renews the lease when no better progress event exists;
- `HANDOFF` releases the claim deliberately and must state one concrete `next_action`;
- if a claimant disappears without handoff, lease expiry returns the task to `HANDOFF_READY / NEEDS_DISPATCH`;
- a second claim cannot preempt a live lease;
- after expiry, handoff, unblock, or other valid release, another conversation may claim the task.

Legacy runtime task events remain valid under `ENTERPRISE_MATH_SCHEDULER_EVENT_V1`; the unified layer may also normalize compatible task runtime events from `ENTERPRISE_MATH_WORK_EVENT_V1`. Event authority follows append-only board comment order.

### 8.3 Generic researcher claim: `领任务`

A current explicit user-selected task always overrides generic selection.

A generic request such as `领任务`, `领取任务`, `claim task`, or equivalent explicitly requests shared-state TASK dispatch. It is distinct from FREE Phase-A research and from an ordinary conversation with no selected topic.

On generic claim, a researcher must:

1. read the unified work-state rules and current board events needed for selection;
2. reduce the current published/runtime-continuation task states;
3. ignore live leases, complete/superseded tasks, valid blocked tasks, dormant BACKLOG, and untouched unpublished legacy READY rows;
4. prefer `HANDOFF_READY` over fresh `READY` within the eligible shared queue;
5. within that state order rank by priority, leverage, oldest accepted progress, then stable task id;
6. post a valid `CLAIM` before substantive task-specific research;
7. resolve/allocate the Researcher-ID from the claim;
8. load the exact published taskbook ref when present, then only the first dependencies needed to start;
9. begin the task without asking the user to provide a task id or handoff prompt.

This rule is deterministic; concurrent claim races are resolved by the first valid append-only claim event.

FREE Phase A is never entered or scheduled by this generic task-claim command.

### 8.4 Research completion and review request

A shared-state research session must not silently disappear from the control plane.

Before ending an unfinished task, post `HANDOFF` with task/claim id, last meaningful progress ref and one concrete next action.

Use `DONE` only when the declared task frontier is actually complete. For a completed shared task requiring review, the same semantic checkpoint also appends `REVIEW_REQUEST` with:

- review id and task id;
- originating Researcher-ID;
- issuing Driver-ID when known from task publication;
- exact review objective;
- target refs;
- evidence refs;
- execution-log refs;
- requested checks;
- priority.

Freeze:

`RESEARCH_DONE -> SAME_TURN_DONE_EVENT + REVIEW_REQUEST`.

The user does not need to copy the return, logs, task id, or review instructions into another conversation.

### 8.5 Generic Driver review claim: `领审核`

A Driver request such as `领审核`, `领取审核`, `claim review`, or equivalent explicitly requests the shared review queue.

Reviews use renewable leases analogous to task claims and support `REVIEW_PROGRESS`, `REVIEW_HANDOFF`, `REVIEW_DONE`, and `REVIEW_SUPERSEDE`.

There is no private issuer lock:

`TASK_ISSUER != REQUIRED_REVIEWER`.

Any active Driver may claim a review. Selection uses review state and priority first; among otherwise comparable items it prefers a Driver-ID different from the task-issuing Driver-ID, then older request time. A P0 review is not delayed merely to obtain a different Driver when only lower-priority cross-review work exists.

If no different Driver is available, same-Driver review is permitted and is explicitly labeled. It is not independent replication merely because a review record exists.

`REVIEW_DONE` records verdict, findings, evidence refs, next action, method-harvest classification and successor disposition.

Truth boundaries remain:

`SCHEDULER_DONE != THEOREM_TRUTH`.

`REVIEW_DONE != CANONICAL_MAIN`.

Foundation and promotion gates remain separate.

### 8.6 Control-plane consistency

`branch_governance_overrides.json` remains the machine owner registry. `research_scheduler.json` remains the durable legacy coverage surface. `TASK_PUBLISH` is the current publication surface for newly approved/re-reviewed task generations; runtime task/review events are the live lease/result surface.

Historical branch ledgers and untouched old scheduler rows remain provenance/snapshots, not automatic executor assignments.

CI, review, L4 replay, or moving `main` may affect evidence/promotion status, but they do not silently mutate a research task into `BLOCKED`.

Policy updates may stale a taskbook for future dispatch/publication without retroactively erasing an already-running frozen execution.

## 9. Relationship to Architecture v2

This protocol preserves Architecture v2's theorem ownership and non-destructive replay rules. It changes only the mistaken scheduling interpretation and the user-relay bottleneck:

> ownership is unique; knowledge is shared; tasks and reviews are shared state; research remains parallel.

The A0–A5 ownership axis prevents duplicate mother theorems. It must not become a serial dependency chain or a private review chain.
