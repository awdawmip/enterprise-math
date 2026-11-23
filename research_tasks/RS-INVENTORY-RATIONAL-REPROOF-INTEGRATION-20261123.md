<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-INVENTORY-RATIONAL-REPROOF-INTEGRATION-20261123",
  "title": "因数库存有理化重证：全范围定理与有限误差集成",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "两轮 C78／C87 作者证明与准确有限证书已保存；正比例差有理充分性、有限识别预算、原库存有效桥和高精度有效尾尚待完成及接合。",
  "next_action": "在四个研究单元产出所需证据后，形成同一观察量与参数域下的组合定理及有限误差预算；保留无法接合的具体缺口。",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "source_refs": [
    "c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/REPORT.md",
    "c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/NEAR_STOCK_SHARP_REPROOF.md",
    "46eec634a39fd202babd05e66b251d90945be948:research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/REPORT.md"
  ],
  "dependencies": [
    "RS-C77-RATIONAL-POSITIVE-RATIO-20261123",
    "RS-C78-EFFECTIVE-RATIONAL-IDENTIFICATION-20261123",
    "RS-C87-EFFECTIVE-NATIVE-HAAR-BRIDGE-20261123",
    "RS-C87-EFFECTIVE-HIGH-PRECISION-ORDER-20261123"
  ],
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "evidence_status": "SOURCE_BOUND_AUTHOR_PROOFS_OPEN_FOLLOWUP",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "FACTOR_INVENTORY",
    "RATIONAL_REPROOF",
    "C78_C87_FOLLOWUP"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-INVENTORY-RATIONAL-REPROOF-INTEGRATION-20261123",
  "parent_objective_id": "OBJ-INVENTORY-RATIONALIZATION-20261123",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "INVENTORY-RATIONAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "taskset_id": "TS-C78-C87-RATIONAL-FOLLOWUPS-20261123",
  "priority_basis": "按原全库存有理化的当前缺口和可独立推进价值分档；沿用现有调度基础权重。",
  "priority_weight_reference": "research_runtime_policy_v2.json#/selection_policy/priority_weights"
}
-->

# 因数库存有理化重证：全范围定理与有限误差的集成

## CURRENT_STATE

本任务于 2026-11-23（Asia/Hong_Kong）首次正式建项，承接用户的因数库存全面有理化研究及本轮“发布后续任务到状态机和中控台”指令。现有基础是两轮已保存的作者侧 C78／C87 证明和准确计算。它们此前以 direct research 形式保存，本任务记录当前的集成工作，不回填历史 Task、CLAIM 或 Result。

母问题是：保持原观察量、全部安排、三条完整尾、原生 X6 类型及联合竞争关系，怎样把已完成基线与新有效化成果接成量词明确、有限输入可核验的整体结论？

## COMPLETED_WORK

已保存 C78 的准确有理归一化、固定阶差分、节点准确 C2 桥、具体正则性多项式、代数方向与小值工具，以及近库存锐阈值。必要性和低精度方向覆盖全部 1<=b<=c。C87 已有原有限库存的全原点证书、最低精度、有限反转和相位平均稳定性。原作者证明与准确计算按其原范围复用，尚未独立 Review。

## REMAINING_WORK

本任务的独立产出是跨单元的组合证明与接口闭合，不重复四项子任务的单独定理。

- 将 C77 正比例差有理充分性与既有近库存证明、全范围必要方向接成全部 1<=b<=c 的锐阈值，写清序列与舍入原点量词、仍用的分析输入。
- 接入 C78 的有限识别界，统一原观察量、Gamma 归一化、精度和定量参数域；有意义的有限 c0 必须携带其输入域或收敛模。
- 接合 C87 原库存有效桥与高精度尾，针对固定位置对或带分离余量的位置族，检验共享有限参数域与 L 的准确尺度转换。
- 对有限排序使用同一预算：已认证主项差 Delta_main 必须大于两方案的尾余项 R1+R2 及库存误差 E1+E2。给出可验证的非空适用域，或准确列明无法拼接的数学障碍和缺失条件。
- 交付组合定理、参数/归一化/误差兼容表、所用子结果的固定证据引用和可复算的有限接受条件。仅有未闭合预算时保留具体缺口；不把四项文稿存在等同于整体目标完成。

## EVIDENCE_AND_ARTIFACT_LOCATIONS

科学基线：

- c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/REPORT.md
- c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/NEAR_STOCK_SHARP_REPROOF.md
- 46eec634a39fd202babd05e66b251d90945be948:research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/REPORT.md

四项正式研究单元由本任务 dependencies 与本任务集 TASKSET.json 列出；接手者读取各项实际的 durable frontier 和证据状态，不需要前一会话的隐藏上下文。

## TAKEOVER_CONDITIONS

四子任务可各自开始，均无彼此硬依赖；本集成任务等待四项所需成果。C87 的有效尾与有效桥可并行，只有实际有限库存排序需要合并它们。完成时核对真正的量词、共同输入域、常数和误差，不要求重做既有基线或选择指定研究方法。子项若给出有效反例或修正版，集成结果应准确保留其范围与仍未闭合的母问题。共享任务运行按原生领取机制进行。
