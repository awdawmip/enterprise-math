# Enterprise Math GitHub Interaction Budget

Status: `ACTIVE / CANONICAL REMOTE-LIVENESS OVERRIDE`  
Effective: 2026-08-10  
Scope: repository reads, GitHub connector/API use, branch/PR publication, Issue coordination, CI invocation, and L4 promotion.

This protocol is a performance/liveness correction. Where older preflight, scheduler, Relay, PR, CI, or promotion wording can be read as requiring routine GitHub activity during every research step, **this later and narrower remote-liveness rule controls**.

It does not weaken theorem ownership, owner isolation, result conservation, final canonical gates, security, or the four-field mathematical/research `HARD_BLOCK` contract.

## 1. Core invariant

> **Research is hot-path work; GitHub is a sparse persistence and integration boundary.**

GitHub is not the research runtime bus. A repository read/write, PR mutation, Issue comment, workflow inspection, or current-main refresh must answer a concrete question that cannot be answered from the already-loaded task packet.

For L1/L2/L3 research, the default execution mode is `REMOTE_SILENT` between semantic checkpoints.

## 2. Task-classified preflight

Do not execute a universal repository checklist mechanically.

### 2.1 Explicit current user task

For an explicit task, the default Enterprise Math startup packet is only:

1. this operating contract / `AGENTS.md` if not already loaded;
2. **one** common router: prefer `research_common_surface.json` for machine routing or `docs/RESEARCH_COMMON_SURFACE.en.md` for human theorem context; do not read both by default;
3. the exact task-relevant canonical theorem/spec/code/test/Lean files needed to begin.

Research starts once that packet is sufficient. The following are conditional, not universal startup reads:

- `research_scheduler.json` / Issue #240: only for auto-dispatch, scheduler reconciliation, or an actual scheduler event;
- `docs/RESEARCH_SCHEDULING_PROTOCOL.*`: only when dispatch/dependency/handoff semantics are material beyond the compact rules already carried by `AGENTS.md`;
- `docs/RESEARCH_OWNER_ISOLATION.*`: when creating/reconciling a branch, auditing scope, or promoting;
- `docs/PROBLEM_STATUS.*`: when numbered status/canonical scope/promotion is material;
- Relay Issue #82: when a relevant WIP result is needed, or before publishing a reusable cross-route result;
- Foundation Issue #164 / steward/backflow files: only for foundation-facing work;
- `docs/LEAN_DIAGNOSTIC_LIVENESS.md`: only for Lean diagnosis/import/root-registration work.

### 2.2 Automatic dispatch

When the user has not selected a task and automatic dispatch is actually needed, load the scheduler packet required to select a frontier. Scheduler writes remain best-effort and non-blocking under `docs/RESEARCH_SCHEDULER_NONBLOCKING_STARTUP.md`.

### 2.3 Cache/reuse rule

Within one uninterrupted execution phase, an already-fetched immutable file/blob/SHA/PR/Issue snapshot is reused. Do not refetch the same object merely to feel current. Refresh only when a new SHA/event is known, the current action genuinely depends on fresh remote state, or the user explicitly requests current status.

A practical soft budget for an explicit-task startup is **at most three Enterprise Math GitHub reads before substantive work begins**. Exceeding this budget requires a concrete unresolved dependency, not general caution.

## 3. Local-first / connector-only modes

### 3.1 When a local checkout exists

Use local `git`, file reads/search, local tests, and local Lean/module diagnosis for the hot path. GitHub is used for publication, PR/Issue coordination, and remote-only evidence.

Do not call GitHub to read a file already present at the required commit in the local checkout.

### 3.2 Connector-only execution

When no usable local checkout exists, assemble the smallest remote task packet once, then reason/work from it. Avoid file-by-file exploratory browsing after the relevant object is already known.

For a multi-file checkpoint, batch the semantic change. Prefer one commit/ref update when the available connector can express the batch; do not manufacture one remote commit per diagnostic edit merely because the contents API is convenient.

## 4. Remote-silent research phase

Between semantic checkpoints, routine L1/L2/L3 work performs **zero GitHub writes by default**.

Do not use GitHub for:

- scratchpad/proof-search state;
- every small code or import edit;
- routine scheduler heartbeats;
- repeated PR-body progress narration;
- repeated Relay fan-out to several downstream PRs/issues;
- workflow status waiting;
- repeated current-main checks while owner research is legitimately behind main.

Keep branch-local/local/session state until there is something worth persisting.

A hard session boundary or loss-risk may justify a checkpoint; persistence should protect work, not dictate the cadence of thought.

## 5. Semantic checkpoint batching

A `SEMANTIC_CHECKPOINT` is reached when at least one of these holds:

- a theorem/counterexample/tool result forms a coherent reusable unit;
- the user asked for publication/persistence;
- the session is ending and unpushed work would otherwise be at risk;
- a handoff requires another executor to resume from exact artifacts;
- an owner payload is being frozen for validation/promotion.

At one checkpoint:

1. batch related file changes into one publication operation / compact commit set;
2. push/update the owner branch once;
3. create or update **at most one Draft research PR** for that owner generation when a PR is useful;
4. emit at most one coordination packet by default (Relay **or** scheduler handoff/progress as appropriate), not one comment per affected route;
5. stop remote activity and return to research.

Intermediate local commits are allowed. Remote publication need not mirror local commit frequency.

## 6. PR lifecycle: one owner generation, one Draft PR

For L1/L2/L3:

- one bounded owner generation normally has one branch and at most one Draft PR;
- do not create a new PR for every theorem, stage number, diagnostic, or test checkpoint;
- start a new generation only when owner/scope genuinely changes, a frozen payload must separate from continuing research, or the existing review surface has become semantically unmanageable;
- research PRs stay **Draft by default**. Do not toggle ready-for-review merely to obtain CI, then convert back to Draft;
- GitHub Actions are not required to continue research. Record local/executable evidence honestly and defer repository-wide gates to the promotion/validation boundary.

Existing historical/stacked PRs remain provenance; this rule prevents new churn rather than rewriting history.

## 7. CI is an acceptance boundary, not a research service

Existing repository workflows already skip strict jobs on Draft PRs. Use that design intentionally.

- L1/L2/L3 research PR: Draft, no routine full-repository CI.
- Dedicated validation slice: use only when remote validation is itself the declared bounded task and local verification cannot answer it.
- L4 integration / final governance release: ready-for-review and subject to applicable final gates.
- `main`: canonical post-merge validation as configured.

Do not use `ready_for_review` as an ad-hoc remote test button for every research edit.

Pending CI follows the one-snapshot/no-polling rule. A failing CI permits one targeted diagnostic pass; after a semantic fix produces a new SHA, a new validation run is a new object.

## 8. Single active L4 promotion lane

Canonical promotion is already serialized mathematically; the repository control plane must reflect that.

By default there is **one active ready-for-review L4 promotion lane for the repository**.

- A promotable owner payload may be frozen and queued without opening another active L4 PR.
- Open/create the L4 integration only when the promotion lane is available and the source payload is frozen.
- At admission: refresh current `main` once, replay the frozen payload once, inspect concurrent integration/governance conflicts once, and publish the frozen L4 head.
- Run the applicable final gates on that exact head.
- If `main` moves for unrelated reasons while gates run, do not chase it continuously. Perform the existing final current-main combination check only when the merge action is actually being attempted.
- A genuine file/semantic conflict may require a new L4 head; unrelated main movement does not create a new research generation.

Urgent repository-liveness/security fixes may bypass the queue as exceptional governance work, but that exception must not become a permanent second lane.

## 9. Coordination compression

Issue #240, Relay #82, Foundation #164, PR bodies, and comments are different views of coordination, not requirements to duplicate the same event everywhere.

- Scheduler: executor/frontier/handoff only.
- Relay: reusable cross-route mathematical result/counterexample only.
- Foundation: unresolved foundation question / steward verification only.
- PR: exact artifact/review surface only.

Publish one authoritative packet and link/reuse it elsewhere only when a consumer genuinely needs the reference. Do not fan out identical prose across multiple GitHub surfaces.

## 10. Global-knowledge batching boundary

High-frequency project WIP does not require a second GitHub transaction in the account-level knowledge repository after every micro-stage.

GLOBAL_KNOWLEDGE write-back is preferred at durable semantic boundaries: canonical promotion, a meaningful generation freeze/handoff, a governance decision, an explicit user request, or another cross-session fact whose loss would materially impair future work. Coalesce several related WIP updates into one durable record/update when practical.

This does not weaken the global repository's own mandatory refresh/concurrency protocol when a write is actually performed.

## 11. Remote operation budget

Budgets are liveness defaults, not correctness ceilings:

- explicit-task startup: <= 3 routine Enterprise Math GitHub reads before substantive work;
- active research between checkpoints: 0 routine GitHub writes and 0 status polls;
- semantic checkpoint: 1 batched branch publication + at most 1 Draft PR mutation + at most 1 coordination write by default;
- unchanged workflow/PR/Issue object: 1 status snapshot per uninterrupted execution phase;
- promotion: one current-main admission refresh, one conflict snapshot, one frozen-head validation cycle, one final merge-time current-main check.

If a budget is exceeded, state the concrete evidence dependency being resolved. `REMOTE_BUDGET_EXCEEDED` is a performance signal, never a mathematical `HARD_BLOCK`.

## 12. What remains strict

Sparse synchronization does **not** authorize:

- bypassing required final repository protections;
- merging unreviewed/conflicting L4 payloads;
- force-pushing/destructive history rewriting;
- weakening theorem status discipline;
- erasing source provenance or result-conservation obligations;
- duplicating another owner's theorem simply to avoid one necessary read.

The intended lifecycle is:

`small task packet -> remote-silent research -> semantic checkpoint batch -> Draft owner record -> frozen payload queue -> one L4 lane -> final gates -> main`.

---

# 进取数论 GitHub 交互预算

状态：`ACTIVE / CANONICAL REMOTE-LIVENESS OVERRIDE`  
生效：2026-08-10

核心规则只有一句：**研究是热路径，GitHub 是稀疏持久化与最终集成边界，不是研究运行时总线。**

对于用户明确指定的任务，默认启动只读取：本执行规则、`research_common_surface.json` 或人类版 Common Surface 二选一、以及真正与任务有关的定理/代码/测试文件。scheduler、Issue #240、Relay #82、`PROBLEM_STATUS`、Foundation Issue #164、owner-isolation 等都改为按任务需要读取，而不是每次启动全扫。显式任务在开始实质工作前，Enterprise Math GitHub 常规读取软预算为 **不超过 3 次**。

L1/L2/L3 研究阶段默认 `REMOTE_SILENT`：证明搜索、小修小改、import 诊断、普通心跳、PR 进度叙述、CI 状态检查、追逐 moving main 都不应产生常规 GitHub 写操作。只有形成语义 checkpoint、需要 handoff、防止成果丢失、用户明确要求发布、或者冻结 payload 准备 promotion 时，才批量持久化。

一个 owner generation 默认只保留一个 branch 和至多一个 **Draft PR**。不得为了获得 CI 把研究 PR 反复切成 ready-for-review。已有 workflow 会跳过 Draft PR 的严格任务，应主动利用这一点。完整 CI 主要属于 L4/最终治理/main 验收边界，而不是研究服务。

Canonical promotion 已经是串行过程，因此控制面也默认只允许 **一个 active ready-for-review L4 promotion lane**。其他成熟 payload 先冻结排队，不提前开多个 L4 PR。轮到时只做一次 current-main admission、一次冲突快照、一次 frozen-head gate，再在真正 merge 时做一次最终 current-main combination check；不得持续追逐 main。

Issue #240 只管调度，Relay #82 只管跨路线数学结果，Foundation #164 只管基础问题，PR 只管 artifact/review。不要把同一进度复制粘贴到所有 GitHub 表面。

GLOBAL_KNOWLEDGE 也按 durable semantic boundary 批量回写，不再为项目每一个微小 WIP stage 额外制造第二套 GitHub 事务；真正回写时仍严格遵守其自身最新 main 刷新和并发规则。

默认远端预算：显式任务启动 <=3 次项目 GitHub 常规读取；两个 checkpoint 之间 0 常规写、0 状态轮询；一次 checkpoint 默认 1 次批量 branch publication + 至多 1 次 Draft PR mutation + 至多 1 次协调写；同一未变化对象每连续执行阶段只看一次状态。超预算必须对应一个具体证据依赖，而不能只是“保险起见”。