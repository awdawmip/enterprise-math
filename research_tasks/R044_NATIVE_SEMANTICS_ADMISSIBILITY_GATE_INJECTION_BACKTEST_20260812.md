<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R044-NATIVE-SEMANTICS-ADMISSIBILITY-GATE-INJECTION-BACKTEST",
  "title": "R044 Native-Semantics Admissibility Gate Injection Backtest",
  "kind": "RESEARCH",
  "owner": "research/r044-native-semantics-gate-v1",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_SEMANTIC_GUARDRAIL",
  "frontier": "Independently audit, harden, and adversarially backtest the newly active native-semantics admissibility gate so Enterprise Math researchers cannot silently promote root choice, distance/equidistance, embedding geometry, propagation, optimization, scalar readouts, or continuum structure into the declared native substrate.",
  "next_action": "Audit the active gate and startup injection from first principles, build a deterministic claim-ledger checker and adversarial fixtures, replay representative R033-R043 claims through the type system, measure false-positive/false-negative behavior, and freeze the exact rerun contract that the subsequent historical semantic reaudit must consume.",
  "dependencies": [
    {
      "target": "native_semantics_admissibility.json at source main",
      "action": "TEST_AND_HARDEN",
      "satisfied": true
    },
    {
      "target": "AGENTS.md native-semantics startup gate",
      "action": "TEST_INJECTION_AND_COMPLIANCE",
      "satisfied": true
    },
    {
      "target": "R033/R034/R037/R038/R039/R041/R043 geometry lineage",
      "action": "BACKTEST_CLAIM_TYPING",
      "satisfied": true
    }
  ],
  "source_refs": [
    "native_semantics_admissibility.json",
    "AGENTS.md native-semantics admissibility gate",
    "R033 shortest-path geometry and R034 propagation-relative geometry",
    "R037 independent replication return",
    "R038 semantic mismatch and Driver correction",
    "R039 native rough-surface calculus",
    "R041 horizon-indexed surface carriers",
    "R043 unexecuted frontier-reconstruction taskbook"
  ],
  "evidence_status": "SEMANTIC_GATE_INJECTION_AND_RETROACTIVE_RETYPE_GATE",
  "last_progress_ref": "Driver activated the Native-Semantics Admissibility Gate in source startup rules and bound native_semantics_admissibility.json into the taskbook policy digest before historical reruns.",
  "last_progress_at": "2026-08-12T18:34:00+08:00",
  "hard_block": null,
  "tags": [
    "R044",
    "native-semantics",
    "ontology",
    "type-system",
    "semantic-admissibility",
    "context-injection",
    "historical-backtest",
    "counterexample",
    "claim-ledger"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R044",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:8eb97ee026cbbd35f77f8bba02547d246beb86021631ab0a5257dd1f97acad19",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R044 — Native-Semantics Admissibility Gate Injection Backtest

Status: `READY / P0 / SEMANTIC GUARDRAIL / INJECTION BACKTEST / NOT CANONICAL`

## 0. 母问题

Enterprise Math 当前已经发现一个系统性失误模式：

> **一个数学对象在某个图、坐标系或经典数学语言中“可以定义”，不等于它属于进取数论声明的原生基底。**

R033/R038 暴露了最清楚的例子：选择 root、shortest-path semantics、graph distance，再按相同距离分 shell，本身已经进行了额外操作与坍缩；之后得到的精确公式可以正确，但不能再无条件写成 metric-free native ontology。

本任务不重新解决 R033-R043 的数学问题。它首先验证新启用的语义门是否足够严格、可执行、可检查，并冻结后续历史重跑必须使用的精确 contract。

---

## 1. 任务内状态机

`READY`
→ taskbook 可领取。

`CLAIMED`
→ 从 active policy 独立重建语义门，不接受 Driver 示例作为正确答案。

`IN_PROGRESS / TYPE_SYSTEM_AUDITED`
→ 已验证/修正 I0/N0/N1/N2/N3 类型、promotion 条件、claim-ledger schema 和 weakest-restatement 规则。

`IN_PROGRESS / INJECTION_PATH_VERIFIED`
→ 已验证新的 researcher startup surface 能实际把 gate 带入研究上下文，并验证旧 policy-stamped taskbook 在再次执行前会要求重新 review。

`IN_PROGRESS / ADVERSARIAL_BACKTEST`
→ 已用正/负/模糊 fixtures 测试 gate，统计 false positive / false negative，并产生最小绕过反例。

`IN_PROGRESS / HISTORICAL_RETYPE_PLAN_FROZEN`
→ 已把 R033-R043 受影响 claims 分级，并冻结下一条历史重跑任务的 exact 输入、优先级和 selective-recompute 规则。

`HANDOFF_READY`
→ 若未完成，留下当前 gate schema、失败 fixture、唯一 next action。

`SEMANTIC_CHECKPOINT`
→ 能回答“哪些定义可以叫 native、怎样证明 derived object 可提升、gate 是否真能拦住旧错误、哪些旧研究必须重算”。

`DONE / RETURNED`
→ 返回 gate audit、checker、mutation/backtest、历史 claim impact matrix、下一任务生成规范。

---

## 2. 必须独立审计的类型系统

从 `native_semantics_admissibility.json` 出发，但不得照抄结论。

至少验证以下分层是否充分：

- `I0_IMPLEMENTATION_CARRIER`：坐标/标签/基/embedding 仅作实现；
- `N0_NATIVE_RELATIONAL`：task 明确声明的 carrier、局部关系、state predicates；
- `N1_DERIVED_OPERATIONAL_SEMANTICS`：root/seed choice、path/metricization、propagation、time、optimization、stochastic kernel、future action language；
- `N2_READOUT_COLLAPSE`：equivalence classes、scalarization、radius/norm、shell、area/volume、moments/spectra、orbit histograms、zeta/aggregate 等；
- `N3_CONTINUUM_CLASSICAL`：Euclidean/smooth/PDE/integral/continuum objects。

若发现某对象必须单独成层，允许提出更小修正，但必须给出 kill test，而不是扩充 ontology vocabulary 取悦已有结论。

---

## 3. Native promotion 必须有 certificate

重点攻击 `NSA-02-DEFINABILITY-PROMOTION`。

候选 derived object `D` 若要被视为由 N0 内生决定，至少检查：

1. **construction**：D 是否能只从 N0 data 构造；
2. **choice independence**：root/basis/orientation/enumeration 等选择改变时是否不变；
3. **relabeling/automorphism invariance**：允许的 N0 重标号是否保留 D；
4. **uniqueness at required semantic strength**：只是 scalar value 唯一，还是完整 relation/object 唯一；
5. **no hidden imported primitive**：证明是否又偷偷使用 Euclidean metric、ordering、measure、optimization 等。

必须生成至少一个“看似 canonical 但 promotion 失败”的最小 fixture。

---

## 4. 强制历史 regression set

必须逐项构造 claim ledger，不得只写自然语言点评。

### R033

审计：

- shortest-path/word metric；
- graph ball/shell；
- cuboctahedral / HCP limit shape；
- exposed-face counts；
- `intrinsic` 术语是否越界。

预期压力：条件数学可保留，但 shortest-path metricization 与 shell scalarization必须显式分层。

### R034

审计：

- uniform NN propagation；
- physical displacement embedding；
- covariance `I/3`；
- random-walk / heat semantics；
- Bloch/Fourier expansion；
- Brownian/Euclidean-leading readout。

必须区分“exact conditional propagation theorem”和“native geometry theorem”。

### R037

这是 algorithm/data replication，不得因为数值/公式复现成功就自动赋予 ontology admissibility。检查其 evidence matrix 是否缺 semantic-typing 维度。

### R038

必须复现 Driver 已发现的 root-distance / radial-zeta semantic mismatch，并主动寻找其他尚未发现的 hidden primitive。

### R039

重点正控制：

- `delta(C)` 是否确实只用 N0 contact + occupancy；
- `S=|delta|` 必须标 N2 scalar collapse；
- local mask/type quotient；
- fixed-volume isoperimetry；
- zonotope/Wulff asymptotic。

要求避免因为后半部分是 derived 就错误否定前半部分 native cut。

### R041

审计 operation-horizon layers `L_r`、`B_h`、`M_h`：它们可以是 exact future carriers，但属于 N1/future-language semantics，不能被误称为 N0 world structure。

### R043

R043 尚未执行。检查其 taskbook 是否已满足新 gate；若有旧术语/隐含 promotion，给出必须重审的 taskbook delta，而不是直接开始研究。

---

## 5. Adversarial fixtures

至少包含：

1. `graph -> shortest-path metric -> therefore native distance`：必须拒绝最后一步；
2. `seed used for enumeration -> therefore center`：必须拒绝；
3. `integer coordinates -> compute Euclidean norm -> therefore native length`：必须拒绝；
4. `automorphism-invariant scalar -> therefore full object native`：必须拒绝强 promotion；
5. `delta(C)` from contact+occupancy：应允许 N0-relational；
6. `S=|delta(C)|`：应保留 exact，但降为 N2；
7. `optimization minimizer unique`：仍需标 N1 optimization semantics；
8. `infinite discrete limit`：不得因“仍然离散”就回升为 N0；
9. `classical/prior-art standard definition`：不得自动加入 base；
10. task 明确把 metric 声明为 base primitive：gate 应允许该 task 的 metric-relative N0，而不能教条式禁止 metric 本身。

第 10 条是关键 negative control：本 gate 约束“偷带 primitive”，不是禁止研究任何 metric world。

---

## 6. Machine-checkable claim ledger

实现 deterministic checker，至少接受：

- declared base carrier/primitives；
- I0/N1/N2/N3 dependency list；
- definability certificate flags/evidence refs；
- future language；
- proposed claim class。

输出至少：

- `NATIVE_ADMISSIBLE`；
- `CONDITIONAL_DERIVED`；
- `READOUT_ONLY`；
- `CONTINUUM_ONLY`；
- `SEMANTIC_MISMATCH`；
- `UNRESOLVED`。

Checker 不能只用关键词决定 verdict。关键词只可作为 trigger；最终 verdict 必须依赖 typed dependency graph / declared base。

---

## 7. Injection backtest

验证新的 startup rule 是否能在以下情况下触发：

- taskbook 明写 `native/intrinsic`；
- taskbook 没写 ontology，但研究过程中临时引入 radius/equidistance；
- 使用 implementation coordinates 后开始计算 embedding quantity；
- researcher 只复现旧公式，没有重新检查语义类型；
- researcher 用“canonical/natural”作为 promotion 理由。

必须设计 mutation tests，至少包含删除 gate、漏掉 N1 dependency、把 N2 假报 N0、改变 base declaration、将 task 明确声明的 metric 错判为 forbidden 等。

目标不是高召回关键词过滤，而是**低 false-negative 的 semantic typing discipline，同时不禁止合法的 conditional mathematics**。

---

## 8. Historical rerun routing

本任务不完整重跑旧数学，而是产生 impact matrix：

每个 claim 标记：

- `KEEP_NATIVE`；
- `KEEP_BUT_RETYPE_CONDITIONAL`；
- `KEEP_AS_READOUT_ONLY`；
- `RECOMPUTE_UNDER_N0`；
- `RETRACT_NATIVE_INTERPRETATION`；
- `UNRESOLVED_NEEDS_NEW_TASK`。

下一条历史重跑任务只能对 `RECOMPUTE_UNDER_N0 / UNRESOLVED` 做 theorem-level recomputation；其余结果应保留并正确重命名，避免浪费已验证的条件数学。

优先级：

1. ontology/native claims；
2. Foundation-facing claims；
3. downstream claims that consumed them；
4. already-explicit conditional/readout results。

---

## 9. 必须返回的 artifacts

至少：

- `research/R044_NATIVE_SEMANTICS_GATE_REPORT.md`；
- `research/r044_generated/R044_CLAIM_IMPACT_MATRIX.json`；
- `research/r044_generated/R044_ADVERSARIAL_FIXTURES.json`；
- `research/r044_generated/R044_INJECTION_BACKTEST.json`；
- deterministic checker + focused tests；
- `R045_RERUN_GENERATION_SPEC.json`，冻结下一任务 scope、claim IDs、selective-recompute criteria。

---

## 10. 返回问题

最终必须明确回答：

1. active gate 是否足以阻止 graph-distance/equidistance/embedding/readout 被偷写成 native primitive？
2. definability promotion 的最弱可靠 certificate 是什么？
3. gate 会不会错误禁止 task 明确声明的 metric/continuum world？
4. R033-R043 哪些 claim 只是重命名，哪些必须真正重算？
5. R043 是否可以直接继续，还是必须先按新 gate 重新 review？
6. 下一条历史重跑任务的最小完整 scope 是什么？
