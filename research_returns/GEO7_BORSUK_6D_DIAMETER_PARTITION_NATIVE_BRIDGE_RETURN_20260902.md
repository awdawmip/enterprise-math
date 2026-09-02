# GEO7 Borsuk six-dimensional diameter-partition native bridge — Research Return

Task: `RS-GEO7-BORSUK-6D-DIAMETER-PARTITION-NATIVE-BRIDGE`
Publication: `TP2-A8D4C16E5B2097F3A621`
Researcher-ID: `EM-GEO7BORSUK6-A56D6E`
Claim: `chatgpt-geo7-borsuk6-20260902-0928`
Execution branch: `research/geo7-borsuk-6d-diameter-partition-native-bridge-em-geo7borsuk6-a56d6e`
Execution record: `ER-F84AD13414D85EB6B300`

## Terminal verdict

`SUCCESS / CURRENT_B6_STATUS_FROZEN / FINITE_METRIC_BRIDGE_EXACT / SIX_LABEL_P000_TRANSFER_OBSTRUCTED`

Hard target:
`BORSUK_6D_CURRENT_STATUS_AND_NATIVE_DIAMETER_PARTITION_INTERFACE_EXACTLY_CLASSIFIED`

Disposition:
`MET / MIXED EXACT FINITE THEOREM + CURRENT-LANGUAGE NATIVE NO-GO`

Accepted Researcher-lane strength:

- external Euclidean status on 2026-09-02: `7 <= b(6) <= 33`, exact `b(6)=7` remains open;
- finite metric theorem: the strict-smaller-diameter partition number equals the chromatic number of the maximum-distance graph;
- finite realization theorem: every nonempty finite simple graph is exactly the maximum-distance graph of an explicit `0/1/2` metric;
- exhaustive six-label certificate: all `32767` nonempty labeled graphs were checked, with no metric, reconstruction, or Borsuk/chromatic mismatch;
- current-language no-go: six labels or six named axes alone do not determine a native P000 metric, maximum-distance relation, or Borsuk invariant.

No Euclidean theorem is promoted into P000 and no historical novelty is claimed.

## 1. External Euclidean status

For Euclidean `R^d`, let `b(d)` be the least number of strictly smaller-diameter parts needed for every bounded positive-diameter set.

The regular `d`-simplex gives `b(d) >= d+1`; hence `b(6) >= 7`.

Lassak's published 1982 construction gives `b(d) <= 2^(d-1)+1`; hence `b(6) <= 33`.

The retained dated status is therefore:

`7 <= b(6) <= 33`, and `b(6)=7` is open.

Publication-state audit:

- Lassak 1982: published journal article; load-bearing upper bound.
- Zong 2021: peer-reviewed survey context.
- Lopez-Campos, Oliveros, Ramirez Alfonsin 2025: peer-reviewed modern low-dimensional status context.
- Tolmachev-Voronov 2026: primary preprint claiming/proving `b(4)<=8`; dimension 4 only, no direct change to `b(6)`.
- Ji 2026: very recent primary preprint claiming `b(63)>=65`; dimension 63 only, no direct change to `b(6)`.
- Martinez-Figueroa 2024: peer-reviewed generalized Borsuk-graph/group-cover framework.

No preprint is silently upgraded to peer-reviewed fact. Search absence is not used as a novelty certificate.

The exact source and status manifest is frozen at:
`research_artifacts/GEO7_BORSUK_6D_DIAMETER_PARTITION_NATIVE_BRIDGE/source_manifest_20260902.json`

The exact dimension-six status matrix is frozen at:
`research_artifacts/GEO7_BORSUK_6D_DIAMETER_PARTITION_NATIVE_BRIDGE/status_matrix_20260902.json`

## 2. M0/M1 exact coloring theorem

Let `(A,d)` be a finite metric space of positive diameter `D`.
Let `Gamma_D(A)` be the graph on `A` with edge `xy` exactly when `d(x,y)=D`.

A block `B` has `diam(B)<D` if and only if it contains no edge of `Gamma_D(A)`.
Therefore Borsuk-admissible blocks are exactly independent sets, and partitions into such blocks are exactly proper colorings.

Thus:

`beta(A,d) = chi(Gamma_D(A))`.

This equivalence is standard prior art. The triangle inequality is not needed after the exact maximum-distance relation has been supplied, but it remains part of the M0 metric contract.

## 3. M1 unrestricted finite-metric realization

Let `G=(V,E)` be a finite simple graph with `E` nonempty. Define

- `d_G(u,u)=0`;
- `d_G(u,v)=2` for graph edges;
- `d_G(u,v)=1` for distinct nonedges.

Then `d_G` is a metric. For any distinct endpoints the left side of a triangle inequality is at most `2`, while any route through a third distinct vertex has two positive summands, each at least `1`.

Since `E` is nonempty, the diameter is `2`, and the maximum-distance graph is exactly `G`. Hence:

`beta(V,d_G) = chi(G)`.

The nonempty hypothesis is essential for positive diameter: a positive-diameter finite metric necessarily has at least one maximum-distance pair, so the empty graph is not realizable as its maximum-distance graph on a nonsingleton carrier.

This theorem is for unrestricted finite metrics. It does not say that every graph is a Euclidean diameter graph in `R^6`.

Prior-art label: `NO_MATERIAL_MATCH`, explicitly not `PROVEN_NOVEL`.

## 4. Exhaustive six-label certificate

Freeze the carrier and readout:

`A={1,2,3,4,5,6}` and `r(i)=AXIS_LABEL(i)`.

There are `2^15-1=32767` nonempty labeled simple graphs on this carrier.

For every one, the checker:

1. constructs `d_G`;
2. checks all metric axioms and every triangle;
3. recomputes the maximum-distance graph;
4. computes the Borsuk number by exact enumeration of all `Bell(6)=203` set partitions;
5. independently computes the chromatic number by exact backtracking.

Results:

- graphs checked: `32767`;
- metric failures: `0`;
- maximum-distance reconstruction failures: `0`;
- Borsuk/chromatic mismatches: `0`.

Distribution:

| beta | labeled graph metrics |
|---:|---:|
| 2 | 5,176 |
| 3 | 22,377 |
| 4 | 5,042 |
| 5 | 171 |
| 6 | 1 |

Thus the identical six-label readout supports all positive-diameter values `beta=2,3,4,5,6`.

Checker:
`research_checks/GEO7_BORSUK_6D_DIAMETER_PARTITION_NATIVE_BRIDGE_CHECK_20260902.py`

Machine certificate:
`research_artifacts/GEO7_BORSUK_6D_DIAMETER_PARTITION_NATIVE_BRIDGE/finite_metric_certificate_20260902.json`

Expected checker summary:
`PASS GEO7 finite Borsuk bridge: graphs=32767 partitions=203 realized_b=[2, 3, 4, 5, 6] mismatches=0`

## 5. Required nontrivial six-label model

Model A uses maximum-distance graph `C5` on labels `1,2,3,4,5` plus isolated label `6`.
Its `0/1/2` metric has diameter `2`.

The odd cycle forces chromatic number at least `3`, and a 3-coloring exists. Therefore:

`beta_A = 3`.

The frozen checker supplies an exact strict-diameter partition and an independent coloring certificate.

## 6. Same-six-label / same-readout countermodel

Model B has the same carrier and identical readout, but maximum-distance graph equal to the perfect matching `{12,34,56}`.

Its `0/1/2` metric has exact Borsuk number:

`beta_B = 2`.

One strict-diameter partition is `{1,3,5} | {2,4,6}`.

Hence the same six labels and same axis-label readout satisfy `beta_A=3` and `beta_B=2`.

Therefore:

`SIX LABELS / SIX NAMED AXES DO NOT DETERMINE A BORSUK INVARIANT`.

They do not determine a metric, a maximum-distance graph, or a strict-diameter partition number.

## 7. M2 relation/path-distance interface

If a connected undirected simple native relation `R` is independently typed, shortest relation-path length is an ordinary finite graph metric `d_R`.

Then the M0 theorem applies exactly:

`beta(A,d_R) = chi(maximum-distance graph of d_R)`.

The checker reuses `enterprise_math.geometry.graph_distance` on the six-cycle `C6`:

- graph-metric diameter `3`;
- maximum-distance graph `{14,25,36}`;
- exact Borsuk number `2`.

This is conditional, not a current P000 theorem. The accepted GEO6 relation-distance result says locked P000 does not itself choose the unit-step relation, and the accepted relation-selector review does not promote a unique native contact/exclusion/support relation into a distance selector.

Disconnected relation input needs a component restriction or an explicitly typed extended-metric convention.

## 8. M3 generalized Borsuk graph / covering interface

Martinez-Figueroa 2024 gives an exact external theorem in a different typed setting: a compact metric space, a free finite-group action, and small-scale `G`-Borsuk graphs whose chromatic behavior is related to a `G`-covering number under the paper's hypotheses.

This is an exact conditional group/topological interface. It is not automatically the ordinary maximum-distance graph of the Euclidean Borsuk problem.

Current P000 supplies neither the required native metric nor the required free finite-group isometric action in this task. Thus M3 is a conditional transfer schema only.

## 9. Typed M0-M3 atlas

| Interface | Minimum typed input | Exact output | Current status |
|---|---|---|---|
| M0 | finite positive-diameter metric/pseudometric with ordered values | Borsuk partition number | exact |
| M1 | exact nonempty maximum-distance relation | graph chromatic number | exact |
| M2 | connected undirected relation plus shortest-path semantics | path metric and its max-distance graph | exact conditional |
| M3 | compact metric space plus free finite-group action and scale hypotheses | generalized Borsuk graph / covering invariant | exact under external hypotheses |

For M1, every nonempty simple graph has an unrestricted finite-metric realization by the `0/1/2` construction. That statement does not transfer to Euclidean realization classes.

## 10. Six-dimensional meaning audit

Six named axis types: insufficient, by the exhaustive same-readout family.

Six coordinates: insufficient without a metric/relation law; coordinates may be bookkeeping only.

Rank-six action module: potentially constraining, but still does not by itself choose a positive-diameter function.

Six-parameter relation family: insufficient until a selector and aggregation/path law is typed.

Therefore the Euclidean count `d+1=7` cannot be imported from the word "six-dimensional" in P000.

## 11. Transfer matrix

| Statement | Euclidean | finite metric | graph | current P000 |
|---|---|---|---|---|
| regular-simplex `b(6)>=7` | exact | Euclidean finite witness | `K7` witness | no automatic transfer |
| Lassak `b(6)<=33` | exact | applies to Euclidean finite subsets | not generic graph bound | no automatic transfer |
| diameter-graph coloring | finite Euclidean sets | exact | exact | conditional on native metric/max relation |
| `0/1/2` graph realization | not Euclidean-6 in general | exact | every nonempty simple graph | countermodel tool only |
| shortest-path metric | comparison model | exact | exact | conditional on typed native relation |
| generalized `G`-Borsuk graph | separate external setting | metric/group | graph/topological | no transfer without metric + free action |
| six labels imply 7 parts | no | refuted | refuted | refuted at current language |

## 12. Prior-art classification

- M0 metric-space Borsuk number: `EXACT_DUPLICATE`.
- finite max-distance graph coloring equivalence: `EXACT_DUPLICATE`.
- `0/1/2` realization of every nonempty finite simple graph: `NO_MATERIAL_MATCH`; no novelty claim.
- exhaustive six-label `beta=2..6` certificate: `NO_MATERIAL_MATCH`; bounded project certificate, no novelty claim.
- M2 path-metric reduction: `STRICT_ANTECEDENT`.
- M3 group-covering theorem: `EXACT_DUPLICATE`.
- current P000 six-label non-determination: `NO_MATERIAL_MATCH`; project-typing statement, no external novelty claim.

## 13. Method, residue, and handoff

Method harvest:
`RESULT_ONLY / FINITE_MAX_DISTANCE_GRAPH_REALIZATION_AND_EXHAUSTIVE_SIX_LABEL_CERTIFICATE`

No new general-purpose project tool is proposed.

Unresolved residue:

- the exact Euclidean value `b(6)` remains open inside the retained interval `7..33`;
- current P000 still lacks a native Borsuk invariant;
- a native continuation requires independent acceptance of at least one metric, exact max-distance relation, connected path relation, or appropriate group-action/covering structure.

Driver recommendation:

Review this Result at exactly the strength

`B6_EXTERNAL_STATUS_7_TO_33_OPEN_AND_FINITE_METRIC_BORSUK_EQUALS_MAX_DISTANCE_CHROMATIC_WITH_SIX_LABEL_NATIVE_NONDETERMINATION`.

Do not publish a successor that merely chooses a metric by fiat. A successor is justified only after independent P000 work supplies a native selector, or under a separately published external Euclidean `b(6)` bound-improvement task.

No Working Truth, Foundation authority, native ontology elevation, Euclidean-to-P000 theorem transfer, canonical promotion, or historical novelty is requested.
