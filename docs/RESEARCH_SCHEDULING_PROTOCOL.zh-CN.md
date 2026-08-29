# Enterprise Math / 进取数论研究调度协议

状态：`ACTIVE / CANONICAL SCHEDULING CONTRACT`  
生效：2026-08-29  
范围：全部 L1 core owner、L2 program owner、L3 bridge/probe 与 L4 integration replay。

本协议用于消除调度歧义，同时冻结一个操作优先级：**研究是热路径；GitHub 只做稀疏协调和耐久溯源，不做逐步研究遥测。**

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

治理、task registry publication、scheduler 状态、CI、review、identity registration、移动中的 `main` 或 pending workflow，本身都不是数学 `HARD_BLOCK`。

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

## 7. 路线状态是语义检查点，不是 heartbeat 税

一条 active owner 应当能够重建：

```text
frontier: <当前数学问题>
hard_block: NONE | <HARD_BLOCK 记录>
last_durable_progress: <确有的 commit/return/checkpoint/Relay result>
shared_surface_seen: <确有需要时读取的 canonical snapshot>
```

这是可恢复性要求，不是要求每一步都去写或刷新记录。

冻结：

`ROUTINE_RESEARCH_STEP -> NO_GOVERNANCE_WRITE_REQUIRED`。

`NO_NEW_DURABLE_PROGRESS -> NO_HEARTBEAT_REQUIRED_BY_DEFAULT`。

`PENDING_CI_OR_REVIEW -> CONTINUE_INDEPENDENT_SAFE_WORK; DO_NOT_POLL_AS_PROGRESS`。

`HEARTBEAT` 事件只保留为 legacy compatibility：在确实需要续 owner lease、又没有更好的语义 progress event 时才使用。它**不是**周期研究义务，也不得作为 owner-scope session liveness 证据。

## 8. 恢复优先的 live dispatch 状态机与对话接力

规范 live scheduling/control route 是：

`research_control_dispatch.py`。

它在 fresh selection 之前先处理 stale-owner recovery，并组合：

- post-cutover immutable task publications：`research_task_records/<task-id>/<publication-id>.json`；
- 仅作冻结 legacy task baseline 的 `research_scheduler.json`；
- recovery-aware live router：`research_control_dispatch.py`；
- ordinary merged fresh selector/reducer：`tools/research_dispatch.py`；
- active-cohort fresh lane selector：`tools/research_lane_dispatch.py`；
- live runtime coordination：Research Dispatch Board Issue #240；
- result/review overlays：`research_result_records/` 与 `research_result_reviews/`。

`tools/research_dispatch.py` 继续作为规范的**任务定义 / 普通 fresh selection** reducer；它不负责 stale-session adoption，也不能单独给出全局 `NO_DISPATCH` 结论。

冻结：

`STALE_SESSION + VALID_OWNER_CLAIM -> ADOPT_EXISTING_WINNING_CLAIM_WITHOUT_NEW_CLAIM`。

`FRESH_SELECTOR_EMPTY + VALID_OWNER_UNKNOWN_LIVENESS -> VERIFY_SESSION_LIVENESS`。

`FRESH_SELECTOR_MISS != NO_DISPATCH`。

`tools/research_scheduler.py` 继续作为 **legacy event reducer/config validator primitive**，但不再是 post-cutover task-definition authority。

scheduler 负责的是**谁来继续哪一个研究前沿**，不负责判定定理是否已证明、是否 canonical、是否有 novelty、或是否已可晋升。

### 8.1 任务存在与状态

对 post-cutover 工作：

`TASKBOOK_FILE != OFFICIAL_TASK`。

`IMMUTABLE_PUBLICATION_RECORD_CREATED -> OFFICIAL_TASK_EXISTS`。

ordinary merged dispatch view 派生的运行状态包括：

`NEEDS_DISPATCH`、`LEASED`、`AWAITING_REVIEW`、`BLOCKED`、`COMPLETE`、`DORMANT`。

历史 `READY`、`HANDOFF_READY`、`CLAIMED`、`IN_PROGRESS`、`DONE`、`SUPERSEDED` 等 task-state 名称继续作为兼容输入/派生细节。

已冻结 return 但尚待 Driver review 的任务是 `AWAITING_REVIEW`，不得再次派给 researcher；有 terminal reviewed result 后才是 `COMPLETE`。

### 8.2 一条 CLAIM，不建立 pre-claim GitHub 事务链

对新的 registered execution，**Issue #240 上唯一一条 `CLAIM` 评论本身就是 execution authorization envelope**。它携带或解析：

- exact task ID 与 current `publication_id`；
- claim ID；
- Researcher-ID 或其确定性推导信息；
- theorem owner；
- execution branch 与 exact base commit；
- allowed output paths/prefixes；
- owner lease duration。

冻结：

`VALIDATE_CURRENT_PUBLICATION -> CREATE_OR_VERIFY_BRANCH -> ONE_CLAIM -> RESEARCH`。

不要求另行提交 pre-claim execution-record commit、PR、merge、CI wait 或第二条 GitHub comment。

immutable execution record 可在 CLAIM 后为了耐久溯源再物化，并与第一次真正的研究 checkpoint 或最终 return 同批提交。

### 8.3 由 GitHub server 认证的 Issue #240 事件

一条 live registered runtime event 就是一条 Issue #240 comment。认证复用**同一条评论**，不会多写第二条。

canonical live-event envelope 来自 GitHub server metadata：

- `comment_id`：事件排序权威；
- `user.login`：认证后的 GitHub author provenance；
- `created_at`：事件/lease 时钟权威；
- `updated_at`：编辑检测；
- exact comment body 的 SHA-256：payload pin。

JSON body 中的 `actor` 与 `at` 只保留为描述性 provenance，不再具有认证或时钟权威。

冻结：

`SERVER_COMMENT_ID > BODY_DECLARED_ORDER`。

`SERVER_CREATED_AT > BODY_DECLARED_AT`。

`EDITED_EVENT_COMMENT -> NOT_RUNTIME_AUTHORITY`。

如果事件需要纠正，应追加新的 correction/superseding event；不得编辑旧 scheduler event 改写历史。

裸 V1 event object 只保留给明确的 historical replay/unit-test compatibility，不能作为 immutably registered task 的 live authority。

### 8.4 CLAIM、owner lease 与 owner-scope session liveness

`CLAIM` 是临时 task-ownership lease，不是永久占有，也不是 exact winning owner scope 仍活跃的证明。

`OWNER_LEASE != OWNER_SCOPE_SESSION_LIVENESS`。

`CONVERSATION_ACTIVITY != OWNER_SCOPE_SESSION_LIVENESS`。

- `PROGRESS` 可续 owner lease 并记录真实 checkpoint；
- `HEARTBEAT` 只有确有需要时才续 owner lease，默认不周期发送，而且不构成 session liveness 证据；
- owner-scope session liveness 只能由独立核验、且绑定 exact current winning `claim_id` 与 task/lane scope 的 `TASK_RESEARCH_RESPONSE` 或 `DURABLE_EXECUTION_PROGRESS` 刷新；
- Control-plane、Driver、Steward、FREE、其他 task/lane、generic chat，以及没有 durable task progress 的 CI/status 活动，都不能刷新一个已暂停的 Researcher claim；
- `HANDOFF` 主动释放 claim，并给出具体 `next_action`；
- legacy reducer 下 owner claim 过期后回到可恢复/可调度状态；
- 第二个合法 claim 不能抢占 live lease；
- owner-scope session stale 时，如果 winning owner claim 仍有效，可在验证 durable frontier 后 adopt 同一 claim，而不是强等 owner lease 到期。

### 8.5 新对话自动路由

用户当前显式指定的任务始终覆盖自动调度。

如果新的 Enterprise Math task-research conversation 没有用户指定任务，且适用 automatic dispatch，则应：

1. 读取 current Common Surface 与本协议；
2. 把 `research_control_dispatch.py` 作为 top-level route；存在独立可核验信息时提供 exact owner-scope liveness observations；
3. 如果 action 是 `ADOPT_OWNER_CLAIM`，验证 durable frontier 后采用**同一个** winning claim，不创建第二个 claim；
4. 如果 action 是 `VERIFY_SESSION_LIVENESS`，先解析 exact owner-scope activity，不能据此推断没有任务；
5. 只有 action 是 `CLAIM_NEW_OWNER` 时，才接受 subordinate fresh selector 选出的 task/lane，并在实质 task-specific research 前发布一条合法 server-backed `CLAIM`；
6. 在证明新内容前，只刷新所选任务真正相关的 source/taskbook/branch dependencies。

不得仅因为直接调用 `tools/research_dispatch.py` 得不到 fresh candidate 就推断 `NO_TASK` / `NO_DISPATCH`。不得预加载整个仓库，不得为了开始研究而轮询 CI，不得追逐 moving `main`，也不得在 claim 后反复重读 Issue #240，除非出现真正 coordination boundary。

并发领取由 GitHub server comment-ID 顺序中的第一条合法 CLAIM 决胜。

### 8.6 会话退出与 result contract

研究会话在有意义边界应留下可恢复 durable frontier，但不能因为一个 turn 要结束就制造无意义 GitHub write。

只有未完成任务确实需要移交给另一个 executor 时才发布 `HANDOFF`，至少包含：

- task ID 与 current claim ID；
- 最近一次真正 durable progress reference；
- 一个具体 next action；
- 除非完整例外 blocker 成立，否则 `hard_block = NONE`。

如果同一个 conversation 只是继续工作、没有转交需求，不需要 HANDOFF。

到达 declared return boundary 时才 freeze result。对 registered task，`DONE` 必须经过 canonical result/review lifecycle；一句裸 DONE 不能自行关闭任务。

handoff 不要求下游 ACK。

### 8.7 控制面一致性

`branch_governance_overrides.json` 继续作为 theorem/owner registry。新 task existence 来自 immutable task publication；frozen scheduler file 只作 legacy baseline。Foundation task links 必须通过 canonical merged dispatch view 解析。

历史 branch ledger 和旧 scheduler row 仍可作为 provenance/snapshot，但不是 live new-task publication authority。

CI、review、L4 replay 或 moving `main` 可以改变 evidence/promotion 状态，但不能静默把 research 变成 `BLOCKED`。

## 9. 交互预算不变量

控制面不能成为研究的主要工作量。

在真正 semantic checkpoint 之间，默认预算为：

- governance-only repository writes：**0**；
- CI polling：**0**；
- review polling：**0**；
- moving-main chase：**0**；
- mandatory scheduler heartbeat：**0**。

允许的稀疏边界包括 task publication、一条 claim、有真实价值时的 durable research checkpoint、frozen return、Driver review/disposition 与最终 integration/promotion。

未来任何规则若要增加 GitHub 操作，必须证明所需信息无法装进已经必需的 semantic-boundary artifact/event；否则属于 control-plane regression。

## 10. 与 Architecture v2 的关系

本协议保留 Architecture v2 的 theorem ownership 与 non-destructive replay 原则，只纠正错误调度解释：

> 母定理归属唯一；知识全局共享；研究保持并行；控制持久化保持稀疏。

A0–A5 归属轴用于防止重复维护母定理，绝不能演变成串行依赖链或 GitHub polling loop。
