<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-COORD-INTEGRATION-ACCEPTANCE-20260916",
  "title": "坐标迁移终验：证据闭合、全空间支持与未完成项隔离",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Seven distinct representation obligations have been identified; final full-space acceptance must not run before their exact reviewed artifacts exist.",
  "next_action": "After the declared evidence dependencies are satisfied, compare their legal domains,source pins and compatibility interfaces and execute the composed acceptance suite.",
  "dependencies": [
    {
      "task_id": "RS-COORD-X6-ATLAS-20260916",
      "required_artifact": "全X6六字段非负地址图册：完整身份、合法域与登记证书：精确输入、证明/反例、可复核实现及范围说明组成的已接受证据包"
    },
    {
      "task_id": "RS-COORD-ATLAS-BRC-TRANSPORT-20260916",
      "required_artifact": "换图、旋转表示与BRC：同晶包别名和真实路径的形式化区分：精确输入、证明/反例、可复核实现及范围说明组成的已接受证据包"
    },
    {
      "task_id": "RS-COORD-LAYER-SHELL-20260916",
      "required_artifact": "第一层从1编号：层号定义、对称条件与新壳层统计：精确输入、证明/反例、可复核实现及范围说明组成的已接受证据包"
    },
    {
      "task_id": "RS-COORD-RUNTIME-REFINEMENT-20260916",
      "required_artifact": "机器坐标语言与Lean一致性：解析、合法域和执行精化：精确输入、证明/反例、可复核实现及范围说明组成的已接受证据包"
    },
    {
      "task_id": "RS-COORD-CALLER-DATA-MIGRATION-20260916",
      "required_artifact": "全调用链和存量地址迁移：身份、缓存、边界及版本保护：精确输入、证明/反例、可复核实现及范围说明组成的已接受证据包"
    },
    {
      "task_id": "RS-COORD-RESEARCH-BRIDGE-AUDIT-20260916",
      "required_artifact": "既有研究的坐标依赖审计：只修受影响桥接引理，不重开母题：精确输入、证明/反例、可复核实现及范围说明组成的已接受证据包"
    },
    {
      "task_id": "RS-COORD-CFD-OPERATOR-TRANSPORT-20260916",
      "required_artifact": "流体工程的地址迁移：网格算子、边界、AMR和舍入次序：精确输入、证明/反例、可复核实现及范围说明组成的已接受证据包"
    }
  ],
  "source_refs": [
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:coordinate_address_contract.json",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:COORDINATE_ADDRESS_CONVENTION.zh-CN.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
    "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:EnterpriseMath/CellAddress/ThreeRegionSlice.lean"
  ],
  "evidence_status": "SCOPED_SLICE_PROOF_COMPLETE_DELTA_UNFINISHED",
  "last_progress_ref": "awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md",
  "hard_block": {
    "missing_object": "The seven exact accepted coordinate-migration artifact packages named in dependencies",
    "owner": "coordinate-migration integration reviewer",
    "necessity": "Local slice proof or numerical samples do not certify full-X6 identity, all callers, layers and solver transport together",
    "unblock_condition": "Every declared dependency has an exact current accepted evidence package and the typed dependency release is validated"
  },
  "tags": [
    "coordinate-address",
    "nonnegative",
    "representation-only"
  ],
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-COORD-INTEGRATION-ACCEPTANCE-20260916",
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

# 坐标迁移终验：证据闭合、全空间支持与未完成项隔离

## Mother question

Can the coordinate migration be accepted as one coherent, scope-honest system rather than a collection of locally successful fragments?

## Frozen inputs and scope

The exact source snapshot is d2984d1a0c5c8221ee103084dd3da68dd039dfaa. The verified three-region slice proof is consumed unchanged (SHA256 2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02). Only final addresses change; native cell population, six axis labels, signed internal displacements, existing adjacency, decoded metric and ordered path data are retained.

All seven required artifacts below are gating evidence. A verified negative or intentionally restricted result must be integrated as a supported-scope restriction, not converted into global success. Existing mathematical task states and accepted statements are preserved. This integration is separate from the legacy program of choosing native upper-structure dynamics.

## Hard target and required outputs

Produce a common typed registry and proof/import dependency closure,version compatibility and caller/data coverage,composed exact and numeric tests,and final disposition by supported domain. Verify unchanged native cell identities,adjacency,metric,ordered BRC and original scalar arithmetic. Report which layer definitions are adopted and which remain parameters. Identify historical baseline failures separately from newly introduced faults. Return research_artifacts/COORD_INTEGRATION_ACCEPTANCE_20260916/acceptance_manifest.json with evidence pins and unresolved obligations.

## Research value to preserve

A gated final integration prevents the already verified two-generator slice or seven partial returns from being advertised as full-X6 completion.

## Success, kill, and return criteria

Success is complete traceable acceptance for the explicitly supported domains. Full-X6 acceptance requires the full codec artifact and every affected integration proof. Otherwise return SCOPED_ACCEPTANCE_WITH_REMAINING_GATES or a precise rejection; never silently narrow the claimed domain.
