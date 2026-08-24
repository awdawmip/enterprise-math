<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043C3-UNOCCUPIED-COMPONENT-FRONTIER-CONNECTIVITY",
  "title": "R043-C3 Unoccupied-Component Frontier Connectivity",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Decide whether every connected component Omega of the unoccupied FCC/HCP graph has a connected current frontier slice F(C)∩Omega for every finite connected occupied cluster C, thereby deciding whether connected components of abstract G0 exactly identify dynamically independent unoccupied components.",
  "next_action": "Prove the frontier-connectivity property from the frozen FCC/HCP local contact/link structure, or freeze the smallest exact counterexample and test whether its disconnected visible frontier pieces are future-interacting under addition. Do not extend naive G0 animal census before resolving this grouping gate.",
  "dependencies": [
    {"target":"R043-C2 owner head a2aaaece1fcdea23f799b73728bb628b7d72bfa5 / PR #623","action":"CONSUME","satisfied":true},
    {"target":"R043-C1 owner head 018dbcc3ee68862af0d834683b20d6211eed1192 / PR #621","action":"CONSUME","satisfied":true},
    {"target":"R043 owner head 566babdb8008db901f8bd057c01a24412cc1495a / PR #532","action":"CONSUME","satisfied":true},
    {"target":"R039 frozen FCC/HCP contact models","action":"CONSUME","satisfied":true}
  ],
  "source_refs": [
    "research_returns/R043C2_G0_FUTURE_SUFFICIENCY_MODULO_SHIELDED_COMPONENTS_RETURN_20260824.md@a2aaaece1fcdea23f799b73728bb628b7d72bfa5",
    "research_artifacts/R043C2_g0_future/RESULTS.json@a2aaaece1fcdea23f799b73728bb628b7d72bfa5",
    "driver_reviews/R043C2_COMPONENT_FACTORIZATION_AND_C3_FRONTIER_CONNECTIVITY_DRIVER_REVIEW_20260824.md"
  ],
  "evidence_status": "COMPLEMENT_COMPONENT_FACTORIZATION_PROVED_FRONTIER_GROUPING_GATE_OPEN",
  "last_progress_ref": "R043-C2: addition-only dynamics factors over current unoccupied connected components; G0 grouping inside one component remains open",
  "last_progress_at": "2026-08-24T14:03:00+08:00",
  "hard_block": null,
  "tags": ["R043C3","native-surface","G0","unoccupied-components","frontier-connectivity","latent-interaction","rigidity"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R043C3",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-R043C2-G0-FUTURE-SUFFICIENCY-MODULO-SHIELDED-COMPONENTS",
  "successor_gate": {
    "new_information_gap": "C2 proves exact factorization of addition-only surface dynamics over connected components of the unoccupied graph. It does not prove that the visible frontier slice of one unoccupied component is connected in G0. If one unoccupied component can contain several disconnected visible G0 pieces, G0 may forget future-relevant grouping even before connected-frontier embedding rigidity is considered.",
    "why_parent_result_does_not_close_it": "Component independence only applies after the true unoccupied-component partition is fixed. Abstract G0 exposes graph components but does not a priori label which disconnected visible pieces belong to the same deeper unoccupied component. This is exactly the remaining grouping ambiguity isolated by C2.",
    "discriminating_outcomes": [
      "frontier slice connected for every unoccupied component in both FCC and HCP, so G0 components exactly identify dynamic components",
      "property proved in FCC but false/open in HCP",
      "property proved in HCP but false/open in FCC",
      "smallest native counterexample found and its disconnected frontier pieces are future-interacting",
      "counterexample exists but disconnected pieces are nevertheless future-equivalent under addition, requiring a finer quotient",
      "problem reduced to a finite local-link obstruction theorem with exact unresolved pattern"
    ],
    "kill_condition": "Do not report arbitrary disconnected G0 as a counterexample unless the pieces are proved to lie in the same unoccupied component. Stop generic digital-topology abstraction if it has no FCC/HCP-specific theorem content. Do not confuse graph connectivity of the entire complement with connectivity of its current frontier slice.",
    "alternative_route_or_free_exploration_considered": "Larger same-G0 animal enumeration was rejected because it mixes harmless independent-component relocation with the unresolved grouping mechanism. Connected-frontier collision search was deferred until this grouping gate is decided. The connectivity theorem/counterexample is the smallest structural discriminator left by C2.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "C2 reached an exact global factorization theorem and isolated a new prior obstruction. C3 has a binary structural target whose positive resolution removes an entire ambiguity class and whose negative resolution supplies a concrete latent-interaction geometry for the G0 stationarity problem."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R043-C3 — Unoccupied-Component Frontier Connectivity

Status: `READY / P1 / CONTINUATION / NOT CANONICAL`

## 0. Mother question

For finite connected occupied `C`, let `Omega` be any connected component of the unoccupied graph `Lambda\C` and define

`F_Omega = F(C) intersect Omega`.

Decide exactly:

> Is the induced native contact graph on `F_Omega` always connected in frozen FCC and HCP?

If yes, connected components of current `G0` coincide exactly with unoccupied components and C2's component-grouping ambiguity disappears.

If no, freeze the smallest exact counterexample and determine whether the disconnected visible pieces can later interact under addition.

## 1. Do not weaken or change the question

The claim is not:

- that `Lambda\C` is connected;
- that all of `F(C)` is connected;
- that every cavity is simply connected;
- that Euclidean/topological boundary is smooth or connected.

It is only the graph-connectivity of the **current frontier slice belonging to one fixed unoccupied component**.

## 2. Structural proof route

Use the frozen native contact graphs only.

Potential proof ingredients to pressure-test rather than assume:

- connectivity / higher connectivity of the native link graph of one FCC/HCP cell;
- how frontier replacement behaves under adding/removing one occupied cell;
- local rerouting of an unoccupied path toward the occupied interface;
- cycle/link consistency around tetrahedral/octahedral close-packed cells;
- minimal separator patterns in the unoccupied component.

Any local-link lemma must be proved for the actual FCC and HCP neighbor relations separately.

## 3. Counterexample route

Search directly for a finite connected occupied `C` and one unoccupied component `Omega` with

`G[F(C) intersect Omega]`

disconnected.

A valid machine witness must certify:

1. `C` finite and connected;
2. the reported frontier pieces lie in the same connected component `Omega` of `Lambda\C`;
3. there is no frontier edge joining those pieces;
4. the same-`Omega` connection uses deeper currently non-frontier unoccupied cells;
5. exact FCC/HCP native adjacency only.

If found, immediately test additions on the visible pieces to determine the first horizon at which their latent common-component geometry becomes observable.

## 4. Finite complement certification

Because `Lambda\C` is infinite, a counterexample must not rely on an arbitrary bounding-box BFS that could misclassify the infinite exterior.

Acceptable exact certificates include:

- an explicit unoccupied path connecting the two frontier pieces, together with direct proof that both are in the same component;
- for finite cavities, an explicit finite void set whose occupied neighbor shell closes it;
- a symbolic/local construction whose connectivity is evident from listed native paths.

A positive global proof must not be inferred from bounded boxes or finite samples.

## 5. Consequence if positive

If every `F_Omega` is connected, then C2-T1 yields a bijection

`{unoccupied components Omega_i} <-> {connected components of G0}`.

Combined with C2-T3, the addition-only future factorizes over **visible G0 connected components**. Relative native placement among different G0 components can then be quotiented permanently.

The only remaining G0 stationarity obstruction is rooted successor-extension ambiguity **inside one connected weighted frontier graph**.

## 6. Consequence if negative

If one `Omega` can expose several disconnected `G0` pieces, abstract `G0` may forget whether two visible pieces are dynamically independent or are linked through deeper unoccupied cells.

The next collision construction should pair:

- one realization where matching visible pieces belong to distinct unoccupied components;
- another where they belong to the same `Omega`;
- exact same abstract weighted `G0`;
- a matched action orbit that exposes the hidden distinction.

This would be the cleanest route to a real stationary-G0 failure.

## 7. Mandatory controls

- C1 single shielded cavity: separate `G0` component and separate unoccupied component — must pass.
- Multiple sealed cavities: each remains a distinct future-independent component — must pass.
- Random/exhaustive positive samples are diagnostics only.
- Do not treat a path through occupied vertices as unoccupied connectivity.
- Do not use Euclidean closeness in place of native adjacency.

## 8. FCC/HCP separation

Return FCC and HCP verdicts separately. The inherited HCP frozen-symmetry completeness caveat is irrelevant to a direct adjacency/path counterexample unless symmetry minimality is claimed.

## 9. Required return

Freeze:

1. exact theorem/counterexample statement;
2. FCC disposition;
3. HCP disposition;
4. structural proof or explicit native witness/path certificate;
5. first future consequence for `G0` grouping;
6. bounded diagnostics, clearly non-theorem;
7. the exact remaining mother obstruction.

## 10. Terminal classifications

- `FRONTIER_COMPONENT_EQUALS_UNOCCUPIED_COMPONENT_BOUNDARY_PROVED_FCC_AND_HCP`;
- `FRONTIER_CONNECTIVITY_PROVED_FCC_ONLY`;
- `FRONTIER_CONNECTIVITY_PROVED_HCP_ONLY`;
- `FRONTIER_CONNECTIVITY_KILLED_BY_NATIVE_COUNTEREXAMPLE`;
- `NEGATIVE_BUT_GROUPING_FUTURE_SAFE`;
- `REDUCED_TO_LOCAL_LINK_SEPARATOR_LEMMA`;
- `OPEN_WITH_EXACT_CONNECTIVITY_OBSTRUCTION`.

No Foundation or canonical-main consequence follows automatically from the return.
