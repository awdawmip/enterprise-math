<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CELL-U27F-08-CONTACT-FORMATION-20261012",
  "title": "由作用形成接触，而不是恢复预置的连接",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "使用有来源的材料—场—支援更新，分离的两单位/四单位能否自行形成持续的有效联系，而不是先给定树或目标位置？",
  "next_action": "先冻结两单位的分离准备、真实支援预算与T02作用输出；分别跟踪成联系、短期保持和最终解联，再加入四单位。",
  "dependencies": [
    "RS-CELL-U27F-02-NATIVE-TRIAD-20261012",
    "RS-CELL-U27F-05-EVENT-SEPARATION-20261012"
  ],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/a02ab81dae21c508708e8774be80a8348a9d469a/research_notes/task_packages/20261012_u27_followup_5d76c1/TASK_PACKAGE.md",
    "https://github.com/awdawmip/enterprise-math/blob/68452be67a2bfdd02b6010c116fdc2f022848611/research_inputs/U27F_20261012/INPUT_MANIFEST.json",
    "https://github.com/awdawmip/enterprise-math/blob/1558a5de9af0f6336d2091e7f30627754f3763a5/research_task_records/RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007/TP2-E49C20B8D0A6569355F6.json",
    "https://github.com/awdawmip/enterprise-math/blob/c92d3f411ec24a09c5606bd29d1bb7dd8b43c7ae/research_result_records/RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007/RR-A2E93EC78BC5FE034176.json",
    "research_inputs/U27F_20261012/fixtures/base_case.json"
  ],
  "evidence_status": "U27_CONDITIONAL_UNREVIEWED_INPUTS; TASK_DESIGN_APPROVED_BY_CURRENT_USER; NO_NEW_SCIENCE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "U27-followup",
    "finite-record",
    "group-B",
    "T08"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CELL-U27F-08-CONTACT-FORMATION-20261012",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "U27F-08",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007",
  "successor_gate": {
    "new_information_gap": "使用有来源的材料—场—支援更新，分离的两单位/四单位能否自行形成持续的有效联系，而不是先给定树或目标位置？",
    "why_parent_result_does_not_close_it": "祖先U2的RR-A2E93EC78BC5FE034176仍是待审的来源接口缺口返回，不提供本项结论。U27提供有条件、尚未独立审查的输入与工作前缀；当前用户明确要求发布本包剩余任务。本项保持旧Result和父目标状态，不以待审结论为已接受前提。",
    "discriminating_outcomes": [
      "至少一项机制在明确输入族中具有可重复的成联系与保持证据；保持来自所声明作用，而不是连通性筛选或有限反射墙。",
      "原生作用归因须满足T02来源与三元资格；未满足时只保留条件机制结果。",
      "提供散逸/解联/欠定的严格子命题或可达反例，明确哪项作用缺失；不通过调节参数追着目标形状拟合。"
    ],
    "kill_condition": "若新结论只能靠重置输入、丢弃相关支路、隐藏额外资源或省略所需作用关系取得，返回可达反例或最小缺口，保留已经成立的条件前沿。",
    "alternative_route_or_free_exploration_considered": "比较了在祖先宽任务中继续、只做单轮参数扩张、独立审查及另起自由探索；本包将多轮、资源、生成、算术和独立审查分为可判别任务。当前指令选择发布这些缺口，后续探索的结论仍按真实前提验收。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "给出一个无需预置目标连接/平方壳的接触生成机制实例，或证明选定有来源机制不足以形成/保持该整体；生成与保持分别验收。；本项拥有独立输入接口、证据和反例出口，不因单轮进展自动断言父目标完成。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:be0a92bae790fc5100f066235a0257c9a75470d152b48cd36909c318d6a61107",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 由作用形成接触，而不是恢复预置的连接

原包：EM-U27-FOLLOWUP-20261012-V1 / PKG-U27F-08。本项仅发布研究任务，未执行研究或审查。

## Mother question

使用有来源的材料—场—支援更新，分离的两单位/四单位能否自行形成持续的有效联系，而不是先给定树或目标位置？

第一项动作：先冻结两单位的分离准备、真实支援预算与T02作用输出；分别跟踪成联系、短期保持和最终解联，再加入四单位。

## Frozen inputs and scope

复用原包 `em_u27_followup_tasks.zip`，SHA256 `a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7`，会话文件 `file_00000000c6d8820697f020b88af9448d`。Source取回入口为 `research_inputs/U27F_20261012/INPUT_MANIFEST.json`；其中已发布起步fixture，完整原代码与证明在该清单指向的原包中，不假称全部安装于Source。取得准确原包后先核对清单；可用原生小输入推进理论/证书设计，科学执行保留真实来源版本。

本项包内输入：
- `fixtures/base_case.json`（原交付包内路径）
- `provenance/authority_pins.json`（原交付包内路径）
- `baseline/cell_u27/reuse/contact_network.py`（原交付包内路径）
- `baseline/cell_u27/NOTE.md`（原交付包内路径）

任务依赖：RS-CELL-U27F-02-NATIVE-TRIAD-20261012、RS-CELL-U27F-05-EVENT-SEPARATION-20261012
原生归因相关依赖：RS-CELL-U27F-02-NATIVE-TRIAD-20261012

依赖未形成时可以先研究显式条件命题；依赖关系保留，最终结论须绑定实际产物，数值或原生归因不越过其前提。

U27及其依赖仍标为有条件、未独立审查的研究输入；同作者复跑不提高证据等级。保留四材料、六轴坐标、来源次序和当前记录分割。工作阶段计数不是物理时钟。具体输入准备或模型修改在返回中分列，不修改P000或原来源证据。

## Hard target and required outputs

给出一个无需预置目标连接/平方壳的接触生成机制实例，或证明选定有来源机制不足以形成/保持该整体；生成与保持分别验收。

工作单元：
1. 只允许当前输入中真实存在的材料、场、支援和有限资源；总预算、边界与来源位置显式。
2. 比较独立分离、相邻未连接、已有连接三种初态；同一规则计算首次成联系、有限保持、再分离与反作用后继。
3. 从两单位推进四单位并允许整体平移/变形；每个可观察方向由来源状态产生，不从预设“向内”开关替代。

交付文件：
- `FORMATION_PREPARATIONS.json`
- `CONTACT_FORMATION_AND_RETENTION.md`
- `formation_brc.py`
- `formation_counterexamples_or_certificates.json`

复用接口：`reuse/contact_network.py`；`reuse/local_latent.material`；`T02 frozen event interface`；`T05 event observers`。
实际科学计算沿当前项目的typed BRC协议；接口不足时返回具体缺口与可检查关系，不把未执行步骤记作已执行。

## Research value to preserve

给出一个无需预置目标连接/平方壳的接触生成机制实例，或证明选定有来源机制不足以形成/保持该整体；生成与保持分别验收。 研究应区分观察对象、初态分布、适用时钟与资源预算，保存对照反例和不能互换的条件。复用正确前沿，不为取得会话上下文而重做整条U1至U27。

## Success, kill, and return criteria

正面验收：
- 至少一项机制在明确输入族中具有可重复的成联系与保持证据；保持来自所声明作用，而不是连通性筛选或有限反射墙。
- 原生作用归因须满足T02来源与三元资格；未满足时只保留条件机制结果。

反例/缺口验收：
- 提供散逸/解联/欠定的严格子命题或可达反例，明确哪项作用缺失；不通过调节参数追着目标形状拟合。

范围说明：
- T06未完成前不声称长期自治寿命；T07未完成的资源估算单独列欠项。
- 有限平均恢复已准备关系不证明自发建立关系。

每次返回保存准确输入和哈希、模型变更、证明或反例、代码对应、实际执行覆盖、未处理支路和最小下一问题。仅有有限数据时保留有限范围；研究返回不自行宣称整条父目标完成。
