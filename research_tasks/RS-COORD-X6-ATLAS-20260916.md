<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-COORD-X6-ATLAS-20260916",
  "title": "全X6六字段非负地址图册：完整身份、合法域与登记证书",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Only a fixed two-generator slice is certified; there is no registered lossless final-address codec for arbitrary native X6 cells.",
  "next_action": "Define the whole native cell population and an explicit six-natural-field address with recoverable chart/frame identity; first prove both inverse laws before implementing all native steps.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:coordinate_address_contract.json",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:COORDINATE_ADDRESS_CONVENTION.zh-CN.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:EnterpriseMath/CellAddress/ThreeRegionSlice.lean",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_tasks/RS_X6_UPPER_STRUCTURE_INTEGRATION_V2_20260909.md"
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
  "registry_key": "RS-COORD-X6-ATLAS-20260916",
  "parent_objective_id": "OBJ-CELL-NONNEGATIVE-COORDINATE-MIGRATION-20260916",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "COORD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "related_existing_tasks": [
    "RS-X6-UPPER-STRUCTURE-INTEGRATION-V2"
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

# 全X6六字段非负地址图册：完整身份、合法域与登记证书

## Mother question

Can the adopted final-address requirements be realized on the full X6 cell space with an explicit, lossless and computationally usable atlas?

## Frozen inputs and scope

The exact source snapshot is d2984d1a0c5c8221ee103084dd3da68dd039dfaa. The verified three-region slice proof is consumed unchanged (SHA256 2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02). Only final addresses change; native cell population, six axis labels, signed internal displacements, existing adjacency, decoded metric and ordered path data are retained.

This is a new representation target, not selection of a physical rotation or time law. Preserve the current slice addresses by an explicit compatibility embedding, not by assuming their three trailing zeros cover arbitrary X6 cells. Region metadata may carry necessary information, but its size and meaning must be disclosed; do not hide extra signed coordinates or relabel twelve sign slots as six. Zero means declared inactivity, not unknown data.

## Hard target and required outputs

Produce a typed legal domain, encode/decode functions, chart overlap maps, native direction update tables and complexity bounds. Prove D(E(x))=x and E(D(a))=a, injectivity of complete wire addresses, and D(step(d,a))=nativeStep(d,D(a)) for all twelve existing operation labels. Establish preservation of ordered words and retained observer data by the existing BRC transport law. Supply Lean proofs and executable exact tests, including large values, all region faces and hidden-diagonal witnesses. Return outputs under research_artifacts/COORD_X6_ATLAS_20260916/ and a proposed registry entry with precise scope.

## Research value to preserve

The full-space gap is the central unfinished mathematical obligation; the already proved slice must not be mistaken for a global codec.

## Success, kill, and return criteria

Success is a complete invertible full-X6 representation with the stated compatibility and proofs. A no-go return must state the exact additional restrictions it obstructs and provide a counterexample or theorem; it may not infer impossibility of all nonnegative encodings from one failed candidate. Stop without registering a global codec when identity or operation compatibility fails.
