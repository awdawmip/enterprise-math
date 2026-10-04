<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-DEFERRED-NONLINEAR-COMPETITION-BOUNDARY-20261005",
  "title": "延后求值在非线性碰撞、容量竞争与外来反馈下的边界",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "可逆二波补算、可加混龄对齐、固定延迟及自主门控/局部自反馈已各有有限证书；P07/P08在本批次提供多源匹配与反馈约束前置任务。",
  "next_action": "在一份既有当前残差上只加入一种明确的新竞争或外部输入规则，比较相同逻辑时刻、来源预算与完整目标输出，证明最大安全延后区间或给最小不可延后反例。",
  "dependencies": [
    "RS-BRC-MULTISOURCE-TRIAD-MATCHING-BUDGET-20261005",
    "RS-BRC-THRESHOLD-RELEASE-FEEDBACK-CONSTRAINT-20261005"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P10",
    "private-evidence:residual_deferred_collision_R1/PROOF.md",
    "private-evidence:residual_additive_late_R2/PROOF.md",
    "private-evidence:residual_timed_R8/PROOF.md",
    "private-evidence:residual_gated_R9/PROOF.md",
    "private-evidence:residual_feedback_R10/PROOF.md",
    "atomic-batch-parent:RS-BRC-MULTISOURCE-TRIAD-MATCHING-BUDGET-20261005",
    "atomic-batch-parent:RS-BRC-THRESHOLD-RELEASE-FEEDBACK-CONSTRAINT-20261005"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; FORMAL_DEPENDENCIES_VERIFIED_OR_ATOMIC_BATCHED; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "DEFERRED_EVALUATION",
    "NONLINEAR_COLLISION",
    "CAPACITY_COMPETITION",
    "EXTERNAL_FEEDBACK",
    "EVENT_ORDER"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-DEFERRED-NONLINEAR-COMPETITION-BOUNDARY-20261005",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P10",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-THRESHOLD-RELEASE-FEEDBACK-CONSTRAINT-20261005",
  "successor_gate": {
    "new_information_gap": "既有可逆二波补算、可加混龄对齐、固定延迟和局部门控/反馈都在各自有限条件内成立；外部输入、容量竞争或他Cell反馈会改变事件合法顺序，使原安全跳区间失效。",
    "why_parent_result_does_not_close_it": "P08只约束阈值/释放反馈表的合法关系，不证明延后求值在新竞争或外部输入下仍可交换；P07的多源匹配也不提供每步时序合法性。",
    "discriminating_outcomes": [
      "在一份既有当前残差上仅加入一种明确竞争/外部输入规则，证明一段最大安全延后区间，并给出维持该区间所需的最小到达/来源状态。",
      "构造最小不可延后反例：终态可相同或总量可相同，但某个中间未结算状态若被跳过，会改变容量分配、来源预算或不可撤销读出。"
    ],
    "kill_condition": "若新规则使状态关系不闭合，则保留所有受影响事件并返回精确拒绝证书；不得由一个成功/失败例子推广成“所有非线性都能/不能补算”。",
    "alternative_route_or_free_exploration_considered": "重跑原双缝全域可以回答特定实例但重复旧工作；同时加入多种竞争规则会难以定位边界。只加入一种明确新规则能给最小因果反例和安全区间。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "P08确定反馈规则的允许空间，本项进一步研究这些或其他单一新规则对延后求值/事件交换的影响；交付物是安全区间或拒绝证书，属于不同的时序问题。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 延后求值在非线性碰撞、容量竞争与外来反馈下的边界

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

在一份既有当前残差上，只加入一种明确的新竞争、容量或外部输入规则后，哪些到达/来源状态必须保留才能继续安全延后求值；最大安全跳区间在哪里，最小不可延后反例是什么？

## Frozen inputs and scope

共同项目语义服从 P000。继承本批 P07 `RS-BRC-MULTISOURCE-TRIAD-MATCHING-BUDGET-20261005` 的多源匹配/共享预算和 P08 `RS-BRC-THRESHOLD-RELEASE-FEEDBACK-CONSTRAINT-20261005` 的反馈表约束。冻结前沿：可逆二波补算、可加混龄对齐、固定延迟、自主门控和局部自反馈分别已有有限证书；这些结果只在原条件下有效。

本任务只新增**一种**竞争或外部输入规则，不重跑原双缝全域，不用终态相同代替每步时序合法。私有恢复入口 SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`。

## Hard target and required outputs

固定一份既有当前残差和一种新规则，明确事件到达、来源预算、容量占用、背景/他 Cell 反馈及不可撤销读出的时序语义。比较逐步求值与延后求值在相同逻辑时刻的完整状态。

交付最小需要保留的到达/来源状态；若可延后，给最大安全区间与证明；若不可延后，给最小严格反例和精确拒绝证书。未结算状态不得驱动不可撤销读出。费用分列下一事件判断、在途队列、背景、证书和输出，稀疏基线与密集反例分开。

## Research value to preserve

延后求值能否加速，关键不是最终总量是否一致，而是中间竞争是否会改变资源归属、来源预算或不可撤销观察。把一种新规则单独加入，可以精确定位安全交换律何时失效，并得到真正可执行的最小在途状态。

## Success, kill, and return criteria

成功：逐步与延后路径在相同逻辑时刻、来源预算和完整目标输出上可比较；给最大安全区间或最小拒绝见证，且未结算状态不触发不可撤销读出。

停止/否定：关系不闭合时保留受影响事件，不声称所有非线性作用都能补算；一个反例也不得外推到未声明规则。
