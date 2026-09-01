<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-NATIVE-RELATION-SELECTOR-CORE",
  "title": "GEO6 native relation selector core",
  "kind": "RESEARCH",
  "owner": "research/geo6-native-relation-selector-core",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Classify the minimum typed native relation core needed to separate or connect contact/readout, non-overlap/exclusion, and Cell×Support incidence without importing carrier geometry or FCA structure by fiat.",
  "next_action": "Freeze the three reviewed selector contracts CONTACT_SELECTOR, NONOVERLAP_SELECTOR, SUPPORT_RELATION_SELECTOR; enumerate the weakest native relation signatures that could satisfy them; prove typed conversions where forced and construct exact countermodels where conversion is not forced; identify the smallest shared primitive set and its equivariance/refinement obligations.",
  "dependencies": ["RR-0A26702D3A361799ADE0", "DR-007256B8119682DF8EFA", "RR-547A186EBDE5EE6CD8A3", "RR-B5DB25EC13BF1C42DC9B", "RR-EC0502A82AD5DC3995F4"],
  "source_refs": ["driver_reviews/GEO6_OBJECTIVE_SELECTOR_SYNTHESIS_V2_DRIVER_REVIEW_20260901.md", "research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/selector_atlas_v2.json"],
  "evidence_status": "OBJECTIVE_SELECTOR_SYNTHESIS_V2_ACCEPTED / THREE_RELATION_ROOTS_SHARED_PREREQUISITE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["GEO6", "contact", "nonoverlap", "support", "native-relation", "typed-semantics"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-NATIVE-RELATION-SELECTOR-CORE",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6RELCORE",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
  "successor_gate": null,
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# GEO6 native relation selector core

Status: `READY / P0 / HIGH LEVERAGE`

## Mother question

What is the weakest genuinely native P000/Full-Cell relation structure that can distinguish and, where justified, connect:

1. `CONTACT_SELECTOR` — a native contact/readout relation rather than a carrier contact analogy;
2. `NONOVERLAP_SELECTOR` — a native exclusion/non-overlap relation suitable for packing semantics;
3. `SUPPORT_RELATION_SELECTOR` — a typed `Cell × Support` incidence suitable for Mahler-style dual-support reasoning?

The task must decide whether these three roots share a primitive core, whether one strictly determines another under accepted native hypotheses, or whether exact countermodels prove non-equivalence.

## Frozen guards

- FCC/HCP first-shell contact is comparison/carrier evidence, not native contact identity.
- Graph independent-set machinery begins only after a native exclusion relation is supplied.
- FCA/Galois closure begins only after a typed Cell×Support incidence is supplied.
- `CONTACT != NONOVERLAP` without an explicit typed conversion theorem.
- `CONTACT != SUPPORT_RELATION` without an explicit typed conversion theorem.
- No `NO_MATERIAL_MATCH` or unresolved status implies novelty.

## Hard target

`GEO6_NATIVE_RELATION_CORE_CONTACT_EXCLUSION_SUPPORT_TYPED_AND_CONVERSIONS_EXACTLY_CLASSIFIED`

## Required outputs

1. A finite typed signature atlas for candidate native relation cores, including source/target sorts and symmetry/refinement obligations.
2. Exact implication matrix among contact, exclusion, and support incidence under each admissible signature.
3. At least one same-carrier/same-readout countermodel for every conversion claimed not to be forced.
4. Minimality proof or exact lower bound for any shared primitive set proposed.
5. Compatibility audit against current accepted P000/Full-Cell data; unreviewed Results may be context but not axioms.
6. Explicit downstream interface showing what becomes available to Packing or Mahler only after the relation core is fixed.
7. Deterministic finite checker/certificate for all finite witness claims.
8. Fresh execution record and writer-conformant Result with complete dual-digest output manifest.

## Kill rules

Kill carrier contact as native identity, conflict graph as a primitive before exclusion is typed, Boolean complement/FCA as a substitute for native support incidence, and any hidden promotion of comparison geometry into P000 ontology.

## Driver handoff

Return a terminal classification. The Researcher must not publish successor tasks or grant Working Truth, Foundation, native-geometry promotion, or novelty authority.