<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE",
  "title": "Prime Coordinate Blind p-adic-to-GCD Bridge",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Construct from N and an independent seed alone an exact integer residue G_N(s) whose local behavior is asymmetric at hidden prime factors, and prove nontrivial-gcd extraction on an infinite semiprime family or freeze the smallest exact obstruction.",
  "next_action": "Using PCF1's admitted N-only surface, rewrite the strongest BRC/p-adic candidate as an N-native integer recurrence, derive proof-side CRT/valuation behavior, and search for the first asymmetric residue, determinant, rank defect or collision whose gcd with N isolates a factor without prime scanning.",
  "dependencies": [
    "research_result_records/RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT/RR-B8D8679EB033E990E825.json@5962795e98743cf8b5dba3fcfc043f508bda34a4",
    "driver_reviews/PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_DRIVER_REVIEW_20260827.md@SAME_PUBLICATION_TRANSACTION"
  ],
  "source_refs": [
    "research_tasks/PRIME_COORD_FACTOR_BLIND_PADIC_GCD_BRIDGE_20260827.md@f1cce110096911438d5633a0cb9a1b4350c2a7d1",
    "research_returns/PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_RETURN_20260827.md@650a01f59534f2652b033873cc7c4dcd8038723a",
    "research_result_records/RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT/RR-B8D8679EB033E990E825.json"
  ],
  "evidence_status": "PCF1_ACCEPTED / ADMISSIBILITY_SET_FROZEN / DEPENDENCY_GATE_RELEASED",
  "last_progress_ref": "RR-B8D8679EB033E990E825 accepted by driver_reviews/PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_DRIVER_REVIEW_20260827.md; PCF1 gate released for PCF4.",
  "last_progress_at": "2026-08-27T08:59:30+00:00",
  "hard_block": null,
  "tags": [
    "prime-coordinate",
    "factorization",
    "n-blind",
    "gcd-extraction",
    "pcf4"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF4",
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
  "requested_risk_tier": "CRITICAL",
  "successor_gate": null,
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7"
}
-->

# Prime Coordinate Blind p-adic-to-GCD Bridge

Status: `PUBLISHED_REGISTERED / READY / PCF1_GATE_RELEASED`

## Mother question

For an unfactored semiprime N=pq, can an integer G_N(s) be constructed from N and an independent seed alone so that gcd(G_N(s),N) is provably nontrivial on an explicit infinite family without square-root-scale prime scanning?

## Frozen inputs and scope

PCF1 has accepted the input model and explicitly forbids p, q, factor-labelled coordinates, factor-derived phases, CRT idempotents and prime-labelled M_{p,q} objects as constructor inputs. CRT and p-adic valuations remain proof tools. Start from audit-admitted N-native BRC/p-adic data only. Every division over a composite modulus must be justified or cleared integrally. State complexity in bit length. Finite splits are regression evidence, not proof.

The generation-1 taskbook `research_tasks/PRIME_COORD_FACTOR_BLIND_PADIC_GCD_BRIDGE_20260827.md` remains the frozen source for any task-local detail not restated here. PCF1 result `RR-B8D8679EB033E990E825` and this Driver release only remove the PCF1 dependency; they do not weaken any theorem, complexity, checker, failure-set, or return obligation.

## Hard target and required outputs

Hard target: `BLIND_PADIC_GCD_BRIDGE_PROVED_REFUTED_OR_EXACTLY_OBSTRUCTED`.

Required outputs:

1. explicit N-only construction of G_N(s), seed policy and stopping rule.
2. proof-side CRT decomposition and exact local valuation/rank analysis.
3. nontrivial-gcd theorem on an infinite family or the strongest exact restricted theorem/no-go.
4. proved success probability or deterministic seed bound and complete synchronization/failure set.
5. bit-complexity and memory bound.
6. two independent exact-integer checkers whose candidate side receives only N, seed and public parameters.
7. durable return at `research_returns/PRIME_COORD_FACTOR_BLIND_PADIC_GCD_BRIDGE_RETURN_20260827.md`.

## Research value to preserve

This is the program's shortest direct route from exact blind arithmetic structure to an actual integer split; PCF1 shows the missing ingredient is an N-only asymmetry generator, not another decoder.

## Success, kill, and return criteria

Freeze exactly one strongest exact verdict from: `GCD_EXTRACTOR_PROVED`, `RESTRICTED_GCD_EXTRACTOR_PROVED`, `PADIC_FINGERPRINT_SYNCHRONIZATION_NO_GO`, `BRIDGE_NOT_CLOSED`, or `TARGET_REFUTED`.

Any claimed factor split must arise from a constructor admissible under PCF1. Finite computation may refute or support regression but does not prove an infinite theorem. Stop at the strongest exact task-local result and preserve the smallest unresolved residue.

## Queue interface

- Program: `PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`.
- State: `READY`.
- Effective priority/leverage request: `P0 / HIGH`.
- Released dependency: `RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT` via `RR-B8D8679EB033E990E825` and its accepted Driver review.
- Parent objective generation: `OG-AA2BAD92F59DC97880C7`.
- First executable action: Using PCF1's admitted N-only surface, rewrite the strongest BRC/p-adic candidate as an N-native integer recurrence, derive proof-side CRT/valuation behavior, and search for the first asymmetric residue, determinant, rank defect or collision whose gcd with N isolates a factor without prime scanning.
