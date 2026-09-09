<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RH-ROAD-KERNEL-20260909",
  "title": "Composite-road anchored spectral kernel and phase-safe tail interface",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The current spectrum retains modal powers, but RH-sensitive anchored off-diagonal rational-frequency coherence has not been bounded.",
  "next_action": "After consuming the audit return, derive the finite-horizon double-frequency kernel and construct a same-power phase witness before any diagonal or tail quotient.",
  "dependencies": [
    "RH-ROAD-AUDIT-20260909"
  ],
  "source_refs": [
    "research_handoffs/COMPOSITE_ROAD_RH_20260909/START_HERE.md",
    "research_handoffs/COMPOSITE_ROAD_RH_20260909/source_manifest.json",
    "research_handoffs/COMPOSITE_ROAD_RH_20260909/stage2_verify.py",
    "research_notes/COMPOSITE_ROAD_RH_BOUNDARY_LAYER_20260906.md",
    "research_notes/COMPOSITE_ROAD_RH_BOUNDARY_SLOPE_CLOSURE_20260906.md",
    "research_notes/COMPOSITE_ROAD_RH_COMPLETED_SCHUR_PICK_20260906.md",
    "research_notes/COMPOSITE_ROAD_RH_DISCRETE_L2_NONCOMMUTATION_20260906.md",
    "research_notes/COMPOSITE_ROAD_RH_FUTURE_PORT_POSITIVE_DEFORMATION_20260906.md",
    "research_notes/COMPOSITE_ROAD_RH_PENETRATION_JET_HIERARCHY_20260906.md",
    "research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md",
    "research_notes/COMPOSITE_ROAD_RH_RAMANUJAN_PHASE_COHERENCE_20260906.md"
  ],
  "evidence_status": "RESEARCH_DERIVATIONS_PENDING_INDEPENDENT_AUDIT_WITH_REPRODUCED_FINITE_CERTIFICATES",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "RH",
    "composite-road",
    "full-integer-population",
    "signed-phase",
    "source-handoff"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RH-ROAD-KERNEL-20260909",
  "parent_objective_id": "OBJ-RH-COMPOSITE-ROAD-20260905",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RH-ROAD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RH-ROAD-AUDIT-20260909",
  "successor_gate": {
    "new_information_gap": "Translation-averaged power loses off-diagonal phase; the anchored double-frequency kernel lacks uniform near-resonance and tail-port bounds.",
    "why_parent_result_does_not_close_it": "A proof-chain audit can validate or correct inputs but supplies neither the new anchored kernel estimates nor a certified phase-preserving compression.",
    "discriminating_outcomes": [
      "Closed kernel formula with uniform resonance/cutoff bounds",
      "Explicit same-power different-anchored-energy witness",
      "Quantified obstruction to a specified proposed tail compression"
    ],
    "kill_condition": "Reject the specific compression if it removes nonzero anchored coupling or its uniform constant diverges; retain the full field and report the witness.",
    "alternative_route_or_free_exploration_considered": "The direct finite Green-energy route remains available; compare it to rational frequencies without forcing a positive-recurrent interpretation.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is a distinct analytic interface after source auditing, with separate outputs and no need to repeat historical finite certificates."
  },
  "origin_research_provenance": "EM-FREE-C4A91D; user-selected classical arithmetic research; ANCHOR_EXPOSED; no raw axiom candidate promoted",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "review_state": "PASS",
    "temporary_overrides": [],
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a"
  }
}
-->

# 合数道路 RH：固定起点谱核与保相位尾接口

## 0. Mother question

对 h_N(theta)=sum_(n=1)^N exp(i*n*theta)，如何把 K(theta,phi)=sum_(N>=1)h_N(theta)conjugate(h_N(phi))/N^2 做成保留固定起点跨频率相位、可证明截断误差的接口？

## 1. Frozen inputs and scope

共同入口为 research_handoffs/COMPOSITE_ROAD_RH_20260909/START_HERE.md 和 source_manifest.json；冻结 EM 源 9d7c4c6eafc5479a6795a128fc0288fc893bed3c，旧证明及全部证书按入口恢复。正式父任务 RH-ROAD-AUDIT-20260909；执行前消费其带作用域清单。这是预发布的条件后续，不断言父任务已完成，不把作者标签或待审的道路斜率当作前提。
频率来自 2*pi*r/q 的既约有理频率。完整道路 n 人口不得被谱系数支撑条件替代。保留合数道路、符号相位及当前最高联合关系规则；历史用户选题来源与 ANCHOR_EXPOSED 状态保持，未引入新的公理。通用角色和持久化规则继承项目合同。

## 2. Hard target and required outputs

输出 research_notes/RH_ROAD_KERNEL_20260909/RETURN.md、kernel_contract.json 和独立可重复的截断/相位见证检查。
推导 K 的闭式或同等精确表达，证明非零频率收敛、Hermitian 性及对角项。给 theta->0、phi->0、theta-phi->0 和分母增长的一致估计。截断误差须带明确参数依赖，不把固定频率常数称为全 q 一致。
构造至少一对有限系数族，逐模功率完全相同而固定起点二次能量不同，独立说明功率不能恢复相位观察。分离低频、近共振和远尾，给保留未来端口耦合的 Schur/Feshbach 或等价接口；每次压缩记录保留及擦除信息。
按当前工具策略核查并复用 T6/T8 或已有谱尾接口，源查询不是执行，有限正权工具不能充当无限复相位抵消引理。足够的已有接口只复用或扩展，不新建同义工具。

## 3. Research value to preserve

近共振常数、固定起点相位见证和尾耦合接口独立于 RH 成败可复用，把道路背景不可轻删转成可检验的观察者条件。

## 4. Success, kill, and return criteria

成功须超过形式级数：至少带范围的核表达、严格相位见证及一个定量截断或尾耦合结果。若商丢失观察量，返回反例和修复坐标，不能反称原方向冗余。禁止平移平均后直接等同固定起点范数，禁止有限 PSD 或固定 q 界升级到无限尺度统一界。常数失控须改变划分或报告准确障碍；交接最小未完成单位，不宣称 RH 已证。
