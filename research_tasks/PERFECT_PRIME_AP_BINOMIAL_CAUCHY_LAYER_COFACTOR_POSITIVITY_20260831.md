<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-BINOMIAL-CAUCHY-LAYER-COFACTOR-POSITIVITY",
  "title": "Perfect Prime AP binomial Cauchy-layer cofactor positivity",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-ap-binomial-cauchy-layer-cofactor-positivity",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Prove or exactly obstruct all-m nonvanishing of the canonical gauge cofactor for the full AP alternating binomial Cauchy-layer deformation, controlling interference among three or more layers.",
  "next_action": "Freeze the exact full-layer cofactor tau_m(t), factor the forced t^(m-1) contribution, then prove tau_m(t) is nonzero on 0<t<=1 for every m>=2 or freeze the first exact obstruction/counterexample without reopening factorwise positivity shortcuts.",
  "dependencies": ["RR-C6E9B75F0A2D8143E6B1", "DR-6C9B75F0A2D8143E6B2"],
  "source_refs": ["research_returns/PERFECT_PRIME_AP_FIXED_POINT_COMPOUND_RESULT_REFREEZE_V2_RETURN_20260831.md", "driver_reviews/PERFECT_PRIME_AP_FIXED_POINT_COMPOUND_REFREEZE_V2_DRIVER_REVIEW_20260831.md"],
  "evidence_status": "ADJACENT_CAUCHY_LAYER_NO_RECROSSING_ACCEPTED / COMPLETE_GEN2_EVIDENCE_CHAIN / MULTILAYER_BINOMIAL_INTERFERENCE_OPEN",
  "hard_block": "FULL_AP_BINOMIAL_CAUCHY_GAUGE_COFACTOR_NONVANISHING_ALL_M",
  "tags": ["Perfect-Prime", "Cauchy", "binomial", "cofactor", "multilayer", "all-m"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-BINOMIAL-CAUCHY-LAYER-COFACTOR-POSITIVITY",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPBCP1",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "MATHEMATICAL_CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-AP-FIXED-POINT-COMPOUND-NO-RECROSSING",
  "successor_gate": {
    "new_information_gap": "The repaired fixed-point compound result proves adjacent two-layer no-recrossing for every m but leaves cancellation among three or more alternating binomial Cauchy layers completely open.",
    "why_parent_result_does_not_close_it": "A two-layer singularity calculation cannot control the determinant/cofactor of the full alternating binomial superposition. Finite m=2..5 positivity is discovery evidence only.",
    "discriminating_outcomes": ["an all-m proof gives tau_m(t) nonzero on 0<t<=1", "a stronger all-m proof gives tau_m(t)/t^(m-1)>0", "an exact m,t counterexample refutes the positivity/nonvanishing route", "an exact obstruction identifies a narrower AP-specific invariant required for multilayer control"],
    "kill_condition": "Reject arguments that use only factorwise STP/GSTP, only adjacent-layer no-recrossing, generic common-measure positivity unchanged at the Cauchy identity endpoint, or finite-m computation as proof.",
    "alternative_route_or_free_exploration_considered": "Generic GSTP, principal-angle and generic common-measure/order-map routes have already been reviewed and either obstructed or narrowed. The full cofactor is the smallest remaining operator-specific residue.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The previous task is terminal at adjacent-layer reduction strength and its evidence envelope is repaired. The parent objective remains open exactly at the full multilayer cofactor."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP binomial Cauchy-layer cofactor positivity

## Hard target

`FULL_AP_BINOMIAL_CAUCHY_GAUGE_COFACTOR_NONVANISHING_ALL_M_PROVED_OR_EXACTLY_OBSTRUCTED`.

For every `m>=2`, use the frozen full deformation

`L_t = sum_{s=0}^{m-1} (-1)^s binom(m-1,s) t^s M_s`

and the canonical gauge cofactor `tau_m(t)` from the accepted fixed-point compound reduction. Prove

`tau_m(t) != 0`

for every `0<t<=1`, or freeze an exact counterexample/obstruction. A preferred stronger sufficient result is

`tau_m(t)/t^(m-1) > 0`.

## Mandatory mathematical obligations

- reproduce the forced `t^(m-1)` vanishing order and the accepted adjacent-layer theorem exactly;
- control interference among **three or more** Cauchy layers rather than only pairwise crossings;
- use the AP alternating binomial structure essentially;
- if using coefficient positivity or a Möbius transform, prove it uniformly in `m` rather than extrapolating from finite rows;
- if using Andreief, compounds, total positivity or variation-diminishing machinery, verify hypotheses for the full alternating superposition, not merely for individual positive factors;
- state precisely whether the output proves nonvanishing, strict positivity, or only a narrower no-crossing invariant.

## Regression firewalls

Mandatory negative controls:

- the Cauchy identity endpoint must remain consistent with the proof;
- factorwise STP/GSTP alone is insufficient;
- generic common-measure/order-map positivity alone is insufficient;
- adjacent two-layer no-recrossing does not imply multilayer noncancellation;
- exact `m=2..5` Möbius/Bernstein positivity and any larger finite census are regression evidence only.

## Required evidence

Freeze the exact symbolic derivation or exact obstruction, deterministic checks for all finite claims, execution provenance, and a NEW Result-ID with complete Git-blob SHA-1 plus SHA-256 bindings for every frozen output. If a positive all-m theorem is obtained, explicitly identify the minimal theorem interface suitable for later independent replication, adversarial stress testing and possible formalization; do not perform those downstream stages inside this task.
