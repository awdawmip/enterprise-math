<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-OUTER-CONDITIONAL-COVARIANCE-DETERMINANT",
  "title": "Perfect Prime AP outer conditional-covariance determinant",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-ap-outer-conditional-covariance-determinant",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Prove or exactly obstruct all-m nonvanishing of the exact outer alternating conditional-covariance determinant S_m(t) that is equivalent to the Perfect Prime fixed-point cofactor.",
  "next_action": "Freeze S_m(t) from the accepted covariance reduction, then derive a noncircular all-m nonvanishing theorem or an equivalent all-m residual Bernstein-positivity theorem, or freeze the first exact counterexample/obstruction.",
  "dependencies": ["RR-A4EBF925BE07691C8C16", "DR-9986FE430DB065EA8EF2"],
  "source_refs": ["research_returns/PERFECT_PRIME_AP_BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_RETURN_20260901.md", "driver_reviews/PERFECT_PRIME_AP_OUTER_CONDITIONAL_COVARIANCE_DRIVER_REVIEW_20260901.md"],
  "evidence_status": "FULL_COFACTOR_EQUIVALENT_TO_OUTER_DETERMINANT / INNER_BLOCKS_INDEFINITE_ALL_M_GE_3 / PARENT_NONVANISHING_OPEN",
  "hard_block": "OUTER_BINOMIAL_CONDITIONAL_COVARIANCE_DETERMINANT_NONVANISHING",
  "tags": ["Perfect-Prime", "conditional-covariance", "determinant", "Bernstein", "all-m"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-OUTER-CONDITIONAL-COVARIANCE-DETERMINANT",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPOCD1",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-AP-BINOMIAL-CAUCHY-LAYER-COFACTOR-POSITIVITY",
  "successor_gate": {
    "new_information_gap": "The full canonical cofactor is now exactly equivalent to det S_m(t), while every individual signed conditional-covariance block is indefinite for m>=3. The missing theorem is therefore an outer cancellation/nonvanishing theorem, not another inner positivity claim.",
    "why_parent_result_does_not_close_it": "The accepted Result closes only the reduction and the direct inner-positive mechanism. It does not prevent the outer alternating determinant from vanishing at an interior parameter.",
    "discriminating_outcomes": ["a noncircular structural theorem proves det S_m(t) nonzero for all m and 0<t<=1", "an all-m proof shows the equivalent double-endpoint residual Bernstein coefficients are strictly positive", "an exact m,t counterexample refutes the nonvanishing target", "an exact obstruction isolates a still narrower AP-specific outer invariant"],
    "kill_condition": "Reject continuity-only fixed-inertia arguments, any proof requiring each inner block to be definite, factorwise STP/GSTP, generic common-measure positivity unchanged at the Cauchy endpoint, or finite-m coefficient positivity as an all-m proof.",
    "alternative_route_or_free_exploration_considered": "The prior GSTP, principal-angle, generic order-map, adjacent-layer and inner conditional-variance routes are already classified. The exact outer determinant is now the smallest load-bearing residue; broad free exploration would duplicate closed mechanisms.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task terminated at an exact negative mechanism boundary and produced a strictly smaller equivalent determinant. The objective cannot close until that determinant is settled."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP outer conditional-covariance determinant

## Mother question

Can the exact outer matrix `S_m(t)` produced by the accepted full multilayer covariance reduction ever become singular for an admissible `m>=2` and `0<t<=1`, or does the AP binomial/Cauchy structure force its determinant to stay nonzero?

## Frozen inputs and scope

Use the accepted Result `RR-A4EBF925BE07691C8C16` exactly. In particular:

- the canonical Perfect Prime cofactor `tau_m(t)` satisfies
  `tau_m(t) = [prod_j w_j Dcal_j(t)] det S_m(t) / [prod_(k=1)^(m-1) k!]^2`;
- every `Dcal_j(t)>0` on the admissible interval;
- hence `tau_m(t)!=0` is equivalent to `det S_m(t)!=0`;
- every inner block `C_j(t)` has inertia `(floor((m-1)/2),ceil((m-1)/2),0)` for `m>=3` and is therefore indefinite;
- `ord_(t=0) tau_m(t)=m-1` is already frozen;
- the double-endpoint residual polynomial `Bhat_m(x)` has positive coefficients only in finite exact regression through `m=10`.

Do not change the AP weight, the binomial layer coefficients, the canonical gauge cofactor, or the definition of `S_m(t)`.

## Hard target and required outputs

Hard target:

`OUTER_BINOMIAL_CONDITIONAL_COVARIANCE_DETERMINANT_NONVANISHING_PROVED_OR_EXACTLY_OBSTRUCTED`.

Prove

`det S_m(t) != 0`

for every `m>=2` and `0<t<=1`, or freeze an exact counterexample/obstruction.

Two proof interfaces are admissible within this single task:

1. derive a structural factorization, congruence, sign-regularity, interlacing, signature, variation or other exact theorem that gives nonvanishing without assuming it; or
2. prove for all `m` that the equivalent double-Cauchy-endpoint residual Bernstein/Mobius coefficients are strictly positive, with the equivalence to the cofactor stated exactly.

A claimed fixed inertia for `S_m(t)` must be derived from additional structure. Continuity plus endpoint inertia is circular unless zero crossings are independently excluded.

Required frozen outputs: symbolic derivation or exact obstruction, deterministic exact checks for all finite claims, execution provenance, and a NEW Result-ID with complete Git-blob SHA-1 plus SHA-256 bindings.

## Research value to preserve

This is the smallest exact scalar/matrix bottleneck currently known for the Perfect Prime all-`m` objective. A positive theorem would close the fixed-point-simplicity obstruction at the present reduction level; a negative result would identify the first genuine outer multilayer failure rather than reopening already-closed generic positivity mechanisms.

Preserve the exact indefinite-inner-block theorem as an adversarial control. Preserve the Cauchy endpoint and the finite `m<=10` residual positivity only as regression evidence.

## Success, kill, and return criteria

Success is an all-`m`, all-`0<t<=1` proof of `det S_m(t)!=0` or an equivalent stronger positivity theorem with exact implication to the canonical cofactor.

A valid negative return is an exact counterexample or a theorem-level obstruction to the declared outer proof mechanism that narrows the remaining invariant.

Kill and reject:

- treating finite `m` computation as proof;
- using the observed fixed inertia of `S_m(t)` as a premise for its own nonvanishing;
- requiring every `C_j(t)` to be positive or negative definite;
- reopening factorwise GSTP/STP or generic common-measure/order-map arguments already frozen as insufficient;
- silently weakening the target to one endpoint, one parity class, or bounded `m`.

If a positive all-`m` theorem is frozen, explicitly state the minimal theorem interface suitable for later independent replication, stress testing and possible formalization; those downstream stages are outside this task.