# Tool Discovery Result — Carrier Voronoi / Delaunay Dual-Cell Calculus

Researcher-ID: `EM-TDVD-4EF6B1`  
Task: `RS-TD-VD-CARRIER-VORONOI-DELAUNAY-DUAL-CELL-CALCULUS`  
Hard target: `ENTERPRISE_CARRIER_VORONOI_DELAUNAY_TOOL_CLASSIFIED`  
Date: `2026-08-23`

## 1. Frozen return

**Terminal classification**

`CURRENT_CENTER_CARRIER_SPECIALIZATION_ONLY`

**Hard target resolution**

`ENTERPRISE_CARRIER_VORONOI_DELAUNAY_TOOL_CLASSIFIED = CURRENT_CENTER_CARRIER_SPECIALIZATION_ONLY`

**Independent negative conclusion**

`NATIVE_METRIC_PROMOTION = EXACT_NO_GO_FOR_NATIVE_METRIC_PROMOTION`

Highest semantic boundary retained:

`CARRIER_NEAREST_SITE_TOOL != NATIVE_ENTERPRISE_METRIC`

No Foundation mutation is proposed or made.

The classical finite-site Voronoi/Delaunay package has a coherent exact carrier-level
API and is not an alias of T1/T2/T3/T7.  However the global-tool gate in the taskbook
requires two semantically independent Enterprise domains with admitted exact
distance/comparator semantics.  The allowed/current baseline exposes only the present
center carrier as a legitimate concrete application for this task.  No second
independent finite Enterprise site family with an admitted exact nearest-site
distance/comparator is established by the baseline.  Therefore the strongest
justified result is a current-center-carrier/domain specialization, not a global
toolbox promotion.

## 2. Source baseline and scope

Read/used exactly as authorized by the taskbook:

- `research_tasks/TOOL_DISCOVERY_CARRIER_VORONOI_DELAUNAY_DUAL_CELL_CALCULUS_20260823.md@ce5f08b392b063f77901b19c26f5290b36a9d43d`
- `enterprise_toolbox_registry.json@bd10bc351dbe7c90b47a3ffba3ef7796479170f5`
- `research_method_inventory.json@bd10bc351dbe7c90b47a3ffba3ef7796479170f5`
- `tool_invocation_policy.json@bd10bc351dbe7c90b47a3ffba3ef7796479170f5`
- `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`
  at blob `393060ebfd6a86ad45f258747d78a14d9c8ac153`

Current executable/source-surface audit at the baseline also found no registered
Voronoi/Delaunay owner and no source-tree path-name hit for `voronoi`, `delaunay`,
`nearest`, or `circum`.  This agrees with the driver taskbook's current-source
search.  The method inventory contains no method explicitly declaring a reusable
finite-site `distance`/`score` comparator API for nearest-site decomposition.

The inventory does contain later native line/gauge and bidirectional-spectrum
domain operators.  Their inventory-level contracts do **not** declare the exact
two-site distance/comparator semantics required by this task.  They are therefore
not silently repurposed as Application B.

## 3. Semantic-layer ledger

| Object / statement | Layer in this return | Status |
|---|---|---|
| finite site labels | abstract input | admissible |
| exact squared-distance / comparator | explicit input | mandatory |
| Euclidean placement of current centers | carrier presentation | admissible |
| Euclidean nearest-center relation | carrier result | admissible |
| Euclidean perpendicular bisector | carrier result | admissible |
| Euclidean circumcenter/circumdisk | carrier result | admissible |
| Voronoi face / tie stratum | relative to declared comparator | admissible |
| Delaunay cell / empty-ball certificate | relative to declared comparator | admissible |
| native Enterprise point-to-point metric | Foundation/native | **not supplied globally** |
| cross-sector native distance | Foundation/native | **requires explicit chart transition** |
| Euclidean carrier distance = native Enterprise distance | cross-layer claim | **forbidden** |
| Voronoi cells = Enterprise circle cells | ontology promotion | **false / forbidden** |
| overlapping Enterprise circle cells = circle packing | ontology promotion | **false / forbidden** |

The Foundation explicitly supersedes the old classical carrier quadratic form as
the native Enterprise metric while allowing it to remain a classical planar
carrier distance.  It also freezes arbitrary cross-sector native point-to-point
distance as requiring an explicit native chart transition.  Those two statements
block any inference from a successful carrier Voronoi computation to a native
Enterprise metric.

## 4. Candidate carrier-safe API

A coherent specialization can expose the following **only after** a finite site
family and exact comparator/distance semantics have been supplied:

- `NEAREST_SITES(x)` -> all minimizers; ties are set-valued and retained.
- `VORONOI_CELL(s)` -> exact nearest-site region under the declared comparator.
- `TIE_STRATUM(S0)` / `VORONOI_FACE` -> locus with exactly/at least the declared
  tied nearest sites, according to the chosen convention.
- `DUAL_ADJACENCY(s,t)` -> codimension-one shared nearest-site face.
- `DELAUNAY_CELL(S0)` -> maximal empty-ball boundary set, not necessarily a
  simplex in degenerate cases.
- `EMPTY_BALL_CERT` -> exact center/radius-score plus
  `(inside, boundary, outside)` site partition.
- `DEGENERACY_CLASS` -> equidistant/cocircular/higher-tie classification.
- `LOCAL_INSERT` / `LOCAL_DELETE` -> optional carrier update certificate.
- `OBSTRUCTION` -> missing comparator, unsupported metric assumptions,
  semantic-layer mismatch, or undeclared weights.

Weighted/power mode is **not claimed** in this return.  It would require separately
declared exact site-weight semantics.  Cell IDs, addresses, native values, or
desired output topology are not legal sources of weights.

## 5. Dedup against T1 / T2 / T3 / T7

| Existing tool | What it can contribute | What it does not supply here | Dedup result |
|---|---|---|---|
| T1 Scale Enumeration / Valuation | count shells/neighbors, valuation of finite overlap data | no admitted distance comparator; no nearest-site cells; no empty-ball duality | not duplicate |
| T2 Block Finite-Certificate | generic bounded witness/obstruction packaging | does not derive metric bisectors, nearest-site strata, or Voronoi-Delaunay duality | composable backend, not duplicate |
| T3 Typed Incidence Circuit | analyze cycles/cuts/circuits after a dual complex exists | does not construct the metric nearest-site dual | downstream consumer, not duplicate |
| T7 Finite Symmetry / Equivariance | relabeling audit, orbit reduction, canonical-choice obstruction | a symmetry orbit is not a Voronoi cell; cannot select a diagonal in a symmetric cocircular case without extra data | validation layer, not duplicate |

Therefore `COMPOSE_T2_T3_T7` is not an adequate semantic replacement for the
nearest-site construction itself.  Conversely, structural distinctness alone is
not enough for global promotion: the taskbook additionally requires two-domain
reuse, which is not met.

## 6. Structural laws at carrier level

### 6.1 Ties are first-class

For an exact comparator `q(x,s)`, define

`N(x) = {s in S : q(x,s) = min_t q(x,t)}`.

The canonical object is the set `N(x)`, not a tie-broken representative.

With two sites `(-1,0)` and `(1,0)` and query `(0,0)` under exact Euclidean
squared distance, `N(0) = {left,right}`.  Choosing either label by ordering would
create presentation-dependent structure.

### 6.2 Voronoi/Delaunay duality

In classical 2D Euclidean carrier mode:

- a codimension-one shared Voronoi face yields a Delaunay edge;
- an empty circle with a maximal boundary set `B` yields a Delaunay cell
  `conv(B)`;
- when `|B|=3` and no fourth cocircular site exists, this is a simplex;
- when `|B|>3`, the canonical dual is a polygonal cell unless extra data
  explicitly chooses a triangulation.

The checker verifies dual adjacency independently by exact feasibility on each
perpendicular bisector and compares it with the edges of the maximal
empty-circle Delaunay cells.

### 6.3 Empty-ball certificate

For a Euclidean carrier triple, a theorem-grade finite certificate is:

1. exact rational circumcenter when it exists;
2. exact squared radius;
3. exact site partition into `inside`, `boundary`, and `outside`;
4. `inside = empty`;
5. maximal boundary set retained under degeneracy.

No square roots or floating tolerances are required.

### 6.4 Relabeling invariance

Relabeling changes names only.  The checker relabels a generic four-site
configuration and verifies that the coordinate-realized Delaunay cells are
unchanged.

### 6.5 Locality

The checker gives a finite local insertion/deletion delta certificate on a generic
four-site carrier example: every changed dual edge after insertion is supported
on the inserted site's new neighbor set, and deletion restores the exact prior
edge set.

This is evidence that the classical carrier specialization can support local
updates.  It is **not** used to claim a new native Enterprise theorem or a global
tool family.

## 7. Application A — current Enterprise center carrier

This application is explicitly carrier-only.

Use a classical axial presentation of the triangular center lattice with
presentation coordinates `(u,v)` and exact carrier squared-distance form

`Q(du,dv) = du^2 + du*dv + dv^2`.

These `(u,v)` values are **carrier axial coordinates**, not replacement native
Enterprise sector addresses.

For the seven-center finite window

- `O=(0,0)`,
- six carrier neighbors
  `(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)`,

the checker proves exactly:

1. all six neighbors have carrier squared distance `1` from `O`;
2. `(1/2,0)` is a two-site nearest-center tie for `O` and `(1,0)`;
3. `(1/3,1/3)` is a three-site nearest-center tie for
   `O,(1,0),(0,1)`;
4. the elementary center triangle has exact carrier circumcenter
   `(1/3,1/3)` and carrier squared circumradius `1/3`;
5. the remaining sites in the finite window lie on or outside that
   circumdisk.

Thus the classical carrier Voronoi cell around an interior center is the familiar
hexagonal nearest-center region and the carrier Delaunay cells are elementary
triangles.

There is an exact carrier coincidence worth recording but not promoting:
the elementary center triangle has Euclidean carrier circumradius `1/sqrt(3)`,
the same carrier radius frozen for the overlapping circle cells.  Hence its
carrier circumcenter is the triple boundary-intersection point of those three
radius-`1/sqrt(3)` carrier circles.  This is a useful finite **carrier
certificate** linking existing center incidence to the Voronoi/Delaunay
presentation.

It does **not** imply any of the following:

- the Voronoi hexagon is an Enterprise `CIRCLE_CELL`;
- the overlapping circle cells form a circle packing;
- Euclidean perpendicular bisectors are native Enterprise orthogonality;
- the Euclidean circumcenter is a new native primitive;
- carrier Euclidean point-to-point distance is the native Enterprise metric.

## 8. Application B — downgrade audit

A global tool requires a second Enterprise family whose site comparator is
independently declared.

Under the frozen baseline, no such second family is established with a contract
strong enough for this task.  In particular, inventory entries for directed
native line gauge and bidirectional segment spectrum do not, at inventory level,
declare a symmetric finite-site distance or an exact nearest-site comparator
suitable for this API.  Treating them as one would add semantics not supplied by
the source.

Therefore:

`APPLICATION_B = NOT_ESTABLISHED_UNDER_ALLOWED_BASELINE`

and by the taskbook's explicit rule:

`NO_APPLICATION_B -> DOWNGRADE_TO_CARRIER_OR_DOMAIN_SPECIALIZATION`.

No metric is manufactured to satisfy the acceptance gate.

## 9. Exact counterexamples

### 9.1 Smallest non-simplicial cocircular degeneracy

Take four sites

`A=(0,0), B=(2,0), C=(2,2), D=(0,2)`.

Their exact Euclidean carrier circumcenter is `(1,1)` and squared radius is `2`.
All four are boundary sites of one empty circle.

Canonical consequences:

- the Delaunay cell is the 4-site polygon `ABCD`;
- Voronoi codimension-one adjacency is on the four sides;
- both diagonals meet only through the common Voronoi vertex relation, not a
  canonical codimension-one choice;
- selecting `AC` or `BD` merely to return a triangulation is noncanonical.

This is the minimal planar cocircular configuration in which a simplicial
Delaunay triangulation is nonunique.  Arbitrary tie breaking would violate the
task's relabeling/presentation requirement.

### 9.2 Missing-distance counterexample

Let the finite set be `{X,S1,S2}`.  Keep the site labels fixed and consider two
exact metric tables:

Metric `M1`:

- `d(X,S1)=1`
- `d(X,S2)=2`
- `d(S1,S2)=3`

Metric `M2`:

- `d(X,S1)=2`
- `d(X,S2)=1`
- `d(S1,S2)=3`

Both satisfy all metric axioms; triangle inequality is attained as equality.
Yet

- under `M1`, nearest site to `X` is `S1`;
- under `M2`, nearest site to `X` is `S2`.

Therefore the finite site family alone does not determine `NEAREST_SITES`.
Distance/comparator semantics are logically necessary input.

The Enterprise-specific version is even sharper: the current Foundation does
not supply an arbitrary cross-sector native point-to-point metric.  Substituting
the classical carrier Euclidean comparator there would not fill a missing
definition; it would cross a frozen semantic layer.

### 9.3 Minimal tie

Two sites and their exact midpoint already force a set-valued nearest-site
answer.  Any total-order tie break is an extra presentation convention and must
not be returned as canonical geometry.

## 10. Checker

Required executable:

`scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py`

Properties:

- Python standard library only;
- exact `Fraction`/integer arithmetic;
- no floating computational geometry;
- generic and cocircular finite 2D cases;
- exact nearest-site ties;
- exact Voronoi/Delaunay adjacency comparison;
- exact empty-circle certificates;
- relabeling invariance;
- insertion/deletion locality certificate;
- exact seven-center Enterprise carrier window;
- explicit missing-comparator rejection;
- explicit carrier-to-native semantic-layer rejection;
- explicit two-metric missing-distance counterexample;
- no weighted-mode claim;
- no false second-domain/global-tool claim.

Deterministic regression result:

```text
classification=CURRENT_CENTER_CARRIER_SPECIALIZATION_ONLY
mismatch_count=0
```

## 11. Tool acceptance gate

| Gate | Result | Reason |
|---|---|---|
| explicit metric/carrier semantic input | PASS | comparator is mandatory and typed |
| reusable nearest-site/dual-cell API | PASS at carrier-interface level | coherent candidate API exists |
| exact primal/dual or empty-ball law | PASS in Euclidean carrier mode | exact rational predicates/certificates |
| compact certificates/local update value | PASS for tested carrier specialization | empty-ball and local delta certificates |
| hard degeneracy/semantic boundaries | PASS | ties retained; native misuse rejected |
| two-domain reuse | **FAIL** | no legitimate second Enterprise comparator family established |
| dedup vs T1/T2/T3/T7/current source | PASS | distinct contract; no current direct owner |

Because the acceptance gate is conjunctive, the global-tool result is negative.

No optional reusable source module is added because the tool gate is not met.

## 12. Final classification

Strongest justified classification:

`CURRENT_CENTER_CARRIER_SPECIALIZATION_ONLY`

The carrier package is mathematically coherent and potentially reusable if a
future Enterprise domain independently declares the needed exact comparator.
That future event could justify reopening the two-domain gate.  This task does
not pre-authorize such a comparator and does not alter Foundation.

Final freeze:

`ENTERPRISE_CARRIER_VORONOI_DELAUNAY_TOOL_CLASSIFIED`

`CARRIER_NEAREST_SITE_TOOL != NATIVE_ENTERPRISE_METRIC`

`TIES_ARE_CANONICAL_SET_VALUED_DATA`

`COCIRCULAR_CELL != CANONICALLY_TRIANGULATED_CELL`

`NO_DECLARED_COMPARATOR -> NO_NEAREST_SITE_STRUCTURE`

`NO_SECOND_ENTERPRISE_DISTANCE_FAMILY -> NO_GLOBAL_TOOL_PROMOTION`

`FOUNDATION_MUTATION = FALSE`
