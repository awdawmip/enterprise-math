<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SEVEN-PHASE-RAW-NOISE-RADIUS",
  "title": "七点与八点相位解码的原始读数噪声锐半径",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "DRAFT",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "三个或四个差分输出在最大范数下已有锐半径。原始位置误差经重叠差分形成相关向量，已有输入充分界未给出其最优性。",
  "next_action": "对 n=7、8 写出第四差分矩阵 H，比较两相位轨道在由集合 H[-1,1]^n 诱导距离下的分离量，检查达到边界的原始噪声。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/shape-seven.md",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/shape-lp.py",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/shape_decode.py"
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
  "registry_key": "RS-SEVEN-PHASE-RAW-NOISE-RADIUS",
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

# 七点与八点相位解码的原始读数噪声锐半径

在已有六个有序相位模板 S_a 上，差分后的理想信号为 A S_a+B·1。给定 g>0，分别研究 A≥g 和 |A|≥g，B 未知。每个原始读数允许独立的加性误差 |w_i|≤ε，观测变成 A S_a+B·1+H w；H 为 n−4 行的相邻四阶差分矩阵。本题研究利用差分观测的任意解码器可保证唯一辨识的最优半径。保持各候选解释各自合法的 A、B、w。
对 n=7,8 的四个模型分别给出阈值，或给出经过认证的上下界及尚缺的差距。要称为锐值，须同时给出所有相位对的分离下界和在半径边界产生同一观测的两组合法原始数据。已知输出级 30g、60g 及相应输入充分界用作复核；将输出阈值除以 16 尚不足以确定输入锐值。若半径可通过有理线性规划得到，交回可独立复算的原始空间证书。
