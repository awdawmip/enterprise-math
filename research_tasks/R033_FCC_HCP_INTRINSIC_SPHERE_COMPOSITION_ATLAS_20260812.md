<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R033-FCC-HCP-INTRINSIC-SPHERE-COMPOSITION-ATLAS",
  "title": "R033 FCC/HCP Intrinsic Sphere Composition Atlas",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_GEOMETRY",
  "frontier": "Determine what a sphere is intrinsically in FCC and HCP cell worlds when the only primitive data are cells, local adjacency, and shell growth; derive the bulk, shell, boundary-type, anisotropy, and topology laws before any continuous-sphere or collapse interpretation is imposed.",
  "next_action": "Build exact combinatorial FCC/HCP cell models, enumerate intrinsic graph balls and boundary complexes at small and medium radii, infer and certify exact or eventual growth laws and boundary-type spectra, characterize the rescaled large-radius shape, then evaluate the certified laws at radii 10^36, 10^37, and 10^38 to test whether the macroscopic composition has already stabilized.",
  "dependencies": [
    {
      "target": "R031 owner head a2836ba25133f8c7ca0eb24e19f435cc97f137ee",
      "action": "CONSUME_ONLY_THE_SCALE_LESSON_THAT_10^36_IS_ALREADY_A_MACROSCOPIC_REGIME_AND_DO_NOT_IMPORT_PI_OR_COLLAPSE_AS_THE_SPHERE_DEFINITION",
      "satisfied": true
    },
    {
      "target": "P012 graph-distance common surface",
      "action": "USE_GRAPH_DISTANCE_AS_THE_PRIMARY_INTRINSIC_RADIUS_CONCEPT_WHERE_THE_DECLARED_CELL_GRAPH_SATISFIES_ITS_PRECONDITIONS",
      "satisfied": true
    }
  ],
  "source_refs": [
    "User correction on 2026-08-12: the next question is not how a sphere collapses but what a sphere is composed of in an FCC/HCP cell world",
    "FCC nearest-neighbor/contact graph and its rhombic-dodecahedral Voronoi cell",
    "HCP nearest-neighbor/contact graph and its ideal close-packed ABAB stacking",
    "R031 large-scale lesson: once exact asymptotic laws are known, 10^36 through 10^38 should be treated as macro-regime evaluation rather than brute-force scale escalation",
    "P012 graph-distance tooling as a reusable metric primitive"
  ],
  "evidence_status": "INTRINSIC_CELLULAR_SPHERE_COMPOSITION_GATE",
  "last_progress_ref": "User reframed the FCC/HCP direction from surface-cut collapse to the more foundational question of how a sphere is intrinsically composed; Driver identified graph balls, shell spectra, boundary cell types, anisotropy, topology, and emergent constants as the direct observables.",
  "last_progress_at": "2026-08-12T10:55:00+08:00",
  "hard_block": null,
  "tags": [
    "R033",
    "fcc",
    "hcp",
    "intrinsic-sphere",
    "cell-composition",
    "graph-ball",
    "shell-growth",
    "boundary-spectrum",
    "anisotropy",
    "emergent-geometry"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R033",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R033 — FCC/HCP Intrinsic Sphere Composition Atlas

Status: `READY / P0 / FOUNDATIONAL GEOMETRY / INTRINSIC CELLULAR SPHERE / NOT CANONICAL`

## 0. 任务定位

本任务不研究：

- 一个预先给定的连续球如何切割 FCC/HCP 胞元；
- DOWN / UP / NEAREST 应当如何处理被切胞；
- 如何让离散结果尽量逼近 `4*pi*r^2` 或 `(4/3)*pi*r^3`；
- 如何把已经丢失的连续细节重新保存起来。

本任务研究更基础的问题：

> 如果空间的原始对象只有 FCC 或 HCP 胞元以及局部邻接关系，那么“球”本身是什么？它由多少层、多少胞、哪些边界胞类型、怎样的缺陷与方向结构组成？这些组成规律在大尺度是否稳定？

连续欧氏球只允许在内禀对象和规律冻结后作为次级比较坐标，不能作为生成器、目标函数或真值裁判。

本任务如果成功，应把研究顺序固定为：

`cell world -> local adjacency -> intrinsic ball -> shell/boundary composition -> macroscopic geometry -> optional continuous comparison -> later observation/collapse`

而不是反过来。

---

## 1. 冻结的两个胞元世界

必须实现两个相互独立的 exact combinatorial model。

### 1.1 FCC

优先采用整数坐标实现 FCC site/contact graph，例如：

- 顶点为满足适当 parity 约束的整数三元组；
- 12 个最近邻由 `(±1,±1,0)` 的坐标排列给出；
- 所有邻接与 graph distance 使用整数运算。

若采用等价坐标系，必须给出与标准 FCC 最近邻图的显式同构或双向映射。

胞元解释：每个 site 对应一个 Voronoi cell；共享 Voronoi 面等价于最近邻接。

### 1.2 HCP

必须给出无浮点歧义的 ABAB close-packed combinatorial model。

推荐：

- 每一层是 triangular lattice；
- 层类型为 A/B；
- 同层有 6 个邻居；
- 每个 site 与上层 3 个、下层 3 个 site 邻接；
- 总度数为 12。

必须显式写出 A/B 层的整数/有理坐标或纯组合 neighbor rule，并检查：

- degree = 12；
- 邻接对称；
- 周期结构正确；
- A/B 基点若在抽象图上等价，则给出证据；若不等价，分别保留 origin class。

不要因为 FCC/HCP 都是 close packing 就预设它们的 intrinsic ball 相同。

---

## 2. 第一原理定义：内禀球与壳层

固定中心胞 `c0`。

定义 graph distance：

`d(c0,c) = 最少最近邻步数`。

定义：

\[
B_r=\{c:d(c_0,c)\le r\},
\]

\[
S_r=B_r\setminus B_{r-1}.
\]

这里：

- `B_r` 是内禀 ball；
- `S_r` 是内禀 shell / sphere layer；
- 不使用 `x^2+y^2+z^2<=R^2` 来决定成员；
- 不存在“部分属于 B_r 的胞”：成员关系首先是离散的。

必须首先研究：

\[
V_r=|B_r|,
\qquad
A_r=|S_r|.
\]

“体积”和“表面”在本任务的第一层语义分别是 bulk cell count 和 shell cell count。

---

## 3. 小域 exact enumeration

分别对 FCC/HCP 至少完成：

- `r=0..20` exact reference；
- 若资源允许，扩展到 `r=100` 或更高；
- 每个 `B_r` 与 `S_r` 必须可重复生成；
- 检查由 BFS、显式 distance formula（若发现）、shell recurrence 三条路径的一致性。

每个 r 至少记录：

- `V_r=|B_r|`；
- `A_r=|S_r|`；
- `ΔA_r`、`Δ²A_r`；
- `ΔV_r`、`Δ²V_r`、`Δ³V_r`；
- shell induced-edge count；
- ball-to-outside boundary edge count；
- 每个 shell cell 的 inside-neighbor count / outside-neighbor count；
- boundary local type orbit；
- origin/basis class；
- HCP layer parity / stacking phase（如仍可见）。

目标不是只拟合一个多项式，而是发现精确组合结构。

---

## 4. 边界胞类型谱

对 `c in S_r`，定义它相对于 `B_r` 的局部邻接图样：

\[
\tau_r(c)=
\{\text{12 个邻接方向中哪些指向 }B_r,\text{哪些指向外部}\}.
\]

至少构造三层分类：

1. **count type**：只看 inside degree / outside degree；
2. **directional type**：保留缺失邻居方向；
3. **symmetry-orbit type**：在 FCC/HCP 各自 point/graph symmetry 下把等价 directional patterns 归并。

定义：

\[
N_\tau(r)=\#\{c\in S_r:\tau_r(c)=\tau\}.
\]

必须检查：

\[
\sum_\tau N_\tau(r)=A_r.
\]

并研究：

\[
p_\tau(r)=\frac{N_\tau(r)}{A_r}.
\]

母问题之一是：

> 是否存在有限或最终周期的边界类型集合，使每个 `N_tau(r)` 都具有 exact polynomial / quasi-polynomial / linear recurrence 结构？

如果存在，优先寻找证明或可检验 certificate，而不是停留在 regression。

---

## 5. 球的拓扑是否真的像球

不能因为名字叫 `B_r` 就预设几何边界是 2-sphere。

若使用 Voronoi cell complex 的组合粘合，必须在可行半径上构造 union boundary complex，并检查：

- connectedness；
- Euler characteristic；
- orientability（可行时）；
- vertex/edge/face incidence；
- 是否出现洞、handle、自交式组合异常；
- 从哪个最小 r 开始（如果存在）边界稳定为拓扑 `S^2`。

如果 graph shell `S_r` 与 Voronoi-union boundary 不是同一个对象，必须严格区分：

- graph shell；
- exposed-cell boundary；
- exposed-face complex。

这三个量不得混写成一个“表面积”。

---

## 6. 增长律与精确外推

优先攻击以下候选：

### H1 — FCC shell polynomial

FCC `A_r` 可能从小 r 起就是 exact quadratic，`V_r` 是 exact cubic。

不得从已知 coordination sequence 直接抄结论；先独立枚举，再 prior-art root，再给出 project-side proof/certificate 或至少 exact identity verification。

### H2 — HCP eventual quasi-polynomial

由于 ABAB stacking，HCP `A_r` / `V_r` 可能是 polynomial 或小周期 quasi-polynomial。

必须搜索最小 period，而不是先假定 period = 2。

### H3 — finite-difference closure

若 `Δ²A_r` 或 `Δ³V_r` 最终周期稳定，提取最小 recurrence / quasi-polynomial。

### H4 — boundary-type quasi-polynomiality

每个主要 `N_tau(r)` 是否也是 degree-2 polynomial/quasi-polynomial？

### H5 — composition-frequency limit

对主要 boundary types，是否存在：

\[
p_\tau(r)\to p_\tau^*?
\]

若存在，求 exact rational/algebraic candidate 或严格数值区间。

### H6 — macro correction scale

如果：

\[
V_r=a_3r^3+a_2r^2+O(r),
\qquad
A_r=b_2r^2+b_1r+O(1),
\]

则归一化宏观组成的有限尺度修正应主要为 `O(1/r)`。

必须据此定量判断 `r=10^36` 是否已经“足够宏观”，而不是凭尺度直觉。

---

## 7. 内禀球的极限形状

这是本任务的关键杀伤项。

graph metric ball 不一定趋向欧氏球。

必须在冻结 combinatorial ball 后，才调用一个 exact 或高精度的标准 FCC/HCP embedding 作为诊断坐标，研究：

\[
\frac{1}{r}B_r
\]

的大尺度支撑函数/方向半径。

至少测：

- 高对称方向的 `R_r(u)/r`；
- 最大/最小方向比；
- directional spread；
- convex-hull facet normals（可行时）；
- FCC 与 HCP 的差异。

候选：

### H7 — Euclidean isotropy

`R_r(u)/r` 对所有方向趋于同一常数。

若反例稳定出现，立即杀掉，不得把各向异性称为“离散误差”。

### H8 — stable polyhedral/Wulff limit

若不是欧氏球，是否趋向一个稳定 convex polyhedral/stable-norm shape？

如果是，这个形状就是该 adjacency world 的自然 metric ball，应作为正结果返回。

### H9 — FCC/HCP macroscopic universality

FCC/HCP 的 rescaled intrinsic balls 是否具有同一极限形状或同一 boundary composition spectrum？

允许三种结果：

- 完全同一；
- bulk 同一但 boundary spectrum 不同；
- 连极限 shape 都不同。

不得预设 close packing 会抹掉 stacking 信息。

---

## 8. 纯组合“形状常数”

不要先输入 pi。

至少研究以下无量纲组合：

\[
K_r=\frac{A_r^3}{V_r^2}.
\]

如果存在：

\[
K_\infty=\lim_{r\to\infty}K_r,
\]

返回 FCC/HCP 各自的 exact/asymptotic candidate。

还应寻找：

- exposed-boundary-edge / `A_r` limit；
- shell-induced-edge / `A_r` limit；
- boundary-type entropy；
- principal orientation proportions；
- 任何从局部组成自然产生且跨尺度稳定的无量纲量。

只有在这些 intrinsic constants 冻结后，才允许作为诊断问：

> 某个组合是否与连续球的 `36*pi` 等常数巧合或渐近相关？

不能为了得到 pi 调整定义。

---

## 9. `10^36`–`10^38` 宏观区验证

禁止枚举 `10^36` 半径的所有胞。

必须先得到 exact law / recurrence / asymptotic certificate，然后用大整数直接评估：

\[
r=10^{36},10^{37},10^{38}.
\]

至少输出：

- `V_r` exact integer；
- `A_r` exact integer；
- 主要 `N_tau(r)` exact integer（若已得公式）；
- `p_tau(r)` exact rational 或严格区间；
- `K_r` exact rational；
- leading/subleading term ratio；
- FCC/HCP 相对差异；
- 若有 period，三尺度分别处于什么 residue class。

定义“这个尺度已经够了”时，不能只说数很大。

必须给出类似：

\[
|Q(r)-Q_\infty|\le C/r
\]

或相应 exact remainder bound，并据此说明在 `10^36` 到 `10^38` 上稳定了多少数量级。

---

## 10. 与“坍缩”的关系只做后置结论

本任务不选择 DOWN/UP。

完成 intrinsic sphere composition 后，只允许回答：

1. graph ball 本身是否已经没有 cut-cell ambiguity；
2. 若宏观观察者把整个 `B_r` 压成一个标量半径/面积/体积，哪些信息才是在这一步被丢弃；
3. boundary spectrum 是否自然诱导某种宏观 coarse observable；
4. 过去所谓“坍缩方向”是否只是从完整 cellular sphere 到低维 observable 的后置读取规则。

若最后发现：

> sphere composition 已经决定了宏观量，而不需要任何额外 directional collapse，

这是强正结果。

若发现：

> 同一 `B_r` 映射成标量时仍存在不可约的多种 coarse readout，

也作为正结果返回，不提前裁决。

---

## 11. Prior-art rooting

必须在独立发现后系统检查：

- FCC coordination sequences / lattice growth series；
- HCP coordination sequences；
- word metrics on periodic graphs；
- growth functions of abelian/crystallographic graphs；
- Ehrhart / rational generating-function analogues；
- stable norms / limit shapes；
- Wulff shapes；
- lattice animals / digital geometry；
- discrete curvature / combinatorial sphere boundaries。

必须区分：

- 已知 exact growth law；
- 已知一般定理在 FCC/HCP 的直接特例；
- 本任务新发现的 Enterprise-specific representation / boundary-type decomposition；
- 仅数值观察。

不要把已知 coordination sequence 重新命名为新定理。

---

## 12. 必须主动攻击的反例

至少执行以下 kill tests：

1. **origin dependence**：换中心胞或 HCP A/B origin 后组成是否变化；
2. **embedding dependence**：graph ball 的组合量必须不依赖任意坐标旋转；
3. **shell != exposed boundary**：找最小 r 检查两者是否不同；
4. **Euclidean-sphere presumption**：测高对称方向，若极限方向比不趋 1，立即拒绝“自然球 = 欧氏球”；
5. **FCC=HCP presumption**：找最小 r 的 growth / boundary-spectrum 分歧；
6. **polynomial overfit**：小 r 拟合后用远端 holdout r 验证；
7. **period overfit**：搜索更小 period 并用 residue-class holdout 验证；
8. **topology presumption**：显式检查 boundary complex，而不是根据视觉判断；
9. **10^36 scale claim**：只有 remainder bound 才能宣称该尺度足够；
10. **pi hindsight**：任何为了匹配连续 pi 而调权重/半径定义的方案都单独标为 external calibration，不得混入 intrinsic result。

---

## 13. 最低实现与数据产物

建议至少生成：

- `experiments/r033_fcc_hcp_intrinsic_sphere.py`
- `tests/test_r033_fcc_hcp_intrinsic_sphere.py`
- `research/R033_FCC_HCP_INTRINSIC_SPHERE_REPORT.md`
- `research/r033_generated/R033_GROWTH_ATLAS.json`
- `research/r033_generated/R033_BOUNDARY_TYPE_ATLAS.json`
- `research/r033_generated/R033_TOPOLOGY_ATLAS.json`
- `research/r033_generated/R033_LIMIT_SHAPE_ATLAS.json`
- `research/r033_generated/R033_MACRO_10E36_10E38.json`
- `research/r033_generated/R033_HYPOTHESIS_DISPOSITIONS.json`
- `research/r033_generated/R033_PRIOR_ART_MATRIX.json`

如果某个产物因数学上不适用而无法生成，必须返回明确的 negative result，而不是用近似替代 exact contract。

---

## 14. 返回时必须直接回答的十个问题

1. FCC intrinsic shell `A_r` 的 exact law 是什么？
2. HCP intrinsic shell `A_r` 的 exact/eventual law 是什么？
3. `V_r` 的 exact/eventual law 是什么？
4. FCC 与 HCP 第一次在哪个 r 产生不可约差异？
5. boundary cell 一共有多少个稳定 symmetry types？
6. 每类 boundary type 的比例是否收敛？
7. exposed boundary 是否最终是拓扑 `S^2`？
8. rescaled intrinsic ball 趋向欧氏球还是 anisotropic limit shape？
9. `r=10^36` 是否已经足以代表宏观组成？严格误差界是多少？
10. π、表面积、体积等连续几何量究竟是输入、近似、还是可以从 cellular composition 中后验出现？

---

## 15. Driver 期待的最强正结果

本任务最理想的结果不是“FCC/HCP 很像连续球”。

更强的是找到类似：

\[
\boxed{
\text{finite local cell alphabet}
+
\text{exact shell growth law}
+
\text{stable boundary composition spectrum}
+
\text{limit shape}
}
\]

使一个半径 `r` 的巨大“球”无需枚举，就能由少量整数/周期类完整描述其宏观组成。

如果这个压缩描述在 `10^36`–`10^38` 已稳定，那么用户提出的“这个尺度已经够了”就得到数学化：

> 不是因为计算机算不动更大，而是因为组成律已经进入可证明的宏观稳定区。

---

## 16. 返回分类

优先返回以下之一或其精确组合：

`INTRINSIC_SPHERE_COMPOSITION_LAW_FOUND`

`FCC_HCP_MACROSCOPIC_UNIVERSALITY_FOUND`

`FCC_HCP_BOUNDARY_MEMORY_SURVIVES`

`ANISOTROPIC_LIMIT_SHAPE_FOUND`

`EUCLIDEAN_SPHERE_EMERGES`

`BOUNDARY_TYPE_SPECTRUM_STABILIZES`

`TOPOLOGICAL_SPHERE_CONFIRMED`

`MACRO_SCALE_10E36_SUFFICIENT`

`POLYNOMIAL_OR_QUASIPOLYNOMIAL_GROWTH_PROVED_OR_CERTIFIED`

若核心猜想被杀：

`INTRINSIC_GRAPH_BALL_NOT_SPHERE_LIKE / REFRAME_REQUIRED`

任何返回均保持 `NOT_CANONICAL`，除非后续独立程序另行处理。
