<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE",
  "title": "Prime Coordinate Factor-Blind Benchmark Suite",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Build a factor-blind, exact-integer benchmark that accepts only N, an independent seed and precommitted public parameters, measures nontrivial-gcd success rather than coordinate concentration, and compares admissible Enterprise candidates against classical baseline methods across adversarial integer families.",
  "next_action": "After the information-leakage audit freezes the admissible input surface, implement the corpus generator, sealed runner, exact metrics and baseline methods, then validate that no execution path or tuning field reads the hidden factorization.",
  "dependencies": [
    "RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT"
  ],
  "source_refs": [
    "research_tasks/ENTERPRISE_BRC_HALF_COUPLING_BLIND_PADIC_FINGERPRINT_20260826.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "research_tasks/PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF_20260826.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "research_tasks/HIGHDIM_PRIME_WALL_FILTER_ALGEBRA_EQUIVALENCE_AUDIT_20260823.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "research_tasks/PRIME_FUSION_FINAL_SOURCE_REPAIR_AND_PACKAGE_FREEZE_20260824.md@8e8ec2fde8adeb4c75580075d63ac76adc562536"
  ],
  "evidence_status": "PROGRAM_SYNTHESIS_PREPUBLICATION / EXACT_INPUT_MODEL_REQUIRED",
  "last_progress_ref": "Published under ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION/OG-AA2BAD92F59DC97880C7 as part of PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827.",
  "last_progress_at": "2026-08-27T05:17:03+00:00",
  "hard_block": [
    "RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT"
  ],
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
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
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

Status: `PUBLISHED_REGISTERED / BLOCKED / PROGRAM PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`

## Mother question

Can every admissible Enterprise candidate be evaluated under a sealed interface
\[
\operatorname{Run}(N,s,\theta_{\mathrm{public}})
\]
whose only successful outcome is an integer \(d\) satisfying
\[
1<d<N,\qquad d\mid N,
\]
with all seeds and public parameters fixed independently of the hidden factorization?

## Frozen inputs and scope

This task remains blocked until the information-leakage audit returns its admissible observable registry. The runner must accept only \(N\), an independent seed, a fixed algorithm identifier and public parameters frozen before the factorization is exposed to the runner.

The corpus must include balanced and unbalanced semiprimes, near-twin factors, prime powers, products of three or more primes, Carmichael numbers, strong pseudoprime families, and coordinate-collision cases identified by the audit. Small instances may retain factors solely in a sealed verifier that is inaccessible to the candidate algorithm.

Implement exact-integer baselines for trial division, Fermat-style search, Pollard rho and Pollard \(p-1\); an ECM-style baseline may be included when its implementation and parameter policy are fixed independently. Record bit operations or a precisely stated machine-cost proxy, memory, seeds used, nontrivial-gcd rate and failure class. Visual or descriptive metrics are secondary diagnostics only.

## Hard target and required outputs

Hard target: `NBLIND_FACTORIZATION_BENCHMARK_SUITE_FROZEN`.

Required outputs:

1. A deterministic corpus generator with independent factor-generation and candidate-execution compartments.
2. A sealed candidate interface that rejects factor inputs, factor-derived phases, adaptive answer-dependent tuning and unbounded implicit scans.
3. Exact baseline implementations and a versioned parameter manifest.
4. A corpus spanning the required adversarial families and multiple bit-length bands.
5. Primary metrics: nontrivial-gcd success probability, operations per successful split, memory, preprocessing, seed amplification and failure-family distribution.
6. A leakage test that deliberately injects forbidden factor fields and verifies rejection.
7. A replay manifest and machine-readable result schema usable by later candidate tasks without modifying the benchmark.
8. A durable return at `research_returns/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_RETURN_20260827.md`.

The suite may report that all current candidates fail. It must not modify a candidate to improve its score inside the same sealed run.

## Research value to preserve

The coordinate program needs a common falsification surface. A benchmark whose target is “prime concentration” or “correct classification after the factors are known” cannot distinguish genuine extraction from descriptive structure.

A factor-blind suite also preserves negative knowledge: it records which integer families synchronize the observables, which parameters leak answers, and which geometric depths are exponential in input length.

## Success, kill, and return criteria

Freeze exactly one primary verdict:

- `BENCHMARK_FROZEN_AND_SEALED` — the corpus, runner, verifier, baselines and schemas pass the leakage and replay tests;
- `BENCHMARK_PARTIAL_WITH_EXACT_BLOCKER` — one required family or baseline cannot be implemented without an exact missing dependency;
- `BENCHMARK_INTERFACE_INVALID` — the proposed sealed separation cannot prevent factor access, with an exact redesign requirement.

Success requires two independent checks that the candidate process cannot read hidden factors and that every claimed split is verified by exact division. The task stops when the suite is frozen; it does not rank mathematical truth or declare a factorization theorem.

## Queue interface

- Program: `PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`.
- Requested priority/leverage: `P1 / HIGH`.
- Requested risk tier: `HIGH`.
- Dependency gate: `["RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT"]`.
- First executable action: After the information-leakage audit freezes the admissible input surface, implement the corpus generator, sealed runner, exact metrics and baseline methods, then validate that no execution path or tuning field reads the hidden factorization.
- Task-terminal return resumes program-level dependency evaluation; this task does not by itself close the program.

## Result return contract

Return one durable report at `research_returns/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_RETURN_20260827.md` with:

1. the primary verdict token;
2. exact theorem, counterexample, computation or no-go statement;
3. source and dependency pins;
4. artifacts and checker paths;
5. remaining assumptions and smallest unresolved unit;
6. a downstream transition recommendation for the program state file.
