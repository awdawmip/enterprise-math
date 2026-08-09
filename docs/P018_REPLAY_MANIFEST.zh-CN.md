# P018 v2 — Semantic Replay Manifest

状态：`ACTIVE REPLAY MANIFEST / NO NEW MATHEMATICS`  
目标 branch：`program/p018-precision-v2`  
基线：`main@c8aae69491fe50b107ca98b5777b9653be9f9aaf`  
主要历史源：`agent/p018-critical-grid@ee6d69fc2bb9894a47a3d5c6273d50d286047ca8` / PR #68  
其它历史源：`research/p018-graded-precision`、`research/p018-proof-certificates`、`research/p018-factor-precision`、`research/p018-centered-prime-radius`

## 1. 目的

本 branch 不是 #68 的 rebase，也不是 Supplements 12–26 的机械复制。

目标是把 P018 历史成果压成一个可以长期继续的**precision-specific program owner**，同时把已经变成一般 future-compatible quotient / operation-language theorem 的内容移交 A2/P023。

硬规则：

> replay manifest 与 integration 只做归属、重放、编号、实现和验证，不产生新数学。

若审计过程中发现新 theorem，停止 replay，回到对应 theorem owner 证明。

---

## 2. 五层目标结构

### P18-L1 — Precision State / Pair / Kernel

P018 保留：

- 有限 precision state 的 typed interpretation；
- State Pair 作为 subtraction-free comparison primitive；
- kernel/diagonal 对 precision observation 的解释；
- optional signed difference 作为 Pair 的坐标，而非底层原语；
- precision-specific critical-square/holonomy 表达。

主要 source assets：

- `state_pair.py`
- `critical_grid.py`
- `EnterpriseMath/State/CriticalGrid.lean`
- old #68 T110–T128 中 precision-specific statements。

归属：`KEEP_P018`。

### P18-L2 — Time / Coalescence / Spectrum Interface

P018 保留：

- precision observation 与 P010/P011 history merge 的接口；
- labelled kernel-time filtration；
- merge-time matrix 作为 precision/history 观察坐标；
- precision coarsening 对 P011 spectrum 的影响边界。

主要 source assets：

- `coalescence_time.py`
- `collision_increment.py`
- `merge_time_complex.py`
- `EnterpriseMath/State/Coalescence.lean`
- old #68 T129–T156 中 precision-facing corollaries。

一般 deterministic coalescence theorem 已属于 A1/P010/P011/P020 语境；P018 只保留 precision interface，不复制母定理。

归属：`KEEP_P018_COROLLARY` / `DEFER_A1_MOTHER`。

### P18-L3 — Observation Closure / Context Separation

P018 保留：

- “raw precision 是否足够承载声明的未来语言”这一 precision interpretation；
- context separation depth 作为“为什么 detail 必须保留”的有限证书；
- precision observation 在 closed / non-closed 情形的正负边界。

但以下一般结果移交 A2/P023：

- finite operation-family congruence criterion；
- largest compatible equivalence inside an observation kernel；
- generic predictive/contextual closure；
- generic minimum reusable interface。

主要 source assets：

- `observation_kernel.py`
- `predictive_closure.py`
- `contextual_closure.py`
- `context_separation.py`
- `EnterpriseMath/State/ObservationClosure.lean`
- `EnterpriseMath/State/OperationCongruence.lean`
- `EnterpriseMath/State/ContextSeparation.lean`

归属：

- precision interpretation / counterexamples → `KEEP_P018`；
- generic theorem implementation / Lean mother statements → `DEFER_A2_P023`。

### P18-L4 — Precision Transport

P018 保留：

- defect/response/carry 作为 precision projection 的 operation-specific transport；
- one-shot transport branching 在具体 precision observation 下的解释；
- persistent detail 与 transient correction token 的分层；
- radix addition/multiplication 等整数实例；
- carry/remainder structured composition。

一般 finite communication/interface theorem 移交 A2/P023 或独立 transport core 候选，不在 P018 重复维护。

主要 source assets：

- `transport_branching.py`
- `transport_fusion.py`
- `reusable_interface.py`
- `EnterpriseMath/State/TransportProtocol.lean`
- `EnterpriseMath/State/ReusableInterface.lean`
- existing `EnterpriseMath/Precision/Carry.lean`

归属：

- radix / precision-specific transport → `KEEP_P018`；
- generic protocol/interface minimum theorem → `DEFER_A2_P023`。

### P18-L5 — Arithmetic / Proof Applications

只保留 P018 应用与压力测试，不再把它们误当 general core：

- graded precision；
- finite proof certificates；
- factor precision；
- prime-gap slack / centered-prime-radius；
- square-basin quotient/root transport；
- all-power quotient transport；
- Legendre/P017 消费的 precision corollaries。

历史源：

- `research/p018-graded-precision`
- `research/p018-proof-certificates`
- `research/p018-factor-precision`
- `research/p018-centered-prime-radius`
- #68 中 QuotientBasin 相关资产。

归属：`APPLICATION_ONLY`，逐个 theorem 做 semantic absorption / replay audit。

---

## 3. Source asset 分类表

| Source asset/family | v2 classification | Target |
|---|---|---|
| State Pair / diagonal / pair coordinates | `KEEP_P018` | P18-L1 |
| Critical-grid endpoint/holonomy precision reading | `KEEP_P018` | P18-L1 |
| Generic deterministic coalescence | `DEFER_A1_MOTHER` | A1/main |
| Precision↔coalescence interface | `KEEP_P018_COROLLARY` | P18-L2 |
| Generic predictive closure | `DEFER_A2_P023` | A2/P023 |
| Generic operation congruence/descent | `DEFER_A2_P023` | A2/P023 |
| Context separation as precision certificate | `KEEP_P018` | P18-L3 |
| Generic contextual-equivalence algorithm | `DEFER_A2_P023` | A2/P023 |
| Carry/defect/radix transport | `KEEP_P018` | P18-L4 |
| Generic transport protocol minimum | `DEFER_A2_P023` | A2/P023 / future transport core |
| Generic reusable-interface theorem | `DEFER_A2_P023` | A2/P023 |
| Graded/factor/proof/prime/square applications | `APPLICATION_ONLY` | P18-L5 |
| Assets already exact on main | `ALREADY_MAIN` | consume, do not copy |
| Duplicate old numbering/prose only | `PROVENANCE_ONLY` | PR/Git history |

---

## 4. 编号策略

v2 **不继续沿用旧 branch 的 Supplement 27+**。

历史 T 编号继续作为 provenance 引用，但 clean replay 后优先使用概念文档/模块作为长期接口。只有需要进入 canonical theorem ledger 的 statement 才重新分配不冲突的规范编号。

禁止为了保留连续数字而覆盖 main 已经占用的 theorem id 或 Supplement path。

---

## 5. 第一重放批次

### Batch A — manifest + source audit

- 本文件；
- source→owner matrix；
- 检查 main 是否已有 exact/strict-generalization；
- 不搬运 theorem code。

### Batch B — P18-L1 precision state core

优先 replay：

- State Pair；
- precision-specific critical grid；
- 与 P009/P010 的精确接口。

### Batch C — P18-L3/L4 precision-specific context/transport

只 replay precision specialization；generic mother theorem 由 A2/P023 消费。

### Batch D — applications

逐小 branch 审计 graded/proof/factor/centered-prime/quotient-basin；已经在 main 的不重复 replay。

---

## 6. #68 冻结条件

PR #68 从本 manifest 建立起进入 `FROZEN REPLAY SOURCE`：

- 不再添加新 theorem / Supplement；
- 允许补充 provenance/迁移说明；
- 每个独有 source asset 必须最终映射到 `ALREADY_MAIN / KEEP_P018 / DEFER_* / APPLICATION_ONLY / PROVENANCE_ONLY` 中一个状态；
- 全部映射完成并重放后，#68 可以关闭而不删除 branch history。

---

## 7. 完成判据

P018 v2 压实完成时应满足：

1. current P018 owner 基于近期 main；
2. 不再复制 A2/P023 一般 closure/congruence theorem；
3. precision-specific state/context/transport 有清晰长期接口；
4. 历史 applications 逐个有 semantic audit；
5. old #68 与小历史 branch 均可降为 provenance；
6. 新研究不需要再读取 100+ commits 的旧树才能确定 theorem ownership。
