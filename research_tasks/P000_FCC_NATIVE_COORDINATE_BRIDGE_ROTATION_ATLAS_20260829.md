<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-FCC-NATIVE-COORDINATE-BRIDGE-ROTATION-ATLAS",
  "title": "P000 FCC 六轴原生坐标桥与旋转换图图册",
  "kind": "RESEARCH",
  "owner": "research/p000-fcc-native-coordinate-bridge-rotation-atlas",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "With FCC selected by direct user criterion as the primary coordinate carrier, construct the exact typed bridge from native positive axes E_1,...,E_6 to the six FCC carrier line families and the four overlapping 120-degree slice charts, including rotation/transition rules without quotienting native six-dimensional state by classical carrier relations.",
  "next_action": "Freeze the six FCC line families and four slice-incidence triples, define native-axis-to-carrier-family typing plus chart-local orientation data, then classify legal coordinate transport and rotation transitions and test exact reconstruction/ambiguity of native addresses under the carrier readout.",
  "dependencies": [
    "p000_reality_foundation.json@main",
    "definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md@main",
    "driver_reviews/P000_FIRST_SHELL_POLYHEDRON_DRIVER_REVIEW_AND_COORDINATE_SELECTION_20260829.md@main"
  ],
  "source_refs": [
    "research_returns/P000_FIRST_SHELL_POLYHEDRON_CLASSIFICATION_RETURN_20260829.md@main",
    "research_tasks/P000_6D_AXIS_MIXING_ROTATION_GROUPOID_20260829.md@main"
  ],
  "evidence_status": "DRIVER_ACCEPTED_FIRST_SHELL / USER_SELECTED_FCC_PRIMARY_COORDINATE_CARRIER / NATIVE_CARRIER_BRIDGE_OPEN",
  "last_progress_ref": "driver_reviews/P000_FIRST_SHELL_POLYHEDRON_DRIVER_REVIEW_AND_COORDINATE_SELECTION_20260829.md",
  "last_progress_at": "2026-08-29T03:12:30+00:00",
  "hard_block": null,
  "tags": ["P000","FCC","coordinate-carrier","six-axis","120-degree-slice","rotation","atlas","native-bridge"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-FCC-NATIVE-COORDINATE-BRIDGE-ROTATION-ATLAS",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000FCC",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-FIRST-SHELL-POLYHEDRON-CLASSIFICATION",
  "successor_gate": {
    "new_information_gap": "The carrier classification is closed and FCC is now selected as the primary coordinate carrier, but there is not yet an exact typed map from native positive axes to the six FCC line families or an exact transition calculus across the four overlapping 120-degree slice charts.",
    "why_parent_result_does_not_close_it": "The first-shell task deliberately stopped at the carrier/native boundary. The coordinate-carrier selection is a design decision, not a theorem identifying native states with FCC vectors.",
    "discriminating_outcomes": [
      "Construct an exact native-axis/FCC-line bridge with chart transitions and rotation action that preserves six-dimensional native identity.",
      "Construct a relation/groupoid-valued bridge if a single global orientation assignment is impossible.",
      "Prove the exact obstruction and identify the additional native incidence datum required for a global coordinate atlas."
    ],
    "kill_condition": "Any bridge that reduces the native dimension by classical carrier rank, identifies v and -v as primitive native axes, treats carrier kernel collisions as native equality, or silently restores a three-dimensional world ontology does not close the task.",
    "alternative_route_or_free_exploration_considered": "Using HCP as primary carrier was considered and rejected by the direct user criterion because HCP requires stacking/basis state and lacks central first-shell symmetry. Leaving FCC only as a visualization was rejected because the user explicitly requested selection of one working coordinate system.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The finite FCC/HCP shell classification is terminal and should remain immutable. The unresolved object is now a different mathematical type: a native-to-carrier coordinate atlas and rotation transition law."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 FCC 六轴原生坐标桥与旋转换图图册

Status: `PUBLISHED_REGISTERED / P000-BOUND / CONTINUATION / FCC-PRIMARY-CARRIER`

## Mother question

Given the user-directed current convention that FCC is the primary coordinate carrier, what is the exact native-to-carrier coordinate atlas relating the six positive native axes `E_1,...,E_6` to the six FCC nearest-neighbor line families and the four overlapping three-axis `120 degree` slices, and how do rotations transport coordinates between those slices without collapsing six-dimensional native identity?

## Frozen inputs and scope

P000 is unconditional: six native spatial dimensions plus one time dimension, discrete Cell space, rotation as the primary spatial operation, and three-axis geometry as a research slice.

Freeze the current coordinate-carrier convention:

`P000_PRIMARY_COORDINATE_CARRIER=FCC_CUBIC_BARLOW`.

Use the six unoriented carrier line families

`L1=[(1,1,0)]`, `L2=[(1,-1,0)]`, `L3=[(1,0,1)]`, `L4=[(1,0,-1)]`, `L5=[(0,1,1)]`, `L6=[(0,1,-1)]`.

Use the four carrier slice-incidence triples

`S_A={L1,L3,L6}`,

`S_B={L1,L4,L5}`,

`S_C={L2,L3,L5}`,

`S_D={L2,L4,L6}`.

The line families are classical carrier objects. `[v]={v,-v}` is not a primitive native point/axis equivalence. Chart-local sign choices used to realize `120 degree` are carrier orientations only.

HCP must remain a regression carrier for detecting any accidental derivation of six native axes from twelve carrier contacts.

## Hard target and required outputs

Hard target: `P000_FCC_NATIVE_SIX_AXIS_ROTATIONAL_COORDINATE_ATLAS_EXACTLY_CLASSIFIED`.

Required outputs:

1. define the native six-axis address/state object used by the atlas without reducing it by FCC linear relations;
2. define the exact typed correspondence between native axis labels and FCC carrier line families, including whether the correspondence is a function, a chart-dependent relation, or a groupoid object;
3. define chart-local orientation data for each of the four `120 degree` slice types and exact transition maps on overlaps;
4. classify the rotation action on the six line families and four slices, including composition and stabilizers at the weakest exact strength available;
5. show how the established `E_1,E_2,E_3` slice embeds into one declared chart and how rotations expose other axes/slices;
6. determine the carrier-readout kernel and prove that carrier collisions do not become native-state equality;
7. give an exact coordinate-continuity criterion for translation and rotation transport;
8. retain HCP non-central symmetry as a regression guard;
9. provide a deterministic checker/certificate for the finite line/slice/rotation incidence claims.

## Research value to preserve

The selected FCC carrier is useful because its coordinate frame can be transported without an `AB` stacking bit and because its six stable line families form an overlapping rotational slice atlas. The important innovation is not the classical FCC lattice itself; it is the attempt to use one translation-consistent finite carrier to organize six native dimensions while preserving the distinction between native state and lower-dimensional readout.

The four overlapping three-axis slices are especially important: they replace the earlier disconnected two-block picture by a connected atlas in which rotations can move through shared axis families.

## Success, kill, and return criteria

Success requires an exact typed six-axis coordinate atlas with legal rotation/transition rules and a proof-level boundary between native identity and FCC carrier readout.

Kill any construction that:

- reduces six native dimensions to classical rank three;
- identifies carrier antipodes as primitive native negative axes;
- assumes one fixed global carrier orientation makes all four slice triples pairwise `120 degree` without checking chart transitions;
- treats a many-to-one FCC readout as native equality;
- imports a continuous `SO(3)`/`SO(6)` geometry as native truth;
- drops the HCP regression guard;
- merely relabels the previous two-block `C_2` model without constructing the four-slice overlap structure.

If no single global orientation assignment exists, return the strongest exact chart/groupoid formulation rather than forcing one.
