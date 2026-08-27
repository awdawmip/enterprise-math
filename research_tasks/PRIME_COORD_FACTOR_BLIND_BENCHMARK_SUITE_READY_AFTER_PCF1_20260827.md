<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE",
  "title": "Prime Coordinate Factor-Blind Benchmark Suite",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Build a factor-blind exact-integer benchmark that accepts only N, an independent seed and precommitted public parameters, measures nontrivial-gcd success, and compares audit-admitted Enterprise candidates against classical baselines across adversarial integer families.",
  "next_action": "Consume the PCF1 admissibility matrix, freeze the sealed Run(N,s,public-parameters) interface, implement the corpus, verifier and classical baselines, and validate that candidate execution cannot access hidden factorization data.",
  "dependencies": [
    "research_result_records/RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT/RR-B8D8679EB033E990E825.json@5962795e98743cf8b5dba3fcfc043f508bda34a4",
    "driver_reviews/PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_DRIVER_REVIEW_20260827.md@SAME_PUBLICATION_TRANSACTION"
  ],
  "source_refs": [
    "research_tasks/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_20260827.md@042229f1401ba83813ff55e5caccc7f47b97512a",
    "research_returns/PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_RETURN_20260827.md@650a01f59534f2652b033873cc7c4dcd8038723a",
    "research_result_records/RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT/RR-B8D8679EB033E990E825.json"
  ],
  "evidence_status": "PCF1_ACCEPTED / ADMISSIBILITY_SET_FROZEN / DEPENDENCY_GATE_RELEASED",
  "last_progress_ref": "RR-B8D8679EB033E990E825 accepted by driver_reviews/PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_DRIVER_REVIEW_20260827.md; PCF1 gate released for PCF2.",
  "last_progress_at": "2026-08-27T08:59:30+00:00",
  "hard_block": null,
  "tags": [
    "prime-coordinate",
    "factorization",
    "n-blind",
    "gcd-extraction",
    "pcf2"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF2",
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

# Prime Coordinate Factor-Blind Benchmark Suite

Status: `PUBLISHED_REGISTERED / READY / PCF1_GATE_RELEASED`

## Mother question

Can every audit-admitted Enterprise candidate be run through a sealed interface `Run(N,s,public_parameters)` whose only success is an exactly verified nontrivial divisor of N, while the candidate process remains unable to read the hidden factorization?

## Frozen inputs and scope

PCF1 is accepted and its admissibility matrix is now the constructor boundary. Preserve the complete mathematical and benchmarking obligations of the generation-1 taskbook. The benchmark must include balanced and unbalanced semiprimes, near-twin factors, prime powers, products of at least three primes, Carmichael and strong-pseudoprime families, and coordinate-collision cases. Hidden factors may exist only inside the sealed verifier. Implement exact trial-division, Fermat-style, Pollard rho and Pollard p-1 baselines; measure nontrivial-gcd success, cost, memory and failure families rather than geometric concentration.

The generation-1 taskbook `research_tasks/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_20260827.md` remains the frozen source for any task-local detail not restated here. PCF1 result `RR-B8D8679EB033E990E825` and this Driver release only remove the PCF1 dependency; they do not weaken any theorem, complexity, checker, failure-set, or return obligation.

## Hard target and required outputs

Hard target: `NBLIND_FACTORIZATION_BENCHMARK_SUITE_FROZEN`.

Required outputs:

1. deterministic corpus generator with independent factor-generation and candidate-execution compartments.
2. sealed N-only candidate interface plus deliberate leakage rejection tests.
3. exact baseline implementations and versioned parameter manifest.
4. machine-readable replay/result schema with nontrivial-gcd primary metrics.
5. durable return at `research_returns/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_RETURN_20260827.md`.

## Research value to preserve

Provides the common sealed falsification surface needed to distinguish genuine N-only extraction from factor-conditional structure and disguised square-root enumeration.

## Success, kill, and return criteria

Freeze exactly one strongest exact verdict from: `BENCHMARK_FROZEN_AND_SEALED`, `BENCHMARK_PARTIAL_WITH_EXACT_BLOCKER`, or `BENCHMARK_INTERFACE_INVALID`.

Any claimed factor split must arise from a constructor admissible under PCF1. Finite computation may refute or support regression but does not prove an infinite theorem. Stop at the strongest exact task-local result and preserve the smallest unresolved residue.

## Queue interface

- Program: `PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`.
- State: `READY`.
- Effective priority/leverage request: `P1 / HIGH`.
- Released dependency: `RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT` via `RR-B8D8679EB033E990E825` and its accepted Driver review.
- Parent objective generation: `OG-AA2BAD92F59DC97880C7`.
- First executable action: Consume the PCF1 admissibility matrix, freeze the sealed Run(N,s,public-parameters) interface, implement the corpus, verifier and classical baselines, and validate that candidate execution cannot access hidden factorization data.
