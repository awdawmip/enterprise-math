# R062 Stage 0 — BRC × Native Multipath Enrichment Bridge Validation

Task-ID: `RS-R062-STAGE0-BRC-MULTIPATH-ENRICHMENT-BRIDGE-VALIDATION`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r062-stage0-brc-multipath-bridge`

This stage is an independent bridge/falsification diagnostic. It does not consume or modify R061 Stage 3 and must not alter the frozen R061 line definitions.

## 0. Read first / frozen inputs

Read first:

1. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`;
2. `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`;
3. `driver_reviews/R061_STAGE1R_NATIVE_LINE_TRACE_FINAL_ACCEPTANCE_20260821.md`;
4. `driver_reviews/R061_STAGE2_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_DRIVER_REVIEW_20260821.md`;
5. frozen Stage 1R reproducibility head `653071b8e230d1e707e0544cab22ad2a408b92bd`;
6. frozen Stage 2 results on `research/r061-stage2-arbitrary-point-line-gluing`.

Freeze from R061:

- one native line identity in a fixed translated sector is a native component trace;
- `T_{P;a,b}^{(ij)}=(P,[X_i^a X_j^b])` under component-preserving commutation `X_iX_j~X_jX_i`;
- its native line path fiber is all trace linearizations after typed start incidence;
- `|Realize_E(T_{P;a,b}^{(ij)})|=binom(a+b,a)`;
- same carrier endpoint is not sufficient for same native line;
- reverse-third carrier shortcuts remain different native component traces;
- graph jump count is not native length;
- native geometry uses three positive axes and no native negative axes.

Repository search at taskbook opening found no authoritative file whose literal contents define `BRC` or `recoalescence`. Therefore **do not assume the Driver's provisional Boolean-BRC interpretation is historically exact**. The first gate of this task is to recover or reconstruct BRC precisely from available repository/history artifacts. If no older authoritative artifact is found, state that fact and work with an explicitly typed `BRC_CANDIDATE_V0` rather than pretending provenance.

## 1. Hard objective

Classify whether BRC is exactly, partially, or not at all the Boolean/support shadow of the frozen R061 native multipath structure, and derive or falsify an enriched bridge.

Hard target:

`BRC_MULTIPATH_ENRICHMENT_BRIDGE_CLASSIFIED_AND_FALSIFIABLE`.

The central candidate chain is:

`PATH_BRC -> N_BRC -> BOOLEAN_BRC`

with the intended meanings:

- `PATH_BRC`: preserve concrete labeled path witnesses/provenance;
- `N_BRC`: preserve path multiplicity/count but forget witness identity;
- `BOOLEAN_BRC`: preserve only support/reachability/nonemptiness.

Do not assume this chain is correct.

At minimum answer:

1. What exactly is BRC's domain, codomain, multiplication/composition, addition/merge, and relabeling semantics?
2. Does Boolean BRC collapse split/recoalescence multiplicity exactly as a Boolean semiring would?
3. Can an `N`-valued enrichment recover the exact number of trace linearizations?
4. Can a path/witness-valued enrichment recover the exact R061 path fiber, not merely its count?
5. Is the frozen trace identity a quotient of Path-BRC by component-preserving commutations?
6. Is ordinary/unlabeled BRC too weak because it admits reverse-third same-endpoint shortcuts?
7. Is a component-labeled BRC sufficient to distinguish `SAME_ENDPOINT` from `SAME_LINE`?
8. Are BRC and native trace two distinct quotients of one richer path object?
9. Does the bridge commute with translation from origin traces to arbitrary-point Stage 2 traces?
10. Is any apparent correspondence only an analogy rather than a genuine algebraic homomorphism/factorization?

## 2. Recover or reconstruct BRC before bridging

Search the repository history, taskbooks, driver reviews, research results, definitions and adjacent Enterprise/Hodge artifacts for BRC or its expanded name/semantics.

Search aliases/concepts, not only the literal token `BRC`, including:

- Boolean relation / relational closure;
- branching relation;
- split / branch / recoalescence;
- relabeling / automorphism transport;
- relation composition;
- Candidate B;
- any object previously classified as losing multiplicity/provenance/weights.

Produce:

`research_results/R062_STAGE0/R062_STAGE0_BRC_PROVENANCE_AND_TYPE_RECOVERY.md`

and machine-readable:

`R062_STAGE0_BRC_TYPE_SIGNATURE.json`.

Classify provenance as exactly one of:

- `AUTHORITATIVE_PRIOR_BRC_RECOVERED`;
- `PARTIAL_PRIOR_BRC_RECOVERED`;
- `NO_AUTHORITATIVE_PRIOR_BRC_ARTIFACT_FOUND`.

If no authoritative prior definition is recovered, define a provisional candidate explicitly as `BRC_CANDIDATE_V0` and keep all later conclusions conditional on that candidate.

## 3. Define labeled native one-step relations

For the frozen circle-cell plane and one translated sector `S_ij(P)`, define one-step labeled relations/operators corresponding to the native component generators:

`R_i`, `R_j`.

A legal edge must encode enough data to distinguish at least:

- start cell;
- terminal cell;
- component label `X_i` or `X_j`;
- translated sector/trace context when needed.

Do **not** replace labeled relations with unlabeled nearest-neighbor adjacency unless testing that weaker candidate as a falsification baseline.

For a word

`w=X_{i_1}...X_{i_n}`

derive the relation/path operator associated to composition in the exact convention used by BRC.

Output:

`R062_STAGE0_LABELED_NATIVE_RELATION_MODEL.md`.

## 4. Three enrichment levels

Construct and type three candidates over the same labeled transition skeleton.

### B0 — BOOLEAN_BRC

Coefficient/entry semiring:

`B={0,1}`

with Boolean OR/addition and AND/composition semantics as appropriate.

It must answer support/nonemptiness only.

### B1 — NATURAL_MULTIPLICITY_BRC

Coefficient semiring:

`N`.

Distinct path contributions must add as integers rather than collapse under idempotent Boolean OR.

Test whether the `(a,b)` line branch produces exactly

`binom(a+b,a)`

at its typed terminal relation entry.

### B2 — PATH_WITNESS_BRC

Entries/coefficient objects preserve actual labeled witness words or path IDs.

Addition = exact witness union/formal sum with explicit duplicate policy.

Multiplication = composable witness concatenation.

The result must be strong enough to reconstruct the prefix cell trajectory, not merely the terminal word string.

If this requires a path category/groupoid/algebra rather than an ordinary matrix semiring, type that honestly.

Output:

`R062_STAGE0_BRC_ENRICHMENT_TOWER_THEOREM.md`.

## 5. Exact forgetful maps / homomorphism audit

Test whether there are exact structure-preserving maps

`Path-BRC -> N-BRC`

by witness cardinality/multiplicity, and

`N-BRC -> Boolean-BRC`

by `n>0 -> 1`.

Also test the direct nonemptiness map

`Path-BRC -> Boolean-BRC`.

Audit which operations commute with these maps:

- composition;
- branch union;
- recoalescence;
- relabeling;
- translated placement;
- trace quotient.

Do not call a map a semiring/category homomorphism if duplicate paths, nonfree composition, typed starts, or partial composition break the relevant law.

Output:

`R062_STAGE0_FORGETFUL_MAPS_AND_HOMOMORPHISM_AUDIT.md`.

## 6. Mandatory `(1,1)` commuting-diamond witness

Use the frozen local commuting diamond:

`Xi Xj`

and

`Xj Xi`.

For one typed start cell, verify exactly:

- two distinct native path witnesses;
- one common typed terminal cell;
- one common native component trace `T_{1,1}^{(ij)}`;
- Path-BRC preserves both witnesses;
- N-BRC records multiplicity `2` if that enrichment is valid;
- Boolean-BRC records only support `1`;
- trace quotient identifies the two witnesses by `XiXj~XjXi`.

This is the minimal split/recoalescence checkpoint.

Output a machine-readable exact witness.

## 7. Mandatory `3-4-5` witness

For one fixed translated sector trace `T_{P;3,4}^{(ij)}` verify:

- native length remains `5`;
- path fiber cardinality is exactly `35`;
- Path-BRC contains exactly the 35 frozen trace linearization witnesses;
- N-BRC terminal multiplicity is exactly `35` if B1 survives;
- Boolean-BRC terminal support is exactly `1`;
- no multiplicity/provenance information survives Booleanization;
- all 35 witnesses map to one trace identity.

Also test `(4,3)` and axis-degenerate branches.

Output:

`R062_STAGE0_N25_BRC_MULTIPATH_CERTIFICATE.json`.

## 8. Third-direction shortcut falsification gate

Replay the smallest Stage 1/2 third-direction witness.

For local `(1,1)`:

- the trace linearizations are `XiXj`, `XjXi`;
- a reverse-third carrier edge may reach the same carrier endpoint.

Test at least:

### U0 — unlabeled adjacency BRC

Does it merge the reverse-third shortcut into the same reachability support?

If yes, preserve the exact counterexample showing:

`UNLABELED_BRC_CANNOT_CLASSIFY_NATIVE_LINE_MEMBERSHIP`.

### L0 — component-labeled BRC

Does retaining generator/component labels distinguish the trace-linearization fiber from the reverse-third shortcut without using jump count?

If yes, prove the distinction comes from labels/trace typing, not by hand-excluding the shortcut.

This gate is mandatory. A BRC bridge that cannot preserve `SAME_ENDPOINT != SAME_LINE` is rejected as a native line bridge.

Output:

`R062_STAGE0_THIRD_DIRECTION_LABEL_NECESSITY_THEOREM.md`.

## 9. Trace quotient versus Boolean quotient

Starting from the strongest surviving witness/path object, construct and compare at least two quotients/projections:

1. **trace quotient**: identify component-preserving adjacent commutations while preserving `(a,b)` component content;
2. **Boolean/support quotient**: forget witness identity/multiplicity and retain only reachability/support.

Test whether the diagram

`MULTIPATH_OBJECT -> TRACE_IDENTITY`

and

`MULTIPATH_OBJECT -> BOOLEAN_BRC`

is genuinely a pair of different quotients/functors of one richer object.

Determine exactly what information each quotient destroys:

- order;
- multiplicity;
- provenance;
- path prefix geometry;
- component labels;
- placement/start vertex;
- endpoint support.

Output:

`R062_STAGE0_TRACE_VS_BOOLEAN_QUOTIENT_DIAGRAM.md`.

## 10. Translation covariance / Stage 2 bridge

Repeat the bridge away from `O_E` using translated traces

`T_{P;a,b}^{(ij)}`.

Require exact covariance under at least several nontrivial coordinate-vertex translations.

The bridge must preserve:

- translated start incidence `Sigma_P^(ij)`;
- concrete placement/start vertex;
- component trace class;
- path witness count;
- terminal typed endpoint;
- third-direction distinction.

Do not collapse parallel translated segments into one identity merely because their local BRC matrices are isomorphic.

Output:

`R062_STAGE0_TRANSLATED_BRC_BRIDGE_AUDIT.md`.

## 11. Recoalescence and information-loss census

Build a finite exact census of branch/recoalescence motifs, including at minimum:

- one diamond `(1,1)`;
- `T_{2,1}`, `T_{2,2}`, `T_{3,2}`;
- `T_{3,4}`;
- at least one translated copy of each;
- at least one same-endpoint third-direction shortcut example.

For every motif report the information tuple retained at each layer:

`Path-BRC` / `N-BRC` / `Boolean-BRC` / `Trace`.

The task must explicitly answer whether Boolean BRC's earlier apparent weakness is exactly explained by early idempotent collapse of multiplicity/provenance, or whether another independent obstruction remains.

Output:

`R062_STAGE0_INFORMATION_LOSS_CENSUS.json`.

## 12. Deterministic checker — mandatory

Commit an executable deterministic checker under `scripts/`.

Minimum requirements:

- exact arithmetic / no floating-point decisions;
- regenerate Stage 1R frozen path counts/hashes needed by the bridge rather than copying result JSON;
- explicit witness enumeration for all `(a,b)` with `a+b<=12` in all three sectors for at least three translated starts;
- verify Boolean support, natural multiplicity and path witness sets from the same generated source;
- verify `N(1,1)=2` and `N(3,4)=35`;
- verify Booleanization of any positive multiplicity is `1`;
- verify trace quotient fiber sizes against `binom(a+b,a)`;
- explicit third-direction unlabeled/labeled comparison;
- verify translated covariance;
- detect duplicate witness counting;
- preserve smallest mismatch/counterexample;
- produce committed replay summary and reproducibility proof.

Checker must not take the desired bridge identity as an input assertion.

## 13. Acceptance gates

Stage passes only after classifying all of the following:

1. `BRC_PROVENANCE_TYPED`;
2. `LABELED_NATIVE_TRANSITION_MODEL_EXACT`;
3. `BOOLEAN_BRC_SUPPORT_SEMANTICS_EXACT`;
4. `N_BRC_MULTIPLICITY_SEMANTICS_EXACT_OR_REFUTED`;
5. `PATH_BRC_WITNESS_SEMANTICS_EXACT_OR_REFUTED`;
6. `PATH_TO_N_FORGETFUL_MAP_CLASSIFIED`;
7. `N_TO_BOOLEAN_FORGETFUL_MAP_CLASSIFIED`;
8. `COMMUTING_DIAMOND_2_TO_1_COLLAPSE_EXACT`;
9. `N25_35_TO_1_BOOLEAN_COLLAPSE_EXACT`;
10. `UNLABELED_BRC_NATIVE_LINE_BRIDGE_ACCEPTED_OR_REFUTED`;
11. `COMPONENT_LABELED_BRC_NATIVE_LINE_BRIDGE_ACCEPTED_OR_REFUTED`;
12. `TRACE_AND_BOOLEAN_ARE_DISTINCT_QUOTIENTS_CLASSIFIED`;
13. `TRANSLATION_COVARIANCE_PASS`;
14. `NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE`;
15. `NO_CARRIER_VECTOR_RELATION_PROMOTED_TO_NATIVE_IDENTITY`;
16. `COMMITTED_DETERMINISTIC_CHECKER_PASS`.

Final classification must choose one strongest truthful outcome, e.g.:

- `BRC_IS_EXACT_BOOLEAN_SHADOW_OF_NATIVE_MULTIPATH_WITH_PATH_ENRICHMENT_RECOVERING_FULL_FIBER`;
- `BRC_IS_ONLY_PARTIAL_SUPPORT_PROJECTION_AND_ENRICHMENT_FAILS_AT_<MINIMAL_OBSTRUCTION>`;
- `PRIOR_BRC_DIFFERS_MATERIALLY_FROM_BOOLEAN_RELATION_CANDIDATE`;
- another precisely typed result.

Do not force a positive bridge.

## 14. Stop condition

Stop for Driver review after Stage 0.

Do not alter R061 Stage 3, do not modify canonical R061 definitions, and do not automatically open R062 Stage 1.
