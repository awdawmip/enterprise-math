# Enterprise Math 当前研究分支账本

状态：`MIGRATION LEDGER / AUDITED SUBSET`  
首次审计基线：`main@fbd95bc3d119c2429d3e83825b5cd44cd044e501`  
当前复核主干：`main@c8aae69491fe50b107ca98b5777b9653be9f9aaf`  
日期：2026-08-09

本账本记录已经通过 Git compare、blob 对比、PR 元数据或 theorem/path 语义检查确认的关键 refs。`ahead/behind` 只是治理信号；是否真正吸收以 `RESEARCH_BRANCH_LIFECYCLE` 的 semantic audit 为准。

## 1. 已确认 `ABSORBED`

### 1.1 机械吸收：`ahead(main)=0`

| Branch | 结果 | 处置 |
|---|---|---|
| `agent/e001-material-foundation` | ahead=0 | provenance only |
| `agent/p017-multiplicative-resource-capacity` | ahead=0 | provenance only |
| `research/p018-all-power-quotient-basin-final` | ahead=0 | provenance only |
| `research/p023-composition-safe-collapse` | ahead=0 | provenance only |
| `research/p023-safe-selector-semigroup` | ahead=0 | provenance only |
| `research/e002-horizon-saturation-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-precision-locked-actuation-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-precision-native-hysteresis-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-predictive-quotient-compiler-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-vector-actuation-v2` | ahead=0 | absorbed E002 generation |

### 1.2 语义吸收：Git ancestry 不同，但资产已进 main

`research/e002-task-observable-v2`：Git 仍显示 `ahead=2`，但本轮已确认：

- `docs/E002_TASK_RELATIVE_OBSERVABLE_SUPPLEMENT_05.en.md` 与 main blob 完全相同；
- `src/enterprise_math/precision_task_observable.py` 与 main blob 完全相同；
- `tests/test_precision_task_observable.py` 与 main blob 完全相同。

因此其独有 commit ancestry 不代表独有数学；当前归类为 `ABSORBED / SEMANTIC`，**不再建立重复 integration replay**。

结论：旧 E002 v2 generation 已整体退出活动研究面；未来 E002 从 current main 新建短 task/program branch。

## 2. 已实际关闭的同步壳

### PR #56 — `Sync canonical main into P018 Stage 9`

状态：`CLOSED / PROVENANCE`。

原因：纯同步 PR，无新数学；Architecture v2 禁止继续用 wholesale sync 维持长期分支。

### PR #85 — `A3 dependency sync into relation-support bridge`

状态：`CLOSED / PROVENANCE`。

原因：dependency-only owner→bridge 同步；以后由 latest-main semantic replay 替代。

## 3. 老 PR 的零风险关闭审计

本轮对以下旧分支重新 compare current main。它们**仍有独有数学，不能关闭**：

| PR / Branch | ahead | behind | 当前结论 |
|---|---:|---:|---|
| #22 `research/p005-multibase-scale-algebra` | 3 | 372 | `SEMANTIC_REPLAY_AUDIT_REQUIRED` |
| #21 `agent/legendre-basin-aggregate` | 4 | 372 | `SEMANTIC_REPLAY_AUDIT_REQUIRED` |
| #23 `agent/legendre-mirror-separation` | 6 | 372 | `SEMANTIC_REPLAY_AUDIT_REQUIRED` |
| #54 `research/p018-centered-prime-radius` | 35 | 317 | `REPLAY_REQUIRED` |
| #65 `research/p017-rough-window-recursion` | 20 | 262 | `REPLAY_REQUIRED` |

特别边界：P017 历史中存在**同一个 Supplement 文件名后来承载不同研究内容**的情况。例如 old `LEGENDRE_PRESSURE_TEST_SUPPLEMENT_06` 与 current main 同名文件并非同 blob/同 theorem family。因此**文件名相同绝不是吸收证据**。

## 4. P018

### `agent/p018-critical-grid` / PR #68

当前审计量级：约 `ahead=121`，且 behind 已超过 100；changed files 横跨 pair/kernel、coalescence、context separation、operation congruence、predictive closure、transport、reusable interface、quotient basin、Supplements 12–26。

状态：`REPLAY_REQUIRED / FROZEN`。

禁止：继续向 #68 追加 Supplement 27+。

重放分工：

- A2/P023 一般 future-compatible quotient / congruence / minimal repair → core owner；
- P018 precision-specific pair/kernel/context-depth/transport → `program/p018-precision-v2`；
- quotient basin/factor/proof specializations → P018 application layer。

### P018 小历史分支

| Branch | 独有量级 | 状态 |
|---|---:|---|
| `research/p018-graded-precision` | 5 commits | replay audit |
| `research/p018-proof-certificates` | 6 commits | replay audit |
| `research/p018-factor-precision` | 5 commits | replay audit |
| `research/p018-centered-prime-radius` | 35 commits | replay audit |

它们与 #68 一起作为 source，不 rebase 旧历史。

## 5. A3 / A4

### `research/core/relation-quotient`

状态：`REPLAY_REQUIRED / FROZEN`。

树已达到数百 ahead/behind commits 并混入 relation-state、guard、causal、geometry 等多类资产。

目标 owner：`core/a3-relation-state-v2`；只 replay A3 structured relation-state / partition quotient / kernel / guard-image / task-derived relation precision。

### `research/core/admissible-support-relations`

状态：`ACTIVE_OWNER -> MIGRATE TO core/a4-admissible-support-v2`。

仍有独有 admissible-support/common-collapse 资产；新 owner 不再继承 E001 工程历史。

### `research/core/relation-support-bridge` / PR #83

状态：`REPLAY_REQUIRED / FROZEN`。

目标：`bridge/a3-a4-v2`，只保留真正 bridge theorem。一般 witness/count/shadow/equitability theorem 必须明确归一个 L1 owner。

## 6. P017

P017 继续是 program owner，但历史 Stage refs 不再全部保持 active。

已抽查：

| Branch | ahead | behind | 处置 |
|---|---:|---:|---|
| `agent/p017-lower-band-root-overlap` | 6 | 148（早期审计） | small semantic replay |
| `agent/p017-full-core-crt-stacked` | 6 | 96（早期审计） | small semantic replay |
| `agent/p017-multiplicative-resource-capacity` | 0 | — | absorbed |
| `agent/legendre-basin-aggregate` | 4 | 372 | replay audit |
| `agent/legendre-mirror-separation` | 6 | 372 | replay audit |
| `research/p017-rough-window-recursion` | 20 | 262 | replay audit |

未来 P017 新研究从 `program/p017-legendre` 或 latest-main 短 task branch 继续。

## 7. E001 / E002 contact stack

当前：PR #101 → #108 → #113。

状态：`ACTIVE_BRIDGE` 短链。

允许完成当前 T38–T42 压力测试；完成后：

1. 一般 future-language quotient/gcd/semigroup 结果上移 A2/P023；
2. contact specialization 留 E001/E002；
3. 从 latest main 建单一 clean replay；
4. #101/#108/#113 归档。

## 8. E001 engineering/material

- PR #70：`PROVENANCE + REPLAY SOURCE`，不再增长一般数学；
- PR #95：`PROVENANCE / REVIEW UNIQUE DELTA`；
- PR #114/#115：current-main clean replay，作为推荐模式。

## 9. P021 / P022

历史 PR #48/#50 保留 provenance，不 wholesale merge。

- P021 → `program/p021-causal-focusing-v2`：只 replay causal/direction 专属结果；
- P022 → `program/p022-geometry-v2`：只 replay lattice/metric/balls/radial/distance-carry；A3 generic machinery 分流。

## 10. Architecture

旧 PR #81 / `chore/research-architecture-v1`：`SUPERSEDED BY V2 REPLAY`。

新 PR #121 / `chore/research-architecture-v2`：current-main 双亲同步，承载 A0–A5 数学归属轴 + L0–L5 Git 生命周期轴 + 本 ledger。

#121 通过门禁后关闭 #81。

## 11. 下一批动作

1. #121 真实门禁；
2. E002 v2 refs 按 semantic-absorbed 归档，不重复 replay；
3. 建 `program/p018-precision-v2` semantic replay manifest；
4. 冻结 #68 并建立 source→owner 映射；
5. 建 A3/A4 v2 owners + thin bridge；
6. P017 old stages 逐 theorem audit；
7. P021/P022 clean replay；
8. 最终删除 absorbed branch refs / checkpoint 改 tag。

## 12. 活动面目标

长期 writable refs 控制在约 8–12 条。Git/PR/tag 保存历史；branch refs 只表示当前研究前沿或短期运输任务。
