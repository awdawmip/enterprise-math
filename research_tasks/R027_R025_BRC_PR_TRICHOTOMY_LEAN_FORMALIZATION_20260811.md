<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R027-R025-BRC-PR-TRICHOTOMY-LEAN-FORMALIZATION",
  "title": "R027 R025 Constant-(p,r) BRC Trichotomy Lean Formalization and Root-Coverage Gate",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_FORMALIZATION",
  "frontier": "Formalize the strongest exact constant-parameter law returned by R025: p-th-power endpoint BRC under constant exponent p and constant integer refinement r splits into aligned freeze, sub-threshold interval-funnel, and super-threshold collision-free binary regimes, with the exact zero/positivity and perfect-power boundaries made explicit.",
  "next_action": "Build an exact Nat.nthRoot-based root-index dynamics layer, prove the three regimes and their finite-support consequences, connect them narrowly to the canonical Boolean/result-support BRC carrier, and obtain a real root-covered warnings-fatal Lean gate without changing R023 semantics.",
  "dependencies": [
    {
      "target": "RS-R025-MULTILAYER-COLLAPSE-POLICY-DYNAMICS-ATLAS",
      "action": "CONSUME_ACCEPTED_R025_CONSTANT_PR_TRICHOTOMY_FROM_PR_504_HEAD_965e8cd52dcf939499c073dbef01789c225f384e",
      "satisfied": true
    },
    {
      "target": "R023/R023I canonical BRC Boolean-support semantic core",
      "action": "CONSUME_CANONICAL_MAIN_AT_3bbddc4661647537834953cfd64264fc965be292_WITHOUT_REOPENING_SEMANTICS",
      "satisfied": true
    },
    {
      "target": "EnterpriseMath.IntegerRoot",
      "action": "REUSE_NAT_NTHROOT_BASIN_GALOIS_AND_PERFECT_POWER_THEOREMS",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R025 Draft PR #504 / owner head 965e8cd52dcf939499c073dbef01789c225f384e",
    "docs/R025_MULTILAYER_COLLAPSE_POLICY_DYNAMICS_REPORT.md §9 and §12 at R025 owner head",
    "R025 exact BRC attacks: 431,361 funnel interval cases and 179,140 binary-regime checks with zero violations",
    "EnterpriseMath/Arithmetic/IntegerRoot.lean canonical main",
    "EnterpriseMath/Relation/BranchRecoalescence.lean canonical main / CANONICAL_MAIN + LEAN_CHECKED_MAIN"
  ],
  "evidence_status": "R025_BRC_TRICHOTOMY_LEAN_FORMALIZATION_GATE",
  "last_progress_ref": "R025 Driver acceptance selected the constant-(p,r) BRC trichotomy as the highest-leverage theorem candidate and froze positivity/zero and aligned-island boundaries",
  "last_progress_at": "2026-08-11T23:22:00+08:00",
  "hard_block": null,
  "tags": [
    "R027",
    "R025",
    "BRC",
    "branch-recoalescence-collapse",
    "Lean",
    "integer-root",
    "perfect-power",
    "interval-funnel",
    "binary-doubling",
    "precision-refinement"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R027",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R027 — R025 Constant-(p,r) BRC Trichotomy Lean Formalization and Root-Coverage Gate

Status: `READY / P0 / FOUNDATIONAL_FORMALIZATION / EXACT ROOT-INDEX DYNAMICS / NOT CANONICAL`

## 1. 母问题

R025 在 exact integer/rational 多层实验中发现：对固定指数 `p`、固定整数 refinement `r`、identity inter-layer operation，以及 p-th-power endpoint BRC，branch dynamics 不是无结构地“指数爆炸”，而是由 `(p,r)` 落入三个精确相区：

1. `r=a^p`：aligned freeze；
2. `1<r<2^p`：root-index interval funnel；
3. `r>2^p` 且 `r` 不是 p-th power：positive root-index support 上 collision-free exact binary doubling。

本任务要回答：

> 这三分律能否只使用 exact natural-number / integer-root 结构，在 Lean 中以最弱而清晰的假设完整证明，并真正通过覆盖新模块本身的 warnings-fatal root gate？

本任务不是重新研究 BRC 的一般语义。R023/R023I 的 Boolean/result-support core 已经 canonical；R027 只证明一个 arithmetic/precision specialization。

---

## 2. 冻结语义与边界

必须保持以下边界：

- `p : ℕ`，主 theorem 使用 `2 ≤ p`；
- `r : ℕ`，主 regime classifier 使用 `1 ≤ r`；
- root-index state `k : ℕ`；
- physical fine state specialization为 `k^p`；
- refinement 后 fine input 为 `r * k^p`；
- collapse endpoints 由 exact `Nat.nthRoot` / `EnterpriseMath.IntegerRoot.root` 决定；
- BRC carrier 仍然是 Boolean/set-valued support；
- 不保留或声称 multiplicity、provenance、probability/weights、signed/amplitude cancellation；
- 不修改 canonical R023 theorem statements、assumptions、namespace 或 carrier。

### 强制零边界

`k=0` 必须特殊处理：

`r * 0^p = 0`

永远 exact，因此 root index `0` 不分叉。

所以 super-threshold 的 `2×` cardinality theorem 必须要求 **positive parent support**。禁止把它偷升格成含 `0` 的任意 support doubling。

### 强制 aligned-island 边界

`r=2^p` 不是 binary boundary point，而是 aligned freeze，因为 `r=(2)^p`。

同样，`r>2^p` 上仍存在 perfect-pth-power freeze islands，如 `p=2,r=9`。

所以禁止陈述：

`r ≥ 2^p -> binary`。

正确 super-threshold 条件必须排除 `r=a^p`。

---

## 3. 推荐 formal object

优先新建：

`EnterpriseMath/Precision/PowerBRCTrichotomy.lean`

可使用同义但更合适的路径，仅在 return 中解释原因；不要把该 specialization 塞进 `BranchRecoalescence.lean` 本体。

建议 exact definitions：

```lean
refinedPowerInput p r k := r * k ^ p
rootIndex p r k := EnterpriseMath.IntegerRoot.root p (refinedPowerInput p r k)
```

定义 root-index child support 时，必须尊重 exact-power convention：

- 若 `r*k^p` 是 exact p-th power：singleton child root index；
- 否则：lower/upper 两个相邻 root indices `{m,m+1}`。

可以使用 `Finset ℕ`、`Set ℕ` 或二者桥接，但 finite cardinality theorem 应有明确 finite carrier。

最终 actual-state BRC support 可通过 `j ↦ j^p` 从 root-index support 得到；不要把 root index 与 p-th-power state 字面混同。

---

## 4. R027-L01 — exact refinement/root bridge

对：

`m = root p (r * k^p)`

建立可复用的 exact basin facts：

```text
m^p ≤ r*k^p < (m+1)^p.
```

优先直接消费：

- `EnterpriseMath.IntegerRoot.root_eq_iff`；
- `root_monotone`；
- `root_pow`；
- `collapse_eq_self_iff`；
- mathlib `Nat.nthRoot` / power monotonicity lemmas。

不得使用 theorem-critical floating root。

---

## 5. R027-L02 — aligned freeze

证明：若

```text
r = a^p
```

则对所有 `k`：

```text
root p (r*k^p) = a*k
```

且

```text
r*k^p = (a*k)^p.
```

因此 child-root support 是 singleton `{a*k}`，actual p-th-power support 也是 singleton `{(a*k)^p}`。

推导 constant `(p,r)` multilayer corollary：第一次 collapse 之后，只要每层都用同一 p-th-power-aligned refinement，后续每层都 exact，不再产生新 branch。

要求覆盖：

- `a=1` / `r=1`；
- `a=2` / `r=2^p`；
- super-threshold aligned islands `a≥3`。

---

## 6. R027-L03 — positive nonalignment means genuine ambiguity

证明以下关键 cancellation lemma：

若：

```text
2 ≤ p,
k > 0,
¬ ∃ a, r = a^p,
```

则：

```text
r*k^p
```

不是 exact p-th power。

建议 proof route：

若 `b^p = r*k^p`，则 `k^p ∣ b^p`；由正指数 power divisibility 得到 `k ∣ b`，写 `b=k*a`，再取消正的 `k^p` 得 `r=a^p`，矛盾。

允许使用 prime-valuation / factorization route，但优先使用更小的 divisibility/cancellation证明。

该 lemma 是 binary doubling 的 load-bearing 前提。若它在 Nat 上需要额外 hypothesis，必须返回最弱正确版本，不得掩盖。

---

## 7. R027-L04 — threshold root-index bounds

令：

```text
m_k = root p (r*k^p).
```

### Sub-threshold

对 `k>0`、`1<r<2^p`，证明：

```text
k ≤ m_k < 2*k.
```

### Super-threshold

对 `k>0`、`r>2^p`，证明至少：

```text
2*k ≤ m_k.
```

这些必须由整数 power/root inequalities 得到，不允许用浮点近似。

---

## 8. R027-L05 — funnel local spacing theorem

在：

```text
2 ≤ p,
1 < r < 2^p
```

下证明 root-index sequence 的 exact local spacing：

```text
m_k + 1 ≤ m_(k+1) ≤ m_k + 2.
```

`k=0` 可以独立证明；正 `k` 推荐使用 L04 与 cross-multiplication/power monotonicity。

一个可尝试的纯整数 proof architecture：

- lower step：从 `k ≤ m_k` 推出 `(m_k+1)k ≤ m_k(k+1)`，与 `m_k^p ≤ r k^p` 结合；
- upper step：从 `m_k < 2k` 推出 `(m_k+1)(k+1) ≤ k(m_k+3)`，与 `r k^p < (m_k+1)^p` 结合；
- 通过正的 `k^p` cancellation 把 inequalities 转回 `r(k+1)^p` 的 root basin。

研究员可以找到更短 Lean proof，但 theorem target 不得无故加强。

---

## 9. R027-L06 — exact interval-funnel support theorem

定义一个 root-index interval support：

```text
[A,B] ∩ ℕ
```

或 `Finset.Icc A B`。

证明在 `1<r<2^p` 下，一层 exact BRC child-root union 仍然是一个无洞整数区间。

目标形式应明确端点。优先证明类似：

```text
ChildSupport([A,B]) = [lower(A), upper(B)]
```

其中：

- `lower(A)=m_A`；
- `upper(B)` 按 exact/nonexact convention 定义；
- 对正 `B` 在该 regime 下可化为 `m_B+1`；
- `A=B=0` 等零边界必须正确。

利用 L05：相邻 parent 的 child pairs 只会 overlap 或 touch，不会留下 hole。

### 强制负边界

禁止证明：

“funnel 每一层都必然发生 duplicate collision”。

有限区间上可能连续出现 spacing `2`，从而当层没有 duplicate；真正冻结的 exact theorem 是 **interval/no-hole representation**，不是每层 collision 必然为正。

---

## 10. R027-L07 — repeated funnel invariant

由 L06 归纳证明：

只要 constant `(p,r)` 满足 `1<r<2^p`，从一个 root-index interval support 出发，任意有限层之后仍是 root-index interval。

因此 exact Boolean support 可以由两个 interval endpoints 表示，而无需物化整棵 branch tree。

至少给出 one-step cardinality upper bound：若 parent interval card 为 `N`，则 child interval card `≤2N`。

若能自然得到更强的 exact finite-depth / asymptotic subbinary bound，可以证明；否则不要为了匹配 R025 prose 强行引入脆弱的 Real `r^(1/p)` asymptotics。定量 `c^t` growth 可留给 descendant theorem。

---

## 11. R027-L08 — super-threshold local separation

在：

```text
2 ≤ p,
r > 2^p
```

下，对正 `k` 证明：

```text
m_k + 2 ≤ m_(k+1).
```

推荐纯整数 route：

- L04 给 `2k ≤ m_k`；
- 因而 `(m_k+2)k ≤ m_k(k+1)`；
- 与 `m_k^p ≤ r k^p`、正 cancellation 组合。

这条 theorem 本身不需要 nonalignment；nonalignment 用于保证每个 positive parent 真有两个 children。

---

## 12. R027-L09 — binary child injection

在：

```text
2 ≤ p,
r > 2^p,
¬ ∃ a, r=a^p,
k>0
```

下，每个 positive parent `k` 有恰好两个 child root indices：

```text
m_k,
m_k+1.
```

利用 L08 证明不同 positive parents 的 child pairs 不相交。

优先构造显式 injection：

```text
(parent, side : Bool) ↦ childRootIndex parent side
```

并证明 injective。

---

## 13. R027-L10 — exact finite-support binary doubling

对任意 finite positive root-index support `S`，在 super-threshold nonaligned regime 证明：

```text
card (ChildSupport S) = 2 * card S.
```

进一步归纳 constant `(p,r)` repeated dynamics：

```text
card S_t = 2^t * card S_0
```

前提必须保证初始 support 全正；并证明正性在该 regime 下被下一层保持。

### 强制 mutation / counterexample

自动验证或 Lean example 必须捕捉：

- 若 `0∈S`，`2*card` blanket theorem 失败；
- `r=2^p` 时 doubling 失败，因为 aligned freeze；
- `p=2,r=9` 时 doubling 失败，因为 super-threshold aligned island。

---

## 14. R027-L11 — regime classifier exhaustion

对：

```text
2 ≤ p,
1 ≤ r
```

给出互斥且穷尽的 arithmetic classification。

推荐 classifier：

### ALIGNED

```text
∃ a, r=a^p
```

### FUNNEL

```text
¬ aligned ∧ r < 2^p
```

在 `r≥1` 下可进一步推出 `1<r<2^p`，因为 `r=1=1^p` 已 aligned。

### BINARY

```text
¬ aligned ∧ 2^p < r
```

由于 `r=2^p` 本身 aligned，nonaligned 情形不会遗漏 equality boundary。

必须证明：

- pairwise disjoint；
- exhaustive；
- classifier 与 L02/L06/L10 的 semantic consequences 对接。

---

## 15. R027-L12 — actual p-th-power support bridge

root-index theorem 不能只停在整数 label。

定义 actual endpoint-state support：

```text
PowerSupport p K = {k^p | k∈K}
```

证明在 `p>0` 下 powering 对 root indices injective，因此：

- root-index singleton freeze 等价于 actual p-th-power singleton freeze；
- interval-funnel root support 唯一决定 actual Boolean endpoint support；
- binary root-index cardinality 等于 actual p-th-power support cardinality。

这一步只做 arithmetic specialization；不要重新实现 generic R023 BRC theorem。

---

## 16. R027-L13 — 与 canonical R023 BRC 的窄连接

R023 已 canonical：

`CANONICAL_MAIN + LEAN_CHECKED_MAIN`。

R027 只允许建立以下 layering：

```text
R023 generic exact Boolean/result-support branching semantics
        ↓ specialization
constant-(p,r) perfect-power endpoint relation
        ↓ arithmetic structure
ALIGNED / FUNNEL / BINARY runtime phase
```

禁止：

- 修改 `EnterpriseMath/Relation/BranchRecoalescence.lean` theorem statement；
- 把 R025 stochastic probability law塞进 Boolean BRC carrier；
- 把 binary branch count 当 path multiplicity theorem；
- 把 R024 runtime benchmark claim 当数学证明。

---

## 17. R027-L14 — executable finite oracle / mutation gate

可以新增一个小型 exact Python oracle 或 Lean finite examples，但它是 proof debugging / regression support，不替代 theorem。

至少自动覆盖：

1. aligned `r=1`；
2. aligned boundary `r=2^p`；
3. aligned island `p=2,r=9`；
4. funnel examples `p=2,r=2,3`、`p=3,r=2..7`；
5. binary examples `p=2,r=5,6,7,8,10` 中排除 square；
6. zero-support mutation；
7. one-step funnel spacing 可以全为 `2` 的有限窗口，确保没有误写“每层必碰撞”。

若 bounded oracle 发现 theorem statement 的真实 counterexample，立即停止 Lean 强推，返回 theorem break。

---

## 18. Lean validation coverage — 本任务的硬要求

R023 曾暴露一个 validation-coverage bug：root build PASS，但新 module 当时没有被 `EnterpriseMath.lean` import，因此并未实际编译。

R027 不得重复该错误。

若返回中出现：

```text
LEAN_CHECKED
ROOT_BUILD_PASS
```

必须提供**实际覆盖 R027 新模块**的编译证据。

推荐最终 owner validation 形态：

1. 新 module 保持在 owner branch；
2. `EnterpriseMath.lean` 在 validation head 显式 import R027 module；
3. 若 root import 进入 owner PR，则 machine/human exact root indexes 同步登记为 WIP，避免 common-surface drift；
4. 实际执行：

```text
lake build --wfail -KCI EnterpriseMath
```

5. run/job log 必须显示 R027 module 被 Built；
6. 不得用“workflow overall PASS”代替 module coverage 证明。

如果只完成 direct module compile 而未完成 root coverage，只能返回 `LEAN_MODULE_CHECKED_WIP`，不能返回 `ROOT_BUILD_PASS`。

---

## 19. Axiom / proof hygiene

最终 Lean payload：

- `sorry = 0`；
- `admit = 0`；
- 不增加 task-local `axiom` / `postulate`；
- 核心 theorem 使用 `#print axioms` 或等价 audit；
- theorem statement 不允许为了让 tactic 通过而静默改弱；
- 若确需加强 hypothesis，必须在 return matrix 中说明 R025 prose → Lean exact statement 的差异。

---

## 20. 强制 kill pressure

必须主动攻击以下错误版本：

1. `r ≥ 2^p` 自动 binary；
2. binary doubling 对含 `0` support 仍成立；
3. `1<r<2^p` 每一层都必有 duplicate collision；
4. nonaligned `r` 乘某个 positive `k^p` 后可能偶然变 exact p-th power；
5. interval funnel 自动等价于某个 multiplicity/probability theorem；
6. variable `(p_t,r_t)` words 自动继承 constant-regime trichotomy；
7. R025 bounded attacks 本身等于 proof。

任何一个若被真实 counterexample 击中，冻结最小反例并缩窄 theorem。

---

## 21. Prior-art / novelty boundary

以下属于普通/既有数学工具，不做 generic novelty claim：

- integer nth root；
- perfect powers；
- divisibility/cancellation；
- finite interval images；
- monotone integer sequences；
- finite-set injections/cardinality；
- elementary regime partition。

Enterprise Math 需要冻结的是：

- 这些结构在 p-th-power collapse + integer precision refinement + exact Boolean BRC endpoint support 中形成的具体三分运行律；
- 它与 canonical R023 semantic core、R024 runtime representation selection 的精确接口。

---

## 22. R024 downstream bridge

若三分律 formalized，return 中必须给出一个不修改 R024 benchmark 结论的 deterministic routing table：

| Formal regime | Runtime implication candidate |
|---|---|
| ALIGNED | fixed-point / exact-power shortcut |
| FUNNEL | symbolic root-index interval / basin cursor |
| BINARY | explicit branch budget or factored binary token; avoid pretending recoalescence exists |

这是 downstream interface，不在 R027 中 benchmark 性能。

---

## 23. Scope / file discipline

优先 owner payload：

- `EnterpriseMath/Precision/PowerBRCTrichotomy.lean`；
- 可选小型 exact oracle/test；
- `docs/R027_R025_BRC_TRICHOTOMY_LEAN_RETURN.md`；
- root validation 所必需的最小 `EnterpriseMath.lean` + machine/human WIP index delta。

不要：

- 修改 R025 research data；
- 吸收 R024 runtime implementation；
- 扩展 R023 carrier；
- 顺手 formalize martingale、microphase、UP closure 等其他 R025 theorem candidates。

这些属于后续独立 lane。

---

## 24. Return matrix

最终至少返回：

| Claim | R025 research form | Lean exact statement | Status | Required hypotheses | Counterexample boundary |
|---|---|---|---|---|---|
| aligned freeze | | | | | |
| nonalignment ambiguity | | | | | |
| funnel spacing | | | | | |
| interval support invariant | | | | | |
| repeated funnel invariant | | | | | |
| binary separation | | | | | |
| finite-support doubling | | | | | |
| repeated `2^t` growth | | | | | |
| regime exhaustion | | | | | |
| actual p-th-power support bridge | | | | | |

---

## 25. Return tokens

优先 positive return：

`R025_BRC_TRICHOTOMY_LEAN_CHECKED / ALIGNED_FUNNEL_BINARY_CLASSIFIED / POSITIVE_SUPPORT_BOUNDARY_FROZEN / ROOT_BUILD_PASS / NOT_CANONICAL`

若 module proved 但只直接编译、未获得真实 root coverage：

`R025_BRC_TRICHOTOMY_LEAN_MODULE_CHECKED / ROOT_COVERAGE_PENDING / NOT_CANONICAL`

若某个主 regime theorem 被真实反例击穿：

`R025_BRC_TRICHOTOMY_BREAK_FOUND / MINIMAL_COUNTEREXAMPLE_FROZEN / RETURN_TO_R025 / NOT_CANONICAL`

若核心三分成立，但部分 quantitative growth prose 必须降级：

`R025_BRC_TRICHOTOMY_CORE_PROVED / QUANTITATIVE_GROWTH_SCOPE_NARROWED / ROOT_BUILD_PASS / NOT_CANONICAL`

不要返回无界自由文本 verdict；在上述 token 后附完整 evidence package。

---

## 26. 最终判断标准

本任务成功的标准不是“把 R025 报告翻译成 Lean 文件”。

真正成功必须回答：

> 对 constant p、constant integer refinement r 的 p-th-power endpoint BRC，是否存在一个 exact arithmetic phase classifier，使我们仅从 `(p,r)` 就能证明下一层 support 是 freeze、interval-funnel，还是 positive-support collision-free binary expansion？

如果答案为是，冻结最弱正确 theorem surface，并让它真正通过覆盖自身的 Lean gate。

如果答案需要额外假设，明确写出。

如果 R025 prose 某一部分过强，保留正确 core、杀掉过强部分，不要为了保持叙述漂亮而修改数学。
