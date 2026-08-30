<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-MULTIPLICITY-COLLISION-FRONTIER",
  "title": "哲学先行 Q16：Return Multiplicity 的首个碰撞边界",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q16-return-multiplicity-collision-frontier",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Q13 proves that return-support semantics fail at first branching, while anonymous primitive-return multiplicity is exact only on U_BR4 and separates one explicit cubic support collision. Determine the first genuinely broader family on which multiplicity itself fails or remains reconstructive.",
  "next_action": "Freeze a connected finite cubic/subcubic family with a precise bounded size order, compute anonymous primitive-return multiplicity without Cell identities, search equal-packet nonisomorphic pairs first, and prove bounded injectivity/representability only where exhaustive coverage is exact.",
  "dependencies": ["RR-1AFF7788DED8C6F6B3D3"],
  "source_refs": ["research_returns/P000_PHILOSOPHY_FIRST_PATH_RETURN_BRANCHING_STRESS_RETURN_20260830.md", "driver_reviews/P000_PHILOSOPHY_FIRST_Q13_Q15_DRIVER_REVIEW_20260830.md"],
  "evidence_status": "DRIVER_ACCEPTED_Q13_MULTIPLICITY_IS_FIRST_MISSING_DATUM_WITH_GLOBAL_COMPLETENESS_OPEN",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["P000","philosophy-first","return-multiplicity","subcubic","reconstruction","representability","countermodel"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-RETURN-MULTIPLICITY-COLLISION-FRONTIER",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-PHILOSOPHY-FIRST-PATH-RETURN-BRANCHING-STRESS",
  "successor_gate": {
    "new_information_gap": "Q13 identifies multiplicity as the first missing datum after support collapse but does not know whether multiplicity is a genuine broader tomography interface or merely the next bounded repair.",
    "why_parent_result_does_not_close_it": "Q13 proves multiplicity injectivity only on the two-type U_BR4 class and gives one ten-Cell witness separated by multiplicity; it explicitly makes no global subcubic completeness claim.",
    "discriminating_outcomes": ["FIRST_EQUAL_MULTIPLICITY_NONISOMORPHIC_PAIR_CLASSIFIED","RETURN_MULTIPLICITY_INJECTIVE_ON_DECLARED_BOUNDED_FAMILY","MULTIPLICITY_REPRESENTABILITY_GAP_EXACTLY_CLASSIFIED"],
    "kill_condition": "At the first exact equal-multiplicity nonisomorphic pair, kill any general reconstruction claim and return the smallest missing relation information exposed by that pair instead of escalating to an almost-complete graph description.",
    "alternative_route_or_free_exploration_considered": "Adjacency spectra, Ihara zeta, full cycle bases and categorical gluing were considered but deferred because Q13 justifies testing multiplicity itself before stronger observation languages.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Q13 is terminal at first branching. This task changes the target from support failure to multiplicity failure/injectivity on a broader declared family and can cleanly kill the candidate interface."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# 哲学先行 Q16：Return Multiplicity 的首个碰撞边界

Status: `READY / P0 / MULTIPLICITY-COLLISION-FRONTIER`

## Mother question

Q13 说明 powerset return-support 太弱，而 multiplicity 是第一个被反模型逼出来的修复。但先质疑 multiplicity 本身：它究竟是 native tomography 的正确对象，还是只是在四 Cell 例子上恰好够用？

## Frozen inputs and scope

冻结 Q13 的 `U_BR4` 定理和十 Cell cubic support collision。候选对象仍为有限简单 native-Cell adjacency，优先 connected cubic/subcubic classes；probe 只报告匿名 primitive-return multiplicity，不得报告 Cell identity、canonical label、完整 adjacency matrix、完整 cycle basis 或外置谱对象。

必须先寻找 equal-multiplicity countermodel，再尝试正向 reconstruction theorem。

## Hard target and required outputs

Hard target: `P000_RETURN_MULTIPLICITY_COLLISION_FRONTIER_EXACTLY_CLASSIFIED`

1. 冻结一个严格大于 `U_BR4` 的有界 subcubic/cubic 模型类与同构等价。
2. 精确定义 anonymous primitive-return multiplicity packet。
3. 按 Cell 数从小到大寻找 packet 相同但非同构的 pair；若找到，给出结构性非同构证书。
4. 在任何宣称 injective 的有界范围，必须 exhaust exact model universe，而不是抽样。
5. 同时分类 formal multiplicity packets 的 representability image 或给出最小 virtual packet。
6. 若 multiplicity 失效，指出最小缺失信息，不得直接升级到几乎完整对象描述。
7. 输出 deterministic checker，并分离 bounded enumeration 与普遍结构证明。

## Research value to preserve

这一步决定 path-return 路线是否还能继续作为低信息 native observation，还是在 branching 后必然进入更丰富的关系结构。找到反例与证明一个大范围正定理同样有价值。

## Success, kill, and return criteria

有效终态：`FIRST_EQUAL_MULTIPLICITY_NONISOMORPHIC_PAIR_CLASSIFIED` / `RETURN_MULTIPLICITY_INJECTIVE_ON_DECLARED_BOUNDED_FAMILY` / `MULTIPLICITY_REPRESENTABILITY_GAP_EXACTLY_CLASSIFIED`。第一处精确碰撞出现后，应优先冻结失败边界，不得用高信息 probe 掩盖失败。
