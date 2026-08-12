<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R036-BARLOW-PROPAGATION-UNIVERSALITY-FRACTURE-ATLAS",
  "title": "R036 Barlow Propagation Universality Fracture Atlas",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_PHYSICAL_DYNAMICS",
  "frontier": "Characterize exactly which perturbations of the ideal uniform nearest-neighbor Barlow propagation law preserve or destroy zero drift, isotropic covariance, leading Brownian universality, higher-order stacking memory, and nearest-neighbor return/DOS gauge universality.",
  "next_action": "Solve the exact propagation-kernel parameter locus preserving isotropic second moments, then introduce the smallest symmetry-breaking and range-extending perturbations and locate the first algebraic/spectral mechanism that fractures each R034 universality class.",
  "dependencies": [
    {
      "target": "R034 owner head 674fb8717d753cd36fd83b061c869d79e8875b31",
      "action": "CONSUME_FROZEN_UNIFORM_NN_COVARIANCE_MEMORY_HIERARCHY_AND_PROPAGATION_RELATIVE_SPHERE_RESULTS_WITHOUT_REDERIVING_R034_AS_THE_MAIN_TASK",
      "satisfied": true
    },
    {
      "target": "R033 owner head c2aa1758c6cf8f194d8b4493b90c903a2dfcd048",
      "action": "USE_ONLY_AS_THE_FROZEN_SHORTEST_PATH_BALLISTIC_BASELINE",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R034 Draft PR #520 and task-scoped exact artifacts",
    "R033 frozen FCC/HCP graph and embedding models",
    "User/Driver continuation: after uniform NN diffusion produced exact I/3 covariance, the next question is where that universality breaks rather than how to re-prove it"
  ],
  "evidence_status": "PROPAGATION_UNIVERSALITY_FRACTURE_GATE",
  "last_progress_ref": "R034 found exact all-time second-moment universality and leading isotropic diffusion for FCC/HCP/Barlow under uniform ideal NN propagation, while higher-order observables retain stacking memory; Driver identified the next frontier as the exact parameter boundary of this universality.",
  "last_progress_at": "2026-08-12T12:57:00+08:00",
  "hard_block": null,
  "tags": [
    "R036",
    "barlow",
    "fcc",
    "hcp",
    "propagation",
    "weighted-random-walk",
    "universality-fracture",
    "diffusion-tensor",
    "gauge-fracture",
    "long-range-hopping",
    "physical-dynamics"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R036",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R036 — Barlow Propagation Universality Fracture Atlas

Status: `READY / P0 / FOUNDATIONAL PHYSICAL DYNAMICS / UNIVERSALITY FRACTURE / NOT CANONICAL`

## 0. 任务定位

R034 已冻结 uniform ideal nearest-neighbor 传播语义下的核心现象：

- FCC/HCP/任意合法 ideal Barlow 局部条件均值为 0；
- 条件二阶矩精确为 `I/3`；
- FCC/HCP 对所有 `n` 有 `E[X_n X_n^T]=n I/3`；
- shortest-path ballistic sphere 与 diffusive leading sphere 不同；
- stacking memory 转移到三阶、四阶、六阶、有限时角分布等更细 observable；
- NN Barlow return/local-DOS stacking-independence 目前是 strong gauge theorem candidate，不与 covariance theorem 同级冻结。

本任务不再问“uniform NN diffusion 会不会圆”。

本任务问：

> **这个圆化 universality 在传播核参数空间中到底有多大？什么是最小破裂机制？**

目标是建立：

`propagation kernel parameters -> exact drift/covariance class -> leading macro geometry -> higher-order memory -> return-gauge status`。

---

## 1. 第一阶段：exact weighted-NN universality locus

### 1.1 一般局部权重

对冻结的 FCC/HCP/Barlow 12 个 unit NN 位移 `v_i`，令转移概率

`p_i >= 0`, `sum_i p_i = 1`。

必须 exact 求解：

- zero drift 条件 `sum p_i v_i = 0`；
- isotropic covariance 条件 `sum p_i v_i v_i^T = c I`；
- 两者同时成立时的完整可行参数集合；
- 该集合的 affine dimension、线性约束秩、极点/face structure；
- FCC 与 HCP-A/HCP-B 的可行集合是否同构；
- 若要求同一个 local rule 在任意 Barlow stacking 每个 cell 都成立，可行集合进一步缩成什么。

不得只测试几个权重例子；优先得到 exact rational/algebraic polytope description。

### 1.2 两速率对称子族

作为必须完成的 sanity family：

- 每个同层边权重为 `a`；
- 每个层间边权重为 `b`；
- `6a+6b=1`。

独立验证候选：

`Sigma(a,b)=diag(3a+b, 3a+b, 4b)`

（在正交物理 stacking frame 中）。

若成立，则证明/杀掉：

`Sigma is scalar <=> a=b=1/12`。

如果成立，这意味着 uniform NN 是该自然对称族中唯一的二阶欧氏点，而不是一个宽松区域。

### 1.3 方向性扰动

对 basal 六方向和 interlayer 三角方向允许最小独立扰动，分类：

- 哪些 perturbation 先产生 drift；
- 哪些仍 zero-drift 但 covariance anisotropic；
- 哪些仍 covariance isotropic 但三阶/四阶已经改变；
- isotropic covariance locus 是否存在 nonuniform positive family。

建立最小 perturbation witnesses。

---

## 2. exact all-time 与 asymptotic 必须分开

对于任意仍满足 cellwise

`E[Delta X_t | F_{t-1}]=0`

和固定/层依赖 conditional covariance 的 weighted NN kernel，分别判断：

1. exact all-time second moment 是否仍有闭式；
2. predictable quadratic variation 是否确定；
3. 如果 local covariance 随 layer/stacking 变动，是否只有 time-averaged/homogenized effective tensor；
4. periodic stacking 与 deterministic nonperiodic stacking 的结论边界；
5. leading Brownian limit 是否各向同性、各向异性、或依赖 stacking frequency。

不要把 local covariance anisotropy 直接等同于 homogenized diffusion anisotropy；必须实际推导。

---

## 3. 第二阶段：最小 range extension 与 gauge fracture

R034 的 NN Barlow return-gauge候选依赖一个关键结构：basal Fourier transform 后，layer graph 是一维链，interlayer hopping 的 stacking dependence 只进入 phase，因此可被 diagonal gauge 消去。

本任务要定位这个机制的最小失效方式。

### 3.1 NN weighted gauge

先 exact 判断：

- 哪些 NN 权重仍只改变 hopping magnitude 而不产生不可消 gauge invariant；
- stacking-dependent orientation weights 是否让 hopping magnitude 本身依赖 stacking；
- 在什么条件下 root return / local spectral measure / integrated DOS 仍可 stacking-independent。

### 3.2 next-layer / longer-range hopping

加入最小的 `Delta layer = 2` 或 task-justified next-nearest physical shell transition，使 basal-Fourier 后的 layer graph 出现 cycle。

重点检验：

- 最近邻 `j<->j+1` 与 `j<->j+2` 共存是否产生最小 gauge-invariant loop phase/flux；
- stacking word 是否第一次进入 gauge-invariant spectral quantity；
- return probability / local DOS 是否立即分裂；
- 最小 `n` 的 return-count witness；
- FCC/HCP/ABC/ABAB/其他周期 stacking 哪一对最早分开。

如果 layer-cycle/flux 是真正断裂机制，提炼成 narrow theorem candidate：

`acyclic reduced layer graph => all phases gauge-removable`；

`cycle + nontrivial phase product => stacking-sensitive gauge invariant`。

不要在没有证明必要/充分条件时过度泛化。

---

## 4. continuous-time control

对相同 spatial kernel 的 continuous-time generator 做 control：

- 如果只是统一 Poissonization，确认宏观几何只发生 time rescaling；
- 如果 rate 依方向/层类型改变，重新计算 generator Hessian 与 effective tensor；
- 区分“时间参数变化”与“传播几何真的变化”。

continuous-time heat 不是独立发现目标，而是离散结论的语义稳定性控制。

---

## 5. persistent propagation 作为第三阶段可选项

只有在 weighted-NN 与 gauge-fracture 主线完成后，才允许引入 one-step memory / persistent walk：状态扩充为 `(cell, previous direction/class)`。

优先问：

- persistence parameter 是否产生 ballistic-to-diffusive crossover；
- effective diffusion tensor 是否仍可 isotropic；
- stacking memory 是否从高阶回落到二阶；
- shortest-path polyhedral geometry 与 diffusion geometry 之间是否出现连续插值或新相。

不要因为“量子/波动听起来更物理”而提前跳过 classical exact fracture calculus。

---

## 6. 必须建立 universality/fracture matrix

至少冻结以下 observable：

- local drift；
- local covariance；
- exact all-time second moment；
- effective diffusion tensor；
- local order-3 memory；
- principal-band quartic memory；
- scalar radial moment memory；
- finite-time path-count distribution；
- return probability；
- root local spectral measure；
- integrated DOS；
- physical momentum-labelled dispersion；
- heat-kernel angular correction。

对每种传播核给出：

`EXACTLY_UNIVERSAL / LEADING_UNIVERSAL / STACKING_DEPENDENT / ANISOTROPIC / DRIFTING / GAUGE_REMOVABLE / GAUGE_FLUX_PRESENT / OPEN`。

---

## 7. 关键候选

### H1 — Uniform NN isolated isotropic point in the two-rate family

在 same-layer/interlayer 对称两速率族中，uniform NN 是唯一 exact isotropic covariance kernel。

### H2 — Nonuniform isotropic-weight polytope

在完整 12-edge weight simplex 中可能存在非均匀、仍 zero-drift 且 covariance scalar 的正维可行集合。必须 exact 求出或杀掉。

### H3 — Barlow-wide second-moment universality is symmetry-conditioned

R034 的 arbitrary Barlow `I/3` universality 不是“close packing 自动导致”，而是 ideal geometry + uniform/special weight constraints 的结果。

### H4 — Gauge universality is acyclicity-conditioned

NN stacking phase之所以能消去，是 reduced layer graph 无 cycle；最小长程 hopping 产生 cycle 后出现不可消 gauge flux，并使 return/local DOS 恢复 stacking memory。

### H5 — Continuous-time Poissonization preserves spatial sphere class

统一 rate continuous-time walk 只重标时间，不改变 normalized leading geometry 与 memory-order hierarchy。

### H6 — Observable memory can move downward under perturbation

uniform NN 下被推到 order 3/4/6 的 stacking memory，在 weighted/long-range/persistent semantics 中可能重新出现在 drift 或 covariance（二阶）层。

---

## 8. exact evidence requirements

优先 exact integers / rationals / algebraic surds。

必须有：

- symbolic linear-system/polytope solve for weighted-NN conditions；
- exact small-state enumeration for representative perturbations；
- exact Fourier/Bloch/Jacobi fibers where periodicity permits；
- minimal counterexamples；
- independent holdout parameters not used in law discovery；
- theorem candidate 与 numerical/asymptotic evidence 严格分级。

如果使用 floating eigensolver，只能作 diagnostic；theorem-critical gauge/weight conditions必须有 exact certificate。

---

## 9. 与 R034 的边界

R034 以下结果不重做：

- uniform ideal NN FCC/HCP covariance `I/3`；
- exact `E[X_nX_n^T]=nI/3`；
- local-3 / spectral-4 / radial-6 memory hierarchy；
- ballistic/diffusive geometry split。

R036 只研究：

`这些 universality 为什么成立，以及最小在哪儿破裂。`

R034 的 all-Barlow return/local-DOS gauge statement在本任务开始时仍按 `STRONG_THEOREM_CANDIDATE` 处理，不得当作已冻结 theorem；R036 应给它独立 operator/algebra certificate 或找到反例。

---

## 10. 最终返回

至少交付：

- weighted-NN isotropy/zero-drift exact parameter atlas；
- two-rate uniqueness theorem verdict；
- FCC/HCP/Barlow universality-locus comparison；
- minimal covariance-fracture perturbations；
- NN gauge theorem independent audit；
- minimum longer-range gauge-fracture model；
- return/DOS split witness or proof of continued universality；
- continuous-time control；
- universality/fracture matrix；
- strongest theorem candidates；
- minimal counterexamples；
- prior-art rooting；
- Foundation/Lean recommendation；
- whether persistent/wave/quantum propagation should be the next independent task.

最高价值正结果包括：

`UNIFORM_NN_ISOLATED_ISOTROPIC_POINT_FOUND`

`NONUNIFORM_ISOTROPIC_WEIGHT_MANIFOLD_FOUND`

`BARLOW_UNIVERSALITY_LOCUS_CLASSIFIED`

`COVARIANCE_FRACTURE_SURFACE_FOUND`

`GAUGE_ACYCLICITY_THEOREM_FOUND`

`MINIMAL_GAUGE_FLUX_FRACTURE_FOUND`

`RETURN_DOS_STACKING_MEMORY_RESTORED`

`MEMORY_ORDER_MOVES_DOWN_UNDER_PERTURBATION`

也允许这些候选被杀掉。
