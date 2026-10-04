<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-MULTISOURCE-TRIAD-MATCHING-BUDGET-20261005",
  "title": "多源三元接触的完整合法匹配与共享预算",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "M2只在最多三个同源槽范围避免匹配歧义；M3只证无碰撞无回流单通道闭合；N1已做共享预算拒绝但未推导一般原生作用；P01已正式发布证据/版本归属修复任务。",
  "next_action": "在原固定接触数据内选择两个来源的最小相遇窗口，枚举全部合法三元匹配并保留关联；分别检查同源与允许跨源候选的逐来源守恒、共享预算单次消费和完整当前状态。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P07",
    "private-evidence:heartbeat_native_candidates_M2/PROOF.md",
    "private-evidence:heartbeat_residual_state_M3/PROOF.md",
    "private-evidence:native_cell_pointer_N1/PROOF.md",
    "https://github.com/awdawmip/enterprise-math/blob/06754542f6e552c705958dee9987096066414a84/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; FORMAL_DEPENDENCIES_VERIFIED_OR_ATOMIC_BATCHED; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "MULTISOURCE",
    "TRIAD_CONTACT",
    "MATCHING",
    "SHARED_BUDGET",
    "PROVENANCE"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-MULTISOURCE-TRIAD-MATCHING-BUDGET-20261005",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P07",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "successor_gate": {
    "new_information_gap": "M2只在少量同源槽内消除匹配歧义，M3只覆盖无碰撞无回流单通道，N1只给共享预算拒绝；多源相遇时跨源承接、反馈和共享总预算尚无唯一合法匹配规则。",
    "why_parent_result_does_not_close_it": "P01修复的是版本、作者、输入输出与证据归属；它不决定两个来源在同一接触窗口中的三元匹配、共享预算如何只消费一次，也不提供跨源承接的原生本构。",
    "discriminating_outcomes": [
      "在固定两个来源的最小相遇窗口中枚举全部合法三元匹配，逐来源槽守恒并证明共享预算只消费一次；分别给出同源与允许跨源候选的完整当前状态。",
      "若现有本构不足以唯一选择候选，则给出至少两个在全部已知约束下均合法但未来不同的候选，证明物理唯一性当前不可识别。"
    ],
    "kill_condition": "没有来源可核验的本构时只报告候选差异和自由度，不得任选ID配对、默认等概率、引入Born规则或人为条纹，也不得把已停用通用对象池/指针恢复为主路径。",
    "alternative_route_or_free_exploration_considered": "可以任意指定ID配对、用等概率混合或引入更强外部概率规则，但这些都会增加未授权本构。完整有限匹配枚举是保留关联和共享预算的最小无偏路线。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "P01只保证早期证据可追溯；本项在这些已归属材料上提出新的有限多源接触科学问题，必须单独给匹配/预算证书或不可识别性结论。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 多源三元接触的完整合法匹配与共享预算

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

在原固定接触数据中选两个来源的最小相遇窗口，全部合法三元匹配有哪些；在不丢失来源关联的前提下，共享预算怎样只消费一次，同源与允许跨源两类候选能否被现有原生约束唯一地区分？

## Frozen inputs and scope

共同项目语义服从 P000。P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 作为证据归属/版本前置，保证 M2、M3、N1 材料不被混并；本任务不把 P01 的治理结论当科学本构。冻结前沿：M2 只在最多三个同源槽避免匹配歧义；M3 只证无碰撞无回流单通道闭合；N1 已做共享预算拒绝但未推导一般原生作用。

禁止新增 Born 规则、等概率假设、人为条纹或任意 ID 配对；不得恢复用户已停用的通用对象池/指针为主路径。私有恢复入口 SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`。

## Hard target and required outputs

固定两个来源的最小相遇窗口，明确槽、来源、三元接触条件、共享预算单位和正负端口语义。枚举**全部**合法三元匹配，保持每个匹配的来源关联；至少分别构造“只允许同源承接”和“明确允许跨源承接”两类候选。

交付逐来源槽守恒、共享预算仅消费一次、完整输出/当前状态、至少一个区分候选的反例；把 P000 前提、已证材料、候选规则和仍自由的本构参数分型。若执行代码或证书，列全匹配生成、关系存储、配对判断及沿途作用费用。

## Research value to preserve

多源相遇的困难不在总量，而在“谁与谁承接”以及共享资源被哪个接触事件消费。若把来源关系压成总数，跨源与同源候选会被错误合并；若任意指定配对，又会把未证本构伪装成原生规则。完整有限匹配枚举能把确定约束与不可识别自由度分开。

## Success, kill, and return criteria

成功：全部合法匹配可回放；逐来源槽守恒；同一共享预算没有重复消费；每个候选给完整当前状态与区分见证。

停止/否定：若现有定义不足以唯一选择匹配，本任务以候选差异/自由参数证书结束，不编造物理唯一性；任何等概率/Born/人为条纹假设均不作为补丁。
