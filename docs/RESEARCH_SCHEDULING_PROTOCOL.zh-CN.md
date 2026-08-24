# Enterprise Math / 进取数论研究调度协议

状态：`ACTIVE / CANONICAL SCHEDULING CONTRACT / V2`
生效：`2026-08-24`
机器配置：`research_scheduler_v2.json`
归约器/CLI：`tools/research_scheduler.py`
实时事件日志：GitHub Issue #240
详细状态机：`docs/RESEARCH_SCHEDULER_V2.md`

## 1. 第一原则

研究默认并行；规范晋升仅在一致性需要时串行。`defer`、`consume`、review、CI、moving main 都不自动构成研究 blocker。只有完整四字段 `HARD_BLOCK` 可以把任务置为 `BLOCKED`。

## 2. 所有任务必须进入状态机

V2 registry 是以下三类对象的并集：

- Issue #240 中的 V2 `PUBLISH` / `REGISTER_ORPHAN` 事件；
- `research_tasks/*.md` 中所有可发现 taskbook；
- 迁移期间只读导入的 V1 `research_scheduler.json` 静态任务。

因此 taskbook 不会再“文件存在但状态机看不见”。未登记 taskbook 自动成为 `ORPHANED`，不可直接调度。

## 3. 标准生命周期

```text
PUBLISH
  -> PENDING_REVIEW
  -> REVIEW(DISPATCH, APPROVE)
  -> READY
  -> CLAIM
  -> CLAIMED / IN_PROGRESS
  -> RETURN
  -> RETURNED
  -> REVIEW(RETURN, APPROVE)
  -> DONE
```

未完成主动退出走 `HANDOFF -> HANDOFF_READY`。

租约静默到期、显式 `ORPHAN`、未登记 taskbook 或外部发现的无主 branch/return 都进入 `ORPHANED`，留下 durable orphan history；必须由 Driver `ADOPT` 或 `REVIEW(ORPHAN_RECOVERY)` 后才能恢复。

## 4. 自由研究员可以发布任务

FREE researcher 和普通 researcher 都可以 `PUBLISH`。

但 `PUBLISH` 只产生 `PENDING_REVIEW`，不产生 `READY`，所以“可以提出/登记新任务”和“可以自行批准任务”严格分开。

FREE 的候选成熟度、来源 provenance、官方 taskbook gate 仍然有效；发布动作不能绕过这些科学治理门。

Driver 也可以发布任务，但 Driver 自己发布的任务不得由同一 Driver-ID 做 DISPATCH 审核。

## 5. Driver 交叉审核是机器状态转移

V2 researcher 不能直接 `DONE`。

研究员完成后必须 `RETURN`，进入 `RETURNED / NEEDS_REVIEW`。Driver 的 `REVIEW(RETURN)` 决定：

- `APPROVE -> DONE`；
- `REVISE -> HANDOFF_READY`，并给出具体 `next_action`；
- `REJECT -> REJECTED`。

DISPATCH 审核还会检查 owner。RESEARCH 任务只有分配给当前 `ACTIVE_OWNER/ACTIVE_BRIDGE` 才能放行；无效 owner 的审核、adopt、claim 均被拒绝。

## 6. CLAIM 是租约，不是永久占有

- 第二个 CLAIM 不能抢占 live lease；
- `HEARTBEAT` / `PROGRESS` 续租；
- `HANDOFF` 主动释放；
- 租约到期不再无痕变成 HANDOFF，而是进入 `ORPHANED` 并保留历史；
- `ORPHANED` 不参与正常自动选择。

## 7. 各角色正确使用方式

研究员/FREE：`PUBLISH`、`CLAIM`、`HEARTBEAT`、`PROGRESS`、`RETURN`、`HANDOFF`、完整 `HARD_BLOCK`。

Driver：`REVIEW(DISPATCH|RETURN|ORPHAN_RECOVERY)`、`ADOPT`、`SUPERSEDE`、调度和 review 选取；不得自审自己发布的 Driver 任务。

任何人都不应手工改静态状态来模拟运行时事件。运行时事实统一追加到 Issue #240。

## 8. 常用命令

```bash
python tools/research_scheduler.py validate
python tools/research_scheduler.py snapshot --events events.jsonl
python tools/research_scheduler.py audit-registry --events events.jsonl
python tools/research_scheduler.py select --events events.jsonl
python tools/research_scheduler.py select-review --events events.jsonl --reviewer-id EM-DVR-ABC123
```

事件应优先由：

```bash
python tools/research_scheduler.py emit ...
```

生成，避免手写 JSON 漏字段。

## 9. 调度与数学真值分离

Scheduler `DONE` 只表示工作流关闭，不表示 theorem canonical、Foundation 已接受、novelty 已成立或 L4 promotion 已完成。数学证据和规范晋升继续服从对应 theorem/taskbook/Driver/Steward/Foundation 合同。

## 10. V1 迁移

原 `research_scheduler.json` 只作为 legacy seed 保留；V1 event 仍可回放，防止历史工作丢失。V2 启用后不再允许新的“研究员 DONE”或“未登记 taskbook 直接 READY”语义。

完整机器语义与 orphan/publication/review 契约见 `docs/RESEARCH_SCHEDULER_V2.md`。
