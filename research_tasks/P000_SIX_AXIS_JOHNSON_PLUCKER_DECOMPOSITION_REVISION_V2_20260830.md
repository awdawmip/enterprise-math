<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION",
  "title": "P000 six-axis Johnson–Plücker decomposition revision V2",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-johnson-plucker-decomposition",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The first frozen result RR-5E7D2DB7840E5D2F8A57 established the Johnson 1+3+2 decomposition, unsigned-versus-exterior separation, Q_orb and the index-24 integral residue, but Driver review found required Pfaffian/Hodge boundary outputs and the consolidated Gen-current regression table incomplete.",
  "next_action": "Using the original taskbook, frozen result/checker and Driver review as immutable inputs, complete the missing Pfaffian polarization/rank/signature/coefficient-ring boundary, Hodge +/- sectors and orientation law, materialize the Gen-current regression table, rerun exact regression, and freeze a NEW Result-ID with a complete dual-digest output manifest.",
  "dependencies": [
    "TP2-88B098FBEE7FEAF82669",
    "RR-5E7D2DB7840E5D2F8A57",
    "PR#876#issuecomment-5466914659"
  ],
  "source_refs": [
    "research_tasks/P000_SIX_AXIS_JOHNSON_PLUCKER_DECOMPOSITION_20260830.md",
    "research_result_records/RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION/RR-5E7D2DB7840E5D2F8A57.json",
    "research/p000-six-axis-johnson-plucker-em-p000jp1-b4e7c2@c62b6f497c416d9a2946bf648ccd1052f442aec4"
  ],
  "evidence_status": "CORE_MATHEMATICS_PROVISIONALLY_SURVIVES / DRIVER_REQUEST_REVISION / NEW_ONE_SHOT_EXECUTION_REQUIRED",
  "hard_block": null,
  "tags": ["P000","Johnson","Plucker","Pfaffian","Hodge","integral-residue","revision"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-REPRESENTATION-ARITHMETIC",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000JP2",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION",
  "successor_gate": {
    "new_information_gap": "The original Result did not deliver every exact exterior-quadratic output required by the taskbook: explicit bilinear polarization, rank/signature, characteristic/coefficient-ring boundary, Hodge +/- sectors with orientation dependence, and one consolidated Gen-current regression table.",
    "why_parent_result_does_not_close_it": "RR-5E7D2DB7840E5D2F8A57 is immutable and its hard-target disposition overstates completion relative to those missing required outputs; Driver review therefore cannot terminally accept it.",
    "discriminating_outcomes": [
      "missing exterior/Pfaffian/Hodge outputs are completed and the original structural classification survives",
      "a new exact counterexample forces a narrower structural classification",
      "coefficient-ring or orientation analysis reveals a material obstruction requiring rejection of part of the original claim"
    ],
    "kill_condition": "Do not change P000, do not reduce native 6D to the four-label representation, do not identify unsigned Johnson complement with Hodge star, and do not mutate the original Result/return/checker bytes.",
    "alternative_route_or_free_exploration_considered": "Closing the route now would discard a verified index-24 arithmetic residue; opening an unrelated successor would evade the missing original obligations. Completing the exact boundary is the smallest useful action.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The prior researcher execution is one-shot and the original immutable Result cannot be edited; a new claimable publication generation is required for a fresh researcher to complete the same mother question without rewriting history."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 six-axis Johnson–Plücker decomposition revision V2

## Mother question

Can the first Johnson–Plücker result be completed to the exact strength of its original published taskbook, with the missing exterior quadratic and Hodge boundary made explicit, while preserving the verified carrier-level `1+3+2` and index-24 arithmetic structure and without promoting the four-label representation to native P000 geometry?

## Frozen inputs and scope

Freeze publication `TP2-88B098FBEE7FEAF82669`, Result `RR-5E7D2DB7840E5D2F8A57`, its exact frozen outputs, and the Driver review on PR #876 as immutable historical input. Preserve the six labels `AB,AC,AD,BC,BD,CD`, frozen carrier `S4`, Johnson complement, projectors and previously returned index-24 residue. `Lambda^2` of a four-label module remains a representation facade only. The new researcher may correct or narrow claims if exact evidence requires it, but may not mutate prior bytes or infer a native-dimension reduction.

## Hard target and required outputs

Hard target:

`P000_JOHNSON_PLUCKER_REVISION_V2_EXTERIOR_QUADRATIC_BOUNDARY_COMPLETE_AND_RESULT_CHAIN_VALID`.

Required outputs:

1. write the bilinear polarization of `Q=x_AB*x_CD-x_AC*x_BD+x_AD*x_BC` explicitly and state the exact normalization convention;
2. determine rank and signature of the polarized form in characteristic zero, and state the exact coefficient-ring/field hypotheses;
3. classify what changes when `2` is not invertible, with characteristic `2` handled explicitly rather than silently importing characteristic-zero polarization;
4. give explicit bases/dimensions for Hodge `*` `+1/-1` sectors under a declared orientation and prove the orientation-reversal law;
5. materialize one exact regression table for frozen `a_xi,b_xi` across Johnson projectors, complement, signed exterior action/Pfaffian law, Hodge law and every residue consumed downstream;
6. preserve or correctly narrow `Q_orb` and the index-24 integral splitting result;
7. run a deterministic exact checker and freeze a NEW Result-ID whose output manifest pins return, checker, every generated artifact/certificate and the new execution record with Git blob SHA-1 plus SHA-256.

## Research value to preserve

The valuable surviving structure is the separation between a clean rational Johnson spectral decomposition and a nontrivial integral arithmetic obstruction. Completing the exterior-quadratic boundary determines exactly which parts are representation-theoretic convenience, which are orientation-sensitive, and which integer residues are safe for later number-theoretic use.

## Success, kill, and return criteria

Success requires all required outputs above, exact regression, a complete Result manifest, and preservation of the P000 typing firewall. If any original mathematical claim fails, return the smallest exact counterexample and narrow the classification rather than forcing `SUCCESS`. Kill any route that equates carrier `S4` with the full native rotation group, treats `Lambda^2(R^4)` as native 4D reality, identifies complement with Hodge star without proof, or edits prior frozen evidence. Return a NEW immutable Result and request Driver review; do not publish a downstream successor from the researcher lane.