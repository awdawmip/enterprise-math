<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RH-ROAD-TAIL-20260909",
  "title": "Composite-road scale-adapted escaping-tail estimate",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Finite road identities and spectral interfaces do not yet yield a uniform bound on sum_(N>=M(a)) B_(a,N)^2/N^2 as a decreases to zero.",
  "next_action": "Consume predecessor returns, choose a declared M(a) and a dyadic or logarithmic shell decomposition, and prove the first bound with explicit dependence on a and shell scale.",
  "dependencies": [
    "RH-ROAD-AUDIT-20260909",
    "RH-ROAD-KERNEL-20260909"
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
  "registry_key": "RH-ROAD-TAIL-20260909",
  "parent_objective_id": "OBJ-RH-COMPOSITE-ROAD-20260905",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RH-ROAD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RH-ROAD-KERNEL-20260909",
  "successor_gate": {
    "new_information_gap": "The full-road energy has no unconditional scale-adapted O(a) control as thickness goes to zero and horizon escapes to infinity.",
    "why_parent_result_does_not_close_it": "An exact anchored kernel or finite safe interface does not bound the arithmetic coefficient-weighted infinite tail uniformly in a.",
    "discriminating_outcomes": [
      "Uniform unconditional full-road energy bound",
      "New quantitative partial tail bound with all parameter dependence",
      "Counterexample to a specified sufficient estimate with preserved alternative"
    ],
    "kill_condition": "Reject any bound using RH-equivalent exclusion, losing phase or interchanging the limits without proof; do not reject the research population.",
    "alternative_route_or_free_exploration_considered": "Compare direct Green-energy shells and anchored Ramanujan kernels; the prior Nyman Schur-gain condition remains an unproved alternative.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Uniform arithmetic tail control is a different theorem obligation from audit or kernel algebra and needs its own falsifiable scope."
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

# 合数道路 RH：尺度适配的逃逸尾估计

## 0. Mother question

令 R_a(n)=prod_(p|n)(1-p^-a)，c_a=1/zeta(1+a)，S_a(N)=sum_(n<=N)R_a(n)，B_(a,N)=S_a(N)-1-c_a(N+1/2)。能否不借 RH 或等价零点排除估计，控制 D_a=sum_(N>=1)B_(a,N)^2/N^2，尤其 N>=M(a)->infinity 的尾部？

## 1. Frozen inputs and scope

先读 research_handoffs/COMPOSITE_ROAD_RH_20260909/START_HERE.md 及 source_manifest.json。研究原件钉在 EM 9d7c4c6eafc5479a6795a128fc0288fc893bed3c，完整旧证明与程序按入口恢复。父任务为 RH-ROAD-KERNEL-20260909，运行依赖它和 RH-ROAD-AUDIT-20260909；预发布不代表前置已完成。只消费有效的带范围返回，目标与 RH 的联系取决于审计的经典桥。
保留全整数道路、联合合数观察量、符号及固定起点相位；当前最高保留合同和 P000 不变。历史用户选题来源及 ANCHOR_EXPOSED 状态不变；没有原始公理被提升。通用执行与持久化规则继承项目。

## 2. Hard target and required outputs

输出 research_notes/RH_ROAD_TAIL_20260909/RETURN.md、bound_ledger.json、必要精确或区间检查，以及可接手的单一最小缺口。
声明 M(a)、a 范围、壳区间、常数与允许交换的求和/极限，分别控制前缀和尾部。完整目标是充分小 a 时 D_a<=C*a 的无条件统一界；可以先完成严格非平凡的子范围估计，或给所选充分条件的精确障碍。
允许固定起点谱核或直接有限 Green 核 1/max(m,n)-1/N。任何跨频率、合数联合项删除都须有适合观察量与尺度的证书，平移平均功率有限不替代固定起点尾界。
旧 Nyman 二倍尺度增益 h_N* S_N^-1 h_N >= eta*d_N^2/log N 仍只是未证充分目标，不宣称必要；否定它不等于否定 RH。有限拟合小不证明无限尾部小，数值发现与误差证书分开。

## 3. Research value to preserve

有明确 a、M 和频率依赖的新界，或准确说明常数为何失控的机制，都能缩小真正缺口。无论结果如何，完整背景、符号和相位保持可恢复。

## 4. Success, kill, and return criteria

有效返回至少包含新定量已证估计、严格反例/障碍，或全部依赖明确且唯一未证引理隔离的条件定理。仅改名、重述等价式、扩大有限实验或列愿望不算完成。
若循环使用 RH、把 fixed-horizon O_M(a^2) 当成全局 O(a)，或用平均化消去难项，撤回该推论并保留原对象。常数不受控不得隐藏在 O 符号中。完整 O(a) 未闭合时明确 RH 未证，并交接剩余估计。
