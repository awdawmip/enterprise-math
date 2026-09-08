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
  "next_action": "First independently audit the exact Chisholm-Deines-Long-Nebe-Swisher 2013 specialization documented in the pinned noncanonical project artifact: verify d=3, lambda=1/2, a=6, the supersingular sign, all target-prime hypotheses, and the frozen bridge from the weighted mod-p^2 congruence to JT0/UR/LC. If that audit passes, close LC/UR/JT0 by prior art and return LIFT as the sole successor; if it fails, resume the direct finite LC deformation attack with the base divided digit and resurrected tail retained.",
  "dependencies": [
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/RR-82F6383FB6634F72B457.json@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE/ur_legendre_companion_connection_frontier_20260909.json@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE/ur_chisholm_closure_lift_frontier_20260908.md@9a1d0b374564abfcc888458b79c1030d52da924c"
  ],
  "source_refs": [
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE/ur_legendre_companion_connection_frontier_20260909.json@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE/ur_chisholm_closure_lift_frontier_20260908.md@9a1d0b374564abfcc888458b79c1030d52da924c",
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE/height2_frobenius_second_digit_reduction_20260908.md@9a1d0b374564abfcc888458b79c1030d52da924c",
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/RR-82F6383FB6634F72B457.json@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f",
    "research_task_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/TP2-A19C97A703AF47D1CBEC.json@f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f"
  ],
  "evidence_status": "PARENT_STRICT_REDUCTION_DURABLE / NONCANONICAL_CHISHOLM_UR_CLOSURE_SOURCE_PINNED_FOR_INDEPENDENT_AUDIT / LC_DIRECT_ROUTE_RETAINED_AS_FALLBACK",
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
    "new_information_gap": "The parent task reduced JT0 to UR. A later noncanonical project research artifact reports that an existing 2013 CM Ramanujan congruence already proves the weighted mod-p^2 statement and hence UR/JT0, while the direct Legendre companion frontier proves UR is equivalent to LC. The project main has not frozen that prior-art closure, so the next task must independently decide this stronger candidate closure before spending effort on a new LC proof.",
    "why_parent_result_does_not_close_it": "The canonical parent Result stops at UR. The later Chisholm specialization is only source-backed candidate evidence on a noncanonical research branch, and the direct LC congruence is also unproved. An independent all-hypotheses audit can either promote the first digit to a proved research return or expose the precise gap that leaves LC live.",
    "discriminating_outcomes": [
      "Verify the pinned Chisholm specialization and frozen weighted-sum bridge exactly, thereby proving UR, LC and JT0 for both target residue classes as a prior-art closure.",
      "Find an exact hypothesis, normalization, sign, or bridge failure in that specialization; record the obstruction and continue with the direct finite LC target.",
      "Produce and independently recompute an exact counterexample to LC or the claimed weighted mod-p^2 bridge, refuting the corresponding first-digit claim.",
      "If both prior-art and direct routes remain open, strictly reduce LC to one smaller finite identity that retains the base divided digit and resurrected tail."
    ],
    "kill_condition": "A validated Chisholm specialization plus the frozen bridge kills the need for a new LC proof and closes the first digit. An independently recomputed counterexample kills LC. Any route that assumes the noncanonical prior-art note as already accepted, drops F_p(0)/p or the post-termination tail, or relies only on finite scanning is non-closing.",
    "alternative_route_or_free_exploration_considered": "Alternatives were to attack LC directly, move immediately to the second-digit LIFT, or leave UR as an inherited conjectural boundary. Because a pinned project research artifact now supplies a potentially complete prior-art proof of UR/JT0, independent audit of that route has higher information value than duplicating a proof; the direct LC route remains a controlled fallback.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task is terminal at strict-reduction scope, while this successor now has a genuinely new source-backed closure candidate and an exact direct fallback. A bounded successor prevents replay of CM0/SIMPLE and ensures that a new owner either closes the first digit from prior art or returns the precise defect before any LIFT work begins."
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

Status: `PUBLISHED_REGISTERED / CONTINUATION / PRIOR-ART-AUDIT-FIRST / DIRECT-LC-FALLBACK`

## Mother question

For every prime
\[
p\equiv13,19\pmod{24},\qquad m=\frac{p-1}{6},\qquad n=\frac{p-1}{3}=2m,
\]
let \(t^2=1/2\) and
\[
g=\sum_{k=0}^{p-1}\frac{(1/6)_k(1/3)_k}{2^k(k!)^2}.
\]
For the Legendre polynomials \(P_r\), define
\[
W_{n-1}(t)=\sum_{j=1}^{n}\frac{P_{j-1}(t)P_{n-j}(t)}{j}.
\]
Determine the first digit exactly by proving, refuting, or strictly reducing
\[
\frac gp\equiv-\frac{t}{6}W_{n-1}(t)\pmod p.
\tag{LC}
\]

A pinned later research artifact reports a stronger route: an existing CM Ramanujan-type theorem at \(d=3,\lambda=1/2,a=6\) may already prove the equivalent weighted congruence and hence `(UR)`, `(LC)`, and `(JT0)`. Audit that route first rather than duplicating a proof.

## Frozen inputs and scope

Freeze only the parent theorem-level facts
\[
P_n(t)=Q_m(1/2)\equiv0\pmod p,\qquad
P_n'(t)=2tQ_m'(1/2)\not\equiv0\pmod p,
\]
and the exact parent equivalence
\[
(JT0)\iff(UR),\qquad
(UR):\quad \frac gp\equiv-\frac1{6Q_m'(1/2)}\pmod p.
\]

Also freeze the exact Legendre companion/Wronskian reduction
\[
\mathcal Q_n(t)=\frac12P_n(t)\log\frac{1+t}{1-t}-W_{n-1}(t),
\]
which at the CM root gives
\[
\mathcal Q_n(t)=-W_{n-1}(t)=-\frac2{P_n'(t)}
\]
and therefore
\[
-\frac t6W_{n-1}(t)=-\frac1{6Q_m'(1/2)}.
\]
Thus
\[
(JT0)\iff(UR)\iff(LC).
\]

Do **not** freeze the later Chisholm-based closure as a theorem. Treat its exact pinned artifact as source-backed candidate evidence and independently verify: the theorem statement, \(d=3,\lambda=1/2,a=6\) specialization, good-reduction and unit hypotheses, supersingular branch, Legendre-symbol sign, and the frozen bridge from the weighted mod-\(p^2\) congruence to `(JT0)`.

If that candidate closure fails, use the exact finite deformation
\[
F_p(\varepsilon)=
\sum_{k=0}^{p-1}
\frac{(-n/2+\varepsilon)_k((n+1)/2-\varepsilon)_k}{2^k(k!)^2},
\qquad
g=F_p(p/6).
\]
Any direct first-order proof must retain both \(F_p(0)/p\) and all terms beyond the centered terminating cutoff that reappear at first \(p\)-adic order.

Both residue classes are required. Finite computation is falsification and regression evidence only. Do not use Sun A14(ii) as a theorem. Do not reopen CM0, SIMPLE, the earlier Clausen-tail or harmonic-block reductions, or the second-digit LIFT before the first digit is settled.

## Hard target and required outputs

Hard target:

`INERT_PLUS_FIRST_DIGIT_UR_LC_JT0_PROVED_REFUTED_OR_STRICTLY_REDUCED`.

Required outputs:

1. an independent disposition of the pinned Chisholm-based prior-art closure, including exact theorem hypotheses, specialization, sign and weighted-sum bridge;
2. if that audit passes, a self-contained theorem chain proving `(UR)`, `(LC)` and `(JT0)` for both target residue classes, labeled as prior-art closure rather than novelty;
3. if that audit fails, the exact failing hypothesis or bridge step followed by an all-prime proof, exact counterexample, or strictly smaller certificate for direct `(LC)`;
4. for any direct LC proof, explicit accounting for \(F_p(0)/p\) and every first-order post-termination tail contribution;
5. a sign- and square-root-independent treatment of \(t^2=1/2\);
6. a deterministic checker used only for falsification and certificate regression;
7. a durable return that identifies the sole next residue: if the first digit closes, return the second-digit LIFT frontier; otherwise return the smallest surviving LC/prior-art defect.

## Research value to preserve

There are now two independent representations of the same first digit: the Legendre companion connection and a source-backed claim that an existing CM Ramanujan theorem already evaluates the equivalent weighted truncation modulo \(p^2\). Resolving their relationship has higher value than generating another finite scan.

A successful prior-art audit closes `(UR)`, `(LC)`, and `(JT0)` without novelty claims and prevents duplicate research. A failed audit identifies exactly why the literature does not apply and leaves the direct LC connection as a sharply bounded fallback. In either case, completed CM0/SIMPLE work stays frozen and the second digit remains separate.

## Success, kill, and return criteria

Success is either:

- a verified all-hypotheses application of the pinned 2013 CM Ramanujan theorem plus the frozen bridge, proving `(UR)`, `(LC)`, and `(JT0)` for both target residue classes; or
- an independent direct proof of `(LC)` with finite cutoff and divided centered digit controlled explicitly.

One independently recomputed exact counterexample terminates the corresponding first-digit claim negatively.

A strict reduction is acceptable only if it produces a genuinely smaller exact identity or a precise literature-hypothesis obstruction. Treating the noncanonical research note as already accepted, enlarging the prime scan, using an uncontrolled infinite-series derivative, or dropping \(F_p(0)/p\) or the resurrected tail is non-closing.

If the first digit closes, stop this task and return the frozen second-digit LIFT as the sole mathematical successor.
