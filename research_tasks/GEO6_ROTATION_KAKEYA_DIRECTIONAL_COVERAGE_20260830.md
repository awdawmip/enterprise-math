<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-ROTATION-KAKEYA-DIRECTIONAL-COVERAGE",
  "title": "高维 Kakeya 的 P000 旋转原生全方向覆盖模型",
  "kind": "RESEARCH",
  "owner": "research/geo6-rotation-kakeya-directional-coverage",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Construct a finite-scale rotation-native Kakeya analogue in P000 by defining direction orbits, Cell paths or tubes, support cost and refinement, then determine nontrivial lower and upper coverage laws without importing Euclidean Hausdorff measure.",
  "next_action": "Choose one declared finite rotation-direction orbit family and one Cell tube or path notion; define support cost at resolution r; compute exact small-r extremizers and prove the first nontrivial refinement law or obstruction.",
  "dependencies": [],
  "source_refs": [
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md@5778529",
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/P000_REALITY_FOUNDATION.json@main"
  ],
  "evidence_status": "EXTERNAL_3D_KAKEYA_SOLVED_2025 / HIGHER_DIMENSIONAL_KAKEYA_OPEN / P000_ROTATION_PRIMARY",
  "last_progress_ref": "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md",
  "last_progress_at": "2026-08-30T02:38:51+00:00",
  "hard_block": null,
  "tags": ["geometry", "P000", "native-6D", "Kakeya", "directional-coverage", "rotation", "Cell-path", "refinement", "external-bridge"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-ROTATION-KAKEYA-DIRECTIONAL-COVERAGE",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6KAK",
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

# 高维 Kakeya 的 P000 旋转原生全方向覆盖模型

## Mother question

给定 P000 的有限分辨率 Cell 模型与声明的 rotation-generated direction orbit set，包含每一个允许方向类的 native Cell path/tube 至少需要占用多少 Cell support？

## Frozen inputs and scope

- 方向只能从声明的 P000 rotation action/readout 生成或分类，不能事后删方向。
- path/tube 必须是 Cell relation 上的 native object；若需要 thickness，明确为分辨率参数。
- cost 使用有限 Cell support、weighted support 或 overlap multiplicity 等 exact 离散量。
- 至少研究两个连续 refinement level。
- 经典高维 Kakeya 只作外部模板；不把欧氏直线、Hausdorff dimension 或 Lebesgue measure 当作 native primitive。

## Hard target and required outputs

Hard target: `P000_ROTATION_NATIVE_DIRECTIONAL_COVERAGE_SCALING_CLASSIFIED`.

必须给出 direction orbit、path/tube、support cost 与 refinement 定义；完成一个 exact finite optimization；给出至少一个非平凡 lower-bound mechanism 和一个 upper construction；分析 rotation symmetry 与 overlap/gluing 的作用；证明至少一个 refinement monotonicity、submultiplicativity、renormalization inequality 或 exact failure certificate；并输出可复核 checker 与 `research_returns/GEO6_ROTATION_KAKEYA_DIRECTIONAL_COVERAGE_RETURN_20260830.md`。

## Research value to preserve

该任务把“旋转是主要几何变换”转成可测代价：方向越丰富，native support 至少增长到什么程度。sharp law 与精确退化 no-go 都有价值。

## Success, kill, and return criteria

Success：得到非退化、rotation-compatible 的 finite-scale coverage invariant，并证明随方向数或 refinement 变化的非平凡界，同时给出 construction 或明确 gap。

有效 kill/no-go：证明当前 direction/path primitives 使全方向覆盖退化为常数规模 support，或 direction classes 本身无 canonical 定义，并定位最小语义缺口。

失败：事后删除难方向、把欧氏直线直接当 Cell path、用经典 Hausdorff 结论替代 native proof、只报优化器数值无 certificate、或重复同一轨道代表制造“全方向”。
