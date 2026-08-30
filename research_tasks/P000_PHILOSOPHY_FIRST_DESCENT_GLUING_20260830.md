<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-DESCENT-GLUING",
  "title": "哲学先行 Q4：局部切面到 Full-Cell 的 Descent 与胶合",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q4-descent-gluing",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine exactly when compatible local slice, overlap, frame and transport data reconstruct a global Full-Cell object, and whether the first genuine obstruction is already ordinary consistency, a cocycle/holonomy condition, or requires a stronger descent object.",
  "next_action": "Freeze a smallest finite cover-like family of slice observations with explicit overlaps, enumerate local data and compatibility laws, then compare pairwise compatibility against actual global realizability to isolate the first nontrivial descent obstruction.",
  "dependencies": [],
  "source_refs": [
    "projects/enterprise-math/P000_NATIVE_FCC_STRICT_BRIDGE.json@global-main",
    "research_tasks/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_20260830.md@main",
    "classical lens: descent / sheaf gluing, only after exact local-global failure appears"
  ],
  "evidence_status": "DIRECT_USER_PHILOSOPHY_FIRST_DIRECTION / FIRST_WAVE_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "descent",
    "gluing",
    "local-global",
    "slice",
    "holonomy",
    "cocycle",
    "cover"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-DESCENT-GLUING",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PHQ4",
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

# 哲学先行 Q4：局部切面到 Full-Cell 的 Descent 与胶合

Status: `READY / P1 / LOCAL-TO-GLOBAL`

## Mother question

如果多个三轴切面、局部邻域或 frame readout 在重叠处彼此兼容，它们是否必然来自一个全局 Full-Cell？

也就是区分：

\[
\text{pairwise compatible local data}
\]

与

\[
\text{globally realizable native object}.
\]

真正的空间概念应由这个差异逼出来，而不是先宣布存在 site/sheaf。

## Frozen inputs and scope

只使用 P000 允许的 finite Cell/slice/rotation/connection 数据。覆盖关系本身是待研究对象，不先验固定。允许普通图胶合、cocycle、holonomy、descent 语言作比较；只有当 set-valued 胶合确实失败于 automorphism 数据时，才讨论更高层结构。

## Hard target and required outputs

Hard target: `P000_LOCAL_SLICE_TO_FULL_CELL_DESCENT_EXACTLY_CLASSIFIED`

1. 定义最小 cover-like probe family 与 overlap 数据。
2. 枚举 local assignments、pairwise compatible assignments 与 globally realizable assignments。
3. 给出最小 compatibility-not-global counterexample，或证明指定有限类中 pairwise 条件已充分。
4. 若出现 obstruction，分类其是否为普通一致性、loop holonomy、cocycle class、automorphism twisting 或其他类型。
5. 反推出最小覆盖/胶合公理，不得预先照搬经典拓扑覆盖定义。
6. 给出 deterministic finite checker 与至少一个非平凡 local-to-global 定理。

## Research value to preserve

P000 的三轴切面只是整体的局部可见部分。若不先解决“什么局部数据能胶成整体”，任何从单一 slice 推断六维结构的路线都可能把局部表示误当本体。

## Success, kill, and return criteria

有效终态：`EXACT_DESCENT_OBSTRUCTION_FOUND` / `FINITE_LOCAL_COMPATIBILITY_SUFFICIENT_THEOREM` / `CURRENT_SLICE_LANGUAGE_CANNOT_DEFINE_MEANINGFUL_OVERLAP`。若后者成立，应返回最小缺失 relation class，而不是强行引入 sheaf 术语。
