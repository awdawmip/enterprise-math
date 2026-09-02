<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION",
  "title": "PCF7 fixed-probe zero-value statement correction",
  "kind": "RESEARCH",
  "owner": "research/prime-coord-factor-complexity-failure-classification-statement-correction",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "PCF7's polynomial-prefix obstruction remains intact, but the frozen fixed-probe prose incorrectly states that every sixth-power fixed-family gcd is 1; seed s=1 produces probe 0 and therefore gcd(N,0)=N.",
  "next_action": "Correct only the fixed-probe zero-value statement, verify the existing checker/certificate semantics against the corrected prose, and freeze a fresh current-schema Result with complete dual-digest bindings and no mathematical expansion.",
  "dependencies": [
    "RR-A9A5ADD3931B3F3EDFAB"
  ],
  "source_refs": [
    "research_returns/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_RETURN_20260827.md",
    "research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py",
    "driver_reviews/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_DRIVER_REVIEW_20260902.md"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "REVISION",
    "DRIVER_AUTO_FOLLOWUP",
    "PCF7",
    "statement-correction",
    "zero-probe"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF7FIX",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:46f9b27002cd7f8a3d64fdec95e8c4519dc99d8f003b48c21e4f94182bc98e8b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# PCF7 fixed-probe zero-value statement correction

Status: `READY / DRIVER REVIEW FOLLOW-UP / PENDING IMMUTABLE PUBLICATION`

## 0. Mother question

Can the single false fixed-probe sentence in PCF7 be corrected so that zero probes return `N`, nonzero avoided-support probes return `1`, and the exact no-proper-factor conclusion is preserved without changing the main polynomial-prefix theorem?

## 1. Frozen inputs and scope

Freeze `RR-A9A5ADD3931B3F3EDFAB`, its return, checker, and certificate as the source evidence. Preserve the polynomial-prefix infinite balanced-semiprime obstruction, the exact worst-case proper-split probability `0` for the declared polynomial-prefix campaign model, the `L=N` recurrence analysis, T1–T5, and the sealed PCF2 benchmark boundary.

The only authorized mathematical correction is the fixed-family zero-probe distinction. For any fixed probe value `a`, the corrected cases are: `a != 0` and its prime support is avoided, hence `gcd(N,a)=1`; or `a=0`, hence `gcd(N,a)=N`. Neither case yields a proper factor.

Do not alter the checker merely to match prose if its current zero/nonzero semantics are already correct. Do not add a numerical benchmark generation, a new factoring algorithm, a universal factoring lower bound, or a stronger N-dependent theorem.

## 2. Hard target and required outputs

Hard target:

`PCF7_FIXED_PROBE_ZERO_VALUE_STATEMENT_CORRECTED_WITH_MAIN_THEOREM_PRESERVED`

Required outputs:

1. a corrected PCF7 return or correction return that explicitly states `gcd(N,0)=N`;
2. an exact before/after statement audit showing the mathematical delta is limited to the false fixed-probe sentence;
3. replay of the existing deterministic checker, or an exact explanation if no checker byte change is necessary;
4. a fresh execution record under this maintenance task;
5. a fresh current-schema Result with complete Git-blob SHA-1 and SHA-256 bindings for every load-bearing output;
6. an explicit statement that the polynomial-prefix theorem, `L=N` classification, sealed PCF2 benchmark boundary, and no-global-lower-bound guards are unchanged.

## 3. Research value to preserve

PCF7 contains a useful negative complexity frontier. Its value is preserved only if the local zero-probe mistake is corrected without weakening the main obstruction and without converting the correction into unsupported novelty or complexity claims.

The correction should make later portfolio review mechanically safe: fixed probes may fail by returning `1` or the trivial gcd `N`, while public polynomial-prefix campaigns still have an infinite balanced family with no proper split.

## 4. Success, kill, and return criteria

SUCCESS requires exact corrected prose, checker/certificate consistency, a fresh current-schema Result, and `MATHEMATICAL_DELTA` limited to the zero-probe statement.

Kill and return for substantive review if the correction changes Theorem 6.1, changes the campaign model, changes the `L=N` complexity calculation, mutates the sealed PCF2 benchmark, or introduces a new factorization/lower-bound claim.

If the existing checker already encodes `gcd(N,0)=N` correctly, preserve its bytes and bind them rather than manufacturing a code delta. Stop once the exact statement and immutable evidence chain are repaired.
