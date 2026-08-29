<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-6D-AXIS-MIXING-ROTATION-GROUPOID",
  "title": "P000 FCC 六线四切面旋转代数公式与魔方算法词合成 V2",
  "kind": "RESEARCH",
  "owner": "research/p000-6d-axis-mixing-rotation-groupoid",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Before further geometric interpretation, force an exact algebraic calculus for rotation on the selected FCC six-line/four-slice carrier atlas and its supported native moves: global permutation representation, composition/inverse, support transport, conjugation, commutators, stabilizers, and Rubik-style algorithm words, with exact obstruction/groupoid fallbacks where total actions fail.",
  "next_action": "Encode the four FCC 120-degree slice charts as vertices A,B,C,D and the six shared line families as the six edges of K4; prove or refute Aut(K4)=S4 as the correct carrier rotation skeleton, derive the induced six-line permutation formula and generator matrices, then lift to support-restricted moves and use conjugates/commutators/setup words to isolate local rotations before attempting further native geometric interpretation.",
  "dependencies": [
    "p000_reality_foundation.json@main",
    "definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md@main",
    "research_task_records/RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE/TP2-A9D4B718C2E65F3084D1.json@main",
    "driver_reviews/P000_6D_ROTATION_SLICE_TOMOGRAPHY_DRIVER_REVIEW_20260829.md@main",
    "driver_reviews/P000_FIRST_SHELL_POLYHEDRON_DRIVER_REVIEW_AND_COORDINATE_SELECTION_20260829.md@main"
  ],
  "source_refs": [
    "research_tasks/P000_6D_AXIS_MIXING_ROTATION_GROUPOID_20260829.md@main",
    "research_returns/P000_6D_ROTATION_SLICE_TOMOGRAPHY_RETURN_20260829.md@main",
    "research_returns/P000_FIRST_SHELL_POLYHEDRON_CLASSIFICATION_RETURN_20260829.md@main"
  ],
  "evidence_status": "USER_REPRIORITIZED_ALGEBRA_FIRST / FCC_PRIMARY_CARRIER_FROZEN / RUBIK_METHODS_ALLOWED_AS_METHOD_TEMPLATE",
  "last_progress_ref": "projects/enterprise-math/P000_FCC_PRIMARY_COORDINATE_CARRIER.json",
  "last_progress_at": "2026-08-29T04:05:00+00:00",
  "hard_block": null,
  "tags": ["P000","FCC","rotation-algebra","S4","K4","six-line-atlas","commutator","conjugation","Rubik","algorithm-word","groupoid","supported-move"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-6D-AXIS-MIXING-ROTATION-GROUPOID",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P0006DROTALG",
  "origin_kind": "DIRECT_USER_REPRIORITIZATION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-6D-ROTATION-SLICE-TOMOGRAPHY",
  "successor_gate": {
    "new_information_gap": "Generation 1 asked broadly for individual-axis mixing/groupoid structure. After FCC selection, the immediate bottleneck is narrower and algebraic: no exact rotation formula, presentation, supported-move calculus, or algorithm-word language has yet been frozen for the six-line/four-slice atlas.",
    "why_parent_result_does_not_close_it": "The accepted tomography result provides only a C2 whole-block exchange. It does not derive the FCC S4/K4 carrier action, six-coordinate update formula, local support algebra, conjugation/commutator identities, or Rubik-style word synthesis needed for fine rotation.",
    "discriminating_outcomes": [
      "derive an exact S4-on-K4 carrier rotation representation and a typed lift to supported native moves",
      "show that the carrier S4 skeleton is exact but the native lift is necessarily partial/groupoid-valued",
      "refute the S4/K4 skeleton or prove that additional orientation/incidence data are required before any algebraic lift"
    ],
    "kill_condition": "A result that only describes rotations geometrically, imports ordinary cube face-turn formulas unchanged, uses SO(3)/SO(6) as native truth, or gives move examples without an exact composition/inverse/conjugation/commutator calculus does not close the task.",
    "alternative_route_or_free_exploration_considered": "Continuing the broad axis-mixing search without first fixing the algebra was rejected by direct user reprioritization. Mature Rubik methods are allowed as algebraic templates but not as ontology.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is a superseding generation of the same task, not a duplicate task. It preserves the original rotation objective while forcing a sharper algebra-first deliverable before further geometry."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 FCC 六线四切面旋转代数公式与魔方算法词合成 V2

Status: `READY / GENERATION-2 / ALGEBRA-FIRST / FCC-PRIMARY-CARRIER / P000-BOUND`

## Mother question

在 P000 六维原生空间与已经选定的 FCC 主坐标载体之下，能否在继续解释几何之前，先把“旋转”逼成一个严格可计算的代数对象：给出全局旋转、局部/分层旋转、复合、逆、共轭、交换子、支撑域传输、稳定子以及算法词的统一公式，并说明这些公式怎样作用于六条载体线族、四个重叠的 `120 degree` 三轴切面以及后续的原生 `E_1,...,E_6` 坐标？

允许参考成熟魔方解法的代数思想，但只允许参考以下方法结构：

- generators / basic turns；
- inverse moves；
- conjugation / setup moves；
- commutators；
- nested commutators；
- algorithm words and cancellation；
- stabilizer chains；
- isolate-then-transport strategy；
- permutation/orientation invariants。

普通三维魔方的具体面、颜色、角块、棱块、`SO(3)` 几何、现成公式都不是 P000 原生定义，不得直接移植。

## Frozen inputs and scope

P000 无条件成立：

`REALITY_DIMENSION=7`，`ENTERPRISE_SPACE_DIMENSION=6`，`ENTERPRISE_TIME_DIMENSION=1`。

当前主坐标载体已经关闭选择：

`P000_PRIMARY_COORDINATE_CARRIER = FCC_CUBIC_BARLOW`。

`HCP_HEXAGONAL_BARLOW = SECONDARY_REGRESSION_CARRIER`。

六条 FCC 无向 carrier line families 固定为：

`L1=[(1,1,0)]`，`L2=[(1,-1,0)]`，`L3=[(1,0,1)]`，`L4=[(1,0,-1)]`，`L5=[(0,1,1)]`，`L6=[(0,1,-1)]`。

四个重叠 `120 degree` 切面固定为：

`S_A={L1,L3,L6}`，
`S_B={L1,L4,L5}`，
`S_C={L2,L3,L5}`，
`S_D={L2,L4,L6}`。

冻结 incidence 重标记候选：

`L_AB=L1`，`L_AC=L3`，`L_AD=L6`，`L_BC=L5`，`L_BD=L4`，`L_CD=L2`。

于是每个 `S_X` 是 `K4` 顶点 `X` 的三条 incident edges。研究员必须首先严格证明这一 `K4` incidence 编码与当前 FCC atlas 完全一致，然后才能使用 `Aut(K4)`。

强制 typing：

`[v]={v,-v}` 只是 carrier 无向线，不是原生负轴。

`NATIVE_AXIS_COUNT=6` 来自 P000，不来自 `K4`、FCC、12 contacts 或经典秩。

`FCC_CARRIER_READOUT_IS_NOT_NATIVE_IDENTITY`。

`CARRIER_KERNEL != NATIVE_COORDINATE_EQUIVALENCE`。

`CLASSICAL_CARRIER_DIMENSION != NATIVE_SPATIAL_DIMENSION`。

已接受的 C2 whole-block exchange 只作为 regression；它不能充当本任务的细旋转答案。

## Hard target and required outputs

Hard target：

`P000_FCC_SIX_LINE_ROTATION_ALGEBRA_AND_RUBIK_WORD_CALCULUS_EXACTLY_CLASSIFIED`。

### A. 先逼出全局旋转母公式

若 `K4` 编码成立，验证：

`G_FCC = Aut(K4) ~= S4`

是否正好给出当前六线四切面 atlas 的 orientation-preserving carrier rotation skeleton。

对 `sigma in S4`，六条 line family 以无序二元组 `{i,j}` 编码时，必须证明或否定候选公式：

`R_sigma(L_{ij}) = L_{sigma(i),sigma(j)}`。

若把六维坐标槽写成

`x=(x_AB,x_AC,x_AD,x_BC,x_BD,x_CD)`，

必须证明或修正候选坐标更新公式：

`(R_sigma x)_{ij} = x_{sigma^{-1}(i),sigma^{-1}(j)}`。

要求给出一个最小生成元集合、其在六坐标槽上的 `6x6` 置换矩阵/置换表示，并验证：

`R_sigma R_tau = R_{sigma tau}`，

`R_sigma^{-1}=R_{sigma^{-1}}`，

`R_e=I`。

不得只列举 24 个旋转；必须给出表示/生成关系或等价压缩代数。

### B. 四切面动作公式

证明或修正：

`R_sigma(S_i)=S_{sigma(i)}`。

给出六线、四切面的同一群作用及 stabilizer：

- `Stab(S_i)`；
- `Stab(L_{ij})`；
- `Stab(S_i,L_{ij})`；
- 必要时的 orientation/chart stabilizer。

解释哪些旋转在 carrier 层只换图，哪些可能对应原生可观察状态变化；二者不得混同。

### C. 分层/局部旋转必须有精确代数

定义 typed supported move：

`M[Omega,sigma]`。

其中 `Omega` 是原生或已声明 carrier-support 区域，`sigma` 是已证明合法的 atlas rotation label。

至少分类两种情况：

1. `R_sigma(Omega)=Omega`：全定义 supported permutation；
2. `R_sigma(Omega)!=Omega`：不得强行写成全局群元素，必须给出 partial action / groupoid arrow / exact obstruction。

若 support invariant，验证候选公式：

`M[Omega,sigma]^{-1}=M[Omega,sigma^{-1}]`。

如果不成立，给出正确公式与最小反例。

### D. 必须建立“魔方式”共轭公式

成熟魔方中的 setup move 思想必须被翻译成当前 typed 形式。

证明、修正或否定候选：

`R_tau M[Omega,sigma] R_tau^{-1} = M[R_tau(Omega), tau sigma tau^{-1}]`。

该公式若成立，应解释为“把一个已知局部算法搬运到另一层/另一切面”的代数核心。

若只在 groupoid/partial-action 条件下成立，必须写出精确 domain/codomain 条件。

### E. 必须建立交换子公式与局域化机制

定义

`[A,B]=A B A^{-1} B^{-1}`。

不得停留在记号层面。至少要做到：

- 推导 `supp([A,B])` 的精确上界；
- 找出何种 support overlap / stabilizer 条件使交换子把大范围动作压缩成局部动作；
- 给出至少一个非平凡 FCC 六线/四切面实例；
- 若交换子不能实现预期局域化，给出最小 obstruction。

目标是获得成熟魔方算法中“多数位置复原、少数位置被置换/旋转”的 P000 对应机制。

### F. 算法词与约简

定义旋转词

`w=g_1^{epsilon_1}...g_m^{epsilon_m}`，`epsilon_i in {+1,-1}`，

及其 evaluation `Eval(w)`。

必须实现：

- immediate inverse cancellation；
- generator-order reduction；
- conjugation recognition；
- commutator recognition；
- 至少一种 canonical/normal-form 或可判等替代方案；
- word -> six-line permutation；
- word -> four-slice permutation；
- 若支持域存在，word -> support/domain transport trace。

可以参考成熟魔方求解中的 move sequence、setup move、commutator、conjugate、stabilizer chain，但必须重新证明当前体系的关系。

### G. 逼出“最小局部算法”

至少完成以下三类中的两类，第三类若失败必须给出 exact no-go：

1. `SLICE_TRANSPORT_WORD`：把一个指定 `120 degree` 切面送到另一个切面；
2. `AXIS_TARGETING_WORD`：改变一个指定 axis family 的可见/相邻关系，同时最大限度稳定其余结构；
3. `OVERLAP_LOCALIZER_WORD`：利用 commutator/conjugate 把影响限制到两个/多个 support 的交叠邻域。

对成功算法，给出 word、作用、逆、稳定子与最短性/局部最短性证据；若不做全局最短证明，至少给出 bounded exhaustive certificate。

### H. 与原生 E_1,...,E_6 的接口

本任务不要求完整解决 native-to-FCC bridge，但必须产出 bridge 可直接消费的 rotation algebra interface：

- line-label action；
- slice-label action；
- chart orientation transport；
- support/domain transport；
- word evaluation；
- kernel/faithfulness 情况。

必须明确：carrier 置换表示可以作为 native rotation 的候选 readout，但不能据此自动把两个 native state 判等。

### I. 回归与反例

必须保留：

- 原 C2 whole-block exchange regression；
- HCP first-shell non-central-symmetry regression；
- 旧 A3 partial-support scale-coherence 反例，防止只看 frame phase 而忽略 support/domain transport。

### J. 确定性 checker

提供 exact deterministic checker，至少验证：

- `K4` incidence；
- `Aut(K4)` 与六线作用；
- generator closure/order；
- `6x6` permutation matrices；
- 四切面作用；
- conjugation identities；
- commutator examples；
- selected algorithm words；
- support/domain typing regressions。

禁止只靠浮点旋转矩阵或视觉动画验收。

## Research value to preserve

进取几何的特色是旋转。当前最危险的做法，是在六维定义还没成熟时不断画几何图、靠直觉命名旋转，却没有一套可复核的代数。

成熟魔方真正值得借鉴的不是三维立方体，而是它把复杂空间动作压缩为：

`生成元 -> 词 -> 逆 -> 共轭 -> 交换子 -> 稳定子 -> 局部算法 -> 复原/运输`。

本任务要把这一套方法移植到 FCC 六线四切面 atlas 上，先获得旋转的“语法和代数”，再让后续几何解释受代数约束。

特别关注 `K4/S4` 结构：四个切面两两交于一条轴，正好给出 4 vertices / 6 edges 的 incidence。如果这一结构成立，则可能第一次得到紧凑的六轴旋转母公式；如果不成立，也必须由 exact counterexample 终结，而不是靠直觉放弃。

## Success, kill, and return criteria

成功至少要求：

1. 一套 exact 全局旋转表示；
2. 六坐标槽的统一更新公式；
3. composition/inverse；
4. supported move 的 typed 代数；
5. conjugation；
6. commutator/localization；
7. algorithm-word evaluation/reduction；
8. 至少两个非平凡 Rubik-style 局部算法或 exact no-go；
9. deterministic checker；
10. 可直接交给 native-to-FCC bridge 的 algebra interface。

以下情况直接判失败：

- 只给几何示意，没有代数公式；
- 只枚举旋转，没有生成关系/复合律；
- 把普通魔方公式原封不动复制过来；
- 把 `SO(3)`、`SO(6)`、经典欧氏矩阵当成 P000 原生定义；
- 忽略 support/domain，只研究 frame permutation；
- 交换子只写符号不算实际作用；
- 没有 inverse/conjugation；
- 没有 exact checker；
- 用 FCC 三维 carrier 的线性关系降低 P000 六维；
- 因 `[v]={v,-v}` 而导入原生负轴；
- 忽略 HCP/A3 回归。

如果全局 S4 载体代数成立但 native lift 失败，返回 `CARRIER_ROTATION_ALGEBRA_PROVED / NATIVE_LIFT_OBSTRUCTED`，并精确给出 obstruction；这仍然是有效终态，不得伪造完整 native rotation group。
