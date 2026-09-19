<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PFSS-JUSTIFIED-NONDEGENERATE-NULL-MECHANISM",
  "title": "PFSS: justified nondegenerate null mechanism",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Two independently checked task returns show that the frozen second-order null degenerates on required observables and that finite structural constraints do not identify a probability law. The missing object is a scientifically justified stochastic or invariance mechanism that yields a nondegenerate law without fitting exposed residual outcomes.",
  "next_action": "Inventory admissible random mechanisms/invariance premises and test each against shared-q consistency, support nondegeneracy and source provenance before defining any new statistic or touching preserved holdouts.",
  "dependencies": [],
  "source_refs": [
    "research_result_records/RS-PRIME-FACTOR-SEMIPRIME-SHELL-SECOND-ORDER-DENSITY-NULL/RR-9F084B92BE8261F3A8D7.json",
    "research_result_records/RS-PFSSV-FINITE-WINDOW-NULL-IDENTIFIABILITY/RR-4760E87D1D3AD2F6AFFA.json",
    "driver_reviews/PFSS2_NULL_MISSPECIFICATION_DRIVER_REVIEW_20260917.md",
    "driver_reviews/PFSSV_FINITE_WINDOW_NULL_IDENTIFIABILITY_DRIVER_REVIEW_20260917.md"
  ],
  "evidence_status": "DRIVER_REVIEWED_INTEGRATION_HOLDOUTS_PRESERVED",
  "hard_block": null,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PFSS-JUSTIFIED-NONDEGENERATE-NULL-MECHANISM",
  "parent_objective_id": "PROGRESSIVE_PLANE_PRIME_SEMIPRIME_COORDINATE_DISCOVERY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFSS-ND",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# PFSS: justified nondegenerate null mechanism

## Mother question

Is there a source-defensible stochastic mechanism or invariance premise for the exposed prime/semiprime finite-window carrier that both respects shared q-address identity and produces a nondegenerate law for the shell observables, without choosing the law by fit to the already exposed residual outcomes?

## Frozen inputs and scope

Freeze RR-9F084B92BE8261F3A8D7 and RR-4760E87D1D3AD2F6AFFA with their 2026-09-17 Driver reviews. Preserve the unopened X=3e8 and X=1e9 holdouts: this task must not enumerate or evaluate them. The 21 historical corrected cells and all previously exposed discovery layers are nonblind context. P000 supplies ontology constraints only; it supplies no prime-process probability law.

Use BRC first-line structure discipline to state the carrier, support, fibres, quotient-compatible symmetries, shared-address consistency and observer map before probability is introduced. BRC applicability ends where a probability law requires an additional invariance or random mechanism not derivable from those structural data.

Admissible candidates may include mathematically stated exchangeability groups, conditioning/randomization mechanisms, or externally justified stochastic models, but every candidate must identify its source and exact assumptions. A familiar null model is not accepted merely because it is convenient.

## Hard target and required outputs

Hard target: JUSTIFIED_NONDEGENERATE_NULL_MECHANISM_ACCEPTED_OR_EXACTLY_OBSTRUCTED.

Deliver: (1) a typed carrier/fibre/observer specification; (2) a candidate-mechanism table with source, assumptions, preserved quantities, broken quantities and exposure status; (3) for every surviving candidate, an exact or replayable proof that required discovery observables have nonzero support variance where the later statistic would use them; (4) a shared-q consistency proof; (5) a proof or explicit assumption statement for the relevant invariance/exchangeability premise; (6) at least one discriminating counterexample against an invalid convenient law; (7) a terminal return choosing ACCEPTED_MECHANISM, NEGATIVE_BOUNDARY, or BLOCKED_SOURCE_GAP.

No new family-wise residual statistic, feature selection or holdout evaluation is part of this task.

## Research value to preserve

The two reviewed results jointly separate three layers that must not be conflated: exact semiprime geometry, a stipulated finite synthetic law, and a scientifically justified null for deterministic prime data. This task preserves that distinction and prevents a third experiment from silently repairing an invalid null after exposure.

## Success, kill, and return criteria

Return ACCEPTED_MECHANISM only if one mechanism has a source-defensible premise, exact shared-address consistency, nondegenerate support for all observables required by the next design, and no parameter chosen from the exposed residual outcome beyond quantities explicitly permitted by the premise.

Return NEGATIVE_BOUNDARY if the admissible source set yields no such mechanism; state the smallest missing premise and close this route without opening holdouts. Return BLOCKED_SOURCE_GAP only when a specific necessary source or artifact is unavailable and name it exactly.

Kill any law justified only by convenience, any variance floor or cell deletion used to manufacture nondegeneracy, any retrospective blindness claim, any use of X=3e8 or X=1e9, and any conversion of a finite synthetic calibration into a theorem or Working Truth about primes.
