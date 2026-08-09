# Enterprise Math / 进取数论研究架构 v2

状态：`PROPOSED / MIGRATION IN PROGRESS`  
基线：`main@fbd95bc3d119c2429d3e83825b5cd44cd044e501`  
日期：2026-08-09

## 1. 双轴架构

Enterprise Math 使用两条彼此独立但必须一致的组织轴：

1. **数学归属轴 A0–A5**：回答“最一般已证明陈述由谁长期维护”；
2. **Git 生命周期轴 L0–L5**：回答“当前工作应该在哪类 branch 上发生，以及何时退出活动面”。

P/E 编号继续表示研究问题、工程项目与发现来源，不等于母定理的永久存放位置。

治理原则：

> 发现位置永远可追溯；最一般已证明陈述只维护一次；branch 只是短生命周期工作指针。

术语相似不构成统一。只有明确证明 `same / strict generalization / specialization / independent / conflict` 关系后才能调整 theorem ownership。

---

## 2. 数学归属轴

### A0 — Primitive Discrete State Algebra

主要来源：P001–P009。

对象：整数根、完全幂坍缩、精确 quotient/remainder、signed-state distinction、total scale factor、typed transition、order adjunction、composition、commutation、fixed points。

A0 已有大量规范结果进入 main；具体 resolved scope 始终以 `PROBLEM_STATUS` 为准。

### A1 — Functional Dynamics / Kernel / Stabilization

主要来源：P010、P011、规范 P019、P020，并与 P018 相连。

对象：单值确定映射、functional kernels/fibers、strict history merge、collision spectrum、eventual coalescence、finite stabilization。项目通用的 functional-kernel / declared-future-signature 语言已经通过 FQ-004 进入 `FOUNDATIONS`。

函数图只是后续 relation/correspondence 的特殊情形，但 A1 不因推广存在而失去规范地位。

### A2 — Observation / Future-Compatible Quotient

主要来源：P018、P023，应用来自 E001/E002/P017/P021。

对象：

- observation equivalence；
- operation factorization / congruence；
- finite predictive/contextual closure；
- minimum exact repair；
- reusable interface；
- future-language sufficiency；
- canonical P018↔P023 quotient-root power-free action basis 等精确有界 future-action language 结果。

归属纪律：

- **P023/core A2** 候选拥有最一般 operation-language/future-compatible quotient 母定理；
- **P018** 保留 precision-specific interpretation、defect/response、context depth、transport 与数值实例；
- E/P applications 只保留领域 specialization。

### A3 — Structured Relation-State Algebra

历史来源：`research/core/relation-quotient`；当前可复用 executable assets 统一通过 `docs/RESEARCH_COMMON_SURFACE.*` 与 `research_common_surface.json` 路由。

核心对象是 structured weighted integer state，例如

`Z_ij = m_j c_i - m_i c_j`，

而不是任意二元 relation。

首批 canonical executable core 已经进入 `main`：`weighted_relation_field.py`、`relation_lattice.py`、`relation_scale.py`。更广的 candidate theorem family 包括 partition quotient、kernel、relation rank/scale、guard-image lattice、refinement memory、task-derived exact relation precision。每个 theorem 必须保留其真实 canonical/WIP 状态；module 已进入 main 不会自动把未 promotion 的 theorem 升级为已证明规范结果。

A3 暂不分配新的 P 编号，也不是 Foundation。后续可复用数学必须以最弱已证明假设陈述，并经过 prior-art audit 后才能 canonical promotion。

### A4 — Admissible Support / Correspondence Algebra

历史来源：E001 relational-collapse 及 admissible-support continuation；首批 canonical executable core 已进入 `main`：`admissible_support.py`、`relational_spectrum.py`。

核心对象：有限多值 correspondence `R ⊆ X×Y`。

Candidate theorem family 包括：

- functional vs relational collapse；
- admissible support families；
- relation composition/common targets；
- split-completeness boundary；
- MAY/MUST support semantics；
- witness/event spectra；
- function-graph degeneration 回 P011。

A4 与 A3 是 sibling cores，不因共享“relation”一词而合并。Canonical executable assets 可立即共享复用；更广 theorem statement 仍保持自己的证明/promotion 状态。

### A3↔A4 Bridge

只有以下类型的陈述属于 bridge：

- A3 state 在什么条件下生成某类 A4 support；
- A4 observable 在什么条件下 factor through A3 quotient；
- 为保留某个 A4 future query，A3 哪些 internal relations 不能删除；
- 两边何时严格不等价的 counterexample。

首批 executable bridge slice `a3_a4_support_bridge.py` 已 canonical 进入 `main`。这不意味着 A3/A4 合并成一个 owner，也不意味着所有历史 bridge theorem 已自动 promotion。若一个 bridge theorem 已脱离两端语义成为一般组合定理，就必须上移到明确 core owner。

### A5 — Intrinsic Discrete Geometry

主要来源：P012、P022。

对象：primitive adjacency、integer shortest-path metric、lattice/root-lattice、balls/shells、radial/quadratic observations、distance carry、geometry-specific contraction。

依赖方向优先写成：

`primitive geometry -> admissible supports -> observations -> future-compatible precision -> application decision`。

几何可以消费 A2/A3/A4，但一般 relation algebra 不应因为发现于 geometry branch 就永久留在 P022。

---

## 3. Program / Application 轴

当前主要 program：

- P017：Legendre / consecutive-square pressure test；
- P018：finite precision calculus；
- P021：causal horizon / focusing；
- P022：minimum-precision geometry；
- P023：composition-safe / future-compatible quotient；
- E001：collision/material engineering probes；
- E002：precision-native control / actuation / task observables；
- P016：物理 falsification contract。

Program 可以发现母定理，但必须向 A0–A5 owner 提炼；program branch 保留 specialization、实验语义、反例、benchmark 与 provenance。

---

## 4. 已确认的跨路线归属

### P017 → P018/A2

square-basin quotient/root transport 若不需要 prime 假设，母定理归 precision/quotient 层；P017 保留 least-factor/lower-band 应用。

### P018 ↔ P023

unary predictive closure 与 operation-family quotient-safety 属于同一母问题的不同范围。一般 operation-language closure 应只维护一次；P018 保留 precision interpretation 和 defect/transport consequences。已经 canonical 的有界 quotient-root power-free action basis 是两条路线共同可消费的 specialization，必须持续保持共享可发现。

### P021 → A2 / witness algebra

direction transport 已证明 cardinality shadow 不自动保留未来 composability。一般“先证明 identity 可删除，才能压缩 witness”原则不应在 P021 内另建平行理论。

### P011 → A4

multivalued support 可以推广 collision/witness spectrum，但 total-function graph 必须显式退化回 P011，且不能继承在 relation 下会失败的单值 monotonicity。

### E001/E002 → A2

contact/action-family/gcd/semigroup 等结果若本质是 future-language minimal quotient，母定理进入 A2/P023；contact/material/collision specialization 留工程 program。Canonical E001 executable specialization 可以作为跨路线 pressure test/tool 共享，但不会因此变成通用物理定律。

### P022 ↔ A3/A4/A2

geometry-only 结果留 P022；structured relation-state 上移 A3；support/correspondence 上移 A4；future-safe erasure 条件上移 A2。

---

## 5. Theorem lifting protocol

当任意 program/bridge 出现可复用结果：

1. 冻结精确 source branch/commit/result payload 与 provenance；
2. 逐个移除领域假设，找最弱已证明 hypotheses；
3. 搜索 lineage / Relay / common surface / 既有 theorem family；
4. 分类为 `same / strict generalization / specialization / independent / conflict`；
5. 只选一个 mother statement owner；
6. source program 留 corollary + provenance；
7. promotion 开始时，在 current `main` snapshot 上创建或协调一条 L4 integration，同时保持冻结 source-result identity；
8. replay theorem + implementation + tests + Lean + bilingual prose + lineage/prior-art + shared theorem/tool surface；
9. 若验证期间 `main` 前进，只检查真实 intervening delta；无关变化不生成新的 replay generation；
10. 通过仓库门禁（适用时包括 shared-surface integrity gate），再做一次 final current-main combination gate 后 merge；
11. 旧 branch 按 lifecycle 进入 `ABSORBED/PROVENANCE`。

禁止仅靠 merge/rebase 解决高度分叉的数学归属问题。若一个可复用结果进入 `main` 后仍无法通过 `docs/RESEARCH_COMMON_SURFACE.*` / `research_common_surface.json` 被发现，则 canonical promotion 仍不完整。

---

## 6. 与 Git 生命周期的绑定

数学 owner 与 Git branch 必须满足：

- A0/A1 已规范结果通常直接由 main 承载；
- A2/A3/A4/A5 活跃母定理在 L1 core owner；
- P/E 前沿在 L2 program owner；
- bridge theorem 在 L3；
- 进入 main 只能经过一次性 L4 canonical integration；
- 历史 branch/PR/checkpoint 最终进入 L5。

具体状态、阈值、命名、moving-main combination 规则、当前迁移批次见 `RESEARCH_BRANCH_LIFECYCLE.*`、`RESEARCH_SCHEDULING_PROTOCOL.*` 与 `RESEARCH_BRANCH_LEDGER.*`。

---

## 7. 当前强制冻结的大树

以下历史树禁止继续通过追加新 theorem 来扩大：

- `agent/p018-critical-grid` / PR #68；
- `research/core/relation-quotient`；
- `research/core/relation-support-bridge` / PR #83。

它们是 semantic replay source，不再作为未来 canonical owner。历史树冻结并不会阻塞 current writable L1/L2/L3 owner 上的新数学。

---

## 8. Research Relay

跨路线可复用 theorem、严格推广、重要 counterexample、precision obligation 继续通过 Research Relay 协调。

Relay 是发现/消费总线，不取代 theorem owner，也不把 relay issue 变成 canonical truth。

每个一般 theorem 至少记录：

- source commit；
- exact statement；
- weakest known hypotheses；
- relation class；
- intended owner；
- affected consumers；
- requested downstream action。

Canonical promotion 后必须把可复用结果从“只在 Relay 可见”迁移到 human/machine common surface。

---

## 9. 压实成功的判据

一个研究员进入仓库后，应能快速回答：

1. 当前 canonical main 是什么？
2. 哪些 P/E 是 active programs？
3. 一般 theorem 由哪个 A-layer owner 维护？
4. 当前长期 writable branches 不超过约 8–12 条；
5. integration/agent branches 为什么存在、何时退出？
6. 历史结果如何从 PR/tag/lineage 恢复？
7. 每个 canonical reusable theorem、root formalization、tool family、negative boundary 与 active foundation alert 从哪里可发现？

如果一个结果只能通过“记住某个 300 commits 老分支”或旧 Relay comment 才能找到，架构仍未压实。
