<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N12-COLLISION-FRONTIER",
  "title": "哲学先行 Q28：固定 Return-Profile 1-WL 的 n=12 首碰撞检验",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q28-return-profile-1wl-n12-collision-frontier",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Q27 proves exact graph-level injectivity of the frozen return-profile-initialized ordinary 1-WL observable on U_BR(n) through n=11. The first possible stable equal-packet nonisomorphic collision is now unresolved at n=12.",
  "next_action": "Keep the Q22/Q25/Q27 observable bit-for-bit unchanged and attack n=12 countermodel-first using equitable partitions, regular covers/lifts, switching-style symmetric constructions, and low-degree kernels; freeze the first exact collision immediately, or only if necessary establish an independently complete exact n=12 collision-free certificate. Partial structural exhaustion must remain partial.",
  "dependencies": [
    "RR-5F80FBDB98CAA0E43177"
  ],
  "source_refs": [
    "research_returns/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N11_COLLISION_FRONTIER_RETURN_20260902.md",
    "driver_reviews/P000_PHILOSOPHY_FIRST_Q27_N11_DRIVER_REVIEW_20260902.md"
  ],
  "evidence_status": "FORMAL_DRIVER_REVIEW_ACCEPTED_POSTREVIEW_PUBLICATION_GENERATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "philosophy-first",
    "tomography",
    "return-profile",
    "1-WL",
    "color-refinement",
    "countermodel",
    "n12",
    "collision-frontier"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N12-COLLISION-FRONTIER",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N11-COLLISION-FRONTIER",
  "successor_gate": {
    "new_information_gap": "Q27 closes the exact finite prefix only through n=11. The first admissible size at which the unchanged observable can still fail is n=12, and no accepted collision witness or exact n=12 injectivity certificate exists.",
    "why_parent_result_does_not_close_it": "Q27 is deliberately bounded to eleven Cells and supplies no structural theorem propagating injectivity to twelve Cells.",
    "discriminating_outcomes": [
      "RETURN_PROFILE_1WL_N12_FIRST_STABLE_COLLISION_CLASSIFIED",
      "RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N12",
      "DECLARED_N12_STRUCTURAL_SEARCH_ROUTE_EXHAUSTED_WITHOUT_CENSUS_OR_MINIMALITY_CLAIM"
    ],
    "kill_condition": "On the first exact nonisomorphic equal-packet pair, freeze immediately. If an independently complete exact n=12 certificate proves injectivity, freeze the n<=12 bound and stop. Do not continue to n=13 inside this task.",
    "alternative_route_or_free_exploration_considered": "Strengthening to 2-WL, spectra, zeta data, full cycle incidence or canonical labeling was considered and rejected because the current objective is to locate the failure of the already frozen low-information observable before repairing it. Closure at n=11 was rejected because n=12 is the smallest unresolved size.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Q27 is terminal at n=11 by its own kill rule. A separate n=12 task preserves the exact finite frontier, isolates the larger search/certificate burden, and can terminate cleanly on either a collision, a complete lower-bound extension, or a declared partial structural boundary."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:46f9b27002cd7f8a3d64fdec95e8c4519dc99d8f003b48c21e4f94182bc98e8b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q28：固定 Return-Profile 1-WL 的 n=12 首碰撞检验

Status: `READY / P0 / HIGH / COUNTERMODEL-FIRST / POST-REVIEW GENERATION`

## Mother question

Q27 已把冻结的 return-profile 初始化普通 1-WL observable 的精确无碰撞前缀推进到 `n<=11`。现在只问第一个仍未解决的规模：在 `U_BR(12)` 中，是否首次存在两个非同构 native-Cell 对象具有完全相同的匿名稳定 packet？若不存在，只有独立完备证书才能把 lower bound 推进到 `n<=12`。

## Frozen inputs and scope

冻结 Q22/Q25/Q27 的模型类 `U_BR(n)`、初始颜色 `c0(x)=m_X(x)`、普通 1-WL 递推 `c_{t+1}(x)=(c_t(x), multiset_{y~x} c_t(y))` 与匿名稳定 packet `R_inf(X)`，定义一字不改。优先搜索 equitable partition、regular cover/lift、switching-style 对称构造和 degree-{2,3} 低度核所产生的精确反模型。不得先加入 2-WL、谱、zeta、完整 cycle incidence、canonical labels 或其他修复性 observable。

## Hard target and required outputs

Hard target: `P000_RETURN_PROFILE_1WL_N12_FIRST_COLLISION_OR_EXACT_LOWER_BOUND_CLASSIFIED`

若找到候选，必须给出 `X not~= Y`、二者均属于 `U_BR(12)`、初始 primitive-return profile 对齐且冻结 1-WL 稳定 packet 完全相等的确定性证书，并单独证明非同构。若宣称 `n=12` 无碰撞，必须给出与候选发现路线独立的 completeness authority，例如 exact degree-sector count 加 automorphism/orbit-stabilizer cover，并对完整 packet serialization 做无哈希判等。若只穷尽若干结构族，必须明确冻结为 partial structural boundary，不得冒充完整 census。

## Research value to preserve

这一步继续测量最低成本 tomography 层的真实失效位置，而不是提前修复它。若 `n=12` 首次出现碰撞，就得到下一阶段设计更强 observable 所需的最小 exact witness；若仍无碰撞，则获得新的严格有限强度下界。

## Success, kill, and return criteria

合法终态只有三类：`RETURN_PROFILE_1WL_N12_FIRST_STABLE_COLLISION_CLASSIFIED`、`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N12`、`DECLARED_N12_STRUCTURAL_SEARCH_ROUTE_EXHAUSTED_WITHOUT_CENSUS_OR_MINIMALITY_CLAIM`。找到 exact collision 立即冻结；若完整证书证明 `n=12` injective，也立即冻结并停在 `n<=12`。不得在本任务内继续 `n=13`，不得以更强 observable 消除尚未定位的失败。
