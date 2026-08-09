# Enterprise Math / 进取数论研究调度协议

状态：`ACTIVE / CANONICAL SCHEDULING CONTRACT`  
生效：2026-08-09  
范围：全部 L1 core owner、L2 program owner、L3 bridge/probe 与 L4 integration replay。

本协议用于消除 Architecture v2 迁移期间形成的调度歧义。旧迁移说明、replay manifest、branch ledger 或 Relay 文本如果可能被理解为“某条研究线必须等待另一条研究线”，其调度解释以本协议为准。

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

## 8. 调度状态机与对话接力

上述路线 heartbeat 由 `research_scheduler.json`、`tools/research_scheduler.py` 与实时 Research Dispatch Board Issue #240 落成可执行调度层。

scheduler 负责的是**谁来继续哪一个研究前沿**，不负责判定定理是否已证明、是否 canonical、是否具有 novelty、或是否已经可以晋升。

### 8.1 任务状态

持久任务前沿使用以下状态：

`BACKLOG -> READY -> CLAIMED -> IN_PROGRESS -> HANDOFF_READY -> DONE`

并有两个异常出口：

- `BLOCKED`：只允许由完整四字段 `HARD_BLOCK` 进入；
- `SUPERSEDED`：该任务前沿已被另一项明确任务替代。

`READY` 与 `HANDOFF_READY` 可被调度；`BACKLOG` 明确保持休眠。存在 live claim 的任务暂时租给一个执行者。已经完成或被替代的任务不会再被自动选择。

### 8.2 CLAIM 是可续期租约

`CLAIM` 是临时执行租约，不是永久占有。默认租约时长由 `research_scheduler.json` 声明。

- `PROGRESS` 续租并记录真实阶段成果；
- 没有更好进展事件可记录时，`HEARTBEAT` 用于续租；
- `HANDOFF` 主动释放任务，并且必须给出一个具体 `next_action`；
- 如果执行者消失而没有 handoff，租约到期后任务自动回到 `HANDOFF_READY / NEEDS_DISPATCH`；
- 第二个 claim 不能抢占尚未到期的 live lease；
- 租约过期、handoff、unblock 或其他合法释放后，新的对话可以重新 claim。

运行时事件以 `ENTERPRISE_MATH_SCHEDULER_EVENT_V1` 结构追加到 Issue #240。事件顺序按 GitHub comment 创建顺序确定；若时间相同，以 comment ID 作为次序。

### 8.3 新对话自动选取任务

用户当前显式指定的任务始终覆盖自动调度。

如果一个新的 Enterprise Math 研究对话没有由用户指定任务，它必须：

1. 读取 common surface、本调度协议、`research_scheduler.json`、owner isolation 与 Issue #240 live events；
2. 把所有合法运行时事件归约成当前任务状态；
3. 排除存在 live lease 的任务、已完成任务、blocked 任务以及休眠的 `BACKLOG`；
4. 优先选择 `HANDOFF_READY`，其次才是新的 `READY`，使被中断的研究优先接上而不是不断开新线；
5. 在同一状态层内，依次按 scheduler priority、跨路线 leverage、最旧 last-progress 时间、稳定 task ID 排序；
6. 在开始实质性 task-specific 研究前，先发布合法 `CLAIM`；
7. 在证明新内容前，刷新所选任务对应的 source PR/branch/Relay/canonical dependencies。

该选择规则是确定性的，因此多个 agent 看见同一状态时会选出同一个首选候选；真正并发领取时，以 GitHub 上第一个合法 CLAIM 事件获胜。

### 8.4 会话退出契约

研究会话不得从控制面静默消失。

未完成任务而准备结束会话时，必须发布 `HANDOFF`，至少包含：

- task ID 与当前 claim ID；
- 最近一次有意义的 commit/PR/Relay 或其他 progress reference；
- 一个具体的下一步数学/工程动作；
- 除非完整例外 blocker 确实成立，否则 `hard_block = NONE`。

只有 scheduler task 声明的 frontier 确实完成后才使用 `DONE`。Canonical promotion 仍是独立的 L4 lifecycle 操作，除非 promotion 本身就是该 scheduler task 声明的任务。

接力不要求下游 ACK。真正保证继续的是 scheduler，而不是另一个对话是否回复确认。

### 8.5 控制面一致性

`branch_governance_overrides.json` 是机器 owner registry；每一个 `ACTIVE_OWNER`/`ACTIVE_BRIDGE` 都必须获得 scheduler 覆盖，即使对应 scheduler task 被有意放在 `BACKLOG`。`tools/research_scheduler.py validate` 会检查这项覆盖并拒绝不完整的 hard-block 记录。

历史 branch ledger 仍可作为 provenance/snapshot 使用，但不再是实时执行者分配面。实时 dispatch 权威由 current owner registry + `research_scheduler.json` + Issue #240 runtime events 共同构成。

CI、review、L4 replay 或 moving `main` 可以改变 evidence/promotion 状态，但不得静默把 research task 变成 `BLOCKED`。

## 9. 与 Architecture v2 的关系

本协议保留 Architecture v2 的 theorem ownership 与 non-destructive replay 原则，只纠正错误的调度解释：

> 母定理归属唯一；知识全局共享；研究保持并行。

A0–A5 归属轴的作用是防止重复维护母定理，绝不能演变成串行依赖链。