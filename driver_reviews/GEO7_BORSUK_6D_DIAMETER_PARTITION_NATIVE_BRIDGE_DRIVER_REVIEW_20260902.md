# GEO7 Borsuk 6D Diameter-Partition Native Bridge — Driver Review

Driver-ID: `EM-DVR-G6K2P9`  
Role: `RESEARCH_DRIVER`  
Task: `RS-GEO7-BORSUK-6D-DIAMETER-PARTITION-NATIVE-BRIDGE`  
Publication: `TP2-A8D4C16E5B2097F3A621`  
Result: `RR-440E83B6F8C06F0808D8`  
Disposition: `ACCEPTED`  
Terminal: `true`

## Decision

The hard target

`BORSUK_6D_CURRENT_STATUS_AND_NATIVE_DIAMETER_PARTITION_INTERFACE_EXACTLY_CLASSIFIED`

is satisfied at the exact mixed external-status / finite-metric / locked-P000 boundary stated below.

The Result package is writer-conformant. Its Return, deterministic checker, finite certificate, source manifest, dated status matrix and execution record match the Git blobs frozen in the Result manifest. The research branch contains exactly the seven authorized output paths.

The original repository validation failure is not a Borsuk defect: validation stopped in the then-current post-cutover publication envelope because of the unrelated decorated-carrier quarantine-head mismatch before any task-local Borsuk failure was reached. That control-plane defect was subsequently repaired independently. No Borsuk output is altered by this review.

## 1. Accepted external Euclidean status

At the dated source cut `2026-09-02`, accept the retained proved interval

`7 <= b(6) <= 33`,

with exact `b(6)=7` still open.

The lower bound is supplied by the regular six-simplex: its seven vertices are pairwise at the common diameter and therefore require seven strictly-smaller-diameter parts.

The retained upper bound is the published Lassak theorem

`b(n) <= 2^(n-1)+1`,

specialized to `n=6` as `b(6)<=33`.

The source audit keeps publication states separate. The 2026 Tolmachev–Voronov claim `b(4)<=8` is a dimension-four primary preprint result and does not itself improve the six-dimensional bound. The 2026 Ji claim `b(63)>=65` is retained only as a recent dimension-63 preprint frontier and likewise does not change dimension six. Search absence is not treated as a novelty certificate.

This review accepts the status matrix as a dated literature-status statement, not as a theorem that no unpublished or future improvement exists.

## 2. Accepted finite metric theorem

Let `(A,d)` be a finite positive-diameter metric space with diameter `D`, and let `Gamma_D(A)` have edge `xy` exactly when `d(x,y)=D`.

A nonempty block has diameter strictly below `D` exactly when it is independent in `Gamma_D(A)`. Hence the finite Borsuk partition number satisfies

`beta(A,d) = chi(Gamma_D(A))`.

This equivalence is standard prior art and receives no novelty status.

## 3. Accepted unrestricted finite realization theorem

For every finite simple graph `G=(V,E)` with `E` nonempty, define

- `d_G(u,u)=0`;
- `d_G(u,v)=2` for `uv in E`;
- `d_G(u,v)=1` for distinct nonedges.

Then `d_G` is a metric, has diameter `2`, and has maximum-distance graph exactly `G`. Therefore

`beta(V,d_G)=chi(G)`.

The theorem is accepted only for unrestricted finite metrics. It does **not** imply that every finite graph is a Euclidean diameter graph in `R^6`, nor that the resulting finite metric embeds isometrically in Euclidean six-space.

## 4. Six-label exhaustive certificate

On the fixed label set `{1,...,6}`, the deterministic checker exhausts all

`2^15-1 = 32767`

nonempty labeled simple graphs. For every graph it independently checks the `0/1/2` metric, reconstructs the maximum-distance graph, searches all `Bell(6)=203` set partitions for strict diameter decrease, and independently computes chromatic number.

Accepted regression:

- metric failures: `0`;
- maximum-distance reconstruction failures: `0`;
- Borsuk/chromatic mismatches: `0`;
- realized positive-diameter finite Borsuk numbers: exactly `2,3,4,5,6`.

The same six labels and the same axis-label readout admit, for example, a `C5` plus isolated-vertex model with `beta=3` and a perfect-matching model with `beta=2`.

Thus six labels / six named axes alone do not determine a metric, a maximum-distance relation, or a Borsuk partition invariant.

This is a bounded finite non-determination certificate. It is not a theorem about Euclidean dimension six.

## 5. M0–M3 transfer boundary

The typed atlas is accepted as follows.

- `M0`: a finite positive-diameter metric supplies an exact finite Borsuk partition number.
- `M1`: once an exact nonempty maximum-distance relation is supplied, the partition problem is exactly graph coloring.
- `M2`: a connected undirected relation with shortest-path semantics supplies a graph metric conditionally; current locked P000 does not itself select that relation.
- `M3`: generalized group-Borsuk/covering results are reusable only under their external compact-metric, free-action and scale hypotheses.

No current P000 datum in this task supplies the missing native metric, maximum-distance relation, connected path relation or appropriate isometric group action. Consequently no native P000 Borsuk invariant is granted.

## 6. Prior-art and scope guards

Accept the source-manifest classifications at declared strength:

- general metric-space Borsuk number: `EXACT_DUPLICATE`;
- finite maximum-distance coloring equivalence: `EXACT_DUPLICATE`;
- path-distance reduction: `STRICT_ANTECEDENT`;
- generalized group-Borsuk covering interface: `EXACT_DUPLICATE`;
- elementary `0/1/2` graph realization and project-local six-label census: retained without historical novelty claim.

No Euclidean theorem is transferred into P000, no six-axis presentation is promoted to metric dimension, and no `b(6)=7` claim is accepted.

## 7. Parent Objective decision

The parent Objective

`OBJ-EXTERNAL-GEOMETRY-BORSUK-DIAMETER-PARTITION-20260902`

has now met all of its declared success and closure criteria:

1. the dated Euclidean dimension-six status is frozen with publication-state labels;
2. the finite typed diameter/partition interface is exact and the locked-P000 missing-structure obstruction is explicit;
3. every finite claim is checker-bound and every classical transfer is type-mapped;
4. after this review no child terminal Result remains unreviewed.

The fact that exact Euclidean `b(6)` remains open does not prevent closure: this Objective asked for status and interface classification, not a solution of the Euclidean Borsuk problem itself. A P000-native continuation would require new ontology and therefore is not authorized from this Objective.

Close the Objective at Generation 2.

## 8. Independent continuation gate

One genuine external mathematical gap remains: the constructive six-dimensional upper bound is still `33`. A separate Euclidean objective may therefore pressure-test the load-bearing Lassak construction and the dimension-four truncation ideas against `R^6`.

That continuation is justified only if it has a different theorem obligation: either a rigorous all-set improvement `b(6)<=32` (or stronger), or an exact obstruction proving that a frozen Lassak/truncation template cannot beat `33` without a new geometric ingredient. Numerical samples, finite point clouds and heuristic optimization cannot certify a universal Euclidean Borsuk bound.

This external continuation does not reopen the closed native-interface Objective and grants no Working Truth, Foundation authority, canonical P000 promotion, or historical novelty.