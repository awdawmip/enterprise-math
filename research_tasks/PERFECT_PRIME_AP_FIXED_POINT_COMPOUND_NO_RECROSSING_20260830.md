<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-FIXED-POINT-COMPOUND-NO-RECROSSING",
  "title": "Perfect Prime AP fixed-point compound no-recrossing",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-ap-fixed-point-compound-no-recrossing",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Prove the AP fixed eigenvalue 1 stays simple for all admissible m by controlling a fixed-point-specific (m-1)-compound or cofactor of the Christoffel defect through derivative singularities, without requiring the remaining spectrum to stay real or positive.",
  "next_action": "Freeze the exact t-dependent fixed-point defect Gamma_(m,t) after quotienting the known fixed direction, select a canonical maximal cofactor or compound coordinate, derive a signed matrix-tree, Andreief, or equivalent exact representation, and prove it is nonzero for every 0<t<=1 or freeze the first exact obstruction.",
  "dependencies": ["RR-B78804DDB25876AD4EE1", "DR-C7F2A0945E1B83D62A40", "RR-0BCEB5E65D4B34FB3462", "DR-4E8A71C25D0F9B3A6182", "RR-A01DA4C69A8CDF44A37C", "DR-28B6F10C93E4A75D1B82"],
  "source_refs": ["research_returns/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_RETURN_20260830.md", "research_returns/PERFECT_PRIME_AP_GSTP_EXTERIOR_CONE_CERTIFICATE_RETURN_20260830.md", "driver_reviews/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DRIVER_REVIEW_20260830.md", "driver_reviews/PERFECT_PRIME_AP_GSTP_EXTERIOR_CONE_DRIVER_REVIEW_20260830.md"],
  "evidence_status": "ALL_M_LOCAL_SPLITTING_PROVED / FULL_SPECTRUM_GSTP_OBSTRUCTED_AT_M10 / POINTWISE_DERIVATIVE_REGULARITY_OBSTRUCTED_AT_M3",
  "hard_block": "ALL_M_FIXED_POINT_COMPOUND_NO_RECROSSING",
  "tags": ["Perfect-Prime", "AP-Christoffel", "fixed-point", "compound", "matrix-tree", "no-recrossing"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-FIXED-POINT-COMPOUND-NO-RECROSSING",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPFPC1",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "MATHEMATICAL_CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-AP-CHRISTOFFEL-J-TRANSVERSALITY-DEFORMATION",
  "successor_gate": {
    "new_information_gap": "The AP deformation now has an all-m nondegenerate first crossing at t=0, but pointwise derivative regularity fails at m=3 and universal GSTP fails at m=10. The remaining theorem is specifically global persistence of the one-dimensional fixed space through those failures.",
    "why_parent_result_does_not_close_it": "Local splitting only controls sufficiently small t, while the m=3 derivative singularity shows that instantaneous crossing-form regularity cannot propagate the result to t=1. The m=10 non-real pair shows full-spectrum positivity cannot replace the missing fixed-point argument.",
    "discriminating_outcomes": ["one explicit maximal cofactor or compound coordinate is proved nonzero for all admissible m and 0<t<=1, closing fixed-point simplicity", "an exact zero of the selected fixed-point compound is found and classified as parent counterexample or coordinate artifact", "a representation theorem reduces global no-recrossing to one narrower sign/nonvanishing lemma"],
    "kill_condition": "Do not assume all quotient eigenvalues are real or positive, do not assume Gamma'_t is everywhere nondegenerate, and do not promote finite-m checks to an all-m proof.",
    "alternative_route_or_free_exploration_considered": "Full-spectrum GSTP and generic oscillation have exact negative boundaries. A fixed-point compound is the shortest surviving route because it asks only for the invariant needed by the parent theorem.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The previous deformation task terminally classified the local crossing theorem and its globalization failure. The new hard target is a different invariant that must survive derivative singularities."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP fixed-point compound no-recrossing

## Hard target

`AP_FIXED_POINT_COMPOUND_NO_RECROSSING_PROVED_OR_EXACTLY_OBSTRUCTED`.

Retain the exact deformation

`rho_(m,t)(u)=(1-t*u^(m^2))^(m-1)`, `0<=t<=1`,

and the accepted fixed direction. Work on the quotient fixed-point defect `Gamma_(m,t)` or an exactly equivalent matrix whose rank `m-1` is equivalent to `det(I-Q_(m,t)) != 0`.

A positive terminal result must exhibit one explicit maximal proper minor, cofactor, compound coordinate, signed tree sum, or equivalent scalar invariant and prove it never vanishes for every admissible `m` and `0<t<=1`.

An obstruction must distinguish an actual fixed-point zero from failure of the chosen coordinate or proof representation.

## Mandatory guards

- At `t=0`, the fixed-space multiplicity is large, but the accepted all-m crossing theorem gives vanishing order exactly `m-1` and immediate splitting for `t>0`.
- Pointwise nondegeneracy of `Gamma'_(m,t)` is not available globally; it fails exactly already at `m=3` without producing a fixed-point zero.
- Universal GSTP/full-spectrum positivity is false for the actual AP family at `m=10`; a non-real non-fixed conjugate pair is allowed.
- Generic STP, entrywise Perron, ordinary norm contraction, generic common-measure oscillation and finite computation as proof remain closed.

## Preferred interfaces

1. signed bipartite-Laplacian / matrix-tree expansion of a quotient cofactor;
2. Andreief or compound-determinant integral formula with an AP-Christoffel-specific sign/nonzero mechanism;
3. exterior `(m-1)`-compound control that is fixed-point-specific and does not require positivity of all lower wedge powers;
4. higher-order crossing/spectral-flow analysis at isolated derivative singularities, provided it concludes a scalar nonzero invariant.

## Required evidence

Freeze a return, exact checker/certificate for finite claims, execution record, and a NEW Result-ID with complete Git-blob/SHA256 bindings. Any all-m statement must be analytic/algebraic; finite exact computation is regression or falsification evidence only.
