<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R040-NATIVE-SURFACE-HORIZON-QUOTIENT-CALCULUS",
  "title": "R040 Native Surface Horizon Quotient Calculus",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_COLLAPSE_THEORY",
  "frontier": "Starting from R039's metric-free native interface transition system, construct and classify the coarsest future-safe surface quotients for finite operation horizons, quantify the correlation/residual debt required as the horizon grows, and determine when a compact quotient can be recursively updated rather than merely answering one terminal query.",
  "next_action": "Freeze the surface transition system and future languages, define horizon-indexed behavioral equivalence and quotient kernels, reproduce the R039 S/H/R2/J_h examples as special cases, then search for minimal R3/higher-horizon sufficient quotients and exact lower bounds on information that cannot be collapsed.",
  "dependencies": [
    {
      "target": "R039 Draft PR #524 owner head c484fb85385b8498982aaa939171957588c836d7",
      "action": "CONSUME_FROZEN_NATIVE_INTERFACE_COLLAPSE_COUNTEREXAMPLES_AND_J_H_SUFFICIENCY",
      "satisfied": true
    },
    {
      "target": "R023/R023I future-safe quotient and BRC semantic core",
      "action": "TEST_AND_SPECIALIZE_WITHOUT_REOWNING_GENERIC_BRC_THEOREMS",
      "satisfied": true
    },
    {
      "target": "Stage131 storage/execution-depth Pareto distinction",
      "action": "INFORM_FOR_REPRESENTATION_COST_ANALYSIS_ONLY",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R039 exact metric-free surface calculus and exhaustive FCC/HCP N<=8 atlas",
    "R039 minimal counterexamples: S one-step failure N=3, H two-step failure N=4, R2 higher-horizon failure at N=6",
    "R039 finite exterior-incidence cone J_h sufficient for fixed addition horizon h",
    "R023/R023I no-resurrection and future-safe branch recoalescence semantics"
  ],
  "evidence_status": "HORIZON_INDEXED_SURFACE_PRECISION_MOTHER_THEOREM_GATE",
  "last_progress_ref": "R039 returned on Draft PR #524 with exact future-relative surface collapse hierarchy and higher-horizon counterexamples.",
  "last_progress_at": "2026-08-12T15:50:00+08:00",
  "hard_block": null,
  "tags": [
    "R040",
    "native-surface",
    "future-relative-precision",
    "quotient",
    "behavioral-equivalence",
    "horizon",
    "correlation-debt",
    "residual",
    "BRC",
    "Markov-sufficiency",
    "state-compression"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R040",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R040 — Native Surface Horizon Quotient Calculus

Status: `READY / P0 / HORIZON-INDEXED SURFACE PRECISION / NOT CANONICAL`

## 0. 母问题

R039 已经说明：原生粗糙表面是 contact/incidence cut，而不是半径或球面；把完整表面压成 `S=|delta(C)|`、frontier histogram `H`、local-type multiset 或 second-order residual，安全性取决于未来要做多少步、问什么 observable。

R040 不再扩大表面枚举本身，而研究：

> **对一个给定 surface future language 和有限 horizon `h`，什么是最粗但仍 exact 的状态？随着 `h` 增大，需要保留多少新的 correlation/residual？一个对终点查询足够的 quotient，什么时候还能作为可递归执行的 Markov state？**

整个 native 主线继续禁止把 root distance、radius、equal-distance shell、Euclidean area/curvature/sphere 当作 primitive。

---

## 1. 任务内状态机

`READY`
→ taskbook 可领取。

`CLAIMED`
→ 先冻结 transition system 与 future language，不得从某个预设 `R3` 表示倒推定义。

`IN_PROGRESS / BEHAVIORAL_KERNEL_FROZEN`
→ 已定义 horizon-indexed future signatures、equivalence kernels、terminal-only 与 trajectory-sensitive 语言。

`IN_PROGRESS / R039_REPLAYED_AS_SPECIAL_CASES`
→ `S/H/R2bar/J_h` 已在统一框架中重新分类，并与 R039 counterexamples 一致。

`IN_PROGRESS / MINIMAL_QUOTIENT_SEARCH`
→ 已构造/搜索 `R3` 或其他 horizon-3/4 sufficient quotient，并给出 exact collision/kill tests。

`IN_PROGRESS / COST_PARETO_BUILT`
→ 已比较 quotient size、storage、update cost、future horizon、branching cost 和 recursive sufficiency。

`HANDOFF_READY`
→ 若未完成，必须留下 frozen definitions、当前 minimal witnesses、唯一 next_action。

`SEMANTIC_CHECKPOINT`
→ 能回答 horizon 增长如何强迫 quotient refinement、哪些 residual 是真正必要的、terminal sufficiency 与 recursive/Markov sufficiency为何不同。

`DONE / RETURNED`
→ 返回 theorem/counterexample hierarchy、machine-checkable quotient atlas、minimal witnesses、cost Pareto、Foundation recommendation。

---

## 2. Frozen native transition system

State space 以 finite connected occupied clusters `C` 为对象，按对应 FCC/HCP native lattice symmetry quotient；坐标只作 contact/symmetry implementation carrier。

Addition action：

`C --x--> C union {x}` for `x in F(C)`.

必要时另开 deletion language，但不得与 addition-only 结论混淆；deletion 要显式携带 connectivity legality。

原生 surface：

`delta(C)={(u,v):u in C, v notin C, u~v}`.

Scalar readout：

`S(C)=|delta(C)|`.

R039 exact identities作为冻结输入：

`S=12|C|-2E_int`,

`Delta S=12-2k_C(x)`.

---

## 3. Future language 必须 typed

至少区分以下语言，不得混在一个“precision”里：

### F0 — current scalar

只问当前 `S(C)`。

### F1-support

问下一步所有可能 `Delta S` 的 Boolean support。

### F1-multi

问下一步 `Delta S` 的 multiplicity-sensitive support。

### Fh-terminal-S

问 exactly `h` 次 addition 后所有可能 terminal `S`。

### Fh-best

只问 exactly `h` 次后能达到的最小 terminal `S`，等价研究 R039 `Lambda_h`。

### Fh-trajectory

保留 horizon `h` 内所有合法 action/S trajectories，而不是只看终点。

### Fh-operational

要求 quotient 本身能够在每一步根据 action 更新到 successor quotient，并继续执行剩余 future language。

必须区分：

`terminal query sufficient != recursively updateable != full trajectory sufficient`.

---

## 4. Horizon-indexed behavioral equivalence

对每个 future language `F` 和 horizon `h`，定义 exact future signature

`Sigma_{F,h}(C)`

以及

`C ~_{F,h} D iff Sigma_{F,h}(C)=Sigma_{F,h}(D)`.

研究 quotient：

`Q_{F,h}=X / ~_{F,h}`.

必须证明/验证：

1. 对 nested future languages，horizon 增长导致 kernel refinement：
   `ker Sigma_{F,<=h+1} subseteq ker Sigma_{F,<=h}`；
2. terminal-only signatures 不自动具有同样的递归闭包；
3. coarsest exact quotient 是 future language 相对的，而不是绝对“最精确表示”。

若这只是标准 behavioral equivalence / Myhill-Nerode / bisimulation 的直接实例，必须 prior-art root，不得宣称一般框架新颖；项目价值应落在 native-surface specialization、exact witnesses 与 residual complexity 上。

---

## 5. R039 representation ladder 统一重放

在统一 signature 语言中 exact 定位：

- `S`：current-S exact；R039 已给 `N=3` one-step unsafe witness；
- `H`：one-step multiplicity exact；R039 已给 `N=4` two-step terminal-S unsafe witness；
- local surface-type multiset：R039 已给 `N=4` correlation-debt witness；
- `R2bar`：two-step terminal-S exact，但 `N=6` 出现 collisions，FCC horizon-4 kill witness；
- `J_h`：fixed horizon addition-only full operational trajectory sufficient，minimality open。

这些不是重新研究 R039，而是作为母框架的 regression suite。

---

## 6. R3 / higher-horizon quotient search

优先研究 horizon 3 与 4。

不要先假定 `R3` 是“再多存一层 histogram”。必须从 future signature 反推必要信息。

候选可以包括：

- frontier-candidate induced contact graph with vertex labels `k`；
- pairwise overlap/incidence matrices；
- small hypergraph residual capturing shared future cells；
- radius-free exterior incidence cone的 quotient；
- Weisfeiler-Lehman-like local correlation summaries，仅作诊断，不得预设充分。

要求：

1. 找到尽可能小的 sufficient candidate；
2. exhaustive/targeted search same-summary/different-future counterexample；
3. 若被杀，定位缺失 correlation 的最小阶；
4. 对 FCC/HCP 分别找 first collision size/horizon；
5. 不把 `J_h` 的充分性误写成 minimality。

---

## 7. Recursive / Markov sufficiency

定义 representation `R` 对 future language 的 one-step update closure：

存在 deterministic or branch-aware operator `T_R`，使得从 `R(C)` 与 chosen admissible action class 可以得到 successor `R(C')`，且后续 future signature exact。

重点证明/杀掉：

- `R2bar` 对 two-step terminal query sufficient，但不是 recursively Markov；
- 某些 terminal-sufficient quotient 是否必然需要额外 correlation residual 才能成为 executable state；
- recursive closure 的最小 residual 是否与 horizon 增长形成严格 hierarchy。

将其与 BRC 区分：BRC 可以保留多分支 support；这里还要研究 branch state 本身用哪个 quotient 才能安全 recoalesce。

---

## 8. Surface BRC / recoalescence

从 R039 exact counterexamples 构造 branch-recoalescence tests：

- same `S` branches premature merge；
- same `H` branches premature merge；
- same `R2bar` branches在更长 suffix下 premature merge。

对每个 `F,h` 定义安全 recoalescence criterion：只有 future signatures 相同的 branches 才允许忘记 provenance。

比较：

- literal branch support；
- multiplicity-preserving branch carrier；
- Boolean BRC carrier；
- quotient-after-each-step vs quotient-only-at-terminal。

不得把 multiplicity/provenance/probability 自动归给 Boolean BRC。

---

## 9. Precision / storage / execution Pareto

至少测量：

- serialized state size；
- number of equivalence classes over exact small-cluster atlas；
- successor update cost；
- branch factor after quotient；
- exact supported horizon；
- first failure witness size；
- residual acquisition cost。

建立至少：

`state size vs exact horizon`

和

`state size vs update/branch cost`

两个 Pareto 图谱。

重点检验是否存在：

- 一个很大的 one-round table 可直接回答 h-step future；
- 一个更小的 recursively executable representation，需要多轮更新；
- 与 Stage131 storage/execution-depth Pareto 同构或不同的结构。

---

## 10. Exact experiments

优先复用 R039 frozen atlas/code作为 input oracle，但新的 quotient/signature engine 应独立实现。

至少：

- FCC/HCP exhaustive states through `N<=8` where feasible；
- exact h=1..4 future signatures for selected languages；
- enumerate quotient class counts；
- produce same-summary/different-future minimal witnesses；
- validate `J_h` sufficiency on exhaustive bounded domain；
- pressure-test R3 candidates。

Theorem-critical path 只用 integer/combinatorial arithmetic。

---

## 11. Candidate hypotheses

H1 `HORIZON_REFINEMENT`：nested future language 的 coarsest exact quotient 随 h 单调细化。

H2 `TERMINAL_VS_OPERATIONAL_GAP`：存在 terminal-S sufficient quotient 不能递归执行同一 horizon semantics；R039 `R2bar` 是候选 witness。

H3 `FINITE_EXTERIOR_CONE_SUFFICIENCY`：对任意固定 addition horizon h，R039 `J_h` 足以计算全部 action/S trajectories。

H4 `DEEP_INTERIOR_COLLAPSIBLE`：固定 addition horizon 下，超出 operational exterior cone 的深内部信息可以安全遗忘。

H5 `STRICT_CORRELATION_HIERARCHY`：从 h=1 到更高 h，至少在某些区间必须依次保留更高阶 frontier correlation。

H6 `COMPACT_R3_EXISTS`：存在严格小于完整 `J_3` 但对声明 horizon-3 language exact 的 quotient。

H7 `SURFACE_BRC_SAFE_IFF_FUTURE_SIGNATURE_EQUAL`：在固定 typed future language 中，branch recoalescence 的最粗安全关系就是 behavioral kernel。

H8 `PRECISION_COST_PARETO`：增加 exact horizon 与降低 update rounds/state size 之间存在非平凡 Pareto，而不是单一“越精越好”。

负结果同样有效。

---

## 12. Kill tests

必须至少包含：

1. 用 terminal-only equality 冒充 recursive state；
2. 用同一 `S/H/R2` 但不同更长 future 的已知 R039 witnesses 回归；
3. abstract graph isomorphism 误合并 embedded future；
4. horizon 3 candidate 在 horizon 4 被误宣传为 universal；
5. addition-only sufficiency 被扩到 deletion without connectivity residual；
6. Boolean branch support 被误宣传为 multiplicity/provenance exact；
7. `J_h` sufficient 被误宣传为 minimal；
8. 用 root distance/radius/Euclidean geometry偷换 native exterior layers。

---

## 13. Required artifacts

建议至少：

- `research/R040_NATIVE_SURFACE_HORIZON_QUOTIENT_REPORT.md`
- `experiments/r040_surface_horizon_quotients.py`
- `tests/test_r040_surface_horizon_quotients.py`
- `research/r040_generated/R040_QUOTIENT_CLASS_ATLAS.json`
- `research/r040_generated/R040_MINIMAL_COUNTEREXAMPLES.json`
- `research/r040_generated/R040_R3_CANDIDATES.json`
- `research/r040_generated/R040_BRC_RECOALESCENCE_MATRIX.json`
- `research/r040_generated/R040_PRECISION_COST_PARETO.json`
- `research/r040_generated/R040_HYPOTHESIS_DISPOSITIONS.json`

---

## 14. Required final answers

返回时必须直接回答：

1. 对每个 typed future language，h=1..4 的 coarsest observed quotient hierarchy是什么？
2. R039 `S/H/R2bar/J_h` 分别 exact 到什么 horizon/observable？
3. 是否找到 compact `R3`？最小 kill witness是什么？
4. terminal sufficiency 与 recursive/Markov sufficiency第一次在哪里分开？
5. fixed horizon 下 deep interior 是否可 exact collapse？
6. branch recoalescence 的最粗安全条件是什么？
7. horizon 增长需要的 correlation order/representation cost 如何增长？
8. 是否存在 storage/update-depth Pareto？
9. FCC/HCP 在 quotient complexity 上第一次哪里不同？
10. 哪些结果值得进入 Foundation/Lean，哪些只保留 experiment/counterexample atlas？

Preferred return classes：

`SURFACE_HORIZON_QUOTIENT_HIERARCHY_FOUND`

`TERMINAL_OPERATIONAL_PRECISION_GAP_FOUND`

`COMPACT_R3_FOUND`

`R3_KILLED_CORRELATION_DEBT_EXTENDS`

`FINITE_EXTERIOR_CONE_FUTURE_SAFETY_CONFIRMED`

`SURFACE_BRC_RECOALESCENCE_CRITERION_FOUND`

`SURFACE_PRECISION_COST_PARETO_FOUND`

`NOT_CANONICAL`.
