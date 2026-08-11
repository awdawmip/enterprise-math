<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R028-BRC-RETROSPECTIVE-DISTINCTION-CREDIT-CALCULUS",
  "title": "R028 Retrospective Distinction Credit, Precision-Debt Attribution, and Rewind Calculus",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_CALCULUS_DISCOVERY",
  "frontier": "Turn the R022/R020/R023 future-relative precision machinery into an exact retrospective information-credit calculus: determine when a past distinction, feature, checkpoint, or branch separation deserves credit relative to a declared future language; quantify how much precision debt or rewind it removes; and classify additivity, interaction, hindsight, and safe-recoalescence boundaries without importing causal or reinforcement-learning semantics by analogy alone.",
  "next_action": "Build a finite exact partition/signature laboratory, formalize candidate debt/credit functionals, exhaustively attack additivity/submodularity/order-independence and hindsight-safety claims, isolate surviving laws, connect zero-credit distinctions to suffix-safe BRC recoalescence, and return a theorem/counterexample/prior-art matrix suitable for later Lean formalization.",
  "dependencies": [
    {
      "target": "RS-R022-HASHCLASH-BRC-TOOL-MINING",
      "action": "CONSUME_PRECISION_DEBT_DISTINCTION_COVER_ADAPTIVE_SIGNATURE_AND_REWIND_RESULTS_FROM_PR_497_HEAD_195b2be6ac184c8073ef6eb1b425a373acebd585",
      "satisfied": true
    },
    {
      "target": "RS-R020-P021-WITNESS-CARDINALITY-DYNAMIC-COMPLETENESS-REAUDIT",
      "action": "CONSUME_FUTURE_LANGUAGE_RELATIVE_DYNAMIC_COMPLETENESS_AND_CARRIER_BOUNDARIES",
      "satisfied": true
    },
    {
      "target": "R023/R023I canonical BRC Boolean-support semantic core",
      "action": "CONSUME_CANONICAL_SUFFIX_SAFE_RECOALESCENCE_AND_NO_RESURRECTION_AT_MAIN_3bbddc4661647537834953cfd64264fc965be292_WITHOUT_REOPENING_SEMANTICS",
      "satisfied": true
    },
    {
      "target": "R014 representation-resource methodology",
      "action": "CHARGE_FEATURE_SIDE_METADATA_CHECKPOINT_STORAGE_PROBES_AND_REWIND_COST_HONESTLY",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R022 Draft PR #497 / owner head 195b2be6ac184c8073ef6eb1b425a373acebd585",
    "R022 precision debt M(E=>F), distinction-cover duality, adaptive signature acquisition, checkpoint sufficiency and storage/rewind Pareto",
    "R020 Draft PR #501 / future-language-relative dynamic carrier classification",
    "canonical EnterpriseMath/Relation/BranchRecoalescence.lean at main@3bbddc4661647537834953cfd64264fc965be292",
    "R023 FORGETFUL_RECOALESCENCE_IFF and NO_RESURRECTION boundaries",
    "user hypothesis: BRC may admit a retrospective information-credit assignment interpretation"
  ],
  "evidence_status": "RETROSPECTIVE_INFORMATION_CREDIT_FOUNDATION_PROBE",
  "last_progress_ref": "User identified the R022 precision-debt/distinction machinery as resembling retrospective credit assignment; Driver sharpened the target to task-relative distinction credit rather than causal reward attribution",
  "last_progress_at": "2026-08-12T00:10:00+08:00",
  "hard_block": null,
  "tags": [
    "R028",
    "BRC",
    "retrospective-credit",
    "distinction-credit",
    "precision-debt",
    "rewind",
    "future-language",
    "feature-attribution",
    "partition-lattice",
    "checkpoint",
    "recoalescence",
    "counterexample"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R028",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R028 — Retrospective Distinction Credit, Precision-Debt Attribution, and Rewind Calculus

Status: `READY / P0 / FOUNDATIONAL_CALCULUS_DISCOVERY / ADVERSARIAL_FINITE_MODEL / NOT CANONICAL`

## 0. 任务前后完成度与推进向量

任务前估计：

- retrospective-credit 概念清晰度：25%
- exact mathematical definition：10%
- minimal counterexample coverage：5%
- executable finite atlas：10%
- prior-art rooting：5%
- BRC/runtime integration boundary：20%

任务目标完成后：

- retrospective-credit 概念清晰度：90%+
- exact mathematical definition：80%+
- minimal counterexample coverage：90%+
- executable finite atlas：90%+
- prior-art rooting：80%+
- BRC/runtime integration boundary：80%+

推进向量：

`credit-calculus +65% / BRC-semantics +0% / runtime-policy +15% / causal-claims +0% / formalization-readiness +45%`

本任务允许研究结果杀掉“后验信用分配”这个术语或某些漂亮公式。若最终只剩 classical partition/feature-attribution machinery，应明确 rooting，不得为了保留新术语而夸大。

---

## 1. 母问题

R022 已经给出三个彼此咬合的结构：

1. future language `U` 决定目标精度：

   `K(U) = intersection_{u in U} ker(o ∘ u)`；

2. 当前 partition/encoding `E` 到目标 `F` 的 exact side-information debt：

   `M(E=>F) = max_{C in X/E} # {F-classes intersecting C}`；

   fixed-width debt：

   `B(E=>F) = ceil(log2 M(E=>F))`；

3. required distinction pairs：

   `P(E,F) = {{x,y}: x E y and not x F y}`；

   feature/probe basis selection呈 Distinction Cover / Set Cover 结构。

R023 又证明：forgetful recoalescence 是否安全，恰好由剩余 suffix 的 support signature 是否相等决定。

这提示一个新的问题：

> 对某个最终任务、未来语言或 suffix 来说，过去保留的哪些 distinction 真正“有信用”？一个 feature、bit、checkpoint、branch split 或 side label 到底减少了多少未来所需信息、多少 rewind、多少不可恢复风险？

以及更强的问题：

> 当未来逐步兑现、remaining language 缩小时，过去某些 distinction 是否会“失去信用”，从而触发合法 recoalescence？

本任务必须把这个直觉从比喻变成 exact calculus，或证明它无法形成一个统一、稳定、非任意的 scalar credit theory。

---

## 2. 首要语义纪律：credit 不是 causal contribution

本任务禁止把“后验信用”直接解释成因果贡献、奖励归因或强化学习 action credit。

必须严格区分：

- `RETROSPECTIVE_RELEVANCE`：某个 distinction 对声明 target/future 是否必要；
- `PRECISION_DEBT_REDUCTION`：保留该 distinction 后，exact completion 所需 side information 减少多少；
- `REWIND_REDUCTION`：保留该 distinction 后，最少回退多少 checkpoint；
- `COVERAGE`：该 feature 区分了多少 required pairs；
- `CAUSAL_CONTRIBUTION`：只有在另有 intervention/counterfactual causal model 时才可谈，本任务默认不拥有。

必须明确冻结：

`retrospective relevance != causal responsibility`。

若 prior-art 中已有 Shapley attribution、cooperative game credit、feature attribution、RL credit assignment 等，只能作为 comparator/rooting；不能把它们的语义自动移植进 Enterprise Math。

---

## 3. 第一阶段 formal universe：有限精确 partition/signature 模型

优先建立有限状态宇宙：

`X = {0,...,n-1}` 或任意 finite carrier。

一个 current encoding `e : X -> ECode` 只通过其 kernel/equivalence 使用：

`E = ker(e)`。

一个 future target/signature `sigma : X -> T` 给出：

`F = ker(sigma)`。

约定 relation inclusion 方向：

- `E' subseteq E` 表示 `E'` 更细；
- exact equality 最细；
- universal equivalence 最粗。

候选 feature/probe：

`phi : X -> A`

引入 refinement：

`E[phi] = E intersect ker(phi)`。

多个 features `S={phi_1,...,phi_m}`：

`E[S] = E intersect intersection_{phi in S} ker(phi)`。

不得把 feature alphabet size、读取成本、storage bits、semantic distinctions 混成同一个量。

---

## 4. R028-D1 — local/global precision debt

冻结 R022 的 exact worst-case side-label debt：

对每个 current class `C in X/E`，定义 local target multiplicity：

`m_C(E=>F) = # {F-classes D : C intersect D != empty}`。

全局 alphabet debt：

`M(E=>F) = max_C m_C(E=>F)`。

fixed-width bit debt：

`B(E=>F) = ceilLog2 M(E=>F)`。

必须验证/证明：

1. `M>=1`；
2. `M(E=>F)=1 iff E subseteq F`；
3. refinement monotonicity：若 `E' subseteq E`，则
   `M(E'=>F) <= M(E=>F)`；
4. 因而 `B` 也不增；
5. local debt 与 worst-case global debt 不可偷换；
6. 若引入概率分布得到 expected debt，必须显式携带 measure，不能从 worst-case 定理推出平均定理。

优先把 R022 的证明/枚举独立复跑，而不是仅复制结论。

---

## 5. R028-D2 — distinction pair universe 与 feature cover

定义 required distinction pair universe：

`P(E,F) = {{x,y}: x E y and not x F y}`。

feature `phi` 的 exact distinction coverage：

`Cover_phi(E,F) = {{x,y} in P(E,F): phi(x) != phi(y)}`。

feature family `S` 完成 target refinement 当且仅当：

`union_{phi in S} Cover_phi(E,F) = P(E,F)`。

应验证其与：

`E[S] subseteq F`

精确等价。

把 minimum feature basis 明确 rooted 到 Set Cover / Test Cover / distinguishing family 等已有结构；项目价值在于 future-safe precision 与 BRC checkpoint 的统一应用，而不是重命名经典 set cover。

---

## 6. R028-C1 — 至少四种不同 credit，不得混为一个数

至少比较以下 credit definitions。

### C1A — Pair Coverage Credit

`C_pair(phi | S) = |Cover_phi \ union_{psi in S} Cover_psi|`

即 feature 在已有 feature set `S` 之外新增区分了多少 required pairs。

研究 normalized / weighted variant，但权重必须显式给定。

### C1B — Alphabet-Debt Marginal Credit

`C_M(phi | S) = M(E[S]=>F) - M(E[S∪{phi}]=>F)`。

这是 exact integer worst-case side-label alphabet reduction。

### C1C — Bit-Debt Marginal Credit

`C_B(phi | S) = B(E[S]=>F) - B(E[S∪{phi}]=>F)`。

注意 ceiling 会制造 plateau；一个 feature 可以区分真实 required pairs，却有 `C_B=0`。

### C1D — Rewind Credit

给定 checkpoint sequence `E_0,...,E_t` 与 target `F`，定义最晚可 exact recover 的 checkpoint、最少 rewind depth；feature/side metadata 的 rewind credit 是其使 recovery point 向前移动的量。

必须严格定义 checkpoint 时间方向与 partition refinement/forgetting方向。

不得宣称这四种 credit 必然同序、同值或可互换。

---

## 7. R028-H1 — nonnegative marginal debt credit

优先证明：

对任意 feature refinement，

`C_M(phi|S) >= 0`

且

`C_B(phi|S) >= 0`。

若失败，给出最小反例并检查定义方向是否错误。

这只是“多保留信息不会让 exact completion 更困难”的 worst-case statement，不代表 feature 有正 causal value。

---

## 8. R028-H2 — ordered credit conservation / telescoping

对 feature sequence `(phi_1,...,phi_m)`，令：

`S_i={phi_1,...,phi_i}`。

则任一标量 debt `D` 的 ordered marginal：

`c_i = D(E[S_{i-1}],F)-D(E[S_i],F)`

应满足 telescoping：

`sum_i c_i = D(E,F)-D(E[S_m],F)`。

若 final feature family exact-completes target：

`E[S_m] subseteq F`，

则 total ordered credit 等于 initial debt。

必须同时对 `M` 与 `B` 分类：

- telescope 是代数恒等式；
- 每项 credit 分配一般可能顺序依赖；
- “总量守恒”不推出“每个 feature 有唯一 intrinsic credit”。

---

## 9. 强制 kill：order-independent intrinsic marginal credit

必须攻击：

`同一个 feature 的 marginal debt credit 与 feature 顺序无关`。

优先搜索最小 `|X|` 反例。

已知 Driver-side sanity target：3-state partition 模型很可能已经足以出现 redundancy/order dependence；研究员必须独立构造、最小化并冻结，不得直接把该提示当 proof。

至少区分：

- redundant features：谁先来谁拿走全部 debt credit；
- synergistic features：单独 credit 低/零，组合后突然支付 debt；
- complementary features；
- dominated features。

若找到更小/更清楚 witness，优先采用。

---

## 10. 强制 kill：debt-reduction 必然是 submodular

定义 set-valued total gain：

`G_D(S)=D(E,F)-D(E[S],F)`。

攻击：

`G_D` 对 feature set 总是 submodular / diminishing returns。

优先对 `M` 与 `B` 分别穷举。

特别寻找 synergy witness：

- feature A 单独不降低 debt；
- feature B 单独不降低 debt；
- A+B 一起降低 debt。

这会直接违反 diminishing returns。

若 submodularity 被杀，进一步研究：

- 是否存在 special regimes 使其成立；
- laminar / nested features；
- binary target；
- product partitions；
- single current fibre；
- uniform fibre profiles。

禁止因为 pair-coverage function 是 classical submodular coverage，就把 debt reduction 也宣称 submodular。

---

## 11. 强制 kill：debt-reduction 必然是 supermodular

同样攻击 supermodularity / increasing returns。

寻找 redundancy witness：多个 feature 单独都能支付同一 debt，组合没有额外收益。

目标是判断：

`G_M`、`G_B`

在一般 partition calculus 中是否既非 submodular 也非 supermodular。

如果成立，冻结最小反例。

---

## 12. R028-H3 — pair-coverage 的正向结构

`G_pair(S)=|union_{phi in S} Cover_phi|`

应属于标准 coverage function。

验证/证明：

- monotone；
- submodular；
- ordered marginal nonnegative；
- total pair coverage 与 exact completion 的关系。

然后明确负边界：

`pair coverage credit != precision-debt credit`。

要求最小 witness 表明：两个 feature 可以新增区分相同数量的 required pairs，却对 worst-case `M`/`B` debt 有不同影响；反之亦可。

---

## 13. R028-C2 — realized-path credit vs declared-future credit

这是本任务的核心语义防线。

对 declared future language `U`：

`F_U = intersection_{u in U} ker(o∘u)`。

对实际发生的一条 realized suffix `u*`：

`F_real = ker(o∘u*)`。

因为 `{u*} subseteq U`：

`F_U subseteq F_real`。

所以只按实际 realized path 计算的 required precision 一般更粗：

`D(E=>F_real) <= D(E=>F_U)`。

必须：

1. 证明该单调关系；
2. 找到最小 strict witness；
3. 冻结错误推论：

   `事后某 distinction 对 realized path 无用 => 当时可以安全删除`。

该推论一般错误，因为 alternate declared futures 可能读取它。

定义术语时至少区分：

- `DECLARED_LANGUAGE_CREDIT`
- `REALIZED_SUFFIX_CREDIT`

后者只对 replay/已冻结 suffix 安全，不能自动作为 online reusable carrier 的删除依据。

---

## 14. R028-H4 — future-language shrink 与 credit release

考虑随执行推进的 remaining future languages：

`U_0 ⊇ U_1 ⊇ ...`。

定义：

`F_t=K(U_t)`。

应证明：

`F_t subseteq F_{t+1}`

即 target partition 随 future language 缩小而变粗或不变。

因而 fixed current encoding `E` 的整体 debt：

`M(E=>F_t)`、`B(E=>F_t)`

应非增。

定义 required pair release：

`Released_t = P(E,F_t) \ P(E,F_{t+1})`。

这些 pair 在较短 future 下不再需要区分。

研究：

- global debt release；
- pair-credit release；
- individual feature marginal credit 是否也必然单调下降——不要预设，必须攻击；
- remaining language 扩张时相反的 precision debt 增长。

---

## 15. R028-C3 — zero-credit distinction 与 BRC recoalescence

把“区别已经没有信用”与 canonical R023 `FORGETFUL_RECOALESCENCE_IFF` 精确对接。

### Point-level

对两个 fine points `x,y`，若：

`pointSignature_U(x)=pointSignature_U(y)`，

则它们在 future target `F_U` 下同类；区分 `x,y` 对该 suffix 的 pair credit 为零。

### Support-level / BRC

R023 的真正 operational theorem作用在 exact supports `A,H`：

forgetful replacement safe iff remaining support signatures equal。

R028 必须明确：

`zero pair credit on points`

不自动推出任意 support replacement 安全。

应建立两层接口：

- point-distinction credit；
- support-signature credit。

如果想定义 branch distinction credit，应直接以 support signature 为 target，而不是把 pointwise equivalence 偷换成 branch safety。

目标表述：

> recoalescence 是“相对于 remaining future，某些 distinction 的 operational credit 降为零”这一解释的精确版本，但 only at the matching carrier/signature level。

不得修改 R023 theorem。

---

## 16. R028-C4 — no-resurrection 与 unpaid debt

利用 canonical `NO_RESURRECTION` 解释 unexpected language extension：

若当前 encoding `E` 已把某 pair 合并，而新 future target `F_new` 又要求区分它，则当前 debt 增加。

若没有：

- side metadata；
- earlier checkpoint；
- exact fine state；
- external reread/replay；

则不能通过之后的 branching“凭空支付”这笔 debt。

建立清晰分类：

- `DEBT_PAYABLE_BY_METADATA`
- `DEBT_PAYABLE_BY_REWIND`
- `DEBT_PAYABLE_BY_EXTERNAL_REREAD`
- `DEBT_UNRECOVERABLE_FROM_CURRENT_ENCODING`

最后一类必须与 no-resurrection 对齐。

---

## 17. R028-C5 — checkpoint rewind calculus

给定 checkpoint sequence：

`C_0, C_1, ..., C_T`

其中每个 checkpoint 有 encoding/kernel `E_t` 与 storage cost `s_t`。

针对 target `F`，定义：

`recoverable(t,F) : E_t subseteq F`

或带 side metadata `Z_t` 时：

`E_t intersect ker(Z_t) subseteq F`。

定义 latest exact checkpoint：

`t*(F)=max {t : recoverable(t,F)}`。

当前在 T 时的 rewind：

`R(F)=T-t*(F)`。

feature/metadata `phi` 的 rewind credit：

`C_R(phi)=R_before(F)-R_after(phi,F)`。

必须研究：

- nonnegative；
- order dependence；
- storage-cost/rewind Pareto；
- semantic debt (`M/B`) 与 rewind debt 是否同序——预期不必然；
- two checkpoints with same `B` debt but different rewind；
- same rewind but different side-bit debt。

至少复跑 R022 8-state `(0 bits, rewind 2)/(1 bit, rewind 1)/(2 bits, rewind 0)` witness，并寻找更小模型或证明其 declared class minimality。

---

## 18. R028-C6 — local credit vs global worst-case credit

全局 `M` 使用 max current fibre，可能导致大量 feature 在非 worst-case fibres 上确实有用，但全局 credit 为 0。

定义 local marginal：

`C_{M,C}(phi)`

并研究：

- global credit 0 but some local credit >0 的最小 witness；
- global credit >0 的必要条件；
- worst-case bottleneck class 如何迁移；
- feature 作用后新的 worst-case fibre 是否切换。

如果加入分布 `mu`，可研究 expected local credit，但：

- theorem input 必须显式含 `mu`；
- 不得从 uniform/sample distribution 偷推自然概率；
- stochastic attribution 与 Boolean BRC semantic core 保持分层。

---

## 19. R028-C7 — symmetric attribution comparator：Shapley 只作为 prior-art baseline

对于 finite feature set，若希望消除 feature ordering 的任意性，可把：

`v(S)=D(E,F)-D(E[S],F)`

视为 cooperative game，并计算 classical Shapley value。

本任务可以实现 exact rational Shapley baseline，但必须：

- 明确这是 classical cooperative-game attribution；
- 不宣称 Enterprise Math 发明 Shapley credit；
- 检查 `v` 非 submodular 时 Shapley 仍可定义，但解释变弱；
- 比较 Shapley、ordered marginal、pair coverage、debt credit、rewind credit 的差异；
- 找到 redundancy/synergy examples 中 Shapley 如何分配；
- 不把 Shapley 数值解释成 causal contribution。

如果 Shapley 对项目没有额外操作价值，可以返回 `PRIOR_ART_COMPARATOR_ONLY`，不必进入后续 formal surface。

---

## 20. Necessity / sufficiency credit classification

除了 scalar credit，还要研究更稳的布尔分类：

对 feature `phi`：

- `ESSENTIAL`：所有 exact-completing minimum bases 都必须包含；
- `OPTIONAL_USEFUL`：存在 exact-completing basis 包含它，但不是必须；
- `REDUNDANT_RELATIVE_TO_LIBRARY`：移除它不影响 achievable target；
- `DOMINATED`：其 distinction coverage 被更低成本 feature 覆盖；
- `SYNERGISTIC`：单独 debt credit 可能为 0，但与其他 feature 组合产生正 credit；
- `ZERO_FUTURE_CREDIT`：对当前 declared future target 不区分任何 required pair。

研究这些分类与 Set Cover / hitting-set backbone / feature selection prior art 的关系。

这部分可能比强行给每个 feature 一个唯一 scalar 更稳；若 scalar credit theory高度不唯一，应允许结论转向 typed credit profile。

---

## 21. 动态 credit profile

对时间 `t`、remaining language `U_t`、current encoding `E_t`、feature `phi`，定义 task-relative credit profile：

`Credit_t(phi) = (pair_coverage, alphabet_debt_reduction, bit_debt_reduction, rewind_reduction, acquisition_cost)`。

研究是否存在 partial order / Pareto dominance，而非强行 scalarize。

候选原则：

`phi` dominates `psi` if it weakly improves all declared credit dimensions and strictly improves one, at no greater acquisition/storage cost。

这直接连接 R014 representation-resource calculus。

若没有用户声明权重，禁止自动把多维 profile 压成一个 scalar score。

---

## 22. Adaptive acquisition / branch-on-demand

消费 R022 adaptive signature acquisition，但重新解释为 credit-aware acquisition：

- 当前 branch/context 下先计算 unresolved required distinctions；
- 只读取能覆盖当前 remaining distinction set 的 feature；
- 已经 zero-credit 的 feature 不读取；
- 新 future extension 可触发 additional acquisition / rewind。

比较：

- static read-all；
- static minimum distinction cover；
- adaptive decision tree；
- greedy marginal pair credit；
- greedy debt reduction；
- cost-aware ratio。

必须把 heuristic optimizer 与 exact verifier 分开。

目标不是发明新 decision-tree theorem，而是判断哪种 credit functional 对 BRC branch-on-demand runtime 真有指导价值。

---

## 23. Exhaustive finite laboratory

优先实现：

`experiments/r028_retrospective_credit_calculus.py`

以及：

`tests/test_r028_retrospective_credit_calculus.py`

最低 exhaustive 范围：

### Partition core

- 全部 `|X|<=5` set partitions；
- 所有 ordered `(E,F)` pairs；
- all candidate feature partitions / binary features where feasible；
- all 2-feature / 3-feature libraries where feasible。

### 必须统计

- debt monotonicity failures；
- zero-debt iff refinement failures；
- distinction-cover equivalence failures；
- marginal credit negativity；
- order-dependence minimal witness；
- submodularity minimal witness；
- supermodularity minimal witness；
- pair-coverage/debt-credit mismatch witnesses；
- local/global mismatch；
- realized-vs-declared strict gap；
- future-language shrink debt monotonicity；
- rewind/bit-debt ordering mismatches。

### BRC support model

再增加小 finite relation/support universe：

- `|X|<=4`；
- small relation generators；
- finite future languages；
- exact supportSignature；
- support-level zero-credit/recoalescence checks。

不要用 OCR、浮点或随机 sampling 替代 exhaustive core。

---

## 24. Candidate laws H1–H16

逐项返回 `PROVED / EXHAUSTIVE_CONFIRMED / KILLED / CONDITIONAL / PRIOR_ART`：

- H1: `M` refinement-monotone。
- H2: `B` refinement-monotone。
- H3: zero debt iff current encoding refines target。
- H4: exact completion iff feature coverage covers all required pairs。
- H5: marginal `M/B` credit nonnegative。
- H6: ordered marginal credit telescopes。
- H7: individual marginal debt credit order-independent。**重点 kill。**
- H8: debt-reduction gain always submodular。**重点 kill。**
- H9: debt-reduction gain always supermodular。**重点 kill。**
- H10: pair-coverage gain monotone submodular。
- H11: realized-path target never requires more precision than declared-language target。
- H12: realized-path zero credit implies ex-ante safe deletion。**重点 kill。**
- H13: shrinking remaining language cannot increase total precision debt。
- H14: every individual feature credit decreases monotonically as future language shrinks。**不要预设，重点攻击。**
- H15: zero support-signature distinction is exactly safe forgetful BRC recoalescence at matching carrier level。
- H16: side metadata/rewind can pay increased debt, but branching from an insufficient current encoding alone cannot resurrect erased required distinctions。

若发现更关键的新 law/negative boundary，可新增 H17+，但不要遗漏 H1–H16。

---

## 25. Minimal counterexample protocol

所有 killed laws 必须：

1. 先找最小 `|X|`；
2. 再最小化 partition block counts；
3. 再最小化 feature library size；
4. 给出 human-readable partition notation；
5. 给出 executable witness；
6. 区分 global minimality theorem 与仅在 declared finite search class 内 minimal。

不得把 bounded exhaustive minimality 偷升格成无界数学 minimality。

---

## 26. Prior-art rooting

必须主动比对并分类：

- partition lattice / equivalence refinement；
- sufficient statistics / minimal sufficient statistics；
- Myhill–Nerode / behavioral equivalence / bisimulation signatures；
- Test Cover / Set Cover / distinguishing sets；
- decision tree function evaluation；
- zero-error / worst-case side-information coding analogues；
- cooperative games / Shapley value；
- feature attribution；
- causal attribution / RL credit assignment；
- checkpointing / reversible computation / time-space tradeoff；
- information lattice / sigma-algebra refinement where relevant。

要求返回：

`PRIOR_ART_ROOTED` / `PROJECT_SPECIFIC_REPACKAGING` / `POSSIBLY_NEW_EXACT_COMBINATION`。

除非有明确文献调查支持，不得声称“后验 distinction credit calculus”是新数学。

---

## 27. 与 R022 的关系

R028 不是重复 HashClash 研究。

R022 已完成：

- precision debt；
- distinction cover；
- adaptive feature acquisition；
- checkpoint rewind；
- certificate calculus。

R028 要做的是把这些对象放进一个统一的 **credit attribution question** 中，研究：

- 哪些 scalar/profile 定义稳定；
- 哪些交互法则失败；
- credit 随 future language 如何变化；
- zero credit 与 recoalescence 的精确关系；
- cost-aware runtime 是否因此获得新的决策规则。

不要重新分析 MD5 differential path 或 SHA-1 collision technique。

---

## 28. 与 canonical R023 的关系

R023/R023I 已 canonical：

- `NO_RESURRECTION`；
- `ONE_STEP_COARSEST`；
- `SUPPORT_BRANCH_INVARIANT`；
- `FORGETFUL_RECOALESCENCE_IFF`。

R028 必须消费，不得修改。

特别地，R028 可以提出解释：

`safe recoalescence = remaining-future support distinction credit becomes zero`

但必须证明该解释严格匹配 support-signature carrier，不能用 credit terminology 改写 theorem truth。

---

## 29. 与 R020 的关系

R020 已冻结：

`COMPOSITION_SAFE[semantic target, future language]`

以及：

`witness/provenance -> N-path count -> Boolean support`

逆向不成立。

R028 必须参数化 credit 的 semantic target：

- `BOOL_SUPPORT_CREDIT`
- `N_PATH_COUNT_CREDIT`
- `WITNESS_PROVENANCE_CREDIT`

至少在概念层明确区分。

本任务核心默认仍是 deterministic/Boolean target precision；不要从 Boolean credit 推出 multiplicity/provenance credit。

---

## 30. 与 R024/runtime 的潜在连接

如果 R028 surviving calculus 足够稳定，给 R024/后续 runtime 返回以下候选决策接口：

`remaining_future_language`

`current_encoding_partition`

`candidate_metadata/features`

`candidate_checkpoint_rewind`

→

`credit_profile / cost_profile / Pareto decision`。

可能的 runtime policies：

- zero-credit metadata eviction；
- future-language shrink triggered recoalescence；
- positive-debt extension triggered feature acquisition；
- rewind vs side-metadata choice；
- adaptive probe ordering；
- checkpoint retention based on future-credit frontier。

这些必须先作为 tool candidate，不直接进入 Foundation primitive。

---

## 31. Resource accounting

所有实验必须计费：

- feature alphabet size；
- read/probe count；
- feature storage bits；
- checkpoint bytes；
- rewind steps；
- recomputation work；
- branch tokens；
- side labels；
- target/future signature storage if materialized。

禁止把 feature library、target partition、future language 或 branch dictionary 当免费 oracle。

若使用 Shapley/permutation averaging，报告 factorial/exponential exact computation成本和任何 approximation 方法；approximation 不得冒充 exact theorem evidence。

---

## 32. Deliverables

至少返回：

1. `docs/R028_RETROSPECTIVE_DISTINCTION_CREDIT_REPORT.md`
2. `experiments/r028_retrospective_credit_calculus.py`
3. `tests/test_r028_retrospective_credit_calculus.py`
4. `experiments/r028_credit_law_matrix.json`
5. `experiments/r028_minimal_counterexamples.json`
6. `experiments/r028_prior_art_matrix.json`
7. `experiments/r028_runtime_credit_profiles.json`

推荐另加：

8. `R028_CREDIT_CALCULUS_MATRIX.md`
9. `R028_FUTURE_LANGUAGE_CREDIT_ATLAS.md`
10. `R028_REWIND_STORAGE_PARETO.md`

---

## 33. Theorem/tool impact matrix

对每个 surviving result 标记：

- `SEMANTICALLY_STABLE`
- `NEW_DERIVED_CALCULUS`
- `CONDITIONALIZED`
- `PRIOR_ART_ROOTED`
- `COUNTEREXAMPLE_BOUNDARY`
- `RUNTIME_TOOL_CANDIDATE`
- `FORMALIZATION_CANDIDATE`
- `DO_NOT_PROMOTE`

至少覆盖：

- R022 precision debt；
- R022 distinction cover；
- R022 adaptive acquisition；
- R023 forgetful recoalescence；
- R023 no-resurrection；
- R020 future-language typing；
- R014 storage/work accounting；
- R024 runtime selector。

---

## 34. Downstream routing

任务结束时必须明确回答：

### A. 是否值得开 Lean formalization？

若 surviving core 清楚，返回建议新任务，只形式化：

- debt monotonicity/zero iff；
- distinction cover equivalence；
- ordered telescoping；
- declared-vs-realized future monotonicity；
- future-language shrink debt release；
- zero-credit/support-signature recoalescence bridge；
- 最关键 minimal counterexamples。

不要把 Shapley 或 runtime heuristic 强行 Lean 化。

### B. 是否需要回改 R022？

默认 `NO`。只有发现 R022 precision-debt theorem 本身错误才返回 owner repair。

### C. 是否需要回改 R023？

默认 `NO`。若 credit interpretation 与 R023 theorem 不兼容，优先修解释，不改 canonical theorem。

### D. 是否值得接 R024？

只有出现稳定、可计算、成本已计费的 credit profile 才建议 runtime integration。

---

## 35. 禁止事项

本任务不得：

- 宣称 credit = causality；
- 把 realized path 的 hindsight relevance 当 ex-ante safety；
- 把 feature coverage 与 debt reduction 混为一谈；
- 假设 marginal credit 顺序无关；
- 假设 debt gain submodular；
- 假设 debt gain supermodular；
- 用 Shapley value 给出一个数后就声称“真正信用”；
- 把 probability-free worst-case debt 解释成 expected information；
- 把 Boolean support credit 推广到 multiplicity/provenance；
- 修改 R023 canonical semantics；
- 重新研究 MD5/SHA collision attack；
- 把 bounded exhaustive minimality 宣称成全局定理。

---

## 36. 研究策略

优先顺序：

1. finite partition exact engine；
2. debt/coverage definitions cross-check；
3. H1–H6 positive core；
4. H7–H9 order/submodular/supermodular kill pressure；
5. H11–H14 hindsight/future-language dynamics；
6. checkpoint rewind calculus；
7. support-level BRC connection；
8. prior-art rooting；
9. runtime credit profiles；
10. only then propose formalization。

不要一开始就写长哲学解释；先让 finite exhaustive data 决定哪些信用直觉能活下来。

---

## 37. 预期最有价值的可能结果

允许以下任一种成为成功返回：

### Outcome A — Typed credit calculus survives

没有唯一 scalar，但存在稳定 profile：

`(distinction coverage, debt reduction, rewind reduction, cost)`

并能精确解释 BRC credit release/recoalescence。

### Outcome B — Ordered/path-dependent calculus survives

总 credit telescopes，但 feature attribution 必然顺序依赖；Shapley 只作为 classical symmetrization。

### Outcome C — Credit metaphor mostly collapses to prior art

若所有有意义部分都等价于 set cover + partition refinement + checkpointing + Shapley，则明确返回 rooting，保留 project-specific接口即可。

### Outcome D — Strong new negative boundary

若“后验信用”无法形成稳定 scalar，且不同 credit notions fundamentally incomparable，这也是高价值结果。

---

## 38. Preferred return markers

若得到稳定 typed/profile calculus：

`RETROSPECTIVE_DISTINCTION_CREDIT_CALCULUS_FOUND / FUTURE_RELATIVE_CREDIT_PROFILE_FROZEN / HINDSIGHT_BOUNDARY_CLASSIFIED / RECOALESCENCE_CREDIT_BRIDGE_CHECKED / NOT_CANONICAL`

若只有 ordered/path-dependent credit 成立：

`RETROSPECTIVE_CREDIT_ORDER_DEPENDENT / TELESCOPING_CORE_SURVIVES / SUBMODULARITY_AND_INTRINSIC_SCALAR_KILLED / NOT_CANONICAL`

若主要 rooted 到 prior art：

`RETROSPECTIVE_CREDIT_PRIOR_ART_ROOTED / PROJECT_SPECIFIC_BRC_INTERFACE_RETAINED / NO_NEW_FOUNDATION_PRIMITIVE / NOT_CANONICAL`

若核心 precision-debt 本身被反例推翻：

`R022_PRECISION_DEBT_BREAK_FOUND / MINIMAL_COUNTEREXAMPLE_VERIFIED / RETURN_TO_R022 / NOT_CANONICAL`

若 credit interpretation 与 canonical BRC 冲突但 theorem 不错：

`CREDIT_INTERPRETATION_NARROWED / R023_THEOREMS_STABLE / NO_SEMANTIC_REPAIR / NOT_CANONICAL`

---

## 39. Git / CI boundary

任务类型：research。

- 使用独立 research branch；
- 稀疏 checkpoint；
- Draft PR 作为研究 artifact；
- `CI_NOT_REQUIRED_FOR_RESEARCH`；
- 不轮询 repository CI；
- focused exact tests + py_compile 必须本地 PASS；
- 若后续 Driver 选择 formalization，再单独开 Lean/root gate。

不要在本任务中为了状态绿而修改 workflow/common surface。

---

## 40. 最终必须回答的九个问题

1. “后验 distinction credit”能否定义成数学上稳定的对象，还是只能作为多维 profile？
2. `M/B` precision debt 的 marginal credit 是否天然 order-dependent？最小反例是什么？
3. debt reduction 是否 submodular？是否 supermodular？各自最小反例是什么？
4. pair coverage 与 precision-debt reduction 的关系是什么？
5. realized-path credit 与 declared-future credit 的精确差距是什么？
6. future language 缩小时，什么意义下 credit 被释放？
7. “区别 credit=0”在什么 carrier 上恰好等价于安全 recoalescence？
8. side metadata、feature acquisition、checkpoint rewind 如何共同支付 future precision debt？
9. 这套 calculus 对 BRC runtime 真正能提供什么决策规则，哪些只是经典 attribution/set-cover 的重新包装？

任务完成后一次性回 Driver。