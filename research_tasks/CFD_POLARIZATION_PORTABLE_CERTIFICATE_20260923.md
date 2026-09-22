<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CFD-POLARIZATION-PORTABLE-CERTIFICATE-20260923",
  "title": "Portable raw-preserving polarization certificate",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Real and complex noncollinear two-mode stationary families are completely classified. Same signed support and modal energies do not determine projected output. Full contraction-menu reconstruction is supplied; inclusion-minimal sufficient subsets for raw R, sigma and projection remain unclassified. Parent R23 benchmark remains open.",
  "next_action": "Use the supplied same-support/energy fiber witness to reject the empty menu. Resolve one unclassified contraction deletion from the full eight-field menu by uniform factorization proof or exact same-observer/different-output fiber. Return the proved subset/domain, certificate and next unresolved subset; do not repeat full-menu reconstruction.",
  "dependencies": [],
  "source_refs": [
    "research_artifacts/CFD_POLARIZATION_SUPPORT_20260923/PROOF.md",
    "research_artifacts/CFD_POLARIZATION_SUPPORT_20260923/portable_problem.json",
    "research_artifacts/CFD_POLARIZATION_SUPPORT_20260923/certificate.json"
  ],
  "evidence_status": "DIRECT_USER_ALGEBRA_AND_INTEGER_CHECKS_NOT_PARENT_ACCEPTANCE",
  "last_progress_ref": "research_artifacts/CFD_POLARIZATION_SUPPORT_20260923/PROOF.md",
  "last_progress_at": "2026-09-22T21:03:50.348310+00:00",
  "hard_block": null,
  "tags": [
    "CFD",
    "BRC",
    "polarization",
    "portable-certificate"
  ],
  "claim_lease_minutes": 120,
  "identity_lane": "CFDPOLAR",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-CFD-SPECTRAL-HYBRID-20260910",
  "successor_gate": {
    "new_information_gap": "The complete two-mode family and full-data reconstruction do not classify which subsets of eight fixed contractions determine raw R, sigma and projection, nor exact fiber witnesses for essential fields.",
    "why_parent_result_does_not_close_it": "R23 gives measurement-error cost bounds; it does not implement the polarization observer or complete the frozen native benchmark.",
    "discriminating_outcomes": "A proved factorization through a strictly reduced observer, or an exact same-observer/different-output fiber proving a deletion impossible; ultimately inclusion-minimal sufficient subsets.",
    "kill_condition": "Reject alias or missing retention presented as full scope, lost conjugacy, magnitude-only substitution, projected-only evidence, input drift and resource stops interpreted as stationarity.",
    "alternative_route_or_free_exploration_considered": "Reuse the proved algebraic family and existing BRC interface; higher-mode classification and repeated real/complex two-mode derivations are outside this bounded support target.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This self-contained interface proof can be delivered independently of the parent native benchmark while preserving its actual lineage and open status."
  },
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CFD-POLARIZATION-PORTABLE-CERTIFICATE-20260923",
  "parent_objective_id": "OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "policy_review": {
    "temporary_overrides": [],
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS"
  }
}
-->

# Portable polarization certificate preserving the raw CFD interface

## Mother question

Which inclusion-minimal subsets of the fixed contraction-field menu below,
together with wavevectors and modal energies, determine raw Vortex R, sigma
and projection for every valid two-mode field? Prove factorization through
each sufficient observer and provide exact same-observer/different-output
counterexamples for essential fields. A portable certificate consumer is the
evidence carrier; the target is mathematical sufficiency and minimality.

## Frozen inputs and scope

Use the complete compact contract in portable_problem.json and PROOF.md at
research_artifacts/CFD_POLARIZATION_SUPPORT_20260923. Let k,l be noncollinear
integer vectors, A,B complex rational vectors with k dot A=l dot B=0. Negative
modes have conjugate amplitudes. The full retained signed support contains
both cross-frequency pairs; there is no alias. These are auxiliary CFD Fourier
labels, not the native six spatial axes. P000 is unconditional.

For every ordered pair p+q=m use the complex bilinear rule
i[q(u_p dot u_q)-(q dot u_p)u_q]. For nonzero m retain sigma=(m dot R)/|m|^2
and P_m R=R-m sigma, and check the zero mode directly. Single modes and two
common-normal modes have zero projected output. For other stationary fields
U=|k|^2=|l|^2, n=k cross l, s=k dot l, Delta=U^2-s^2, and exactly
A=alpha(U l-s k+i tau n)/Delta, B=beta(U k-s l-i tau n)/Delta, with nonzero
complex alpha,beta and real tau. This complete classification is supplied;
its derivation is not an open item. Rational inputs have rational parameters.

The source raw interface and static carrier are reused, including the actual
same-support/same-energy counterexample. The R23 measurement-error frontier
remains the latest consumed parent frontier and native 32^3 benchmarking
remains open. A symbolic counterexample or certificate is not that benchmark.

Freeze this finite menu: Jk=A dot A, Jl=B dot B, S=A dot B, T=A dot conj(B),
X=(A dot l)B, Y=(B dot k)A, Z=(A dot l)conj(B), W=(conj(B) dot k)A.
The base observer always retains k,l and modal energies A dot conj(A),
B dot conj(B). A menu item is its full exact complex scalar/vector value.
Seek inclusion-minimal subsets of these eight named items, not an unconstrained
encoding that simply stores the answer. Uniform results quantify over all
noncollinear k,l and valid complex rational A,B. Any restricted-domain result
must declare its exact extra premises.

The full menu is already sufficient via R_(2k)=i k Jk, R_(2l)=i l Jl,
R_(k+l)=i[(k+l)S-X-Y], R_(k-l)=i[(k-l)T+Z-W], negative modes by conjugacy
and R_0=0. Projection and sigma follow directly. Do not present this immediate
full-data reconstruction alone as the result. The open content is which
contractions can be omitted uniformly and the fiber witnesses for lost data.

## Hard target and required outputs

Determine the inclusion-minimal sufficient observers within the menu, or resolve
one genuine deletion with a proof or exact fiber counterexample and retain a
precise map of open deletions. Prove that retained data determine all three
outputs simultaneously. Bind observer, domain and output in an exact portable
certificate. Distinguish raw-zero from projected-zero and preserve a nonzero
coefficient witness. Invalid contracts and resource limits are distinct.

Start with the supplied same-support/energy fiber witness, which already rejects
the empty menu. Then address one unclassified contraction deletion from the full
menu. Deliver one complete mathematical increment and its exact next unresolved
subset. Reuse existing BRC arithmetic;
do not invent another arithmetic family. Pure proof or any exact implementation
is allowed. Fully preserve signs, phases and ordered multiplicity.

## Research value to preserve

Positive energy/support observers miss a demonstrated polarization distinction.
This consumer makes the proved refinement usable without discarding the raw
gradient information required by the existing API. It closes a concrete gap
between an exact family proof and trustworthy interface replacement; it does
not repeat the original classification or pretend a local test is a native
benchmark. A future performance experiment can consume this certificate.

## Success, kill, and return criteria

Success is the complete minimal-observer classification, or a verified strict
new sufficiency/minimality increment with an unresolved subset map. The consumer
carries the mathematical claim and rejects false-zero/altered fields. An exact
same-observer/different-output fiber is a valid negative result. Implementing
all original amplitudes or restating full-menu reconstruction is insufficient.

Kill aliasing or missing retention silently treated as full retention; lost
conjugacy; replacing bilinear amplitudes by magnitudes; returning only projected
zero; or accepting tampered raw/sigma bindings. Native arithmetic materialization
must follow current BRC policy. Resource exhaustion cannot mean stationary.
Return exact files, commands if used, proof and input bindings, all actual
checks and remaining limitations. Parent benchmark, Driver Acceptance and
global Foundation statuses are not changed by this support task.
