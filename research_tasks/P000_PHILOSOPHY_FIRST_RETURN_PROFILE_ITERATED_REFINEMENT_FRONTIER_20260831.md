<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-ITERATED-REFINEMENT-FRONTIER",
  "title": "哲学先行 Q22：Return Profile 的迭代邻域精化与稳定碰撞边界",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q22-return-profile-iterated-refinement-frontier",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Q19 shows that the full global edge-profile histogram repairs the Q16 eight-Cell collision but first fails at nine Cells because it forgets which neighboring profile classes co-occur at the same anonymous root. Determine whether the native rootwise neighbor-profile refinement stabilizes as a genuinely stronger low-information tomography interface or reaches its own exact nonisomorphic collision.",
  "next_action": "Freeze the native iterative refinement c0(x)=return-multiplicity profile and c_{t+1}(x)=(c_t(x), multiset of c_t-neighbor classes), anonymize the stable root-color multiset, verify the Q19 nine-Cell pair separates, then search the declared U_BR(n) size order countermodel-first for the first stable equal-packet nonisomorphic pair before considering any higher-order relation.",
  "dependencies": ["RR-AC29BC88CA7CB2AFBA21"],
  "source_refs": ["research_returns/P000_PHILOSOPHY_FIRST_RETURN_EDGE_CORRELATION_COLLISION_FRONTIER_RETURN_20260831.md"],
  "evidence_status": "Q19_RESULT_REVIEW_BOUND_SUCCESSOR; PUBLICATION_ONLY_AFTER_DRIVER_ACCEPTANCE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["P000","philosophy-first","tomography","return-profile","local-refinement","countermodel","representability"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-ITERATED-REFINEMENT-FRONTIER",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-EDGE-CORRELATION-COLLISION-FRONTIER",
  "successor_gate": {
    "new_information_gap": "Q19 isolates rootwise co-occurrence of neighboring anonymous profile classes as information not contained in the global class-edge histogram. The minimal systematic repair is iterative native neighbor-profile refinement, but its separation power and stable collision frontier are unknown.",
    "why_parent_result_does_not_close_it": "Q19 supplies only a witness-specific root-incidence scalar and explicitly does not claim completeness of the rootwise refinement it suggests.",
    "discriminating_outcomes": ["STABLE_RETURN_PROFILE_REFINEMENT_FIRST_COLLISION_CLASSIFIED","ITERATED_REFINEMENT_INJECTIVE_AND_REPRESENTABLE_ON_EXACT_DECLARED_PREFIX","ITERATED_REFINEMENT_COLLAPSES_TO_HIGH_INFORMATION_ENCODING_AND_LOW_INFORMATION_ROUTE_KILLED"],
    "kill_condition": "If a stable equal-refinement nonisomorphic pair is found, freeze it immediately and do not repair by importing full adjacency, spectra, zeta data, canonical labels, or higher-order tuple machinery inside the same task. If the refinement only succeeds by becoming an almost-complete encoding of the object, kill its status as a low-information tomography interface.",
    "alternative_route_or_free_exploration_considered": "Immediate higher-order tuple refinement, spectral invariants, complete cycle incidence, and canonical labeling were considered and rejected because Q19 exposes a strictly lower one-root co-occurrence gap first.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Q19 is terminal for the global edge-profile histogram. The successor changes the observable from an aggregate class-edge count to a recursively rooted local relation and can refute that repair cleanly without weakening Q19."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q22：Return Profile 的迭代邻域精化与稳定碰撞边界

Status: `READY / P0 / COUNTERMODEL-FIRST`

## Mother question

Q19 已证明：知道每种匿名 return profile 之间有多少条边仍然不够，因为全局直方图不知道这些边是否在同一个 root 上共同出现。

因此先质疑下一问本身：真正缺的是“更远距离的信息”，还是只需要把**一步邻域关系重新绑定到每个匿名 root**，然后重复这一最低成本操作？如果这种迭代最终仍把非同构对象压成同一个稳定 packet，就应该在那个反模型处停止，而不是直接升级到完整邻接描述。

## Frozen inputs and scope

冻结 Q19 的 `U_BR(n)`：有限、连通、简单 native-Cell 邻接图，每个 Cell 度数属于 `{2,3}`，至少一个度 3 Cell，按 Cell relabeling / graph isomorphism 取等价类。

冻结 `c0(x)=m_X(x)` 为 Q16/Q19 已接受的 primitive-return multiplicity profile。递归定义

`c_{t+1}(x) = ( c_t(x), multiset_{y~x} c_t(y) )`

并在每一步只保留等价结构签名，不保留 Cell 名字。令 `R_t(X)` 为所有 root color 的匿名 multiset；当分割稳定时记 `R_inf(X)`。

必须先以 native root/profile/neighbor 语言定义。只有该定义冻结以后，才允许比较经典 color refinement / 1-dimensional Weisfeiler-Leman 文献，用于 prior-art/duplication 识别；不得把经典名称当作原语，也不得提出方法新颖性主张。

## Hard target and required outputs

Hard target: `P000_RETURN_PROFILE_ITERATED_REFINEMENT_STABLE_FRONTIER_EXACTLY_CLASSIFIED`

1. 证明每层 `R_t` 及稳定 packet `R_inf` 在 Cell relabeling 下不变，并给出有限稳定上界。
2. 复现 Q19 的九 Cell collision，证明最少一轮 rootwise refinement 是否将其分离。
3. 在明确的 `U_BR(n)` size order 上 countermodel-first 搜索 `R_inf(X)=R_inf(Y)` 但 `X`、`Y` 非同构的最小或首个精确 collision；若找到，给出短结构证书。
4. 对所有宣称 collision-free 的有界前缀同时给出 exact separation 与 representability image/certificate；禁止只证明 injectivity 而不检查 formal packet image。
5. 记录每个对象达到稳定所需的最少轮数，并判断信息增长是否仍属于低信息局部精化，还是已经退化为近乎完整对象编码。
6. 原生定义冻结后，执行一次明确的 classical prior-art/dedup 对照，说明本任务与标准 color refinement / 1-WL 的关系；项目结论只能是声明 native 初始化与模型类上的精确边界，不能把标准算法包装成新工具。
7. 输出确定性 checker；有限枚举只支撑真实穷举范围，普遍结论必须另给结构证明。

## Research value to preserve

Q16、Q19 已连续显示：先是 root return multiplicity 丢掉“位置”，再是全局 profile-edge correlation 丢掉“同一 root 上的共现”。Q22 检验最低成本的局部关系精化能走多远。如果稳定 packet 很快碰撞，我们会得到升级到更高关系阶数的精确失败见证；如果它在较大精确前缀仍可重建，则得到一个比完整邻接更低信息的 native tomography 候选，而且与经典方法的关系会被明确去重。

## Success, kill, and return criteria

有效终态包括：

- `STABLE_RETURN_PROFILE_REFINEMENT_FIRST_COLLISION_CLASSIFIED`；
- `ITERATED_REFINEMENT_INJECTIVE_AND_REPRESENTABLE_ON_EXACT_DECLARED_PREFIX`；
- `ITERATED_REFINEMENT_COLLAPSES_TO_HIGH_INFORMATION_ENCODING_AND_LOW_INFORMATION_ROUTE_KILLED`。

一旦找到稳定 equal-packet 非同构反模型，不得在同一任务中通过加入二元 tuple、谱、完整 cycle incidence 或 canonical labeling 抹掉反例。下一层抽象必须重新通过最低充分抽象门槛。
