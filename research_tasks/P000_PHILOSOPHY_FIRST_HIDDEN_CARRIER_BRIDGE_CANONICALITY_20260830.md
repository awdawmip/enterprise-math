<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-HIDDEN-CARRIER-BRIDGE-CANONICALITY",
  "title": "哲学先行 Q18：Hidden–Carrier Bridge 的典范性与签名稳健性",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q18-hidden-carrier-bridge-canonicality",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Q15 internalizes a finite nonsplit hidden kernel using HiddenBalance3 plus a primitive HiddenAxisInc bridge, but does not decide whether the cross-sort bridge is canonically derivable from the internal hidden relation and the existing carrier, or whether the success depends on an arbitrary 24-fold matching.",
  "next_action": "Derive the four hidden fibres from HiddenBalance3 without a bridge, derive the four carrier stars from Q10, compute the full primitive-preserving automorphism action on all bijections between these two four-object sets, and test for fixed/natural bridge choices before adding any weaker cross-sort relation.",
  "dependencies": ["RR-D0BDDC6304CFFA6278DE"],
  "source_refs": ["research_returns/P000_PHILOSOPHY_FIRST_HIDDEN_KERNEL_MODEL_SIGNATURE_RETURN_20260830.md", "driver_reviews/P000_PHILOSOPHY_FIRST_Q13_Q15_DRIVER_REVIEW_20260830.md"],
  "evidence_status": "DRIVER_ACCEPTED_Q15_FINITE_NONSPLIT_INTERNALIZATION_WITH_PRIMITIVE_CROSS_SORT_BRIDGE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["P000","philosophy-first","hidden-kernel","bridge","canonicality","naturality","torsor","signature-minimality"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-HIDDEN-CARRIER-BRIDGE-CANONICALITY",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-PHILOSOPHY-FIRST-HIDDEN-KERNEL-MODEL-SIGNATURE",
  "successor_gate": {
    "new_information_gap": "Q15 proves that a cross-sort bridge relation is deletion-necessary for its internal nonsplit witness, but does not test whether that bridge is naturally definable from the bridge-free hidden and carrier structures or how much independent matching information it contributes.",
    "why_parent_result_does_not_close_it": "Q15 treats HiddenAxisInc as primitive and proves deletion failure; primitive necessity is not the same as canonical derivability or information-minimality of the bridge choice.",
    "discriminating_outcomes": ["NO_NATURAL_HIDDEN_CARRIER_BRIDGE_WITH_EXACT_TORSOR_CERTIFICATE","CANONICAL_BRIDGE_DERIVED_FROM_EXISTING_RELATIONS","WEAKER_CROSS_SORT_RELATION_SUFFICES_FOR_NONSPLIT_INTERNALIZATION"],
    "kill_condition": "If the bridge choices form a free/transitive symmetry orbit with no fixed point, kill any claim that Q15's bridge is derived canonically; if a weaker relation still merely names one bijection, reject it as repackaged choice rather than structural repair.",
    "alternative_route_or_free_exploration_considered": "Treating HiddenAxisInc as permanently primitive is a valid closure option. Searching new hidden groups or nonabelian cohomology is deferred until the information cost and canonicality of the existing bridge are understood.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Q15 is terminal for existence of one deletion-minimal finite signature. Q18 asks a different object-language question: whether its cross-sort coupling is natural, how many choices it contains, and whether a weaker structural bridge can replace it."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# 哲学先行 Q18：Hidden–Carrier Bridge 的典范性与签名稳健性

Status: `READY / P1 / BRIDGE-CANONICALITY`

## Mother question

Q15 已经证明：没有 `HiddenAxisInc`，hidden automorphisms 与 carrier automorphisms 会解耦，nonsplit mechanism 消失。但这只说明桥“有用且必要”，还没有说明桥是不是**自然产生的**。

先质疑桥本身：hidden relation 内部派生出的四个 fibre 与 carrier 四个 star 之间，是否存在不用人为选择就能定义的对应？如果没有，Q15 的成功应被理解为“需要额外跨 sort 信息”，而不是 hidden relation 自动解释 carrier。

## Frozen inputs and scope

冻结 Q15 的 `HiddenBalance3` 8-point finite witness、Q10 carrier-star structure与 Q7 naturality fixed-point纪律。第一阶段必须移除 `HiddenAxisInc`，只保留两侧各自的 primitive structure。

不得以 `F3^2` 坐标、projective labels、A/B/C/D star 名称或预先选定 bijection 作为 bridge 定义。任何 weaker bridge candidate 必须按 automorphism invariance 与 deletion test 审核。

## Hard target and required outputs

Hard target: `P000_HIDDEN_CARRIER_BRIDGE_CANONICALITY_AND_INFORMATION_COST_CLASSIFIED`

1. 从 bridge-free `HiddenBalance3` 派生四个 hidden fibres；从 Q10 派生四个 carrier stars。
2. 计算两侧 primitive automorphism groups 对全部 fibre-to-star bijections 的作用。
3. 判定是否存在 automorphism-fixed / natural bridge；若不存在，给出完整 orbit/torsor certificate。
4. 量化选择桥所增加的最小 finite information，区分 presentation labels 与 invariant choice class。
5. 测试至少两个比 full `HiddenAxisInc` 更弱的 cross-sort relations，判断是否足以恢复 Q15 nonsplit readout，同时不直接编码完整 bijection。
6. 若 weaker relation 成功，做 deletion/minimality audit；若失败，证明失败原因。
7. 输出 deterministic checker；不得把 certificate group names 提升为 bare P000 ontology。

## Research value to preserve

这一步决定 Q15 是真正的“hidden structure 自发耦合到 carrier”，还是“hidden structure + 一个独立桥选择”才产生 nonsplit extension。两种答案都重要，因为它们对应完全不同的本体成本。

## Success, kill, and return criteria

有效终态：`NO_NATURAL_HIDDEN_CARRIER_BRIDGE_WITH_EXACT_TORSOR_CERTIFICATE` / `CANONICAL_BRIDGE_DERIVED_FROM_EXISTING_RELATIONS` / `WEAKER_CROSS_SORT_RELATION_SUFFICES_FOR_NONSPLIT_INTERNALIZATION`。若无 fixed/natural choice，应明确冻结非典范性，不得用任意 labeling 选一个 bridge 后称为 canonical。
