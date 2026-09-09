<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION",
  "title": "PCF7 fixed-probe zero-value statement correction — policy-refreshed generation",
  "kind": "RESEARCH",
  "owner": "research/prime-coord-factor-complexity-failure-classification-statement-correction",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "PCF7's polynomial-prefix obstruction remains intact. The only accepted defect is the fixed-probe sentence: seed s=1 gives probe 0, so gcd(N,0)=N rather than 1. The current task generation refreshes execution policy only; it changes no mathematical target.",
  "next_action": "Correct only the fixed-probe zero-value statement, bind an exact before/after statement audit, replay or byte-preserve the existing deterministic checker as appropriate, and freeze a fresh current-schema Result with complete evidence digests and no mathematical expansion.",
  "dependencies": [
    "RR-A9A5ADD3931B3F3EDFAB"
  ],
  "source_refs": [
    "research_returns/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_RETURN_20260827.md",
    "research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py",
    "driver_reviews/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_DRIVER_REVIEW_20260902.md",
    "research_task_records/RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION/TP2-C4DB35B43FE7334D2B63.json",
    "research_artifacts/PCF_PERSISTENT_LINE_DRIVER_20260909/dossier.md"
  ],
  "evidence_status": "POLICY_REFRESH_ZERO_MATH_DRIFT / DRIVER_REQUEST_REVISION_BOUNDARY_PRESERVED",
  "last_progress_ref": "research_result_reviews/RR-A9A5ADD3931B3F3EDFAB/DR-8183213860B7A72A2BD3.json",
  "last_progress_at": "2026-09-02T12:56:00+00:00",
  "hard_block": null,
  "tags": [
    "PCF",
    "PCF7",
    "REVISION",
    "statement-correction",
    "zero-probe",
    "policy-refresh"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF7FIX",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# PCF7 fixed-probe zero-value statement correction — policy-refreshed generation

Status: `READY / PUBLISHED_REGISTERED / POLICY_REFRESH / ZERO_MATH_DRIFT`

## Mother question

Can the single false fixed-probe sentence in PCF7 be corrected so that zero probes return `N`, nonzero avoided-support probes return `1`, and the exact no-proper-factor conclusion is preserved without changing the main polynomial-prefix theorem?

## Frozen inputs and scope

Freeze `RR-A9A5ADD3931B3F3EDFAB`, its return, checker, certificate, and Driver review `DR-8183213860B7A72A2BD3` as the source evidence. Preserve the polynomial-prefix infinite balanced-semiprime obstruction, the exact worst-case proper-split probability `0` for the declared polynomial-prefix campaign model, the `L=N` recurrence analysis, T1–T5, and the sealed PCF2 benchmark boundary.

The only authorized mathematical correction is the fixed-family zero-probe distinction. For any fixed probe value `a`, the corrected cases are: `a != 0` and its prime support is avoided, hence `gcd(N,a)=1`; or `a=0`, hence `gcd(N,a)=N`. Neither case yields a proper factor.

This generation refreshes task-policy compatibility only. It does not reopen the original theorem proof and does not authorize a numerical benchmark generation, a new factoring algorithm, a universal factoring lower bound, or a stronger N-dependent theorem.

## Hard target and required outputs

Hard target:

`PCF7_FIXED_PROBE_ZERO_VALUE_STATEMENT_CORRECTED_WITH_MAIN_THEOREM_PRESERVED`

Required outputs:

1. a corrected PCF7 return or correction return that explicitly states `gcd(N,0)=N`;
2. an exact before/after statement audit proving the mathematical delta is limited to the false fixed-probe sentence;
3. replay of the existing deterministic checker, or an exact explanation and byte binding if no checker change is necessary;
4. a fresh execution record under this current task generation;
5. a fresh current-schema Result with complete Git-blob SHA-1 and SHA-256 bindings for every load-bearing output;
6. an explicit statement that the polynomial-prefix theorem, `L=N` classification, sealed PCF2 benchmark boundary, and no-global-lower-bound guards are unchanged.

## Research value to preserve

PCF7 contains a useful negative complexity frontier. Its value is preserved only if the local zero-probe mistake is repaired without weakening the main obstruction and without converting the repair into unsupported novelty or complexity claims.

The corrected evidence package should make later portfolio review mechanically safe: fixed probes may fail by returning `1` or the trivial gcd `N`, while the declared public polynomial-prefix campaign still has an infinite balanced family with no proper split.

## Success, kill, and return criteria

SUCCESS requires exact corrected prose, checker/certificate consistency, a fresh current-schema Result, and `MATHEMATICAL_DELTA` limited to the zero-probe statement.

Kill and return for substantive review if the correction changes Theorem 6.1, changes the campaign model, changes the `L=N` complexity calculation, mutates the sealed PCF2 benchmark, or introduces a new factorization/lower-bound claim.

If the existing checker already encodes `gcd(N,0)=N` correctly, preserve its bytes and bind them rather than manufacturing a code delta. Stop once the exact statement and immutable evidence chain are repaired.
