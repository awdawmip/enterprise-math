# 研究调度协议 V2

状态：`ACTIVE / CURRENT ONLY`

定时对话的每轮入口、角色职责、未完请求恢复及跨轮接续见 [自主研究执行协议](AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md)。先协调未知副作用、恢复已有前沿，再领取新任务；一个控制子流程完成不等于研究父目标完成。

任务定义只来自不可变的 V2 发布记录。在开始新研究单元的边界，`research_control_dispatch.py` 将可领取的新任务、cohort lane 及已核实陈旧 owner 的后继候选一起排序。活跃的精确 owner 会话仍受保护；恢复仍须保留精确 predecessor/frontier，并通过现行认证后继 CLAIM/CAS。选择本身不授予执行权限。

Issue #240 的运行态变更必须来自经服务器认证、未编辑且属于授权操作者的 GitHub 评论封装。`tools/research_runtime_reducer.py` 只是纯 reducer，不持有任务表，也没有数学权威。

比例在 `research_runtime_policy_v2.json` 配置，初始 P0/P1/P2/P3 = 40/30/20/10。这是工程初始值，不是用户指定数字。`tools/research_fair_selection.py` 从共享认证事件快照中、reducer 实际接受的 CLAIM 和可领取状态变化重建加权服务余额：每次成功领取按当时可用档位的归一化权重记份额，实际获领档位扣一个机会。缺席档不累计欠账，其份额可以借用，恢复时不要求偿还缺席期的份额。交接或过期后新的成功领取计入；失败、同 claim_id 重试、HEARTBEAT、PROGRESS 及原 owner 的读取/续租不增加次数。

同优先级按显式 `parent_task_id` 父链识别方向，在当时可用方向间均分机会；缺失父链时透明退回精确任务 ID，不凭任务名字或身份 ID 前缀模糊聚类。同方向先兼顾较少成功领取的任务，再照顾等待更久的任务。leverage 与 HANDOFF 状态不再享有无条件优先。显式优先级过滤和 Source 正式定向分派保留原范围。

这是建议性的加权选择，不是原子的全局配额，也不新增领取拒绝门槛。实际归属仍由现行单任务/lane CLAIM 及 predecessor CAS 决定。多终端可能用同一旧快照成功领取不同任务；下次读取会计入每个实际赢家，再由后续选择补偿，不能保证每十次并发领取精确为 4/3/2/1。竞争后按原流程刷新 canonical 状态，无须新锁、轮询器或后台服务。

历史计账范围是 canonical reducer 已准入的当前发布代次/lane 认证事件；不能凭任务名字把已被过滤的旧发布 CLAIM 当作有效历史。`fair_selection` 明示缺失历史/可用状态/父链时的退化，退回当前可见任务。历史依赖或发布变化若没有保留状态转移，无法证明过去的精确可领取性。原事件、科学结论、发布权限及旧任务记录不变。owner lease 与会话存活仍相互独立；claim 过期释放归属，不会自动执行或恢复 job。

canonical Result/Review 的 freeze/reopen 时间也约束可领取区间：任务完成或等待审查期间，原始 READY、租约过期轨迹不能继续累积份额。cohort 开启及 lane Result freeze 时间同样约束 lane 可用期。覆盖状态缺少开始时间时，排除该任务未经证明的可用区间并报告历史降级原因，仍保留成功 CLAIM 事实；只在当前时间追加 false 无法消除过去的幽灵欠账。

## 已注册 HANDOFF 的意图

HANDOFF 的终态意图必须由机器可读字段明确表达。自然语言字段 `next_action`、`summary` 和 `progress_ref` 仅提供描述性证据，不能决定 owner 是将工作返回给 Driver 审查，还是交给另一位研究员继续。

对于经认证的已注册 Issue #240 HANDOFF 事件，若 GitHub 服务器 `created_at` 位于经审计的兼容边界 `2026-09-07T02:20:00Z` 或之后，事件生产方必须使用以下结构形式之一：

- 交给研究员继续：`handoff_scope: CONTINUATION`；
- 冻结返回并等待 Driver 审查：`handoff_scope: FROZEN_RETURN_AWAITING_DRIVER_REVIEW`；
- 携带不可变 Result 的冻结返回：非空的 `result_id`；
- 兼容历史格式的冻结返回：精确的 `terminal_scope: RESEARCH_RETURN_FROZEN_AWAITING_DRIVER_REVIEW`。

兼容边界是在重放该时段完整的 Issue #240 事件流后选定的。启用约束之前，边界时刻及之后恰有两个 HANDOFF：一个结构意图不明确的 PCF 返回，以及一个已经结构化的 P021 冻结返回；不存在需要重新解释的普通研究员间续接。

`terminal_candidate` 仍作为边界之前事件的历史 reducer 兼容标记。新的已注册事件生产方不得将它作为唯一的终态标记。

边界之后的 HANDOFF 若结构范围缺失、格式错误、未知或相互矛盾，则不得生效。特别是，`CONTINUATION` 不能与冻结返回标记共存。结构意图不明确的 HANDOFF 不会将任务释放为可重新调度状态。只有当该被拒绝事件属于在经服务器认证的事件时刻实际有效的 claim 时，它才具有临时阻断权限；错误或不存在的 `claim_id` 不能阻断任务。

更正只能追加。在原 owner lease 仍然有效时，使用同一个有效 claim 追加结构合法的新 HANDOFF。不得编辑旧的 Issue #240 评论。

同一有效 claim 来源规则也适用于因缺少冻结 Result 及终态 Driver 审查而被拒绝的已注册 `DONE`：伪造或已失效的 claim 不能仅凭发出一个看似终态的事件就取得任务阻断权限。

冻结约束：

`HANDOFF_TEXT != TERMINAL_AUTHORITY`。

`POST_BOUNDARY_REGISTERED_HANDOFF -> EXPLICIT_MACHINE_SCOPE`。

`AMBIGUOUS_HANDOFF != FRESH_REDISPATCH`。

`WRONG_OR_GHOST_CLAIM_TERMINAL_EVENT != BLOCKING_AUTHORITY`。
