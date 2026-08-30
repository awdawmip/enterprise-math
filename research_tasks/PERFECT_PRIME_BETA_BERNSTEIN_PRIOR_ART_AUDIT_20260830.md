<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-BETA-BERNSTEIN-PRIOR-ART-AUDIT",
  "title": "Perfect Prime Beta–Bernstein Möbius quotient external prior-art / duplication audit",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-beta-bernstein-prior-art-audit",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine whether the exact common-measure Beta–Bernstein / binomial-Möbius quotient eigenvalue-1 exclusion already follows from known total positivity, Bernstein-basis, oscillatory-matrix, composition-operator or principal-angle literature, and classify exact duplication versus partial antecedents.",
  "next_action": "Search independent external literature and repositories with the exact operator ingredients: Beta/Bernstein moment matrices from one measure, Pascal/binomial Mobius involution, u -> u^m composition, products/compressions of totally positive transforms, simplicity/exclusion of eigenvalue 1, oscillation/interlacing and principal-angle/Gram-product theorems; map every plausible result to the frozen Q_m statement hypothesis-by-hypothesis.",
  "dependencies": [
    "RR-86E59AB8D7FBF3917D94",
    "DR-31F878F8AA6815962C6A"
  ],
  "source_refs": [
    "research_returns/PERFECT_PRIME_TABLE_BETA_BERNSTEIN_QUOTIENT_RESULT_REFREEZE_V2_RETURN_20260830.md@main",
    "driver_reviews/PERFECT_PRIME_BETA_BERNSTEIN_REFREEZE_DRIVER_REVIEW_20260830.md"
  ],
  "evidence_status": "EXTERNAL_DUPLICATION_GATE_REQUIRED_BY_ACCEPTED_REVIEW",
  "last_progress_ref": "DR-31F878F8AA6815962C6A",
  "last_progress_at": "2026-08-30T02:52:30+00:00",
  "hard_block": null,
  "tags": ["PerfectPrime","prior-art","Beta-Bernstein","total-positivity","oscillatory-matrices","Pascal-Mobius","principal-angles"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-BETA-BERNSTEIN-PRIOR-ART-AUDIT",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTBBPAUD",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "EXTERNAL_PRIOR_ART_DUPLICATION",
  "parent_task_id": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "successor_gate": {
    "new_information_gap": "The exact Beta–Bernstein/Mobius quotient formulation is now stable enough for a claim-specific prior-art search, but the existing research record does not establish whether known TP/oscillation/Bernstein/composition theory already contains the needed eigenvalue-1 exclusion or a close equivalent.",
    "why_parent_result_does_not_close_it": "The accepted result is internal mathematics and finite exact regression; it does not contain an external duplication audit of the now-stable quotient formulation.",
    "discriminating_outcomes": [
      "EXACT_DUPLICATE: identify a theorem whose hypotheses map exactly to Q_m and which proves the required nonvanishing/simplicity",
      "PARTIAL_ANTECEDENT: identify one or more theorems that prove a strict sublemma or supply a missing proof interface but do not close the exact Q_m statement",
      "ADJACENT_ONLY: document nearby TP/Bernstein/oscillation theory and exact hypothesis gaps",
      "NO_MATERIAL_MATCH_FOUND: record search surfaces and queries without inferring novelty"
    ],
    "kill_condition": "Do not report generic references to total positivity or Bernstein polynomials as matches. Every candidate must be mapped to the exact common measure, Mobius involution, quotient/compression and eigenvalue-1 claim. No novelty claim is authorized from a negative search.",
    "alternative_route_or_free_exploration_considered": "Prior-art work is not a substitute for the two mathematical lanes; it runs in parallel because a precise antecedent may immediately supply the missing theorem or redirect both proof attempts.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The exact quotient statement only became stable after the accepted re-freeze, so a dedicated claim-specific search is now well-posed and is required by the post-review follow-up contract."
  }
}
-->

# Perfect Prime Beta–Bernstein Möbius quotient external prior-art / duplication audit

## Exact claim to audit

Audit the accepted all-`m` frontier

`det(I_(m-1)-Q_m) != 0`,

where `Q_m` is the quotient block of

`T_m = R Bhat R Ahat`,

`R` is the binomial/Pascal Möbius involution, and `Ahat,Bhat` are strictly totally positive Beta–Bernstein moment matrices arising from the same measure `(1-u^(m^2))^(m-1) du` with coordinates related by `u -> u^m`.

## Required external search surfaces

Search mathematically independent sources, including journal literature, monographs/preprints and relevant theorem/code repositories, around:

- total positivity and oscillatory matrices (Gantmacher–Krein, Karlin, Schoenberg and descendants);
- Bernstein bases, totally positive bases and Beta/Bernstein moment matrices;
- Pascal/binomial matrices and Möbius/involution transforms;
- products/compressions of Gram or totally positive operators;
- principal angles/canonical correlations and products of projections/Gram maps;
- variation diminishing, Chebyshev systems and zero interlacing;
- composition operators or moment transforms induced by `u -> u^m`;
- fixed-point simplicity / eigenvalue `1` exclusion for Markov-like or positive-kernel transforms where applicable.

## Mandatory return structure

For every serious candidate source record:

1. exact citation/source URL or repository ref;
2. theorem/lemma identifier;
3. hypotheses;
4. mapping to `Ahat,Bhat,R,Q_m`;
5. exact missing hypothesis or exact closure if it matches;
6. classification: `EXACT_DUPLICATE`, `PARTIAL_ANTECEDENT`, `ADJACENT_METHOD`, or `NO_MATERIAL_MATCH`.

Record search date, surfaces and queries. A no-match is not a novelty result.

## Kill conditions

Reject as insufficient:

- “STP matrices have nice spectra” without a theorem matching this product/quotient;
- generic Bernstein positivity with no fixed-point statement;
- numerical or finite-`m` studies;
- references whose hypotheses require entrywise positivity of `Q_m` (known false at `m=4`);
- references whose claimed contraction contradicts the exact row-sum counterexample.

## Terminal classes

- `EXACT_DUPLICATE_FOUND`
- `PARTIAL_ANTECEDENT_WITH_ACTIONABLE_THEOREM_FOUND`
- `ADJACENT_PRIOR_ART_ONLY`
- `NO_MATERIAL_MATCH_FOUND_WITH_AUDIT_TRAIL`
