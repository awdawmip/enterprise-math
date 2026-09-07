# 研究调度协议 V2

状态：`ACTIVE / CURRENT ONLY`

任务定义只来自不可变的 V2 发布记录。`research_control_dispatch.py` 先处理陈旧会话下的既有 owner 恢复，再把全新任务选择交给 `tools/research_dispatch.py`，把并行 cohort lane 选择交给 `tools/research_lane_dispatch.py`。

Issue #240 的运行态变更必须来自经服务器认证、未编辑且属于授权操作者的 GitHub 评论封装。`tools/research_runtime_reducer.py` 只是纯 reducer，不持有任务表，也没有数学权威。

选择顺序由 `research_runtime_policy_v2.json` 定义。owner lease 与会话存活相互独立；陈旧会话在核验 durable frontier 后接管原 claim，不创建第二个 claim。

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
