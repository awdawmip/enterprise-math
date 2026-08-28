<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-SECOND-ORDER-CM-JACOBI-LIFT",
  "title": "Enterprise BRC Inert-Minus Second-Order CM/Jacobi Lift",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-inert-minus-second-order-cm-jacobi-lift",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Prove, refute, or strictly reduce the two exact second-order congruences R0-minus and R1-minus for inert-minus primes p congruent to 17 or 23 modulo 24, preserving the proved unit-tail mod-p cancellation and exact two-rate deformation.",
  "next_action": "Start from the frozen g0, g1, tau0, tau1, J0, and J1 interface. Seek a p-squared CM or Jacobi lift of the reverse-tail factorization and an exact first-digit evaluation. Test a terminating deformation or WZ route and a structurally distinct CM, Frobenius, or Jacobi-sum route unless one closes or refutes the target.",
  "dependencies": [
    "driver_reviews/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_UNIT_TAIL_BLOCK_CANCELLATION_BRIDGE_DRIVER_REVIEW_20260828.md@main",
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-UNIT-TAIL-BLOCK-CANCELLATION-BRIDGE/RR-ED9623B2B5753F6E6464.json@main",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_UNIT_TAIL_BLOCK_CANCELLATION_BRIDGE_RETURN_20260827.md@main"
  ],
  "source_refs": [
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_UNIT_TAIL_BLOCK_CANCELLATION_BRIDGE/reduction_certificate_20260827.json@main",
    "Zhi-Hong Sun, Congruences involving binom(2k,k)^2 binom(3k,k), arXiv:1104.2789v3, Theorem 4.5"
  ],
  "evidence_status": "DRIVER_ACCEPTED_MOD_P_CANCELLATION / EXACT_R0_MINUS_R1_MINUS_INTERFACE_OPEN / FULL_MINUS_TARGET_UNPROVED",
  "last_progress_ref": "RR-ED9623B2B5753F6E6464",
  "last_progress_at": "2026-08-28T04:35:00+00:00",
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "DRIVER_AUTO_FOLLOWUP",
    "p-adic",
    "inert-minus",
    "CM",
    "Jacobi",
    "Frobenius",
    "WZ",
    "second-order-lift"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-SECOND-ORDER-CM-JACOBI-LIFT",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP5M2",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-UNIT-TAIL-BLOCK-CANCELLATION-BRIDGE",
  "successor_gate": {
    "new_information_gap": "The reviewed result proves all four parent block divisibilities, closes unit-tail cancellation modulo p, and reduces the full minus target exactly to R0-minus and R1-minus, but neither second-order congruence is proved or refuted uniformly.",
    "why_parent_result_does_not_close_it": "The imported CM vanishing theorem supplies only the zero-order mod-p factor. The required p-squared lift and the first p-adic digits of the deformed middle and high blocks remain outside its precision.",
    "discriminating_outcomes": [
      "Prove R0-minus and R1-minus uniformly for both inert-minus residue classes, closing the minus branch.",
      "Prove R0-minus and isolate one strictly smaller exact second-digit CM or Jacobi certificate.",
      "Produce an exact counterexample and independently recompute it, refuting the corresponding minus target.",
      "Prove a route-specific no-go and freeze the smallest surviving Frobenius, Jacobi-sum, or terminating WZ identity."
    ],
    "kill_condition": "Any independently recomputed exact counterexample kills the corresponding identity. A larger prime scan, use of the mod-p CM theorem as if it supplied a p-squared lift, or reopening the proved unit-tail and valuation bookkeeping is non-closing.",
    "alternative_route_or_free_exploration_considered": "Closing the minus route at the proved mod-p cancellation boundary, assigning a new owner to the broad weighted supercongruence, and returning to unrestricted hypergeometric exploration were considered. The two-scalar second-order interface is strictly smaller and directly discriminates the remaining obstruction.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task is terminal at cancellation and exact-reduction scope. The successor has a new second-order proof interface and must preserve the completed unit-tail layer rather than repeat it."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC Inert-Minus Second-Order CM/Jacobi Lift

Status: `PUBLISHED_REGISTERED / CONTINUATION / EXACT SECOND-ORDER GATE`

## Mother question

For every prime

\[
p\equiv17,23\pmod{24},
\]

prove, refute, or strictly reduce the two exact congruences

\[
g_0J_0-\tau_0\equiv-1\pmod p,
\tag{R0-}
\]

and

\[
\frac{g_0J_0-\tau_0+1}{p}
+g_0J_1+g_1J_0-\tau_1
\equiv0\pmod p.
\tag{R1-}
\]

Together these are exactly equivalent, under the frozen predecessor reductions, to the inert-minus derivative-weighted target modulo \(p^3\).

## Frozen inputs and scope

Freeze the proved divisibilities

\[
p\mid T_{00},\quad p\mid T_{01},\quad
p^2\mid T_{02},\quad p^2\mid T_{11},
\]

the proved congruence \(p\mid G_p\), the reverse-tail factorization, and the exact two-rate deformation defining \(g_0,g_1,\tau_0,\tau_1,J_0,J_1\).

Do not reopen the unit-tail mod-\(p\) cancellation, the valuation-block support, or the already-eliminated finite-tail bookkeeping unless an exact contradiction to the accepted proof is found.

The cited CM/Legendre theorem is an admissible zero-order input only at its proved precision. The task must derive the second-order lift rather than assume it. Both residue classes are mandatory. Finite computation is falsification and identity-regression evidence only.

## Hard target and required outputs

Hard target:

`INERT_MINUS_R0_R1_SECOND_ORDER_CM_JACOBI_LIFT_PROVED_REFUTED_OR_STRICTLY_REDUCED`.

Required outputs:

1. a uniform proof, exact counterexample, or strictly smaller exact certificate for `(R0-)` and `(R1-)`;
2. exact separation of the zero-order CM factor from every first and second p-adic correction;
3. a terminating derivation controlling the middle and high deformation blocks at the required precision;
4. explicit treatment of both residue classes `17` and `23 mod 24`;
5. at least two structurally distinct proof mechanisms seriously tested unless one closes or refutes the target;
6. exact dependency mapping for WZ, creative microscoping, Jacobi, Frobenius, finite-field, or p-adic inputs;
7. a deterministic checker used only as regression support;
8. a durable task return and exact smallest residue if the full lift remains open.

## Research value to preserve

The previous task has already solved the surprising valuation-zero unit-tail cancellation modulo \(p\). The remaining problem is genuinely second-order. Preserving that separation prevents repeated work and focuses the minus branch on the first p-adic lift of a CM/Jacobi factorization.

A proof closes the minus half; a counterexample refutes it exactly; and a stricter reduction can identify the precise Frobenius or terminating identity absent from the current literature-facing interface.

## Success, kill, and return criteria

Success is an all-prime proof of both `(R0-)` and `(R1-)` with the minus sign derived. A valid partial result may prove `(R0-)` and isolate a strictly smaller second-digit identity whose equivalence is established exactly.

One independently recomputed exact counterexample terminates the corresponding claim negatively. A route-specific no-go is valuable only when it precisely eliminates a mechanism and leaves a smaller live target.

Kill any route whose main output is a larger finite scan, an assumed p-squared CM lift, an infinite-series identity lacking finite truncation control, or a return to the proved unit-tail and valuation-block formulation. Stop at the strongest exact result and do not promote it into BRC physics or Foundation semantics.
