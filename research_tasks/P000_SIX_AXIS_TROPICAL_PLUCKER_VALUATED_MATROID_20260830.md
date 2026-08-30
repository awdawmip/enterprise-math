<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID",
  "title": "P000 六轴 Tropical Plücker / Valuated-Matroid 坍塌几何生存性审计",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-tropical-plucker-valuated-matroid",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine whether any already-admissible six-axis Enterprise weight or valuation semantics yields a nontrivial tropical Plucker / rank-2 valuated-matroid structure, rather than a post-selected or tautological re-encoding of generic six-tuples.",
  "next_action": "Inventory admissible pre-existing scalar weight semantics on the frozen six axis labels, freeze at least one factor-blind candidate before inspecting survivor outcomes, then compute the three complementary pair sums, tropical defect, symmetry law and exact survivor census with adversarial controls.",
  "dependencies": [
    "research_tasks/P000_SIX_AXIS_JOHNSON_PLUCKER_DECOMPOSITION_20260830.md",
    "enterprise_toolbox_registry.json@main"
  ],
  "source_refs": [],
  "evidence_status": "DRIVER_EXTERNAL_THEORY_SCOUTING_COMPLETE / TROPICAL_PLUCKER_INTERFACE_IDENTIFIED / ENTERPRISE_SURVIVOR_STRUCTURE_UNTESTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["P000","six-axis","tropical","Plucker","valuated-matroid","Dressian","valuation","collapse","piecewise-linear","survivor-census"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-TROPICAL-COLLAPSE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000TP1",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 六轴 Tropical Plücker / Valuated-Matroid 坍塌几何生存性审计

Status: `READY / P1 / HIGH / P000-BOUND / SURVIVOR-CENSUS-FIRST`

## Mother question

在冻结的六轴 pair labels 上，经典 tropical Plücker 条件
`min(w_AB+w_CD, w_AC+w_BD, w_AD+w_BC)`
至少两次达到最小值，形式上给出 rank-2 valuated-matroid / tropical `Gr(2,4)` 结构。问题是：**进取数论已有的、语义上合法的六轴 weight/valuation/cost/collapse observables 中，是否真的自然出现这一结构；还是只有通过事后挑选权重、强行取 logarithm/valuation 才能制造出来？**

任务目标是做生存性与判别力审计，不把 tropical vocabulary 本身当作成果。

## Frozen inputs and scope

1. P000 原生空间仍是 6D；tropicalization 只能作用于一个已声明的六轴 scalar field，不是 native geometry 的替代定义。
2. 六标签及 complementary pairs 冻结为 `(AB,CD)`, `(AC,BD)`, `(AD,BC)`。
3. 第一阶段必须从已有或独立有语义依据的 Enterprise quantities 中选择 `w_ij`。禁止观察 survivor 以后再定义 weight。
4. 如果没有任何合法的六轴 scalar semantics，允许以 `NO_ADMISSIBLE_WEIGHT_SEMANTICS` 精确终止；不得为了让定理成立而发明一个只服务于 tropical condition 的观测量。
5. 对每个冻结 weight family，定义 `s1=w_AB+w_CD`, `s2=w_AC+w_BD`, `s3=w_AD+w_BC`，以及 exact tropical defect `delta_T=second_min(s1,s2,s3)-min(s1,s2,s3)`；因此 `delta_T=0` 当且仅当最小值至少出现两次。
6. 若 `w_ij=v(x_ij)` 来自某个 nonarchimedean valuation，必须区分 `Q=0` 导致的经典 valuation consequence 与对非 Plücker states 的真正额外 survivor phenomenon。不得把前者重复包装成新规律。
7. 工具复用优先：valuation/enumeration 使用现有 T1 系列；circuit/cocircuit/matroid typing 使用 T3；群作用与 equivariance 使用 T7。只有明确能力缺口才能提出 extension。
8. 不预设 Dressian、tropical Grassmannian 或 valuated matroid 是 P000 Foundation object；它们只是候选 derived state classes。

## Hard target and required outputs

Hard target:

`P000_TROPICAL_PLUCKER_SURVIVOR_GEOMETRY_NONTRIVIAL_OR_TAUTOLOGICAL_BOUNDARY_EXACTLY_CLASSIFIED`.

### A. Admissible weight registry

列出至少一组、优先多组 pre-outcome frozen weight semantics。每组必须说明输入对象和 coefficient domain、为什么在六轴上都有定义、是否 factor-blind / route-blind、对 carrier `S4` 与 complement `c` 如何变换、是否依赖额外 orientation/frame/hidden state。若没有 admissible family，直接给出 exact typing obstruction。

### B. Tropical defect calculus

对每组 weight：

- 推导 `delta_T` 的 exact piecewise-linear formula；
- 证明其 `S4`/`c` transformation law；
- 分类 `delta_T=0`, `>0` 的 orbit/stabilizer types；
- ties multiplicity 3 单独分类；
- 检查它是否可由已有单轴 statistics、Johnson spectral sectors 或 Pfaffian residue直接重构。

### C. Valuated-matroid criterion

严格核验 rank-2 four-ground-element valuated-matroid typing。若只有某个子族满足条件，给 necessary/sufficient criterion；若条件在当前 weight semantics 下自动成立，标记为 tautological consequence，而不是新结构。

### D. Survivor census and adversarial controls

至少包括 exact small-box census、symmetry-stratified census、deterministic adversarial families、保持已有 coarse observables 相同但改变 `delta_T` 的 matched controls，以及保持 `delta_T` 相同但改变 arithmetic/geometry labels 的 matched controls。survivor density 只在 exact finite range 内陈述。

### E. Collapse interpretation gate

只有在证明 `delta_T` 或 tropical cell decomposition 与某个已有 Enterprise collapse/transport quantity存在 exact nontrivial relation 后，才允许使用“tropical collapse geometry”称呼。否则保持“six-weight piecewise-linear classifier”。

必须区分：`piecewise-linear classifier != native collapse law != factorization mechanism`。

### F. Classical-to-tropical bridge

如果前一任务的 Pfaffian `Q` 可用，证明或否定：

- `Q=0` 加 valuation 是否强制 tropical Plücker；
- `Q!=0` 时 valuation of `Q` 与 `delta_T` 的关系；
- cancellation 能否让只看 valuations 的模型丢失关键 residue；
- 是否存在同 valuations / 不同 `Q` 的最小反例。

### G. Deterministic checker

提交 exact checker/certificate，验证 pair sums、ties、`delta_T`、group action、survivor classification 与所有有限 census。不得使用浮点 tolerance 判 tie。

## Research value to preserve

这条路线第一次把同一组六轴 complementary pairs 从 quadratic Plücker algebra 送入 `min/+` 的 piecewise-linear 世界。如果它 survives，可能给“坍塌/最低层/valuation”提供一个不依赖欧氏长度的六轴分类器，并把 algebraic relation、matroid combinatorics 与离散 cost geometry 连在一起。

若它不 survives，精确 no-go 同样重要：它会说明 tropical Plücker 只是对特定 `Q=0`/valuation families 的经典影子，不能作为进取数论的新通用结构，从而阻止后续把大量 tropical 名词误当新公理。

## Success, kill, and return criteria

成功必须满足至少一项：

- 找到 pre-frozen、语义合法的 Enterprise weight family，其中 tropical survivor class 非空、非全体、非由已有单一 observable 平凡决定，并给出 exact characterization；
- 证明 `delta_T` 与一个现有 collapse/transport invariant 有新的 exact relation；
- 得到清晰 all-family obstruction，证明当前 admissible weight semantics 下 tropical condition 只能是经典 Plücker/valuation 的影子。

Kill / downgrade：weight 是看到答案后才定义；通过任意 monotone transform 调参直到 survivor 出现；只对 `Q=0` states 重证标准 valuation consequence；把有限频率提升成无限定理；把 tropical locus 直接称为 native 6D geometry；新建与 T1/T3/T7 重复的通用工具。

Return 必须给 frozen weight semantics、exact theorems/no-go、survivor/control tables、checker、与 Johnson/Pfaffian 层的关系，以及明确 verdict：`NONTRIVIAL_SURVIVOR`, `TAUTOLOGICAL_CLASSICAL_SHADOW`, `NO_ADMISSIBLE_WEIGHT`, 或 `INCONCLUSIVE_WITH_EXACT_BOUNDARY`。
