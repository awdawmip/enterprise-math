<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-PRIOR-ART-AUDIT-20260910",
  "title": "CFD prior-art and contribution-boundary audit",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The CFD portfolio now has multiple algorithmic hypotheses, but no single source-backed audit classifies which mechanisms are standard, which are reusable implementations, and which exact contribution claims remain open.",
  "next_action": "Freeze the current CFD task portfolio and build a primary-source comparison matrix for sparse spectral evaluation, a-posteriori error control, reduced-order modeling, adaptive mesh refinement, multigrid pressure solution, and lattice-Boltzmann code generation.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@13a7cdc9dfac3b7f6d7120f7b020733d7c91f964:research_notes/CFD9R2K7/cfd_public_algorithm_probe_20260910.json",
    "awdawmip/enterprise-math@e40e5303234c5e8bd725528aad9bff9edf0c059d:research_notes/CFD-B1F673/main/summary.json",
    "research_notes/CFD-B1F673/prior_3d/probe.py",
    "research_notes/CFD-B1F673/prior_chat_bundle_20260910/README.md",
    "research_notes/CFD-B1F673/prior_chat_bundle_20260910/prior_local_main_results.json",
    "research_notes/CFD-B1F673/prior_chat_bundle_20260910/prior_taskset_manifest.json",
    "research_notes/CFD-B1F673/prior_chat_bundle_20260910/RAW_VORTEX_INTERFACE.md",
    "research_notes/CFD-B1F673/task_packet.md",
    "research_tasks/RS-CFD-SPECTRAL-HYBRID-20260910.md",
    "research_tasks/RS-CFD-ROUNDING-ENVELOPE-20260910.md",
    "research_tasks/RS-CFD-CANCELLATION-GROUPS-20260910.md",
    "research_tasks/RS-CFD-TRAJECTORY-VERIFY-20260910.md",
    "research_tasks/RS-CFD-ROM-ITHACA-20260910.md",
    "research_tasks/RS-CFD-AMR-BASILISK-20260910.md",
    "research_tasks/RS-CFD-PRESSURE-GAMG-20260910.md",
    "research_tasks/RS-CFD-LBM-CODEGEN-20260910.md"
  ],
  "evidence_status": "PRIOR_ART_CLASSIFICATION_NOT_YET_COMPLETED",
  "last_progress_ref": "research_notes/CFD-B1F673/task_packet.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "CFD",
    "user-directed-20260910",
    "prior-art",
    "contribution-boundary"
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

# CFD prior-art and contribution-boundary audit

Status: `READY / PUBLISHED_REGISTERED / SOURCE-BACKED AUDIT`

## Mother question

Across the current CFD portfolio, which mathematical mechanisms and software techniques already have close public antecedents, which public implementations should be reused as baselines or hosts, and what exact residual contribution claims remain both technically meaningful and unsupported by the identified antecedents?

## Frozen inputs and scope

Audit the currently published CFD task family and the preserved exploratory sources. Cover at least sparse or support-aware Fourier evaluation, pseudospectral nonlinear terms, a-posteriori or residual-based error control, cancellation-aware bounds, reduced-order modeling, adaptive mesh refinement, multigrid pressure solution, and lattice-Boltzmann collision or code-generation optimization.

Prefer original papers, official project documentation and source code. Distinguish theorem antecedent, algorithm antecedent, implementation antecedent and performance precedent. A failure to locate a close match is evidence of an unresolved search boundary, not proof of novelty.

Treat P000 as the project premise while reporting external classical CFD faithfully as an external effective model. Do not reinterpret standard CFD terminology as native P000 mathematics merely to create differentiation.

## Hard target and required outputs

Return a source-backed comparison matrix for every current CFD task with:

1. the closest identified antecedent and source;
2. the exact overlap in operator, representation, approximation, certificate, adaptive rule, or software architecture;
3. the exact difference proposed by the Enterprise Math task;
4. reusable public code or benchmark surfaces where licensing and scope permit;
5. a classification of the proposed claim as standard, incremental engineering, potentially differentiating but unproved, or currently unsupported;
6. wording constraints that prevent performance, proof, or originality claims from exceeding the evidence.

For the finite-trajectory certification task, compare both classical numerical-analysis error propagation and a-posteriori Navier-Stokes validation literature. For the spectral line, distinguish ordinary sparse convolution from any genuinely new observer-safe grouping or certification mechanism.

## Research value to preserve

This audit prevents duplicated research and directs effort toward improvements that survive comparison with mature public methods. It also supplies the evidence boundary needed for eventual papers, software documentation, benchmarking and intellectual-property decisions without treating internal terminology as a substitute for external novelty.

## Success, kill, and return criteria

SUCCESS requires primary-source citations or exact source-code references for the material comparisons and a task-by-task residual claim boundary.

Do not label a method novel merely because the project uses a different vocabulary, representation diagram, or BRC interpretation. Do not dismiss a potentially useful engineering improvement merely because its primitive ingredients are standard if the tested composition or certificate creates a measurable new capability.

If a task is fully subsumed by prior work, return that conclusion and the best reusable implementation. If the search remains inconclusive, return the exact unresolved comparison rather than a novelty claim.
