<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-X6-TRIAD-PARTIAL-SOURCE-IDENTIFICATION",
  "title": "三槽细分中部分来源可见时的分支权重辨识",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已有单一标记子边的五类中点读数反演。尚需在来源被合并、或后代只保留相关副本时判定可辨参数。",
  "next_action": "在固定二层路径树上明确一个来源合并方案，列出观测分箱在四条根支与标记强度上的精确读数。",
  "parent_objective_id": "PO-X6-UPPER-STRUCTURE-20260906",
  "created_by_role": "RESEARCHER",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-X6-TRIADIC-CLOSURE-DYNAMICS",
  "successor_gate": {
    "new_information_gap": "部分来源可见时怎样完整刻画可辨参数及恢复的最小额外信息？",
    "why_parent_result_does_not_close_it": "已有五箱和三箱反演固定中点保留方式；它们没有分类匿名化或共享根重采样协议。",
    "discriminating_outcomes": "给出可逆观测、等价参数族及最少补读，或同末框的可验证冲突对。",
    "kill_condition": "若补读或同根复制无法由原生操作实现，可给对照模型定理及原生映射的具体缺项。",
    "alternative_route_or_free_exploration_considered": "读取整个根中点可直接分权，但不回答来源缺失时的识别能力。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "这一统计识别问题由有限来源树给定，可与原生门控证据和纯闭路分类并行。"
  },
  "identity_lane": "X6U",
  "dependencies": [
    {
      "target": "Heartbeat X6 typed-path research at 7b6ea72b90918af5363b319ef16e25122a123ad9",
      "action": "CONSUME",
      "satisfied": true
    }
  ],
  "source_refs": [
    "awdawmip/enterprise-math@fa76228ee339e27b64f595f4ad645e515974d919:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md",
    "awdawmip/enterprise-math@fa76228ee339e27b64f595f4ad645e515974d919:p000_reality_foundation.json",
    "awdawmip/enterprise-math@fa76228ee339e27b64f595f4ad645e515974d919:research_constraints/heartbeat_brc_only.json",
    "awdawmip/enterprise-math@ab4699ad2a80b0e040c5a5f287cd34a537d75e6f:research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md",
    "awdawmip/enterprise-math@7b6ea72b90918af5363b319ef16e25122a123ad9:research_notes/portable_direct/20261116_heartbeat_triad_refinement/GATED_REFINEMENT.md",
    "awdawmip/enterprise-math@7b6ea72b90918af5363b319ef16e25122a123ad9:research_notes/portable_direct/20261116_heartbeat_triad_refinement/POLICY_OBSERVATIONS.md",
    "awdawmip/enterprise-math@7b6ea72b90918af5363b319ef16e25122a123ad9:research_notes/portable_direct/20261116_heartbeat_triad_refinement/check_source_readout.py"
  ],
  "evidence_status": "CONDITIONAL_AUTHOR_RESULTS_AND_OPEN_FOLLOWUP",
  "claim_lease_minutes": 120,
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-X6-TRIAD-PARTIAL-SOURCE-IDENTIFICATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL"
}
-->

# 三槽细分中部分来源可见时的分支权重辨识

## 研究问题

固定粗边 012→013、根中点 014/015/023/123 以及旧证明中只在 012→014 子边实施的未知强度标记。研究两种有实际差别的读取方式：只见一部分子中点类别（包括 4、5 互换后被合并的情形），以及只看末框但在确实可定义的模型中保留同一根来源产生的后代相关性。已证的五类单树反演及 r4=0 的边界可直接引用。

## 可交付结果

对至少一个含来源合并的非平凡协议族，给出“两个参数产生相同全部可读记录”的充要条件，并明确分辨的是四支权、乘积 r4·t 或标记强度 t。对可逆状态给出反演及适用域；对不可逆状态给两组可复算的同读数参数，并求一种足够的最小额外来源类别或独立联合统计量，说明最小性所针对的协议。若采用双副本，分别建模同一根条件下独立分出的后代、与重新抽根的两次实验，对比二阶观测，覆盖零权、零标记等退化。引入可复制或可标记的假设时，保留其比较模型身份与原生许可证据。复算须使用有序来源分支，保持具名槽与可组合的中间状态；引用既有 64 条路径与反演基线，避免把既有五箱结果再作为待证结论。
