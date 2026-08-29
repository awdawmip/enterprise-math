<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION",
  "title": "Native Filament — Post-audit Hyperbola/Joukowski Independent Replication",
  "kind": "RESEARCH",
  "owner": "audit/native-filament-postaudit-hyperbola-joukowski-replication-v2-20260825",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED",
  "next_action": "Using only the frozen statement-only post-audit packet, independently prove, narrow, or refute H1/H2/J1/J2/C1/C2, reconstruct the finite-field and boundary pressure checks with an independent checker, freeze exact theorem wording and counterexamples if any, and stop before reading PR #627 source proofs/checkers.",
  "dependencies": [
    "driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_DRIVER_REVIEW_20260825.md@d4e3f8eca68bff1d8803b8eb74402fc6d69e7b5f",
    "audit/native-filament-postaudit-hyperbola-joukowski-replication-20260825:research_inputs/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_BLIND_PACKET_20260825.md#blob=6ce9ea10f02fded1959c55a1b78044ada434360f"
  ],
  "source_refs": [
    "audit/native-filament-postaudit-hyperbola-joukowski-replication-20260825:research_inputs/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_BLIND_PACKET_20260825.md#blob=6ce9ea10f02fded1959c55a1b78044ada434360f",
    "driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_DRIVER_REVIEW_20260825.md@d4e3f8eca68bff1d8803b8eb74402fc6d69e7b5f",
    "legacy Driver-approved V6 reissue in audit/native-filament-postaudit-hyperbola-joukowski-replication-v2-20260825"
  ],
  "evidence_status": "IMMUTABLE_V2_MIGRATION_OF_OPEN_DRIVER_APPROVED_BLIND_REPLICATION",
  "last_progress_ref": "PR #637 packet/task surface without return",
  "last_progress_at": "2026-08-25T20:13:00+08:00",
  "hard_block": null,
  "tags": ["native-filament","hyperbola","Joukowski","independent-replication","post-audit","boundary-closure","C3"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION",
  "parent_objective_id": "RS-NATIVE-FILAMENT-COUPLED-SELECTION-INDEPENDENT-AUDIT",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "NFHJREP",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-NATIVE-FILAMENT-COUPLED-SELECTION-INDEPENDENT-AUDIT",
  "successor_gate": {
    "new_information_gap": "The earlier blind audit closed only the original V2 statement layer. H1/H2/J1/J2/C1/C2 were derived later and have no independent frozen return.",
    "why_parent_result_does_not_close_it": "A result on the earlier frozen statement universe cannot independently certify theorem rows that were absent from that universe.",
    "discriminating_outcomes": [
      "all H1/H2/J1/J2/C1/C2 claims survive exactly",
      "one or more claims require explicit field/prime/domain narrowing",
      "a concrete counterexample refutes a bridge, orbit count, saturation uniqueness, or boundary closure",
      "a dependency gap blocks one claimed closure"
    ],
    "kill_condition": "If PR #627, the source generalization branch, prohibited source proofs, or package-specific source checkers are read before the return freezes, stop and mark provenance contaminated.",
    "alternative_route_or_free_exploration_considered": "Direct source review could check internal consistency but would not supply independent blind evidence.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This registered migration preserves the earlier audit boundary while making the genuinely new theorem layer executable under the current immutable state machine."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:7ae52d1c45fefb96c7f127599c0dad100519ebc671c3c299b76174bd60760b26",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Native Filament — Post-audit Hyperbola/Joukowski Independent Replication

Status: `READY / PUBLISHED / CLAIMABLE / BLIND POST-AUDIT REPLICATION`

Hard target: `POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

## Mother question

Do the post-audit theorem rows H1/H2/J1/J2/C1/C2 in the frozen statement-only Native Filament packet hold at exactly their stated strength, or must any row be narrowed, refuted by a minimal counterexample, or marked as depending on an unproved premise?

## Frozen inputs and scope

The only theorem packet authorized before return freeze is `audit/native-filament-postaudit-hyperbola-joukowski-replication-20260825:research_inputs/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_BLIND_PACKET_20260825.md#blob=6ce9ea10f02fded1959c55a1b78044ada434360f`. The earlier independent audit may be used only for the fact that the original V2 base package passed with its stated narrowing; it does not prove H1/H2/J1/J2/C1/C2.

Before freezing the return, do not read PR #627, branch `research/native-filament-generalization-theorem-package-20260824`, any source file whose name contains `HYPERBOLA`, `JOUKOWSKI`, `BOUNDARY_CLOSURE`, or `357_ORBIT`, corresponding source checker scripts, or source-researcher proof opinions. If this wall is breached, return provenance-contaminated instead of claiming independence.

## Hard target and required outputs

Audit H1 split-hyperbola tangent/cover bridge, H2 finite-field sign-orbit quotient and breaker bound, J1 odd-sector central-lane Joukowski map, J2 extremal saturation uniqueness, C1 longitudinal/transverse boundary closure, and C2 C3 bouquet coherence. Assign each exactly one verdict: `VERIFIED_EXACT`, `VERIFIED_WITH_NARROWING`, `REFUTED_COUNTEREXAMPLE`, or `DEPENDENCY_GAP`.

Mandatory pressure tests are: symbolic H1 verification in characteristic not 2; H2 enumeration including q=5,7,13,53; direct Lambda_s image enumeration for odd s<=15 and primes q<=101; active J2 counterexample search for odd s<=101 whenever 2s-1 or 2s+1 is prime; independent C1 derivation; explicit separation of breaker-coprime capacity 9 from the unrelated native typed-Cell prime-incidence cap 9; and boundary checks q=2, divisors of B or s, slope collisions, small s, and nonprime extremal characteristics. Build an independent checker only from the frozen packet formulas. Finite testing may support but cannot replace universal proofs.

## Research value to preserve

This task supplies genuinely independent evidence for a theorem layer created after the earlier blind audit froze. Keeping the statement-only wall intact distinguishes reconstruction from source consistency checking, while exact narrowing or refutation prevents later Native Filament work from inheriting unsupported field, orbit, saturation, or closure strength.

## Success, kill, and return criteria

Success is a frozen return at `research_returns/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_RETURN_20260829.md` plus a fresh independent checker under `tools/` or `research_checks/`, containing the fresh Researcher-ID and independence attestation, row verdict matrix, independent derivations in dependency order, pressure-test log and checker provenance, minimal counterexamples/failure modes, exact final theorem wording after narrowing, and one final hard-target verdict. Kill the execution as provenance-contaminated if the independence wall is breached. Stop after the return and immutable task result are frozen for review; do not read source proofs/checkers or merge/promote automatically.
