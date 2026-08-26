<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE",
  "title": "R043-C4 Native Interface Link-Separator Closure",
  "kind": "RESEARCH",
  "owner": "research/r043c4-native-interface-link-separator-closure",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Prove or refute the exact FCC/HCP native interface-to-frontier connectivity lemma isolated by R043-C3, thereby deciding whether one unoccupied connected component can expose multiple disconnected visible G0 frontier pieces.",
  "next_action": "Build exact FCC and HCP local site-link/interface incidence cases; prove every admissible connected interface lifts to a frontier-site 12-contact chain, or freeze the first exact native separator and certify global realizability as a finite connected occupied/unoccupied counterexample.",
  "dependencies": [
    {"target":"R043-C3 owner head 49877b834c4f15e7f30cb54f03ba5f106dba0342 / PR #625","action":"CONSUME","satisfied":true},
    {"target":"R043-C2 owner head a2aaaece1fcdea23f799b73728bb628b7d72bfa5 / PR #623","action":"CONSUME","satisfied":true},
    {"target":"R039 frozen FCC/HCP contact/link models","action":"CONSUME","satisfied":true}
  ],
  "source_refs": [
    "research_returns/R043C3_UNOCCUPIED_COMPONENT_FRONTIER_CONNECTIVITY_RETURN_20260824.md@49877b834c4f15e7f30cb54f03ba5f106dba0342",
    "research_artifacts/R043C3_frontier_connectivity/RESULTS.json@49877b834c4f15e7f30cb54f03ba5f106dba0342",
    "driver_reviews/R043C3_LOCAL_LINK_REDUCTION_AND_C4_DRIVER_REVIEW_20260824.md"
  ],
  "evidence_status": "CURRENT_POLICY_REREVIEW_PASS__LEGACY_FRONTIER_MIGRATED_FOR_FIRST_EXECUTION",
  "last_progress_ref": "driver_reviews/R043C3_LOCAL_LINK_REDUCTION_AND_C4_DRIVER_REVIEW_20260824.md",
  "last_progress_at": "2026-08-26T14:10:00+08:00",
  "hard_block": null,
  "tags": ["R043C4","native-surface","FCC","HCP","interface","link-graph","separator","frontier-connectivity","G0"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE",
  "parent_objective_id": "OBJ-R043-STATIONARY-G0-COMPONENT-GROUPING-CLOSURE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R043C4",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-R043C3-UNOCCUPIED-COMPONENT-FRONTIER-CONNECTIVITY",
  "successor_gate": {
    "new_information_gap": "C3 isolates the sole prior grouping question to a native local incidence lift: connected topological/interface incidence does not automatically imply connected frontier-site 12-contact incidence. This finite local bridge remains theorem-critical and has not been executed under C4.",
    "why_parent_result_does_not_close_it": "C3 bounded pressure is not a global proof, and its topological glue route still needs an exact FCC/HCP combinatorial bridge from interface incidences to frontier-site contacts. Without that bridge, G0 component grouping remains unresolved.",
    "discriminating_outcomes": [
      "native interface-to-frontier connectivity proved in both FCC and HCP",
      "proved in FCC only",
      "proved in HCP only",
      "exact local separator pattern found and lifted to a finite C3 counterexample",
      "local separator exists but cannot be globally realized with finite connected occupied C",
      "problem reduced to an explicit finite list of unresolved FCC/HCP link configurations"
    ],
    "kill_condition": "Stop any route that merely enlarges the animal census, invokes continuum connectedness without the native incidence lift, or creates a generic digital-topology framework. A negative local pattern is not theorem-useful until native realizability is certified.",
    "alternative_route_or_free_exploration_considered": "Further generic G0 collision search and larger U=N[D] pressure were considered and rejected as proof strategy because C3 isolates a logically prior finite local grouping gate. Closure was considered and rejected because the global C3 theorem remains open. No later accepted result found in current-state review closes this specific FCC/HCP link-separator obligation.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "C3 reached its terminal reduction classification. C4 owns a narrower finite local incidence theorem/counterexample with different evidence requirements and a direct yes/no consequence for stationary G0 grouping; the task has never been executed, so migration rather than a new successor is the minimal action."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R043-C4 — Native Interface Link-Separator Closure

Status: `PUBLISHED_REGISTERED / CLAIMABLE / P1 / HIGH / CONTINUATION / NOT CANONICAL`

## Mother question

For the frozen FCC/HCP close-packed native incidence, let `C` be finite connected occupied sites and `Omega` one connected component of the unoccupied graph. Must

`F_Omega = F(C) intersect Omega`

be connected in the original native 12-contact graph?

Equivalently: can one connected unoccupied component expose more than one disconnected visible G0 frontier component?

C3 did not prove or refute this. It reduced the question to the exact local native interface/link-separator bridge `R043C3-L1`.

## Frozen inputs and scope

Use the accepted C3/C2 results and frozen R039 FCC/HCP contact/link models listed in task metadata. FCC and HCP are separate theorem obligations.

Do not use the old bounded `U=N[D]` census as a global proof. It is regression evidence only: C3 found no counterexample for all frozen-symmetry FCC connected cores through `|D|<=8` and HCP cores through `|D|<=7`.

Allowed proof routes:

1. purely discrete shortest-path/minimal-separator analysis in the actual native site links;
2. exact native cell/interface incidence plus a global connected-interface glue theorem, provided the final interface-to-frontier 12-contact lift is proved combinatorially.

Forbidden as substitutes for the target:

- enlarging generic animal enumeration;
- Euclidean distance-threshold adjacency;
- continuum boundary connectedness without the native incidence lift;
- generic digital-topology machinery that does not resolve the exact FCC/HCP cases.

## Hard target and required outputs

Prove or refute `R043C3-L1` separately for FCC and HCP.

A positive result must provide an auditable finite local incidence/link certificate covering every transition type used by the global glue.

A negative local separator must be lifted to, or accompanied by an exact proof about the possibility/impossibility of lifting to, finite sets with:

- finite connected occupied `C`;
- connected unoccupied component `Omega`;
- at least two disconnected components of `F(C) intersect Omega`;
- an explicit native unoccupied path joining them;
- exact absence of any frontier-frontier 12-contact path between them.

Required return must freeze:

1. FCC disposition;
2. HCP disposition;
3. local incidence certificate/table or separator witness;
4. global glue proof or realizability disposition;
5. consequence for C3 frontier connectivity;
6. consequence for C2/G0 component grouping;
7. weakest remaining obstruction.

## Research value to preserve

C2 already proves dynamics factorizes over true unoccupied components. C3 shows that identifying those components from visible G0 frontier connectivity is the remaining grouping gate and reduces that gate to a finite native link/interface problem. Closing C4 therefore decides whether G0 connected components faithfully encode true dynamic component grouping, or exposes the first exact local separator responsible for hidden grouping ambiguity.

## Success, kill, and return criteria

Freeze exactly one primary classification:

- `NATIVE_INTERFACE_FRONTIER_CONNECTIVITY_PROVED_FCC_AND_HCP`;
- `NATIVE_INTERFACE_FRONTIER_CONNECTIVITY_PROVED_FCC_ONLY`;
- `NATIVE_INTERFACE_FRONTIER_CONNECTIVITY_PROVED_HCP_ONLY`;
- `LOCAL_SEPARATOR_LIFTED_TO_GLOBAL_FRONTIER_COUNTEREXAMPLE`;
- `LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`;
- `FINITE_LINK_CASES_REMAIN`;
- `OPEN_WITH_EXACT_NATIVE_INCIDENCE_OBSTRUCTION`.

Success includes proof, exact counterexample, or a strict finite residual classification. Kill any route that turns back into unbounded animal census or substitutes continuum intuition for the native link lift.

No Foundation/canonical promotion follows automatically. Task completion returns to the R043 parent objective for a new successor-gate decision rather than opening C5 automatically.
