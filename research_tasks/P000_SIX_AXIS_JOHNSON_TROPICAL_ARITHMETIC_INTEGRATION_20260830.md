<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-JOHNSON-TROPICAL-ARITHMETIC-INTEGRATION",
  "title": "P000 six-axis Johnson–Tropical arithmetic integration",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-johnson-tropical-arithmetic-integration",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Johnson/Pfaffian and Tropical Plücker are now separately classified at safe derived six-axis strength; the unresolved cross-task question is exactly how much joint integer and p-adic information is carried by Q_orb, the index-24 residue rho, Johnson sector data, and delta_T, and where their combined fibers still hide Pfaffian cancellation.",
  "next_action": "Freeze one common six-coordinate integer domain, define the joint invariant packet from the accepted Johnson and Tropical results without promoting either to native geometry, then classify exact dependence, fibers, 2/3-primary interactions, p-adic tie regimes and matched counterexamples with a deterministic census.",
  "dependencies": [
    "RR-930072E4A6F2E0FD912F",
    "RR-43B397CD1E8953F613B3"
  ],
  "source_refs": [
    "research_result_records/RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION/RR-930072E4A6F2E0FD912F.json",
    "research_result_records/RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID/RR-43B397CD1E8953F613B3.json"
  ],
  "evidence_status": "DRIVER_ACCEPTED_INPUTS_REQUIRED / CROSS_TASK_INTEGRATION / NO_NATIVE_PROMOTION",
  "hard_block": null,
  "tags": [
    "P000",
    "six-axis",
    "Johnson",
    "Tropical-Plucker",
    "Q_orb",
    "rho",
    "delta_T",
    "arithmetic-integration"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-SIX-AXIS-JOHNSON-TROPICAL-ARITHMETIC-INTEGRATION",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-ARITHMETIC-TROPICAL-INTEGRATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000JTAI1",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 six-axis Johnson–Tropical arithmetic integration

## Mother question

At the exact derived six-axis strength already supported by the accepted Johnson–Plücker and Tropical Plücker results, what additional arithmetic information is obtained by using their safe invariants jointly rather than separately, and what exact fibers or cancellation ambiguities remain?

## Frozen inputs and scope

Freeze the accepted Johnson packet at representation/carrier level: the rational `1+3+2` projectors, `Q_orb`, the integral index-24 splitting residue `rho`, the characteristic-aware Pfaffian/Hodge boundary, and frozen carrier `S4` action. Freeze the accepted Tropical packet only at derived six-weight classifier level: complementary pair sums, `delta_T`, carrier/complement invariance, the exact `W_COORD` census, and the finite nonzero-coordinate `W_VP` valuation theorem. P000 remains a native six-dimensional discrete Cell space plus one-dimensional time. Neither `Lambda^2` nor tropical/valuated-matroid language is a native-dimension replacement, native collapse law, factorization mechanism, Full-Cell lift, Working Truth, or Foundation object.

## Hard target and required outputs

Hard target:

`P000_JOHNSON_TROPICAL_JOINT_ARITHMETIC_INFORMATION_EXACTLY_CLASSIFIED_OR_REDUNDANCY_BOUNDARY_PROVED`.

Required outputs:

1. freeze an exact common integer domain for the six coordinates and, separately where needed, the nonzero-coordinate valuation subdomain;
2. define the joint packet using only safe accepted quantities, including at minimum `Q_orb`, `rho`, `delta_T`, complementary-pair order/tie type, and the Johnson sector data needed to state exact comparisons;
3. classify which components are functionally dependent, independent, or only partially refining one another under the carrier `S4` action;
4. compute exact fibers or rigorous bounded-family certificates showing how much the joint packet reduces ambiguity compared with each accepted packet separately;
5. isolate the interaction of the `(Z/2)^3 x Z/3` integral residue with tropical unique-minimum, two-minimum and triple-tie regimes;
6. on the finite `W_VP` domain, determine what the joint packet can and cannot say about Pfaffian valuation/cancellation, with matched states having identical coarse data but different `Q` or `v_p(Q)` whenever such states exist;
7. include adversarial controls designed to refute an apparent new invariant if it is only a repackaging of the separate accepted data;
8. supply a deterministic exact checker/certificate and a complete Result manifest with Git blob SHA-1 plus SHA-256 for every output.

## Research value to preserve

The Johnson result exposed a genuine rational-versus-integral gap with 2- and 3-primary residue, while the Tropical result exposed a nonredundant piecewise-linear tie classifier and a one-way p-adic cancellation boundary. Their joint fiber structure is the smallest unresolved place where these two independently useful derived calculi can either produce a stronger arithmetic discriminator or be proved redundant. Either outcome is valuable because it determines whether later number-theoretic work should keep the packets coupled or separate.

## Success, kill, and return criteria

Success is an exact joint-information classification with explicit symmetry laws, fibers/counterexamples, arithmetic boundary and deterministic verification. A negative result proving that the combined packet adds no material information beyond a specified product of the separate invariants is also terminal success if accompanied by an exact redundancy certificate. Kill any attempt to infer factorization, native P000 tropical geometry, native dimension reduction, Full-Cell dynamics, or a new general-purpose tool merely from coordinate coincidences. Do not post-select domains or weights after seeing outcomes. Return a NEW immutable Result and request Driver review; do not publish a downstream successor from the researcher lane.
