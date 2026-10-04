<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-R11-LOCAL-PERTURBATION-CYCLE-RECOVERY-20261005",
  "title": "R11局部扰动后的周期恢复与受影响域更新",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "R11给活动二态/全域六拍的完整当前状态证书；有限性不保证普遍高效；P01已正式发布证据/版本归属修复任务。",
  "next_action": "从R11已有完整检查点施加一个预声明局部扰动，明确影响域和旧周期证书的失效/再认证条件，并与同一扰动的逐步语义比较完整目标场、端口活动及来源。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P09",
    "private-evidence:residual_cycle_R11/PROOF.md",
    "private-evidence:residual_feedback_R10/PROOF.md",
    "https://github.com/awdawmip/enterprise-math/blob/06754542f6e552c705958dee9987096066414a84/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; FORMAL_DEPENDENCIES_VERIFIED_OR_ATOMIC_BATCHED; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "R11",
    "LOCAL_PERTURBATION",
    "CYCLE_RECOVERY",
    "AFFECTED_DOMAIN",
    "RECERTIFICATION"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-R11-LOCAL-PERTURBATION-CYCLE-RECOVERY-20261005",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P09",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "successor_gate": {
    "new_information_gap": "R11已有活动二态/全域六拍完整当前状态证书，但局部改变少数残差或边界后，旧周期证书何处失效、影响域是否有限、何时可以局部再认证尚未执行。",
    "why_parent_result_does_not_close_it": "P01只负责源材料版本与归属，不研究R11检查点在局部扰动后的动力学更新；读取旧周期本身也不能证明扰动后仍可复用。",
    "discriminating_outcomes": [
      "对一个预声明局部扰动给出受影响域、旧周期证书失效边界和局部/全局再认证条件，并与同一扰动的明确逐步语义在完整目标场、端口活动和来源上逐项一致。",
      "给出反例证明扰动导致密集影响或长新周期，使局部恢复无收益；据此保留完整逐步更新而非强行周期跳跃。"
    ],
    "kill_condition": "若影响迅速变密或新周期长到局部恢复无收益，则停止优化并保留该事实；不得从总量、背景重复或旧周期直接跳过完整状态。",
    "alternative_route_or_free_exploration_considered": "整域从零重跑始终可行但浪费已验证检查点；直接沿用旧六拍又不安全。局部影响域+再认证是最小可验证增量路线。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "P01解决证据身份，P09消费已验证R11检查点研究一个新的扰动恢复问题；交付物是失效/再认证条件和影响域证书，不能由P01或读取旧周期代替。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R11局部扰动后的周期恢复与受影响域更新

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

从 R11 已验证的完整检查点出发，对一个预声明局部扰动，旧周期证书在哪些 Cell/端口上失效，影响是否只传播到有限域，何时可以局部重建并重新认证周期？

## Frozen inputs and scope

共同项目语义服从 P000。P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 仅提供证据/版本归属前置。冻结科学前沿：R11 已给活动二态与全域六拍完整当前状态证书，但有限性不保证普遍高效。读取旧周期不是新发现，也不证明扰动后周期仍有效。

背景仍按逐 Cell 语义一致，不允许用总量或背景重复替代完整状态。私有恢复入口 SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`。

## Hard target and required outputs

选定一个明确局部扰动（少数残差、端口或边界字段），从 R11 检查点开始确定可能受影响的最小域；声明旧周期证书的失效条件、可局部复用条件和再认证条件。

必须与同一扰动的明确逐步语义比较完整目标场、端口活动及来源；若找到新周期，给周期起点、长度和全状态证书；若没有收益，给密集影响或长周期反例。费用分列影响域判定、局部重建、周期搜寻、重验证与完整输出。

## Research value to preserve

周期证书的价值来自“状态真的回到同一完整状态”，不是来自背景或总量相似。局部扰动后若能证明影响域有限，就能复用大部分既有证书；若影响迅速扩散，则应及时停止局部优化。这个边界决定周期加速是否真正可靠。

## Success, kill, and return criteria

成功：受影响域、旧证书失效点、局部更新和再认证条件明确，且与逐步语义在完整目标场/端口/来源上吻合。

停止/否定：密集影响或长周期导致无收益必须保留；不得从总量/背景重复跳过完整状态，也不得把读取旧周期计为新发现。
