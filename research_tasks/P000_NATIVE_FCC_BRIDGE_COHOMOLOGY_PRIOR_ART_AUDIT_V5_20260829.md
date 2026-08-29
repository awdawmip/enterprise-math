<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT",
  "title": "P000 native/FCC signed-K4 上同调、S4 提升与双覆盖外部先例审计 V5",
  "kind": "RESEARCH",
  "owner": "research/p000-6d-rotation-prior-art-audit",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Perform claim-by-claim external duplication analysis for the accepted signed-K4 chart transition system and the Gen6 cohomological S4 lifting problem, with special attention to signed graph switching/antibalance, two-graph cohomological automorphism lifting, discrete Z2 holonomy, Schur/double covers of S4, binary octahedral comparison, and projective/groupoid lifts.",
  "next_action": "Verify the seeded authoritative sources, expand literature search around Cameron two-graph cohomology and signed switching classes, identify exact theorem statements controlling S4-invariant representatives and double-cover lifts, compare all relevant C2 extensions of S4, and map each result to the exact P000 internal claim without treating absence as novelty.",
  "dependencies": [
    "research_notes/P000_FCC_S4_Z2_PRIOR_ART_SYNTHESIS_20260829.md@main",
    "research_tasks/P000_NATIVE_MIXED_STAR_COHOMOLOGY_LIFT_V6_20260829.md@main",
    "research_returns/P000_L1_NATIVE_FCC_CARRIER_BRIDGE_V2_RETURN_20260829.md@main"
  ],
  "evidence_status": "SEEDED_EXTERNAL_SEARCH_COMPLETE / FORMAL_CLAIM_BY_CLAIM_AUDIT_OPEN",
  "hard_block": null,
  "tags": ["prior-art","signed-graph","switching","two-graph","cohomology","S4","Schur-cover","binary-octahedral","Z2-holonomy","P000"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P0006DPA5",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "successor_gate": {
    "new_information_gap": "A bounded Driver search has already found strong prior art showing that most carrier/signed-graph ingredients are classical, but the exact overlap with the P000 native lifting claim has not yet been formally audited theorem-by-theorem. Gen5 must resolve that boundary and especially determine whether Cameron/two-graph cohomological lifting results already subsume the carrier-level obstruction/lift problem.",
    "why_parent_result_does_not_close_it": "The Driver synthesis is a seed and no-novelty guard, not a complete literature audit or novelty determination.",
    "discriminating_outcomes": ["exact duplicate of carrier theorem", "partial antecedent with precise missing P000-native constraint", "known extension/cohomology theorem fully solves carrier lift only", "no exact match after documented search with novelty still undecided"],
    "kill_condition": "A bibliography dump, search-result list, or statement that P000-specific vocabulary has no hits is nonresponsive. Every source must map to an exact internal claim and theorem strength.",
    "alternative_route_or_free_exploration_considered": "Searching only cuboctahedron/FCC terminology is insufficient because the closest theory lives under signed graphs, switching classes, two-graphs, group cohomology, discrete connections, and central extensions.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Generation 5 replaces the broad holonomy audit with a seeded, source-specific cohomological audit aligned to the new Gen6 mathematical task."
  }
}
-->

# P000 native/FCC signed-K4 上同调、S4 提升与双覆盖外部先例审计 V5

Status: `READY / GENERATION-5 / P1 / PRIOR-ART / SEEDED / P000-BOUND`

## Hard target

`P000_NATIVE_FCC_S4_COHOMOLOGY_EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED`

## Seeded sources that MUST be checked

1. Peter J. Cameron, `Automorphisms and cohomology of switching classes`, JCTB 22 (1977), 297–298.
2. Peter J. Cameron, `Cohomological aspects of two-graphs`, Math. Z. 157 (1977), 101–119.
3. Peter J. Cameron & A. L. Wells Jr., `Signatures and signed switching classes`, JCTB 40 (1986), 344–361.
4. Frank Harary / Thomas Zaslavsky signed-graph balance, antibalance, switching and negative-cycle theory.
5. Solé & Zaslavsky, `A Coding Approach to Signed Graphs`, SIAM J. Discrete Math. 7 (1994), 544–553.
6. discrete signature / magnetic Laplacian literature for cycle holonomy and switching invariance.
7. discrete principal-bundle connection literature for cochain/holonomy formulation.
8. octahedral/cuboctahedral proper rotation `S4` references.
9. Johnson graph / line graph `L(K4)=J(4,2)` literature, including distinction between physical proper rotations and full graph automorphisms.
10. group-theory sources on `S4` central/double/Schur covers, including binary octahedral and `GL(2,3)` comparison.
11. Rubik-group literature for commutator/conjugation methods.

## Required claim map

For each source, classify at least these internal claims:

- `O_FCC ~= S4`;
- faithful six-edge `S4` carrier action;
- star/complement obstruction;
- signed-K4 transition signature;
- all triangle holonomy `-1` / antibalance;
- no global signed section / switching trivialization;
- full `S4` stability of switching class;
- existence/nonexistence of invariant representative;
- group-cohomological obstruction to lift;
- canonical/double-cover lift;
- split versus non-split `C2` extension;
- binary octahedral or other `2.S4` comparison;
- P000 mixed native slice geometry;
- P000 state-level legal automorphism preserving native Cell relations;
- operation-safe prohibition on quotienting native states by carrier fibers.

Every row must be labeled:

`EXACT_DUPLICATE / PARTIAL_ANTECEDENT / ADJACENT_METHOD / NO_MATERIAL_MATCH`.

## Special question

Determine whether the accepted chart-sign class on `K4` is simply the classical antibalanced switching class, and whether Cameron's cohomological lifting framework already gives an exact carrier-level criterion for lifting the `S4` action to a double cover.

If yes, state exactly what remains after importing that theorem: the likely surviving frontier is only the **P000 native Cell realization** of mixed slices and legal state transformations.

## Novelty guard

`NO_MATERIAL_MATCH != NOVELTY`.

No claim of originality is authorized by this task. It only classifies the external boundary.
