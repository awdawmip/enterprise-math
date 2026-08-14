# R057 Problem Packet — Pi-Supervised Algebraic Collapse Synthesis

Status: `FROZEN PROBLEM PACKET / NEW MOTHER QUESTION / SUPERVISED DISCOVERY / NOT CANONICAL`

## 0. Purpose

R053/R054 showed that a very small hand-declared collapse library can improve lattice-circle perimeter recovery, but the search space was intentionally narrow. R057 changes the question.

The goal is not to derive pi blindly. The goal is to use known classical pi and teacher circles as a **supervised discovery signal** to invent the correct discrete collapse language, then compress the discovered rule system into a smaller algebraic grammar or recurrence.

For discovery in R057, the following are explicitly allowed:

- classical pi as a numerical target;
- teacher circle, teacher center, radius and tangent information;
- post-selection;
- overfitting;
- repeated refitting after seeing results;
- expansion of packet length K;
- expansion of the collapse operator library;
- symbolic regression / program synthesis;
- importing structural motifs from known pi algorithms;
- choosing later experiments based on earlier errors.

These are not contamination events because R057 is an explicitly supervised calibration/discovery task, not a foundational or blind derivation.

The only epistemic requirement is provenance: a rule discovered using pi must be labeled `PI_SUPERVISED_DISCOVERY`. A later proof that the rule has a theorem-level property must be recorded separately from how the rule was found.

## 1. Fixed substrate

Use the same normalized triangular lattice as R053/R054:

- axial lattice `Lambda = Z^2`;
- edge directions are the six nearest-neighbor directions;
- exact squared chord norm `Q(a,b)=a^2+a*b+b^2`;
- a chord displacement `d` has Euclidean length `sqrt(Q(d))` in lattice units.

Teacher circles and exposed lattice boundaries are calibration-side objects. They may be generated fresh rather than copied from old scored outputs.

R053 and R054 are historical seeds, not immutable search constraints. In particular, R054's frozen K=3 sequential parser must **not** be inherited as the universal parser because its spatial reflection invariance failed. R057 should use a cyclic/D6-aware representation by construction.

Useful historical anchors:

- R053 protocol `fb8f731160e29d7f11e51c8ffbc70257427d32149e77da462c56d548deed5044`;
- R053 collapse library `7c051a3b141b7fa46a4820b026185c602193bb692d2d8d3a02f385999de0d83f`;
- R054 parser contract `70137fe7dae892759c956e418563506c8818987809034e76acff13f9660803c3` (historical only; reflection defect preserved);
- R054 K3 library `d42af9ee4baaa8cbc7b6553b3c13c260cd0915d7aac2911dee03a93ee552e114`;
- R054 selected K3 policy `751566bc5f12360986829041ff9da6a0cc496e385be7bdb28e7bbaaaf73abcb0`.

## 2. Discovery philosophy

R057 has three epistemic layers.

### Layer D — supervised discovery

Use pi directly to search for rules that reduce teacher-circle perimeter error. Overfit if useful. Change the grammar if useful. Add K values if useful. Add operator primitives if useful.

The question is:

> What discrete collapse syntax is expressive enough to reproduce pi from triangular-lattice boundary data?

### Layer C — algebraic compression

After good rules exist, try to compress them:

- fewer generators;
- shorter syntax trees;
- recurrences in packet length;
- dependence on turn words or D6 invariants;
- periodic/modular rules;
- finite-state transducers;
- operator identities;
- generating functions;
- polynomial/rational selection laws.

### Layer T — theorem candidates

Only after discovery/compression ask which statements can be proved exactly or asymptotically. A theorem may concern a rule that was originally found by supervised fitting. That is acceptable; the discovery provenance remains explicit.

R057 does not require a blind rediscovery of pi before a theorem can be valuable.

## 3. Boundary packet representation

Represent each teacher boundary as a cyclic word of six lattice directions.

For a contiguous packet of `k` exposed edges, record at least:

- raw direction word;
- turn word in `{-1,0,+1}` or the exact available turn alphabet;
- endpoint displacement;
- `Q(endpoint displacement)`;
- counts of the six directions;
- cyclic/reversal/D6 canonical class;
- local convex/concave/straight descriptors where defined;
- packet length `k`.

Do not require one fixed K. Start with a bounded K for runtime, but K is a **versioned search parameter**, not a frozen scientific premise.

A useful initial range is `1<=k<=8`. The researcher may expand to `k=12`, `16`, or another justified bound inside the same R057 generation if the complexity/error frontier says the language is still underexpressive. Every expansion must be recorded in grammar genealogy.

## 4. Collapse expression grammar

R057 should synthesize expressions, not merely choose among RAW1/CHORD2/CHORD3.

At minimum the initial grammar should support the following primitive ideas.

### G0 discrete chord/partition primitives

For packet vertices `p_0,...,p_k`:

- `RAW(i)` — keep one raw lattice edge;
- `CHORD(i,j)` — replace the contiguous subpacket `i..j` by the straight endpoint chord `|p_j-p_i|`;
- `PARTITION[b_1,...,b_t]` — partition the packet into contiguous blocks and sum the chord of each block;
- `WHOLE_CHORD(k)` — one block of length k;
- `IDENTITY_PACKET(k)` — no collapse.

Thus all compositions of k are candidate discrete collapse structures. This directly permits examples of the form “a k-edge crystal packet effectively becomes c(k) collapsed pieces,” while retaining turn-word dependence.

### G1 expression combinators

Allow versioned addition of:

- `SUM(E1,...,En)`;
- `DIFF(E1,E2)` where useful;
- rational scaling with bounded denominator;
- algebraic scaling by exact lattice radicals when independently generated by chord geometry;
- conditional selection by packet invariants;
- composition of collapse operators;
- finite-state context dependence on neighboring packet types.

The researcher may add further primitives after seeing results. New primitives must be versioned and their motivation/error witness logged. They do not require a new research generation.

## 5. Pi-algorithm structural motifs

Known pi algorithms may be used as design inspiration or direct teacher-side feature generators.

Examples of structural motifs worth testing include:

- alternating correction;
- multiplicative/product correction;
- repeated averaging / AGM-like two-channel fusion;
- decomposition into several local roles followed by recombination;
- nested/recursive collapse;
- sparse high-order correction terms;
- rational recurrences;
- hypergeometric-like rapidly shrinking residual corrections.

R057 need not copy any classical formula literally. The point is to ask whether successful pi algorithms suggest reusable **collapse algebra motifs**.

Any literal imported formula must be labeled teacher-side and may not be misreported as a lattice-native derivation.

## 6. Teacher data and target

Generate a fresh, reproducible teacher-circle corpus using a frozen initial data generator.

The initial corpus should cover:

- multiple radii, including some substantially larger than R053/R054 construction scales;
- multiple center phases;
- enough phase diversity to avoid fitting one lattice alignment only.

A recommended initial radius set is

`[24,32,40,56,72,96,128,160,224]`.

A recommended initial phase family is 8-12 deterministic phases spanning generic and symmetric offsets.

This initial corpus is not a sacred holdout split. R057 may add larger radii/phases after inspecting errors and then refit. Corpus evolution must be versioned in `R057_TEACHER_DATA_GENEALOGY.json`.

Primary teacher target for a circle of radius R is

`P_target = 2*pi*R`.

Primary error may be circumference error or equivalently

`pi_hat = P_eff/(2R)`.

Use high-precision arithmetic sufficient to distinguish close grammar candidates. Tangent misalignment and phase sensitivity may be secondary diagnostics.

## 7. Global parsing / segmentation

Avoid reintroducing the R054 sequential-parser reflection defect.

The preferred model is a cyclic segmentation/tiling of the full boundary word by local packets, with each packet assigned a collapse expression.

Possible synthesis approaches include:

- dynamic programming over cyclic segmentations;
- shortest-path / Viterbi-style parsing;
- integer programming;
- exhaustive search for small grammar versions;
- beam search;
- symbolic program synthesis.

The same boundary must evaluate invariantly under cyclic starting-point changes and spatial D6 transformations unless a deliberately orientation-sensitive grammar version is explicitly being tested.

## 8. Search lanes

Run at least two conceptually distinct lanes.

### Lane A — discrete operator synthesis

No free continuous coefficient is required. Search partitions/chords/operator compositions and type-to-operator mappings.

Goal: determine how far purely discrete collapse structure can recover pi.

### Lane B — algebraic operator synthesis

Allow rational/algebraic coefficients or operator mixtures and symbolic expressions.

Goal: determine whether a compact algebraic expression can dramatically beat a large discrete lookup table.

Optional Lane C — sequence law

From selected expressions define derived sequences such as:

- `c(k)` = effective number of collapsed output blocks for packet length k;
- `g(k)` = selected generator class by k;
- `c(k,w)` = collapse order conditioned on turn-word class w.

Fit/inspect these sequences for recurrence, modularity, eventual periodicity, polynomial/floor laws, automata, or generating functions.

## 9. Complexity-error frontier

Because overfitting is allowed, R057 must explicitly track model complexity rather than pretending every low error is equally informative.

For each grammar version record at least:

- teacher error metrics;
- maximum K used;
- number of packet classes with independent rules;
- operator-library size;
- syntax-tree/node count;
- number and algebraic complexity of coefficients;
- parser/context-state count;
- total description length under a declared simple coding convention.

Construct a Pareto frontier of error versus complexity.

Important targets include:

- exact finite-corpus interpolation;
- orders-of-magnitude error drops at small complexity increments;
- a compact rule that matches or beats a huge lookup table;
- evidence of exponential or super-polynomial error decay versus algebraic complexity;
- sudden transition to an exact identity.

## 10. Grammar genealogy and post-selection

Post-selection is allowed, but every meaningful grammar change must be logged:

- parent grammar version;
- change made;
- error or pattern that motivated it;
- new primitive/K/context introduced;
- before/after score;
- whether the change increased or decreased description length.

Do not call this leakage. It is intentional supervised discovery.

The forbidden behavior is only historical falsification: do not later claim that a post-selected rule was fixed before the target was observed.

## 11. Algebraic compression

After at least one high-performing supervised grammar exists, attempt to replace the lookup table by a smaller generator system.

Questions:

- Can packet rules be generated by a small set `A,B,C,...`?
- Are many selected collapses powers/compositions of the same operators?
- Does packet length k obey a recurrence in operator space?
- Do turn-word classes fall into a few algebraic orbits?
- Does a finite automaton generate the mapping from local word to collapse expression?
- Can a rational/polynomial/generating-function law reproduce the fitted rule sequence?

The preferred outcome is not merely `pi_hat close to pi`; it is a compact **collapse algebra** whose outputs explain why many fitted local cases share one rule.

## 12. Scale stress after discovery

After a grammar version is interesting, evaluate it at larger radii/phases.

This is diagnostic, not sacred blind holdout. The researcher may modify the grammar after seeing these results, but must create a new grammar version and preserve the prior score.

At least one final frozen grammar version should be evaluated without further modification on a clearly identified set of larger scales so its final reported robustness is reproducible. This final evaluation is a reporting discipline, not a claim that discovery was blind.

## 13. Theorem candidate ledger

R057 may return conjectures or proofs about discovered rules.

Keep separate fields:

- `discovery_provenance` — teacher/pi-supervised, post-selected, etc.;
- `mathematical_status` — empirical fit / finite exact identity / proved recurrence / proved asymptotic statement.

A supervised origin does not weaken a subsequently valid proof.

Do not claim a theorem solely from numerical fit.

## 14. Initial Stage-0 freeze

Before expensive synthesis, freeze and return:

- `R057_DISCOVERY_PROTOCOL_SHA256`
- `R057_INITIAL_TEACHER_DATA_REGISTRY_SHA256`
- `R057_GRAMMAR_META_PROTOCOL_SHA256`

These hashes freeze the **rules for evolving the search**, not one immutable grammar library.

The Stage-0 meta-protocol must explicitly say that later grammar/corpus versions may expand within R057 with genealogy logging.

## 15. Runtime staging

Avoid another very long silent run.

Recommended checkpoints:

1. Stage 0 meta-protocol hashes;
2. initial packet/type catalog and G0 partition grammar results for small K;
3. first meaningful complexity-error frontier;
4. grammar expansion only if frontier justifies it;
5. algebraic compression attempt;
6. final frozen grammar + scale stress + report.

If a synthesis search becomes expensive, checkpoint the best grammar/frontier found so far instead of silently extending combinatorics.

## 16. Required artifacts

Return at least:

- `R057_REPORT.md`
- `R057_DISCOVERY_PROTOCOL.json`
- `R057_INITIAL_TEACHER_DATA_REGISTRY.json`
- `R057_TEACHER_DATA_GENEALOGY.json`
- `R057_GRAMMAR_META_PROTOCOL.json`
- `R057_PACKET_TYPE_CATALOG.json`
- `R057_OPERATOR_LIBRARY_GENEALOGY.json`
- `R057_GRAMMAR_GENEALOGY.json`
- `R057_SYNTHESIS_ATLAS.json`
- `R057_COMPLEXITY_ERROR_FRONTIER.json`
- `R057_ALGEBRAIC_COMPRESSION.json`
- `R057_SCALE_STRESS.json`
- `R057_THEOREM_CANDIDATE_LEDGER.json`
- `R057_ADVERSARIAL_TEST_RESULTS.json`
- `R057_EXACT_CHECK_RESULTS.json`
- `R057_ARTIFACT_MANIFEST.json`
- executable synthesis/checker/tests.

Final result vocabulary may include:

- `SUPERVISED_COLLAPSE_GRAMMAR_FOUND`
- `EXACT_FINITE_CORPUS_FIT_FOUND`
- `COMPACT_COLLAPSE_ALGEBRA_FOUND`
- `SEQUENCE_OR_RECURRENCE_LAW_FOUND`
- `LOW_COMPLEXITY_PI_RECOVERY_FOUND`
- `FIT_FOUND_BUT_NOT_COMPRESSIBLE`
- `NO_USEFUL_COLLAPSE_LANGUAGE_WITHIN_SEARCH_BUDGET`

## 17. Interpretation boundary

R057 is intentionally allowed to use the answer to discover the method.

Therefore a successful fit is not a foundational derivation of pi. It is a discovered discrete algorithm for reproducing pi from lattice-boundary data.

Its scientific value comes from what happens next:

`known pi -> discover collapse grammar -> compress grammar -> prove properties -> compare with other pi roles`.

Do not downgrade a valid discovered rule merely because it was post-selected. Do not upgrade a fitted rule to theorem status without proof.
