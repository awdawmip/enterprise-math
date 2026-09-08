<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT",
  "title": "Enterprise BRC CM(-24) UR External Prior-Art Duplication Audit",
  "owner": "research/enterprise-brc-half-inert-plus-cm24-ur-external-prior-art-audit",
  "kind": "RESEARCH",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Audit external literature and repositories for exact or partial antecedents of the CM(-24) inert supersingular unit-reciprocity certificate UR, separating exact duplication from partial antecedent, adjacent method, and no material match.",
  "next_action": "Search task-specific sources for Sun A14(ii), truncated 2F1(1/6,1/3;1;1/2) inert-prime congruences, CM(-24) Hesse/Legendre Hasse derivative formulas, Dwork supersingular hypergeometric derivatives, Jacobi sums, Gross-Koblitz, and p-adic Gamma evaluations; freeze bibliographic evidence and an exact duplication classification.",
  "dependencies": [
    "RR-82F6383FB6634F72B457",
    "DR-2EA60F5817976E662FA6"
  ],
  "source_refs": [
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md",
    "driver_reviews/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_DRIVER_REVIEW_20260908.md",
    "Zhi-Wei Sun, Open Conjectures on Congruences, arXiv:0911.5665, Conjecture A14(ii)"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": "EXTERNAL_DUPLICATION_STATUS_OF_CM24_UR",
  "tags": [
    "EXTERNAL_PRIOR_ART_DUPLICATION",
    "DRIVER_AUTO_FOLLOWUP",
    "BRC",
    "CM-24",
    "supercongruence",
    "prior-art",
    "UR"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP6URPA",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE",
  "successor_gate": {
    "new_information_gap": "The accepted mathematical reduction names UR precisely, but the repository contains no dedicated external-duplication audit for this exact reciprocal-scalar statement and normalization.",
    "why_parent_result_does_not_close_it": "The parent research cites Sun A14(ii) and audits several proof technologies, but it does not classify whether UR itself, its Hesse CM(-24) derivative form, or an equivalent inert supersingular formula already appears externally.",
    "discriminating_outcomes": [
      "An exact external antecedent equivalent to UR is found and pinned.",
      "Only a partial antecedent is found, with the missing normalization or inert-prime step identified exactly.",
      "Adjacent methods are found but no material statement match is established.",
      "A previously cited source is shown not to contain the claimed UR-strength statement."
    ],
    "kill_condition": "Do not infer novelty from failure to find a match. Do not treat title or keyword similarity as mathematical equivalence. Do not broaden into a generic survey unrelated to the exact UR normalization.",
    "alternative_route_or_free_exploration_considered": "The current repository search found no dedicated UR prior-art task. Reusing the older broad reflected-product technology audit would leave the exact reciprocal-scalar duplication question unresolved, so a narrow external audit is justified.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The accepted review requires external duplication handling, and the mathematical successor is narrow enough that its literature firewall should be equally narrow and independently auditable."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:cf093f1f89f9a177490c674eae7a40aa6d64306cb2d6fe26e93b1b71febaa0d7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC CM(-24) UR External Prior-Art Duplication Audit

Status: `READY / DRIVER REVIEW FOLLOW-UP / PUBLISHED_REGISTERED`

## 0. Mother question

Does the exact inert-prime reciprocal-scalar certificate

\[
\left(\frac{g}{p}\right)\left(-6Q_m'(1/2)\right)\equiv1\pmod p
\]

for `p mod 24` in `{13,19}` already occur externally, verbatim or through a mathematically equivalent CM(-24), supersingular Hasse-derivative, finite-field Jacobi-sum, Dwork, or p-adic special-function formulation?

## 1. Frozen inputs and scope

Freeze the accepted JT2 strict reduction and the exact UR statement. This task does not re-prove UR and does not decide `LIFT`.

Search independent external literature and repository sources for Sun Conjecture A14(ii) and later work on its inert-plus cases; truncated `2F1(1/6,1/3;1;1/2)` congruences and divided-by-p evaluations; Legendre or Hesse Hasse invariants at discriminant `-24` and derivatives at supersingular CM points; supersingular Dwork formulas; finite-field hypergeometric functions, Jacobi sums, Gross-Koblitz and p-adic Gamma identities matching the factor `-6Q_m'(1/2)`; and transformations giving the exact UR normalization.

Record search date, exact queries, candidate sources, theorem or equation locations, and whether hypotheses and strength match UR.

## 2. Hard target and required outputs

Hard target: `CM24_UR_EXTERNAL_DUPLICATION_CLASSIFIED`.

Classify each serious candidate as `EXACT_DUPLICATE_OR_EQUIVALENT`, `PARTIAL_ANTECEDENT`, `ADJACENT_METHOD`, or `NO_MATERIAL_MATCH`. Exact duplication requires a bidirectional mathematical translation with the same residue classes and normalization. A partial antecedent must state precisely the missing factor, precision, or inert/supersingular hypothesis.

Required outputs are a durable audit return, independently checkable bibliographic/link evidence, a theorem-comparison table, and a NEW Result-ID with frozen evidence bindings.

## 3. Research value to preserve

A future UR proof may use Wronskian, Gauss-Manin, Jacobi-sum, or p-adic-Gamma ideas. This audit separates derivation inside the Enterprise BRC chain from any external novelty claim and may expose the shortest already-proved ingredient matching the inert supersingular normalization.

## 4. Success, kill, and return criteria

Success is an evidence-backed duplication classification for exact UR and its strongest close antecedents. If an exact antecedent is found, return the translation and source location. If no material antecedent is found, return only the bounded search result and candidate map; search silence is not a novelty theorem.

Reject vague bibliographic resemblance, unsourced recollection, ordinary split-CM formulas presented as supersingular results without matching hypotheses, finite numerical agreement as proof, or novelty declarations from failure to locate a match.

No theorem truth, Working Truth, Foundation status, or priority claim is created by this audit.
