<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION",
  "title": "Coherent-BRC F7 — Rank-Two Balanced Mixing Existence and Selector Classification (V2 migration)",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_STATUS_CLASSIFIED",
  "next_action": "In a context that has not opened the forbidden pre-freeze mathematical history, claim the migrated task, freeze the execution stamp before opening the blind packet, and independently classify exact balanced reversible two-slot mixing existence and selector status on the F6-minimal rank-two carrier.",
  "dependencies": [
    "research_tasks/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_20260825.md@blob:1215bf9bb950e3b791de8ccb78f9cab476048f7e",
    "research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md@bc046c8d77910ddb1f42b572a736d9d938ecbb9c"
  ],
  "source_refs": [
    "research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md@bc046c8d77910ddb1f42b572a736d9d938ecbb9c"
  ],
  "evidence_status": "LEGACY_F7_MIGRATED_TO_V2_WITH_ZERO_MATH_DELTA / CLEAN_BLIND_CONTEXT_STILL_REQUIRED",
  "tags": ["CBRC","F7","rank-two","two-slot-mixing","balanced","selector-status","blind-forward","v2-migration"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION",
  "parent_objective_id": "COHERENT_BRC_WORKING_EXTENSION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "CBRCF7",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-CBRC-F6-MINIMAL-RANK-TWO-CONSERVATIVE-CARRIER-CLASSIFICATION",
  "successor_gate": {
    "new_information_gap": "F6 fixes the least additive/unary rank-two carrier but deliberately leaves every two-slot mixing operation and scalar selector unclassified.",
    "why_parent_result_does_not_close_it": "Unary triviality of the new free summand neither proves nor refutes existence of a balanced reversible two-slot automorphism and does not determine whether the new free direction must participate.",
    "discriminating_outcomes": "Exact no-go; unique physical class; finitely many physical classes; strict underdetermination; or existence with selector classification still incomplete.",
    "kill_condition": "Freeze immediately on exact no-go, target-leak invalidity, or a complete existence/selector classification; do not escalate to ring, norm, square-law or wave semantics.",
    "alternative_route_or_free_exploration_considered": "A new free direction or later semantic layer could be explored instead, but F6 itself identifies two-slot existence as the first load-bearing unresolved gate and the blind packet allows a direct falsifiable classification without importing downstream targets.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "F6 was frozen with two-slot mixing explicitly outside its accepted scope; reopening F6 would destroy its terminal boundary, whereas F7 isolates exactly the new operation class authorized by the accepted F6 result."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Coherent-BRC F7 — Rank-Two Balanced Mixing Existence and Selector Classification (V2 migration)

Status: `READY / LEGACY-MIGRATION / ZERO-MATH-DELTA`

## Mother question

On the unique least rank-two additive/unary object frozen by the accepted F6 stage, does there exist an exact balanced reversible two-slot additive automorphism with one fixed marked scalar satisfying the blind F7 packet, and if so do those axioms select a unique physical mixing/scalar class or leave genuine underdetermination?

## Frozen inputs and scope

This publication is a post-cutover migration of the 2026-08-25 F7 task, not a new mathematical hypothesis and not a change of target. The mathematical source before raw freeze remains exactly the blind packet `research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md@bc046c8d77910ddb1f42b572a736d9d938ecbb9c`.

The original firewall remains binding: before raw freeze the execution conversation may use the taskbook and repository/governance files for procedure, but must not open historical F3/F3R/F3R2 mixing mathematics, downstream coherent-BRC/wave work, external quantum/wave formalisms, complex/Gaussian/Eisenstein targets, ring/field/multiplicative structure, norms/inner products/quadratic forms, roots-of-unity/phase targets, Hadamard/Fourier/splitter targets, or a known downstream rank-two answer.

A conversation that has already opened forbidden pre-freeze mathematical history is not eligible to claim clean-blind provenance for this task. It must not assert `TARGET_LEAK_AUDIT_PASS`; a clean execution context must perform the raw freeze.

Current runtime procedure supersedes only the legacy publication envelope: after a valid V2 CLAIM, use the CLAIM execution branch and write an execution stamp before opening the blind packet. No mathematical condition from the 2026-08-25 task is weakened or strengthened.

## Hard target and required outputs

Hard target: `RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_STATUS_CLASSIFIED`.

The execution must classify, at exact theorem strength:

1. existence/no-go for balanced reversible rank-two mixing;
2. whether the new free direction may remain spectator or must participate;
3. structural restrictions on the free `GL_4(Z)` block;
4. scalar feasibility and uniqueness/nonuniqueness of the marked scalar;
5. physical equivalence under only the packet-authorized relabeling/orientation/typed-carrier symmetries;
6. the ten legacy mandatory ablations;
7. target-leak status.

Primary verdict must be one of the six verdict classes frozen in the legacy F7 taskbook.

Current-envelope outputs are restricted to:

- `evidence/cbrc_f7_execution_stamp_v2.json`;
- `research_returns/CBRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_RETURN_20260831.md`;
- `research_checks/CBRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_CHECK_20260831.py`;
- `research_artifacts/CBRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION/*`;
- `research_execution_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/*`;
- `research_result_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/*`.

## Research value to preserve

F6 proved that rank two is the unique least additive/unary extension under its frozen order but did not establish that rank two is dynamically used. F7 is the first falsifiable gate that can distinguish a merely available extra free direction from genuinely forced two-slot dynamics, while still forbidding familiar transform targets and richer algebraic structure. Losing this task would sever the accepted F6 frontier from its first authorized operational test.

## Success, kill, and return criteria

Success is an exact existence/selector classification with deterministic checker evidence, explicit inequivalent witnesses for any underdetermination claim, and a clean target-leak audit. A bounded `GL_4(Z)` census is regression evidence only and cannot substitute for a theorem.

Kill/freeze on any exact no-go, proof that the clean-blind firewall was violated, or completion of the declared selector classification. Stop at F7 scope: do not continue into arbitrary torsion-lift membership, multiplication/rings, norms/inner products, square laws, complex/quadratic interpretations, or wave/continuum semantics without a separately published successor.
