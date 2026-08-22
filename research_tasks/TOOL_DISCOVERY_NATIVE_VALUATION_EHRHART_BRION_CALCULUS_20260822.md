<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TD-EV-NATIVE-VALUATION-EHRHART-BRION-CALCULUS",
  "title": "Tool Discovery — Native Valuation / Ehrhart / Brion Calculus",
  "kind": "RESEARCH",
  "owner": "research/tool-native-valuation-ehrhart-brion-calculus",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Discover a reusable native scale-counting and valuation calculus rather than another isolated scale formula.",
  "next_action": "Extract the operational core of Ehrhart/valuation/Brion theory, rebuild it under Enterprise finite discrete semantics, and test whether one reusable calculus works on at least two distinct Enterprise problem families.",
  "dependencies": [
    "current Enterprise foundational logic",
    "current native foundation router",
    "historical Ehrhart / valuation / Brion mechanisms used only as comparison and inspiration"
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
    "valuation",
    "ehrhart",
    "brion",
    "scale-counting",
    "discrete-geometry"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "TDEV",
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

# Tool Discovery — Native Valuation / Ehrhart / Brion Calculus

Status: `READY / DRIVER_APPROVED / PARALLEL TOOL DISCOVERY`

## 0. Mother question

Can Enterprise Math obtain a reusable finite-scale counting calculus in which a discrete object `X` is assigned scale-dependent data such as

`F_X(d) = number of native states / fibers / boundary events / relation packets visible at scale d`,

and the family `F_X` obeys strong structural laws analogous in role to Ehrhart polynomiality, valuation additivity, finite-difference dimension detection, reciprocity, or Brion-style local decomposition — without importing Euclidean volume or a classical polytope definition as a native premise?

The goal is a **tool family**, not one successful counting identity.

## 1. Historical mechanism to extract

Study the operational ideas behind:

- lattice-point counting under integer dilation;
- valuation laws under decomposition and gluing;
- finite differences as dimension/degree detectors;
- rational generating functions for discrete counts;
- decomposition of global counts into local cone/vertex contributions.

Historical terminology is not authority. Identify which mechanism survives after removing classical coordinates, convex volume, and target formulas.

## 2. Required native reconstruction

Produce an explicit candidate interface containing, at minimum:

1. an admissible class of Enterprise objects `X`;
2. a native scale/refinement parameter and the exact meaning of `X[d]`;
3. one or more scale enumerators `F_X(d)`;
4. a decomposition/gluing operation with a proved valuation law or an exact obstruction to one;
5. a finite-difference or generating-function operator that exposes information not visible from a single scale;
6. composition rules: how the tool behaves under disjoint union, sector gluing, product, refinement, quotient, or another declared native operation;
7. an exact semantic statement of what information is forgotten by the enumerator.

Do not name something an Ehrhart object merely because a few sample counts fit a polynomial.

## 3. Cross-domain tool test

A positive tool verdict requires successful use on at least **two genuinely different Enterprise problem families**.

Choose two or more from distinct categories such as:

- native spatial sector/chart/path structures;
- integer-root basins, shell widths, or refinement fibers;
- BRC/path-support or relation-multiplicity structures;
- another current discrete family with a separately defined scale semantics.

For each domain, show that the same abstract operator/interface is reused rather than separately refitted.

At least one application must produce a new compression, invariant, certificate, decomposition, or complexity reduction that is not merely a restatement of already-known pointwise formulas.

## 4. Polynomiality is a question, not a premise

Test whether `F_X(d)` is:

- polynomial;
- quasi-polynomial;
- piecewise polynomial;
- eventually polynomial;
- rational-generating-function controlled;
- or genuinely outside those classes.

If polynomiality fails, classify the obstruction and determine whether a weaker valuation calculus still survives.

A negative theorem that sharply explains why no useful Ehrhart-style law can exist at the intended native scope is an acceptable strong result.

## 5. Local-to-global decomposition pressure test

Search for an Enterprise analogue of local contribution decomposition:

`GLOBAL SCALE COUNT = combination of LOCAL CRITICAL CONTRIBUTIONS`.

The local objects need not be classical vertices or cones. Candidates may arise from native boundary strata, sector branches, shell transitions, critical fibers, or other task-derived local pieces.

A valid local decomposition must specify overlap correction and provenance; double counting hidden by notation is not accepted.

## 6. Tool acceptance gate

Classify the final result using exactly one leading verdict:

- `NATIVE_VALUATION_CALCULUS_DISCOVERED`
- `NATIVE_SCALE_ENUMERATOR_PARTIAL_TOOL`
- `RESULT_NOT_TOOL`
- `EXACT_NO_GO_FOR_NATIVE_VALUATION_TOOL`

Use `NATIVE_VALUATION_CALCULUS_DISCOVERED` only if all are present:

- explicit reusable input/output interface;
- at least one nontrivial algebraic law such as valuation, composition, reciprocity, or local decomposition;
- at least one invariant/certificate visible across scales;
- successful reuse on two distinct Enterprise problem families;
- explicit kill conditions and negative boundaries.

A beautiful theorem on one family is `RESULT_NOT_TOOL` unless the general interface is independently justified.

## 7. Deliverables

Return:

1. a theorem/definition report;
2. minimal assumptions and semantic-layer typing;
3. historical-mechanism comparison with novelty claims kept conservative;
4. exact examples plus counterexamples;
5. executable finite checks when useful;
6. a compact `TOOL API` section listing inputs, outputs, laws, failure modes, and two cross-domain demonstrations;
7. the leading verdict from Section 6.

Do not modify current Foundation definitions in this task.