<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-RESIDUAL-BERNSTEIN-MOBIUS-ALL-M-POSITIVITY",
  "title": "Perfect Prime AP residual Bernstein-Mobius all-m positivity",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-ap-residual-bernstein-mobius-all-m-positivity",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "The canonical outer determinant remains open after exact failure of the canonical scalar flag, fixed t-independent bounded-block congruence, canonical adjacent pairing, and bare adaptive block-LDL existence as an independent invariant. The surviving independent route is the double-Cauchy-endpoint residual Bernstein/Mobius polynomial whose coefficients are exactly positive only in finite regression through m<=10.",
  "next_action": "Freeze the exact residual polynomial Bhat_m(x), derive an all-m coefficient formula or structurally equivalent positive expansion, and prove every coefficient is strictly positive for all m>=2 or freeze the first exact coefficient counterexample/theorem-level obstruction without weakening the parent determinant target.",
  "dependencies": [
    "RR-19DB7617DE41BD10CCF7",
    "DR-4B27C9136E5A08D1F624",
    "RR-A4EBF925BE07691C8C16",
    "DR-9986FE430DB065EA8EF2"
  ],
  "source_refs": [
    "research_returns/PERFECT_PRIME_AP_OUTER_BLOCK_HYPERBOLIC_CONGRUENCE_RETURN_20260902.md",
    "driver_reviews/PERFECT_PRIME_AP_OUTER_BLOCK_HYPERBOLIC_CONGRUENCE_DRIVER_REVIEW_20260902.md",
    "research_returns/PERFECT_PRIME_AP_BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_RETURN_20260901.md"
  ],
  "evidence_status": "OUTER_DETERMINANT_TARGET_OPEN / FLAG_AND_GENERIC_BLOCK_ROUTES_CLOSED / RESIDUAL_COEFFICIENTS_FINITE_POSITIVE_THROUGH_M10_ONLY",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": "RESIDUAL_BERNSTEIN_MOBIUS_ALL_M_COEFFICIENT_POSITIVITY",
  "tags": ["Perfect-Prime", "Bernstein", "Mobius", "residual-polynomial", "coefficient-positivity", "all-m"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-RESIDUAL-BERNSTEIN-MOBIUS-ALL-M-POSITIVITY",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPRBM1",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-AP-OUTER-BLOCK-HYPERBOLIC-CONGRUENCE",
  "successor_gate": {
    "new_information_gap": "Two successive structural audits have closed the canonical scalar flag and the generic bounded-block interpretations without deciding det S_m(t). The independent residual polynomial route remains untouched and has exact positive finite evidence through m=10 but no all-m coefficient theorem.",
    "why_parent_result_does_not_close_it": "The accepted block Result proves only that static simultaneous bounded blocks fail and unstructured adaptive block existence is circular. It does not address the Mobius-transformed residual polynomial or its coefficient signs.",
    "discriminating_outcomes": [
      "all coefficients of Bhat_m(x) are proved strictly positive for every m>=2, implying the canonical cofactor is nonzero on 0<t<=1",
      "an exact coefficient counterexample shows coefficientwise positivity is false while the parent determinant may remain open",
      "a theorem-level obstruction proves the current coefficient representation cannot yield uniform positivity and identifies a strictly smaller equivalent residual invariant"
    ],
    "kill_condition": "Reject bounded-m interpolation as proof, empirical coefficient positivity, any reuse of the disproved canonical flag or generic block-existence claims, and any argument that silently assumes det S_m(t) nonzero or fixed inertia.",
    "alternative_route_or_free_exploration_considered": "The parent Objective cannot close because det S_m(t) remains undecided. A third generic block-search continuation would duplicate two accepted negative boundaries. The residual Bernstein/Mobius route is the smallest genuinely different surviving interface already exposed by exact algebra.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The block task is terminal at an exact negative boundary. Switching to the separately frozen residual polynomial changes the load-bearing invariant rather than renaming another block pivot schedule."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP residual Bernstein-Mobius all-m positivity

## Mother question

Does the exact double-endpoint residual polynomial attached to the Perfect Prime AP cofactor have strictly positive coefficients for every admissible `m`, thereby proving the still-open outer determinant/cofactor nonvanishing theorem without using the failed canonical flag or generic block mechanisms?

## Frozen inputs and scope

Use the accepted AP cofactor and outer-covariance reductions unchanged. Put `n=m-1` and write

`tau_m(t)=t^n q_m(t)`

with the accepted exact degree

`deg q_m = n(2m-3)`.

Use the Mobius variable

`x=t/(1-t)`

and define the accepted residual polynomial

`Bhat_m(x)=(1+x)^(n(2m-3)) q_m(x/(1+x))`.

The accepted double-endpoint relation is

`det Ltilde_x[hat(2m),hat(2m)] = x^n (1+x)^n Bhat_m(x)`.

The exact finite checker previously found every coefficient of `Bhat_m` strictly positive for `2<=m<=10`. This is frozen only as regression/discovery evidence. No bounded census may be promoted to an all-`m` theorem.

Preserve all accepted negative controls: inner conditional-covariance blocks are indefinite for `m>=3`; canonical monomial leading-minor sign regularity fails at `m=15,t=4/5`; a fixed `t`-independent bounded-block basis already fails at `m=4`; and unstructured adaptive `1x1/2x2` block-LDL existence is equivalent to nonsingularity itself.

## Hard target and required outputs

Hard target:

`RESIDUAL_BERNSTEIN_MOBIUS_ALL_M_COEFFICIENT_POSITIVITY_PROVED_OR_EXACTLY_OBSTRUCTED`.

Primary positive target: prove for every `m>=2` that **every coefficient** of `Bhat_m(x)` is strictly positive.

A valid proof must derive a uniform symbolic coefficient formula, positive combinatorial/integral expansion, recurrence with sign control, or an equivalent exact representation whose positivity is proved uniformly in `m`. Because the leading coefficient of the Mobius transform records the `t=1` endpoint, strict positivity of all coefficients must cover the full admissible interval `0<t<=1`, not merely `0<t<1`.

A valid negative result may give an exact coefficient counterexample or a theorem-level obstruction to coefficientwise positivity. Such a negative result must state whether the parent nonvanishing theorem remains open and must not infer singularity merely from failure of coefficient positivity.

Freeze a NEW Result-ID with complete Git-blob SHA-1 plus SHA-256 bindings for the symbolic Return, deterministic exact checker for finite claims, exact certificate/artifacts, and execution provenance.

## Research value to preserve

This route is now the cleanest surviving independent interface for the Perfect Prime all-`m` objective. It avoids the circularity of fixed-inertia and adaptive-LDL arguments and is algebraically separated from the already-refuted flag/block mechanisms.

A positive all-`m` coefficient theorem would immediately imply positivity of the residual for `x>=0` and hence nonvanishing of the canonical cofactor on the full admissible interval. A negative coefficient theorem would still be valuable by closing the last currently explicit positivity mechanism and exposing the exact remaining parent obstruction.

## Success, kill, and return criteria

Success is a uniform all-`m` proof of strict coefficient positivity with the exact implication back to `tau_m(t)` and the original critical cofactor stated explicitly.

A valid negative return is an exact counterexample or theorem-level no-go for coefficientwise positivity at the declared representation strength, together with the smallest surviving residual invariant.

Kill and reject:

- finite `m` coefficient tables as proof;
- numerical floating-point sign evidence;
- continuity/fixed-inertia reasoning that assumes the desired determinant nonvanishing;
- revival of the closed canonical flag, fixed static bounded-block, canonical adjacent-pair, or bare adaptive block-existence mechanisms;
- silent weakening to one endpoint, one parity class, or bounded `m`.

If a positive all-`m` theorem is frozen, return its minimal theorem interface clearly enough for subsequent independent replication, adversarial stress testing, and possible formalization.