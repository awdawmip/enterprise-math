<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT",
  "title": "Native Filament — Post-audit Hyperbola/Joukowski External Prior-art and Duplication Audit",
  "kind": "RESEARCH",
  "owner": "audit/native-filament-postaudit-hyperbola-joukowski-prior-art",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Classify the external prior-art and duplication boundary of the accepted narrowed H1/H2/J1/J2/C1/C2 statement layer without rewriting the independently replicated result.",
  "next_action": "Search authoritative literature and repositories for exact or structurally equivalent antecedents of the split-hyperbola tangent quotient, finite-field sign-orbit count, Joukowski/Dickson image formula, extremal saturation obstruction, and boundary-closure arithmetic; classify exact duplicate, partial antecedent, adjacent method, and no material match separately.",
  "dependencies": [
    "research_result_records/RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION/RR-680C6257EEF10F6F1C16.json@main",
    "research_returns/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_RETURN_20260829.md@main",
    "driver_reviews/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260829.md@main"
  ],
  "source_refs": [
    "research_inputs/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_BLIND_PACKET_20260825.md#blob=6ce9ea10f02fded1959c55a1b78044ada434360f",
    "RR-680C6257EEF10F6F1C16",
    "DR-289F116DBE89C6FA1339"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1 / ACCEPTED_WITH_NARROWING",
  "last_progress_ref": "driver_reviews/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260829.md",
  "last_progress_at": "2026-08-29T01:33:20+00:00",
  "hard_block": null,
  "tags": [
    "EXTERNAL_PRIOR_ART_DUPLICATION",
    "DRIVER_AUTO_FOLLOWUP",
    "native-filament",
    "hyperbola",
    "Joukowski",
    "Dickson",
    "finite-field",
    "prior-art"
  ],
  "claim_lease_minutes": 480,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT",
  "parent_objective_id": "RS-NATIVE-FILAMENT-COUPLED-SELECTION-INDEPENDENT-AUDIT",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "NFHJPA",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION",
  "successor_gate": {
    "new_information_gap": "The blind replication establishes exact/narrowed mathematical truth inside the frozen statement universe but intentionally does not determine whether the accepted mechanisms are classical, duplicated, partially anteceded, or distinctive only in their Enterprise composition.",
    "why_parent_result_does_not_close_it": "Independent reconstruction and source novelty are different questions. The accepted result deliberately makes no external-prior-art or novelty claim.",
    "discriminating_outcomes": [
      "Find an external theorem exactly equivalent to one or more accepted rows under matching hypotheses.",
      "Find classical antecedents for individual ingredients but no source matching the integrated H/J/C statement layer.",
      "Find a stronger external framework that subsumes an accepted row and should be reused as terminology or proof machinery.",
      "Find no material match in the audited set while explicitly declining to infer novelty from absence."
    ],
    "kill_condition": "Keyword similarity without exact hypothesis/conclusion mapping, or a no-match search promoted into a novelty claim, does not close the audit.",
    "alternative_route_or_free_exploration_considered": "A new mathematical continuation was considered and rejected because the classification task is already terminal; external duplication audit is the only forced post-acceptance gate not already satisfied by the reviewed result.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Separating prior-art classification preserves the clean blind result while allowing source comparison only after the independent freeze is complete."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Native Filament — Post-audit Hyperbola/Joukowski External Prior-art and Duplication Audit

Status: `READY / DRIVER REVIEW FOLLOW-UP / SOURCE-COMPARISON ONLY`

## Mother question

Which parts of the accepted narrowed H1/H2/J1/J2/C1/C2 layer are exact duplicates of known external mathematics, which are special cases or recombinations of classical structures, and which have no material match in the audited sources?

## Frozen inputs and scope

Freeze `RR-680C6257EEF10F6F1C16` and its Driver-accepted wording. J1/J2/C1 are consumed exactly; H1/H2/C2 are consumed only under the narrowed statements frozen in the return and Driver review.

This task may now read external literature and the previously withheld source package because the blind replication has already frozen. External comparison may classify duplication, terminology, proof ancestry, and reusable tools; it must not retroactively alter the independent provenance of the frozen result.

Do not restore stronger H1/H2/C2 wording merely because a source branch used it. Do not infer novelty from absence of a match.

## Hard target and required outputs

Hard target: `NATIVE_FILAMENT_HJ_EXTERNAL_PRIOR_ART_DUPLICATION_BOUNDARY_CLASSIFIED`.

Required outputs: a source-backed table for H1, H2, J1, J2, C1 and C2; exact hypotheses/conclusions for every candidate antecedent; classification into `EXACT_DUPLICATE`, `PARTIAL_ANTECEDENT`, `ADJACENT_METHOD`, or `NO_MATERIAL_MATCH_IN_AUDITED_SET`; explicit treatment of classical split hyperbolas, Burnside orbit counting, finite-field quadratic characters, Joukowski/Dickson maps, involution image counts, extremal finite-field moment arguments, and the arithmetic closure step; and a final statement of which Enterprise composition claims remain only project-specific recombinations.

## Research value to preserve

The blind replication established mathematical reliability without source anchoring. This follow-up prevents that success from being confused with novelty and prevents standard external mathematics from being unnecessarily rediscovered under project-specific names.

## Success, kill, and return criteria

Success requires authoritative sources plus exact structural mapping, not a generic bibliography.

Kill any conclusion that treats terminology overlap as theorem duplication, treats no search hit as proof of novelty, or uses a stronger external/source statement to overwrite the already accepted narrowed theorem boundary.

Return one strongest duplication map and recommendations for reusable terminology or proof machinery. No Working Truth, Foundation, or promotion follows automatically.
