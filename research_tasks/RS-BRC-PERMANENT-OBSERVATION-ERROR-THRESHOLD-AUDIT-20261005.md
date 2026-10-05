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
  "task_id": "RS-BRC-PERMANENT-OBSERVATION-ERROR-THRESHOLD-AUDIT-20261005",
  "title": "永久观察合同与误差门槛的独立证明校核",
  "frontier": "对话已修复有限自治周期相位论证：固定x0=(1,0)，P门槛1，R门槛sqrt(2-sqrt3)，精确Q不可能；旧错误结论不得复活。P01已正式发布用于固定相关证据版本与归属。",
  "next_action": "对已有三个声明构造最小依赖图和逐行独立数学审计；列准确定理、机器Z/f/g/初始化/时间范围、恒零见证、每周期相位稠密证明与极限方向，只补遗漏前提、有限辅助证书或反例，不扩新模型。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P20",
    "private-evidence:rational_cell_continuation/INFINITE_OBSERVATION_AND_CERTIFIED_ZERO_TAIL_20261002.md",
    "private-evidence:CONVERSATION_FRONTIER.md",
    "https://github.com/awdawmip/enterprise-math/blob/dd9b44fafe3e6a02c5c6c8ba825e1f130a05bfe5/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; P01_CURRENT_PUBLICATION_VERIFIED; PRIOR_COMPLETED_UNITS_CONSUMED_WITHOUT_REPLAY; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "PERMANENT_OBSERVATION",
    "ERROR_THRESHOLD",
    "PROOF_AUDIT",
    "DENSITY",
    "HALF_OPEN_CELL",
    "QUANTIFIER_SCOPE"
  ],
  "registry_key": "RS-BRC-PERMANENT-OBSERVATION-ERROR-THRESHOLD-AUDIT-20261005",
  "identity_lane": "P20",
  "parent_task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "successor_gate": {
    "new_information_gap": "一般证明与聊天推导尚未独立校核；输出范围、极限点、半开胞、固定初态/标签、真轨道见证与合成输出的量词容易混用。",
    "why_parent_result_does_not_close_it": "P01只固定版本和证据归属；它不独立审计三个永久观察声明的定理量词、初始化、时间范围、稠密性步骤和误差门槛。",
    "discriminating_outcomes": [
      "给出三个声明的最小依赖图和逐行独立审计，明确Z/f/g、初始化、时间范围、恒零见证、每周期相位稠密与极限方向，并映射旧错误撤回点。",
      "若发现量词、半开边界或真轨道见证存在缺口，则缩窄为局部命题并保留不确定项，不依赖摘要或对话结论自证。"
    ],
    "kill_condition": "不扩新模型、不生成新轨迹实验、不把经典稠密性重报为新发现；不能证明的步骤保持未决，不自动推广到所有初态。",
    "alternative_route_or_free_exploration_considered": "可以重新做数值轨迹实验或扩展模型，但不能替代独立证明校核。本项只允许有限代数/整数辅助证书，用于检查既有声明。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "旧对话已经修复一处错误，本项要把三个声明独立审计并固定正确量词和门槛，是从聊天推导到可核验证明的不同阶段。"
  }
}
-->

# 永久观察合同与误差门槛的独立证明校核
Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question
对已有三个永久观察声明做独立逐行证明校核后，固定初态、时间范围、半开胞、真轨道见证和误差门槛的量词是否都正确；旧对话修复后的门槛能否在不扩新模型的情况下得到可核验定理？

## Frozen inputs and scope
共同项目语义服从 P000。固定 `x0=(1,0)` 属于两坐标部分/外部辅助表示，**不是完整三维切片，遗漏第三坐标不得默认补 0**；本任务不据此做原生三维推广。
P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 只固定材料版本和归属。冻结前沿：有限自治周期相位论证已在对话中修复；P 门槛为 1，R 门槛为 `sqrt(2-sqrt(3))`，精确 Q 不可能；旧错误结论不得复活。
私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。

## Hard target and required outputs
对已有三个声明构造最小依赖图与逐行独立数学审计。列出准确定理、机器 `Z/f/g`、初始化、时间范围、恒零见证、每周期相位稠密证明与极限方向，并附旧错误撤回映射。
只补遗漏前提、反例或证明检查器可接受的有限代数/整数辅助证书；不扩新模型，不生成新的轨迹实验，不把经典稠密性重报为新发现。证明审查与有限辅助校核成本单列。

## Research value to preserve
对话中的修复只有经过独立量词与依赖审计，才能避免把输出范围、极限点、半开胞或合成输出误当真轨道结论。该任务固定可用的永久观察合同和误差门槛，而不制造新模型。

## Success, kill, and return criteria
成功：三个声明的定理、依赖、初始化、时间范围、恒零见证、相位稠密与极限方向全部逐行可核验，并明确旧错误撤回。
停止/否定：发现缺口则保持局部命题和不确定项；不把摘要信任当独立验证，不自动推广所有初态。
