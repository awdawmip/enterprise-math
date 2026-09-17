<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GBRC-R1-POSITIVE-STABILITY",
  "title": "正权残差包络与有限稳定证书",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Bh<h 和收缩上界是已有接口；具体正包络的正确支配关系、注入条件以及失效边界尚待构造。",
  "next_action": "检查 src/enterprise_math/brc_weighted_recurrent.py 与对应有限递归来源；写明 E 控制的是哪种范数/读出，再逐项由 R1-02 传递推导 B。",
  "dependencies": [
    "RS-GBRC-R1-TYPED-CARRIER",
    "RS-GBRC-R1-TRANSPORT-COMPOSITION"
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
  "registry_key": "RS-GBRC-R1-POSITIVE-STABILITY",
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

# R1-04｜正权残差包络与有限稳定证书

## Mother question

怎样从具体几何传递与分支权重推出可认证的有限非负残差包络，而不是直接假设一个有利的收缩矩阵？

## Frozen inputs and scope

有限非负有理 B；声明权重是概率、计数还是增益。torsion 状态由信息接口处理，不强制作为实数误差。不得由正包络发散推断符号/向量真实和发散。

依赖：RS-GBRC-R1-TYPED-CARRIER, RS-GBRC-R1-TRANSPORT-COMPOSITION

## Hard target and required outputs

1. envelope_derivation.md：E、B、d 的定义及逐项支配证明。

2. stability_certificate.json：精确 h、lambda、注入界和加权范数；调用现有验证器的结果与版本。

3. negative_controls.json：两条 3/5 增益回路；无统一余量的 B_k=[1-1/k]；缺少注入界或范数比较时的失败证据。

4. scope_of_bounds.md：有限路径、有限状态递归和跨尺度三个强度的分界；不开展未冻结的连续极限推导。

首个动作：检查 src/enterprise_math/brc_weighted_recurrent.py 与对应有限递归来源；写明 E 控制的是哪种范数/读出，再逐项由 R1-02 传递推导 B。

## Research value to preserve

把分支增殖与单路径收缩同时纳入可检查的稳定性结论，阻止将局部稳定误当整体或跨尺度稳定。

## Success, kill, and return criteria

成功：先证明包络支配，再给出正有理证书；所有常量、初值、源项和观察范围明示；负例精确可回放。

停止/否定：若找不到支配包络或 Bh<h 失败，返回确切缺口/不可认证结果；不能为得到收缩而无说明归一化权重或删除分支。

返回：保存精确输入、已证与未证范围、最小未解问题及可执行下一步。当前任务只是首轮计划的一个工作包；未获结论不能被其他任务当作成立的前提。
