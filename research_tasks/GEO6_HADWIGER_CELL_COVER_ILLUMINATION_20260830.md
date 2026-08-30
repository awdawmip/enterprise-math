<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-HADWIGER-CELL-COVER-ILLUMINATION",
  "title": "六维 Hadwiger 模板与 P000 Cell 覆盖照明界",
  "kind": "RESEARCH",
  "owner": "research/geo6-hadwiger-cell-cover-illumination",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Define native Cell covering and illumination operations under declared translation or rotation actions and establish nontrivial finite six-dimensional bounds or an exact obstruction to transferring the Hadwiger covering paradigm.",
  "next_action": "Freeze one finite native object family, one allowed transformation family and one cover/illumination predicate; compute exact small-model cover numbers; then derive symmetry-based upper constructions and independent lower certificates.",
  "dependencies": [],
  "source_refs": [
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md@5778529",
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/P000_REALITY_FOUNDATION.json@main"
  ],
  "evidence_status": "EXTERNAL_HADWIGER_GENERAL_OPEN / CLASSICAL_2_POWER_6_TARGET_HEURISTIC_ONLY / P000_NATIVE_COVER_SEMANTICS_UNFROZEN",
  "last_progress_ref": "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md",
  "last_progress_at": "2026-08-30T02:38:51+00:00",
  "hard_block": null,
  "tags": ["geometry", "P000", "native-6D", "Hadwiger", "covering", "illumination", "rotation", "external-bridge"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-HADWIGER-CELL-COVER-ILLUMINATION",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6HAD",
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

# 六维 Hadwiger 模板与 P000 Cell 覆盖照明界

## Mother question

在 P000 native Cell geometry 中，给定明确的对象类和允许的 translation/rotation action，覆盖一个对象或“照明”其全部边界/关系方向最少需要多少变换副本或方向操作？

## Frozen inputs and scope

- cover/illumination predicate 必须由 native Cell membership、relation、boundary 或 direction readout 定义。
- 经典 Hadwiger 猜想与六维 `2^6=64` 只作结构与数值 heuristic，不作为 native target theorem。
- translation/rotation action 必须显式声明；不同 action family 分开统计。
- 先做 finite exact model 与可证明 bounds，再考虑 refinement。

## Hard target and required outputs

Hard target: `P000_NATIVE_CELL_COVER_ILLUMINATION_BOUNDS_ESTABLISHED_OR_TRANSFER_NO_GO`.

必须定义 native cover number 与至少一种 illumination/directional variant；完成 exact small-model census；给出 symmetry-based upper construction 与 independent lower certificate；分析 rotation/translation/refinement；与 classical Hadwiger 结构做明确 transfer/no-transfer 分类；提供 deterministic checker；输出 `research_returns/GEO6_HADWIGER_CELL_COVER_ILLUMINATION_RETURN_20260830.md`。

## Research value to preserve

覆盖问题直接测试 Cell support、边界、旋转和局部—整体关系。如果 native cover number 稳定存在，它可能成为以后 packing、Kakeya 和 duality 任务的共同压力测试；若不存在，也能定位缺失的 action/boundary 语义。

## Success, kill, and return criteria

Success：在声明模型类上得到非平凡 cover/illumination 上下界，最好包含 exact extremizer 或 sharp small-model classification，并明确 classical comparison 的合法强度。

有效 kill/no-go：证明 cover number 对 representation/action choice 极端敏感，当前 primitives 无 canonical 定义，或所有自然定义都退化为对象大小的平凡界。

失败：直接把 classical 64 当 native 答案、把欧氏凸体覆盖定义原样搬入、只给启发式图示、或只做优化无 lower certificate。
