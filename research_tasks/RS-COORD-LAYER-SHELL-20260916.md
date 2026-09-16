<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-COORD-LAYER-SHELL-20260916",
  "title": "第一层从1编号：层号定义、对称条件与新壳层统计",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Layer-one intent is clear but no single first-layer population has been frozen; new layer counts cannot inherit old center-radius shell counts.",
  "next_action": "Declare parameterized first-layer sets S1 and separate address fields, layer observations and metric-center choices before computing any counts.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:coordinate_address_contract.json",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:COORDINATE_ADDRESS_CONVENTION.zh-CN.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:EnterpriseMath/CellAddress/ThreeRegionSlice.lean",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/NATIVE_SHELL_GRADE_MONOTONE_INTEGER_ALLOCATION_FOUNDATION_AUDIT_20260827.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_REVISION_V2_20260828.md"
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
  "registry_key": "RS-COORD-LAYER-SHELL-20260916",
  "parent_objective_id": "OBJ-CELL-NONNEGATIVE-COORDINATE-MIGRATION-20260916",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "COORD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "related_existing_tasks": [
    "RS-NATIVE-SHELL-GRADE-MONOTONE-INTEGER-ALLOCATION-FOUNDATION-AUDIT",
    "RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION"
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

# 第一层从1编号：层号定义、对称条件与新壳层统计

## Mother question

Which layer statistics really change when the first layer is an explicit set of cells rather than the old selected center?

## Frozen inputs and scope

The exact source snapshot is d2984d1a0c5c8221ee103084dd3da68dd039dfaa. The verified three-region slice proof is consumed unchanged (SHA256 2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02). Only final addresses change; native cell population, six axis labels, signed internal displacements, existing adjacency, decoded metric and ordered path data are retained.

Use L_S1(P)=1+min_{Q in S1} d_G(Q,P) only when S1 is nonempty and reachability and minima are justified. A finite three-cell test seed is not the unique intended global S1. An infinite layer may have infinite population. Retain the prior grade-monotone allocation audit at its accepted torsor/readout strength. No unit radial-distance assertion follows from layer label one.

## Hard target and required outputs

Prove layer-one identity, local Lipschitz bounds, L_(gS1)(gP)=L_S1(P), and the exact condition for fixed-S1 symmetry. Give exact layer population and interlayer edge/BRC tables for explicitly named finite seeds and state infinite-layer cases separately. Preserve old fixed-center squared-radius25 witnesses (30 endpoints,846 shortest words) under recoding and exhibit changed-center counts only as new questions. Return a parameterized implementation, scope ledger and proofs under research_artifacts/COORD_LAYER_SHELL_20260916/.

## Research value to preserve

The statistical questions genuinely change when the seed set changes, unlike pure address relabeling; this prevents false reuse of old shell counts.

## Success, kill, and return criteria

Success is a scoped family of definitions and certified counts, not an unsupported universal first layer. Report UNRESOLVED_SEED_SELECTION for the final global choice while completing seed-independent theorems. Do not infer intrinsic canonical allocation from a convenient numbering.
