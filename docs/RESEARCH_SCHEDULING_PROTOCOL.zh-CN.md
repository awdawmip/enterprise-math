# Enterprise Math 研究调度协议 V2

状态：`ACTIVE / CANONICAL CONTROL PLANE / V2`
切换时点：`2026-08-24T16:00:00+08:00`
运行看板：GitHub Issue `#240`
状态机：`research_scheduler.json`
归约器：`tools/research_scheduler.py`
事件生成器：`tools/research_scheduler_event.py`

## 1. 唯一控制面

每一个研究任务身份都必须在 Scheduler V2 中可见。任务书不能因为在 Issue #240 之外创建或执行，就变成状态机看不见的“隐形任务”。

V2 注册表由三部分合成：冻结的 V1 静态注册表、`research_tasks/` 下全部任务型工件、以及 V2 的 `PUBLISH`、`MIGRATE`、`ORPHAN` 事件。

V2 切换前已经存在但没有有效运行历史的任务书，一律登记为 `ORPHANED`，不会静默重新派发。V2 任务可以先通过 `PUBLISH` 进入状态机，不要求任务书已经合并到 `main`。

## 2. 标准生命周期

新任务统一走：

`PUBLISH -> REVIEW_PENDING -> REVIEW_CLAIM -> APPROVE -> READY -> CLAIM -> IN_PROGRESS -> SUBMIT -> RETURN_REVIEW -> REVIEW_CLAIM -> REVIEW -> DONE`

返工必须显式：

`REVIEW(RETURN_TO_RESEARCH) -> HANDOFF_READY`

失联必须显式：

`CLAIM 租约到期 -> ORPHANED -> ADOPT -> CLAIMED`

V2 不存在合法的 `DONE` 直达事件。研究员不能自行把自己的任务关闭为 DONE。

## 3. 发布权限

普通研究员、自由研究员、Driver、Foundation Steward 都可以发布任务建议；发布本身绝不等于可领取。

尤其冻结：

`FREE RESEARCHER PUBLISH -> REVIEW_PENDING`，绝不直接进入 `READY`。

任务进入可领取状态，必须有当前的跨 Driver 发布审核，并绑定不可变的 Driver-approved taskbook ref。发布人不得审核批准自己发布的任务。

## 4. Driver 交叉审核

V2 的发布审核和研究结果审核都必须先取得 `REVIEW_CLAIM` 审核租约。

状态机会拒绝：发布人自审、执行人自审、没有审核租约直接给 verdict。

`REVIEW` 只是研究控制与路由结论，不自动等于定理为真，也不自动把内容提升为 canonical source。

## 5. 孤儿任务登记

孤儿任务是正式状态，不再把 lease expiry 无痕改成 `HANDOFF_READY`。孤儿记录至少持久保存 Task-ID、孤儿原因、原 claim/execution identity、最后 progress ref、next action、发现时间，以及可取得的 recovery/evidence ref。

`ORPHANED` 不能普通 `CLAIM`，必须使用带 recovery ref 的 `ADOPT` 恢复。

V2 自动发现旧状态机之外的任务书时，若没有可靠历史解释其当前状态，就登记为 orphan，而不是假装它 READY。

## 6. V1 退役

切换时点以前的 `ENTERPRISE_MATH_SCHEDULER_EVENT_V1` 历史事件继续可重放。切换时点及以后新增的 V1 事件一律忽略。所有新工作必须使用 `ENTERPRISE_MATH_SCHEDULER_EVENT_V2`。

历史 V1 `DONE` 只保留为历史完成证据，不会给 V2 留下“执行人自己 DONE”的后门。

## 7. 正确使用方式

先读机器状态，不凭聊天记忆猜：

```bash
python tools/research_scheduler.py validate
python tools/research_scheduler.py registry --events events.jsonl
python tools/research_scheduler.py select --events events.jsonl --kind ANY
python tools/research_scheduler.py select-review --events events.jsonl --reviewer-id EM-DVR-XXXXXX
```

事件优先使用生成器，不手写 JSON：

```bash
python tools/research_scheduler_event.py publish-taskbook research_tasks/TASK.md --taskbook-ref research_tasks/TASK.md@<sha> --publisher-id <ID> --publisher-role RESEARCH_DRIVER --at <ISO8601>
python tools/research_scheduler_event.py publish-proposal --task-id <TASK> --title <TITLE> --publisher-id <ID> --publisher-role RESEARCHER --frontier <F> --next-action <N> --at <ISO8601>
python tools/research_scheduler_event.py review-claim --task-id <TASK> --reviewer-id <DRIVER> --review-claim-id <ID> --at <ISO8601>
python tools/research_scheduler_event.py claim --task-id <TASK> --execution-id <ID> --claim-id <ID> --at <ISO8601>
python tools/research_scheduler_event.py submit --task-id <TASK> --execution-id <ID> --claim-id <ID> --return-ref <path@sha> --at <ISO8601>
```

生成器输出的单个 JSON 对象，作为 Issue #240 的一条独立评论追加。

## 8. 通用领取语义

用户只说 `领任务`：状态机必须先物化当前 V2 注册表，选最高优先级的 `NEEDS_DISPATCH`，再 CLAIM、解析身份并开始任务；用户不需要人工搬运 Task-ID。

Driver 只说 `领审核`：状态机选最高优先级且不存在自审冲突的 `NEEDS_REVIEW`，取得审核租约并开始审核；用户不需要在不同对话之间搬运 return。

## 9. 迁移事件

`MIGRATE` 只用于 V2 上线时接管已经在旧控制面之外运行的工作，只有 Driver 能发，必须写精确 migration ref 和 target state。切换后的正常任务禁止用 MIGRATE 绕过 PUBLISH 或交叉审核。

## 10. 真值边界

`SCHEDULER_DONE != THEOREM_TRUTH`。

`REVIEW_DONE != CANONICAL_MAIN`。
