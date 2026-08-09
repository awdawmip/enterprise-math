# Enterprise Math 当前研究分支账本

状态：`CANONICAL MIGRATION LEDGER / AUDITED STATE`  
快照：`main@7ca013f461716e0f9d3050e26970d598ef20ff8b`  
日期：2026-08-09

本账本记录当前**数学归属拓扑与已审计迁移状态**。具体活动 branch head 可能在该快照之后继续变化；实时 ancestry/scope 数据应使用只读 branch governance auditor。`ahead/behind` 单独永远不能证明数学已经被吸收。

当前治理文件为：

- `RESEARCH_ARCHITECTURE`：A0–A5 数学归属；
- `RESEARCH_BRANCH_LIFECYCLE`：L0–L5 branch 生命周期；
- `RESEARCH_SCHEDULING_PROTOCOL`：研究并行 / canonical promotion 串行；
- `RESEARCH_COMMON_SURFACE`：共享研究知识；
- `RESEARCH_OWNER_ISOLATION`：owner 负责研究，L4 integration 负责运输；
- `branch_governance_overrides.json` + `tools/audit_branch_lifecycle.py`：ancestry 与 scope-drift 审计。

## 1. 已进入 `main` 的可复用数学 home

### A2 — observation / future-compatible quotient

Canonical main 目前已经包含：

- P023 的 fiber/descent、minimum repair、operation-family refinement、word semantics 与 coarsest compatible quotient；
- `EnterpriseMath/Quotient/OperationCongruence.lean` 中的有限 arity 推广。

`core/a2-future-quotient-v2` 继续作为研究 owner/source，而不是 main 的滚动镜像。P024/material/contact 等 specialization 即使消费 A2，也不因此属于 A2 文件。

### A3 — structured relation state

Canonical main 已包含第一批干净 A3 core：

- `weighted_relation_field.py`；
- `relation_lattice.py`；
- `relation_scale.py`；
- 对应回归测试与 replay provenance。

该 core 拥有 capacity-weighted signed relation state、partition coarsening、primitive capacity shift、relation quantum 与 relation-scale carry。后续 A3 研究继续由 `core/a3-relation-state-v2` 承载。

### A4 — admissible support / correspondence

Canonical main 已包含第一批干净 A4 core：

- `admissible_support.py`；
- `relational_spectrum.py`；
- 自足 finite-relation 回归测试与 replay provenance。

A4 拥有 finite correspondence composition/common-target structure、split-completeness 边界、witness spectrum `W_k`、source-group spectrum `G_k`，以及 total-function 情形严格退化到 P011。后续 A4 研究继续由 `core/a4-admissible-support-v2` 承载。

## 2. 当前长期研究 owner

| Home | 当前 owner | 当前角色 |
|---|---|---|
| A2 | `core/a2-future-quotient-v2` | Canonical P023 之后的通用 quotient/factorization/compatibility 扩展 |
| A3 | `core/a3-relation-state-v2` | Structured relation-state、partition kernel/selector 扩展 |
| A4 | `core/a4-admissible-support-v2` | Correspondence/support、witness 与 relation algebra 扩展 |
| P017 | `program/p017-legendre` | 连续平方/Legendre pressure test，当前 discovery frontier |
| P018 | `program/p018-precision-v2` | Precision-specific pair/kernel/defect/transport 与 proof application |
| P021 | `program/p021-causal-focusing-v2` | Causal/focusing 应用 owner；第一批 causal-boundary 已完成 owner-level 验证 |
| P022 | `program/p022-geometry-v2` | Intrinsic geometry owner；A_p lattice core 加活动中的 HCP/Barlow 路线 |
| P024 | `program/p024-action-precision` | Closed-form action-language / threshold / boundary-pullback specialization program |

Owner 合法地可以落后于 `main`。不得仅为了“保持最新”而 whole-tree 同步 moving main。

## 3. 当前 bridge 拓扑

### A3 ↔ A4

当前 thin generation：

`bridge/a3-a4-generated-support-v3`

第一批故意只保留三个资产：

- canonical A3 `Z_ij` 生成 A4 support；
- 对应回归测试；
- replay manifest。

它直接消费 canonical A4 relation/common-target 操作，不复制实现。历史 B07+ metric/frontier/count/equitability 工作，在 owner 归属完成前都不 promotion。

历史 umbrella PR #83 仅作为 provenance/replay source。

### P017 ↔ P018

P017/P018 bridge 只有在假设确实同时需要 square-basin arithmetic 与 P018 quotient/root structure 时才属于 L3。bridge 不能演变成第二个 P017 或 P018 owner。

## 4. 已验证但尚未 canonical 的 owner slice

### P021 第一批

`program/p021-causal-focusing-v2` 已有 owner-level green checkpoint，包含：

- replay manifest；
- `causal_boundary.py`；
- `test_causal_boundary.py`。

验证后 PR 按设计回到 Draft。Canonical promotion 必须在未来从当时最新 main 新建 fresh L4 replay。

### P022 当前 owner

P022 正在同一个 theorem home 内快速推进，目前 owner 同时包含：

- replay 的 A_p/root-lattice geometry；
- HCP/geodesic multiplicity 与 Barlow-stacking 研究。

这是合法 same-owner growth，不是跨 home scope drift。Canonical promotion 应冻结并分批 replay 已验证切片，而不是等待整条活动 geometry owner 停止移动后一次 merge。

## 5. 已确认 provenance / superseded integration history

以下类别不得重新回到活动 owner 表面：

- 历史 P018 #68 长树：仅 replay/provenance source；
- 历史 A3/A4 #83 bridge 树：仅 replay/provenance source；
- 历史 P021 #48 与 P022 #50 umbrella：在 unique assets 完成分类前继续做 provenance；
- #56、#85、#123 等 obsolete whole-main synchronization PR：已按 Owner-Isolation 关闭；
- 旧 Architecture v1 #81：已由 canonical Architecture v2 取代；
- 被污染或 base 过期的 integration vehicle：保留 provenance，不再作为 merge vehicle；
- A2/A3/A4 的旧 validation/release PR：其 exact payload canonical 后即退出活动面。

是否删除 branch ref 只是可选清理；数学 provenance 由 commit、closed PR、lineage 与 manifest 承担。

## 6. Semantic absorption 规则

`ahead(main)=0` 是机械吸收的充分条件，但不是必要条件。

若 theorem/doc/code/test 资产已经以 exact blob，或经过明确审计的 equivalent/generalized canonical result 进入 main，那么即使 commit ancestry 不同，branch 仍可标为 `ABSORBED`。E002 task-observable 历史就是标准例子。

反过来，路径名或文件名相同不代表已经吸收。历史 P017/P018 branch 曾用相同 Supplement 编号/文件名承载不同数学，最终以 theorem/content audit 为准。

## 7. Scope-drift 规则

Owner purity 与 ancestry 是两个独立维度。

若 branch-side changes 只是因为同步其它 owner 或 whole main，而出现无关 theorem home 文件，就属于 `SCOPE_DRIFT`。真实迁移已经在 A2、A3、A4 和 lifecycle-tooling L4 上复现过这一故障。

恢复时保留全部历史，只把 current tree 恢复成声明的 owner/integration asset set，不做 force history rewrite。

Canonical auditor 现在从 merge-base 到 owner head 计算 branch-side changes，并与声明的 allowed paths/prefixes 比较。

## 8. Promotion pipeline

L1/L2/L3 的标准流：

`owner research -> freeze exact payload -> fresh L4 from latest main -> replay owner-only assets -> final combination gates -> main`。

只有 L4 必须追 current main，owner 不追。

Multi-owner L4 release 仅作为例外：每个 payload 必须先独立验证，combined release 必须显式、可审计。

## 9. 下一批压实任务

1. 完成三资产 A3↔A4 bridge owner-validation；若选中，再通过 fresh L4 promotion；
2. P021 的 causal-boundary slice 在 program boundary/prior-art 准备好后做 canonical L4；
3. P022 按有限切片 promotion，不等待整个活动 geometry owner 停止；
4. 逐 theorem/blob 审计旧 P017/P018 PR，只关闭真正被吸收的历史；
5. 将 P024 中通用 adjoint/stabilization formalization 上移 A0/A1，P024 只保留 action-language specialization；
6. 继续退出 pure synchronization PR 与 stale integration vehicle；
7. E001 engineering/material owner 与可复用 A2/A3/A4 数学继续严格分开。

## 10. 目标活动面

长期可写 refs 应大致维持为：

- A2 / A3 / A4 core owners；
- P017 / P018 / P021 / P022 / P024 program owners；
- 少量有明确范围的 E001 engineering/material owners；
- 0–2 条真正 thin bridge。

`integration/*` 与短期 `agent/*` 是运输/执行指针，任务结束后应退出。历史 discovery 不需要通过永久“活跃 branch”才能保留。
