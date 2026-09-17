<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PFSS-NONDEGENERATE-NULL-PREFLIGHT",
  "title": "PFSS: nondegenerate-null statistic and support preflight",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "A future blind-forward screen cannot be specified until an accepted justified mechanism exists. Once it does, the next missing unit is a discovery-only preflight proving that the exact statistic is defined and nondegenerate before any preserved holdout is opened.",
  "next_action": "After RS-PFSS-JUSTIFIED-NONDEGENERATE-NULL-MECHANISM returns ACCEPTED_MECHANISM, instantiate that exact mechanism on exposed discovery scales only and prove support/variance/statistic definability before freezing any later holdout protocol.",
  "dependencies": ["RS-PFSS-JUSTIFIED-NONDEGENERATE-NULL-MECHANISM"],
  "source_refs": [
    "research_result_records/RS-PRIME-FACTOR-SEMIPRIME-SHELL-SECOND-ORDER-DENSITY-NULL/RR-9F084B92BE8261F3A8D7.json",
    "research_result_records/RS-PFSSV-FINITE-WINDOW-NULL-IDENTIFIABILITY/RR-4760E87D1D3AD2F6AFFA.json",
    "driver_reviews/PFSS2_NULL_MISSPECIFICATION_DRIVER_REVIEW_20260917.md",
    "driver_reviews/PFSSV_FINITE_WINDOW_NULL_IDENTIFIABILITY_DRIVER_REVIEW_20260917.md",
    "research_tasks/RS-PFSS-JUSTIFIED-NONDEGENERATE-NULL-MECHANISM_20260917.md"
  ],
  "evidence_status": "BLOCKED_ON_ACCEPTED_MECHANISM_HOLDOUTS_PRESERVED",
  "hard_block": "Requires ACCEPTED_MECHANISM from RS-PFSS-JUSTIFIED-NONDEGENERATE-NULL-MECHANISM.",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PFSS-NONDEGENERATE-NULL-PREFLIGHT",
  "parent_objective_id": "PROGRESSIVE_PLANE_PRIME_SEMIPRIME_COORDINATE_DISCOVERY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFSS-ND",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PFSS-JUSTIFIED-NONDEGENERATE-NULL-MECHANISM",
  "successor_gate": {
    "new_information_gap": "Even a justified probability mechanism would not by itself prove that the previously prescribed shell statistic is defined and nondegenerate on the exposed discovery carrier.",
    "why_parent_result_does_not_close_it": "The mechanism task decides the law/premise question. It deliberately does not choose or validate a family-wise test statistic and does not touch preserved holdouts.",
    "discriminating_outcomes": [
      "The accepted mechanism yields defined nonzero-variance discovery observables and a fully frozen statistic suitable for a later separate blind-forward task.",
      "The accepted mechanism still degenerates or makes the proposed statistic undefined, closing this screen design without touching holdouts.",
      "Multiple equally justified mechanisms produce materially incompatible calibration, returning the problem to mechanism identification rather than choosing a favorable law."
    ],
    "kill_condition": "Do not execute unless the parent returns ACCEPTED_MECHANISM; do not inspect X=3e8 or X=1e9; do not repair undefined statistics by variance floors, cell deletion or post-hoc feature changes.",
    "alternative_route_or_free_exploration_considered": "Immediate holdout testing, closing the PFSS route, and unrelated exploration were considered. A discovery-only definability preflight is the smallest safe continuation if and only if a justified mechanism is first accepted.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Mechanism validity and statistic definability are distinct falsifiable obligations. Separating them prevents an accepted probabilistic premise from being mistaken for a validated test design."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# PFSS: nondegenerate-null statistic and support preflight

## Mother question

Assuming and only assuming that the upstream mechanism task returns an accepted source-defensible nondegenerate law, can a concrete shell statistic be frozen on exposed discovery data whose null distribution is actually defined and nondegenerate before any preserved holdout is touched?

## Frozen inputs and scope

This task is blocked until RS-PFSS-JUSTIFIED-NONDEGENERATE-NULL-MECHANISM returns ACCEPTED_MECHANISM with exact assumptions and preserved quantities. Import that mechanism unchanged. Use only already exposed discovery scales and the existing exact semiprime enumeration conventions. X=3e8 and X=1e9 remain sealed.

BRC is used only to preserve the typed carrier, shared-address fibres and observer map from the accepted mechanism. It may expose where the statistic factors through a degenerate fibre; it cannot supply a missing probability premise.

## Hard target and required outputs

Hard target: NONDEGENERATE_NULL_STATISTIC_PREFLIGHT_PASS_OR_FAIL.

Deliver: (1) the exact imported mechanism and provenance; (2) the proposed statistic written before numerical evaluation; (3) exact/replayable support and variance diagnostics for every component used by the statistic; (4) covariance structure required by shared q-address overlap; (5) deterministic replay evidence; (6) a frozen discovery-only specification suitable for later independent review, or an exact failure certificate; (7) an explicit statement that preserved holdouts were not accessed.

This task does not publish or execute the later holdout screen.

## Research value to preserve

PFSS2 failed because a sophisticated-looking test was undefined under its own frozen null. This preflight makes definability and support an explicit gate before any new blind-forward claim can be created.

## Success, kill, and return criteria

PASS only if every statistic component used by the frozen design has defined null moments/distribution under the accepted mechanism, the family-wise statistic is executable without numerical conventions that change semantics, and replay confirms the support/covariance calculations on exposed discovery data.

FAIL if any required component is structurally degenerate or undefined, or if equally justified implementations disagree materially. In that case return the smallest exact obstruction and do not publish a holdout-screen successor automatically.

Kill execution if the dependency is not an accepted mechanism, if any preserved holdout is accessed, or if a variance floor, omitted cell, changed binning or post-hoc statistic is introduced to force a pass.
