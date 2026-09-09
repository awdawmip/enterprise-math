<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GV-PCF-POST-AUDIT-PORTFOLIO-SYNTHESIS",
  "title": "PCF post-correction / prior-art portfolio synthesis",
  "kind": "GOVERNANCE",
  "owner": "governance",
  "base_state": "BLOCKED",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "PCF5 and PCF6 are accepted at narrow frozen strengths. PCF7 awaits an exact zero-probe correction and PCF5/6 await a source-backed prior-art/duplication classification. A mathematical successor must not be chosen until both current tasks receive terminal Driver review.",
  "next_action": "After the PCF7 correction and PCF5/6 prior-art audit each have a terminal current Driver disposition, synthesize the exact surviving factorization interface and decide whether to publish one genuinely N-dependent successor or park/close the line.",
  "dependencies": [
    {
      "task_id": "GV-PCF7-STATEMENT-CORRECTION-DRIVER-REVIEW",
      "required_artifact": "terminal Driver disposition on current PCF7 correction Result"
    },
    {
      "task_id": "GV-PCF5-PCF6-PRIOR-ART-DRIVER-REVIEW",
      "required_artifact": "terminal Driver disposition on current PCF5/PCF6 prior-art Result"
    }
  ],
  "source_refs": [
    "research_artifacts/PCF_PERSISTENT_LINE_DRIVER_20260909/dossier.md",
    "research_artifacts/PCF_PERSISTENT_LINE_DRIVER_20260909/review_ledger.md",
    "research_task_records/GV-PCF7-STATEMENT-CORRECTION-DRIVER-REVIEW/TP2-C5E4206C2B7D933199FF.json",
    "research_task_records/GV-PCF5-PCF6-PRIOR-ART-DRIVER-REVIEW/TP2-2235B3DE0C2AE341184D.json",
    "research_task_records/GV-PCF-PRIME-COORD-FACTOR-PERSISTENT-LINE-DRIVER/TP2-D5F8B97303D440E64FAB.json"
  ],
  "evidence_status": "BLOCKED_ON_TWO_TERMINAL_DRIVER_REVIEW_CHECKPOINTS / NO_SPECULATIVE_SUCCESSOR_AUTHORIZED",
  "last_progress_ref": "research_artifacts/PCF_PERSISTENT_LINE_DRIVER_20260909/dossier.md",
  "last_progress_at": "2026-09-09T06:10:14+00:00",
  "hard_block": {
    "missing_objects": [
      "terminal current Driver disposition for PCF7 correction",
      "terminal current Driver disposition for PCF5/PCF6 prior-art audit"
    ],
    "owner": "GV-PCF-PRIME-COORD-FACTOR-PERSISTENT-LINE-DRIVER",
    "unblock_condition": "Both blocked Driver-review gates have terminal dispositions and the persistent line dossier records their exact immutable review identifiers."
  },
  "tags": [
    "PCF",
    "governance",
    "portfolio-synthesis",
    "N-dependent",
    "blocked"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "GV-PCF-POST-AUDIT-PORTFOLIO-SYNTHESIS",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCFSYN",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# PCF post-correction / prior-art portfolio synthesis

Status: `BLOCKED / PUBLISHED_REGISTERED / DRIVER PORTFOLIO GATE`

## Mother question

After the PCF7 statement repair and the PCF5/PCF6 external antecedent audit are both terminally reviewed through their explicit Driver gates, what exact factorization interface remains genuinely open, and does it justify one new N-dependent bounded research task or a park/closure decision?

## Frozen inputs and scope

This is a GOVERNANCE synthesis task, not a mathematical Result and not an authorization to start a speculative factorization route.

It is blocked until both of these Driver tasks have terminal dispositions on current-generation Results:

- `GV-PCF7-STATEMENT-CORRECTION-DRIVER-REVIEW` / `TP2-C5E4206C2B7D933199FF`;
- `GV-PCF5-PCF6-PRIOR-ART-DRIVER-REVIEW` / `TP2-2235B3DE0C2AE341184D`.

When unblocked, consume the accepted PCF5 and PCF6 reviews, the corrected PCF7 review, and the source-backed prior-art classification. Preserve the exact theorem scopes and all negative boundaries. The public-prefix generic-factor family remains closed. The sealed PCF2 benchmark is not reopened.

The strongest currently named open PCF6 object is `N_ONLY_NONTRIVIAL_IDEMPOTENT_OR_EQUIVALENT_SELECTOR_GENERATOR`. It is a candidate residue to evaluate, not a preapproved theorem or task. Any successor must be genuinely N-dependent and must not merely rename fixed/public-prefix probes.

## Hard target and required outputs

Hard target:

`PCF_POST_AUDIT_PORTFOLIO_EXACTLY_DECIDED`

After both Driver prerequisites are terminal:

1. write an exact synthesis table for PCF5, PCF6 and corrected PCF7: accepted statement, killed family, surviving object/interface, prior-art classification, and any unproved bridge;
2. test whether the surviving N-dependent selector/idempotent residue is materially outside the already-killed or standard antecedent families;
3. choose exactly one primary disposition:
   - publish one bounded N-dependent Researcher task with a discriminating hard target and kill condition;
   - park/close the PCF research line at the current verified negative frontier;
   - escalate one genuine cross-line/shared-semantics decision to the portfolio Owner;
4. if publishing a successor, record why closure and existing tasks/routes were insufficient and why the new task is not a renamed public-prefix route;
5. update the PCF dossier and review ledger so a replacement Driver can continue from the chosen disposition without this conversation.

## Research value to preserve

The purpose of this synthesis is to prevent route proliferation after a sequence of negative and restricted results. PCF5, PCF6 and PCF7 are useful precisely because they rule out or narrow mechanisms. The next task should exist only if the combined evidence isolates a new, discriminating N-dependent interface.

A single explicit portfolio gate is more informative than prepublishing multiple speculative factorization tasks whose premises may disappear after correction or prior-art review.

## Success, kill, and return criteria

SUCCESS is one exact post-audit portfolio disposition with a durable evidence map.

Do not unblock this task from publication alone. Do not infer novelty from `NO_MATERIAL_MATCH`, do not strengthen the accepted PCF5/PCF6 claims, do not reopen public-prefix generic-factor probing, and do not create more than one primary mathematical successor from the same synthesis.

If the prerequisite Driver reviews disagree or remain nonterminal, remain blocked or return the smallest reconciliation obligation rather than choosing a successor from stale evidence.
