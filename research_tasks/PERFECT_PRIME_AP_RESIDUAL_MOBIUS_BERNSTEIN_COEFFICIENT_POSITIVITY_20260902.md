<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-RESIDUAL-MOBIUS-BERNSTEIN-COEFFICIENT-POSITIVITY",
  "title": "Perfect Prime AP residual Möbius–Bernstein coefficient positivity",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-ap-residual-mobius-bernstein-coefficient-positivity",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "The exact AP cofactor reduction and double-endpoint transform are already accepted. The canonical flag route and the fixed t-independent <=2 block-congruence route are exactly obstructed, while the residual polynomial Bhat_m(x) has strictly positive coefficients in exact finite regressions through m<=10. The all-m coefficient sign remains open.",
  "next_action": "Freeze the accepted definition of Bhat_m(x), derive an all-m coefficient formula or recurrence, and prove every coefficient is strictly positive for every m>=2; otherwise freeze the first exact nonpositive coefficient with its m and coefficient index, without inferring a full determinant zero unless separately proved.",
  "dependencies": [
    "RR-A4EBF925BE07691C8C16",
    "RR-19DB7617DE41BD10CCF7"
  ],
  "source_refs": [
    "research_returns/PERFECT_PRIME_AP_BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_RETURN_20260901.md",
    "research_returns/PERFECT_PRIME_AP_OUTER_BLOCK_HYPERBOLIC_CONGRUENCE_RETURN_20260902.md",
    "driver_reviews/PERFECT_PRIME_AP_OUTER_BLOCK_HYPERBOLIC_CONGRUENCE_DRIVER_REVIEW_20260902.md"
  ],
  "evidence_status": "EXACT_DOUBLE_ENDPOINT_BERNSTEIN_TRANSFORM_ACCEPTED / COEFFICIENT_POSITIVITY_VERIFIED_ONLY_THROUGH_M10 / ALL_M_OPEN",
  "last_progress_ref": "research_returns/PERFECT_PRIME_AP_OUTER_BLOCK_HYPERBOLIC_CONGRUENCE_RETURN_20260902.md",
  "last_progress_at": "2026-09-02T12:34:00+00:00",
  "hard_block": null,
  "tags": [
    "Perfect-Prime",
    "AP",
    "cofactor",
    "Mobius-transform",
    "Bernstein",
    "coefficient-positivity",
    "all-m",
    "exact-arithmetic"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-RESIDUAL-MOBIUS-BERNSTEIN-COEFFICIENT-POSITIVITY",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPRMBP1",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-AP-OUTER-BLOCK-HYPERBOLIC-CONGRUENCE",
  "successor_gate": {
    "new_information_gap": "The accepted determinant-structure Results remove a fixed canonical scalar flag and a fixed t-independent small-block basis, but leave the separately derived residual polynomial Bhat_m(x) untouched. Exact finite arithmetic shows coefficient positivity only through m<=10, so an all-m coefficient theorem or exact first sign obstruction is genuinely unresolved.",
    "why_parent_result_does_not_close_it": "The block-congruence Result classifies only block-based proof mechanisms. It neither proves nor refutes any coefficient of Bhat_m(x), and it leaves the parent all-m determinant statement open.",
    "discriminating_outcomes": [
      "ALL_M_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_PROVED",
      "FIRST_EXACT_NONPOSITIVE_RESIDUAL_COEFFICIENT_CLASSIFIED",
      "EXACT_COEFFICIENT_INTERFACE_REDUCED_TO_A_NAMED_UNRESOLVED_ARITHMETIC_SUBPROBLEM"
    ],
    "kill_condition": "Freeze immediately on the first exact coefficient <=0. If an all-m strict-positivity proof is completed, bind it to the exact determinant factorization and stop. A finite extension beyond m=10 is not a terminal all-m proof.",
    "alternative_route_or_free_exploration_considered": "A structured t-dependent block congruence remains logically possible, but no concrete independent pivot law is currently frozen. The residual polynomial interface is already exact, accepted, and mathematically distinct, so it is the higher-information next test.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The block task has reached its declared negative boundary, while the parent objective remains open. A separate coefficient task isolates a distinct exact invariant with a direct implication to nonvanishing and a clean exact counterexample terminal if the sign pattern fails."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:46f9b27002cd7f8a3d64fdec95e8c4519dc99d8f003b48c21e4f94182bc98e8b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP residual Möbius–Bernstein coefficient positivity

Status: `READY / P0 / HIGH / EXACT-COEFFICIENT ROUTE`

## Mother question

Let `n=m-1`. The accepted AP cofactor reduction gives a scalar `tau_m(t)` whose nonvanishing is equivalent to the frozen outer determinant problem. At the first endpoint,

`tau_m(t)=t^n q_m(t)`,

and the accepted double-endpoint transform sets

`x=t/(1-t)`

and

`Bhat_m(x)=(1+x)^(n(2m-3)) q_m(x/(1+x))`.

The exact factorization is

`det Ltilde_x[hat(2m),hat(2m)] = x^n (1+x)^n Bhat_m(x)`.

Exact arithmetic has verified that every coefficient of `Bhat_m(x)` is strictly positive for `2<=m<=10`, but this is finite evidence only.

The task asks:

> Are all coefficients of `Bhat_m(x)` strictly positive for every `m>=2`?

If yes, prove it uniformly in `m` and connect the proof back to the accepted cofactor/nonvanishing statement. If no, freeze the first exact coefficient obstruction.

## Frozen inputs

Use without alteration:

1. the accepted AP moment matrix and canonical cofactor `tau_m(t)`;
2. the exact reduction `tau_m(t) != 0 <=> det S_m(t) != 0` for `0<t<=1`;
3. the exact endpoint order `ord_(t=0) tau_m(t)=m-1`;
4. the exact double-endpoint transform and degree formulas above;
5. the existing exact coefficient regression through `m<=10`.

The finite regression is a test oracle, not a premise for induction.

## Hard target

`OUTER_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_ALL_M_PROVED_OR_EXACTLY_OBSTRUCTED`

## Required work

### 1. Exact coefficient representation

Derive an exact expression for

`[x^k] Bhat_m(x)`

valid for general `m` and every legal coefficient index `k`.

Prioritize representations that expose sign structurally, for example finite sums of binomial/Cauchy factors, determinant/minor expansions with an explicit sign-reversing or sign-preserving involution, recurrences in `m` and `k`, or an exact combinatorial interpretation.

Every denominator used in a sign argument must have its sign proved on the full parameter range.

### 2. All-m positivity route

If claiming positivity, prove

`[x^k] Bhat_m(x) > 0`

for every `m>=2` and every coefficient index.

The proof must not rely on extrapolation from finite `m`, numerical root locations, floating-point evaluation, an assumed fixed inertia, or any determinant nonvanishing statement equivalent to the parent target.

### 3. Exact obstruction route

If any coefficient is nonpositive, freeze the smallest or first independently verified witness found:

- exact `m`;
- exact coefficient index `k`;
- exact coefficient value or reduced rational/integer numerator;
- deterministic recomputation certificate.

A nonpositive coefficient kills this positivity mechanism only. It is not by itself a zero of `det S_m(t)` or `tau_m(t)`.

### 4. Endpoint closure if positivity succeeds

Strict coefficient positivity gives `Bhat_m(x)>0` for every `x>0`, corresponding to `0<t<1`.

The return must separately handle the admissible endpoint `t=1` using an accepted exact endpoint identity or a newly proved exact endpoint argument. Do not replace endpoint proof by a limiting assertion unless continuity and the nonzero limit are established.

### 5. Structural compression

If the raw coefficient formula is too large, isolate the smallest exact auxiliary quantity whose positivity is equivalent to the coefficient theorem. A valid reduction must name the residual subproblem precisely enough that a later task does not restart the same algebra from zero.

## Forbidden route recycling

Do not use any of the following as the load-bearing all-m proof:

- the rejected canonical leading-principal-minor sign pattern;
- a fixed `t`-independent simultaneous `1x1/2x2` block basis;
- bare existential adaptive `1x1/2x2` block elimination;
- inner-block definiteness;
- generic common-measure or total-positivity arguments already shown insufficient for the AP deformation;
- bounded-`m` coefficient checks.

Do not bundle a new structured `t`-dependent block-congruence search into this task.

## Required outputs

1. Research return with one terminal typed classification.
2. Exact derivation of the coefficient representation or exact reduction.
3. Deterministic checker for every finite identity, witness, and regression used.
4. Compact certificate recording the all-m theorem interface or the first exact obstruction.
5. Fresh execution record and writer-conformant immutable Result binding all outputs.

## Legal terminal outcomes

- `ALL_M_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_PROVED`;
- `FIRST_EXACT_NONPOSITIVE_RESIDUAL_COEFFICIENT_CLASSIFIED`;
- `EXACT_COEFFICIENT_INTERFACE_REDUCED_TO_A_NAMED_UNRESOLVED_ARITHMETIC_SUBPROBLEM`.

The third outcome must be a genuine exact reduction with new information, not a restatement of coefficient positivity.

## Scope boundary

This task carries no authority to strengthen the parent theorem unless the exact implication is proved. It does not change the accepted negative boundaries for the canonical scalar flag or fixed small-block basis, and it makes no historical-priority claim.
