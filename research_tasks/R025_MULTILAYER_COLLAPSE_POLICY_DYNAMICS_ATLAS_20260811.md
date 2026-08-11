<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R025-MULTILAYER-COLLAPSE-POLICY-DYNAMICS-ATLAS",
  "title": "R025 Multi-Layer Collapse Policy Dynamics and Precision-Exponent Phase Atlas",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH_DISCOVERY_AND_DATA",
  "frontier": "Build an exact multi-layer collapse laboratory that compares always-down, always-up, nearest, farthest, reproducible pseudorandom, unbiased stochastic, alternating and all-endpoint/BRC policies under precision lifts and exponent schedules; collect trajectory data and extract exact or falsifiable laws for policy divergence, precision scaling, exponent growth, order effects and recoalescence.",
  "next_action": "Implement the exact integer/rational experiment engine and schema, run exhaustive small-domain and broad parameter sweeps, test the frozen candidate laws and their minimal counterexamples, then return a precision-exponent-policy phase atlas plus the strongest surviving theorem candidates.",
  "dependencies": [
    {
      "target": "EnterpriseMath/Arithmetic/IntegerRoot.lean",
      "action": "CONSUME_EXACT_PTH_POWER_BASIN_CHARACTERIZATION",
      "satisfied": true
    },
    {
      "target": "R021 accepted branching-collapse calculus",
      "action": "CONSUME_BOOLEAN_SUPPORT_AND_NO_RESURRECTION_BOUNDARY_FOR_ALL_ENDPOINTS_BASELINE",
      "satisfied": true
    },
    {
      "target": "R023/R023I BRC semantic core",
      "action": "CONSUME_EXACT_SUPPORT_RECOALESCENCE_SEMANTICS_WITHOUT_REOPENING_THEOREMS",
      "satisfied": true
    },
    {
      "target": "P003/P019 collapse-word commutation and stabilization family",
      "action": "USE_AS_REFERENCE_FOR_MIXED_EXPONENT_ORDER_EFFECTS",
      "satisfied": true
    }
  ],
  "source_refs": [
    "EnterpriseMath/Arithmetic/IntegerRoot.lean at source main@0a0af206326a873f28620426371f894ccc92db51",
    "R021 Draft PR #496 / accepted Branch-Recoalescence Collapse calculus",
    "R023 Draft PR #498 and R023I shared-surface replay lineage",
    "R024 Collapse Atlas taskbook as optional runtime acceleration only, not a semantic dependency",
    "R014 representation/resource methodology for honest data and state accounting"
  ],
  "evidence_status": "MULTILAYER_COLLAPSE_EMPIRICAL_LAW_DISCOVERY_GATE",
  "last_progress_ref": "User requested systematic data collection across directional/random collapse policies, precision growth and exponent growth",
  "last_progress_at": "2026-08-11T21:09:00+08:00",
  "hard_block": null,
  "tags": [
    "R025",
    "collapse-policy",
    "multilayer",
    "precision-tower",
    "p-th-power",
    "nearest",
    "farthest",
    "pseudorandom",
    "stochastic-rounding",
    "phase-atlas",
    "BRC",
    "data-mining",
    "scaling-law"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R025",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R025 — Multi-Layer Collapse Policy Dynamics and Precision-Exponent Phase Atlas

Status: `READY / P0 / EMPIRICAL-LAW DISCOVERY / EXACT INTEGER MODEL / NOT CANONICAL`

## 1. 母问题

建立一个可重复、可穷举、可扩展的**多层坍缩动力学实验台**，系统回答：

> 对同一个初态、同一个精度层级与次方序列，如果每一层都采用不同的坍缩选择政策——全部向下、全部向上、全部就近、全部就远、伪随机、按距离无偏随机、交替选择、或者同时保留全部端点世界——长期结果会出现什么系统性差异？这些差异怎样随精度提高、次方提高、次方顺序改变而变化？

本任务的第一目标是**采数据找规律**，但数据必须建立在 exact integer/rational semantics 上，不能让浮点误差制造假规律。

最终必须交付一张真正可查询的：

**Collapse Policy Dynamics Atlas / 坍缩策略动力学图谱**。

它至少要告诉我们：

- 哪些政策产生单调漂移；
- 哪些政策局部有偏/无偏；
- 不同政策的最大可能分歧是多少；
- 精度提高时分歧按什么速率收缩或不收缩；
- 次方提高时 basin/gap、漂移、随机方差和策略敏感性如何变化；
- 多个不同次方按不同顺序执行时是否出现 order defect；
- 多世界支持何时真正分叉、何时重新汇合；
- 哪些经验规律能升级成 exact theorem candidate，哪些只是有限区间现象。

---

## 2. 为什么不能只重复同一个 collapse

Enterprise Math 已有下坍缩

`C_p(n) = floorRoot_p(n)^p`。

同一指数 `p` 连续重复时，第一次以后会因为 perfect-power fixed point 很快变成平凡轨迹。

因此本任务的多层模型必须至少包含一种使下一层重新产生非平凡 basin 的机制：

1. **precision lift / 精度提升**；
2. **改变 exponent**；
3. 可选的显式 arithmetic operation。

主实验以 precision lift 为核心，使“精度增加对规律的影响”直接成为动力学的一部分，而不是事后换一个网格再比较。

---

## 3. 精确基本模型

### 3.1 p-th-power bracket

对 `p >= 2` 和 `n in N_0`，令

`k = floorRoot_p(n)`，

`L_p(n) = k^p`。

定义 upper endpoint：

- 若 `n = k^p`，则 `U_p(n)=n`；
- 否则 `U_p(n)=(k+1)^p`。

于是非 exact state 位于唯一开区间：

`L < n < U`。

记录：

`G = U-L`  （basin gap），

`d = n-L`  （lower offset），

`u = U-n = G-d`  （upper offset）。

非 exact state 的 phase 只以 exact rational 保存：

`phi = d/G`。

禁止以 binary float 作为 theorem-critical phase。

### 3.2 precision state

每层有一个正整数 precision scale `M_t`。

坐标 `n_t` 表示 normalized physical value

`x_t = n_t / M_t`。

精度提升使用整数 refinement ratio `r_t >= 1`：

`M_(t+1) = r_t * M_t`。

一个已坍缩坐标 `y_t` 被精确搬到下一精度层：

`s_(t+1) = r_t * y_t`。

因此纯 precision lift 不改变其 normalized physical value：

`s_(t+1)/M_(t+1) = y_t/M_t`。

但 `r_t*y_t` 未必仍是下一个 exponent 的 perfect power，因此下一层可以重新产生非平凡坍缩。

### 3.3 optional operation layer

每层允许一个显式操作 `A_t`：

`a_t = A_t(s_t)`，

然后才执行 collapse selector。

主基线强制：

`A_t = identity`。

只有主规律稳定后，才加入 operation-perturbed suite，例如：

- exact physical translation；
- integer multiplication；
- 已证明合法的 declared operation。

跨精度比较时，translation 必须按 `M_t` 正确换算，不能让“单位改变”伪装成精度效应。

### 3.4 layer recurrence

给定 policy `pi_t` 与 exponent `p_t`：

`y_t = S_(pi_t,p_t)(a_t)`。

若还有下一层：

`s_(t+1) = r_t*y_t`。

每条 trajectory 的可观测输出至少包含：

`(s_t, a_t, y_t, M_t, p_t, r_t, L, U, G, d, u, policy_choice)`。

---

## 4. 必须实现的 collapse policies

所有 policy 在 exact perfect power 上必须返回原状态。

### P0 — ALWAYS_DOWN

`S_DOWN(n)=L`。

### P1 — ALWAYS_UP

`S_UP(n)=U`。

### P2 — NEAREST

选择距离 `n` 最近的 endpoint。

若 `d<u`：选 `L`；
若 `d>u`：选 `U`；
若 `d=u`：默认选 `L`。

另保留一个 explicit tie-up variant 仅用于边界测试，不混入默认数据。

### P3 — FARTHEST

选择距离 `n` 最远的 endpoint。

默认 tie 时选 `U`，使其与默认 NEAREST 在 midpoint 上也保持互补端点。

### P4 — PRNG_50_50

每个非 exact layer 用可复现 counter-based pseudorandom source 选择 `L/U`，目标概率 `1/2`。

随机性必须由：

`(seed, trajectory_id, layer_id)`

或另一明确 frozen scheme 决定。

不要使用全局隐式 RNG state。

### P5 — STOCHASTIC_UNBIASED

定义理想选择概率：

`P(U) = d/G`，

`P(L) = u/G`。

这样单步条件期望候选为：

`E[S(n) | n] = n`。

实现时需要 exact discrete sampling 或等价的可审计方法；若使用有限 bit source，必须记录任何 modulo bias，不能把近似均匀冒充 exact theorem evidence。

### P6 — ALTERNATING

按层号交替 `DOWN/UP`，并至少测试：

- DOWN-first；
- UP-first。

### P7 — PHASE_THRESHOLD(alpha)

对 rational `alpha in [0,1]`：

`phi < alpha -> L`，否则 `U`，

并明确 equality tie rule。

扫 `alpha`，寻找 policy family 的相变边界。

### P8 — ALL_ENDPOINTS / BRC ENVELOPE

非 exact state 同时保留 `{L,U}`；exact state 保留 `{n}`。

逐层做 exact set-valued execution，并在字面状态相同或已有安全 certificate 时 recoalesce。

此政策不是“平均值”，而是所有 endpoint-selector trajectory 的 exact support baseline。

---

## 5. R025-T01 — 实验引擎与 exact dataset schema

建议实现：

`experiments/r025_multilayer_collapse_atlas.py`

以及独立测试文件。

每一行 layer-level 数据至少包含：

- `trajectory_id`；
- `initial_value_num/den`；
- `initial_precision`；
- `layer`；
- `precision_M`；
- `refinement_ratio_r`；
- `exponent_p`；
- `operation_id`；
- `policy_id`；
- `seed`；
- `pre_operation_state`；
- `pre_collapse_state`；
- `root_index_k`；
- `lower_L`；
- `upper_U`；
- `gap_G`；
- `lower_offset_d`；
- `upper_offset_u`；
- `phase_num/phase_den`；
- `selected_endpoint`；
- `post_collapse_state`；
- `signed_coordinate_error`；
- `absolute_coordinate_error`；
- `signed_physical_error_num/den`；
- `exact_power_before_collapse`；
- `branch_count_before/after` for ALL_ENDPOINTS；
- `recoalescence_count`；
- `state_bit_length`。

同时建立 trajectory summary：

- final normalized value；
- total signed physical drift；
- cumulative absolute physical displacement caused only by collapse；
- maximum excursion from initial value；
- ambiguous-layer count；
- exact-hit count；
- number of distinct terminal states；
- pairwise policy separation；
- all-endpoints support width/cardinality；
- branch creation and recoalescence counts；
- random ensemble mean/variance when applicable。

原始整数/有理数据必须可重新计算全部 summary。

---

## 6. R025-T02 — 小域穷举基准

先建立一个可以穷尽的 reference box。

最低建议覆盖：

- `n_0 = 0..500`；
- constant `p = 2..6`；
- `r = 1..12`；
- depth `1..8`；
- DOWN / UP / NEAREST / FARTHEST / ALTERNATING / ALL_ENDPOINTS；
- 多个 `PHASE_THRESHOLD(alpha)`；
- pseudorandom 另做 seed ensemble。

该小域用于：

- 找最小反例；
- 验证 proposed invariants；
- 检查 off-by-one/tie behavior；
- 独立实现交叉验证。

不要因为大规模 Monte Carlo 很漂亮而跳过小域 exhaustiveness。

---

## 7. R025-T03 — Policy Envelope 候选规律

对相同初态、相同 operation/exponent/precision schedule，测试并尝试证明：

`ALL_DOWN_t <= ANY_ENDPOINT_POLICY_t <= ALL_UP_t`

在每一层的 coordinate/normalized physical value 上是否始终成立。

这里 `ANY_ENDPOINT_POLICY` 包括任意逐层选择 `L/U` 的 deterministic word，也包括单条 pseudorandom realized path。

若成立，进一步验证：

`ALL_ENDPOINTS support subseteq [DOWN_extreme, UP_extreme]`

以及 extrema 是否真的由 all-down / all-up 达到。

输出：

- exact theorem candidate；
- 最弱假设；
- operation layer 加入后何时失效；
- signed/negative extension 是否需要单独处理。

若任何部分错误，返回最小反例。

---

## 8. R025-T04 — 单调性与累计漂移

在 identity-operation、positive precision lift 下检查：

- ALWAYS_DOWN 的 normalized physical trajectory 是否单调不增；
- ALWAYS_UP 是否单调不减；
- NEAREST/FARTHEST 是否可能多次换方向；
- alternating/random 是否出现系统漂移。

对 DOWN/UP 给出 cumulative error decomposition：

`x_(t+1)-x_t`

完全由本层 collapse error 除以 precision 产生。

寻找 exact telescoping identity 和可计算上下界。

---

## 9. R025-T05 — NEAREST / FARTHEST 互补律

对同一个非 exact input，验证并尝试证明：

- 默认 tie convention 下 NEAREST 与 FARTHEST 选择相反端点；
- `abs(error_near) + abs(error_far) = G`；
- `output_near + output_far = L+U`。

然后研究：

> 这种单步互补在多层反馈后保留什么，丢失什么？

采集：

- 同源 near/far trajectory 的 separation；
- 首次达到最大 envelope 的层；
- 是否存在 later recoalescence；
- precision/exponent 对 separation growth 的影响。

---

## 10. R025-T06 — precision scaling 与 p-power-free refinement kernel

这是本任务最高优先级之一。

### 10.1 perfect-power covariance

对几何 deterministic policies DOWN/UP/NEAREST/FARTHEST，测试并证明/杀死：

`S_p(a^p*n) = a^p*S_p(n)`。

必须包含 midpoint/tie case。

### 10.2 constant-p exact-aligned refinement

如果 exponent 恒定为 `p`，且每个 refinement ratio

`r_t = a_t^p`，

则第一次 collapse 后，precision lift 是否永远把状态送到另一个 exact p-th power，从而后续 collapse 都成为 no-op？

若成立，写成显式 theorem candidate：

**p-power-aligned precision refinement is dynamically invisible after the first collapse**

（normalized physical value 意义下）。

### 10.3 p-power-free precision kernel

把 refinement ratio 唯一分解为：

`r = a^p * d`，

其中 `d` 不含非平凡 p-th-power divisor。

测试几何政策下 normalized next-layer dynamics 是否只依赖 `d` 而与 `a` 无关。

目标公式形态：

`S_p(r*k^p)/(r*M) = S_p(d*k^p)/(d*M)`。

若成立，`d` 就是 precision lift 对 constant-p collapse 的一个极强压缩坐标。

必须说明它对哪些政策成立：

- deterministic geometry policies；
- ideal stochastic distribution；
- state-dependent pseudorandom realization。

不要强迫 PRNG trajectory 继承不存在的 scale covariance。

---

## 11. R025-T07 — 精度增加的收敛速率

固定 physical rational `x>0` 和 exponent `p`，用多组 increasingly fine `M` 比较包含 `x` 的 p-th-power basin physical width：

`W_p(M,x) = ((k+1)^p-k^p)/M`，

其中 `k=floorRoot_p(M*x)`，且选择的 `M` 使坐标 exact integral。

数据上检验：

`W_p(M,x) ~ p*x^((p-1)/p)*M^(-1/p)`。

但最终报告不能只给 regression。

必须寻找 exact finite bounds，例如由 binomial expansion 得到：

`p*k^(p-1) <= (k+1)^p-k^p <= p*(k+1)^(p-1)`

或更精确的整数界，并把 `k^p <= Mx < (k+1)^p` 合入物理尺度。

输出每个 `p` 的：

- log-log empirical slope；
- exact upper/lower envelope；
- crossover region；
- finite-size deviation。

重点验证一个直觉：

> **p 越大，precision 增长带来的 physical gap 收缩指数 `1/p` 越小，因此单纯提高精度可能越来越“慢”。**

这只是待验 hypothesis，不能预先写成项目事实。

---

## 12. R025-T08 — 次方增加与 exponent phase transitions

固定 coordinate `n` 或固定 physical `(x,M)`，扫 `p`。

记录：

- root index `k_p`；
- basin gap `G_p`；
- phase `phi_p`；
- DOWN/UP spread；
- nearest/farthest error；
- stochastic variance；
- exact-hit status。

必须显式处理高次方稀疏区：

对 `1<n<2^p`，root index 落入 `k=1` basin。

寻找 exponent threshold：

`p ~ log_2(n)`

附近是否出现策略敏感性突变。

更一般地，研究 `k_p` 的 exponent plateaus：

`k^p <= n < (k+1)^p`。

构建：

**Exponent Phase Atlas**

按 `(n,p)` 或 `(Mx,p)` 标记 root-index plateau、gap、policy spread 和 random variance。

---

## 13. R025-T09 — 普通伪随机与真正无偏随机的区别

这是必须单独比较的一组。

### 13.1 50/50 random

固定 input 时：

`E[S_50(n)] = (L+U)/2`。

因此 expected local drift 候选为：

`G/2-d`。

验证：50/50 endpoint random 只有在 midpoint 附近才局部无偏，而不是天然“公平”。

### 13.2 distance-weighted stochastic collapse

对 ideal law

`P(U)=d/G`，`P(L)=u/G`，

验证/证明：

`E[S(n)|n]=n`，

`Var(S(n)|n)=d*u`。

在 pure precision-lift tower 中，进一步研究 normalized physical trajectory 是否构成 martingale：

`E[x_(t+1) | history_t] = x_t`。

同时采集方差累积、tail distribution 与 precision/p 的关系。

如果成立，这可能成为“随机坍缩”里一个比 50/50 更自然的基准政策。

### 13.3 pseudorandom realization vs probability law

必须区分：

- 单个 seed 的 deterministic trajectory；
- 多 seed empirical ensemble；
- ideal stochastic theorem。

不能从单一 seed 轨迹推导概率定理。

---

## 14. R025-T10 — mixed exponent words 与次方顺序

构造 exponent words：

- constant `p`；
- increasing `2,3,4,...`；
- decreasing；
- alternating `(p,q,p,q,...)`；
- 同一 multiset 的不同 permutations；
- divisibility-comparable pairs，例如 `(2,4)`、`(3,6)`；
- incomparable pairs，例如 `(2,3)`、`(4,6)`。

对 DOWN 先与已有 collapse-word/commutation/stabilization 结果交叉检查，避免把已知规律当新发现。

然后重点测：

- UP 是否有对应但不同的 order law；
- NEAREST/FARTHEST 的 order defect；
- stochastic law 对 exponent order 的敏感性；
- 同一 exponent multiset 是否可能产生不同 terminal distribution；
- precision refinement 是否放大或压低 order defect。

定义至少一个 exact order-defect observable，例如：

`D_word = y_(p then q) - y_(q then p)`

以及 normalized physical version。

寻找最小非零 witness 和 defect 的界。

---

## 15. R025-T11 — ALL_ENDPOINTS / 多世界轨迹

把每个 ambiguous collapse 看成两个合法 endpoint worlds。

从 singleton support 开始，逐层 exact 传播所有 endpoints。

记录：

- live support cardinality；
- cumulative branch creation；
- duplicate endpoint collisions；
- exact recoalescence count；
- terminal support width；
- deterministic policy terminal states 在 support 中的位置；
- extreme values 是否恰由 all-down/all-up 达到。

重点寻找：

1. branch count 是否真的指数增长，还是大量世界会自动汇合；
2. precision 增加会让 recoalescence 更少还是更多；
3. exponent 增大是否导致 support 更稀疏、更宽或更快汇合；
4. mixed exponent 是否制造特别强的 branch funnel；
5. support cardinality 与 interval width 是否可以由更小 symbolic token 描述。

遵守 `NO_RESURRECTION`：ALL_ENDPOINTS 表示所有合法 endpoint alternatives 的 support，不表示已经丢失的某个原始 fine point。

---

## 16. R025-T12 — operation-perturbed robustness suite

只有在 identity baseline 完成后运行。

加入少量明确操作，例如：

- physical `+c` translations；
- integer scaling；
- 可证明 unit-consistent 的操作词。

问：

> 前面发现的 envelope、monotonicity、p-power-free precision kernel、martingale 或 scaling law，哪些依赖 identity dynamics，哪些在合法 operation family 下仍成立？

每个被 operation 打破的规律都要返回最小 counterexample 和失效原因。

不要为了“规律更漂亮”而限制掉真实反例。

---

## 17. R025-T13 — 数据采样矩阵

### Layer A — exact exhaustive

小 `n,p,r,depth` 全穷举，用于 theorem/counterexample discovery。

### Layer B — boundary-focused

大量采样：

- `L+1`；
- `U-1`；
- midpoint 附近；
- perfect powers；
- exponent plateau 切换点；
- precision-aligned / misaligned ratios。

### Layer C — broad deterministic

建议至少覆盖：

- `p=2..16`，并追加部分 `p=17..32` 高次方探针；
- depth `8,16,32,64`；
- `r` 包含 `2,3,4,5,8,9,10,16` 以及按 `p` 动态生成的 perfect-pth-power 和 non-pth-power ratios；
- 初始坐标从小整数、稀疏大整数与 fixed physical rational families 中抽取。

### Layer D — stochastic ensemble

对 PRNG_50_50 与 STOCHASTIC_UNBIASED：

- 多 seed；
- 报告 sample count；
- 置信区间仅作为统计描述；
- exact expectation/variance 若有代数证明必须与 empirical estimate 分开标记。

### Layer E — cross-precision replication

选择 fixed rational physical values `x=a/b`。

只用能让 `M*x` 为整数的 precision scales，确保不同精度实验对应同一个 exact physical target。

---

## 18. R025-T14 — Law Mining / 规律挖掘协议

不要直接把大表喂给黑箱模型然后接受相关性。

优先按以下可解释结构分组：

1. `phase phi=d/G`；
2. root index `k`；
3. exponent `p`；
4. precision `M`；
5. refinement ratio `r`；
6. `p`-power-free part of `r`；
7. exponent divisibility class；
8. boundary distance；
9. policy family；
10. support width / branch count。

对每个 candidate law 执行：

`pattern -> exact normalization -> integer/rational formula guess -> exhaustive small-domain attack -> targeted large-domain attack -> theorem candidate or killed hypothesis`。

优先寻找：

- exact equality；
- divisibility law；
- monotonicity；
- finite-difference law；
- scale covariance；
- asymptotic power law with exact finite bounds；
- threshold/phase transition；
- invariant distribution or martingale law；
- branch/recoalescence combinatorics。

每个规律必须有唯一 ID，例如：

`R025-LAW-001`。

状态只能是：

- `EXACT_PROVED_OR_DERIVED`；
- `EXHAUSTIVE_FINITE_CONFIRMED`；
- `STATISTICALLY_SUPPORTED`；
- `CONJECTURAL`；
- `KILLED_WITH_COUNTEREXAMPLE`。

---

## 19. Frozen candidate laws to attack, not assume

至少逐条测试以下初始假说：

### H1 — Extremal Envelope

all-down / all-up 是全部 endpoint-selector trajectories 的逐层下/上包络。

### H2 — Physical Monotonicity

pure precision tower 中 all-down normalized trajectory 不增，all-up 不减。

### H3 — Near/Far Complement

同一 basin 内 nearest/farthest 的 absolute error 之和等于 gap。

### H4 — p-Power Covariance

几何 endpoint policy 满足 `S_p(a^p n)=a^p S_p(n)`。

### H5 — Aligned Precision Freeze

constant `p` + perfect-pth-power refinement ratio 时，第一次 collapse 后再无新的 collapse motion。

### H6 — Precision Kernel Reduction

constant `p` 时 normalized geometric dynamics 只依赖 refinement ratio 的 p-power-free part。

### H7 — Precision Scaling

fixed physical `x,p` 下 basin physical width 的主尺度是 `M^(-1/p)`。

### H8 — Exponent Sparsification

`p` 增大导致 p-th-power anchors 稀疏，并在 `2^p` 相对 state scale 附近产生明显 policy-sensitivity transition。

### H9 — 50/50 Is Not Locally Unbiased

uniform endpoint random 的 expected drift 等于 basin midpoint minus current state。

### H10 — Distance-Weighted Martingale

无偏 stochastic selector 在 pure precision tower 中保持 normalized value 的条件期望。

### H11 — Stochastic Variance Law

单步 exact variance 为 `d*(G-d)`，physical variance 按 `M^-2` 缩放，再通过 `G(M,p)` 获得整体 precision/exponent scaling。

### H12 — Order Defect Phase

mixed exponent word 的 order sensitivity 与 exponent divisibility/comparability 存在明显分区，但 nearest/farthest/random 可能比 lower-collapse 产生更丰富的非交换现象。

### H13 — Recoalescence Funnel

ALL_ENDPOINTS 的 branch count 在某些 precision/exponent regimes 远低于 naive `2^depth`，并可由 gap/root/phase 信息预测。

任何一条被杀死都算有效成果。

---

## 20. 可视化与 Phase Atlas

至少生成以下二维/三维数据视图；图像只是辅助，raw exact data 才是来源：

1. `(precision, exponent) -> physical basin width`；
2. `(precision, exponent) -> UP-DOWN terminal spread`；
3. `(phase, exponent) -> nearest/farthest local error`；
4. `(precision, exponent) -> stochastic variance`；
5. `(refinement p-power-free kernel, exponent) -> normalized dynamics class`；
6. `(word order, exponent pair) -> order defect`；
7. `(depth, exponent, precision schedule) -> ALL_ENDPOINTS branch cardinality`；
8. `(depth, exponent, precision schedule) -> recoalescence ratio`。

如果发现清晰相界，返回 exact threshold candidate，不要只画热力图。

---

## 21. 资源与性能记录

本任务的主要目标是规律，不是跑分快，但数据规模必须可控。

记录：

- experiment count；
- layer-row count；
- maximum integer bit length；
- runtime；
- peak memory estimate；
- ALL_ENDPOINTS maximum live support；
- random ensemble size。

若 R024 Collapse Atlas runtime 已经可用，可作为 acceleration backend；但结果必须与 direct exact root baseline 抽样交叉验证。

R025 不得因为 acceleration backend 不可用而改变数学模型。

---

## 22. Required artifacts

最低交付：

1. `docs/R025_MULTILAYER_COLLAPSE_POLICY_DYNAMICS_REPORT.md`；
2. `experiments/r025_multilayer_collapse_atlas.py`；
3. focused test file；
4. raw/sample dataset（CSV/JSONL 或等价可审计格式）；
5. machine summary JSON；
6. `R025_LAW_MATRIX.md`；
7. `R025_PRECISION_EXPONENT_PHASE_ATLAS.md`；
8. policy comparison table；
9. precision scaling table；
10. exponent phase-transition table；
11. random-vs-unbiased stochastic comparison；
12. ALL_ENDPOINTS branch/recoalescence table；
13. 最小反例集合；
14. top theorem candidates with exact assumptions；
15. 下一步建议：formalize / continue data / connect to R024 / connect to BRC / kill route。

若数据量大，不要把整个巨大 dataset 塞进 prose；保留 machine-readable artifact，并在报告中给摘要、hash/row count 和复现实验参数。

---

## 23. Success / kill criteria

成功不要求“发现一个惊人的统一公式”。

以下任一组合均可成功：

- 至少 3 条跨大范围、经反例攻击后仍存活的 exact/scaling laws；
- 找到精度与次方之间一个稳定 phase boundary；
- 找到 random policy 的系统偏差和一个更自然的无偏替代；
- 找到 ALL_ENDPOINTS branch/recoalescence 的可预测 regime；
- 找到 mixed exponent order 的新最小 counterexample/classification；
- 证明若干最直观猜想其实错误，并给出清晰负边界。

必须杀死或降级任何仅由：

- 小样本；
- float rounding；
- 单一 seed；
- 单一初值；
- 未收费的 branch state；
- 把 coordinate scale 改变误当 physical precision effect；
- 把 one-step relation 偷升格为 multi-layer theorem

产生的假规律。

---

## 24. Return classes

优先正向：

`MULTILAYER_COLLAPSE_LAWS_FOUND / PRECISION_EXPONENT_PHASE_ATLAS_FROZEN / POLICY_DIFFERENCES_CLASSIFIED / DATASET_CHECKED / NOT_CANONICAL`

如果随机部分特别强：

`UNBIASED_STOCHASTIC_COLLAPSE_LAW_FOUND / RANDOM_BIAS_CLASSIFIED / PRECISION_VARIANCE_SCALING_FOUND / NOT_CANONICAL`

如果 BRC 支持规律特别强：

`ALL_ENDPOINTS_RECOALESCENCE_REGIME_FOUND / BRANCH_GROWTH_CLASSIFIED / BRC_DATA_TOOL_CANDIDATE / NOT_CANONICAL`

如果规律主要来自已知基础：

`ROOTING_SUCCESS / KNOWN_COLLAPSE_LAWS_EXPLAIN_DATA / NEW_PHASE_ATLAS_ONLY / NOT_CANONICAL`

如果没有稳定规律：

`NO_STABLE_CROSS_SCALE_LAW / PARAMETER_SENSITIVITY_DOMINATES / NEGATIVE_ATLAS_FROZEN / NOT_CANONICAL`

---

## 25. 最终必须回答的 8 个问题

最终报告首页必须直接回答：

1. 全部向下与全部向上的长期差距是什么？
2. 就近与就远是否存在 exact 对偶/互补结构？
3. 50/50 伪随机到底有没有系统偏差？
4. 距离加权随机是否给出真正的无偏多层坍缩？
5. precision 增加一倍/十倍时，误差与 policy spread 大约按什么规律变化？
6. exponent 从 `p` 增大到 `p+1` 时，哪些指标单调，哪些存在跳变？
7. mixed exponent 顺序是否产生可预测的 order defect？
8. ALL_ENDPOINTS 多世界轨迹到底是指数爆炸，还是会在某些 regime 大量 recoalesce？

不要用“看起来”“大概”结束；每个答案必须给 evidence status。