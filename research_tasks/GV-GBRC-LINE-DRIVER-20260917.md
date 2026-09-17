<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GV-GBRC-LINE-DRIVER-20260917",
  "title": "Geometry–BRC 残差系统持续 Driver 协调与证据接力",
  "kind": "GOVERNANCE",
  "owner": "governance",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "R1 六项研究工作包即将进入正式状态机，但尚无持续的线级证据接收、依赖解锁、独立复核和后续材料化责任链。",
  "next_action": "核对本目标下九项当前发布记录与依赖状态，从 R1-01 开始路由可执行工作；每次冻结返回只消费可定位证据，并更新线级 dossier 的最小未解单位。",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@9b3c656f310bed58e8c99c1754d09af5ae653413:research_notes/geometry_brc_residual_systems_r1_taskpack_20260916_eb416786.md",
    "awdawmip/enterprise-math@577bf1f0599bb91f8337b4de7e464562d4f254b9:research_activity_records/RA-geometry-brc-residual-20260916-eb416786.json",
    "research_notes/GBRC_RESIDUAL_SYSTEMS_20260917/DRIVER_DOSSIER.md",
    "research_artifacts/GBRC_RESIDUAL_SYSTEMS_20260917/manifest.json"
  ],
  "evidence_status": "SOURCE_BACKED_DRIVER_GOVERNANCE_TASK_NOT_EXECUTED",
  "last_progress_ref": "awdawmip/enterprise-math@9b3c656f310bed58e8c99c1754d09af5ae653413:research_notes/geometry_brc_residual_systems_r1_taskpack_20260916_eb416786.md",
  "last_progress_at": "2026-09-16T05:08:59.191778+00:00",
  "hard_block": null,
  "tags": [
    "GBRC",
    "residual",
    "driver",
    "evidence-routing",
    "R1"
  ],
  "claim_lease_minutes": 1440,
  "identity_lane": "GBRC",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "GV-GBRC-LINE-DRIVER-20260917",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# GBRC Driver｜持续协调与证据接力

## Mother question

怎样使 Geometry–BRC 残差累积研究在多个执行者和多轮返回之间保持同一母问题、精确依赖与可恢复证据，而不依赖前任聊天中的隐含状态？

## Frozen inputs and scope

冻结当前父目标、六项 R1 研究任务及本次发布的两项后续治理任务。Driver 只管理线级路由、证据绑定、审查责任和后续任务材料化；任务发布本身不构成任何数学结论的接受。

## Hard target and required outputs

1. 维护一份精确线级 dossier：当前任务发布代、依赖是否满足、最近冻结证据、独立复核状态、最小未解单位和下一控制动作。
2. 从 R1-01 起按依赖逐步解锁；上游反例或范围缩减必须传播到所有受影响下游，不得仅凭任务曾经进入 READY 就继续套用。
3. 每个研究任务的冻结返回必须绑定可定位的 Result 或任务允许的等价持久证据；作者自检与独立复核分栏。
4. 将 R1 的完整结果交给后续审查门；只有审查后仍存在具体信息缺口时，才材料化同一路线的后续研究任务。
5. 对重复任务、失效前提、无新信息路线及时去重或停止，保留负结果和可复用构件。

首个动作：核对本目标下九项当前发布记录与依赖状态，从 R1-01 开始路由可执行工作；每次冻结返回只消费可定位证据，并更新线级 dossier 的最小未解单位。

## Research value to preserve

把“几何—BRC 残差系统论”从一次性提案变成可持续、可交接、可否证的研究线，防止任务完成与父目标完成混淆，也防止已有结果在换人后被重复研究。

## Success, kill, and return criteria

成功：六项 R1 都获得明确的执行/返回状态，冻结结果进入独立复核或得到精确退回理由；后续审查和材料化任务获得完整输入，另一位 Driver 可仅凭持久状态接管。

停止/返回：若当前授权失效、关键持久证据缺失或任务定义与实际返回发生不可解释冲突，冻结到最小冲突单元并返回，不自行补造研究结论或审查结论。
