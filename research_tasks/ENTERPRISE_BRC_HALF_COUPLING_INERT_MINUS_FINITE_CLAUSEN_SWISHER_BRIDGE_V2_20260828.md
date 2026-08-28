<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-FINITE-CLAUSEN-SWISHER-BRIDGE",
  "title": "Enterprise BRC Inert-Minus Finite Clausen-Swisher Bridge",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-inert-minus-finite-clausen-swisher-bridge",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "Prove, refute, duplicate, or strictly reduce the single finite Clausen-to-Swisher congruence C_p modulo p^3 that is equivalent to the remaining inert-minus target for p congruent to 17 or 23 modulo 24.",
  "next_action": "Work only on the terminating finite certificate C_p. Test exact terminating cubic, WZ, or creative-microscoping identities with explicit boundary divisibility; use Domb or CM routes only with proved finite-boundary transfer.",
  "dependencies": [
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-SECOND-ORDER-CM-JACOBI-LIFT/RR-FFAA492DFF8FEBC025B5.json@main",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_SECOND_ORDER_CM_JACOBI_LIFT_RETURN_20260828.md@main",
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_SECOND_ORDER_CM_JACOBI_LIFT/reduction_certificate_20260828.json@main",
    "driver_reviews/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_SECOND_ORDER_CM_JACOBI_LIFT_AUTHORIZED_DRIVER_REVIEW_20260828.md@main"
  ],
  "source_refs": [
    "Swisher (2015), finite supercongruence E_p == -2p (mod p^3) for primes p congruent 2 modulo 3",
    "Zhi-Wei Sun, Open Conjectures on Congruences, arXiv:0911.5665v41, Conjecture A14(ii), identification only",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_SECOND_ORDER_CM_JACOBI_LIFT_RETURN_20260828.md@main"
  ],
  "evidence_status": "AUTHORIZED_DRIVER_ACCEPTED_STRICT_EXACT_REDUCTION / SINGLE_FINITE_BRIDGE_OPEN / FULL_INERT_MINUS_TARGET_UNPROVED",
  "last_progress_ref": "RR-FFAA492DFF8FEBC025B5",
  "last_progress_at": "2026-08-28T09:11:00+00:00",
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "DRIVER_AUTO_FOLLOWUP",
    "p-adic",
    "supercongruence",
    "finite-Clausen",
    "Swisher",
    "terminating-hypergeometric",
    "WZ",
    "creative-microscoping",
    "inert-minus"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-FINITE-CLAUSEN-SWISHER-BRIDGE",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP6M",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-SECOND-ORDER-CM-JACOBI-LIFT",
  "successor_gate": {
    "new_information_gap": "The reviewed parent compresses two second-order CM/Jacobi congruences to one terminating finite certificate C_p modulo p^3; that single certificate is now the smallest exact unresolved interface.",
    "why_parent_result_does_not_close_it": "The finite Clausen collapse and Swisher congruence establish equivalence but do not prove or refute C_p uniformly. Infinite analytic identities do not control the finite boundary.",
    "discriminating_outcomes": [
      "Prove C_p congruent 0 modulo p^3 for both target classes.",
      "Prove the stronger statement for all primes p congruent 2 modulo 3.",
      "Produce and independently recompute a target-class counterexample.",
      "Match C_p to a verified prior theorem under identical hypotheses.",
      "Freeze a strictly smaller exact terminating boundary obstruction."
    ],
    "kill_condition": "Kill any target claim on an independently recomputed counterexample. Reject uncontrolled infinite-series truncation, treatment of Sun A14(ii) as proved, or larger finite scans as proof. Exact prior-theorem duplication closes rather than reopens the task.",
    "alternative_route_or_free_exploration_considered": "Closure at strict-reduction strength, continuing inside the two-scalar parent, the Domb/modular route, another portfolio route, and unrestricted hypergeometric exploration were considered. The single finite certificate is the smallest current discriminating object and remains P2 rather than automatic top priority.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent has completed its reduction mission. A separate finite-certificate task preserves closed unit-tail, valuation, deformation, and two-scalar layers while giving the new residue exact proof and kill conditions."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC Inert-Minus Finite Clausen-Swisher Bridge

Status: `PUBLISHED_REGISTERED / CONTINUATION / SINGLE FINITE CERTIFICATE`

## Mother question

For primes `p ≡ 17,23 (mod 24)`, set `M=(2p-1)/3`, define

\[
\widetilde W_p=\sum_{k=0}^{M}(6k+1)
\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3\,2^k},
\qquad
E_p=\sum_{k=0}^{M}(-1)^k(6k+1)\frac{(1/3)_k^3}{(k!)^3},
\]

and `C_p=2\widetilde W_p-E_p`. Prove, refute, duplicate, or strictly reduce

\[
C_p\equiv0\pmod{p^3}.
\]

A proof for all primes `p ≡ 2 (mod 3)` is admissible and stronger, but both target classes remain mandatory.

## Frozen inputs and scope

Freeze the reviewed parent conclusions: the finite identity `S_p=W_p`; exact equivalence of `(R0-) & (R1-)` with `W_p ≡ -p (mod p^3)` on the target classes; the valuation cutoff at `M`; and Swisher's proved `E_p ≡ -2p (mod p^3)` for primes `p ≡ 2 (mod 3)`.

Zhi-Wei Sun Conjecture A14(ii) is identification only, not theorem input. Do not reopen the accepted unit-tail cancellation, valuation-block decomposition, two-rate deformation, or two-scalar bookkeeping unless an exact contradiction is found. An infinite analytic identity is not a finite proof without explicit boundary control.

## Hard target and required outputs

Hard target: `INERT_MINUS_FINITE_CLAUSEN_SWISHER_BRIDGE_PROVED_REFUTED_DUPLICATED_OR_STRICTLY_REDUCED`.

Return exactly one strongest outcome: an exact all-prime proof on both target classes; an independently recomputed exact counterexample; a verified prior-theorem match under matching hypotheses; or a strictly smaller exact terminating certificate/obstruction. Every imported hypergeometric, WZ, p-adic, CM, finite-field, Domb, or transformation theorem must be mapped at the exact precision used. Finite computation is falsification/regression only.

## Research value to preserve

The route has successively removed already-closed lower layers and compressed the remaining inert-minus problem to one finite transformation certificate. Proving this certificate closes the current minus branch, refuting it kills the target, identifying duplication prevents repeated work, and a strict reduction is useful only if it produces a smaller exact obligation.

## Success, kill, and return criteria

Success requires a proof of `C_p ≡ 0 (mod p^3)` for both target residue classes, or a stronger uniform proof for all `p ≡ 2 (mod 3)`. Any exact target-class counterexample must be independently recomputed and terminates the claim negatively. A verified exact prior theorem closes the task as duplication. A route-specific no-go is terminal only for that route unless it yields the smallest exact surviving certificate.

Reject larger prime scans as proof, any uncontrolled infinite-series truncation, or any use of Sun A14(ii) as a proved theorem. Stop at the strongest exact statement reached and infer no physical BRC, Working Truth, Foundation, or novelty consequence.
