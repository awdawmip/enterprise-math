<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 混合三轴切面与状态级 S4 旋转提升 / Z2 holonomy 障碍 V4",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "After accepting the strict Gen2 axis-type/FCC bridge, star-complement obstruction and nontrivial chart-local Z2 holonomy, construct the three mixed native K4-star slices and a state-level lift of the accepted FCC S4 generators, or prove the exact native obstruction/minimal state extension. The old clone-product whole-factor C2 route is now excluded as a direct FCC-S4 lift.",
  "next_action": "Treat J_A={1,2,3}, J_B={1,4,5}, J_C={2,4,6}, J_D={3,5,6} as observation windows only; attempt to endow J_B,J_C,J_D with legal native Cell slice structures compatible on overlaps, then construct native lifts of a=(BCD), b=(AB) and classify whether the S4 relations close exactly or leave a chart/hidden Z2 cocycle or other obstruction.",
  "dependencies": [
    "p000_reality_foundation.json@main",
    "definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md@main",
    "research_returns/P000_6D_AXIS_MIXING_ROTATION_ALGEBRA_FORMULA_V2_RETURN_20260829.md@main",
    "driver_reviews/P000_FCC_SIX_LINE_ROTATION_ALGEBRA_DRIVER_REVIEW_20260829.md@main",
    "research_returns/P000_L1_NATIVE_FCC_CARRIER_BRIDGE_V2_RETURN_20260829.md@main",
    "driver_reviews/P000_NATIVE_FCC_STRICT_BRIDGE_GEN2_DRIVER_REVIEW_20260829.md@main"
  ],
  "evidence_status": "GEN2_STRICT_BRIDGE_ACCEPTED / STAR_COMPLEMENT_OBSTRUCTION_FROZEN / GLOBAL_SIGN_SECTION_OBSTRUCTED / MIXED_NATIVE_GEOMETRY_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","FCC","S4","mixed-slice","Z2-holonomy","state-lift","group-extension","groupoid","rotation"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000NATFCC4",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "successor_gate": {
    "new_information_gap": "Gen2 proved only an axis-type/L1-edge bridge and K4 observation atlas, while also proving that the old complementary factor slices and whole-factor C2 exchange cannot realize the FCC star/S4 geometry and that global chart orientation has nontrivial Z2 holonomy. It remains unknown whether mixed native star slices exist and whether carrier S4 has any state-level native lift after the necessary local orientation data are retained.",
    "why_parent_result_does_not_close_it": "RR-A8EDE17557A1C30BC189 explicitly leaves MIXED_NATIVE_STAR_SLICE_GEOMETRY_AND_STATE_LEVEL_S4_LIFT_NOT_PROVED. It classifies the old model as too small rather than proving a universal native no-go.",
    "discriminating_outcomes": [
      "construct J_B,J_C,J_D as legal native Cell slices and obtain exact state-level lifts of a,b closing to S4",
      "construct a typed lift only after adjoining minimal chart/orientation/hidden state, yielding a nontrivial extension, cocycle, groupoid or double-cover-like algebra derived from the model",
      "prove an exact obstruction to all such mixed-slice/state-level lifts under the current native Cell axioms and identify the minimal additional axiom/data needed"
    ],
    "kill_condition": "Any result that redoes K4/S4, reuses the old whole-factor rho as the lift, ignores the frozen Z2 holonomy, simply declares J_B/J_C/J_D to be geometric slices, identifies chart signs with native negative axes, or quotients hidden native state by carrier readout is nonresponsive.",
    "alternative_route_or_free_exploration_considered": "Reinterpreting the clone-product C2 as an FCC rotation is now exactly killed by the star/complement obstruction. More carrier Rubik-word enumeration is also downstream-only. The remaining high-leverage route is mixed native slice construction plus state-level lift or exact obstruction.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is Generation 4 of the existing bridge task. Generation 3 was published while the valid Gen2 lease was in flight and therefore predates the new obstruction/holonomy result; Gen4 folds that late accepted evidence into the canonical execution target."
  }
}
-->

# P000 混合三轴切面与状态级 S4 旋转提升 / Z2 holonomy 障碍 V4

Status: `READY / GENERATION-4 / P0 / P000-BOUND / MIXED-SLICE-AND-STATE-LIFT`

## Mother question

已冻结 carrier 代数：

\[
O_{FCC}\cong S_4,
\qquad
R_\sigma(L_{ij})=L_{\sigma(i)\sigma(j)}.
\]

已冻结 strict native/carrier bridge：六个 native axis **types** 与六条 FCC unoriented line families 有显式 bijection，且四个 observation windows

\[
J_A=\{1,2,3\},\quad
J_B=\{1,4,5\},\quad
J_C=\{2,4,6\},\quad
J_D=\{3,5,6\}
\]

在 carrier readout 下是 K4 四个 stars。

但只有 `J_A` 已是建立过的 native three-axis geometric slice；旧 clone-product 的互补 `I_B` 映到 opposite triangle，不是 star，旧 whole-factor `rho` 不能成为 FCC-S4 lift；同时四 chart orientation 存在不可消去的 Z2 loop holonomy `-1`。

本任务只问：

\[
\boxed{\text{这些 mixed observation windows 能否升级成真正 native slices，并承载 state-level rotation?}}
\]

若可以，逼出完整状态级代数；若不可以，逼出 exact obstruction。

## Frozen results — 禁止重做

1. P000: native spatial dimension=6, time separately typed；
2. FCC is the selected primary carrier；
3. FCC six-line/four-slice incidence exactly K4；
4. carrier proper rotation skeleton exactly S4；
5. carrier generators `a=(BCD)`, `b=(AB)`；
6. carrier support action-groupoid / conjugation / commutator / Rubik-word calculus accepted；
7. axis-type bridge `beta` accepted；
8. K4 observation windows `J_A..J_D` accepted only as observation incidence；
9. complementary factor slices cannot both be K4 stars；
10. old whole-factor `rho` has no FCC-S4 intertwiner；
11. no global signed six-line section realizes all four 120-degree charts；
12. every triangular chart loop has gauge-invariant Z2 holonomy `-1`；
13. FCC/HCP antipodal-pair regression `6/3` accepted。

## P000 guards

- `J_i` observation window != geometric slice until constructed；
- chart-local sign != native negative axis；
- carrier vector zero-sum != native axis relation；
- carrier readout collision != native state equality；
- no rank/embedding argument may reduce native 6D；
- six axes are not declared pairwise 120°；
- time remains trace/order, not spatial rotation coordinate。

## Hard target

`P000_MIXED_NATIVE_STAR_SLICES_AND_STATE_LEVEL_ROTATION_LIFT_OR_EXACT_OBSTRUCTION_CLASSIFIED`

Valid terminal classes:

- `MIXED_NATIVE_STAR_SLICES_AND_EXACT_S4_LIFT_CONSTRUCTED`；
- `MIXED_SLICES_CONSTRUCTED_BUT_ROTATION_REQUIRES_NONTRIVIAL_EXTENSION_OR_GROUPOID`；
- `EXACT_MIXED_SLICE_OR_STATE_LEVEL_LIFT_OBSTRUCTION_PROVED`。

## Required outputs

### A. Mixed native slice admissibility

For each of `J_B,J_C,J_D`, define or refute a native Cell slice structure. A successful construction must specify:

- native states/cells visible in the slice；
- adjacency/legal moves；
- overlap with the other three slices；
- relation to the established `J_A=I_A` three-positive-axis Cell geometry；
- what survives under chart transport。

Merely naming a 3-subset a slice is forbidden.

### B. Overlap/gluing law

For every pair `J_i,J_j`, the shared native axis must have an exact transition law. Determine whether the frozen carrier transition sign `q_ij` is:

- pure readout gauge；
- the shadow of additional native orientation state；
- or an obstruction to the proposed slice gluing。

Triple-loop transport must be computed, not hand-waved.

### C. Minimal state extension test

Start with the smallest candidate native state supporting the four mixed slices. If a state-level lift fails, test minimal extra state in increasing strength:

1. chart label；
2. one Z2 orientation bit / torsor fiber；
3. overlap/incidence state；
4. support/domain state；
5. other explicitly derived finite hidden state。

Do not add state unless the exact obstruction demands it.

### D. Lift the carrier generators

Construct or obstruct native transformations `tilde R_a`, `tilde R_b` corresponding to

`a=(BCD)`, `b=(AB)`.

They must preserve the declared native relations and transport mixed slices consistently. Give a typed readout `Phi` such that, where defined,

\[
\Phi(\widetilde R_g x)=R_g^{FCC}(\Phi(x)).
\]

### E. Test the group relations in native state

Compute exactly the fate of

\[
a^3=e,\qquad b^2=e,\qquad (ab)^4=e.
\]

At native level each relation must be classified as:

- strict identity；
- identity only after carrier readout；
- nontrivial hidden residue / holonomy；
- undefined without groupoid domain transport。

If a carrier identity leaves native residue, record the residue rather than quotienting it away.

### F. Z2 holonomy algebra classification

The frozen chart loop holonomy is `-1`. Determine whether this induces, for the actual native lift problem:

- no additional algebra beyond chart gauge；
- a nontrivial 1-cocycle/2-cocycle；
- a central extension of part/all of carrier S4；
- a double-cover-like rotation algebra；
- a groupoid/gerbe-like local transport object；
- or a different exact structure。

These are candidates, not assumptions. Give exact multiplication/relations or exact no-go.

### G. Supported local moves

Revisit the accepted carrier supported move/groupoid only after a state-level/global generator lift exists. Determine whether carrier-localized commutators remain local on full native state or leave hidden support residue.

Mandatory regression:

`[U_A,U_B]=(AB AC BC)` at carrier readout strength.

### H. Time trace and path dependence

If two native rotation words yield the same final carrier readout but distinct hidden/orientation state, provide a time-ordered witness:

`(X_t, g_t, Phi(X_t))`。

This is a candidate native holonomy observable. Time remains ordering only.

### I. Obstruction taxonomy

At minimum distinguish:

- `MIXED_SLICE_ADMISSIBILITY_OBSTRUCTION`；
- `OVERLAP_GLUE_OBSTRUCTION`；
- `Z2_ORIENTATION_HOLONOMY_OBSTRUCTION`；
- `NATIVE_RELATION_NOT_PRESERVED`；
- `CARRIER_RELATION_HAS_NATIVE_RESIDUE`；
- `SUPPORT_DOMAIN_OBSTRUCTION`；
- `STATE_EXTENSION_INSUFFICIENT`。

Give smallest witnesses.

### J. Deterministic checker

Provide an exact finite checker for every finite incidence/group/cocycle claim and bounded exhaustive search used. No floating-only acceptance.

## Kill conditions

The task fails if it:

- redoes the 24 FCC rotations or K4/S4；
- claims the old clone-product `rho` is the lift；
- silently promotes `J_B,J_C,J_D` to native geometry；
- ignores the accepted `-1` holonomy；
- declares a central/double cover merely by analogy；
- interprets chart sign as native negative axis；
- identifies native states through carrier kernel；
- uses SO(6) as native definition；
- or reduces native 6D by classical carrier rank。
