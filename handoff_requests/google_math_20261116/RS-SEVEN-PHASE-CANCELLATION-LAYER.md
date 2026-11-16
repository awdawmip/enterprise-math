<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SEVEN-PHASE-CANCELLATION-LAYER",
  "title": "共同分子误差抵消后的次阶相位辨识",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "DRAFT",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已知极限增益 A=(1+u)/(1+v)^2。在 u=−1 六相的首阶形状重合，既有余项 O(1/r) 未说明次阶能否恢复相位。",
  "next_action": "从精确 C(q),T(q) 计算七点窗口的次阶相位差，选择 v=0、λ=0 基准并核验可实现的整误差序列，随后比较有界参数区域。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/joint-seven-proof.md",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/joint_check.py",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/shape-seven.md"
  ],
  "evidence_status": "TASKBOOK_DRAFT_V2",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PENDING_PUBLICATION",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-SEVEN-PHASE-CANCELLATION-LAYER",
  "parent_objective_id": "OBJ-GOOGLE-20261116-ERDOS1063-SEVEN-PHASE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# 共同分子误差抵消后的次阶相位辨识

固定五来源计数、七个连续样本及三个相邻四阶差分。写 u=25920e/r⁶，v=4320d/r⁵。考虑 u=−1+λ/r 的边界层，λ 有界，|v|≤δ<1。明确整 e,d 的取整方式和误差阶，比较不同 r mod 6 时选取一致的参数约定；若将 v 替换为其极限，跟踪偏差对次阶的影响。
先界定参数已知时哪些相位可区分，再单独研究参数未知、每个候选相位可用不同合法参数时哪些相位仍可统一分离。可采用商去共同平移的观测，须说明所保留的信息与误差范数。交回首个可检验的次阶展开和余项控制、可分参数域或明确的碰撞证据，并用原始整数计数核验六种相位。若仅证得某阶丢失全部或部分信息，标明该阶和相位对，勿据此断言所有更高阶也丢失。
