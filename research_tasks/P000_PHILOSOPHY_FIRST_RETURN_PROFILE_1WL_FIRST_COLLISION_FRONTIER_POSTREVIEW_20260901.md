<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-FIRST-COLLISION-FRONTIER",
  "title": "哲学先行 Q25：Return-Profile 初始化 1-WL 的首个稳定碰撞边界",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q25-return-profile-1wl-first-collision-frontier",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Q22 fixes the rootwise refinement as ordinary 1-WL/color refinement initialized by primitive-return multiplicity profiles and proves exact injectivity only through n=9. The unresolved datum is the first stable equal-packet nonisomorphic witness, or a rigorously extended collision-free lower bound within an explicit search range.",
  "next_action": "Keep the Q22 observable unchanged and search countermodel-first beyond n=9, prioritizing equitable partitions, regular covers/lifts, and symmetric degree-{2,3} constructions before broader enumeration; freeze the first exact collision or only an explicitly bounded extended lower frontier.",
  "dependencies": [
    "RR-8A1951FD6A09D5D232CD"
  ],
  "source_refs": [
    "research_returns/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_ITERATED_REFINEMENT_FRONTIER_RETURN_20260831.md",
    "driver_reviews/P000_PHILOSOPHY_FIRST_Q22_Q24_DRIVER_REVIEW_20260901.md"
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
    "collision-frontier"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-FIRST-COLLISION-FRONTIER",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-ITERATED-REFINEMENT-FRONTIER",
  "successor_gate": {
    "new_information_gap": "Q22 establishes exact injectivity only for 4<=n<=9 and explicitly leaves n>=10 open. Because the recurrence is standard 1-WL with a project-specific initial coloring, the next meaningful datum is the first exact failure of this fixed observable on U_BR, not another feature addition.",
    "why_parent_result_does_not_close_it": "Q22 gives a finite exact prefix and a general stabilization theorem, but neither proves global reconstruction nor supplies a stable equal-packet nonisomorphic countermodel.",
    "discriminating_outcomes": [
      "RETURN_PROFILE_1WL_FIRST_STABLE_COLLISION_CLASSIFIED",
      "RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_STRICTLY_EXTENDED",
      "DECLARED_STRUCTURAL_SEARCH_ROUTE_EXHAUSTED_WITHOUT_MINIMALITY_CLAIM"
    ],
    "kill_condition": "Once an exact stable equal-packet nonisomorphic witness is found, stop and freeze it. Do not repair the witness by adding 2-WL, spectra, zeta data, complete cycle incidence, or canonical labels inside this task.",
    "alternative_route_or_free_exploration_considered": "Immediate higher-dimensional WL and richer invariants were rejected because the minimum-abstraction rule requires an exact failure witness for the frozen Q22 observable first. Structural countermodel mechanisms are preferred before broad size escalation.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Q22 is terminal for the exact n<=9 prefix and algorithm-identification audit. Q25 changes the hard target to the first failure frontier while keeping the observable fixed, so it can terminate cleanly without rewriting Q22."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q25：Return-Profile 初始化 1-WL 的首个稳定碰撞边界

Status: `READY / P0 / COUNTERMODEL-FIRST / POST-REVIEW GENERATION`

## Mother question

Q22 已经把递推去重为标准 1-WL/color refinement，并证明 `U_BR(n)` 在 `4<=n<=9` 的精确前缀没有稳定 packet 碰撞。现在固定这一 observable 不动：它第一次在哪里把两个非同构 native-Cell 对象压成同一个稳定 packet？若明确的有界搜索范围内仍未找到，只能冻结经验证的 collision-free lower bound。

## Frozen inputs and scope

冻结 Q22 的模型类 `U_BR(n)`、初始 profile `c0(x)=m_X(x)`、递推 `c_{t+1}(x)=(c_t(x), multiset_{y~x} c_t(y))` 与匿名稳定 packet `R_inf(X)`。不得加入 2-WL、谱、zeta、完整 cycle incidence 或 canonical label。先走 equitable partition、regular cover/lift、对称 degree-{2,3} 构造等结构反模型路线，再扩大有限精确搜索。

## Hard target and required outputs

Hard target: `P000_RETURN_PROFILE_1WL_FIRST_COLLISION_OR_EXTENDED_LOWER_BOUND_EXACTLY_CLASSIFIED`

复核 `n<=9` 作为 regression guard；对 `n>=10` 主动构造并验证 `R_inf(X)=R_inf(Y)` 且 `X`、`Y` 非同构的 exact witness。若宣称“首个”，必须排除全部更小 admissible size；若仅得到 lower bound，必须写清覆盖范围。每个候选需给出初始 profile 对齐、稳定后仍对齐、非同构的短证书，并提供确定性 checker/certificate。

## Research value to preserve

本任务只定位最低成本 tomography 层的真实失效点，不把标准 1-WL 重新包装成新数学。拿到失效见证后，后续是否需要更高阶关系语言才有正当性；若无碰撞前缀显著延长，则量化这一低信息 observable 的实际强度。

## Success, kill, and return criteria

有效终态为 `RETURN_PROFILE_1WL_FIRST_STABLE_COLLISION_CLASSIFIED`、`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_STRICTLY_EXTENDED` 或 `DECLARED_STRUCTURAL_SEARCH_ROUTE_EXHAUSTED_WITHOUT_MINIMALITY_CLAIM`。一旦得到 exact collision 立即冻结；修复该 collision 的更高阶 observable 必须另立任务。
