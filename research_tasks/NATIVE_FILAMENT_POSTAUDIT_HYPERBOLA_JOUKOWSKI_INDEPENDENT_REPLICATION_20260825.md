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
  "next_action": "Using only the frozen statement-only post-audit packet, independently prove, narrow, or refute H1/H2/J1/J2/C1/C2, reconstruct the required finite-field and boundary pressure checks with an independent checker, freeze the exact theorem wording and counterexamples if any, and stop before reading PR #627 source proofs/checkers.",
  "dependencies": [
    "driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_DRIVER_REVIEW_20260825.md@d4e3f8eca68bff1d8803b8eb74402fc6d69e7b5f",
    "audit/native-filament-postaudit-hyperbola-joukowski-replication-20260825:research_inputs/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_BLIND_PACKET_20260825.md#blob=6ce9ea10f02fded1959c55a1b78044ada434360f"
  ],
  "source_refs": [
    "audit/native-filament-postaudit-hyperbola-joukowski-replication-20260825:research_inputs/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_BLIND_PACKET_20260825.md#blob=6ce9ea10f02fded1959c55a1b78044ada434360f",
    "driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_DRIVER_REVIEW_20260825.md@d4e3f8eca68bff1d8803b8eb74402fc6d69e7b5f",
    "PR #637 statement/task surface; no independent return exists at reissue time"
  ],
  "evidence_status": "POST_AUDIT_NEW_THEOREM_LAYER_NOT_COVERED_BY_631_INDEPENDENT_REPLICATION_OPEN",
  "last_progress_ref": "PR #637 packet/task surface without return",
  "last_progress_at": "2026-08-25T20:13:00+08:00",
  "hard_block": null,
  "tags": ["native-filament","hyperbola","Joukowski","independent-replication","post-audit","boundary-closure","C3"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "NFHJREP",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-NATIVE-FILAMENT-COUPLED-SELECTION-INDEPENDENT-AUDIT",
  "successor_gate": {
    "new_information_gap": "The #631 blind audit closed the original coupled-selection V2 statement layer only. The split-hyperbola, sign-orbit quotient, lane Joukowski, extremal saturation and longitudinal/transverse boundary-closure theorems were derived later and were not present in the #631 blind packet.",
    "why_parent_result_does_not_close_it": "A PASS_WITH_NARROWING on an earlier frozen statement universe cannot supply independent evidence for theorem rows that did not yet exist. Source-branch checkers and direct derivations are not substitutes for a fresh blind reconstruction.",
    "discriminating_outcomes": [
      "all post-audit H1/H2/J1/J2/C1/C2 claims survive exactly",
      "one or more claims survive only after explicit field/prime/domain narrowing",
      "a concrete counterexample refutes a claimed bridge, orbit count, saturation uniqueness or boundary closure",
      "a dependency gap shows that one claimed closure uses an unproved earlier fact"
    ],
    "kill_condition": "If the executor reads PR #627, the source generalization branch, HYPERBOLA/JOUKOWSKI/BOUNDARY_CLOSURE/357_ORBIT source proofs, or package-specific source checkers before freezing the return, stop and mark the execution provenance-contaminated rather than independent.",
    "alternative_route_or_free_exploration_considered": "The source branch already contains derivations and checkers, but reviewing those directly would only establish source consistency. A blind replication is required because these claims extend beyond the independently audited V2 universe.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Reopening #631 would violate its frozen statement boundary. This reissued current-policy task preserves the earlier audit as closed while isolating the genuinely new post-audit theorem layer."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Native Filament — Post-audit Hyperbola/Joukowski Independent Replication

Status: `READY / DRIVER_APPROVED / BLIND POST-AUDIT REPLICATION / NO SOURCE PROOFS`

Task-ID:

`RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION`

Owner branch:

`audit/native-filament-postaudit-hyperbola-joukowski-replication-v2-20260825`

Hard target:

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

## 0. Reissue provenance

An earlier researcher-issued task surface exists in Draft PR #637, but no independent return is present. This file is the current Driver-approved V6 reissue under the live taskbook policy. It preserves the same mathematical target and pins the existing statement-only packet byte-for-byte by Git blob.

Frozen input:

`audit/native-filament-postaudit-hyperbola-joukowski-replication-20260825:research_inputs/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_BLIND_PACKET_20260825.md#blob=6ce9ea10f02fded1959c55a1b78044ada434360f`

## 1. Independence wall

Before freezing the return, do **not** read:

- PR #627;
- branch `research/native-filament-generalization-theorem-package-20260824`;
- any source file whose name contains `HYPERBOLA`, `JOUKOWSKI`, `BOUNDARY_CLOSURE`, or `357_ORBIT`;
- corresponding source checker scripts;
- direct source-researcher opinions about proof correctness.

The earlier #631 audit may be used only for the fact that the original V2 base package was verified with C1/D1/D2 narrowing. It does not prove any post-audit claim.

Generate a fresh runtime Researcher-ID on claim. Do not reuse `EM-FREE-NEPS-239A6D` or an identity that authored/reviewed the withheld post-audit proofs.

## 2. Required theorem rows

Audit every packet group:

- `H1`: split-hyperbola tangent/cover bridge;
- `H2`: finite-field sign-orbit quotient and breaker bound;
- `J1`: odd-sector central-lane Joukowski map;
- `J2`: extremal saturation uniqueness;
- `C1`: longitudinal/transverse boundary closure;
- `C2`: C3 bouquet coherence.

For each row return exactly one:

- `VERIFIED_EXACT`;
- `VERIFIED_WITH_NARROWING`;
- `REFUTED_COUNTEREXAMPLE`;
- `DEPENDENCY_GAP`.

Finite testing supports proofs but cannot replace a universal proof.

## 3. Mandatory pressure tests

At minimum:

1. symbolic H1 verification in characteristic not 2;
2. H2 finite-field enumeration including `q=5,7,13,53`;
3. direct `Lambda_s` image enumeration for odd `s<=15`, primes through `q<=101`;
4. active J2 counterexample search for odd `s<=101` whenever `2s-1` or `2s+1` is prime;
5. independent C1 derivation without source closure proofs;
6. explicit scope guard that breaker-coprime capacity `9` is not the separate native typed-Cell prime-incidence cap `9`;
7. boundary checks for `q=2`, divisors of `B`/`s`, slope collisions, small `s`, and nonprime extremal characteristics.

Build an independent checker from the packet formulas; do not reuse source scripts.

## 4. Required return

Freeze:

`research_returns/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_RETURN_20260825.md`

Required contents:

- fresh Researcher-ID and independence attestation;
- H1/H2/J1/J2/C1/C2 verdict matrix;
- independent derivations in dependency order;
- finite pressure-test log and checker provenance;
- minimal counterexamples/failure modes if any;
- exact final theorem wording after narrowing;
- one final hard-target verdict.

After freeze, stop. Do not read source proofs/checkers or merge/promote automatically.
