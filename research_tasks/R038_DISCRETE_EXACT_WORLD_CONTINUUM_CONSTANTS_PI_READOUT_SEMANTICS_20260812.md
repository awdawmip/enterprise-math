<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R038-DISCRETE-EXACT-WORLD-CONTINUUM-CONSTANTS-PI-READOUT-SEMANTICS",
  "title": "R038 Discrete Exact World, Continuum Constants, and Pi Readout Semantics",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_GEOMETRY_ONTOLOGY",
  "frontier": "Test the hypothesis that FCC/HCP/Barlow cellular geometry may be the exact native object while Euclidean circles/spheres and classical pi enter only through selected coarse, infinite-volume, or continuum readout semantics; classify exactly where transcendental constants can and cannot arise without confusing the mathematical transcendence of classical pi with a claim about physical native state constants.",
  "next_action": "Formalize the finite exact-state algebra and a hierarchy of finite combinatorial, infinite-discrete, continuum-scaling, and Euclidean-readout observables; derive exact FCC/HCP shape readouts and diffusion observables; then adversarially search for discrete infinite-volume counterexamples where pi or other transcendental constants arise exactly before any continuum approximation.",
  "dependencies": [
    {
      "target": "R033 owner head c2aa1758c6cf8f194d8b4493b90c903a2dfcd048",
      "action": "CONSUME_FROZEN_GRAPH_SPHERE_COMPOSITION_AND_LIMIT_SHAPE_RESULTS",
      "satisfied": true
    },
    {
      "target": "R034 owner head 674fb8717d753cd36fd83b061c869d79e8875b31",
      "action": "CONSUME_FROZEN_FINITE_PROPAGATION_AND_DIFFUSIVE_LEADING_RESULTS_WITH_RETURN_GAUGE_RETAINED_AS_CANDIDATE",
      "satisfied": true
    },
    {
      "target": "RS-R037-R033-R034-INDEPENDENT-ALGORITHM-DATA-REPLICATION-AUDIT",
      "action": "PARALLEL_TEST_INPUTS_AND_ABSORB_ANY_CONFIRMED_MISMATCH_WITHOUT_WAITING_FOR_THE_AUDIT_TO_START",
      "satisfied": false
    }
  ],
  "source_refs": [
    "R033 exact FCC/HCP shell/bulk laws, boundary composition and anisotropic graph-distance limit shapes",
    "R034 exact finite-time path counts, local covariance I/3, leading diffusive isotropy and observable memory hierarchy",
    "User foundational hypothesis on 2026-08-12: perhaps FCC/HCP cellular structure is exact, exact Euclidean circles do not exist physically, and pi belongs to approximation/readout rather than microscopic state composition"
  ],
  "evidence_status": "DISCRETE_EXACTNESS_AND_CONTINUUM_READOUT_FOUNDATION_GATE",
  "last_progress_ref": "User explicitly reframed the question from why a discrete world approaches a circle to whether the exact world has no literal circle at all, with classical pi functioning as a continuum approximation/readout constant.",
  "last_progress_at": "2026-08-12T13:17:00+08:00",
  "hard_block": null,
  "tags": [
    "R038",
    "discrete-exact-world",
    "fcc",
    "hcp",
    "barlow",
    "circle",
    "sphere",
    "pi",
    "transcendental",
    "continuum-limit",
    "coarse-readout",
    "ontology"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R038",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R038 — Discrete Exact World, Continuum Constants, and Pi Readout Semantics

Status: `READY / P0 / FOUNDATIONAL GEOMETRY ONTOLOGY / ADVERSARIAL HYPOTHESIS TEST / NOT CANONICAL`

## 0. 母问题

本任务研究以下候选，但不得预设它正确：

> **也许 FCC/HCP/Barlow 胞元世界才是 exact native world；严格欧氏圆/球不是 microscopic object，而是 coarse/continuum description；经典 π 因而可能属于这种描述语言，而不是底层状态代数。**

必须首先固定一个逻辑边界：

- 经典实数 `pi` 的超越性是已有数学定理，本任务不尝试推翻它；
- 本任务真正检验的是：**物理/胞元世界是否存在一个 exact native observable 必须等于经典 `pi`，以及 `pi` 第一次在哪一层描述中出现。**

禁止把 `pi_eff=5/2` 或 `21/8` 写成“π 不是超越数”。

正确问题是：

`exact cellular object -> exact observable -> optional infinite/continuum operation -> optional Euclidean readout constant`。

---

## 1. 任务内状态机

本任务不预绑 Researcher-ID；领取后由现行 claim/identity 机制绑定执行身份。

`READY`
→ taskbook 可领取；核心假设仍为未验证候选。

`CLAIMED`
→ 执行身份已绑定；必须先写出四层 observable taxonomy，禁止直接开始“证明 π 是近似”。

`IN_PROGRESS / EXACT_ALGEBRA_FROZEN`
→ finite cellular state、embedding number field、允许的 exact operations 和 finite observables 已精确定义。

`IN_PROGRESS / READOUT_CHANNELS_BUILT`
→ FCC/HCP graph sphere、finite random walk、infinite discrete observable、continuum scaling、Euclidean-form readout 已分别实现至少一个可复核 channel。

`IN_PROGRESS / ADVERSARIAL_KILL_TESTS`
→ 主动搜索“完全离散系统中 exact transcendental constant”的反例；任何一个反例都必须用于收窄而不是隐去母假设。

`HANDOFF_READY`
→ 若尚未完成，必须留下当前 taxonomy、已活/已死 hypothesis、最小反例和唯一 next_action。

`SEMANTIC_CHECKPOINT`
→ 已能严格回答：哪些层保证只含整数/有理/代数数，哪些层允许/需要 transcendental constants，经典 π 在 FCC/HCP 各 readout 中扮演什么角色。

`DONE / RETURNED`
→ 返回 theorem/counterexample hierarchy、exact readout atlas、transcendence-entry atlas 和明确的 ontology verdict；不得以哲学语言代替数学条件。

---

## 2. 四层 observable taxonomy

必须显式区分，禁止混层：

### L0 — finite exact cellular state

有限胞元集合、有限路径、有限邻接、有限 graph ball、有限 shell、有限 transition count。

### L1 — finite exact derived observable

由 L0 经有限次整数/有理/指定代数运算得到的：

- counts；
- rational probabilities；
- finite moments；
- finite tensor contractions；
- exact polyhedral coordinates/volumes（若处于指定 algebraic field）；
- exact finite-radius shape ratios。

### L2 — infinite discrete observable

不引入 continuum geometry，但允许：

- `n -> infinity`；
- infinite lattice sums；
- Green functions；
- spectral measures；
- thermodynamic/infinite-volume limits；
- generating functions 在特殊点的值。

### L3 — continuum/coarse readout

包括：

- diffusive rescaling；
- PDE/heat-kernel continuum limit；
- Lebesgue/Fourier integral normalization；
- Euclidean area/volume/circumference calibration；
- effective radius / effective `pi`；
- observer-defined coarse equivalence classes。

必须寻找：

`first_transcendental_layer(observable_family)`。

不能预设永远是 L3。

---

## 3. Finite exact-state algebra

从冻结 FCC/HCP/Barlow 模型独立列出：

- cell coordinates 所在环/数域；
- physical embedding 引入的 algebraic generators，例如 `sqrt(2), sqrt(3), sqrt(6)`；
- NN transition probabilities；
- finite path counts；
- finite moment algebra；
- graph-ball counts 和边界 type counts。

尝试证明一个有明确 assumptions 的 closure theorem：

> 对固定有限时间/有限半径，若输入坐标和 transition weights 属于给定 number field `K`，且 observable 只使用有限次 `+,-,*,/` 和任务明确允许的 algebraic operations，则输出仍属于某个显式 algebraic extension；不会仅靠有限 combinatorial propagation 自动生成 transcendental constant。

必须把允许操作写清楚。若 observable 自己调用 `sin`, `exp`, infinite series 或 transcendental special function，则不能再声称 closure。

---

## 4. “世界上是否有 exact 圆”的严格版本

不要用视觉近似。

至少研究两个定义：

### 4.1 Exact continuous rotational symmetry

对固定 FCC/HCP embedding，定义一个非平凡 finite cellular object 是否可能在物理空间中对中心的完整 `SO(2)` / `SO(3)` 连续旋转群保持不变。

优先证明或杀掉：

> 离散 locally finite point/cell set 中，任何包含非零半径 cell center 的 finite object 都不可能拥有完整连续旋转轨道，因此 exact Euclidean circle/sphere symmetry 不是 finite cellular object's native symmetry。

必须清楚区分：

- topological sphere；
- graph-distance sphere；
- Euclidean metric sphere；
- rotationally invariant probability law；
- rotationally invariant continuum limit。

它们不是同一个命题。

### 4.2 Exact equidistance locus

研究：

`{cell centers x : |x|=R}`

在 FCC/HCP 中是否只能形成有限方向 orbit，以及其 convex hull/point-group symmetry；不要把大量等距点误称为 continuous circle/sphere。

---

## 5. FCC/HCP Euclidean-form readout constants

冻结 graph radius `r`，只作为后验读取，定义：

`pi_A^W(r)=A_r^W/(4 r^2)`

和

`pi_V^W(r)=3 V_r^W/(4 r^3)`。

独立推导：

### FCC candidate

`pi_A^FCC(r) -> 5/2`

`pi_V^FCC(r) -> 5/2`。

### HCP candidate

`pi_A^HCP(r) -> 21/8`

`pi_V^HCP(r) -> 21/8`。

必须给 exact finite-r formulas 与 remainder。

但这只是第一组 readout。

必须更换 radius convention，例如：

- graph radius；
- physical circumradius；
- physical inradius；
- equal-volume effective radius；
- second-moment radius（若有自然定义）。

比较 `pi_eff` 是否变化。

若变化，则返回：

`NO_UNIQUE_NATIVE_PI_FROM_SHAPE_WITHOUT_READOUT_SEMANTICS`。

若某个非平凡 family 在多种独立 calibration 下稳定汇合，则作为强结果研究。

---

## 6. Finite diffusion without microscopic pi

复核并扩展 R034 的层次解释：

- `P(X_n=x)=c_n(x)/12^n` 是 exact rational；
- finite `n` moments/tensors 位于指定 algebraic field；
- local covariance `I/3` 不含 `pi`；
- finite-time distribution 并不 exact rotationally invariant。

然后明确定位 continuum Gaussian：

`X_n/sqrt(n) -> N(0,I/3)`。

研究 `pi` 是在哪一步出现：

- Gaussian density normalization；
- Fourier inversion；
- radial continuum integration；
- Euclidean sphere volume element。

必须区分：

`microscopic transition rule has no pi`

与

`all exact discrete observables can never contain pi`。

后者必须专门接受反例攻击。

---

## 7. 最关键 kill test：纯离散 infinite-volume 是否会 exact 产生 transcendental constants

这是本任务不能回避的部分。

主动寻找 prior art 和可复算例子：

- lattice Green functions；
- exact return probabilities / escape probabilities；
- integrated DOS；
- spanning-tree constants；
- Mahler measures；
- infinite product/sum limits；
- special values of generating functions。

目标不是证明它们一定含 `pi`，而是判断：

> **是否存在完全从离散格点/图定义出发、没有先输入欧氏圆周率，却在 exact infinite discrete observable 中出现 `pi`、Gamma 值、elliptic integrals 或其他 transcendental/special-function constants？**

若存在一个可靠例子，就杀掉过强命题：

`TRANSCENDENTALS_ONLY_APPEAR_AFTER_CONTINUUM_APPROXIMATION`。

然后把理论收窄为：

`finite exact algebra may be algebraic, while infinite completion/limit operations can generate transcendental constants even before continuum geometric approximation`。

这是允许且高价值的正结果。

---

## 8. “π 是近似运算”必须形式化

如果数据支持，不要停留在语言上。

至少定义一种 readout operator：

`R_E : exact cellular object -> Euclidean parameter tuple`

例如输出：

- effective radius；
- effective area；
- effective volume；
- effective `pi`；
- Gaussian covariance；
- continuum density parameters。

研究：

- `R_E` 丢掉哪些 microscopic distinctions；
- FCC/HCP 哪些对象在 `R_E` 下 recoalesce；
- error/remainder 如何随 scale 衰减；
- `R_E` 是否依 propagation semantics 而变；
- `R_E` 是否可能是 many-to-one；
- classical `pi` 是否只在特定 readout family 中出现。

若“π 是近似运算”成立，最终应重述成类似：

> `pi` is a structural constant of a chosen Euclidean continuum readout, not necessarily an element of the finite microscopic state algebra.

而不是声称经典 `pi` 失去超越性。

---

## 9. Circle as coarse equivalence class

构造至少一个可检验 equivalence relation，而不是哲学比喻。

候选：

两个离散对象 `X,Y` 在 scale `s` 和 observable family `O` 下等价，当且仅当其 normalized readout vector 的距离 `<= eps(s)`，且 `eps(s)->0`。

或在 diffusion channel：

当 principal quadratic form 相同，则定义 leading-diffusive equivalence；quartic correction 作为下一 refinement level。

用 R033/R034 检验：

- FCC/HCP graph balls 在 ballistic leading class 中不等价；
- FCC/HCP uniform diffusion 在 quadratic leading class 中等价；
- quartic refinement 后再次区分。

目标是把：

`circle/sphere = coarse observational equivalence class`

变成 typed mathematical statement。

---

## 10. 必须攻击的 hypotheses

### H1 — Finite Exact Algebraicity

在明确 finite-operation assumptions 下，finite cellular observables 保持在 algebraic closure / declared number field extension 内。

### H2 — No Native Continuous Circle at Finite Cellular Scale

非平凡 finite FCC/HCP cellular object 不具有完整 continuous rotational symmetry。

### H3 — Graph-Sphere Euclidean-Form Rational Readouts

在 graph-radius convention 下，FCC/HCP `pi_A` 与 `pi_V` 分别趋于 `5/2` 与 `21/8`。

### H4 — Readout Dependence

改变 radius/observable semantics 会改变上述 `pi_eff`；因此没有无条件唯一的 native `pi`。

### H5 — Finite Diffusion Pi-Free Microscopic Algebra

finite path counts/probabilities/moments 不需要输入 classical `pi`。

### H6 — Pi Appears in Gaussian Continuum Readout

classical `pi` 在 Gaussian normalization / Fourier inversion / Euclidean integration 中自然出现。

### H7 — Transcendentals Only After Continuum Approximation

必须 adversarially 攻击。优先寻找 pure-discrete infinite-volume exact counterexample。

### H8 — Discrete Infinite Completion Is a Separate Transcendence Gateway

若 H7 被杀，研究 L2 infinite discrete completion 是否本身就是 transcendental/special-function constants 的生成层。

### H9 — Circle/Sphere as Observable-Relative Equivalence Class

用 ballistic vs diffusive FCC/HCP 形成 exact positive/negative test。

### H10 — Physical Native Pi Is Not a Well-Posed Scalar Without Semantics

只有在先声明 geometry、radius、propagation、observable/readout 后，`pi_eff` 才有确定含义。

---

## 11. 禁止偷换

不得：

- 写 `pi=5/2`、`pi=21/8`；
- 说经典 π“不再是超越数”；
- 从“有限离散计算只给代数数”推出“一切无限离散物理量也只给代数数”；
- 把 Gaussian limit 当 microscopic object；
- 因为 R033 graph sphere 各向异性，就否定 R034 diffusion 的 leading isotropy；
- 因为 diffusion leading isotropy，就说 exact finite world 有 continuous rotational symmetry；
- 为了支持用户假设忽略纯离散 infinite-volume counterexample。

---

## 12. 高价值返回类别

允许：

`FINITE_EXACT_STATE_ALGEBRA_CLASSIFIED`

`NO_FINITE_NATIVE_CONTINUOUS_CIRCLE_FOUND`

`GRAPH_RADIUS_READOUT_5_OVER_2_AND_21_OVER_8_CONFIRMED`

`NO_UNIQUE_NATIVE_PI_WITHOUT_READOUT_SEMANTICS`

`PI_ENTERS_AT_CONTINUUM_GAUSSIAN_READOUT`

`TRANSCENDENTALS_ONLY_AFTER_CONTINUUM_SURVIVES`

也允许且非常重要：

`TRANSCENDENTAL_PURE_DISCRETE_INFINITE_COUNTEREXAMPLE_FOUND`

`INFINITE_DISCRETE_COMPLETION_SEPARATE_GATEWAY_FOUND`

`CIRCLE_AS_COARSE_EQUIVALENCE_CLASS_FORMALIZED`

`USER_HYPOTHESIS_PARTIALLY_KILLED_AND_REFINED`

---

## 13. 必须返回

至少形成：

- exact-state algebra specification；
- finite/infinite/continuum/readout observable taxonomy；
- exact FCC/HCP `pi_eff` readout atlas under multiple radius conventions；
- finite cellular rotational-symmetry theorem/counterexample；
- finite diffusion algebra audit；
- pure-discrete infinite-volume transcendental search with at least one deeply checked example or a clearly bounded negative result；
- continuum `pi`-entry derivation；
- coarse-equivalence formalization；
- H1–H10 dispositions；
- prior-art matrix；
- strongest theorem candidates；
- minimal counterexamples；
- final ontology verdict。

最终必须直接回答：

> **在 FCC/HCP/Barlow exact cellular worldview 下，经典 `pi` 是 microscopic native constant、infinite-discrete exact constant、continuum-limit structural constant、Euclidean readout constant，还是这些角色中的一部分；“世界上没有 exact 圆，圆只是近似”应当被证明、收窄，还是被反例杀掉。**
