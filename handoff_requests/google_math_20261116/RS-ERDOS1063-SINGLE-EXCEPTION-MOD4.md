<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ERDOS1063-SINGLE-EXCEPTION-MOD4",
  "title": "Erdős 第 1063 题的周期计数模 4 分类",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "DRAFT",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "一个最小周期的成功类数 H_k 的奇偶已定。H_k 为偶数时，哪些 k 满足 H_k≡2 (mod 4) 仍缺少结构判据。",
  "next_action": "从已存 CRT 局部表按反射位置配对，对非中心位置的单点计数提取奇偶贡献，核对与直接计数的模 4 结果。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/erdos-reflection.md",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/erdos_parity.py",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/erdos_parity.json"
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
  "registry_key": "RS-ERDOS1063-SINGLE-EXCEPTION-MOD4",
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

# Erdős 第 1063 题的周期计数模 4 分类

对 k≥3，令 P_k=lcm(1,…,k)·lcm(1,…,⌊k/2⌋)。H_k 统计 n mod P_k 中恰有一个 0≤i<k 使 n−i 不整除 C(n,k) 的类。已知 H_k 为奇数恰对应 k=2^j−1、j≥3。k=2 的具名周期和布尔最小周期分别处理。
目标是刻画 H_k≡2 (mod 4) 的 k，或在明确的无限子族上给出判定定理并确定仍未覆盖的情形。另一可交付结果是可证明地减少所需局部计数的模 4 判据，给出相对原 CRT 逐位置累加节省的对象或运算。直接对已有输出取余仅作基准。如果提出单由 k 的低位或反射固定点决定的规律，应标明输入族，并给出证明或能区分该规律的反例和剩余贡献。交回论证、精确核算程序、与可枚举小周期的交叉结果，以及适用范围。
