<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-MAHLER-DUAL-SUPPORT-PRODUCT",
  "title": "六维 Mahler 模板与 P000 离散对偶支撑乘积",
  "kind": "RESEARCH",
  "owner": "research/geo6-mahler-dual-support-product",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Determine whether P000 admits a nontrivial native support-duality construction with an extremal complexity product analogous in structure, but not definition, to Mahler volume product; otherwise prove an exact duality obstruction.",
  "next_action": "Freeze one finite native object class and one relation-derived support functional; define a candidate dual or incidence-complement object without Euclidean polarity; test involutivity, rotation covariance and product bounds on exact small models.",
  "dependencies": [],
  "source_refs": [
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md@5778529",
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/P000_REALITY_FOUNDATION.json@main"
  ],
  "evidence_status": "EXTERNAL_SYMMETRIC_MAHLER_OPEN_IN_DIMENSION_6 / P000_NATIVE_POLARITY_NOT_ASSUMED",
  "last_progress_ref": "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md",
  "last_progress_at": "2026-08-30T02:38:51+00:00",
  "hard_block": null,
  "tags": ["geometry", "P000", "native-6D", "Mahler", "duality", "support", "extremal-product", "external-bridge"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-MAHLER-DUAL-SUPPORT-PRODUCT",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6MAH",
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

# 六维 Mahler 模板与 P000 离散对偶支撑乘积

## Mother question

P000 的 finite Cell objects 是否存在一个完全由 native relation/incidence/support 数据定义的对偶操作，使对象与对偶对象之间出现非平凡 extremal product law？若不存在，阻止离散对偶的最小结构障碍是什么？

## Frozen inputs and scope

- 不把 convex body、polar body、volume 或 Euclidean inner product 当作 native primitive。
- dual candidate 必须从声明的 Cell relation、incidence、support 或 admissibility 数据构造。
- 经典 Mahler 只提供“原对象—对偶对象—极值乘积”的结构模板。
- 必须检验 involutivity、information loss、rotation covariance 与 refinement behavior。

## Hard target and required outputs

Hard target: `P000_DISCRETE_DUAL_SUPPORT_PRODUCT_DEFINED_AND_EXTREMAL_STRUCTURE_CLASSIFIED_OR_DUALITY_NO_GO`.

必须给出 native support functional 与 dual candidate；分类 dual-of-dual；定义非平凡 complexity/product quantity；在 exact finite model class 上建立 lower/upper extremal statement 或 no-go；给出 extremizer/counterexample；分析 rotation/refinement；提供 checker；输出 `research_returns/GEO6_MAHLER_DUAL_SUPPORT_PRODUCT_RETURN_20260830.md`。

## Research value to preserve

若成功，这会为进取数论增加“原对象—对偶对象”这一新的几何组织原则；若失败，则会精确说明为何经典凸几何的 polarity 不能无条件进入 Cell 世界。

## Success, kill, and return criteria

Success：得到 nontrivial native duality 与可证明的 product bound/extremal classification，且不是定义性恒等式。

有效 kill/no-go：证明任何自然 dual candidate 都不可逆、依赖额外 metric/order datum，或 product 可任意退化，从而当前 primitives 不支持 canonical dual-support theory。

失败：直接复制 classical polar、把体积换名后称 native invariant、只看少量对称例、或通过定义 dual 使 product 人为恒定。
