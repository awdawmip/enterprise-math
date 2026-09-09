<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RH-ROAD-AUDIT-20260909",
  "title": "Composite-road RH proof-chain and correction audit",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The Sep 6 positive-road, raw/completed comparison, boundary-slope and phase claims exist as researcher derivations but lack one independent source-and-proof audit.",
  "next_action": "Read research_handoffs/COMPOSITE_ROAD_RH_20260909/START_HERE.md and source_manifest.json; classify each claim by assumptions and independently check the raw/completed comparison before consuming any RH-equivalence rate.",
  "dependencies": [],
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
  "registry_key": "RH-ROAD-AUDIT-20260909",
  "parent_objective_id": "OBJ-RH-COMPOSITE-ROAD-20260905",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RH-ROAD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "origin_research_provenance": "EM-FREE-C4A91D; user-selected classical arithmetic research; ANCHOR_EXPOSED; no raw axiom candidate promoted",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "review_state": "PASS",
    "temporary_overrides": [],
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a"
  }
}
-->

# 合数道路 RH：证明链独立审计

## 0. Mother question

当前全整数道路研究链中，哪些论断已经有充分证明，哪些依赖 RH、零点单性或未证的交换极限，哪些必须修正？形成无需旧聊天即可消费的证据图。

## 1. Frozen inputs and scope

先读 research_handoffs/COMPOSITE_ROAD_RH_20260909/START_HERE.md 与 source_manifest.json，运行 stage2_verify.py。研究原件冻结在 EM commit 9d7c4c6eafc5479a6795a128fc0288fc893bed3c。Sep 5 完整证明在 GK commit bb649a26fd04db9bee3cf237b7c0d0311f99e7d2 的 journal/enterprise-math/2026-09-05/20260905T073134Z-composite-residue-rh-stage2-c4a91d.md。
本任务为用户明确请求的有源独立复核，不是盲验证。历史来源为 EM-FREE-C4A91D 的用户选题研究，ANCHOR_EXPOSED，没有新的原始公理获得认可。旧作者的 PROVED 标签只作为待审论断。保留完整整数、合数联合方向、符号相位及当前根公理和最高保留合同。通用执行与持久化规则直接继承项目，不在此重设。
范围覆盖 manifest 中全部 COMPOSITE_ROAD_RH_*_20260906.md 笔记和 Sep 5 余数证书。外部母定理须核对一手原文确切假设，尤其 Báez-Duarte math/0202141、Burnol math/0202166 及实际使用的其他文献。

## 2. Hard target and required outputs

输出 research_notes/RH_ROAD_AUDIT_20260909/RETURN.md、claim_audit.json、必要的最小独立检查程序及运行证据。
逐条审计零尾 Nyman 归一化、L_n 提取器与统一下界、R_a 和 Burnol 函数恒等式的收敛区、raw Q_a 与 completed Delta_a 的比较、A(a)=O(a) 范围及 U_road 阈值、边界斜率的重数及求和/极限、离散端点项、Ramanujan 展开与平移平均交换。
特别检查：两个量满足不同充分条件，不足以单独证明观察者不可约。相位丢失须给同功率异相位有限见证，或降为对角化擦除了交叉项、是否足够控制固定起点量尚缺证明。
claim_audit.json 每项含 statement、source_commit/path/blob、assumptions、proof_or_counterexample、status、downstream_action；状态为 VERIFIED_DERIVATION、CLASSICAL_INPUT_VERIFIED、CONDITIONAL、REPAIR_REQUIRED 或 UNRESOLVED。有限回归不是普遍证明。保留原件，以附加纠错修复历史。

## 3. Research value to preserve

输出可信最小依赖链。某个强斜率论断失败时，仍保留有限 Green 恒等式、坐标刚性、严格分离证书及独立谱核定义，明确可继续的后续。发布方已经复核的机械计算不包装为新发现。

## 4. Success, kill, and return criteria

成功要求所有消费节点状态明确，至少独立核验 raw/completed 误差链及全道路离散判据范围。反例、缺失引理或循环论证也是有效结果，但须给最小定位和下游影响。只为明确待审断言扩展证据，不扩展无关文献或重复计算。不能删去引用中的条件假设。未闭合断言记录最小缺口，不宣告整条合数路线无用。任务返回不等于 RH 完成。
