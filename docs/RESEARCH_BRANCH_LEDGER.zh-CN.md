# Enterprise Math 当前研究分支账本

状态：`MIGRATION LEDGER / AUDITED SUBSET`  
审计基线：`main@fbd95bc3d119c2429d3e83825b5cd44cd044e501`  
日期：2026-08-09

本账本不是永久手工真相；它记录本轮已经通过 Git `compare` / PR 元数据确认的关键 refs，并为后续自动 ledger 提供初始分类。

状态定义见 `RESEARCH_BRANCH_LIFECYCLE`。

## 1. 已确认 `ABSORBED`

以下 branch 在本轮 compare 中满足 `ahead(main)=0`，即当前 main 已包含其全部提交：

| Branch | 结果 | 处置 |
|---|---|---|
| `agent/e001-material-foundation` | ahead=0 | 历史 provenance；不再作为活动 owner |
| `agent/p017-multiplicative-resource-capacity` | ahead=0 | 归档 branch ref |
| `research/p018-all-power-quotient-basin-final` | ahead=0 | 归档；all-power 结果以后只从 main 消费 |
| `research/p023-composition-safe-collapse` | ahead=0 | 归档；P023 后续从 current main 新 owner 继续 |
| `research/p023-safe-selector-semigroup` | ahead=0 | 归档 |
| `research/e002-horizon-saturation-v2` | ahead=0 | E002 generation 已吸收 |
| `research/e002-precision-locked-actuation-v2` | ahead=0 | E002 generation 已吸收 |
| `research/e002-precision-native-hysteresis-v2` | ahead=0 | E002 generation 已吸收 |
| `research/e002-predictive-quotient-compiler-v2` | ahead=0 | E002 generation 已吸收 |
| `research/e002-vector-actuation-v2` | ahead=0 | E002 generation 已吸收 |

规则：确认相关 PR/lineage 能恢复 provenance 后，关闭 stale PR 并删除 branch ref；必要时以 tag 固定审计锚。

## 2. E002 generation 尾部

`research/e002-task-observable-v2`：

- `ahead=2`
- `behind=64`

状态：`REPLAY_REQUIRED`，但体量很小。

处置：从 latest main 建一次性 `integration/e002-task-observable-current`，只 replay 这 2 个独有提交对应的 task-observable theorem/doc/test/lineage；通过门禁后整个旧 E002 v2 branch family 退出活动面。

## 3. P018

### `agent/p018-critical-grid` / PR #68

审计：

- `ahead=121`
- `behind=146`
- changed files 横跨 pair/kernel、coalescence、context separation、operation congruence、predictive closure、transport、reusable interface、quotient basin、Supplements 12–26。

状态：`REPLAY_REQUIRED / FROZEN`。

禁止：继续向 #68 追加 Supplement 27+。

重放分工：

- A2/P023 一般 future-compatible quotient / congruence / minimal repair → core owner；
- P018 precision-specific pair/kernel/context-depth/transport → `program/p018-precision-v2`；
- quotient basin/factor/proof specializations → P018 application layer。

### P018 小历史分支

| Branch | ahead | behind | 状态 |
|---|---:|---:|---|
| `research/p018-graded-precision` | 5 | 337 | `REPLAY_REQUIRED` |
| `research/p018-proof-certificates` | 6 | 336 | `REPLAY_REQUIRED` |
| `research/p018-factor-precision` | 5 | 335 | `REPLAY_REQUIRED` |

三者不 rebase/merge；与 #68 的有效资产一起从 latest main 组装 P018 v2。

## 4. A3 / A4

### `research/core/relation-quotient`

审计：数百 commits ahead/behind，且 tree 已混入 relation-state、guard、causal、geometry 等多类资产。

状态：`REPLAY_REQUIRED / FROZEN`。

目标 owner：`core/a3-relation-state-v2`。

只 replay A3 structured relation-state / partition quotient / kernel / guard-image / task-derived relation precision。

### `research/core/admissible-support-relations`

审计：仍有独有 admissible-support/common-collapse 资产。

状态：`ACTIVE_OWNER`，但应在 architecture v2 生效后迁为 `core/a4-admissible-support-v2`，避免继续从 E001 历史继承工程资产。

### `research/core/relation-support-bridge` / PR #83

审计：高度分叉且已拥有大量 staged support/count/witness/equitability/semantic-shadow 结果。

状态：`REPLAY_REQUIRED / FROZEN`。

目标：`bridge/a3-a4-v2`。

只保留真正 bridge theorem；一般 witness/count/shadow theorem 必须明确归 A2/A3/A4 或其他 core owner。

### PR #85 `A3 dependency sync into relation-support bridge`

状态：`OBSOLETE SYNC PATTERN`。

新 lifecycle 禁止用长期 wholesale sync PR 维持 bridge；应关闭，以 semantic replay 代替。

## 5. P017

P017 继续是 program owner，但历史大量 `agent/legendre-*` / `integration/p017-*` 不应全部保持活跃。

已抽查：

| Branch | ahead | behind | 处置 |
|---|---:|---:|---|
| `agent/p017-lower-band-root-overlap` | 6 | 148 | small semantic replay |
| `agent/p017-full-core-crt-stacked` | 6 | 96 | small semantic replay |
| `agent/p017-multiplicative-resource-capacity` | 0 | 198 | `ABSORBED` |

目标：所有 P017 新研究从 `program/p017-legendre` 或从 latest main 的短 task branch 继续；不再让每个 Stage 成为长期 branch。

## 6. E001 / E002 contact stack

当前：

- PR #101 `predictive Boolean-contact quotient bridge`；
- PR #108 `symmetric contact action-family gcd quotient`；
- PR #113 `contact semigroup versus group-completion precision`。

这是一条短期 stacked bridge 链，不应成为长期三 owner。

状态：`ACTIVE_BRIDGE`，允许完成当前 T38–T42 压力测试；完成后：

1. 一般 future-language quotient/gcd/semigroup 结果上移 A2/P023；
2. contact specialization 留 E001/E002；
3. 从 latest main 建一个 clean replay PR；
4. #101/#108/#113 全部归档。

## 7. E001 engineering/material

### PR #70 historical E001 collision

状态：`PROVENANCE + REPLAY SOURCE`。

工程 workload 与 benchmark 继续属于 E001；一般 support/correspondence 数学已迁 A4。禁止继续在 #70 扩大一般理论。

### PR #95 stacked material response

状态：`PROVENANCE / REVIEW FOR UNIQUE DELTA`。

已有 current-main clean replay 的 material foundation/validation PR，应只审计 #95 是否还有未重放的独有 material-response probe；无独有资产后关闭。

### PR #114 / #115

属于正确模式：从 current main clean replay、增量小、边界明确。作为未来 E-series integration 范例。

## 8. P021 / P022

历史 PR #48/#50 保留 provenance，不 wholesale merge。

- P021 下一 owner：`program/p021-causal-focusing-v2`，从 latest main clean replay causal/direction 专属结果；一般 witness-sufficiency 上移 core。
- P022 下一 owner：`program/p022-geometry-v2`，只 replay lattice/metric/balls/radial/distance-carry；A3 generic relation machinery 不跟随。

## 9. Architecture

旧 PR #81 / `chore/research-architecture-v1`：

状态：`SUPERSEDED BY V2 REPLAY`。

本轮 `chore/research-architecture-v2` 从 current main 重放数学归属原则，并新增 Git lifecycle。V2 门禁通过后关闭 #81。

## 10. 第一批动作顺序

1. 合入 architecture v2 + lifecycle + ledger。
2. 关闭明确 obsolete 的 sync/provenance PR（优先 #56、#85；再审计 ahead=0 对应 PR）。
3. replay `e002-task-observable-v2` 的 2 个独有提交。
4. 建 `program/p018-precision-v2`，冻结 #68。
5. 建 A3/A4 v2 owners + 薄 bridge。
6. P017 小批 replay。
7. P021/P022 clean replay。
8. branch refs 最终清壳。

## 11. 活动面目标

长期 writable refs 控制在约 8–12 条；其余要么是短期 agent/integration，要么是 Git/PR/tag provenance，不再被下一位研究员误认作并行 current owner。
