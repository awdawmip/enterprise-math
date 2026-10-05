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
  "task_id": "RS-BRC-FUSION-C2-OWNERSHIP-REFERENCE-INTEGRATION-20261005",
  "title": "已验证融合与C2所有权转移的参考执行集成",
  "frontier": "origin8例/16配对、三节点32mask顺序冷暖、C2四组加三拒绝均已完成；实际复制100→61，基线逻辑253/实现替换214分列，不能冒充全S15或墙钟收益。P01已正式发布用于固定早期证据版本。",
  "next_action": "冻结同48请求、两预算和完整输出，只在隔离参考副本中集成已验证新增变体；复用旧基线输出/证明，不重跑完成局部组，不改生产，并逐执行路径检查真实别名、对象生命期、所有权转移和比较开销。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P18",
    "private-evidence:EM_S15SUPPORT_ORIGIN_FUSION_CERTIFICATE.json",
    "private-evidence:EM_S15SUPPORT_THREE_NODE_CERTIFICATE.json",
    "private-evidence:EM_S15SUPPORT_FOUR_LEAF_CERTIFICATE.json",
    "private-evidence:shor_online_S14/PROTOCOL.json",
    "https://github.com/awdawmip/enterprise-math/blob/dd9b44fafe3e6a02c5c6c8ba825e1f130a05bfe5/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; P01_CURRENT_PUBLICATION_VERIFIED; PRIOR_COMPLETED_UNITS_CONSUMED_WITHOUT_REPLAY; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "FUSION",
    "C2",
    "OWNERSHIP_TRANSFER",
    "REFERENCE_EXECUTION",
    "ALIASING",
    "LIFETIME",
    "COPY_LEDGER"
  ],
  "registry_key": "RS-BRC-FUSION-C2-OWNERSHIP-REFERENCE-INTEGRATION-20261005",
  "identity_lane": "P18",
  "parent_task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "successor_gate": {
    "new_information_gap": "局部等价与C2所有权规则尚未接到固定48请求/两预算的完整参考副本；真实别名、对象生命期、比较开销和峰值内存需要逐执行路径检查。",
    "why_parent_result_does_not_close_it": "P01只固定证据版本和归属；已完成origin8、三节点32mask与C2局部组也不证明完整固定工作负载集成后的输出、生命周期和成本保持。",
    "discriminating_outcomes": [
      "在隔离参考副本中集成新增变体后，完整输出字节、外部输入/身份、转移句柄/活叶、共同初memo/key多重集与基线保持合同一致，并给实际ledger、逻辑账和实现账。",
      "若出现第二消费者、逃逸、不可控别名或同期基线总成本缺失，则拒绝优化或只报告新变体成本，不宣称全局加速。"
    ],
    "kill_condition": "禁止重跑已完成局部组、修改生产、跨比较C1六输出与C2四叶；隐藏Python别名不能据此声称普遍探测。",
    "alternative_route_or_free_exploration_considered": "可以直接修改生产或重测全部S15，但会改变风险边界并重复已完成工作。隔离参考副本是验证集成语义和所有权的最小安全路线。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "局部证书已完成，本项专门检查固定工作负载的完整集成、生命周期与实际copy账，交付物不同。"
  }
}
-->

# 已验证融合与C2所有权转移的参考执行集成
Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question
已经通过局部证书的融合与 C2 所有权转移，在固定 48 请求、两预算和完整输出合同下接入隔离参考副本后，能否保持输出与生命周期语义，同时真正减少 copy 或执行成本？

## Frozen inputs and scope
共同项目语义服从 P000。P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 只固定早期证据版本与归属。
冻结前沿：origin 8 例/16 配对、三节点 32 mask 顺序冷暖、C2 四组加三拒绝均已完成；实际复制 100→61，基线逻辑 253/实现替换 214 分列，但这不是全 S15 或墙钟收益。C1 六输出和 C2 四叶绝不跨合同比较。
私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。

## Hard target and required outputs
冻结同 48 请求、两预算与完整输出，只在隔离参考副本集成已验证新增变体；旧基线输出/证明复用，不重跑已完成局部组，不改生产。
逐执行路径核对新变体完整输出字节、外部输入/身份、转移句柄/活叶、共同初始 memo/key 多重集、真实别名、第二消费者、逃逸和对象生命期。构造、生命周期分析、融合判断、所有读取/写出/删除、真实 copy、逻辑账、实现账、验证和峰值内存全部分列。

## Research value to preserve
局部融合正确不等于完整参考执行安全。真正价值在于证明所有权转移不会改变输出合同、泄露别名或把逻辑减少误写成实际执行加速。

## Success, kill, and return criteria
成功：完整固定工作负载下的输出、所有权和 ledger 可回放，第二消费者/逃逸/受控别名被严格处理。
停止/否定：同期基线全成本未获量测时只报告新变体成本，不宣称加速；不把隐藏 Python 别名探测外推为普遍能力。
