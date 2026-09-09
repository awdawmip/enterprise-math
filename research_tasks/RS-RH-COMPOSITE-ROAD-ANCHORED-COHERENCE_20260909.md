<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RH-COMPOSITE-ROAD-ANCHORED-COHERENCE",
  "title": "Composite-road RH: anchored rational-frequency coherence and safe tail interface",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Retain anchored cross-frequency phase while constructing a finite-to-infinite kernel and quantified low-frequency/tail coupling.",
  "next_action": "On simultaneous finite frequency and horizon cutoffs derive the centered quadratic identity, including the constant -1-c_a/2 channel, before any limiting operation.",
  "dependencies": ["RS-RH-COMPOSITE-ROAD-BASELINE-AUDIT"],
  "source_refs": [
    "research_notes/COMPOSITE_ROAD_RH_RESEARCHER_HANDOFF_20260909.md",
    "artifacts/composite_road_rh/handoff_20260909/source_index.json",
    "https://github.com/awdawmip/chatgpt-global-knowledge/blob/bb649a26fd04db9bee3cf237b7c0d0311f99e7d2/journal/enterprise-math/2026-09-05/20260905T073134Z-composite-residue-rh-stage2-c4a91d.md",
    "https://github.com/awdawmip/enterprise-math/blob/07f7175664f78ff35d0bdb1986ed37f264acb7e1/research_notes/COMPOSITE_ROAD_RH_FUTURE_PORT_POSITIVE_DEFORMATION_20260906.md",
    "https://github.com/awdawmip/enterprise-math/blob/815a0f3f7eb5f2061ecb565cc015965a46f84448/research_notes/COMPOSITE_ROAD_RH_COMPLETED_SCHUR_PICK_20260906.md",
    "https://github.com/awdawmip/enterprise-math/blob/9d7c4c6eafc5479a6795a128fc0288fc893bed3c/research_notes/COMPOSITE_ROAD_RH_BOUNDARY_SLOPE_CLOSURE_20260906.md",
    "https://github.com/awdawmip/enterprise-math/blob/9d7c4c6eafc5479a6795a128fc0288fc893bed3c/research_notes/COMPOSITE_ROAD_RH_PENETRATION_JET_HIERARCHY_20260906.md",
    "https://github.com/awdawmip/enterprise-math/blob/9d7c4c6eafc5479a6795a128fc0288fc893bed3c/research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md",
    "https://github.com/awdawmip/enterprise-math/blob/9d7c4c6eafc5479a6795a128fc0288fc893bed3c/research_notes/COMPOSITE_ROAD_RH_DISCRETE_L2_NONCOMMUTATION_20260906.md",
    "https://github.com/awdawmip/enterprise-math/blob/bf181bfa6c4f1fdbe4ddf6352385c5f4b819cc53/research_notes/COMPOSITE_ROAD_RH_RAMANUJAN_PHASE_COHERENCE_20260906.md"
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
  "registry_key": "RS-RH-COMPOSITE-ROAD-ANCHORED-COHERENCE",
  "parent_objective_id": "OBJ-RH-COMPOSITE-ROAD-UNIFORM-ENERGY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RH-COMPOSITE-ROAD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-RH-COMPOSITE-ROAD-BASELINE-AUDIT",
  "successor_gate": {
    "new_information_gap": "The anchored rational-frequency quadratic kernel, centering channels and inter-block tail control are not supplied by the diagonal translation-averaged variance.",
    "why_parent_result_does_not_close_it": "The parent audits existing finite and conditional claims; it does not prove anchored off-diagonal phase bounds or an infinite-frequency approximation theorem.",
    "discriminating_outcomes": [
      "An exact anchored finite-block kernel plus certified tail/coupling theorem",
      "A concrete phase-loss witness or obstruction to a proposed block reduction",
      "A scoped mathematical reduction with an explicit remaining uniform estimate"
    ],
    "kill_condition": "Reject an argument that drops off-diagonal phase or centering terms, interchanges divergent limits, or concludes uniform cancellation from diagonal positivity alone.",
    "alternative_route_or_free_exploration_considered": "The independent finite Green/escaping-tail route is retained; completed Schur/Pick is an alternative interface but its holomorphicity and positivity cannot be assumed.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is a distinct analytic construction following baseline validation, not a repetition of existing identities. Closure is not justified because the uniform road-energy bound remains open."
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

# Composite-road RH: anchored rational-frequency coherence

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_BY_STATE_MACHINE`

## Mother question

Can the full fixed-origin road discrepancy be represented and bounded by a rational-frequency quadratic kernel without discarding the phase coherence that translation averaging removes?

## Frozen inputs and scope

Use the shared handoff and S7 together with the corrected S5/S6 energy definitions. Consume the baseline audit's actual validated scope. Let u_a(n)=R_a(n)-c_a and h_N(theta)=sum_(1<=n<=N) exp(i*n*theta). Nonzero rational frequencies are retained with their full signed amplitudes and denominators. Define B_(a,N)=sum_(n<=N)u_a(n)-1-c_a/2; the constant channel and cross terms are part of the observer.

The parent is `RS-RH-COMPOSITE-ROAD-BASELINE-AUDIT`. Earlier direct research is cited as provenance, not misrepresented as a previously published task. The companion escaping-tail task is not a hard dependency.

## Hard target and required outputs

First establish the exact doubly truncated anchored quadratic form. Derive a usable expression for K(theta,phi)=sum_(N>=1)h_N(theta)conj(h_N(phi))/N^2, including diagonal limits and near-zero/near-collision behavior. A closed special-function formula alone is insufficient.

Construct a frequency-block or future-port interface with an explicit coupling remainder that controls the original anchored observer. Justify every infinite-frequency passage, retain sign/phase and centering, and state constants and their dependence on a, cutoffs, denominators and frequency separation. Supply independently checkable small-block identities and at least one adversarial phase/centering test. If an averaging reduction is proposed, provide an actual observer-preservation proof; the contrast between an unconditional average bound and an RH-equivalent target alone is not such a proof.

Deliver a mathematical note, reproducible checker or interval certificate where computation is used, and a sharply formulated sufficient bound for Q_a=O(a), or an exact scoped obstruction. No RH premise is allowed for the intended unconditional improvement.

## Research value to preserve

This directly preserves the joint-composite road and tests whether its coherent off-diagonal structure adds control beyond the known translation-averaged diagonal spectrum. It keeps the latest recovered frontier rather than restarting the old Euler or residue-coordinate reformulation.

## Success, kill, and return criteria

Success requires a genuine new kernel-coupling estimate, an observer-complete reduction with quantified tails, or a concrete no-go witness that identifies the remaining necessary information. A finite kernel identity without tail control is only a partial return. Reject phase erasure, hidden RH/zero-location assumptions, unjustified exchange of the a→0 and N→infinity limits, or declaring high-denominator composites redundant from finite fitting. Report the strongest valid theorem and the exact remaining inequality; do not relabel task progress as an RH proof.
