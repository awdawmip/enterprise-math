# 进取数论研究反哺底层闭环

状态：`ACTIVE / CANONICAL GOVERNANCE CONTRACT`  
生效：2026-08-09  
机器路由：`foundation_backflow.json`  
相关运行面：Research Relay #82、Foundation Problem Set #164、Research Dispatch Board #240

## 1. 目的

进取数论的研究架构必须同时支持两个方向：

1. `Foundation -> research`：所有研究路线消费统一的定义、定理、工具和边界；
2. `research -> Foundation`：成熟研究反向暴露更弱原语、更小充分状态、最小修复、共享工具和失败边界，并经过验证后修正公共底层。

只有第一条而没有第二条，会使 Foundation 逐渐成为历史起点，而不是被研究持续压力测试的活底层。

本协议把现有三个实时表面接成一个闭环：

- **#82 Research Relay**：传播可复用的 theorem / counterexample / tool finding；
- **#164 Foundation Problem Set**：记录已经通过底层最小验证、但仍需要真实研究的 Foundation Question；
- **#240 Research Dispatch Board**：解决谁在当前会话继续哪一个研究/治理 frontier，并通过 lease/handoff 防止静默失联。

三者职责不同，任何一个都不单独决定 canonical truth。

## 2. 不可混同的权威边界

必须长期保持：

- Relay `PROVED` 不等于 `CANONICAL_MAIN`；
- Scheduler `DONE` 只表示声明的执行 frontier 完成，不等于 theorem proved，也不等于进入 main；
- FQ `ANSWERED` 只表示研究员返回了答案，不等于底层维护者已经接受；
- Steward `ACCEPTED` 仍不是 main，必须经过当前 main 上的规范集成与适用门禁；
- **只有 source repository `main` 中经过适用门禁的内容，才是 canonical source truth。**

因此规范路径是：

`research evidence -> backflow packet -> classification -> FQ/research when needed -> returned answer -> steward verification -> current-main integration -> gates -> main -> common surface/tool routing -> later research pressure test`。

## 3. 阶段状态机

一个反哺候选使用以下逻辑阶段；不是每个候选都必须走完所有阶段。

### `DETECTED`

某条研究路线、工程压力测试、Relay、工具审计或底层维护发现了可能具有跨路线价值的结构。

### `PACKETIZED`

将发现压缩成 Foundation Feedback Packet，至少尽量回答：

- `candidate_object_or_tool`；
- `weakest_scope_hypotheses`；
- `minimal_state`；
- `minimal_repair_or_extension`；
- `negative_boundary`；
- `cross_route_evidence`；
- `proof_status`；
- `tool_surface`；
- `prior_art_and_owner`；
- `foundation_destination`。

### `CLASSIFIED`

只允许三种分流：

1. `DIRECT_FOUNDATION_MAINTENANCE`；
2. `FOUNDATION_QUESTION`；
3. `APPLICATION_LOCAL_OR_NOT_READY`。

第三类在这里退出闭环，继续留在原 owner；它不是失败。

### `FQ_OPEN`

需要真实研究的候选以稳定 `FQ-*` ID 进入 #164。FQ 必须明确 `verified_so_far` 与 `unknown`，不能把猜想写成已经证明的问题前提。

### `RESEARCH_SCHEDULED`

每个需要执行的 OPEN/CLAIMED/RESEARCHING FQ 必须能通过 `foundation_backflow.json` 找到一个 #240 scheduler task：

- 真正数学研究链接到 `RESEARCH` task，由合适的 L1/L2/L3 active owner/bridge 承担；
- task 自身必须在 `foundation_questions` 字段显式声明所承载的 FQ；
- 现有 owner task 只有当该 FQ 真正属于它已声明的 frontier 时才能承载；owner 相同本身不够；
- 已有 live claim 的 task 不得被静态配置事后改题；不同问题应使用独立的 bounded scheduler task；
- steward 不把自己伪装成 research owner；
- 若 FQ 已经返回答案，则进入 governance-side steward verification，而不是再次自动派发同一研究。

### `RESEARCHING`

当 #240 运行面可用时，研究执行遵守其 lease 状态机。#164 保持数学问题/回答记录；#240 保持执行连续性。Scheduler 可用性不是研究启动门禁，两者也不得互相替代。

### `ANSWERED`

研究员向 #164 返回 proof/counterexample/exact tool evidence、最弱范围、source ref、owner/prior-art 边界和 canonical change 建议。可复用结果同时 Relay 到 #82。

### `STEWARD_VERIFICATION`

底层维护者独立核对 returned answer 与当前 `FOUNDATIONS`、`THEOREMS/PROBLEM_STATUS`、common surface、源码/tests/Lean、Relay 和 provenance。

可能结果：

- `ACCEPTED`；
- `NEEDS_NARROWER_ANSWER`；
- `REJECTED`；
- `KEEP_OPEN`。

### `INTEGRATION`

`ACCEPTED` 结果从**当时最新 main**构造一个最小规范补丁。数学 owner/source 证据被冻结；集成层不得在运输过程中偷偷创造新数学。

### `CANONICALIZED`

适用门禁通过并合入 main 后：

1. #164 对应 FQ 标为 `CANONICALIZED`；
2. common research surface / machine router 暴露新底层接口；
3. theorem/tool/status/lineage 按需要更新；
4. 当运行面可用时，#240 对应治理 frontier 记录完成或 handoff；
5. GLOBAL_KNOWLEDGE 记录 durable architecture/state；
6. 后续所有研究 preflight 消费新 Foundation，继续压力测试。

这一步闭合回到 `DETECTED`：新底层不是终点，而是下一轮研究的输入。

## 4. Scheduler 接入规则

`research_scheduler.json` 继续是 durable task/frontier 定义；#240 在可用时继续是 runtime event log。

`foundation_backflow.json` 只增加**语义链接**，不复制 scheduler 状态机。每个 active FQ link 至少记录：

- `question_id`；
- `phase`；
- `scheduler_task_id`；
- `scheduler_role`；
- `research_owner`（研究阶段适用）；
- `source_refs`。

规则：

- `scheduler_role=RESEARCH` 必须指向 scheduler 的 `kind=RESEARCH` task；
- 被引用的 research task 必须在 `foundation_questions` 中显式列出该 FQ；
- `scheduler_role=STEWARD_VERIFICATION` 或 `INTEGRATION` 必须指向 `kind=GOVERNANCE` task；
- 一个 FQ 可以随阶段改变链接，但不能同时把“research answer”和“steward acceptance”混成同一状态；
- 一个现有 owner task 只有在 task 显式声明该 FQ 时才能承载它；仅 owner 相同不是充分条件；
- 不得为了复用 task ID 而事后改写一个已经 live claimed task 的语义；不同问题应建立独立 bounded task；
- 若承载会造成 owner scope drift，则新建明确的 L3 bridge/probe，而不是挤进不相关 owner；
- FQ canonicalize 后必须移出 active scheduler link，改由 `canonicalized_examples`/provenance 保留，不能继续伪装成待执行任务。

这些链接是 durable recovery metadata。无法读取或写入 #240 只属于协调降级，不是数学 `HARD_BLOCK`，也不能阻止用户明确任务继续推进。

## 5. Relay 接入规则

研究路线出现以下任一情况，应生成或更新 Feedback Packet：

- 新母定理候选；
- 多条路线重复出现同一最小状态/最小修复；
- 一个 application counterexample 否定了 Foundation 层看似自然的推广；
- 可执行工具暴露 theorem/API domain mismatch；
- 新工具被至少两个 owner 复用；
- 某个坐标被证明只是派生表示，而不是必须原语。

若结果已经通过 Relay #82 传播，Feedback Packet 应引用 Relay entry，而不是重新复制一份 theorem prose。

## 6. Canonical promotion 接入规则

反哺闭环不降低现有 promotion 门槛：

- owner research 可并行；
- canonical promotion 串行；
- latest-main integration 是最终组合面；
- bilingual/reference/quality/Lean 等门禁按改动范围适用；
- WIP、实验结果、物理解释或 branch ahead 数都不能自动升级 canonical 状态。

反哺协议只保证“好结果能回到底层”，不保证“所有结果都应该进底层”。

## 7. 回归实例

### FQ-20260809-004 —— 已闭合 canonicalized 样板

FQ-004 是第一条已经完整走通的 research-to-Foundation 样板。A1/A2 研究结果 RETURN 后，经 steward 独立复核并收窄到最小接口，再通过 clean canonical integration，由 PR #268 合入 `fe94a3201c4f6ca996c78cb55e719709d5144a54`；最终 `quality`、`bilingual-sync`、`reference-integrity` 全部成功。

其 canonical scope 是：

`typed state -> deterministic/observation functional kernel -> declared future-signature kernel`。

没有把整套 P018 substrate 上移：

- `State Pair = X×X` 是派生 carrier；
- Difference/defect/critical-grid 只有在针对任务证明 factorization/sufficiency 后才能代替底层状态；
- P023 继续拥有 future-compatible refinement/minimal repair 的一般构造；
- P024 继续拥有整数动作语言特化；
- A3 structured relation-state 与 A4 multivalued support 保持显式扩展层；
- generic kernel / behavioral-equivalence / partition-refinement machinery 属于成熟前人数学，不主张抽象本身原创。

该实例现在只保留在 `canonicalized_examples`，不再占 active scheduler link。

### FQ-20260809-005 —— 活跃调度样板

FQ-005 仍处于 `FQ_OPEN -> RESEARCH_SCHEDULED`：稳定 `graph_distance` API 的运行域比 P012 ordinary metric theorem domain 更宽。

它应由 A5/P012/P022 几何 owner 研究 API/domain layering，而不是由 foundation steward 直接选择“收窄 API”或“保留 directed helper”。`foundation_backflow.json` 已将该问题链接到 `program/p022-geometry-v2` 下独立的 `RS-P022-GRAPH-DISTANCE-API` research task；这**不会**改写另一条 `RS-P022-OBSERVATION-HISTORY` frontier，也不会事后重解释其任何 live lease。

这两个实例故意位于闭环两端，用于持续回归整条流程。

## 8. 完成判据

闭环健康时，任意重要 Foundation 候选都能回答：

1. 它最初在哪条研究/工具线上出现？
2. Feedback Packet 在哪里？
3. 为什么它是 direct maintenance、FQ，还是 local/not-ready？
4. 若需要研究，#240 哪个**显式声明该 FQ**的 task/owner 负责继续？
5. 研究答案在哪里返回，proof status 是什么？
6. steward 是否已经独立接受？
7. 哪个 current-main integration 把它变成 canonical？
8. 后续研究从哪里发现并消费新底层？

如果任一问题只能依赖某个对话的记忆才能回答，闭环仍未完成。