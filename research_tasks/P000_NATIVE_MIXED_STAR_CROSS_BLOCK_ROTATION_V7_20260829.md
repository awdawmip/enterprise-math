<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 原生混合星 J_B 与 cross-block b 型全状态旋转原语 V7",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Construct or exactly obstruct the first genuine mixed native star J_B={E1,E4,E5} together with a legal full-state cross-block b-type rotation inducing (E2 E4)(E3 E5), then complete the native star orbit and S4 relations only if this primitive exists.",
  "next_action": "Start from primitive native Cell relations rather than carrier signs. Define a native geometric slice structure on J_B and a legal full-state R~_b preserving native adjacency/Cell typing, or return the smallest exact obstruction. Only after that construct R~_a/orbit completion to J_C,J_D and check a^3,b^2,(ab)^4 at native-state strength.",
  "dependencies": [
    "research_returns/P000_NATIVE_MIXED_STAR_COHOMOLOGY_LIFT_V6_RETURN_20260829.md@main",
    "driver_reviews/P000_NATIVE_MIXED_STAR_COHOMOLOGY_LIFT_V6_DRIVER_REVIEW_20260829.md@main",
    "research_returns/P000_NATIVE_FCC_BRIDGE_COHOMOLOGY_PRIOR_ART_AUDIT_V5_RETURN_20260829.md@main",
    "driver_reviews/P000_NATIVE_FCC_COHOMOLOGY_PRIOR_ART_V5_DRIVER_REVIEW_20260829.md@main"
  ],
  "evidence_status": "CARRIER_COHOMOLOGY_CLOSED_SPLIT_S4xC2 / PRIOR_ART_BOUNDARY_ACCEPTED / NATIVE_CROSS_BLOCK_OPERATION_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","mixed-star","J_B","cross-block","rotation","S4","Cell","state-automorphism","no-quotient"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000NATFCC7",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "successor_gate": {
    "new_information_gap": "Gen6 proved that the signed-K4/S4 carrier lifting problem is split and leaves no carrier-forced central residue. The remaining discriminating gap is native: the current Cell interface does not construct mixed stars or a partial cross-block b-type full-state motion.",
    "why_parent_result_does_not_close_it": "RR-0C7464292459CAF82805 explicitly freezes J_B/J_C/J_D as observation-only and identifies R~_b as the first missing native operation.",
    "discriminating_outcomes": [
      "construct J_B as a genuine native three-axis Cell slice and a legal full-state R~_b, then complete S4 orbit/relations",
      "construct only a typed partial/groupoid R~_b with exact source/target domains and classify the obstruction to globality",
      "prove the current native Cell axioms obstruct J_B or R~_b and identify the minimal new native relation/state primitive required"
    ],
    "kill_condition": "Do not reopen signed-K4 switching, H1, Cameron gamma/beta, S4xC2 versus 2.S4, binary octahedral, or carrier word enumeration. Do not declare J_B geometric by relabeling, add a passive Z2 bit as a substitute for missing base motion, quotient native states by carrier readout, or import SO(6)/classical rank arguments.",
    "alternative_route_or_free_exploration_considered": "Carrier cohomology and double-cover routes are closed by Gen6 and the accepted prior-art audit. The old whole-factor C2 route is already killed by star/complement. The earliest unresolved operation is the cross-block b mixer, so primitive native construction is now the highest-leverage route.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is the next generation of the canonical bridge task, narrowing the search to the first missing native operation after exact elimination of carrier-cohomological alternatives."
  }
}
-->

# P000 原生混合星 `J_B` 与 cross-block `b` 型全状态旋转原语 V7

Status: `READY / GENERATION-7 / P0 / P000-BOUND / NATIVE-PRIMITIVE-FIRST`

## Mother question

当前 carrier 层已经严格闭合：

\[
E_q\cong S_4\times C_2,
\qquad
(\alpha,\beta,\gamma)=(0,0,0).
\]

所以不再问“holonomy 会不会自动产生一个双覆盖旋转群”。真正的问题是：

\[
\boxed{J_B=\{E_1,E_4,E_5\}\text{ 能否成为真正的 native geometric Cell slice？}}
\]

以及是否存在合法 full-state transform

\[
\boxed{\widetilde R_b}
\]

在轴类型上实现

\[
(E_2\ E_4)(E_3\ E_5),
\qquad E_1,E_6\text{ fixed},
\]

同时保持 P000 原生 Cell relation / adjacency / support-domain typing。

## Frozen inputs — 不得重做

1. P000 六空间轴 `E_1,...,E_6`；
2. FCC primary carrier；
3. carrier `K4/S4` algebra；
4. `beta(E_i)` 六线 type bridge；
5. `J_A={1,2,3}`, `J_B={1,4,5}`, `J_C={2,4,6}`, `J_D={3,5,6}` observation incidence；
6. old clone-product `rho` 无 FCC-S4 intertwiner；
7. signed-K4 q antibalanced，`[q]!=0 in H1`；
8. carrier correction extension split：`E_q ~= S4 x C2`；
9. lifted carrier relations residue `(0,0,0)`；
10. passive finite fiber cannot create missing base native motion；
11. external prior-art boundary：signed switching/cohomology/double-cover mathematics is classical or finite specialization。

## Hard target

`P000_PRIMITIVE_MIXED_STAR_AND_CROSS_BLOCK_FULL_STATE_ROTATION_EXACTLY_CONSTRUCTED_OR_OBSTRUCTED`

## Required outputs

### A. Primitive native state semantics

不得从 carrier 反推定义。明确当前 full native Cell state、哪些关系允许识别单轴/混合轴局部信息、哪些关系仍只有 whole-factor typing。如果现有 `X6=C_A x C_B` 不够，任何 refinement 必须作为显式新 derived model，不得改写 P000。

### B. `J_B` geometric slice

构造或否定 `J_B={E_1,E_4,E_5}` 的 native geometric slice。若构造，至少给出：

- native Cell set / address or local state object；
- adjacency；
- 三轴关系；
- 与 `J_A` 在共享 `E_1` 上的 overlap/gluing law；
- 如果继承既有 `120°` slice strength，必须给出精确 transport 依据，不能只按 FCC 图画宣布。

### C. cross-block `R~_b`

构造合法 full-state transform 或 exact obstruction：

\[
\widetilde R_b:
(E_2,E_3,E_4,E_5)\mapsto(E_4,E_5,E_2,E_3),
\]

固定 `E_1,E_6` 的 axis-type action。必须检查 full-state bijectivity/partiality、native adjacency、payload、support/domain、inverse。

### D. `J_A <-> J_B`

若 `R~_b` 存在，验证它把 `J_A` 的 native geometric structure 合法搬运到 `J_B`；如果只能在 readout 上成立，必须返回 obstruction，不能冒充 native equivalence。

### E. `R~_a` 与 orbit completion

仅在 B/C 成功后构造 `R~_a` 或等价 orbit-completion operation，使 mixed stars 扩展到 `J_C,J_D`。检查是否为全局群作用、partial action 或 groupoid。

### F. Native relations

检查：

\[
\widetilde R_a^3,
\qquad
\widetilde R_b^2,
\qquad
(\widetilde R_a\widetilde R_b)^4.
\]

carrier 已无强迫 residue；若 native 出现 residue，必须来自 native state/composition，并给 exact witness。

### G. Minimal-obstruction theorem

若失败，区分并证明最小障碍类型：

`NO_AXIS_REFINED_STATE_PROJECTION` / `MIXED_SLICE_RELATION_MISSING` / `CROSS_BLOCK_ADJACENCY_NOT_PRESERVED` / `GLOBALITY_FAILS_BUT_GROUPOID_EXISTS` / `NATIVE_RELATION_RESIDUE` / `OTHER_EXACT_TYPED_OBSTRUCTION`。

必须说明什么最小新增 native relation/state primitive 才可能解除障碍；不得用 passive sign bit 顶替。

### H. Time trace

如存在多条 native rotation path 到相同 carrier readout，记录 `(X_t,R_t,Phi(X_t))`；time 仅排序关系变化。

### I. Deterministic checker

至少覆盖：`J_B` 构造/反例、`R~_b` legality、overlap gluing、`R~_a`/orbit（若存在）、native relation residues、旧 C2 no-intertwiner、carrier split S4xC2、no-quotient regressions。

## Kill conditions

- 重新研究 `q` 是否 antibalanced；
- 再比较 binary octahedral / `GL(2,3)`；
- 以 carrier `S4` permutation 直接定义 native motion；
- 把 `J_B` observation window 当几何 slice；
- passive `C2` fiber 充当 cross-block motion；
- carrier switching equivalence quotient native state；
- 用 SO(6)、负轴、经典 rank 降低 P000 六维。

## Success strength

允许：

- `FULL_NATIVE_MIXED_STAR_AND_S4_LIFT_CONSTRUCTED`；
- `PRIMITIVE_JB_AND_b_LIFT_CONSTRUCTED_PARTIAL_OR_GROUPOID_COMPLETION_OPEN`；
- `EXACT_NATIVE_PRIMITIVE_OBSTRUCTION_PROVED`。

任何有效终态都必须在 native 层有可复核结构或最小反例，不能只返回 carrier 代数。
