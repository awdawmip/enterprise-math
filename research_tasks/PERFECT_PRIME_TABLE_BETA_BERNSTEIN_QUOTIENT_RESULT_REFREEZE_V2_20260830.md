<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "title": "Perfect Prime Table Beta-Bernstein quotient 结果完整性重冻结 V2",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-table-critical-cofactor-all-m-proof",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Re-freeze the already-completed Beta-Bernstein all-m frontier under a complete current result envelope, preserving the reduction to det(I_{m-1}-Q_m) != 0 and all proved STP/common-measure structure without reopening earlier generic-STP or sign-regularity routes.",
  "next_action": "Reproduce the frozen return and exact checker from the pinned prior execution, emit a no-mathematical-delta revision return, and freeze a new Result-ID whose output manifest binds every frozen output with Git blob SHA-1 and SHA-256.",
  "dependencies": [
    "research_tasks/PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF_20260828.md@main",
    "research_objective_records/OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M/OG-9CD71978EC19A9D5B7FA.json@main"
  ],
  "source_refs": [
    "research/perfect-prime-table-critical-cofactor-all-m-proof-em-ppta-6d8f31@e9bc32b33b56b26af73824c4ed21c9b0686ac85e",
    "research_returns/PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF_RETURN_20260828.md@blob:e6d67ffeea432f52e7b15fe03eb6a07d98ade476",
    "scripts/check_perfect_prime_table_critical_cofactor_all_m_proof.py@blob:822e99b5cdcf823cc1b2b7beab335f221f09d661"
  ],
  "evidence_status": "BETA_BERNSTEIN_FRONTIER_FROZEN / RESULT_ENVELOPE_INCOMPLETE / NO_MATH_DELTA_RECOVERY",
  "last_progress_ref": "research/perfect-prime-table-critical-cofactor-all-m-proof-em-ppta-6d8f31@e9bc32b33b56b26af73824c4ed21c9b0686ac85e",
  "last_progress_at": "2026-08-28T13:57:22+00:00",
  "hard_block": null,
  "tags": ["perfect-prime-table","Route-A","Beta-Bernstein","Mobius-quotient","result-integrity","all-m","STP","no-math-delta"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTABBR2",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "successor_gate": {
    "new_information_gap": "The strongest execution isolated the all-m theorem to a common-measure Beta-Bernstein Mobius quotient, but its immutable Result record pins only the return while the same frozen execution also produced the checker and execution record; current review authority therefore cannot consume it.",
    "why_parent_result_does_not_close_it": "The missing digest bindings occur in the immutable Result envelope and cannot be repaired by weakening, editing, or reinterpreting the existing Result.",
    "discriminating_outcomes": [
      "a new Result-ID reproduces the exact frozen mathematics and binds return, checker, execution record and every other frozen output with SHA-1 and SHA-256",
      "the exact checker or frozen source fails to reproduce, forcing substantive revision rather than envelope repair",
      "the revision changes theorem content, in which case the no-math-delta recovery fails"
    ],
    "kill_condition": "Do not reopen generic STP sufficiency, entrywise Perron-Frobenius, ordinary norm contraction, the falsified full sign-regularity shortcut, or finite-m verification as a substitute for the isolated all-m quotient problem.",
    "alternative_route_or_free_exploration_considered": "Restarting from the older Frobenius frontier would discard verified progress. Publishing a new mathematical successor before repairing the evidence chain would build on a nonreviewable Result. Integrity-only re-freeze is the smallest safe action.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The existing Result is immutable and incomplete under the current digest contract. A superseding publication generation permits a new execution/result chain while preserving the old bytes as history."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime Table Beta-Bernstein quotient 结果完整性重冻结 V2

## Mother question

已经完成的 Route-A 执行把 all-m critical cofactor 非退化问题进一步压缩为显式 common-measure Beta-Bernstein Möbius quotient `Q_m` 上的

`det(I_{m-1}-Q_m) != 0`。

数学前沿已经冻结，但旧 Result envelope 没有完整绑定同一执行产生的 checker 与 execution record。如何在**零数学漂移**条件下恢复完整、可审核的 evidence chain，并让后续 Driver 只从这个最新前沿继续？

## Frozen inputs and scope

1. 冻结旧执行 branch head：`e9bc32b33b56b26af73824c4ed21c9b0686ac85e`。
2. 冻结旧 return blob：`e6d67ffeea432f52e7b15fe03eb6a07d98ade476`，其旧 Result 所列 SHA-256 为 `3c249fd8acc8cf55b2294e05dfe47035485187d224a3955cf3dc707e27e6a1b2`。
3. 冻结旧 checker blob：`822e99b5cdcf823cc1b2b7beab335f221f09d661`。
4. 冻结旧 execution record：`ER-B05E70EFD72590BCB0BF`；新执行必须形成自己的 current execution record，不能把旧 execution id 当作新 provenance。
5. 数学内容不得改变：
   - `(WHW)^(-1)` 的 STP 结构；
   - `A=Ahat R`、`B=Bhat R` 型 binomial-Möbius / Beta-Bernstein common-measure reduction；
   - hard target 尚未闭合；
   - 当前剩余精确问题为 `det(I_{m-1}-Q_m) != 0` 对所有 admissible `m`，或 exact counterexample；
   - generic STP alone 不足；
   - entrywise PF、普通 `l_infinity` contraction 与先前 full sign-regular core shortcut 不得复活。
6. 本 revision 不尝试证明 `det(I-Q_m) != 0`；只恢复证据链。若复现中发现数学差异，必须返回 substantive revision，而不是静默修改旧结论。

## Hard target and required outputs

Hard target:

`PPTA_BETA_BERNSTEIN_FRONTIER_RESULT_ENVELOPE_REFROZEN_WITH_ZERO_MATH_DRIFT`。

必需输出：

1. revision return，逐条声明与冻结 return 的数学内容一致；
2. deterministic exact checker；
3. current execution record；
4. 新 immutable Result-ID；
5. Result `output_manifest` 对每一个冻结输出都同时给出 `path + Git blob SHA-1 + SHA-256`；
6. 若还有 certificate/artifact 被 revision 冻结，也必须进入 manifest；
7. return 中明确写出下一数学前沿仍是 common-measure Beta-Bernstein Möbius quotient 的 all-m eigenvalue-1 exclusion。

## Research value to preserve

这条支线已经从“Perfect Prime Table 看起来满秩”推进到一个非常窄的谱/全正性问题。真正有价值的累积是：多个早期 shortcut 已被排除，剩余对象不再是 generic STP pair，而是**同一 Beta measure 连接的两个 Beta-Bernstein moment structures 经 Möbius reversal 形成的 quotient**。

重做早期搜索会丢失这层压缩。修复 envelope 后，下一研究应优先 exterior powers、principal-angle 或 oscillation arguments，并使用 `u -> u^m` 的 common-measure order structure。

## Success, kill, and return criteria

成功仅指 evidence-chain 完整恢复，不等于 all-m theorem 得证。

Kill conditions：

- 任何数学 theorem、domain、counterexample 或 reduction 发生未声明变化；
- 只复制旧 Result-ID 或修改旧 immutable record；
- manifest 漏掉本次实际冻结的输出；
- 用 finite `m` checker 通过替代 all-m theorem；
- 重新采用已被旧执行排除的 generic shortcut；
- 在证据链修好之前直接声称 mother theorem closed。
