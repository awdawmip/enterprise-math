<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TD-DC-DISCRETE-CONFORMAL-CIRCLE-PATTERN-ADMISSIBILITY-CALCULUS",
  "title": "Tool Discovery B — Discrete Conformal / Circle-Pattern Admissibility Calculus",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "ENTERPRISE_DISCRETE_CONFORMAL_CIRCLE_PATTERN_TOOL_CLASSIFIED",
  "next_action": "Classify whether any explicitly metric finite Enterprise complex admits a reusable discrete-conformal/circle-pattern curvature calculus, while proving that the current overlapping circle-cell Foundation is not silently reinterpreted as Euclidean circle packing or native conformal geometry.",
  "dependencies": [
    "enterprise_toolbox_registry.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5",
    "research_method_inventory.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5",
    "tool_invocation_policy.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5"
  ],
  "source_refs": [
    "definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md@393060ebfd6a86ad45f258747d78a14d9c8ac153",
    "enterprise_toolbox_registry.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5",
    "research_method_inventory.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5"
  ],
  "related_task_ids": [
    "RS-TD-LP-DISCRETE-LAPLACIAN-CHIP-FIRING-POTENTIAL-CALCULUS",
    "RS-TD-IE-WEIGHTED-INCIDENCE-ENERGY-DIRICHLET-CALCULUS",
    "RS-TD-VD-CARRIER-VORONOI-DELAUNAY-DUAL-CELL-CALCULUS"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "tags": [
    "tool-discovery",
    "B",
    "discrete-conformal",
    "circle-pattern",
    "circle-packing",
    "curvature",
    "triangulated-complex",
    "semantic-admissibility"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "TDDC",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Tool Discovery B — Discrete Conformal / Circle-Pattern Admissibility Calculus

Task-ID: `RS-TD-DC-DISCRETE-CONFORMAL-CIRCLE-PATTERN-ADMISSIBILITY-CALCULUS`

Intended owner branch:

`research/tool-discrete-conformal-circle-pattern-admissibility`

## 0. Driver semantic warning

The phrase `discrete conformal` does not name one unique finite theory. Vertex scaling, circle packing, circle patterns with prescribed intersection angles, cotangent-Laplacian formulations, and other models have different input data and invariants.

This task must **classify the model before building a tool**.

The current canonical Enterprise plane has equal-radius circle cells of radius `1/sqrt(3)` whose neighboring cells overlap with positive area. Those cells form a gap-free cover and are explicitly not defined as a tangency packing. Carrier Euclidean geometry is also explicitly distinct from native Enterprise length/orthogonality.

Freeze for this task:

`CURRENT_ENTERPRISE_CIRCLE_CELLS != CIRCLE_PACKING`.

`CARRIER_EUCLIDEAN_CONFORMAL_DATA != NATIVE_ENTERPRISE_CONFORMAL_DATA`.

No positive result may silently reinterpret the current cell cover as a classical circle packing or infer native angle/curvature from carrier coordinates.

Current source search found no registered T0–T9 family or direct executable owner named for discrete conformal maps, circle packing, circle patterns, cotangent Laplacians, or discrete curvature flow.

Hard target:

`ENTERPRISE_DISCRETE_CONFORMAL_CIRCLE_PATTERN_TOOL_CLASSIFIED`.

## 1. Mother question

Is there a semantically admissible, reusable finite conformal/curvature tool for Enterprise Math once the necessary metric or circle-pattern data is explicitly declared?

Candidate capability:

> finite triangulated/incidence complex + declared metric/conformal model -> local angle/circle data -> discrete curvature -> admissible conformal update -> exact invariant/obstruction/certificate.

A valid negative result may conclude that current native Foundation supplies insufficient data and that any such tool is only conditional on extra metric structure.

## 2. Model-selection gate

Before doing calculations, choose and justify one or more precise modes.

### Mode A — edge-length / vertex-scaling model

Possible input:

- finite triangulated 2-complex;
- positive edge lengths satisfying triangle inequalities;
- an explicit vertex scale law for changing lengths;
- boundary/interior typing.

The exact scale law must be stated. Do not call two inequivalent scaling conventions the same tool.

### Mode B — circle-pattern model

Possible input:

- finite combinatorial complex;
- positive circle radii;
- prescribed tangency or intersection-angle data;
- exact rule relating neighboring radii/angles to edge geometry.

The current fixed-radius overlapping circle cells do not automatically satisfy this model.

### Mode C — weighted Laplacian/energy derivative layer

If curvature variation is expressed through a cotangent or related weighted Laplacian, this mode must be compared with the sibling Laplacian and weighted-energy tasks. It may be a specialization rather than a separate global family.

The researcher may reject any mode whose semantic input cannot be justified.

## 3. Candidate API

A positive tool should expose a model-specific interface, not a vague `CONFORMAL()` function.

Possible operations:

- `VALIDATE_TRIANGULATED_METRIC`;
- `VALIDATE_CIRCLE_PATTERN_DATA`;
- `ANGLE_DATA` — exact local face angles from declared metric data;
- `ANGLE_SUM` — vertex total;
- `CURVATURE` — explicit interior/boundary deficit according to the chosen model;
- `CONFORMAL_SCALE` or `RADIUS_UPDATE` — one admissible update;
- `METRIC_AFTER_UPDATE` — verify triangle/pattern validity;
- `CURVATURE_JACOBIAN` — only when an exact derivative law is established;
- `GAUSS_BONNET_CERT` — finite global curvature-sum certificate if supported;
- `TARGET_CURVATURE_SOLVER` — conditional on convexity/monotonicity/existence hypotheses;
- `PATTERN_OBSTRUCTION` — inconsistent angle/radius constraints;
- `SEMANTIC_LAYER_CHECK` — prevent carrier-to-native leakage;
- `OBSTRUCTION` — invalid triangle, nonpositive radius, unsupported model, or missing metric data.

A visualization that rescales circles until they look conformal is `RESULT_NOT_TOOL`.

## 4. Structural laws required

### 4.1 Local metric validity

Every update must preserve the exact triangle inequalities or circle-pattern consistency conditions required by the chosen model.

### 4.2 Curvature definition

State the discrete curvature formula exactly and distinguish:

- interior vertices;
- boundary vertices;
- carrier Euclidean angle deficits;
- any separately declared native notion.

No native curvature exists merely because a carrier deficit can be computed.

### 4.3 Global curvature identity

If a finite Gauss–Bonnet-type identity is claimed, prove/cite it for the exact complex and boundary convention.

Do not infer smooth-surface topology beyond the finite complex.

### 4.4 Conformal invariance/equivalence

State precisely what the chosen discrete conformal change preserves and what it changes.

Possible preserved data may include combinatorics, intersection angles, or a declared conformal class, depending on model. Do not merge these notions.

### 4.5 Variational/monotonicity law

If target-curvature solving uses a convex energy, monotone map, or positive Jacobian, classify the exact domain and failure boundary.

Any energy must respect the separate weighted-energy semantic gate.

### 4.6 Relabeling and presentation

Abstract outputs must be invariant under vertex/cell relabeling. Carrier coordinate similarity invariance may be claimed only at the carrier layer.

## 5. Mandatory ownership comparison

### Current circle-cell Foundation

The current Foundation supplies:

- a fixed triangular center carrier;
- fixed circle radius `1/sqrt(3)`;
- positive overlap of neighboring cells;
- triple boundary intersections;
- native `120 degree` right sectors;
- explicit carrier/native metric separation.

The researcher must state whether this data is sufficient for any conformal model. If not, freeze the missing-structure list exactly.

### Sibling Laplacian / energy tasks

Cotangent/weighted Laplacians, curvature Jacobians, and variational energies may be specializations of those families. A conformal task does not get a separate global tool name merely because the application vocabulary is geometric.

### T3 — incidence circuits

T3 supplies finite incidence/cycle structure but not face-angle metric data.

### T7 — symmetry

T7 can classify equivalent local configurations or absence of canonical scale choices. It does not define conformal geometry.

### Carrier Voronoi/Delaunay task

A Delaunay triangulation may be useful input to a conformal model, but carrier Delaunay duality does not make its angles native.

## 6. Enterprise reuse gate

A separate global tool requires two semantically legitimate applications.

### Application A — conditional carrier triangulation

Use a finite portion of an explicitly Euclidean carrier triangulation, including the canonical triangular center arrangement if appropriate, but label every angle/length as carrier data.

Test curvature/update identities without changing the native Foundation interpretation.

### Application B — distinct declared metric complex

Use another Enterprise finite complex whose edge lengths, radii, or intersection angles are independently meaningful.

If no second current Enterprise family has such data, classify the result as a conditional geometry/domain tool rather than fabricate metric semantics.

## 7. Circle-packing-specific no-go gate

The current Enterprise circle cells overlap with positive area, so the existing cell family is not a tangency packing.

To invoke classical circle packing the caller must separately provide or derive:

- a tangency/contact graph;
- variable positive radii or another packing parameterization;
- non-overlap/tangency conditions;
- boundary normalization when uniqueness requires it.

Do not alter the canonical cell radius merely to fit a packing theorem.

A useful terminal result may be:

`CURRENT_FOUNDATION_NOT_A_CIRCLE_PACKING / EXTRA_STRUCTURE_REQUIRED`.

## 8. Hard negative boundaries

At minimum classify:

- arbitrary graph without faces/triangulation -> no angle-deficit curvature;
- triangulation without edge lengths/circle-pattern data -> no metric conformal tool;
- invalid triangle inequalities;
- zero/negative radii;
- overlapping canonical circle cells incorrectly treated as tangency packing;
- carrier 60/120-degree drawing facts incorrectly promoted to native conformal angles;
- cotangent weights with obtuse/degenerate faces when positivity assumptions fail;
- curvature target with no existence/uniqueness theorem;
- floating numerical convergence incorrectly treated as proof;
- conformal equivalence incorrectly treated as isometry.

## 9. Classical prior-art discipline

Discrete conformal geometry, circle packing theorems, circle patterns, vertex scaling, discrete curvature, cotangent Laplacians, discrete Ricci/Yamabe-type flows, and finite Gauss–Bonnet identities have extensive classical literature.

The return must separate:

1. chosen classical model and theorem input;
2. current Enterprise metric/incidence data;
3. extra structure that had to be declared;
4. overlap with Laplacian/energy/T3/T7 tools;
5. new Enterprise interface/composition if any;
6. theorem novelty if any.

`CONDITIONAL_CLASSICAL_GEOMETRY_TOOL != NATIVE_FOUNDATION`.

## 10. Deterministic checker

Required executable:

`scripts/tool_discovery_discrete_conformal_circle_pattern_admissibility_check.py`

Minimum regression:

- exact or algebraically checkable triangle-angle examples;
- equilateral and simple non-equilateral triangulations;
- boundary/interior curvature sums;
- relabeling invariance;
- valid and invalid scale updates;
- circle-pattern consistency examples if Mode B is retained;
- explicit demonstration that the canonical overlapping circle-cell family is not a tangency packing;
- comparison with sibling Laplacian/energy capability if those interfaces are available;
- a second metric complex if a global tool is claimed;
- explicit semantic-layer rejection cases;
- mismatch count `0` for exact claims.

High-precision trigonometric numerics may support diagnostics, but theorem-level identities require analytic or exact-algebraic justification.

## 11. Tool acceptance gate

A positive global tool requires:

1. one explicitly selected conformal/circle-pattern model;
2. exact metric input contract;
3. reusable curvature/update/certificate API;
4. at least one global or variational structural law;
5. hard semantic and degeneracy boundaries;
6. two-domain reuse;
7. exact reason the capability is not merely a Laplacian/energy specialization.

Allowed terminal classifications:

- `NEW_ENTERPRISE_CONDITIONAL_GEOMETRY_TOOL`;
- `NEW_ENTERPRISE_TOOL_INTERFACE`;
- `SUBTOOL_OF_LAPLACIAN_ENERGY`;
- `CARRIER_GEOMETRY_SPECIALIZATION_ONLY`;
- `CURRENT_FOUNDATION_EXTRA_STRUCTURE_REQUIRED`;
- `CURRENT_FOUNDATION_NOT_A_CIRCLE_PACKING`;
- `DUPLICATE_ALIAS`;
- `RESULT_NOT_TOOL`;
- `EXACT_NO_GO`.

## 12. Required artifacts

Return:

1. `research_notes/TOOL_DISCOVERY_DISCRETE_CONFORMAL_CIRCLE_PATTERN_ADMISSIBILITY_RESULT_20260823.md`
2. `scripts/tool_discovery_discrete_conformal_circle_pattern_admissibility_check.py`
3. optional reusable source module only if the acceptance gate is met.

The report must include Researcher-ID, source baseline, chosen model, semantic-layer ledger, missing-extra-structure list, dedup/ownership table, curvature/update evidence, circle-packing no-go audit, checker summary, and strongest final classification.

## 13. Stop condition

Freeze the terminal classification and required artifacts, then stop.

Do not turn a conditional carrier result into a new Foundation statement from this task.

---

Driver issue note:

`B HISTORICAL TOOL CANDIDATE; MODEL SELECTION AND SEMANTIC ADMISSIBILITY PRECEDE ANY DISCRETE-CONFORMAL OR CIRCLE-PACKING CLAIM.`
