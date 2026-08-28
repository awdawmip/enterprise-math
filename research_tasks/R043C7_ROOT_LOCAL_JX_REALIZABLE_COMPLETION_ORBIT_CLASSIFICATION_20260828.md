<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043C7-ROOT-LOCAL-JX-REALIZABLE-COMPLETION-ORBIT-CLASSIFICATION",
  "title": "R043-C7 Root-Local J_x Realizable Completion-Orbit Classification",
  "kind": "RESEARCH",
  "owner": "research/r043c7-root-local-jx-realizable-completion-orbits",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Classify the globally realizable root-local J_x completion orbits compatible with a fixed rooted weighted G0 in frozen FCC and HCP, and decide whether all completions are successor-equivalent or an exact harmful collision exists.",
  "next_action": "Use the C6 theorem ROOTED G0 + J_x -> successor as frozen input. Parameterize only the at-most-eleven newly exposed vertices and their root-local incidences, impose exact FCC/HCP realizability, and prove orbit uniqueness or return the smallest exact harmful pair. Do not resume broad occupied-animal census.",
  "dependencies": [
    "driver_reviews/R043C6_SINGLE_COMPONENT_ROOTED_SUCCESSOR_EXTENSION_RIGIDITY_DRIVER_REVIEW_20260828.md@main",
    "research_result_records/RS-R043C6-SINGLE-COMPONENT-ROOTED-SUCCESSOR-EXTENSION-RIGIDITY/RR-8D9FB5AF4B6388F62765.json@main",
    "research_returns/R043C6_SINGLE_COMPONENT_ROOTED_SUCCESSOR_EXTENSION_RIGIDITY_RETURN_20260827.md@main",
    "driver_reviews/R043C5_OCTAHEDRAL_OPPOSITE_PAIR_GLOBAL_REALIZABILITY_DRIVER_REVIEW_20260827.md@main"
  ],
  "source_refs": [
    "research_artifacts/R043C6_rooted_successor/RESULTS.json@main",
    "scripts/check_r043c6_rooted_successor.py@main"
  ],
  "evidence_status": "C6_EXACT_REDUCTION_ACCEPTED / ROOTED_G0_PLUS_JX_ONE_STEP_SUCCESSOR_PROVED / REALIZABLE_JX_ORBIT_GATE_OPEN",
  "last_progress_ref": "RR-8D9FB5AF4B6388F62765",
  "last_progress_at": "2026-08-28T04:50:00+00:00",
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "DRIVER_AUTO_FOLLOWUP",
    "R043C7",
    "FCC",
    "HCP",
    "rooted-G0",
    "local-completion",
    "orbit-classification",
    "harmful-collision"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R043C7-ROOT-LOCAL-JX-REALIZABLE-COMPLETION-ORBIT-CLASSIFICATION",
  "parent_objective_id": "OBJ-R043-G0-STATIONARY-FUTURE-SUFFICIENCY-CLOSURE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R043C7",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-R043C6-SINGLE-COMPONENT-ROOTED-SUCCESSOR-EXTENSION-RIGIDITY",
  "successor_gate": {
    "new_information_gap": "C6 proves that one-step successor uncertainty is exactly the realizable root-local J_x completion orbit, but it neither proves uniqueness of that orbit nor constructs a harmful pair.",
    "why_parent_result_does_not_close_it": "The exact reconstruction theorem is conditional on J_x. The root-star regression covers only a strict finite subfamily and cannot decide every globally realizable root-local completion.",
    "discriminating_outcomes": [
      "Prove all globally realizable J_x completions for every reachable rooted weighted G0 are successor-equivalent in FCC and HCP.",
      "Construct an exact FCC harmful completion pair with the same rooted weighted G0 and nonisomorphic successors.",
      "Construct an exact HCP harmful completion pair with the same rooted weighted G0 and nonisomorphic successors.",
      "Reduce realizable completion uniqueness to a strictly smaller finite link or extension invariant with an exact certificate."
    ],
    "kill_condition": "Any exact harmful pair closes one-step raw-G0 sufficiency negatively in that world. Generic radius expansion, broad animal enumeration, Euclidean surrogate adjacency, or reopening C3-C5 component grouping is non-closing.",
    "alternative_route_or_free_exploration_considered": "A broad new G0 sufficiency search, direct all-horizon induction, and unrestricted lattice-animal exploration were considered. The bounded J_x completion orbit is the only unresolved one-step datum and is strictly more discriminating.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "C6 is terminal at exact-reduction scope. C7 has a different finite-realizability interface and a decisive uniqueness-versus-collision outcome, so continuing inside C6 would conflate reconstruction with completion classification."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R043-C7 Root-Local J_x Realizable Completion-Orbit Classification

Status: `PUBLISHED_REGISTERED / CONTINUATION / BOUNDED COMPLETION GATE`

## Mother question

For each frozen FCC/HCP world, fix a reachable rooted weighted frontier state `[G,x]`. Among all globally realizable root-local profiles `J_x` compatible with that same state, are the resulting one-step successor weighted graphs always isomorphic, or does a harmful collision exist?

## Frozen inputs and scope

Use the accepted C6 theorem:

`ROOTED G0 + J_x -> EXACT ONE-STEP SUCCESSOR`.

The profile `J_x` contains only the newly exposed set `Z_x`, its internal native-contact edges, and incidences to the surviving old frontier. Its new side satisfies

`|Z_x| = 12 - w_G0(x) - deg_G0(x) <= 11`.

FCC and HCP are separate obligations. Use exact frozen native 12-contact incidence. Do not infer global uniqueness from the existing root-star census.

## Hard target and required outputs

Hard target:

`R043C7_REALIZABLE_JX_COMPLETION_ORBITS_CLASSIFIED_UNIQUE_OR_HARMFUL_COLLISION`.

Required outputs:

1. an exact realizability definition for a J_x completion over a rooted weighted G0;
2. a complete uniqueness theorem, exact harmful pair, or strictly smaller exact invariant;
3. FCC and HCP dispositions separately;
4. exact successor weighted-graph comparison modulo rooted-current automorphisms;
5. a theorem-discriminating finite certificate or a global structural proof;
6. explicit consequence for one-step and finite-horizon stationary G0 sufficiency;
7. a deterministic checker for every finite certificate;
8. a durable return with no broad census substitution.

## Research value to preserve

C6 has removed every deep hidden-geometric degree of freedom from the one-step update. Resolving the remaining bounded completion orbit either proves stationary one-step sufficiency or identifies the first exact future-relevant datum missing from raw G0.

The at-most-eleven-vertex new side makes this a finite local-completion problem even when the old frontier is large. That compression must be preserved.

## Success, kill, and return criteria

Success is a uniform completion-orbit uniqueness theorem for both worlds, or an exact harmful collision with full realizability and successor verification. A mixed FCC/HCP classification is admissible.

Any exact harmful collision immediately refutes raw one-step G0 sufficiency in that world. A finite search result is theorem-grade only when its parameterization is proved complete for the realizability class it claims.

Kill routes based mainly on expanding radius, enumerating generic animals, replacing native adjacency by Euclidean distance, or revisiting already-closed component grouping and octahedral pinch questions.
