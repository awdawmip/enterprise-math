<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT",
  "title": "HODGE H0N — Non-Split Weil Sixfold Exceptional ch3 Seed Object Gate",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "NONSPLIT_WEIL_SIXFOLD_TARGET_SIDE_EXCEPTIONAL_CH3_SEED_OBJECT_CONSTRUCTED_OR_NATURAL_SOURCE_FAMILY_NO_GO_CLASSIFIED",
  "next_action": "Independently re-verify the H0M non-split target carrier and discriminant barrier from the pinned H0M artifacts, then classify target-side algebraic/derived source families and either construct an object E with nonzero exceptional projection of ch_3(E) to W_K or prove exact no-go results for the declared natural families without inferring non-algebraicity of W_K.",
  "dependencies": [
    "research_task_records/RS-HODGE-H0M-WEIL-SIXFOLD-SEMIREGULARITY-OBSTRUCTION-CANCELLATION/TP2-4D8C1A7E2B609F35C614.json@main",
    "research/hodge-h0m-weil-sixfold-obstruction-cancellation-em-direct-7b2f9a:research_result_records/RS-HODGE-H0M-WEIL-SIXFOLD-SEMIREGULARITY-OBSTRUCTION-CANCELLATION/RR-5E9C7A3D1F842B60C417.json@1c0a65c40add3ec5c10a0444f22e451baf4f9e64",
    "research/hodge-h0m-weil-sixfold-obstruction-cancellation-em-direct-7b2f9a:research_artifacts/HODGE_H0M_WEIL_SIXFOLD/HODGE_H0M_WEIL_SIXFOLD_MODEL_SPEC.json@1c0a65c40add3ec5c10a0444f22e451baf4f9e64",
    "research/hodge-h0m-weil-sixfold-obstruction-cancellation-em-direct-7b2f9a:research_artifacts/HODGE_H0M_WEIL_SIXFOLD/HODGE_H0M_DISCRIMINANT_DEFECT_REGISTRY.json@1c0a65c40add3ec5c10a0444f22e451baf4f9e64"
  ],
  "source_refs": [
    "research/hodge-h0m-weil-sixfold-obstruction-cancellation-em-direct-7b2f9a:research_returns/HODGE_H0M_WEIL_SIXFOLD_SEMIREGULARITY_OBSTRUCTION_CANCELLATION_RETURN_20260831.md@1c0a65c40add3ec5c10a0444f22e451baf4f9e64"
  ],
  "evidence_status": "H0M_RESEARCHER_FROZEN_HARD_BLOCK / DRIVER_REVIEW_PENDING / FOLLOWUP_PUBLICATION_DOES_NOT_GRANT_H0M_WORKING_TRUTH",
  "tags": ["HODGE","H0N","Weil-sixfold","non-split","exceptional-Hodge-class","ch3","derived-object","source-object","countermodel-first"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT",
  "parent_objective_id": "HODGE_SPECIAL_OPEN_FRONTIER_ALGEBRAICITY_MECHANISM",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "HODGEH0N",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-HODGE-H0M-WEIL-SIXFOLD-SEMIREGULARITY-OBSTRUCTION-CANCELLATION",
  "successor_gate": {
    "new_information_gap": "H0M freezes a target-side object-level gap: the non-split Weil carrier can be typed and standard split transport can be obstructed, but no algebraic or derived object on the target component with nonzero exceptional ch_3 projection was constructed.",
    "why_parent_result_does_not_close_it": "The H0M terminal class is an exact hard block with an unblock condition, not a cycle construction and not a non-algebraicity theorem. It therefore leaves the first target-side exceptional source object completely unresolved.",
    "discriminating_outcomes": [
      "construct an explicit coherent sheaf/complex or algebraic family on the declared non-split component and prove proj_WK(ch_3(E)) != 0",
      "construct a target-side algebraic correspondence producing a nonzero exceptional Weil class",
      "prove exact no-go for semihomogeneous/FM-of-line-bundle/divisor-generated or other declared natural source families because their ch_3 remains in the divisor algebra",
      "narrow the search to a smaller source family with an exact missing datum and unblock condition",
      "show the H0M model/frontier premise fails on independent re-verification and terminate without using it"
    ],
    "kill_condition": "Stop on an exact target-side seed object, a complete no-go for all source families declared in the task, invalidation of the H0M target model/frontier, or a precise hard block that identifies the next missing object. Never infer that W_K is non-algebraic merely because the declared source families fail.",
    "alternative_route_or_free_exploration_considered": "Waiting for Driver review of H0M, resuming CBRC F7, and unrelated free exploration remain available. This task is published now because the user explicitly requested capture of the newly isolated object-level frontier; execution must independently re-check every H0M premise it consumes because publication does not grant Working Truth.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "H0M has reached its stated terminal hard-block classification and explicitly forbids fabricating a frontier cycle. H0N changes the mother question from mechanism classification to source-object existence/no-go, so reopening H0M would mix two distinct proof obligations and erase its terminal boundary."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# HODGE H0N — Non-Split Weil Sixfold Exceptional `ch_3` Seed Object Gate

Status: `READY / CONTINUATION / OBJECT-FIRST / NO-WORKING-TRUTH-GRANT`

## Mother question

On a genuinely non-split polarized abelian sixfold of Weil type, can one construct a target-side algebraic or derived object whose codimension-3 characteristic class has a nonzero component in the exceptional two-dimensional Weil-Hodge space, or can one prove that the most natural source families are structurally confined to the divisor algebra?

The task is object-first. It does not ask for a proof of the Hodge conjecture and it does not treat failure of a candidate family as evidence of non-algebraicity.

## Frozen inputs and scope

The immediate motivation is the frozen H0M Researcher result `RR-5E9C7A3D1F842B60C417`, currently awaiting Driver review. H0N receives no Working Truth from that status. Before using any H0M statement as a premise, independently re-check the exact target model, the dimension/type of `W_K`, the divisor-algebra separation, and the discriminant transport obstruction from the pinned source artifacts or primary mathematics.

If those checks fail, terminate with `H0M_PREMISE_INVALIDATED` rather than repairing the parent silently.

If they survive, preserve the declared non-split target class and the target-leakage rule: no known split/discriminant-minus-one cycle, secant sheaf, Chern character or deformation family may be imported merely by renaming it as a target-side construction.

P000 remains the Enterprise Math project starting axiom. Classical Hodge/abelian-variety results used here are external source mathematics and must be reported at their own exact strength; they neither prove nor falsify P000.

Primary source families to audit, without assuming any is exhaustive:

1. semihomogeneous bundles and their shifts/extensions;
2. Fourier-Mukai images of line bundles or semihomogeneous objects that genuinely live on the target component;
3. algebraic constructions generated from the polarization and target-side `K`-endomorphisms;
4. target-side degeneracy/determinantal constructions from explicitly defined vector bundles/complexes;
5. algebraic correspondences from auxiliary varieties that are defined directly for the non-split target and do not cross the forbidden discriminant transport wall.

A new general-purpose computational or formal tool may be introduced only after current tool/method coverage is checked and an exact capability gap is recorded.

## Hard target and required outputs

Hard target:

`NONSPLIT_WEIL_SIXFOLD_TARGET_SIDE_EXCEPTIONAL_CH3_SEED_OBJECT_CONSTRUCTED_OR_NATURAL_SOURCE_FAMILY_NO_GO_CLASSIFIED`.

Required mathematical outputs:

1. an independent H0M-premise audit at the exact strength actually used;
2. a typed exceptional projection map or equivalent decomposition allowing one to distinguish divisor-generated `H^6` from `W_K`;
3. for each audited source family, an exact formula/constraint for its codimension-3 Chern/characteristic class;
4. at least one of:
   - a target-side `E` with a proof that `proj_{W_K}(ch_3(E)) != 0`;
   - a target-side algebraic correspondence with exact nonzero exceptional image;
   - a theorem that a declared natural family always has zero exceptional projection;
5. active counterexample search against every positive or no-go claim;
6. a deterministic checker/certificate only for finite or symbolic reductions that are genuinely checkable; finite computation must not replace an unbounded theorem.

If one nonzero algebraic Weil class is found, the task may test whether the algebraic `K`-action generates the full rational two-dimensional Weil space, but it must prove the exact action on the class rather than assume spanning.

## Research value to preserve

H0M converts a vague open-frontier program into one concrete missing object. H0N preserves that gain by attacking the first place where standard source theory could actually touch the exceptional Weil carrier. A positive seed object would be a genuine new bridge toward class-first algebraicity; a family-level no-go would also be valuable because it removes broad source classes without overclaiming non-algebraicity.

## Success, kill, and return criteria

Success may be positive or negative.

Positive success requires an explicitly defined target-side algebraic/derived object or correspondence and an exact cohomological proof of nonzero exceptional `W_K` component.

Negative success requires a theorem-level obstruction for the declared source family, with the family definition broad enough to be reusable and with explicit counterexample testing against omitted hypotheses.

Kill the route immediately if the target model/frontier is independently invalidated, if a candidate secretly lives only on the split positive-control component, or if the argument reduces to Hodge/Mumford-Tate/absolute-Hodge status without an algebraic source object.

A precise hard block with a named missing object and unblock condition is a valid terminal return. Do not open H1, claim the Hodge conjecture, or claim non-algebraicity from failure of this task.
