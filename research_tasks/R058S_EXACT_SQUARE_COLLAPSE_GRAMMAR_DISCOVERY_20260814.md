# RS-R058S-EXACT-SQUARE-COLLAPSE-GRAMMAR-DISCOVERY

Status: `DRIVER_ISSUED / NEW_SIBLING_GENERATION`
Date: `2026-08-14`
Mode: `RESEARCHER`
identity_policy: `AUTO_RESOLVE_OR_ALLOCATE`
identity_lane: `R058S_EXACT_SQUARE_COLLAPSE`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## 0. Purpose

This generation starts a new sibling discovery branch whose goal is to learn collapse laws from exact, simpler geometric teachers before returning to circles/spheres.

The first teacher is the Euclidean square. The task is **not** to study squares for their own sake and is **not** to prove classical square formulas. The task is to use squares as a controlled laboratory in which local boundary-collapse generators can be separated into straight-edge and corner roles.

The existing R055/R056/R057/R057X/R057Y generations remain immutable and independent. Nothing in this task may rewrite their frozen bytes or retroactively reinterpret their fitted coefficients as if they had been discovered here.

## 1. Research question

Given a square digitized on the same normalized triangular-lattice / regular-hexagonal Voronoi carrier used by the recent geometry work, can a finite local packet-collapse grammar recover the exact teacher perimeter

`P_square = 4 s`

across scale, phase, and orientation?

More specifically, when a contiguous boundary packet of `k` exposed Voronoi edges is replaced by one or more endpoint chords, does the discovered rule naturally separate into something like

`straight side -> one whole chord`

and

`corner neighborhood -> two or more chord blocks`

without being told where the teacher corner is?

The primary object is therefore a discrete collapse-count / ordered-composition law

`packet -> ordered composition of k -> sum of block endpoint chords`.

The task must discover rather than assume the correct collapse count `c(packet)`.

## 2. Epistemic and semantic status

This is a supervised discovery/calibration generation.

Allowed:

- exact classical square teacher;
- exact target perimeter `4s`;
- post-selection and high-capacity benchmark search;
- teacher-supervised loss;
- later compression of a successful lookup into a smaller grammar.

Required provenance label for target-informed discoveries:

`SQUARE_TEACHER_SUPERVISED_DISCOVERY`

Forbidden:

- later calling a teacher-selected rule blind or target-free;
- importing a classical square/corner object into the native substrate and calling it N0;
- claiming a native/foundational theorem merely because a teacher-supervised grammar fits.

Semantic typing:

- triangular-lattice adjacency: declared substrate relation;
- axial/Cartesian coordinates and explicit Voronoi embedding: `I0_IMPLEMENTATION_CARRIER`;
- local packet extraction / ordered-composition choice: `N1_DERIVED_OPERATIONAL_SEMANTICS`;
- chord length / estimated perimeter / collapse count summaries: `N2_READOUT_COLLAPSE`;
- Euclidean square, side length, perpendicularity, teacher perimeter `4s`: `N3_CONTINUUM_CLASSICAL`.

This generation is a Foundation-adjacent inverse problem in the sense:

`known exact engineering/classical success -> surviving local collapse structure -> later transfer test`.

It is not yet a Foundation proof.

## 3. Hard firewalls

Until the first serious R058S grammar checkpoint is frozen, do not use the fitted R057-A/G/X grammar outputs as search hints.

Permitted reuse from R057-era code:

- generic triangular-lattice coordinate utilities;
- regular-hexagonal Voronoi boundary extraction;
- corrected spatial-D6 reflection/orientation implementation;
- hashing/checker/publication utilities.

Forbidden before the first serious checkpoint:

- fitted `WHOLE_CHORD + AREA + RUN` coefficients;
- D1/D2/D3 winner information as a search prior;
- R057 packet-class lookup choices;
- R057 exception predicates;
- circle/arc/tangent/radius/circumference targets;
- classical pi as a target or feature.

After the first serious R058S checkpoint, cross-generation transfer may be authorized by the Driver in a later stage.

## 4. Teacher square and carrier

### 4.1 Triangular lattice

Use axial lattice coordinates `(a,b)` with nearest-neighbor Euclidean spacing normalized to `1` and quadratic form

`Q(a,b) = a^2 + ab + b^2`.

Each occupied lattice site represents its regular-hexagonal Voronoi cell.

The physical Voronoi boundary-edge length must be derived and frozen independently in Stage 0; do not silently assume an old unit conversion.

### 4.2 Square orientation without trigonometric/pi parameterization

A square orientation is specified by a primitive nonzero axial vector

`d=(a,b)`.

Let its Euclidean embedding be the first square axis. Construct an integer axial perpendicular direction using the triangular-lattice bilinear form, for example a primitive reduction of

`d_perp = (a+2b, -(2a+b))`,

and verify exact Euclidean orthogonality in the chosen embedding.

Normalize the two Euclidean directions to unit vectors `u,v`.

Teacher square:

`S(s,c,d) = {x : |<x-c,u>| <= s/2 and |<x-c,v>| <= s/2}`.

Teacher perimeter is exactly

`P=4s`.

No trigonometric angle or pi value is needed to define the square.

### 4.3 Digitization

Default digitization:

`occupied site <=> lattice-site center lies in the closed teacher square`.

Stage 0 must freeze:

- exact/high-precision membership predicate;
- equality/tie rule;
- threshold-fallback protocol;
- topology audit;
- boundary orientation convention.

For every generated sample audit at least:

- finite nonempty cluster;
- connectedness;
- hole-free status;
- one oriented exposed-edge boundary cycle;
- occupied-left / CCW convention;
- deterministic byte reproduction.

If an exact-boundary center tie occurs, record it explicitly; do not silently perturb the teacher.

## 5. Frozen discovery registry

Stage 0 must freeze the registry **before corpus generation or grammar search**.

### 5.1 Discovery side lengths

`S_DISC = {12,16,24,32,48,64,96,128}`.

### 5.2 Discovery orientations

Use primitive axial directions

`D_DISC = {(1,0),(3,1),(2,1),(3,2)}`

subject to Stage-0 duplicate/equivalence audit under spatial D6 and square symmetry. If two are equivalent, replace only during Stage 0 and record the replacement before hashing.

### 5.3 Discovery center phases

Use 12 rational phases in one lattice fundamental cell:

`P_DISC(j) = (j/13, (5j mod 13)/13), j=1..12`,

interpreted in the axial lattice basis.

Expected nominal discovery sample count before any equivalence removal:

`8 * 4 * 12 = 384`.

Every removal/replacement must be explicit in the frozen registry.

## 6. Frozen square holdout registry

Freeze but **do not evaluate or inspect outcomes during the first serious search**.

### 6.1 Holdout side lengths

`S_HOLD = {20,28,40,56,80,112,160,224}`.

### 6.2 Holdout orientations

Initial candidates:

`D_HOLD = {(5,1),(7,2),(5,3),(4,3)}`

subject to the same Stage-0 D6/square-equivalence audit. Holdout orientations must not duplicate discovery orientations after canonicalization.

### 6.3 Holdout phases

`P_HOLD(j) = (j/17, (7j mod 17)/17), j=1..12`.

The holdout parameter registry may be hashed and published. The holdout corpus/perimeter predictions must not be generated or consumed until a later Driver authorization after the first serious grammar checkpoint.

This is a provenance firewall, not a claim that the formula `4s` is secret.

## 7. Boundary packet protocol

Traverse the exposed Voronoi boundary cyclically with occupied interior on the left.

For each `k=1..8`, every boundary edge index defines one cyclic contiguous `k`-edge packet.

The packet record must contain enough exact data to reproduce:

- ordered boundary vertices;
- ordered edge directions;
- turn word;
- endpoint displacement/chord;
- every candidate block endpoint chord;
- spatial-D6 canonical class.

Reflection semantics must be spatial reflection followed by restoration of the occupied-left / CCW traversal convention. Do not identify words by naive free-word reversal.

Teacher-side labels such as `SIDE_INTERIOR`, `CORNER_NEAR`, teacher corner index, distance to teacher corner, square orientation, side length, phase, or teacher perimeter are **forbidden grammar inputs**.

They may be computed only in the post-search interpretation lane after the grammar is frozen.

## 8. Ordered-composition collapse grammar

For a packet of `k` boundary edges, an admissible collapse composition is an ordered composition

`pi = (m_1,...,m_r)`,

where each `m_j >= 1` and

`sum_j m_j = k`.

The packet is split into consecutive blocks of those edge counts. Each block is replaced by the Euclidean chord joining its two block endpoints.

Define

`C_pi(packet) = sum_j chord_length(block_j)`.

Important anchor compositions:

- identity/raw-boundary: `(1,1,...,1)`;
- whole chord: `(k)`;
- two-block split: `(t,k-t)`;
- unrestricted ordered compositions: all `2^(k-1)` possibilities.

Collapse count:

`c_pi = number of blocks = r`.

Do not assume `c=1` on sides or `c=2` at corners; those are hypotheses to test after discovery.

## 9. Cyclic local readout without segmentation optimization

For a fixed packet length `k` and local grammar `g` mapping a packet's allowed local representation to an ordered composition, define the whole-boundary estimator

`P_hat_{k,g}(C) = (1/k) * sum_i C_{g(packet_i)}(packet_i)`,

where the sum is over **all cyclic starting edges**.

The factor `1/k` is mandatory.

This readout is chosen to remove arbitrary packet-start segmentation and active-set optimization from the first square generation.

Sanity requirement:

for the identity composition on every packet,

`P_hat = raw digital Voronoi perimeter`.

Stage 0 must prove/check this identity exactly or to the strongest exact-number representation supported by the implementation.

## 10. Search-capacity ladder

The first serious search must include distinct capacity classes and preserve their genealogy.

### G0 — fixed composition by k

For each `k=2..8`, exhaustively evaluate every ordered composition of `k` used uniformly for all packets.

Purpose: establish whether whole-chord or another universal partition dominates before any class conditioning.

### G1 — compact local rule grammar

Freeze a bounded grammar before search.

Allowed primitive inputs may include only teacher-free local packet information, for example:

- edge-direction word;
- turn word / turn counts;
- run boundaries;
- endpoint displacement;
- prefix/suffix chord vectors;
- exact dot/determinant comparisons between prefix/suffix chords;
- D6-invariant or equivariant combinations of the above.

The grammar may choose among ordered compositions of `k`.

Bound the rule-tree/program size and record description units.

The grammar must not contain teacher-side/corner labels or sample metadata.

### G2 — high-capacity packet-class lookup benchmark

Allow a canonical packet-class -> ordered-composition lookup as a high-capacity reference.

This is explicitly a benchmark and may surface-fit the discovery corpus.

It must never be misreported as a compact law merely because it has low error.

### G3 — post-hoc compression

Only after G2 is frozen may its regularities inspire a smaller G1-style grammar.

Record the genealogy honestly as post-selection/compression.

## 11. Loss and reporting

Every square sample receives equal sample weight.

For each candidate report at least:

- signed perimeter error `P_hat - 4s`;
- absolute error;
- pooled RMSE in physical length units;
- pooled MAE;
- worst absolute error;
- relative error `(P_hat-4s)/(4s)`;
- per-side-length bias;
- per-orientation bias/spread;
- per-phase bias/spread;
- description units / rule complexity;
- exact/near-exact hit count with the declared numerical tolerance.

Do not select a claimed structural law by pooled RMSE alone.

Maintain a Pareto view over at least:

`error / worst-case error / description complexity / orientation stability / phase stability`.

High-capacity lookup superiority in fit does not by itself defeat a compact rule if the compact rule gives substantial explanatory compression.

## 12. Post-search edge/corner interpretation

Only after the first serious grammar/checkpoint is frozen, compute teacher-side geometric role labels for interpretation.

Classify deployed packet windows into at least:

- `SIDE_INTERIOR`;
- `CORNER_NEAR`;
- `AMBIGUOUS_ROLE` if the deterministic teacher-side association is not unique.

The role classifier itself must be frozen before reading collapse-count statistics.

Then report:

- distribution of selected `c(packet)` by role;
- selected split positions by role;
- composition entropy by role;
- whether side packets concentrate at `c=1`;
- whether corner packets concentrate at `c=2` or another finite pattern;
- whether the same local packet class appears in both roles and, if so, whether a purely local grammar can distinguish them.

This is a central scientific diagnostic.

A particularly important possible outcome is:

`STRAIGHT_WHOLE_CHORD_PLUS_CORNER_SPLIT_DISCOVERED`.

But it must not be assumed.

## 13. Exact edge/corner decomposition lane

After a compact candidate is frozen, attempt to decompose its square perimeter error into

`straight-side density defect + finite corner defect`.

Because the estimator has finite packet range, sufficiently large squares should permit a clean separation between windows far from corners and windows intersecting corner neighborhoods.

Investigate whether, for fixed orientation/phase and fixed local grammar,

`P_hat(s) - 4s`

becomes eventually constant, periodic, bounded, or exactly zero as `s` grows.

This lane may use exact periodic/cutting-word structure where available.

Allowed statuses include:

- `EDGE_DENSITY_EXACT_CORNER_DEFECT_REMAINS`;
- `EDGE_DENSITY_BIASED`;
- `FINITE_CORNER_CORRECTION_SUFFICES_ON_DISCOVERY_FAMILY`;
- `NO_FINITE_LOCAL_EXACT_SQUARE_RULE_FOUND_WITHIN_FROZEN_GRAMMAR`.

Do not turn a finite sample trend into an all-scale theorem.

## 14. Stage structure

### Stage 0 — protocol freeze only

Before expensive corpus generation or grammar enumeration, create and freeze:

1. `R058S_SQUARE_TEACHER_PROTOCOL.json`
2. `R058S_INITIAL_SQUARE_TEACHER_REGISTRY.json`
3. `R058S_SQUARE_HOLDOUT_REGISTRY.json`
4. `R058S_BOUNDARY_PACKET_PROTOCOL.json`
5. `R058S_COMPOSITION_COLLAPSE_GRAMMAR_META_PROTOCOL.json`
6. `R058S_COMPUTATION_REGISTRY.json`
7. deterministic Stage-0 checker output.

Return at least these hashes:

`R058S_SQUARE_TEACHER_PROTOCOL_SHA256`

`R058S_INITIAL_SQUARE_TEACHER_REGISTRY_SHA256`

`R058S_SQUARE_HOLDOUT_REGISTRY_SHA256`

`R058S_BOUNDARY_PACKET_PROTOCOL_SHA256`

`R058S_COMPOSITION_COLLAPSE_GRAMMAR_META_PROTOCOL_SHA256`

`R058S_COMPUTATION_REGISTRY_SHA256`

Then **STOP for Driver review**.

Do not generate the full discovery corpus in Stage 0.

### Stage A — square corpus + packet catalog

Only after Driver approves Stage 0:

- generate the frozen discovery square corpus;
- audit topology/ties/threshold fallback;
- build `k=1..8` packet census and D6 catalog;
- reproduce raw digital perimeter and teacher perimeter;
- build the teacher-side role-label protocol but do not expose those labels to grammar search;
- run independent deterministic checks.

Freeze Stage-A corpus/catalog/check hashes and stop for Driver review if requested.

### Stage B — first serious square grammar search

Only after Stage A is accepted:

- run G0/G1/G2/G3 capacity ladder;
- keep holdout unconsumed;
- freeze the first serious compact grammar checkpoint before cross-generation comparison;
- perform post-hoc side/corner role analysis only after candidate freeze;
- attempt the exact edge/corner decomposition lane;
- return the strongest honest status.

After Stage B, STOP. Do not consume the square holdout and do not start rectangles/cubes without Driver authorization.

## 15. Required Stage-B artifacts

At minimum:

- `R058S_SQUARE_DISCOVERY_RESULTS.json`
- `R058S_COMPOSITION_SEARCH_LEDGER.json`
- `R058S_COMPACT_GRAMMAR.json`
- `R058S_HIGH_CAPACITY_LOOKUP_BENCHMARK.json`
- `R058S_EDGE_CORNER_COLLAPSE_LEDGER.json`
- `R058S_SCALE_ORIENTATION_PHASE_ATLAS.json`
- `R058S_EDGE_CORNER_DECOMPOSITION_RESULTS.json`
- `R058S_FIRST_SERIOUS_SQUARE_GRAMMAR_CHECKPOINT.json`
- independent checker results.

## 16. Decision outcomes

Return one or more of:

- `STRAIGHT_WHOLE_CHORD_PLUS_CORNER_SPLIT_DISCOVERED`
- `OTHER_COMPACT_EDGE_CORNER_COLLAPSE_DISCOVERED`
- `COMPACT_SQUARE_COLLAPSE_GRAMMAR_FOUND`
- `HIGH_CAPACITY_LOOKUP_ONLY`
- `EDGE_DENSITY_BIASED`
- `FINITE_CORNER_CORRECTION_SUFFICES_ON_DISCOVERY_FAMILY`
- `NO_FINITE_LOCAL_EXACT_SQUARE_RULE_FOUND_WITHIN_FROZEN_GRAMMAR`
- `SQUARE_COLLAPSE_STRUCTURE_OPEN_WITH_EXACT_BOUNDED_EVIDENCE`

Every result remains `DISCOVERY / NOT_CANONICAL / NOT_FOUNDATIONAL_THEOREM` unless a later proof generation upgrades it.

## 17. Prohibitions

Do not:

- use circle, disk, arc, tangent, radius, circumference, or pi teacher targets;
- alter R055/R056/R057/R057X/R057Y frozen bytes;
- use R057 fitted rules before the first serious R058S checkpoint;
- let teacher corner labels enter the grammar input;
- change the holdout after seeing Stage-B results;
- expand `K>8` during this generation;
- expand to rectangles or cubes during this generation;
- call a lookup table a law without compression;
- claim exactness from floating-point coincidence;
- use a large-scale regression as an all-scale theorem;
- optimize packet segmentation/start offset; use the frozen all-cyclic-window readout;
- perform CI polling; ordinary research status is `CI_NOT_REQUIRED_FOR_RESEARCH`.

## 18. Highest-priority scientific questions

In order:

1. Does `whole chord` emerge on straight-side packets without being hard-coded as the winner?
2. Do corner-near packets require a finite split count distinct from side-interior packets?
3. Can the side/corner distinction be inferred from teacher-free local packet structure?
4. Does one compact grammar remain stable across square side length, phase, and the discovery orientation family?
5. Is square error dominated by straight-side density bias or by a finite corner defect?
6. Does the discovered rule compress a high-capacity lookup substantially?
7. Only after this generation: does the rule transfer to unseen square orientations/phases, then rectangles, then higher-dimensional cubes?

## 19. Research interpretation

The desired conceptual ladder is:

`digital boundary -> local packet -> ordered chord composition -> straight-edge law + corner law -> square perimeter`

If a stable square law is found, later sibling generations should test:

`square -> rectangle -> rotated/held-out square -> polygon angle ladder -> circle`

and separately

`square -> cube -> face/edge/vertex collapse hierarchy`.

Those later routes are not part of R058S Stage 0/A/B.
