# Enterprise Math Research Scheduler — Non-Blocking Startup Addendum

Status: `ACTIVE / V2 NON-BLOCKING LIVENESS ADDENDUM`  
Effective: `2026-08-25`  
Canonical scheduler: `research_scheduler_v2.json`  
Canonical protocol: `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md` / `.zh-CN.md`

This addendum preserves one narrow liveness principle:

> **scheduler coordination must not become a polling/wait ritual, but official shared-task execution must still use Scheduler V2.**

The old V1 allowance for silently continuing an official scheduler task as an unleased execution is superseded.

## Startup

1. An explicit current user instruction may be researched immediately as a direct conversational task.
2. If that work becomes a persistent official Enterprise Math task, it must enter Scheduler V2 through `PUBLISH` or an explicit migration/bootstrap record.
3. Automatic portfolio selection is allowed only from current V2 `NEEDS_DISPATCH` state computed with the available runtime event stream.
4. A scheduler-selected official task must be `CLAIM`ed before the conversation represents itself as that task's executor.
5. Failure to write a scheduler event does not make mathematics impossible, but it means the conversation has **not acquired the official shared-task lease**. It may continue only as direct/user-scoped exploration or a non-owning contribution until coordination is restored.
6. Never invent a claim, lease, READY state, review, return, DONE state, or orphan recovery in prose when the reducer does not contain it.

## Publication and review are not startup waits

A mature task may be published and then remain `PUBLISHED / NEEDS_REVIEW` without blocking unrelated research.

A Driver review may remain pending without requiring polling. The task simply is not READY yet.

Likewise, `RETURNED` may await Driver review without keeping the executor's claim open. The executor has returned; another task or parent objective may proceed.

## Claims, handoff, and orphan liveness

For official execution:

```text
READY / HANDOFF_READY / CHANGES_REQUESTED
  -> CLAIM
  -> work / PROGRESS
  -> HANDOFF or RETURN
```

V2 claim expiry creates `ORPHANED` and durable orphan history. It does not silently grant another worker permission to resume. Driver recovery is required.

Historical V1 expired leases are replayed under their old reclaim semantics only for append-only compatibility, while V2 still records the historical orphan provenance.

## CI / review polling

Workflow and review status are snapshots, not wait primitives.

For an unchanged commit/run/PR set, take at most one routine status snapshot in one uninterrupted execution phase. If it is pending/running/requested, record that fact and continue whatever non-waiting work remains.

Do not sleep, back off, recursively refresh, or repeatedly call status APIs merely to wait for change.

A new failure may justify one targeted log inspection. A materially new object (new head SHA/run ID/new user turn requiring current state) may justify a fresh snapshot.

## What is not a mathematical HARD_BLOCK

The following are not mathematical/research HARD_BLOCK reasons:

- scheduler connector/read/write failure;
- CI/review pending;
- moving main;
- inability to merge/publish immediately;
- a task being PUBLISHED/RETURNED/ORPHANED and awaiting the correct control-plane action.

Only the canonical four-field missing-object/owner/necessity/unblock-condition record can be a mathematical HARD_BLOCK.

## Integrity boundary

Non-blocking does **not** mean bypassing control state.

Freeze:

`NO_POLLING != NO_SCHEDULER`.

`DIRECT_USER_RESEARCH != OFFICIAL_SHARED_TASK_LEASE`.

`UNLEASED_EXPLORATION != CLAIMED_EXECUTION`.

`PUBLISHED != READY`.

`RETURNED != DONE`.

---

# 进取数论研究调度器——V2 非阻塞启动补充

状态：`ACTIVE / V2 NON-BLOCKING LIVENESS ADDENDUM`  
生效：`2026-08-25`

本补充只保留一个活性原则：**状态机不能变成轮询等待仪式，但正式共享任务仍必须走 Scheduler V2。**

旧 V1 中“scheduler 写不上就以 unleased 身份继续占用正式任务”的规则废止。

- 用户当前直接指定的问题可以立即研究；若形成持续性的官方任务，则必须 PUBLISH/迁移进入状态机。
- 自动调度只能从 V2 `NEEDS_DISPATCH` 中选。
- 正式 scheduler task 在宣称自己是执行者前必须有有效 CLAIM。
- 写事件失败不阻止思考，但意味着没有取得正式共享任务 lease，只能作为用户直接研究或非 owner 贡献继续。
- PUBLISHED、RETURNED、ORPHANED 等待正确控制动作时，不需要轮询，也不能靠文字绕过。
- V2 lease 到期必须 ORPHANED；旧 V1 仅为历史 replay 保留原 reclaim 语义，同时仍记录 orphan provenance。
- CI/review 状态只做一次性快照，不得 sleep/retry/poll 等待变化。

冻结：

`NO_POLLING != NO_SCHEDULER`  
`DIRECT_USER_RESEARCH != OFFICIAL_SHARED_TASK_LEASE`  
`UNLEASED_EXPLORATION != CLAIMED_EXECUTION`  
`PUBLISHED != READY`  
`RETURNED != DONE`
