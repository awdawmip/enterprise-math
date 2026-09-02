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

The result has three independent parts.

1. **External Euclidean status, dated 2026-09-02:** the retained proved interval is
   \[
   \boxed{7\le b(6)\le 33},
   \]
   and the equality `b(6)=7` remains open.
2. **Finite exact bridge:** for every finite positive-diameter metric space, strict-smaller-diameter partition number equals the chromatic number of its maximum-distance graph. Conversely, every **nonempty** finite simple graph is the maximum-distance graph of an explicit `0/1/2` metric.
3. **Native boundary:** a six-axis/six-label presentation does not determine a metric, maximum-distance relation, or Borsuk number. On the same six labels and identical axis-label readout, exact finite metrics with Borsuk numbers `2` and `3` are exhibited; in fact the six-label `0/1/2` family realizes every value `2,3,4,5,6`. Current locked P000 therefore has no native Borsuk invariant until a relation/metric selector is independently typed.

No Euclidean theorem is transferred into P000, no classical dimension is identified with a native six-label presentation, and no novelty status is claimed.

---

## 1. External Euclidean status of `b(6)`

For Euclidean `R^d`, write `b(d)` for the least integer such that every bounded positive-diameter set can be partitioned into `b(d)` subsets of strictly smaller Euclidean diameter.

### 1.1 Lower bound

The standard regular-simplex obstruction gives
\[
b(d)\ge d+1.
\]
Indeed, the `d+1` vertices of a regular `d`-simplex are pairwise at the common diameter, so every smaller-diameter part contains at most one vertex. At `d=6`,
\[
\boxed{b(6)\ge 7}.
\]

The 2026 Tolmachev–Voronov preprint explicitly records this lower bound in its introduction.

### 1.2 Upper bound

Lassak's published 1982 construction gives the general small-dimension constructive estimate
\[
b(d)\le 2^{d-1}+1.
\]
The 2026 Tolmachev–Voronov paper explicitly identifies this as the best constructive general upper bound in small dimensions for `d>=4` before their dimension-4-only improvement. Hence
\[
\boxed{b(6)\le 2^5+1=33}.
\]

No checked source through 2026-09-02 supplied a stricter six-dimensional universal upper bound.

### 1.3 Exact status

Combining the two retained bounds:
\[
\boxed{7\le b(6)\le 33}.
\]

The exact equality `b(6)=7` is **open**. A modern peer-reviewed account before the 2026 preprints states that the Borsuk conjecture remained open in dimensions `4<=d<=63`; the May 2026 Tolmachev–Voronov preprint still states that the conjecture is known for `d<=3` and fails for `d>=64`.

The August 2026 Ji preprint claims a 321-point counterexample in `R^63`, proving `b(63)>=65` if correct. This is a very recent primary preprint, not a peer-reviewed fact in this return. Even if its claim is fully verified, it changes the high-dimensional failure frontier only; it does not improve either side of the six-dimensional interval.

### 1.4 Mandatory nearby-dimension audit

| Source | Claim | State on 2026-09-02 | Effect on `b(6)` |
|---|---|---|---|
| Tolmachev–Voronov, arXiv:2605.19068 | `b(4)<=8` | primary preprint, submitted 2026-05-18 | none directly; it is an `R^4` construction |
| Ji, arXiv:2608.12561 | `b(63)>=65` | very recent primary preprint, submitted 2026-08-12 | none directly; dimension 63 only |
| Lassak (1982) | `b(d)<=2^(d-1)+1` | published journal article | load-bearing six-dimensional upper `33` |
| regular simplex | `b(d)>=d+1` | classical exact obstruction | load-bearing six-dimensional lower `7` |

Search absence is not used as novelty evidence. The source manifest records the exact publication-state labels and consumed claims.

---

## 2. M0 — finite metric interface

Let `(A,d)` be a finite metric space with positive diameter
\[
D=\max_{x,y\in A} d(x,y)>0.
\]
Define the maximum-distance graph
\[
\Gamma_D(A)=(A,E_D),\qquad
\{x,y\}\in E_D \iff d(x,y)=D.
\]

For a partition `A=A_1 sqcup ... sqcup A_k` into nonempty blocks, call it Borsuk-admissible when every block has diameter `<D`.

### Theorem M0/M1-A — exact diameter-graph coloring equivalence

\[
\boxed{\beta(A,d)=\chi(\Gamma_D(A))},
\]
where `beta(A,d)` is the least number of strict-smaller-diameter blocks.

**Proof.** A block `B` has `diam(B)<D` exactly when it contains no pair at distance `D`; equivalently, `B` is an independent set of `Gamma_D(A)`. Thus Borsuk-admissible partitions are exactly proper vertex colorings, with blocks equal to the nonempty color classes. Minimizing the number of blocks/colors gives the equality. QED.

The triangle inequality is not used in this equivalence once the exact maximum-distance relation is already supplied. It is, however, part of M0 when the input is claimed to be a metric rather than merely a symmetric dissimilarity.

This theorem is standard prior art and receives **no novelty claim**.

---

## 3. M1 — maximum-distance relation only

The relation-only interface is exact if its semantics are frozen:

- finite carrier `A`;
- symmetric irreflexive relation `F`;
- explicit assertion that `F` is **exactly** the set of pairs realizing the global positive diameter.

Then the partition number is simply `chi(A,F)`.

The task also asks which abstract relations are realizable as maximum-distance graphs.

### Theorem M1-B — unrestricted finite-metric realization

Let `G=(V,E)` be a finite simple graph with `E != emptyset`. Define
\[
d_G(u,v)=
\begin{cases}
0,&u=v,\\
2,&\{u,v\}\in E,\\
1,&u\ne v,\ \{u,v\}\notin E.
\end{cases}
\]

Then:

1. `d_G` is a metric;
2. `diam(V,d_G)=2`;
3. the maximum-distance graph of `(V,d_G)` is exactly `G`;
4. its Borsuk number is exactly `chi(G)`.

**Triangle proof.** For distinct endpoints, `d_G(u,v)<=2`. For any intermediate `w` distinct from both, both summands on the right are at least `1`, hence
\[
d_G(u,v)\le2\le d_G(u,w)+d_G(w,v).
\]
Cases with repeated vertices are immediate.

The nonempty-edge hypothesis is essential for exact realization at positive diameter: any positive-diameter finite metric has at least one pair attaining its maximum, so an empty graph cannot be its maximum-distance graph on a nonsingleton carrier.

This shows that under the class of **all finite metrics**, graph realizability imposes almost no restriction beyond nonemptiness. This statement must not be imported into Euclidean `R^6`: Euclidean diameter graphs obey additional realization constraints.

Targeted prior-art search found the general metric Borsuk framework and the standard diameter-graph/coloring translation, but no load-bearing exact source for this particular `0/1/2` realization lemma. It is therefore labeled `NO_MATERIAL_MATCH`, explicitly **not** `PROVEN_NOVEL`.

---

## 4. Exact six-label census

Freeze the carrier and readout
\[
A=\{1,2,3,4,5,6\},\qquad r(i)=\text{AXIS_LABEL}(i).
\]

There are `2^15-1=32767` nonempty labeled simple graphs on this carrier. For every one, the checker constructs `d_G`, verifies every metric triangle, recomputes the maximum-distance graph, independently computes:

- the Borsuk number by restricted-growth enumeration of the `Bell(6)=203` set partitions, ordered by block count; and
- the chromatic number by a separate exact backtracking coloring algorithm.

Result:

- nonempty graph metrics checked: `32767`;
- metric failures: `0`;
- maximum-distance graph reconstruction failures: `0`;
- Borsuk/chromatic mismatches: `0`.

Distribution by exact Borsuk number:

| `beta` | labeled nonempty graph metrics |
|---:|---:|
| 2 | 5,176 |
| 3 | 22,377 |
| 4 | 5,042 |
| 5 | 171 |
| 6 | 1 |

Hence the same six labels support
\[
\boxed{\beta\in\{2,3,4,5,6\}}
\]
under exact finite metrics.

This is a bounded exhaustive project certificate, not an external novelty theorem.

---

## 5. Required nontrivial six-label model

Take the six labels and maximum-distance graph
\[
G_A=C_5\sqcup K_1
\]
with edges
\[
12,23,34,45,51,
\]
and let `d_A=d_{G_A}`.

Then `diam(A)=2`. The odd 5-cycle proves `chi(G_A)>=3`. A 3-coloring exists, for example
\[
1,3,6\mapsto 0,\qquad
2,4\mapsto 1,\qquad
5\mapsto 2.
\]
Every color class has only distances `0` or `1`, hence diameter `<2`. Therefore
\[
\boxed{\beta(A,d_A)=3}.
\]

The deterministic checker supplies both lower and upper certificates.

---

## 6. Same-six-label / same-readout countermodel

On the **same** carrier and with the **same** readout `r(i)=AXIS_LABEL(i)`, define a second metric by the perfect-matching maximum-distance graph
\[
G_B=\{12,34,56\},
\qquad d_B=d_{G_B}.
\]

The graph is nonempty and bipartite, so
\[
\boxed{\beta(A,d_B)=2}.
\]
An exact smaller-diameter partition is
\[
\{1,3,5\}\sqcup\{2,4,6\}.
\]

Thus the same six-label presentation and same readout admit
\[
\beta(A,d_A)=3\ne2=\beta(A,d_B).
\]

Consequently:

\[
\boxed{\text{SIX LABELS / SIX AXES DO NOT DETERMINE A BORSUK INVARIANT.}}
\]

They do not determine the metric, the maximum-distance relation, or the strict-diameter partition number. A dimension label is presentation metadata until additional structure tells the mathematics how labels generate distance.

---

## 7. M2 — relation/path-distance input

The accepted GEO6 relation-distance result already supplies the correct conditional interface. If an undirected simple Cell relation `R` is independently declared and the relevant finite carrier is connected, then
\[
d_R(x,y)=\text{shortest number of R-steps from x to y}
\]
is an ordinary finite graph metric.

M0 therefore applies:
\[
\beta(A,d_R)
=
\chi\bigl(\{xy:d_R(x,y)=\operatorname{diam}_R(A)\}\bigr).
\]

The checker reuses `enterprise_math.geometry.graph_distance` on the six-cycle `C6`:

- graph-metric diameter: `3`;
- maximum-distance graph: perfect matching `{14,25,36}`;
- exact Borsuk number: `2`.

This is a legal **conditional** native-style construction. It is not yet a P000 theorem because the accepted GEO6 result explicitly states that locked P000 does not itself select the unit-step relation, and the accepted native relation-selector review does not promote carrier contact/exclusion/support into a unique native distance relation.

For disconnected relation input, ordinary shortest-path distance is not finite between components; a component restriction or an explicitly typed extended-metric convention is required.

---

## 8. M3 — generalized Borsuk graph / covering input

Martinez-Figueroa (2024) studies a different but relevant exact interface:

- a compact metric space `M`;
- a finite group `G` acting freely;
- the `G`-Borsuk graph at scale `epsilon`, with edges defined through nonidentity translates;
- for sufficiently small `epsilon`, chromatic number governed by the `G`-covering number under the paper's hypotheses.

This is an exact theorem **inside that typed group-action/compact-metric setting**. It is not the same object as a maximum-distance graph and is therefore classified as an adjacent/topological transfer route for the present Euclidean diameter problem unless a reduction is separately proved.

Current P000 supplies neither the necessary native metric nor the required free finite-group isometric action as part of this task. Hence M3 contributes a reusable conditional schema, not a current P000 Borsuk theorem.

---

## 9. Typed M0–M3 atlas

| Interface | Required typed data | Exact output | Conversion status |
|---|---|---|---|
| M0 finite metric | finite `A`, exact ordered distance, symmetry/diagonal/triangle, positive attained max | `beta(A,d)` | **EXACT** to M1 via max-distance graph |
| M1 max-distance relation | finite `A`, nonempty symmetric irreflexive `F`, semantics `F=argmax d` | `chi(A,F)` | **EXACT** once `F` is genuinely the max relation; every nonempty simple `F` has some unrestricted finite metric realization |
| M2 relation/path metric | typed connected undirected relation `R` | shortest-path metric and its antipodal/max-distance graph | **EXACT CONDITIONAL**; blocked natively until `R` is selected |
| M3 group/topological Borsuk graph | compact metric `M`, free finite-group action, scale hypotheses | chromatic / `G`-covering invariant | **EXACT UNDER EXTERNAL HYPOTHESES**, otherwise adjacent method |

A pseudometric can be handled in M0 if positive diameter and exact comparison are retained; distinct zero-distance points do not affect the M0/M1 coloring proof. If one instead starts with a relation only, “diameter” is semantic shorthand until a dissimilarity/metric realization is supplied.

---

## 10. Six-dimensional meaning audit

### Six named axis types

**Insufficient.** The exhaustive six-label family above proves this directly: identical six labels/readout support Borsuk numbers `2` through `6`.

### Six-coordinate presentation

**Insufficient without a metric law.** Coordinates can be bookkeeping only. The accepted GEO6 Falconer lane already enforces this distinction: its `Z^6` chart is a declared test chart, while shortest relation-path semantics are primary.

### Rank-six action module

**Potentially meaningful only with extra structure.** A module/action can constrain allowed transformations but does not by itself choose a positive diameter function or a max-distance relation.

### Six-parameter relation family

**Potentially meaningful only after a selector law.** A family of relations does not determine which relation, aggregation, or path rule defines diameter.

Therefore no current path allows the Euclidean constant `d+1=7` to be read off from the word “six-dimensional” in P000.

---

## 11. Transfer matrix

| Claim/method | Euclidean theorem | finite metric theorem | graph theorem | topological/group cover | current P000 consequence |
|---|---:|---:|---:|---:|---|
| regular simplex lower `b(6)>=7` | YES | finite Euclidean witness | `K7` coloring witness | no | NO automatic transfer |
| Lassak `b(6)<=33` | YES | applies to Euclidean finite subsets as a consequence | not a generic graph bound | covering construction | NO automatic transfer |
| diameter graph coloring | finite Euclidean sets | YES | YES | no | CONDITIONAL on native metric/max relation |
| `0/1/2` graph realization | not Euclidean-6 in general | YES | every nonempty simple graph | no | countermodel tool only |
| shortest-path relation metric | comparison model | YES | YES | no | CONDITIONAL on typed native relation |
| generalized `G`-Borsuk graph | not ordinary diameter partition by default | metric/group setting | YES | YES | NO without metric + free action |
| six labels imply `7` parts | NO | REFUTED | REFUTED by same-label family | no | REFUTED at current language |

---

## 12. Prior-art classification

| Project-local statement | Classification | Reason |
|---|---|---|
| M0 Borsuk number for bounded metric spaces | `EXACT_DUPLICATE` | general metric Borsuk numbers are already studied |
| finite max-distance graph coloring equivalence | `EXACT_DUPLICATE` | standard diameter-graph formulation |
| `0/1/2` metric realizes every nonempty finite simple graph | `NO_MATERIAL_MATCH` | no exact load-bearing match found; elementary proof retained; **not novelty** |
| six-label spectrum `beta=2..6` | `NO_MATERIAL_MATCH` | bounded project certificate/corollary; **not novelty** |
| M2 path-metric reduction | `STRICT_ANTECEDENT` | follows from the general metric/diameter-graph framework once a connected relation is typed; graph-Borsuk work is adjacent |
| M3 group-covering theorem | `EXACT_DUPLICATE` | Martinez-Figueroa 2024 under the exact external hypotheses |
| current P000 six-label non-determination | `NO_MATERIAL_MATCH` | project-typing statement supported by same-readout countermodels; external novelty not asserted |

---

## 13. Source and publication-state boundary

Load-bearing external sources are frozen in
`research_artifacts/GEO7_BORSUK_6D_DIAMETER_PARTITION_NATIVE_BRIDGE/source_manifest_20260902.json`.

The b(6) status is separately frozen in
`research_artifacts/GEO7_BORSUK_6D_DIAMETER_PARTITION_NATIVE_BRIDGE/status_matrix_20260902.json`.

Important publication-state separations:

- Lassak 1982: published journal article;
- Zong 2021: peer-reviewed version of record;
- Lopez-Campos–Oliveros–Ramirez Alfonsin 2025: peer-reviewed journal article;
- Martinez-Figueroa 2024: peer-reviewed journal article;
- Tolmachev–Voronov 2026 `b(4)<=8`: preprint;
- Ji 2026 `b(63)>=65`: very recent preprint;
- Caceres–Garijo–Marquez–Silveira 2026 graph variant: preprint.

No preprint is silently upgraded to peer-reviewed status.

---

## 14. Deterministic finite certificate

Checker:

`research_checks/GEO7_BORSUK_6D_DIAMETER_PARTITION_NATIVE_BRIDGE_CHECK_20260902.py`

Frozen machine output:

`research_artifacts/GEO7_BORSUK_6D_DIAMETER_PARTITION_NATIVE_BRIDGE/finite_metric_certificate_20260902.json`

Expected summary:

`PASS GEO7 finite Borsuk bridge: graphs=32767 partitions=203 realized_b=[2, 3, 4, 5, 6] mismatches=0`

The checker uses exact integer distances only, enumerates all nonempty simple graphs on six fixed labels, and reuses the existing project `graph_distance` helper for the M2 regression. No floating-point geometry or Euclidean embedding solver is used.

Method harvest:

`RESULT_ONLY / FINITE_MAX_DISTANCE_GRAPH_REALIZATION_AND_EXHAUSTIVE_SIX_LABEL_CERTIFICATE`

No new general-purpose project tool is proposed.

---

## 15. Unresolved residue

The research does **not** determine the exact Euclidean value `b(6)`. The retained external interval is still
\[
7\le b(6)\le33.
\]

It also does not define a native P000 Borsuk number. The exact missing object is a typed native structure that selects at least one of:

1. a finite positive-diameter metric/pseudometric;
2. an exact maximum-distance relation;
3. a connected native relation from which shortest-path metric is authorized;
4. a group-action/covering structure satisfying an external transfer theorem.

The six-label counterfamily proves that the dimension label alone cannot fill this gap.

## 16. Driver recommendation

`DRIVER_REVIEW` this mixed terminal result at exactly the following strength:

`B6_EXTERNAL_STATUS_7_TO_33_OPEN_AND_FINITE_METRIC_BORSUK_EQUALS_MAX_DISTANCE_CHROMATIC_WITH_SIX_LABEL_NATIVE_NONDETERMINATION`

If accepted, do **not** publish a successor that merely chooses a metric by fiat. A future successor is justified only if independent P000 work supplies a native metric/relation/action selector, or if the Driver deliberately opens an external Euclidean `b(6)` bound-improvement task with its own geometric proof obligations.

No Working Truth, Foundation authority, native ontology elevation, Euclidean-to-P000 theorem transfer, or historical novelty is requested.
