<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-NS-BRC-CERTIFIED-REFERENCE-ENGINE-20260917",
  "title": "BRC Certified Reference Engine: Goal-Oriented All-Mode Residual Verification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "The project already has phase/rate-resolved residual Grams, causal inverse bounds, inexact Newton ledgers, goal-oriented primal/dual certificates, branch selection, and all-mode tails. These pieces need consolidation into one reproducible certifier whose failure diagnosis distinguishes insufficient approximation from a genuine bound or norm obstruction.",
  "next_action": "Define one typed certificate interface for reference trajectories, coherent packets, inverse-growth bounds, nonlinear feedback constants, perturbation budgets, and primal/dual stopping tests; then replay the current A3 family end-to-end and separate generic residual-certification structure from NS-specific symmetry.",
  "dependencies": [],
  "source_refs": [
    "research_notes/ns_brc_program_handoff_20260917.md",
    "research_notes/ns-goal-primal-dual-certificate-20260910.md",
    "research_notes/ns-greedy-temporal-certificate-20260910.md",
    "research_notes/ns-inexact-newton-error-ledger-20260909.md",
    "research_notes/ns-causal-inverse-newton-basin-20260909.md"
  ],
  "evidence_status": "RESEARCH_PROGRAM_INTEGRATION_V1",
  "last_progress_ref": "research_notes/ns_brc_program_handoff_20260917.md",
  "last_progress_at": "2026-09-17T12:53:00+08:00",
  "hard_block": "CERTIFICATION_TOOLCHAIN_FRAGMENTED_ACROSS_RESEARCH_CHECKPOINTS",
  "tags": ["BRC", "certification", "Navier-Stokes", "a-posteriori", "Newton", "Gram", "MHD", "tool"],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-NS-BRC-CERTIFIED-REFERENCE-ENGINE-20260917",
  "parent_objective_id": "EM-NS-BRC-JITTER-REGULARITY-PROGRAM-20260917",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R-NSCE",
  "origin_kind": "DIRECT_USER_DIRECTION",
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

# BRC Certified Reference Engine: Goal-Oriented All-Mode Residual Verification

Status: `READY / DIRECT USER RESEARCH INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

Can the existing BRC residual and causal-inverse machinery be consolidated into a reproducible certifier that proves complete PDE error bounds, explains failures, and transfers to other quadratic dissipative systems without erasing phase/provenance information?

## 1. Frozen inputs and scope

Consolidate only interfaces already proved in the cited checkpoints, or label experimental extensions explicitly. Preserve exact packet labels until the intended Gram operation and attach every finite approximation to an explicit error certificate.

The certifier must distinguish finite approximation error, infinite Fourier tail, linearized inverse growth, nonlinear feedback, initial perturbation, and numerical enclosure error. A successful finite solve is not a PDE theorem unless the all-mode analytic conditions also pass.

The first reference implementation is the periodic incompressible NS family already used in this line. An equal-diffusivity MHD adapter may be included only with its ordered interaction terms treated faithfully; NS-specific symmetric constants may not be copied without proof.

## 2. Hard target and required outputs

Hard target: `REPRODUCIBLE_BRC_PDE_CERTIFIER_WITH_FAILURE_DIAGNOSIS`.

Deliver all of the following:

1. A typed mathematical interface for packet carriers, residual Grams, reference-flow norms, causal inverses, nonlinear feedback constants, perturbation budgets, and final contraction or continuation conditions.
2. A deterministic implementation that recomputes the current A3 certificates from source data without hidden cached numerical state.
3. Primal and dual or lower-bound diagnostics that certify both success and 'this fixed certificate cannot succeed' outcomes.
4. An adaptive refinement rule whose decisions are checkable and whose fallback dictionary is complete for each fixed admissible linear problem.
5. Separate analytic-tail and finite-core checks; no finite frequency or time grid may stand in for an all-mode proof.
6. A minimal equal-diffusivity MHD adapter and a classification of which interfaces are generic, divergence-free-only, NS-specific, or require new ordered-interaction proofs.

## 3. Research value to preserve

The line has produced a reusable style of operation-safe residual certification, but it is scattered across many checkpoints. Consolidation makes the mathematics reproducible, allows independent falsification, and converts future analytic improvements into immediate end-to-end experiments rather than bespoke recalculations.

## 4. Success, kill, and return criteria

Success is a source-reproducible certifier with explicit proof obligations and failure modes, plus a faithful MHD adapter or a pinned reason the adapter cannot yet be completed.

Kill any design that silently truncates outputs, uses optimizer convergence as proof, hides coefficient rounding or interval error, conflates a certificate failure with PDE singularity, hardcodes the present A3 example as the general interface, or imports the NS symmetric constant into ordered MHD terms without proof.

Return the smallest reusable certified core and the list of mathematical interfaces that remain external assumptions.
