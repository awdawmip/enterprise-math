<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RH-COMPOSITE-ROAD-BASELINE-AUDIT",
  "title": "Composite-road RH: independent audit of the corrected research baseline",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Independent verification of the corrected raw/completed energy bridge and source assumptions before the next unbounded-scale continuation.",
  "next_action": "Read the shared handoff and S5/S6/S7, match S3 corrections, then run the unchanged stage-2 verifier and audit analytic hypotheses.",
  "dependencies": [],
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
  "registry_key": "RS-RH-COMPOSITE-ROAD-BASELINE-AUDIT",
  "parent_objective_id": "OBJ-RH-COMPOSITE-ROAD-UNIFORM-ENERGY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RH-COMPOSITE-ROAD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
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

# Composite-road RH: independent baseline audit

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_BY_STATE_MACHINE`

## Mother question

Which exact statements from the preserved composite-road research can a new researcher safely consume, at what strength and under which assumptions, after the raw/completed energy correction?

## Frozen inputs and scope

Read `research_notes/COMPOSITE_ROAD_RH_RESEARCHER_HANDOFF_20260909.md` and `artifacts/composite_road_rh/handoff_20260909/source_index.json`. S0 is the complete frozen residue-certificate source. S3, S5 and S6 are the corrected analytic baseline. S7 is the anchored-phase continuation frontier. These immutable sources, not missing predecessor conversation state, are the evidence boundary.

This is a newly proposed independent REPLAY/audit task, not a retroactively invented completed parent task. Preserve prior FREE/ANCHOR_EXPOSED provenance. The user selected the composite-inclusive RH direction directly; no raw axiom candidate is being promoted by this audit. The finite verifier has already passed a current rerun; independently verify its integrity rather than search the rational coefficients again.

## Hard target and required outputs

Produce a claim-by-claim ledger distinguishing exact finite identities, general proved derivations, conditional-on-RH results, RH-equivalent targets, and unresolved bounds. Inspect in particular: the strong Nyman–Beurling/Burnol bridge; raw Q_a versus completed Delta_a; completion error A(a)=O(a) on an explicit sufficiently small-a interval; the exact cell and finite Green formulas; the order of the thickness and horizon limits; and the precise scope of the translation-averaging information-loss statement.

Return a source-pinned audit report, a correction dependency table, an unchanged-verifier transcript, and any explicit counterexample or missing majorant. Do not claim independence merely by rerunning the author's own algorithm; label reused and independently checked components separately.

## Research value to preserve

The research already contains exact prime-only separation and composite-sign certificates. The audit protects those results while preventing old false raw=completed or Weil-PSD shortcuts from contaminating a new researcher's hypotheses. No rediscovery credit is sought.

## Success, kill, and return criteria

Success is a complete auditable baseline and a precise statement of the next unresolved unit. A material error is also a valuable return: exhibit it, identify the smallest affected source claim, preserve unaffected mathematics, and issue a corrected assumption packet. Do not complete this task by assuming RH to prove an unconditional target, by stamping finite computation as infinite convergence, or by rejecting all composite directions because one shortcut fails. Freeze the audit at its actual evidence strength; later work remains separately scoped.
