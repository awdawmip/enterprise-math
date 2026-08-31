<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-HODGE-H0M-WEIL-SIXFOLD-SEMIREGULARITY-OBSTRUCTION-CANCELLATION",
  "title": "HODGE H0M — Weil Sixfold Open-Frontier Semiregularity / Obstruction-Cancellation Gate (V2 migration)",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "OPEN_WEIL_SIXFOLD_ENTERPRISE_ALGEBRAICITY_MECHANISM_CLASSIFIED_WITHOUT_TARGET_LEAKAGE",
  "next_action": "Re-audit the sixfold Weil-type algebraicity frontier from primary literature as of execution date, freeze an actually open discriminant/model scope, then establish the exact rational Weil-Hodge carrier before any cycle or obstruction-mechanism search.",
  "dependencies": [
    "research/hodge-h0m-weil-sixfold-obstruction-cancellation:research_tasks/HODGE_STAGE_H0M_WEIL_SIXFOLD_SEMIREGULARITY_OBSTRUCTION_CANCELLATION_20260823.md@blob:1c5a47ac177fc827022f8872e14ff8b0b0225339",
    "research/hodge-h0m-weil-sixfold-obstruction-cancellation:driver_reviews/HODGE_H0L_CONIVEAU_SUPPORT_DOWNWARD_COLLAPSE_DRIVER_REVIEW_20260823.md@blob:10aefd2e5ab10e9ccac7fa184a24722548a3ec5a",
    "arXiv:2502.03415",
    "arXiv:2603.20268"
  ],
  "source_refs": [
    "arXiv:2502.03415",
    "arXiv:2603.20268"
  ],
  "evidence_status": "LEGACY_H0M_MIGRATED_TO_V2_WITH_ZERO_MATH_DELTA / CURRENT_LITERATURE_GATE_REQUIRED",
  "tags": ["HODGE","H0M","abelian-sixfold","Weil-type","semiregularity","obstruction-cancellation","open-frontier","v2-migration"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-HODGE-H0M-WEIL-SIXFOLD-SEMIREGULARITY-OBSTRUCTION-CANCELLATION",
  "parent_objective_id": "HODGE_SPECIAL_OPEN_FRONTIER_ALGEBRAICITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "HODGEH0M",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-HODGE-H0L-CONIVEAU-SUPPORT-DOWNWARD-COLLAPSE",
  "successor_gate": {
    "new_information_gap": "H0E-H0L repeatedly collapse to source-inherited mechanisms on known-positive Hodge benchmarks and therefore do not test an Enterprise mechanism on a genuinely unresolved algebraicity frontier.",
    "why_parent_result_does_not_close_it": "H0L establishes a source-derived coniveau/Gysin normal form at audited positive scope; it neither proves nor refutes algebraicity of open Weil classes on abelian sixfolds outside the solved split/discriminant-minus-one locus and supplies no obstruction-cancellation classification there.",
    "discriminating_outcomes": "Frontier now solved and model must be reselected; exact frontier hard block; discriminant/transport/semiregularity no-go; source-inherited cycle; or a genuinely new class-first frontier cycle with robust attribution.",
    "kill_condition": "Stop if current literature closes the chosen family, if no exact open-frontier model can be instantiated, if all legal transports preserve the obstructing discriminant class, or once the declared H0M classification is frozen. No automatic H1 promotion.",
    "alternative_route_or_free_exploration_considered": "Continuing additional known-positive benchmark transforms was considered but H0E-H0L already show repeated source inheritance. Moving to a genuinely open sixfold Weil frontier changes both benchmark status and mechanism and has higher discriminating value than another positive-family replay.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "H0L was terminal at coniveau/support-first scope and explicitly did not authorize H1. H0M is a distinct continuation because it changes the benchmark to an unresolved algebraicity frontier and the operational mechanism to derived obstruction formation/cancellation while preserving the Hodge-special mother question."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# HODGE H0M — Weil Sixfold Open-Frontier Semiregularity / Obstruction-Cancellation Gate (V2 migration)

Status: `READY / LEGACY-MIGRATION / ZERO-MATH-DELTA`

## Mother question

Can the Hodge-special program produce or sharply classify an algebraicity mechanism for the two-dimensional Weil-Hodge space on a genuinely open polarized abelian sixfold of Weil type, using exact obstruction/semiregularity/transport analysis rather than replaying source-complete positive benchmark mechanisms?

## Frozen inputs and scope

This is a current-control migration of the legacy H0M task at Git blob `1c5a47ac177fc827022f8872e14ff8b0b0225339`; its mathematical target is not strengthened by publication. H0L is frozen as the accepted negative/source-inherited predecessor at `RS-HODGE-H0L-CONIVEAU-SUPPORT-DOWNWARD-COLLAPSE`.

Before Enterprise mechanism evaluation, recheck current primary literature and classify the selected sixfold family as exactly one of `CURRENTLY_OPEN_FRONTIER_AT_DECLARED_SCOPE`, `NOW_CLASSICALLY_SOLVED__RESELECT_MODEL`, or `LITERATURE_STATUS_UNRESOLVED`.

The benchmark remains a polarized complex abelian sixfold `A` of Weil type for an imaginary quadratic field `K`, with `dim_Q H^1(A,Q)=12`, `dim_K H^1(A,Q)=6`, Weil signature `(3,3)`, and distinguished rational space `W_K(A)=wedge_K^6 H^1(A,Q) subset H^6(A,Q)`. The chosen model/discriminant must be outside every sixfold locus proved algebraic by the literature ledger. The discriminant-minus-one/split construction is a positive control only and may not be renamed as a frontier generator.

The legacy target-leak firewall remains binding: no known solved-locus cycle, secant sheaf, characteristic class, future-signature minimization, provenance quotient, Fermat DFT, coniveau/Gysin rank, or ordinary semiregularity theorem may be relabeled as new Enterprise leverage.

## Hard target and required outputs

Primary hard target: `OPEN_WEIL_SIXFOLD_ENTERPRISE_ALGEBRAICITY_MECHANISM_CLASSIFIED_WITHOUT_TARGET_LEAKAGE`.

The task must first satisfy `OPEN_WEIL_SIXFOLD_EXACT_RATIONAL_HODGE_CARRIER_AND_FRONTIER_MODEL_ESTABLISHED`, including a proof that `dim_Q W_K(A)=2`, that all of `W_K(A)` is of Hodge type `(3,3)` under the `(3,3)` Weil signature, and that the target exceptional Weil space is not silently replaced by the divisor-generated Hodge algebra.

Current-envelope required artifacts are:

- `research_artifacts/HODGE_H0M_WEIL_SIXFOLD/HODGE_H0M_LITERATURE_FRONTIER_LEDGER.json`;
- `research_artifacts/HODGE_H0M_WEIL_SIXFOLD/HODGE_H0M_WEIL_SIXFOLD_MODEL_SPEC.json`;
- `research_artifacts/HODGE_H0M_WEIL_SIXFOLD/HODGE_H0M_DISCRIMINANT_DEFECT_REGISTRY.json`;
- `research_artifacts/HODGE_H0M_WEIL_SIXFOLD/HODGE_H0M_OBSTRUCTION_CANCELLATION_REGISTRY.json`;
- `research_artifacts/HODGE_H0M_WEIL_SIXFOLD/HODGE_H0M_DERIVED_TRANSPORT_REGISTRY.json`;
- `research_artifacts/HODGE_H0M_WEIL_SIXFOLD/HODGE_H0M_CLASS_FIRST_WEIL_LIFT_REGISTRY.json`;
- `research_returns/HODGE_H0M_WEIL_SIXFOLD_SEMIREGULARITY_OBSTRUCTION_CANCELLATION_RETURN_20260831.md`;
- `research_checks/HODGE_H0M_WEIL_SIXFOLD_SEMIREGULARITY_OBSTRUCTION_CANCELLATION_CHECK_20260831.py`;
- current execution/result records under the exact H0M task id.

Accepted terminal classifications remain: robust attributed frontier cycle; frontier cycle but source-inherited; exact discriminant/semiregularity no-go; or exact hard block with missing object and unblock condition.

## Research value to preserve

H0M is the first Hodge-special stage deliberately moved away from theorem-positive controls to a live algebraicity frontier. Its value is not a promise to solve the Hodge conjecture; it is a rigorous discriminator between genuinely new obstruction-cancellation leverage, source-inherited derived geometry, transport no-go, and an exact missing-object frontier. That classification can prevent further benchmark overfitting while preserving a credible route to a real open problem.

## Success, kill, and return criteria

Success requires a primary-source literature ledger, an exact open-frontier model or explicit hard block, exact carrier typing before cycle search, and a target-leak-audited classification of the obstruction/transport/class-first mechanisms. A cycle claim must give an actual codimension-three algebraic cycle or source-generated algebraic family on the frontier model whose rational class equals/spans the declared Weil-Hodge target; absolute-Hodge or Mumford-Tate status alone is insufficient.

Freeze on any exact hard block or no-go rather than substituting a solved special family. Do not automatically open H1 even if a frontier cycle is found; H1 requires a separately published review/promotion decision.
