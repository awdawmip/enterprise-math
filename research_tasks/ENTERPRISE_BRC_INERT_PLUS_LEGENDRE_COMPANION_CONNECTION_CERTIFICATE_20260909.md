<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-INERT-PLUS-LEGENDRE-COMPANION-CONNECTION-CERTIFICATE",
  "title": "Enterprise BRC Inert-Plus Legendre Companion Connection (LC) Certificate",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-inert-plus-legendre-companion-connection",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Prove, refute, or strictly reduce the finite Legendre-companion connection LC for inert-plus primes, which is exactly equivalent to the remaining first-digit unit-reciprocity certificate UR and hence to JT0 under the frozen parent CM0/SIMPLE facts.",
  "next_action": "Start from the persisted UR-Legendre companion frontier. Expand the exact p-term deformation F_p(epsilon) at epsilon=p/6 to first p-adic order while retaining both F_p(0)/p and the resurrected post-termination tail, then identify the resulting finite scalar with -t W_{n-1}(t)/6 or isolate the smallest exact obstruction.",
  "dependencies": [
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/RR-82F6383FB6634F72B457.json@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE/ur_legendre_companion_connection_frontier_20260909.json@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f"
  ],
  "source_refs": [
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE/ur_legendre_companion_connection_frontier_20260909.json@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/RR-82F6383FB6634F72B457.json@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_task_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/TP2-A19C97A703AF47D1CBEC.json@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f"
  ],
  "evidence_status": "PARENT_STRICT_REDUCTION_DURABLE / UR_IFF_LC_EXACT_REDUCTION_PERSISTED / LC_UNPROVED",
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "p-adic",
    "inert-plus",
    "Legendre",
    "second-kind",
    "Wronskian",
    "hypergeometric",
    "unit-reciprocity",
    "finite-connection"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-INERT-PLUS-LEGENDRE-COMPANION-CONNECTION-CERTIFICATE",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP6UR",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE",
  "successor_gate": {
    "new_information_gap": "The parent task reduced JT0 to UR but did not express or prove the finite connection from the divided hypergeometric sum g/p to the Legendre second-solution companion polynomial. The persisted successor frontier proves UR is exactly equivalent to the smaller LC congruence g/p = -t W_{n-1}(t)/6 mod p.",
    "why_parent_result_does_not_close_it": "CM0 and SIMPLE determine the reciprocal target scalar but do not evaluate g/p. The parent's finite regression cannot supply the missing all-prime finite connection, and its second-digit LIFT interface is strictly larger than needed for the first digit.",
    "discriminating_outcomes": [
      "Prove LC uniformly for both target residue classes, which closes UR and JT0 under the frozen parent equivalence.",
      "Produce and independently recompute an exact counterexample to LC, which refutes UR and JT0 on the corresponding prime.",
      "Strictly reduce LC to one smaller finite telescoping, parameter-derivative, or companion-connection identity whose equivalence includes the base divided digit and resurrected tail.",
      "Prove a precise route-specific no-go that rules out a proposed finite connection mechanism without reopening the larger JT2 interface."
    ],
    "kill_condition": "Any independently recomputed exact counterexample kills LC. Any purported proof route that drops F_p(0)/p, discards the post-termination first-order tail, replaces the finite p-term object by an uncontrolled infinite derivative, or relies only on a larger finite scan is non-closing.",
    "alternative_route_or_free_exploration_considered": "Alternatives considered were leaving the parent at the conjectural UR boundary, attacking the second-digit LIFT immediately, reassigning the broad weighted supercongruence, or returning to unrestricted hypergeometric exploration. LC is smaller than UR as an executable finite identity and is a prerequisite for a clean LIFT continuation.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task is terminal at its authorized strict-reduction scope. LC introduces a new finite first-order parameter-connection interface with explicit cutoff and base-quotient guards, so a separate bounded continuation preserves completed CM0/SIMPLE/JT2-reduction work and gives a new owner a single falsifiable target."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC Inert-Plus Legendre Companion Connection (LC) Certificate

Status: `PUBLISHED_REGISTERED / CONTINUATION / SINGLE FINITE CONNECTION`

## Mother question

For every prime
\[
p\equiv13,19\pmod{24},\qquad m=\frac{p-1}{6},\qquad n=\frac{p-1}{3}=2m,
\]
let \(t^2=1/2\) and
\[
g=\sum_{k=0}^{p-1}\frac{(1/6)_k(1/3)_k}{2^k(k!)^2}.
\]
For the Legendre polynomials \(P_r\), define the finite companion
\[
W_{n-1}(t)=\sum_{j=1}^{n}\frac{P_{j-1}(t)P_{n-j}(t)}{j}.
\]
Prove, refute, or strictly reduce the finite connection congruence
\[
\frac gp\equiv-\frac{t}{6}W_{n-1}(t)\pmod p.
\tag{LC}
\]

The frozen parent facts imply that `(LC)` is exactly equivalent to the remaining unit-reciprocity certificate `(UR)` and therefore to the first Jacobi-jet digit `(JT0)`.

## Frozen inputs and scope

Freeze the parent theorem-level facts
\[
P_n(t)=Q_m(1/2)\equiv0\pmod p,\qquad
P_n'(t)=2tQ_m'(1/2)\not\equiv0\pmod p,
\]
and the exact parent equivalence
\[
(JT0)\iff(UR),\qquad
(UR):\quad \frac gp\equiv-\frac1{6Q_m'(1/2)}\pmod p.
\]

Also freeze the finite companion representation of the Legendre second solution
\[
\mathcal Q_n(t)=\frac12P_n(t)\log\frac{1+t}{1-t}-W_{n-1}(t)
\]
and its Wronskian. At the frozen CM root this gives
\[
\mathcal Q_n(t)=-W_{n-1}(t)=-\frac2{P_n'(t)},
\]
hence
\[
-\frac t6W_{n-1}(t)=-\frac1{6Q_m'(1/2)}.
\]
Thus the new work is only the finite connection `(LC)`.

Use the exact deformation
\[
F_p(\varepsilon)=
\sum_{k=0}^{p-1}
\frac{(-n/2+\varepsilon)_k((n+1)/2-\varepsilon)_k}{2^k(k!)^2},
\qquad
g=F_p(p/6).
\]
The centered value terminates, but the perturbed finite sum does not. Any first-order argument must retain both the divided centered value \(F_p(0)/p\) and the terms beyond the centered terminating cutoff that reappear at first \(p\)-adic order.

Both residue classes are required. Finite computation is falsification and regression evidence only. Do not use Sun A14(ii) as a theorem. Do not reopen CM0, SIMPLE, the earlier Clausen-tail or harmonic-block reductions, or the second-digit LIFT until LC/UR is closed.

## Hard target and required outputs

Hard target:

`INERT_PLUS_LEGENDRE_COMPANION_CONNECTION_LC_PROVED_REFUTED_OR_STRICTLY_REDUCED`.

Required outputs:

1. an all-prime proof of `(LC)`, one exact independently recomputed counterexample, or one strictly smaller exact certificate with proved equivalence;
2. a finite derivation from the \(p\)-term deformation \(F_p(\varepsilon)\) that controls the centered cutoff and every first-order resurrected tail term;
3. explicit accounting for the divided centered digit \(F_p(0)/p\), rather than silently replacing CM divisibility by exact zero;
4. a sign- and square-root-independent treatment of \(t^2=1/2\) showing that the final LC scalar lies in the required base field;
5. serious testing of a terminating parameter-derivative/telescoping route and a structurally distinct discrete Legendre Green/Wronskian or finite-field route unless one closes or refutes the target;
6. a deterministic checker used only for falsification and certificate regression;
7. a durable return that states exactly whether LC, UR and JT0 are proved, refuted, or reduced, and identifies the smallest remaining residue.

## Research value to preserve

The parent route has already removed the CM zero, simple-root transversality, harmonic blocks and the full second-digit interface from the first-digit problem. The remaining obstacle is now one finite connection between a divided \(p\)-truncated hypergeometric value and the polynomial companion of the Legendre second solution.

A proof of `(LC)` immediately proves `(UR)` and `(JT0)` under the frozen parent equivalence and opens a clean path to the separate second-digit LIFT problem. A counterexample would refute that first digit exactly. A further valid reduction should expose the smallest finite connection identity without restoring completed parent machinery.

## Success, kill, and return criteria

Success is a uniform proof of `(LC)` for both \(p\equiv13\) and \(19\pmod{24}\), with the finite cutoff and divided centered digit controlled explicitly.

One independently recomputed exact counterexample terminates `(LC)` negatively and, through the frozen equivalence, disposes of `(UR)` and `(JT0)` for that prime.

A strict reduction is acceptable only if it produces a genuinely smaller finite identity and proves the equivalence without dropping \(F_p(0)/p\) or the first-order post-termination tail. A finite prime scan, an uncontrolled infinite-series parameter derivative, an assumed reciprocal sign, or a return to the larger JT2 bookkeeping is non-closing.

Stop at the strongest exact statement and keep the second-digit LIFT separate unless LC/UR has first been closed.
