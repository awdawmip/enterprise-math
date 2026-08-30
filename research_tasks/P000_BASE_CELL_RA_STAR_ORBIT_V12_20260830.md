<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 framed Full-Cell a 型提升、四星轨道与 S4 关系闭合 V12",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Construct or exactly obstruct, in one common declared framed/PF-10 Full-Cell model, a strict lift of carrier generator a=(BCD) together with the accepted b-type lift, transport the four K4-star native slice objects, and classify whether a^3=b^2=(ab)^4=id holds at enriched-state and bare-Cell levels without quotienting native identity.",
  "next_action": "Freeze the six-axis action a_xi=(E1 E2 E3)(E4 E6 E5), define r_a and Pi^a_x=f_{r_a(x)} a_xi f_x^-1, impose the Gen11 strict-lift criterion, require one common model carrying both r_a and r_b, then compute star transport, relation residues, generated action order and kernels before any claim of native S4.",
  "dependencies": [
    "research_returns/P000_BASE_CELL_RB_EQUIVARIANCE_V11_RETURN_20260830.md@main",
    "driver_reviews/P000_BASE_CELL_RB_EQUIVARIANCE_V11_DRIVER_REVIEW_20260830.md@main",
    "research_returns/P000_AXIS_CHANNEL_FRAME_CONNECTION_V10_RETURN_20260830.md@main",
    "projects/enterprise-math/P000_FCC_ROTATION_ALGEBRA.json@global"
  ],
  "evidence_status": "GEN11_FRAMED_BASE_b_GATE_DRIVER_ACCEPTED / COMMON_MODEL_a_AND_b_ORBIT_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","R_a","R_b","S4","K4-star","J_C","J_D","full-cell","equivariance","kernel"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000FCC12",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "successor_gate": {
    "new_information_gap": "Gen11 classifies and witnesses one strict framed base-Cell b lift, but no common model yet carries the second carrier generator a or the full K4-star orbit and S4 relations.",
    "why_parent_result_does_not_close_it": "Individual existence of r_b does not imply simultaneous existence of r_a and r_b, nor relation closure on Cell identities/decorations.",
    "discriminating_outcomes": [
      "construct one common framed Full-Cell model with strict r_a and r_b satisfying exact S4 generator relations and four-star transport",
      "construct both generators but expose a nontrivial Cell-kernel/relation residue, classifying an extension rather than S4",
      "prove an exact simultaneous-lift obstruction even though the b lift exists individually"
    ],
    "kill_condition": "Do not use two unrelated witness models; do not identify carrier S4 with bare-P000 rotation by fiat; do not infer J_C/J_D geometry from carrier labels alone; do not quotient Cell identity by carrier/readout; do not treat local channel S6 as native rotation; do not suppress nontrivial relation residues or Cell-level kernels.",
    "alternative_route_or_free_exploration_considered": "The b gate is solved at declared-model strength. The highest-leverage next step is simultaneous generator lifting and relation closure, not more contact/frame algebra.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Generation 12 changes the target from one generator's automorphism criterion to the first common-model rotation-group/orbit test."
  }
}
-->

# P000 framed Full-Cell `a` 型提升、四星轨道与 `S4` 关系闭合 V12

Status: `READY / GENERATION-12 / P0 / P000-BOUND / COMMON-MODEL-GROUP-RELATION-FIRST`

## Mother question

Gen11 已在声明的 framed/PF-10 Full-Cell derived model 类中严格关闭 `b` gate：存在非平凡 strict base-Cell `R_b` witness，且其必要充分等变条件已分类。

现在必须回答更强的问题：

\[
\boxed{\text{同一个 Full-Cell 模型里，能否同时实现 }R_a,R_b\text{ 并闭合 carrier }S_4\text{ 关系？}}
\]

不能把两个不同模型中的单生成元 witness 拼成一个旋转群。

## Frozen carrier/native-axis actions

Carrier generators：

\[
a=(BCD),\qquad b=(AB).
\]

在冻结 `beta` 标号下，六 native axis types 上：

\[
\boxed{a_\xi=(E_1\ E_2\ E_3)(E_4\ E_6\ E_5)}
\]

\[
\boxed{b_\xi=(E_2\ E_4)(E_3\ E_5)},\qquad E_1,E_6\text{ fixed}.
\]

Carrier relation regression：

\[
a_\xi^3=b_\xi^2=(a_\xi b_\xi)^4=id.
\]

这些是 axis-type/carrier-compatible actions，不自动定义 Cell map。

## Hard target

`P000_FRAMED_BASE_CELL_a_LIFT_K4_STAR_ORBIT_AND_S4_RELATIONS_EXACTLY_CLASSIFIED`

## A. Strict `a`-lift criterion

在 Gen11 同一 typed language 下定义候选 Cell map

`r_a:D_a -> D_a'`

以及

\[
\Pi^a_x=f_{r_a(x)}\circ a_\xi\circ f_x^{-1}.
\]

必须逐项测试 Gen11 的 strict-lift 模板：

- Cell bijection；
- 若声明 order-3 lift，则 `r_a^3=id`；
- native adjacency/incidence preservation；
- full PF-10 `I/O/M` tensor equivariance；
- independent connection naturality；
- gauge covariance；
- time fixed；
- no carrier/native quotient。

不得把 `a_xi` 本身当作 `r_a`。

## B. One common model gate

必须在**同一个** finite/exact framed Full-Cell model 中同时给出：

- frames `f_x`；
- native Cell identities and adjacency；
- PF-10 tensors；
- retained connection；
- strict `r_a`；
- strict `r_b`。

如果只能分别在两个不同 witness 中实现 `a` 与 `b`，不得宣告 group lift 成功。

## C. K4-star orbit / native slice transport

冻结 derived slice objects：

`J_A={E1,E2,E3}`;
`J_B={E1,E4,E5}`;
`J_C={E2,E4,E6}`;
`J_D={E3,E5,E6}`.

必须证明或精确否定：

- `a_xi(J_A)=J_A`；
- `a_xi(J_B)=J_C`；
- `a_xi(J_C)=J_D`；
- `a_xi(J_D)=J_B`；
- `b_xi(J_A)=J_B` 与相应 inverse transport。

集合标签变换不够。若把 `J_C,J_D` 升为声明模型内的 geometric slice objects，必须通过 `r_a` transport 继承 Cell set/state object、adjacency、local three-axis relation 与 overlap/gluing，不得仅凭 FCC chart 宣布。

## D. Exact group relations on enriched automorphisms

定义 composition convention 并计算：

\[
R_a^3,\qquad R_b^2,\qquad (R_aR_b)^4.
\]

至少区分三个层次：

1. axis-type action；
2. full enriched framed/PF-10 automorphism；
3. bare Cell-identity permutation。

不得因为 axis action 关系闭合就静默认为 Cell map 关系闭合。

## E. Residue / kernel classification

若

`R_a^3` 或 `(R_aR_b)^4`

在 axis types 上为 identity、但在 Cell identities / hidden relational state 上非 identity，必须冻结 exact residue。

分类：

- exact `S4` representation；
- nontrivial kernel on bare Cell identities；
- central/noncentral extension-like residue；
- groupoid/partial-domain obstruction；
- no simultaneous lift。

禁止 quotient 掉 residue 来制造 `S4`。

## F. Generated action size / faithfulness

若两个 strict generators 存在，计算它们生成的 automorphism set/group：

`<R_a,R_b>`.

必须给：

- enriched-action order；
- bare-Cell permutation image order；
- kernel of forgetful map from enriched action to Cell permutations；
- kernel of axis-type readout if material；
- whether the carrier `S4` action is faithfully represented at each level。

`24` 只能由 exact enumeration/proof 得出，不能按 carrier 预填。

## G. `Omega_b` / contact route regression

Gen11 已冻结：

`Omega_b` 与 base `R_b` 逻辑独立，`Omega_b=CONTACT_ROUTE_SPECIFIC`。

V12 不得重新把 contact 变成 rotation prerequisite。若共同模型恰好在 `Omega_b`，只能作为附加结构记录。

## H. Holonomy / connection compatibility

若 connection 独立且可能非平坦，必须检查 `R_a` 与 `R_b` 对 holonomy representation 的等变性，并验证 group words 对 connection data 的作用。

非平坦本身不是 obstruction；违反相应 conjugacy/naturality law 才是 obstruction。

## I. Positive witness or exact obstruction

成功必须给至少一个 finite exact **single common model**，其中 `R_a,R_b` 均非平凡或明确解释 fixed-Cell internal case，并验证全部关系。

若失败，给最小 countermodel 与失败层：

`A_LIFT_FAILS` / `COMMON_MODEL_FAILS` / `STAR_TRANSPORT_FAILS` / `RELATION_RESIDUE` / `CONNECTION_NATURALITY_FAILS` / `OTHER_EXACT_OBSTRUCTION`.

## J. Deterministic checker

至少覆盖：

- frozen axis permutations and carrier relations；
- Gen11 strict `b` regression；
- candidate strict `a`；
- one-common-model requirement；
- four-star transport；
- `R_a^3`,`R_b^2`,`(R_aR_b)^4` at enriched and Cell levels；
- generated action order/kernels；
- connection/holonomy equivariance；
- no P000 mutation / no quotient / no native `S6` promotion。

## Valid terminal classes

- `FRAMED_COMMON_MODEL_S4_LIFT_AND_FOUR_STAR_ORBIT_EXACTLY_REALIZED`;
- `FRAMED_a_AND_b_LIFTS_EXIST_WITH_NONTRIVIAL_RELATION_RESIDUE_CLASSIFIED`;
- `EXACT_SIMULTANEOUS_a_b_FULL_CELL_LIFT_OBSTRUCTION_PROVED`.

即使第一类成功，也只建立声明的 downstream framed Full-Cell model 中的 rotation representation。不得直接宣布 bare P000 的完整 rotation group 就是 `S4`。

External prior-art lane remains:

`RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT / TP2-5A7C1D9E3B6042F8D117 / Generation 7`.
