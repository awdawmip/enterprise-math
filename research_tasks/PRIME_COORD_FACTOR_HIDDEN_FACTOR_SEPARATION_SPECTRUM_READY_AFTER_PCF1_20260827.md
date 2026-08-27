<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-HIDDEN-FACTOR-SEPARATION-SPECTRUM",
  "title": "Prime Coordinate Hidden-Factor Separation Spectrum",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Unify the audit-admitted factor-blind coordinate observables into one typed response spectrum and determine which components can desynchronize hidden CRT factors, with synchronized collision families classified exactly.",
  "next_action": "Use only PCF1-admitted N-blind observables to define the response vector, derive proof-side CRT projections, compute separation/collision data, and pursue the strongest exact separator or synchronization no-go.",
  "dependencies": [
    "research_result_records/RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT/RR-B8D8679EB033E990E825.json@5962795e98743cf8b5dba3fcfc043f508bda34a4",
    "driver_reviews/PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_DRIVER_REVIEW_20260827.md@SAME_PUBLICATION_TRANSACTION"
  ],
  "source_refs": [
    "research_tasks/PRIME_COORD_FACTOR_HIDDEN_FACTOR_SEPARATION_SPECTRUM_20260827.md@c7a4cd1d13be4d53e0b7064207ef06a46df34aed",
    "research_returns/PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_RETURN_20260827.md@650a01f59534f2652b033873cc7c4dcd8038723a",
    "research_result_records/RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT/RR-B8D8679EB033E990E825.json"
  ],
  "evidence_status": "PCF1_ACCEPTED / ADMISSIBILITY_SET_FROZEN / DEPENDENCY_GATE_RELEASED",
  "last_progress_ref": "RR-B8D8679EB033E990E825 accepted by driver_reviews/PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_DRIVER_REVIEW_20260827.md; PCF1 gate released for PCF3.",
  "last_progress_at": "2026-08-27T08:59:30+00:00",
  "hard_block": null,
  "tags": [
    "prime-coordinate",
    "factorization",
    "n-blind",
    "gcd-extraction",
    "pcf3"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-HIDDEN-FACTOR-SEPARATION-SPECTRUM",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF3",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "program_id": "PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827",
  "requested_risk_tier": "HIGH",
  "successor_gate": null,
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7"
}
-->

# Prime Coordinate Hidden-Factor Separation Spectrum

Status: `PUBLISHED_REGISTERED / READY / PCF1_GATE_RELEASED`

## Mother question

For N=pq, which PCF1-admitted N-only coordinate observables or finite combinations have proof-side projections modulo p and q that provably fail to remain synchronized on a nontrivial scope?

## Frozen inputs and scope

PCF1's admissibility matrix is binding for constructor inputs: factor-conditional quantities may appear only in proof-side CRT analysis. Preserve the generation-1 spectrum obligations for holonomy/incidence, wall, shell, filament, BRC/p-adic and Prime-Fusion observables only where PCF1 admitted an N-only constructor. A useful separation event must be convertible to an integer residue or an exact input to PCF4. Classify symmetry-induced collisions, same-shell/filament responses, phase conjugacy and near-twin cases.

The generation-1 taskbook `research_tasks/PRIME_COORD_FACTOR_HIDDEN_FACTOR_SEPARATION_SPECTRUM_20260827.md` remains the frozen source for any task-local detail not restated here. PCF1 result `RR-B8D8679EB033E990E825` and this Driver release only remove the PCF1 dependency; they do not weaken any theorem, complexity, checker, failure-set, or return obligation.

## Hard target and required outputs

Hard target: `HIDDEN_FACTOR_SEPARATION_SPECTRUM_CLASSIFIED`.

Required outputs:

1. typed N-only response vector and exact proof-side CRT projections.
2. taxonomy of valuation, rank, determinant, collision-time and related separation events.
3. exact collision registry on benchmark families with factor-independent seed policy.
4. at least one exact separator/restricted separator or synchronization/no-go theorem.
5. ranked integerizable-asymmetry handoff to PCF4.
6. durable return at `research_returns/PRIME_COORD_FACTOR_HIDDEN_FACTOR_SEPARATION_SPECTRUM_RETURN_20260827.md`.

## Research value to preserve

Tests whether the coordinate observables contain independent hidden-factor information at all, and isolates a smallest integerizable asymmetry instead of accumulating descriptive signals.

## Success, kill, and return criteria

Freeze exactly one strongest exact verdict from: `SEPARATOR_FOUND_WITH_EXACT_SCOPE`, `RESTRICTED_SEPARATOR_ONLY`, `SPECTRUM_SYNCHRONIZATION_NO_GO`, or `SPECTRUM_CLASSIFIED_EMPIRICALLY_ONLY`.

Any claimed factor split must arise from a constructor admissible under PCF1. Finite computation may refute or support regression but does not prove an infinite theorem. Stop at the strongest exact task-local result and preserve the smallest unresolved residue.

## Queue interface

- Program: `PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`.
- State: `READY`.
- Effective priority/leverage request: `P1 / HIGH`.
- Released dependency: `RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT` via `RR-B8D8679EB033E990E825` and its accepted Driver review.
- Parent objective generation: `OG-AA2BAD92F59DC97880C7`.
- First executable action: Use only PCF1-admitted N-blind observables to define the response vector, derive proof-side CRT projections, compute separation/collision data, and pursue the strongest exact separator or synchronization no-go.
