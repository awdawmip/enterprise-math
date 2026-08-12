<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043-NATIVE-SURFACE-FRONTIER-RECONSTRUCTION-MARKOV-CARRIER",
  "title": "R043 Native Surface Frontier Reconstruction and Minimal Markov Carrier",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_COLLAPSE_THEORY",
  "frontier": "Determine whether the current weighted native frontier graph already determines exact future addition-only surface dynamics on FCC/HCP, and if not isolate the first hidden exterior correlation and the smallest exact residual that repairs recursive prediction without restoring the full exterior cone.",
  "next_action": "Treat R041's weighted-frontier-only no-collision result as an adversarial theorem candidate rather than evidence of sufficiency; independently search for reconstruction theorems or exact collisions, then characterize the minimal missing L0-L1 overlap/shared-future-cell structure and test whether a compact stationary or horizon-indexed Markov carrier survives.",
  "dependencies": [
    {
      "target": "R041 owner head 688661e76255b3e86df6d5c69695f2932b650740",
      "action": "CONSUME_TYPED_HORIZON_KERNELS_R2_B2_B3_AND_M_H_CARRIER",
      "satisfied": true
    },
    {
      "target": "R039 owner head c484fb85385b8498982aaa939171957588c836d7",
      "action": "CONSUME_NATIVE_INTERFACE_AND_SMALL_CLUSTER_COLLAPSE_WITNESSES",
      "satisfied": true
    },
    {
      "target": "R023/R023I future-safe quotient and BRC semantic core",
      "action": "SPECIALIZE_WITHOUT_REOWNING_GENERIC_QUOTIENT_THEORY",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R041 exact one-layer-shaved M_h carrier and bounded weighted-frontier-only no-collision search",
    "R041 R2bar exact for B2 but unsafe for B3 at N=6",
    "R039 metric-free contact-cut surface algebra and correlation-debt counterexamples"
  ],
  "evidence_status": "FRONTIER_RECONSTRUCTION_AND_MINIMAL_RECURSIVE_STATE_GATE",
  "last_progress_ref": "R041 returned a positive horizon-indexed M_h family and an unresolved stronger candidate: the weighted current-frontier graph showed no collisions in bounded FCC/HCP searches despite omitting explicit L1 future cells.",
  "last_progress_at": "2026-08-12T17:52:00+08:00",
  "hard_block": null,
  "tags": [
    "R043",
    "native-surface",
    "frontier-graph",
    "reconstruction",
    "Markov-carrier",
    "future-relative-precision",
    "correlation-debt",
    "shared-future-cell",
    "quotient",
    "BRC"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R043",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R043 — Native Surface Frontier Reconstruction and Minimal Markov Carrier

Status: `READY / P0 / FRONTIER RECONSTRUCTION / MINIMAL RECURSIVE STATE / NOT CANONICAL`

## 0. 母问题

R039/R041 已经把原生粗糙表面从“球/半径”中彻底分离出来，并得到：

- native surface 是 contact cut；
- scalar `S`、histogram `H`、`R2bar` 都是不同强度的坍缩；
- `R2bar` 对 Boolean `B2` exact，但到 `B3` 出现 correlation debt；
- 对固定 horizon `h>=2`，`M_h = S + weighted induced graph on L0..L_{h-2}` 是 exact recursively executable carrier；
- 然而更激进的 `G0` —— 只保留当前 frontier `L0` 的 weighted induced graph —— 在已有 bounded search 中没有出现 abstract weighted-graph collision。

本任务只问一个更尖锐的问题：

> **当前粗糙表面的 weighted frontier graph 是否已经隐式编码了足够的外部几何，使它能够递归决定后续 surface dynamics？若否，第一处缺失信息到底是什么，最小需要补回多少 correlation？**

不要预设 horizon 必须增加显式 exterior depth，也不要预设一个固定 frontier state 必然足够。两边都必须接受 kill test。

---

## 1. 状态机

`READY`
→ 任务可领取；`G0` 既不是 theorem 也不是已杀候选。

`CLAIMED`
→ 先冻结 `G0`、action labels、future language 和 embedding/symmetry equivalence，禁止从想要的答案反推 representation。

`IN_PROGRESS / G0_RECONSTRUCTION_AUDIT`
→ 已完成 bounded collision search、constructive reconstruction 尝试与 targeted adversarial construction。

`IN_PROGRESS / FIRST_HIDDEN_CORRELATION_LOCALIZED`
→ 若 `G0` 被杀，已找到最小 same-`G0` / different-future witness，并把缺失信息定位到明确的 L0-L1 / shared-future-cell / slot-incidence relation；若 `G0` 生存，则已形成可检验 reconstruction theorem candidate。

`IN_PROGRESS / MINIMAL_RESIDUAL_BUILT`
→ 已构造至少一个严格小于 full `M_3` 的 repair carrier，并完成 exact sufficiency/kill tests。

`IN_PROGRESS / STATIONARY_VS_HORIZON_CLASSIFIED`
→ 已回答是否存在 fixed-form recursively updateable surface state，或必须随 horizon 增长 relation depth。

`HANDOFF_READY`
→ 若未完成，必须留下最小 collision/reconstruction lemma、当前 carrier、唯一 next action。

`SEMANTIC_CHECKPOINT`
→ 能严格回答 surface-only reconstruction 是否成立、第一 correlation debt 在哪里、最小修复保留什么。

`DONE / RETURNED`
→ 返回 exact theorem/counterexample hierarchy、machine-check witness、carrier Pareto 与 Foundation 建议。

---

## 2. Frozen native objects

仅使用 FCC/HCP frozen native contact relation；坐标只作实现 carrier，不得引入 norm/radius/equidistance。

对 cluster `C`：

`F(C)=L0(C)` 为当前 frontier。

定义 weighted frontier graph：

`G0(C) = ( S(C), induced contact graph on F(C), vertex weight k_C(x) )`。

研究 branch-aware Boolean surface future：

`B_0(C)=(S(C),)`，

`B_{h+1}(C)=(S(C), {(k_C(x), B_h(C+x)) : x in F(C)})`。

Boolean set semantics与 multiplicity/provenance 必须分开。

---

## 3. 第一主攻：kill or prove `G0 -> B3`

R041 bounded search只说明在已测范围内没有 same-`G0` embedded states；这不能当 sufficiency proof。

必须并行走三条路径：

### 3.1 Exhaustive / targeted collision search

- FCC 至少覆盖 frozen atlas `N<=8`；
- HCP 至少覆盖 frozen atlas `N<=8` where practical；
- 不要因 class count 爆炸只做 naive全枚举，允许 canonical frontier-hash + exact graph-isomorphism filter；
- 若 `G0` classes仍接近 state classes，转向 deliberate constructive collision / SAT/backtracking / local surgery search。

目标：找

`G0(C)=G0(D)` but `B3(C)!=B3(D)`。

若找到，要求 cluster-size minimality尽可能向下证明。

### 3.2 Reconstruction theorem route

尝试证明 weighted `L0` graph能否重建每个 omitted `L1` cell 的 frontier-neighbor incidence。

核心问题：对每个 exterior future cell `y in L1`，集合

`N(y) intersect L0`

是否由 `G0` 中的 graph/weights唯一决定，至少 up to future-equivalent relabeling？

必须明确区分：

- reconstruct exact embedded `L1`；
- reconstruct only successor `R2bar`；
- reconstruct only `B3`；
- reconstruct only terminal `T3/T4`。

最弱足够结论优先。

### 3.3 Local surgery / ambiguity route

寻找两个 frontier patches：

- weighted `L0` induced graph identical；
- 但某些 frontier pair/triple拥有不同数量或不同身份的 common future neighbors；
- 导致一次 addition 后 successor frontier graph / `R2bar` 分裂。

优先定位最小局部 ambiguity，而不是先追大 cluster。

---

## 4. 若 `G0` 被杀：建立最小 correlation residual

按从弱到强顺序测试：

1. **pair-overlap matrix**
   `O_2(x,y)=# {z in L1 : z~x and z~y}`；
2. pair-overlap + candidate local slot orbit/type；
3. **shared-future hypergraph**：每个 `z in L1` 对应其邻接 frontier subset `N(z) intersect L0`；
4. quotient of that hypergraph by weighted-frontier automorphisms；
5. full `M3 = L0 union L1` only as upper bound。

要求每个候选都：

- exact update derivation；
- same-summary/different-`B3` kill search；
- state-size/update-cost measurement；
- 明确是否 recursively updateable，而不是只回答 terminal query。

目标是找到严格小于 `M3` 的 carrier，或者给出必须保留某阶 hyperedge correlation 的 lower bound。

---

## 5. 若 `G0` 生存：升级成 stationary-surface theorem candidate

只有在获得 structural proof 后，才允许返回：

`G0 -> B3`。

随后必须继续攻击：

- `G0 -> B4`；
- 是否存在 deterministic/branch-aware update `G0(C),action -> G0(C+x)`；
- 若能直接更新 successor `G0`，则测试是否 induction 得到 all finite Boolean horizons；
- 若 `G0` 只能回答 `B3` 但不能更新自身，则仍属于 terminal/finite-depth carrier，不是 stationary Markov state。

真正强结论需要：

`G0(C)` + chosen action class → exact successor `G0(C+x)`

up to declared symmetry/future equivalence。

如果成立，这将推翻“exact horizon 必然要求显式更深 exterior layers”的强版本；如果失败，则精确定位失败信息。

---

## 6. Surface reconstruction 与 deep interior

R041 已说明 fixed horizon 下 deep interior 可 collapse。

R043进一步问：

- 当前 boundary/frontier 是否足以决定 future exterior completion；
- 是否存在两个不同 interior clusters产生相同 complete native interface/frontier state但不同 addition future；
- 若 future只依赖 exterior interface，则 interior provenance何时可完全忘记。

这里要非常严格区分：

`same scalar S`
`same local-type bag`
`same weighted frontier graph`
`same full contact cut with slot labels`

不是同一个 equivalence。

---

## 7. 与代数坍缩/BRC 的连接

对每个 candidate carrier `Q`，定义 kernel：

`C ~_Q D iff Q(C)=Q(D)`。

与 future kernel 比较：

`ker(Q) subseteq ker(B_h)` 是 h-step安全的必要充分判据。

研究：

- `G0` 的 kernel到底比 `B3` 细、相等还是交叉；
- residual加入时 quotient如何 refinement；
- branch recoalescence在 same carrier state时是否 suffix-safe；
- Boolean安全不自动提升到 multiplicity/provenance/probability。

若 general statement直接来自 R023/R023I，不重新主张新母理论；本任务只贡献 surface-specific exact carrier/counterexample/reconstruction structure。

---

## 8. Candidate hypotheses

H1 `G0_B3_SUFFICIENCY`：weighted current-frontier graph exact决定 Boolean `B3`。

H2 `G0_RECURSIVE_CLOSURE`：`G0`可在一次 addition 后 exact更新成 successor `G0`。

H3 `FRONTIER_STATIONARY_MARKOV`：存在 fixed-form frontier-only state对任意有限 Boolean addition horizon递归 exact。

H4 `PAIR_OVERLAP_REPAIR`：若 H1失败，pairwise L1 overlap已足够修复 B3。

H5 `HYPERGRAPH_DEBT`：若 pairwise不足，第一 irreducible debt 是 shared-future-cell hyperedge identity。

H6 `INTERIOR_FORGETFULNESS`：对 addition-only surface future，给定 sufficiently rich native interface/exterior state 后 deep interior provenance 可安全忘记。

H7 `FCC_HCP_RECONSTRUCTION_SPLIT`：FCC/HCP 的最小 residual阶数可能不同。

H8 `FIXED_STATE_VS_HORIZON_GROWTH`：要么找到 stationary carrier，要么给出必须随 horizon增长 correlation depth 的 exact witness family。

全部允许被杀。

---

## 9. Mandatory negative controls

必须至少攻击：

- bounded无 collision → theorem 的错误升级；
- abstract graph isomorphism 忽略 contact-slot / world embedding future；
- pairwise overlap相同但 triple shared-future structure不同；
- B3 sufficient carrier误宣称 all-horizon；
- terminal answer carrier误宣称 recursively Markov；
- Boolean branch support误宣称 multiplicity/provenance exact；
- FCC positive直接外推 HCP；
- current surface graph误当 Euclidean smooth surface。

---

## 10. Exact evidence要求

至少返回：

- independent `G0` canonicalizer / exact weighted graph equality checker；
- collision/reconstruction atlas；
- exact `B3/B4` oracle on witness range；
- pair-overlap / hypergraph residual engine if needed；
- first kill witness with full contact data；
- carrier class counts and serialized/update-cost comparison；
- theorem/counterexample ledger。

Theorem-critical path使用 integer/combinatorial arithmetic。

---

## 11. 返回问题

最终必须明确回答：

1. weighted current frontier 是否足以预测 B3？
2. 它能否递归更新自身？
3. 若不能，第一缺失 correlation 是 pairwise、triple/hypergraph，还是 slot/embedding identity？
4. 最小 practical repair 比 `M3` 小多少？
5. FCC/HCP 在 reconstruction debt 上是否不同？
6. surface future precision 是否需要随 horizon显式增长，还是存在 fixed-form stationary carrier？
7. 哪些 interior信息可以永久 collapse，哪些必须通过 boundary residual继续携带？

核心目标：

`native rough surface -> minimal recursive frontier state -> algebraic collapse boundary`。
