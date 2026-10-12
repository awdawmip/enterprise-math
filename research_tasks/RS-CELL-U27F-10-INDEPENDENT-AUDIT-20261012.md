<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CELL-U27F-10-INDEPENDENT-AUDIT-20261012",
  "title": "独立审查、先例核对与可复用核心",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "U27及后续被用作关键前提的具体结果，哪些得到独立证据支持，哪些只应作为候选继续？",
  "next_action": "由未参与被审证明/代码且如实披露接触范围的研究者，先冻结U27 NOTE与work_exposure的哈希；优先检查停时事件、初始分布、工作计数和前缀解释。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/a02ab81dae21c508708e8774be80a8348a9d469a/research_notes/task_packages/20261012_u27_followup_5d76c1/TASK_PACKAGE.md",
    "https://github.com/awdawmip/enterprise-math/blob/68452be67a2bfdd02b6010c116fdc2f022848611/research_inputs/U27F_20261012/INPUT_MANIFEST.json",
    "https://github.com/awdawmip/enterprise-math/blob/1558a5de9af0f6336d2091e7f30627754f3763a5/research_task_records/RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007/TP2-E49C20B8D0A6569355F6.json",
    "https://github.com/awdawmip/enterprise-math/blob/c92d3f411ec24a09c5606bd29d1bb7dd8b43c7ae/research_result_records/RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007/RR-A2E93EC78BC5FE034176.json"
  ],
  "evidence_status": "U27_CONDITIONAL_UNREVIEWED_INPUTS; TASK_DESIGN_APPROVED_BY_CURRENT_USER; NO_NEW_SCIENCE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "U27-followup",
    "finite-record",
    "group-B",
    "T10"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CELL-U27F-10-INDEPENDENT-AUDIT-20261012",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "U27F-10",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:be0a92bae790fc5100f066235a0257c9a75470d152b48cd36909c318d6a61107",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 独立审查、先例核对与可复用核心

原包：EM-U27-FOLLOWUP-20261012-V1 / PKG-U27F-10。本项仅发布研究任务，未执行研究或审查。

## Mother question

U27及后续被用作关键前提的具体结果，哪些得到独立证据支持，哪些只应作为候选继续？

第一项动作：由未参与被审证明/代码且如实披露接触范围的研究者，先冻结U27 NOTE与work_exposure的哈希；优先检查停时事件、初始分布、工作计数和前缀解释。

## Frozen inputs and scope

复用原包 `em_u27_followup_tasks.zip`，SHA256 `a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7`，会话文件 `file_00000000c6d8820697f020b88af9448d`。Source取回入口为 `research_inputs/U27F_20261012/INPUT_MANIFEST.json`；其中已发布起步fixture，完整原代码与证明在该清单指向的原包中，不假称全部安装于Source。取得准确原包后先核对清单；可用原生小输入推进理论/证书设计，科学执行保留真实来源版本。

本项包内输入：
- `baseline/cell_u27/NOTE.md`（原交付包内路径）
- `baseline/cell_u27/CHECKPOINT.json`（原交付包内路径）
- `baseline/cell_u27/evidence/results.json`（原交付包内路径）
- `baseline/cell_u27/work_exposure.py`（原交付包内路径）
- `provenance/intake_validation.json`（原交付包内路径）

任务依赖：无硬任务依赖；独立审查的输入取得与贡献隔离另行核对。
原生归因相关依赖：仅在实际作原生归因时核对相应来源接口；本项不自动授予原生结论。

本项谱系采用REPLAY：对冻结来源作独立复验/审查，而非把新机制作为已完成的续接。T01至T09产物只在实际产生并冻结后逐项补充审查。本发布者已经参与原来源，发布不等于担任独立执行者。

U27及其依赖仍标为有条件、未独立审查的研究输入；同作者复跑不提高证据等级。保留四材料、六轴坐标、来源次序和当前记录分割。工作阶段计数不是物理时钟。具体输入准备或模型修改在返回中分列，不修改P000或原来源证据。

## Hard target and required outputs

对一个明确被冻结的结果集完成独立数学/代码判断，并提取一个有适用条件与证明的可复用核心；不把同作者复跑计作独立审核。

工作单元：
1. 先检查U27四个事件的区别、完整56态范围、mode商为何失效、首次释放取样、TOTAL/工作标记闭合；只复跑依赖的有界分段。
2. 后续T01–T09每项到达可审前沿时，按精确产物另记审查；原实现与独立实现/论证分开保留。
3. 对拟宣称的新方法查作者原文或官方论文，记录先例仅覆盖的一般方法与本模型特有命题；不因名称近似判定重复。
4. 选择一个已经审查的有限命题作机器可检验证书或形式化核心，不把工具包装本身当作定理。

交付文件：
- `INDEPENDENCE_AND_EXPOSURE.json`
- `DECISIVE_REVIEW.md`
- `PRIMARY_SOURCE_MATCH.md`
- `REUSABLE_CORE_SPEC.json`
- `independent_checker.py`

复用接口：`baseline/cell_u27/check_u27.py named bounded parts`；`reuse/sources/brc_weighted.py`；`templates/RESULT_TEMPLATE.json`。
实际科学计算沿当前项目的typed BRC协议；接口不足时返回具体缺口与可检查关系，不把未执行步骤记作已执行。

## Research value to preserve

对一个明确被冻结的结果集完成独立数学/代码判断，并提取一个有适用条件与证明的可复用核心；不把同作者复跑计作独立审核。 研究应区分观察对象、初态分布、适用时钟与资源预算，保存对照反例和不能互换的条件。复用正确前沿，不为取得会话上下文而重做整条U1至U27。

## Success, kill, and return criteria

正面验收：
- 审查记录写明真实作者/接触/贡献范围、输入哈希、逐命题结论、反例或修订要求；最终采纳由当前正式规则处理。
- 可复用核心携带明确类型、输入输出和适用条件，经典外部方法与原生解释之间有界限。

反例/缺口验收：
- 发现推导/代码错误时提供最小复现及受影响结论集合；保全正确前沿，并给出最小修复任务，不重做整条U1–U27。

范围说明：
- 本包编制者已深度参与/接触前线，因此本次打包校验不承担独立审核。
- 本任务是跨组并行审查通道，不是让全部其他任务停在等待审查后才能探索；以未审前提继续时清楚标为条件结果。

每次返回保存准确输入和哈希、模型变更、证明或反例、代码对应、实际执行覆盖、未处理支路和最小下一问题。仅有有限数据时保留有限范围；研究返回不自行宣称整条父目标完成。
