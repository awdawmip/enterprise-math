<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-PRIOR-ART-AUDIT-20260910",
  "title": "CFD prior-art and novelty-boundary audit",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "A partial public-algorithm scan exists, but there is no claim-by-claim novelty map covering the current spectral hybrid, rounding/cancellation certification, ROM, AMR, pressure-solver and LBM directions.",
  "next_action": "Build a source-backed comparison matrix for the eight published CFD tasks, starting with spectral sparse evaluation and certified truncation, and classify each proposed contribution as established, implementation reuse, uncertain overlap, or genuinely open.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@13a7cdc9dfac3b7f6d7120f7b020733d7c91f964:research_notes/CFD9R2K7/cfd_public_algorithm_probe_20260910.json",
    "awdawmip/enterprise-math@e40e5303234c5e8bd725528aad9bff9edf0c059d:research_notes/CFD-B1F673/main/summary.json",
    "research_notes/CFD-B1F673/task_packet.md",
    "research_notes/CFD-B1F673/legacy_local_handoff_20260910/README.zh-CN.md"
  ],
  "evidence_status": "PARTIAL_PUBLIC_SOURCE_SCAN / NO_COMPLETE_NOVELTY_DETERMINATION",
  "last_progress_ref": "awdawmip/enterprise-math@13a7cdc9dfac3b7f6d7120f7b020733d7c91f964:research_notes/CFD9R2K7/cfd_public_algorithm_probe_20260910.json",
  "last_progress_at": "2026-09-10T08:31:05+00:00",
  "hard_block": null,
  "tags": [
    "CFD",
    "prior-art",
    "novelty-boundary",
    "user-directed-20260910"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-PRIOR-ART-AUDIT-20260910",
  "parent_objective_id": "OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "CFD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
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

# CFD prior-art and novelty-boundary audit

## Mother question

Which parts of the current CFD optimization program are already established in sparse spectral evaluation, certified/reduced computation, model reduction, adaptive methods, multilevel pressure solvers or LBM code generation, and which precisely stated residual contributions remain worth researching under Enterprise Math?

## Frozen inputs and scope

Audit the eight currently published CFD tasks and the preserved 2D/3D exploratory evidence at their exact stated strength. External CFD models remain external effective models; this task does not derive fluid dynamics from P000. Preserve wavevector labels, signed/complex amplitudes, target observables, boundary assumptions and solver interfaces when comparing methods. Positive-weight BRC results do not establish phase cancellation. Distinguish theorem novelty, algorithmic novelty, implementation novelty and performance novelty. Use primary papers, official project documentation and source code where available; absence from a limited search is not evidence of novelty.

## Hard target and required outputs

Produce a claim-by-claim matrix for the eight published CFD tasks. For each proposed mechanism, identify the closest antecedents, exact source/version, reusable implementation surface, material differences, and claims that must not be made. Classify the residual as ESTABLISHED/REUSE, OVERLAP-UNCERTAIN, OPEN-BUT-UNPROVED, or NO-NOVELTY. Give the smallest defensible research claim for any surviving contribution and identify experiments or proofs needed to distinguish it from prior work.

## Research value to preserve

The parent objective is trustworthy acceleration rather than terminology replacement. This audit prevents ordinary sparse convolution, thresholding, POD/DEIM, adaptive refinement, Schur/multigrid ideas or symbolic kernel optimization from being relabeled as new merely because they are expressed in Enterprise Math language. A negative novelty finding is valuable because it redirects effort toward tighter certification, observer-safe compression or other genuinely discriminating work.

## Success, kill, and return criteria

SUCCESS requires source-backed coverage sufficient to support a conservative novelty boundary for each of the eight tasks, with unresolved searches explicitly marked. Kill or downgrade any proposed contribution that is materially covered by prior work unless a narrower measurable difference survives. Do not infer novelty from search failure, project naming, or benchmark speed alone. Return the comparison matrix, citations/versions, reusable code surfaces, uncertainty list, and exact next research target.
