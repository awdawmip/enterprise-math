<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043C6-SINGLE-COMPONENT-ROOTED-SUCCESSOR-EXTENSION-RIGIDITY",
  "title": "R043-C6 Single-Component Rooted Successor-Extension Rigidity",
  "kind": "RESEARCH",
  "owner": "research/r043c6-single-component-rooted-successor-extension-rigidity",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Decide whether, after R043-C5 removes component-grouping ambiguity, the abstract weighted frontier slice of one connected unoccupied component together with a rooted action orbit uniquely determines the successor weighted frontier after deleting that action, or produce an exact harmful same-rooted-G0 collision.",
  "next_action": "Work only inside one connected unoccupied component Omega. Either prove a rooted successor-extension theorem from the current weighted frontier and rooted action orbit, or construct the smallest exact FCC/HCP pair with rooted weighted G0 isomorphism before the action and nonisomorphic successor frontier after the matched action. Avoid broad animal census and do not reopen component grouping.",
  "dependencies": [
    "research_returns/R043C2_G0_FUTURE_SUFFICIENCY_MODULO_SHIELDED_COMPONENTS_RETURN_20260824.md@a2aaaece1fcdea23f799b73728bb628b7d72bfa5",
    "research_result_records/RS-R043C5-OCTAHEDRAL-OPPOSITE-PAIR-GLOBAL-REALIZABILITY/RR-D4B443215DC78E8ACFF3.json@main",
    "driver_reviews/R043C5_OCTAHEDRAL_OPPOSITE_PAIR_GLOBAL_REALIZABILITY_DRIVER_REVIEW_20260827.md@main",
    "research_result_reviews/RR-D4B443215DC78E8ACFF3/DR-19F816CFB666F1FF7C00.json@main"
  ],
  "source_refs": [
    "research_returns/R043C2_G0_FUTURE_SUFFICIENCY_MODULO_SHIELDED_COMPONENTS_RETURN_20260824.md@a2aaaece1fcdea23f799b73728bb628b7d72bfa5",
    "research_returns/R043C5_OCTAHEDRAL_OPPOSITE_PAIR_GLOBAL_REALIZABILITY_RETURN_20260826.md@main"
  ],
  "evidence_status": "R043C2_COMPONENT_FACTORIZATION_PROVED / R043C5_COMPONENT_GROUPING_AMBIGUITY_REMOVED / SINGLE_COMPONENT_ROOTED_EXTENSION_IS_SOLE_REMAINING_STATIONARY_G0_GATE",
  "last_progress_ref": "R043-C5 accepted global frontier connectivity in FCC/HCP, eliminating the component-grouping branch of R043-C2 and leaving only the single-component rooted successor-extension ambiguity.",
  "last_progress_at": "2026-08-27T08:40:00+00:00",
  "hard_block": null,
  "tags": ["R043C6","G0","rooted-successor","future-sufficiency","FCC","HCP","single-component","rigidity","counterexample"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R043C6-SINGLE-COMPONENT-ROOTED-SUCCESSOR-EXTENSION-RIGIDITY",
  "parent_objective_id": "OBJ-R043-G0-STATIONARY-FUTURE-SUFFICIENCY-CLOSURE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R043C6",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-R043C5-OCTAHEDRAL-OPPOSITE-PAIR-GLOBAL-REALIZABILITY",
  "successor_gate": {
    "new_information_gap": "R043-C2 proved asynchronous factorization over current unoccupied components and isolated two possible harmful mechanisms. R043-C5 then proved every frontier slice F(C) intersect Omega is connected in FCC/HCP, eliminating component-grouping ambiguity. The sole remaining mechanism is whether one connected component's current rooted weighted frontier determines its successor extension.",
    "why_parent_result_does_not_close_it": "C5 proves connectivity of the visible frontier but does not prove that deeper hidden cells of one connected Omega are reconstructible from the current weighted frontier, nor that matched rooted frontier states have matched successors after deleting the action vertex.",
    "discriminating_outcomes": [
      "A global rooted successor-extension rigidity theorem in FCC and HCP.",
      "An exact harmful same-rooted-G0 one-step collision in FCC.",
      "An exact harmful same-rooted-G0 one-step collision in HCP.",
      "A mixed FCC/HCP classification.",
      "A strictly smaller exact hidden-extension invariant required beyond current weighted G0."
    ],
    "kill_condition": "Any exact globally realizable rooted pair with isomorphic current weighted frontier/action orbit but nonisomorphic successor weighted frontier kills one-step rooted sufficiency. Conversely, bounded search without a structural certificate cannot prove rigidity. Component-grouping counterexamples are out of scope because C5 has closed that mechanism.",
    "alternative_route_or_free_exploration_considered": "Preferred routes are rooted graph reconstruction, native link/interface constraints, deletion-locality, finite extension certificates and targeted SAT/graph-isomorphism search over one Omega. Generic larger-N connected-animal enumeration is lower value and must not become the main route.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "C5 reached a terminal global-connectivity theorem and removed one entire branch of the C2 obstruction tree. The remaining rooted-extension question has different witness and proof obligations, so a new task is cleaner than reopening the closed C5 pinch problem."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4","review_state":"PASS","temporary_overrides":[]}
}
-->

# R043-C6 — Single-Component Rooted Successor-Extension Rigidity

Status: `PUBLISHED_REGISTERED / DRIVER SUCCESSOR / CONTINUATION`

## Mother question

Work in the frozen FCC and HCP native 12-contact worlds. Let `C` be a finite connected occupied state, let `Omega` be one connected component of the unoccupied graph, and let

`F_Omega = F(C) intersect Omega`.

R043-C5 now guarantees that `F_Omega` is connected. Choose a rooted admissible action `x in F_Omega`.

Does the abstract weighted rooted state

`(G0[F_Omega], orbit(x))`

uniquely determine, up to weighted graph isomorphism, the successor frontier state produced by the addition `C -> C union {x}` inside that same `Omega`?

Equivalently: can two globally realizable single-component configurations have isomorphic current rooted weighted frontier states but different next weighted frontier states after matched actions?

A yes-to-uniqueness theorem closes the remaining one-step stationary `G0` obstruction. One exact harmful rooted collision refutes it.

## Frozen inputs and scope

Consume R043-C2 and R043-C5 exactly at their accepted boundaries.

R043-C2 proved that addition-only dynamics factorizes asynchronously over connected components of the current unoccupied graph. Distinct current components never merge under future additions, and relative placement between distinct components is future-irrelevant once their own rooted transition systems are fixed.

R043-C2 isolated two possible remaining defects: component-grouping ambiguity and single-component rooted-extension ambiguity.

R043-C5 subsequently proved, for every finite connected occupied `C` and every unoccupied component `Omega` in FCC/HCP, that `F(C) intersect Omega` is native-12-contact connected. Therefore the component-grouping ambiguity branch is closed and must not be reopened here.

The only target is the single-component rooted extension. Preserve the current weighted `G0` semantics exactly. Do not strengthen the observable by silently adding deeper `Omega` data, native embedding coordinates, or future labels unless the task concludes that such an extra invariant is mathematically necessary.

FCC and HCP are separate obligations. Native adjacency must be exact frozen 12-contact adjacency; Euclidean-distance surrogate adjacency is forbidden.

Finite computation is permitted only when it produces an exact rooted collision certificate, an exhaustive theorem-discriminating local extension classification, or a sharply smaller invariant. Broad size-only animal census is not proof.

## Hard target and required outputs

Hard target:

`R043C6_SINGLE_COMPONENT_ROOTED_SUCCESSOR_EXTENSION_RIGIDITY_DECIDED`

Required outputs:

1. A precise definition of the rooted current observable and its matched action orbit.
2. A precise successor observable after adding/deleting the rooted frontier vertex.
3. Either a global proof that every matched rooted current state has a uniquely determined successor in FCC/HCP, or an exact finite globally realizable harmful collision certificate.
4. FCC and HCP dispositions separately.
5. If negative, the smallest exact extra hidden-extension datum needed to separate the witness, without automatically promoting it to a new canonical state.
6. If positive at one step, an explicit audit of whether induction gives all-finite-horizon future sufficiency or whether a later-horizon recoalescence obstruction remains.
7. A deterministic checker for every finite witness or finite local classification used.
8. No Foundation promotion and no unrelated R043 stage opening inside the return.
9. Durable return at `research_returns/R043C6_SINGLE_COMPONENT_ROOTED_SUCCESSOR_EXTENSION_RIGIDITY_RETURN_20260827.md`.

## Research value to preserve

The R043 program has now removed two large classes of false counterexamples: relocation of distinct shielded/unoccupied components is future-safe, and disconnected visible frontier pieces cannot occur inside one connected `Omega` in the frozen FCC/HCP worlds. This leaves one sharply defined information-loss question rather than raw native-state reconstruction.

A positive C6 theorem would show that the current rooted weighted frontier already contains the one-step extension data needed by the stationary Boolean future. A negative witness would identify the first genuinely future-relevant hidden datum missing from `G0`. Either outcome directly advances the mother question and is more discriminating than a larger generic census.

## Success, kill, and return criteria

Freeze the strongest exact classification supported by the evidence:

- `ROOTED_SUCCESSOR_EXTENSION_RIGIDITY_PROVED_FCC_AND_HCP`;
- `ROOTED_SUCCESSOR_EXTENSION_RIGIDITY_PROVED_FCC_ONLY`;
- `ROOTED_SUCCESSOR_EXTENSION_RIGIDITY_PROVED_HCP_ONLY`;
- `HARMFUL_ROOTED_G0_COLLISION_CERTIFIED_FCC_AND_HCP`;
- `HARMFUL_ROOTED_G0_COLLISION_CERTIFIED_FCC_ONLY`;
- `HARMFUL_ROOTED_G0_COLLISION_CERTIFIED_HCP_ONLY`;
- `MIXED_ROOTED_EXTENSION_CLASSIFICATION`;
- `REDUCED_TO_STRICTLY_SMALLER_HIDDEN_EXTENSION_INVARIANT`.

Any negative claim requires exact current rooted weighted-graph isomorphism, exact matched-action compatibility, globally realizable connected occupied states, a single connected `Omega` on each side, and exact nonisomorphism of the successor weighted frontier.

Any positive claim requires a structural proof; finite search cannot establish global rigidity.

If one-step rigidity is proved, explicitly test whether the theorem composes inductively to all finite horizons. Do not silently equate one-step determinism with all-horizon stationarity without proving closure under successors.

Stop after the strongest exact C6 result is frozen and hand it to Driver review. Do not reopen the already-closed component-grouping or octahedral-pinch questions.
