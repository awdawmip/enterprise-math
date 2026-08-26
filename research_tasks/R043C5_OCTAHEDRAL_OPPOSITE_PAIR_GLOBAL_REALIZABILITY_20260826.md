<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043C5-OCTAHEDRAL-OPPOSITE-PAIR-GLOBAL-REALIZABILITY",
  "title": "R043-C5 Octahedral Opposite-Pair Global Realizability",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Decide whether the unique R043-C4 local obstruction—the octahedral opposite-pair point pinch—can be realized by a finite connected occupied set so that two local frontier sides remain in one connected unoccupied component while every native frontier repair between them is blocked.",
  "next_action": "Work only around the certified opposite-pair pinch. Either construct an exact finite FCC/HCP occupied-set certificate whose same unoccupied component has disconnected native frontier pieces, or prove that same-component connectivity necessarily forces a native frontier repair. Prefer separator/cut/dual-surface reasoning or a theorem-discriminating finite certificate; do not resume broad animal census.",
  "dependencies": [
    "research_returns/R043C4_NATIVE_INTERFACE_LINK_SEPARATOR_CLOSURE_RETURN_20260826.md@6b14cd76fa41209b83712d68a7a0050caccd6721",
    "research_result_records/RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE/RR-402C8F4C1B5DFDCB3BCF.json@6d0c2c0ee5c9785c5052a464715b9a3fbd117e46",
    "driver_reviews/R043C4_NATIVE_INTERFACE_LINK_SEPARATOR_CLOSURE_DRIVER_REVIEW_20260826.md@6d0c2c0ee5c9785c5052a464715b9a3fbd117e46",
    "research_returns/R043C3_UNOCCUPIED_COMPONENT_FRONTIER_CONNECTIVITY_RETURN_20260824.md@49877b834c4f15e7f30cb54f03ba5f106dba0342"
  ],
  "source_refs": [
    "research_artifacts/R043C4_link_separator/RESULTS.json@6b14cd76fa41209b83712d68a7a0050caccd6721",
    "research_artifacts/R043C4_link_separator/one_shell_pressure.py@6b14cd76fa41209b83712d68a7a0050caccd6721",
    "scripts/check_r043c4_native_interface_link_separator.py@6b14cd76fa41209b83712d68a7a0050caccd6721",
    "research_result_reviews/RR-402C8F4C1B5DFDCB3BCF/DR-32985388D8EA8EFC60FE.json@6d0c2c0ee5c9785c5052a464715b9a3fbd117e46"
  ],
  "evidence_status": "DRIVER_ACCEPTED_UNIQUE_THEOREM_CRITICAL_RESIDUE_FROM_R043C4",
  "last_progress_ref": "DR-32985388D8EA8EFC60FE accepted the unique octahedral opposite-pair local separator and froze global realizability as the sole remaining R043-C3 grouping obstruction",
  "last_progress_at": "2026-08-26T17:25:00+08:00",
  "hard_block": null,
  "tags": [
    "R043C5",
    "FCC",
    "HCP",
    "octahedron",
    "opposite-pair",
    "point-pinch",
    "frontier-connectivity",
    "global-realizability",
    "separator",
    "G0"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R043C5-OCTAHEDRAL-OPPOSITE-PAIR-GLOBAL-REALIZABILITY",
  "parent_objective_id": "OBJ-R043-G0-STATIONARY-FUTURE-SUFFICIENCY-CLOSURE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R043C5",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE",
  "successor_gate": {
    "new_information_gap": "R043-C4 independently certified that the only bad local Delaunay-cell colouring is the octahedral opposite-pair point pinch, but the minimal pinch repairs externally and all 12,951 targeted one-shell extensions per lattice remain frontier-connected. The exact remaining question is whether a finite connected occupied set can kill every frontier repair while preserving a deeper same-component unoccupied connection.",
    "why_parent_result_does_not_close_it": "C4 disproved the proposed pointwise local lift but did not construct a global R043-C3 counterexample and did not prove that every local pinch must repair globally. Its one-shell pressure is bounded regression evidence only.",
    "discriminating_outcomes": [
      "a certified finite FCC global pinch counterexample",
      "a certified finite HCP global pinch counterexample",
      "global pinch impossibility proved in FCC",
      "global pinch impossibility proved in HCP",
      "global pinch impossibility proved in both FCC and HCP, closing R043-C3 positively",
      "a strictly smaller exact native separator/barrier remainder with a finite certificate and no generic census inflation"
    ],
    "kill_condition": "Stop any route whose main progress is generic radius expansion, broad connected-animal enumeration, a continuum-only surface argument, Euclidean-distance surrogate adjacency, or reclassification of local Delaunay cells already closed by C4. Any computation must be targeted to the opposite-pair pinch and return an exact certificate or theorem-discriminating structural reduction.",
    "alternative_route_or_free_exploration_considered": "C4 already executed the complete local tetrahedral/octahedral classification, minimal FCC/HCP pinch construction, and the full 0..4 subset pressure over the fixed 24-site initial one-shell pool. Repeating or enlarging those searches is lower-value than deciding the global separator mechanism itself.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "C4 reached its authorized terminal classification and froze one unique global residue. C5 has different evidence requirements and decisive consequences: a finite certificate refutes global C3, while an impossibility theorem closes C3 and removes the remaining component-grouping ambiguity."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R043-C5 — Octahedral Opposite-Pair Global Realizability

Status: `PUBLISHED_REGISTERED / DRIVER SUCCESSOR / CONTINUATION`

## Frozen predecessor result

R043-C4 is accepted at exactly:

`LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`.

The local classification is frozen: tetrahedra have no bad nonconstant two-colouring; octahedra have exactly six bad nonconstant two-colourings, precisely the three opposite-vertex pairs and their complements. In each bad case the eight occupied–unoccupied cut incidences split `4+4`.

The unique local obstruction is therefore the **octahedral opposite-pair point pinch**. This kills the proposed automatic pointwise C3 local interface-to-frontier lift, but it does **not** refute the global R043-C3 theorem.

The minimal equator-4 realization repairs externally in both FCC and HCP. The C4 pressure result `0 / 12,951` in each lattice is frozen only as targeted regression evidence: it enumerates all subsets of size `0..4` from the fixed 24-site initial one-shell frontier pool. It is not a general animal census and may not be cited as evidence of global impossibility.

## Exact mother question

Work in each frozen FCC/HCP native 12-contact graph separately. Does there exist a finite connected occupied set `C` and an octahedral cell `Q` with opposite unoccupied vertices `u,v` and the other four vertices of `Q` occupied such that:

1. `u` and `v` lie in the same connected component `Omega` of the unoccupied graph;
2. `u,v` lie in the visible frontier `F(C) intersect Omega`;
3. the two local pinch sides are not connected inside `F(C) intersect Omega` under native 12-contact—in particular all external native-frontier repair paths joining the sides are blocked;
4. nevertheless a deeper unoccupied path in `Omega` joins the sides, so the loss of frontier connectivity is not caused by splitting `Omega` itself?

A certified example is a genuine global counterexample to the R043-C3 frontier-connectivity statement. A proof that such an example is impossible shows that the unique local pinch is always globally repairable and therefore closes R043-C3 positively.

## Hard target

`R043C5_OCTAHEDRAL_OPPOSITE_PAIR_GLOBAL_REALIZABILITY_DECIDED`.

FCC and HCP are separate obligations. Mixed outcomes are allowed and must be stated explicitly.

## Required outputs

1. exact formal definition of the pinch, frontier-side separation, and same-component condition in each frozen native graph;
2. either a finite occupied-set counterexample certificate with exact adjacency/component verification, or a proof that every attempted pinch with same-component connectivity forces a native frontier repair;
3. FCC disposition and HCP disposition separately;
4. exact consequence for R043-C3 and for the R043-C2/G0 component-grouping ambiguity;
5. a small independent checker for every finite certificate used in the argument;
6. explicit regression against the C4 minimal pinch and the frozen `12,951` one-shell pressure result;
7. weakest remaining obstruction only if the hard target cannot be fully decided;
8. durable return `research_returns/R043C5_OCTAHEDRAL_OPPOSITE_PAIR_GLOBAL_REALIZABILITY_RETURN_20260826.md` plus task-local certificates/checkers.

## Preferred proof routes

The preferred positive-counterexample route is a structurally targeted barrier construction: start from the opposite-pair pinch, characterize the set of frontier repairs that must be blocked, and produce the smallest exact native shell/wall that blocks those repairs while leaving a deeper unoccupied tunnel in the same `Omega`.

The preferred impossibility route is a native separator theorem: prove that any occupied barrier separating the two pinch sides in the frontier necessarily also separates them in the whole unoccupied graph, or that any deeper same-component path can be pushed/rerouted to an unoccupied frontier path. Cell-star, cut-set, dual-surface, or minimal-path arguments are admissible only when every step is translated back to exact FCC/HCP 12-contact incidence.

Targeted computation is permitted when it certifies one of those structures. It must parameterize a theorem-relevant barrier/separator family or output a finite exact witness; it may not become generic animal census by incremental radius growth.

## Terminal classifications

Use the strongest exact classification supported by the evidence, including mixed FCC/HCP cases:

- `GLOBAL_OPPOSITE_PAIR_PINCH_COUNTEREXAMPLE_CERTIFIED_FCC_AND_HCP`;
- `GLOBAL_OPPOSITE_PAIR_PINCH_COUNTEREXAMPLE_CERTIFIED_FCC_ONLY`;
- `GLOBAL_OPPOSITE_PAIR_PINCH_COUNTEREXAMPLE_CERTIFIED_HCP_ONLY`;
- `GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_FCC_AND_HCP`;
- `GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_FCC_ONLY`;
- `GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_HCP_ONLY`;
- `MIXED_GLOBAL_REALIZABILITY_CLASSIFIED`;
- `OPEN_WITH_STRICTLY_SMALLER_NATIVE_SEPARATOR_REMAINDER`.

Any counterexample claim requires a finite exact certificate verifying connectedness of `C`, same-component membership of the two sides in `Omega`, and disconnection of `F(C) intersect Omega`. Any impossibility claim requires a global argument and cannot be inferred from bounded search.

## Kill conditions and strength boundary

Do not reopen the closed tetrahedral/octahedral local-colouring classification. Do not enlarge generic FCC/HCP animal census. Do not replace native contact by Euclidean threshold adjacency. Do not infer a theorem from absence of examples in a bounded search.

Until a finite global witness is certified, R043-C3 remains **OPEN, not refuted**. Until a global impossibility theorem is proved in a lattice, C3 is **not positively closed** there. R043-C2 component factorization remains frozen and unchanged.

No Foundation promotion is authorized automatically. Stop after the exact C5 return is frozen and hand the result back to Driver review.
