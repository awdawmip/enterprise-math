<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R045-HISTORICAL-NATIVE-SEMANTICS-RETYPE-R038-N0-REPAIR",
  "title": "R045 Historical Native-Semantics Retype and R038 N0 Repair",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_SEMANTIC_REPAIR",
  "frontier": "Apply the hardened native-semantics admissibility gate to the R033-R041 geometry/readout lineage, conserve exact mathematics by retyping rather than recomputing when possible, and repair the only frozen theorem-level native-ontology defects isolated by R044: R038-C05 and R038-C06.",
  "next_action": "Freeze a complete typed historical claim ledger from the R044 impact matrix, preserve all conditional/readout results that remain mathematically valid, then rebuild R038-C05 and R038-C06 from the declared metric-free N0 substrate without importing root, distance, equidistance, radius, embedding geometry, optimization, propagation, or continuum structure unless explicitly typed as added semantics.",
  "dependencies": [
    {
      "target": "R044 owner head 0af3c999874e0768a88f34f66c5c618900a036e4",
      "action": "CONSUME_CLAIM_IMPACT_MATRIX_HARDENING_AND_R045_GENERATION_SPEC",
      "satisfied": true
    },
    {
      "target": "native_semantics_admissibility.json V2 at source commit a70c56e5c43772903a74d258ab237825c6045a8c",
      "action": "CONSUME_ACTIVE_GATE",
      "satisfied": true
    },
    {
      "target": "R033/R034/R037/R038/R039/R041 frozen research artifacts",
      "action": "RETYPE_AND_SELECTIVELY_TEST",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R044 R044_CLAIM_IMPACT_MATRIX.json",
    "R044 R045_RERUN_GENERATION_SPEC.json",
    "R044 R044_GATE_HARDENING_DELTA.json",
    "R038 owner head d45cb42de4e259439ce1b56c7fa00debabbeb129",
    "R037 owner head 744fcf737d1037cc1c1a3ba810ce79817fd4f464",
    "R039 owner head c484fb85385b8498982aaa939171957588c836d7",
    "R041 owner head 688661e76255b3e86df6d5c69695f2932b650740"
  ],
  "evidence_status": "HISTORICAL_SEMANTIC_RETYPE_AND_R038_N0_REPAIR_GATE",
  "last_progress_ref": "R044 isolated the historical semantic impact and reduced theorem-level repair to R038-C05/C06 after hardening the admissibility gate.",
  "last_progress_at": "2026-08-12T19:40:00+08:00",
  "hard_block": null,
  "tags": [
    "R045",
    "native-semantics",
    "historical-retype",
    "R038",
    "N0",
    "pi",
    "ontology",
    "semantic-repair",
    "typed-dependencies",
    "selective-recompute"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R045",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:2899eeb698a6c5fe4d770618588ba03125d727afe4a6fe7183515de99a078d58",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R045 — Historical Native-Semantics Retype and R038 N0 Repair

Status: `READY / P0 / HISTORICAL RETYPE / R038 N0 REPAIR / NOT CANONICAL`

## 0. 母问题

R044 已经表明，R033–R041 的绝大多数 exact 数学并不因为 native-semantics 纠错而失效；真正的问题是若干结果曾把 N1/N2/N3 结构提升成 N0/native ontology。R045 的目标不是重算历史，而是回答：

> **在 hardened native-semantics gate 下，历史结论的最强合法表述分别是什么？去除 root、distance/equidistance、radius、embedding geometry、propagation、optimization 与 continuum 等未声明结构之后，R038 对 metric-free N0 世界关于超越常数 / “native pi” 的两条核心判断还能否成立？**

本任务必须优先保守数学信息：一个公式若作为明确 N1/N2/N3 条件下的 theorem 仍正确，就保留它；只有 theorem-critical inference 确实依赖错误的跨层提升时才重新研究。

---

## 1. 任务内状态机

`READY`
→ 可领取；先读取 active V2 semantic gate 与 R044 frozen rerun spec。

`CLAIMED`
→ 冻结 declared N0、typed dependency DAG 与 claim-strength ledger；不得先选想要的 pi 结论。

`IN_PROGRESS / HISTORICAL_LEDGER_FROZEN`
→ R033/R034/R037/R038/R039/R041 的列入 claims 均已得到 typed dependency closure、semantic strength、weakest valid restatement 与 no-recompute/recompute disposition。

`IN_PROGRESS / R038_C05_N0_REBUILT`
→ 已在纯 N0 scope 下重新表述并 kill/prove/open R038-C05；原 rooted graph-zeta theorem 与 N0 inference 已严格分离。

`IN_PROGRESS / R038_C06_NATIVE_PI_RESOLVED`
→ 已给出“native pi”候选的可检验类型定义，并 prove/kill/open 唯一性、存在性或不可判定性；不得以“存在多个 readout”替代 N0 非存在证明。

`IN_PROGRESS / DOWNSTREAM_IMPACT_AUDITED`
→ 所有消费 R038-C05/C06 的 Foundation-facing / ontology-facing downstream claims 已定位并 retype、downgrade、repair 或标 OPEN。

`HANDOFF_READY`
→ 若未完成，留下 frozen ledger、当前最小 counterexample / obstruction、唯一 next action。

`SEMANTIC_CHECKPOINT`
→ 能区分保留的 conditional mathematics、撤回的 native interpretation、真正重算后的 N0 theorem、以及仍然 OPEN 的问题。

`DONE / RETURNED`
→ 返回完整历史 retype ledger、R038-C05/C06 repaired dispositions、downstream impact matrix、no-recompute certificate 与后续任务建议。

---

## 2. Frozen selective-rerun contract

使用 R044 的 impact matrix 与 generation spec 作为路由输入，而不是重新决定哪些历史公式值得重算。

### 2.1 禁止无意义重算

以下方向不得仅因 semantic retype 而重新计算：

- R033 shortest-path/word-metric 的 exact shell/bulk/limit-shape formulas；
- R034 propagation moments、path-count、spectral expansions 与 conditional limits；
- R037 对上述 conditional mathematics 的独立数值/公式 replication；
- R039 contact-cut update laws、collapse witnesses 与 fixed-future results；
- R041 typed future signatures、R2bar/B2/B3 separations 与 M_h carrier results。

它们应写入 `NO_RECOMPUTE_PRESERVED_MATH` ledger，并给出正确 N0/N1/N2/N3 类型。

### 2.2 theorem-level repair core

只把以下两条作为默认 theorem-level repair target：

- `R038-C05`；
- `R038-C06`。

如果研究过程中发现第三条历史 theorem 事实上也依赖未列出的 hidden primitive，必须给出 typed dependency witness 后才能扩大 recompute scope。

---

## 3. 必须冻结的 N0 substrate

在 R038 repair 中，起始 N0 只能来自任务明确声明并经 gate 允许的 relational substrate，例如：

- cell carrier；
- declared local contact/incidence；
- declared FCC/HCP/Barlow stacking relation where relevant；
- occupancy / finite-cluster membership when该 claim需要它。

必须单独列出 `DECLARED_N0_PRIMITIVE` 与 `N0_DEFINABLE_DERIVED`。

任何 root、seed-as-center、shortest path、distance、equal-distance class、radius、norm、physical embedding measurement、random walk、heat flow、optimization objective、Fourier/Bloch object、scalar calibration、continuum completion 若被使用，都必须作为新增 typed semantics；它们不能再被用来无条件判定 metric-free N0 ontology。

---

## 4. Historical claim ledger

对 R044 generation spec 列出的每条 historical claim，返回至少：

- `claim_id`；
- `native_basis_status`；
- `declared_base_carrier`；
- `critical_symbols`；
- `typed_dependency_graph`；
- `transitive_dependency_closure_checked`；
- `promotion_target_strength`；
- `certificate_semantic_strength`；
- `admissibility_verdict`；
- `weakest_valid_restatement`；
- `recompute_status`；
- `evidence_ref`。

语义强度至少区分：

`SCALAR < QUOTIENT < RELATION < OBJECT < PRIMITIVE`。

不得用 scalar invariant 的不变性去证明完整 object / primitive 已 native-promoted。

---

## 5. R038-C05 — 重建 metric-free N0 命题

历史错误：rooted graph-zeta

`Z_G(s;o)=sum_{x!=o} d_G(o,x)^(-s)`

作为 shortest-path/readout mathematics 可以完全正确，但它不能攻击一个没有 root/distance/equidistance 的更强 N0 hypothesis。

R045 必须先把原 H7 想表达的 N0 问题重新写成 well-typed statement，再攻击它。

至少区分：

1. **有限局部 N0 表达式闭包**：在明确的 finitary relational operator language 下可得到什么数域/对象类；
2. **无限 N0-definable relational completion**：若允许 choice-free / automorphism-invariant 的 infinite construction，它是否能产生经典超越常数或 special values；
3. **需要 N1/N2 才能定义的 infinite aggregate**：不能拿来回答 1/2。

关键要求：

- 不得为了构造 infinite observable 偷偷选 root、metric、ordering、embedding 或 measure；
- 若某个 infinite construction 可以从 N0 choice-free 定义，必须给出完整 definability certificate 与 semantic-strength match；
- 若在当前 N0 语言中连目标 scalar observable 都无法 well-type，则返回 `N0_QUESTION_UNDERSPECIFIED` / `OPEN`，而不是伪造 nonexistence theorem；
- conditional rooted-zeta theorem必须显式保留，不能因为 N0 kill 失败而删除。

目标输出之一：

`R038_C05_REPAIRED = PROVED_N0 | KILLED_N0 | OPEN_N0 | ILL_TYPED_WITHOUT_ADDITIONAL_OBSERVABLE_LANGUAGE`。

---

## 6. R038-C06 — “native pi” 的存在/唯一性必须先类型化

历史表述 `NO_UNIQUE_NATIVE_PI_WITHOUT_READOUT_SEMANTICS` 不能仅由多个不兼容 readout 推出。

R045 首先定义一个 claim-strength 明确的候选，例如：

> 一个 `native-pi candidate` 是从 declared N0 choice-free 构造、在 relevant N0 relabeling 下 invariant/equivariant、且具有声明的 scalar/object role 的 N0-definable derived object。

但不要预设这个定义一定合适；应先测试它是否足够表达原问题。

随后分别研究：

- `EXISTENCE`：是否存在满足定义的非平凡 candidate；
- `UNIQUENESS`：若存在，N0 是否足以唯一指定；
- `ROLE`：candidate 是否真的有资格承担原来所谓 pi 的角色，还是 role 本身已经需要 N1/N2 readout language；
- `NONEXISTENCE`：若要声称不存在，必须排除整个已声明 candidate class，而不是展示多个后验 readout。

允许的高价值结果包括：

- `NATIVE_PI_NOT_WELL_TYPED_AT_N0`；
- `N0_DEFINABLE_SCALAR_EXISTS_BUT_PI_ROLE_REQUIRES_READOUT`；
- `MULTIPLE_N0_CANDIDATES_KILL_UNIQUENESS`；
- `UNIQUE_N0_CANDIDATE_PROVED`；
- `NONEXISTENCE_PROVED_FOR_EXPLICIT_CANDIDATE_CLASS`；
- `OPEN_AFTER_EXACT_SCOPE`。

不要把 classical pi 的超越性或定义重新定义掉。

---

## 7. R037 semantic evidence repair

R037 的独立 replication 继续作为 conditional R033/R034 mathematics 的证据。

新增一维 evidence grade：

- `NUMERIC_OR_FORMULA_REPRODUCED`；
- `SEMANTIC_TYPING_REPRODUCED`；
- `ONTOLOGY_ADMISSIBILITY_NOT_IMPLIED_BY_REPLICATION`。

重点确认：一个 theorem 被独立复算，不意味着它自动属于 N0。

不得重跑原 numerical matrix，除非发现原数字本身有 mismatch。

---

## 8. Downstream impact audit

搜索并列出消费以下历史强表述的 downstream 项：

- rooted graph-zeta 对 metric-free N0 的 kill；
- `NO_UNIQUE_NATIVE_PI...` 的 N0/nonexistence reading；
- `TRANSCENDENTALS_ONLY_AFTER_CONTINUUM_KILLED` 或等价过强表述。

每个 consumer 返回：

`KEEP / RETYPE / DOWNGRADE / REPAIR / RETRACT / OPEN`。

只修依赖链，不重做无关研究。

---

## 9. Mandatory negative controls

至少攻击：

1. shortest-path 可从 graph 定义，因此自动是 declared N0 primitive；
2. automorphism-invariant scalar 因为 invariant，所以能提升完整 object；
3. 多个 readout 值不同，因此任何 N0-definable scalar 都不存在；
4. 没找到 N0 scalar，因此证明不存在；
5. classical definition 常用，因此可直接进口为 N0；
6. infinite discrete construction 自动属于 N0，而不检查它依赖的 root/order/measure/metric；
7. replication PASS 自动等于 ontology PASS；
8. retyping conditional theorem 等同于撤销 theorem。

必须保留 explicit-metric-base / explicit-continuum-base 的正控制，确保 gate 不演化成禁止经典数学的词汇过滤器。

---

## 10. Required outputs

至少返回：

1. `R045_HISTORICAL_TYPED_CLAIM_LEDGER.json`；
2. `R045_NO_RECOMPUTE_PRESERVATION_LEDGER.json`；
3. `R045_R038_C05_N0_REPAIR.md/json`；
4. `R045_R038_C06_NATIVE_PI_DISPOSITION.md/json`；
5. `R045_R037_SEMANTIC_EVIDENCE_DELTA.json`；
6. `R045_DOWNSTREAM_IMPACT_MATRIX.json`；
7. exact theorem/counterexample/open ledger；
8. 若发现新的 N0 mother question，给出最小 next-task specification，但不得把 R043 当前任务并入本任务。

---

## 11. 完成条件

R045 只有在以下条件同时满足时才算 `DONE / RETURNED`：

- historical claims 全部有 hardened typed ledger；
- preserved conditional/readout mathematics 有明确 no-recompute certificate；
- R038-C05 已在 metric-free N0 下重新得到 `PROVED/KILLED/OPEN/ILL_TYPED` 之一；
- R038-C06 已对 existence / uniqueness / role / nonexistence 分别给出 exact disposition；
- downstream overclaims 已定位并修正建议；
- 不再遗留任何“因为某 N1/N2 theorem 正确，所以 N0 ontology 也成立”的隐式推理。

Preferred return：

`R045_HISTORICAL_SEMANTIC_RETYPE_COMPLETE / CONDITIONAL_MATH_CONSERVED / R038_C05_N0_REPAIRED_OR_OPEN / R038_C06_NATIVE_PI_SCOPE_RESOLVED_OR_OPEN / DOWNSTREAM_OVERCLAIMS_ISOLATED / R043_REVIEW_STILL_SEPARATE / NOT_CANONICAL`
