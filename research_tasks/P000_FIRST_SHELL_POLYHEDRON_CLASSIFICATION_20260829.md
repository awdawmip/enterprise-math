<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-FIRST-SHELL-POLYHEDRON-CLASSIFICATION",
  "title": "P000 进取几何第一层 Cell 壳层的多面体类型精确分类",
  "kind": "RESEARCH",
  "owner": "research/p000-first-shell-polyhedron-classification",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Determine exactly what classical polyhedral readouts, if any, are induced by the first native Cell adjacency layer under close-packed sphere carriers, distinguishing nearest-neighbor shell hull, Voronoi/Dirichlet cell, stacking type, and the P000 six-axis native layer.",
  "next_action": "Freeze typed definitions of first native adjacency layer, nearest-neighbor center shell hull, and Voronoi cell; then compute exact FCC and HCP/Barlow local coordination data and decide whether the shell face count 14 is universal, carrier-dependent, or the wrong native object.",
  "dependencies": [
    "p000_reality_foundation.json@main",
    "definitions/00_CURRENT_NATIVE_FOUNDATION.md@main"
  ],
  "source_refs": [
    "research_returns/P000_6D_ROTATION_SLICE_TOMOGRAPHY_RETURN_20260829.md@main",
    "driver_reviews/P000_6D_ROTATION_SLICE_TOMOGRAPHY_DRIVER_REVIEW_20260829.md@main"
  ],
  "evidence_status": "USER_REQUESTED_P000_GEOMETRY_VERIFICATION / NO_POLYHEDRON_TYPE_PREACCEPTED",
  "last_progress_ref": "driver_reviews/P000_6D_ROTATION_SLICE_TOMOGRAPHY_DRIVER_REVIEW_20260829.md",
  "last_progress_at": "2026-08-29T01:20:00+00:00",
  "hard_block": null,
  "tags": [
    "P000",
    "first-shell",
    "polyhedron",
    "close-packing",
    "FCC",
    "HCP",
    "Barlow",
    "Voronoi",
    "coordination-shell",
    "6D-space"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-FIRST-SHELL-POLYHEDRON-CLASSIFICATION",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000SHELL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 进取几何第一层 Cell 壳层的多面体类型精确分类

Status: `PUBLISHED_REGISTERED / P000-BOUND / NEW_DIRECTION / FIRST-SHELL-VERIFICATION`

## Mother question

Under the locked P000 premise that Enterprise space is a six-dimensional discrete Cell space, what exactly is meant by the “first layer” around one Cell, and which classical polyhedron—if any—is its correct carrier readout?

In particular, verify rather than assume the candidate statement that the first nearest-neighbor shell is a 14-faced polyhedron. Distinguish this from the center Cell's Voronoi/Dirichlet region and from the native P000 adjacency layer itself.

The task is not allowed to question P000. It is allowed, and required, to reject an incorrect polyhedral readout.

## Frozen inputs and scope

P000 is unconditional:

`REALITY_DIMENSION=7`.

`ENTERPRISE_SPACE_DIMENSION=6`.

`ENTERPRISE_TIME_DIMENSION=1`.

`ENTERPRISE_SPACE_KIND=DISCRETE_CELL_SPACE`.

`NATIVE_SPATIAL_DIMENSION=NATIVE_SPATIAL_AXIS_COUNT=6`.

`CURRENT_THREE_AXIS_MODEL=RESEARCH_SLICE_OF_6D_SPACE`.

`ENTERPRISE_GEOMETRY_PRIMARY_TRANSFORMATION=ROTATION`.

The exact three-axis `120 degree` circle-Cell geometry remains a slice theorem only.

For this task, use equal-sphere close packing only as a typed carrier/readout for probing one local layer. Do not promote FCC, HCP, Barlow stacking, Euclidean convexity, or Voronoi geometry into P000 native ontology without an explicit bridge.

Freeze four distinct object types:

1. `L1_NATIVE(c)` — the first native Cell adjacency layer around a center Cell `c`;
2. `KISS1(c)` — the carrier nearest-neighbor / kissing-center set corresponding to that layer under a declared close-packed-sphere realization;
3. `HULL1(c)=conv(KISS1(c))` — the classical convex hull of those neighbor centers, when the carrier embedding makes this meaningful;
4. `VOR(c)` — the classical Voronoi/Dirichlet region of the center in the carrier packing.

These objects must never be silently identified.

The task must examine at least FCC and HCP local close packing. If the local classification extends to arbitrary Barlow stackings, prove the exact extension or return the smallest stacking-dependent distinction.

Do not assume in advance that FCC and HCP have the same coordination polyhedron merely because both have kissing number 12.

Do not assume that 12 carrier contact directions automatically equal six native axes by pairing Euclidean opposites. P000 fixes six native axes; the carrier-to-native correspondence must be typed and audited rather than declared.

## Hard target and required outputs

Hard target:

`P000_FIRST_NATIVE_LAYER_POLYHEDRON_AND_READOUTS_EXACTLY_CLASSIFIED`.

A successful return must provide all of the following.

### 1. Exact first-layer definitions

Give precise definitions of `L1_NATIVE`, `KISS1`, `HULL1`, and `VOR`, including which relations are native and which require a classical carrier embedding.

State clearly whether “一层” in later Rubik/shell work should default to native adjacency distance 1, a carrier kissing shell, a convex-hull boundary, or something else.

### 2. FCC first-shell census

Using exact coordinates or an equivalent exact combinatorial construction, compute the FCC nearest-neighbor shell around one center:

- number of neighbors / hull vertices;
- hull edge count;
- hull face count;
- face-type multiset;
- combinatorial/polyhedron name if standard;
- symmetry information actually needed to certify the classification.

Do not accept the name `cuboctahedron` without an exact incidence or coordinate check.

### 3. HCP and Barlow comparison

Perform the same exact local classification for HCP.

Determine whether the HCP first-shell hull is combinatorially/geometrically the same as FCC or a distinct 14-faced coordination polyhedron.

Then determine the strongest correct statement for Barlow stackings: universal face count, finite list of local types, stacking-dependent family, or exact obstruction to a universal claim.

### 4. Voronoi distinction

Compute or source-check the center Voronoi/Dirichlet cell for FCC and HCP at the same exact strength needed to settle face count and type.

Explicitly test the candidate confusion:

`FIRST_NEIGHBOR_CENTER_HULL_HAS_14_FACES`

versus

`CENTER_VORONOI_CELL_HAS_12_FACES`.

If either statement is not universally correct in the declared scope, replace it with the strongest correct statement.

### 5. Euler/incidence verification

For every claimed polyhedral type, provide an independent incidence check such as

`V - E + F = 2`

together with the face-edge incidence count.

A visual resemblance or software polyhedron label alone is insufficient.

### 6. Six-axis P000 interpretation

Classify what, if anything, the first-shell carrier data says about the six native P000 axes.

At minimum distinguish:

- carrier neighbor count;
- carrier direction families;
- native axis count;
- slice axes;
- absence of primitive native negative axes.

If a 12-to-6 correspondence survives, state the exact relation and hypotheses. If it does not survive native typing, return the correct boundary rather than forcing it.

### 7. Rotation/shell consequence

State the exact consequence for the P000 Rubik/tomography program.

In particular, decide which object should be used as the default first support layer for rotation experiments and whether a 14-faced carrier hull is merely a visualization, a combinatorial control object, or a genuine invariant of the native layer.

### 8. Deterministic checker or exact certificate

Provide a deterministic exact-integer/rational/radical-coordinate checker or an equivalent hand-verifiable incidence certificate for the finite shell classifications.

The checker must distinguish FCC and HCP inputs rather than hard-code a single expected polyhedron name.

## Research value to preserve

The project must not build six-dimensional rotation geometry on an ambiguous use of “layer”.

If the first close-packed shell has 12 neighboring Cells but its neighbor-center hull has 14 faces while the center Voronoi region has 12 faces, those numbers encode different structures and must remain separately typed.

Equally important, FCC and HCP/Barlow may share the same face count while differing in incidence or geometry. The task should recover that distinction if it exists.

The result will become the regression boundary for later native shell, partial rotation, and multi-layer tomography tasks.

## Success, kill, and return criteria

Success requires an exact typed classification of the first layer and its carrier polyhedral readouts, with FCC/HCP comparison and the 14-face versus 12-face ambiguity resolved.

Kill any return that:

- answers only “14面体” from FCC without checking HCP/Barlow;
- confuses `HULL1` with `VOR`;
- treats kissing number 12 as face count 12;
- treats six P000 axes as a theorem derived from dividing 12 Euclidean directions by 2;
- imports a classical 3D packing as the full six-dimensional native geometry;
- labels a polyhedron by appearance without incidence verification;
- ignores a stacking-dependent distinction because two candidates have the same `V,E,F`;
- promotes the carrier hull itself to P000 Foundation without a native bridge.

If no unique classical polyhedron corresponds to `L1_NATIVE`, return that exact negative conclusion and give the complete typed family of valid carrier readouts.
