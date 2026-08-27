<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-LEAN-GCD-EXTRACTION-FORMALIZATION",
  "title": "Prime Coordinate Blind GCD Extraction Lean Formalization",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Formalize the minimal factor-blind extraction chain from an N-native constructor through CRT-local asymmetry to a nontrivial gcd, using only assumptions frozen by the proof and complexity lanes and without formalizing unrelated geometry.",
  "next_action": "After the gcd-bridge and complexity tasks freeze exact theorem statements, translate the constructor and local divisibility hypotheses into Lean, prove the gcd extraction lemmas and restricted end-to-end theorem, and build with no sorry, admit or custom axiom.",
  "dependencies": [
    "RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE",
    "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION"
  ],
  "source_refs": [
    "research_tasks/PRIME_FUSION_F1_LEAN_FINITE_ALGEBRA_FORMALIZATION_20260824.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "research_tasks/ENTERPRISE_BRC_HALF_COUPLING_BLIND_PADIC_FINGERPRINT_20260826.md@8e8ec2fde8adeb4c75580075d63ac76adc562536",
    "PACKET_PATH_FOUNDATION.md@8e8ec2fde8adeb4c75580075d63ac76adc562536"
  ],
  "evidence_status": "PROGRAM_SYNTHESIS_PREPUBLICATION / EXACT_INPUT_MODEL_REQUIRED",
  "last_progress_ref": "Published under ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION/OG-AA2BAD92F59DC97880C7 as part of PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827.",
  "last_progress_at": "2026-08-27T05:17:03+00:00",
  "hard_block": [
    "RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE",
    "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION"
  ],
  "tags": [
    "prime-coordinate",
    "factorization",
    "n-blind",
    "gcd-extraction",
    "pcf8"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-LEAN-GCD-EXTRACTION-FORMALIZATION",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF8",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "program_id": "PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827",
  "requested_risk_tier": "MEDIUM",
  "successor_gate": {
    "new_information_gap": "A mathematical gcd-bridge theorem, even when proved on paper, still needs a machine-checked separation between N-native computation, CRT-local hypotheses and the final nontrivial-gcd conclusion.",
    "why_parent_result_does_not_close_it": "The parent task supplies the arithmetic construction and proof. It does not provide a Lean theorem with pinned assumptions, build guards and no-sorry validation.",
    "discriminating_outcomes": [
      "A no-sorry formalization of the restricted end-to-end extractor theorem.",
      "A formalization of the abstract gcd bridge with one precisely isolated unformalized arithmetic lemma.",
      "An exact type or dependency obstruction showing the frozen theorem statement is underspecified.",
      "A regression counterexample to an overstrong theorem statement."
    ],
    "kill_condition": "Any hidden factor input in the formalized constructor or any weakening that replaces a nontrivial gcd conclusion by a descriptive local statement invalidates the target. Sorry, admit and custom axioms are forbidden.",
    "alternative_route_or_free_exploration_considered": "The alternative is to formalize only the abstract gcd lemma and leave the candidate-specific arithmetic theorem for later. Full geometry formalization is intentionally excluded unless the frozen extractor theorem requires it.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The proof task should freeze mathematics and complexity assumptions first. A separate formalization lane can then preserve those exact statements without expanding or silently changing the research target."
  },
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7"
}
-->

# Prime Coordinate Blind GCD Extraction Lean Formalization

Status: `PUBLISHED_REGISTERED / BLOCKED / PROGRAM PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`

## Mother question

Can the proved restricted extractor be represented in Lean as a function whose executable inputs contain only \(N\), a seed and public parameters, while the theorem proves from explicit factor hypotheses that its output residue has a nontrivial gcd with \(N\)?

## Frozen inputs and scope

This task remains blocked until the gcd-bridge lane freezes an exact constructor/theorem and the complexity lane freezes the theorem-ready assumption package. Formalize only the minimum chain needed for extraction:

1. the N-native constructor or its exact abstract interface;
2. proof-side factorization hypotheses for \(N=pq\);
3. one-sided divisibility or valuation asymmetry;
4. the conclusion \(1<\gcd(G,N)<N\), or the corresponding exact factor equality.

Do not formalize the full coordinate, BRC or Prime Fusion universe unless a definition is logically required by the frozen theorem. Preserve existing corrected universes and regression guards where reused. No `sorry`, `admit`, custom axiom or silently weakened theorem is permitted.

## Hard target and required outputs

Hard target: `LEAN_BLIND_GCD_EXTRACTION_NO_SORRY_BUILD_PASS`.

Required outputs:

1. A Lean module with the abstract nontrivial-gcd extraction lemmas.
2. A Lean representation of the frozen N-native constructor or a precisely typed interface to it.
3. The strongest restricted end-to-end theorem supported by the parent proof.
4. Explicit separation between executable inputs and proof-only factor witnesses.
5. Regression examples covering success, synchronized failure and degenerate input guards.
6. A clean build under the pinned Enterprise Math toolchain with warnings treated as failures.
7. A dependency note identifying any arithmetic theorem imported rather than reproved.
8. A durable return at `research_returns/PRIME_COORD_FACTOR_LEAN_GCD_EXTRACTION_FORMALIZATION_RETURN_20260827.md`.

If one arithmetic lemma remains outside current library coverage, formalize the entire surrounding bridge and freeze that lemma exactly rather than replacing it with an axiom.

## Research value to preserve

The main formal risk is not elementary gcd algebra; it is accidental factor leakage in the constructor or a theorem statement that assumes the desired local split. A narrow formal model makes those boundaries reviewable.

Deferring broad geometry formalization preserves effort until an actual extraction theorem identifies the load-bearing definitions.

## Success, kill, and return criteria

Freeze exactly one primary verdict:

- `LEAN_END_TO_END_EXTRACTOR_CHECKED` — the restricted extractor theorem builds with no gaps;
- `LEAN_ABSTRACT_GCD_BRIDGE_CHECKED` — the generic bridge is complete and one candidate-specific arithmetic lemma is frozen externally;
- `FORMAL_STATEMENT_UNDERSPECIFIED` — the parent theorem lacks a type-correct constructor or explicit assumptions;
- `FORMALIZATION_BLOCKED_BY_LIBRARY_GAP` — one exact library lemma is missing after the rest is checked.

Success requires a clean pinned build and no theorem weakening. The task stops after the strongest checked theorem and exact residual gap are frozen.

## Queue interface

- Program: `PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`.
- Requested priority/leverage: `P2 / MEDIUM`.
- Requested risk tier: `MEDIUM`.
- Dependency gate: `["RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE", "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION"]`.
- First executable action: After the gcd-bridge and complexity tasks freeze exact theorem statements, translate the constructor and local divisibility hypotheses into Lean, prove the gcd extraction lemmas and restricted end-to-end theorem, and build with no sorry, admit or custom axiom.
- Task-terminal return resumes program-level dependency evaluation; this task does not by itself close the program.

## Result return contract

Return one durable report at `research_returns/PRIME_COORD_FACTOR_LEAN_GCD_EXTRACTION_FORMALIZATION_RETURN_20260827.md` with:

1. the primary verdict token;
2. exact theorem, counterexample, computation or no-go statement;
3. source and dependency pins;
4. artifacts and checker paths;
5. remaining assumptions and smallest unresolved unit;
6. a downstream transition recommendation for the program state file.
