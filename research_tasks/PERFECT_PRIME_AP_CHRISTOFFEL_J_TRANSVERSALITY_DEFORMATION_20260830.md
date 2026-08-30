<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-CHRISTOFFEL-J-TRANSVERSALITY-DEFORMATION",
  "title": "Perfect Prime AP Christoffel J-transversality deformation flow",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-ap-christoffel-j-transversality-deformation",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Use the AP Christoffel weight essentially by deforming rho_(m,t)(u)=(1-t*u^(m^2))^(m-1) from the exact Cauchy identity endpoint to the AP target and prove that only the known fixed direction survives for every t>0, or freeze the first exact obstruction/no-zero failure.",
  "next_action": "Construct the exact t-dependent normalized half maps and J-twisted operator, quotient out the known fixed direction, identify a scalar/compound/inertia invariant whose first nonzero t-order can be controlled, and prove it has no zero on (0,1] or exhibit an exact obstruction.",
  "dependencies": ["RR-33B5E1F81BCD9EEF1BD1", "DR-7A3C1E9F42B6D0A85C11", "RR-4B168EE0BCE14D5C058A"],
  "source_refs": ["research_returns/PERFECT_PRIME_BETA_BERNSTEIN_OSCILLATION_ORDER_MAP_RETURN_20260830.md@main", "driver_reviews/PERFECT_PRIME_BETA_BERNSTEIN_OSCILLATION_DRIVER_REVIEW_20260830.md@driver/perfect-prime-completed-taskset-review-em-dvr-p8h4q2"],
  "evidence_status": "GENERIC_OSCILLATION_OBSTRUCTED / AP_CHRISTOFFEL_WEIGHT_MANDATORY",
  "hard_block": "ALL_M_AP_CHRISTOFFEL_J_TRANSVERSALITY_NO_ZERO_FLOW",
  "tags": ["Perfect-Prime","Beta-Bernstein","Christoffel","J-transversality","deformation","eigenvalue-1"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-CHRISTOFFEL-J-TRANSVERSALITY-DEFORMATION",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPCHR1",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "MATHEMATICAL_CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-BETA-BERNSTEIN-OSCILLATION-ORDER-MAP",
  "successor_gate": {
    "new_information_gap": "The completed oscillation lane gives an exact Cauchy endpoint with all generic order-map/SSR/TN features intact but eigenvalue 1 maximally non-simple. The AP factor rho_m is therefore the first load-bearing datum not yet isolated by an all-m theorem.",
    "why_parent_result_does_not_close_it": "The oscillation Result is a no-go for generic structure, not a proof of the AP determinant. It explicitly recommends an AP-sensitive deformation or equivalent invariant.",
    "discriminating_outcomes": ["a no-zero/inertia/compound theorem proves the quotient determinant is nonzero for all t in (0,1] and all admissible m", "an exact t or m obstruction disproves the proposed deformation invariant without disproving the AP parent theorem", "a strict local splitting theorem at t=0 plus a separately isolated global no-recrossing residue"],
    "kill_condition": "Do not reuse generic STP, generic common-measure oscillation, finite-m numerics, or complete-monotonicity arguments as proof. The t=0 identity endpoint must be reproduced exactly as a negative control.",
    "alternative_route_or_free_exploration_considered": "The GSTP exterior-cone task tests a distinct external theorem engine. This deformation task is the shortest internal route forced by the Cauchy no-go and does not depend on a generic cone representation.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The oscillation lane has terminally classified its generic route as insufficient. Continuing under a new AP-specific hard target prevents silent reuse of the killed hypothesis class."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP Christoffel J-transversality deformation flow

## Hard target

`AP_CHRISTOFFEL_J_TRANSVERSALITY_NO_ZERO_FLOW_PROVED_OR_EXACTLY_OBSTRUCTED`.

For each admissible `m`, introduce the exact positive-weight deformation

`rho_(m,t)(u) = (1-t*u^(m^2))^(m-1)`, `0 <= t <= 1`.

Freeze the induced normalized half maps and full operator `T_(m,t)` in the same coordinate conventions as the accepted parent. At `t=0`, reproduce the Cauchy control `T_(m,0)=I`. At `t=1`, recover the actual AP target.

Quotient out the known fixed direction. A preferred scalar is the first nonzero normalized coefficient of the quotient determinant near `t=0`, but another exact compound-minor, Krein/J-inertia, crossing form, or transversality invariant is allowed if its implication to `det(I-Q_m)!=0` is proved.

The target is to show that the nontrivial fixed-space multiplicity collapses immediately for `t>0` and never reappears up to `t=1`, or to prove the smallest exact obstruction to such a no-zero flow.

## Mandatory guards

- `t=0` identity is not a nuisance to ignore; it is the adversarial endpoint the proof must depart from correctly.
- The AP Christoffel factor must enter essentially. Any proof that survives unchanged when `rho=1` is invalid.
- Generic STP, entrywise Perron, ordinary norm contraction, generic SSR/TN, and finite-m-as-proof are closed routes.
- Preserve the exact parent equivalence: closing the quotient eigenvalue-1 exclusion must be shown to imply the original all-m cofactor theorem.

## Suggested exact subproblems

1. Determine the exact vanishing order in `t` of the quotient determinant/pseudodeterminant at `t=0`.
2. Compute the crossing form on the `m-1`-dimensional degenerate fixed subspace and seek a sign/inertia law uniform in `m`.
3. Express derivatives of moment/normalizer matrices as Christoffel-weight insertions and search for an Andreief/compound determinant with controlled sign.
4. Prove a no-recrossing theorem on `(0,1]`, or isolate the first exact parameter where current invariants lose control.

## Required evidence

Freeze a return, deterministic exact checker/certificate for finite symbolic claims, execution record, and NEW Result-ID with a complete Git-blob/SHA256 manifest. Finite rational checks may falsify or regress conjectured identities but do not substitute for the all-m proof.
