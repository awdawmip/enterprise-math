<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION",
  "title": "Prime Coordinate Factorization Complexity and Failure Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "For every factor-blind extractor or support candidate surviving the earlier lanes, derive rigorous bit-complexity, memory, seed-amplification and failure-family classifications, distinguishing polynomial, subexponential, square-root-scale and merely descriptive behavior.",
  "next_action": "After the sealed benchmark and at least one candidate lane return a precise algorithmic object, decompose every arithmetic and coordinate operation into bit costs, prove success-amplification bounds, and classify adversarial integer families against both theorem assumptions and exact runs.",
  "dependencies": [
    "RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE",
    "ONE_OF:RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE|RS-PRIME-COORD-FACTOR-CRITICAL-COFACTOR-SUPPORT-COMPRESSION|RS-PRIME-COORD-FACTOR-PRIME-FUSION-NBLIND-REALIZATION"
  ],
  "source_refs": [
    "research_tasks/ENTERPRISE_BRC_HALF_COUPLING_BLIND_PADIC_FINGERPRINT_20260826.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "research_tasks/PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF_20260826.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "research_tasks/PRIME_FUSION_FINAL_SOURCE_REPAIR_AND_PACKAGE_FREEZE_20260824.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "research_tasks/HIGHDIM_PRIME_WALL_FILTER_ALGEBRA_EQUIVALENCE_AUDIT_20260823.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "research_tasks/PRIME_NATIVE_FILAMENT_SHARP_BOUND_INDEPENDENT_REPLICATION_20260823.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "research_tasks/NATIVE_SHELL_GRADE_MONOTONE_INTEGER_ALLOCATION_FOUNDATION_AUDIT_20260827.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "research_tasks/NATIVE_TRISECTOR_P0P1_ARITHMETIC_BRIDGE_FOUNDATION_GENERATIVITY_20260826.md@8e8ec2fde8adeb4c75580075d63ac76adc562536"
  ],
  "evidence_status": "PROGRAM_SYNTHESIS_PREPUBLICATION / EXACT_INPUT_MODEL_REQUIRED",
  "last_progress_ref": "Published under ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION/OG-AA2BAD92F59DC97880C7 as part of PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827.",
  "last_progress_at": "2026-08-27T05:17:03+00:00",
  "hard_block": [
    "RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE",
    "ONE_OF:RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE|RS-PRIME-COORD-FACTOR-CRITICAL-COFACTOR-SUPPORT-COMPRESSION|RS-PRIME-COORD-FACTOR-PRIME-FUSION-NBLIND-REALIZATION"
  ],
  "tags": [
    "prime-coordinate",
    "factorization",
    "n-blind",
    "gcd-extraction",
    "pcf7"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF7",
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

# Prime Coordinate Factorization Complexity and Failure Classification

Status: `PUBLISHED_REGISTERED / BLOCKED / PROGRAM PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`

## Mother question

Given a factor-blind candidate constructor \(A(N,s)\) from the p-adic, support-compression or Prime-Fusion lane, what is its true cost as a function of
\[
n=\lceil\log_2 N\rceil,
\]
and on which arithmetic families does its extraction probability vanish, decay, or remain amplifiable?

## Frozen inputs and scope

This task begins only after the benchmark suite is frozen and at least one candidate lane returns an exact constructor, support map or no-go theorem with measurable operations.

Count modular multiplication, gcd, integer growth, denominator clearing, matrix or carrier dimension, coordinate traversal, seed trials and preprocessing. Convert all geometric scales to functions of \(n\). Separate one-time precomputation independent of \(N\) from input-dependent work.

Classify balanced and unbalanced semiprimes, near-twin factors, prime powers, multifactor inputs, Carmichael and strong pseudoprime families, synchronized coordinate sectors, equal shell/filament responses and any candidate-specific exceptional congruence classes. Compare against the frozen baseline suite under the same cost model.

## Hard target and required outputs

Hard target: `FACTOR_ALGORITHM_COMPLEXITY_AND_FAILURE_CLASSIFIED`.

Required outputs:

1. A line-by-line bit-complexity derivation for each surviving candidate.
2. Memory and intermediate-integer growth bounds.
3. A seed-success and amplification theorem, or an exact statement that no useful lower bound is available.
4. A classification into polynomial, subexponential, square-root-scale, worse-than-baseline or descriptive-only regimes.
5. A failure-family atlas tied to exact assumptions and benchmark evidence.
6. Direct comparisons with the frozen baselines using one common metric and no answer-dependent tuning.
7. A theorem-ready assumption package for formalization, with every empirical premise excluded or typed separately.
8. A portfolio recommendation identifying which candidate should advance, remain restricted, or close as a no-go.
9. A durable return at `research_returns/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_RETURN_20260827.md`.

A coordinate step count without bit-cost conversion is not an accepted complexity result.

## Research value to preserve

The program can be structurally close to factorization while remaining exponentially far in input length. This task makes that distinction explicit and prevents a thin geometric support from being credited before its construction and testing costs are counted.

The failure atlas is also reusable: it supplies adversarial families for every later algorithmic claim and may reveal which second observable is needed to break synchronization.

## Success, kill, and return criteria

Freeze exactly one primary verdict per candidate and one portfolio verdict:

- `POLYNOMIAL_OR_SUBEXPONENTIAL_BOUND_PROVED`;
- `STRICT_SUB_SQRT_BOUND_PROVED`;
- `SQRT_SCALE_OR_WORSE_PROVED`;
- `SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED`;
- `DESCRIPTIVE_ONLY_AFTER_COST_AUDIT`;
- `COMPLEXITY_FRONTIER_FROZEN`.

Every asymptotic claim must include its input family, seed model and arithmetic cost assumptions. The task stops after the portfolio classification and formalization assumption package are frozen.

## Queue interface

- Program: `PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`.
- Requested priority/leverage: `P1 / HIGH`.
- Requested risk tier: `HIGH`.
- Dependency gate: `["RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE", "ONE_OF:RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE|RS-PRIME-COORD-FACTOR-CRITICAL-COFACTOR-SUPPORT-COMPRESSION|RS-PRIME-COORD-FACTOR-PRIME-FUSION-NBLIND-REALIZATION"]`.
- First executable action: After the sealed benchmark and at least one candidate lane return a precise algorithmic object, decompose every arithmetic and coordinate operation into bit costs, prove success-amplification bounds, and classify adversarial integer families against both theorem assumptions and exact runs.
- Task-terminal return resumes program-level dependency evaluation; this task does not by itself close the program.

## Result return contract

Return one durable report at `research_returns/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_RETURN_20260827.md` with:

1. the primary verdict token;
2. exact theorem, counterexample, computation or no-go statement;
3. source and dependency pins;
4. artifacts and checker paths;
5. remaining assumptions and smallest unresolved unit;
6. a downstream transition recommendation for the program state file.
