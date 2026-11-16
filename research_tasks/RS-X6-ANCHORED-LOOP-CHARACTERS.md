<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-X6-ANCHORED-LOOP-CHARACTERS",
  "title": "心跳三槽中固定一根具名轴后的闭路相位分类",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "三槽全开时，裸支撑图上的全轴重命名不变标量相位只读置换奇偶。保留一根具名轴后的分类待定。",
  "next_action": "在 J(6,3) 的平坦三角商上，指定一根轴 d 并确定其 S5 稳定子对整系数闭路循环的作用。",
  "parent_objective_id": "PO-X6-UPPER-STRUCTURE-20260906",
  "created_by_role": "RESEARCHER",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-X6-TRIADIC-CLOSURE-DYNAMICS",
  "successor_gate": {
    "new_information_gap": "一根持续可读轴的稳定子允许哪些标量字符？",
    "why_parent_result_does_not_close_it": "已有定理对全部六轴重命名取不变，固定轴会改变不变条件。",
    "discriminating_outcomes": "新增字符可由闭路对区分，或证明只有平凡和奇偶。",
    "kill_condition": "若同一固定轴及同一平坦路径商下已有完整证明，则核对命题、复算并返回引用。",
    "alternative_route_or_free_exploration_considered": "只保留具名末框是另一种观测，无法决定对整路的乘法字符。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "这是一个可独立解出的有限群作用问题，母任务继续处理原生事件许可。"
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
    "awdawmip/enterprise-math@7b6ea72b90918af5363b319ef16e25122a123ad9:research_notes/portable_direct/20261116_heartbeat_triad_refinement/LOOP_CHARACTERS.md",
    "awdawmip/enterprise-math@7b6ea72b90918af5363b319ef16e25122a123ad9:research_notes/portable_direct/20261116_heartbeat_triad_refinement/check_flat_paths.py"
  ],
  "evidence_status": "CONDITIONAL_AUTHOR_RESULTS_AND_OPEN_FOLLOWUP",
  "claim_lease_minutes": 120,
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-X6-ANCHORED-LOOP-CHARACTERS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL"
}
-->

# 心跳三槽中固定一根具名轴后的闭路相位分类

## 研究问题

三槽全开，保留每步的具名来源。在六根轴中固定一根持续可读的轴 d，d 可在路径中进入或离开占用支撑。背景结构只提供这个轴名。其余五轴可以一致重命名，平坦三角内的局部改道仍等价。对这些闭路，按串接相乘、反向取逆、搬移基点相容的 U(1) 标量相位有多少种？

## 可交付结果

求平坦三角商的整系数第一同调在 d 的稳定子 S5 下的余不变量群，或给出等价的完整字符分类。给出自由部分、挠部分及其如何作用在具名来源闭路上。若有超出置换奇偶的字符，给出一对奇偶相同、该字符可分的具体闭路；若只有两种，则证明其穷尽性。轴标签是对照输入；原生来源若提供这个标记，另列其出处。可使用包含图生成树、整数关系或其它等价证明。

六轴全开、无标记的秩 26 与奇偶定理可作退化校验。此前关于轴稳定子选取确定通道置换的研究（PR #1271、#1287）约束的是另外的输出；对比时明确区分其作用对象与本题的整闭路字符。引用 Craig 格点精细比较时仅使用其粗细路径比较动机。
