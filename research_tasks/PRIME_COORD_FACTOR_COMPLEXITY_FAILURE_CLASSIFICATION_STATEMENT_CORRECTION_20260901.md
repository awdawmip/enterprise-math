<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "base_state": "READY",
  "leverage": "HIGH",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION",
  "title": "PCF7 fixed-probe zero-value statement correction",
  "owner": "research/prime-coord-factor-complexity-failure-classification-statement-correction",
  "priority": "P0",
  "frontier": "Correct the exact fixed-probe sentence in PCF7 Section 7 while preserving Theorem 6.1, the complexity frontier, T1-T5, and all nonzero-probe arguments with zero other mathematical drift.",
  "next_action": "Replace the false all-gcd-equals-1 sentence by the exact no-proper-split statement: nonzero probes give gcd 1 on the selected semiprimes, while zero probes give gcd N; add an explicit zero-probe regression if useful and freeze a corrected Result.",
  "dependencies": [
    "RR-A9A5ADD3931B3F3EDFAB"
  ],
  "source_refs": [
    "RR-A9A5ADD3931B3F3EDFAB",
    "research_returns/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_RETURN_20260827.md"
  ],
  "evidence_status": "DRIVER_REQUEST_REVISION_V1",
  "tags": [
    "REVISION",
    "DRIVER_AUTO_FOLLOWUP",
    "PCF7",
    "statement-correction",
    "zero-math-drift-except-exact-wording"
  ],
  "registry_key": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION",
  "identity_lane": "PCF7-REVISION"
}
-->

# PCF7 fixed-probe zero-value statement correction

Status: `READY / DRIVER REQUEST REVISION`

## 0. Mother question

Can the PCF7 fixed-probe family statement be made exact without changing its main polynomial-prefix theorem or portfolio conclusion?

## 1. Frozen inputs and scope

Freeze `RR-A9A5ADD3931B3F3EDFAB` except for the exact Section 7 statement identified by Driver review. Preserve Theorem 6.1, the infinite balanced zero-success family for every polynomial public-prefix cap, the `L=N` complexity classification, T1-T5, the sealed PCF2 boundary, and the prohibition on global factoring lower-bound claims.

The defect is narrow: for the sixth-power seed `s=1`, `s^6-1=0`, so `gcd(N,0)=N`, not `1`. The existing checker already skips the zero value when asserting gcd 1.

## 2. Hard target and required outputs

Hard target: `PCF7_FIXED_PROBE_ZERO_VALUE_STATEMENT_EXACTLY_CORRECTED_WITH_MAIN_THEOREM_UNCHANGED`.

Correct the prose and any certificate text so that the exact statement is: for the selected semiprimes, every nonzero fixed probe has gcd `1`, every zero fixed probe has gcd `N`, and therefore no probe returns a proper factor. Add a deterministic explicit zero-probe assertion to the checker if needed. Freeze a fresh Result with complete current digest bindings.

## 3. Research value to preserve

The main PCF7 result closes the generic PCF4 public-prefix route at worst-case polynomial-prefix strength. A one-line fixed-probe overstatement should not force re-research of that theorem, but it must be corrected before Driver acceptance because `gcd(N,0)=N` is an exact arithmetic boundary and immutable Result prose cannot be accepted while stating otherwise.

## 4. Success, kill, and return criteria

Success requires the exact zero/nonzero probe distinction and zero drift in Theorem 6.1, complexity estimates, T1-T5, benchmark boundaries, and no-lower-bound guards. Kill the revision if it weakens the polynomial-prefix theorem, changes the benchmark corpus, upgrades the Result to a global factoring lower bound, or introduces unrelated successor mathematics.
