<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043C1-NATIVE-SLOT-COMPLETION-G0-INJECTIVITY",
  "title": "R043-C1 Native Slot Completion and G0 Injectivity",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Decide whether the forgetful map from the stationary native slot-cut carrier K_partial to the abstract weighted current-frontier graph G0 is globally injective on finite connected reachable FCC/HCP interfaces, or produce and classify the first realizable non-equivalent completion.",
  "next_action": "Construct a native slot-completion solver from abstract weighted G0, separate local incidence feasibility from slot-transition consistency and global cluster realizability, then either extract the weakest rigidity lemma forcing a unique K_partial completion or freeze a realizable same-G0/different-K_partial collision and its future consequence.",
  "dependencies": [
    {
      "target": "R043 owner head 566babdb8008db901f8bd057c01a24412cc1495a",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "R041 owner head 688661e76255b3e86df6d5c69695f2932b650740",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "R039 owner head c484fb85385b8498982aaa939171957588c836d7",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "current finite-symmetry / graph-isomorphism / constraint-search toolbox",
      "action": "TEST",
      "satisfied": true
    }
  ],
  "source_refs": [
    "research_artifacts/R043_native_surface_frontier/CHECKPOINT.md",
    "research_artifacts/R043_native_surface_frontier/RESULTS.json",
    "research_artifacts/R043_native_surface_frontier/frontier_reconstruction.py",
    "driver_reviews/R043_RETURN_RECOVERY_AND_C1_SUCCESSOR_DRIVER_REVIEW_20260824.md"
  ],
  "evidence_status": "GLOBAL_NATIVE_SLOT_COMPLETION_RIGIDITY_OR_REALIZABLE_COLLISION_GATE",
  "last_progress_ref": "R043 recovered checkpoint: stationary K_partial proved; pi:K_partial->G0 globally open",
  "last_progress_at": "2026-08-24T13:04:00+08:00",
  "hard_block": null,
  "tags": ["R043C1","native-surface","slot-completion","G0","injectivity","embedding-rigidity","counterexample"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R043C1",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-R043-NATIVE-SURFACE-FRONTIER-RECONSTRUCTION-MARKOV-CARRIER",
  "successor_gate": {
    "new_information_gap": "R043 proves a fixed-form stationary native slot-cut carrier K_partial and bounded injectivity of the abstract weighted frontier graph G0 through the complete frozen N<=8 FCC/HCP atlases, but leaves global injectivity of the forgetful map pi:K_partial->G0 unproved and without a realizable collision.",
    "why_parent_result_does_not_close_it": "The parent proves that retaining native inward-slot identity is sufficient and stationary. It does not show that this identity is reconstructible from the abstract weighted frontier graph. Bounded singleton G0 classes cannot replace a global reconstruction theorem, and absence of bounded collisions does not prove injectivity.",
    "discriminating_outcomes": [
      "native slot completion is uniquely forced for every reachable G0 in FCC and HCP, proving global injectivity of pi",
      "global injectivity is proved for one frozen world but a realizable collision or open obstruction remains in the other",
      "two non-equivalent globally realizable K_partial completions with the same G0 are constructed, killing global injectivity",
      "local completion is nonunique but all surviving completions are future-equivalent at the declared surface language",
      "the problem is reduced to an exact finite propagation/rigidity lemma whose unresolved obstruction is strictly smaller than arbitrary cluster enumeration"
    ],
    "kill_condition": "Stop the route if a current owner already proves or kills pi injectivity, if the only surviving problem is generic graph embedding/CSP machinery with no FCC/HCP-specific theorem content, or if a proposed alternative completion satisfies only weight equations but fails native slot consistency or finite-connected-cluster realizability.",
    "alternative_route_or_free_exploration_considered": "More animal enumeration was considered and rejected as the default because the parent already exhausts the frozen N<=8 atlas with zero G0 collisions. Generic quotient/BRC continuation was rejected because it cannot supply the missing native embedding rigidity. The completion route attacks the exact hidden information discarded by pi.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent question about existence of a compact stationary carrier is already answered positively by K_partial. Reopening it would repeat settled work. This continuation isolates the one remaining forgetful-map injectivity question and has independent proof, collision, one-world split, and reduction outcomes."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R043-C1 — Native Slot Completion and G0 Injectivity

Status: `READY / P1 / CONTINUATION / NOT CANONICAL`

## 0. Mother question

The frozen parent establishes a fixed-form stationary native carrier

`K_partial = current coherently embedded frontier + inward occupied native contact slots`.

Its forgetful image

`G0 = surface scalar + abstract weighted induced current-frontier graph`

erases slot/embedding identity.

The complete frozen finite atlas has no same-`G0` collision through `N<=8` in either FCC or HCP, but this is finite evidence only.

This task asks exactly:

> Is `pi: K_partial -> G0` globally injective, up to the declared native symmetry / future-equivalent relabeling, on every finite connected reachable interface?

Do not reopen the already-settled question whether a stationary carrier exists.

## 1. Three completion layers must remain distinct

For an abstract weighted `G0`, distinguish:

1. `LOCAL_INCIDENCE_FEASIBLE` — per-frontier inward-slot choices merely reproduce the node weights;
2. `NATIVE_SLOT_CONSISTENT` — local choices glue across frontier contacts under the frozen FCC/HCP slot-transition law;
3. `GLOBALLY_REALIZABLE` — the completion is the exact boundary of a finite connected occupied cluster and creates no undeclared frontier cells.

Only layer 3 gives a competing `K_partial` state.

A balance solution at layer 1 is a negative control, not a collision certificate.

## 2. Primary attack — rooted native slot completion

Start from one abstract weighted frontier graph and one rooted action/frontier vertex.

Build completion by:

- assigning one native local slot frame at the root modulo the local point stabilizer;
- propagating frontier-edge slot constraints to adjacent vertices;
- enforcing each vertex weight as the number of inward occupied slots;
- identifying slot targets that must coincide as the same ambient cell;
- rejecting assignments that create forbidden frontier adjacencies or inconsistent target identities;
- quotienting equivalent completions by native world symmetry and weighted-frontier automorphisms.

Do not store a hidden coordinate embedding as free data. Any embedding used by the solver is a witness to a completion and must be quotiented by the declared symmetry.

## 3. Global realizability gate

For every locally consistent completion, test whether there exists a finite connected occupied set `C` such that:

- its current frontier is exactly the reconstructed frontier;
- its inward slots are exactly the proposed `I_C(x)`;
- no proposed inward target is exterior;
- no omitted exterior target is adjacent to an occupied cell;
- the occupied component is finite and connected.

If local slot equations admit multiple completions but all but one fail this gate, record that as a rigidity mechanism rather than a counterexample.

## 4. Two proof routes

### A. Rigidity route

Extract progressively stronger lemmas:

- local link rigidity from weighted rooted frontier neighborhoods;
- edge-to-edge frame propagation;
- cycle consistency / holonomy closure of native slot frames;
- uniqueness of inward/outward classification after global frontier completeness;
- uniqueness of the finite occupied component behind the reconstructed cut.

A complete theorem may combine these, but each lemma should be pressure-tested separately in FCC and HCP.

### B. Collision route

If two non-equivalent completions survive global realizability, freeze the smallest available pair `C,D` with

`G0(C) ~= G0(D)`

but

`K_partial(C) !~= K_partial(D)`.

Then determine the weakest semantic split:

- different successor `G0` under matched action orbit;
- different `B_h` for the smallest horizon;
- or no difference in the declared Boolean future despite different slot completions.

The last outcome kills injectivity without automatically killing future sufficiency.

## 5. Separate abstract-graph and native-embedding questions

A useful decomposition is:

`abstract weighted G0`
`-> native embedded frontier`
`-> inward-slot completion`
`-> finite occupied component`.

Do not claim a single black-box reconstruction theorem when only one arrow is proved.

If the first arrow is the only hard step, freeze that reduction explicitly. If the embedded frontier plus weights uniquely determines the inward component, prove that separately.

## 6. Mandatory bounded regression, not search target

Use the frozen `N<=8` no-collision atlas as a regression surface for the completion solver:

- every realized `G0` in the bounded atlas must recover the known `K_partial` completion up to declared symmetry;
- no solver-created second completion may be reported unless global realizability is independently checked;
- bounded replay is validation of the solver, not the main research result.

Do not increase the animal ceiling merely because the solver has not yet proved rigidity.

## 7. Owner/tool boundary

Reuse current finite-symmetry, graph-isomorphism and constraint-search capabilities when adequate. The task owns only the native FCC/HCP completion theorem/counterexample and its exact consequence for `pi`.

Generic graph embedding, generic constraint solving, future-safe quotient and branch recoalescence remain prior/upstream machinery.

If tool reuse exposes a semantic bug in the frozen slot model, report the bug and stop the affected claim rather than patching around it.

## 8. Required return

Freeze:

1. exact completion variables and constraints;
2. local/native/global completion distinction;
3. FCC and HCP dispositions separately;
4. proof lemmas or the smallest realizable collision;
5. action-rooted successor consequence;
6. bounded regression matrix against the frozen atlas;
7. tool/method ownership classification;
8. weakest supported statement about `pi`.

## 9. Terminal classifications

Return one primary verdict:

- `PI_GLOBAL_INJECTIVITY_PROVED_FCC_AND_HCP`;
- `PI_GLOBAL_INJECTIVITY_PROVED_FCC_ONLY`;
- `PI_GLOBAL_INJECTIVITY_PROVED_HCP_ONLY`;
- `PI_INJECTIVITY_KILLED_BY_REALIZABLE_COLLISION`;
- `PI_NONINJECTIVE_BUT_BOOLEAN_FUTURE_EQUIVALENT_AT_TESTED_SCOPE`;
- `EMBEDDING_RIGIDITY_REDUCED_TO_EXACT_FINITE_PROPAGATION_LEMMA`;
- `OPEN_WITH_EXACT_SLOT_COMPLETION_OBSTRUCTION`.

No Foundation or canonical-main consequence follows automatically from the return.
