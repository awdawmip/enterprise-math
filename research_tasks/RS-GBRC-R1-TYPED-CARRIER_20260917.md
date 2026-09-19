<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GBRC-R1-TYPED-CARRIER",
  "title": "残差类型系统与四面体可回放基准",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "原提案已有条件性公式；缺少统一实例 schema、明确整数/模二类型边界和可供后续任务消费的冻结数据。",
  "next_action": "逐字段建立实例 schema；由 PROGRAM 第5节的 V0/E0/delta/m/e/N 和三生成元生成最小测试输入。",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@9b3c656f310bed58e8c99c1754d09af5ae653413:research_notes/geometry_brc_residual_systems_r1_taskpack_20260916_eb416786.md",
    "awdawmip/enterprise-math@577bf1f0599bb91f8337b4de7e464562d4f254b9:research_activity_records/RA-geometry-brc-residual-20260916-eb416786.json",
    "research_notes/GBRC_RESIDUAL_SYSTEMS_20260917/DRIVER_DOSSIER.md"
  ],
  "evidence_status": "SOURCE_BACKED_TASK_PUBLICATION_NOT_EXECUTED",
  "hard_block": null,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GBRC-R1-TYPED-CARRIER",
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

# R1-01｜残差类型系统与四面体可回放基准

## Mother question

如何把细状态、粗观察、残差纤维、部分操作和正权分支分成可检验的接口，并使旧四面体结果成为可回放而不误标创新的首个实例？

## Frozen inputs and scope

冻结顶点/边顺序、左作用约定、整数残差与 F2^3 的不同载体。来源为本包 PROGRAM 第2、5节和 SOURCES 中 proposal、p023、tetrahedron_manuscript。图格基准不是原生 Cell 的同义词。

依赖：无上游研究任务；使用本包已冻结定义和可核查出处。

## Hard target and required outputs

1. instance_schema.json：X/G/q/A/F/O/W/R/encode/H、每个函数的源靶、合法性、残差类型和证据级别。

2. tetrahedron_fixture.json：八状态、三个生成元、matching/e/all-star 观察和整数提升边界；给出整数格基准的符号定义。

3. carrier_bridge.md：一般集合接口 -> 阿贝尔仿射接口 -> 正权包络接口的假设清单；指出哪些映射不存在或未构造。

4. exact_tests.py 与执行结果：类型错误、非法模二/整数替代、缺失操作合法性必须被拒绝。

首个动作：逐字段建立实例 schema；由 PROGRAM 第5节的 V0/E0/delta/m/e/N 和三生成元生成最小测试输入。

## Research value to preserve

防止同名“残差”在整数格、torsion、路径和实数上界之间无说明切换；为其余任务提供同一输入，而不是各自发明模型。

## Success, kill, and return criteria

成功：字段完整且两个执行者按文件可重构同一有限实例；所有有意非法输入被拒绝；已知结论与新目标分栏。

停止/否定：若某强制字段没有数学意义，缩小该接口而不是补造结构；若旧基准重现失败，冻结最小冲突输入并暂停依赖它的任务。

返回：保存精确输入、已证与未证范围、最小未解问题及可执行下一步。当前任务只是首轮计划的一个工作包；未获结论不能被其他任务当作成立的前提。
