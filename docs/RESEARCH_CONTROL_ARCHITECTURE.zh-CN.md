# Enterprise Math 研究架构 V2

[英文版本](RESEARCH_ARCHITECTURE.md)

状态：`ACTIVE / CANONICAL GOVERNANCE / V2.6`
日期：`2026-08-28`
Driver-ID：`EM-DVR-K7Q4N8`

机器合同：

- `research_architecture.json`——角色/研究语义；
- `control_plane/current_control_authority.json`——发布/调度/工具复用/活跃性的局部控制优先级；
- `research_runtime_state_machine.json`；
- `research_task_publication_contract_v2.json`；
- `research_dispatch_contract.json`；
- `active_turn_liveness.json`；
- `research_axiom_candidate_state_machine.json`。

FREE 原始基础：`definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`
任务发布：`docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md`
提升流程活跃性：`docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`

对于 `control_plane/current_control_authority.json` 覆盖的字段，该局部优先级与其指定的精确机器合同，优先于旧文档中陈旧的 V1 兼容表述。这不改变这些控制字段之外的数学/角色权威。

## 1. 四项研究职能与非研究控制维护

### FREE_AXIOM_DISCOVERY

`PRIMITIVE SUBSTRATE -> SELF-GENERATED QUESTION -> FROZEN CANDIDATE -> PHASE-B AUDIT`。

FREE 接收原始基础，不接收当前成果或建议菜单。原始 A 阶段发现不发布任务议程。B 阶段审计后，符合条件的已审计候选可直接发布不可变 V2 任务，无需 Driver 接纳。

### TASK_RESEARCH

执行选定的明确/已登记母问题。任务研究者可以通过 V2 发布有价值的旁支残留成果，而不切换当前任务。

### RESEARCH_DRIVER

负责研究组合的优先级调整、去重、接续/关闭、Working Truth 激活、Foundation/复现路由及提升。Driver 与研究者使用相同的 V2 任务发布事务；仅让一个任务成立，不需要 Driver 权威。

### FOUNDATION_STEWARD

维护/验证共享定义、接口、状态及工具，并可通过 V2 发布治理任务。任务发布从不自动提升 Foundation 真值。

### CONTROL_PLANE_MAINTENANCE

在收到明确请求时维护调度、活跃性、CI、权威及控制入口。它不是研究身份，不授予定理评审、Driver、Steward、Working Truth 或提升权限。

## 2. 规范运行时链路

每个研究角色保留：

`PARENT_OBJECTIVE -> TASK_REGISTRATION -> TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`。

固定约束：

`OFFICIAL_POST_CUTOVER_TASK -> IMMUTABLE_V2_PUBLICATION_RECORD`。

`UNREGISTERED_NEW_TASK -> NO READY / NO CLAIM / NO_SHARED_TASK_EXECUTION_AUTHORITY`。

此生命周期约束正式共享任务。理解适用基础及精确问题后，可以继续直接开展未共享的推导、构造、计算准备和材料保全。活动可见性、工具覆盖、正式新颖性、共享接纳及控制写入，保留各自实际操作对应的时点；它们不是每个有用步骤的通用登记前提。未绑定研究任务的控制/文档维护，不通过此路径获得研究身份或 CLAIM。

`OWNER_LEASE != SESSION_LIVENESS`。

`SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE`。

`DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN`。

以下事项本身不终结母目标：任务发布、工具返回、可恢复错误、检查点/journal 写入、Stage/Driver 裁定、分支/PR 边界、`PENDING_NONBLOCKING` 或进度更新。

开放式接续在这些子流程之后仍然有效，直到母目标标准满足或被撤销。

## 3. 不可变 V2 任务发布与孤立任务预防

切换后所有新增或修改的任务使用：

- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`；
- `tools/research_task_records.py`；
- 不可变的 `research_task_records/<task-id>/<publication-id>.json`。

允许的发布者：`RESEARCHER`、`RESEARCH_DRIVER`、`FOUNDATION_STEWARD`。

`research_task_records/<task-id>/<publication-id>.json` 和 `tools/research_task_records.py` 是当前不可变 V2 发布入口。旧 V1 共享注册表及其写入器属于历史迁移来源，不是切换后的发布权威。

固定约束：

`TASKBOOK_FILE != PUBLISHED_TASK`。

`RESEARCHER_MAY_PUBLISH_TASK_WITHOUT_DRIVER_APPROVAL`。

`TASK_PUBLICATION != WORKING_TRUTH`。

`TASK_PUBLICATION != FOUNDATION_OR_CANONICAL_PROMOTION`。

每次 V2 发布保留非空的 `parent_objective_id`、`research_value`、精确前沿/下一动作、来源/谱系，以及不可变任务书身份。

研究者发布的任务默认有效优先级为 `P2 / MEDIUM`；发布者请求的优先级仍作为来源信息保留，Driver 对研究组合的优先级调整另行处理。

发布属于 `SUBFLOW`：V2 审计 PASS 后，返回当前母目标。

切换前的调度器/任务书状态，只作为既有兼容执行的旧基线保留。新的重新调度、修改或依据当前政策重新评审，需要迁移至 V2。

## 4. 规范实时调度

规范实时路由为：

`research_control_dispatch.py`。

它组合相互隔离故障的运行时视图、过期 owner 恢复、普通新任务选择，以及活跃 cohort 的 lane 选择。

`tools/research_dispatch.py` 是普通的**新任务选择器**，不是完整的实时路由决策。

`tools/research_lane_dispatch.py` 是活跃 cohort 的 lane 选择器。

固定约束：

`STALE_SESSION + VALID_OWNER_CLAIM -> PREPARE_SUCCESSOR_CLAIM`。

依据 `research_dispatch_contract.json` 与 `control_plane/executor_succession_policy.json`，跨会话后继执行使用真实且具有角色权限的身份、不可变接续证据、新的已认证 CLAIM、精确前任 CAS 及旧写入者隔离。旧 CLAIM 保留为来源；读取包和准备步骤均不授权执行。不能抢占仍活跃的精确会话。

`FRESH_SELECTOR_EMPTY + VALID_OWNER_LIVENESS_UNKNOWN -> VERIFY_SESSION_LIVENESS`。

只有在可恢复的过期 owner 范围和新目标都已排除后，`NO_DISPATCH` 才有效。

## 5. FREE A 阶段信息制度

固定约束：

`FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS`。

`NO_DEFAULT_DISCOVERY_LENS_MENU`。

FREE A 阶段只加载原始基础、实际需要的精确原始概念、受保护且相关的世界观，以及完整性/类型规则。当前任务、路线、历史、下游成果、其他分支的 Working Truth、建议菜单，以及项目工具/表示便利性，都不是发现先验。

候选冻结后，当前及既往上下文成为 B 阶段审计材料。
冻结前，独立形成的问题实际包含相关类型化结构时，可依 FREE 角色及基础合同使用精确定义、适用条件和必要工具来源。这不开放整份目录、比较或去重，也不抹去此前暴露。

## 6. 候选生命周期

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`。

`DISCOVERY_IN_PROGRESS -> BLIND_CANDIDATE_FROZEN -> PHASE_B_AUDIT -> CLASSIFICATION`。

从 `AUDITED_AXIOM_CANDIDATE`、`AUDITED_REPLACEMENT_CANDIDATE` 或 `EXACT_NEGATIVE_OBSTRUCTION` 状态出发，研究者可以发布不可变 V2 任务，同时保留 `origin_kind=FREE_AXIOM_CANDIDATE`、候选 ID/状态及语义谱系。

Driver/Steward 接纳仍是后续独立决策，处理研究组合优先级、Working Truth、Foundation/复现及提升。

`TASK_ORIGIN_AND_LINEAGE_CANNOT_BE_ERASED_BY_RENAMING`。

## 7. Working Truth

Working Truth 仅在 Driver 明确冻结，或精确任务语义明确授予执行前提后激活。仅完成 V2 任务发布，不构成激活事件。

## 8. 工具查询与实际复用

理解 TASK 语义后，遵循 `tool_invocation_policy.json` 与 `control_plane/current_control_authority.json` 的实际时点：查询可与未共享推导并行，或在保存成果后进行。工具覆盖及相关匹配判定是方法新颖性声明或共享工具接纳之前的要求，不是开始私下探索的前提。明确的发现隔离保留其来源范围和冻结时点。

`TOOL_COVERAGE_LOOKUP != TOOL_USE`。

在上述新颖性或共享接纳必需步骤，每个相关匹配必须依据 `tool_invocation_policy.json` 获得明确的复用处置，按实际情形包括：

- `REUSE_APPLIED`；
- `REUSE_EXECUTED`；
- `COMPOSE_APPLIED`；
- `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE`；
- `EXTEND_EXISTING_TOOL`；
- `CAPABILITY_GAP_CONFIRMED`；
- `NOT_APPLICABLE`。

环境无法执行一个足够适用的既有实现，本身不构成数学能力缺口。

FREE A 阶段不把当前项目工具词汇作为发现先验；B 阶段为审计、去重和复用打开工具箱/方法上下文。

## 9. Stage 与后继任务规则

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`。

接续需要真实的新信息缺口、可区分结果、终止条件、`parent_task_id`，并明确考虑关闭、转交其他 owner 或自由探索。

Stage 2 及以后属于接续语义；重命名不重置谱系。

`STAGE_TERMINAL_VERDICT -> SAME_TURN_SUCCESSOR_GATE_EVALUATION`。

## 10. 调度器、Foundation 与研究组合

规范控制调度是 TASK 深化研究的基础设施，不是 FREE A 阶段的问题选择机制。切换后的新工作必须在 CLAIM 前具有 V2 权威。

原始发现不会自动进入 Foundation 回流，任务发布也不会自动提升 Foundation 真值。

Foundation Steward 研究交接使用 V2 任务发布及 `research_control_dispatch.py`；不得通过编辑 `research_runtime_policy_v2.json` 发布新工作。

近期路线成功本身不是路线图证据。已登记保全不意味着立即被选中。

## 11. 独立性与证据

干净的盲发现主张要求生成前上下文干净，并冻结原始基础/世界观快照。

`DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE`。

独立运行在冻结前不共享候选包或建议菜单。发布任务不会产生独立性。

## 12. 读取性能与控制面效率

`SMALLEST_SUFFICIENT_ROLE_PACKET > UNIVERSAL_PRELOAD`。

FREE：`ROLE -> PRIMITIVE SUBSTRATE -> NEEDED PRIMITIVES -> DISCOVERY`。

TASK：`APPLICABLE FOUNDATION/RULES -> EXACT TASK OR PACKET -> FIRST DEPENDENCY -> WORK -> TRIGGERED EXPANSION`。

宿主已注入 `AGENTS.md` 时复用其内容；普通 TASK 启动不增加对该路由的远程读取。使用 `docs/RESEARCHER_STARTUP_CONTEXT_PROTOCOL.md` 中现行角色适用的基础与传输路径。

控制面工作使用 `active_turn_liveness.json` 中的协作式软看门狗：

- 每个检查周期通常调用控制工具 2—3 次，然后重新计算；
- 证据充分时停止扩大诊断；
- 相同错误特征归并为一个根因；
- 用户的状态/方向消息优先于非必要诊断；
- `READ_SNAPSHOT != WRITE_AUTHORITY`；
- 持续产生语义进展的长时间数学计算，不属于控制面无进展。

## 13. 远程操作与发布活跃性

`REMOTE_SILENT` 描述仓库活动，不描述对话不活跃。

`CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK`。

`CHECKPOINT_PERSISTED -> RESUME_PARENT_TASK`。

`PUBLICATION_COMPLETE -> RESUME_PARENT_TASK`。

任务发布、GitHub 发布及检查点子流程，在母目标仍未完成时，都在同一轮返回母目标。

## 14. 提升

`READY_PR != PROMOTION_LANE_LEASE`。

数学 L4 仍然每次只允许一个有界的活跃提升尝试。严格的 `NO_NEW_MATHEMATICS` 治理维护使用单独的有界维护尝试，不能夹带数学主张变更。

## 15. 持久化与真值

- 不可变 V2 任务记录＝切换后的任务存在性/来源证据；
- `research_task_records/<task-id>/<publication-id>.json`＝规范不可变 V2 任务发布记录；
- 任务书＝任务局部研究内容；
- Issue #240＝稀疏的运行时归属/控制事件；
- 不可变结果/评审记录＝终态来源证据；
- journal＝事件来源证据，不是定理真值；
- Driver Continuity＝路由摘要，不是任务存在性或定理证据；
- 规范数学真值＝经过门禁的 Source `main`。

## 16. 轮次终结

仅在母目标完成、用户明确要求停止/暂停/等待，或因真实的安全、授权、缺少用户数据、不可避免的外部事件或平台限制，导致没有可执行的下一动作时，本轮才结束。

因阻断而终结前，完成所有独立或下游安全的工作，并交付当前最强结果。

当 `continue` 不会增加信息时，不得使用 `WAITING_FOR_CONTINUE`。
