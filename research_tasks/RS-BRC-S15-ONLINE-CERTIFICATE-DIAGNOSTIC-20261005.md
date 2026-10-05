<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-BRC-S15-ONLINE-CERTIFICATE-DIAGNOSTIC-20261005",
  "title": "S15稳定校准的在线决策证书与诊断负担",
  "frontier": "S15已执行：11次改选观察7利4害，8→1含菜单轨迹变化；384请求均无合法在线误差/漂移联合证书，pseudo=1/window8/clip[1/4,4]已核对。P01已正式发布用于固定早期证据版本与归属。",
  "next_action": "仅从既有冻结日志构造固定菜单、固定selected-history的机制分解与有限可达结构界；逐请求核对先验可用字段、伪计数/clip/取整顺序和替换交互，只在独立前提成立处输出在线证书，其余保持UNCERTIFIED。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P16",
    "private-evidence:S14_S15_INDEPENDENT_RESULT_EM_S15SUPPORT_866CDE_20261001.json",
    "private-evidence:S15_MINIMAL_SUPPLEMENT.json",
    "private-evidence:shor_online_S14/PROTOCOL.json",
    "https://github.com/awdawmip/enterprise-math/blob/dd9b44fafe3e6a02c5c6c8ba825e1f130a05bfe5/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; P01_CURRENT_PUBLICATION_VERIFIED; PRIOR_COMPLETED_UNITS_CONSUMED_WITHOUT_REPLAY; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "S15",
    "ONLINE_CERTIFICATE",
    "CALIBRATION",
    "DIAGNOSTIC_COST",
    "SELECTED_HISTORY",
    "UNCERTIFIED"
  ],
  "registry_key": "RS-BRC-S15-ONLINE-CERTIFICATE-DIAGNOSTIC-20261005",
  "identity_lane": "P16",
  "parent_task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "successor_gate": {
    "new_information_gap": "既有S15执行没有独立结构漂移界，不能用当前pairing/verifier或历史max冒充在线保证；预测MAE、科学数与诊断时间也不能直接相加。",
    "why_parent_result_does_not_close_it": "P01只修复证据版本、作者和归属，不提供S15在线结构漂移界、逐请求可认证条件或诊断成本分解。",
    "discriminating_outcomes": [
      "从冻结日志给出逐请求可认证所需的先验字段、pseudo/clip/取整真实顺序、替换顺序和交互项，并仅在独立前提成立时输出在线证书。",
      "若无法获得合法当前状态界，则明确返回UNCERTIFIED，保留已完成S15执行和7利4害观察，不把不可认证误写成无效实验。"
    ],
    "kill_condition": "禁止重跑S15、重训或改变选择；若只能靠当前pairing/verifier、历史最大值或零改选观察来制造保证，则停止并返回不可认证。",
    "alternative_route_or_free_exploration_considered": "可以重新运行或调参以制造更好历史，但会污染已冻结执行。本项只做只读证书和机制分解，以隔离认证能力与既有选择结果。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "P01解决证据归属；本项解决已完成S15数据能否支持在线决策证书及其诊断负担，交付物是认证或UNCERTIFIED边界而非重复执行。"
  }
}
-->

# S15稳定校准的在线决策证书与诊断负担
Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question
从既有冻结 S15 日志出发，在不重跑、重训或改变选择的前提下，能否对固定菜单和固定 selected-history 给出真正在线可用的决策证书；如果不能，哪些请求必须保持 `UNCERTIFIED`，诊断本身需要付出多少成本？

## Frozen inputs and scope
共同项目语义服从 P000。P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 仅固定早期证据版本与归属。
冻结事实：S15 已执行；11 次改选观察为 7 利 4 害，8→1 含菜单轨迹变化；384 请求均没有合法在线误差/漂移联合证书；`pseudo=1/window8/clip[1/4,4]` 已核对。不得把这些完成项重新运行后计为新成果。
私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。

## Hard target and required outputs
只读取冻结日志。逐请求列出决策前可用字段、伪计数/clip/取整真实顺序、替换顺序及交互项，并在固定菜单、固定 selected-history 下构造机制分解和有限可达结构界。
只在独立前提真正成立时输出在线证书，其余返回 `UNCERTIFIED`。预测 MAE、科学数和诊断时间分账，不允许直接相加；元数据获取、预测、证书、配对/独立检查和诊断开销全部收费。

## Research value to preserve
既有 S15 结果已经包含真实改选利害与失败的在线认证尝试。价值在于把“实际做过什么”“现在能证明什么”和“诊断需要付多少钱”分开，而不是通过重跑覆盖原历史。

## Success, kill, and return criteria
成功：逐请求认证前提、运算顺序、替换交互和同一见证历史可回放，诊断成本独立列示。
停止/否定：拿不到合法当前状态界就保持 `UNCERTIFIED`；不把零观察改选称硬阻断，也不抹掉既有执行。任务终止于在线证书或明确不可认证边界。
