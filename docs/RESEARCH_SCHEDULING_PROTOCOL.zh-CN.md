# Enterprise Math / 进取数论研究调度协议

状态：`ACTIVE / CANONICAL SCHEDULING CONTRACT / V2`  
生效：`2026-08-25`  
机器契约：`research_scheduler_v2.json`  
Reducer / 事件生成器：`tools/research_scheduler.py`  
运行时事件日志：GitHub Issue #240

## 1. 核心不变量

进取数论把科研自由与控制面权限分开：

> **任何具备资格的角色都可以发布成熟任务；只有经过审核的任务才能执行；执行者提交 RETURN；Driver 独立审核后才能 DONE；任何失联任务都必须留下孤儿记录。**

状态机负责“任务是否存在、是否可派工、由谁执行、是否已返回、谁审核、是否成为孤儿、如何恢复”；它不负责把数学结论自动提升为规范真理。

冻结：

`TASKBOOK_FILE != RUNTIME_STATE_AUTHORITY`  
`PUBLISH != READY`  
`RETURN != DONE`  
`LEASE_EXPIRY != SILENT_HANDOFF`

## 2. 所有任务统一进入一个 registry

官方任务必须存在于 Scheduler V2。

任务有两类登记入口：

1. V2 `PUBLISH`：事件一经合法接受，任务立即进入 `PUBLISHED / NEEDS_REVIEW`；
2. V2 迁移：旧 V1 registry 中的任务以及明确列入 V2 bootstrap 的历史有效任务被导入。

Markdown taskbook 只描述任务，不能靠文件中的 `READY`、`DONE` 字样绕过状态机。

CI 必须检查 taskbook 与 registry 的差集：任何 taskbook 自称处于可执行状态而 task_id 不在 registry，直接失败。

## 3. 正常生命周期

```text
PUBLISH
  -> PUBLISHED / NEEDS_REVIEW
  -> REVIEW(DISPATCH, ACCEPT)
  -> READY / NEEDS_DISPATCH
  -> CLAIM
  -> CLAIMED / IN_PROGRESS
  -> RETURN
  -> RETURNED / NEEDS_REVIEW
  -> REVIEW(RETURN, ACCEPT)
  -> DONE / COMPLETE
```

允许的旁路包括：

```text
RETURNED -> REVIEW(RETURN, CHANGES_REQUESTED) -> CHANGES_REQUESTED -> CLAIM ...
PUBLISHED -> REVIEW(DISPATCH, CHANGES_REQUESTED) -> PUBLISHED
PUBLISHED -> REVIEW(DISPATCH, REJECT) -> REJECTED
执行中 -> HANDOFF -> HANDOFF_READY
执行中 -> HARD_BLOCK -> BLOCKED -> UNBLOCK -> HANDOFF_READY
任务 -> ORPHAN -> ORPHANED -> RECOVER / REVIEW(RECOVERY) -> HANDOFF_READY
任务 -> SUPERSEDE -> SUPERSEDED
```

## 4. 自由研究员可以发布，但不能自行派工

FREE Phase A 仍不参加 scheduler 自动选题/CLAIM，避免当前研究议程反向污染自由发现。

当自由研究候选完成规定的 Phase-B 审计并达到 candidate lifecycle 要求的 intake-eligible 状态后，原 FREE researcher 可以自行撰写 taskbook，并发送 `PUBLISH`。

这一步只得到：

`PUBLISHED / NEEDS_REVIEW`。

研究员不能把自己发布的任务改成 `READY`。是否进入 `READY` 必须由 Driver 的 `REVIEW(stage=DISPATCH)` 决定。

## 5. Driver 交叉审核是一等状态转移

`REVIEW` 有三类：

- `DISPATCH`：审核 `PUBLISHED` 是否进入 `READY`；
- `RETURN`：审核 `RETURNED` 是否进入 `DONE`；
- `RECOVERY`：审核 `ORPHANED` 如何恢复或退出。

若任务由某 Driver-ID 发布，该 Driver-ID 不得自己把任务审核为 READY。

执行结果也不能由执行身份自己审核为 DONE。

审核必须携带 `review_ref`，并写入 `review_history`。

## 6. 执行者使用 RETURN，不使用 DONE

`CLAIM` 是可续租的执行 lease，仅 `READY`、`HANDOFF_READY`、`CHANGES_REQUESTED` 可领取。

- `HEARTBEAT`：续租，不代表科研进展；
- `PROGRESS`：续租并记录真实 checkpoint；
- `HANDOFF`：主动释放，必须给出明确 next_action；
- `RETURN`：提交执行结果，释放 claim，进入待审核；
- V2 执行者不得发送 `DONE`。

只有 Driver `REVIEW(RETURN, ACCEPT)` 才把任务变成 `DONE`。

## 7. 孤儿任务是一等状态

claim lease 到期时，V2 不再静默转成 `HANDOFF_READY`。

状态变为：

`ORPHANED / ORPHANED`。

并持久保留尽可能完整的信息：

- orphaned_at、reason；
- 原 claim_id；
- actor / Researcher-ID；
- last_progress_ref；
- next_action。

显式 `ORPHAN` 还可以登记 branch、last_commit、source_ref、发现人和失联原因。

`orphan_history` 在恢复后仍保留。ORPHANED 不参与自动派工，必须先由 Driver `RECOVER` 或 `REVIEW(RECOVERY, ...)`。

## 8. HARD_BLOCK 仍然是例外

必须同时有：

```text
missing_object
owner
necessity
unblock_condition
```

CI、review、scheduler 工具、moving main、没有 ACK 都不是数学 HARD_BLOCK。

## 9. 自动选择

TASK_RESEARCH 无用户指定任务时，只从 `dispatch_state=NEEDS_DISPATCH` 选择：

1. `HANDOFF_READY`；
2. `CHANGES_REQUESTED`；
3. `READY`；

再按 priority、leverage、最旧进度时间、稳定 task_id 排序。

`PUBLISHED`、`RETURNED`、`ORPHANED`、`BLOCKED`、终态和 live lease 均不会被自动领取。

FREE_AXIOM_DISCOVERY 不走该自动选择路径。

## 10. 事件与兼容

新事件统一使用：

`ENTERPRISE_MATH_SCHEDULER_EVENT_V2`。

Issue #240 是 append-only 日志。V2 reducer 为迁移保留旧 V1 事件兼容；历史 V1 `DONE` 可以 grandfather，但 V2 激活后不得再产生新的 V1 DONE。

优先用生成器：

```text
python tools/research_scheduler.py emit-publish ...
python tools/research_scheduler.py emit-review ...
python tools/research_scheduler.py emit-claim ...
python tools/research_scheduler.py emit-progress ...
python tools/research_scheduler.py emit-handoff ...
python tools/research_scheduler.py emit-return ...
python tools/research_scheduler.py emit-orphan ...
python tools/research_scheduler.py emit-recover ...
```

## 11. 必须通过的控制面检查

```text
python tools/research_scheduler.py validate
python tools/research_scheduler.py registry-integrity
```

单元测试必须覆盖：任务发布、Driver 独立审核、RETURN 审核、lease expiry 孤儿化、显式 orphan、恢复、选择顺序、V1 迁移以及隐藏 taskbook 检测。

## 12. 研究仍然并行

V2 不把所有数学研究串行化。它只对同一个任务的冲突 claim 和必要审核转移做序列化。

`ownership is unique; knowledge is shared; research remains parallel.`
