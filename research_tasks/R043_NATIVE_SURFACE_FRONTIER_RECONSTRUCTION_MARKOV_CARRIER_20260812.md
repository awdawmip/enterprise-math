<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R043-NATIVE-SURFACE-FRONTIER-RECONSTRUCTION-MARKOV-CARRIER",
  "title": "R043 Native Surface Frontier Reconstruction and Minimal Markov Carrier",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine whether the weighted current native frontier graph G0 already determines exact addition-only Boolean surface future on FCC/HCP; if not, isolate the first hidden exterior correlation and the smallest recursively executable residual strictly below the full one-layer exterior carrier where possible.",
  "next_action": "Starting from the frozen R041 M_h theorem candidate and its unresolved G0 diagnostic, independently kill or prove G0 -> B3, then localize the first L0-L1/shared-future-cell correlation debt and test the smallest recursively updateable repair before restoring full M3.",
  "dependencies": [
    {
      "target": "R041 PR #527 owner head 688661e76255b3e86df6d5c69695f2932b650740",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "R039 PR #524 owner head c484fb85385b8498982aaa939171957588c836d7",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "R044 PR #530 semantic impact matrix classifying R043-TB04 as UNRESOLVED_NEEDS_NEW_TASK",
      "action": "TEST",
      "satisfied": true
    },
    {
      "target": "R023/R023I future-safe quotient and BRC semantic core",
      "action": "CONSUME",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R041 PR #527: M_h=S+weighted induced graph on L0..L_{h-2} determines Boolean B_h and updates to child M_{h-1}; weighted-frontier-only G0 showed no bounded collision but remained unproved",
    "R039 PR #524: metric-free contact-cut surface algebra and correlation-debt counterexamples",
    "R044 PR #530: R043 stationary Markov/all-horizon carrier hypotheses remain unresolved after native-semantics backtest"
  ],
  "evidence_status": "CURRENT_POLICY_REVIEWED_ORPHAN_CONTINUATION / G0_RECONSTRUCTION_OR_MINIMAL_CORRELATION_DEBT_GATE",
  "last_progress_ref": "Driver orphan-frontier maintenance sweep 2026-08-24; R043 had no runtime CLAIM/return and remained unresolved after R044",
  "last_progress_at": "2026-08-24T09:48:00+08:00",
  "hard_block": null,
  "tags": [
    "R043",
    "native-surface",
    "frontier-graph",
    "Markov-carrier",
    "future-relative-precision",
    "correlation-debt",
    "shared-future-cell",
    "BRC",
    "orphan-recovery"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R043",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-R041-NATIVE-SURFACE-HORIZON-QUOTIENT-CALCULUS",
  "successor_gate": {
    "new_information_gap": "R041 proved/validated a horizon-indexed recursively executable carrier M_h and isolated a strictly stronger unresolved candidate: the weighted current-frontier graph G0 had no bounded collision in the tested FCC/HCP atlases, but no theorem established G0 -> B3 or recursive closure. The exact first hidden correlation, if G0 fails, also remains unknown.",
    "why_parent_result_does_not_close_it": "M_h sufficiency gives an upper bound that retains explicit L1..L_{h-2} exterior structure; it does not prove minimality and does not decide whether current frontier weights/adjacency already encode those omitted future cells. R041 explicitly left this as its next structural frontier.",
    "discriminating_outcomes": [
      "G0 is proved sufficient for B3 and recursively updateable, yielding a stationary/frontier-only theorem candidate",
      "an exact same-G0 different-B3 counterexample is found and the first missing pair/shared-future correlation is localized",
      "a strict repair below full M3 is proved sufficient and recursively updateable",
      "bounded lower-bound evidence shows no tested compact residual below the declared shared-future hypergraph is exact, narrowing the carrier frontier without claiming universal minimality"
    ],
    "kill_condition": "Stop or rehome the task if later current work already proves/kills G0, if the surviving statement is entirely a generic T6/BRC behavioral-quotient theorem with no surface-specific content, or if exact counterexamples show that the proposed frontier-only question is ill-typed without adding non-native geometry.",
    "alternative_route_or_free_exploration_considered": "Closure was considered and rejected because R041 leaves a precise falsifiable minimality/reconstruction residue. Rehoming to generic A2/A4/BRC was considered; only the generic kernel/recoalescence layer belongs upstream, while the FCC/HCP contact-cut reconstruction and minimal exterior-correlation question remains owner-local. Free exploration is not preferred because the next information gap is already exact and bounded.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "R041 already froze the broad horizon-indexed quotient theorem and its positive M_h carrier. R043 narrows the next work to one adversarial reconstruction/minimal-residual question with different success and kill outcomes, allowing the parent result to remain frozen instead of reopening its entire quotient census."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R043 — Native Surface Frontier Reconstruction and Minimal Markov Carrier

Status: `READY / P1 / CURRENT-POLICY REVIEWED CONTINUATION / NOT CANONICAL`

## 0. Mother question

R039/R041 establish a metric-free native surface transition system based on the occupied-to-unoccupied contact cut. R041's strongest positive carrier is horizon-indexed:

`M_h = S + weighted induced contact graph on L0..L_{h-2}`

for the declared Boolean addition-only future, with exact recursive update to the child `M_{h-1}`.

The unresolved question is narrower:

> Does the weighted **current frontier only** state `G0` already determine the exact Boolean future and recursively update itself? If not, what is the first irreducible L0-L1/shared-future-cell correlation, and how little of it must be restored?

The task is successful either by a proof or by an exact minimal/narrow counterexample hierarchy.

## 1. Frozen semantic layer

Use only the declared FCC/HCP contact relation and finite connected occupied clusters. Coordinates may implement contact/symmetry but may not import radius, norm, equal-distance shell, Euclidean area/curvature, sphere semantics, or an embedding metric into the native state.

For cluster `C`:

- current frontier: `L0(C)`;
- native contact-cut size: `S(C)`;
- frontier label `k_C(x)`: occupied-neighbor/contact-incidence count used by the R039/R041 exact update law;
- candidate `G0(C)`: `S(C)` plus the weighted induced contact graph on `L0(C)`;
- target future: the frozen R041 branch-aware Boolean addition future `B_h` unless an explicitly stronger multiplicity/provenance comparator is being used only as a boundary test.

Do not identify Boolean support with multiplicity or provenance semantics.

## 2. First decisive gate — kill or prove `G0 -> B3`

Run three genuinely different attacks rather than expanding the old census mechanically.

### A. Exact collision search

Search for clusters `C,D` with

`G0(C) = G0(D)` up to the declared native symmetry/isomorphism notion

but

`B3(C) != B3(D)`.

Reuse the frozen R039/R041 atlas as an input oracle where appropriate, but implement the new G0-signature/collision logic independently enough to detect inherited coding assumptions. If bounded class counts remain nearly injective, switch to constructive/local-surgery search rather than merely increasing N.

### B. Reconstruction route

Test whether `G0` determines, up to future-equivalent relabeling, the omitted shared-future-cell incidence family

`{ N(y) intersect L0 : y in L1 }`.

Separate progressively weaker targets:

1. exact embedded L1 reconstruction;
2. successor `R2bar` reconstruction;
3. `B3` reconstruction;
4. recursive successor-G0 reconstruction.

A proof of a weaker target must not be reported as a stronger one.

### C. Local ambiguity route

Construct weighted-frontier-isomorphic local patches whose frontier pairs/triples have different common future neighbors. Determine whether that difference survives to successor R2/B3. Prefer the smallest local ambiguity over a large-cluster witness.

## 3. If G0 fails — residual ladder

Test candidate repairs in increasing information strength:

1. pair-overlap counts among frontier cells;
2. pair-overlap plus local slot/orbit type when symmetry makes raw pair labels redundant;
3. shared-future hypergraph recording each L1 cell by its neighboring frontier subset;
4. quotient of that hypergraph by weighted-frontier automorphisms;
5. full `M3 = L0 union L1` only as an established upper bound.

For every candidate record:

- exact sufficiency or a kill witness;
- whether it can update to the same representation type after one action;
- first failure size/horizon in bounded evidence;
- serialized state size / relation count relative to G0 and M3.

Do not claim universal minimality from bounded exhaustion alone.

## 4. If G0 survives — stationary-state pressure test

A B3 theorem alone is not enough. Test whether there is a closed action update

`G0(C), action-class -> G0(C+x)`

up to the declared future-equivalence/symmetry.

If the update exists, test B4 and then formulate the exact induction condition required for all finite Boolean horizons. If B3 is answerable but successor G0 is not reconstructible, classify G0 as a finite-query carrier rather than a stationary Markov state.

## 5. Mandatory negative controls

The return must preserve at least these boundaries:

- same scalar `S` is already unsafe for richer futures;
- same histogram/local-type data can lose correlation;
- same `R2bar` can agree through shorter horizons and split later;
- abstract graph isomorphism is not automatically embedded/native future equivalence;
- terminal-query sufficiency does not imply recursive executability;
- Boolean safety does not automatically lift to multiplicity/provenance/probability.

Any proposed carrier that erases one of these known distinctions without an explicit factorization proof fails.

## 6. Tool/owner comparison required by this task

After the surface information structure is fixed, compare any proposed generic mechanism with the current Toolbox before claiming a new reusable calculus. In particular:

- generic future-safe quotient / descent belongs to the existing operation-safe quotient owner;
- generic branch/recoalescence support belongs to BRC/A4 ownership;
- finite symmetry/orbit reduction may be reused for frontier automorphism quotients;
- the task-local novelty question is the exact **surface contact-cut reconstruction/minimal correlation** result, not the existence of generic quotient or graph-isomorphism machinery.

A tool collision narrows implementation ownership; it does not erase a surface-specific theorem/counterexample.

## 7. Required outputs

Return a compact evidence package containing:

1. exact definition of the tested G0 equivalence;
2. proof or smallest available exact counterexample for `G0 -> B3`;
3. if G0 fails, the first localized missing correlation and the strongest tested repair below M3;
4. recursive-update verdict for the surviving carrier;
5. FCC/HCP comparison at the exact tested scope;
6. machine-checkable witnesses/certificates for every finite claim;
7. explicit separation of theorem proof, exhaustive finite evidence, and conjecture;
8. method-harvest classification against the current Toolbox.

## 8. Terminal classifications

Return exactly one primary research verdict:

- `G0_STATIONARY_BOOLEAN_CARRIER_PROVED`;
- `G0_B3_SUFFICIENT_BUT_NOT_RECURSIVELY_CLOSED`;
- `G0_KILLED_MINIMAL_CORRELATION_LOCALIZED`;
- `STRICT_SUB_M3_REPAIR_PROVED`;
- `NO_COMPACT_REPAIR_PROVED_AT_REQUESTED_STRENGTH`;
- `SURFACE_SPECIFIC_RESIDUE_REDUCES_TO_EXISTING_OWNER`;
- `OPEN_WITH_EXACT_NEW_BOUNDARY`.

The return must state the weakest supported claim. No Foundation-state change or source-canonicality claim follows automatically from this task.
