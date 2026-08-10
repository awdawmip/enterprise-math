<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R008-P016-ESCAPE-PROOF-PHYSICAL-KILL-TESTS",
  "title": "R008 P016 Escape-Proof Physical Kill Tests",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Turn Enterprise Math's broad finite-resolution/fundamental-many-to-one physical hypothesis into a small set of escape-proof quantitative P016 specializations, rank which real experiments genuinely constrain them, and prove negative boundaries showing why discreteness or collapse alone does not imply Lorentz violation, hard interferometric dead zones, universal Landauer heating, or control failure.",
  "next_action": "Consume P016 and its prior-art appendix; first classify the proposed LIGO, matter-wave, heating/radiation, atomic-clock/GPS, semiconductor, and control-system attacks into direct kill tests, parameter bounds, or non-tests. Then build at least three explicit M=(X,T,Pi,S,Q,theta) specializations with frozen parameters and predeclared falsified_if conditions, while proving the strongest possible no-go statements and recording counterexamples to overbroad claims.",
  "dependencies": [
    {"target": "P016 physical falsification contract", "action": "CONSUME", "satisfied": true},
    {"target": "P012/P016 canonical prior-art boundary", "action": "CONSUME", "satisfied": true}
  ],
  "source_refs": [
    "research_tasks/R008_P016_ESCAPE_PROOF_PHYSICAL_KILL_TESTS_20260810.md",
    "README.zh-CN.md",
    "docs/P016_PHYSICAL_FALSIFICATION_CONTRACT.zh-CN.md",
    "docs/PRIOR_ART_P012_P016.zh-CN.md"
  ],
  "evidence_status": "INDEPENDENT_PHYSICAL_STRESS_TEST_CANDIDATE",
  "last_progress_ref": "independent audit supplied by user",
  "last_progress_at": "2026-08-10T14:57:00+08:00",
  "hard_block": null,
  "tags": ["R008", "P016", "physics", "falsification", "LIGO", "interferometry", "collapse", "heating", "Lorentz", "unitarity", "kill-test"],
  "claim_lease_minutes": 1440,
  "context_policy": {
    "mode": "TASK_ISOLATED",
    "memory_policy": "UNTRUSTED_HINT_ONLY",
    "cross_task_import_policy": "EXPLICIT_ONLY"
  }
}
-->

# R008 — P016 无逃逸物理 Kill-Test 与理论级 No-Go 压力测试

Status: `CANDIDATE RESEARCH HANDOFF / P016 PRESSURE TEST / NOT CANONICAL`

## 0. 立项原因

一份独立审核提出：与其继续攻击已经证明/Lean 检查的整数定理，更应攻击 Enterprise Math 从“有限分辨率、离散状态、基本 many-to-one collapse”走向自然物理时必须承担的实验后果。

这个方向是正确的，但原审核中的若干推断过强：

- LIGO 测到极小 differential strain，不自动推出“任何空间离散都被排除”；
- 量子大质量干涉能强约束会导致相干损失的具体 collapse 动力学，但不直接约束所有 many-to-one 数学模型；
- GPS/原子钟只能约束会产生特定时钟量化、优选方向、色散或不可平均漂移的模型；
- 半导体和控制系统中连续方程成功并不能逻辑证明底层连续；
- Landauer 原理不能未经模型推导就被当成“每一次 fundamental collapse 必须产生 kT ln2 热量”的普适定律；
- “任何离散/坍缩理论都不可能同时保持 Lorentz 对称”这类总 no-go 过宽，已有 causal-set 与 relativistic-collapse 前人路线本身就是反例边界。

本任务的目标不是替 Enterprise Math 找借口，而是把这些“逃逸口”全部提前形式化：只有把模型参数、状态、动力学和 observable 冻结以后，实验才有资格真正杀死它。

方向可以激进，证据必须残酷。

---

# 1. 唯一 canonical 起点：P016 contract

直接消费 P016，不重做协议层。

任何具体物理实现必须写成

\[
\mathcal M=(X,T,\Pi,\mathcal S,\mathcal Q,\theta),
\]

其中：

- `X`：物理状态空间；
- `T`：基本前向转移律/转移族；
- `Pi`：观测映射；
- `S`：精确或涌现对称；
- `Q`：声称严格守恒量；
- `theta`：有限参数。

每个模型在看实验结果之前必须给出：

1. 参数允许区；
2. 至少一个不可回避 observable；
3. `falsified_if` 条件；
4. 允许/不允许的参数逃逸方式；
5. 哪些 null result 只是参数排除，哪些足以排除整个 specialization。

任何“看到实验后再把作用变量改掉、把尺度调到实验之外、把耦合设成零”的做法必须登记为 post-hoc escape，而不能算理论通过实验。

---

# 2. 第一阶段：把六类工程攻击重新评级

对以下六类必须逐项给出：`DIRECT_KILL_TEST / PARAMETER_BOUND / WEAK_PRESSURE / NOT_A_TEST`，并说明最低缺失假设。

## 2.1 LIGO / 激光干涉

必须严格区分至少两条不同路线。

### A. hard-resolution/dead-zone model

如果模型声称长度 observable 本身存在硬最小增量 `delta_x`，并推出：

\[
|\Delta L|<\delta_x
\Rightarrow
\Pi(L+\Delta L)=\Pi(L),
\]

那么干涉仪可以直接给 `delta_x` 上界。

但必须证明实验读出的 phase/strain 与模型里的 primitive length observable 是同一个量，不能把“仪器能够估计 10^{-18}m 级 differential displacement”直接偷换成“时空格点间距必小于 10^{-18}m”。

### B. collapse/noise model

如果 fundamental collapse 对 test-mass motion、phase 或 force spectrum 注入额外噪声，则 LIGO/LISA Pathfinder/AURIGA 类测量可以像 CSL bounds 一样约束参数。

这条路线和“空间离散”是不同 kill test，不得混在一起。

第一阶段需要建立 LIGO-compatible observable compiler：

\[
\theta\mapsto S_h(f;\theta)
\quad\text{或}\quad
\theta\mapsto \Delta L_{\rm min}(\theta).
\]

如果无法推出其中之一，则 LIGO 不是当前模型的直接反证。

## 2.2 大质量 matter-wave interference

这是优先级最高的真实 collapse test 之一。

若模型对量子叠加给出不可避免 coherence factor

\[
\eta(m,\Delta x,t;\theta)<1,
\]

则实验 fringe visibility 直接约束 `theta`。

必须以已有大分子 matter-wave 实验与 collapse-model parameter-exclusion 方法为 prior art，禁止把“质量越大应该越 collapse”当无公式的直觉。

优先目标：构造一个最小 Enterprise Math physical specialization，使 primitive many-to-one transition 导出可计算的 `eta`；然后判断现有干涉结果排除了整个 specialization 还是只排除参数区域。

## 2.3 自发加热 / 辐射

这是第二条高价值 kill route。

若 `T` 非幺正/随机 collapse 必然产生

\[
P_{\rm collapse}(\theta)>0
\]

或

\[
\Gamma_\gamma(E;\theta)>0,
\]

则低本底、低温、X-ray 数据可直接排除参数区域。

但禁止未经推导直接写：

\[
E_{\rm collapse}\ge kT\ln2.
\]

Landauer 是关于特定 thermodynamic information-erasure setting 的成熟结果；它不是“任意 fundamental many-to-one dynamics 每步都必须付同样热代价”的自动定理。

R008 必须先从具体 `T` 推出 energy balance，再比较实验。

## 2.4 原子钟 / GPS

不能把“连续轨道传播和相对论修正工程上成功”直接变成对离散本体的反证。

只有当模型明确推出以下至少一种后果时才进入 kill test：

- clock tick quantization；
- deterministic phase slip；
- preferred-frame/sidereal modulation；
- energy-dependent propagation；
- non-averaging secular drift；
- direction-dependent navigation residual。

研究目标是给出误差传播律，而不是先假定

\[
\text{error}\sim N\Delta x.
\]

必须证明误差是线性累积、随机游走、可平均噪声还是完全抵消。

原子钟 Lorentz tests 应优先于泛泛 GPS 叙述，因为它们已经直接形成方向/频率调制上界。

## 2.5 半导体

默认评级候选：`WEAK_PRESSURE`。

连续 Maxwell/Schrödinger/Poisson 模型的工程成功不能证明 primitive ontology 连续；现代半导体本身也包含晶格、电荷量子化、能带、隧穿等离散/量子结构。

只有具体 Enterprise Math specialization 推出额外普适：

- voltage/current staircase；
- extra threshold noise；
- forbidden transition；
- nonstandard tunneling law；
- lattice-orientation signature；

并且幅度超过器件实验上界时，才升级为 kill test。

任务必须寻找一个最小 semiconductor observable；如果找不到，明确判定为 `NOT_YET_A_TEST`，不要靠“连续方程很成功”宣判。

## 2.6 工程控制系统

默认评级候选：`NOT_A_GENERIC_TEST`。

Kalman/PID/robot state estimation 的成功说明有效状态模型可用于预测和控制，但并不说明 fundamental state 必须连续可逆。

只有当一个具体 collapse 会合并两个对控制未来响应不同的物理状态，而且无法通过 P023-style repair / additional observable 区分，才构成真实控制 no-go。

若存在 future-safe sufficient coarse state，控制系统完全可以在 coarse state 上闭合运行。

因此该路线若继续，应转化成：

> **physical future-sufficiency test**，而不是“控制成功 => 本体连续”。

---

# 3. 第二阶段：两个必须先证明的负边界

这一步是为了阻止 R008 自己制造错误大 no-go。

## R008-C01 — discreteness does not imply Lorentz violation

必须注册 causal-set / Poisson-sprinkling prior art：存在离散/locally finite structures，在特定意义下不选择 preferred Lorentz frame。

因此以下命题禁止使用：

\[
\text{fundamental discreteness}\Rightarrow\text{Lorentz violation}.
\]

可研究的正确命题只能是：

> 某个具体 Enterprise Math discrete realization 是否强制可观察的 preferred direction / modified dispersion / broken covariance？

## R008-C02 — collapse does not universally imply nonrelativistic preferred frame

必须注册 relativistic GRW/flash 类前人模型作为 boundary case。它们不证明 Enterprise Math 物理可行，但足以否定：

\[
\text{fundamental collapse}\Rightarrow\text{必然无法 Lorentz-compatible}
\]

这种无条件陈述。

R008 必须寻找更窄、可证明的假设组合，而不是挑战已知反例。

---

# 4. 第三阶段：真正可证明的理论级 no-go 候选

## R008-T01 — many-to-one vs full-state unitarity

若一个 fundamental transition

\[
T:X\to X
\]

在同一个完整物理状态空间 `X` 上是严格 many-to-one，则 `T` 不可能同时是 bijective/unitary full-state evolution。

这本身是非常基础的逻辑事实，不得包装成新物理定理。

真正需要研究的是：

1. full fundamental state 上 nonunitary；
2. observable/effective quantum sector 上仍近似或严格 unitary；

两者何时能共存？

必须给出 exact commuting/factorization diagram，例如

\[
X\xrightarrow{T}X
\]

下方 observable quantum state `Y` 是否存在

\[
\Pi\circ T=U\circ\Pi
\]

且 `U` 为 unitary/bijective。

如果可以，则 fundamental information loss 对该 observable sector 完全不可见；P016 接下来必须问：它在哪个 observable 上不可见性失败？

## R008-T02 — no-escape observable exposure

尝试形式化：一个声称 fundamental many-to-one dynamics 且同时要求“物理上不同于隐藏可逆 coarse-graining”的 specialization，至少必须存在一个声明的 observable/future language，使其预测不能与某个完全可逆 latent completion 对所有实验等价。

若所有可测 `Pi` 都满足存在 reversible completion 产生完全相同的 observable process，则该 specialization 在现有 observable language 下没有证据区分 fundamental collapse 与 effective coarse-graining。

目标是给出有限状态版本的 exact identifiability/no-identifiability theorem，而不是哲学口号。

## R008-T03 — symmetry + locality + finite-branch constraints

探索最小假设组合，在这些假设下 fundamental finite-state/many-to-one dynamics 是否真的与 Lorentz covariance、locality、conservation 或 quantum predictions 发生 no-go。

必须主动寻找 countermodel。任何 broad theorem 一旦被 causal set、relativistic GRW、hidden reversible completion 或 stochastic Lorentz-covariant model 击穿，就立即收窄假设。

成功标准不是“证明不可能”本身；找到最小缺失假设同样算高价值结果。

---

# 5. 三个必须落地的 P016 specialization

第一阶段至少建立三个可运行 toy specialization，每个都完整填写

\[
(X,T,\Pi,\mathcal S,\mathcal Q,\theta).
\]

## Model A — hard resolution interferometer

目标：明确什么含义下 primitive length resolution 会导致 phase dead-zone / quantization / extra noise。

必须输出：

- exact observable；
- predicted spectrum/staircase/dead-zone；
- LIGO-like experiment 对 `theta` 的上界形式；
- 说明为何该模型不代表所有 discrete spacetime。

## Model B — collapse-induced decoherence

目标：从 explicit many-to-one/stochastic transition 推导

\[
\eta(m,\Delta x,t;\theta)
\]

或等价 density-matrix visibility law。

必须输出：

- matter-wave experiment 可排除区域；
- parameter-free 版本是否已死亡；
- 哪些参数调整仍合法、哪些属于 post-hoc escape。

## Model C — collapse-induced energy/noise

目标：从同一或另一个 explicit `T` 推出

\[
P_{\rm collapse},\ \Gamma_\gamma,\ S_F(f)
\]

至少一个。

必须与一个低温/X-ray/force-noise实验形成定量 overlap test。

---

# 6. Escape ledger

每个 specialization 都必须维护：

| escape | allowed before data? | changes model class? | kills falsifiability? |
|---|---:|---:|---:|
| lower collapse rate | ? | ? | ? |
| smaller resolution | ? | ? | ? |
| change affected variable | ? | ? | ? |
| exact Lorentz symmetrization | ? | ? | ? |
| conserve energy by new channel | ? | ? | ? |
| add hidden reversible state | ? | ? | ? |

规则：

- 数据之前声明的自由参数可以被实验约束；
- 数据之后新加入的自由度必须标记 model revision；
- 如果所有 observable consequences 永远都可调成零，则该实现不是可反证理论。

---

# 7. 实验优先级候选

不要机械继承独立审核的原排名。第一轮建议按“与 fundamental collapse 的直接耦合程度”排序：

1. **matter-wave / coherence loss** — 对指定 collapse law 直接；
2. **spontaneous heating / radiation / force noise** — 对指定 nonunitary collapse 直接；
3. **Lorentz/anisotropy/dispersion precision tests** — 对指定 discrete implementation 直接；
4. **LIGO hard-resolution interpretation** — 只有 observable mapping 明确时直接；
5. **atomic clocks / GPS secular effects** — 需先推导累积律；
6. **semiconductor / control systems** — 当前主要作为寻找 observable 的工程压力测试。

研究员可以改变排名，但必须以“模型是否强制对应 observable”作为依据，不以实验名气排序。

---

# 8. 需要核实的 primary prior art / experimental anchors

只用 primary paper / official collaboration source核关键数值和结论。至少覆盖：

- LIGO/Virgo `Observation of Gravitational Waves from a Binary Black Hole Merger`（GW150914；peak strain ~1e-21；4 km arms 由官方仪器资料交叉核）；
- LIGO displacement calibration work reaching ~1e-18 m actuator amplitudes；
- Fein et al., `Quantum superposition of molecules beyond 25 kDa`（>25 kDa、up to ~2000 atoms、>90% expected visibility）；
- Toroš/Bassi collapse-model bounds from matter-wave interferometry；
- Piscicchia et al. spontaneous-radiation CSL bounds；
- Sanner et al. optical-clock Lorentz test（sidereal modulation null at ~1e-19 level in that parameterization）；
- Bombelli/Henson/Sorkin `Discreteness without symmetry breaking: a theorem`；
- Tumulka relativistic GRW flash-process work。

所有数值必须标注实验/模型语境，禁止从一个 parameterization 的上界直接翻译成 Enterprise Math 参数。

---

# 9. Kill tests for this task itself

R008 必须主动尝试推翻自己的路线：

1. 找到一个 explicit finite/discrete model that preserves tested Lorentz symmetry and evades LIGO hard-resolution interpretation；
2. 找到一个 many-to-one fundamental map whose declared observable sector remains exactly deterministic/unitary；
3. 找到一个 collapse model with no mandatory heating in the tested channel；
4. 证明 GPS cumulative-error assumption can cancel/average rather than grow `N delta`；
5. 证明 a semiconductor/control observable can be reproduced by both continuous and finite-state ontologies；
6. 构造 two physically distinct ontologies with identical declared observable language，展示 identifiability failure。

如果这些 countermodels 成功，必须缩小 no-go statement，而不是忽略。

---

# 10. 第一阶段交付

必须交付：

- 六类工程攻击的严格评级表；
- 至少三份完整 P016 specialization；
- 每份 specialization 的 frozen parameter/escape ledger；
- 至少一个真实实验 parameter-exclusion calculation；
- 至少两个“过宽攻击不成立”的明确 counterexample/prior-art boundary；
- full-state unitarity vs many-to-one 的 exact scope statement；
- observable reversible-completion / identifiability analysis；
- 一个可执行 physical-kill-test calculator 或 exact parameter-overlap checker；
- primary-source prior-art map；
- 对 README/P016 是否需要措辞收紧的最小建议；
- 是否产生 Foundation Feedback Packet 的结论。

---

# 11. 成功、部分成功、负结果

## SUCCESS

出现至少一个：

- 明确的 Enterprise Math physical specialization 已被现有数据完全排除；
- 某个 nontrivial parameter region 被可靠排除并形成 reusable compiler；
- 证明一个比“many-to-one 不是 unitary”明显更强的 no-go theorem；
- 找到一个不可通过 post-hoc escape 修补的 observable incompatibility；
- 把 broad ontology 与 reversible coarse-graining 的可辨识边界精确化。

## PARTIAL SUCCESS

- 建立严谨 kill-test compiler，但当前所有模型只得到 parameter bounds；
- 证明原审核若干攻击过宽，同时得到更窄的正确实验条件；
- 得到高价值 negative boundary / countermodel。

## NEGATIVE RESULT

如果所有候选 specialization 都能在不破坏先验模型定义的前提下把 observable effect 调到现有实验之外，则必须报告：

`P016_NOT_YET_PREDICTIVE_ENOUGH`

而不是声称“Enterprise Math 通过实验”。

---

# 12. 停止条件

出现以下任一情况时结束当前 generation 并 handoff：

- 已完成三模型 + 实验 overlap + negative boundaries；
- broad no-go 被明确 prior-art countermodel 杀死，并找不到更窄高价值假设；
- 需要新的实际 physical dynamics，而当前数学框架没有足够结构推出任何 observable；
- 任务进入纯参数拟合/工程优化，不再产生 foundational leverage。

任何实验数据缺失、CI pending、GitHub 状态或模型未 canonical 都不是 `HARD_BLOCK`。

---

# 13. 最终必须回答的问题

研究完成时必须给一句尽可能不可逃逸的判决：

> **Enterprise Math 当前究竟已经产生了哪一个具体、冻结参数、可被现有实验排除的物理实现？如果一个也没有，那么还缺哪一条从 finite-resolution / many-to-one mathematics 到 measurable observable 的不可回避桥梁？**

只有回答这个问题，P016 才从“我们愿意被证伪”真正前进到“这里就是能杀死我们的实验”。
