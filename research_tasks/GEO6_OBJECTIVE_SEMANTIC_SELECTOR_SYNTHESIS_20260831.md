<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
  "title": "GEO6 objective-level semantic-selector synthesis",
  "kind": "RESEARCH",
  "owner": "research/geo6-objective-semantic-selector-synthesis",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Normalize and deduplicate the twelve selector labels surviving the three canonically reviewed GEO6 prior-art boundaries, then determine exactly which are resolved, partially constrained, duplicated, dependent, or still unresolved by the latest canonical ACCEPTED P000/Full-Cell evidence.",
  "next_action": "Build a selector provenance/equivalence/dependency atlas from the three accepted GEO6 prior-art reviews; scan the current repository for canonical ACCEPTED P000/Full-Cell review+Result pairs; require an explicit type/hypothesis map before any accepted datum can count as a resolver; return a normalized selector set and at most three justified successor recommendations without publishing those successors.",
  "dependencies": [
    "RR-547A186EBDE5EE6CD8A3",
    "DR-CE3F008C48F9EBBFF9FA",
    "RR-B5DB25EC13BF1C42DC9B",
    "DR-4187E7655E4E30A30253",
    "RR-EC0502A82AD5DC3995F4",
    "DR-6A6587387463AE326117"
  ],
  "source_refs": [
    "driver_reviews/GEO6_FIRSTWAVE_PRIOR_ART_GEN3_DRIVER_REVIEW_20260830.md",
    "driver_reviews/GEO6_PACKING_KAKEYA_EXACT_SET_V3_DRIVER_REVIEW_20260831.md",
    "driver_reviews/GEO6_MAHLER_PRIOR_ART_DRIVER_REVIEW_20260830.md"
  ],
  "evidence_status": "THREE_CANONICAL_PRIOR_ART_BOUNDARIES_AVAILABLE / OBJECTIVE_SELECTOR_NORMALIZATION_REQUIRED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["GEO6", "objective-integration", "semantic-selector", "P000", "Full-Cell", "exact-set", "resolver-audit"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6OBJSYN",
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

# GEO6 objective-level semantic-selector synthesis

Status: `READY / P0 / OBJECTIVE INTEGRATION`

## Mother question

After all six original GEO6 mathematics lanes and all three GEO6 prior-art/control boundaries have canonical terminal Driver review authority, what is the **minimal normalized set of genuinely unresolved native semantic selectors**, and does the latest canonical ACCEPTED P000/Full-Cell evidence already resolve or partially constrain any of them?

The task is not another classical-geometry search and not permission to open twelve independent research lanes. It is the parent-objective integration gate that decides whether the geometry objective should close, revise, or publish a small successor task set.

## Frozen selector inputs

### First-wave Kissing/Falconer/Hadwiger

- `CONTACT_SELECTOR`
- `LOCALITY_REFINEMENT_SELECTOR`
- `ROTATION_CLOSURE_SELECTOR`
- `TRANSLATION_ACTION_SELECTOR`

### Packing/Kakeya

- `NONOVERLAP_SELECTOR`
- `TRANSLATION_FOLNER_SELECTOR`
- `PHYSICAL_REFINEMENT_SELECTOR`
- `MIXED_DIRECTION_SELECTOR`

### Mahler/dual support

- `SUPPORT_RELATION_SELECTOR`
- `SELF_DUAL_IDENTIFICATION_SELECTOR`
- `COMPLEXITY_FUNCTIONAL_SELECTOR`
- `REFINEMENT_TRANSPORT_SELECTOR`

The source prior-art classifications and kill decisions are immutable inputs. This task may normalize selector terminology and dependency structure, but may not resurrect classical finite/fixed-carrier claims that the reviewed audits already continuation-killed.

## Resolver authority rule

A selector may be classified `RESOLVED_BY_ACCEPTED_DATUM` only if the researcher identifies all of:

1. an immutable canonical Driver review record with `disposition=ACCEPTED`;
2. the exact Result bound by that review;
3. an explicit type/hypothesis map showing that the accepted datum satisfies every obligation of the selector rather than merely resembling it.

Raw Results, open/draft research PRs, unreviewed artifacts on `main`, routing notes, comparison carriers, external models, or suggestive current mathematics **cannot** close a selector. They may be recorded as context only.

## Required selector relations

For every relevant selector pair, classify the relation as exactly one of:

- `SAME_SELECTOR`
- `STRICT_DEPENDENCY`
- `OVERLAP_NOT_EQUIVALENT`
- `ORTHOGONAL`
- `UNRESOLVED_RELATION`

If `A STRICT_DEPENDENCY B`, state direction explicitly and prove why resolving one is necessary or sufficient for progress on the other.

## Required normalized status

Every normalized selector must receive one status:

- `RESOLVED_BY_ACCEPTED_DATUM`
- `PARTIALLY_CONSTRAINED_BY_ACCEPTED_DATUM`
- `UNRESOLVED`
- `DUPLICATE_SELECTOR`

`PARTIALLY_CONSTRAINED_BY_ACCEPTED_DATUM` requires an exact accepted theorem that eliminates at least one admissible semantic class but does not meet the full selector contract.

## Hard target and outputs

Hard target:

`GEO6_OBJECTIVE_SELECTOR_SET_NORMALIZED_AND_CURRENT_ACCEPTED_RESOLVERS_EXACTLY_CLASSIFIED`

Required outputs:

1. a selector provenance matrix linking every original selector to its reviewed Result/review authority;
2. a selector equivalence/dependency graph with one of the five permitted pair relations;
3. an accepted-resolver manifest listing every candidate accepted P000/Full-Cell datum actually audited;
4. a normalized selector set with one of the four permitted statuses per selector;
5. a prerequisite ordering or dependency DAG for unresolved selectors;
6. a kill list for duplicate, already-resolved, or merely renamed classical structures;
7. a ranked Driver recommendation containing **at most three** candidate successor tasks; zero is allowed and preferred when no accepted datum creates a justified route;
8. a deterministic checker and machine-readable selector atlas/resolver manifest;
9. a fresh execution record and writer-conformant Result with a complete dual-digest output manifest.

## Parent-objective decision surface

The researcher must return enough information for the Driver to choose one of:

- `PARENT_OBJECTIVE_CLOSE`
- `PARENT_OBJECTIVE_REVISE`
- `MINIMAL_SUCCESSOR_TASKSET_JUSTIFIED`

The researcher does **not** publish successor tasks and does not grant Working Truth, Foundation status, native-geometry promotion, or novelty authority.

## Kill rules

Kill any proposed resolver that relies only on an unreviewed Result, a comparison carrier, a loose analogy, or a missing type map. Kill any selector continuation whose remaining content is already classical under the accepted hypotheses. Kill any attempt to infer novelty from `NO_MATERIAL_MATCH`, unresolved status, or search absence.

Do not mechanically split the normalized selector set into one task per label. If multiple selectors share a missing primitive, relation, action, or refinement transport, represent that dependency explicitly and prefer one lower-level prerequisite.

## Success and return criteria

Success requires an exact, source-backed normalized selector atlas and accepted-resolver classification at a declared repository snapshot. The return must make clear which conclusions depend on accepted review authority versus contextual/unreviewed evidence.

If no accepted P000/Full-Cell datum resolves any selector, that is a valid terminal synthesis outcome: rank the minimal prerequisites, recommend at most three follow-ups, and leave actual task publication to Driver review.
