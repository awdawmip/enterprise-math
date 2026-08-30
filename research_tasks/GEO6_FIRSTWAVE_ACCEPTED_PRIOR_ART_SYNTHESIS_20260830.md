<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-FIRSTWAVE-ACCEPTED-PRIOR-ART-SYNTHESIS",
  "title": "GEO6 第一波已验收几何结果外部先验理论与重复性综合审计",
  "kind": "RESEARCH",
  "owner": "research/geo6-firstwave-accepted-prior-art-synthesis",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Classify the exact external prior-art status of the accepted Kissing contact-capacity atlas, Falconer relation-distance forcing/locality no-go, and Hadwiger signed-shell cover/illumination classification, then isolate only the Enterprise-specific semantic residue that survives theorem-by-theorem comparison.",
  "next_action": "Search and reconstruct the strongest formal antecedents for each accepted theorem family, build one cross-result comparison matrix, and return exact duplicate/strict antecedent/adjacent method/no-material-match labels without inferring novelty from absence.",
  "dependencies": [
    "research_result_records/RS-GEO6-KISSING-CONTACT-CAPACITY-BRIDGE/RR-EBAF426828157644FB51.json",
    "research_result_records/RS-GEO6-FALCONER-RELATION-DISTANCE-SPECTRUM/RR-36E518770A5FB701B42C.json",
    "research_result_records/RS-GEO6-HADWIGER-CELL-COVER-ILLUMINATION/RR-589899C832BA7069520F.json"
  ],
  "source_refs": [
    "research_result_records/RS-GEO6-KISSING-CONTACT-CAPACITY-BRIDGE/RR-EBAF426828157644FB51.json",
    "research_returns/GEO6_KISSING_CONTACT_CAPACITY_BRIDGE_RETURN_20260830.md",
    "research_result_records/RS-GEO6-FALCONER-RELATION-DISTANCE-SPECTRUM/RR-36E518770A5FB701B42C.json",
    "research_returns/GEO6_FALCONER_RELATION_DISTANCE_SPECTRUM_RETURN_20260830.md",
    "research_result_records/RS-GEO6-HADWIGER-CELL-COVER-ILLUMINATION/RR-589899C832BA7069520F.json",
    "research_returns/GEO6_HADWIGER_CELL_COVER_ILLUMINATION_RETURN_20260830.md"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1 / THREE_ACCEPTED_RESULTS / EXTERNAL_PRIOR_ART_DUPLICATION_REQUIRED",
  "last_progress_ref": "research_result_records/RS-GEO6-HADWIGER-CELL-COVER-ILLUMINATION/RR-589899C832BA7069520F.json",
  "last_progress_at": "2026-08-30T06:13:00+00:00",
  "hard_block": null,
  "tags": [
    "EXTERNAL_PRIOR_ART_DUPLICATION",
    "DRIVER_AUTO_FOLLOWUP",
    "GEO6",
    "geometry",
    "prior-art",
    "dedup",
    "integration"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-FIRSTWAVE-ACCEPTED-PRIOR-ART-SYNTHESIS",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6PA",
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

# GEO6 第一波已验收几何结果外部先验理论与重复性综合审计

Status: `READY / DRIVER REVIEW FOLLOW-UP / P1`

## Mother question

For the three first-wave GEO6 results already accepted at exact task scope—Kissing contact capacity, Falconer relation spectrum, and Hadwiger signed-shell cover/illumination—what is the strongest published antecedent for each accepted theorem, and which residue, if any, remains specific to P000 typing, readout, locality, or operation semantics?

## Frozen inputs and scope

Freeze only `RR-EBAF426828157644FB51`, `RR-36E518770A5FB701B42C`, and `RR-589899C832BA7069520F` as accepted Enterprise source claims. Audit each theorem separately against finite homogeneous spaces and association schemes, root systems and spherical codes, graph metrics and lattice growth, Hamming/coding schemes, sign-vector and hypercube set-cover problems, group actions, oriented-matroid-style combinatorics, and relevant classical geometry only where formal hypotheses match. Packing, Kakeya, and Mahler are excluded until their Result envelopes are repaired and separately accepted. A no-match search result is not a novelty certificate.

## Hard target and required outputs

Hard target: `GEO6_FIRSTWAVE_ACCEPTED_CLAIMS_PRIOR_ART_EXACTLY_CLASSIFIED`.

Required outputs:
1. source-backed exact statements and hypotheses for every strongest candidate antecedent;
2. one claim-to-source matrix covering every accepted theorem and obstruction;
3. classification `EXACT_DUPLICATE / STRICT_ANTECEDENT / ADJACENT_METHOD / NO_MATERIAL_MATCH`;
4. at least one formal comparison argument for every nontrivial exact/strict match;
5. a cross-result residue map separating standard finite mathematics from P000-specific semantic gaps;
6. a recommendation that kills duplicate continuations and identifies only genuinely unresolved research interfaces.

## Research value to preserve

Even if the finite combinatorics are classical, the accepted results may still expose project-specific semantic bottlenecks: contact definability under current readouts, locality/refinement selection, and dependence of cover numbers on the permitted operation family. The audit must preserve those typed residues while removing unsupported novelty implications.

## Success, kill, and return criteria

Success means every accepted claim receives a source-backed classification and the remaining Enterprise-specific residue is sharply bounded. If an exact antecedent matches a claim, kill novelty-based continuation for that claim. Return `AUDIT_COMPLETE` even if all claims are duplicates. Do not force a match across non-equivalent hypotheses, and do not treat search absence as proof of novelty.
