<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 原生六轴到 FCC-S4 旋转代数的等变桥接 V3",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Consume the Driver-accepted FCC carrier S4/action-groupoid rotation algebra and determine whether an explicit P000 native six-axis Cell state admits an exact equivariant native-to-FCC rotation/readout bridge for global generators and supported arrows, or prove the exact obstruction/minimal additional native state required, without quotienting native six-dimensional identity by carrier relations.",
  "next_action": "Freeze one explicit full native Cell state X6 with E_1,...,E_6 and native adjacency/rotation typing; define Phi into the frozen FCC six-line/four-slice atlas; lift a=(BCD) and b=(AB) equivariantly or produce the smallest exact obstruction, then classify word and supported-groupoid consequences.",
  "dependencies": [
    "p000_reality_foundation.json@main",
    "definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md@main",
    "research_returns/P000_6D_AXIS_MIXING_ROTATION_ALGEBRA_FORMULA_V2_RETURN_20260829.md@main",
    "research_result_records/RS-P000-6D-AXIS-MIXING-ROTATION-GROUPOID/RR-774CF0739BD6CD117CF6.json@main",
    "driver_reviews/P000_FCC_SIX_LINE_ROTATION_ALGEBRA_DRIVER_REVIEW_20260829.md@main"
  ],
  "evidence_status": "DRIVER_ACCEPTED_CARRIER_S4_INTERFACE / NATIVE_EQUIVARIANT_LIFT_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","FCC","S4","equivariant-lift","rotation","groupoid","bridge","six-axis","readout"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000NATFCC3",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-6D-AXIS-MIXING-ROTATION-GROUPOID",
  "successor_gate": {
    "new_information_gap": "The carrier rotation algebra is now exact: K4 incidence, O_FCC congruent to S4, faithful six-line/four-slice actions, support action-groupoid, conjugation, commutator localization and word calculus are accepted. What remains unknown is whether these carrier actions are readouts of legal native transformations on full P000 six-axis Cell states.",
    "why_parent_result_does_not_close_it": "RR-774CF0739BD6CD117CF6 explicitly freezes NATIVE_TO_FCC_EQUIVARIANT_LIFT_NOT_PROVED and forbids identifying carrier faithfulness with native state identity.",
    "discriminating_outcomes": [
      "construct an exact native action lifting the accepted global S4 generators and extend it equivariantly to all carrier words",
      "construct only a typed partial/groupoid native lift and classify its exact domains/codomains",
      "prove no such lift exists for the chosen native state/readout and identify the minimal hidden orientation/incidence/support state required"
    ],
    "kill_condition": "Any result that merely declares E_i=L_i, treats the carrier S4 permutation as a native rotation by definition, quotients distinct native states because they share one FCC readout, imports SO(6) without native derivation, or redoes K4/S4 instead of solving the lift is nonresponsive.",
    "alternative_route_or_free_exploration_considered": "Reopening FCC versus HCP, enlarging the carrier rotation census, and deriving more Rubik words were rejected because the accepted carrier interface already closes those questions at task strength. The only high-leverage continuation is the native equivariant lift or an exact obstruction.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is Generation 3 of the existing canonical bridge task, not a duplicate. It consumes the new accepted carrier algebra that did not exist when Generation 2 was published."
  }
}
-->

# P000 原生六轴到 FCC-S4 旋转代数的等变桥接 V3

Status: `READY / GENERATION-3 / P0 / P000-BOUND / CARRIER-S4-CONSUMER`

## Mother question

在 P000 完整原生六轴 Cell state 与已经 Driver 验收的 FCC carrier 旋转代数之间，构造 typed readout

\[
\Phi:X_6\to C_{FCC}
\]

以及原生旋转 `tilde R_sigma`，使至少对 accepted generators `a=(BCD)`、`b=(AB)` 满足

\[
\boxed{\Phi(\widetilde R_\sigma x)=R_\sigma^{FCC}(\Phi(x))}.
\]

如果做不到，必须精确证明 obstruction，并指出最少还缺哪一种 native orientation / incidence / support state。

## Frozen inputs — 不得重做

1. 四切面六线 incidence = `K4`；
2. `O_FCC ~= S4` 是 orientation-preserving FCC carrier rotation skeleton；
3. `R_sigma(L_ij)=L_sigma(i)sigma(j)`；
4. 六 carrier-slot update law；
5. `a=(BCD)`, `b=(AB)` 生成全部 `S4`；
6. support invariant iff identity-outside extension is an ambient permutation；
7. non-invariant support 是 action-groupoid arrow；
8. exact conjugation/setup law；
9. accepted commutator localization theorem；
10. finite Rubik-word calculus 与三类 accepted algorithms。

当前唯一硬缺口：`NATIVE_TO_FCC_EQUIVARIANT_LIFT_NOT_PROVED`。

## P000 guards

- `NATIVE_AXIS_COUNT=6` 来自 P000；
- `FCC_CARRIER_READOUT_IS_NOT_NATIVE_IDENTITY`；
- `CARRIER_FAITHFULNESS != NATIVE_STATE_IDENTITY`；
- `[v]={v,-v}` 只是 carrier unoriented line，不导入 native negative axis；
- 经典 carrier 线性关系不得降低 native 6D；
- 不得宣称六轴两两 120°；
- time 只记录关系变化顺序，不参加空间旋转群。

## Hard target

`P000_NATIVE_TO_FCC_S4_EQUIVARIANT_ROTATION_BRIDGE_EXACTLY_CLASSIFIED`

允许三个有效终态：

- `FULL_GLOBAL_EQUIVARIANT_LIFT_CONSTRUCTED`；
- `TYPED_PARTIAL_OR_GROUPOID_LIFT_CLASSIFIED`；
- `EXACT_NATIVE_LIFT_OBSTRUCTION_PROVED`。

## Required outputs

### A. 显式完整 native state model

必须声明完整六轴 Cell state、native adjacency/legal relation，以及 orientation、incidence、support、payload 的 typing。遗漏 coordinate 不得自动置零。

### B. 定义 readout `Phi`

至少输出六 line-family labels、四 slice labels、必要的 chart orientation 与 support/domain readout。分类 `Phi` 的 injectivity、collision/fiber、hidden state；禁止 `Phi(x)=Phi(y)` 自动推出 `x=y`。

### C. 先提升两个 generators

寻找合法 native transforms `tilde R_a`, `tilde R_b` 并检验：

`Phi o tildeR_a = R_a^FCC o Phi`；

`Phi o tildeR_b = R_b^FCC o Phi`。

其中任一失败都必须给 smallest exact witness，不能跳过。

### D. 扩展到 algorithm words

若两个 generator 可提升，检查 carrier relations `a^3=e`, `b^2=e`, `(ab)^4=e` 在 native 层是严格 identity、只在 readout 后 identity，还是留下 hidden holonomy/cocycle。若 carrier identity 在 native 留 residue，必须报告，不得 quotient 掉。

### E. 提升 supported action-groupoid

对 `m[Omega,sigma]:Omega -> R_sigma(Omega)` 给 native source/target domain、support transport、hidden-state transport、inverse 与 composition。non-invariant support 禁止伪造成 global permutation。

### F. native conjugation / commutator fate

检验 accepted setup formula 在 native 层是否严格成立或出现额外 cocycle。特别检查 `[U_A,U_B]=(AB AC BC)`：它在 native state 是否仍局域，还是仅 carrier readout 局域而 hidden state 有更大 support。

### G. 时间顺序

若不同 native paths 有相同 final carrier readout，记录 time-ordered trace `(X_t, tildeR_t, Phi(X_t))` 并判断历史是否区分 hidden state。time 不得变成第七空间轴。

### H. Obstruction taxonomy

失败时至少区分：`STATE_FIBER_OBSTRUCTION`、`ORIENTATION_STATE_MISSING`、`INCIDENCE_STATE_MISSING`、`SUPPORT_DOMAIN_OBSTRUCTION`、`RELATION_NOT_PRESERVED`、`CARRIER_RELATION_HAS_NATIVE_HOLONOMY`，并给 smallest witness。

### I. Regressions

保留 accepted C2/two-shot tomography、FCC primary carrier、HCP non-central-symmetry、A3 support/domain warning，以及本次 accepted S4 carrier algebra/checker。

### J. Deterministic checker

至少验证 generator equivariance 或最小 obstruction、native relation preservation、word relations、support/groupoid typing、carrier-vs-native hidden residue 与所有 finite regressions。

## Kill conditions

以下不能关闭任务：直接定义 `E_i:=L_i`；把 `S4` 宣布为 full native rotation group；用 carrier kernel quotient native states；只验 carrier equations 不定义 native state；导入任意 `SO(6)` 替代 native derivation；重做 24 rotations/K4/S4；继续做更多 Rubik words 却不处理 native lift；用 classical rank/embedding 降维。
