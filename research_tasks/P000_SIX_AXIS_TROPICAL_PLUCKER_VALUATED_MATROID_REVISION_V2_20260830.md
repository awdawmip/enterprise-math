<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID",
  "title": "P000 six-axis Tropical Plücker / valuated-matroid revision V2",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-tropical-plucker-valuated-matroid",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The first frozen result RR-1D3266F488123BBE9369 supports NONTRIVIAL_SURVIVOR at derived six-weight classifier scope, but Driver review found the Result manifest incomplete and the extended valuation convention at zero coordinates insufficiently typed.",
  "next_action": "Preserve the first result as immutable input, repair the Result envelope with every output pinned, then either give a rigorous extended-tropical +infinity convention and prove the valuation implications on its exact domain or restrict those theorems to the finite-valuation nonzero domain actually certified; rerun exact regression and freeze a NEW Result-ID.",
  "dependencies": [
    "TP2-FEC91ABA20FAAFF4D480",
    "RR-1D3266F488123BBE9369",
    "PR#901#issuecomment-5466915618"
  ],
  "source_refs": [
    "research_tasks/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_20260830.md",
    "research_result_records/RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID/RR-1D3266F488123BBE9369.json",
    "research/p000-six-axis-tropical-plucker-em-p000tp1-8f2c41@221e89ff76bf9011857983857a3cc659d5753db3"
  ],
  "evidence_status": "DERIVED_CLASSIFIER_PROVISIONALLY_SURVIVES / DRIVER_REQUEST_REVISION / NEW_ONE_SHOT_EXECUTION_REQUIRED",
  "hard_block": null,
  "tags": ["P000","tropical-Plucker","valuated-matroid","valuation","result-integrity","revision"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-TROPICAL-COLLAPSE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000TP2",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID",
  "successor_gate": {
    "new_information_gap": "The first Result did not bind checker/certificate/execution outputs in its manifest, and its prose invokes v_p(0)=+infinity without a fully typed extended-tropical domain for delta_T=second_min-min.",
    "why_parent_result_does_not_close_it": "RR-1D3266F488123BBE9369 is immutable; its core finite-domain mathematics may survive, but the current evidence chain and theorem domain are insufficient for terminal Driver acceptance.",
    "discriminating_outcomes": [
      "complete envelope plus exact finite-domain theorem retains NONTRIVIAL_SURVIVOR",
      "a rigorously defined extended +infinity domain validates a stronger zero-inclusive boundary",
      "zero/infinite cases force a narrower theorem or counterexample"
    ],
    "kill_condition": "Do not promote delta_T to native P000 tropical geometry, collapse law, factorization mechanism or Foundation object; do not post-select weights after outcomes; do not mutate the first Result or its frozen outputs.",
    "alternative_route_or_free_exploration_considered": "A new native-collapse successor is premature until the existing classifier result is operationally sound. Discarding the classifier would lose an exact nonredundancy result. Repair and type the existing theorem first.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The first researcher is one-shot and the immutable Result cannot be edited; a new claimable publication generation lets an independent execution close the exact review gaps without rewriting history."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 six-axis Tropical Plücker / valuated-matroid revision V2

## Mother question

Can the first Tropical Plücker result be made terminally auditable by completing its immutable evidence chain and giving an exact domain for its p-adic valuation statements, while preserving only the derived six-weight classifier claim actually supported by evidence?

## Frozen inputs and scope

Freeze publication `TP2-FEC91ABA20FAAFF4D480`, Result `RR-1D3266F488123BBE9369`, its frozen return/checker/certificate/execution provenance, and the Driver review on PR #901 as immutable inputs. The admissible six-axis weight inventory remains pre-outcome. `delta_T` remains a derived classifier; no native collapse law, native tropical geometry, factorization mechanism, Working Truth or Foundation promotion is granted. Sibling Johnson quantities may be used only when locally rederived or explicitly marked as nonterminal comparison data.

## Hard target and required outputs

Hard target:

`P000_TROPICAL_PLUCKER_REVISION_V2_RESULT_CHAIN_AND_VALUATION_DOMAIN_EXACT`.

Required outputs:

1. create a NEW Result-ID and complete output manifest pinning return, checker, every certificate/artifact and the new execution record with Git blob SHA-1 plus SHA-256;
2. state the exact domain of `W_VP`; if zero coordinates are excluded, restrict the valuation theorems to that finite-valuation domain and say so explicitly;
3. alternatively, if zeros are included, define the extended ordered monoid containing `+infinity`, define when `second_min-min` is meaningful, cover all partially/all-infinite cases, and prove every claimed implication on that domain;
4. retain exact carrier `S4`/complement invariance and the all-box `W_COORD` survivor formula or provide a counterexample;
5. retain the matched-control nonredundancy claim only at the tested derived-classifier scope;
6. rerun a deterministic exact checker including boundary cases for the chosen valuation domain.

## Research value to preserve

The result isolates an exact piecewise-linear six-weight classifier that appears nonredundant relative to tested coarse arithmetic observables while simultaneously showing that the p-adic relation to Pfaffian cancellation is only one-way. A rigorous domain boundary is essential before this can safely inform any future collapse/transport research.

## Success, kill, and return criteria

Success requires a complete immutable Result chain and a theorem statement whose valuation domain exactly matches the checker and proof. If zero-inclusive extension fails, narrowing to the certified nonzero domain is acceptable and is not a failure. Kill any attempt to reinterpret ordinary six-tuples as native tropical geometry by fiat, to infer factorization, or to strengthen `Q=0 => delta_T=0` outside the proved valuation domain. Return a NEW immutable Result with exact boundary classification and request Driver review; do not auto-publish a collapse successor.