<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RSA-EXPONENT-COLLISION-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT",
  "title": "RSA Exponent-Collision External Prior-Art and Duplication Audit",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The accepted RSA exponent-collision result cleanly overlaps the classical Miller/Rabin known-annihilating-exponent route for global exponent-map collisions, but the exact prior-art status of the local iff 2-depth criterion, its closed random-unit probability, and the multi-certificate diagonal-graph obstruction has not yet been exhaustively classified.",
  "next_action": "Search primary and high-quality secondary literature for exact or equivalent formulations of the local collision-depth criterion, its probability law, and the subgroup/graph obstruction; classify each match as exact duplicate, partial antecedent, adjacent method, or no material match, without turning absence of a match into a novelty claim.",
  "dependencies": [
    "research_result_records/RS-RSA-EXPONENT-COLLISION-CRT-COLLAPSE/RR-2D43CCB30B906AFB6E20.json",
    "research_returns/RSA_EXPONENT_COLLISION_CRT_COLLAPSE_RETURN_20260827.md"
  ],
  "source_refs": [
    "Gary L. Miller, Riemann's hypothesis and tests for primality, JCSS 13 (1976), DOI 10.1016/S0022-0000(76)80043-8",
    "Menezes–van Oorschot–Vanstone, Handbook of Applied Cryptography, §8.2 Fact 8.6"
  ],
  "evidence_status": "DRIVER_ACCEPTED_MATHEMATICS / CLASSICAL_GLOBAL_ROUTE_IDENTIFIED / EXACT_LOCAL_AND_MULTI_CERTIFICATE_DUPLICATION_STATUS_OPEN",
  "last_progress_ref": "main@628aad28918a8fcf1937713299405c2efb54f5f1",
  "last_progress_at": "2026-08-28T08:02:30+00:00",
  "hard_block": null,
  "tags": [
    "RSA",
    "exponent-collision",
    "prior-art",
    "duplication-audit",
    "Miller-Rabin",
    "Carmichael",
    "CRT",
    "2-adic-collapse"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RSA-EXPONENT-COLLISION-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT",
  "parent_objective_id": "RSA_COLLISION_COLLAPSE_PRACTICE_20260827",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RSAPA",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-RSA-EXPONENT-COLLISION-CRT-COLLAPSE",
  "successor_gate": {
    "new_information_gap": "The source result proves the mathematics but does not exhaustively establish whether its exact local iff criterion, probability formula, or multi-certificate diagonal-graph characterization already appears in the literature.",
    "why_parent_result_does_not_close_it": "Mathematical correctness and prior-art duplication are distinct questions. The result itself deliberately makes no novelty claim and only identifies the classical global-annihilator overlap.",
    "discriminating_outcomes": [
      "An exact equivalent prior theorem is located and the corresponding source claim is classified as duplicate.",
      "Only partial antecedents are located, isolating which sharpenings are genuinely beyond the cited classical reduction without asserting novelty.",
      "No material match is found after a reproducible search; the output records only a bounded no-match audit, not a novelty theorem."
    ],
    "kill_condition": "Kill any route that drifts into generating collisions, improving RSA factorization complexity, or inferring novelty from a negative search. This task is evidence classification only.",
    "alternative_route_or_free_exploration_considered": "Immediate closure was considered, but the accepted-result control gate requires explicit prior-art/duplication classification before the parent line can close cleanly. A new mathematical continuation is not justified because the hard target has no unresolved mathematical residue.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "A separate audit preserves the accepted proof unchanged while isolating literature provenance and duplicate detection from mathematics, preventing both overclaiming and unnecessary re-opening of the completed extraction theorem."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78ae73bf9790b5afb87d2cfe01f8ca4549bf4a658547e1a9030374221a7ec74",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# RSA Exponent-Collision External Prior-Art and Duplication Audit

Status: `PUBLISHED_REGISTERED / CONTINUATION / EXTERNAL_PRIOR_ART_DUPLICATION_AUDIT`

## Mother question

Which parts of `RR-2D43CCB30B906AFB6E20` are exact restatements of established RSA/Miller–Rabin order-to-factor theory, and do the following stronger-looking formulations already have exact or equivalent antecedents: (i) local collision collapse succeeds iff the two CRT order components have unequal 2-adic depths, (ii) the closed random-unit failure law in terms of `v2(p-1), v2(q-1)`, and (iii) the multi-certificate failure barrier as a graph of an isomorphism between local cyclic 2-primary projections?

## Frozen inputs and scope

Treat the accepted source result as the mathematical object to classify, not as a novelty premise. The classical global statement that a known nonzero multiple of `lambda(n)` enables Miller-style randomized factor extraction is already expected to be prior art and must not be presented as new.

Search primary literature and high-quality cryptography/number-theory references using task-specific terminology around RSA key recovery, known multiples of `phi(n)` or `lambda(n)`, nontrivial square roots of one, strong probable-prime witnesses, local order 2-adic valuations, and multi-base/subgroup variants. Record search date, surfaces, exact queries, candidate matches, and why each candidate is or is not equivalent.

Do not perform new collision-generation research and do not weaken or strengthen the accepted theorem.

## Hard target and required outputs

Hard target:

`RSA_EXPONENT_COLLISION_PRIOR_ART_DUPLICATION_CLASSIFIED`

Required outputs:

1. classify the global exponent-map collision consequence against Miller 1976 and standard RSA key-recovery references;
2. search for exact/equivalent prior statements of the single-local-collision iff depth criterion;
3. search for the closed random-unit probability formula and distinguish it from the coarser classical `>=1/2` success bound;
4. search for multi-certificate lcm/subgroup aggregation and the diagonal-graph obstruction;
5. return a table of `EXACT_DUPLICATE / PARTIAL_ANTECEDENT / ADJACENT_METHOD / NO_MATERIAL_MATCH`;
6. state explicitly that a bounded no-match search is not proof of novelty.

## Research value to preserve

The mathematical task is complete, but its interpretation matters. Separating classical Miller/Rabin content from any sharper local or subgroup formulation prevents false novelty claims while preserving potentially useful exact structure for future work.

## Success, kill, and return criteria

Success is a reproducible source-backed duplication classification for each of the three layers: global annihilating exponent, single local collision, and multi-certificate aggregation/barrier.

Kill any attempt to turn this audit into an efficient collision-generation claim, a new factoring-complexity claim, or a novelty claim based solely on failure to find a source.

Return with the strongest bounded provenance classification and close the audit even if the answer is simply that the global layer is classical while the exact local/multi formulations remain unmatched in the searched corpus.
