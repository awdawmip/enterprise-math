<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-BETA-BERNSTEIN-PRINCIPAL-ANGLE-EXTERIOR-POWER",
  "title": "Perfect Prime Beta–Bernstein common-measure principal-angle / exterior-power closure",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-beta-bernstein-principal-angle-exterior-power",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Exploit the common Beta measure behind Ahat and Bhat to prove det(I_(m-1)-Q_m) != 0 for all admissible m through a genuine Gram/principal-angle/exterior-power structure, or freeze the smallest exact geometric obstruction.",
  "next_action": "Reconstruct the accepted common-measure Beta–Bernstein factorization as explicit maps between finite-dimensional Bernstein subspaces in one Hilbert/L2 measure space; identify the quotient fixed-vector equation and test whether principal angles, compound matrices or wedge-power transversality exclude eigenvalue 1 beyond the distinguished e0 direction.",
  "dependencies": [
    "RR-86E59AB8D7FBF3917D94",
    "DR-31F878F8AA6815962C6A"
  ],
  "source_refs": [
    "research_returns/PERFECT_PRIME_TABLE_BETA_BERNSTEIN_QUOTIENT_RESULT_REFREEZE_V2_RETURN_20260830.md@main",
    "driver_reviews/PERFECT_PRIME_BETA_BERNSTEIN_REFREEZE_DRIVER_REVIEW_20260830.md"
  ],
  "evidence_status": "ACCEPTED_BETA_BERNSTEIN_FRONTIER / ALL_M_QUOTIENT_NONDEGENERACY_OPEN",
  "last_progress_ref": "RR-86E59AB8D7FBF3917D94 / DR-31F878F8AA6815962C6A",
  "last_progress_at": "2026-08-30T02:52:30+00:00",
  "hard_block": "EIGENVALUE_1_EXCLUSION_FOR_Q_M",
  "tags": ["PerfectPrime","Beta-Bernstein","principal-angles","exterior-power","compound-matrix","common-measure","all-m"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-BETA-BERNSTEIN-PRINCIPAL-ANGLE-EXTERIOR-POWER",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTBBPA",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "MATHEMATICAL_CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "successor_gate": {
    "new_information_gap": "The accepted result reduces the entire Route-A theorem to det(I-Q_m) != 0 and proves that generic STP/PF/norm shortcuts are insufficient, but it does not use the strongest extra datum: Ahat and Bhat arise from one common Beta measure and Bernstein systems linked by u -> u^m.",
    "why_parent_result_does_not_close_it": "The parent Result is an integrity re-freeze of an unresolved exact frontier; no all-m exclusion of eigenvalue 1 has been proved.",
    "discriminating_outcomes": [
      "FULL: construct an exact common-Hilbert-space/principal-angle or exterior-power representation that proves eigenvalue 1 is simple for every admissible m",
      "STRICT_PARTIAL: reduce det(I-Q_m) != 0 to one explicit all-m transversality/compound-minor inequality that is strictly narrower than generic STP",
      "OBSTRUCTION: prove the principal-angle/exterior-power interface cannot distinguish the quotient fixed point without an additional invariant, with an exact counterexample/model preserving the accepted hypotheses"
    ],
    "kill_condition": "Do not restart generic STP, entrywise Perron-Frobenius, ordinary norm contraction, full sign-regularity, or finite-m census as proof; do not merely rename det(I-Q_m) as a Gram determinant without deriving a new all-m sign/transversality mechanism.",
    "alternative_route_or_free_exploration_considered": "The sibling oscillation/order-map lane attacks sign-change dynamics rather than Hilbert/principal-angle geometry. Keeping the interfaces separate gives a genuine cross-check and prevents two parallel researchers from repeating the same STP argument.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The envelope-repair task is terminal at revision scope; the remaining work is substantive mathematics with a new proof interface and therefore requires a distinct immutable task."
  }
}
-->

# Perfect Prime Beta–Bernstein common-measure principal-angle / exterior-power closure

## Frozen frontier

Consume `RR-86E59AB8D7FBF3917D94` and `DR-31F878F8AA6815962C6A` exactly. The accepted reduction is

`T_m = R K R = R Bhat R Ahat = [[1,*],[0,Q_m]]`

with `Ahat,Bhat` strictly totally positive Beta–Bernstein matrices arising from the **same** one-dimensional measure

`(1-u^(m^2))^(m-1) du`

and Bernstein coordinates related by `u -> u^m`.

The hard target is

`det(I_(m-1)-Q_m) != 0`

for every admissible `m`, or an exact counterexample to the parent theorem.

## Required attack

Do not treat `Ahat` and `Bhat` as arbitrary STP matrices. Reconstruct their common-measure origin explicitly. Preferred interfaces include:

- Gram/moment factorizations in a single weighted `L2` or finite moment space;
- two Bernstein subspaces/flags and their principal angles;
- compound matrices / exterior powers / wedge products;
- total positivity plus transversality of flags generated by the common measure;
- an exact determinant identity converting `det(I-Q_m)` into a positive/nonzero mixed Gram, angle, or compound-minor object.

A successful proof must explain why the distinguished fixed direction `e0` is the only fixed direction. A strict partial result must reduce the problem to a smaller explicit all-m inequality or transversality lemma, not to an equivalent restatement.

## Exact evidence

Freeze:

1. a symbolic derivation of the chosen representation;
2. exact low-m rational checks only as regression;
3. an adversarial example showing which weaker geometric statement is insufficient if the full proof does not close;
4. a deterministic checker for all finite identities used in the proof interface.

## Guards

Forbidden as terminal evidence:

- finite-m verification alone;
- generic STP => spectral conclusion;
- entrywise PF on `Q_m`;
- ordinary `l_infinity` contraction;
- the falsified full sign-regular core shortcut;
- numerical floating-point principal angles without exact symbolic control;
- claiming novelty or Foundation/Working Truth status.

## Terminal classes

- `FULL_COMMON_MEASURE_GEOMETRIC_CLOSURE_PROVED`
- `STRICT_TRANSVERSALITY_REDUCTION_PROVED`
- `PRINCIPAL_ANGLE_EXTERIOR_POWER_ROUTE_OBSTRUCTED_WITH_EXACT_MODEL`
- `EXACT_COUNTEREXAMPLE_TO_PARENT_FOUND`
