<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS",
  "title": "GEO6 native translation and Følner semantics",
  "kind": "RESEARCH",
  "owner": "research/geo6-native-translation-folner-semantics",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Derive or refute a typed native P000 translation/amenable action together with admissible period, window, boundary and Følner semantics; do not import Z^6 translation structure from the comparison model.",
  "next_action": "Freeze TRANSLATION_ACTION_SELECTOR and TRANSLATION_FOLNER_SELECTOR; enumerate current accepted candidate actions on Cells/Full-Cells; require exact source/target/action laws and native invariance; classify period/window/boundary notions and prove a Følner-type density interface or an exact obstruction.",
  "dependencies": ["RR-0A26702D3A361799ADE0", "DR-007256B8119682DF8EFA", "RR-547A186EBDE5EE6CD8A3", "RR-B5DB25EC13BF1C42DC9B"],
  "source_refs": ["driver_reviews/GEO6_OBJECTIVE_SELECTOR_SYNTHESIS_V2_DRIVER_REVIEW_20260901.md", "research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/selector_atlas_v2.json"],
  "evidence_status": "OBJECTIVE_SELECTOR_SYNTHESIS_V2_ACCEPTED / TRANSLATION_ROOT_CHAIN_SHARED_PREREQUISITE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["GEO6", "translation", "Folner", "amenable-action", "period", "window", "density"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6TRANSFOL",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
  "successor_gate": null,
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# GEO6 native translation and Følner semantics

Status: `READY / P1 / HIGH LEVERAGE`

## Mother question

Does current accepted P000/Full-Cell structure provide a genuinely native translation or amenable action from which period/window/boundary and Følner-density semantics can be derived, or is the entire global-density layer still dependent on an externally declared `Z^6` comparison model?

## Frozen dependency

`TRANSLATION_ACTION_SELECTOR -> TRANSLATION_FOLNER_SELECTOR`.

The task must settle the lower-level action before treating Følner density as native. If no acceptable native action exists, freeze that obstruction instead of importing one.

## Frozen guards

- `Z^6` translation is comparison structure, not native P000 truth.
- Periodic quotient density theorems are classical after an action and finite-index period structure are declared.
- A window/boundary notion must be native-typed and action-compatible before a Følner limit has native meaning.
- Do not infer amenability from finite carrier symmetry or from notation such as coordinates/axes.
- Do not reopen the already-classical periodic counting theorem; the research target is semantic authorization.

## Hard target

`GEO6_NATIVE_TRANSLATION_ACTION_AND_FOLNER_DENSITY_INTERFACE_TYPED_OR_EXACTLY_OBSTRUCTED`

## Required outputs

1. Inventory of current accepted candidate native actions on Cell/Full-Cell states, with exact source/target and composition laws.
2. Classification `NATIVE_ACTION / PARTIAL_ACTION / PRESENTATION_EQUIVALENCE_ONLY / COMPARISON_ONLY / TYPE_MAP_REJECTED`.
3. If a native action exists, exact admissible period and window classes, boundary operator, and a Følner/amenability criterion sufficient for density.
4. If no native action exists, finite same-readout countermodels showing why comparison translations are not forced.
5. Typed interface showing precisely when the accepted classical periodic/Følner counting results may be reused downstream.
6. Equivariance compatibility with the native relation core where relevant, without requiring that other successor to finish first unless logically necessary.
7. Deterministic checker/certificate for finite witness claims.
8. Fresh execution record and writer-conformant Result with complete dual-digest output manifest.

## Kill rules

Kill `coordinate shift = native translation` by notation alone; kill finite carrier permutations as proof of amenability; kill classical Følner theory as a substitute for the missing native action; kill novelty inference from an obstruction.

## Driver handoff

Return a terminal typed classification. The Researcher must not publish successors or grant Working Truth, Foundation authority, canonical promotion, or novelty authority.