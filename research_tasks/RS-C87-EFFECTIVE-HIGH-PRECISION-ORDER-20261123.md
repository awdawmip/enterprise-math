<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-C87-EFFECTIVE-HIGH-PRECISION-ORDER-20261123",
  "title": "C87 高精度位置排序的有效余项与起效倍率",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "完整位置主常数的严格排序及有理差区间已保存；高倍率尾仍为 o(L^(-1/10))，没有明确起效 L0 或任意联动库存与倍率的统一误差。",
  "next_action": "以已严格定号的位置主系数差为输入，研究高倍率尾的明确误差并求可核验的排序起效倍率；保留固定位置或分离余量的量词。",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-INVENTORY-RATIONAL-REPROOF-INTEGRATION-20261123",
  "successor_gate": {
    "new_information_gap": "高精度尾余项只有渐近小量，缺固定位置对或分离位置族的明确起效倍率。",
    "why_parent_result_does_not_close_it": "母任务于本批首次正式建立，继承的是已固定的作者侧重证基线和未完前沿；当前没有覆盖本项缺口的母任务结果。",
    "discriminating_outcomes": [
      "证明具体尾界并认证 L0",
      "证明所要求统一位置族需额外分离条件并给出修正版"
    ],
    "kill_condition": "若统一位置量词被准确反例否定，停止该量词并保留必要条件；尚未算出 L0 保持开放。",
    "alternative_route_or_free_exploration_considered": "可以先给固定位置对的有效尾界，也可研究带分离余量的位置族；无需等待原库存有效桥完成。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "本项有独立的科学验收对象，可与其他单元并行；母任务保留跨单元归一化、输入域和误差预算的最终拼接责任。"
  },
  "source_refs": [
    "c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/REPORT.md",
    "c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/FINITE_PHASE_STABILITY.md",
    "46eec634a39fd202babd05e66b251d90945be948:research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/C87_POSITION_PROOF.md",
    "46eec634a39fd202babd05e66b251d90945be948:research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/REPORT.md"
  ],
  "dependencies": [],
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
  "registry_key": "RS-C87-EFFECTIVE-HIGH-PRECISION-ORDER-20261123",
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

# C87 高精度位置排序的有效余项与起效倍率

## CURRENT_STATE

目标为原极限曲线
\[
1-\Phi_\theta(L)\sim W I_\theta L^{-1/10}
\]
给出明确余项，并为固定位置对或有分离余量的位置族认证起效倍率 \(L_0\)。主要比较可沿已有四分点与中点证书。任意趋近的位置不能未经证明共用同一个 \(L_0\)。

## COMPLETED_WORK

已保存 \(I_{1/4}-I_{1/2}\) 的严格有理负区间、C87 全位置排序与定量严格凹性、有限正部面积证明、61段有理代理及误差。原高精度尾层给同一正数 \(W\) 的主项。已有有限反转明确区分主常数排序、极限曲线、相位平均与逐原点结论。

## REMAINING_WORK

原来源明确没有给出 \(L_0\)，主项符号尚不能判定任意指定倍率。

验收目标：

- 给出可核验的系数界与具体 \(R_\theta(L)\)，使
  \[
  |(1-\Phi_\theta(L))-W I_\theta L^{-1/10}|\le R_\theta(L)
  \]
  在声明域成立。
- 对目标位置对给明确 \(L_0\)，验证 \(L\ge L_0\) 时两方案余项总和小于已认证的主项差，从而严格排序。
- 若扩展到位置族，写清端点或主系数分离条件；若允许 \(L=L_c\to\infty\) 与库存联动，补足相应统一误差。
- 已有 \(I_\theta\) 差和核网格直接作为来源；只针对实际不足的余量或参数范围改进。
- 准确反例或必要分离条件可支持有范围的修正目标；尚未求出 \(L_0\) 只记进展。

## EVIDENCE_AND_ARTIFACT_LOCATIONS

以下为 enterprise-math 中的固定提交及精确路径。已完成研究按已保存作者侧证明与准确计算证据复用，尚未独立 Review；本任务不把来源保存或内部核对等同于正式接纳。

- c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/REPORT.md
- c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/FINITE_PHASE_STABILITY.md
- 46eec634a39fd202babd05e66b251d90945be948:research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/C87_POSITION_PROOF.md
- 46eec634a39fd202babd05e66b251d90945be948:research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/REPORT.md

## TAKEOVER_CONDITIONS

极限曲线的有效尾和 \(L_0\) 可与原库存到 Haar 的有效桥并行，不应将本任务整体设为等待有效桥完成。只有回到给定有限 \(c,B,p\) 的原库存排序时，才额外扣除有效桥中两方案的误差。原 C85/C86 来源按已保存报告和位置证明追踪；保持作者侧来源状态，方法开放，不将普通研究强制为独立审查或形式化工具流程。

## 正式谱系

本任务是本批首次建立的母任务 `RS-INVENTORY-RATIONAL-REPROOF-INTEGRATION-20261123` 的研究单元。母任务与四项子任务在同一原子提交中首次发布；既有 C78／C87 证据来自固定的 direct research 报告，不回填历史 Task、CLAIM 或 Result。
