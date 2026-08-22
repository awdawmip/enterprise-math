<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TD-OM-NATIVE-ORIENTED-MATROID-CIRCUIT-CALCULUS",
  "title": "Tool Discovery — Native Oriented-Matroid / Circuit Calculus",
  "kind": "RESEARCH",
  "owner": "research/tool-native-oriented-matroid-circuits",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Discover a coordinate-free sign/circuit calculus that preserves useful native geometry while discarding metric and carrier presentation data.",
  "next_action": "Extract oriented-matroid mechanisms, attempt a native chirotope/circuit reconstruction from Enterprise incidence and direction data, and test whether the resulting calculus solves at least two distinct problems without metric input.",
  "dependencies": [
    "current Enterprise foundational logic",
    "current native foundation router",
    "historical oriented-matroid / chirotope / circuit mechanisms used only as comparison and inspiration"
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
    "oriented-matroid",
    "chirotope",
    "circuits",
    "coordinate-free",
    "discrete-geometry"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "TDOM",
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

# Tool Discovery — Native Oriented-Matroid / Circuit Calculus

Status: `READY / DRIVER_APPROVED / PARALLEL TOOL DISCOVERY`

## 0. Mother question

How much of current Enterprise discrete geometry can be expressed using only finite orientation, incidence, support, sign, and circuit data — with coordinates, metric length, carrier angle, and drawing conventions removed from the primitive interface?

The goal is to discover a reusable **combinatorial geometry engine** analogous in role to oriented matroids, not to rename the current three-axis picture with oriented-matroid vocabulary.

## 1. Historical mechanism to extract

Study the operational ideas behind:

- chirotopes/sign patterns;
- circuits and cocircuits;
- circuit elimination;
- duality;
- covectors/topes and region decomposition;
- realizable versus nonrealizable oriented matroids.

Historical axioms are comparison tools. Determine which minimal fragment, if any, is actually native to Enterprise geometry.

## 2. Native reconstruction problem

Starting from current admissible native incidence/direction data, attempt to define an abstract finite combinatorial structure containing some or all of:

1. a ground set of native direction/constraint elements;
2. an orientation/sign observable;
3. signed circuits or minimal dependencies;
4. cocircuits or separating observables;
5. an elimination/composition operation;
6. relabeling/gauge action;
7. a dual object if one exists naturally.

The construction must not use `120 degrees`, Euclidean determinants, slopes, coordinates, or current metric formulas to define the sign/circuit structure. Those may be used only afterward to compare realizations.

## 3. Axiom audit and failure modes

Determine exactly which oriented-matroid-like axioms hold.

Possible acceptable outcomes include:

- a full oriented matroid;
- a matroid without orientation;
- a partial oriented matroid / COM / weaker circuit system;
- a task-specific signed elimination calculus;
- an exact obstruction showing why the current native structure cannot support such a calculus without added data.

Do not force a full classical structure if a weaker native object is the correct one.

## 4. Cross-domain tool test

A positive tool verdict requires reuse on at least **two genuinely different Enterprise problems**.

At least one application must be spatial/incidence-facing, for example:

- sector legality;
- direction reversal/orientation;
- line/segment incidence;
- address support compatibility.

At least one second application must use the same circuit/sign machinery for a distinct task such as:

- path or provenance compatibility;
- BRC support interaction;
- local-process obstruction;
- another relation/constraint problem not reducible to the first spatial example.

The second application may fail; if it does, classify the exact scope boundary.

## 5. Required tool operations

A successful calculus should expose explicit operations such as:

- `SIGN(configuration)`;
- `CIRCUITS(configuration)`;
- `ELIMINATE(C1,C2,e)`;
- `SEPARATE(A,B)` or cocircuit certificate;
- `DUAL(structure)` when meaningful;
- `REALIZATION_CHECK` distinguishing native combinatorial content from carrier representation.

Prove which outputs are invariant under native relabeling/gauge actions.

## 6. Metric-independence pressure test

The strongest value of this direction is obtained only if useful theorems survive after metric erasure.

Explicitly test:

`same combinatorial orientation/circuit data + different admissible metric/carrier realization`

and determine which Enterprise conclusions remain fixed.

If every useful conclusion still requires the current scalar law or carrier angle, downgrade the result.

## 7. Tool acceptance gate

Classify the final result using exactly one leading verdict:

- `NATIVE_CIRCUIT_CALCULUS_DISCOVERED`
- `PARTIAL_ORIENTED_COMBINATORIAL_TOOL_DISCOVERED`
- `RESULT_NOT_TOOL`
- `EXACT_NO_GO_FOR_ORIENTED_MATROID_TOOL`

Use `NATIVE_CIRCUIT_CALCULUS_DISCOVERED` only if all are present:

- coordinate-free definitions;
- a nontrivial elimination/composition or duality law;
- invariant certificates;
- successful reuse on two distinct Enterprise problems;
- exact separation between native combinatorics and carrier realization.

## 8. Deliverables

Return:

1. formal ground-set/sign/circuit definitions;
2. axiom audit with proof or minimal counterexample;
3. relabeling/gauge invariance analysis;
4. historical comparison and conservative novelty statement;
5. executable finite checks where useful;
6. a compact `TOOL API` section;
7. two cross-domain demonstrations;
8. the leading verdict from Section 7.

Do not modify current Foundation definitions in this task.