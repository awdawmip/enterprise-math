# Enterprise Math Research Scheduler — Non-Blocking Startup Addendum

Status: `ACTIVE / CANONICAL STARTUP OVERRIDE`  
Effective: 2026-08-10  
Scope: new-conversation dispatch, scheduler claims, runtime event publication, session handoff, and CI/review polling liveness.

This addendum is a narrow liveness correction to `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md` / `.zh-CN.md`. Where Sections 8.2–8.5 of that protocol can be read as requiring a GitHub Issue #240 write before research may start or before a user-facing response may finish, **this later and narrower addendum controls**. It also controls any execution pattern that turns workflow, CI, review, or concurrent-governance status inspection into a synchronous wait loop.

It does not change theorem ownership, research scope, canonical promotion, L4 replay, or the four-field mathematical/research `HARD_BLOCK` contract.

## Canonical invariant

**The scheduler coordinates research; it never grants permission to research. Status inspection observes external state; it never becomes a wait primitive.**

Issue #240, `CLAIM`, `PROGRESS`, `HEARTBEAT`, and `HANDOFF` are coordination signals. They are not startup transactions, workflow gates, or prerequisites for replying to the user.

## New-conversation startup

1. An explicit current user task always overrides automatic dispatch and starts without any scheduler write.
2. With no user-selected task, a new research conversation should read `research_scheduler.json` and reduce live Issue #240 events when they are available through a non-blocking read path.
3. If Issue #240 cannot be read, use the static canonical scheduler frontier and the same deterministic ranking policy. Read unavailability is a coordination degradation, not a blocker.
4. After selecting an owner-scoped frontier, research may begin immediately. **No `CLAIM` is required before substantive task-specific work.**
5. A `CLAIM` may be posted only when the Issue #240 write path is immediately available without interactive workflow/approval. If the write is unavailable, errors, times out, is rate-limited, or requires user interaction, skip the write and continue unleased.
6. Do not retry, wait, or ask the user for confirmation solely to obtain scheduler bookkeeping.

## Successfully published claims

If a `CLAIM` is successfully published, the normal race rule still applies: re-read Issue #240 through the new event and use the lease only if that `claim_id` is the winning live claim. If another published claim won first, choose the next eligible frontier.

This race rule applies to published claims only. Failure to publish a claim does not revoke the right to continue owner-scoped research.

## Unleased research safety

An unleased session must still obey theorem ownership, owner isolation, common-surface reuse, and scope rules.

Before publishing persistent results from an unleased session, refresh the dispatch board when practical. If a newly visible live lease overlaps the same frontier, preserve the work but re-route it as a non-conflicting owner-local result, a `TEST`/Relay contribution, or another valid scope. Do not discard mathematics and do not stop the user-facing conversation merely because a lease appeared.

## Progress and handoff

Runtime event writes are best-effort coordination:

- publish `PROGRESS` / `HEARTBEAT` when a live claim exists and the write path is non-blocking;
- publish `HANDOFF` before leaving an unfinished live claim when the write path is non-blocking;
- if scheduler writes are unavailable or require interaction, complete the user-facing response normally, preserve a concrete `next_action` in the available branch/PR/Relay/output, and allow any live lease to expire naturally;
- scheduler publication must never delay or block user-facing completion.

## CI, workflow, review, and concurrent-governance polling liveness

Workflow and review status reads are snapshots, not wait operations.

1. For an unchanged commit, workflow run, or concurrent-PR set, take at most **one routine status snapshot in one uninterrupted execution phase**. If the relevant state is `queued`, `pending`, `requested`, or `in_progress`, record `CI_PENDING` (or the corresponding review-pending state) and stop checking that unchanged object.
2. **Never sleep, back off, retry, recursively refresh, or repeatedly call workflow/commit/PR status APIs merely to see whether a pending state has changed.** In particular, repeated `Checking workflow run status for commit` / `Fetching` cycles are a protocol violation.
3. `Reviewing Concurrent Governance Pull Requests` is likewise a one-snapshot conflict audit. Inspect the currently visible concurrent PR set once, classify actual file/semantic conflicts, and continue. Do not repeatedly rescan the same PR set waiting for reviews, CI, merges, or branch movement to settle.
4. Recheck is allowed only after a materially new observable input exists: a new commit SHA, a new workflow run ID, an already-surfaced completion/failure event, an explicit current user request to refresh status, or a later user turn/session resumption where current status is again necessary.
5. Required CI/review may prevent the specific **merge or canonical-promotion action** from executing. It does not block research, analysis, drafting, local validation, branch work, or the user-facing response. If merge/promotion is the only remaining action and its required checks are pending, report `CI_PENDING` and finish the current response instead of polling.
6. A newly observed **failure** is different from a pending state: one targeted log/failure inspection is allowed to diagnose the failure. That diagnostic allowance does not authorize repeated status polling.
7. Moving `main` or an unrelated concurrent governance PR does not reset the polling budget by itself. Only a new object relevant to the current action (for example a new head SHA or new run ID) does.

## What is not a `HARD_BLOCK`

The following are never valid mathematical/research `HARD_BLOCK` reasons:

- GitHub Issue #240 read/write failure;
- connector or tool unavailability;
- an interactive workflow/approval requirement;
- rate limiting, network failure, or timeout;
- inability to post `CLAIM`, `PROGRESS`, `HEARTBEAT`, or `HANDOFF`;
- pending/running CI, workflow, review, or concurrent-governance status;
- CI/review/moving-main conditions already excluded by the scheduling protocol.

Only the existing complete four-field missing-object/owner/necessity/unblock-condition record may stop a research route.

## Unchanged boundaries

This addendum does not relax:

- L1/L2/L3 owner isolation;
- unique mother-theorem ownership;
- reusable-result propagation through the common surface/Relay;
- L4 `NO NEW MATHEMATICS`;
- final current-main combination gates for canonical promotion;
- required repository checks before a merge when repository protection actually requires them.

---

# 进取数论研究调度器——新对话非阻塞启动补充协议

状态：`ACTIVE / CANONICAL STARTUP OVERRIDE`  
生效：2026-08-10  
范围：新对话自动调度、scheduler claim、运行时事件发布、会话 handoff，以及 CI/review 轮询活性。

本补充协议只修正 `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md` / `.zh-CN.md` 第 8.2–8.5 节可能形成的启动阻塞语义。凡旧条文可能被理解为“必须先向 GitHub Issue #240 写入事件，才能开始研究或结束用户回复”，**均以本补充协议这一更晚、范围更窄的规则为准**。任何把 workflow、CI、review 或并发治理状态检查变成同步等待循环的执行方式，也由本补充协议约束。

本协议不改变定理归属、研究 scope、canonical promotion、L4 replay，也不改变四字段数学/研究 `HARD_BLOCK` 契约。

## 规范不变量

**scheduler 只协调研究，不授予研究许可；状态检查只观察外部状态，不得成为等待原语。**

Issue #240、`CLAIM`、`PROGRESS`、`HEARTBEAT`、`HANDOFF` 都只是协调信号，不是启动事务、workflow 门禁，也不是向用户回复的前置条件。

## 新对话启动

1. 用户当前显式指定的任务始终覆盖自动调度，且无需任何 scheduler 写操作即可开始。
2. 如果用户没有指定任务，新研究对话应读取 `research_scheduler.json`；Issue #240 能通过非阻塞读取路径获得时，再归约其 live events。
3. Issue #240 无法读取时，直接使用 canonical 静态 scheduler frontier 与相同的确定性排序策略。读取失败只是协调降级，不是 blocker。
4. 选定 owner-scoped frontier 后，可以立即开始研究。**开始实质性 task-specific 工作前不再强制要求 `CLAIM`。**
5. 只有当 Issue #240 写路径无需交互 workflow/批准且可立即使用时，才发布 `CLAIM`。如果写入不可用、报错、超时、限流或需要用户交互，跳过写入并以 unleased 模式继续。
6. 不得仅为了 scheduler 记账而重试、等待或要求用户确认。

## 已成功发布的 claim

如果 `CLAIM` 已成功发布，原有并发竞争规则继续有效：立即重读 Issue #240，通过新事件重新归约；只有该 `claim_id` 是胜出的 live claim 时才按该 lease 执行。若另一条已发布 claim 更早获胜，则选择下一个 eligible frontier。

该竞争规则只约束已经成功发布的 claim。发布失败不剥夺继续 owner-scoped 研究的资格。

## Unleased 研究的安全边界

Unleased 会话仍必须遵守 theorem ownership、owner isolation、common-surface 复用与 scope 规则。

在发布持久化成果前，应在现实可行时刷新 dispatch board。如果此时发现新的 live lease 与本 frontier 重叠，应保留已经完成的工作，并将其重新路由为不冲突的 owner-local 结果、`TEST`/Relay 证据或其他合法 scope；不得丢弃数学成果，也不得因为 lease 出现而卡住用户对话。

## Progress 与 handoff

运行时事件写入属于 best-effort 协调：

- 有 live claim 且写路径非阻塞时，发布 `PROGRESS` / `HEARTBEAT`；
- 未完成的 live claim 会话退出前，写路径非阻塞时发布 `HANDOFF`；
- scheduler 写不可用或需要交互时，正常完成用户回复，把具体 `next_action` 保存在可用 branch/PR/Relay/output 中，并允许 live lease 自然到期；
- scheduler 事件发布不得延迟或阻断用户可见的任务完成。

## CI、workflow、review 与并发治理轮询活性

Workflow 与 review 状态读取是一次性快照，不是等待操作。

1. 对同一个未变化的 commit、workflow run 或并发 PR 集合，在一次连续执行阶段中默认最多进行 **一次常规状态快照**。如果相关状态为 `queued`、`pending`、`requested` 或 `in_progress`，记录 `CI_PENDING`（或相应 review-pending 状态）后停止检查该未变化对象。
2. **绝不能仅为了观察 pending 状态是否变化而 sleep、退避、重试、递归刷新，或反复调用 workflow/commit/PR 状态 API。**尤其是连续出现 `Checking workflow run status for commit` / `Fetching` 的循环，属于协议违规。
3. `Reviewing Concurrent Governance Pull Requests` 同样只能作为一次性冲突快照：对当前可见的并发 PR 集合检查一次，识别真实文件/语义冲突后继续。不得为了等待 review、CI、merge 或 branch movement 稳定而反复扫描同一 PR 集合。
4. 只有出现实质性的新可观察输入时才允许重新检查：新的 commit SHA、新的 workflow run ID、已经浮现的完成/失败事件、用户当前明确要求刷新状态，或后续新的用户回合/恢复会话确实再次需要当前状态。
5. 必需的 CI/review 可以阻止具体的 **merge 或 canonical-promotion 动作**执行，但不能阻止研究、分析、写作、本地验证、branch 工作或用户可见回复。如果 merge/promotion 已是唯一剩余动作而检查仍 pending，记录 `CI_PENDING` 并结束当前回复，禁止继续轮询。
6. 新观察到的 **failure** 与 pending 不同：允许针对失败额外读取一次日志/失败信息以定位原因；该诊断许可不允许恢复重复状态轮询。
7. `main` 移动或无关并发治理 PR 本身不会重置轮询预算。只有与当前动作相关的新对象（例如新的 head SHA 或新的 run ID）才会重置。

## 哪些绝不是 `HARD_BLOCK`

以下情况绝不能作为数学/研究 `HARD_BLOCK`：

- GitHub Issue #240 读写失败；
- connector 或工具不可用；
- 需要交互式 workflow/批准；
- 限流、网络失败或超时；
- 无法发布 `CLAIM`、`PROGRESS`、`HEARTBEAT` 或 `HANDOFF`；
- pending/running 的 CI、workflow、review 或并发治理状态；
- 调度协议已经排除的 CI/review/moving-main 条件。

只有原有完整四字段 missing-object / owner / necessity / unblock-condition 记录才允许真正停止研究路线。

## 不变边界

本补充协议不放松：

- L1/L2/L3 owner isolation；
- 母定理唯一归属；
- 通过 common surface / Relay 传播可复用结果；
- L4 `NO NEW MATHEMATICS`；
- canonical promotion 前针对 current `main` 的最终 combination gate；
- 仓库保护规则确实要求时，merge 前必须满足的 repository checks。
