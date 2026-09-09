<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY",
  "title": "Enterprise BRC inert-plus discriminant -24 supersingular unit reciprocity",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-coupling-inert-plus-d24-supersingular-unit-reciprocity",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Prove, refute, or strictly reduce the discriminant -24 supersingular unit reciprocity UR for every prime p congruent to 13 or 19 modulo 24, starting from the Driver-accepted CM0/SIMPLE strict reduction and without reopening the eliminated finite-tail or harmonic-block interface.",
  "next_action": "Consume the successor handoff and accepted parent Result/Review. First verify the new quadratic-transform bridge from UR to (L_p(u)/p)L_p'(u)=2t/3 mod p and independently validate or reject the ordinary-Legendre candidate (P_{2n}(t)+2P_n(t))P_n'(t)=-pt mod p^2. Then attack the surviving unit reciprocity using the generalized-Legendre p-adic recurrence at a=-1/3 together with t<->-t Frobenius/parity elimination, or a structurally distinct supersingular Frobenius/Wronskian route.",
  "dependencies": [
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/RR-82F6383FB6634F72B457.json@main",
    "research_result_reviews/RR-82F6383FB6634F72B457/DR-2EA60F5817976E662FA6.json@main"
  ],
  "source_refs": [
    "research_notes/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_D24_UR_SUCCESSOR_HANDOFF_20260909.md",
    "research_task_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/TP2-A19C97A703AF47D1CBEC.json",
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/RR-82F6383FB6634F72B457.json",
    "research_result_reviews/RR-82F6383FB6634F72B457/DR-2EA60F5817976E662FA6.json",
    "driver_reviews/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_DRIVER_REVIEW_20260908.md",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md",
    "scripts/check_enterprise_brc_half_coupling_inert_plus_terminating_jacobi_jet_certificate_independent.py"
  ],
  "evidence_status": "PARENT_ACCEPTED_STRICT_REDUCTION / CM0_SIMPLE_PROVED / UR_OPEN / LIFT_DEFERRED_UNTIL_UR",
  "last_progress_ref": "DR-2EA60F5817976E662FA6",
  "last_progress_at": "2026-09-08T14:03:30+00:00",
  "hard_block": "UR_SUPERSINGULAR_UNIT_RECIPROCITY_OPEN",
  "tags": [
    "p-adic",
    "hypergeometric",
    "Legendre",
    "CM",
    "supersingular",
    "D-24",
    "unit-reciprocity",
    "Frobenius",
    "BRC"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP6UR",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE",
  "successor_gate": {
    "new_information_gap": "The accepted parent proves the discriminant -24 Hasse zero and its simplicity and reduces JT0 exactly to UR, but it does not determine the remaining nonzero p-adic unit relating the divided period G_p=g/p to the transverse Hasse derivative.",
    "why_parent_result_does_not_close_it": "CM0 and SIMPLE determine the zero locus and prove the derivative is a unit; they do not evaluate that unit or the first divided p-adic period. The 77-prime regression is finite evidence only.",
    "discriminating_outcomes": [
      "Prove UR uniformly for both p mod 24 residue classes, thereby proving JT0 at the accepted parent interface.",
      "Produce one exact independently recomputed counterexample to UR, refuting JT0 and the inherited plus branch.",
      "Prove the new quadratic/ordinary-Legendre equivalence and reduce UR to a genuinely smaller all-prime finite-field or p-adic identity.",
      "Prove a precise no-go for one proposed recurrence/Frobenius mechanism while freezing a strictly smaller surviving certificate."
    ],
    "kill_condition": "A verified all-prime proof or an exact independently recomputed counterexample terminates UR. A finite prime scan, an assumed Sun A14(ii) statement, a split ordinary-CM formula on this inert lane, or a return to the eliminated harmonic/tail bookkeeping is non-closing.",
    "alternative_route_or_free_exploration_considered": "The parent task has already been terminally accepted at strict-reduction scope. Launching LIFT immediately, reopening the broad supercongruence, handing the work to a fresh unrestricted route, and stopping after the accepted reduction were considered. UR is the uniquely smaller first-digit residue explicitly selected by the accepted Driver review; LIFT is deferred until UR closes.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task is terminal and must not be redispatched. UR removes the already-proved CM zero/simple-root layer and isolates a single scalar unit identity with a new Legendre/Frobenius proof interface, so a separate continuation preserves the accepted reduction rather than replaying completed work."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC inert-plus discriminant -24 supersingular unit reciprocity

Status: `READY / P1 / HIGH / CONTINUATION / PUBLISHED_REGISTERED`

## Mother question

For every prime
\[
p\equiv13,19\pmod{24},\qquad m=\frac{p-1}{6},
\]
prove, refute, or strictly reduce the single first-digit unit reciprocity
\[
\boxed{G_p\bigl(-6Q_m'(1/2)\bigr)\equiv1\pmod p,}
\tag{UR}
\]
where the accepted parent Result defines \(G_p=g/p\) and \(P_{2m}(T)=Q_m(T^2)\).

The parent has already proved \(Q_m(1/2)=0\pmod p\) and \(Q_m'(1/2)\ne0\pmod p\), and has proved that `(UR)` is exactly equivalent to `(JT0)`. Those completed steps are frozen inputs, not subproblems of this task.

## Frozen inputs and scope

Freeze the accepted parent Result `RR-82F6383FB6634F72B457` and Driver Review `DR-2EA60F5817976E662FA6`. In particular, preserve the terminating Legendre transport, the discriminant \(-24\) Hesse/CM supersingular zero, the simple-root argument, and the scalar reconstruction
\[
G_p=\frac{g}{p},\qquad
g=\sum_{k=0}^{p-1}B_k,\qquad
\frac{B_{k+1}}{B_k}=
\frac{(6k+1)(3k+1)}{36(k+1)^2}.
\]

Do not reopen the eliminated Clausen-tail, finite-tail valuation blocks, or separate harmonic arrays unless an exact contradiction to the accepted parent reduction is produced. Treat Zhi-Wei Sun A14(ii) as conjectural background only.

The successor handoff records a new quadratic-extension reduction candidate. Let \(t^2=1/2\), \(u=(1-t)/2\), and
\[
L_p(u)=\sum_{k=0}^{p-1}
\frac{(1/3)_k(2/3)_k}{(k!)^2}u^k .
\]
A first required substep is to verify from the terminating quadratic transformation, at the needed precision, the proposed equivalent form
\[
\boxed{\frac{L_p(u)}{p}L_p'(u)\equiv\frac{2t}{3}\pmod p.}
\tag{UR-L}
\]
The same handoff isolates the ordinary-Legendre candidate, with \(n=(p-1)/3\),
\[
\boxed{\bigl(P_{2n}(t)+2P_n(t)\bigr)P_n'(t)\equiv-pt\pmod{p^2}.}
\tag{UR-LEG}
\]
`(UR-LEG)` is a task-local candidate exact reduction until its equivalence is independently derived; it is not an inherited theorem.

BRC typing is valuation/jet/provenance sensitive here. Retain the term index, \(p\)-adic precision, derivative data and the two Frobenius-conjugate ports \(t\leftrightarrow-t\); a positive total-mass summary is not an adequate carrier for the required cancellation.

## Hard target and required outputs

Hard target: `D24_SUPERSINGULAR_UNIT_RECIPROCITY_PROVED_REFUTED_OR_STRICTLY_REDUCED`.

Required outputs are: an all-prime proof, exact counterexample, or genuinely smaller exact certificate for `(UR)`; an exact disposition of `(UR-L)` and `(UR-LEG)` before either is used as an equivalence; treatment of both residue classes \(13\) and \(19\pmod{24}\); explicit control of the divided \(p\)-adic value rather than only its residue-zero Hasse factor; and a deterministic exact checker used only for regression/falsification.

Test at least two structurally distinct mechanisms unless one closes or refutes the target. The primary suggested route is the generalized-Legendre \(p\)-adic parameter recurrence at \(a=-1/3\), evaluated at the Frobenius pair \(t,-t\) with parity elimination and then differentiated. A distinct acceptable route is a supersingular Frobenius/Wronskian or Jacobi-sum argument that computes the same unit without assuming an ordinary split-CM unit-root formula.

If the full reciprocity remains open, freeze the smallest surviving identity and show exactly why it is smaller than `(UR)`.

## Research value to preserve

Closing `(UR)` proves the entire first \(p\)-adic digit `(JT0)` on the accepted inert-plus interface and removes the only first-digit obstruction before the single second-digit `LIFT` problem. Even a further exact reduction is valuable only if it preserves the already-achieved CM/simple-root compression and exposes a genuinely more elementary finite-field, Legendre, Frobenius or divided-period identity.

The continuation must also preserve the information-loss boundary established by the parent work: exact \(p\)-adic valuation and Frobenius-port data cannot be replaced by a scalar magnitude or by finite numerical agreement.

## Success, kill, and return criteria

Success is a uniform proof of `(UR)` for all target primes, with the sign and normalization derived rather than fitted. A single exact independently recomputed counterexample is a valid negative terminal result. A valid strict reduction must prove equivalence to an object with fewer live parameters or lower \(p\)-adic/derivative complexity and must not merely rename the parent certificate.

Finite regression, an unproved character sign, Sun A14(ii), or the ordinary split-CM ASD theorem on an inert prime does not close this task. If a proposed route fails structurally, record the precise hypothesis mismatch and continue only with the smallest surviving route.

The second-digit `LIFT` is outside this task's hard target. Preserve any useful \(p^3\) quadratic-transform defect information for the deferred successor, but do not claim `LIFT`, `(JT2)`, or the inherited supercongruence from a proof of `(UR)` alone.
