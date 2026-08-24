# Enterprise Math / 进取数论研究调度协议

状态：`ACTIVE / CANONICAL SCHEDULING CONTRACT / V2`  
生效：2026-08-24  
范围：全部 L1 core owner、L2 program owner、L3 bridge/probe、L4 integration replay，以及共享 Driver 审核工作。

本协议用于消除 Architecture v2 迁移以及后续任务/审核扩张过程中形成的调度歧义。旧迁移说明、replay manifest、branch ledger、Relay 文本或静态 scheduler 条目如果可能被理解为“某条研究线必须等待另一条研究线”或“某项任务/审核私有绑定到一个对话”，其调度解释以本协议为准。

## 1. 第一不变量：研究并行，规范晋升串行

Enterprise Math 必须区分两类活动：

- **研究/发现**：新证明、反例、构造、工具、实验、领域特化；
- **规范晋升**：语义归属审计、编号、中英文 replay、reference/lineage 登记、最终仓库门禁以及合入 `main`。

研究/发现默认并行。只有规范晋升在仓库一致性确有必要时才串行。

某个依赖对 theorem ownership 或未来 integration 有必要，**不等于正在进行的研究必须等待它**。

## 2. `defer` 不等于 blocker

`defer`、`consume from`、`owner moved`、`audit against`、`replay after`、`depends on owner` 以及同义路由文字，只表示：

> 本路线不要复制母定理，也不要过早把它提升为自己的规范结果。

它们绝不自动表示：

> 停止本路线，等另一条 branch 完成以后再研究。

只要缺失结果并不妨碍提出和检验问题，本路线就继续。可以使用已证明的上游定理、把下游结果写成条件定理、构造例子/反例、推导特化、或精确隔离真正缺失的 lemma。

## 3. 只有显式 `HARD_BLOCK` 才允许停止

一条路线只有同时记录以下四项时才允许等待：

```text
HARD_BLOCK:
  missing_object: <精确缺失的定理/数据/实验/产物>
  owner: <负责路线或外部来源>
  necessity: <为什么不存在有意义的独立下一步>
  unblock_condition: <什么精确条件满足后恢复>
```

少任何一项，都不是 hard block。

`HARD_BLOCK` 应极少出现。只要还能证明条件定理、寻找反例、削弱假设、构造 executable oracle、验证特例、或攻击同路线的另一个 open frontier，就不属于真正 blocked。

## 4. L1/L2/L3 owner 始终允许产生新数学

- L1 core owner：允许并且应当继续产生新的可复用母定理；
- L2 program owner：允许并且应当继续产生 program-specific 数学、应用、反例和候选推广；
- L3 bridge/probe：在其声明的桥梁问题范围内允许新数学；
- L4 integration replay：**NO NEW MATHEMATICS**。

如果某个 L1/L2/L3 owner branch 的 replay manifest 写有

`no_new_mathematics_during_replay = true`

该约束只作用于明确标识的 replay slice 或 replay 操作，绝不能冻结整个 owner branch。

如果搬运某个 replay slice 时发现了新定理，应回到正确的 L1/L2/L3 research frontier 记录和证明；不得把新数学偷偷塞进 L4 transport commit。

## 5. `main` 持续移动不是研究 blocker

如果 `main` 每推进一次就重建同一份已验证结果，会形成 integration livelock。

改用以下规则：

1. 用 source commit/blob/theorem identity 冻结已经证明的语义 payload；
2. 其他研究照常继续；
3. 真正准备晋升时再创建或刷新 L4 integration replay；
4. merge 前只需针对当时 current `main` 做一次最终 combination gate；
5. 如果 `main` 只是加入无关变化，不得因此创建新的 research generation，也不得重新证明；
6. 只有新 `main` 造成真实语义冲突或使某项假设失效，才重新进入研究。

因此要求的是**最终合并状态兼容**，不是追逐每一个中间 `main` head。

## 6. Relay 下游动作四分类

今后的跨路线 Relay 条目必须把 requested downstream action 明确归入且仅归入以下一种：

- `INFORM`：提供有价值上下文；继续研究不需要先处理；
- `CONSUME`：应复用该结果，不再复制母定理；
- `TEST`：适合时进行压力测试、桥梁验证或反例搜索；
- `HARD_DEPENDENCY`：下游当前声明的 frontier 确实无法在缺少该结果时继续。

只有 `HARD_DEPENDENCY` 才可能形成 `HARD_BLOCK`，而且下游自己仍必须记录上述四个 `HARD_BLOCK` 字段。

下游没有 ACK，不阻断上游继续推进。

## 7. 路线 heartbeat

每条 active owner 都应能给出：

```text
frontier: <当前数学问题>
hard_block: NONE | <HARD_BLOCK 记录>
last_progress: <commit/PR/Relay result>
shared_surface_seen: <main SHA 或 common-surface revision>
```

只要 `hard_block = NONE`，该路线就应继续研究，而不是等待另一个对话、branch、review 或 replay。

## 8. 统一任务/审核状态机与对话接力

上述路线 heartbeat 由以下控制面共同落成可执行状态：

- `research_scheduler.json` / `tools/research_scheduler.py`：保留作为旧任务状态归约器；
- `research_work_state_machine.json` / `tools/research_work_state.py`：负责任务发布、安全通用领取以及 Driver 审核状态；
- append-only Research Dispatch Board Issue #240：作为共享事件日志。

控制面负责的是**谁执行哪项已选择任务、谁审核哪份研究返回**，不负责判定定理是否已证明、是否 canonical、是否具有 novelty、或是否已经可以晋升。

冻结：

`USER != MANUAL_TASK_OR_REVIEW_MESSAGE_BUS`。

### 8.1 任务状态与发布 generation

持久任务前沿继续沿用：

`BACKLOG -> READY -> CLAIMED -> IN_PROGRESS -> HANDOFF_READY -> DONE`

并有两个异常出口：

- `BLOCKED`：只允许由完整四字段 `HARD_BLOCK` 进入；
- `SUPERSEDED`：该任务前沿已被另一项明确任务替代。

但静态 `READY` 本身不再足以进入通用自动领取队列。

对新批准或重新审核的 taskbook：

`TASKBOOK_DISPATCH_PASS -> SAME_TURN_TASK_PUBLISH`。

`TASK_PUBLISH` 必须记录不可变的 `taskbook_ref=path@commit`、发布 Driver-ID 和当前 routing 字段。对同一 task-id，最新合法 publication 是当前 generation。该 publication 之前旧 generation 的 DONE/SUPERSEDE/CLAIM 等 runtime 事件保留为 provenance，但不得直接改变新 generation 的状态。

通用领取只允许：

1. 当前已发布 task generation；
2. 确实存在 reducer 接受的 runtime 执行历史、需要 continuation/handoff 恢复的旧任务。

从未实际执行过的历史静态 `READY`/`HANDOFF_READY` 条目仍可作为 provenance 查看，但不能悄悄重新进入通用队列。

### 8.2 CLAIM 是可续期租约

`CLAIM` 是临时执行租约，不是永久占有。默认租约时长由任务/调度契约声明。

- `PROGRESS` 续租并记录真实阶段成果；
- 没有更好进展事件可记录时，`HEARTBEAT` 用于续租；
- `HANDOFF` 主动释放任务，并且必须给出一个具体 `next_action`；
- 如果执行者消失而没有 handoff，租约到期后任务回到 `HANDOFF_READY / NEEDS_DISPATCH`；
- 第二个 claim 不能抢占尚未到期的 live lease；
- 租约过期、handoff、unblock 或其他合法释放后，新的对话可以重新 claim。

旧任务 runtime 事件继续兼容 `ENTERPRISE_MATH_SCHEDULER_EVENT_V1`；统一层也可把 `ENTERPRISE_MATH_WORK_EVENT_V1` 中兼容的 task runtime event 归一到旧 reducer。事件权威以 append-only board comment 顺序为准。

### 8.3 研究员通用领取：`领任务`

用户当前显式指定的任务始终覆盖通用选择。

`领任务`、`领取任务`、`claim task` 及同义指令，明确表示“从共享状态领取 TASK”，它不同于 FREE Phase-A，也不同于“一个没有指定主题的普通对话”。

收到通用领取后，研究员必须：

1. 读取完成本次选择所需的统一 work-state 规则与当前 board events；
2. 归约当前已发布/runtime-continuation 任务状态；
3. 排除 live lease、已完成/已替代、合法 blocked、休眠 BACKLOG，以及未发布的陈旧 legacy READY；
4. 在共享可领取队列中优先 `HANDOFF_READY`，其次 `READY`；
5. 在同一状态层按 priority、leverage、最旧已接受 progress、稳定 task-id 排序；
6. 在实质 task-specific 研究开始前发布合法 `CLAIM`；
7. 通过 claim 解析/分配 Researcher-ID；
8. 若存在 publication，则读取精确 `taskbook_ref`，随后只展开启动所需第一批 dependency；
9. 不向用户索取 task-id 或 handoff prompt，直接开始任务。

该规则是确定性的；并发领取由第一个合法 append-only CLAIM 决定。

FREE Phase A 永远不会因为这个通用领取命令而被自动调度进入。

### 8.4 研究完成与审核请求

共享状态中的研究会话不得从控制面静默消失。

未完成任务准备退出时，发布 `HANDOFF`，至少包含 task/claim id、最近 progress ref 和一个具体 next action。

只有声明 frontier 真正完成后才使用 `DONE`。对于需要审核的共享任务，在同一个语义 checkpoint 还必须追加 `REVIEW_REQUEST`，包含：

- review id / task id；
- originating Researcher-ID；
- 若 task publication 可知，则带发布 Driver-ID；
- 精确 review objective；
- target refs；
- evidence refs；
- execution-log refs；
- requested checks；
- priority。

冻结：

`RESEARCH_DONE -> SAME_TURN_DONE_EVENT + REVIEW_REQUEST`。

用户不再负责把研究返回、日志、task-id 或审核指令复制到另一个对话。

### 8.5 Driver 通用领取审核：`领审核`

Driver 收到 `领审核`、`领取审核`、`claim review` 或同义指令时，即表示从共享审核队列领取工作。

审核使用与 task claim 类似的可续期 lease，并支持 `REVIEW_PROGRESS`、`REVIEW_HANDOFF`、`REVIEW_DONE` 和 `REVIEW_SUPERSEDE`。

不存在发布者私有锁：

`TASK_ISSUER != REQUIRED_REVIEWER`。

任何 active Driver 都可以领取 pending review。选择顺序先看 review state 和 priority；在其他条件相当时，优先把审核交给与 task-issuing Driver-ID 不同的 Driver，然后按更早 request 时间排序。不能为了追求形式上的交叉审核而把一个 P0 review 压在更低优先级工作之后。

如果暂时没有其他 Driver，同一个 Driver 可以兜底审核，但必须显式标记 same-Driver review；这不会仅因存在审核记录就变成 independent replication。

`REVIEW_DONE` 必须保存 verdict、findings、evidence refs、next action、method-harvest classification 与 successor disposition。

真值边界继续冻结：

`SCHEDULER_DONE != THEOREM_TRUTH`。

`REVIEW_DONE != CANONICAL_MAIN`。

Foundation 与 promotion gate 保持独立。

### 8.6 控制面一致性

`branch_governance_overrides.json` 继续作为机器 owner registry。`research_scheduler.json` 继续作为旧 durable coverage surface。对新批准/重审 task generation，`TASK_PUBLISH` 是当前发布面；task/review runtime event 是实时 lease/result surface。

历史 branch ledger 和未经发布的旧 scheduler 行仍然是 provenance/snapshot，不是自动执行者分配面。

CI、review、L4 replay 或 moving `main` 可以改变 evidence/promotion 状态，但不得静默把 research task 变成 `BLOCKED`。

政策更新可以使某个 taskbook 对未来 dispatch/publication 变 stale，但不得追溯抹除正在执行的 frozen research execution。

## 9. 与 Architecture v2 的关系

本协议保留 Architecture v2 的 theorem ownership 与 non-destructive replay 原则，只纠正错误的调度解释以及 user-relay 瓶颈：

> 母定理归属唯一；知识全局共享；任务与审核进入共享状态；研究保持并行。

A0–A5 归属轴的作用是防止重复维护母定理，绝不能演变成串行依赖链或私有审核链。
