<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE",
  "title": "GEO8 Borsuk R6 Lassak-33 compression pressure — current-policy revalidation Gen2",
  "kind": "RESEARCH",
  "owner": "research/geo8-borsuk-r6-lassak-33-compression-pressure",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Generation 1 produced RR-68BA014D54542DA7221C with an exact K33 whole-atom coarsening obstruction and a uniform 10/7 center-fixed cube-facet subtemplate obstruction, but the Gen1 task publication is nonoperational under the current V2 mandatory-body-section contract. Revalidate the exact same Euclidean hard target under a policy-complete publication and freeze zero mathematical drift unless current evidence forces a change.",
  "next_action": "Re-run the exact task-local checker, verify every RR-68BA output blob and source boundary against current main, audit whether any accepted or external source change since the frozen execution changes the theorem scope, then issue a fresh execution/result envelope bound to this Gen2 publication. Reuse the frozen mathematical artifacts byte-for-byte when still correct.",
  "dependencies": [
    "RR-440E83B6F8C06F0808D8",
    "DR-4C239DD3C0C251A78E45",
    "RR-68BA014D54542DA7221C"
  ],
  "source_refs": [
    "research_returns/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE_RETURN_20260902.md",
    "research_checks/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE_CHECK_20260902.py",
    "research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/lassak_r6_exact_obstruction_20260902.json",
    "research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/r4_to_r6_transfer_audit_20260902.json",
    "research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/source_manifest_20260902.json",
    "research_result_records/RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE/RR-68BA014D54542DA7221C.json"
  ],
  "evidence_status": "GEN1_MATHEMATICS_FROZEN / CURRENT_POLICY_REPUBLICATION_REQUIRED / ZERO_MATH_DRIFT_REVALIDATION_EXPECTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["GEO8", "Borsuk", "R6", "Lassak", "revalidation", "template-obstruction", "current-policy"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-BORSUK-R6-UPPER-BOUND-PRESSURE-20260902",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GEO8BORSUKR6",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-GEO7-BORSUK-6D-DIAMETER-PARTITION-NATIVE-BRIDGE",
  "successor_gate": {
    "new_information_gap": "The Euclidean constructive question is mathematically answered at restricted-template strength by RR-68BA, but current control requires a policy-complete immutable publication before that Result can receive current canonical Driver disposition.",
    "why_parent_result_does_not_close_it": "RR-68BA is bound to Gen1 TP2-D425335E9566A3F6A54C, whose taskbook lacks four mandatory V2 body sections. The mathematics is evidence, but the publication cannot serve as the current operational review anchor.",
    "discriminating_outcomes": [
      "ZERO_MATH_DRIFT_CURRENT_POLICY_REFREEZE_OF_RR_68BA",
      "CURRENT_HEAD_EVIDENCE_FORCES_STRONGER_OR_WEAKER_TEMPLATE_BOUNDARY",
      "GEN1_MATHEMATICAL_DEFECT_FOUND_AND_EXACTLY_CLASSIFIED"
    ],
    "kill_condition": "Do not enlarge RR-68BA into b(6)=33, a global impossibility of b(6)<=32, or a no-go for all R4-style truncation. If current evidence does not alter the theorem, preserve the K33, 15/13, 10/7 and scope guards exactly.",
    "alternative_route_or_free_exploration_considered": "Direct atom-splitting/UCS continuation is deferred until the existing exact obstruction is current-policy reviewable. Repeating the entire discovery search is unnecessary unless current-head evidence invalidates a frozen premise.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is a corrected generation of the same stable task identity. It repairs the operational publication envelope while preserving the original Euclidean mother question and prevents downstream work from relying on an invalid publication anchor."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# GEO8 Borsuk R6 Lassak-33 compression pressure — current-policy revalidation Gen2

Status: `READY / P1 / HIGH LEVERAGE / CURRENT-POLICY REVALIDATION`

## Mother question

For the external Euclidean six-dimensional Borsuk problem, can the retained Lassak bound `b(6)<=33` be strictly improved inside a precisely stated continuous construction, or can one prove that a frozen Lassak-derived construction class cannot use `<=32` strict-diameter parts?

Generation 1 already returned the restricted-template answer `RR-68BA014D54542DA7221C`. Generation 2 does not reopen discovery by default. It asks whether that exact mathematical answer survives current-head source and control revalidation unchanged.

## Frozen inputs and scope

Freeze the external Euclidean status and the Gen1 mathematical evidence:

- `7 <= b(6) <= 33`; no exact value is assumed;
- the R6 Lassak lens normalization with `r^2=3/7`, `ell^2=1/84`, `2r ell=1/7`, `rho^2=5/12`;
- the Gen1 frozen template: one cap plus 32 sign-sector atoms, arbitrary legal cap parameter, horizontal `O(5)` rotation, and deterministic orthant-boundary tie-breaking, with repartitioning restricted to unions of whole atoms;
- the exact Gen1 witnesses giving cap-sector distance squared `1` and sector-sector distance squared at least `15/13`;
- the resulting incompatibility graph `K_33`;
- the auxiliary center-fixed untruncated 12 hypercube-facet cone subtemplate with uniform same-part witness squared distance `10/7` for every cube orientation;
- the Gen1 R4-to-R6 audit leaving truncation, movable apex, atom splitting, non-hypercubic directions, multiple UCS representatives, and new five-dimensional orbit geometry outside the obstruction.

The Gen1 Result is evidence, not current Driver authority. Revalidate its exact blobs and source boundaries. If no current evidence changes them, reuse the mathematical Return/checker/artifacts byte-for-byte and create only fresh Gen2 execution/result records as needed by the result contract.

## Hard target and required outputs

Hard target:

`BORSUK_R6_LASSAK_33_BOUND_STRICTLY_IMPROVED_OR_TEMPLATE_OBSTRUCTION_EXACTLY_CLASSIFIED`.

A successful zero-drift Gen2 outcome must certify exactly:

`FROZEN_LASSAK_COMPRESSION_TEMPLATE_CANNOT_BEAT_33`,

at the same restricted strength as RR-68BA, together with the auxiliary `10/7` center-fixed cube-facet obstruction.

Required outputs:

1. a current-head audit of every premise/source used by RR-68BA;
2. deterministic replay of the exact checker and verification of `33` atoms, `528` incompatibility edges, sector-pair lower bound `15/13`, and center-fixed facet lower bound `10/7`;
3. verification that the Gen1 Return, exact-obstruction artifact, transfer audit, dependency graph, source manifest, and adversarial audit remain mathematically unchanged, or an explicit delta if current evidence forces one;
4. a fresh execution record bound to this Gen2 publication;
5. a fresh writer-conformant Result bound to this Gen2 publication with complete Git-blob SHA-1 and SHA-256 bindings;
6. explicit confirmation that no `b(6)=33`, global `b(6)>32`, or full R4-transfer impossibility claim is made.

Do not publish a mathematical successor from the Researcher lane.

## Research value to preserve

The project-local value is the exact structural statement that the obvious whole-atom compression route is maximally rigid: all 33 Lassak atoms are pairwise incompatible. This converts an unsuccessful search direction into a theorem and identifies the smallest structural escape—split/repartition an atom or introduce new truncation/UCS geometry.

The auxiliary `10/7` theorem similarly removes the simplest center-fixed untruncated R6 hypercube-facet port while leaving the genuinely new geometric degrees of freedom open. Preserving these scope boundaries prevents a restricted-template obstruction from being mistaken for a solution of the six-dimensional Borsuk problem.

## Success, kill, and return criteria

Success is either:

- a zero-mathematical-drift current-policy refreeze of RR-68BA at exactly the restricted-template strength; or
- a precisely documented stronger/weaker theorem forced by genuinely new current-head evidence.

Kill or reject any return that:

- turns `K_33` for the frozen atoms into `b(6)>=33`;
- claims global impossibility of `b(6)<=32`;
- treats the `10/7` center-fixed subtemplate no-go as blocking truncation or movable-apex constructions;
- replaces continuous proofs by finite sampling or floating-point search;
- silently upgrades the R4 preprint publication state;
- changes the original Euclidean hard target merely to make revalidation easier.

Return one terminal typed classification and a fresh Gen2 Result. If the exact Gen1 theorem survives unchanged, state `ZERO_MATH_DRIFT` explicitly and stop; atom-splitting/UCS continuation belongs to Driver follow-up after review.