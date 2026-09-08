<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-SUPERSINGULAR-UNIT-RECIPROCITY",
  "title": "Enterprise BRC Inert-Plus CM(-24) Supersingular Unit Reciprocity",
  "owner": "research/enterprise-brc-half-inert-plus-cm24-supersingular-unit-reciprocity",
  "kind": "RESEARCH",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Prove, refute, or strictly reduce the single first-digit reciprocity certificate UR: (g/p)(-6 Q_m'(1/2)) congruent 1 modulo p for p=6m+1 with p mod 24 in {13,19}, using the accepted CM(-24) simple-zero reduction without reopening CM0, SIMPLE, or the finite-tail bookkeeping.",
  "next_action": "Treat g as the p-adic parameter displacement of the same terminating hypergeometric family because 1/6=-m+p/6 and 1/3=-2m+p/3. Test a Gauss-Manin/Wronskian proof at the supersingular CM(-24) simple zero and a structurally distinct finite-field Jacobi-sum or p-adic-Gamma normalization; freeze an exact proof, counterexample, or one-scalar strict reduction.",
  "dependencies": [
    "RR-82F6383FB6634F72B457",
    "DR-2EA60F5817976E662FA6"
  ],
  "source_refs": [
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md",
    "driver_reviews/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_DRIVER_REVIEW_20260908.md",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": "DISCRIMINANT_MINUS24_SUPERSINGULAR_UNIT_RECIPROCITY",
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "DRIVER_AUTO_FOLLOWUP",
    "BRC",
    "hypergeometric",
    "CM-24",
    "supersingular",
    "unit-reciprocity",
    "p-adic"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-SUPERSINGULAR-UNIT-RECIPROCITY",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP6UR",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE",
  "successor_gate": {
    "new_information_gap": "The accepted JT2 result proves the CM(-24) Hasse value vanishes simply and reduces the entire first p-adic digit to one reciprocal scalar, but does not determine the normalized parameter displacement g/p.",
    "why_parent_result_does_not_close_it": "CM0 gives Q_m(1/2)=0 and SIMPLE gives Q_m'(1/2) nonzero, yet neither identifies g/p with the inverse of -6Q_m'(1/2); the previous finite parameter deformation only rewrites this missing equality as R0.",
    "discriminating_outcomes": [
      "A uniform proof of UR for both residue classes p congruent 13,19 modulo 24.",
      "An exact counterexample to UR, independently recomputed.",
      "A strict reduction of UR to one explicitly normalized CM(-24) deformation/Wronskian or finite-field scalar.",
      "An exact obstruction showing that an additional normalization datum is genuinely required."
    ],
    "kill_condition": "Finite prime regression is not a proof; Sun A14(ii) may not be assumed; ordinary split-CM unit-root or ASD formulas may not be imported at inert supersingular primes without a theorem matching this normalization; CM0, SIMPLE, and the eliminated tail/harmonic bookkeeping must not be reopened as if unresolved.",
    "alternative_route_or_free_exploration_considered": "Proceeding directly to LIFT is premature because UR is a necessary first digit. Replaying the terminating-Jacobi or finite-tail reductions would duplicate closed work. The justified independent routes are a local deformation/Wronskian argument and a finite-field or p-adic special-function normalization.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task is terminal at its authorized strict-reduction scope and identifies UR as the unique first-digit residue. A narrow successor preserves that terminal boundary while isolating one theorem-sized scalar."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:cf093f1f89f9a177490c674eae7a40aa6d64306cb2d6fe26e93b1b71febaa0d7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC Inert-Plus CM(-24) Supersingular Unit Reciprocity

Status: `READY / DRIVER REVIEW FOLLOW-UP / PUBLISHED_REGISTERED`

## 0. Mother question

For every prime `p=6m+1` with `p mod 24` equal to `13` or `19`, prove, refute, or strictly reduce

\[
\left(\frac{g}{p}\right)\left(-6Q_m'(1/2)\right)\equiv1\pmod p.
\]

## 1. Frozen inputs and scope

Freeze the accepted JT2 reduction. Let

\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2}2^{-k},\qquad g=\sum_{k=0}^{p-1}B_k,
\]

with `p | g`, and let `P_{2m}(T)=Q_m(T^2)` satisfy

\[
Q_m(1/2)=0,\qquad Q_m'(1/2)\ne0\quad\text{in }\mathbb F_p.
\]

These are frozen theorem inputs. The parent equivalences `JT0 iff UR` and `JT2 iff UR + LIFT` are frozen. Use

\[
\frac16=-m+\frac p6,\qquad \frac13=-2m+\frac p3
\]

to view `g/p` as the first nonzero p-adic parameter displacement of the same terminating hypergeometric family at its supersingular CM(-24) simple zero.

Do not attack `LIFT` here. Do not reopen CM0, SIMPLE, the reflected finite tail, or the five finite deformation sums except as frozen identities required to translate a candidate proof.

## 2. Hard target and required outputs

Hard target: `CM24_SUPERSINGULAR_UNIT_RECIPROCITY_PROVED_REFUTED_OR_STRICTLY_REDUCED`.

A positive proof must cover both target residue classes and produce the constant `1` and factor `-6` from exact normalization. Test two structurally distinct routes unless one already closes or refutes UR: (i) a local Hesse/Legendre deformation, Gauss-Manin, companion-solution, or Wronskian calculation at the CM(-24) supersingular simple zero; (ii) a finite-field Jacobi-sum, Gross-Koblitz, p-adic-Gamma, or equivalent special-function calculation with exact inert-prime hypotheses.

Required outputs are a theorem-level derivation or exact obstruction, dependency map for imported arithmetic theorems, an exact deterministic checker for falsification only, execution provenance, and a NEW Result-ID with frozen Git-blob and SHA-256 bindings.

## 3. Research value to preserve

UR is the exact first p-adic digit left after the terminating Jacobi-jet task proved CM0 and SIMPLE. Proving it reduces the inert-plus problem to the single second-digit `LIFT`; refuting it kills the accepted JT0 route. Preserve the structural fact that `g` is the parameter displacement `(-m,-2m) -> (1/6,1/3)`, so UR is a normalized pairing between parameter-normal and spatial-derivative directions at a simple supersingular Hasse zero.

## 4. Success, kill, and return criteria

Success is an all-prime proof of UR for the target classes with exact normalization. A valid negative return is an exact counterexample or theorem showing the normalization cannot be uniform. A valid strict reduction must lower UR to one explicit scalar identity bidirectionally equivalent to UR.

Reject finite hit rates as proof, assuming Sun A14(ii) or JT0, importing split ordinary-CM unit-root formulas at inert supersingular primes without matching hypotheses, numerically fitting the normalization, or re-expanding into closed parent tail/harmonic bookkeeping.

No Working Truth, Foundation status, or broader theorem follows merely from publishing or solving this task.
