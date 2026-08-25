<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-NATIVE-FILAMENT-COUPLED-SELECTION-EXTERNAL-NOVELTY-INDEPENDENT-REEXECUTION",
  "title": "Native Filament Coupled Selection — Provenance-Clean External Novelty Re-execution",
  "kind": "RESEARCH",
  "owner": "audit/native-filament-coupled-selection-independent-novelty-reexecution-20260825",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_INDEPENDENTLY_CLASSIFIED_WITH_PROVENANCE_CLEAN",
  "next_action": "Using only the frozen statement-only literature-audit packet and external literature, independently classify S1-S8 and the whole coupled chain against prior art without reading PR #627, the source branch, or the direct nonblind literature audit before return freeze. Freeze theorem-level mappings, search logs, confidence and one allowed classification per row; do not infer novelty from absence of a hit.",
  "dependencies": [
    "driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_DRIVER_REVIEW_20260825.md@d4e3f8eca68bff1d8803b8eb74402fc6d69e7b5f",
    "driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_AUDIT_DRIVER_REVIEW_20260825.md@d9d3db11489196e5ef62ff435d4691f08b6b77d5",
    "audit/native-filament-coupled-selection-literature-20260825:research_inputs/NATIVE_FILAMENT_COUPLED_SELECTION_V2_LITERATURE_AUDIT_PACKET_20260825.md#blob=2199c2bd34b44361570a4b68d85dcece70d6fba4"
  ],
  "source_refs": [
    "audit/native-filament-coupled-selection-literature-20260825:research_inputs/NATIVE_FILAMENT_COUPLED_SELECTION_V2_LITERATURE_AUDIT_PACKET_20260825.md#blob=2199c2bd34b44361570a4b68d85dcece70d6fba4",
    "driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_DRIVER_REVIEW_20260825.md@d4e3f8eca68bff1d8803b8eb74402fc6d69e7b5f",
    "driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_AUDIT_DRIVER_REVIEW_20260825.md@d9d3db11489196e5ef62ff435d4691f08b6b77d5"
  ],
  "evidence_status": "ORIGINAL_INDEPENDENT_NOVELTY_HARD_TARGET_OPEN_NONBLIND_SUPPORTING_AUDIT_ALREADY_FROZEN",
  "last_progress_ref": "driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_AUDIT_DRIVER_REVIEW_20260825.md@d9d3db11489196e5ef62ff435d4691f08b6b77d5",
  "last_progress_at": "2026-08-25T20:13:00+08:00",
  "hard_block": null,
  "tags": ["native-filament","external-novelty","independent-audit","prior-art","provenance-clean","coupled-selection"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "NFNOV2",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-NATIVE-FILAMENT-COUPLED-SELECTION-EXTERNAL-NOVELTY-AUDIT",
  "successor_gate": {
    "new_information_gap": "The completed literature work is explicitly direct/nonblind because its auditor had already participated in PR #627. Its content is useful supporting evidence, but the original taskbook's provenance-clean independent novelty classification remains unclosed.",
    "why_parent_result_does_not_close_it": "The parent execution failed the independence wall by disclosed provenance and intentionally did not occupy the reserved independent-return role. Accepting its content cannot manufacture independent evidence retroactively.",
    "discriminating_outcomes": [
      "a clean external auditor independently finds direct theorem antecedents or immediate-corollary coverage",
      "a clean external auditor independently classifies only known components or partial overlap requiring narrower publication wording",
      "a clean external auditor finds no direct theorem-statement match after reproducible serious search, without converting absence into a novelty claim"
    ],
    "kill_condition": "If the executor has read PR #627, the source generalization branch, the direct nonblind audit, or its detailed Driver review before freezing the return, independence is contaminated; stop and return PROVENANCE_CONTAMINATED rather than relabeling the work independent.",
    "alternative_route_or_free_exploration_considered": "No new mathematics is needed. Further theorem proving or formalization cannot resolve historical/prior-art provenance. A clean literature re-execution is the narrowest route that can close the remaining hard target.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The original task has a durable nonblind supporting output but no valid independent return. A separately identified clean re-execution preserves that evidence while preventing provenance laundering and gives the scheduler a falsifiable remaining objective."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Native Filament Coupled Selection — Provenance-Clean External Novelty Re-execution

Status: `READY / DRIVER_APPROVED / CLEAN EXTERNAL LITERATURE AUDIT / NO NEW MATHEMATICS`

Task-ID:

`RS-NATIVE-FILAMENT-COUPLED-SELECTION-EXTERNAL-NOVELTY-INDEPENDENT-REEXECUTION`

Owner branch:

`audit/native-filament-coupled-selection-independent-novelty-reexecution-20260825`

Hard target:

`NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_INDEPENDENTLY_CLASSIFIED_WITH_PROVENANCE_CLEAN`

## 0. Frozen input

Read only the statement packet before the return freezes:

`audit/native-filament-coupled-selection-literature-20260825:research_inputs/NATIVE_FILAMENT_COUPLED_SELECTION_V2_LITERATURE_AUDIT_PACKET_20260825.md#blob=2199c2bd34b44361570a4b68d85dcece70d6fba4`

The mathematical statement strength has already passed blind audit with the C1/D1/D2 narrowings. This task does not re-prove the package except as needed to map hypotheses and conclusions to literature.

## 1. Independence wall

Before freezing the return, do **not** read:

- PR #627;
- branch `research/native-filament-generalization-theorem-package-20260824`;
- source proofs or package-specific checkers from that branch;
- `research_returns/NATIVE_FILAMENT_COUPLED_SELECTION_DIRECT_NONBLIND_LITERATURE_AUDIT_20260825.md`;
- detailed conclusions of `driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_AUDIT_DRIVER_REVIEW_20260825.md` beyond the fact that a nonblind execution failed the independence requirement.

The #631 blind mathematical audit may be used only to know that the supplied V2 statements are the corrected mathematical targets. It is not novelty evidence.

Generate a fresh runtime Researcher-ID on claim. Do not reuse the source researcher or any identity that has read #627/source novelty discussion.

## 2. Required classification

For each S1-S8 and for the package as a whole, return exactly one:

- `KNOWN_DIRECT_THEOREM`;
- `KNOWN_IMMEDIATE_COROLLARY`;
- `KNOWN_COMPONENTS_ONLY`;
- `PARTIAL_OVERLAP_REQUIRES_NARROWING`;
- `NO_DIRECT_MATCH_FOUND`.

`NO_DIRECT_MATCH_FOUND != PROVEN_NOVEL`.

Do not use `NOVEL`, `FIRST`, `FIRST_KNOWN`, or equivalent historical-priority language.

## 3. Evidence standard

For each row:

1. search theorem statements, not project terminology alone;
2. identify strongest sources with author/title/year/source/DOI or stable identifier;
3. map hypotheses and conclusions precisely;
4. distinguish direct theorem, routine corollary, component overlap, and non-subsuming false positives;
5. record confidence and reproducible search terms/databases;
6. preserve negative results as search evidence, not priority proof.

At minimum cover integral/arithmetic arrangements, modular codes, RS/MDS, finite conics and tangent duality, order-2 cyclotomy, quadratic sequence coverings, CRT/profinite sieve products, arithmetic/deterministic percolation and geometry-selected arithmetic couplings.

## 4. Required return

Freeze:

`research_returns/NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_INDEPENDENT_REEXECUTION_RETURN_20260825.md`

The return must include:

- fresh Researcher-ID and independence attestation;
- S1-S8 theorem-level verdict matrix;
- package-level verdict;
- exact source mapping and search log;
- closest false positives;
- explicit novelty-language guard;
- final hard-target verdict.

After freeze, stop. Only a later Driver review may compare this return with the direct nonblind supporting audit.
