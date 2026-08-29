<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT",
  "title": "半素数 residual-priority / Hart streaming 全成本审计",
  "kind": "RESEARCH",
  "owner": "research/semiprime-residual-priority-hart-streaming-cost-audit",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine whether the only surviving finite-window residual-priority multiplier ordering from RR-2A424E3B8EC11DC1278C yields any factor-blind total-cost improvement over explicitly matched Hart/Fermat baselines once coverage collapse, square tests, gcds, modular sieving and preprocessing are counted.",
  "next_action": "Freeze matched streaming baselines and cost units, implement factor-blind residual-priority and Hart/Fermat orderings with the same modular sieve budget, then compare total work across stratified bit sizes and factor ratios with explicit kill conditions.",
  "dependencies": ["research_result_records/RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION/RR-2A424E3B8EC11DC1278C.json@main"],
  "source_refs": ["research_returns/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_RETURN_20260829.md@main"],
  "evidence_status": "DRIVER_ACCEPTED_NEGATIVE_BOUNDARY / ONLY_SURVIVING_COST_QUESTION",
  "hard_block": null,
  "tags": ["semiprime","factorization","Hart","Fermat","residual-priority","streaming","cost-audit","factor-blind"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT",
  "parent_objective_id": "OBJ-SEMIPRIME-SQUARE-SHELL-FACTORIZATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "SSMFCOST",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION",
  "successor_gate": {
    "new_information_gap": "The accepted parent rules out a stable static shell predictor but leaves one finite-window multiplier ordering whose total streaming cost has not been compared fairly to Hart/Fermat under the same sieve budget.",
    "why_parent_result_does_not_close_it": "RR-2A424 measures conditional rank and coverage but explicitly does not prove a total-cost or asymptotic advantage.",
    "discriminating_outcomes": ["prove a reproducible factor-blind total-cost gain in a precisely delimited regime", "classify the ordering as cost-equivalent to a known Hart/Fermat schedule", "show coverage/preprocessing/square-test cost eliminates the apparent rank gain"],
    "kill_condition": "Terminate negative if matched total work does not improve, if productive coverage collapses with bit size, or if the ordering reduces to standard Hart ordering plus ordinary modular sieving.",
    "alternative_route_or_free_exploration_considered": "Further static shell correlation and larger census were rejected by the accepted negative boundary.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is a distinct algorithmic-cost question with a binary/quantitative outcome, not another correlation scan."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e","review_state":"PASS","temporary_overrides":[]}
}
-->

# 半素数 residual-priority / Hart streaming 全成本审计

Status: `PUBLISHED_REGISTERED / DRIVER_FOLLOWUP / COST_AUDIT`

Hard target: `RESIDUAL_PRIORITY_HART_STREAMING_TOTAL_COST_CLASSIFIED`.

Use only factor-blind inputs at deployment time. Compare residual-priority, matched Hart/Fermat multiplier orderings, and identical modular-sieve budgets. Count multiplier generation, integer square roots/square tests, gcds, modular filtering, preprocessing, memory, and failures before a productive hit. Report coverage separately from conditional rank.

At minimum test 32/40/48/56/64/80/96-bit stratified semiprimes across factor-ratio bands and preserve an unseen holdout. Do not use the hidden factors to choose k or stop early except for offline labeling of the true first productive event.

Success may be positive, equivalent, or negative. No asymptotic or practical factorization claim is allowed without total-cost evidence. Freeze checker, raw/summary artifacts, Result and HANDOFF.