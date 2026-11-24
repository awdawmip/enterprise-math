# POWER 研究问题发布与成果复用 — 2026-11-24

用户授权：将 POWER 审阅中值得进取数论研究的问题发布到中控，并在 POWER 开 PR 给出建议方向。本文件记录本次问题拆分与去重决定。

## 新发布的问题

| Task | 问题 | Publication | 母目标 |
|---|---|---|---|
| [RS-POWER-TASK-PRECISION-COMPILER-20261124](../research_tasks/RS-POWER-TASK-PRECISION-COMPILER-20261124.md) | 资源约束下的近似状态编译及任务变化后的可计算精度升级 | [TP2-D2EFEEFB3E6FCC346366](../research_task_records/RS-POWER-TASK-PRECISION-COMPILER-20261124/TP2-D2EFEEFB3E6FCC346366.json) | OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS / OG-7AE66316D7566C519AE0 |
| [RS-POWER-INCREMENTAL-FUTURE-QUOTIENT-20261124](../research_tasks/RS-POWER-INCREMENTAL-FUTURE-QUOTIENT-20261124.md) | 变化证据、动作与观察下的增量未来安全商 | [TP2-DD8B3B7291FF9E6FD8C0](../research_task_records/RS-POWER-INCREMENTAL-FUTURE-QUOTIENT-20261124/TP2-DD8B3B7291FF9E6FD8C0.json) | OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS / OG-7AE66316D7566C519AE0 |
| [RS-POWER-CERTIFIED-RESIDUAL-LATTICE-20261124](../research_tasks/RS-POWER-CERTIFIED-RESIDUAL-LATTICE-20261124.md) | 特殊算术残差格的保根构造与认证精度成本 | [TP2-3255B42C5DCC00A62CC7](../research_task_records/RS-POWER-CERTIFIED-RESIDUAL-LATTICE-20261124/TP2-3255B42C5DCC00A62CC7.json) | OBJ-POWER-RESEARCH-TRANSFER-20261124 / OG-F544DAB4BAD84437CB9D |
| [RS-POWER-FROBENIUS-SECTION-SEPARATION-20261124](../research_tasks/RS-POWER-FROBENIUS-SECTION-SEPARATION-20261124.md) | 循环 Frobenius 细粗层的双素数截面分离条件 | [TP2-65B32E1AB172F45CF517](../research_task_records/RS-POWER-FROBENIUS-SECTION-SEPARATION-20261124/TP2-65B32E1AB172F45CF517.json) | OBJ-POWER-RESEARCH-TRANSFER-20261124 / OG-F544DAB4BAD84437CB9D |

新 Task 采用独立未解问题的范围：资源约束近似编译及任务升级、变化模型下增量拆分与合并、特殊残差格的保根与认证成本、循环 Frobenius 双侧分离。前两项复用现有 OPEN geometry 目标，后两项绑定本次原生生成并选择的 OPEN 目标。已有固定模型的最小商、一般观察充分性、已完成计数及 δ_p 缺陷塔直接复用，不重新声明为新成果。

## 既有方向的处理

- 稀疏鲁棒观测：沿用 `RTASK-POWER-ROBUST-INTAKE-20260927`、`RTASK-POWER-ROBUST-MARK-GAP-20260927`、`RTASK-POWER-HIGH-ERASURE-SPARSE-20260927`、`RTASK-POWER-PROTECTED-CORE-TRADEOFF-20260927`。本次原生清单在 2026-11-24T11:19:49.760565+00:00 将四者投影为 READY / NEEDS_DISPATCH，保持原 publication、依赖和来源。旧 parent 字符串没有当前 objective generation，不把该历史字段充当本次新任务的父目标。
- CRT：`RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST` 已为 DONE / COMPLETE；publication `TP2-F3369CF79B942BBC9DAB`、Result `RR-79DED8D7DF67EEB5FB57`、Review `DR-A1CDCEE97F3295286EE6`。复用已接收的精确索引和完整计费边界，并向 POWER 指出实现校正；本次不重开相同研究问题。原窄范围负边界不推广到压缩、共享、摊销、rank-only/select-only 或其他排除范围。
- 相邻 future-faithful integration 保留自身 HANDOFF_READY 前沿；R1 observer-memory 保留自身 DORMANT/BLOCKED 状态。新任务没有接管这些 owner、claim 或结果。

## 发布依据与验证范围

- 发布身份：`EM-DVR-5F0F6F`，原生授权 `DA-9939899B5A3A045BEEE5`；[Source 事件](https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-7130056517)。
- 本次创建任务与目标，不 CLAIM、运行或完成任何科研 Task，不授予 Working Truth、Foundation 或数学接纳。
- 使用当前源 `tools/research_task_records.py` 的 prepare、严格 `_prepared`、语义字段保留 build_record、逐条父目标 operational-tenure 证明及实际任务/目标 audit。所有调用保留真实契约、兼容性记录和相应 Driver 来源；没有手写政策 PASS。
- 验证作用域为四个新 Task、一个新 Objective 及所需加载依赖；远端逐项确认新 Task/目标不存在，当前源与准备源比较未修改相关控制契约或父目标。不是全仓重审。
- 任务书、精确 blob pin 的不可变 publication、Objective generation/head/selection receipt 在一个 Git 事务中同时发布，非强制 CAS 保留其他作者的写入。
- 原始审阅固定于 POWER `5561f5a792cd0e43473b326c9bd6ebdc2076a2f5`；相关底座已核对到 `049bc552ec90820094ecfdb4013d71cb1a668386` 且未改变；新增85号端到端管线不在已复算范围。

## 可复用来源

- [原始审阅记录](https://github.com/awdawmip/chatgpt-global-knowledge/blob/ae6894814c8637560bd1e1d4b6dbc0131ddbc788/journal/power/2026-11-24/20261124T190334%2B0800-power-source-review-5561f5a.md)
- [本次实际 preflight 记录](../research_control/POWER_DIRECTIONS_PREFLIGHT_20261124.json)
- 各任务书列出固定源码、相关既有 Task 及验收。POWER 建议 PR 的最终链接在账户级本次交付日志中保存。
