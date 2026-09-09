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
  "task_id": "RS-EMF6D046-R106-TWO-ADIC-HERMITIAN-UNITARY",
  "title": "P46 2-adic integral Hermitian unitary automorphism group",
  "frontier": "R105 reduces the remaining principalization ambiguity to the full non-scalar unitary automorphism group of the rank-two integral Hermitian lattice at the unramified 2-adic CM place. Scalar units, Frobenius data, Newton/EO data, scalar orders, and the C3 ring-class defect are exhausted and do not decide the three-line orbit.",
  "next_action": "Recover the exact rank-two integral Hermitian lattice and Gram/module data underlying R105, enumerate its full unitary automorphism group, and compute the induced permutation action on the three nonzero F4 principalization lines. Decide exactly whether the image is trivial or C3 and certify the result.",
  "dependencies": [],
  "source_refs": [
    "research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md",
    "research-branch:research/em-free-f6d046-ramanujan-period-wronskian-20260904@574f53c7b37ae6703ade390df851d8822af6364c",
    "research_notes/EM_FREE_F6D046_LATEST_FRONTIER_R105_20260904.md"
  ],
  "evidence_status": "FREE_RESEARCH_R105_DURABLE_HANDOFF",
  "last_progress_ref": "research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:21:00+08:00",
  "hard_block": "FULL_TWO_ADIC_HERMITIAN_UNITARY_ORBIT",
  "tags": ["EM-FREE-F6D046", "P46", "2-adic", "Hermitian-lattice", "unitary", "principalization", "F4", "C3"],
  "registry_key": "RS-EMF6D046-R106-TWO-ADIC-HERMITIAN-UNITARY",
  "identity_lane": "RF6D106",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# P46 2-adic integral Hermitian unitary automorphism group

Status: `READY / R105 STATE-MACHINE INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

For the R105 Prym principalization frontier, what is the exact full non-scalar unitary automorphism group `U(L)` of the rank-two integral Hermitian lattice at the unramified two-adic CM place, and how does it act on the three nonzero principalization lines in `L^#/L ≅ F4`?

## 1. Frozen inputs and scope

Read `research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md` first. It pins the R1–R105 evidence branch, the six-file minimal reading order, and the scope corrections.

Consume rather than replay these frozen facts: the scalar-unit image on `F4^x` is trivial; the ring-class defect is `C3`; `F tensor Q2` has an unramified quadratic factor with residue field `F4`; the Prym polar kernel is integrally `O_unr/2 O_unr`; and selecting a line lowers the scalar local order to `Z2+2 O_unr`.

This task is local/integral. It must preserve the distinction between local lattice equivalence and global ppav isomorphism. It grants no new axiom, foundation status, Working Truth, or theorem promotion.

## 2. Hard target and required outputs

Hard target: `FULL_TWO_ADIC_HERMITIAN_UNITARY_ORBIT`.

Deliver all of the following, or an exact underdetermination certificate replacing an impossible item:

1. Recover and state an exact Gram matrix/module model for `L`, with coefficient order, involution, and dual lattice.
2. Enumerate or classify the full `U(L)`, not merely scalar units.
3. Compute the induced homomorphism `U(L) -> S3` on the three nonzero `F4` principalization lines.
4. Decide exactly whether the image is `1` or `C3`; give exact generators when nontrivial.
5. Produce machine-checkable evidence sufficient for a replacement researcher to reproduce the group and orbit computation.
6. If R105 does not determine `L` uniquely, identify the smallest missing integral datum and exhibit two admissible lattices with different outcomes whenever possible.

## 3. Research value to preserve

R105 exhausts Frobenius polynomials, rational endomorphism algebras, Newton/EO data, scalar CM units, scalar order and scalar center information. The full non-scalar Hermitian automorphism group is therefore the first remaining invariant capable of deciding whether the three local principalizations are genuinely distinct before the global theta problem is attempted.

An exact `U(L)` computation either collapses the local ambiguity or proves that a real global distinction survives. An exact underdetermination result is equally valuable because it identifies the missing integral carrier rather than hiding it behind a heuristic `C3` symmetry.

## 4. Success, kill, and return criteria

Success is an exact group/action theorem with a reproducible lattice model and certified permutation action, or an exact proof that the available R105 data do not determine that action.

Kill any route that infers the full unitary action from scalar units, Teichmuller heuristics, floating-point matrix recognition, or the mere existence of a local `C3`. Do not choose an implicit Gram matrix when the evidence does not force it.

Return the exact group/action theorem or the smallest additional integral datum required to continue.
