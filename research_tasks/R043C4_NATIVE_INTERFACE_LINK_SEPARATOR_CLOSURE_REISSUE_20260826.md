<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE",
  "title": "R043-C4 Native Interface Link-Separator Closure — Current-Policy Reissue",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Prove or refute the exact FCC/HCP native interface-to-frontier connectivity lemma isolated by R043-C3, thereby deciding whether one connected unoccupied component can expose multiple disconnected visible G0 frontier pieces.",
  "next_action": "Build the exact FCC and HCP local site-link/interface incidence cases. Either prove that every connected occupied/unoccupied interface lifts to a connected chain of unoccupied frontier sites under native 12-contact with a valid global glue argument, or freeze the first exact native local separator and lift it to a finite connected occupied/unoccupied counterexample.",
  "dependencies": [
    "research_returns/R043C3_UNOCCUPIED_COMPONENT_FRONTIER_CONNECTIVITY_RETURN_20260824.md@49877b834c4f15e7f30cb54f03ba5f106dba0342",
    "research_returns/R043C2_G0_FUTURE_SUFFICIENCY_MODULO_SHIELDED_COMPONENTS_RETURN_20260824.md@a2aaaece1fcdea23f799b73728bb628b7d72bfa5",
    "R039 frozen FCC/HCP contact-link models"
  ],
  "source_refs": [
    "research_tasks/R043C4_NATIVE_INTERFACE_LINK_SEPARATOR_CLOSURE_20260824.md#blob=1e425bfc7f8179df4cfac25c27ac5c9c46e1f2a3",
    "research_returns/R043C3_UNOCCUPIED_COMPONENT_FRONTIER_CONNECTIVITY_RETURN_20260824.md@49877b834c4f15e7f30cb54f03ba5f106dba0342",
    "research_artifacts/R043C3_frontier_connectivity/RESULTS.json@49877b834c4f15e7f30cb54f03ba5f106dba0342",
    "driver_reviews/R043C3_LOCAL_LINK_REDUCTION_AND_C4_DRIVER_REVIEW_20260824.md@63f9c86a52bb1545b89903a8b204bc4b00041048"
  ],
  "evidence_status": "CURRENT_POLICY_REISSUE_OF_DRIVER_AUTHORIZED_UNEXECUTED_SUCCESSOR",
  "last_progress_ref": "R043-C3 reduced global grouping to the native FCC/HCP local interface-link separator gate",
  "last_progress_at": "2026-08-24T14:12:00+08:00",
  "hard_block": null,
  "tags": [
    "R043C4",
    "native-surface",
    "FCC",
    "HCP",
    "interface",
    "link-graph",
    "separator",
    "frontier-connectivity",
    "G0"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE",
  "parent_objective_id": "OBJ-R043-G0-STATIONARY-FUTURE-SUFFICIENCY-CLOSURE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R043C4",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-R043C3-UNOCCUPIED-COMPONENT-FRONTIER-CONNECTIVITY",
  "successor_gate": {
    "new_information_gap": "R043-C3 isolated the remaining grouping question to a native local incidence lift: connected interface incidence does not by itself imply connected frontier-site 12-contact incidence. The exact FCC/HCP local link bridge is the unresolved theorem-critical gap.",
    "why_parent_result_does_not_close_it": "R043-C3 supplied bounded exact pressure and a reduction, not a global proof. Its global route still requires an exact local bridge from interface incidences to admissible frontier-site contacts.",
    "discriminating_outcomes": [
      "native interface-to-frontier connectivity proved in both FCC and HCP",
      "proved in FCC only",
      "proved in HCP only",
      "exact local separator pattern lifted to a finite global frontier counterexample",
      "local separator exists but finite connected global realizability fails or remains open",
      "problem reduced to an explicit finite list of unresolved native link configurations"
    ],
    "kill_condition": "Stop any route that merely enlarges generic animal census, substitutes continuum connectedness for the native incidence lift, or builds a generic digital-topology framework instead of resolving the exact FCC/HCP link cases. A negative local pattern is not decisive until native finite realizability is certified.",
    "alternative_route_or_free_exploration_considered": "Further global G0 collision search and larger U=N[D] census were already considered and rejected as theorem strategy because C3 exposed the logically prior grouping gate. The local finite link/interface problem is the smallest discriminating route.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "R043-C3 reached a terminal reduction classification. C4 owns a narrower finite local incidence theorem/counterexample with distinct evidence requirements and a direct yes/no consequence for the remaining G0 component-grouping ambiguity."
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

Status: `PUBLISHED_REGISTERED / CURRENT-POLICY REISSUE / CONTINUATION`

## Mother question

For the frozen FCC/HCP close-packed native 12-contact incidence, if one unoccupied component `Omega` is connected and its occupied-side interface is connected in the exact native cell/interface sense, must the visible unoccupied frontier `F(C) intersect Omega` be connected under the original 12-contact graph?

The task must prove the implication at exact native scope or produce the first exact separator pattern and certify whether it lifts to a finite connected global counterexample.

## Frozen inputs and scope

Consume R043-C2 and R043-C3 as frozen predecessors. Preserve C2 component factorization and C3's reduction boundary. The C3 bounded `U=N[D]` census is regression evidence only and cannot be promoted into a global theorem.

FCC and HCP are separate obligations. Use only their exact native contact/link/incidence structures; do not replace adjacency by Euclidean distance thresholds.

The primary route is local and finite. For a minimal hypothetical counterexample, take a shortest unoccupied path in `Omega` between two disconnected frontier components. Interior vertices of such a shortest path have no occupied neighbor. At the first frontier departure and last frontier arrival, classify the exact occupancy constraints in the native 12-neighbor link and determine whether a frontier-site rerouting chain is forced.

A second allowed route may use native cell/star thickenings and a global interface glue argument, but any continuum/topological connectivity statement is insufficient unless every required interface transition is lifted back to a chain of 12-contact-adjacent unoccupied frontier sites.

## Hard target and required outputs

Hard target:

`R043C4_NATIVE_INTERFACE_LINK_SEPARATOR_EXACTLY_CLOSED_OR_REDUCED_TO_FINITE_NATIVE_OBSTRUCTION`.

Required outputs:

1. exact FCC local link/interface disposition;
2. exact HCP local link/interface disposition;
3. finite local incidence table/certificate or separator witness for each structure;
4. a valid global glue proof if positive, or an explicit finite realizability lift if negative;
5. exact consequence for the R043-C3 frontier-connectivity question;
6. exact consequence for the R043-C2/G0 component-grouping ambiguity;
7. weakest remaining obstruction, if any;
8. durable return `research_returns/R043C4_NATIVE_INTERFACE_LINK_SEPARATOR_CLOSURE_RETURN_20260826.md` and any task-local exact checker/certificate needed to support the verdict.

## Research value to preserve

R043-C1 already killed raw completion injectivity without killing future sufficiency, and R043-C2 proved factorization over distinct unoccupied components. R043-C3 then isolated the only remaining component-grouping mechanism to whether one connected unoccupied component can expose disconnected frontier pieces. C4 therefore decides whether that entire hidden grouping mechanism exists or disappears. Closing this local gate sharply reduces the stationary-G0 problem without another broad census.

## Success, kill, and return criteria

Success is one exact classification among:

- `NATIVE_INTERFACE_FRONTIER_CONNECTIVITY_PROVED_FCC_AND_HCP`;
- `NATIVE_INTERFACE_FRONTIER_CONNECTIVITY_PROVED_FCC_ONLY`;
- `NATIVE_INTERFACE_FRONTIER_CONNECTIVITY_PROVED_HCP_ONLY`;
- `LOCAL_SEPARATOR_LIFTED_TO_GLOBAL_FRONTIER_COUNTEREXAMPLE`;
- `LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`;
- `FINITE_LINK_CASES_REMAIN`;
- `OPEN_WITH_EXACT_NATIVE_INCIDENCE_OBSTRUCTION`.

A positive proof must contain the native local lift and cannot rely only on continuum boundary connectedness. A negative result must certify finite native realizability before it is allowed to refute the global frontier-connectivity statement.

Kill any route whose only progress is a larger generic animal census, a Euclidean-distance surrogate for native contact, or an unrelated general topology framework. Stop the task after the exact return is frozen; do not promote the result to Foundation automatically and do not open a broader R043 successor inside this task.
