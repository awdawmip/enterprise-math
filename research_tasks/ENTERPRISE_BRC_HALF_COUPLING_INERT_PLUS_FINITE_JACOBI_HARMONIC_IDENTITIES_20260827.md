<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-FINITE-JACOBI-HARMONIC-IDENTITIES",
  "title": "Enterprise BRC Inert-Plus Finite Jacobi–Harmonic Identities R0/R1",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-inert-plus-finite-jacobi-harmonic-identities",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "For primes p=6m+1 with p congruent to 13 or 19 modulo 24, prove, refute, or exactly obstruct the two finite identities A_m J0 congruent 1 modulo p and (A_m J0-1)/p + A_m J1 + F2 J0 congruent R_p modulo p obtained from the accepted second-order deformation reduction.",
  "next_action": "Normalize the finite sums as terminating hypergeometric/Jacobi objects and attempt a certificate for R0 first, then the p-adic first correction R1, using terminating creative microscoping or finite-field Jacobi-sum/Frobenius structure; do not reopen the finite Clausen tail or enlarge prime scans as proof.",
  "dependencies": [
    "driver_reviews/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_DRIVER_REVIEW_20260827.md@main",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md@main"
  ],
  "source_refs": [
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE/reduction_certificate_20260827.json@main",
    "Zhi-Hong Sun, Congruences involving binom(2k,k)^2 binom(3k,k), J. Number Theory 133 (2013), 1572-1595"
  ],
  "evidence_status": "PARENT_EXACT_REDUCTION_ACCEPTED / PRODUCT_TARGET_EQUIVALENT_TO_R0_AND_R1 / ALL_PRIME_IDENTITIES_OPEN",
  "last_progress_ref": "RR-810D5213FA9BCF4698C8",
  "last_progress_at": "2026-08-27T20:47:00+08:00",
  "hard_block": null,
  "tags": [
    "p-adic",
    "inert-primes",
    "Jacobi-sum",
    "harmonic-sums",
    "creative-microscoping",
    "WZ",
    "finite-hypergeometric"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-FINITE-JACOBI-HARMONIC-IDENTITIES",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP5JH",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-REFLECTED-DERIVATIVE-PRODUCT-BRIDGE",
  "successor_gate": {
    "new_information_gap": "The accepted parent has eliminated the finite tail and reduced the plus-sign product congruence exactly to two finite scalar identities R0 and R1; their all-prime proof is now the sole remaining unit.",
    "why_parent_result_does_not_close_it": "The second-order deformation proves equivalence and verifies the coefficient algebra, but supplies no all-prime terminating certificate or finite-field evaluation of R0 or R1.",
    "discriminating_outcomes": [
      "Prove R0 and R1 uniformly for both residue classes, closing the inert-plus product bridge.",
      "Prove R0 but isolate an exact obstruction or counterexample for R1.",
      "Find an exact counterexample to either identity, thereby refuting the parent plus target.",
      "Reduce R0/R1 to a strictly smaller named Jacobi-sum, Frobenius, or WZ certificate with a precise remaining hypothesis."
    ],
    "kill_condition": "One independently recomputed exact counterexample kills the corresponding all-prime identity and the plus target. A larger finite scan, an assumed Frobenius sign, or redoing finite-tail support is non-closing.",
    "alternative_route_or_free_exploration_considered": "The parent already audited p-adic Gamma/Dwork precision and direct one-term Gosper telescoping. Closing the route now, returning to broad free exploration, and assigning another owner were considered; the sharply finite R0/R1 interface is higher leverage than reopening any broader formulation.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task has reached its permitted exact-reduction terminal state. R0/R1 have a different proof interface and can be attacked without the original length-p product or tail bookkeeping, so a separate bounded continuation preserves the new information gap."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC Inert-Plus Finite Jacobi–Harmonic Identities R0/R1

Status: `PUBLISHED_REGISTERED / DRIVER CONTINUATION / EXACT FINITE IDENTITY`

## Mother question

For every prime \(p=6m+1\) with \(p\equiv13\) or \(19\pmod{24}\), decide the two finite identities

\[
A_mJ_0\equiv1\pmod p
\tag{R0}
\]

and

\[
\frac{A_mJ_0-1}{p}+A_mJ_1+F_2J_0\equiv R_p\pmod p.
\tag{R1}
\]

Here \(A_m,F_2,J_0,J_1,R_p\) are the exact finite quantities frozen by the parent second-order parameter-deformation reduction. Together, R0 and R1 are equivalent to the inert-plus product congruence through \(p^3\).

## Frozen inputs and scope

The following are frozen inputs:

- the parent finite Clausen tail identity \(T_p\equiv p^2R_p\pmod{p^3}\);
- the deformation \(b_{m,k}(\varepsilon)\) and its exact low/middle/high Taylor coefficients;
- \(G_p\equiv F_0+pF_1+p^2F_2\pmod{p^3}\);
- \(H_p\equiv J_0+pJ_1\pmod{p^2}\);
- the imported unweighted inert congruence used only to establish \(p\mid G_p\);
- the exact equivalence between the product target and R0 plus R1.

Do not reopen the finite convolution tail, the valuation-block classification, or the second-order coefficient expansion unless an exact contradiction is found. Treat the two residue classes uniformly unless a proved class-specific obstruction emerges. Finite prime checks are falsification evidence only.

## Hard target and required outputs

Hard target:

`INERT_PLUS_FINITE_JACOBI_HARMONIC_R0_R1_PROVED_REFUTED_OR_EXACTLY_OBSTRUCTED`.

Required outputs:

1. an all-prime proof or exact refutation of R0;
2. an all-prime proof or exact refutation of R1, conditional only on already frozen inputs;
3. explicit separation of any imported finite-field, Jacobi-sum, hypergeometric, WZ, or \(p\)-adic theorem and the precision it supplies;
4. exact handling of both \(m\equiv2\) and \(3\pmod4\);
5. an independent deterministic checker used only for regression;
6. a durable return that states whether the original inert-plus product bridge is proved, refuted, or remains reduced to a smaller exact certificate.

## Research value to preserve

The original length-\(p\) derivative product has been compressed to two finite, structured identities. Proving them would close the positive-sign inert half without any new tail conjecture. Refuting either would kill the target exactly. Even a further strict reduction to a standard Jacobi-sum or terminating certificate would be reusable and materially smaller than the parent problem.

## Success, kill, and return criteria

Success is a uniform theorem for R0 and R1 with the \(+\) sign derived rather than assumed. A valid partial success may prove R0 and isolate one exact remaining R1 certificate. One exact counterexample terminates the corresponding claim negatively after independent recomputation.

Do not claim completion from a bounded scan, numerical stabilization, or a mod-\(p\) statement that lacks the first correction needed for R1. Do not return to the already-closed finite-tail bookkeeping. Freeze the strongest exact theorem, counterexample, or minimal certificate and return at task scope.
