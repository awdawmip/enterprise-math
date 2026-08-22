# Enterprise Math GitHub Interaction Budget

Status: `ACTIVE / CANONICAL REMOTE-LIVENESS OVERRIDE`
Effective: `2026-08-22`
Scope: repository reads, GitHub connector/API use, branch/PR publication, Issue coordination, CI and promotion.

## 1. Core invariant

> **Research is the hot path; GitHub is a sparse remote persistence/integration boundary.**

Ordinary L1/L2/L3 research is `REMOTE_SILENT` between semantic checkpoints.

## 2. ChatGPT GitHub route

In ChatGPT/Project execution, when the connected GitHub capability is available:

`CONNECTED_GITHUB_PLUGIN = PRIMARY_REMOTE_GITHUB_PATH`.

Use the GitHub connector/plugin for:

- repository file reads/search;
- commits/branches;
- PRs/issues/comments;
- allowed workflow/status operations.

Do not use ChatGPT/container networking to `git clone`, curl/fetch GitHub, or read `raw.githubusercontent.com` when the connected capability supports the required action.

A local checkout may be used for **local execution** only when already available: file processing, tests, Lean/module diagnosis, generated artifacts, etc. It is not the fallback transport for remote GitHub retrieval/synchronization.

If a local/container GitHub network route is known unavailable, do not retry it later and do not keep reporting the same environment failure. Only a failure of the connected GitHub route that prevents the requested operation is a remote-access issue worth surfacing.

## 3. Startup read budget

Do not execute a universal repository preflight.

For an explicit TASK_RESEARCH task, normal remote startup is:

1. `AGENTS.md` if needed;
2. exact task entry;
3. first exact dependency needed to start.

Soft budget: `<= 3` routine source reads before substantive work.

FREE Phase A follows its primitive-substrate route and does not preload current-result/project-control catalogs.

Reuse immutable fetched blobs/SHAs within one execution phase.

## 4. CI circuit breaker

Ordinary L1/L2/L3 research has **0 routine workflow-status queries**.

CI/status may be read only when:

1. the task is explicitly CI/debug/remote-validation;
2. an actual final merge/promotion attempt is happening now;
3. the user asks for current CI/status;
4. a concrete previously observed CI failure is being diagnosed.

For one unchanged validation object, take at most one status snapshot.

Pending/running status is nonblocking for research and user-facing completion.

## 5. Remote-silent research

Between semantic checkpoints:

- 0 routine source writes;
- 0 routine CI/status reads;
- 0 scheduler heartbeat requirements;
- 0 moving-main chasing;
- 0 review polling.

Do not use GitHub as scratchpad state.

## 6. Semantic checkpoint batching

Publish when a coherent theorem/counterexample/tool/artifact checkpoint, handoff, loss-risk boundary, user request or promotion payload exists.

At one checkpoint:

1. batch related changes;
2. publish/update the owner branch once;
3. create/update at most one Draft PR for the bounded owner generation when useful;
4. stop remote activity and return to research/finish.

Generated artifacts additionally follow `docs/ARTIFACT_PUBLICATION_LIVENESS.md`.

## 7. PR lifecycle

For L1/L2/L3:

- normally one branch + at most one Draft PR per bounded owner generation;
- do not create a PR for every minor stage/diagnostic;
- do not toggle ready merely to trigger CI;
- report local/executable evidence honestly.

## 8. Promotion liveness

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 remains serialized as one **bounded active promotion attempt** at a time.

An actual attempt uses only the bounded current-main/conflict/head/final-combination checks defined by current governance.

Strict `NO_NEW_MATHEMATICS` governance maintenance follows `docs/GOVERNANCE_MAINTENANCE_LIVENESS.md` and may not smuggle theorem/native-definition/evidence/ownership changes.

## 9. Coordination compression

Scheduler, Relay, Foundation, PR and journal have separate functions. Do not duplicate the same progress packet across all surfaces.

GLOBAL_KNOWLEDGE append-only journaling is a separate loss-prevention channel.

## 10. Remote operation defaults

- explicit TASK startup: `<= 3` routine source reads before work;
- ordinary L1/L2/L3: `0` routine source writes, `0` CI/status reads;
- checkpoint: one bounded publication batch;
- allowed CI/validation: one snapshot per unchanged validation object;
- promotion: one bounded attempt, then release.

Remote/tool limitations are performance signals, not mathematical `HARD_BLOCK`s.

## 11. Current-only policy surface

This file describes current remote behavior only. Older workflow/preflight/lane policies remain in Git history and are not restated here.
