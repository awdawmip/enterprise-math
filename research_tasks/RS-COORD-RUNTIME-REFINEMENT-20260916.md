<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-COORD-RUNTIME-REFINEMENT-20260916",
  "title": "机器坐标语言与Lean一致性：解析、合法域和执行精化",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The Lean model is certified and runtime tests pass; whole-input refinement between actual wire parsing, Python implementation and the formal codec is not established.",
  "next_action": "Extract the exact installed wire grammar and direct transition table; compare every constructor and branch to the frozen Lean definitions.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:coordinate_address_contract.json",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:COORDINATE_ADDRESS_CONVENTION.zh-CN.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:EnterpriseMath/CellAddress/ThreeRegionSlice.lean",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:src/enterprise_math/cell_address.py",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:src/enterprise_math/_cell_slice_codec.py",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:tests/test_cell_address_contract.py",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:schemas/cell_address.schema.json",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:EnterpriseMath/CellAddress/Contract.lean"
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
  "registry_key": "RS-COORD-RUNTIME-REFINEMENT-20260916",
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

# 机器坐标语言与Lean一致性：解析、合法域和执行精化

## Mother question

Can the implemented coordinate language and its supported execution paths be tied to the certified mathematical codec for all legal inputs?

## Frozen inputs and scope

The exact source snapshot is d2984d1a0c5c8221ee103084dd3da68dd039dfaa. The verified three-region slice proof is consumed unchanged (SHA256 2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02). Only final addresses change; native cell population, six axis labels, signed internal displacements, existing adjacency, decoded metric and ordered path data are retained.

Scope is the currently registered three_region_slice_v1 and declared frame, independent of unfinished full-X6 design. Preserve exact nonnegative integers and distinguish final address, raw chart, displacement and display reference. A finite random test is not a proof about all Python executions. State the trusted computing and extraction boundary explicitly.

## Hard target and required outputs

Give a grammar/AST, parser rejection specification, exact constructor correspondence and all-branch refinement proof or verified generated implementation for the supported subset. Cover booleans,1.0,negative numbers,duplicate keys,unknown codecs/frames/versions,oversized integers,invalid zero patterns and out-of-slice inputs. Verify serialization roundtrip and schema/runtime differences explicitly. Connect Lean Contract and ThreeRegionSlice imports without altering the certified proof. Provide regression tests and a complete correspondence ledger under research_artifacts/COORD_RUNTIME_REFINEMENT_20260916/.

## Research value to preserve

This is the missing machine-language trust link, not another proof of the already certified abstract slice identities.

## Success, kill, and return criteria

Success specifies and verifies the exact implementation subset and trusted boundary. Return counterexamples with reproducible inputs. Do not label differential testing alone as complete interpreter formal verification; unresolved runtime semantics remain explicit.
