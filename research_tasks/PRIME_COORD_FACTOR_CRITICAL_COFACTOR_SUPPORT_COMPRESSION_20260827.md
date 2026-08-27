<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-CRITICAL-COFACTOR-SUPPORT-COMPRESSION",
  "title": "Prime Coordinate Critical-Cofactor Support Compression",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Convert the critical-cofactor table from an all-m structural theorem into an N-blind candidate-support map that contains every prime divisor of N while proving a nontrivial support-size and construction-cost bound, or prove that the current table cannot compress factor search.",
  "next_action": "After the parent critical-cofactor result and the leakage audit are frozen, define the N-native table coordinates and candidate support, prove divisor coverage, derive cardinality and bit-complexity bounds, and independently search for integers whose true factors escape or whose support remains square-root scale.",
  "dependencies": [
    "RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT",
    "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF"
  ],
  "source_refs": [
    "research_tasks/PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF_20260826.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "RELATIONAL_AXIS_CONVENTION.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "THREE_DIMENSIONAL_RELATIONAL_AXIS_CONVENTION.md@8e8ec2fde8adeb4c75580075d63ac76adc562536"
  ],
  "evidence_status": "PROGRAM_SYNTHESIS_PREPUBLICATION / EXACT_INPUT_MODEL_REQUIRED",
  "last_progress_ref": "Published under ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION/OG-AA2BAD92F59DC97880C7 as part of PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827.",
  "last_progress_at": "2026-08-27T05:17:03+00:00",
  "hard_block": [
    "RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT",
    "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF"
  ],
  "tags": [
    "prime-coordinate",
    "factorization",
    "n-blind",
    "gcd-extraction",
    "pcf5"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-CRITICAL-COFACTOR-SUPPORT-COMPRESSION",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF5",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "program_id": "PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827",
  "requested_risk_tier": "HIGH",
  "successor_gate": {
    "new_information_gap": "The all-m critical-cofactor route studies structural rank and determinant behavior, but it does not establish a factor-blind map from an input integer N to a small support containing its unknown prime divisors.",
    "why_parent_result_does_not_close_it": "An all-m determinant or cofactor theorem can certify uniqueness or rank after the table is defined; it does not bound the number of N-derived candidate coordinates or the cost of constructing them without a factor oracle.",
    "discriminating_outcomes": [
      "A coverage theorem and support bound strictly below square-root scale.",
      "A restricted-family compression theorem with explicit excluded families.",
      "An exact lower bound showing the current support is generically square-root scale or worse.",
      "A counterexample showing a true factor can fall outside the proposed N-blind support."
    ],
    "kill_condition": "Any independently verified counterexample to divisor coverage kills the proposed support map. A support whose construction enumerates all candidates up to square root is classified as no algorithmic compression.",
    "alternative_route_or_free_exploration_considered": "The alternative is to use the table only as a proof-side classifier and move extraction effort to the p-adic or Prime-Fusion lanes. A weaker support can still be retained if it provably accelerates one exact family.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task is about the internal all-m cofactor system. The new task has a different deliverable—an N-blind support-size theorem and factor-search interface—and should preserve the parent result without rewriting its target."
  },
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7"
}
-->

# Prime Coordinate Critical-Cofactor Support Compression

Status: `PUBLISHED_REGISTERED / BLOCKED / PROGRAM PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`

## Mother question

Can the critical-cofactor structure define, from an unfactored integer \(N\) alone, a finite coordinate support \(\mathcal F_N\) such that
\[
p\mid N,\ p\text{ prime}\quad\Longrightarrow\quad \operatorname{coord}(p)\in\mathcal F_N,
\]
while both \(|\mathcal F_N|\) and the cost of constructing it are provably smaller than the ordinary \(\sqrt N\) search scale on a nontrivial input family?

## Frozen inputs and scope

The exact critical \(d=m-2\) cofactor system and its parent result are frozen inputs. Do not assume that a row, minor, coordinate or phase containing the true factor is known. Every element of \(\mathcal F_N\) must be generated from \(N\) and public parameters.

Separate three quantities: the mathematical support size, the time needed to construct the support, and the time needed to test or integerize its candidates. State all bounds in the bit length of \(N\). A visually thin filament or table slice is not a compression result if its index set is still \(N^{1/2-o(1)}\) or costly to generate.

The first positive target may be a restricted infinite family. Prime powers and multifactor integers must be included in the coverage analysis even if the strongest bound is first proved for semiprimes.

## Hard target and required outputs

Hard target: `CRITICAL_COFACTOR_NBLIND_SUPPORT_COMPRESSION_PROVED_OR_NO_GO`.

Required outputs:

1. A complete N-blind definition of \(\mathcal F_N\) and the coordinate map used for candidate divisors.
2. A divisor-coverage theorem, restricted-family theorem, or exact counterexample.
3. A cardinality bound for \(|\mathcal F_N|\) and a separate construction-time bound in \(\log N\).
4. A proof that duplicate coordinates, gauge choices and symmetry orbits do not hide the true support cost.
5. Exact treatment of balanced semiprimes, unbalanced semiprimes, prime powers and multifactor inputs.
6. An integerization or candidate-testing interface that can feed the benchmark and gcd-bridge lanes.
7. An independent exact search for missed factors and worst-case support growth.
8. A durable return at `research_returns/PRIME_COORD_FACTOR_CRITICAL_COFACTOR_SUPPORT_COMPRESSION_RETURN_20260827.md`.

The preferred positive milestone is \(|\mathcal F_N|\ll N^{1/2-\varepsilon}\) for an explicit \(\varepsilon>0\), but an exact lower bound or no-go result is an admissible closure.

## Research value to preserve

Cofactor geometry is naturally adjacent to multiplication and therefore may provide a genuine candidate generator. The essential test is not whether a known factor has a special table position, but whether that position can be found from \(N\) inside a provably smaller support.

A negative support theorem will prevent the table from being oversold as a factoring method while preserving its structural mathematics.

## Success, kill, and return criteria

Freeze exactly one primary verdict:

- `SUPPORT_COMPRESSION_PROVED` — coverage and a strict sub-square-root support/construction bound are proved on the stated scope;
- `RESTRICTED_SUPPORT_COMPRESSION_PROVED` — the theorem holds on an explicit infinite family;
- `SUPPORT_COVERAGE_REFUTED` — an exact input has a prime divisor outside the proposed support;
- `SUPPORT_COMPRESSION_NO_GO` — coverage may hold but support size or construction cost is proved not to improve the relevant scale;
- `SUPPORT_FRONTIER_FROZEN` — one smaller unresolved lemma is isolated after exact work.

Any coverage counterexample must be independently recomputed. The task stops after the support theorem or no-go and does not claim an end-to-end factorization algorithm unless the gcd interface is separately proved.

## Queue interface

- Program: `PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`.
- Requested priority/leverage: `P1 / HIGH`.
- Requested risk tier: `HIGH`.
- Dependency gate: `["RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT", "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF"]`.
- First executable action: After the parent critical-cofactor result and the leakage audit are frozen, define the N-native table coordinates and candidate support, prove divisor coverage, derive cardinality and bit-complexity bounds, and independently search for integers whose true factors escape or whose support remains square-root scale.
- Task-terminal return resumes program-level dependency evaluation; this task does not by itself close the program.

## Result return contract

Return one durable report at `research_returns/PRIME_COORD_FACTOR_CRITICAL_COFACTOR_SUPPORT_COMPRESSION_RETURN_20260827.md` with:

1. the primary verdict token;
2. exact theorem, counterexample, computation or no-go statement;
3. source and dependency pins;
4. artifacts and checker paths;
5. remaining assumptions and smallest unresolved unit;
6. a downstream transition recommendation for the program state file.
