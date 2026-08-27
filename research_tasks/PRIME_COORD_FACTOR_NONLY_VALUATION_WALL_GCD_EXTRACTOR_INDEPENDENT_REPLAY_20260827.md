<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY",
  "title": "Prime Coordinate N-only Valuation-Wall GCD Extractor Independent Replay",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Independently determine whether the explicit N-only factorial valuation-wall construction yields a deterministic nontrivial gcd for every distinct odd semiprime, or isolate the exact counterexample/failure boundary.",
  "next_action": "Reconstruct the factorial-valuation wall from N alone, prove or refute the first dyadic nonunit and synchronization alternatives, then settle the sqrt(N)/3 two-seed fallback with an independent exact-integer implementation before any source comparison.",
  "dependencies": [
    "research_result_records/RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE/RR-A33E88150B0DAD0B13B8.json@687a217f283f41d898a42d1951ffcd7f63a1b7ce"
  ],
  "source_refs": [
    "research_tasks/PRIME_COORD_FACTOR_BLIND_PADIC_GCD_BRIDGE_READY_AFTER_PCF1_20260827.md@1b7c1988d59492f709e4afc0755a3c1300289cf1",
    "research_result_records/RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE/RR-A33E88150B0DAD0B13B8.json@687a217f283f41d898a42d1951ffcd7f63a1b7ce"
  ],
  "evidence_status": "PCF4_FIXED_PUBLIC_PREFIX_NO_GO_ACCEPTED / N_DEPENDENT_OBSERVABLE_REMAINS_OPEN / SUPPLEMENTAL_DUPLICATE_EXECUTION_WITHHELD_UNTIL_PHASE_B",
  "last_progress_ref": "RR-A33E88150B0DAD0B13B8 accepted with fixed-public-prefix scope; a non-authoritative duplicate execution exposed a stronger N-dependent valuation-wall candidate that requires clean replay.",
  "last_progress_at": "2026-08-27T11:06:00+00:00",
  "hard_block": null,
  "tags": ["prime-coordinate", "factorization", "n-only", "valuation-wall", "gcd-extraction", "independent-replay"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF4R",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE",
  "successor_gate": {
    "new_information_gap": "The accepted parent no-go covers fixed finite public-prefix probes only; genuinely N-dependent observables remain unresolved.",
    "why_parent_result_does_not_close_it": "The parent theorem has no claim about seed schedules or observable support growing with N.",
    "discriminating_outcomes": "Prove the N-only splitter for all distinct odd semiprimes, prove it on a sharp subfamily, or exhibit an exact counterexample/failure mechanism.",
    "kill_condition": "Kill the candidate if hidden factors enter the constructor, if the first-wall or synchronization implications fail, if both fallback seeds can be trivial on a valid distinct odd semiprime, or if the exact recurrence mismatches the factorial observable.",
    "alternative_route_or_free_exploration_considered": "The weak-prime-shadow/mod-p^3 route and unrestricted free exploration remain alternatives; the valuation-wall route is preferred because it is explicit, N-only and deterministic.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent generation is terminal for its fixed-prefix theorem, while the stronger candidate arose in a non-authoritative duplicate execution; clean independent replay prevents provenance laundering."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "program_id": "PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827",
  "requested_risk_tier": "CRITICAL"
}
-->

# Prime Coordinate N-only Valuation-Wall GCD Extractor Independent Replay

Status: `PUBLISHED_REGISTERED / READY / CLEAN_REPLAY_REQUIRED`

## Mother question

For a distinct odd semiprime `N=pq`, `3<p<q`, can the public factorial observable

`A_s=(2s)!(3s)!/(s!)^5`

be used with an N-only seed schedule and exact gcd tests to deterministically return a nontrivial factor without hidden-factor constructor inputs or prime scanning?

Reconstruct independently the candidate local law

`v_r(A_s)=floor(2s/r)+floor(3s/r)` for prime `r>3` and `0<=s<r`,

the first-dyadic valuation-wall alternative, and the proposed synchronized fallback `t=floor(sqrt(N)/3), t+1`.

## Frozen inputs and scope

Phase A is blind-forward. Before its freeze, use only this taskbook, accepted parent result `RR-A33E88150B0DAD0B13B8`, its admitted N-only input model, standard elementary number theory, and independently written exact-integer code. The candidate statement is a target, not accepted truth.

Withhold the originating duplicate execution's derivation, return, scripts and discussion until Phase A has frozen both a mathematical derivation and an independent checker. In Phase B compare against that preserved supplemental execution and perform current tool/method dedup.

Constructor-side code may receive only `N`, public constants and public seed indices. Hidden factors may appear only in proof-side reasoning or test oracles. Every division must be exact or justified. State complexity in bit length. A correct square-root-scale splitter is structurally valuable but is not a factoring-speedup theorem.

## Hard target and required outputs

Hard target: `N_ONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENTLY_RECONSTRUCTED_AND_VERIFIED_OR_NARROWED_OR_REFUTED`.

Required outputs:

1. proof or exact counterexample for the valuation formula;
2. proof or exact counterexample for the first-dyadic nonunit alternative;
3. exact synchronization implication with endpoint inequalities;
4. exact proof or counterexample for the two-seed fallback;
5. explicit public stopping rule with no hidden-factor query;
6. exact recurrence or equivalent constructor for `A_s mod N`, cross-checked against direct bounded evaluation;
7. independently authored checker and adversarial semiprime regression;
8. bit-complexity and memory analysis;
9. Phase-B comparison against withheld supplemental evidence and current-tool dedup;
10. durable return at `research_returns/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY_RETURN_20260827.md`.

## Research value to preserve

This tests the shortest concrete route around the accepted fixed-prefix no-go: allow observable support to grow with `N` while keeping the constructor factor-blind. Positive closure would give an explicit deterministic N-only asymmetry generator; negative closure would sharply extend the fixed-integer obstruction into N-dependent schedules.

## Success, kill, and return criteria

Freeze exactly one strongest verdict: `N_ONLY_GCD_EXTRACTOR_VERIFIED`, `RESTRICTED_N_ONLY_GCD_EXTRACTOR_VERIFIED`, `VALUATION_WALL_CANDIDATE_REFUTED`, `VALUATION_WALL_INTERFACE_NARROWED`, or `NO_PROGRESS_WITH_EXACT_BLOCKER`.

A positive verdict requires complete constructor admissibility plus synchronization/fallback proof. Bounded scans cannot prove the universal theorem. A negative verdict requires an exact counterexample or exact logical failure point. No Working Truth, Foundation mutation or new tool-family promotion follows from this task alone.
