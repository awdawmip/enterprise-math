<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-BETA-BERNSTEIN-OSCILLATION-ORDER-MAP",
  "title": "Perfect Prime Beta–Bernstein oscillation / u-to-u^m order-map closure",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-beta-bernstein-oscillation-order-map",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Use the special u -> u^m relation between the two common-measure Bernstein systems to exclude a second fixed vector of T_m, via oscillation, variation-diminishing, interlacing or sign-change transport, or freeze the smallest exact obstruction.",
  "next_action": "Translate the quotient fixed-vector equation into a functional/Bernstein coefficient equation over the shared Beta measure; track zero/sign-change counts under the Bernstein transforms, Mobius involution and u -> u^m composition, and determine whether a nontrivial quotient fixed vector violates a strict oscillation/interlacing law.",
  "dependencies": [
    "RR-86E59AB8D7FBF3917D94",
    "DR-31F878F8AA6815962C6A"
  ],
  "source_refs": [
    "research_returns/PERFECT_PRIME_TABLE_BETA_BERNSTEIN_QUOTIENT_RESULT_REFREEZE_V2_RETURN_20260830.md@main",
    "driver_reviews/PERFECT_PRIME_BETA_BERNSTEIN_REFREEZE_DRIVER_REVIEW_20260830.md"
  ],
  "evidence_status": "ACCEPTED_BETA_BERNSTEIN_FRONTIER / ORDER_MAP_OSCILLATION_UNUSED",
  "last_progress_ref": "RR-86E59AB8D7FBF3917D94 / DR-31F878F8AA6815962C6A",
  "last_progress_at": "2026-08-30T02:52:30+00:00",
  "hard_block": "EIGENVALUE_1_EXCLUSION_FOR_Q_M",
  "tags": ["PerfectPrime","Beta-Bernstein","oscillation","variation-diminishing","u-to-u^m","Chebyshev-system","all-m"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-BETA-BERNSTEIN-OSCILLATION-ORDER-MAP",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTBBOSC",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "MATHEMATICAL_CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "successor_gate": {
    "new_information_gap": "The accepted reduction has not exploited the functional order relation u -> u^m linking the two Bernstein systems. Generic total positivity is already known insufficient, so the remaining unused information is the special composition/order structure of the common measure model.",
    "why_parent_result_does_not_close_it": "The all-m quotient fixed-point exclusion remains open and no oscillation or sign-change theorem has yet been derived for this exact operator.",
    "discriminating_outcomes": [
      "FULL: prove a strict oscillation/variation-diminishing/interlacing theorem forcing the quotient fixed-vector space to be zero for every admissible m",
      "STRICT_PARTIAL: reduce the theorem to one explicit sign-change/interlacing lemma for a named Bernstein/Chebyshev transform tied to u -> u^m",
      "OBSTRUCTION: construct an exact model satisfying the accepted TP/common-measure hypotheses where the proposed oscillation principle fails, identifying the additional structure still needed"
    ],
    "kill_condition": "Do not use generic STP as a spectral black box; do not use finite-m sign patterns as proof; do not duplicate the principal-angle lane by merely rewriting a Gram determinant. A valid result must use the u -> u^m order/composition structure or prove that this structure is insufficient.",
    "alternative_route_or_free_exploration_considered": "The sibling principal-angle lane uses Hilbert/compound geometry. This lane is intentionally coefficient/sign/zero-count based so the two methods provide genuinely independent leverage on the same exact quotient.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The repaired parent task has reached a stable exact quotient frontier. A separate immutable continuation isolates the unused oscillation mechanism and permits an independent terminal no-go without reopening the envelope task."
  }
}
-->

# Perfect Prime Beta–Bernstein oscillation / `u -> u^m` order-map closure

## Frozen frontier

Use exactly the accepted Beta–Bernstein quotient model from `RR-86E59AB8D7FBF3917D94`. The mother equation is

`det(I_(m-1)-Q_m) != 0`.

Both `Ahat` and `Bhat` arise from one Beta measure, with Bernstein coordinates linked by the nonlinear order map `u -> u^m`. This relation, not generic STP, is the object of this lane.

## Required attack

Translate a hypothetical second fixed vector into one or more of:

- a Bernstein coefficient vector and associated polynomial/function;
- a pair of common-measure moment functions before/after `u -> u^m`;
- a Chebyshev-system interpolation identity;
- a sign-variation/zero-count transport identity.

Then seek a strict contradiction using:

- variation-diminishing transforms;
- oscillatory/strictly sign-regular matrix theory only where hypotheses are actually proved for the named transform;
- interlacing of zeros or alternation;
- monotonicity/order properties induced by `u -> u^m`;
- exact endpoint multiplicity or fixed-vector sign constraints.

The lane may return a strict reduction if it produces a single explicit all-m oscillation lemma whose proof would close the parent theorem.

## Required negative controls

At minimum, explain why these are insufficient and keep them frozen as negative controls:

- arbitrary product of STP matrices;
- entrywise positivity of the quotient;
- ordinary norm contraction;
- finite-m observed sign patterns;
- the previously falsified full sign-regular shortcut.

## Exact evidence

Provide a deterministic exact checker for finite symbolic identities and regression cases. Floating numerical eigenvectors or zero plots may guide discovery but cannot be terminal evidence.

## Terminal classes

- `FULL_ORDER_MAP_OSCILLATION_CLOSURE_PROVED`
- `STRICT_OSCILLATION_LEMMA_REDUCTION_PROVED`
- `ORDER_MAP_OSCILLATION_ROUTE_OBSTRUCTED_WITH_EXACT_MODEL`
- `EXACT_COUNTEREXAMPLE_TO_PARENT_FOUND`
