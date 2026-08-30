<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS",
  "title": "GEO6 第二波 Packing/Kakeya 已验收结果外部先验理论与重复性综合审计",
  "kind": "RESEARCH",
  "owner": "research/geo6-secondwave-packing-kakeya-prior-art-synthesis",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Classify the exact external prior-art status of the accepted GEO6 Packing declared-model theorem and Kakeya fixed-six-axis negative boundary, then isolate only the P000-specific semantic selectors that survive theorem-by-theorem comparison.",
  "next_action": "Audit the exact packing occupancy/refinement/Følner statements and Kakeya overlap-forest/K6(r)=6r-5/circuit statements against graph theory, coding/Lee/Cayley geometry, Følner-periodic density, matroid/incidence geometry and discrete Kakeya antecedents; return one source-backed comparison matrix without inferring novelty from absence.",
  "dependencies": [
    "research_result_records/RS-GEO6-SPHERE-PACKING-DENSITY-BRIDGE/RR-71FABB059247512DF390.json",
    "research_result_records/RS-GEO6-ROTATION-KAKEYA-DIRECTIONAL-COVERAGE/RR-9D6C3A7E42B1F805C264.json"
  ],
  "source_refs": [
    "research_returns/GEO6_SPHERE_PACKING_DENSITY_BRIDGE_RESULT_REFREEZE_V2_RETURN_20260830.md",
    "research_returns/GEO6_ROTATION_KAKEYA_DIRECTIONAL_COVERAGE_RESULT_REFREEZE_V2_RETURN_20260830.md",
    "driver_reviews/GEO6_PACKING_GEN2_DRIVER_REVIEW_20260830.md",
    "driver_reviews/GEO6_KAKEYA_GEN2_DRIVER_REVIEW_20260830.md"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1 / PACKING_AND_KAKEYA_GEN2_ACCEPTED / EXTERNAL_PRIOR_ART_DUPLICATION_REQUIRED",
  "last_progress_ref": "research_result_records/RS-GEO6-ROTATION-KAKEYA-DIRECTIONAL-COVERAGE/RR-9D6C3A7E42B1F805C264.json",
  "last_progress_at": "2026-08-30T08:18:31+00:00",
  "hard_block": null,
  "tags": [
    "EXTERNAL_PRIOR_ART_DUPLICATION",
    "DRIVER_AUTO_FOLLOWUP",
    "GEO6",
    "packing",
    "Kakeya",
    "prior-art",
    "dedup",
    "integration"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6PA2",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# GEO6 第二波 Packing/Kakeya 已验收结果外部先验理论与重复性综合审计

Status: `READY / DRIVER REVIEW FOLLOW-UP / P1`

## Mother question

For the accepted GEO6 Packing generation-2 result and Kakeya generation-2 result, what is the strongest existing mathematical antecedent for each exact theorem, obstruction and finite construction, and which residue genuinely depends on unresolved P000 semantics rather than classical discrete mathematics?

## Frozen inputs and scope

Freeze only `RR-71FABB059247512DF390` and `RR-9D6C3A7E42B1F805C264` as accepted source claims. Packing must be separated into finite conflict-graph occupancy, exact `1/2` torus optimum, matching/Hoffman upper certificates, periodic/Følner density under declared translation, and quotient/refinement behavior. Kakeya must be separated into the independent-axis overlap forest, exact `K_6(r)=6r-5`, equality via connected overlap incidence, and the dependent-direction circuit countermodel. Audit against Cayley graphs, bipartite/parity codes, Lee/Hamming geometry, independent-set bounds, Følner-periodic density, hypergraph/matroid incidence, discrete line-cover problems and finite/discrete Kakeya literature only when hypotheses match. No-match is not novelty.

## Hard target and required outputs

Hard target: `GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACTLY_CLASSIFIED`.

Required outputs:
1. one source-backed claim matrix for every accepted Packing and Kakeya theorem/obstruction;
2. classification `EXACT_DUPLICATE / STRICT_ANTECEDENT / ADJACENT_METHOD / NO_MATERIAL_MATCH` for each row;
3. exact hypothesis comparison for every exact/strict match;
4. a kill list for continuations that merely rename standard graph/coding/Følner/incidence facts;
5. a surviving selector map restricted to `NONOVERLAP_SELECTOR`, `TRANSLATION_FOLNER_SELECTOR`, `PHYSICAL_REFINEMENT_SELECTOR`, and `MIXED_DIRECTION_SELECTOR`;
6. a Driver recommendation stating which selector, if any, has a concrete accepted P000/Full-Cell datum capable of resolving it.

## Research value to preserve

The purpose is not to erase useful Enterprise geometry because a finite theorem is classical. It is to separate reusable standard mathematics from the genuinely unresolved typing question: which conflict relation, translation action, physical refinement and mixed-direction semantics are native. Preserve exact countermodels and P000 firewalls.

## Success, kill, and return criteria

Success means every accepted claim has a source-backed classification and all duplicate-only continuations are explicitly killed. Return `AUDIT_COMPLETE` even if every finite theorem is classical. Do not infer novelty from search absence. Do not publish a mathematical successor from this Researcher execution. A stronger GEO6 continuation is Driver-only after this audit and must name both one surviving selector and the accepted native datum proposed to resolve it.
