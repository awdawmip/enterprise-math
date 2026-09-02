<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-OUTER-BLOCK-HYPERBOLIC-CONGRUENCE",
  "title": "Perfect Prime AP outer block-hyperbolic congruence invariant",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-ap-outer-block-hyperbolic-congruence",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "The exact m=15,t=4/5 witness refutes a universal fixed-sign canonical leading-minor flag, while the full outer determinant stays nonzero and the 12th/13th one-by-one LDL pivots exchange signs as an adjacent pair without changing the 7+/7- inertia. The unresolved question is whether a noncanonical congruence or mixed 1x1/2x2 block structure controls the full determinant for all m and 0<t<=1.",
  "next_action": "Freeze the exact outer matrix S_m(t) and search for a symbolic noncanonical congruence or symmetric-indefinite block LDL/hyperbolic-pair factorization with blocks of size at most two whose block determinants and signatures are controlled for all m and 0<t<=1; otherwise freeze an exact obstruction that rules out this block mechanism without weakening the parent determinant target.",
  "dependencies": [
    "RR-F5AB0AF5F544393896D9"
  ],
  "source_refs": [
    "research_returns/PERFECT_PRIME_AP_OUTER_CONDITIONAL_COVARIANCE_DETERMINANT_RETURN_20260901.md",
    "driver_reviews/PERFECT_PRIME_AP_OUTER_CONDITIONAL_COVARIANCE_DETERMINANT_DRIVER_REVIEW_20260902.md",
    "research_artifacts/PERFECT_PRIME_AP_OUTER_CONDITIONAL_COVARIANCE_DETERMINANT/flag_obstruction_certificate_20260901.json"
  ],
  "evidence_status": "CANONICAL_1X1_FLAG_REFUTED / FULL_DETERMINANT_NONVANISHING_OPEN / ADJACENT_PIVOT_PAIR_EXCHANGE_EXACT",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": "NONCANONICAL_BLOCK_CONGRUENCE_OR_RESIDUAL_BERNSTEIN_CLOSURE",
  "tags": [
    "Perfect-Prime",
    "outer-determinant",
    "block-LDL",
    "hyperbolic-pair",
    "congruence",
    "all-m"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-OUTER-BLOCK-HYPERBOLIC-CONGRUENCE",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPOBHC1",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-AP-OUTER-CONDITIONAL-COVARIANCE-DETERMINANT",
  "successor_gate": {
    "new_information_gap": "The accepted witness kills the fixed canonical one-by-one flag but reveals an adjacent two-pivot sign exchange with unchanged total signature and nonzero full determinant. It is unknown whether this pair exchange is governed by a uniform noncanonical 1x1/2x2 block congruence for the exact AP outer matrix.",
    "why_parent_result_does_not_close_it": "The negative boundary proves only that every canonical leading principal minor cannot carry one universal sign pattern. It neither proves nor refutes existence of an all-m noncanonical block factorization whose block determinants exclude singularity.",
    "discriminating_outcomes": [
      "an exact all-m all-parameter congruence or mixed 1x1/2x2 block factorization proves det S_m(t) nonzero",
      "an exact symbolic obstruction or finite exact witness rules out the proposed uniform block-hyperbolic mechanism while preserving the parent determinant question",
      "a proved reduction shows that any viable block theorem is equivalent to a sharper explicitly stated residual invariant"
    ],
    "kill_condition": "Reject any argument that assumes fixed inertia by continuity, reinstates the disproved canonical leading-minor sign pattern, treats bounded-m checks as an all-m proof, or reopens inner-block definiteness, factorwise total positivity, generic common-measure, or generic order-map mechanisms.",
    "alternative_route_or_free_exploration_considered": "Closing the parent Objective is invalid because the full determinant question remains undecided. The all-m residual Bernstein/Mobius route remains a separate viable fallback; the block route is selected first because the exact obstruction exhibits a paired pivot exchange that a 2x2 hyperbolic block could naturally absorb.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task is terminal at a theorem-level negative boundary for its strongest tested flag mechanism. A separate task cleanly changes the load-bearing invariant from canonical 1x1 pivots to noncanonical bounded blocks without rewriting the accepted failure result."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP outer block-hyperbolic congruence invariant

Status: `READY / P0 / HIGH LEVERAGE`

## Mother question

For the exact symmetric outer matrix `S_m(t)` already frozen by the Perfect Prime AP reduction, can the all-`m`, all-`0<t<=1` determinant nonvanishing statement be proved by a **noncanonical congruence** or by a symmetric-indefinite block factorization using `1x1` and `2x2` blocks, even though the canonical one-by-one leading-minor flag is known to cross zero?

The target is the actual AP matrix. A block theorem is valuable only if it excludes singularity independently and preserves every exact equivalence back to the original critical cofactor.

## Frozen inputs and scope

Use the accepted outer-covariance reduction and the exact negative-boundary Result `RR-F5AB0AF5F544393896D9` unchanged.

In particular freeze:

- `tau_m(t)!=0 <=> det S_m(t)!=0` on the admissible interval;
- the exact formula for `S_m(t)=sum_j (-1)^j binom(m-1,j) C_j(t)`;
- positivity of every accepted denominator factor;
- indefiniteness of each inner block for `m>=3`;
- the exact witness `m=15,t=4/5`;
- the fact that the canonical order-12 leading minor crosses zero inside `(3/4,1)`;
- the exact adjacent one-by-one pivot exchange at orders 12 and 13 while the full determinant remains nonzero and the inertia remains `7+/7-`.

The failed canonical leading-minor sign theorem may be used only as a regression falsifier. It may not be restored as a premise.

## Hard target and required outputs

Hard target:

`OUTER_BINOMIAL_COVARIANCE_BLOCK_HYPERBOLIC_CONGRUENCE_NONVANISHING_PROVED_OR_EXACTLY_OBSTRUCTED`.

Produce one of the following exact outcomes.

1. **Positive block theorem.** Construct, for every `m>=2` and `0<t<=1`, an explicit congruence or symmetric block elimination of `S_m(t)` into `1x1` and `2x2` blocks with exact nonzero block determinants and controlled signatures, and prove that this structure forces `det S_m(t)!=0`.

2. **Exact block obstruction.** Prove that the proposed bounded block/hyperbolic mechanism cannot hold uniformly, by a symbolic contradiction or an exact witness that falsifies the required block invariant while carefully preserving the parent full-determinant question.

3. **Sharper reduction.** If the block structure is neither closed nor refuted but can be exactly reduced to a smaller invariant, freeze that invariant and prove the equivalence. The reduction must be strictly narrower than the current full determinant statement.

Required evidence:

- an explicit block ordering, congruence, Schur-complement, or hyperbolic-pair formula rather than a verbal inertia heuristic;
- exact treatment of odd/even matrix sizes and endpoint behavior;
- a regression check reproducing the `m=15,t=4/5` paired-pivot witness;
- deterministic exact checks for every finite witness or symbolic identity used;
- a fresh execution record and Result with complete Git-blob and SHA-256 bindings.

## Research value to preserve

The exact witness shows that the old one-by-one flag was too rigid, not that determinant nonvanishing is false. The adjacent pivot exchange suggests that two-dimensional indefinite blocks may carry the invariant that scalar pivots cannot.

A positive block theorem would solve the current all-`m` determinant bottleneck without relying on circular continuity arguments. A negative block theorem would eliminate another sharply defined mechanism and leave the residual Bernstein/Mobius interface as a genuinely different route rather than mixing multiple failed ideas.

## Success, kill, and return criteria

Success is an exact all-`m`, all-parameter proof of full determinant nonvanishing through the declared block/congruence structure, with the implication to the original critical cofactor stated explicitly.

A valid negative return is a theorem-level obstruction or exact witness that refutes the declared uniform block mechanism and identifies what invariant remains undecided.

Kill and reject:

- continuity plus endpoint inertia as proof of nonvanishing;
- any assumption that all canonical leading principal minors keep fixed signs;
- finite-`m` verification presented as an all-`m` theorem;
- reintroduction of inner-block definiteness;
- reopening factorwise total-positivity, generic common-measure, or generic order-map routes already classified as insufficient;
- silently changing the AP weights, basis-level matrix definition, admissible parameter interval, or critical cofactor.

If the block mechanism is exactly obstructed, return the obstruction and the narrow residue. Do not automatically append the residual Bernstein route inside this task.
