<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-FIRST-COLLISION-FRONTIER",
  "title": "哲学先行 Q25：Return-Profile 初始化 1-WL 的首个稳定碰撞边界",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q25-return-profile-1wl-first-collision-frontier",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Q22 identifies the frozen rootwise refinement exactly as ordinary 1-WL/color refinement initialized by primitive-return multiplicity profiles and proves exact injectivity on U_BR(n) only through n=9. The next unresolved question is not another repair but the first stable equal-packet nonisomorphic witness, or a rigorously extended collision-free lower bound if no witness is found in the declared search range.",
  "next_action": "Keep the Q22 observable unchanged and search countermodel-first beyond n=9, prioritizing structural 1-WL-indistinguishability mechanisms such as equitable partitions, regular covers/lifts, and symmetric cubic/degree-{2,3} constructions before broad enumeration; freeze the first exact collision found or an explicitly bounded extended lower frontier.",
  "dependencies": ["RR-8A1951FD6A09D5D232CD"],
  "source_refs": ["research_returns/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_ITERATED_REFINEMENT_FRONTIER_RETURN_20260831.md"],
  "evidence_status": "Q22_RESULT_REVIEW_BOUND_SUCCESSOR; PUBLICATION_ONLY_AFTER_DRIVER_ACCEPTANCE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["P000","philosophy-first","tomography","return-profile","1-WL","color-refinement","countermodel","collision-frontier"],
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
    "new_information_gap": "Q22 establishes exact injectivity only for 4<=n<=9 and explicitly leaves n>=10 open. Because the recurrence is now identified with standard 1-WL, the meaningful next datum is the first exact failure of this fixed observable on the native U_BR family, not another unmotivated feature addition.",
    "why_parent_result_does_not_close_it": "Q22 gives a finite exact prefix and a general stabilization theorem, but neither proves global reconstruction nor supplies a stable equal-packet nonisomorphic countermodel.",
    "discriminating_outcomes": ["RETURN_PROFILE_1WL_FIRST_STABLE_COLLISION_CLASSIFIED","RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_STRICTLY_EXTENDED","DECLARED_STRUCTURAL_SEARCH_ROUTE_EXHAUSTED_WITHOUT_MINIMALITY_CLAIM"],
    "kill_condition": "Once an exact stable equal-packet nonisomorphic witness is found, stop the task and freeze it. Do not repair the witness by adding 2-WL, spectra, zeta data, complete cycle incidence, or canonical labels inside this task.",
    "alternative_route_or_free_exploration_considered": "Immediate higher-dimensional WL and richer graph invariants were considered but rejected because Q8's minimum-abstraction rule requires an exact failure witness for the frozen Q22 observable first. Pure blind size escalation was also rejected in favor of structural countermodel mechanisms before broader finite search.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Q22 is terminal for the exact n<=9 prefix and the algorithm-identification audit. Q25 changes the hard target to the first failure frontier while keeping the observable fixed, so it can terminate cleanly without rewriting Q22."
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

Status: `READY / P0 / COUNTERMODEL-FIRST`

## Mother question

Q22 已经把新增递推准确去重为标准 1-WL/color refinement，只是初始颜色来自进取数论的 primitive-return multiplicity profile。它在 `U_BR(n)` 的 `4<=n<=9` 精确前缀上没有碰撞，但这并不构成全局重建定理。

因此现在不应继续给 packet 加信息。真正的问题是：**固定 Q22 observable 不动，它第一次在哪里把两个非同构 native-Cell 对象压成同一个稳定 packet？** 如果短期找不到，最多只能把经过精确验证的 collision-free lower bound 向前推进，不能把“尚未找到”改写成“不会发生”。

## Frozen inputs and scope

完整冻结 Q22 的模型类、初始 profile 与递推：`U_BR(n)`、`c0(x)=m_X(x)`、`c_{t+1}(x)=(c_t(x), multiset_{y~x}c_t(y))`，以及匿名稳定 packet `R_inf(X)`。

不得改变初始颜色，不得加入二元 root tuple、2-WL、谱、zeta、完整 cycle incidence 或 canonical graph label。经典 1-WL 文献在本任务中只用于寻找已知失效机制与去重，不是原生公理。

搜索必须先走结构反模型路线：equitable partition、regular cover/lift、对称 cubic/degree-{2,3} 构造，以及已知 1-WL 不可分辨机制在 `U_BR` 限制下的可实现性。只有结构路线没有给出足够小的候选时，才扩大有限精确枚举。

## Hard target and required outputs

Hard target: `P000_RETURN_PROFILE_1WL_FIRST_COLLISION_OR_EXTENDED_LOWER_BOUND_EXACTLY_CLASSIFIED`

1. 复核 Q22 的 `n<=9` frozen prefix 作为 regression guard，而不是重新研究 Q22。
2. 在 `n>=10` 中主动构造并验证 `R_inf(X)=R_inf(Y)` 且 `X`、`Y` 非同构的 exact witness；若宣称“首个”，必须排除全部更小 admissible size。
3. 若资源允许的明确 bounded range 内未发现碰撞，只冻结严格的 collision-free lower bound，并写清未覆盖范围；禁止作全局 completeness 推断。
4. 对候选对给出短结构证书：为什么初始 return profile 对齐、为什么 1-WL 稳定后仍对齐、为什么对象非同构。
5. 说明 countermodel 机制是否是标准 1-WL failure 的直接实例、受 `U_BR` 限制后的新特例，或需要项目特定的 return-profile 初始化才能成立。
6. 输出确定性 checker/certificate，有限搜索结论与结构证明分层记录。

## Research value to preserve

Q22 的价值不是“1-WL 很强”，而是它证明最低成本的 rootwise relational repair 至少能走到九 Cells。Q25 的价值是给这一最低抽象层找到**真正的失效点**。只有拿到失效见证，后续是否需要二阶关系语言才有正当性；若可把无碰撞前缀大幅推进，也能量化这套低信息 tomography 的实际强度，而不把标准算法误包装成新数学。

## Success, kill, and return criteria

有效终态包括：

- `RETURN_PROFILE_1WL_FIRST_STABLE_COLLISION_CLASSIFIED`；
- `RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_STRICTLY_EXTENDED`；
- `DECLARED_STRUCTURAL_SEARCH_ROUTE_EXHAUSTED_WITHOUT_MINIMALITY_CLAIM`。

一旦得到 exact collision，立即冻结；任何“修复 collision”的更高阶 observable 都属于新的问题，必须重新通过最低充分抽象门槛。
