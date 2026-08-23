# Tool Discovery B — Discrete Conformal / Circle-Pattern Admissibility Result

Researcher-ID: `EM-TDDC-04C56C`

Task-ID: `RS-TD-DC-DISCRETE-CONFORMAL-CIRCLE-PATTERN-ADMISSIBILITY-CALCULUS`

Taskbook source baseline: `ce5f08b392b063f77901b19c26f5290b36a9d43d`

Taskbook branch: `driver/tool-discovery-b-geometry-batch-20260823`

Owner branch: `research/tool-discrete-conformal-circle-pattern-admissibility`

Hard target: `ENTERPRISE_DISCRETE_CONFORMAL_CIRCLE_PATTERN_TOOL_CLASSIFIED`

## 0. Frozen terminal verdict

Strongest final classification:

`CURRENT_FOUNDATION_EXTRA_STRUCTURE_REQUIRED`

Mandatory corollaries:

- `CURRENT_FOUNDATION_NOT_A_CIRCLE_PACKING`
- `CARRIER_GEOMETRY_SPECIALIZATION_ONLY`
- `MODE_C_WEIGHTED_CURVATURE_DERIVATIVE -> SUBTOOL_OF_LAPLACIAN_ENERGY`
- `GLOBAL_DISCRETE_CONFORMAL_TOOL_CLAIM -> REJECTED`

The current Foundation does not by itself provide a native discrete-conformal or circle-pattern metric. A classical finite piecewise-Euclidean vertex-scaling calculus is semantically admissible only after an explicit metric layer is declared. That gives a conditional carrier-geometry specialization, not a native Foundation upgrade. The current canonical overlapping circle cells cannot be silently reinterpreted as a tangency packing.

Frozen highest semantic boundaries:

`CURRENT_ENTERPRISE_CIRCLE_CELLS != CIRCLE_PACKING`

`CARRIER_EUCLIDEAN_CONFORMAL_DATA != NATIVE_ENTERPRISE_CONFORMAL_DATA`

No Foundation modification is proposed by this task.

## 1. Source/read discipline

Per the user instruction, this run read and executed only the designated taskbook as project research input. No sibling return, Foundation definition file, theorem package, registry body, or downstream report was opened. Sibling ownership comparisons below therefore use only the binding distinctions stated in the taskbook itself.

Classical formulas used below are standard finite Euclidean-triangle identities and are written explicitly so the checker does not depend on an external theorem package or numerical convergence.

## 2. MODEL SELECTION gate

### 2.1 Mode A — edge-length / vertex-scaling model: RETAINED, CONDITIONAL ONLY

Selected model:

- finite triangulated 2-complex;
- explicit boundary/interior vertex typing;
- for every face, three positive declared Euclidean edge lengths satisfying strict triangle inequalities;
- an explicit metric-layer tag, at minimum `carrier` versus separately declared `native`;
- vertex scaling law

`l'_{ij} = exp((u_i+u_j)/2) l_{ij}`.

For exact checking set

`q_i = exp(u_i/2) > 0`,

so

`l'_{ij} = q_i q_j l_{ij}`.

The checker uses rational `q_i` test fixtures. This is a test subset of the stated scaling law, not a different conformal model.

For a valid Euclidean face with side lengths `a,b,c`, the angle opposite `c` is determined by

`cos(theta_c) = (a^2+b^2-c^2)/(2ab)`.

Curvature convention:

- interior vertex `v`:
  `K_v = 2*pi - sum(theta_f,v)`;
- boundary vertex `v`:
  `K_v = pi - sum(theta_f,v)`.

Every update is admissible only if all updated face lengths remain positive and satisfy the strict triangle inequalities.

This model is retained because its inputs and outputs can be stated without semantic leakage. It is not inferred from native Enterprise incidence alone.

### 2.2 Mode B — circle packing / circle pattern: NOT RETAINED FOR CURRENT FOUNDATION

The taskbook freezes that neighboring canonical Enterprise circle cells have positive-area overlap. A classical tangency packing requires contacts without positive-area interior overlap. Therefore the current cell family fails the packing admissibility condition before any curvature computation.

No radius is modified to force a packing theorem.

A separate circle-pattern model could be admitted only after the caller independently supplies all model-defining data, including positive radii, tangency or intersection-angle data, the exact radius/angle/edge relation, and any required normalization. Those declarations are extra structure and are not supplied by the current Foundation as frozen in the taskbook.

Thus:

`CURRENT_FOUNDATION_NOT_A_CIRCLE_PACKING`.

### 2.3 Mode C — weighted/cotangent Laplacian derivative layer: NOT A SEPARATE GLOBAL FAMILY

If the derivative of curvature is represented by cotangent or related weighted Laplacian coefficients, the operator requires the same explicit metric data as Mode A and falls under the taskbook's sibling Laplacian/weighted-energy ownership boundary.

In particular, geometric vocabulary does not create a new global tool family when the executable content is a weighted Laplacian or quadratic/variational energy.

Therefore:

`MODE_C_WEIGHTED_CURVATURE_DERIVATIVE -> SUBTOOL_OF_LAPLACIAN_ENERGY`.

### 2.4 Other discrete-conformal models: NOT MERGED

No attempt is made to merge circle packing, intersection-angle circle patterns, edge-length scaling, and weighted Laplacian formulations under one vague `CONFORMAL()` interface. The taskbook explicitly forbids treating inequivalent models as the same tool.

## 3. Is the current Foundation sufficient?

No.

The current Foundation data listed in the taskbook is enough to specify a triangular carrier arrangement and an overlapping circle-cell cover, but it is not enough to define a native discrete-conformal structure.

The carrier drawing can support a conditional Euclidean calculation only when the caller explicitly declares that carrier metric data is being used.

### 3.1 Frozen missing-extra-structure list

At least the following extra structure is required before a positive conformal/curvature calculation can be semantically admitted:

1. `FINITE_FACE_COMPLEX` — explicit faces/triangulation, not merely a graph;
2. `BOUNDARY_INTERIOR_TYPING` — for the chosen curvature convention;
3. `METRIC_LAYER_DECLARATION` — carrier Euclidean versus separately declared native metric;
4. for Mode A, `POSITIVE_EDGE_LENGTHS` on every face;
5. for Mode A, `STRICT_TRIANGLE_INEQUALITIES` on every face;
6. `EXACT_CONFORMAL_CHANGE_LAW` — e.g. the selected vertex-scaling law, not an unnamed rescaling;
7. for Mode B, `POSITIVE_RADII`;
8. for Mode B, `CONTACT_OR_INTERSECTION_GRAPH`;
9. for Mode B, `TANGENCY_OR_INTERSECTION_ANGLE_DATA`;
10. for Mode B, `EXACT_RADIUS_ANGLE_EDGE_RELATION`;
11. for packing claims, `NONOVERLAP_TANGENCY_CONDITIONS`;
12. where uniqueness requires it, `BOUNDARY_OR_SCALE_NORMALIZATION`;
13. for target-curvature solving, an explicit `EXISTENCE_DOMAIN`;
14. for uniqueness, a `UNIQUENESS_THEOREM_OR_GAUGE_FIX`;
15. for variational/Jacobian claims, the precise signed/positive weight hypotheses required by the chosen Laplacian/energy model;
16. `EXACT_CERTIFICATE_POLICY` — numerical convergence alone is not theorem evidence.

This list is frozen by this run; no item is silently supplied by carrier coordinates.

## 4. Exact structural law retained under Mode A

### 4.1 Finite Gauss–Bonnet certificate

For a finite triangulated compact 2-manifold with boundary, with Euclidean faces and the curvature convention above,

`sum_v K_v = 2*pi*chi`.

A finite combinatorial proof is available directly from the selected input contract.

Let `V_i` and `V_b` be the numbers of interior and boundary vertices. Since each Euclidean face has angle sum `pi`,

`sum_v K_v = 2*pi*V_i + pi*V_b - pi*F`.

For a triangulated 2-manifold with boundary, write `E_i,E_b` for interior and boundary edges. Then

`3F = 2E_i + E_b`,

and because every boundary component is a cycle,

`E_b = V_b`.

Hence

`2*chi = 2(V-E+F)`

`= 2V_i + 2V_b - 2E_i - 2E_b + 2F`

`= 2V_i + V_b - F`.

Multiplying by `pi` gives exactly the curvature sum above.

This is a finite piecewise-Euclidean identity. It is not a claim that the native Enterprise plane has acquired smooth or native conformal curvature.

### 4.2 Relabeling invariance

The selected outputs depend on face incidence, boundary typing, and declared edge lengths, not vertex names. Reindexing vertices transports the same metric data and therefore preserves the curvature multiset and the global certificate.

The checker verifies this on an equilateral six-triangle disk fan.

### 4.3 Conformal change is not isometry

Under the declared vertex-scaling law, uniform `q_i=2` multiplies each edge of a unit equilateral face by `4`. This is a legal conformal update by the chosen contract but does not preserve lengths. Therefore

`DISCRETE_CONFORMAL_EQUIVALENCE != ISOMETRY`.

## 5. Curvature/update evidence

The deterministic checker establishes the following exact/algebraic cases.

### 5.1 Exact triangle examples

- equilateral `(1,1,1)` is valid and has `cos(theta)=1/2`, hence angle `pi/3`;
- `(3,4,5)` is valid and has the angle opposite `5` equal to `pi/2` because its cosine is exactly `0`;
- the other two exact cosines are `4/5` and `3/5`;
- using the associated exact sine values `3/5` and `4/5` proves algebraically that the two acute angles sum to `pi/2`.

### 5.2 Valid and invalid scale updates

Starting from a unit equilateral face and `l'_{ij}=q_i q_j l_{ij}`:

- `q=(1,1,2)` gives edge lengths `(1,2,2)`, which satisfy all strict triangle inequalities;
- `q=(1,2,10)` gives `(2,20,10)`, which fails because `2+10 <= 20`.

Thus a vertex update is not admissible merely because all scale parameters are positive; post-update metric validity must be checked face by face.

### 5.3 Boundary/interior curvature sums

Two exact equilateral fixtures are checked:

1. tetrahedral sphere: each of four vertices has three incident `pi/3` angles, so each curvature is `pi` and the total is `4*pi = 2*pi*chi(S^2)`;
2. six-triangle disk fan: the interior center sees six `pi/3` angles and has curvature `0`; each of six boundary vertices sees two `pi/3` angles and has curvature `pi/3`; total curvature is `2*pi = 2*pi*chi(D^2)`.

These are checker fixtures for the conditional Euclidean model, not a second native Enterprise application.

## 6. Circle-packing no-go audit

### 6.1 Current canonical cell family

The taskbook freezes positive-area overlap between neighboring canonical cells. Therefore the tangency-packing condition fails immediately.

No classical packing theorem can be invoked merely from the current circle-cell cover.

### 6.2 Invalid radii

`r <= 0` is rejected. Zero and negative radii are explicit regression cases.

### 6.3 Missing normalization and nonuniqueness

Even in a generic two-circle tangency equation, absent a scale normalization,

`(r1,r2,d)=(1,1,2)`

and

`(2,2,4)`

both satisfy `d=r1+r2`. Thus the tangency equations alone do not provide an absolute unique scale. This is an exact nonuniqueness obstruction and explains why a packing/pattern tool must state its normalization or gauge.

This generic obstruction is not asserted to be a current Enterprise packing instance.

## 7. Hard negative boundaries and counterexamples

| Boundary | Exact counterexample / rejection |
|---|---|
| arbitrary graph without faces | no face angles exist, so angle-deficit curvature is undefined |
| triangulation without metric | face combinatorics alone does not determine Euclidean angles |
| invalid triangle | `(1,1,2)` is degenerate and rejected |
| negative edge | `(-1,2,2)` rejected |
| valid positive scale but invalid updated metric | unit face with `q=(1,2,10)` -> `(2,20,10)` |
| zero/negative radii | rejected |
| canonical circle cells as tangency packing | rejected from frozen positive-area overlap |
| carrier angle promoted to native angle | rejected by semantic-layer gate |
| positive cotangent assumption on obtuse face | `(2,3,4)` has angle opposite `4` with cosine `-1/4`; cotangent sign is negative |
| degenerate cotangent face | degenerate triangles are rejected before weight construction |
| target curvature with no existence theorem | solver admission rejected |
| target curvature with no uniqueness/gauge fix | solver admission rejected |
| floating convergence as proof | exact-certificate flag required; numerical-only path rejected |
| conformal equivalence treated as isometry | uniform scaling changes every edge length |
| packing uniqueness without normalization | homothetic tangency solutions give explicit nonuniqueness |

## 8. Semantic-layer ledger

| Object / operation | Admissible layer | Status |
|---|---|---|
| triangular center drawing geometry | carrier Euclidean | usable only when explicitly declared |
| carrier edge lengths | carrier Euclidean metric | valid Mode A input when declared |
| carrier face angles | carrier Euclidean | computable from declared lengths |
| carrier angle deficit | carrier Euclidean curvature | conditional only |
| native Enterprise angle/curvature | native | **not supplied by current Foundation** |
| canonical fixed-radius overlapping circle cells | native cell-cover object plus carrier presentation facts | **not a tangency packing** |
| separately declared radii/intersection angles | conditional pattern layer | possible extra structure, not current Foundation |
| cotangent curvature derivative | weighted Laplacian/energy specialization | no separate global ownership claimed |

Semantic rejection rule frozen by the checker:

`metric_layer=carrier AND requested_output_layer=native AND no explicit native metric declaration -> REJECT`.

## 9. Dedup / ownership table

| Neighboring capability | What it can contribute under the taskbook | Ownership conclusion |
|---|---|---|
| T3 incidence circuits | incidence/cycle structure | insufficient for metric face angles or conformal curvature |
| T7 symmetry | relabeling/equivalence or absence of canonical scale | does not define conformal metric |
| Carrier Voronoi/Delaunay | carrier triangulation / dual-cell input | any distances/angles remain carrier data |
| Laplacian / chip-firing sibling | discrete Laplacian operator family | curvature Jacobian expressed as a weighted Laplacian belongs here unless a genuinely distinct interface survives |
| Weighted Energy sibling | positive quadratic/variational energy layer | any convex-energy target-curvature argument must satisfy that sibling semantic gate; no duplicate global family claimed here |
| Current circle-cell Foundation | fixed overlapping cover and triangular carrier | not circle packing; insufficient for native conformal data |

This task therefore does not establish a new non-duplicate global operator family.

## 10. Enterprise reuse gate

### Application A — conditional carrier triangulation

PASS only as a conditional carrier specialization.

A finite carrier triangulation can be assigned explicitly declared Euclidean edge lengths and then passed to Mode A. The checker uses unit-equilateral carrier fixtures solely to exercise the calculus. Every result is labeled carrier Euclidean.

This does not change the native interpretation of the canonical Enterprise cells.

### Application B — second independently meaningful Enterprise metric complex

NOT ESTABLISHED from the allowed source packet.

The taskbook itself does not provide a second current Enterprise family with independently meaningful edge lengths, radii, or intersection-angle semantics. Under the two-domain rule, this absence is decisive: no second application is fabricated.

The generic tetrahedral sphere, disk fan, and `3-4-5` triangle in the checker are mathematical regression fixtures. They do **not** satisfy the Enterprise two-domain reuse gate by themselves.

Therefore:

`GLOBAL_DISCRETE_CONFORMAL_TOOL_CLAIM -> REJECTED`.

## 11. Candidate API after classification

The following operations are semantically coherent only inside the conditional Mode A domain:

- `VALIDATE_TRIANGULATED_METRIC`
- `ANGLE_DATA`
- `ANGLE_SUM`
- `CURVATURE`
- `CONFORMAL_SCALE`
- `METRIC_AFTER_UPDATE`
- `GAUSS_BONNET_CERT`
- `SEMANTIC_LAYER_CHECK`
- `OBSTRUCTION`

The following are **not** promoted by this run:

- `VALIDATE_CIRCLE_PATTERN_DATA` as a current Foundation tool;
- `RADIUS_UPDATE` for the canonical cells;
- `CURVATURE_JACOBIAN` as a new standalone family;
- `TARGET_CURVATURE_SOLVER` without explicit existence/uniqueness/variational hypotheses.

No reusable source module is created because the positive global-tool acceptance gate is not met.

## 12. Checker

Required executable:

`scripts/tool_discovery_discrete_conformal_circle_pattern_admissibility_check.py`

The checker uses only exact integer/rational arithmetic for the theorem-level regressions.

Observed terminal output:

```text
MISMATCH_COUNT=0
TERMINAL_CHECK=PASS
PRIMARY_CLASSIFICATION=CURRENT_FOUNDATION_EXTRA_STRUCTURE_REQUIRED
COROLLARY=CURRENT_FOUNDATION_NOT_A_CIRCLE_PACKING
COROLLARY=CARRIER_GEOMETRY_SPECIALIZATION_ONLY
MODE_C_OWNERSHIP=SUBTOOL_OF_LAPLACIAN_ENERGY
```

## 13. Classical prior-art / Enterprise novelty ledger

1. **Chosen classical model and theorem input:** piecewise-Euclidean triangulated metric, law-of-cosines face angles, explicit vertex scaling, angle-deficit curvature, finite Gauss–Bonnet identity.
2. **Current Enterprise data:** triangular carrier, fixed radius `1/sqrt(3)` circle cells, positive neighbor overlap, gap-free cover, native `120 degree` right sectors, carrier/native metric separation, as frozen by the taskbook.
3. **Extra structure required:** the exact list in Section 3.1.
4. **Overlap with existing tools:** Mode C is Laplacian/energy specialization; T3/T7 provide incidence/symmetry but not metric conformal data; carrier Voronoi/Delaunay may only supply carrier input.
5. **New Enterprise composition:** semantic-layer guard plus explicit conditional Mode A contract is a useful classification interface, but it does not clear the two-domain/global-tool gate.
6. **Theorem novelty:** none claimed. The mathematical identities used are classical finite Euclidean facts; the contribution of this task is semantic admissibility, ownership, no-go classification, and deterministic regression.

Freeze:

`CONDITIONAL_CLASSICAL_GEOMETRY_TOOL != NATIVE_FOUNDATION`.

## 14. Final stop condition

Hard target reached:

`ENTERPRISE_DISCRETE_CONFORMAL_CIRCLE_PATTERN_TOOL_CLASSIFIED`.

Frozen strongest result:

`CURRENT_FOUNDATION_EXTRA_STRUCTURE_REQUIRED`.

With mandatory corollaries:

`CURRENT_FOUNDATION_NOT_A_CIRCLE_PACKING`;

`CARRIER_GEOMETRY_SPECIALIZATION_ONLY`;

`MODE_C_WEIGHTED_CURVATURE_DERIVATIVE -> SUBTOOL_OF_LAPLACIAN_ENERGY`.

No Foundation change, no forced radius modification, no successor task, and no global discrete-conformal tool claim are made.
