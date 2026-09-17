<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GBRC-R1-TRANSPORT-COMPOSITION",
  "title": "几何传递、分支组合与参考截面障碍",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "仿射组合律已知；几何端口、部分衔接、分支来源和共同参考截面的精确接口尚未形成。",
  "next_action": "读取 R1-01 的精确冻结输出；先构造带源靶类型的两段组合，再定位一个顺序敏感和一个不兼容端口的最小例子。",
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
  "registry_key": "RS-GBRC-R1-TRANSPORT-COMPOSITION",
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

# R1-02｜几何传递、分支组合与参考截面障碍

## Mother question

在已定型的残差纤维上，何种过程标签足以保证路径和分支组合闭合，哪些偏差可由参考截面消去？

## Frozen inputs and scope

限 R1-01 接受的阿贝尔残差纤维及其同态。PROGRAM 第3、6节给出待复用恒等式；不假设所有原生演化都仿射。分支权重正有理且与可能存在的符号残差分开。

依赖：RS-GBRC-R1-TYPED-CARRIER

## Hard target and required outputs

1. transport_contract.json：源靶、T/d、可组合条件、分支依赖关系与读出。

2. composition_proof.md：结合律、路径展开、带兼容关系的分支串联；标为既有代数的具体应用。

3. gauge_section.md：共同方程的充要判据，闭路必要性；在明确可逆连通情形证明足够性，或给出缺失假设的反例。

4. exact_witnesses.json：顺序敏感、T_gamma=I 的非零偏差障碍、T_gamma!=I 但偏差可消去、局部不动点不保证全局共用截面。

首个动作：读取 R1-01 的精确冻结输出；先构造带源靶类型的两段组合，再定位一个顺序敏感和一个不兼容端口的最小例子。

## Research value to preserve

把“先传递再累积”从口号变成可组合过程数据，并区分坐标选择与真实结构障碍。

## Success, kill, and return criteria

成功：符号证明与精确例子一致；串联仅配对合法分支；新结论限于具体接口或障碍，不以一般仿射结合律充当创新。

停止/否定：若带有限标签不能保留所选未来观察，给出最短区分上下文并增补最小必要标签；禁止用无限完整历史掩盖未解的有限闭合问题。

返回：保存精确输入、已证与未证范围、最小未解问题及可执行下一步。当前任务只是首轮计划的一个工作包；未获结论不能被其他任务当作成立的前提。
