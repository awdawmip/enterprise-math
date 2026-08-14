# R057G Problem Packet — Pi-Supervised Geometric Collapse Synthesis

Status: `FROZEN PROBLEM PACKET / SIBLING ARM TO R057-A / SUPERVISED DISCOVERY / NOT CANONICAL`

## 0. Why R057G exists

R057-A searches for an algebraic/operator collapse language. R057G runs in parallel and asks the same discovery question in a different representation:

> Given digitized triangular-lattice teacher circles and known classical pi, what geometric surrogate should each local boundary packet collapse into so that the total collapsed boundary recovers the teacher geometry as accurately and compactly as possible?

This is explicitly supervised discovery. Blind recovery of pi is not required.

R057G is a sibling arm, not a continuation after R057-A. In its first discovery round it must not consume R057-A's best grammar, fitted operator table, or selected generator system. Both arms may independently use the same classical teacher objects. Later cross-arm comparison is allowed only after each arm has produced a serious independent grammar checkpoint.

R056 final read-only context:

- R056 final head: `a41a47f3a5bb96fd5cc5cdc10c497afbd288eae7`
- R056 artifact manifest SHA-256: `9622f9af050ba01645ca9b9fa27584896e93debf5fbc5ae00fe76e1fe38bfa9f`
- R056 result: fixed support radius 3 already escapes the radius-1 D1 metastability; this fact is context only and does not constrain the teacher-circle collapse grammar.

## 1. Discovery philosophy

The following are allowed and expected in R057G discovery:

- classical pi;
- teacher circles;
- teacher center;
- radius and diameter;
- chord length;
- tangent and tangent intersection constructions;
- polygonal and arc surrogates;
- Euclidean lengths and areas;
- local turning angles / direction words;
- post-selection;
- overfitting;
- symbolic regression;
- program synthesis;
- increasing packet size K after seeing errors;
- adding geometric primitives after seeing errors;
- adding teacher radii/phases after seeing errors;
- fitting rational, algebraic or floating coefficients;
- using structural motifs from known pi algorithms as inspiration.

These are not contamination because R057G is not a foundational derivation.

The only mandatory epistemic separation is:

`SUPERVISED_DISCOVERY != THEOREM_PROOF`.

Every fitted rule must record its genealogy and may later be compressed/proved.

## 2. Anti-degeneracy classification

Teacher pi may be used without restriction in scoring, selection, optimization, error analysis and rule invention.

However, distinguish two output classes:

1. `STRUCTURAL_GEOMETRIC_RULE`: the deployed packet rule is computed from declared packet/teacher geometric primitives and fitted parameters; it does not simply emit the target pi constant or a target contribution copied directly from the scoring label.
2. `TARGET_LITERAL_DEGENERATE`: the deployed rule contains a direct hard-coded pi/teacher-target literal that makes the fit tautological.

`TARGET_LITERAL_DEGENERATE` candidates may be retained as upper-bound or sanity baselines but cannot count as discovery of a collapse structure.

This does not forbid coefficients learned using pi. It only prevents the trivial program “return the answer label” from being mistaken for geometry.

## 3. Fixed lattice carrier and teacher-circle digitization

Use the normalized triangular lattice in axial coordinates:

- `e1=(1,0)`;
- `e2=(1/2,sqrt(3)/2)`;
- `Q(a,b)=a^2+a*b+b^2`.

Teacher geometry is Euclidean and explicitly classical.

The initial teacher corpus must include multiple radii and multiple sub-cell center phases/orientations so that a rule cannot win only by exploiting one favorable lattice alignment.

Stage 0 must freeze the initial teacher-data registry before expensive synthesis. The registry may later be expanded under the frozen genealogy rules.

Each teacher sample must preserve enough exact/reproducible information to reconstruct:

- teacher center;
- radius;
- lattice sampling/digitization convention;
- cyclic boundary walk;
- boundary direction/turn word;
- teacher circumference `2*pi*r` or normalized pi target;
- phase/orientation metadata.

## 4. Boundary packets

Represent the digitized boundary as a cyclic sequence of lattice vertices/edges.

A contiguous packet of size `k` is

`B=(x_0,x_1,...,x_k)`

with its cyclic direction/turn word and D6/cyclic equivalence metadata.

Packet typing may use, and later expand, features such as:

- `k`;
- endpoint displacement/chord;
- ordered or cyclic turn word;
- net turn;
- local convex/flat/concave pattern;
- teacher-center-relative radial data;
- tangent directions at endpoints;
- chord-to-radius ratio;
- local signed area;
- local triangle/polygon invariants;
- neighboring packet context.

Do not assume packet size alone determines the optimal collapse.

## 5. Initial geometric collapse grammar G0

R057G starts with a broad but interpretable geometric grammar. It is not frozen forever.

At minimum include:

### G0-RAW — raw polyline
Keep all original packet edges.

### G0-CHORD — whole endpoint chord
Replace the packet by the straight segment `x_0 x_k`.

### G0-PARTITION — contiguous chord partition
Partition the packet into contiguous blocks and replace each block by its endpoint chord. Search all compositions of `k` within the current packet-size cap.

### G0-MULTI_CHORD — selected internal breakpoints
Choose one or more internal packet vertices and join successive selected vertices by chords.

### G0-TRIANGLE — triangle surrogate
Represent a packet using endpoint chord plus one selected/effective apex, with candidate readouts based on triangle sides, altitude, area or perimeter.

### G0-TANGENT — endpoint tangent surrogate
Use teacher-side or packet-estimated endpoint tangents and their intersection, tangent lengths, or tangent/chord hybrid readouts.

### G0-ARC — local circular-arc surrogate
Fit/select a local arc or osculating-circle-style surrogate from declared local geometry. Teacher center/radius may be used in the fully supervised lane, but must be genealogically marked.

### G0-AREA — area-preserving / sector-style surrogate
Use local signed area or sector/triangle decompositions to infer an effective boundary contribution.

### G0-COLLAPSE-COUNT — effective discrete collapse count
Learn a map such as

`c(k,turn_word,context) -> effective number/partition of collapsed geometric pieces`.

This directly includes hypotheses of the form `1->1, 2->2, 3->3, 4->3, ...` without assuming that example is correct.

## 6. Scoring

The primary teacher objective is global pi/circumference reconstruction across the current teacher corpus.

A candidate grammar should produce a collapsed geometric readout `P_hat(sample)` and a normalized estimate such as

`pi_hat = P_hat / (2*r)`

when the readout is length-like.

For non-length readouts, define the normalization explicitly and genealogically.

Track at least:

- absolute/relative pi error;
- per-radius error;
- per-phase error;
- worst-case error;
- signed bias;
- grammar complexity;
- number of packet types / branches;
- number and algebraic complexity of fitted coefficients;
- target-literal degeneracy flag.

Do not collapse all evaluation into one scalar. Keep a Pareto frontier of error vs complexity vs phase robustness.

## 7. Grammar evolution is allowed

R057G may expand within the same generation after inspecting results.

Allowed expansions include:

- increase K;
- add new packet context;
- add new geometric surrogate families;
- add fitted coefficients;
- add rational/algebraic transforms;
- add conditional rules;
- add local arc/tangent/area constructions;
- add teacher radii/phases;
- add recursive or multiscale packet grouping.

Every meaningful grammar/data change must enter a genealogy record:

- parent grammar/version;
- motivating error/pattern;
- proposed change;
- score before/after;
- complexity before/after;
- teacher data available when the change was made;
- whether the change was target-guided;
- whether it introduces a target literal.

No post-selection is forbidden; hidden post-selection is forbidden.

## 8. First-round independence from R057-A

Before R057G freezes its first serious grammar checkpoint, it must not read or import:

- R057-A best operator mapping;
- R057-A selected packet collapse counts;
- R057-A fitted coefficients;
- R057-A compressed generators/recurrences.

It may read shared older evidence such as R053/R054 only as historical context, but it must record any inherited operator ideas explicitly.

After both arms have independent checkpoints, later cross-comparison may look for correspondences such as:

- the same `k -> partition` law;
- equivalent type partitions;
- equivalent recurrence structure;
- geometric interpretations of algebraic operators;
- algebraic encodings of geometric surrogates.

That later correspondence study is not part of Stage 0.

## 9. Stage 0 freeze

Before expensive teacher-corpus generation, packet enumeration or synthesis, create and return exactly these three frozen anchors:

- `R057G_GEOMETRIC_DISCOVERY_PROTOCOL_SHA256`
- `R057G_INITIAL_TEACHER_GEOMETRY_REGISTRY_SHA256`
- `R057G_GEOMETRIC_GRAMMAR_META_PROTOCOL_SHA256`

These freeze:

- how supervision is used;
- how target-literal degeneracy is classified;
- how teacher data may expand;
- how grammar versions may expand;
- genealogy requirements;
- first-round independence from R057-A;
- evaluation/reporting fields.

They do **not** freeze a small final grammar or fixed K forever.

Stop after Stage 0 and return the three hashes for Driver review.

## 10. Later stages after Driver review

### Stage A — initial teacher corpus and packet census
Generate the frozen initial corpus and cyclic/D6-aware packet catalog.

### Stage B — initial geometric synthesis
Search G0 and return an early complexity/error frontier before aggressive expansion.

### Stage C — target-guided geometric grammar evolution
Expand K/primitives/context/teacher corpus when errors indicate underexpression. Preserve full genealogy.

### Stage D — geometric compression
Compress the best large rule tables into smaller geometric laws: collapse-count laws, partition recurrences, finite-state rules, local invariant formulas, or small surrogate families.

### Stage E — cross-scale robustness
Test whether the compressed geometry remains accurate over larger radii/phases and whether complexity stabilizes.

### Stage F — theorem candidates
Only after discovery/compression, attempt mathematical statements explaining why selected geometric rules work. Mark theorem status separately from fit status.

## 11. Required artifacts eventually

At minimum:

- `R057G_REPORT.md`
- `R057G_GEOMETRIC_DISCOVERY_PROTOCOL.json`
- `R057G_INITIAL_TEACHER_GEOMETRY_REGISTRY.json`
- `R057G_GEOMETRIC_GRAMMAR_META_PROTOCOL.json`
- `R057G_TEACHER_CORPUS_MANIFEST.json`
- `R057G_PACKET_CATALOG.json`
- `R057G_GRAMMAR_GENEALOGY.json`
- `R057G_COMPLEXITY_ERROR_FRONTIER.json`
- `R057G_BEST_GEOMETRIC_GRAMMARS.json`
- `R057G_COLLAPSE_COUNT_ATLAS.json`
- `R057G_GEOMETRIC_COMPRESSION_RESULTS.json`
- `R057G_ADVERSARIAL_TEST_RESULTS.json`
- `R057G_EXACT_CHECK_RESULTS.json`
- `R057G_ARTIFACT_MANIFEST.json`
- executable synthesis/checker/tests.

## 12. Primary return classes

Final R057G may return one or more accurately scoped discovery classes, including:

- `COMPACT_GEOMETRIC_COLLAPSE_GRAMMAR_FOUND`
- `HIGH_ACCURACY_GEOMETRIC_LOOKUP_ONLY`
- `GEOMETRIC_COLLAPSE_COUNT_LAW_FOUND`
- `GEOMETRIC_COMPRESSION_FAILED`
- `TARGET_LITERAL_ONLY_FIT`
- `GEOMETRIC_PI_SUPERVISED_DISCOVERY_OPEN`

These are discovery classifications, not foundational claims.
