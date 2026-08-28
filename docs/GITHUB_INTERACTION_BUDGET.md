# Enterprise Math GitHub Interaction Budget

Status: `ACTIVE / CANONICAL REMOTE-LIVENESS OVERRIDE`
Effective: `2026-08-22`
Scope: repository reads, GitHub connector/API use, branch/PR publication, Issue coordination, CI and promotion.

## 1. Core invariant

> **Research is the hot path; GitHub is a sparse remote persistence/integration boundary.**

Ordinary L1/L2/L3 research is `REMOTE_SILENT` between semantic checkpoints.

`REMOTE_SILENT` means low repository traffic. It does **not** mean the assistant stops working or waits for a user wake-up message.

Active-turn parent-task liveness is governed by:

`docs/ACTIVE_TURN_CONTINUATION_LIVENESS.md`.

Freeze:

`REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED`.

## 2. ChatGPT GitHub route

In ChatGPT/Project execution, when the connected GitHub capability is available:

`CONNECTED_GITHUB_PLUGIN = PRIMARY_REMOTE_GITHUB_PATH`.

Use the connected GitHub capability for repository reads/search, commits/branches, PRs/issues/comments and allowed workflow/status operations.

Do not use ChatGPT/container networking to clone/fetch GitHub or read raw GitHub URLs when the connected capability supports the required action.

A pre-existing local checkout may be used for actual local execution/tests. It is not the fallback transport for remote GitHub synchronization.

If a local/container GitHub network route is known unavailable, do not retry it later and do not keep reporting the same environment failure.

## 3. Startup read budget

Do not execute a universal repository preflight.

For explicit TASK_RESEARCH, normal remote startup is:

1. `AGENTS.md` if needed;
2. exact task entry;
3. first exact dependency needed to start.

Soft budget: `<= 3` routine source reads before substantive work.

FREE Phase A follows its primitive-substrate route.

Reuse immutable fetched blobs/SHAs within one execution phase.

<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_BEGIN: CONTEXT_READ_BUDGET -->
### Context fanout circuit breaker

Canonical machine-readable policy: `research_context_budget.json`.

`UNBOUNDED_COLLECTION_READ_FOR_DISCOVERY = FORBIDDEN`.

Conversational tool context is a bounded execution resource. Repository discovery must narrow before expanding; a connector call that can return an unknown or very large collection is not a harmless preflight.

- Do not enumerate high-fanout directories such as `tests/`, `research_tasks/`, `research_returns/`, task/result/review record directories, or `driver_reviews/` merely to discover one file.
- Do not request a recursive repository tree in conversational context merely to discover paths.
- Do not load all Issue #240 comments into conversational context. Prefer the canonical reducer when executable; otherwise use bounded GitHub API pages with at most 20 comments and expand only when the target event is not yet resolved.
- Use an exact path when already known; otherwise use bounded code/file search (`topn <= 20`), then exact-file line ranges (soft `<= 200` lines per read).
- A known large file is read by triggered ranges, not by repeatedly asking for the entire file.
- If a response is truncated, stop widening the same collection and narrow the query/range instead.

`TOOL_OUTPUT_TRUNCATED -> NARROW_AND_CONTINUE`.

`CONTEXT_COMPACTION -> RESTORE_DURABLE_TASK_STATE -> NARROW_READS -> CONTINUE`.

Context compaction is not a task-completion boundary, a reason to abandon an already-determined mutation, or a reason to ask the user to repeat durable state.
<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_END: CONTEXT_READ_BUDGET -->
## 4. CI/status circuit breaker

Ordinary L1/L2/L3 research has **0 routine workflow-status queries**.

CI/status may be read only when:

1. the task is explicitly CI/debug/remote-validation;
2. an actual final merge/promotion attempt is happening now;
3. the user asks for current CI/status;
4. a concrete previously observed CI failure is being diagnosed.

For one unchanged validation object, take at most one status snapshot.

Pending/running status is nonblocking:

`CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK`.

Do not return a pending status and stop when independent/downstream-safe parent work remains.

## 5. Remote-silent research

Between semantic checkpoints:

- 0 routine source writes;
- 0 routine CI/status reads;
- 0 scheduler heartbeat requirements;
- 0 moving-main chasing;
- 0 review polling.

Do not use GitHub as scratchpad state.

Research reasoning and tool-independent work continue normally.

## 6. Semantic checkpoint batching

Publish when a coherent theorem/counterexample/tool/artifact checkpoint, handoff, loss-risk boundary, user request or promotion payload exists.

At one checkpoint:

1. batch related changes;
2. publish/update the owner branch once;
3. create/update at most one Draft PR for the bounded owner generation when useful;
4. terminate the remote publication subflow;
5. **resume the parent research/Driver/user objective in the same turn unless that parent objective is complete.**

Freeze:

`CHECKPOINT_PERSISTED -> RESUME_PARENT_TASK`.

Generated artifacts additionally follow `docs/ARTIFACT_PUBLICATION_LIVENESS.md`.

## 7. PR lifecycle

For L1/L2/L3:

- normally one branch + at most one Draft PR per bounded owner generation;
- do not create a PR for every minor stage/diagnostic;
- do not toggle ready merely to trigger CI;
- report local/executable evidence honestly.

A PR metadata boundary is not a conversational stop point. If the next authorized action is already determined, take it in the same turn.

## 8. Promotion liveness

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 remains serialized as one bounded active promotion attempt at a time.

An actual attempt uses only the bounded current-main/conflict/head/final-combination checks defined by current governance.

Strict `NO_NEW_MATHEMATICS` governance maintenance follows `docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`.

When an attempt ends in merge/defer/failure, release the remote subflow and resume the parent objective. Do not wait for user `继续` if the parent task still has an executable next action.

## 9. Coordination compression

Scheduler, Relay, Foundation, PR and journal have separate functions. Do not duplicate the same progress packet across all surfaces.

GLOBAL_KNOWLEDGE append-only journaling is a separate loss-prevention channel.

## 10. Remote operation defaults

- explicit TASK startup: `<= 3` routine source reads before work;
- ordinary L1/L2/L3: `0` routine source writes, `0` CI/status reads;
- checkpoint: one bounded publication batch, then resume parent task;
- allowed CI/validation: one snapshot per unchanged validation object;
- promotion: one bounded attempt, then release and resume parent task.

Remote/tool limitations are performance signals, not mathematical `HARD_BLOCK`s.

## 11. Current-only policy surface

This file describes current remote behavior only. Historical policy provenance remains in Git history.