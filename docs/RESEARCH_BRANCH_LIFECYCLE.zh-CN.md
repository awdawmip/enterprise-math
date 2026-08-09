# Enterprise Math 研究分支生命周期 v2

状态：`PROPOSED / EXECUTABLE MIGRATION CONTRACT`  
生效候选：2026-08-09  
基线：`main@fbd95bc3d119c2429d3e83825b5cd44cd044e501`

## 1. 目的

Enterprise Math 已经进入多研究员、多路线并行阶段。长期数学归属、问题/应用身份、Git 分支历史三者必须分开。

核心原则：

> **数学的长期权威来自 `main` 与明确 theorem owner；Git branch 只是研究层级之间的短生命周期工作指针。**

发现历史由 commit/PR/tag 保存，不要求旧 branch 永久保持“活跃”。

本文件补充 `RESEARCH_ARCHITECTURE` 的 A0–A5 数学归属轴，增加独立的 Git 生命周期轴。两条轴不可混用：一个数学对象属于 A2/A3/A4，不意味着它必须永远住在某一条历史 branch 上。

---

## 2. 六层 Git 生命周期

### L0 — Canonical Main

唯一规范集成层：`main`。

允许内容：

- 已通过适用门禁的规范结果；
- canonical problem/status 文档；
- 可被所有下游直接依赖的实现、Lean、tests、lineage/prior-art；
- 已经完成 semantic replay 的 research result。

禁止：

- 直接把高度分叉的历史 research branch wholesale merge 进来；
- 仅凭 branch/PR 中存在就把问题状态升级为 `RESOLVED`。

### L1 — Core Owner

用于跨多个 P/E program 可复用的母定理。

当前候选：

- `core/a2-future-quotient`：future-compatible quotient / factorization / congruence / minimal repair；
- `core/a3-relation-state`：structured relation-state / partition quotient / kernel；
- `core/a4-admissible-support`：multivalued support/correspondence / witness algebra。

规则：

1. 每个 theorem family 只有一个 owner。
2. owner 必须使用尽可能弱的已证明假设。
3. P/E program 保留 specialization、应用、反例与 provenance，不复制母定理。
4. Core owner 不承担应用 benchmark、物理解释或工程 workload。

### L2 — Program Owner

用于编号问题或工程项目的当前前沿。

典型：

- `program/p017-legendre`；
- `program/p018-precision`；
- `program/p021-causal-focusing`；
- `program/p022-geometry`；
- `engineering/e001-collision`；
- `engineering/e001-material`；
- `engineering/e002-control`（仅在有活跃工作时存在）。

规则：

- Program 可以发现母定理，但必须 relay 到 L1，并在 owner 建立后只消费一般版本。
- Program 只拥有领域特化陈述，不把一般数学永久锁在应用 branch 中。

### L3 — Bridge / Probe

只解决两个 owner 之间一个明确的问题。

例如：

- `bridge/a3-a4-*`；
- `bridge/e001-e002-contact-*`。

Bridge 必须薄：

- 可以拥有“何时 factor / specialize / reconstruct / fail”的桥梁定理；
- 不得逐渐吸收任一端 owner 的整个 theorem family；
- 一旦一个 bridge result 变成独立可复用母定理，应上移到 L1；
- bridge 完成或失败后进入 L5，不成为长期 owner。

### L4 — Integration Replay

从**最新 main** 创建的一次性运输层。

唯一职责：

1. semantic replay 已筛选的 theorem；
2. 解决规范编号；
3. 同步中英文；
4. 搬运 executable specification/tests/Lean；
5. 更新 lineage/prior-art；
6. 运行仓库门禁。

硬规则：

> **Integration branch 不得产生新数学。**

若 replay 过程中发现新定理，立即回到对应 L1/L2/L3 owner 证明；integration 只消费稳定结果。

merge 后 integration branch 删除，PR 保留历史。

### L5 — Provenance / Archive

包含：

- 已被 main 完全吸收的旧 branch；
- superseded research branch；
- historical PR；
- immutable checkpoint tag；
- 发现来源 commit。

L5 不再接收新研究提交。

推荐：

- `checkpoint/*` 逐步改成 immutable tag；
- `agent/*` 若被吸收或 superseded，关闭 PR 后删除 branch ref；
- Git/PR/tag 历史承担 provenance，不依赖 branch 永久存在。

---

## 3. 状态分类

每条非 `main` branch 必须落在以下一个状态：

### `ACTIVE_OWNER`

仍有独有数学，且被明确指定为当前 L1/L2 owner。

### `ACTIVE_BRIDGE`

仍有独有桥梁结果，且问题边界明确。

### `INTEGRATION`

直接基于近期 main，正在做 semantic replay；禁止新数学。

### `REPLAY_REQUIRED`

有独有提交，但已高度分叉或混合多个 owner，禁止继续追加研究，必须从 latest main clean replay。

默认触发条件之一：

- `behind(main) >= 50` 且 branch 仍有独有提交；
- 一个 branch 同时包含两个以上 theorem owner；
- PR 已大到无法作为可审计的单一研究增量；
- branch 出现 canonical numbering/file-path collision。

### `ABSORBED`

`ahead(main)=0`。branch 对当前 main 已无独有提交。

处理：关闭/标注对应 PR，必要时留 tag，然后删除 branch ref。

### `PROVENANCE`

明确冻结的历史 branch/checkpoint，不参与当前研究调度。

---

## 4. 单向状态机

推荐生命周期：

`ACTIVE_OWNER / ACTIVE_BRIDGE`

→ theorem audit / relay

→ `INTEGRATION`

→ `main`

→ `ABSORBED`

→ `PROVENANCE`。

允许从 `REPLAY_REQUIRED` 新建 clean owner/integration branch，但**禁止通过反复 wholesale merge 把旧大树重新变成 current owner**。

---

## 5. ahead/behind 不是数学真理，但必须触发治理动作

- `ahead=0`：机械地说明当前 branch 没有 main 缺失的提交；默认降为 `ABSORBED`。
- `ahead>0, behind<20`：通常可作为普通 current-main replay / short program branch。
- `ahead>0, behind>=50`：默认进入 `REPLAY_REQUIRED`，除非有明确理由证明整条 history 仍应作为 owner。
- `ahead>100` 或 changed files 跨多个 theorem homes：无论 behind 数，优先 semantic distillation，不再扩大原 PR。

这些阈值是 Git 治理阈值，不是数学质量评价。

---

## 6. 当前大树的直接处置原则

### P018 `agent/p018-critical-grid`

属于 `REPLAY_REQUIRED`。

原因：已形成跨 pair/kernel、coalescence、context closure、operation congruence、transport/reusable-interface、quotient-basin 等多层的长树；并与 main 长期双向分叉。

下一 owner：

- 一般 future-compatible quotient 母定理 → A2/P023 owner；
- precision-specific state/kernel/context/transport → `program/p018-precision-v2`；
- square-basin/factor/proof specializations → P018 application supplements。

旧 #68 冻结为 provenance，禁止继续追加 Supplement。

### A3 `research/core/relation-quotient`

属于 `REPLAY_REQUIRED`。

新 owner：`core/a3-relation-state-v2`。

只 replay structured relation-state / partition quotient / kernel / guard-image 等 A3 所有内容；geometry、A4 correspondence、causal application 分流。

### A3/A4 `research/core/relation-support-bridge`

属于 `REPLAY_REQUIRED`。

新 bridge：`bridge/a3-a4-v2`，只 replay 真正 bridge theorem；semantic shadows/equitability/witness algebra 若是一般结果必须归明确 L1 owner。

### E002 v2 历史分支

多数 `ahead(main)=0`，应降为 `ABSORBED`；只保留仍有独有提交的当前小增量，再 clean replay 到统一 E002 program/integration branch。

---

## 7. 分支命名

长期可写 owner 只使用：

- `core/<home>`
- `program/<problem>`
- `engineering/<program>`

临时层使用：

- `bridge/<a>-<b>-<question>`
- `integration/<scope>-<date-or-stage>`
- `agent/<task>`（短期执行，不得成为长期 theorem owner）

`checkpoint/*` 不再新建；使用 immutable annotated tag。

---

## 8. PR 规则

- L1/L2/L3 PR 可以包含新数学。
- L4 integration PR 必须声明 `NO NEW MATHEMATICS`。
- 大于一个 theorem home 的 PR 必须拆分或标记 `REPLAY_REQUIRED`。
- `ABSORBED` PR 不因为历史重要而保持 open；PR 本身就是历史记录。
- stacked PR 只允许短链；不允许形成长期依赖 DAG。

---

## 9. 目标活动面

长期可写 branch 目标控制在约 8–12 条，而不是让每个阶段留下永久 ref。

建议稳定活动集合：

- A2 / A3 / A4 三个 core owner；
- P017 / P018 / P021 / P022 四个 program owner；
- E001 collision / material；
- 有工作时的 E002；
- 0–2 条 bridge。

Integration/agent branch 不计入长期活动面，完成后退出。

---

## 10. 不变量

任何整理都必须保持四个问题可回答：

1. 结果最初在哪里发现？
2. 最一般已证明形式现在由谁拥有？
3. 哪个 current owner 可以继续研究？
4. 哪些 program/application 仍消费它？

如果删除 branch ref 会让其中任何答案无法从 Git/PR/tag/lineage 恢复，就先补 provenance 再删除。
