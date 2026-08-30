<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-RESIDUE-ONTOLOGY",
  "title": "哲学先行 Q5：Kernel/Relation Residue 的本体分类",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q5-residue-ontology",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Classify whether lifted relation residues and hidden kernels are disposable presentation artifacts, gauge-dependent coordinates, stable enriched-state invariants, holonomy-like data, or genuine obstructions, rather than treating every nonidentity residue as an error to eliminate.",
  "next_action": "For small finite extension models, vary lift representatives and gauge/frame choices exhaustively, compute the orbits of A^3, B^2 and (AB)^4 inside K, and isolate the strongest quotient-free invariant retained across allowed equivalences.",
  "dependencies": [],
  "source_refs": [
    "research_tasks/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_20260830.md@main",
    "projects/enterprise-math/P000_NATIVE_FCC_STRICT_BRIDGE.json@global-main",
    "classical lens: split/non-split extensions, nonabelian cohomology when hypotheses permit"
  ],
  "evidence_status": "DIRECT_USER_PHILOSOPHY_FIRST_DIRECTION / FIRST_WAVE_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "kernel",
    "relation-residue",
    "obstruction",
    "holonomy",
    "gauge",
    "extension"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-RESIDUE-ONTOLOGY",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PHQ5",
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

# 哲学先行 Q5：Kernel/Relation Residue 的本体分类

Status: `READY / P1 / DEFECT-AS-OBJECT`

## Mother question

对 lift \(A,B\) 的

\[
z_a=A^3,\qquad z_b=B^2,\qquad z_{ab}=(AB)^4\in K,
\]

为什么默认目标应该是“把 residue 消掉”？

更基础的问题是：在允许的换 lift、frame/gauge 变化和模型同构下，哪些 residue 只是表示，哪些保留为真正 enriched-state invariant 或 obstruction？

## Frozen inputs and scope

不得通过 quotient hidden kernel 来制造 exact \(S_4\)。普通 group extension、Schreier theory、中心/阿贝尔情形的 \(H^2\) 只作为经典工具，必须核对适用条件。P000 native identity 与 carrier readout 继续分 sort。

## Hard target and required outputs

Hard target: `P000_KERNEL_AND_RELATION_RESIDUE_ONTOLOGY_EXACTLY_CLASSIFIED`

1. 在若干最小 finite extension 中枚举所有 lift representatives。
2. 精确计算 \(z_a,z_b,z_{ab}\) 在换 lift、conjugation、gauge 变化下的轨道。
3. 定义并证明至少一种 quotient-free residue invariant，或证明给定模型类不存在这种非平凡 invariant。
4. 区分 `PRESENTATION_ARTIFACT` / `GAUGE_COVARIANT_DATA` / `ENRICHED_INVARIANT` / `OBSTRUCTION_CLASS`。
5. 构造 residue 非平凡但结构合法的正例，以及 residue 导致 no-section/no-lift 的反例。
6. 给出何时可以使用普通 \(H^2\)、何时必须转向非阿贝尔 extension 数据的明确边界。

## Research value to preserve

“缺陷”有时正是新对象。若 relation residue 承载局部—整体或隐藏状态信息，把它消掉等于主动丢弃进取几何最可能的新结构。

## Success, kill, and return criteria

有效终态：`NONTRIVIAL_RESIDUE_INVARIANT_CLASSIFIED` / `ALL_ALLOWED_RESIDUES_GAUGE_REMOVABLE_IN_DECLARED_CLASS` / `RESIDUE_LANGUAGE_TOO_WEAK_WITH_EXACT_COUNTERMODEL`。禁止把经典 cohomology 名称本身当作新发现。
