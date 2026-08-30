<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "research/seed6-degenerate-strata-global-gluing",
  "base_state": "READY",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-SEED6-MULTIPLICATIVE-GROWTH-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-SEED6-DEGENERATE-STRATA-GLOBAL-GLUING",
  "claim_lease_minutes": 240,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-SEED6-DEGENERATE-STRATA-GLOBAL-GLUING",
  "title": "Seed-6 退化层全局拼接结果完整性重冻结 V2",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Re-freeze the already-frozen Seed-6 degenerate-strata global-gluing mathematics under a complete execution-linked result manifest, repairing the missing SHA-256 bindings without changing any theorem, model, counterexample, or interpretation.",
  "next_action": "Reproduce the existing exact checker, emit a no-mathematical-delta revision return, and freeze a new result whose every output-manifest row contains path, Git blob SHA-1 and SHA-256; verify the local result audit before returning for Driver review.",
  "dependencies": [
    "research_returns/SEED6_DEGENERATE_STRATA_GLOBAL_GLUING_RETURN_20260830.md@main",
    "driver_reviews/SEED6_DECORATED_CARRIER_AND_DEGENERATE_GLOBAL_GLUE_DRIVER_REVIEW_20260830.md@main"
  ],
  "evidence_status": "MATHEMATICAL_PAYLOAD_DRIVER_PASS_PENDING_RESULT_RECORD_INTEGRITY_REPAIR",
  "tags": [
    "seed6",
    "result-integrity",
    "manifest-refreeze",
    "degenerate-strata",
    "global-gluing",
    "no-math-delta"
  ],
  "registry_key": "RS-SEED6-DEGENERATE-STRATA-GLOBAL-GLUING",
  "identity_lane": "S6DGGV2",
  "successor_gate": {
    "new_information_gap": "The mathematical return is complete at the declared typed-CW strength, but its immutable result record omits SHA-256 fields on two output-manifest rows, so the current digest chain cannot receive terminal Driver acceptance.",
    "why_parent_result_does_not_close_it": "The missing SHA-256 bindings are in the immutable result record itself and cannot be repaired by interpreting the theorem more weakly or by editing the existing record.",
    "discriminating_outcomes": [
      "a new execution-linked result reproduces the frozen mathematical payload and has a complete manifest for every declared output",
      "the existing checker fails to reproduce the frozen payload, in which case the task returns for substantive mathematical revision",
      "the new return changes any mathematical theorem or scope, in which case the no-math-delta repair fails"
    ],
    "kill_condition": "Do not alter the resonance-pinch theorem, H1/H2 formulas, carrier-height cocycle, support-safety rules, operator-lift boundary, or any factorization-free scope merely to obtain a clean record.",
    "alternative_route_or_free_exploration_considered": "Closing the task would leave the reviewed digest chain structurally incomplete. Publishing new geometry before repairing the record would build on nonterminal control evidence. A narrow re-freeze is the smallest safe action.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The current publication already produced an immutable malformed result record. A superseding revision generation preserves the old bytes as history while allowing a clean new execution/result chain."
  }
}
-->
# Seed-6 退化层全局拼接结果完整性重冻结 V2

## Mother question

现有 Seed-6 退化层全局拼接数学已经冻结，Driver 对其声明强度的数学内容没有要求改写。唯一问题是：当前 immutable result record 的两个 `output_manifest` 行缺少 SHA-256，因此如何在**零数学漂移**条件下重新形成一条完整、可审核的 execution → return → result digest chain？

本任务不是继续发现新规律，而是把已经完成的数学结果重新冻结成完整证据。

## Frozen inputs and scope

1. 冻结源 return：
   `research_returns/SEED6_DEGENERATE_STRATA_GLOBAL_GLUING_RETURN_20260830.md`
   - return Git blob: `sha1:51fa53affb4ce9cb71024922822fe7851b7c3525`
   - return SHA-256: `sha256:927a93285cd0d309dd7372fb93f67ba918079333a929f8f55195745b4fb0bfa9`
2. 冻结的数学强度不得改变：
   - support-retaining `3:2` resonance pinch；
   - `X_str(R) ~= K_R vee (vee^m S^1)`；
   - `H1` rank 增加 `m`，`H2=0`；
   - carrier-height cocycle / mod-2 row holonomy；
   - horizontal transport flat；
   - global pairing-state `S3` connection 未建立；
   - atom-level `S4` lift 仍有 `V4` ambiguity。
3. 当前旧 result record `RR-1386FD1AA93DB153E701` 保留为 immutable history，不修改、不删除。
4. 不引入新的 `(a,b)` generalization，不新增 resonance theorem，不扩展 operator connection。
5. 不引入 additive distance、factor recovery、factorization performance、smooth curvature 或 manifold 解释。
6. 允许重新执行现有 checker；若 checker 与冻结 return 冲突，必须报告 substantive revision，而不能改记录掩盖冲突。

## Hard target and required outputs

Hard target:

`RESULT_MANIFEST_INTEGRITY_REPAIRED_WITHOUT_MATHEMATICAL_DRIFT`

Required outputs:

A. 新的 revision return：

`research_returns/SEED6_DEGENERATE_STRATA_GLOBAL_GLUING_MANIFEST_REFREEZE_RETURN_20260830.md`

其中必须明确列出：
- 源 return 的 blob 与 SHA-256；
- `MATHEMATICAL_DELTA = NONE`；
- 重放 checker 的结果；
- 新 result manifest 的完整性审计；
- 若有任何数学变化，则任务不得以 SUCCESS 结束。

B. 至少一个 machine-readable integrity artifact：

`research_artifacts/SEED6_DEGENERATE_STRATA_GLOBAL_GLUING_REFREEZE/manifest_audit.json`

记录所有被新 result 声明为 output 的：
- path；
- Git blob SHA-1；
- SHA-256。

C. 新 execution-linked result record 的每个 `output_manifest` 行必须同时包含：
- `path`；
- `git_blob_sha1`；
- `sha256`。

D. 新 result record 必须绑定本 revision publication 与新的 execution record，而不是伪装成旧 publication 的修补。

E. 本地 result audit 对新 result 链必须无该任务相关错误。

## Research value to preserve

本任务要保护的不是格式本身，而是以下研究价值：

1. 已完成的 resonance-pinch 数学不因控制面缺陷被丢失；
2. support-retaining 与 support-erasure 的边界保持不变；
3. 真正的 `H1` / carrier-row holonomy 证据与伪 `H2` 区分保持不变；
4. 后续 decorated-carrier generalization 只消费完整、可追溯的 Driver-accepted evidence；
5. immutable 历史不被重写。

## Success, kill, and return criteria

SUCCESS 仅在以下条件全部满足时成立：

1. 新 return 明确 `MATHEMATICAL_DELTA = NONE`；
2. 现有 exact checker 可复现冻结数学；
3. 新 result 的所有 output rows 都含 Git blob 与 SHA-256；
4. 新 result 通过本地结果完整性审计；
5. 没有新增或删除任何数学主张。

Kill / revision conditions：

- 任一冻结 theorem、normal form、homology formula、holonomy boundary 或 support-safety rule 被改变；
- 为修复记录而删除失败样本或放宽 checker；
- 新 manifest 再次缺少 digest；
- checker 与冻结 return 发生实质冲突。

若出现上述任一项，必须返回 `REQUEST_REVISION` 语义，而不是把控制修复冒充为数学成功。
