<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-COORD-ATLAS-BRC-TRANSPORT-20260916",
  "title": "换图、旋转表示与BRC：同晶包别名和真实路径的形式化区分",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The slice update theorem is complete; cross-frame, axis-permuted, time-dependent and partial-support address transport is not formally integrated.",
  "next_action": "Build a typed chart groupoid over certified slice codecs, then prove identity-preserving chart changes separately from actual native steps.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:coordinate_address_contract.json",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:COORDINATE_ADDRESS_CONVENTION.zh-CN.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:EnterpriseMath/CellAddress/ThreeRegionSlice.lean",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/P000_6D_AXIS_MIXING_ROTATION_ALGEBRA_FORMULA_V2_20260829.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/P000_FCC_NATIVE_COORDINATE_BRIDGE_ROTATION_ATLAS_SYNTHESIZED_V3_20260829.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_REVISION_V2_20260828.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/EM7D3C9A_1255_ROTATION_LAW_ATLAS_20260909.md"
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
  "registry_key": "RS-COORD-ATLAS-BRC-TRANSPORT-20260916",
  "parent_objective_id": "OBJ-CELL-NONNEGATIVE-COORDINATE-MIGRATION-20260916",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "COORD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "related_existing_tasks": [
    "RS-P000-6D-AXIS-MIXING-ROTATION-GROUPOID",
    "RS-P000-FCC-NATIVE-COORDINATE-BRIDGE-ROTATION-ATLAS",
    "RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION",
    "RS-EM7D3C9A-1255-ROTATION-LAW-ATLAS"
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

# 换图、旋转表示与BRC：同晶包别名和真实路径的形式化区分

## Mother question

Which exact chart and support laws preserve cell identity, path order and weights under coordinate relabeling and existing symmetry operations?

## Frozen inputs and scope

The exact source snapshot is d2984d1a0c5c8221ee103084dd3da68dd039dfaa. The verified three-region slice proof is consumed unchanged (SHA256 2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02). Only final addresses change; native cell population, six axis labels, signed internal displacements, existing adjacency, decoded metric and ordered path data are retained.

Use existing S6 native axis permutations and the narrower FCC S4 readout only at their actual scope. A moving address frame is not a new dynamical law. Distinguish fifteen unordered axis pairs, twenty unordered triples and four FCC STAR slices. Consume the A3 partial-support counterexample and the frozen FCC return as evidence, not as accepted global atlas authority. This task does not redo native rotation-law selection or choose a physical clock.

## Hard target and required outputs

Prove D_beta(H_beta_alpha(a))=D_alpha(a), identity/inverse/composition on legal overlap domains, and K=E_beta F D_alpha for actual motion. Prove H_gamma_beta H_beta_alpha=H_gamma_alpha where defined; map partial support domains as well as labels. Formalize stable cell/edge identities and alias normalization preserving genuinely distinct ports and parallel branches. Verify the one-chain-three-aliases counterexample stays one path rather than nine. Prove time-indexed recoding E_(t+1) F_t D_t preserves stationary states and ordered weighted traces. Instantiate at least two distinct axis-pair charts; provide Lean bridge and exact witnesses under research_artifacts/COORD_ATLAS_TRANSPORT_20260916/.

## Research value to preserve

This closes representation-induced false motion, false symmetry and duplicate-path risks without reopening the actual rotational or causal law programs.

## Success, kill, and return criteria

Success is the chart/partial-domain transport theorem plus concrete registered-codec instances. A failed total action must return its exact domain obstruction, not silently extend it. Missing physical law selection is not a failure of this representation theorem. Preserve all preexisting task results and report only the address-dependent delta.
