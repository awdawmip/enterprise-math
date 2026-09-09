<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-HCM0-EXTREME-BRANCH-PARITY-DOMINATION",
  "title": "Perfect Prime AP HCM0 extreme branch parity domination",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The parent HCM0 execution has an all-m inverse-free signed branch expansion for every mixed coefficient. For the first dangerous extreme three-support coefficient it reduces the normalized trace to a labeled three-index alternating-square sum with positive beta/binomial magnitudes and explicit Vandermonde-integral branch amplitudes. Full-parameter trace positivity is exact for m=3,4,5,6, while the all-m parity-mass comparison remains open.",
  "next_action": "Starting from the handoff index and the exact trace formula in EXTREME_COEFFICIENT_SIGNED_BRANCH_BRC_REDUCTION_20260906.md, prove that for actual synchronized gaps M=m a and N=m(a+c) the oriented positive-parity branch mass strictly dominates the negative-parity mass at the strength needed for the coalescent baseline n=m-1, or freeze the first exact actual-gap obstruction.",
  "dependencies": [],
  "source_refs": [
    "git:awdawmip/enterprise-math@623a4ee81911cc79d07ed5db1887a06ebe91ffd5:research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/HCM0_RESEARCH_HANDOFF_INDEX_20260909.md",
    "git:awdawmip/enterprise-math@623a4ee81911cc79d07ed5db1887a06ebe91ffd5:research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/EXTREME_COEFFICIENT_SIGNED_BRANCH_BRC_REDUCTION_20260906.md",
    "git:awdawmip/enterprise-math@623a4ee81911cc79d07ed5db1887a06ebe91ffd5:research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/M6_ALL_PARAMETER_NORMALIZED_TRACE_CERTIFICATE_20260906.md",
    "git:awdawmip/enterprise-math@623a4ee81911cc79d07ed5db1887a06ebe91ffd5:research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/ALL_M_TANGENT_FACE_COEFFICIENTWISE_POSITIVITY_20260906.md"
  ],
  "evidence_status": "ALL_M_SIGNED_BRANCH_REDUCTION / ALL_M_TANGENT_FACE / FULL_PARAMETER_TRACE_M3_TO_M6",
  "last_progress_ref": "git:awdawmip/enterprise-math@623a4ee81911cc79d07ed5db1887a06ebe91ffd5:research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/HCM0_RESEARCH_HANDOFF_INDEX_20260909.md",
  "last_progress_at": "2026-09-09T01:07:54+00:00",
  "hard_block": "M7_EXTREME_BRANCH_PARITY_DOMINATION",
  "tags": [
    "Perfect-Prime",
    "HCM0",
    "signed-branch",
    "mixed-discriminant",
    "BRC",
    "parity",
    "three-support"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-HCM0-EXTREME-BRANCH-PARITY-DOMINATION",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPM7",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT",
  "successor_gate": {
    "new_information_gap": "The parent task produced a new all-m signed branch carrier, maximal-minor rigidity, an inverse-free three-index trace formula, and an explicit Vandermonde integral for each branch amplitude. The unresolved question is no longer a generic determinant sign problem but a precise parity-mass domination theorem on this branch space.",
    "why_parent_result_does_not_close_it": "Both parity classes are nonempty and termwise positivity is false. The parent execution proves exact low-dimensional trace certificates and the tangent face, but it does not compare the two all-m branch populations.",
    "discriminating_outcomes": [
      "Prove the parity-mass domination for every m>=2 and actual positive block lengths, establishing the all-m normalized extreme-coefficient trace theorem.",
      "Freeze an exact actual-gap counterexample to parity domination, showing that the observed m=3,4,5,6 trace theorem does not extend uniformly.",
      "Prove the extreme coefficient by an alternative exact summation or involution on the same labeled branch carrier while preserving parity provenance.",
      "Show that the current branch amplitudes omit a necessary statistic and isolate the minimal additional invariant required for an all-m comparison."
    ],
    "kill_condition": "Reject finite-m tables as an all-m proof, termwise positivity of signed branches, positive-real spectrum, generic total positivity without the actual beta/gap synchronization, and any compression that merges the two parity populations.",
    "alternative_route_or_free_exploration_considered": "A complementary tangent-face induction route attacks the same parent objective through c-degree structure rather than branch pairing. Broader direct HCM0 exploration remains possible, but the branch route is now justified by a new exact all-m carrier that preserves the previously hidden cancellation data.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This isolates one falsifiable all-m theorem—the first dangerous genuine three-support coefficient—into a provenance-preserving finite-index signed-mass problem. It can be solved or killed independently and reused by later HCM0 work without carrying the full parent exploration."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP HCM0 extreme branch parity domination

Status: `READY / RESEARCHER-PUBLISHED CONTINUATION`

## 0. Mother question

Can the exact residue-dual signed branch formula for the first dangerous genuine three-support coefficient be converted into an all-`m` parity-domination theorem for the actual Perfect-Prime gaps
`M=m a`, `N=m(a+c)`, with `a,c>0`, so that the normalized relative trace exceeds the coalescent baseline `n=m-1`?

## 1. Frozen inputs and scope

Read the immutable HCM0 handoff index first and treat its all-`m` statements, finite-only evidence, and closed-route list as frozen boundaries. The primary input is the exact formula in `EXTREME_COEFFICIENT_SIGNED_BRANCH_BRC_REDUCTION_20260906.md`: every branch retains endpoint provenance, row labels, parity, positive beta/binomial magnitude, and a squared mixed-minor amplitude; the extreme coefficient is an inverse-free three-index alternating-square sum.

Use the actual synchronization `r0=mS`, `M=ma`, `N=m(a+c)`. Preserve the positive and negative parity populations separately. The exact `m=3,4,5,6` full-parameter trace theorems and the all-`m` positive tangent face are regression and structural input, not an all-`m` conclusion.

Do not reopen the already refuted arbitrary-shift, positive-real-spectrum, arbitrary-integer-shift, pointwise-discriminant, P-matrix, or termwise branch-positivity mechanisms unless genuinely new information changes their exact counterexample boundary.

## 2. Hard target and required outputs

Hard target: `M7_EXTREME_BRANCH_PARITY_DOMINATION_PROVED_OR_EXACTLY_OBSTRUCTED`.

Required output is one of the following at theorem strength:

1. An explicit pairing, involution, finite-difference summation, beta-ratio inequality, or other exact comparison proving the oriented parity-mass domination for every `m>=2`, `S>=0`, `a,c>0`.
2. An equivalent proof that the normalized trace
   `tr(H_(a+c)^(-1) H_a) > m-1`
   holds for every actual three-layer base slice.
3. The first exact actual-gap obstruction to that inequality, with deterministic exact certificate and a clear explanation of which finite certificates remain valid.

A positive proof must show how the Vandermonde-integral amplitudes and beta-weight ratios interact; generic positivity of the secant frame is insufficient. State precisely what the theorem proves about the extreme mixed coefficient and what remains open for other three-support coefficients and HCM0.

## 3. Research value to preserve

The parent exploration already converted an opaque signed determinant into a labeled branch space on which cancellation provenance is explicit. Solving this parity comparison would be the first all-`m` theorem for a genuinely three-support extreme mixed coefficient beyond the two-shift theorem and would give a reusable sign-comparison mechanism for the HCM0 route. Killing it would be equally valuable because it would prevent the strong low-dimensional polynomial pattern from being mistaken for a uniform law.

## 4. Success, kill, and return criteria

Success is an all-`m` exact parity-domination theorem or an equivalent exact extreme-trace theorem under the actual block synchronization. A negative terminal result is the first exact actual configuration where the normalized trace fails the required inequality, together with an exact certificate.

Kill any argument that substitutes finite tables for uniform proof, assumes every signed branch is positive, derives coefficient signs from real spectrum, or discards parity provenance by summing only positive mass. If the branch carrier proves insufficient, return the smallest missing invariant or exact obstruction rather than broadening to unrelated matrix routes.

The parent HCM0 objective remains open unless the returned theorem is separately proved to control every required HCM0 cell.
