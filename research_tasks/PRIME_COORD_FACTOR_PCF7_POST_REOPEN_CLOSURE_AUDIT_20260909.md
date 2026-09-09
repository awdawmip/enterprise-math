<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-PCF7-POST-REOPEN-CLOSURE-AUDIT",
  "title": "PCF7 Post-Reopen Closure and Driver-Review Reconciliation Audit",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The authorized PCF7 mathematical revision is complete in fresh Result RR-E9908FEE020773DEF39C, and the nonterminal reopen ownership defect has already been repaired in the current dispatch implementation. The remaining gap is to classify the post-reopen control state: the fresh Result has no bound Driver review record, while the parent taskbook still carries legacy BLOCKED metadata from before the successful revision.",
  "next_action": "Read the durable PCF7 reconciliation handoff first, then audit the fresh Result, its exact closure artifact, the prior REQUEST_REVISION review/followup, and the current result/dispatch semantics; produce one bounded closure certificate that identifies the unique lawful next control action without reopening completed mathematics or the completed reopen repair.",
  "dependencies": [],
  "source_refs": [
    "research_notes/PCF7_PARENT_REVISION_AND_REOPEN_RECONCILIATION_HANDOFF_20260909.md",
    "research_task_records/RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION/TP2-8F7443BCAF2BC5243574.json",
    "research_result_records/RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION/RR-E9908FEE020773DEF39C.json",
    "research_artifacts/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION/PCF7_PARENT_REVISION_CLOSURE_RETURN_20260906_V2.md",
    "research_result_reviews/RR-A9A5ADD3931B3F3EDFAB/DR-8183213860B7A72A2BD3.json",
    "research_driver_followups/DR-8183213860B7A72A2BD3/DFU-0204BC0AB65CDE176BBC.json",
    "tools/research_dispatch.py",
    "tests/test_research_dispatch_reopen_claim_overlay.py"
  ],
  "evidence_status": "POST_REOPEN_CLOSURE_AUDIT_READY",
  "last_progress_ref": "research_notes/PCF7_PARENT_REVISION_AND_REOPEN_RECONCILIATION_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T09:30:18+08:00",
  "hard_block": "FRESH_RESULT_DRIVER_DISPOSITION_OR_EXACT_POST_REOPEN_CONTROL_CLOSURE",
  "tags": [
    "prime-coordinate",
    "factorization",
    "pcf7",
    "closure-audit",
    "driver-review",
    "post-reopen",
    "control-integration"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-PCF7-POST-REOPEN-CLOSURE-AUDIT",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF7C",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION",
  "successor_gate": {
    "new_information_gap": "A fresh parent-scope revision Result exists after the requested statement correction, and the reopen ownership implementation is repaired, but that fresh Result still has no Driver disposition and the parent task's legacy base metadata does not itself express the post-revision closure frontier.",
    "why_parent_result_does_not_close_it": "RR-E9908FEE020773DEF39C explicitly leaves Driver review and control integration unresolved and does not carry authority to issue a Driver disposition or terminalize the parent control state.",
    "discriminating_outcomes": [
      "The evidence shows that Driver review of RR-E9908FEE020773DEF39C is the only remaining lawful action and no new research residue exists.",
      "The evidence exposes one concrete post-reopen control inconsistency requiring a bounded reconciliation artifact before Driver review can act.",
      "A genuinely new task-local residue is identified with exact evidence and scope; absent such a residue, continuation stops at closure review."
    ],
    "kill_condition": "Stop without opening further research if the current durable records already determine a unique lawful closure path and no unresolved mathematical or control question remains inside PCF7.",
    "alternative_route_or_free_exploration_considered": "Direct closure and return to the parent objective were considered first. Free exploration is not justified because the unresolved gap is a bounded authority/state question, not an open mathematical search problem.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "A separate bounded audit keeps the completed proof and completed reopen repair immutable while producing one review-ready control certificate; editing the parent proof again would mix already-closed mathematics with a distinct authority-state residue."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# PCF7 Post-Reopen Closure and Driver-Review Reconciliation Audit

Status: `READY / POST-REOPEN CLOSURE AUDIT / PUBLISHED_REGISTERED`

## 0. Mother question

Given the fresh successful parent-scope revision Result `RR-E9908FEE020773DEF39C` and the already repaired nonterminal reopen ownership semantics, what is the unique current PCF7 closure state, and what exact evidence packet is sufficient for the next authorized Driver disposition without reopening completed mathematics?

## 1. Frozen inputs and scope

Read `research_notes/PCF7_PARENT_REVISION_AND_REOPEN_RECONCILIATION_HANDOFF_20260909.md` first. Treat the parent publication, the fresh Result, its closure return, the earlier `REQUEST_REVISION` review/followup, and the current dispatch implementation/tests listed in `source_refs` as the frozen evidence set.

The mathematical revision boundary is closed for this task: nonzero fixed probes may be arranged to return gcd `1`, the zero probe returns gcd `N`, and therefore the fixed finite probe family yields only trivial outputs `{1,N}` and no proper factor on the constructed semiprimes. The polynomial-prefix, `L=N`, `T1-T5`, sealed-benchmark, and other unchanged parent conclusions are read-only premises here.

The control repair that preserves a reducer-accepted live lease through a nonterminal reopen is also read-only. This task may test and classify its consequences for PCF7, but must not redesign that implementation or broaden its authority semantics.

No factor-aware, result-sensitive, answer-dependent, factor-oracle, or hidden-factor branch may be relabeled as factor-blind. No new factorization theorem, lower bound, benchmark result, or project-level truth status may be inferred from a closure-state audit.

## 2. Hard target and required outputs

Hard target: `PCF7_POST_REOPEN_CLOSURE_STATE_UNIQUELY_CLASSIFIED`.

Deliver all of the following, or an exact negative boundary for an impossible item:

1. A chronological evidence table from the parent publication through the prior revision request, correction followup, fresh successful Result, and current reopen semantics, with every conclusion tied to a durable repository object.
2. A machine-checkable determination of whether `RR-E9908FEE020773DEF39C` has a bound Driver review/disposition. Absence must be proved by the authoritative record surface used by the project, not by filename guessing alone.
3. A state-classification proof distinguishing completed mathematical scope, completed control repair, pending Driver authority, and any truly unresolved task-local residue.
4. A consistency check showing that a valid live post-review owner is preserved by the current nonterminal reopen overlay, while a claimless reopen remains dispatchable, using the existing focused regression surface rather than inventing a second implementation.
5. A closure certificate at `research_artifacts/PRIME_COORD_FACTOR_PCF7_POST_REOPEN_CLOSURE_AUDIT/PCF7_POST_REOPEN_CLOSURE_AUDIT_CERTIFICATE_20260909.json` identifying exactly one of: `DRIVER_REVIEW_ONLY`, `BOUNDED_CONTROL_RECONCILIATION_REQUIRED`, or `NEW_RESEARCH_RESIDUE_PROVED`.
6. A checker at `research_checks/PCF7_POST_REOPEN_CLOSURE_AUDIT_CHECK_20260909.py` that fails if the certificate reopens the fixed-probe mathematics, treats the prior repair as unfinished, or asserts Driver authority not present in the evidence.
7. A durable return at `research_returns/PCF7_POST_REOPEN_CLOSURE_AUDIT_RETURN_20260909.md` that gives the exact next authorized control action and stops there.

## 3. Research value to preserve

PCF7 now contains two different kinds of completed work that must not be confused with the remaining authority gap: a narrow mathematical correction and a runtime reopen repair. Preserving their exact boundary prevents future researchers from repeating either task and turns the remaining uncertainty into a finite auditable question.

A negative audit is valuable: if the only remaining action is Driver review of the fresh Result, proving that fact eliminates duplicate research and provides a clean handoff. A positive audit is also valuable if it exposes one concrete control inconsistency, provided the inconsistency is stated narrowly and does not mutate the closed mathematical result.

## 4. Success, kill, and return criteria

Success is a single evidence-backed classification of the PCF7 post-reopen state, with the certificate and checker agreeing on the next authorized action. The preferred terminal form is `DRIVER_REVIEW_ONLY` if no independent unresolved residue is proved.

Kill any route that edits or reproves the fixed-probe theorem, repeats the completed reopen implementation repair, treats absence of a review as permission to issue one, changes sealed benchmark content, or broadens factor-blind scope through answer-dependent information.

Return immediately once the evidence distinguishes completed mathematics, completed reopen repair, and the remaining authority/control state. If no further research residue survives that distinction, do not manufacture a successor; hand the fresh Result to the authorized review layer and stop.