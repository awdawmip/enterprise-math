<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R037-R033-R034-INDEPENDENT-ALGORITHM-DATA-REPLICATION-AUDIT",
  "title": "R037 Independent R033/R034 Algorithm and Data Replication Audit",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_VERIFICATION",
  "frontier": "Independently reproduce the theorem-critical algorithms, exact data, formulas, finite certificates, asymptotic bounds, and evidence classifications of R033 and R034 without using their executable implementation as the derivation engine, and identify any mismatch before the discrete-world/continuum-readout theory is extended further.",
  "next_action": "Build an independent exact model of FCC/HCP/ideal-Barlow geometry and propagation, reproduce the frozen R033/R034 results from definitions, compare only after independent derivation, and return a claim-by-claim evidence matrix with exact counterexamples for any failure.",
  "dependencies": [
    {
      "target": "R033 owner head c2aa1758c6cf8f194d8b4493b90c903a2dfcd048",
      "action": "TEST_FROZEN_INTRINSIC_GRAPH_SPHERE_RESULTS",
      "satisfied": true
    },
    {
      "target": "R034 owner head 674fb8717d753cd36fd83b061c869d79e8875b31",
      "action": "TEST_FROZEN_PROPAGATION_SPHERE_RESULTS",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R033 task-scoped report, exact generated atlases, experiment and focused tests at frozen owner head",
    "R034 task-scoped report, exact generated atlases, experiment and focused tests at frozen owner head",
    "Driver audit boundary: R034 generic Barlow covariance is accepted as exact research evidence while NN Barlow all-stacking return/local-DOS gauge universality remains a strong theorem candidate pending a harder independent proof"
  ],
  "evidence_status": "INDEPENDENT_REPLICATION_AND_EVIDENCE_GRADE_GATE",
  "last_progress_ref": "User requested a separate algorithm/data replication task before further foundational interpretation of FCC/HCP exactness and pi as a possible continuum readout.",
  "last_progress_at": "2026-08-12T13:17:00+08:00",
  "hard_block": null,
  "tags": [
    "R037",
    "replication",
    "audit",
    "fcc",
    "hcp",
    "barlow",
    "graph-ball",
    "random-walk",
    "spectral",
    "exact-data",
    "evidence-grade"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R037",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R037 — R033/R034 Independent Algorithm and Data Replication Audit

Status: `READY / P0 / INDEPENDENT REPLICATION / NO THEORY ADVANCE / NOT CANONICAL`

## 0. 任务边界

本任务只有一个目的：

> **独立复核 R033/R034 的算法、数据、公式和 evidence grade，决定哪些结论真正可重复。**

本任务不是继续提出新的球、π、连续极限或物理解释，也不是替 R033/R034 辩护。

必须把冻结结果视为待审计 claim，而不是正确答案。

禁止把 R033/R034 的实验脚本直接作为复算引擎。允许在独立实现完成后读取其输出做逐项 diff。

优先采用不同表示方式、不同枚举逻辑或独立符号推导，避免“复制同一个 bug 得到相同结果”。

---

## 1. 任务内状态机

本任务使用以下明确 semantic gate；claim 身份解析继承仓库现行身份规则，不在 taskbook 固定 Researcher-ID。

`READY`
→ taskbook 可领取；尚无执行者绑定。

`CLAIMED`
→ 已绑定本次执行身份；只允许读取冻结输入和建立独立复核计划，尚不得宣告任何 claim PASS。

`IN_PROGRESS / MODEL_REBUILT`
→ FCC/HCP/Barlow 的独立坐标、邻接、物理 embedding 与 exact arithmetic 模型已从定义重建；至少一个 sanity domain 已与冻结模型交叉检查。

`IN_PROGRESS / CLAIM_MATRIX_RUNNING`
→ 按本任务 §3–§8 对每条 claim 独立推导、复算和压力测试；每条 claim 必须记录 evidence grade。

`HANDOFF_READY`
→ 若会话结束但尚有 claim 未审计，必须留下已完成 claim matrix、失败点和唯一 next_action；不得用“整体看来没问题”代替逐项状态。

`SEMANTIC_CHECKPOINT`
→ §3–§8 全部完成，所有 theorem-critical 数值至少有一个独立生成路径，所有 mismatch 已最小化为可复现 witness。

`DONE / RETURNED`
→ 返回最终 replication report；明确区分 `REPRODUCED_EXACT`、`REPRODUCED_FINITE_CERTIFICATE`、`REPRODUCED_ASYMPTOTIC_CERTIFICATE`、`THEOREM_CANDIDATE_ONLY`、`FAILED_OR_MISMATCH`。

任何 `FAILED_OR_MISMATCH` 都是有效完成结果，不得为了与冻结输出一致修改独立实现。

---

## 2. 独立性要求

至少满足：

1. graph enumeration 与 distance formula 不能互相循环验证；必须有一条 BFS/DP reference path 和一条 closed-form/structural path；
2. R034 path probability 使用 integer path counts，概率仅作为后置除法；
3. moment/tensor 复核使用 exact rational/algebraic arithmetic；
4. spectral expansion 至少有一条与冻结脚本不同的 symbolic derivation；
5. macro `10^36` 结果只由已复核 closed form 直接求值，不做巨量枚举；
6. 所有“等于”与“渐近”等级分开记录。

---

## 3. R033 growth / graph-ball audit

独立复核：

### FCC

- `D3` 12-neighbor graph degree/reciprocity；
- exact graph distance；
- `A_r = 10 r^2 + 2`；
- `V_r = (10 r^3 + 15 r^2 + 11 r + 3)/3`；
- 至少 `r=0..20` exhaustive reference；
- 至少一个未用于拟合的 `r>=100` holdout。

### HCP

- A/B layer adjacency 与 degree/reciprocity；
- A/B origin equivalence；
- exact distance formula；
- `A_r = floor(21 r^2/2)+2`；
- period-2 bulk formula；
- `r=0..20` exhaustive reference 与 `r>=100` holdout。

必须验证：

- rooted induced graph 第一次不可同构差异是否确在 `r=1`；
- shell count 第一次差异是否确在 `r=2`；
- leading FCC/HCP shell/bulk coefficient ratio 是否精确为 `21/20`。

---

## 4. R033 boundary / topology / limit-shape audit

独立复核：

- FCC stable boundary symmetry-orbit alphabet 与 exact population formulas；
- HCP stable period-2 boundary alphabet 与 exact population formulas；
- limiting frequencies 与 TV remainder bounds；
- FCC/HCP exposed-face orientation proportions；
- shell、exposed-cell boundary、exposed-face complex 三者没有被混用；
- common exposed-face count candidate
  `F_boundary(r)=12(3r^2+3r+1)`；
- exact rational boundary complex 在冻结 reference range 的 `V,E,F,chi`、connectedness、edge incidence、vertex link；
- all-radius `S^2` 仍只能保留为未完成证明，除非本审计任务独立给出真正证明；若意外完成，作为附加结果单列，不改变审计主线。

独立复核 limit shapes：

- FCC cuboctahedral graph-distance ball；
- HCP 18-vertex stable velocity polytope；
- 两者 anisotropy ratios；
- HCP finite-radius support bound。

---

## 5. R033 intrinsic scalar / macro audit

复核：

`K_r=A_r^3/V_r^2`

是否满足：

- FCC `K_inf=90`；
- HCP `K_inf=189/2`；
- 已报告 `O(1/r)` remainder bounds；
- `10^36`, `10^37`, `10^38` 宏观误差量级。

另外必须独立审计一个新但简单的后置 readout 推论：

若仅把 graph radius `r` 临时塞入欧氏形式

`A=4*pi_eff*r^2`, `V=(4/3)*pi_eff*r^3`,

则 shell-leading 与 bulk-leading 两个通道是否都给出：

- FCC `pi_eff -> 5/2`；
- HCP `pi_eff -> 21/8`。

必须明确标记这些只是 **EUCLIDEAN_FORM_READOUT_CONSTANTS**，不能写成 `pi=5/2` 或 `pi=21/8`，并检查改用不同 radius calibration 后常数是否变化。

---

## 6. R034 local / finite-time propagation audit

最近邻物理长度归一为 1 后，独立重建 FCC/HCP-A/HCP-B 的 12 个 physical step vectors。

复核：

- exact zero conditional drift；
- exact local covariance `I/3`；
- generic ideal Barlow local outer-product certificate；
- exact recurrence `E[X_n X_n^T]=n I/3`；
- `E|X_n|^2=n`。

不得从二阶矩推出 finite-time spherical distribution。

独立 path-count enumeration 至少覆盖：

- 完整 `n=0,1,2`；
- compact summaries 至少到 `n=12`；
- `n=2` FCC support `55` / HCP support `57` 与 path-count multiset witness；
- return counts reference；
- same-radius nonuniformity witness。

---

## 7. R034 memory-order / moment audit

独立复核：

- FCC one-step cubic tensor 为 0；
- HCP-A cubic harmonic
  `sqrt(3)/72 * y*(3*x^2-y^2)`；
- HCP-B 反号；
- rooted local first memory order `3`；
- full fourth-order tensor差异；
- scalar radial fourth moment
  `E|X_n|^4=(5n^2-2n)/3` 是否精确共通；
- FCC/HCP sixth radial formulas；
- 差值
  `E_H|X_n|^6-E_F|X_n|^6=-(n-1)/54`；
- scalar radial first memory order `6`。

所有 closed form 必须以独立 recurrence / symbolic derivation 加有限 enumeration 双重检查，而不是只做拟合。

---

## 8. R034 spectral / Barlow audit

独立构造：

- FCC Fourier transition symbol；
- HCP 2x2 Bloch fiber；
- principal band small-k expansion。

复核：

- common quadratic term `-|k|^2/6`；
- FCC/HCP quartic log terms；
- principal spectral first memory order `4`；
- diffusive scaling 下 quartic angular correction 为 `O(1/n)`；
- `10^36` small-k certificate 的数量级，且不得升级成 global uniform heat-kernel bound。

### Barlow return/local-DOS claim 的特殊证据等级

冻结状态不是 theorem。

必须独立审计 layer-gauge argument：

1. basal Fourier 后 reduced layer operator 的 exact hopping amplitude；
2. stacking dependence 是否真的只进入 removable edge phases；
3. bi-infinite layer graph 是否无 gauge-invariant cycle flux；
4. root gauge 是否保持 root local spectral measure；
5. integrated DOS 推论需要什么周期/非周期定义与假设。

只有给出完整 algebraic/operator proof 或等价的独立 theorem checker，才能升级为 `REPRODUCED_EXACT`。

否则即使 FCC/HCP return counts 枚举到很大 `n` 仍保持：

`THEOREM_CANDIDATE_ONLY`。

---

## 9. Evidence matrix

最终必须逐条输出机器可读 + human-readable matrix，至少包含：

- claim_id；
- frozen_claim；
- independent_method；
- exact_domain；
- holdout_domain；
- result；
- evidence_grade；
- minimal_counterexample（如有）；
- source/provenance boundary。

Evidence grade 只能从：

- `REPRODUCED_EXACT`；
- `REPRODUCED_FINITE_CERTIFICATE`；
- `REPRODUCED_ASYMPTOTIC_CERTIFICATE`；
- `THEOREM_CANDIDATE_ONLY`；
- `FAILED_OR_MISMATCH`。

不得使用模糊的 `looks correct`。

---

## 10. 必须返回

至少形成：

- independent replication runner；
- focused independent tests；
- R033 replication atlas；
- R034 replication atlas；
- spectral/moment derivation certificate；
- macro/readout audit；
- full evidence matrix；
- mismatch report（允许为空，但必须存在）；
- final replication report。

最终 verdict 应直接回答：

> **R033/R034 中哪些 exact 核心可独立复现，哪些只是有限证书/渐近证书，哪些仍是 theorem candidate，是否存在会改变后续“离散 exact world / π readout”研究方向的错误。**
