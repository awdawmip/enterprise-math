<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT",
  "title": "Perfect Prime AP signed-secant HCM0 Hausdorff lift",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-ap-signed-secant-hcm0-hausdorff-lift",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "The residual Mobius-Bernstein coefficient task has been reduced exactly to HCM0: strict positivity of the initial signed finite-difference row of h_(m,a)=(-1)^a q_(m,a)/binom(d,a). A stronger full shifted finite-Hausdorff complete-monotonicity pattern is exact-regression-positive only through m<=10.",
  "next_action": "Use the signed squared-secant basis formula to prove HCM0 for every m>=2 and 0<=k<=d, or freeze the first exact HCM0 counterexample/theorem-level obstruction. A positive finite-Hausdorff moment representation may be used only if proved uniformly in m.",
  "dependencies": [
    "RR-23D512CBD58341BB6BDB",
    "DR-23D512CBD58341BB6BDC",
    "DR-5D1B8E24C79A6F30B442"
  ],
  "source_refs": [
    "research_returns/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_RETURN_20260903.md",
    "driver_reviews/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_DRIVER_REVIEW_20260903.md"
  ],
  "evidence_status": "SIGNED_SECANT_BERNSTEIN_FORMULA_PROVED_ALL_M / HCM0_EXACTLY_EQUIVALENT_TO_COEFFICIENT_POSITIVITY / FULL_HCM_FINITE_ONLY_M2_TO_M10",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": "SIGNED_SECANT_HCM0_ALL_M_POSITIVITY",
  "tags": ["Perfect-Prime", "signed-secant", "Hausdorff", "finite-differences", "HCM0", "all-m"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPSSH1",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-AP-RESIDUAL-MOBIUS-BERNSTEIN-COEFFICIENT-POSITIVITY",
  "successor_gate": {
    "new_information_gap": "The parent task did not merely fail to prove coefficient positivity; it derived a new all-m signed-secant Bernstein representation and proved exact equivalence between ordinary coefficient positivity and the HCM0 initial finite-difference row. The arithmetic sign problem is now strictly smaller and typed.",
    "why_parent_result_does_not_close_it": "The Result freezes HCM0 as unresolved. Full shifted HCM is verified only for 2<=m<=10 and is explicitly not promoted, so neither coefficient positivity nor the parent determinant theorem is closed.",
    "discriminating_outcomes": [
      "HCM0 is proved for every m>=2 and all admissible k, yielding all-m strict coefficient positivity and the corresponding residual nonvanishing implication",
      "an exact m,k HCM0 counterexample is frozen, refuting coefficientwise positivity while leaving the parent determinant theorem separately open",
      "full shifted Hausdorff monotonicity fails but HCM0 survives, isolating a weaker exact invariant sufficient for the coefficient target",
      "a uniform positive measure/moment or recurrence representation is proved and rigorously shown to imply HCM0"
    ],
    "kill_condition": "Reject bounded-m tables, floating-point signs, assuming q coefficients alternate, invoking the Hausdorff moment criterion without constructing/proving the required moment sequence, continuity/fixed-inertia arguments, and revival of closed flag/block routes.",
    "alternative_route_or_free_exploration_considered": "Direct outer-determinant attacks remain logically possible, but the current Result supplies a new exact arithmetic interface with a precise necessary-and-sufficient coefficient target. Broad exploration would discard that information gain.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The coefficient task is terminal at a named unresolved subproblem. The successor changes the load-bearing object from Bhat coefficient extraction to the normalized signed-secant finite-difference sequence and explicitly distinguishes HCM0 from the stronger optional full-HCM lift."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP signed-secant HCM0 Hausdorff lift

## Mother question

Can the exact signed squared-secant representation of the Perfect Prime AP residual polynomial be used to prove, for every `m>=2`, the strict initial finite-difference inequalities

`(-1)^k Delta^k h_(m,0) > 0`

for all `0<=k<=d`, where

`h_(m,a)=(-1)^a q_(m,a)/binom(d,a)`

and `d=(m-1)(2m-3)`?

## Frozen inputs

Use unchanged the accepted all-`m` identities from `RR-23D512CBD58341BB6BDB`:

- every nonzero atomic basis meets every outer `j`-group;
- full atom minors factor into a fixed outer Vandermonde times a squared within-group secant determinant;
- every nonzero basis term contains `x^(m-1)(1+x)^(m-1)` individually;
- after endpoint division, `Bhat_m` has the signed squared-secant Bernstein expansion;
- strict coefficient positivity is exactly equivalent to HCM0.

The stronger condition

`(-1)^k Delta^k h_(m,r)>0`

for all shifted `r,k` is discovery evidence only through `m<=10`.

## Hard target

`SIGNED_SECANT_HCM0_ALL_M_PROVED_OR_EXACTLY_OBSTRUCTED`.

A positive result must prove HCM0 uniformly in `m`. Acceptable routes include:

- a positive measure/Hausdorff moment representation of `h_(m,a)` proved from the signed-secant formula;
- an exact recurrence or variation-diminishing inequality with uniform sign control;
- a sign-reversing involution or regrouping of signed secant bases producing positive HCM0 cells;
- another exact representation whose implication to HCM0 is proved.

Full shifted HCM may be proved as a stronger theorem, but it is not required. If full HCM fails, the task must continue to test the weaker HCM0 target rather than treating the stronger failure as terminal.

A valid negative result is the first exact `(m,k)` with

`(-1)^k Delta^k h_(m,0) <= 0`

or a theorem-level obstruction proving the proposed HCM0 mechanism cannot work. Failure of coefficient positivity must not be reported as a zero of the parent determinant unless such a zero is independently proved.

## Required evidence

Freeze a NEW Result-ID with:

- symbolic Return separating all-`m` proof from finite discovery;
- deterministic exact checker for every finite claim;
- exact certificate for any counterexample or moment/recurrence identity;
- execution provenance and complete Git blob SHA-1 + SHA-256 manifest.

If HCM0 is proved all-`m`, expose a minimal theorem interface suitable for immediate independent replication, adversarial stress testing, and possible Lean formalization.

## Kill rules

Reject:

- finite `m` interpolation or tables as an all-`m` proof;
- floating-point positivity;
- assuming alternating `q_(m,a)` signs;
- using a Hausdorff criterion without proving the required moments/finite differences;
- continuity or fixed-inertia reasoning that presupposes nonvanishing;
- reopening canonical flag, static bounded-block, adjacent-pair or bare adaptive-LDL routes.
