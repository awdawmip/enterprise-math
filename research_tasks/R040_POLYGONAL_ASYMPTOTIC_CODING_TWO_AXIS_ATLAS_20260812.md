<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R040-POLYGONAL-ASYMPTOTIC-CODING-TWO-AXIS-ATLAS",
  "title": "R040 Polygonal Refinement Asymptotic Coding: Branch Geometry, Arithmetic Phase, and Limit Support",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_DYNAMICS_ATLAS",
  "frontier": "Consume the provenance-preserved union of the R035 project and isolated arms and determine whether polygonal endpoint dynamics really decomposes into a branch-overlap geometry axis and an arithmetic-coding axis, or whether those apparent axes are coupled/redundant; classify the square and nonsquare asymptotic coding, exact-hit defects, support growth, and normalized limit geometry without assuming a phase diagram in advance.",
  "next_action": "Derive the exact real-inverse asymptotics from the discriminant coordinate, sharpen the square-refinement affine theorem, attack nonsquare increment coding against mechanical/Beatty/continued-fraction models, relate exact-hit Pell structure to coding defects, and determine which support-growth/limit-shape statements survive for separated versus recoalescing regimes.",
  "dependencies": [
    {
      "target": "R035 paired-arm selected findings",
      "action": "CONSUME_PROVENANCE_PRESERVED_PROJECT_AND_ISOLATED_THEOREM_UNION_FROM_RESEARCH_INPUT_MEMO",
      "satisfied": true
    },
    {
      "target": "R035 project arm owner head a0aa4a91f8302feeb6e41fa94175e26a3f0a3f71",
      "action": "CONSUME_PROJECT_ARM_GLOBAL_CARRIER_RECOALESCENCE_AND_R4_BOUNDARIES",
      "satisfied": true
    },
    {
      "target": "R035 isolated arm return sha256 2cda7c60dfb38fb27033138c9d0036a578d5eb5ede0e681b1a85d96bd58cd0fc",
      "action": "CONSUME_ISOLATED_SQUARE_REFINEMENT_AFFINE_DIGIT_RESULTS_WITH_SOURCE_PROVENANCE_PRESERVED",
      "satisfied": true
    }
  ],
  "source_refs": [
    "research_inputs/R035_PAIRED_ARM_SELECTED_FINDINGS_20260812.md",
    "R035 project arm report/code at owner head a0aa4a91f8302feeb6e41fa94175e26a3f0a3f71",
    "R035 isolated arm return ZIP sha256 2cda7c60dfb38fb27033138c9d0036a578d5eb5ede0e681b1a85d96bd58cd0fc",
    "Chahal-Griffin-Priddis arXiv:1806.07981 only for already-rooted fixed-multiple polygonal/Pell prior art; broader coding/limit-set prior art must be independently rooted if used"
  ],
  "evidence_status": "PAIRED_ARM_THEOREM_UNION_TO_ASYMPTOTIC_CODING_GATE",
  "last_progress_ref": "R035 paired experiment found a strong common intrinsic core plus complementary project-only global carrier laws and isolated-only square-refinement digit geometry; Driver identified a possible but unproved branch-geometry x arithmetic-coding decomposition.",
  "last_progress_at": "2026-08-12T15:00:00+08:00",
  "hard_block": null,
  "tags": [
    "R040",
    "polygonal-numbers",
    "endpoint-dynamics",
    "asymptotic-coding",
    "beatty",
    "continued-fractions",
    "pell",
    "digit-sets",
    "limit-support",
    "recoalescence",
    "paired-arm-synthesis"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R040",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R040 — Polygonal Refinement Asymptotic Coding: Branch Geometry, Arithmetic Phase, and Limit Support

Status: `READY / P0 / FOUNDATIONAL DYNAMICS ATLAS / NOT CANONICAL`

## 0. 母问题

R035 的项目臂与隔离臂在同一 polygonal endpoint dynamics 上独立得到共同主干，同时各自长出了不同的 exact theorem family。

把这些结果放在一起后，出现一个很自然、但目前完全不能预设为真的候选：

\[
\text{support / parent-overlap geometry}
\quad\times\quad
\text{arithmetic coding type}.
\]

直觉上，前者似乎与 `sqrt(r)` 相对 `2` 的位置有关，后者似乎与 `sqrt(r)` 是否为整数、以及 exact-hit Pell arithmetic 有关。

R040 的目标不是证明这个二维图景，而是回答：

> 这两个候选坐标究竟是真正独立的结构轴、只有局部有效的坐标、还是同一个更深对象的两个投影？

如果二轴图景失败，优先冻结最小耦合反例和更好的替代坐标。

本任务的 paired input 是肩膀，不是研究方法。不得因为输入 memo 使用了某个组织方式，就把后续结论强行写成同一 taxonomy。

---

## 1. 冻结输入与 provenance

首先读取：

`research_inputs/R035_PAIRED_ARM_SELECTED_FINDINGS_20260812.md`

必须永久区分：

- `R035_PROJECT_ARM`；
- `R035_ISOLATED_ARM`；
- `R040_NEW`；
- `PRIOR_ART`。

R040 可以重新证明输入 theorem，但不得把 isolated-arm-only 发现重写成 project-arm provenance。

冻结的共同核心包括：

- exact discriminant coordinate；
- `r=4` critical structure；
- universal singleton-root interval iff `r<=4`；
- exact `r=4` child formulas；
- generalized Pell exact-hit surface。

冻结的 project-only 输入包括：

- ordered lower-map / local collision law；
- no-recoalescence iff `r=1` or `r>=4`；
- exact finite-support loss accounting；
- global interval/separated carrier laws；
- no nontrivial finite positive periodic supports for `r>1`。

冻结的 isolated-only 输入包括：

- `r=q^2,s!=4` 的 eventual affine two-child theorem；
- stable base-`q` `{0,1}` digit support；
- `q=2` interval versus `q>=3` sparse digit geometry；
- `s=4` rounded-dilation specialization；
- fixed `r>=5` 的 high-index separation interpretation。

---

## 2. Exact coordinate and real inverse

写

\[
a=s-2,\qquad c=s-4,
\]

\[
P_s(k)=\frac{ak^2-ck}{2},
\qquad
z_k=2ak-c.
\]

则

\[
z_k^2=c^2+8aP_s(k).
\]

对正 parent，定义 exact real inverse

\[
\Phi_{s,r}(k)
=
\frac{c+\sqrt{r z_k^2+(1-r)c^2}}{2a},
\]

并有

\[
F_{s,r}(k)=\lfloor \Phi_{s,r}(k)\rfloor.
\]

必须从这个 exact formula 独立推导大 `k` 展开，不允许把浮点拟合当成结构来源。

至少明确：

- leading slope；
- constant offset；
- first nonzero inverse-power correction；
- correction 在 `r` square / nonsquare、`s=3,4,>4` 时如何改变；
- 哪些 floor/ceil 决策可能被 subleading correction 改写。

---

## 3. Lower-jump coding

定义

\[
d_k=F_{s,r}(k+1)-F_{s,r}(k).
\]

R035 已知它 eventually 落在 `sqrt(r)` 附近的相邻整数中，但尚未分类完整 word structure。

R040 必须研究：

1. `r=q^2` 时，`d_k` 是否在所有非退化 family 中最终常数化？精确阈值是什么？
2. nonsquare `r` 时，`d_k` 是否能由某个 mechanical / Beatty / Sturmian 型 word 精确或近精确描述？
3. 如果存在自然 baseline mechanical word，定义并枚举真正的 defect set；判断 defect 是有限、无限、零密度、正密度还是依赖 `(s,r)`；
4. 如果 Beatty/Sturmian 语言并不合适，必须主动 kill，而不是通过改名保留类比。

重点不是套现成 symbolic-dynamics 名称，而是找最小 exact state/coordinate，使 `d_k` 的未来尽可能可预测。

---

## 4. Square refinement branch — sharpen the isolated theorem

对 `r=q^2`：

### 4.1 `s!=4`

重新推导 isolated arm 的 eventual affine law

\[
E_s(q^2P_s(k))=\{qk+c_0,qk+c_0+1\}
\]

在稳定区成立的精确条件。

必须进一步攻击：

- offset `c_0` 的 closed form；
- 最小稳定阈值 `K(s,q)` 或严格上/下界；
- stable region 是否对任意 finite support 一旦进入就保持 forward-invariant；
- exact-hit parent 是否真的只有有限个，以及例外集合如何显式描述；
- stable support 是否总可写成 affine shift + digit set。

### 4.2 normalized digit geometry

从 exact digit formula 出发研究

\[
q^{-t}(S_t-\text{appropriate affine center/shift}).
\]

对 `q=2`、`q>=3` 分别确定：

- finite-time exact set；
- Hausdorff/box-counting/covering-type limit candidate（如定义合理）；
- `log 2 / log q` 是否真是 intrinsic support-dimension quantity，还是只对特定 normalization/starting regime 有意义；
- exact-hit finite prefix 是否只改变有限前缀，还是会影响 limit object 的某些离散不变量。

不得先称其为 Cantor set；先给 exact set/limit 定义，再判断经典对象是否适用。

---

## 5. Nonsquare refinement branch

对 integer `r` 非平方，`alpha=sqrt(r)` 为二次无理数。

必须实际攻击：

- `F(k)` 的 floor coding 与 `alpha k + beta` 的关系；
- continued fraction convergents 是否控制 floor decision 的 exceptional indices；
- exact-hit generalized Pell solutions与这些 exceptional/defect indices 是否共享同一 Diophantine skeleton；
- 若两者并不同源，给出最小反例并保持类型分离；
- 对 `r>=5` 的 separated-parent regime，support 是否有一个 beta-expansion / two-map rounded-affine description；
- 对 `r=2,3` 的 overlap regime，同样的 arithmetic coding 在 recoalescence 后还保留多少可观察结构。

优先 exact integer/rational/quadratic-field 实现。continued-fraction 数据可用于生成候选，但 theorem statement 必须明确证据等级。

---

## 6. Exact-hit process as a dynamical defect

定义 exact-hit set

\[
\mathcal H_{s,r}=\{k\ge0:rP_s(k)\in P_s(\mathbb N)\}.
\]

R040 不只把它当 Pell side problem，而要研究它在 support dynamics 中的作用。

至少回答：

- `r` square / nonsquare 时 `\mathcal H_{s,r}` 的有限/无限行为；
- exact-hit indices 的 asymptotic sparsity / recurrence；
- 在 `r>=4` distinct-parent separation 下，
  \[
  |S_{t+1}|=2|S_t|-H_t
  \]
  中的 `H_t` 能否形成 closed recursion、density law 或严格 growth bounds；
- 是否存在起点使 branch 无限次命中 exact-hit set；
- finite exact-hit prefix 与 infinite Pell-hit subsequence 对 normalized support 的影响是否本质不同。

---

## 7. Test the alleged two-axis decomposition

建立 machine-readable matrix，但不要预先给 cell 命名。

至少覆盖：

- `r=1`；
- `r=2,3`；
- `r=4`；
- square `r=q^2>=9`；
- nonsquare `r>=5`；
- `s=3`、`s=4`、多个 `s>4`。

对每个 cell 分开记录：

- parent overlap/recoalescence；
- lower-jump word；
- exact-hit behavior；
- support interval/gap/digit geometry；
- cardinality growth；
- normalized support candidate；
- smallest known sufficient state/coordinate。

然后明确判定：

### Outcome A — genuine factorization

两个轴在清楚意义下可独立组合，并且主要 observables 可由二者的 product data 重建。

### Outcome B — coupled atlas

存在不可消去的 coupling invariant；给出最小 coupling witness 和 replacement coordinate。

### Outcome C — wrong ontology

二轴语言本身误导；给出更小或更自然的统一对象。

三种结果都视为成功。

---

## 8. Exact executable laboratory

优先建立：

`experiments/r040_polygonal_asymptotic_coding.py`

至少支持：

- exact `P_s,L_s,E_s,F_s,r`；
- exact quadratic/discriminant coordinate；
- exact lower-jump sequence；
- exact-hit detector；
- support iteration and parent incidence；
- square affine-law detector / threshold finder；
- nonsquare continued-fraction candidate diagnostics；
- mechanical-word comparator and defect extractor；
- normalized support snapshots；
- exact cardinality loss decomposition。

建立独立 holdout oracle，避免 discovery path 与 validation path 完全共用同一反演实现。

建议先 exhaustive 小域，再对大 `k` 做 exact sampled holdout；不能以大样本替代 proof。

---

## 9. 必须主动杀的过强说法

至少攻击以下说法，不得默认接受：

- `sqrt(r)>=2` alone 决定全部 dynamics；
- `sqrt(r)` 是否整数 alone 决定全部 dynamics；
- branch geometry 与 arithmetic coding 必然独立；
- nonsquare coding 必然 Sturmian；
- Pell exact hits 必然就是 mechanical-word defects；
- square refinement 的 normalized support 必然是标准 Cantor object；
- exact-hit density alone 决定 support growth；
- isolated-arm theorem 是 project-arm theorem 的简单 corollary；
- 一次 paired experiment 已证明项目环境无 anchoring。

对被杀说法，保存最小反例和 surviving weaker structure。

---

## 10. Prior-art rooting

在内部 exact structure 稳定后，系统 rooting：

- polygonal-number multiple equations / generalized Pell equations；
- Beatty sequences / mechanical words / Sturmian words；
- quadratic irrational continued fractions；
- beta-expansions / Bernoulli convolutions / digit IFS（仅在数学对象确实匹配时）；
- symbolic dynamics of rounded affine maps；
- discrete self-similar / automatic / substitutive sets。

不能因为相邻 prior art 存在就抹掉 task-specific exact carrier / coding interface；也不能仅靠换术语主张新颖性。

---

## 11. 交付

至少返回：

1. `docs/R040_POLYGONAL_ASYMPTOTIC_CODING_REPORT.md`；
2. exact research executable；
3. focused tests + independent holdout；
4. `R040_TWO_AXIS_DISPOSITION.json`；
5. `R040_CODING_ATLAS.json`；
6. `R040_EXACT_HIT_ATLAS.json`；
7. `R040_LIMIT_SUPPORT_ATLAS.json`；
8. `R040_PROVENANCE_MATRIX.json`，逐项标明 `PROJECT_ARM / ISOLATED_ARM / R040_NEW / PRIOR_ART`；
9. killed/narrowed claim matrix；
10. unresolved frontier list。

如果一个全局统一 theorem 不存在，不要为了闭环制造它。高质量的 coupled counterexample atlas 或多个互不化约的 exact branches 同样是完整成功返回。

---

## 12. 推荐返回分类

若二轴分解真正成立：

`POLYGONAL_TWO_AXIS_DYNAMICS_ATLAS_FOUND / BRANCH_AND_ARITHMETIC_COORDINATES_CLASSIFIED / LIMIT_SUPPORT_REGIMES_FROZEN / NOT_CANONICAL`

若存在关键耦合：

`POLYGONAL_TWO_AXIS_INDEPENDENCE_KILLED / COUPLING_INVARIANT_FOUND / ASYMPTOTIC_CODING_ATLAS_FROZEN / NOT_CANONICAL`

若更好的单一对象取代二轴：

`POLYGONAL_TWO_AXIS_ONTOLOGY_REPLACED / SMALLER_UNIFIED_CODING_OBJECT_FOUND / NOT_CANONICAL`
