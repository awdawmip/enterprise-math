<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-X6-NONFCC-SLICE-REALIZATION",
  "title": "Native realization of the sixteen non-FCC three-axis selections",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "All 20 three-axis coordinate selections are native X6 observers/subtorsors, but only four FCC/K4 STAR selections have the complete overlapping-circle carrier realization. The other sixteen lack a native rotation/path realization audit and any carrier classification.",
  "next_action": "Use the intrinsic triadic signed-C6 generator and X6 BRC path lift on every three-axis subtorsor, then classify which additional selections admit any carrier realization without importing FCC star relations.",
  "dependencies": [
    {"target":"ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905","action":"CONSUME","satisfied":true},
    {"target":"ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905","action":"CONSUME","satisfied":true},
    {"target":"RS-X6-NATIVE-ROTATION-DYNAMICS","action":"CONSUME_PARTIAL","satisfied":false}
  ],
  "source_refs": [
    "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md",
    "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md"
  ],
  "evidence_status": "20_NATIVE_SELECTIONS_4_FCC_REALIZED_16_OPEN",
  "last_progress_ref": "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
  "last_progress_at": "2026-09-05T11:53:48Z",
  "hard_block": null,
  "tags": ["X6","three-axis","non-FCC","rotation","carrier","observer"],
  "claim_lease_minutes": 120,
  "created_by_role": "FREE_RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-X6-NONFCC-SLICE-REALIZATION",
  "parent_objective_id": "PO-X6-UPPER-STRUCTURE-20260906",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "X6U",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": null,
  "successor_gate": "DIRECT_USER_UPPER_STRUCTURE_ATTACK_AFTER_X6_SPATIAL_FOUNDATION_CLOSED",
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:fbe51ab884e1267b7bb6de0de598ad5504fd0d67d1570475115a9a16a6ec4ca0","review_state":"PASS","temporary_overrides":[]}
}
-->

# RS-X6-NONFCC-SLICE-REALIZATION

Status: `PUBLISHED_REGISTERED / CLAIMABLE / DIRECT_USER_DIRECTION`

## Mother question

Which structures on the sixteen non-FCC three-axis X6 selections are intrinsically native, and which parts of the familiar three-axis geometry depend specifically on the FCC/K4 carrier realization?

## Hard target

- Construct intrinsic signed C6/C12 Cell microcycles where possible using only X6 adjacency and rotation, not carrier angles.
- Classify the 20 selections under the strongest currently justified rotation group and compare with the old `4 STAR + 4 FACE + 12 PATH` S4 carrier orbit split.
- Determine which circle/gate/overlap statements are carrier-specific, which lift natively, and which require a new carrier.
- Give explicit counterexamples to any silent promotion from coordinate selection to realized slice.

## Hard boundaries

A coordinate observer is not automatically a physical carrier slice. Native X6 results may be stronger than carrier availability, but carrier geometry must not be invented to match them.
