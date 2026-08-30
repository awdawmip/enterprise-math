<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-GSTP-EXTERIOR-CONE-CERTIFICATE",
  "title": "Perfect Prime AP full-operator GSTP exterior-cone certificate",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-ap-gstp-exterior-cone-certificate",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Determine whether the actual AP operator T_m=R Bhat R Ahat is generalized strictly totally positive in an explicit proper-cone system on every exterior power, so the known eigenvalue 1 is simple, or prove an exact task-local obstruction to that theorem engine.",
  "next_action": "Pin the actual AP operator and accepted GSTP antecedent, construct candidate proper cones K_j(m) for wedge^j T_m, prove strict invariance and properness uniformly in m and j or freeze the first exact obstruction; keep the Cauchy identity endpoint as a negative control against generic common-measure arguments.",
  "dependencies": ["RR-4B168EE0BCE14D5C058A", "DR-5D1B8E24C79A6F30B442", "RR-33B5E1F81BCD9EEF1BD1"],
  "source_refs": ["research_returns/PERFECT_PRIME_BETA_BERNSTEIN_PRIOR_ART_AUDIT_RETURN_20260830.md@main", "research_returns/PERFECT_PRIME_BETA_BERNSTEIN_OSCILLATION_ORDER_MAP_RETURN_20260830.md@main"],
  "evidence_status": "PRIOR_ART_ACTIONABLE / AP_SPECIFIC_GSTP_INTERFACE_OPEN",
  "hard_block": "EXPLICIT_ALL_WEDGE_PROPER_CONE_SYSTEM_OR_EXACT_OBSTRUCTION",
  "tags": ["Perfect-Prime","Beta-Bernstein","GSTP","exterior-power","proper-cone","AP-Christoffel"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-GSTP-EXTERIOR-CONE-CERTIFICATE",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPGSTP1",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "MATHEMATICAL_CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-BETA-BERNSTEIN-PRIOR-ART-AUDIT",
  "successor_gate": {
    "new_information_gap": "The external audit identifies GSTP as a theorem engine that would immediately imply fixed-point simplicity, but no explicit proper-cone family is known for the signed AP product T_m. Factorwise STP is insufficient.",
    "why_parent_result_does_not_close_it": "The prior-art Result only maps hypotheses. The oscillation Result further proves that generic common-measure/order-map positivity survives at a Cauchy endpoint where T=I, so any valid cone certificate must use AP-specific Christoffel information.",
    "discriminating_outcomes": ["explicit all-m proper cones on every exterior power prove GSTP and hence simplicity of eigenvalue 1", "an exact obstruction shows at least one required wedge cone/invariance condition cannot hold for the actual AP family", "a strict partial cone theorem isolates the first unresolved wedge degree or m-uniform step"],
    "kill_condition": "Do not infer GSTP from STP of Ahat/Bhat, finite-m positive spectra, or an ordinary positive cone on Q_m. Do not ignore the Cauchy K=I negative control.",
    "alternative_route_or_free_exploration_considered": "The independent Christoffel deformation lane attacks AP transversality directly; this task is retained because GSTP supplies an external theorem that would close the parent target immediately if its exact hypotheses can be verified.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The prior-art audit is terminal at literature-classification scope; verifying the missing GSTP hypotheses is a distinct mathematical theorem task."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP GSTP exterior-cone certificate

## Hard target

`AP_FULL_TM_GSTP_EXTERIOR_CONE_SYSTEM_PROVED_OR_EXACTLY_OBSTRUCTED`.

Freeze the exact actual AP operator

`T_m = R Bhat R Ahat`, `T_m e_0=e_0`,

and determine whether it satisfies a Kushel-style generalized strict total positivity theorem in an **explicit** proper-cone system on every `wedge^j R^m`.

A positive terminal result must identify the cones, prove properness, prove strict invariance for every relevant `m,j`, and then spell out the implication: the spectrum of `T_m` is simple, hence the known eigenvalue `1` is simple, hence `det(I_(m-1)-Q_m) != 0`.

An obstruction terminal result must be exact and operator-specific. It is acceptable to prove that the GSTP engine cannot apply, provided the failed hypothesis is exhibited rather than inferred from a finite search.

## Mandatory guards

- Factorwise STP of `Ahat` and `Bhat` is already known and is **not** enough.
- The Cauchy endpoint with the same broad architecture has `K_0=I`; any purported generic common-measure/order-map cone proof is invalid unless it distinguishes the AP Christoffel weight.
- Direct TN/positivity of `Q_m` is already false at small m.
- Finite exact computation is regression/counterexample evidence only, never an all-m proof.
- No novelty claim follows from the prior-art no-exact-match search.

## Required evidence

Freeze a return, exact checker/certificate for all finite claims, execution record, and NEW Result-ID with complete Git-blob/SHA256 manifest. If an external theorem is invoked, pin the theorem statement and verify its hypotheses one by one for the actual operator.
