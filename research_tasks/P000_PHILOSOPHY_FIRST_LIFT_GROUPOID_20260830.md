<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-LIFT-GROUPOID",
  "title": "哲学先行 Q3：S4 Lift 群胚与选择问题重构",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q3-lift-groupoid",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Replace the question of choosing one carrier-compatible S4 lift by the intrinsic structure of all admissible lifts and equivalences over each Full-Cell model, and test whether existence, no-lift, hidden-kernel and noncanonical-choice regimes become fibers of one exact groupoid-valued construction.",
  "next_action": "Define the lift objects and allowed morphisms over a declared finite model class, recover Gen12 as a rigid trivial-kernel fiber, then construct nontrivial automorphism, multi-section and empty-fiber examples without quotienting away relation residue.",
  "dependencies": [],
  "source_refs": [
    "research_tasks/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_20260830.md@main",
    "research_returns/P000_BASE_CELL_RA_STAR_ORBIT_V12_RETURN_20260830.md@main",
    "projects/enterprise-math/P000_NATIVE_FCC_STRICT_BRIDGE.json@global-main",
    "classical lens: group extensions / torsors / groupoids of choices"
  ],
  "evidence_status": "DIRECT_USER_PHILOSOPHY_FIRST_DIRECTION / FIRST_WAVE_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "S4",
    "lift",
    "groupoid",
    "moduli",
    "section",
    "kernel",
    "canonicality"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-LIFT-GROUPOID",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PHQ3",
  "origin_kind": "DIRECT_USER_DIRECTION",
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

# 哲学先行 Q3：S4 Lift 群胚与选择问题重构

Status: `READY / P0 / ALL-CHOICES-NOT-ONE-CHOICE`

## Mother question

当前若问“选哪个 \(S_4\) lift”，可能已经把非典范性误当成缺陷。对每个允许的 Full-Cell model \(M\)，应先研究全部合法 lift 及其等价：

\[
\mathbf{Lift}_{S_4}(M).
\]

这个对象是否能同时容纳 rigid witness、多个等价 section、hidden kernel、relation residue 与 no-lift？

## Frozen inputs and scope

Gen12 的 split faithful \(K=1\) 模型只作 regression，不作为一般模型定义。Gen13 的 \(q:\widetilde G\to S_4\)、kernel 与 residue 可直接使用。箭头必须来自实际允许的 primitive-preserving/gauge/kernel equivalence；不得凭空增加形式同构。先做 finite groupoid，不预设 stack。

## Hard target and required outputs

Hard target: `P000_S4_LIFT_GROUPOID_AND_FIBER_REGIMES_EXACTLY_CLASSIFIED`

1. 给出 \(\mathbf{Lift}_{S_4}(M)\) 的对象与 morphism 的严格定义。
2. 证明定义在允许的 model isomorphism 下保持不变。
3. 将 Gen12 重现为一个 rigid/trivial-kernel fiber。
4. 构造至少一个多对象或非平凡 automorphism fiber；若不可能，给 exact no-go。
5. 构造 empty fiber 与非 empty fiber 的最小差异证书。
6. 区分“存在某个 lift”“所有 lift 同构”“存在唯一同构类”“存在无 automorphism 的唯一对象”四种强度。
7. 给出与 Gen13 extension/section 语言之间的等价或严格差异定理。

## Research value to preserve

把“任取一个 section”改写为“研究所有选择及其对称性”，可以把 noncanonicality 从模糊警告变成数学对象，并防止把一个漂亮 witness 误称为 native 结构。

## Success, kill, and return criteria

有效终态：`LIFT_GROUPOID_FINITE_CLASSIFICATION` / `GROUPOID_REFORMULATION_COLLAPSES_TO_ORDINARY_EXTENSION_THEORY` / `CURRENT_MORPHISM_LANGUAGE_INSUFFICIENT_WITH_EXACT_GAP`。如果群胚语言没有增加任何可区分的结构，应明确杀死该升级。
