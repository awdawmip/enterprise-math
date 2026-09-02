<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-ROTATION-LAW-EXTENSION-CLAUSE-NONCANONICITY",
  "title": "哲学先行 Q31：Rotation Law 扩展判别条款的非典范性审计",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q31-rotation-law-extension-clause-noncanonicity",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Q29 proves by matched finite typed countermodels that current P000 does not select a unique native 6D rotation law. Even inside the active structure-preserving equivalence class, E2 and E3 survive the same current-P000 tests while having inequivalent state-action representation images. Thus any law-selection step needs additional information rather than more manipulation of the existing clauses.",
  "next_action": "Freeze current P000 and the Q29 typed-law equivalence. Define a candidate-blind invariant language for possible extension clauses, then classify the lowest noncircular clauses that separate admissible rotation-law families. Search first for two incomparable minimal discriminators; if they exist, freeze noncanonicity instead of choosing one by preference.",
  "dependencies": [
    "RR-EAA5E06ACC18BB1E21BE"
  ],
  "source_refs": [
    "research_result_records/RS-P000-PHILOSOPHY-FIRST-NATIVE-6D-ROTATION-LAW-CANDIDATE-DISCRIMINATION/RR-EAA5E06ACC18BB1E21BE.json",
    "research_returns/P000_PHILOSOPHY_FIRST_NATIVE_6D_ROTATION_LAW_CANDIDATE_DISCRIMINATION_RETURN_20260902.md",
    "driver_reviews/P000_PHILOSOPHY_FIRST_Q29_ROTATION_LAW_DRIVER_REVIEW_20260902.md"
  ],
  "evidence_status": "FORMAL_DRIVER_REVIEW_ACCEPTED_EXTENSION_AUDIT_ONLY",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "philosophy-first",
    "rotation",
    "6D",
    "typed-law",
    "extension-clause",
    "minimality",
    "noncanonicity",
    "countermodel"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-ROTATION-LAW-EXTENSION-CLAUSE-NONCANONICITY",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-PHILOSOPHY-FIRST-NATIVE-6D-ROTATION-LAW-CANDIDATE-DISCRIMINATION",
  "successor_gate": {
    "new_information_gap": "Q29 establishes underdetermination but does not classify the minimal additional invariant information needed to discriminate admissible typed rotation laws, nor whether such minimal additions are unique or form incomparable choices.",
    "why_parent_result_does_not_close_it": "The Q29 kill condition correctly stops canonical law selection under current P000. It does not answer the extension-level question of what extra information would be sufficient, minimal, noncircular, and invariant under typed-law equivalence.",
    "discriminating_outcomes": [
      "NO_CANONICAL_MINIMAL_ROTATION_EXTENSION_CLAUSE_ON_DECLARED_LANGUAGE",
      "UNIQUE_MINIMAL_NONCIRCULAR_ROTATION_EXTENSION_PRINCIPLE_ISOLATED_WITHOUT_P000_PROMOTION",
      "DECLARED_EXTENSION_CLAUSE_LANGUAGE_TOO_WEAK_OR_CIRCULAR"
    ],
    "kill_condition": "If two candidate-blind invariant clauses are each minimal, noncircular and sufficient to select inequivalent admissible subfamilies, with neither implied by current P000 nor by the other, freeze NO_CANONICAL_MINIMAL_ROTATION_EXTENSION_CLAUSE and stop. If a unique minimal principle is proved, freeze it only as an extension candidate and do not promote it to P000. If the clause language can distinguish candidates only by naming target models or encoding their action tables, freeze circularity and stop.",
    "alternative_route_or_free_exploration_considered": "Directly adopting U_r^2=id, a fixed-point count, a preferred finite group, SO(6), or one of E2/E3 was considered and rejected because Q29 proves that current P000 does not authorize such a preference. Closing all rotation research was also considered, but it would leave the newly isolated extension-information question unclassified.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Q29 is terminal at no-selection and must not be reopened to choose a law. A separate extension-audit task preserves that theorem while asking the next falsifiable question: whether the missing information itself has a canonical minimal form."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:46f9b27002cd7f8a3d64fdec95e8c4519dc99d8f003b48c21e4f94182bc98e8b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q31：Rotation Law 扩展判别条款的非典范性审计

Status: `READY / P0 / HIGH / EXTENSION-AUDIT / COUNTERMODEL-FIRST`

## Mother question

Q29 已经证明：在当前 P000 下，即使把讨论限制在 active、structure-preserving 的 typed Full-Cell equivalence laws，也仍然存在满足同一冻结条件但彼此不等价的候选。因此下一步不能“挑一个旋转律”，而应先问：**让 rotation law 从欠定变成可判别，最低还缺什么信息？这种最低信息本身是否唯一、自然、非循环？**

## Frozen inputs and scope

冻结当前 P000、Q26 typed interface、Q23 zero-support boundary、Q24 observation discipline 与 Q29 typed-law equivalence，不修改其内容。候选扩展条款必须以 typed-law equivalence 下的不变量语言表达，不能点名 `E2/E3/U/F`，不能把目标 action table、目标群、目标阶数答案直接编码为 primitive。允许审计有限 action equations、invertibility/rank/orbit/image/fixed-set 等候选 invariant families，但每类都必须做删除、反模型与循环性检查。`SO(6)`、连续角度、connection/holonomy、非零 effectivity 均不得预装。

## Hard target and required outputs

Hard target: `P000_ROTATION_LAW_EXTENSION_CLAUSE_MINIMALITY_OR_NONCANONICITY_CLASSIFIED`

必须先构造 candidate-blind 的扩展条款语言和等价关系，再寻找最小充分条款。若存在两个互不蕴含、都最小且非循环的判别条款，并分别保留不同 admissible law families，则应冻结“最低扩展信息不典范”，而不是任选其一。若声称存在唯一最低原则，必须证明删除任一成分都会重新出现 matched countermodels，并证明该原则不是对目标候选的重命名。若当前声明语言只能靠直接编码 action table 才能选出结果，应返回 circularity / language-too-weak，而不是升级语言掩盖失败。

## Research value to preserve

Q29 把“P000 缺少 rotation law”从直觉变成了精确欠定定理；Q31 要进一步区分“缺一个自然公理”与“缺的是一个本质上非唯一的选择”。这决定未来 rotation 研究是否应该寻找新的原生可观测量/关系，还是明确承认一族 admissible dynamics，而不是人为指定一个经典模型。

## Success, kill, and return criteria

合法终态仅允许：
`NO_CANONICAL_MINIMAL_ROTATION_EXTENSION_CLAUSE_ON_DECLARED_LANGUAGE`、
`UNIQUE_MINIMAL_NONCIRCULAR_ROTATION_EXTENSION_PRINCIPLE_ISOLATED_WITHOUT_P000_PROMOTION`、
`DECLARED_EXTENSION_CLAUSE_LANGUAGE_TOO_WEAK_OR_CIRCULAR`。

找到两条互不蕴含的最小非循环 discriminator 后立即冻结 noncanonicity；找到唯一原则也只冻结为 extension candidate，不授予 P000/Working Truth/Foundation/L4；若所有有效 discriminator 都循环地编码目标模型，立即冻结 circularity。不得在本任务内把任何候选条款写成新的 P000 公理。
