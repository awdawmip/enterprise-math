<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N11-COLLISION-FRONTIER",
  "title": "哲学先行 Q27：固定 Return-Profile 1-WL 的 n=11 首碰撞检验",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q27-return-profile-1wl-n11-collision-frontier",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Q25 proves that the frozen return-profile-initialized ordinary 1-WL observable is exactly injective on U_BR(n) through n=10. The first stable equal-packet nonisomorphic collision remains unknown beginning at n=11.",
  "next_action": "Keep the Q22/Q25 observable bit-for-bit unchanged and attack n=11 countermodel-first via equitable partitions, regular covers/lifts, switching-style symmetric constructions and degree-{2,3} kernels; only if needed, build an independently complete exact n=11 census/certificate. Freeze either the first exact collision or an exact n=11 collision-free bound.",
  "dependencies": [
    "RR-234ABD5082081CEBAB05"
  ],
  "source_refs": [
    "research_returns/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_FIRST_COLLISION_FRONTIER_RETURN_20260901.md",
    "driver_reviews/P000_PHILOSOPHY_FIRST_Q25_N10_DRIVER_REVIEW_20260902.md"
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
    "n11",
    "collision-frontier"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N11-COLLISION-FRONTIER",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-FIRST-COLLISION-FRONTIER",
  "successor_gate": {
    "new_information_gap": "Q25 closes the exact finite prefix only through n=10. The smallest admissible size at which the frozen observable can still fail is now n=11, and neither a collision witness nor an exact n=11 injectivity certificate exists in the accepted record.",
    "why_parent_result_does_not_close_it": "Q25 is deliberately bounded: its orbit-stabilizer certificate is complete for ten Cells and explicitly leaves n>=11 unresolved. It gives no structural theorem that propagates injectivity to eleven Cells.",
    "discriminating_outcomes": [
      "RETURN_PROFILE_1WL_N11_FIRST_STABLE_COLLISION_CLASSIFIED",
      "RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N11",
      "DECLARED_N11_STRUCTURAL_SEARCH_ROUTE_EXHAUSTED_WITHOUT_CENSUS_OR_MINIMALITY_CLAIM"
    ],
    "kill_condition": "If an exact nonisomorphic pair in U_BR(11) with equal frozen stable packets is found, freeze it immediately. If a complete exact n=11 certificate proves injectivity, freeze the n<=11 lower bound and stop; do not continue to n=12 inside this task.",
    "alternative_route_or_free_exploration_considered": "Higher-order WL, spectra, zeta data, full cycle incidence and canonical labels are rejected because they change the observable before its first failure is located. Unbounded size escalation is also rejected; structural countermodels at the first unresolved size are preferred before a complete census.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Q25 terminally records the n=10 exact census. A separate n=11 stage preserves immutable finite-frontier provenance, gives the larger computation its own claim/lease/certificate boundary, and can stop cleanly on either a first collision or a new bounded lower frontier."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q27：固定 Return-Profile 1-WL 的 n=11 首碰撞检验

Status: `READY / P0 / HIGH / COUNTERMODEL-FIRST / POST-REVIEW GENERATION`

## Mother question

Q25 已经把冻结的 return-profile 初始化 1-WL observable 的精确无碰撞前缀推进到 `n<=10`。现在只问第一个仍未解决的规模：在 `U_BR(11)` 中，是否首次存在两个非同构 native-Cell 对象具有完全相同的匿名稳定 packet？若不存在，必须用独立完备证书把 lower bound 精确推进到 `n<=11`。

## Frozen inputs and scope

冻结 Q22/Q25 的模型类 `U_BR(n)`、初始颜色 `c0(x)=m_X(x)`、普通 1-WL 递推 `c_{t+1}(x)=(c_t(x), multiset_{y~x} c_t(y))` 与匿名稳定 packet `R_inf(X)`，定义一字不改。先做 equitable partition、regular cover/lift、switching-style 对称构造和 degree-{2,3} suppression-kernel 的结构反模型搜索；只有确有必要时才做完整 `n=11` 精确 census。不得加入 2-WL、谱、zeta、完整 cycle incidence、canonical labels 或其他修复性 observable。

## Hard target and required outputs

Hard target: `P000_RETURN_PROFILE_1WL_N11_FIRST_COLLISION_OR_EXACT_LOWER_BOUND_CLASSIFIED`

若找到候选，必须给出 `X not~= Y`、初始 primitive-return profile 对齐、冻结 1-WL 稳定后 packet 仍完全相等的确定性短证书，并确认二者均属于 `U_BR(11)`。若宣称 `n=11` 无碰撞，必须给出与代表 discovery 独立的 completeness authority，例如 exact degree-sector count + automorphism/orbit-stabilizer cover，并对完整 packet serialization 做无哈希判等；哈希只能用于冻结已验证图像。任何只覆盖部分结构族的阴性结果只能返回 declared structural-search boundary，不能冒充 `n=11` census。

## Research value to preserve

这一阶段定位最低成本 tomography 层在第一个未决规模上的真实失效点。价值在于获得一个 exact failure witness，或继续量化固定低信息 observable 的有限强度；不在于把标准 1-WL 重新命名，也不在于提前引入更高抽象。

## Success, kill, and return criteria

合法终态只有三类：`RETURN_PROFILE_1WL_N11_FIRST_STABLE_COLLISION_CLASSIFIED`、`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N11`、`DECLARED_N11_STRUCTURAL_SEARCH_ROUTE_EXHAUSTED_WITHOUT_CENSUS_OR_MINIMALITY_CLAIM`。找到 exact collision 立即冻结；若完整证书证明 `n=11` injective，也立即冻结并停在 `n<=11`。不得在本任务内继续 `n=12`，不得用更强 observable 修补碰撞。
