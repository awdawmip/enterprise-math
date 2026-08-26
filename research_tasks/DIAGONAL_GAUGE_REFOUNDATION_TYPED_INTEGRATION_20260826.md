<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-DIAGONAL-GAUGE-REFOUNDATION-TYPED-INTEGRATION",
  "title": "Diagonal Gauge Refoundation — Typed Derived Displacement Integration",
  "kind": "GOVERNANCE",
  "owner": "integration/diagonal-gauge-refoundation-typed-integration",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "DERIVED_G1_DIAGONAL_DISPLACEMENT_TYPED_INTEGRATION_APPLIED_WITHOUT_NATIVE_POINT_OR_PATH_COLLAPSE",
  "next_action": "Integrate only the Driver-accepted G1 derived-displacement typing boundary: add the separately typed G_D/A_D derived object, narrow the primitive native-point diagonal-shift prohibition, preserve all current R061/R062 formulas and metric semantics, and freeze a no-new-mathematics integration audit.",
  "dependencies": [
    "driver_reviews/DIAGONAL_GAUGE_REFOUNDATION_INDEPENDENT_REVIEW_DRIVER_REVIEW_20260826.md@55fb2954ab3509e5d10580d85db96d1a7d2e004e",
    "research_result_reviews/RR-A2BA65F5CC061AF93340/RV-00BD838F76D25EEA4A11.json@07c07dd8affa5f6af7ba830f216fd1232a973b33",
    "definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md#blob=393060ebfd6a86ad45f258747d78a14d9c8ac153",
    "definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md#blob=03c3cd9d11df4005f2c1c3ab8bd76ee8eb6763a6",
    "definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md#blob=da35c76869ff88e46e28e33ba5bc37c95374a15d",
    "definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md#blob=6ec0d73a19e28ec586c59a97d24f5798c9119771"
  ],
  "source_refs": [
    "driver_reviews/DIAGONAL_GAUGE_REFOUNDATION_INDEPENDENT_REVIEW_DRIVER_REVIEW_20260826.md@55fb2954ab3509e5d10580d85db96d1a7d2e004e",
    "research_result_reviews/RR-A2BA65F5CC061AF93340/RV-00BD838F76D25EEA4A11.json@07c07dd8affa5f6af7ba830f216fd1232a973b33",
    "definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md#blob=393060ebfd6a86ad45f258747d78a14d9c8ac153",
    "definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md#blob=03c3cd9d11df4005f2c1c3ab8bd76ee8eb6763a6",
    "definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md#blob=da35c76869ff88e46e28e33ba5bc37c95374a15d",
    "definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md#blob=6ec0d73a19e28ec586c59a97d24f5798c9119771"
  ],
  "evidence_status": "DRIVER_ACCEPTED_TYPED_NARROWING_INTEGRATION_AUTHORIZED",
  "last_progress_ref": "driver_reviews/DIAGONAL_GAUGE_REFOUNDATION_INDEPENDENT_REVIEW_DRIVER_REVIEW_20260826.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["DGR", "diagonal-gauge", "typed-integration", "G1", "derived-displacement", "R061", "R062", "no-new-mathematics"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-DIAGONAL-GAUGE-REFOUNDATION-TYPED-INTEGRATION",
  "parent_objective_id": "OBJ-DIAGONAL-GAUGE-REFOUNDATION-TYPED-CORRECTION-EVIDENCE-CLOSURE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "DGRINT",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "INTEGRATION",
  "parent_task_id": "RS-DIAGONAL-GAUGE-REFOUNDATION-INDEPENDENT-REVIEW",
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Diagonal Gauge Refoundation — Typed Derived Displacement Integration

Status: `PUBLISHED_REGISTERED / CLAIMABLE / NO_NEW_MATHEMATICS`

## Mother question

Can the independently accepted diagonal-gauge result be integrated as a separately typed G1 derived endpoint/displacement object while preserving the primitive native point/address ontology, current R061/R062 formulas, current metric semantics, Path-formal provenance, and source/target composition typing exactly?

## Frozen inputs and scope

Use only the accepted Driver review and immutable result disposition together with the four pinned current definition blobs listed in task metadata. This task is source integration, not theorem discovery.

The accepted mathematical content is fixed:

- `G_D = Z^3 / Z(1,1,1) ~= Z^2` as a derived displacement object;
- `can(z)=z-min(z)(1,1,1)` as its unique nonnegative min-zero section;
- current R061 Stage-2 displacement decoding, composition, and reversal are compatible with that derived object;
- introduce a semantic type `A_D = MIN_ZERO_DERIVED_DISPLACEMENT_SECTION` distinct from the primitive/current address type `A_E`;
- the primitive native-point/address layer is not quotiented by diagonal shift;
- current R061 directed line gauge and Stage-3 bidirectional spectrum remain unchanged;
- R062 Path-formal/N/Boolean semantics remain unchanged;
- bare Path-formal paths do not receive a total Stage-2 displacement map without explicit endpoint typing;
- ordinary untyped `N[G_D]` multiplication is not native path composition;
- the historical diagonal-invariant quadratic `Delta` is not restored as the native Enterprise length.

Allowed source changes are limited to an explicit derived-displacement definition and narrowly scoped interpretive/type annotations necessary to remove the old blanket ambiguity. No new mathematical premise, theorem strengthening, metric law, path quotient, or carrier identification may be introduced.

## Hard target and required outputs

Hard target:

`DERIVED_G1_DIAGONAL_DISPLACEMENT_TYPED_INTEGRATION_APPLIED_WITHOUT_NATIVE_POINT_OR_PATH_COLLAPSE`.

Required outputs:

1. add `definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md` defining `G_D`, `can`, and `A_D` strictly as a G1 derived endpoint/displacement layer;
2. narrow the plane-foundation wording so the prohibition is exactly `NO_PRIMITIVE_NATIVE_POINT_DIAGONAL_SHIFT_QUOTIENT`, while explicitly stating that this does not prohibit a separately typed derived G1 displacement quotient;
3. add only non-formula-changing cross-reference/typing notes to the current R061 definition if needed to record Stage-2 compatibility; do not change its decoder, composition, reversal, directed gauge, or Stage-3 spectrum;
4. do not change R062 mathematical content; if a note is necessary, it may only restate that displacement forgetting does not identify Path-formal witnesses or native line identity;
5. freeze `research_returns/DIAGONAL_GAUGE_REFOUNDATION_TYPED_INTEGRATION_RETURN_20260826.md` listing every changed path and proving that each change is interpretive/type-only;
6. freeze a compact invariant audit showing `A_D != A_E`, no bare global `PF_PATH -> G_D`, no untyped path multiplication in `N[G_D]`, no native-metric replacement, and no change to the accepted R061/R062 equations.

## Research value to preserve

The independent review found a real derived displacement algebra already latent in current R061, but also found that the original candidate overreached at the primitive-address and path-category boundaries. Preserving the narrowed result removes a Foundation typing ambiguity without erasing path provenance, weakening the native point ontology, or silently reviving a superseded metric. This distinction is load-bearing for future geometry and BRC work.

## Success, kill, and return criteria

Success requires all required outputs to agree exactly with the Driver-accepted narrowing and to leave all current R061/R062 mathematical formulas unchanged.

Kill and stop with verdict `DGR_TYPED_INTEGRATION_REQUIRES_NEW_MATHEMATICS_OR_OVERREACH` if any requested integration would require a new theorem, a new cell-to-vertex bridge, a total bare path-to-displacement map, an untyped path algebra on `N[G_D]`, identification of `A_D` with `A_E`, restoration of `Delta` as native length, or any other change beyond the accepted G1 typing boundary.

The frozen return must state one of:

- `DGR_TYPED_INTEGRATION_APPLIED_EXACTLY`;
- `DGR_TYPED_INTEGRATION_APPLIED_WITH_STRICTER_NARROWING`;
- `DGR_TYPED_INTEGRATION_REQUIRES_NEW_MATHEMATICS_OR_OVERREACH`.

Stop after the integration return and invariant audit. Do not open a new geometry theorem stage from this task.
