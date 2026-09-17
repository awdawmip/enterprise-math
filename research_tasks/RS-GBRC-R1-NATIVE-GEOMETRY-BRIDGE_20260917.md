<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GBRC-R1-NATIVE-GEOMETRY-BRIDGE",
  "title": "原生几何接口与外部基准的边界",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "四面体是可回放的外部图格基准；它与当前原生 Cell/旋转/路径体系之间还没有本计划可消费的比较态射。",
  "next_action": "按 P000 和 native_semantics_admissibility.json 选择一个最小、已有源定义的原生有限观察实例，固定其出处和运算后再尝试比较。",
  "dependencies": [
    "RS-GBRC-R1-TYPED-CARRIER"
  ],
  "source_refs": [
    "awdawmip/enterprise-math@9b3c656f310bed58e8c99c1754d09af5ae653413:research_notes/geometry_brc_residual_systems_r1_taskpack_20260916_eb416786.md",
    "awdawmip/enterprise-math@577bf1f0599bb91f8337b4de7e464562d4f254b9:research_activity_records/RA-geometry-brc-residual-20260916-eb416786.json",
    "research_notes/GBRC_RESIDUAL_SYSTEMS_20260917/DRIVER_DOSSIER.md"
  ],
  "evidence_status": "SOURCE_BACKED_TASK_PUBLICATION_NOT_EXECUTED",
  "hard_block": "WAITING_FOR_DECLARED_DEPENDENCIES",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GBRC-R1-NATIVE-GEOMETRY-BRIDGE",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GBRC-R1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R1-05｜原生几何接口与外部基准的边界

## Mother question

首轮残差核心能否从一个精确的原生几何实例导出，而不把四面体六边坐标、普通向量空间或外部几何偷当原生六维 Cell？

## Frozen inputs and scope

本任务不检验或改写 P000。允许三轴切片作为明确切片；空间六维、原生六维平面与四面体六条边的计数不同。不得先放入目标模型的加法、范数或物理意义再声称从原生结构导出。

依赖：RS-GBRC-R1-TYPED-CARRIER

## Hard target and required outputs

1. native_instance_sources.json：精确模型、定义源、观察、允许操作和最小有限范围。

2. comparison_diagram.md：若可行，给出状态/操作/观察的比较映射和交换性证明，标明信息损失。

3. native_obstruction.md：若不可行，提供精确缺失结构或不交换见证；区分未找到映射与已证明不存在映射。

4. contribution_boundary.json：哪些结论是原生、外部比较、条件性导入或尚未建立，明确剩余母问题。

首个动作：按 P000 和 native_semantics_admissibility.json 选择一个最小、已有源定义的原生有限观察实例，固定其出处和运算后再尝试比较。

## Research value to preserve

决定本体系究竟已进入原生几何，还是仅完成了有用但外部的有限方法整合，防止研究对象被悄悄替换。

## Success, kill, and return criteria

成功：得到非平凡可复核比较接口，或边界明确的否定/未决报告；两类均为有效首轮产出，但不得互换强度。

停止/否定：如果任务只能通过改写原生定义成立，停止该比较路线并返回所需额外假设；保留有限外部核心，不把失败解释成 P000 被推翻。

返回：保存精确输入、已证与未证范围、最小未解问题及可执行下一步。当前任务只是首轮计划的一个工作包；未获结论不能被其他任务当作成立的前提。
