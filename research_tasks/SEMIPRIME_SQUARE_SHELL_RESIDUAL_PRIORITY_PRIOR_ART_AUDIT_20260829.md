<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SEMIPRIME-SQUARE-SHELL-RESIDUAL-PRIORITY-PRIOR-ART-AUDIT",
  "title": "半素数平方壳 residual-priority / Fermat-Lehman-Hart 外部先例审计",
  "kind": "RESEARCH",
  "owner": "audit/semiprime-square-shell-residual-priority-prior-art",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Classify external antecedents for the exact shell-to-Fermat bridge, multiplier residual ordering, modular quadratic-residue filtering and the surviving finite-window residual-priority heuristic from RR-2A424E3B8EC11DC1278C.",
  "next_action": "Search primary/authoritative literature and repositories for Fermat, Lehman, Hart/OLF and multiplier near-square ordering variants, then classify each audited claim as exact duplicate, partial antecedent, adjacent method, or no material match in the audited set.",
  "dependencies": ["research_result_records/RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION/RR-2A424E3B8EC11DC1278C.json@main"],
  "source_refs": ["driver_reviews/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_DRIVER_REVIEW_20260829.md@main"],
  "evidence_status": "DRIVER_ACCEPTED_NEGATIVE_BOUNDARY / EXTERNAL_DUPLICATION_GATE_REQUIRED",
  "hard_block": null,
  "tags": ["semiprime","prior-art","Fermat","Lehman","Hart","multiplier","residual-priority","duplication"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-SEMIPRIME-SQUARE-SHELL-RESIDUAL-PRIORITY-PRIOR-ART-AUDIT",
  "parent_objective_id": "OBJ-SEMIPRIME-SQUARE-SHELL-FACTORIZATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "SSMFPA",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION",
  "successor_gate": {
    "new_information_gap": "The parent return identifies strong similarity/equivalence to Fermat, Lehman and Hart but does not supply a claim-by-claim external duplication ledger for the exact residual-priority formulation.",
    "why_parent_result_does_not_close_it": "Internal classification is not an external prior-art audit and cannot support novelty boundaries by itself.",
    "discriminating_outcomes": ["exact duplicate", "partial antecedent", "adjacent method", "no material match in audited set"],
    "kill_condition": "Do not infer novelty from no match and do not weaken known classical attribution merely because notation differs.",
    "alternative_route_or_free_exploration_considered": "A new mathematical continuation is handled separately by the total-cost task; this task is only the duplication boundary.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Accepted-result governance requires an explicit external duplication classification before any novelty-style interpretation."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e","review_state":"PASS","temporary_overrides":[]}
}
-->

# 半素数平方壳 residual-priority / Fermat-Lehman-Hart 外部先例审计

Status: `PUBLISHED_REGISTERED / EXTERNAL_PRIOR_ART_DUPLICATION`

Hard target: `SEMIPRIME_SHELL_RESIDUAL_PRIORITY_EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED`.

Audit at least: classical Fermat difference-of-squares; multiplier Fermat; Lehman factorization; Hart one-line factorization and ordering variants; modular quadratic-residue sieves; near-square residual ranking/normalization; any literature using square-distance or shell-equivalent coordinates to prioritize multipliers.

For every candidate record bibliographic source, exact claim matched, assumptions, and one label: `EXACT_DUPLICATE`, `PARTIAL_ANTECEDENT`, `ADJACENT_METHOD`, `NO_MATERIAL_MATCH_IN_AUDITED_SET`. A no-match is not novelty. Freeze search date/surfaces/queries and evidence links in the return.