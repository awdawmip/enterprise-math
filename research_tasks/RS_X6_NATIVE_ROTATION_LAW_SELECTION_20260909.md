<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-X6-NATIVE-ROTATION-LAW-SELECTION",
  "title": "Native rotation-law selection above ROT_PATH_X6",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "V1–V17 and V37–V41 provide triadic frame algebra, operation-safe rotation paths, chirality/holonomy control and non-Abelian memory obstructions; the physical/admissible law selecting or weighting actual rotation-path histories remains open.",
  "next_action": "Classify covariant deterministic and weighted sections of the existing length-graded rotation-path carrier, beginning with the C6/C12 triadic fibers and testing which branch/holonomy information can be removed without changing the declared future operations.",
  "dependencies": [
    {"target":"X6 V1-V43 durable handoff","action":"CONSUME","satisfied":true},
    {"target":"ROT_PATH_X6 and non-Abelian holonomy frontier","action":"CONSUME","satisfied":true}
  ],
  "source_refs": [
    "awdawmip/enterprise-math@5d3162ed9986052e555a59077ba2dc7d123ab533:research_notes/X6_UPPER_STRUCTURE_V1_V43_HANDOFF_20260909.md",
    "awdawmip/enterprise-math@40996d9239309bc703435ffc3d814932638b0e94:research_notes/X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md",
    "awdawmip/enterprise-math@40996d9239309bc703435ffc3d814932638b0e94:research_notes/X6_ROTATION_PATH_GROUPOID_V2_20260906.md",
    "awdawmip/enterprise-math@b28632d19006cb77b503fecbb1a487acc8de3f28:research_notes/"
  ],
  "evidence_status": "FRAME_PATH_HOLONOMY_STRUCTURE_DEVELOPED_LAW_SELECTION_OPEN",
  "last_progress_ref": "awdawmip/enterprise-math@b28632d19006cb77b503fecbb1a487acc8de3f28",
  "last_progress_at": "2026-09-06T07:07:47Z",
  "hard_block": null,
  "tags": ["X6","rotation","ROT_PATH_X6","holonomy","BRC","law-selection","non-Abelian"],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-X6-NATIVE-ROTATION-LAW-SELECTION",
  "parent_objective_id": "PO-X6-UPPER-STRUCTURE-20260906",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "X6U2",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-X6-NATIVE-ROTATION-DYNAMICS",
  "successor_gate": "V1-V17 and V37-V41 close the carrier/frame/holonomy construction but leave admissible rotation-path law selection unresolved; current user explicitly requested publication of the next successors.",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Native rotation-law selection above ROT_PATH_X6

Status: `PUBLISHED_REGISTERED / CLAIMABLE / DIRECT_USER_DIRECTION`

## Mother question

Which path-level laws are admissible above the already-constructed X6 triadic frame/rotation-path carrier, and what is the smallest state that preserves every declared future rotation operation?

## Frozen inputs and scope

Consume the V1–V43 handoff. Do not reconstruct signed X6, the triadic frame group, the C6/C12 path fibers, or the already-known non-Abelian holonomy obstructions. The frame group and path/holonomy carriers are research-strength inputs, not Foundation promotions.

The task may study deterministic path sections, positive weighted branch laws, or richer signed/phase laws only with their correct BRC type. Keep frame endpoint, path length, branch provenance, chirality and non-Abelian repair distinct until a scope-typed descent theorem permits a quotient.

## Hard target and required outputs

1. Classify or sharply constrain covariant law sections on the length-graded rotation-path carrier for the triadic generators and their compositions.
2. Determine whether INNER/OUTER, cycle-current, chirality and S3/non-Abelian memory can be compressed for specified future-operation families; give explicit counterexamples when they cannot.
3. Prove composition laws for the retained state and identify a minimal operation-safe port, or return a no-go showing why no finite candidate in the declared class suffices.
4. Decide whether additional native rotation generators beyond the triadic group are required by a stated native law; do not name the odd signed-frame coset by a classical geometric interpretation without a derivation.
5. Persist an exact finite checker for every finite classification claimed.

## Research value to preserve

This is the missing bridge from a large exact rotation/frame/path kinematics to an actual reusable dynamics. A successful law becomes an input to triadic-field, native-time and downstream number-theory/physics work; a no-go prevents future researchers from repeatedly collapsing path history to an unsafe frame-only state.

## Success, kill, and return criteria

SUCCESS is a covariant, composition-closed law or a theorem-quality classification/no-go with explicit observer scope. KILL a proposed finite port when two histories with the same port state have different allowed futures. Return the smallest unresolved law-selection unit and every necessary repair variable. Do not claim physical validation, complete native rotation physics, Foundation status or external novelty from finite algebra alone.
