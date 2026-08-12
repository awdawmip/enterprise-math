<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R041-NATIVE-SURFACE-HORIZON-QUOTIENT-CALCULUS",
  "title": "R041 Native Surface Horizon Quotient Calculus",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_COLLAPSE_THEORY",
  "frontier": "Starting from R039's metric-free native interface transition system, construct and classify the coarsest future-safe surface quotients for finite operation horizons, quantify the correlation/residual debt required as the horizon grows, and determine when a compact quotient can be recursively updated rather than merely answering one terminal query.",
  "next_action": "Freeze the surface transition system and typed future languages, define horizon-indexed behavioral equivalence and quotient kernels, reproduce the R039 S/H/R2/J_h examples as regression cases, then search for minimal R3/higher-horizon sufficient quotients and exact lower bounds on information that cannot be collapsed.",
  "dependencies": [
    {
      "target": "R039 Draft PR #524 owner head c484fb85385b8498982aaa939171957588c836d7",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "R023/R023I future-safe quotient and BRC semantic core",
      "action": "TEST",
      "satisfied": true
    },
    {
      "target": "Stage131 storage/execution-depth Pareto distinction",
      "action": "INFORM",
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
  "last_progress_ref": "R039 returned on Draft PR #524 with exact future-relative surface collapse hierarchy and higher-horizon counterexamples; this task was renumbered from an erroneous R040 allocation after conflict with the pre-existing polygonal R040 owner.",
  "last_progress_at": "2026-08-12T16:46:00+08:00",
  "hard_block": null,
  "tags": [
    "R041",
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
  "identity_lane": "R041",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R041 — Native Surface Horizon Quotient Calculus

Status: `READY / P0 / HORIZON-INDEXED SURFACE PRECISION / NOT CANONICAL`

## 0. 母问题

R039 已经建立了一个无需半径、等距或球语义的 native surface calculus：原生表面是 occupied-to-unoccupied contact cut，而 `S=|delta(C)|`、frontier histogram `H`、local-type multiset、`R2bar` 都只是针对不同 future language 的不同坍缩。

R041 的母问题是：

> **对指定 surface future language 与有限 horizon `h`，什么是最粗但仍 exact 的 quotient？随着 horizon 增长，必须补回多少 frontier correlation / residual；一个对 terminal query 足够的 quotient，什么时候还能作为 recursively executable / Markov state？**

本任务不重新研究“球是什么”，也不扩大 R039 的纯枚举规模作为主轴。

---

## 1. 任务内状态机

`READY`
→ taskbook 可领取。

`CLAIMED`
→ 冻结 transition system 与 typed future language；不得先假定某个 `R3` 结构。

`IN_PROGRESS / BEHAVIORAL_KERNEL_FROZEN`
→ 已定义 horizon-indexed signature、equivalence kernel、terminal/trajectory/operational language。

`IN_PROGRESS / R039_REGRESSION_REPLAYED`
→ `S/H/local-type/R2bar/J_h` 已在统一框架中分类，与 R039 counterexamples 完全一致。

`IN_PROGRESS / MINIMAL_QUOTIENT_SEARCH`
→ 已构造/杀掉 horizon-3/4 compact quotient candidate，并给出 minimal or bounded collision witnesses。

`IN_PROGRESS / COST_PARETO_BUILT`
→ 已比较 state size、update rounds、branch cost、exact horizon、residual acquisition cost。

`HANDOFF_READY`
→ 未完成时保留 frozen definitions、最小 witness、当前 candidate 与唯一 next action。

`SEMANTIC_CHECKPOINT`
→ 能回答 horizon 增长如何强迫 quotient refinement、terminal sufficiency 与 recursive sufficiency 的差别，以及哪些 correlation 是不可坍缩的。

`DONE / RETURNED`
→ 返回 theorem/counterexample hierarchy、machine-checkable quotient atlas、minimal witnesses、cost Pareto 和 Foundation recommendation。

---

## 2. Frozen native transition system

状态是 finite connected occupied clusters `C`，按 FCC/HCP 的 native lattice symmetry quotient。

Addition action：

`C --x--> C union {x}` for `x in F(C)`.

Native surface：

`delta(C)={(u,v):u in C, v notin C, u~v}`.

Scalar collapse：

`S(C)=|delta(C)|`.

冻结 R039 exact identities：

`S(C)=12|C|-2E_int(C)`

以及

`Delta S=12-2k_C(x)`.

坐标只可作为 contact/symmetry implementation carrier；不得把 root distance、radius、norm、equal-distance shell、Euclidean area/curvature/sphere 引入 native state。

---

## 3. Future language 必须 typed

至少区分：

- `F0-current-S`：只问当前 `S`；
- `F1-support`：下一步 `Delta S` Boolean support；
- `F1-multi`：下一步 multiplicity-sensitive support；
- `Fh-terminal-S`：exactly `h` additions 后 terminal `S` support；
- `Fh-best`：exactly `h` additions 后最小 terminal `S`，等价于 R039 `Lambda_h`；
- `Fh-trajectory`：保留 horizon 内合法 action/S trajectory；
- `Fh-operational`：要求 quotient 可逐步更新到 successor quotient 并继续执行剩余 future。

必须始终区分：

`terminal-query sufficient != recursively updateable != full-trajectory sufficient`.

---

## 4. Horizon-indexed behavioral quotient

对每个 future language `F` 和 horizon `h`，定义 exact signature：

`Sigma_{F,h}(C)`

以及：

`C ~_{F,h} D  iff  Sigma_{F,h}(C)=Sigma_{F,h}(D)`.

研究：

`Q_{F,h}=X / ~_{F,h}`.

要求证明/验证：

1. nested future language 下，`h+1` 的 exact kernel 细化 `h` 的 kernel；
2. terminal-only language 不自动给 recursive closure；
3. coarsest exact quotient 是 future-language-relative，而不是绝对“最精确状态”；
4. 若一般结构只是标准 behavioral equivalence / Myhill-Nerode / bisimulation 的实例，明确 prior-art root；项目价值落在 surface specialization、exact witnesses 和 residual complexity。

---

## 5. R039 regression suite

统一重放但不重做 R039：

- `S`：current exact，`N=3` 已 one-step unsafe；
- `H`：one-step multiplicity exact，`N=4` 已 two-step terminal-S unsafe；
- local surface-type multiset：`N=4` 已有 correlation-debt witness；
- `R2bar`：two-step terminal-S exact，但 `N=6` collision，FCC horizon-4 kill witness；
- `J_h`：fixed-h addition-only operational trajectory sufficient，minimality open。

任何新 abstraction 若不能复现这些正负边界，直接判失败。

---

## 6. Compact R3 / higher-horizon search

优先攻击 horizon 3 与 4。

不得先假定 `R3` 是“再加一层 histogram”。从 future signature 反推必要 correlation。

候选包括但不限于：

- frontier-candidate induced contact graph + `k` labels；
- pairwise overlap/incidence matrix；
- shared-future-cell hypergraph residual；
- radius-free exterior-incidence cone quotient；
- local refinement/WL-like summaries，仅作为 diagnostic candidate。

对每个 candidate：

1. 证明 sufficient 或找 exact kill witness；
2. 找 first collision size/horizon；
3. 定位缺失 correlation 的最小阶；
4. 比较 FCC/HCP 是否具有相同 failure order；
5. 不把 `J_h` sufficiency 误写成 minimality。

---

## 7. Recursive / Markov sufficiency

定义 representation `R` 的 update closure：存在 deterministic 或 branch-aware update rule，使得从 `R(C)` 与 admissible action class 能计算 successor `R(C')` 并继续 exact future semantics。

重点研究：

- `R2bar` terminal-sufficient but not recursively Markov 的最小修复；
- terminal quotient 到 executable quotient 需要增加的最小 residual；
- recursive closure 是否形成 strict horizon hierarchy；
- branch-aware carrier 是否能比 deterministic Markov carrier 更省 state。

---

## 8. Surface BRC / recoalescence

用 R039 witnesses 建立：

- same-`S` premature recoalescence；
- same-`H` premature recoalescence；
- same-`R2bar` 在更长 suffix 下 premature recoalescence。

对固定 `F,h`，测试：

> branch recoalescence 的最粗安全关系是否正好是 `~_{F,h}`。

分别比较 Boolean support、multiplicity、provenance-sensitive carrier；不得把 richer semantics 自动归给 Boolean BRC。

---

## 9. Precision / storage / execution Pareto

至少记录：

- quotient state serialized size；
- exact bounded atlas 上 quotient class count；
- successor update cost；
- branch factor after quotient；
- exact supported horizon；
- first failure witness size；
- residual acquisition cost。

至少给出：

`state size vs exact horizon`

与

`state size vs update/branch cost`

两个 Pareto。

重点比较：

- large one-shot terminal table；
- smaller recursively executable representation；
- full `J_h` exterior cone；
- compact residual hierarchy。

---

## 10. Exact experiments

复用 R039 frozen atlas/code作为 input oracle，但新的 signature/quotient engine 独立实现。

至少：

- FCC/HCP exact states through `N<=8` where feasible；
- `h=1..4` future signatures；
- quotient class counts；
- same-summary/different-future minimal witnesses；
- bounded exhaustive validation of `J_h` sufficiency；
- pressure-test compact R3 candidates。

Theorem-critical path 只用 integer/combinatorial arithmetic。

---

## 11. Candidate hypotheses

- H1 `HORIZON_REFINEMENT`：nested future language 的 coarsest exact quotient 随 horizon 单调细化；
- H2 `TERMINAL_VS_OPERATIONAL_GAP`：terminal-sufficient quotient 可以不是 recursively executable；
- H3 `FINITE_EXTERIOR_CONE_SUFFICIENCY`：固定 addition horizon 的 `J_h` 足够；
- H4 `DEEP_INTERIOR_COLLAPSIBLE`：固定 horizon 下 exterior cone 之外的深内部可安全遗忘；
- H5 `STRICT_CORRELATION_HIERARCHY`：某些 horizons 必须逐步保留更高阶 frontier correlation；
- H6 `COMPACT_R3_EXISTS`：存在严格小于完整 `J_3` 且对声明 horizon-3 language exact 的 quotient；
- H7 `SURFACE_BRC_SAFE_IFF_FUTURE_SIGNATURE_EQUAL`：固定 typed future language 下，behavioral kernel 是最粗安全 recoalescence；
- H8 `PRECISION_COST_PARETO`：exact horizon、state size 与 update rounds 存在非平凡 Pareto。

负结果同样有效。

---

## 12. Mandatory kill tests

至少包含：

1. terminal-only equality 冒充 recursive state；
2. same `S/H/R2bar` 的 R039 已知更长 future 分叉；
3. abstract graph isomorphism 误合并 embedded future；
4. horizon-3 sufficient candidate 被误宣传为 universal；
5. addition-only sufficiency 被错误延伸到 deletion legality；
6. Boolean support 被误当 multiplicity/provenance；
7. 用 root/radius/equidistance 构造 candidate state；
8. 用大表覆盖所有 future 后错误宣称 minimality。

---

## 13. Deliverables

至少返回：

- `R041_NATIVE_SURFACE_HORIZON_QUOTIENT_REPORT.md`；
- exact future-signature / quotient engine；
- machine-readable quotient atlas；
- `S/H/R2bar/J_h` regression matrix；
- compact R3 candidate or rigorous negative result；
- minimal collision/correlation-debt witnesses；
- surface BRC recoalescence matrix；
- state/horizon/update Pareto；
- theorem/counterexample ledger；
- prior-art boundary；
- Foundation/Lean recommendation。

最终必须明确回答：

> **进取数论中的“精度”能否在这个 native surface world 中被具体化为：为了未来 `h` 步而必须保留的最小关系信息？**
