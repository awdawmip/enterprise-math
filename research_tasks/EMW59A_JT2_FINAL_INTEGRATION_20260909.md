<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-EMW59A-JT2-FINAL-INTEGRATION",
  "title": "JT2 final integration of verified UR and QTF3 certificates",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The route-level implication to JT2 is not yet a standalone source-faithful proof; both minimal certificates and their compatibility audit remain prerequisites.",
  "next_action": "Once the line Driver binds a positive independent audit and the exact original theorem source, compose the two certificates into a standalone JT2 proof with an explicit assumption and precision ledger.",
  "dependencies": [
    {
      "task_id": "RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT",
      "required_artifact": "accepted uniform proof"
    },
    {
      "task_id": "RS-EMW59A-JT2-QTF3-FIXED-POINT",
      "required_artifact": "accepted p^3 proof or proved equivalent LIFT"
    },
    {
      "task_id": "RS-EMW59A-JT2-INDEPENDENT-CERTIFICATE-AUDIT",
      "required_artifact": "VERIFIED_COMPATIBLE audit and recovered original JT2 source"
    }
  ],
  "source_refs": [
    "research_notes/EMW59A_JT2_COMPLETE_RELEASE_AND_DRIVER_HANDOFF_20260909.md",
    "https://github.com/awdawmip/enterprise-math/blob/587e6ee4a138c34de9d87bc90e06f17d7fe1b910/research_notes/EM_FREE_W59A_JT2_UR_QTF3_STATE_MACHINE_HANDOFF_20260909.md",
    "https://github.com/awdawmip/chatgpt-global-knowledge/blob/f48cd4d076f61a5b804a7617158359e198b2fd5d/journal/progressive-number-theory/2026-09-09/20260909T105443%2B0800-ur-legendre-barycentric-lift.md"
  ],
  "evidence_status": "PREDECESSOR_REPORTED_FRONTIER_WITH_EXPLICIT_PROOF_SOURCE_GAPS",
  "last_progress_ref": "research_notes/EMW59A_JT2_COMPLETE_RELEASE_AND_DRIVER_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T04:11:39.921477+00:00",
  "hard_block": {
    "missing_object": "Positive independent compatibility audit, both accepted proof certificates, and exact original JT2 theorem/reduction sources",
    "owner": "GV-EMW59A-JT2-PERSISTENT-LINE-DRIVER",
    "necessity": "Local proof candidates cannot establish an unspecified or incompatible global target.",
    "unblock_condition": "The activated line Driver records the exact accepted UR/QTF3 revisions, a VERIFIED_COMPATIBLE independent audit, and recovered original JT2/CM0/transversality proof pins; otherwise keep BLOCKED."
  },
  "tags": [
    "JT2",
    "Ramanujan-Legendre",
    "handoff-20260909",
    "RW59JT2"
  ],
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-EMW59A-JT2-FINAL-INTEGRATION",
  "parent_objective_id": "EM-FREE-W59A-JT2-RAMANUJAN-LEGENDRE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RW59JT2",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-EMW59A-JT2-INDEPENDENT-CERTIFICATE-AUDIT",
  "successor_gate": {
    "new_information_gap": "Uniform proof of the original JT2 theorem is a separate logical composition obligation.",
    "why_parent_result_does_not_close_it": "A compatibility audit checks inputs but does not write or certify every implication to the final theorem.",
    "discriminating_outcomes": [
      "full original JT2 proof",
      "conditional theorem with exact residual",
      "source recovery gap",
      "counterexample to a claimed bridge"
    ],
    "kill_condition": "Any unrecovered original conclusion or unmatched normalization prevents an unconditional theorem.",
    "alternative_route_or_free_exploration_considered": "Direct JT2 proof and closing a disproved reduction remain alternatives; the present synthesis is conditional on the two certificate route surviving audit.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The user requires this downstream task to exist before the chat ends; explicit blocking avoids premature execution."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# JT2 final source-faithful integration

## 0. Mother question

After UR-Legendre and QTF3 have compatible verified proof certificates, do they establish the exact original JT2 statement without any extra unproved normalization, changed prime range, or lost valuation?

## 1. Frozen inputs and scope

Read `research_notes/EMW59A_JT2_COMPLETE_RELEASE_AND_DRIVER_HANDOFF_20260909.md` and the returned certificate from `RS-EMW59A-JT2-INDEPENDENT-CERTIFICATE-AUDIT`. The two mathematical inputs remain `RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT` and `RS-EMW59A-JT2-QTF3-FIXED-POINT`. This task is published now at the user's request but starts BLOCKED, not as a claim that the inputs already hold.

The original JT2 statement and definitions must be pinned from a genuine source before integration starts. The current handoff supplies the implication label `JT2 <= UR-Legendre + QTF3 / single-scalar LIFT`, not a full source theorem. Do not invent its missing conclusion. Consume the recovered CM0, transversality and barycentric-lift proofs. Preserve the retired-route boundary and every valuation, first-jet, two-port, and truncation datum needed by composition.

## 2. Hard target and required outputs

1. Freeze and quote the complete original JT2 statement from exact durable source bytes with coefficient ring, prime classes, exceptional primes and normalization.
2. Build an explicit dependency graph from the already completed CM0/transversality/barycentric results, the accepted UR certificate, and the accepted QTF3 or proved equivalent LIFT certificate to that exact target.
3. Write every implication back through `B(t)/p`, `lambda_p`, `Q_m'(1/2)`, and `G_p` with their recovered definitions. Recheck precision loss under division, substitution and differentiation.
4. Produce a standalone theorem-and-proof note and an exact-arithmetic checker with a recorded tested range and boundary cases. Finite checks remain diagnostics rather than the uniform proof.
5. Provide a proof-assistant-ready lemma/dependency manifest. Any formal checker used must preserve the original theorem strength; record the kernel/tool version and all assumptions. Do not claim formal verification from a proof sketch or test run.
6. If composition exposes a new scalar or missing bridge, return its exact statement and a conditional theorem rather than an unconditional JT2 claim.

## 3. Research value to preserve

This closes the logical gap between two local certificates and the original research objective. It preserves both a reproducible standalone argument and an explicit obstruction when the apparent reduction has not actually closed.

## 4. Success, kill, and return criteria

Success is a standalone proof of the exact source JT2 statement, with an independent compatible audit and all dependencies bound to immutable artifacts. Deliver the proof, checks, assumption ledger and formalization manifest for the line Driver's final review.

Return `JT2_PROOF_CANDIDATE`, `CONDITIONAL_JT2`, `EXACT_OBSTRUCTION`, or `SOURCE_GAP`. Kill any composition that silently narrows the original prime domain, changes the target, hides a correction scalar, or treats a conditional dependency as a theorem. A negative result must preserve the valid upstream lemmas and isolate only the broken implication. No source theorem may be invented merely to close the task.
