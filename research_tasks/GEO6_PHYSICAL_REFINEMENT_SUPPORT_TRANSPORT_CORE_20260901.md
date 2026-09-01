<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-PHYSICAL-REFINEMENT-SUPPORT-TRANSPORT-CORE",
  "title": "GEO6 physical refinement and support transport core",
  "kind": "RESEARCH",
  "owner": "research/geo6-physical-refinement-support-transport-core",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Derive or refute a genuinely physical P000 scale-refinement map from native locality/refinement structure and classify Cell/support transport across it, without confusing abstract combinatorial refinement with physical scale semantics.",
  "next_action": "Freeze LOCALITY_REFINEMENT_SELECTOR, PHYSICAL_REFINEMENT_SELECTOR, REFINEMENT_TRANSPORT_SELECTOR and the cross-refinement portion of MIXED_DIRECTION_SELECTOR; identify the minimum typed source/target maps, locality compatibility, fiber behavior and support transport law; construct exact models separating combinatorial cover/refinement from physical P000 scale refinement.",
  "dependencies": ["RR-0A26702D3A361799ADE0", "DR-007256B8119682DF8EFA", "RR-547A186EBDE5EE6CD8A3", "RR-B5DB25EC13BF1C42DC9B", "RR-EC0502A82AD5DC3995F4"],
  "source_refs": ["driver_reviews/GEO6_OBJECTIVE_SELECTOR_SYNTHESIS_V2_DRIVER_REVIEW_20260901.md", "research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/selector_atlas_v2.json"],
  "evidence_status": "OBJECTIVE_SELECTOR_SYNTHESIS_V2_ACCEPTED / REFINEMENT_ROOT_CHAIN_SHARED_PREREQUISITE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["GEO6", "locality", "physical-refinement", "support-transport", "mixed-direction", "typed-semantics"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-PHYSICAL-REFINEMENT-SUPPORT-TRANSPORT-CORE",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6REFCORE",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
  "successor_gate": null,
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# GEO6 physical refinement and support transport core

Status: `READY / P0 / HIGH LEVERAGE`

## Mother question

Does current accepted P000/Full-Cell structure determine a **physical scale-refinement map**, rather than merely an abstract graph cover, quotient lift, or formal refinement grammar; and if such a physical map exists, how do native locality, support incidence, and mixed-direction data transport across it?

## Frozen selector chain

- `LOCALITY_REFINEMENT_SELECTOR -> PHYSICAL_REFINEMENT_SELECTOR`.
- `PHYSICAL_REFINEMENT_SELECTOR -> REFINEMENT_TRANSPORT_SELECTOR`.
- `PHYSICAL_REFINEMENT_SELECTOR -> MIXED_DIRECTION_SELECTOR` for the cross-refinement component only.
- `SUPPORT_RELATION_SELECTOR -> REFINEMENT_TRANSPORT_SELECTOR`; if support incidence remains undefined, record that dependency instead of inventing transport.

## Frozen guards

- Finite graph-cover pullback is not physical scale refinement by itself.
- Q17/Q20 abstract refinement/effectivity grammars are not physical P000 scale maps without an accepted type conversion.
- Observation/reduct maps are not automatically Full-Cell model-change arrows.
- A transport law must state source/target sorts, fiber behavior, locality compatibility and composition/coherence explicitly.
- Do not import Euclidean scaling, continuum homothety, or bundle/connection semantics by fiat.

## Hard target

`GEO6_PHYSICAL_SCALE_REFINEMENT_AND_SUPPORT_TRANSPORT_TYPED_OR_EXACTLY_OBSTRUCTED`

## Required outputs

1. Minimal typed contract for a physical P000 refinement map, including source/target state spaces and scale/locality interpretation.
2. Classification of every currently accepted candidate map as `PHYSICAL_REFINEMENT`, `ABSTRACT_REFINEMENT_ONLY`, `OBSERVATION_REDUCT_ONLY`, or `TYPE_MAP_REJECTED`.
3. Exact existence theorem or finite countermodel/no-go for physical refinement under the frozen current interface.
4. If physical refinement exists, a typed support-transport law and coherence/refinement-composition audit; if support incidence is absent, an exact dependency obstruction.
5. Classification of which mixed-direction structures can legally transport across levels, without reopening the immediate native-rotation lift owned by P000-L1.
6. Regression separation between finite quotient cover and physical refinement.
7. Deterministic checker/certificate for all finite witness claims.
8. Fresh execution record and writer-conformant Result with complete dual-digest output manifest.

## Kill rules

Kill any identification of `n -> kn` combinatorial cover with physical refinement without proof; kill abstract refinement grammar as physical geometry by notation; kill unreviewed Q22–Q26 research as accepted selector authority; kill any duplicate P000-L1 rotation/mixed-lift task.

## Driver handoff

Return a terminal typed classification. No successor publication, Working Truth, Foundation authority, native-geometry promotion, or novelty claim from the Researcher lane.