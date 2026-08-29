<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 原生混合星切面、signed-K4 上同调与最小旋转提升 V6",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Translate the accepted FCC chart Z2 transition system into exact signed-K4/switching/cohomology data, compute the S4 equivariant lifting obstruction and minimal extension class, then construct the mixed native star slices and legal state-level rotation lift or prove the exact native obstruction without quotienting native six-dimensional state through the carrier.",
  "next_action": "First classify the accepted q_ij signs as a signed-K4 switching/cohomology class and compute S4 invariance/lift obstruction; then derive the exact lifted generator relations for a=(BCD), b=(AB), classify the minimal C2/central/projective/groupoid extension if any, and only then attempt native mixed-slice geometry on J_B,J_C,J_D.",
  "dependencies": [
    "research_notes/P000_FCC_S4_Z2_PRIOR_ART_SYNTHESIS_20260829.md@main",
    "research_returns/P000_L1_NATIVE_FCC_CARRIER_BRIDGE_V2_RETURN_20260829.md@main",
    "driver_reviews/P000_NATIVE_FCC_STRICT_BRIDGE_GEN2_DRIVER_REVIEW_20260829.md@main",
    "research_returns/P000_6D_AXIS_MIXING_ROTATION_ALGEBRA_FORMULA_V2_RETURN_20260829.md@main",
    "driver_reviews/P000_FCC_SIX_LINE_ROTATION_ALGEBRA_DRIVER_REVIEW_20260829.md@main",
    "p000_reality_foundation.json@main"
  ],
  "evidence_status": "PRIOR_ART_SYNTHESIZED / CLASSICAL_COMPONENTS_SEPARATED / NATIVE_LIFT_FRONTIER_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","FCC","S4","K4","signed-graph","switching","Z2-holonomy","cohomology","central-extension","binary-octahedral-comparison","mixed-slice","state-lift","groupoid"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000NATFCC6",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "successor_gate": {
    "new_information_gap": "Gen5 correctly asks for mixed native slices and a state-level S4 lift but does not exploit the newly established external fact that the chart-sign obstruction belongs to mature signed-graph/switching/cohomology theory, where automorphism-lifting and double-cover obstructions have direct antecedents. The remaining information gap is the exact cohomology/extension class induced by the frozen FCC chart data and its compatibility with P000 native Cell legality.",
    "why_parent_result_does_not_close_it": "The accepted strict bridge proves q-triangle holonomy=-1 and no global signed section, but does not classify the switching class in standard terms, compute the S4 lifting obstruction, identify the minimal extension algebra, or construct/refute the mixed native geometric slices and state automorphisms.",
    "discriminating_outcomes": [
      "the signed-K4 class is S4-equivariant and admits a split native lift after adding exactly derived local state",
      "the lift is necessarily non-split and realizes a precisely identified C2 central/projective extension after native legality checks",
      "only a partial/groupoid lift exists because support/chart domains obstruct a global action",
      "no finite Z2-type extension suffices and a stronger exact native obstruction/minimal extra state is proved"
    ],
    "kill_condition": "Do not claim novelty for S4, K4 edge action, signed-graph antibalance, Z2 holonomy, Rubik commutators, or known double covers; do not assume binary octahedral/Schur cover from analogy; do not define mixed native slices or E_i=L_i by fiat; do not quotient native states through carrier readout; do not import SO(6) or classical rank reduction.",
    "alternative_route_or_free_exploration_considered": "More carrier enumeration and more Rubik words are closed at task strength. Direct geometric construction without first resolving the switching/cohomology obstruction risks rediscovering known mathematics and guessing the wrong extension. The algebraic obstruction-first route is now the highest-leverage continuation.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Generation 6 supersedes Gen5 because the external prior-art synthesis materially changes the research method and novelty boundary: standard signed-graph/cohomology machinery becomes mandatory input before native geometry is attempted."
  }
}
-->

# P000 原生混合星切面、signed-K4 上同调与最小旋转提升 V6

Status: `READY / GENERATION-6 / P0 / P000-BOUND / PRIOR-ART-INFORMED / ALGEBRA-OBSTRUCTION-FIRST`

## 0. Mother question

冻结当前 P000/FCC 体系：

- 原生空间：`CELL_STATE=(E_1,...,E_6)`，六轴来自 P000；
- FCC 只是一套选定 carrier/readout；
- 四个 carrier star/charts：`A,B,C,D`；
- 六 carrier lines = `K4` 六边；
- carrier proper rotation skeleton：`O_FCC ~= S4`；
- 已接受 chart transition signs `q_ij in {+1,-1}`；
- 每个三角 chart-loop holonomy 为 `-1`；
- 旧 clone-product `C2` whole-block exchange 已证明不能直接 intertwine FCC `S4`；
- `J_A={1,2,3}` 已有三轴切面，`J_B={1,4,5}`, `J_C={2,4,6}`, `J_D={3,5,6}` 目前只是 observation windows。

本代不再从画图出发。先回答：

> accepted `q_ij` 在标准 signed-graph/cohomology 语言中究竟是哪一个 switching class？`S4` 对它的作用是否能提升到带最小隐藏状态的 native 旋转？如果能，精确是哪一种 extension/groupoid；如果不能，最小 obstruction 是什么？

然后才允许构造 native mixed slices。

## 1. External prior-art freeze — 不得重新发明

任务必须读取：

`research_notes/P000_FCC_S4_Z2_PRIOR_ART_SYNTHESIS_20260829.md`。

下列内容视为外部成熟数学，不是本任务 novelty target：

1. proper octahedral/cuboctahedral rotation group `~= S4`；
2. `S4` 对 `K4` 六边 / 2-subsets 的六点表示；
3. `L(K4)=J(4,2)=octahedral graph`，且 full graph automorphism 可比 physical proper-rotation `S4` 更大；
4. signed graph switching、cycle-sign invariance、balance/antibalance；
5. graph/group signature 的 loop holonomy；
6. switching class / two-graph 的 cohomological automorphism-lifting理论；
7. `S4` 的已知双覆盖/Schur covers，包括 binary octahedral comparison objects；
8. Rubik conjugation/commutator/setup methods。

任何最终 novelty claim 只能落在 **P000-native compatibility theorem / exact obstruction / minimal native extension** 上。

## 2. Hard target

`P000_NATIVE_MIXED_STAR_COHOMOLOGY_AND_MINIMAL_ROTATION_LIFT_EXACTLY_CLASSIFIED`

允许有效终态：

- `NATIVE_S4_LIFT_SPLIT_EXTENSION_CONSTRUCTED`；
- `NATIVE_NONTRIVIAL_C2_EXTENSION_EXACTLY_IDENTIFIED`；
- `NATIVE_PROJECTIVE_OR_GROUPOID_LIFT_EXACTLY_CLASSIFIED`；
- `EXACT_NATIVE_LIFT_OBSTRUCTION_AND_MINIMAL_MISSING_STATE_PROVED`。

“看起来像 binary octahedral”不是终态。

## 3. Required Output A — 把 q_ij 精确翻译成 signed-K4

冻结当前 chart transition：

`q_AB=-1`, `q_AC=-1`, `q_AD=+1`, `q_BC=-1`, `q_BD=+1`, `q_CD=+1`。

必须：

1. 视其为 `K4` edge signature `q:E(K4)->C2`；
2. 计算所有独立 cycle products；
3. 证明/推翻它是 antibalanced；
4. 给出其 switching-equivalence class；
5. 给出最小 gauge-normal form；
6. 若采用 `H^1(K4;Z2)` / cut-cocycle-code 语言，明确 class representative 与 gauge quotient；
7. 证明这些 carrier gauge statements **不产生 native negative axis，也不 quotient native state**。

必须区分：

`CARRIER_SWITCHING_EQUIVALENCE != NATIVE_STATE_EQUIVALENCE`。

## 4. Required Output B — S4 对 switching class 的作用

carrier `S4` 已接受，不得重做。

必须计算：

1. `sigma.q` 如何作用；
2. switching class `[q]` 是否被全部 `S4` 稳定；
3. 是否存在一个单一 representative 被全部 `S4` 严格固定；
4. 若只有 switching-class 级不变，求每个 `sigma` 所需 gauge correction `g_sigma`；
5. 检查 `g_sigma` 的组合是否产生 1-cocycle / 2-cocycle residue。

这一段必须对照 Cameron/two-graph/switching-class prior art，但结论只在 carrier/transition-data 层。

## 5. Required Output C — 逼出提升代数，而不是猜群名

carrier generators：

`a=(BCD)`, `b=(AB)`,

满足 carrier relations：

`a^3=e`, `b^2=e`, `(ab)^4=e`。

若最小附加 hidden state 是 central `z` 且 `z^2=e`，必须实际计算 lifts `A~,B~` 后的关系：

`A~^3 = z^alpha`,

`B~^2 = z^beta`,

`(A~B~)^4 = z^gamma`,

其中 `alpha,beta,gamma in {0,1}`。

还必须检查完整 associativity/cocycle condition，不能只看三个 relation。

随后才可分类：

- split `S4 x C2`；
- 某个 non-split `C2` central extension；
- known Schur-cover comparison object（例如 binary octahedral / GL(2,3) 型）;
- projective action；
- action groupoid；
- exact no-go。

### Critical guard

`Z2_LOOP_HOLONOMY != AUTOMATIC_PROOF_OF_BINARY_OCTAHEDRAL_GROUP`。

如果与 known `2O` 或其他 `2.S4` 同构，必须由 exact presentation / element orders / extension map / central kernel 证明；不得从 `Spin(3)` analogy 偷渡到 native 6D。

## 6. Required Output D — 最小 hidden state

必须回答：为了让 chart-local orientation 与 carrier composition 可传递，native state 是否需要新增信息？

候选只能从 obstruction 推导，例如：

- one `Z2` orientation bit；
- chart-indexed local torsor state；
- incidence state；
- support/domain state；
- path/history/holonomy state；
- higher finite fiber。

若提出扩展 `X_hat -> X_6`，必须证明：

1. fiber 最小性；
2. forgetting map 不改变 P000 六轴原生身份；
3. hidden state 不是额外空间轴；
4. time/history 与 spatial state typing 区分；
5. carrier readout collision 不被 quotient。

## 7. Required Output E — mixed native star slices

只在 A-D 完成后进入。

必须对：

`J_B={1,4,5}`,
`J_C={2,4,6}`,
`J_D={3,5,6}`

分别构造或否定 native geometric slice structure。

若构造，至少给出：

- Cell state restriction / local coordinates；
- native adjacency；
- 与 `J_A={1,2,3}` 已建立三轴切面的同强度 comparison；
- overlap axis transport；
- carrier `120 degree` chart readout；
- chart-local orientation state；
- rotation transport compatibility。

禁止仅因为 `beta(J_i)=S_i` 就宣布 `J_i` 已是几何切面。

## 8. Required Output F — native generator lifts

构造或否定 legal native transforms：

`R~_a`, `R~_b`。

必须作用于完整 native/extended state，不得只 permute axis labels。

检验：

`Phi(R~_a X)=R_a^FCC Phi(X)`，

`Phi(R~_b X)=R_b^FCC Phi(X)`。

同时检验：

- native adjacency preservation；
- mixed-slice transport；
- hidden-state transport；
- inverse/composition；
- support/domain typing；
- P000 dimension guards。

## 9. Required Output G — carrier identity 的 native residue

对所有 shortlex carrier words，尤其：

`a^3`, `b^2`, `(ab)^4`, commutators, conjugates，

分类：

- strict native identity；
- central `Z2` residue；
- chart gauge residue；
- hidden holonomy；
- domain mismatch/groupoid residue；
- non-liftable word。

若两个不同 native paths 有相同 carrier endpoint，必须记录 time-ordered trace；time 只负责 relation-change order，不是第七空间轴。

## 10. Required Output H — 与已知数学做 claim-by-claim 对照

最终 return 必须有一张表：

`INTERNAL_CLAIM | EXTERNAL_ANALOG | EXACT_DUPLICATE/PARTIAL/NEW_COMBINATION | P000_NATIVE_EXTRA_CONSTRAINT | NOVELTY_STATUS`。

至少覆盖：

- signed-K4 antibalance；
- switching class；
- S4 invariance；
- group-cohomology obstruction；
- double cover / central extension；
- mixed native slice geometry；
- state-level native automorphism；
- operation-safe no-quotient boundary。

不得因为“找不到完全一样的 P000 论文”就宣称数学新颖。

## 11. Required Output I — deterministic checker

checker 至少必须 exact 验证：

1. all K4 cycle signs；
2. switching orbit / canonical representatives；
3. S4 action on switching class；
4. gauge corrections `g_sigma`；
5. candidate cocycle identity；
6. lifted generator relations / extension order where finite；
7. mixed-slice incidence；
8. state-level equivariance or smallest obstruction witnesses；
9. regressions：carrier S4, old C2 no-intertwiner, q triangle holonomy=-1, FCC/HCP 6/3 antipodal pairs；
10. no native quotient through carrier kernel。

## 12. Kill conditions

以下任何一种都判 nonresponsive：

- 重新证明 `O_FCC ~= S4` 当成成果；
- 重新发现 signed graph negative cycle / switching 当成成果；
- 看到 all triangles `-1` 就只说“有 holonomy”而不算 switching/cohomology class；
- 看到 `Z2` 就直接命名 binary octahedral；
- 用 `Spin(3)` / `SO(3)` 定义 native rotation；
- 把 chart sign 变成 primitive native negative axis；
- 把 `E_i` 直接等同 carrier vector；
- 用 carrier kernel quotient native states；
- 未构造 mixed native geometry就宣布 state-level lift；
- 只做 carrier group theory，不碰 P000 native legality。

## 13. Desired decisive outcome

最优结果不是“又找到一个群名”，而是得到一个 exact commuting/lifting structure：

`FULL P000 NATIVE STATE / MINIMAL EXTENSION`
`--R~-->`
`FULL P000 NATIVE STATE / MINIMAL EXTENSION`
` | Phi                         | Phi`
` v                             v`
`FCC SIGNED-K4 CARRIER ATLAS --R_sigma--> FCC SIGNED-K4 CARRIER ATLAS`

并明确：

- 哪一部分是 1950s-1980s 起已有的 signed-graph/cohomology 数学；
- 哪一部分是经典 octahedral/Schur-cover 数学；
- 哪一部分是 P000 native Cell compatibility 新问题；
- 若失败，最小 obstruction 到底落在哪个 typed layer。
