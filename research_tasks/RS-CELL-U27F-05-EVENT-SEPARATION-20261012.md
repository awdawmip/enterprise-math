<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CELL-U27F-05-EVENT-SEPARATION-20261012",
  "title": "首次新解绑与首次整体失联的分离计算",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "允许一次中断后继续恢复时，首次新解绑、严格前缀失联、有效整体失联和最终修复分别具有怎样的概率与工作量？",
  "next_action": "将T01的有效联系观察和T03续接接口绑定到U27原始BC首次释放输入；先在delta=0时判断前缀失联观察，而不是直接计算更大状态表。",
  "dependencies": [
    "RS-CELL-U27F-01-OPERATIVE-CONTINUITY-20261012",
    "RS-CELL-U27F-03-INTERRUPTED-RECOVERY-20261012"
  ],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/a02ab81dae21c508708e8774be80a8348a9d469a/research_notes/task_packages/20261012_u27_followup_5d76c1/TASK_PACKAGE.md",
    "https://github.com/awdawmip/enterprise-math/blob/1558a5de9af0f6336d2091e7f30627754f3763a5/research_task_records/RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007/TP2-E49C20B8D0A6569355F6.json",
    "https://github.com/awdawmip/enterprise-math/blob/c92d3f411ec24a09c5606bd29d1bb7dd8b43c7ae/research_result_records/RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007/RR-A2E93EC78BC5FE034176.json",
    "research_inputs/U27F_20261012/INPUT_MANIFEST.json",
    "research_inputs/U27F_20261012/fixtures/base_case.json",
    "research_inputs/U27F_20261012/fixtures/interrupted_after_carry.json",
    "research_inputs/U27F_20261012/fixtures/recorded_oracles.json"
  ],
  "evidence_status": "U27_CONDITIONAL_UNREVIEWED_INPUTS; TASK_DESIGN_APPROVED_BY_CURRENT_USER; NO_NEW_SCIENCE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "U27-followup",
    "finite-record",
    "native-X6",
    "U27F-05"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CELL-U27F-05-EVENT-SEPARATION-20261012",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "U27F-05",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "origin_candidate_id": null,
  "origin_candidate_state": null,
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007",
  "successor_gate": {
    "new_information_gap": "允许一次中断后继续恢复时，首次新解绑、严格前缀失联、有效整体失联和最终修复分别具有怎样的概率与工作量？",
    "why_parent_result_does_not_close_it": "祖先U2的RR-A2E93EC78BC5FE034176是待Driver审核的SOURCE_INTERFACE_GAP返回，原生作用来源、反作用与占位接口仍UNKNOWN。本任务不使用它的待审定理作为已接受前提；按当前用户指令，从U27的更新输入与可达前缀研究本项缺口，保留原Result及其审核状态。",
    "discriminating_outcomes": [
      "各事件不混同；TOTAL守恒，工作标记只计实际完成阶段；至少一个参数点提供精确证书和所有首步等式。",
      "声称一般δ界时须给证明与适用状态域，有限数值不用于外推。",
      "若新增有效联系或中断后继尚无法冻结，返回明确的不可辨识状态与待定义的唯一接口，而非继续把INTERRUPTED当成全部失联。"
    ],
    "kill_condition": "若仅能改名、复制既有结论或绕过本项源资格而得到目标，则返回最小反例或准确缺口，不把条件接口升级成原生定律。",
    "alternative_route_or_free_exploration_considered": "比较了在原U2宽任务内继续、等待全U27独立审核、以及另起无输入探索；当前用户已选定五项具体缺口，独立审核不由本发布替代，逐项冻结可使不同来源范围和依赖可检验。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "U27新增了有限库存中间快照、逐阶段新解绑与不同停止事件，五项分别有独立硬目标与正面/反例出口；祖先保持FROZEN_RETURN/AWAITING_REVIEW，整体父目标保持OPEN，不修改原有owner或审核状态。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:be0a92bae790fc5100f066235a0257c9a75470d152b48cd36909c318d6a61107",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 首次新解绑与首次整体失联的分离计算

Task-ID: `RS-CELL-U27F-05-EVENT-SEPARATION-20261012`；Package item: `PKG-U27F-05`。

## Mother question

允许一次中断后继续恢复时，首次新解绑、严格前缀失联、有效整体失联和最终修复分别具有怎样的概率与工作量？

## Frozen inputs and scope

冻结任务包 EM-U27-FOLLOWUP-20261012-V1 / PKG-U27F-05；完整会话原包 em_u27_followup_tasks.zip，SHA256 a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7。原包代码与依赖保持原字节；本次按原JSON值抽取的初始fixture在 `research_inputs/U27F_20261012/fixtures/`，完整取回与校验清单在 `research_inputs/U27F_20261012/INPUT_MANIFEST.json`。当前输入足以开始第一项关系分析；复验特定实现前须取得清单对应原码，未取得部分如实报告，不从摘要重建。

U27输入为条件模型及同作者执行证据，尚未经独立科学准入。本任务延续已记录的源关系，不把其作为已确认原生力。原始空间为六个显式坐标，全部十二原生方向保留；具体试验B=4、λ=1/48。

正式谱系祖先：`RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007`（原任务FROZEN_RETURN/AWAITING_REVIEW、原Result及作者均保持）；本任务使用U27更晚的具体前缀输入，不宣称完成或替代祖先。父目标：`OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS`。

必需输入：`fixtures/base_case.json`；`fixtures/interrupted_after_carry.json`；`fixtures/recorded_oracles.json`；`baseline/cell_u27/NOTE.md`。

执行依赖：`RS-CELL-U27F-01-OPERATIVE-CONTINUITY-20261012`、`RS-CELL-U27F-03-INTERRUPTED-RECOVERY-20261012`。

实际复用入口：`work_exposure.exposure_transfer`, `work_exposure.build_episodes`, `work_exposure.eliminate_transfers`, `work_exposure.freeze_loss`。

## Hard target and required outputs

构造保留真实中断后继的单次修复模型，分别计算四个终止/观察事件；至少证明一个相对于U27停止模型的严格关系或显式反例。

第一动作：将T01的有效联系观察和T03续接接口绑定到U27原始BC首次释放输入；先在delta=0时判断前缀失联观察，而不是直接计算更大状态表。

1. 先固定事件顺序、工作阶段、失联谓词和恢复目标；保留“新联系提交后旧联系释放仍可能连通”的分支。

2. 在完整56态基准的可比子域及新增前缀状态上作精确BRC计算，给出所有结果、存活量和未解决质量；额外几何反射另行标注。

3. 继续检验参考无新损伤过程的路径耦合何时有效；一旦发生中断，旧E∏(1−δh)不能无修改代表全部未来恢复。

交付文件：`EVENT_OBSERVER_CONTRACT.json`, `continued_episode_brc.py`, `FIRST_LOSS_VS_REPAIR.md`, `continued_episode_results.json`。

## Research value to preserve

允许一次中断后继续恢复时，首次新解绑、严格前缀失联、有效整体失联和最终修复分别具有怎样的概率与工作量？本项把已保存的工作前缀或中断状态变成独立可检验问题，保留正结论、可达反例及精确本构缺口三种科学出口，为依赖它的后续任务提供真实接口，而非仅增加模型标签。

## Success, kill, and return criteria

正面验收：
- 各事件不混同；TOTAL守恒，工作标记只计实际完成阶段；至少一个参数点提供精确证书和所有首步等式。
- 声称一般δ界时须给证明与适用状态域，有限数值不用于外推。

反例与缺口验收：
- 若新增有效联系或中断后继尚无法冻结，返回明确的不可辨识状态与待定义的唯一接口，而非继续把INTERRUPTED当成全部失联。

适用范围：
- T02未完成时，只验收候选关系动力学层结果；原生归因另行保留。
- 与T04并发变体的结论分列，串行恢复不自动获得重叠执行保证。

返回准确输入及哈希、模型差分、证明或反例、实际BRC对应、执行/未执行范围、未处理分支、资源与时序语义、贡献接触范围和最小下一问题。发布者已参与U1至U27及此任务包，不担任这些输入的独立审查者。本任务出版不产生科学接受。
