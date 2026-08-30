<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ADDMUL-FORMAL-GROUP-INTERPOLATION",
  "title": "加乘桥 A3 Formal Group Result envelope re-freeze V2",
  "kind": "RESEARCH",
  "owner": "research/addmul-formal-group-interpolation",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Re-freeze the already completed finite interpolating-law classification under a fresh execution with a contract-complete Result: add top-level return SHA-256, SHA-256 on every manifest row, and current canonical enum values for method harvest, independence and source exposure, without changing any formal-group theorem, truncation defect, primorial boundary or scope firewall.",
  "next_action": "Reproduce the frozen A3 return/checker/interface artifact from the accepted mathematical payload, create a fresh authorized execution record and NEW Result-ID, freeze return + checker + interface artifact + execution record with Git blob SHA-1 and SHA-256, and use only current Result enum values; any mathematical drift fails the maintenance task.",
  "dependencies": [
    "TP2-07769644BE60D76159D9",
    "RR-DDEA1AE4685D68564D55"
  ],
  "source_refs": [
    "research_returns/ADDMUL_FORMAL_GROUP_INTERPOLATION_RETURN_20260830.md",
    "research_checks/ADDMUL_FORMAL_GROUP_INTERPOLATION_CHECK_20260830.py",
    "research_artifacts/ADDMUL_FORMAL_GROUP_INTERPOLATION/FINITE_INTERPOLATING_LAW_INTERFACE_V1.json"
  ],
  "evidence_status": "MATHEMATICAL_PAYLOAD_RETAINED / RESULT_ENVELOPE_INCOMPLETE / ZERO_MATH_DRIFT_REFREEZE_REQUIRED",
  "last_progress_ref": "RR-DDEA1AE4685D68564D55",
  "last_progress_at": "2026-08-30T06:34:15+00:00",
  "hard_block": null,
  "tags": [
    "ADDMUL",
    "A3",
    "result-integrity",
    "envelope-refreeze",
    "maintenance",
    "zero-math-drift"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ADDMUL-FORMAL-GROUP-INTERPOLATION",
  "parent_objective_id": "OBJ-ADDMUL-BRIDGE-STRUCTURE",
  "parent_objective_generation_id": "OG-9D6617146723B8E72C6F",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "AMFGR2",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 加乘桥 A3 Formal Group Result envelope re-freeze V2

Status: `READY / RESULT INTEGRITY MAINTENANCE / ZERO MATH DRIFT`

## Mother question

已经完成的 `RR-DDEA1AE4685D68564D55` 数学内容能否在不改变任何定理、反例、截断缺陷或范围边界的前提下，以当前 Result 合同要求的完整双摘要证据链重新冻结？

## Frozen inputs and scope

冻结旧结果的数学内容：`F_c(x,y)=x+y+cxy` 的结合交换幺半群结构；`T_c(x)=1+cx` 的精确乘法 transport；信息 kernel 与逆映射定义域；有限 `Z/N` 与 nilpotent formal-jet interface；整数 log/exp 的 primorial 安全边界；普通多项式截断产生的 typed associativity defect 及其最小反例。旧 Result 保持不可变历史证据，不得编辑。第二个 A3 空 CLAIM 没有提交或 Result，不构成并行数学证据。

## Hard target and required outputs

Hard target: `RS-ADDMUL-FORMAL-GROUP-INTERPOLATION_RESULT_ENVELOPE_REFROZEN_WITH_COMPLETE_DIGEST_CHAIN_AND_ZERO_MATH_DRIFT`.

Required outputs：维护 return、确定性 checker、原 interface artifact、fresh execution record，以及 NEW Result-ID。新 Result 必须具有 top-level return SHA-256、每个 output manifest row 的 Git blob SHA-1 + SHA-256，并使用当前合法的 `method_harvest / independence_status / source_exposure_status` 枚举。

## Research value to preserve

A3 数学已经完成实质审读，阻塞点只在不可变 Result 信封不符合当前控制合同。修复证据链可保留研究价值，同时避免旧式不完整记录获得正式审核权威。

## Success, kill, and return criteria

Success：fresh execution 产生数学内容零漂移的新 Result-ID，双摘要链完整且当前审计通过。若 return/checker/interface 的定理内容发生任何实质变化，立即 kill 本维护任务并改走 substantive revision，而不能伪装成信封重冻。本维护任务不得借机开启更强 formal-group 数学。