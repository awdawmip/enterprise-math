<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TD-GON-NATIVE-GEOMETRY-OF-NUMBERS-MINIMA-CALCULUS",
  "title": "Tool Discovery — Native Geometry-of-Numbers / Successive-Minima Calculus",
  "kind": "RESEARCH",
  "owner": "research/tool-native-geometry-of-numbers-minima",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Discover reusable lattice-free, minima, packing/covering, and existence-certificate tools under native discrete semantics rather than Euclidean volume arguments.",
  "next_action": "Extract the operational core of geometry of numbers, rebuild lattice/body/minima notions using Enterprise finite discrete structure, and test whether one toolkit yields reusable existence or obstruction certificates across at least two problem families.",
  "dependencies": [
    "current Enterprise foundational logic",
    "current native foundation router",
    "historical Minkowski / successive minima / lattice-free / packing-covering mechanisms used only as comparison and inspiration"
  ],
  "source_refs": [
    "awdawmip/enterprise-math@00765cc76ea71f789481fbe91c29d852bbf6b209:FOUNDATIONAL_LOGIC.md",
    "awdawmip/enterprise-math@00765cc76ea71f789481fbe91c29d852bbf6b209:definitions/00_CURRENT_NATIVE_FOUNDATION.md"
  ],
  "foundation_questions": [],
  "evidence_status": "DRIVER_OPENED_TOOL_DISCOVERY",
  "last_progress_ref": null,
  "last_progress_at": "2026-08-22T21:54:00+08:00",
  "hard_block": null,
  "tags": [
    "tool-discovery",
    "geometry-of-numbers",
    "minkowski",
    "successive-minima",
    "lattice-free",
    "packing-covering"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "TDGN",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d5cbe89c8620ca6efa2af5219900424485c85bba1fc042576e17034c10e38299",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Tool Discovery — Native Geometry-of-Numbers / Successive-Minima Calculus

Status: `READY / DRIVER_APPROVED / PARALLEL TOOL DISCOVERY`

## 0. Mother question

Can Enterprise Math build a native geometry-of-numbers toolkit that turns discrete existence/avoidance problems into quantitative statements about lattice-free regions, packing/covering, successive minima, or short witnesses — without importing Euclidean volume as the decisive native quantity?

The target is a reusable existence/obstruction calculus, not a one-off lattice estimate.

## 1. Historical mechanism to extract

Study the operational ideas behind:

- Minkowski-style “large enough region contains a nonzero lattice point” reasoning;
- successive minima;
- lattice-free convex bodies and flatness phenomena;
- packing and covering radii;
- Voronoi/Delaunay duality where it serves a certificate role;
- shortest/closest lattice-vector formulations.

Identify which parts rely essentially on Euclidean convexity/volume and which parts can be replaced by native finite counting, relation capacity, shell size, order structure, or another endogenous discrete measure.

## 2. Native objects to define

A positive direction must define exact Enterprise analogues or substitutes for:

1. a discrete lattice/module/translation carrier appropriate to the selected domain;
2. an admissible “body” or feasible set class;
3. a native size/capacity observable;
4. a notion of lattice-free or witness-free region;
5. first minimum and, if meaningful, successive minima;
6. packing/covering or separation quantities;
7. witness extraction: an actual short/nonzero state when an existence threshold is crossed.

Definitions must be semantically typed. Carrier lattices are not automatically native state spaces.

## 3. Minkowski-style theorem pressure

Search for a theorem schema of the form

`NATIVE SIZE/CAPACITY EXCEEDS THRESHOLD  ->  NONTRIVIAL DISCRETE WITNESS EXISTS`,

or an exact obstruction proving that no such threshold can be representation-independent at the intended scope.

The threshold should be structural, not a disguised enumeration of the entire finite state space.

Determine sharpness on small instances and identify equality/extremal configurations.

## 4. Successive-minima tool

If a first witness notion exists, investigate whether a sequence

`lambda_1 <= lambda_2 <= ...`

can measure how much native scale/capacity is required to obtain increasingly independent witnesses.

Independence must be defined in the selected Enterprise semantic layer; do not silently import linear independence from a carrier unless justified.

If a full minima sequence is not natural, identify the strongest weaker hierarchy that remains intrinsic.

## 5. Cross-domain tool test

A positive tool verdict requires reuse on at least **two genuinely different Enterprise problem families**.

Choose distinct categories such as:

- native spatial displacement/sector/path feasibility;
- integer-root, factor, shell, or basin candidate sets;
- relation-capacity or BRC witness sets;
- another discrete existence/avoidance problem.

For each application, show the same minima/lattice-free/packing-covering interface at work.

At least one application must yield a nontrivial witness bound, impossibility certificate, or search-space reduction not already present as a direct formula.

## 6. Volume replacement audit

The task must explicitly answer:

- What plays the role of “size”?
- Is it additive, monotone, subadditive, or only order-valued?
- Is the existence theorem invariant under admitted native relabelings?
- Can two states have equal native size but different witness behavior?
- Does a continuous volume argument prove only an effective comparison theorem rather than a native theorem?

If no endogenous size observable supports the theorem, freeze that negative boundary rather than importing volume by fiat.

## 7. Tool acceptance gate

Classify the final result using exactly one leading verdict:

- `NATIVE_GEOMETRY_OF_NUMBERS_TOOLKIT_DISCOVERED`
- `PARTIAL_MINIMA_OR_LATTICE_FREE_TOOL_DISCOVERED`
- `RESULT_NOT_TOOL`
- `EXACT_NO_GO_FOR_NATIVE_GEOMETRY_OF_NUMBERS`

Use `NATIVE_GEOMETRY_OF_NUMBERS_TOOLKIT_DISCOVERED` only if all are present:

- explicit reusable object/size/witness interface;
- at least one nontrivial existence or obstruction theorem;
- a minima, packing/covering, or lattice-free calculus with composition/monotonicity laws;
- successful reuse on two distinct Enterprise problem families;
- exact carrier/native and size-semantics boundaries.

## 8. Deliverables

Return:

1. formal native definitions;
2. theorem proofs or exact no-go constructions;
3. sharp/extremal examples;
4. historical comparison and conservative novelty statement;
5. executable finite checks where useful;
6. a compact `TOOL API` section listing body/set input, size observable, minima/witness output, laws, and failure modes;
7. two cross-domain demonstrations;
8. the leading verdict from Section 7.

Do not modify current Foundation definitions in this task.