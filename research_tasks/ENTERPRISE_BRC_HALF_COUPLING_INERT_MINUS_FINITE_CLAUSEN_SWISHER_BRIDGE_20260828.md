<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-FINITE-CLAUSEN-SWISHER-BRIDGE",
  "title": "Enterprise BRC Inert-Minus Finite Clausen-Swisher Bridge",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-inert-minus-finite-clausen-swisher-bridge",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "Prove, refute, or exactly obstruct the single finite Clausen-to-Swisher transformation congruence C_p modulo p^3 that is now equivalent to the entire remaining inert-minus second-order target for p congruent to 17 or 23 modulo 24.",
  "next_action": "Freeze M=(2p-1)/3 and the two terminating weighted sums in C_p. Seek a terminating cubic transformation, WZ certificate, or creative-microscoping identity with explicit boundary divisibility modulo p^3. Use the Domb/Rogers pullback only as a structurally distinct route whose finite boundary must also be proved.",
  "dependencies": [
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-SECOND-ORDER-CM-JACOBI-LIFT/RR-FFAA492DFF8FEBC025B5.json@main",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_SECOND_ORDER_CM_JACOBI_LIFT_RETURN_20260828.md@main",
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_SECOND_ORDER_CM_JACOBI_LIFT/reduction_certificate_20260828.json@main",
    "driver_reviews/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_SECOND_ORDER_CM_JACOBI_LIFT_DRIVER_REVIEW_20260828.md@main"
  ],
  "source_refs": [
    "Swisher (2015), finite supercongruence E_p == -2p (mod p^3) for primes p congruent 2 modulo 3",
    "Zhi-Wei Sun, Open Conjectures on Congruences, arXiv:0911.5665v41, Conjecture A14(ii), identification only",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_SECOND_ORDER_CM_JACOBI_LIFT_RETURN_20260828.md@main"
  ],
  "evidence_status": "DRIVER_ACCEPTED_STRICT_EXACT_REDUCTION / SINGLE_FINITE_BRIDGE_OPEN / FULL_INERT_MINUS_TARGET_UNPROVED",
  "last_progress_ref": "RR-FFAA492DFF8FEBC025B5",
  "last_progress_at": "2026-08-28T06:44:00+00:00",
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
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
    "new_information_gap": "The parent has been strictly reduced from two second-order CM/Jacobi congruences to one explicit terminating finite certificate C_p modulo p^3. This certificate did not exist as the operative interface of the older all-inert finite-Clausen task.",
    "why_parent_result_does_not_close_it": "The exact finite Clausen collapse and the imported Swisher congruence prove equivalence of the parent target with C_p, but no all-prime proof or counterexample for C_p is supplied. The analytic infinite transformation cannot be truncated without a separately controlled finite boundary.",
    "discriminating_outcomes": [
      "Prove C_p congruent 0 modulo p^3 uniformly for p congruent 17 or 23 modulo 24, closing the remaining inert-minus target.",
      "Prove the stronger uniform statement for all primes p congruent 2 modulo 3 without weakening the target-class proof.",
      "Produce and independently recompute an exact target-class counterexample, refuting the inert-minus target.",
      "Prove an exact route-specific obstruction and freeze a strictly smaller terminating boundary or certificate.",
      "Identify a verified prior theorem that already proves the exact same finite identity under matching hypotheses, closing the task as duplication rather than reproving it."
    ],
    "kill_condition": "Any independently recomputed target-class counterexample kills the claim. Any argument that substitutes the infinite analytic identity without finite boundary control, treats Sun A14(ii) as proved, or replaces proof by a larger finite scan is rejected as non-closing. If a verified prior theorem exactly matches C_p under the required hypotheses, stop and classify duplication.",
    "alternative_route_or_free_exploration_considered": "Closure of the minus branch at strict-reduction strength, continuation inside the two-scalar parent interface, the independent Domb/modular lane, another portfolio route, and unrestricted hypergeometric exploration were considered. The explicit C_p certificate is the smallest currently discriminating object and is kept at P2 rather than automatic top priority.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task has completed its second-order reduction mission: R0-minus and R1-minus have collapsed to one self-contained finite identity. A separate task preserves that terminal parent result and prevents reopening the closed unit-tail, deformation, and two-scalar bookkeeping while giving the new finite certificate precise proof and kill conditions."
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

Let

\[
p\equiv17,23\pmod{24},
\qquad
M=\frac{2p-1}{3}.
\]

Define

\[
\widetilde W_p
=
\sum_{k=0}^{M}(6k+1)
\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3\,2^k}
\]

and

\[
E_p
=
\sum_{k=0}^{M}(-1)^k(6k+1)
\frac{(1/3)_k^3}{(k!)^3}.
\]

Set

\[
C_p=2\widetilde W_p-E_p.
\]

Prove, refute, or exactly obstruct

\[
\boxed{C_p\equiv0\pmod{p^3}}
\tag{Bridge-}
\]

uniformly for the target residue classes.

The frozen parent reduction proves that `(Bridge-)` is equivalent to the entire remaining inert-minus second-order target. A proof for all primes `p ≡ 2 (mod 3)` is admissible and stronger, but the required target is only `17,23 mod 24`.

## Frozen inputs and scope

The following parent conclusions are frozen inputs at their accepted strength:

1. the finite Clausen collapse `S_p=W_p`;
2. the equivalence `(R0-) & (R1-)` with `W_p ≡ -p (mod p^3)` on the target classes;
3. the valuation formula
   \[
   v_p\!\left(\binom{2n}{n}^2\binom{3n}{n}\right)
   =
   \left\lfloor\frac{2n}{p}\right\rfloor+
   \left\lfloor\frac{3n}{p}\right\rfloor;
   \]
4. the consequent truncation at `M=(2p-1)/3` modulo `p^3`;
5. Swisher's proved finite congruence
   \[
   E_p\equiv-2p\pmod{p^3}
   \]
   for primes `p ≡ 2 (mod 3)`.

Zhi-Wei Sun Conjecture A14(ii) is a prior-conjecture identification only and is not a theorem input.

Do not reopen the already accepted unit-tail mod-`p` cancellation, valuation-block decomposition, two-rate deformation, or `(R0-),(R1-)` bookkeeping unless an exact contradiction is found.

The ordinary infinite Ramanujan/Clausen transformation is not a valid finite proof by truncation. Any terminating transformation must account explicitly for the boundary or tail modulo `p^3`.

## Proof lanes

The primary lane is a terminating cubic transformation, WZ certificate, or creative-microscoping identity that directly produces `(Bridge-)` with boundary terms of proved p-adic order at least three.

A structurally distinct lane may use the Rogers/Domb pullback or a finite-field/CM transformation, but only if its finite truncation boundary is proved at the required precision.

Existing mathematics and exact transformations should be reused before introducing a new general-purpose mechanism.

## Hard target and required outputs

Hard target:

`INERT_MINUS_FINITE_CLAUSEN_SWISHER_BRIDGE_PROVED_REFUTED_DUPLICATED_OR_STRICTLY_REDUCED`.

Required outputs:

1. an all-prime proof on `p ≡ 17,23 (mod 24)`, an exact counterexample, a verified exact prior-theorem match, or a strictly smaller exact certificate;
2. exact finite-boundary control modulo `p^3`;
3. explicit statement of whether the argument covers only the target classes or all `p ≡ 2 (mod 3)`;
4. complete dependency mapping for every imported hypergeometric, WZ, p-adic, CM, finite-field, or Domb identity used;
5. if a WZ or terminating-deformation route is used, the exact certificate and boundary valuations;
6. if a Domb/Rogers or analytic pullback is used, an exact finite truncation transfer rather than an infinite-value analogy;
7. deterministic finite checking only as falsification/regression support;
8. a durable return that freezes the smallest remaining identity if the full bridge is not closed.

## Research value

This task is intentionally narrower than the old all-inert finite-Clausen bridge and the immediately preceding second-order CM/Jacobi task. The route has successively removed the split classes, closed the minus unit-tail cancellation layer, compressed the second-order interface to two scalar congruences, and now compressed those two congruences to one finite transformation certificate.

Closing `C_p` closes the remaining inert-minus branch at the current exact interface. Refuting it refutes the target. Finding an exact prior theorem prevents duplicated research. A strict obstruction is useful only if it leaves an even smaller certificate rather than reopening earlier layers.

## Success, kill, and return criteria

A proof of `(Bridge-)` on both target residue classes is success. A proof on all `p ≡ 2 (mod 3)` is accepted as a stronger uniform closure.

Any exact target-class counterexample must be independently recomputed and then terminates the claim negatively.

If a verified prior theorem proves exactly the same finite identity under the required hypotheses, return duplication with exact citation and theorem matching.

A route-specific no-go is terminal only for that route unless it also proves impossibility of every permitted finite mechanism. A larger prime scan or an uncontrolled infinite-series truncation is not progress toward proof.

Stop at the strongest exact statement reached. Do not infer physical BRC semantics, Working Truth, or Foundation consequences from this arithmetic task.
