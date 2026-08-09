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

## 8. 与 Architecture v2 的关系

本协议保留 Architecture v2 的 theorem ownership 与 non-destructive replay 原则，只纠正错误的调度解释：

> 母定理归属唯一；知识全局共享；研究保持并行。

A0–A5 归属轴的作用是防止重复维护母定理，绝不能演变成串行依赖链。