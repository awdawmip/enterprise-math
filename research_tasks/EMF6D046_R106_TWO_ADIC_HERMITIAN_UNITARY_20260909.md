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

## 0. Entry point

Read `research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md` first. It points to the exact R105 evidence branch and the minimal read order. Consume the frozen R1–R105 chain; do not replay it.

## 1. Hard target

Determine the full non-scalar unitary automorphism group `U(L)` of the rank-two integral Hermitian lattice `L` at the unramified two-adic CM place and its action on the three principalization lines in `L^#/L ≅ F4`.

Required outputs:

1. Recover and state an exact Gram matrix/module model for `L`, with its coefficient order and involution.
2. Enumerate or classify the full `U(L)`, not merely scalar units.
3. Compute the induced homomorphism `U(L) -> S3` on the three nonzero `F4` lines.
4. Decide exactly whether the image is `1` or `C3`; give generators when nontrivial.
5. Produce machine-checkable evidence sufficient for a replacement researcher to reproduce the group and orbit computation.
6. Preserve the distinction between local lattice equivalence and global ppav isomorphism.

## 2. Frozen facts

The scalar-unit image is already trivial; the ring-class defect is `C3`; `F tensor Q2` has an unramified quadratic factor with residue field `F4`; selecting a principalization line lowers the scalar local order to `Z2+2 O_unr`. These facts are inputs, not targets.

## 3. Kill boundary

Do not infer the full unitary action from scalar units, Teichmuller heuristics, numerical matrix recognition, or the existence of a local `C3`. If the exact R105 data do not determine `L` uniquely, freeze the missing integral datum as an exact obstruction instead of choosing an implicit lattice.

## 4. Return criterion

Return an exact group/action theorem or an exact underdetermination certificate identifying the smallest additional integral datum needed. This task grants no new axiom, foundation status, Working Truth, or theorem promotion.
