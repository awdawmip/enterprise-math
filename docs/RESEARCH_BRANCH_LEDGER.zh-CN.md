# Enterprise Math 研究分支快照

状态：`CANONICAL ADVISORY SNAPSHOT / NOT LIVE DISPATCH AUTHORITY`  
快照基线：`main@0ef6f40bf925c4fa759e7865b269e2f27fc23ecb`  
日期：2026-08-10

本文档是一份经过审计的**归属/来源快照**。它明确不是实时调度器，也不应因为每一次 branch head 或 `main` 移动就重写。

实时执行权威按以下顺序确定：

1. 当前用户明确指令；
2. `branch_governance_overrides.json`：可写 owner/bridge 状态与 scope；
3. `research_scheduler.json`：持久任务定义；
4. Research Dispatch Board Issue #240：claim、lease、progress、handoff 与 block；
5. `docs/RESEARCH_COMMON_SURFACE.*` / `research_common_surface.json`：可复用 canonical theorem/tool 路由。

`ahead/behind` 只是 Git 信号，永远不是数学归属或创新性的证明。

## 1. 当前长期研究表面

在本快照中，机器 owner registry 共有 12 条长期 `ACTIVE_OWNER` / `ACTIVE_BRIDGE` 路线。

| Home | 可写路线 | 类型 | Scheduler task |
|---|---|---|---|
| A3 | `core/a3-relation-lattice-v3` | L1 owner | `RS-A3-RELATION-LATTICE` |
| A3 ↔ A4 | `bridge/a3-a4-generated-support-v3` | L3 bridge | `RS-A3-A4-GENERATED-SUPPORT` |
| P017 ↔ P018 | `bridge/p017-p018-hard-core-v2` | L3 bridge | `RS-P017-P018-ANALYTIC-MASS` |
| A2 ↔ E001 | `bridge/a2-e001-material-markov` | L3 bridge | `RS-A2-E001-MATERIAL-MARKOV` |
| P017 | `program/p017-legendre` | L2 owner | `RS-P017-GLOBAL-CAPACITY` |
| P018 | `program/p018-precision-v2` | L2 owner | `RS-P018-TERNARY-CARRY` |
| P021 | `program/p021-causal-focusing-v3` | L2 owner | `RS-P021-FOCUSING-DIRECTION` |
| P022 | `program/p022-geometry-v2` | L2 owner | `RS-P022-OBSERVATION-HISTORY` |
| P024 | `program/p024-action-precision` | L2 owner | `RS-P024-HIGHER-ACTION-PRECISION` |
| P025 | `program/p025-abc-support-collapse` | L2 owner | `RS-P025-WITNESS-PRECISION` |
| E001 impulse | `engineering/e001-material-impulse-v2` | L2 owner | `RS-E001-IMPULSE-V2` |
| E001 contact network | `engineering/e001-material-contact-network` | L2 owner | `RS-E001-CONTACT-NETWORK` |

本快照下，owner registry 与 scheduler coverage 集合严格相等。Scheduler task 在运行时可以处于 `BACKLOG`、`READY`、`HANDOFF_READY`、leased、blocked 或 complete；**不要把运行时状态复制进本文档**，应直接读取 Issue #240。

## 2. 已完成的 canonical 压实

以下可复用层/切片已经进入 `main`；其历史 validation/replay branch 不再是 current owner：

- A2/P023 通用 descent、future-compatible quotient 与有限 arity operation congruence；
- 第一批干净 A3 weighted relation-state / relation-lattice / relation-scale core；
- 第一批干净 A4 admissible-support / relational-spectrum core；
- 薄 A3→A4 generated-support/cancellation executable bridge；
- P021 finite causal-boundary executable core；
- P022 `A_p` root-lattice executable core；
- P022 geodesic-multiplicity/HCP、periodic Barlow stacking、task-relative Barlow precision 与 periodic-growth executable slices（至 L4 #296）；
- P018 centered-prime-radius executable remainder，以及从历史 #54 保存的详细 proof note（至 L4 #297）；
- canonical E001 wall/pair impulse 及其它明确 promotion 的 application slices；
- E001 measured-polyline area refinement 与 refinement-variation 切片，冻结源 #227 的资产已经通过 #264 promotion。

Canonical executable 文件存在本身不会自动把其中所有陈述升级为 `PROVED`；theorem/proof 状态仍由 canonical theorem 文档、Lean 覆盖与 Relay/provenance 控制。

## 3. Provenance 与已吸收 generation

已经退出可写研究表面的典型 branch/PR generation 包括：

- 历史 P018 长树 `agent/p018-critical-grid` / PR #68；
- A2/A3/A4 v2 owner generation，在选定 core promotion 后退出；
- P021 v2，在 causal-boundary promotion 后退出；
- E001 one-body impulse-world、pair-impulse、multi-action generation，在各自 L4 后退出；
- `engineering/e001-measurement-area-refinement` / source PR #227：Git ancestry 仍显示 ahead，但四个 owner-scoped source/test blob 已经通过 #264 与 canonical `main` 逐字节一致，因此该冻结 generation 是 provenance，而不是可写 owner；
- payload 已机械或语义吸收的 E002 v2 generations；
- obsolete whole-main synchronization PR；
- P005 #22、P022 geodesic validation #220 等在 exact payload 已 canonical 后退出的 validation/publication shadow。

关闭 PR 或删除 branch ref 不会删除数学来源：discovery commit、closed PR discussion、lineage 与 replay manifest 仍可恢复。

## 4. 仍需语义 replay 的历史树

当前机器 registry 将以下历史树保留为 `REPLAY_REQUIRED`，而不是可写 owner：

- `research/core/relation-quotient` —— 历史 mixed A3 source；
- `research/core/relation-support-bridge` —— B01–B06 已抽取后的历史 broad A3/A4 source；
- `bridge/a3-a4-v2` —— obsolete broad bridge generation；
- `engineering/e001-material-state-cost` —— 带上游 A2/E001 依赖的 stacked E001 application branch。

`REPLAY_REQUIRED` 的含义是：保留历史、停止扩张混合旧树、逐项判定 theorem home，并将选中的 still-unique payload 通过 fresh L4 发布。它**不**意味着 wholesale merge/rebase。

## 5. 语义吸收规则

一个 branch 只有在不存在仍缺失于 `main` 的 branch-owned semantic asset 时才算 absorbed。

常见证明方式有两种：

1. 机械吸收：`ahead(main)=0`；
2. 语义吸收：ancestry 不同，但 theorem/doc/code/test/lineage 已以 exact、equivalent 或 strict-generalization 形式进入 `main`，并且没有剩余独有 specialization/counterexample。

路径名/文件名相同不够。历史 P017/P018 曾复用 supplement 编号与文件名承载不同数学；最终由内容/theorem audit 决定。

这次退出的 E001 measurement owner 是第二种证明的标准例子：冻结 owner head 与 current main 虽然 ancestry 不同，但四个 changed path 的 Git blob ID 全部精确相同。

## 6. Owner isolation 与 promotion

L1/L2/L3 owner 合法地可以落后 moving `main`。不得仅为“保持最新”而 whole-tree merge/rebase/copy `main`。

Canonical publication 固定为：

`owner/bridge research -> freeze exact payload -> one L4 integration -> shared-surface delta or explicit N/A -> applicable gates -> one final current-main combination gate -> main -> provenance`。

L4 **NO NEW MATHEMATICS**。如果 replay 暴露新 theorem，必须先回到正确 owner。

验证期间无关的 `main` 前进不会生成新的 replay generation。只检查实际 intervening delta，在同一 integration line 中解决真实 overlap，然后执行一次 final combination gate。

## 7. Scheduler 与 Foundation 边界

Scheduler state 只协调工作，不证明 theorem，也不提升 canonical truth。

当一个 owner generation 已降为 provenance 且没有声明新的 frontier 时，其冻结 scheduler task 应一并退出，而不是保留一条假的可写路线。未来若出现真正不同的问题，应创建新的 owner generation 与新的显式 task，而不是悄悄重新激活已经吸收的 source branch。

Foundation question 的权威在 Foundation Problem Set Issue #164。Research answer 必须经过独立 steward verification 才能进入 Foundation integration。Active tool/interface alert 在被明确解决前始终保持 active；仅仅存在 scheduler task ID，不代表对应数学/接口问题已经被回答。

## 8. 本快照的维护规则

只有当**长期 ownership/provenance 拓扑**发生实质变化时才刷新本 ledger，例如：

- 注册新的长期 owner/bridge；
- 某个 owner generation 降为 provenance；
- 历史 mixed tree 完成全部成果归宿审计；
- promotion/control-plane contract 本身改变。

以下情况不要刷新：

- `main` 前进；
- owner head 前进；
- lease 换人；
- CI/review 状态变化；
- 出现短期 task/integration branch。

实时 dispatch 永远读取机器 owner registry、scheduler config 与 Issue #240。
