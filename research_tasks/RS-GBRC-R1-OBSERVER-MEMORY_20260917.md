<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GBRC-R1-OBSERVER-MEMORY",
  "title": "观察相容压缩与最小充分残差",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "P023、部分操作商和旧四面体一比特修复可复用；几何标签、正权输出及更强未来观察的联合边界待定位。",
  "next_action": "先检查当前 src/enterprise_math/partial_operation_quotient.py 和 composition_safe_collapse.py 的现有接口，实例化八状态回归；不重写通用细化算法。",
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
  "registry_key": "RS-GBRC-R1-OBSERVER-MEMORY",
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

# R1-03｜观察相容压缩与最小充分残差

## Mother question

对明确的观察及操作语言，何种最小残差编码既保留合法性又支持全部允许的未来？CWM 终端等价何时不能充当逐步状态同余？

## Frozen inputs and scope

冻结三种语言：matching-only；e 及三生成元；增加合法性/端口/来源可见性的扩展语言。对整数提升另设整数域谓词。终端正权等价与操作同余分别定义。

依赖：RS-GBRC-R1-TYPED-CARRIER

## Hard target and required outputs

1. observer_contracts.json：各语言和保留/丢弃字段。

2. minimal_memory.md：按观察纤维划分宽度给出最小编码证明或反例；回放 e 的 2/4/8 深度类数和 matching 的可安全商。

3. separation_certificates.json：每项不安全压缩的输入对、最短区分操作字、合法性或输出差异。

4. weighted_vs_contextual.md：证明采用的 CWM 简化在所声明上下文下安全，或提供终端相等但来源/中间观察不同的反例；报告最小修复而非强称等价。

首个动作：先检查当前 src/enterprise_math/partial_operation_quotient.py 和 composition_safe_collapse.py 的现有接口，实例化八状态回归；不重写通用细化算法。

## Research value to preserve

解释哪些残差必须保留、哪些可删，以及最小内存成本对观察语言的依赖。

## Success, kill, and return criteria

成功：最小性有下界区分证据和足够性证明；有限穷举仅为相应有限实例证书；无限整数纤维结论另有符号论证。

停止/否定：若只复现旧一比特/2,4,8 结果，明确记为 REPLAY_ONLY；未增加新观察边界或非平凡联合接口时不宣称新定理。

返回：保存精确输入、已证与未证范围、最小未解问题及可执行下一步。当前任务只是首轮计划的一个工作包；未获结论不能被其他任务当作成立的前提。
