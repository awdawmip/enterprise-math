<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-COORD-CALLER-DATA-MIGRATION-20260916",
  "title": "全调用链和存量地址迁移：身份、缓存、边界及版本保护",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Global constraints and a supported runtime are installed, but full caller and persisted-data migration has not been evidenced.",
  "next_action": "Inventory public Cell-address producers and consumers by actual type use, separating them from scalar arithmetic and private signed chart APIs.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:coordinate_address_contract.json",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:COORDINATE_ADDRESS_CONVENTION.zh-CN.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:EnterpriseMath/CellAddress/ThreeRegionSlice.lean",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:coordinate_contract_migration_manifest.json",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:src/enterprise_math/cell_address.py"
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
  "registry_key": "RS-COORD-CALLER-DATA-MIGRATION-20260916",
  "parent_objective_id": "OBJ-CELL-NONNEGATIVE-COORDINATE-MIGRATION-20260916",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "COORD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "related_existing_tasks": [],
  "lineage_rationale": "New address-representation delta under the explicit user request; does not revise or restart the related tasks with their different frozen mathematical targets.",
  "policy_review": {
    "temporary_overrides": [],
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:98ee2981553fb4eeaf5bd8599513719ee2ac987fae875e9c5daf8a3e2156f3cf",
    "review_state": "PASS"
  }
}
-->

# 全调用链和存量地址迁移：身份、缓存、边界及版本保护

## Mother question

Which existing callers and stored records need adapters, and can their exact cell/edge identities survive versioned migration?

## Frozen inputs and scope

The exact source snapshot is d2984d1a0c5c8221ee103084dd3da68dd039dfaa. The verified three-region slice proof is consumed unchanged (SHA256 2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02). Only final addresses change; native cell population, six axis labels, signed internal displacements, existing adjacency, decoded metric and ordered path data are retained.

Do not mass-replace negative integers, old proofs, arithmetic valuations, geometric variety coordinates or Fourier indices. Migrate supported slice records only when their original frame and complete identity are known. Preserve native zero cells, source/boundary sets and time labels; unsupported full-X6 records require an explicit gate rather than a lossy slice fallback.

## Hard target and required outputs

Return a source-line caller inventory, versioned reversible data converter, stable identity/cache-key contract, boundary/initial-state mapping, rollback fixtures and negative controls. Test old numeric-coordinate consumers cannot accept FinalCellAddress as an ordinary integer sequence. Map regions by decoded cell sets, not by raw address-number intervals. Include unknown legacy frame and duplicate alias conflicts with fail-closed outcomes. Produce a coverage manifest of changed, unaffected, unavailable and gated surfaces under research_artifacts/COORD_CALLER_MIGRATION_20260916/.

## Research value to preserve

This is engineering migration and type safety; it protects correct old algebra while making the new final-address contract effective throughout supported callers.

## Success, kill, and return criteria

Success includes complete bounded inventory and tested supported migrations with exact identities; unknown provenance must stay quarantined. Full-X6 deployment waits for a registered full codec. A repository-wide claim is forbidden while uninspected producers or datasets remain.
