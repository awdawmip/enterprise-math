# Enterprise Math Research Scheduler V2 — Non-Blocking Startup Addendum

Status: `ACTIVE / CANONICAL V2 LIVENESS ADDENDUM`  
Effective: 2026-08-24  
Scope: task registration, claims, review claims, orphan recovery, runtime event publication, session handoff, and CI/review polling liveness.

This addendum refines `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md` / `.zh-CN.md`. It preserves the rule that bookkeeping must not stall mathematical work while also enforcing the V2 invariant that **every task identity must enter the registry or orphan ledger**.

It does not change theorem ownership, research scope, canonical promotion, L4 replay, or the four-field mathematical/research `HARD_BLOCK` contract.

## Canonical V2 invariant

**The scheduler coordinates research; it never certifies truth. But a task-like object may not remain intentionally invisible to the scheduler.**

Freeze:

`ALL_TASK_IDENTITIES -> V2_REGISTRY_OR_ORPHAN_LEDGER`.

`SCHEDULER_UNAVAILABLE -> REGISTER_PENDING_NONBLOCKING`, not silent unregistered execution.

`TASKBOOK_POLICY_PASS != SCHEDULER_READY`.

`PUBLISH != READY`.

`SUBMIT != DONE`.

`LEASE_EXPIRY -> ORPHANED`.

## New-conversation startup

1. An explicit current user task controls the mathematical scope. If it is already a registered Scheduler V2 task, use its current state; if it is a genuinely new task, register/publish it as soon as the non-blocking scheduler write path is available.
2. With no user-selected task, materialize `research_scheduler.json` plus current Issue #240 V2 events and select only an eligible `NEEDS_DISPATCH` task.
3. When Issue #240 is readable/writable, a selected scheduled task must be `CLAIM`ed before it is treated as the active scheduled owner. An orphan must be `ADOPT`ed rather than ordinary-claimed.
4. A FREE researcher is excluded from automatic claiming but may publish a concrete post-freeze proposal into `REVIEW_PENDING`.
5. If the scheduler connector is temporarily unavailable, substantive reasoning may continue under `REGISTER_PENDING_NONBLOCKING`, but the work is **not an official live scheduler claim** and may not be represented as `READY`, `CLAIMED`, `DONE`, or canonical task ownership.
6. As soon as the scheduler path is restored, the first coordination action is to register/reconcile the task using the normal V2 event or, only for genuine pre-V2/cutover work, Driver `MIGRATE`. Do not deliberately continue a hidden task after the write path is available.
7. Do not ask the user to act as the routing bus merely because a scheduler write failed.

## Successfully published claims and review claims

After a `CLAIM`, `ADOPT`, or `REVIEW_CLAIM` is published, reduce the event stream through that event. Use the lease only if it is the accepted live claim. If another accepted claim won, select another eligible item or follow the explicit handoff/review route.

A publication or return review without a live `REVIEW_CLAIM` is not valid V2 review authority.

## Register-pending safety

A `REGISTER_PENDING_NONBLOCKING` session must still obey theorem ownership, owner isolation, scope, and evidence rules.

Before publishing persistent research results, freezing a task return, or claiming completion, scheduler registration/reconciliation must be attempted whenever the connected path is available. If a conflicting live claim becomes visible, preserve the mathematics but reroute the contribution as evidence, a non-conflicting owner-local result, or an explicit Driver-reviewed recovery path.

`REGISTER_PENDING_NONBLOCKING` is a temporary transport degradation state, not a second scheduler.

## Progress, submit, handoff, and orphan behavior

- with a live execution lease, publish `PROGRESS` / `HEARTBEAT` when useful and non-blocking;
- an unfinished session may `HANDOFF` with a concrete `next_action`;
- successful task completion emits `SUBMIT`, not V2 `DONE`;
- a return closes only after a different Driver's `REVIEW`;
- if a live claim expires, V2 records `ORPHANED`; it does not silently become `HANDOFF_READY`;
- resume an orphan with `ADOPT` and a recovery ref;
- temporary event-write failure must not be described as a mathematical `HARD_BLOCK`.

## CI, workflow, review, and concurrent-governance polling liveness

Workflow and review status reads are snapshots, not wait operations.

1. For an unchanged commit, workflow run, or concurrent-PR set, take at most one routine status snapshot in one uninterrupted execution phase. If the relevant state is `queued`, `pending`, `requested`, or `in_progress`, record the pending state and stop checking that unchanged object.
2. Never sleep, back off, retry, recursively refresh, or repeatedly call workflow/commit/PR status APIs merely to see whether a pending state has changed.
3. A concurrent-governance audit is likewise one snapshot: identify actual semantic/file conflicts and continue. Do not repeatedly rescan the same set waiting for review, CI, merge, or branch movement.
4. Recheck is allowed after a materially new observable input: new commit SHA, new workflow run ID, surfaced completion/failure event, an explicit user refresh request, or a later user turn/session where current status is again necessary.
5. Required CI/review may block the specific merge or promotion action. It does not block research, analysis, local validation, task registration, return preparation, or the user-facing response.
6. A newly observed failure permits one targeted diagnostic read; it does not restore polling loops.

## What is not a mathematical `HARD_BLOCK`

The following are never mathematical/research hard-block reasons:

- GitHub Issue #240 read/write failure;
- connector or tool unavailability;
- interactive workflow/approval requirements;
- rate limiting, network failure, or timeout;
- inability to post a V2 coordination event at that moment;
- pending/running CI, workflow, review, or concurrent-governance state.

These conditions may create `REGISTER_PENDING_NONBLOCKING`, `CI_PENDING`, or another workflow state. They do not change mathematical truth or the four-field `HARD_BLOCK` contract.

## Unchanged boundaries

This addendum does not relax owner isolation, unique mother-theorem ownership, common-surface/Relay propagation, L4 `NO NEW MATHEMATICS`, canonical promotion gates, or repository checks actually required for merge.

---

# 进取数论研究状态机 V2——非阻塞启动补充协议

状态：`ACTIVE / CANONICAL V2 LIVENESS ADDENDUM`  
生效：2026-08-24

本补充协议同时冻结两件事：**记账不能卡住数学研究；任务也不能故意长期游离在状态机之外。**

核心不变量：

`所有任务身份 -> V2 注册表或孤儿登记`。

`状态机暂时不可用 -> REGISTER_PENDING_NONBLOCKING`，而不是无登记研究。

`任务书 policy PASS != READY`；`PUBLISH != READY`；`SUBMIT != DONE`；`lease 到期 -> ORPHANED`。

## 新对话

1. 用户明确指定任务时，数学 scope 以用户指令为准；已有 V2 任务先读取当前状态，新任务则在非阻塞写路径可用时立即登记/发布。
2. 用户没有指定任务时，只能从 V2 物化结果中的 `NEEDS_DISPATCH` 领取。
3. Issue #240 可读写时，scheduled task 必须成功 `CLAIM` 后才算当前 scheduler owner；孤儿必须 `ADOPT`，不能普通 `CLAIM`。
4. FREE 研究员不参与自动领取，但在相应发现冻结之后可以把具体任务建议 `PUBLISH` 到 `REVIEW_PENDING`。
5. 如果状态机连接临时不可用，可以继续实质推理，但必须明确处于 `REGISTER_PENDING_NONBLOCKING`；此时不得声称任务已经 `READY`、`CLAIMED` 或 `DONE`。
6. 写路径恢复后，第一项控制动作就是登记/对账；只有真正属于 V2 上线时已经在运行的旧任务，才允许 Driver 使用一次性 `MIGRATE`。
7. 不得因为状态机写失败而要求用户在不同对话之间人工搬运任务和 return。

## Claim、Review 与孤儿

`CLAIM`、`ADOPT`、`REVIEW_CLAIM` 发布后必须按事件流重新归约，只使用被状态机接受的 live lease。

发布审核和 return 审核都必须先有 review lease；发布者不得审核自己的发布，执行者不得审核自己的 return。

任务完成使用 `SUBMIT`，之后进入 `RETURN_REVIEW`；只有另一名 Driver 的 `REVIEW` 才能把调度任务关闭。

执行 lease 到期后留下持久 `ORPHANED` 记录，不再无痕变回 `HANDOFF_READY`；恢复时必须 `ADOPT` 并携带 recovery ref。

## CI / workflow / review 轮询

对同一个未变化对象默认只做一次状态快照；pending/running 后停止刷新。禁止 sleep、退避、递归刷新或连续查询同一 commit/run/PR 只为等状态变化。只有出现新的 SHA、run ID、已浮现的完成/失败事件、用户明确要求刷新，或后续新回合确有必要时才重新查询。

CI/review 可以阻止具体 merge/promotion，但不能把数学研究、状态机登记、return 准备或用户回复变成等待循环。

## HARD_BLOCK 边界

Issue #240 读写失败、connector 不可用、限流、超时、工作流 pending 都不是数学 `HARD_BLOCK`。它们只能产生 `REGISTER_PENDING_NONBLOCKING`、`CI_PENDING` 等工作流状态，不改变数学真值，也不改变四字段 HARD_BLOCK 契约。
