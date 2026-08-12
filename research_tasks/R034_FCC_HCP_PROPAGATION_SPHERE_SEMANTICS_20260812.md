<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R034-FCC-HCP-PROPAGATION-SPHERE-SEMANTICS",
  "title": "R034 FCC/HCP Propagation-Sphere Semantics: Ballistic, Diffusive, and Spectral Geometry",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_GEOMETRY_PHYSICS_BRIDGE",
  "frontier": "Determine whether R033's permanent FCC/HCP anisotropy is specific to shortest-path reachability or persists under intrinsic stochastic/spectral propagation on the same cell worlds; test whether an isotropic and possibly FCC/HCP-universal macroscopic sphere can emerge without inserting a continuous sphere or pi into the microscopic definition.",
  "next_action": "Freeze the R033 exact FCC/HCP graphs as microscopic input, derive exact nearest-neighbor moment tensors, build random-walk and heat-kernel/spectral propagation models, compare their macroscopic level-set geometry with the R033 word-metric balls, identify the first order at which FCC/HCP stacking memory survives, and certify the finite-scale correction at very large propagation scales.",
  "dependencies": [
    {
      "target": "R033 owner head c2aa1758c6cf8f194d8b4493b90c903a2dfcd048",
      "action": "CONSUME_EXACT_FCC_HCP_GRAPH_MODELS_PHYSICAL_GRAM_MATRICES_AND_WORD_METRIC_LIMIT_SHAPES_AS_FROZEN_RESEARCH_INPUT",
      "satisfied": true
    },
    {
      "target": "P012 graph-distance common surface",
      "action": "USE_ONLY_FOR_THE_BALLISTIC_WORD_METRIC_BASELINE_AND_KEEP_PROPAGATION_SEMANTICS_TYPE_DISTINCT",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R033 exact graph-ball laws, boundary spectra, exposed-face topology atlas, and FCC/HCP polyhedral word-metric limit shapes",
    "User/Driver observation after R033: a graph ball is one intrinsic sphere semantics, not automatically every physical propagation sphere",
    "standard martingale/random-walk invariance principles and periodic-graph spectral/Bloch methods to be rooted only after the task's exact local calculations are frozen",
    "Barlow close-packed stacking family as an optional generalization after FCC/HCP core completion"
  ],
  "evidence_status": "PROPAGATION_RELATIVE_INTRINSIC_GEOMETRY_GATE",
  "last_progress_ref": "R033 showed leading-order FCC/HCP memory under graph distance but an identical exposed-face scalar law; Driver identified a new semantic split between ballistic reachability and diffusive/spectral propagation, with an independently hand-checked candidate isotropic one-step covariance for both FCC and ideal HCP.",
  "last_progress_at": "2026-08-12T12:00:00+08:00",
  "hard_block": null,
  "tags": [
    "R034",
    "fcc",
    "hcp",
    "barlow",
    "random-walk",
    "diffusion",
    "heat-kernel",
    "spectral-geometry",
    "emergent-isotropy",
    "propagation-sphere",
    "intrinsic-geometry"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R034",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R034 — FCC/HCP Propagation-Sphere Semantics: Ballistic, Diffusive, and Spectral Geometry

Status: `READY / P0 / FOUNDATIONAL GEOMETRY-PHYSICS BRIDGE / NOT CANONICAL`

## 0. 任务定位与推进向量

R033 已经回答了一个明确问题：以最近邻最短步数作为半径时，FCC 与 HCP 的内禀 graph ball 都具有稳定多面体极限，而且二者不同。

R034 不重新证明 R033，也不把 R033 的 word metric 当成唯一可能的“物理半径”。

本任务问：

> 在完全相同的 FCC/HCP 胞元和最近邻局部规则上，如果宏观距离/球面不是由“最少几步能到达”定义，而是由随机传播、热传播或低频谱定义，那么大尺度几何是否仍然保持 R033 的多面体各向异性？还是会出现另一个、可能各向同性甚至 FCC/HCP 普适的宏观球？

任务前估计：

- ballistic / word-metric geometry：`~90%`，R033 已建立；
- diffusive exact local tensor：`~20%`，只有 Driver 手算 sanity candidate；
- heat-kernel / low-frequency spectral geometry：`~10%`；
- FCC/HCP propagation-semantics comparison：`~5%`；
- Barlow-stack universality：`~0%`。

目标推进向量：

`propagation-relative geometry +60% / emergent-isotropy test +60% / stacking-memory order classification +50% / continuous-prior dependence -80%`.

---

## 1. 冻结输入与禁止偷换

### 1.1 FCC/HCP microscopic world

直接复用 R033 的 exact combinatorial models：

- FCC `D3` 12-neighbor graph；
- ideal HCP ABAB 12-neighbor graph；
- R033 exact physical Gram matrices/embeddings；
- nearest-neighbor physical length统一归一化为 1。

不得修改邻接关系来追求各向同性。

### 1.2 R033 ballistic baseline

冻结：

- FCC word-metric limit = cuboctahedral norm ball；
- HCP word-metric limit = distinct 18-vertex polytope；
- FCC/HCP word-metric leading shell/bulk growth differs by 5%；
- graph-distance macroscopic universality is killed。

本任务不能把 diffusive/spectral 结果回写成“R033 错了”。不同 propagation semantics 必须保持类型分离。

### 1.3 不允许把连续球作为生成器

不得先写 `x^2+y^2+z^2<=R^2` 再调参数让随机过程拟合它。

所有有效的二次型、扩散张量、level set、谱展开，都必须从局部转移/邻接算子推出。

`pi` 不得作为 microscopic input。

---

## 2. Propagation semantics A — Ballistic / shortest-path baseline

只做必要复算和接口冻结：

\[
B_r^{word}=\{x:d_G(0,x)\le r\}.
\]

记录 R033 的：

- stable norm；
- anisotropy ratio；
- FCC/HCP leading shell/bulk coefficient；
- boundary-type spectrum。

此通道是对照组，不再扩大枚举。

---

## 3. Propagation semantics B — Uniform nearest-neighbor random walk

定义：从每个胞元等概率选择 12 个最近邻之一：

\[
P(x\to y)=1/12.
\]

使用 R033 exact physical embedding，把一步位移记为 `Delta X`。

### 3.1 必须 exact 计算

分别对 FCC、HCP-A、HCP-B 计算：

\[
E[\Delta X\mid x],
\]

\[
\Sigma(x)=E[\Delta X\Delta X^T\mid x],
\]

以及四阶、六阶局部 moment tensors。

Driver sanity candidate 必须独立攻击：

\[
\boxed{E[\Delta X\mid x]=0}
\]

并且在 nearest-neighbor length = 1 的正交物理坐标中：

\[
\boxed{\Sigma(x)=\frac13 I}
\]

是否对 FCC、HCP-A、HCP-B 全部精确成立？

不得因为点群“看起来对称”而直接接受，必须给 exact tensor calculation。

### 3.2 多步 second moment

如果条件均值为零且条件 covariance 为固定 `I/3`，检验/证明：

\[
E[X_n]=0,
\qquad
E[X_nX_n^T]=\frac n3 I
\]

是否 exact 对所有 n 成立。

若成立，要明确区分：

- second-moment isotropy；
- full distribution isotropy；
- heat-kernel/CLT isotropy；
- finite-n shell isotropy。

不得把二阶矩自动升级为完整球对称。

### 3.3 exact finite-n oracle

对小/中 n 实际传播 probability distribution（优先 exact integer path counts / rational probabilities），至少记录：

- support size；
- radial moment hierarchy；
- directional anisotropy observables；
- FCC/HCP distribution distance；
- residue / layer-parity effects；
- first n at which distributions become distinguishable beyond second moments。

---

## 4. Propagation semantics C — Heat kernel / spectral low-frequency geometry

使用同一个 transition operator `P` 或 graph Laplacian。

### 4.1 FCC Fourier symbol

FCC 是单轨道 periodic graph。构造 exact/closed Fourier symbol：

\[
\lambda_F(k)=\frac1{12}\sum_{v\in N_F}e^{i k\cdot v}.
\]

在 `k=0` 附近展开至少到四阶，优先六阶。

必须抽取：

- Hessian / quadratic form；
- quartic tensor；
- first anisotropic invariant；
- 对应 finite-scale correction order。

### 4.2 HCP Bloch symbol

HCP 有 A/B 两个周期轨道。构造 `2x2` Bloch/transition matrix，研究主 eigenvalue band `lambda_+(k)` 在 `k=0` 的展开。

必须比较：

- quadratic term 是否与 FCC 完全相同；
- quartic / sixth-order term 是否保存 stacking memory；
- optical/secondary band 是否影响 long-time leading geometry；
- AB parity 是否只进入 subleading correction。

### 4.3 Intrinsic diffusive sphere

从任务内部得到的有效 quadratic form `Q` 定义 diffusive radial coordinate；例如 heat-kernel principal exponent 或 covariance ellipsoid。

只有在 `Q` 被 exact 推出之后，才能判断 level set 是否为 Euclidean sphere。

若：

\[
Q=c\,I,
\]

返回 `DIFFUSIVE_ISOTROPY_FOUND`；若 FCC/HCP 的 c 相同，再返回 `FCC_HCP_DIFFUSIVE_LEADING_UNIVERSALITY_FOUND`。

这两个结论都不能否定 R033 的 ballistic anisotropy；它们共同意味着 sphere semantics 是 propagation-relative。

---

## 5. 重点攻击 H1–H12

### H1 — exact local zero drift

FCC/HCP uniform NN walk 均满足一步条件均值 0。

### H2 — exact common covariance

在 NN length=1 归一化下：

\[
\Sigma_F=\Sigma_{H,A}=\Sigma_{H,B}=I/3.
\]

### H3 — exact n-step second-moment universality

若 H1/H2 成立，则：

\[
E[X_nX_n^T]=nI/3
\]

对 FCC/HCP 全 n exact。

### H4 — leading diffusive isotropy

适当 `sqrt(n)` 缩放后，FCC/HCP principal diffusive geometry 都由同一个 isotropic quadratic form 控制。

必须给 theorem/prior-art boundary；不能仅靠 histogram。

### H5 — stacking memory moves to higher order

即使 H2–H4 成立，FCC/HCP 在 quartic/sixth moment、Bloch expansion 或 finite-n distribution 中仍可区分。

必须找最小阶数与最小 witness。

### H6 — ballistic/diffusive sphere non-equivalence

同一个胞元 world 同时拥有：

- ballistic stable polytope；
- diffusive quadratic sphere/ellipsoid。

若成立，冻结为 `PROPAGATION_RELATIVE_SPHERE`，不要强迫选唯一 sphere semantics。

### H7 — R033 common exposed-face scalar as coarse-memory-loss analogue

研究但不预设：R033 中 FCC/HCP exact common exposed-face count，与本任务可能的 common second-moment tensor 是否只是两个独立巧合，还是都来自某个更低阶局部 balance invariant。

若无结构联系，明确 kill。

### H8 — Barlow local second-moment universality

在 FCC/HCP 完成后，推广到一般 Barlow close-packed stacking：

- 6 same-layer + 3 above + 3 below；
- arbitrary legal stacking word。

攻击候选：每个局部环境都 exact zero drift + `I/3` covariance，因此二阶 diffusive geometry 与 stacking sequence 无关。

如果任意 Barlow stacking 都成立，这是高优先级 theorem candidate。

### H9 — Barlow full diffusive universality

H8 不自动推出完整 CLT/heat-kernel universality，尤其对非周期 stacking。必须分开：

- exact local martingale tensor；
- periodic stacking CLT；
- arbitrary/nonperiodic stacking invariance principle。

### H10 — no-pi microscopic input / post-hoc pi appearance

若 isotropic Gaussian/heat kernel 的 continuum normalization 后验出现 `pi`，必须记录它出现在哪一步。

不得把它重写成 microscopic sphere definition。

### H11 — finite-scale anisotropy decay law

找到一个明确定义的 diffusive anisotropy observable `A_n`，导出 exact/asymptotic decay law或严格界。

候选尺度可以是 `O(1/n)`、`O(1/sqrt(n))` 或其他；由数据和展开决定，不预设。

### H12 — macro-scale sufficiency under propagation semantics

只有得到 H11 型 bound 后，才评估：

- `n=10^36`；
- 如需 radius-matched comparison，明确 `R~sqrt(n)` 后再评价对应 n。

必须回答：“10^36 对 diffusive sphere 是否也已经足够洗掉 subleading stacking memory？”

---

## 6. 关键量与输出分类

至少输出以下层级，不得混写：

1. `WORD_METRIC_BALL_SHAPE`
2. `ONE_STEP_MOMENT_TENSOR`
3. `N_STEP_SECOND_MOMENT`
4. `FINITE_N_DISTRIBUTION`
5. `HEAT_KERNEL_QUADRATIC_FORM`
6. `FIRST_STACKING_SENSITIVE_HIGHER_ORDER_TENSOR`
7. `LOW_FREQUENCY_BAND_EXPANSION`
8. `DIFFUSIVE_LIMIT_SHAPE`
9. `FINITE_SCALE_ANISOTROPY_REMAINDER`
10. `BARLOW_EXTENSION_STATUS`

允许一个世界在不同层级同时“universal”和“non-universal”。

---

## 7. 实验与证明纪律

优先顺序：

1. exact one-step tensor；
2. exact small-n path-count oracle；
3. symbolic moment recurrence；
4. Fourier/Bloch expansion；
5. asymptotic theorem candidate；
6. finite-scale remainder；
7. Barlow generalization；
8. 最后 prior-art rooting。

漂亮的 isotropy 结果一旦出现，立即寻找：

- quartic counterexample；
- parity counterexample；
- modified stacking counterexample；
- unequal transition-weight counterexample。

不要把“uniform NN walk 的特殊平衡”误写成所有 dynamics 的宇宙规律。

---

## 8. 必须生成的 artifact

至少：

- `research/R034_FCC_HCP_PROPAGATION_SPHERE_REPORT.md`
- executable exact experiment/symbolic engine；
- focused tests；
- `R034_LOCAL_MOMENT_TENSORS.json`
- `R034_FINITE_N_PROPAGATION_ATLAS.json`
- `R034_SPECTRAL_EXPANSION.json`
- `R034_PROPAGATION_SEMANTICS_MATRIX.json`
- `R034_BARLOW_EXTENSION.json`
- `R034_HYPOTHESIS_DISPOSITIONS.json`
- strongest theorem candidates + minimal counterexamples。

---

## 9. PASS / KILL 判据

### 强正结果

任一成立均有高价值：

`FCC_HCP_DIFFUSIVE_LEADING_UNIVERSALITY_FOUND`

`DIFFUSIVE_ISOTROPY_FOUND`

`PROPAGATION_RELATIVE_SPHERE_FOUND`

`STACKING_MEMORY_MOVES_TO_HIGHER_ORDER`

`BARLOW_SECOND_MOMENT_UNIVERSALITY_FOUND`

`NO_PI_INPUT_BUT_CONTINUUM_ISOTROPY_EMERGES`

### 强负结果

也允许：

`DIFFUSIVE_ANISOTROPY_SURVIVES_LEADING_ORDER`

`FCC_HCP_DIFFUSIVE_UNIVERSALITY_KILLED`

`LOCAL_COVARIANCE_SANITY_CANDIDATE_KILLED`

`BARLOW_UNIVERSALITY_KILLED_WITH_MINIMAL_STACKING_WORD`

### 必须避免的伪结论

- `R033 graph ball anisotropic => all physical propagation anisotropic`；
- `second moment isotropic => full finite-n distribution spherical`；
- `FCC/HCP same covariance => same graph`；
- `pi appears in Gaussian normalization => pi was microscopic input`。

---

## 10. 最终必须直接回答

1. R033 的“球不是欧氏球”究竟是 word-metric 专属，还是传播无关？
2. FCC 与 HCP 的 uniform NN diffusion 在 leading order 是否相同？
3. stacking memory 第一次出现在哪个 moment / spectral order？
4. 同一个 cell world 是否同时自然产生 polyhedral ballistic sphere 与 isotropic diffusive sphere？
5. 如果出现 isotropic continuum geometry，它是在什么数学步骤中涌现的？
6. `10^36` 对这种 propagation sphere 是否也已经是稳定宏观尺度？
7. 结果是否值得进一步进入 wave / quantum-walk / finite-field 等不同 future-language 的 sphere/geometry 研究？
