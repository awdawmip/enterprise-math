<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-FALCONER-RELATION-DISTANCE-SPECTRUM",
  "title": "六维 Falconer 模板与 P000 关系距离谱强迫律",
  "kind": "RESEARCH",
  "owner": "research/geo6-falconer-relation-distance-spectrum",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Define a native relation-distance readout and subset-richness measure in P000, then classify when rich Cell subsets force many distinct relation-distance values or exhibit exact counterfamilies, using Falconer only as an external structural template.",
  "next_action": "Freeze one declared native relation-distance readout and one finite subset-richness statistic; compute exact small-model spectra; then prove the first forcing inequality or construct an infinite-style refinement family that defeats it.",
  "dependencies": [],
  "source_refs": [
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md@5778529",
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/P000_REALITY_FOUNDATION.json@main"
  ],
  "evidence_status": "EXTERNAL_FALCONER_OPEN / CLASSICAL_D_OVER_2_THRESHOLD_IS_HEURISTIC_ONLY / P000_DISTANCE_READOUT_UNFROZEN",
  "last_progress_ref": "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md",
  "last_progress_at": "2026-08-30T02:38:51+00:00",
  "hard_block": null,
  "tags": ["geometry", "P000", "native-6D", "Falconer", "distance-spectrum", "relation-readout", "refinement", "external-bridge"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-FALCONER-RELATION-DISTANCE-SPECTRUM",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6FAL",
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

# 六维 Falconer 模板与 P000 关系距离谱强迫律

## Mother question

在声明的 P000 native relation-distance readout 下，一个 Cell 子集达到何种可验证“丰富度”时，必须产生大量不同的关系距离值？如果不存在这样的强迫律，最小反例机制是什么？

## Frozen inputs and scope

- distance/readout 必须先用 native relation、transition、path 或其他已声明结构定义；不默认欧氏范数。
- subset richness 采用 exact finite statistic，并说明 rotation/refinement 下行为。
- 经典 Falconer 与 `d/2` 只作外部模板；六维中的数值 3 不是 native theorem。
- 必须同时搜索 forcing law 与结构化 counterfamily，避免只证正例。

## Hard target and required outputs

Hard target: `P000_NATIVE_DISTANCE_SPECTRUM_FORCING_LAW_CONSTRUCTED_OR_DECLARED_MODEL_NO_GO`.

必须定义 native distance-spectrum 与 richness statistic；完成 bounded exact census；提出并证明至少一个非平凡 forcing inequality，或给出可延拓的 counterfamily/no-go；分析 rotation/refinement 稳定性；给出至少一个 extremal or near-extremal family；提供 deterministic checker；输出 `research_returns/GEO6_FALCONER_RELATION_DISTANCE_SPECTRUM_RETURN_20260830.md`。

## Research value to preserve

该任务把“足够丰富的集合必须产生足够丰富的距离”转成纯 relation-spectrum 问题，可能直接连接进取数论已有的关系状态、缺陷谱与旋转结构。

## Success, kill, and return criteria

Success：得到一个严格声明模型中的 nontrivial richness-to-spectrum law，并有 sharp/near-sharp witness；或证明某个自然候选 law 被结构化 counterfamily 精确击穿。

有效 kill/no-go：证明当前 primitives 下任何 distance readout 都依赖额外 metric datum，或 richness 定义在 rotation/refinement 下无法保持非退化。

失败：直接使用欧氏距离、把 classical `d/2=3` 当 native 临界值、只报随机样本相关性、或从有限 census 外推一般定理。
