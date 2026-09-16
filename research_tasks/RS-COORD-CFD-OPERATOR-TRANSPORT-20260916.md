<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-COORD-CFD-OPERATOR-TRANSPORT-20260916",
  "title": "流体工程的地址迁移：网格算子、边界、AMR和舍入次序",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Ten CFD tasks exist; no address-specific mesh/operator transport certificate connects them to the new final Cell-address interface.",
  "next_action": "Fix one existing finite mesh and its actual pressure or spectral kernel; map cells,faces and degrees of freedom separately before comparing outputs.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:coordinate_address_contract.json",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:COORDINATE_ADDRESS_CONVENTION.zh-CN.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:EnterpriseMath/CellAddress/ThreeRegionSlice.lean",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/RS-CFD-SPECTRAL-HYBRID-20260910.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/RS-CFD-PRESSURE-GAMG-20260910.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/RS-CFD-AMR-BASILISK-20260910.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/RS-CFD-ROUNDING-ENVELOPE-20260910.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/RS-CFD-TRAJECTORY-CERTIFICATION-20260910.md"
  ],
  "evidence_status": "SCOPED_SLICE_PROOF_COMPLETE_DELTA_UNFINISHED",
  "last_progress_ref": "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
  "hard_block": null,
  "tags": [
    "coordinate-address",
    "nonnegative",
    "representation-only"
  ],
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-COORD-CFD-OPERATOR-TRANSPORT-20260916",
  "parent_objective_id": "OBJ-CELL-NONNEGATIVE-COORDINATE-MIGRATION-20260916",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "COORD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "related_existing_tasks": [
    "RS-CFD-SPECTRAL-HYBRID-20260910",
    "RS-CFD-PRESSURE-GAMG-20260910",
    "RS-CFD-AMR-BASILISK-20260910",
    "RS-CFD-ROUNDING-ENVELOPE-20260910",
    "RS-CFD-TRAJECTORY-CERTIFICATION-20260910"
  ],
  "lineage_rationale": "New address-representation delta under the explicit user request; does not revise or restart the related tasks with their different frozen mathematical targets.",
  "policy_review": {
    "temporary_overrides": [],
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:98ee2981553fb4eeaf5bd8599513719ee2ac987fae875e9c5daf8a3e2156f3cf",
    "review_state": "PASS"
  }
}
-->

# 流体工程的地址迁移：网格算子、边界、AMR和舍入次序

## Mother question

Does relabeling mesh cells preserve the existing discrete fluid operators and trajectories, and where can changed floating-point evaluation order matter?

## Frozen inputs and scope

The exact source snapshot is d2984d1a0c5c8221ee103084dd3da68dd039dfaa. The verified three-region slice proof is consumed unchanged (SHA256 2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02). Only final addresses change; native cell population, six axis labels, signed internal displacements, existing adjacency, decoded metric and ordered path data are retained.

Reuse the CFD-B1F673 spectral handoff and the existing pressure,AMR,LBM,ROM,cancellation and trajectory tasks. Computational degree-of-freedom indices are not automatically final Cell addresses. Preserve face orientation,flux weights,boundary/source cells,refinement maps and full trajectory events. This task selects no new Navier-Stokes model and does not repeat benchmark work with unchanged kernels.

## Hard target and required outputs

Prove exact permutation conjugacy A_new=U A_old U^-1 and corresponding state/source/boundary maps for one frozen operator; include face-incidence maps where rectangular operators need distinct permutations. Prove transported updates and AMR commuting diagrams or return exact defects. Separate integer/rational equality from floating accumulation-order differences and bound the latter with the existing rounding-envelope interface. Test equal-value crossing,alias deduplication and out-of-scope addresses. Deliver operator certificate,trajectory comparisons and performance-cost accounting under research_artifacts/COORD_CFD_TRANSPORT_20260916/.

## Research value to preserve

This protects engineering results from address-induced boundary or rounding bugs while preserving already useful numerical algorithms.

## Success, kill, and return criteria

Success is exact structural correspondence plus explicitly bounded finite-precision behavior on the frozen mesh. A mismatch must identify address mapping,orientation,operator change or rounding order. Do not infer physical instability from a relabeling error; do not claim full solver equivalence from endpoint-only agreement.
