<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-Q30-N14-EVIDENCE-RECOVERY-CANONICALIZATION-GATE",
  "title": "P000 Q30 n=14 证据恢复与结果规范化门禁",
  "kind": "RESEARCH",
  "owner": "research/p000-q30-n14-evidence-recovery-canonicalization-gate",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "The original Q30 n=14 task is HANDOFF_READY on current main but has no canonical result record. An immutable old research head b90378c332e0dbf80aad0c09d363047abb2ee2f3 contains an exact kernel/orbit certificate claiming 56,972 representatives, 56,972 exact stable packets, 0 collision fibers and total normalized connected count 26,406,647,416,800. That evidence must be replayed/reconciled into the current result protocol before any n=15 continuation can rely on it.",
  "next_action": "Pin b90378c332e0dbf80aad0c09d363047abb2ee2f3; consume the recovery handoff and old certificate without restarting the census. Replay the persisted sector evidence for r=2,4,6,8,10,12 and the dedicated r=14 reconstruction checker; reconcile the certificate's stale r=14 monolithic shard citation with the later reconstruction shards/supplement; then return either a reproducible exact recovery result or the first exact mismatch/provenance gap.",
  "dependencies": [],
  "source_refs": [
    "research_notes/P000_Q30_N14_EVIDENCE_RECOVERY_HANDOFF_20260909.md",
    "research_task_records/RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N14-COLLISION-FRONTIER/TP2-8969646E7FF5FB8A9F5D.json",
    "git:awdawmip/enterprise-math@b90378c332e0dbf80aad0c09d363047abb2ee2f3:research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER/P000_Q30_RETURN_PROFILE_1WL_N14_EXACT_KERNEL_ORBIT_CERTIFICATE_V2.json",
    "git:awdawmip/enterprise-math@b90378c332e0dbf80aad0c09d363047abb2ee2f3:research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER/P000_Q30_N14_R14_RECONSTRUCTION_REPLAY_SUPPLEMENT_V1.json",
    "git:awdawmip/enterprise-math@b90378c332e0dbf80aad0c09d363047abb2ee2f3:research_checks/P000_Q30_N14_R14_RECONSTRUCTION_REPLAY_CHECK_20260905.py",
    "git:awdawmip/enterprise-math@b90378c332e0dbf80aad0c09d363047abb2ee2f3:research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER/P000_Q30_N14_ORBIT_COVER_CHECKPOINT_V1.json"
  ],
  "evidence_status": "Q30_N14_OLD_BRANCH_EXACT_EVIDENCE_PRESENT_RESULT_RECORD_MISSING_RECOVERY_REQUIRED",
  "last_progress_ref": "git:awdawmip/enterprise-math@b90378c332e0dbf80aad0c09d363047abb2ee2f3:research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER/P000_Q30_RETURN_PROFILE_1WL_N14_EXACT_KERNEL_ORBIT_CERTIFICATE_V2.json",
  "last_progress_at": "2026-09-05T05:42:32+00:00",
  "hard_block": "Q30_N14_RESULT_RECORD_ABSENT_AND_R14_LEGACY_SHARD_PIN_SUPERSEDED",
  "tags": [
    "P000",
    "Q30",
    "n14",
    "return-profile",
    "1-WL",
    "replay",
    "evidence-recovery",
    "provenance",
    "result-gate",
    "BRC"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-Q30-N14-EVIDENCE-RECOVERY-CANONICALIZATION-GATE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000Q30REC",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 Q30 n=14 证据恢复与结果规范化门禁

Status: `READY / P0 / HIGH / REPLAY-FIRST / PUBLISHED_REGISTERED`

## 0. Mother question

现有不可变旧研究证据是否足以在当前严格语义下重放并确认 Q30 的有限结论：固定 primitive-return-profile 初始化的 ordinary 1-WL 在 `U_BR(14)` 上没有非同构 equal-packet collision，从而把已接受的有限无碰撞前缀推进到 `n<=14`；若不能，最先失败的是数学重放、穷尽性还是证据链完整性中的哪一环？

## 1. Frozen inputs and scope

只恢复 Q30 已经冻结的对象类与观察器，不改变 Q22/Q25/Q27/Q28/Q29/Q30 的 primitive-return-profile 初始颜色、ordinary 1-WL 邻居多重集递推和匿名稳定 packet。旧证据源固定为 commit `b90378c332e0dbf80aad0c09d363047abb2ee2f3`，并以本任务 `source_refs` 中的 exact paths 为入口。

旧 V2 证书声称按 `r=2,4,6,8,10,12,14` 的 cubic-kernel sectors 穷尽 `n=14`，总计 `56,972` 个代表、`56,972` 个 exact stable packets、`0` collision fibers、normalized connected total `26,406,647,416,800`。这些数值是待重放的断言，不因写入本任务而获得接受地位。

必须保留原始 packet 的精确结构与来源分支。digest 只可用于文件完整性，不能替代 packet 判等；kernel/orbit 坐标只证明搜索覆盖，不得被当成更强 observable。不得加入 2-WL、谱、zeta、完整 cycle incidence 或 canonical labeling 来修复 Q30。

证据链有一个已知缺口需要显式处理：证书仍引用 `P000_Q30_N14_KERNELS_R14_V1.json`，而旧分支最终头上该文件已被后续 r=14 reconstruction shards、replay supplement 与 direct reconstruction checker 取代。恢复结论必须证明这些后续证据确实覆盖并 supersede 旧引用，而不是忽略该差异。

## 2. Hard target and required outputs

Hard target: `Q30_N14_EXACT_EVIDENCE_RECOVERED_OR_FIRST_FAILURE_CLASSIFIED`.

需要交付一个不可变 recovery evidence ledger；对 `r=2,4,6,8,10,12` compact evidence 与 `r=14` 509-object reconstruction 的可复核重放；sector 与全局 totals、exact packet equality、collision 与 coverage 一致性检查；以及当前协议下的 execution/result/return，使后续路线可引用本恢复任务的结果而不依赖聊天记录。若任一步失败，返回最小确定性 mismatch 或 provenance gap，不得用摘要或总数补齐缺口。

## 3. Research value to preserve

这项工作不是重复枚举，而是防止已经完成的大规模精确研究因旧分支未形成当前 result record 而丢失。若重放通过，可把 Q30 的 56,972-class / zero-collision 证据变成后续研究可安全引用的显式门禁结果；若重放失败，则能把失败收缩到一个精确 sector、对象或 provenance edge，避免 n=15 建在未经接受的前提上。它同时保留 BRC 所要求的结构与来源不被摘要吞掉的信息边界。

## 4. Success, kill, and return criteria

成功终态是 `Q30_N14_EXACT_EVIDENCE_RECOVERED_AND_REPLAY_VALIDATED`：所有必要 sector coverage 与 exact packet checks 均可从固定旧证据重放，r=14 supersession 关系得到明确证明，并形成当前可引用的 result/return。

失败终态是 `Q30_N14_RECOVERY_MISMATCH_OR_PROVENANCE_GAP_CLASSIFIED`：一旦发现计数、packet、automorphism/orbit coverage、r=14 reconstruction 或文件来源无法闭合，立即冻结第一个可复现失败点并返回，不得继续用推测修补。

本任务只处理 `n=14` 证据恢复，不研究 `n=15`。只有本恢复结果经过后续正常审查后，才由父目标重新判断是否值得开放新的最小前沿。
