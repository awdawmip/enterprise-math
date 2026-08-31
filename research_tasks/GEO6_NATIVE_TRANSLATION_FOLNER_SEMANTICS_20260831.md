<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS",
  "title": "GEO6 Native Translation and Følner Semantics",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Derive or refute a typed native translation/amenable action and admissible period, window and boundary semantics that can support a genuine Følner selector.",
  "next_action": "Define candidate native translation actions from accepted Cell structure without assuming Euclidean vectors; test group/semigroup action laws and finite-window boundary ratios, then prove amenability/Følner behavior or an exact obstruction.",
  "dependencies": ["RR-35C4FE925E9C12E53604"],
  "source_refs": ["research_returns/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS_RETURN_20260831.md","research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/selector_atlas.json","research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/accepted_resolver_manifest.json"],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": "RR-35C4FE925E9C12E53604",
  "last_progress_at": "2026-08-31T02:47:19+00:00",
  "hard_block": null,
  "tags": ["GEO6","DRIVER_AUTO_FOLLOWUP","MATHEMATICAL_CONTINUATION","GEO6_TRANSLATION_CORE"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GEO6_TRANSLATION_CORE",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
  "successor_gate": {
    "new_information_gap": "The accepted atlas has TRANSLATION_ACTION as a root and proves it is a prerequisite for TRANSLATION_FOLNER, with neither currently resolved.",
    "why_parent_result_does_not_close_it": "The prior Packing/Kakeya work cannot interpret windows or density limits until the underlying native action is typed.",
    "discriminating_outcomes": ["NATIVE_TRANSLATION_AND_FOLNER_SEMANTICS_PROVED","NATIVE_TRANSLATION_EXISTS_BUT_FOLNER_FAILS","NATIVE_TRANSLATION_ACTION_OBSTRUCTED"],
    "kill_condition": "If every candidate is merely a classical coordinate translation or a chosen enumeration shift not preserved by native structure, freeze that no-go.",
    "alternative_route_or_free_exploration_considered": "A separate Følner task before translation was considered and rejected because the atlas proves translation action is the prerequisite root.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent atlas is terminal; this continuation directly attacks one independent root with a sharply bounded semantic interface."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]},
  "parent_objective_generation_id": "OG-BB398D541DDECF58D19E"
}
-->

# GEO6 Native Translation and Følner Semantics

Status: `READY / P0 / GEO6 DRIVER FOLLOW-UP`

## Mother question

Is there a native translation action on the accepted Cell system from which period/window/boundary and Følner semantics actually follow?

## Frozen inputs and scope

Freeze `RR-35C4FE925E9C12E53604`: native translation action and TRANSLATION_FOLNER_SELECTOR are unresolved; period/window language alone is not an action, and classical Euclidean/lattice translation is not native without a typed theorem. Existing P000 rotation work is orthogonal and must not be duplicated.

## Hard target and required outputs

Hard target: `GEO6_NATIVE_TRANSLATION_FOLNER_SEMANTICS_EXACTLY_CLASSIFIED`.

Required outputs: (1) a typed candidate action or exact no-action theorem for the declared native state space; (2) action/naturality laws; (3) admissible finite windows and boundary definition; (4) Følner/amenability theorem with hypotheses or exact obstruction; (5) dispositions for TRANSLATION_ACTION_SELECTOR and TRANSLATION_FOLNER_SELECTOR; (6) explicit comparison firewall against classical Euclidean translation.

## Research value to preserve

Translation is the missing semantic bridge behind the Packing/Kakeya boundary. The goal is not to import amenability vocabulary but to test whether the native system genuinely supports it.

## Success, kill, and return criteria

Success requires a native action plus exact Følner theorem, or a scoped obstruction identifying the minimum additional state/action needed. Kill mere coordinate shifts, preselected periodic boxes, or boundary ratios without an action law. Return a durable Result and no automatic novelty claim.
