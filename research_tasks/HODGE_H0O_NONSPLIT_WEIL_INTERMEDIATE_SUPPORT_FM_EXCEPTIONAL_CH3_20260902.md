<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3",
  "title": "HODGE H0O — Non-Split Weil Sixfold Intermediate-Support Fourier–Mukai Exceptional ch3 Gate",
  "kind": "RESEARCH",
  "owner": "research/hodge-h0o-intermediate-support-fm-exceptional-ch3",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "H0N isolates an exact algebraic projector Pi_W onto the exceptional Weil space and proves zero exceptional ch_3 for several natural divisor-generated and semihomogeneous source families, while explicitly leaving genuinely non-semihomogeneous Fourier–Mukai outputs with intermediate support unresolved.",
  "next_action": "Fix one explicit intermediate-support Fourier–Mukai kernel/output family on the same non-split discriminant [-3] Weil sixfold, derive its codimension-three GRR contribution block-by-block, and either construct a target-side algebraic/derived object with nonzero Pi_W(ch_3) or prove a theorem-level zero-projection obstruction for that declared family.",
  "dependencies": [
    "research_result_records/RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT/RR-65EB865C14B89B964BB9.json",
    "research_artifacts/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT/HODGE_H0N_PREMISE_PROJECTOR_AUDIT.json",
    "research_artifacts/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT/HODGE_H0N_SOURCE_FAMILY_NO_GO_REGISTRY.json"
  ],
  "source_refs": [
    "research_returns/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_RETURN_20260902.md"
  ],
  "evidence_status": "H0N_DRIVER_SCOPE_AUDIT_ACCEPTED_NEGATIVE_BOUNDARY / EXACT_EXCEPTIONAL_PROJECTOR_AVAILABLE / GENERAL_SEED_EXISTENCE_OPEN",
  "tags": [
    "HODGE",
    "H0O",
    "Weil-sixfold",
    "non-split",
    "Fourier-Mukai",
    "GRR",
    "intermediate-support",
    "exceptional-ch3",
    "counterexample-first"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3",
  "parent_objective_id": "HODGE_SPECIAL_OPEN_FRONTIER_ALGEBRAICITY_MECHANISM",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "HODGEH0O",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT",
  "successor_gate": {
    "new_information_gap": "H0N proves exact no-go results for semihomogeneous bundles, finite cone/extension closures, divisor-generated constructions, determinantal classes with divisor-algebra Chern data, and only those Fourier–Mukai outputs already known to be semihomogeneous. It does not classify genuinely non-semihomogeneous Fourier–Mukai outputs with intermediate support, where GRR can mix source support geometry into degree six.",
    "why_parent_result_does_not_close_it": "H0N explicitly restricts its Fourier–Mukai no-go to verified semihomogeneous-output subfamilies and states that arbitrary target-side Fourier–Mukai objects remain open unless output type and support are independently controlled. The existence of the algebraic projector Pi_W separates the target component but does not supply a nonzero seed.",
    "discriminating_outcomes": [
      "construct an explicitly defined intermediate-support Fourier–Mukai object E on the fixed non-split target and prove Pi_W(ch_3(E)) is nonzero",
      "prove by an exact GRR/block-decomposition argument that every object in the declared intermediate-support kernel family has Pi_W(ch_3)=0",
      "show that the declared family cannot be instantiated on the fixed non-split target without importing forbidden split/discriminant-minus-one data, and isolate the exact missing kernel or support datum"
    ],
    "kill_condition": "Freeze immediately on a verified nonzero exceptional ch_3 seed, a theorem-level zero-projection result for the whole declared intermediate-support family, or an exact target-side instantiation obstruction with a named unblock condition. Do not broaden within this task to arbitrary correspondences, all derived objects, or a claim of non-algebraicity.",
    "alternative_route_or_free_exploration_considered": "A general search over arbitrary algebraic correspondences was rejected as too broad because H0N already shows that correspondences can project onto W_K at operator level. A general search over all non-semihomogeneous objects was also rejected as under-typed. Intermediate-support Fourier–Mukai/GRR is preferred because it is the narrowest major source family explicitly left open by H0N and admits exact support and Chern-character bookkeeping.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "H0N is terminal at a reusable negative boundary for its declared natural families. Reopening H0N would blur an accepted no-go package with a new source family whose support geometry and GRR terms require different hypotheses and counterexamples. Closure would discard the most specific open family identified by the accepted boundary."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:46f9b27002cd7f8a3d64fdec95e8c4519dc99d8f003b48c21e4f94182bc98e8b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# HODGE H0O — Non-Split Weil Sixfold Intermediate-Support Fourier–Mukai Exceptional `ch_3` Gate

Status: `READY / CONTINUATION / FAMILY-FIRST / COUNTEREXAMPLE-FIRST`

## Mother question

For the fixed very-general non-split Weil sixfold with `K=Q(i)` and discriminant class `[-3]`, does a genuinely non-semihomogeneous Fourier–Mukai construction with controlled intermediate support produce a target-side algebraic or derived object `E` with `Pi_W(ch_3(E)) != 0`, or does Grothendieck–Riemann–Roch force zero exceptional projection for the declared family?

This task asks only about one explicitly typed intermediate-support Fourier–Mukai family. It does not ask for a theorem about all derived objects or all correspondences.

## Frozen inputs and scope

Use the H0N exact target model and its algebraic spectral projector `Pi_W` only at the strength accepted by Driver review: `Pi_W` isolates the exceptional two-dimensional Weil space in degree six, annihilates the divisor-cube line, and is a separator rather than a seed.

Preserve the H0N negative boundary. Semihomogeneous outputs, finite shifts/direct sums/extensions/cones built from them, divisor-generated inputs, and determinantal classes whose Chern data already lie in the divisor algebra are not to be rediscovered as new work.

Choose and freeze before calculation one explicit target-side Fourier–Mukai setup `Phi_P : D^b(X) -> D^b(A_gen)` or an endo-Fourier–Mukai kernel on `A_gen`, together with the source object class, support dimension/codimension, WIT/cohomological-amplitude hypotheses if used, and the exact GRR pushforward formula. The output family must not be certified semihomogeneous by the hypotheses; otherwise it falls back into H0N.

Known split or discriminant-minus-one cycle constructions may be used only as negative controls. They may not be transported or relabeled onto the non-split target without an independently valid target-side construction.

## Hard target and required outputs

Hard target:

`NONSPLIT_WEIL_INTERMEDIATE_SUPPORT_FM_EXCEPTIONAL_CH3_SEED_OR_EXACT_NO_GO_CLASSIFIED`.

Required outputs:

1. a typed specification of the chosen Fourier–Mukai kernel, source family, support geometry, and target output;
2. an exact GRR decomposition of the degree-six / codimension-three contribution to `ch(Phi_P(F))`;
3. a blockwise computation against the H0N `B_p` decomposition or an equivalent exact test for `Pi_W`;
4. at least one terminal theorem:
   - an explicit algebraic/derived output `E` with `Pi_W(ch_3(E)) != 0`;
   - a theorem that every output in the declared family has `Pi_W(ch_3)=0`;
   - an exact proof that the declared family cannot be instantiated on the fixed non-split target, with the missing datum named;
5. adversarial tests against hidden semihomogeneity, divisor-algebra collapse, imported split data, and unsupported support/WIT assumptions;
6. finite symbolic checks only where they certify a finite reduction; they must not replace the unbounded GRR or geometric argument.

A positive result must identify an actually algebraic/derived source object and cannot consist only of applying `Pi_W` to an unspecified algebraic class.

## Research value to preserve

H0N converts the open sixfold problem into an exact separator plus a list of broad natural source families that provably miss the exceptional component. H0O preserves that progress and attacks the sharpest remaining structured gap: Fourier–Mukai outputs whose intermediate support prevents immediate reduction to the semihomogeneous/divisor-algebra formulas already closed.

Either outcome is useful. A nonzero seed would supply the first target-side bridge into `W_K`; a family-level no-go would eliminate a major unresolved construction route without making any non-algebraicity claim.

## Success, kill, and return criteria

Positive success requires an explicit target-side object in the frozen family and a theorem that its exceptional `ch_3` projection is nonzero.

Negative success requires a theorem-level obstruction for the entire declared intermediate-support family, with all support, WIT, smoothness, and GRR hypotheses stated exactly.

A precise target-side instantiation obstruction is also terminal if it names the missing kernel/support datum and gives a falsifiable unblock condition.

Kill the route on the first valid terminal theorem. Do not expand the task to arbitrary correspondences, arbitrary derived categories, all Fourier–Mukai kernels, H1, the full Hodge conjecture, or non-algebraicity of `W_K`.
