<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "EM-FREE-F6D046-RAMANUJAN-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-EMF6D046-R108-HONDA-TATE-CORRESPONDENCE-REDUCTION",
  "title": "P46 explicit Honda-Tate projector correspondence and reduction stratification",
  "frontier": "R105 gives a rational rank-one idempotent in M2(F), an explicit genus-two realization B ~ Jac(C7) over F49, C6 strictification data, and a characteristic-zero U(4) semidirect C2 Sato-Tate structure. The missing object is an explicit low-bidegree algebraic correspondence and a theorem that organizes these reduction phenomena without confusing isogeny, polarization, or automorphism decompositions.",
  "next_action": "Construct an algebraic correspondence over F49 that realizes a rank-one Honda-Tate projector from the special P46 factor to the explicit genus-two Jacobian, minimizing bidegree when possible. Then state and prove the strongest reduction-stratification theorem relating the F49 square decomposition, C6 strictification, C3 principalization carrier, and characteristic-zero component structure.",
  "dependencies": [],
  "source_refs": [
    "research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md",
    "research-branch:research/em-free-f6d046-ramanujan-period-wronskian-20260904@574f53c7b37ae6703ade390df851d8822af6364c"
  ],
  "evidence_status": "FREE_RESEARCH_R105_PARALLEL_RESIDUE",
  "last_progress_ref": "research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:21:00+08:00",
  "hard_block": "EXPLICIT_PROJECTOR_CORRESPONDENCE_AND_REDUCTION_STRATIFICATION",
  "tags": ["EM-FREE-F6D046", "P46", "Honda-Tate", "correspondence", "F49", "genus2", "reduction", "stratification"],
  "registry_key": "RS-EMF6D046-R108-HONDA-TATE-CORRESPONDENCE-REDUCTION",
  "identity_lane": "RF6D108",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# P46 explicit Honda-Tate projector correspondence and reduction stratification

Status: `READY / R105 PARALLEL INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

Can the rank-one idempotents in `End^0_F49(P46,7) ≅ M2(F)` be realized by an explicit low-bidegree algebraic correspondence tied to the explicit genus-two factor, and what exact reduction-stratification theorem organizes this finite-field splitting together with the `C2`, `C3`, and `C6` carriers already proved?

## 1. Frozen inputs and scope

Read `research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md` first and use the pinned R1–R105 evidence branch.

Frozen inputs include the explicit genus-two realization `B ~ Jac(C7)` over `F49`, the square decomposition `P46,F49 ~ B^2`, the non-descent of rank-one idempotents to `F7`, the `C6` strictification datum, the `C3` principalization carrier, and the characteristic-zero unitary component structure.

Tate existence of a rational correspondence is not an explicit low-bidegree cycle. Honda-Tate square splitting is not a new curve-automorphism quotient. Algebraic Sato-Tate component data do not by themselves prove analytic equidistribution.

## 2. Hard target and required outputs

Hard target: `EXPLICIT_PROJECTOR_CORRESPONDENCE_AND_REDUCTION_STRATIFICATION`.

1. Give a cycle/correspondence over `F49` whose induced homomorphism realizes one rank-one Honda-Tate projector, preferably directly between the special `C46` geometry and the explicit genus-two curve `C7`.
2. Prove the induced map on Jacobians or Tate modules and state its degree/bidegree exactly.
3. Explain descent/non-descent to `F7` and its relation to Frobenius swapping the two rank-one idempotents.
4. Integrate the `C2`, `C3`, and `C6` carriers with the characteristic-zero unitary component structure without identifying logically distinct notions.
5. State the strongest precise reduction-stratification theorem with explicit hypotheses and scope.

## 3. Research value to preserve

R105 has already supplied the rational endomorphism algebra and the explicit isogeny factor, but the geometric carrier of a rank-one projector is still missing. Constructing it would connect finite-field Honda-Tate data back to curve geometry and give a reusable model for distinguishing isogeny, polarization, descent, and automorphism phenomena.

An exact obstruction is also valuable if it determines the minimum degree, extension field, or correspondence complexity forced by the descent structure.

## 4. Success, kill, and return criteria

Success is an explicit certified correspondence plus a scoped reduction-stratification theorem.

Kill any route that turns abstract Tate existence into an explicit cycle without construction, identifies the square splitting with a new special-fiber automorphism quotient, or claims analytic Sato-Tate equidistribution from algebraic component information alone.

Return the correspondence/theorem pair or an exact degree/descent obstruction that explains why the requested explicit realization cannot occur at the attempted level.
