<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-C77-RATIONAL-POSITIVE-RATIO-20261123",
  "title": "C77 正比例库存差的有理重证",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "已完成近库存 b=o(c) 的锐充分性、全部 1<=b<=c 的必要尺度和低精度结论；正比例差充分性的其余连接仍引用原 C77。",
  "next_action": "围绕 b/c 趋正极限的原双读数对应，补齐有限有理输入到全库存碰撞计数的证明，并与已保存近库存结论接合。",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-INVENTORY-RATIONAL-REPROOF-INTEGRATION-20261123",
  "successor_gate": {
    "new_information_gap": "正比例库存差的有理充分性尚未与近库存锐阈值组成完整新证明。",
    "why_parent_result_does_not_close_it": "母任务于本批首次正式建立，继承的是已固定的作者侧重证基线和未完前沿；当前没有覆盖本项缺口的母任务结果。",
    "discriminating_outcomes": [
      "正比例差全称充分性和全范围拼接成立",
      "准确反例或必要条件支持有范围的修正定理"
    ],
    "kill_condition": "若准确证据否定原量词，停止宣称该量词并保存反例、必要条件与可支持的修正版；未完成推导保持开放。",
    "alternative_route_or_free_exploration_considered": "可保留原 C77 为输入先推进其他任务；本项专门补齐其有理有限证据链，方法由研究者选择。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "本项有独立的科学验收对象，可与其他单元并行；母任务保留跨单元归一化、输入域和误差预算的最终拼接责任。"
  },
  "source_refs": [
    "c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/NEAR_STOCK_SHARP_REPROOF.md",
    "c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/RATIONAL_NORMALIZATION_AND_DISCRETE_JETS.md",
    "c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/RATIONAL_HERMITE_C2_BRIDGE.md",
    "c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/REAL_PARAMETER_AFFINE_RIGIDITY.md",
    "46eec634a39fd202babd05e66b251d90945be948:research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/FINITE_KERNEL_PROOF.md",
    "46eec634a39fd202babd05e66b251d90945be948:research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/FINITE_PRODUCT_BOUND.md"
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
  "registry_key": "RS-C77-RATIONAL-POSITIVE-RATIO-20261123",
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

# C77 正比例库存差的有理重证

## CURRENT_STATE

保持原三态因子路径、三条完整尾、原 \(H(0,1)\) 和全部 \(\binom c2\) 个安排。对库存 \(c,c+b\) 的两次读数，每轴全局舍入原点任意且可随库存改变，精度量为
\[
\Xi_c=2^{4p_c}b_c^2/c^9.
\]
目标是正比例差 \(b/c\to z_*>0\) 的充分性有理重证，再接回全范围锐阈值。

## COMPLETED_WORK

已保存：\(b=o(c)\) 时 \(\Xi_c\to\infty\) 推出唯一率趋一；全部 \(1\le b\le c\) 的必要性、有界 \(\Xi_c\) 歧义缺口及 \(\Xi_c\to0\) 结论。准确归一化 \(\Gamma_c=5(g-1)/(27F_1(c))\)、固定阶联合差分、节点准确的 Hermite \(C^2\) 桥，以及固定正实参数仿射刚性均可复用。

## REMAINING_WORK

补齐正比例差对应、正则性、跨分支及全库存覆盖的实际连接；近库存 Euler 差商不能直接替代两个固定比例库存的读数对应。

验收目标：

- 对任意 \(b/c\to z_*>0\)、\(\Xi_c\to\infty\) 的合法序列，证明原全库存唯一率趋一，统一于两个全局原点；等价的正比例差紧区间命题也可采用。
- 处理实际有理库存比、极限参数、同步与符号分支，给足有限读数到所用辅助对象的误差。
- 与已完成近库存及必要方向拼接，写清全部 \(1\le b\le c\) 的完整量词及依赖。
- 可核验的书面证明与必要有限证书承担全称结论；准确反例或必要条件证明可支持有明确范围的修正结论。未完成推导记作进展。

## EVIDENCE_AND_ARTIFACT_LOCATIONS

以下为 enterprise-math 中的固定提交及精确路径。已完成研究按已保存作者侧证明与准确计算证据复用，尚未独立 Review；本任务不把来源保存或内部核对等同于正式接纳。

- c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/NEAR_STOCK_SHARP_REPROOF.md
- c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/RATIONAL_NORMALIZATION_AND_DISCRETE_JETS.md
- c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/RATIONAL_HERMITE_C2_BRIDGE.md
- c9d661935fc64e300c0a0d5dd7fb42de213e6401:research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/REAL_PARAMETER_AFFINE_RIGIDITY.md
- 46eec634a39fd202babd05e66b251d90945be948:research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/FINITE_KERNEL_PROOF.md
- 46eec634a39fd202babd05e66b251d90945be948:research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/FINITE_PRODUCT_BOUND.md

## TAKEOVER_CONDITIONS

从所列固定来源接续，不重做已完成近库存证明；原 C77 来源从 NEAR_STOCK_SHARP_REPROOF.md 的来源节追到实际文本。方法开放，保留所用实分析辅助工具的真实范围；固定实参数常数域不冒称为可计算的纯有理输入。本项可独立启动，不依赖其他新任务完成。辅助坐标保持其类型，原生 X6、完整尾和联合竞争关系沿用。

## 正式谱系

本任务是本批首次建立的母任务 `RS-INVENTORY-RATIONAL-REPROOF-INTEGRATION-20261123` 的研究单元。母任务与四项子任务在同一原子提交中首次发布；既有 C78／C87 证据来自固定的 direct research 报告，不回填历史 Task、CLAIM 或 Result。
