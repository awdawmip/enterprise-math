<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE",
  "title": "R043-C4 Native Interface Link-Separator Closure",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Prove or refute the exact FCC/HCP native interface-to-frontier connectivity lemma isolated by R043-C3, thereby deciding whether one unoccupied connected component can expose multiple disconnected visible G0 frontier pieces.",
  "next_action": "Do not expand naive animal census. Build the exact FCC and HCP local site-link/interface incidence cases. Either prove that every connected occupied/unoccupied interface lifts to a connected chain of unoccupied frontier sites under 12-contact, with a valid global glue argument, or freeze the first exact native local separator pattern and lift it to a finite connected C,Omega counterexample.",
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
  "evidence_status": "GLOBAL_GROUPING_GATE_REDUCED_TO_NATIVE_LOCAL_LINK_SEPARATOR",
  "last_progress_ref": "R043-C3: no counterexample in exact U=N[D] thick-void family through FCC core N<=8 / HCP core N<=7; global theorem reduced to native local link/interface incidence",
  "last_progress_at": "2026-08-24T14:12:00+08:00",
  "hard_block": null,
  "tags": ["R043C4","native-surface","FCC","HCP","interface","link-graph","separator","frontier-connectivity","G0"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R043C4",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-R043C3-UNOCCUPIED-COMPONENT-FRONTIER-CONNECTIVITY",
  "successor_gate": {
    "new_information_gap": "C3 isolates the sole prior grouping question to a native local incidence lift: connected topological/interface incidence does not automatically imply connected frontier-site 12-contact incidence. This finite local bridge is now the theorem-critical gap.",
    "why_parent_result_does_not_close_it": "C3 bounded pressure is not a global proof, and its Mayer-Vietoris/topological glue route still needs an exact FCC/HCP combinatorial bridge from interface incidences to frontier-site contacts. Without that bridge, G0 component grouping remains unresolved.",
    "discriminating_outcomes": [
      "native interface-to-frontier connectivity proved in both FCC and HCP",
      "proved in FCC only",
      "proved in HCP only",
      "exact local separator pattern found and lifted to a finite C3 counterexample",
      "local separator exists but cannot be globally realized with finite connected occupied C",
      "problem reduced to an explicit finite list of unresolved FCC/HCP link configurations"
    ],
    "kill_condition": "Stop any route that merely enlarges the animal census, invokes continuum connectedness without the native incidence lift, or creates a generic digital-topology framework. A negative local pattern is not theorem-useful until native realizability is certified.",
    "alternative_route_or_free_exploration_considered": "Further global G0 collision search was rejected because C3 identifies a logically prior grouping gate. Larger U=N[D] pressure was rejected as proof strategy. The local link/interface problem is finite, falsifiable, and directly determines whether the grouping ambiguity exists at all.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "C3 reached its terminal reduction classification. C4 owns a narrower finite local incidence theorem/counterexample with different evidence requirements and a direct yes/no consequence for the stationary G0 program."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R043-C4 — Native Interface Link-Separator Closure

Status: `READY / P1 / CONTINUATION / NOT CANONICAL`

## 0. Exact target

C3 left one local lemma:

> For frozen FCC/HCP close-packed native incidence, can a connected interface between one connected unoccupied component `Omega` and its connected complementary side correspond to more than one connected component of unoccupied frontier sites under the original 12-contact graph?

Prove `NO`, or freeze an exact `YES` pattern and lift it to a finite connected occupied-cluster counterexample.

## 1. Purely discrete route

Assume a minimal counterexample `C,Omega` with disconnected `F_Omega`.

Take a shortest native unoccupied path in `Omega` between two visible frontier components. Its strict interior vertices have no occupied neighbor, otherwise they would themselves be frontier and shorten the witness.

At the first departure from one frontier component and last arrival to another, enumerate the exact local occupancy/unoccupancy constraints in the 12-neighbor link.

The theorem obligation is to show that the frozen FCC/HCP link graph always provides a frontier-site rerouting chain, or else isolate the exact separator subset that prevents such a chain.

Do not infer this from link connectivity alone: occupied/non-frontier labels constrain which link vertices are admissible.

## 2. Native cell-interface route

An alternative exact route may define the close-packed cell/star thickening associated to the frozen contact graph and use connected-interface topology as the global glue.

Required steps:

1. define the FCC and HCP local cell incidence exactly;
2. prove graph-connected occupied/unoccupied site sets give connected thickenings at the required scale;
3. prove the chosen `Omega` side and complementary side form the intended connected cover;
4. prove their common interface is connected by an accepted topological argument;
5. prove every transfer of interface connectivity through a face/edge/vertex incidence can be lifted locally to a chain of **unoccupied frontier sites that are 12-contact adjacent**.

Step 5 is the theorem-critical native lemma. Steps 1–4 do not replace it.

## 3. Finite local certificate

Whether proving or refuting, produce an auditable finite local incidence table/certificate separately for FCC and HCP.

For a positive proof, the table must cover every local interface transition type needed by the global glue. For a negative result, it must list the exact neighboring site pattern and show:

- local occupied/unoccupied consistency;
- the two interface pieces are connected through native cell incidence;
- no frontier 12-contact chain exists locally;
- the pattern is not eliminated by the actual FCC/HCP link constraints.

## 4. Global realizability gate for a negative pattern

A local separator pattern is not enough. Lift it to explicit finite sets or prove a symbolic family with:

- finite connected occupied `C`;
- a connected unoccupied component `Omega`;
- at least two disconnected components in `F(C) intersect Omega`;
- an explicit native unoccupied path joining them;
- exact absence of frontier-frontier paths between them.

Then route immediately back to C2 and test whether the hidden same-`Omega` grouping changes a rooted successor future.

## 5. Mandatory regressions

- C1 singleton-cavity control remains a separate unoccupied component.
- C2 component-factorization theorem must remain intact.
- C3 exact `U=N[D]` pressure counts are regression-only and must not be reinterpreted as proof.
- FCC and HCP are separate obligations.

## 6. Forbidden shortcuts

Do not:

- increase generic animal N as the primary route;
- replace native adjacency by Euclidean distance thresholds;
- claim connected continuum boundary implies connected G0 without the local lift;
- import a generic digital-topology framework as a substitute for the exact close-packed link cases;
- promote any result to Foundation automatically.

## 7. Required return

Freeze:

1. exact FCC link/interface disposition;
2. exact HCP link/interface disposition;
3. finite local incidence certificate/table or separator witness;
4. global glue argument or explicit finite realizability lift;
5. exact consequence for C3 frontier connectivity;
6. exact consequence for C2/G0 component grouping;
7. weakest remaining obstruction after this task.

## 8. Terminal classifications

- `NATIVE_INTERFACE_FRONTIER_CONNECTIVITY_PROVED_FCC_AND_HCP`;
- `NATIVE_INTERFACE_FRONTIER_CONNECTIVITY_PROVED_FCC_ONLY`;
- `NATIVE_INTERFACE_FRONTIER_CONNECTIVITY_PROVED_HCP_ONLY`;
- `LOCAL_SEPARATOR_LIFTED_TO_GLOBAL_FRONTIER_COUNTEREXAMPLE`;
- `LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`;
- `FINITE_LINK_CASES_REMAIN`;
- `OPEN_WITH_EXACT_NATIVE_INCIDENCE_OBSTRUCTION`.

No Foundation or canonical-main consequence follows automatically from this return.
