<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RH-COMPOSITE-ROAD-ESCAPING-TAIL",
  "title": "Composite-road RH: escaping-horizon bounds and certified Green energies",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Find explicit scale-dependent control of sum_(N>=M(a)) B_(a,N)^2/N^2 without using an RH-equivalent bound.",
  "next_action": "Instantiate the exact finite Green/cell identity with interval control of c_a and all nonlinear weights; separate prefix error, tail error and completion error.",
  "dependencies": ["RS-RH-COMPOSITE-ROAD-BASELINE-AUDIT"],
  "source_refs": [
    "research_notes/COMPOSITE_ROAD_RH_RESEARCHER_HANDOFF_20260909.md",
    "artifacts/composite_road_rh/handoff_20260909/source_index.json",
    "artifacts/composite_road_rh/handoff_20260909/verification/stage2_certificate_rerun.json"
  ],
  "evidence_status": "PUBLISHED_SOURCE_BACKED_HANDOFF",
  "last_progress_ref": "research_notes/COMPOSITE_ROAD_RH_RESEARCHER_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:20:00+08:00",
  "hard_block": null,
  "tags": ["RH", "composite-road", "all-integer", "signed-phase", "handoff"],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RH-COMPOSITE-ROAD-ESCAPING-TAIL",
  "parent_objective_id": "OBJ-RH-COMPOSITE-ROAD-UNIFORM-ENERGY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RH-COMPOSITE-ROAD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-RH-COMPOSITE-ROAD-BASELINE-AUDIT",
  "successor_gate": {
    "new_information_gap": "No unconditional estimate controls the horizon tail of the centered positive road uniformly as thickness tends to zero.",
    "why_parent_result_does_not_close_it": "Baseline verification establishes identities and conditional comparisons, not a scale-adapted tail bound or uniformly certified road-energy rate.",
    "discriminating_outcomes": [
      "Certified finite Green energies with honest tail intervals and parameter dependencies",
      "A scale law M(a) with sufficient rigorous prefix and tail budgets",
      "A lower bound or obstruction excluding a proposed truncation or compression"
    ],
    "kill_condition": "Reject finite sample saturation, use of U_comp as a raw-energy bound, or an unproved RH-equivalent input disguised as a tail estimate.",
    "alternative_route_or_free_exploration_considered": "Anchored rational-frequency coherence is retained as an independent complementary route; direct finite Green identities avoid starting from a spectral projection.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The unbounded-horizon quantitative problem is not closed by the earlier finite certificates or the audit. It has an independent concrete deliverable and can return a useful scoped obstruction."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "prior_research_provenance": {
    "researcher": "EM-FREE-C4A91D",
    "mode": "FREE_AXIOM_DISCOVERY",
    "blindness": "ANCHOR_EXPOSED",
    "status": "PRIOR_SOURCE_NOT_NEW_TASK_HISTORY",
    "source_index": "artifacts/composite_road_rh/handoff_20260909/source_index.json"
  }
}
-->

# Composite-road RH: escaping-horizon bounds

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_BY_STATE_MACHINE`

## Mother question

Which scale M(a) and information-preserving estimates can control the escaping horizon of the full positive composite road as a tends to zero?

## Frozen inputs and scope

Use the shared handoff and its pinned S4-S7 sources. Work with the raw road energy Q_a and the midpoint series D_a. Keep the continuous-background cross term and the full integer population. The parent task is `RS-RH-COMPOSITE-ROAD-BASELINE-AUDIT`.

## Hard target and required outputs

Give an exact or outward-rounded finite Green calculation with separate budgets for road weights, c_a, subtraction cancellation and completion error. Study M(a) tending to infinity and the remaining tail sum over N>=M(a). Return either an unconditional uniform O(a) tail estimate, a rigorously sufficient weaker reduction, or a precise obstruction to a proposed scale. Finite extrapolation is not an infinite-tail certificate.

## Research value to preserve

This is the quantitative form of the road-before-holes principle: remote composite layers and composite/composite Green interactions stay visible until an observer-safe reduction is proved.

## Success, kill, and return criteria

Success is a new uniform tail theorem, a rigorously sufficient reduction, or a scoped obstruction with checkable evidence. Reject any argument that substitutes the completed energy for the raw energy, imports an RH-equivalent estimate as an unconditional input, or treats fixed-window smallness as global redundancy. Return the strongest valid bound and the smallest remaining open estimate.
