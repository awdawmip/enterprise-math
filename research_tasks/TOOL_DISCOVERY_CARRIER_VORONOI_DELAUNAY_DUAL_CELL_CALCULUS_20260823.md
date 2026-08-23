<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TD-VD-CARRIER-VORONOI-DELAUNAY-DUAL-CELL-CALCULUS",
  "title": "Tool Discovery B — Carrier Voronoi / Delaunay Dual-Cell Calculus",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "ENTERPRISE_CARRIER_VORONOI_DELAUNAY_TOOL_CLASSIFIED",
  "next_action": "Classify whether explicitly metric finite carrier sites support a reusable nearest-site/dual-cell/certificate calculus useful across Enterprise problems while remaining carrier-typed and not being confused with native Enterprise metric semantics.",
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
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "tags": [
    "tool-discovery",
    "B",
    "voronoi",
    "delaunay",
    "dual-cell",
    "nearest-site",
    "carrier-geometry",
    "finite-certificate"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "TDVD",
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

# Tool Discovery B — Carrier Voronoi / Delaunay Dual-Cell Calculus

Task-ID: `RS-TD-VD-CARRIER-VORONOI-DELAUNAY-DUAL-CELL-CALCULUS`

Intended owner branch:

`research/tool-carrier-voronoi-delaunay-dual-cell`

## 0. Driver semantic boundary

Current Enterprise Foundation contains a triangular center carrier of overlapping circle cells with nearest center spacing `1` and carrier radius `1/sqrt(3)`. It also explicitly separates classical carrier Euclidean geometry from the native Enterprise metric.

Therefore this task is **carrier-typed by default**.

Freeze for this discovery task:

`CARRIER_NEAREST_SITE_TOOL != NATIVE_ENTERPRISE_METRIC`.

A successful Voronoi/Delaunay implementation on the center carrier does not prove that Euclidean perpendicular bisectors, circumcircles, angles, or point-to-point distances are native Enterprise objects.

Current source search found no registered T0–T9 family and no direct current executable owner named for Voronoi, Delaunay, power diagrams, nearest-site cells, or empty-circumcircle certificates.

Hard target:

`ENTERPRISE_CARRIER_VORONOI_DELAUNAY_TOOL_CLASSIFIED`.

## 1. Mother question

Given an explicitly declared finite site set in a metric or distance-bearing carrier, can Enterprise Math use a reusable primal/dual cell calculus to replace repeated nearest-neighbor and local-neighborhood reasoning?

Candidate capability:

> sites + declared carrier distance -> nearest-site cells -> dual adjacency/simplices -> local certificates -> incremental/local updates.

The tool is valuable only if it gives reusable structure or finite certificates beyond drawing a diagram.

## 2. Admissible input

A positive tool must require explicit site and distance semantics.

Possible input:

- finite sites `S`;
- an exact carrier distance or squared-distance comparator `d`;
- optional site weights for a power-diagram mode;
- finite ambient candidate cells/points when a fully discrete implementation is intended;
- exact coordinate carrier only when coordinates are explicitly presentation data.

For the current Enterprise center carrier, the classical planar placement may be used as **carrier implementation geometry** only at the semantic layer allowed by the Foundation source.

Do not substitute native `L_E` for a cross-sector carrier distance unless a separate theorem provides the required chart transition.

## 3. Candidate API

A positive tool should classify a coherent subset of:

- `NEAREST_SITES(x)` — all minimizing sites, preserving ties;
- `VORONOI_CELL(s)` — exact nearest-site region under the declared carrier semantics;
- `VORONOI_FACE` / `TIE_STRATUM` — shared nearest-site locus;
- `DUAL_ADJACENCY` — sites whose nearest-site cells share the declared codimension-one relation;
- `DELAUNAY_CELL` or `DUAL_SIMPLEX` — exact dual object when the input satisfies the necessary genericity/degeneracy rules;
- `EMPTY_BALL_CERT` — finite certificate for a dual simplex under metric-ball semantics;
- `POWER_CELL` — optional additively weighted variant with explicit weight meaning;
- `LOCAL_INSERT` / `LOCAL_DELETE` — locality certificate for changes if supported;
- `DEGENERACY_CLASS` — co-circular/equidistant or higher-tie classification;
- `NEIGHBOR_CERT` — compact witness that two sites are or are not dual neighbors;
- `OBSTRUCTION` — missing distance, unsupported degeneracy, nonmetric comparator, or semantic-layer misuse.

A nearest-neighbor list without a structural duality/certificate law is `RESULT_NOT_TOOL`.

## 4. Structural laws required

### 4.1 Partition with ties

State exactly whether nearest-site cells form a partition, cover with shared boundaries, or a finite set-valued assignment under ties.

Do not erase degeneracies by arbitrary tie breaking unless the tie-break is explicitly presentation-only.

### 4.2 Primal/dual correspondence

Classify the exact correspondence between shared nearest-site strata and dual adjacency/simplices under the chosen metric assumptions.

For Euclidean carrier mode, classical Voronoi–Delaunay duality may be cited/proved at its exact finite strength.

### 4.3 Empty-ball certificate

If Delaunay cells are characterized by empty circumdisks/balls, specify:

- existence;
- uniqueness versus degeneracy;
- strict versus non-strict emptiness;
- exact certificate data.

### 4.4 Relabeling / presentation invariance

Site relabeling must not alter the abstract dual incidence structure.

Coordinate rotations/translations/scalings may be invariances only if the declared carrier distance supports them.

### 4.5 Locality

Determine whether inserting/removing one site changes only a certified local region and whether this yields a reusable update algorithm/certificate.

### 4.6 Weighted mode

Power diagrams or weighted Delaunay structures require explicit weight semantics. The researcher must not infer weights from cell IDs, native addresses, or unrelated result values merely to make a desired dual complex appear.

## 5. Mandatory comparison with current tools

### T2 — finite certificate calculus

If the main value is a small incompatibility/emptiness witness, T2 may supply the generic certificate layer. Explain whether nearest-site duality adds an independent geometric decomposition.

### T3 — typed incidence circuits

Once a Delaunay/dual complex is constructed, T3 may analyze its cycles/cuts. T3 does not currently construct metric nearest-site duals.

### T7 — finite symmetry

T7 may reduce equivalent site configurations and classify degeneracies under relabeling. A symmetry orbit is not itself a Voronoi cell.

### T1 — scale enumeration

Counting shells/neighbors belongs to T1 unless the nearest-site partition or dual-cell structure contributes additional information.

## 6. Required Enterprise applications

A global tool requires two distinct uses.

### Application A — current circle-center carrier, carrier layer only

Use a finite window of the canonical center carrier.

Classify the carrier Voronoi cells and Delaunay duals of centers and compare them with known nearest-center/incidence structure.

The report must state explicitly which facts are merely classical carrier consequences and which, if any, give reusable Enterprise certificates.

Do not use this application to redefine the native right angle or native length.

### Application B — independently metric finite site family

Use a different Enterprise object whose site distance/score is independently declared, such as a finite collapse-target carrier or another finite address/state set with an admitted exact distance comparator.

If no second semantically legitimate metric site family exists, downgrade to a carrier/domain specialization instead of inventing one.

## 7. Hard negative boundaries

At minimum classify:

- no declared distance/comparator -> no nearest-site tool;
- cross-sector native distance unavailable -> do not use carrier Euclidean distance as a substitute;
- ties/co-circularity -> nonunique simplicial dual unless a cell-complex convention is retained;
- weighted/power mode without declared weights -> forbidden target leakage;
- nearest-site carrier cells do not become Enterprise circle cells merely because both are called cells;
- current overlapping circle cells are not a circle packing;
- Euclidean perpendicularity/circumcenter structure is not automatically native Enterprise orthogonality;
- finite visualization geometry is not native ontology.

Produce smallest exact degeneracy counterexamples.

## 8. Classical prior-art discipline

Voronoi diagrams, Delaunay triangulations/complexes, power diagrams, empty-ball certificates, and local insertion algorithms are classical computational/discrete geometry.

The return must distinguish:

1. classical carrier theorem;
2. existing Enterprise center/incidence facts;
3. new reusable Enterprise interface or certificate;
4. a domain-specific adapter;
5. no-new-tool result.

`CLASSICAL_CARRIER_GEOMETRY_PACKAGING != NEW_NATIVE_GEOMETRY`.

## 9. Deterministic checker

Required executable:

`scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py`

Minimum exact regression:

- finite integer/rational 2D site sets with generic and degenerate cases;
- nearest-site ties;
- Voronoi/Delaunay adjacency consistency;
- empty-disk certificates using exact squared distances;
- relabeling invariance;
- insertion/deletion locality if claimed;
- power-diagram small cases if weighted mode is claimed;
- finite window of the Enterprise center carrier;
- second independent site family if a global tool is claimed;
- explicit rejection of missing-distance/native-metric misuse;
- mismatch count `0`.

Prefer exact rational/integer predicates; floating computational geometry is not theorem evidence.

## 10. Tool acceptance gate

A positive global tool requires:

1. explicit metric/carrier semantic input;
2. reusable nearest-site and dual-cell API;
3. exact primal/dual or empty-ball law;
4. compact certificates or local update value;
5. hard degeneracy/semantic boundaries;
6. two-domain reuse;
7. exact dedup against T1/T2/T3/T7 and current source.

Allowed terminal classifications:

- `NEW_ENTERPRISE_CARRIER_TOOL_FAMILY`;
- `NEW_ENTERPRISE_TOOL_INTERFACE`;
- `COMPOSE_T2_T3_T7`;
- `CURRENT_CENTER_CARRIER_SPECIALIZATION_ONLY`;
- `DOMAIN_SPECIALIZATION_ONLY`;
- `DUPLICATE_ALIAS`;
- `RESULT_NOT_TOOL`;
- `EXACT_NO_GO_FOR_NATIVE_METRIC_PROMOTION`.

## 11. Required artifacts

Return:

1. `research_notes/TOOL_DISCOVERY_CARRIER_VORONOI_DELAUNAY_DUAL_CELL_RESULT_20260823.md`
2. `scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py`
3. optional reusable source module only if the tool gate is met.

The report must include Researcher-ID, source baseline, semantic-layer ledger, tool dedup table, carrier/native separation, two-domain evidence or downgrade reason, degeneracy counterexamples, checker summary, and final classification.

## 12. Stop condition

Freeze the strongest justified classification and required artifacts, then stop.

Do not promote a carrier geometry result into Foundation from this task.

---

Driver issue note:

`B HISTORICAL TOOL CANDIDATE; VORONOI/DELAUNAY IS CARRIER-TYPED UNLESS A SEPARATE NATIVE METRIC THEOREM JUSTIFIES MORE.`
