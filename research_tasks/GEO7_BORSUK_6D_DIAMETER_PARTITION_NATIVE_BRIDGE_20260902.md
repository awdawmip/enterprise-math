<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO7-BORSUK-6D-DIAMETER-PARTITION-NATIVE-BRIDGE",
  "title": "GEO7 Borsuk six-dimensional diameter-partition native bridge",
  "kind": "RESEARCH",
  "owner": "research/geo7-borsuk-6d-diameter-partition-native-bridge",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Freeze the exact current primary-source status of the Euclidean Borsuk number in dimension six, then construct or obstruct a finite typed native diameter-partition interface without importing Euclidean norm, continuum dimension or n+1 by fiat.",
  "next_action": "Audit current b(6) lower and upper bounds with publication-state labels; define a finite native diameter relation and strict-smaller-diameter partition contract; classify exact links to Borsuk graphs, coloring and covering; produce one finite theorem, counterfamily or no-go with deterministic certification.",
  "dependencies": [
    "OG-7A3E19C4D8B2056F1A92",
    "RR-36E518770A5FB701B42C",
    "DR-5954202B88BC061A0314",
    "RR-85C8C9CDB6C3A8B8622C",
    "DR-4B7A2D91E6C0538FA124"
  ],
  "source_refs": [
    "research_artifacts/GEO7_BORSUK_6D_DIAMETER_PARTITION_NATIVE_BRIDGE/external_status_seed_20260902.json",
    "driver_reviews/EXTERNAL_GEOMETRY_STRUCTURAL_TRANSFER_OBJECTIVE_CLOSURE_20260902.md",
    "research_returns/GEO6_FALCONER_RELATION_DISTANCE_SPECTRUM_RETURN_20260830.md",
    "driver_reviews/GEO6_NATIVE_RELATION_SELECTOR_CORE_DRIVER_REVIEW_20260902.md"
  ],
  "evidence_status": "NEW_WORLD_GEOMETRY_DIRECTION / PRIMARY_SOURCE_STATUS_FIRST / NATIVE_METRIC_INTERFACE_NOT_YET_GRANTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["GEO7", "Borsuk", "dimension-6", "diameter", "partition", "metric-geometry", "graph-coloring", "native-interface"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO7-BORSUK-6D-DIAMETER-PARTITION-NATIVE-BRIDGE",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-BORSUK-DIAMETER-PARTITION-20260902",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GEO7BORSUK6",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# GEO7 Borsuk six-dimensional diameter-partition native bridge

Status: `READY / P1 / HIGH LEVERAGE`

## Mother question

For Euclidean space, let `b(d)` denote the least integer such that every bounded subset of `R^d` of positive diameter can be partitioned into `b(d)` subsets, each of strictly smaller diameter.

The task asks two separately typed questions:

1. **External status:** what is the exact current proved lower/upper status of `b(6)`, with every claim labeled by date and publication state?
2. **Native bridge:** what is the weakest finite P000-compatible diameter/partition structure on which an analogous Borsuk number is mathematically meaningful, and which classical graph or covering methods transfer under an explicit theorem?

The external answer is not a P000 theorem. The native answer must not inherit Euclidean norm or the conjectural count `d+1` merely from the word “six-dimensional.”

## 1. External primary-source audit

Start from the frozen seed manifest, then independently search the primary literature through the execution date.

Produce a status matrix containing at least:

- the best proved lower bound for `b(6)`;
- the best proved upper bound for `b(6)`;
- whether `b(6)=7` is proved, disproved or open;
- the theorem hypotheses and proof technology behind every retained bound;
- publication state: peer reviewed, accepted manuscript, or preprint;
- submission/publication date and exact source;
- explicit treatment of later work that changes nearby dimensions but does not change dimension six.

The 2026 claims `b(4)<=8` and `b(63)>=65` are mandatory audit points. They must be checked as primary preprints and may not be treated as established merely because they are recent. Determine whether either changes the six-dimensional status, supplies only an adjacent method, or reveals a reusable finite certificate.

Search absence is not a novelty certificate. When reliable sources disagree, preserve both statements and identify the unresolved verification point.

## 2. Minimum finite native diameter interface

Classify at least the following candidate interfaces.

### M0 — finite metric or pseudometric

A finite set `C` with a typed function

`d : C × C -> Q_nonnegative`

or another exact ordered value domain, with explicit symmetry, diagonal and triangle-law status.

For nonempty `A subset C`, define

`diam(A)=max{d(x,y):x,y in A}`.

A Borsuk partition of `A` is a partition into nonempty blocks `A_1,...,A_k` satisfying

`diam(A_i) < diam(A)`

for every block. Define the finite native partition number only after the comparison relation and maximum are typed.

### M1 — maximum-distance relation only

For finite `A`, let `F_A(x,y)` record that the pair realizes `diam(A)`. Prove or refute whether partition into strictly smaller-diameter blocks is exactly proper coloring of the graph `(A,F_A)` under stated hypotheses.

Do not assume that an arbitrary relation is a maximum-distance graph. Determine which finite graphs are realizable under each accepted metric class and which graph certificates are merely comparison objects.

### M2 — relation-spectrum or path-distance input

Audit whether the accepted GEO6 relation-distance spectrum supplies enough structure to define diameter and strict decrease. An ordinary connected graph metric may give a legal finite model, but it is not native P000 unless the graph/path relation itself is independently typed.

### M3 — generalized Borsuk graph or covering input

Classify the exact hypotheses under which chromatic number, group covering number or topological obstruction yields a diameter-partition bound. Preserve the distinction among exact equivalence, one-way implication, strict antecedent and adjacent method.

## 3. Six-dimensional native meaning audit

A finite native Borsuk construction must state what “six-dimensional” means in its own type system. Candidate meanings may include six named axis types, a rank-six action module, a six-coordinate presentation, or a six-parameter relation family, but none is accepted automatically.

For each candidate:

- state the native sorts and relations;
- state which transformations preserve the diameter interface;
- determine whether the dimension label affects the partition theorem or is only presentation metadata;
- give same-readout countermodels when the six-dimensional label fails to determine the metric or maximum-distance relation.

Do not identify `R^6`, `E6`, FCC/HCP carrier data or a six-axis presentation with native P000 identity.

## Hard target

`BORSUK_6D_CURRENT_STATUS_AND_NATIVE_DIAMETER_PARTITION_INTERFACE_EXACTLY_CLASSIFIED`

## Required outputs

1. A dated primary-source status matrix for Euclidean `b(6)`, with exact lower/upper bounds and publication-state labels.
2. A source manifest recording every load-bearing paper or preprint and the precise claim consumed.
3. A typed atlas for M0–M3, including source/target sorts, hypotheses and permitted conversions.
4. A theorem proving the maximum-distance-graph coloring equivalence when valid, or an exact counterexample showing the missing condition.
5. At least one nontrivial finite six-labeled model with an exact Borsuk partition number, plus a lower and upper certificate.
6. At least one same-six-label/same-readout countermodel showing which metric or partition information is not forced by the current native interface.
7. A transfer matrix separating Euclidean theorem, finite metric theorem, graph theorem, topological covering method, P000 consequence and comparison-only analogy.
8. Prior-art classification for every project-local claim: `EXACT_DUPLICATE`, `STRICT_ANTECEDENT`, `ADJACENT_METHOD`, or `NO_MATERIAL_MATCH`.
9. A deterministic checker for all finite enumerations, colorings, diameter computations and countermodels.
10. A fresh execution record and writer-conformant Result with complete Git-blob and SHA-256 bindings for every required output.

## Success outcomes

Any one of the following is valid if fully proved and typed:

- an exact native finite diameter-partition invariant with a nontrivial six-labeled theorem;
- a parameterized counterfamily separating six-dimensional presentation from Borsuk behavior;
- a sharp current-language no-go identifying the minimum missing metric/dimension structure;
- a mixed result combining an exact finite theorem with an obstruction to P000 transfer.

## Kill rules

Kill the execution if it:

- assumes `b(6)=7` without a current proof;
- treats a preprint claim as peer-reviewed fact;
- equates arbitrary graph coloring with diameter partition without proving maximum-distance realization;
- imports Euclidean norm, coordinates, convexity or dimension constants into P000 by name;
- treats six named axes as a metric dimension theorem;
- reopens the closed GEO6 contact/packing/refinement/translation mother questions under new labels;
- promotes search absence or `NO_MATERIAL_MATCH` to novelty;
- publishes its own successor before Driver review.

## Driver handoff

Return one terminal typed classification. Report the exact Euclidean status independently from the native finite result. Grant no Working Truth, Foundation authority, native ontology elevation, classical-to-native theorem transfer or novelty status from the Researcher lane.
