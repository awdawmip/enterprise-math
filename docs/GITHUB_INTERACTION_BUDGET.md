# Enterprise Math GitHub Interaction Budget

Status: `ACTIVE / CANONICAL REMOTE-LIVENESS OVERRIDE`  
Effective: 2026-08-10  
Scope: repository reads, GitHub connector/API use, branch/PR publication, Issue coordination, CI invocation, and L4 promotion.

Post-research artifact/checkpoint publication must additionally follow `docs/ARTIFACT_PUBLICATION_LIVENESS.md`. That supplement is mandatory whenever a semantic checkpoint contains generated artifacts or when publication could involve multiple file/blob/tree operations; its stricter liveness and duplicate-writer rules control that slice.

This protocol is the narrow liveness authority for GitHub interaction. Where older preflight, scheduler, Relay, PR, CI, validation, or promotion wording can be read as requiring routine GitHub activity during research, **this later remote-liveness rule controls**.

It does not weaken theorem ownership, owner isolation, result conservation, security, canonical promotion gates, or the four-field mathematical/research `HARD_BLOCK` contract.

## 1. Core invariant

> **Research is hot-path work; GitHub is a sparse persistence and integration boundary.**

GitHub is not the research runtime bus. For L1/L2/L3, the default source-repository mode is `REMOTE_SILENT` between semantic checkpoints.

### 1.1 Hard CI circuit breaker

For ordinary L1/L2/L3 research, **the allowed routine GitHub workflow-status query budget is ZERO**.

Do **not** enter a step named or equivalent to:

- `Checking CI Workflow Runs`;
- `Checking workflow run status for commit`;
- `Waiting for CI`;
- `Checking whether Actions finished`;
- repeated status/review/current-main refresh.

A semantic checkpoint, branch push, Draft PR update, handoff, or user-facing completion does **not** by itself authorize a workflow-status read.

Workflow/CI status may be queried only when at least one of these is true:

1. the current task is an explicit CI/debugging or remote-validation task;
2. an L4/final-governance merge or canonical-promotion action is actually being attempted now;
3. the user explicitly asks for current CI/workflow status;
4. a previously surfaced CI failure is the concrete object being diagnosed.

If none applies, record:

`CI_NOT_REQUIRED_FOR_RESEARCH`

and continue/finish without calling workflow-run/status APIs.

In an allowed CI context, take at most one status snapshot for the unchanged validation object. `queued`, `pending`, `requested`, or `in_progress` becomes:

`CI_PENDING_NONBLOCKING`

and the CI subflow terminates immediately. No sleep, backoff, retry, recursive refresh, per-run polling, or status fan-out is permitted. Required pending CI may defer only the specific merge/promotion action; it may not defer research, handoff, artifact delivery, or the user-facing response.

This circuit breaker is stronger than older wording that allowed one routine snapshot on arbitrary unchanged objects. For ordinary L1/L2/L3 research, zero workflow-status reads is the rule.

## 2. Task-classified preflight

Do not execute a universal repository checklist mechanically.

For an explicit current user task, the default startup packet is only:

1. `AGENTS.md` / this contract if not already loaded;
2. one common router: normally `research_common_surface.json` **or** `docs/RESEARCH_COMMON_SURFACE.en.md`, not both by default;
3. the exact task-relevant theorem/spec/code/test/Lean files needed to begin.

Research starts once that packet is sufficient. Scheduler, Issue #240, Relay #82, `PROBLEM_STATUS`, owner-isolation, Foundation surfaces, CI surfaces, and governance PRs are conditional reads, not universal startup reads.

Automatic dispatch may load the scheduler packet when no user task is selected. Scheduler writes remain best-effort and non-blocking under `docs/RESEARCH_SCHEDULER_NONBLOCKING_STARTUP.md`.

Within one uninterrupted execution phase, reuse already-fetched immutable blobs/SHAs/PR/Issue snapshots. Do not refetch merely to feel current.

Explicit-task startup soft budget: **<= 3 routine Enterprise Math GitHub reads before substantive work** unless one concrete missing dependency requires more.

## 3. Local-first / connector-only

When a local checkout exists, use local git, file reads/search, tests, and Lean/module diagnosis for the hot path. Do not call GitHub to read files already present at the required commit.

In connector-only execution, assemble the smallest remote task packet once and reuse it. Do not turn remote file browsing into the research loop.

## 4. Remote-silent research phase

Between semantic checkpoints, ordinary L1/L2/L3 work performs:

- 0 routine source-repository writes;
- 0 workflow/CI status queries;
- 0 scheduler heartbeat requirements;
- 0 moving-main chasing;
- 0 review polling.

Do not use the source repository for scratchpad state, every small edit, routine heartbeat bookkeeping, repeated PR narration, repeated Relay fan-out, or workflow waiting.

A hard session boundary or loss-risk may justify a source checkpoint; persistence protects work but does not dictate thought cadence.

GLOBAL_KNOWLEDGE progress journaling is a separate append-only loss-prevention plane and is not counted as Enterprise Math source-repository churn.

## 5. Semantic checkpoint batching

A source `SEMANTIC_CHECKPOINT` exists when a coherent theorem/counterexample/tool artifact is ready, the user asks for persistence, a handoff needs exact artifacts, source work risks loss, or a payload is frozen for validation/promotion.

At one checkpoint:

1. batch related source changes;
2. publish/update the owner branch once;
3. create/update at most one Draft research PR for that owner generation when useful;
4. emit at most one source-control coordination packet by default;
5. stop remote source activity and return to research or finish the handoff.

**Do not check CI merely because a checkpoint was published.**

Generated-artifact publication is further bounded by `docs/ARTIFACT_PUBLICATION_LIVENESS.md`: generate once, check once, take one pre-publication owner-head snapshot, and use the simplest bounded contents/git publication path. Do not optimize a completed result into a long per-blob/minify/chunk/tree choreography, and do not build a duplicate checkpoint after an equivalent same-generation owner head has already advanced.

## 6. PR lifecycle

For L1/L2/L3:

- one bounded owner generation normally has one branch and at most one Draft PR;
- do not create a new PR for every theorem/stage/diagnostic;
- keep research PRs Draft by default;
- do not toggle ready-for-review to obtain CI;
- local/executable evidence is reported honestly; repository-wide validation is deferred to a declared validation/promotion boundary.

## 7. CI is an acceptance boundary, not a research service

- L1/L2/L3 research: Draft PR, **no workflow-status read by default**.
- Dedicated validation task: one frozen validation object, one status snapshot; pending => `CI_PENDING_NONBLOCKING` and return.
- L4/final governance: final gates apply, but status remains snapshot-based and non-blocking for the conversation.
- `main`: canonical post-merge validation remains configured by repository workflows.

A newly observed failure permits one targeted failure/log diagnostic pass. After a semantic fix creates a new SHA, that new SHA is a new validation object. Failure diagnosis does not authorize polling.

## 8. Single active L4 promotion lane

Canonical promotion is serialized. Default to one active ready-for-review L4 lane.

Other mature payloads freeze/queue. At L4 admission perform one current-main refresh, one conflict snapshot, one frozen-head validation cycle, and one final current-main combination check only when merge is actually attempted.

Unrelated movement of `main` does not trigger continuous refresh or replay. A genuine semantic/file conflict may require a new L4 head.

Urgent repository-liveness/security fixes may bypass the normal lane as exceptional governance maintenance.

## 9. Coordination compression

- Scheduler / Issue #240: executor/frontier/handoff only.
- Relay #82: reusable cross-route mathematical results/counterexamples.
- Foundation #164: unresolved foundation questions/steward verification.
- PR: exact artifact/review surface.

Do not duplicate the same progress packet across all surfaces.

## 10. GLOBAL_KNOWLEDGE exception

GLOBAL_KNOWLEDGE has a separate mission: **do not lose research/process progress**.

Append-only progress events may be written directly under its journal protocol without waiting for an Enterprise Math source checkpoint. Ordinary journal events do not require branches/PRs/index rebuilds or workflow waiting. Later curation handles deduplication and durable promotion.

## 11. Remote operation budget

Defaults for the Enterprise Math source/control repository:

- explicit-task startup: <= 3 routine reads before substantive work;
- ordinary L1/L2/L3 research: 0 routine source writes and **0 workflow-status reads**;
- source checkpoint: 1 batched branch publication + at most 1 Draft PR mutation + at most 1 coordination write;
- generated-artifact checkpoint: 1 frozen artifact generation + 1 checker pass + 1 pre-publication owner-head snapshot + 1 bounded publication path; no per-artifact blob/tree optimization loop;
- ordinary L1/L2/L3 unchanged workflow object: **0 snapshots**;
- allowed CI/debug/validation context: 1 snapshot per unchanged validation object;
- promotion: one admission refresh, one conflict snapshot, one frozen-head validation cycle, one final merge-time current-main check.

`REMOTE_BUDGET_EXCEEDED` and `PUBLICATION_CRITICAL_PATH_EXPANDED` are performance signals, never mathematical `HARD_BLOCK`s.

## 12. What remains strict

This liveness policy does not authorize bypassing repository protections, merging unreviewed/conflicting L4 payloads, force-pushing/destructive rewriting, weakening theorem status, erasing provenance, or duplicating another owner's theorem.

Only a complete mathematical/research hard block with all four fields may stop a research route:

- `missing_object`;
- `owner`;
- `necessity`;
- `unblock_condition`.

Pending/running CI, workflow API latency, missing workflow access, scheduler failure, review delay, moving `main`, or a publication implementation failure are never valid research `HARD_BLOCK`s.

Intended source lifecycle:

`small task packet -> remote-silent research -> semantic checkpoint batch -> Draft owner record -> frozen payload queue -> one L4 lane -> final gates -> main`.

---

# 进取数论 GitHub 交互预算（中文摘要）

状态：`ACTIVE / CANONICAL REMOTE-LIVENESS OVERRIDE`。

核心规则：**研究是热路径，GitHub 是稀疏持久化/最终验收边界，不是研究运行时总线。**

普通 L1/L2/L3 研究默认 0 次 CI/workflow 状态查询。只有当前任务就是 CI/debug/remote-validation、正在执行 L4/final merge/promotion、用户明确要求查看当前 CI，或正在诊断已出现的具体 CI failure 时才能查一次状态；pending 就记录 `CI_PENDING_NONBLOCKING` 并立即结束 CI 子流程。

Artifact 发布新增硬约束：研究完成后不得再启动第二个长发布工程。必须遵守 `docs/ARTIFACT_PUBLICATION_LIVENESS.md`：**本地一次生成完整 artifacts -> checker 一次 -> 发布前一次 owner-head 去重/竞态检查 -> 一次 bounded checkpoint publication**。不得为了“单一漂亮 commit”逐文件 minify/chunk/create_blob/assemble tree；connector 无法原子提交目录时，优先少量 contents writes 或正常 git push。若同一 generation 已有等价 checkpoint 先行推进，消费/比较已有结果，只补真正缺失 delta，不重复组装未挂接 commit。

机械发布期间仍必须保持用户可见 liveness；长操作遵守平台更新节奏，不能让 UI 看起来像死掉。

GLOBAL_KNOWLEDGE append-only progress journal 仍是独立的防丢失通道，不需要等待 Enterprise Math CI。
