<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "EM-FREE-7D3C9A-ISSUE1255-VIETE-X6-ROTATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-EM7D3C9A-1255-PATH-DAGGER-CATEGORY",
  "title": "X6 concrete rotation-path dagger category and safe groupoid quotient audit",
  "frontier": "The current concrete rotation-path carrier correctly retains primitive Cell path history and composes by literal concatenation, but its V2 groupoid naming is too strong: reversing a nonempty concrete path produces a backtracking loop under concatenation, not the empty identity. The provenance-preserving object should be a dagger/path category unless an explicit cancellation or homotopy quotient is defined and proved observer-safe.",
  "next_action": "Start from the state-machine handoff and X6_ROTATION_PATH_DAGGER_AND_BRANCH_JET_V3_20260909.md; formalize the concrete path category and dagger laws, then audit every use of true inverse in the V2 rotation-path note and identify the strongest safe quotient, if any, that is genuinely a groupoid.",
  "dependencies": [],
  "source_refs": [
    "research_notes/VIETE_X6_ROTATION_STATE_MACHINE_HANDOFF_20260909.md",
    "research_notes/X6_ROTATION_PATH_DAGGER_AND_BRANCH_JET_V3_20260909.md",
    "research_notes/X6_ROTATION_PATH_GROUPOID_V2_20260906.md",
    "research_notes/X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md",
    "experiments/x6_rotation_path_dagger_jet_20260909/check_rotation_path_dagger_jet.py",
    "research-commit:9323a0a39199d780439b4e64cbe2506ec824fe60",
    "research-commit:40996d9239309bc703435ffc3d814932638b0e94"
  ],
  "evidence_status": "EXACT_TYPE_CORRECTION_AND_FINITE_CHECKER_AVAILABLE",
  "last_progress_ref": "research_notes/VIETE_X6_ROTATION_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T11:09:00+08:00",
  "hard_block": "CONCRETE_PATH_INVERSE_TYPING_AND_SAFE_CANCELLATION_QUOTIENT",
  "tags": ["issue-1255", "X6", "rotation-path", "dagger-category", "groupoid", "BRC", "provenance"],
  "registry_key": "RS-EM7D3C9A-1255-PATH-DAGGER-CATEGORY",
  "identity_lane": "R7D3DAG",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# X6 concrete rotation-path dagger category and safe groupoid quotient audit

Status: `READY / FREE-RESEARCH TYPE REPAIR`

## Mother question

What is the exact categorical type of the provenance-preserving X6 rotation-path carrier when morphisms are concrete primitive Cell paths and composition is literal concatenation, and under which explicitly typed quotient, if any, does a true groupoid emerge without erasing future-observable path information?

## Frozen inputs and scope

Read `research_notes/VIETE_X6_ROTATION_STATE_MACHINE_HANDOFF_20260909.md` first. Consume the V2 rotation-path carrier rather than rebuilding it. Keep concrete path history, branch identity, length and primitive signed-axis steps distinct from the frame/action quotient.

The exact correction already established is:

`CONCRETE_PATH_REVERSAL = DAGGER/INVOLUTION`, not a categorical inverse under literal concrete-path equality.

A forward path followed by its reverse is a nonempty backtracking loop. Do not remove it unless the proposed future-operation lease proves that the removal is safe.

## Hard target and required outputs

Hard target: `X6_ROTATION_PATH_DAGGER_CATEGORY_AND_SAFE_GROUPOID_QUOTIENT_EXACTLY_TYPED`.

Deliver one exact package that:

1. Defines objects, concrete path arrows, source/target, literal composition, empty identities and dagger/reversal.
2. Proves associativity, identity laws, dagger involution and reversal of composition.
3. Proves explicitly why `f^dagger o f` is generally not the concrete identity.
4. Audits `X6_ROTATION_PATH_GROUPOID_V2_20260906.md` and downstream consumers for statements that actually require true inverses versus only reversal/dagger.
5. If proposing a cancellation, reduction or homotopy quotient, defines the equivalence relation and proves composition compatibility.
6. Runs the BRC observer/provenance-loss gate: declare future operations, then prove fiber constancy before erasing backtracking loops or branch history.
7. Determines the strongest exact quotient that is genuinely a groupoid; a no-go showing that no nontrivial quotient is safe for the declared rich observer is acceptable.
8. Supplies executable/formal evidence at the strongest practical level and records any consumer retyping needed.

## Research value to preserve

This repair sits below all later rotation-law, path-jet and native-time work. Leaving a concrete-history carrier mislabeled as a groupoid silently forces path cancellation and can destroy exactly the loop/provenance information that BRC requires. A clean dagger/category layer lets later researchers distinguish reversible traversal from observer-safe cancellation.

## Success, kill, and return criteria

Success is an exact categorical repair plus a typed quotient theorem or exact no-go. Preserve the existing useful path carrier and frame action; do not discard them merely because the word `groupoid` was too strong.

Kill any proof that obtains inverses only by silently identifying a nonempty backtracking path with the empty path. Matching endpoints or frame elements is not enough for path equality.

Return the smallest corrected interface that downstream rotation research can consume without ambiguity, together with the exact observer lease for any quotient that erases concrete path history.
