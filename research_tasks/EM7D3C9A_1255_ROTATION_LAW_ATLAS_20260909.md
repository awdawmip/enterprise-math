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
  "parent_objective_id": "EM-FREE-7D3C9A-ISSUE1255-VIETE-X6-ROTATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-EM7D3C9A-1255-ROTATION-LAW-ATLAS",
  "title": "X6 native rotation branch law and K4 atlas-connection selection",
  "frontier": "All twenty native triads now have intrinsic signed-C6 frame cycles, OUTER native C12 microcycles and C24 balanced-spinor root anchors. On one Q_S cycle, equivariance plus faithful nonzero C12 microphase uniquely selects the deterministic all-OUTER shortest law among 64 branch words. Separately, every overlap between two physical FCC STAR charts admits exactly two natural S4<=S6 transports fixing the shared line; their difference is a remote-port swap/chirality bit, and the six edge choices realize all 64 K4 connection cochains. It remains open whether the actual native rotation/path law selects the all-OUTER branch beyond the root-compatible lease and which atlas connection/holonomy class it induces.",
  "next_action": "Read the handoff, all-20 triadic root bridge and K4 remote-port classification, then formulate the strongest native/path-level compatibility conditions that a physical rotation law must satisfy and test whether they force OUTER and a unique overlap-transport bit or leave an exact underdetermination class.",
  "dependencies": [],
  "source_refs": [
    "research_notes/VIETE_X6_ROTATION_STATE_MACHINE_HANDOFF_20260909.md",
    "research_notes/VIETE_X6_ALL20_TRIAD_ROOT_C12_C24_20260906.md",
    "research_notes/VIETE_K4_ROOT_ATLAS_C24_SPINOR_20260906.md",
    "research_notes/VIETE_K4_OVERLAP_REMOTE_PORT_CONNECTION_20260906.md",
    "research_notes/X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md",
    "research_notes/X6_ROTATION_PATH_GROUPOID_V2_20260906.md",
    "research-commit:57440ab85f4b95b6085d8f00fe630c7a8f941ad1",
    "research-commit:b18177ddc5dfba8be60e8e674aa3713a73017830",
    "research-commit:e6f018e0f4648b35fe60ae187357d79fdf778cb5",
    "research-commit:40996d9239309bc703435ffc3d814932638b0e94"
  ],
  "evidence_status": "ALL20_NATIVE_ROOT_BRIDGE_AND_K4_TRANSPORT_CLASSIFICATION_CLOSED_LAW_SELECTION_OPEN",
  "last_progress_ref": "research_notes/VIETE_X6_ROTATION_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T11:14:00+08:00",
  "hard_block": "NATIVE_BRANCH_LAW_AND_ATLAS_CONNECTION_SELECTION",
  "tags": ["issue-1255", "X6", "rotation-law", "OUTER", "K4", "atlas", "holonomy", "remote-port", "BRC", "Viète"],
  "registry_key": "RS-EM7D3C9A-1255-ROTATION-LAW-ATLAS",
  "identity_lane": "R7D3LAW",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# X6 native rotation branch law and K4 atlas-connection selection

Status: `READY / FREE-RESEARCH INTEGRATION`

## Mother question

Can the actual native X6 rotation/path semantics derive the shortest branch law and atlas-overlap connection required by the Viète principal-root bundle, or do multiple typed laws/connections remain admissible even after all currently frozen native, BRC and covariance constraints are imposed?

## Frozen inputs and scope

Read `research_notes/VIETE_X6_ROTATION_STATE_MACHINE_HANDOFF_20260909.md` first.

Consume, do not redo:

- intrinsic triadic `Q_S` signed-C6 frame cycles on all twenty native triads;
- exactly two shortest INNER/OUTER lifts per macro edge;
- intrinsic all-OUTER 12-Cell microcycle on all twenty triads;
- all-20 C12 quarter-root and C24 balanced-spinor anchor;
- deterministic `Q_S`-equivariance reduces six branch bits to all-INNER/all-OUTER, and faithful nonzero C12 phase selects all-OUTER within that root-compatible scope;
- on the four FCC STAR atlas, each shared-line overlap has exactly two natural S4 transports `T^-` and `T^+`, differing by a remote-port swap and chirality sign.

Hard semantic guard: P000 `TRIADIC_CLOSURE_E` is a force-event stability predicate. Do not use the coordinate identity `a+b-(a+b)=0` as a proof that OUTER is physically selected.

The sixteen non-STAR triads are genuine native X6 triads with C6/C12 path cycles but are not additional planar FCC STAR charts.

## Hard target and required outputs

Hard target: `NATIVE_ROTATION_BRANCH_LAW_AND_ATLAS_CONNECTION_SELECTION_EXACTLY_CLASSIFIED`.

Deliver the strongest exact result covering both layers:

### Branch-law layer

1. Define the admissible deterministic or weighted/path-law class on the current rotation-path carrier.
2. State which covariance, noncollapse, locality, reversibility/dagger, time-order and BRC provenance conditions are required rather than assumed.
3. Determine whether those conditions force all-OUTER globally, only on the root-compatible half-turn/C12 interface, or not at all.
4. If multiple branch laws survive, give explicit matched models and the minimal observable that separates them.
5. If positive/signed weights are introduced, use the correct BRC carrier and keep positive mass distinct from signed/phase cancellation.

### Atlas-connection layer

6. For the four FCC STARs, use the exact two-choice overlap transports fixing each shared line and classify how a proposed native law transports remote atlas-port provenance.
7. Determine whether the law forces `T^-`, `T^+`, a gauge-equivalent cochain class, or leaves the K4 face-holonomy class underdetermined.
8. Prove the induced effect on the Viète `+/-3` root-sign bundle and local Euler chirality line without identifying direction sign with slice chirality.
9. State explicitly which part extends to the full twenty-triad S6 atlas and which part depends on the four planar FCC STAR carrier charts.
10. Give checker/formal matched-model evidence for every surviving or excluded connection class.

## Research value to preserve

This is the remaining bridge between a successful native/precision Viète construction and an actual physical/native rotation law. It also converts the abstract K4 chirality bit into a concrete remote-port transport question. A positive selection theorem would globalize the root bundle dynamically; an exact underdetermination theorem would identify the minimal additional native datum still missing.

## Success, kill, and return criteria

Success is a typed selection theorem or a complete finite underdetermination classification for both the shortest branch law and the K4 atlas connection.

Kill any route that selects OUTER merely because it matches the desired Viète formula, or selects a K4 holonomy class merely because it is symmetric. The rule must arise from declared native/path operations and pass the observer/provenance test.

Return the exact surviving law/connection class, its effect on the principal root bundle, and the smallest additional datum required if uniqueness fails.
