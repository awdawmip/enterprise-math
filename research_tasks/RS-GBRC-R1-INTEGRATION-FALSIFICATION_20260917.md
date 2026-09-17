<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GBRC-R1-INTEGRATION-FALSIFICATION",
  "title": "首轮核心集成、反例与交接审查",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "首轮任务尚未执行；不得预先认定上游都成功或将任务包的结构审查当作数学验收。",
  "next_action": "等待五项输入具有固定内容；建立逐结论依赖和证据矩阵。若上游缺失或冲突，列出确切缺口而不补写其结果。",
  "dependencies": [
    "RS-GBRC-R1-TYPED-CARRIER",
    "RS-GBRC-R1-TRANSPORT-COMPOSITION",
    "RS-GBRC-R1-OBSERVER-MEMORY",
    "RS-GBRC-R1-POSITIVE-STABILITY",
    "RS-GBRC-R1-NATIVE-GEOMETRY-BRIDGE"
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
  "registry_key": "RS-GBRC-R1-INTEGRATION-FALSIFICATION",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GBRC-R1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
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

# R1-06｜首轮核心集成、反例与交接审查

## Mother question

首轮各接口是否在相同类型、观察和证据强度下真正衔接？剩余新贡献是什么，哪些候选已被反例关闭？

## Frozen inputs and scope

只消费可定位的上游证据，不用聊天摘要替代。作者自检与独立复核分开标记；本任务产出不自行授予 Foundation 或其他真值地位。

依赖：RS-GBRC-R1-TYPED-CARRIER, RS-GBRC-R1-TRANSPORT-COMPOSITION, RS-GBRC-R1-OBSERVER-MEMORY, RS-GBRC-R1-POSITIVE-STABILITY, RS-GBRC-R1-NATIVE-GEOMETRY-BRIDGE

## Hard target and required outputs

1. R1_CORE_REPORT.md：完整定义、接口定理/反例、应用实例与范围。

2. claim_evidence_matrix.json：结论、假设、源、证明/有限证书/未决、依赖与审查状态。

3. regression_report.json：合法实例、非法类型、错误商、顺序混淆、图册偏差、分支增益、非统一尺度七类测试及命令。

4. HANDOFF.md：已完成、最小未解单位、可复用代码、应停止路线、是否有独立的新信息缺口足以建议下一轮。

首个动作：等待五项输入具有固定内容；建立逐结论依赖和证据矩阵。若上游缺失或冲突，列出确切缺口而不补写其结果。

## Research value to preserve

使这套体系能够被另一个研究者接手、复核与反驳，而不是只能依靠原对话理解。

## Success, kill, and return criteria

成功：所有相互依赖的类型和观察一致；逐项证据无悬空引用；明确首轮是新结果、条件性核心、整合复用还是局部否定。

停止/否定：任何关键证据缺失或矛盾均阻止整体结论；若无新贡献则如实收束为 INTEGRATION_ONLY_NO_NEW_THEOREM，不自动生成下一轮。

返回：保存精确输入、已证与未证范围、最小未解问题及可执行下一步。当前任务只是首轮计划的一个工作包；未获结论不能被其他任务当作成立的前提。
