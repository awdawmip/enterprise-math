# Enterprise Math Research Architecture

Status: `PROPOSED / MIGRATION IN PROGRESS`  
Effective snapshot: `2026-08-09`  
Source-main snapshot: `9fe0eb4b9a5a635a029ca5c0d0b5211280aa0c2c`

## 1. Purpose and authority boundary

Enterprise Math has grown beyond a linear list of numbered problems. The numbered `Pxxx` and `Exxx` programs remain important research identities and provenance anchors, but several branches now discover the same mathematical structure from different domains.

This document adds a **second organizational axis** for reusable mathematics. It does not renumber solved problems, silently widen a `RESOLVED` scope, promote research-WIP into `FOUNDATIONS`, or change the authoritative status ledger in `PROBLEM_STATUS`.

The governing rule is:

> Preserve the place where a result was discovered, but maintain the most general proved statement only once, in the narrowest reusable mathematical home that actually owns its hypotheses.

A problem branch keeps its domain-specific corollary, examples, counterexamples, motivation, and provenance even when its mother theorem is lifted into a reusable core.

A second rule is equally important:

> Similar vocabulary is not evidence of identical mathematics. Two routes are merged only after an explicit equivalence, specialization, or strict-generalization theorem is established.

## 2. Two orthogonal axes

### Axis A — reusable mathematical homes

These are theorem homes, not new axiom labels.

#### A0. Primitive discrete state algebra

Primary sources: `P001–P009`.

Objects include integer roots and collapses, signed-state distinctions, total scale factors, typed scale transitions, exact quotient/remainder semantics, order adjoints, composition, commutation, and fixed-point structure.

This layer supplies operations and type discipline to later programs. Its resolved problem scopes remain controlled by `PROBLEM_STATUS`.

#### A1. Functional dynamics, kernels, and stabilization

Primary sources: `P010`, `P011`, canonical `P019`, `P020`, with links to `P018`.

This home is for single-valued deterministic maps and their fibers: strict history merging, collision spectra, time-resolved kernel growth, eventual coalescence, and finite stabilization.

The canonical meaning of `P019` is **collapse-word stabilization**. Historical research files that used `P019` for geometry or relation work do not acquire canonical `P019` ownership merely because the old filenames survive on research branches.

#### A2. Precision, observation, and future-compatible quotient

Primary sources: `P018` and `P023`, with arithmetic instances from `P002/P007` and applications from `P017/P021/E001`.

This home contains finite observations, refinement fibers, exact defect/response transport, proof-specific ambiguity, dynamic closure/congruence, predictive refinement, minimal repair, and the rule that detail may be discarded only when the required future operations and observations descend through the quotient.

`P018` remains the finite-precision calculus. `P023` is the candidate home for the most general future-compatible quotient theorem family. Until `P023` is integrated, this is an ownership plan rather than a canonical renumbering of already proved P018 statements.

#### A3. Partition relation-state algebra — candidate reusable core

Primary source: the later stages of the former minimum-precision-geometry branch, now continued on `research/core/relation-quotient`, with links to `P018/P022/P023`.

Its central object is a **structured integer relation field**, not an arbitrary binary relation. For positive block capacities `m_i` and integer block totals `c_i`, the current route uses

`Z_ij = m_j c_i - m_i c_j`.

Together with capacities and grand total, a legal `Z` reconstructs the current block totals. Partition coarsening acts by aggregating capacities/totals and by `Z' = A Z A^T`; the associated integer partition kernel describes both the state fiber and coarse-invisible additive motion.

Current A3 candidates include:

- tree-independent weighted relation state `(m,C,Z)`;
- arbitrary partition quotient and composition;
- partition kernel `K_A`, relation rank, and relation-scale quantum;
- exact present-state refinement data and Refinement Forest;
- minimum exact partition/relation precision required by declared linear operations and observations;
- geometry-independent observation channels defined on the structured relation state.

A3 is **not yet a Foundation and is not assigned a new `P` number**. It must first be distilled from historical P019/P022 naming and audited against prior art.

#### A4. Admissible support / correspondence algebra — candidate reusable core

Primary source: E001 relational-collapse work, now continued on `research/core/admissible-support-relations`, with links to `P011/P012/P018`.

Its central object is a **finite binary relation / correspondence** `R ⊆ X×Z`, generally multivalued. A source may have several allowed target states. This is not the same object as A3's skew integer field `Z_ij`.

Current A4 candidates include:

- functional collapse versus multivalued relational support;
- radius-indexed admissible relation families `R_r`;
- monotonicity and relational subadditivity `R_r ; R_s ⊆ R_(r+s)`;
- split-completeness as the stronger equality case rather than a universal axiom;
- common-target composition `R_r ; converse(R_s)`;
- target-incidence representations;
- witness spectrum `W_k` and group/event spectrum `G_k`;
- exact degeneration `W_k=G_k=J_k` when the relation is the graph of a total function;
- higher-order common-target structure and admissibility constraints.

A4 is also **RESEARCH WIP**, not a Foundation or a newly numbered problem.

#### A3/A4 bridge — explicitly open

The word “relation” is overloaded across A3 and A4. No equivalence is currently assumed.

A3 is a structured numeric state representation derived from capacities and totals. A4 is a set-valued incidence/correspondence between sources and allowed targets.

A bridge theorem would need to answer questions such as:

- when is an A4 support family generated completely from an A3 state plus declared geometry/operations?
- when does an A4 observation factor through an A3 partition quotient?
- which A3 internal relations are necessary to reconstruct or decide an A4 common-target query?

Until such statements are proved, the two cores remain siblings rather than one merged “relation theory.”

#### A5. Intrinsic discrete geometry

Primary sources: `P012` and `P022`, consuming A0/A2/A3/A4 where useful.

This home is for primitive adjacency, integer shortest-path metrics, lattice/root-lattice geometry, finite balls and shells, distance carry, radial/quadratic observations, and geometry-specific contraction results.

Geometry may generate A4 admissible support relations and may be observed through A3 structured relation states, but neither general relation-state algebra nor general support/correspondence algebra should remain trapped inside a geometry-numbered branch.

### Axis B — research and application programs

Problem/application programs remain first-class even when they reuse Axis-A mathematics.

- `P017`: Legendre/consecutive-square pressure test and its square-basin arithmetic structures.
- `P018`: finite-precision proof calculus and precision-specific applications.
- `P021`: finite-precision causal horizon/focusing and physical-facing directional research.
- `P022`: minimum-precision lattice geometry and distance/carry research.
- `E001`: executable collision/common-collapse pressure test.
- `P016`: falsification contract governing physical realizations.

A program is allowed to discover a general theorem. When that happens, the general statement is lifted to Axis A while the program keeps the original specialization and provenance.

## 3. Already identified cross-route consolidations

### 3.1 P017 → P018: quotient response and basin transport

P017's exact cofactor-window width was shown to be the same `whole blocks + boundary carry` pattern already present in P018 quotient response. Those are one structure in different coordinates and should not be maintained as independent theories.

Likewise the square-basin/floor-division result discovered in P017 no longer needs a prime hypothesis: the general theorem belongs to P018 quotient/root transport, while P017 keeps the lower-band least-factor application.

### 3.2 P018 ↔ P023: predictive closure versus general future-compatible quotient

P018's dynamic-closure/predictive-closure results and P023's future-compatible quotient results share the same mother question: when does a coarse observation admit exact autonomous future evolution, and what is the coarsest repair if it does not?

Working ownership rule:

- P018 owns the precision interpretation, precision-time filtration, defect/response coordinates, and finite-precision applications;
- P023 owns the general operation-language factorization/congruence/minimal-repair statements after promotion;
- theorem equivalence or strict generalization must be recorded explicitly instead of duplicating theorem families under two vocabularies.

### 3.3 P021 → P023: witness identity before cardinality collapse

P021 direction transport produced an important negative result: count matrices can preserve adjacent cardinalities while losing the identities needed for exact later composition. Its safe reduction regimes motivated the broader rule that witness detail may be discarded only after future compositional sufficiency is proved.

The general quotient-safety rule belongs in A2/P023. P021 keeps direction-orbit, causal-role, focusing, and witness-join applications.

### 3.4 P011 → A4 relation spectra: functional maps are a special case

For a finite relation `R ⊆ X×Z`, E001 relational work separates witness multiplicity `W_k` from common-target group/event count `G_k`. When `R` is the graph of a total function `F`, both reduce exactly to P011's `J_k(F)`.

Therefore P011 remains the canonical single-valued/function-partition spectrum. A4 may generalize it to relations, but must state the degeneration theorem explicitly and must not silently replace P011's monotonicity results by claims that fail for multivalued relations.

### 3.5 E001 ↔ P018 ↔ A4

E001 no longer owns an independent precision calculus. P018 already supplies finite observation/refinement logic, including MAY/MUST-style refinement behavior once the observation is applied to finite supports.

The split is:

- A4 owns admissible target/support relations and common-target mathematics;
- P018/A2 owns observation/refinement and future compatibility;
- E001 owns the executable collision workload, certificates, schedules, benchmarks, and engineering falsification.

### 3.6 Former P019 relation-state work ↔ P022 ↔ P023

The former geometry branch discovered tree-independent weighted relation state `(m,C,Z)`, partition quotient `Q_A`, integer kernel `K_A`, and exact refinement-memory results. Those are more general than lattice geometry.

The split is:

- A3 owns the abstract structured relation-state/partition representation and kernel algebra;
- P022 owns root-lattice, metric, ball, radial, distance-carry, and geometry-specific contraction statements;
- A2/P023 owns the future-language condition determining when A3's erased internal relations may actually be forgotten.

The post-split relation branch has already continued this direction with observation-aware minimum exact relation precision; this is A3/A2 work, not new P022 geometry.

### 3.7 P012 → A4/E001/P022: geometry as a generator of admissible supports

P012's primitive adjacency can generate finite graph balls and hence A4 target-support relations. E001's square supports are one concrete instance. This makes the dependency direction explicit:

`primitive geometry -> admissible supports -> support observations -> precision/refinement -> application decision`.

It prevents an application-specific collision formula from being mistaken for a new primitive geometry.

### 3.8 A3 ↔ A4: bridge required, not assumed

A3 and A4 may interact strongly, but their current objects are not interchangeable.

A3 can reconstruct a present block-total state from structured weighted relations. A4 asks which target states are admissible for each source and how those target sets compose/intersect. A future result may show that a particular A4 family is a derived observation of a particular A3 state, but that must be proved for the declared generator/geometry.

This distinction prevents a terminology-driven false unification.

## 4. Theorem lifting protocol

When a branch appears to discover a reusable result:

1. **Preserve the discovery branch and exact commit.** Do not force-rebase it merely to rename the idea.
2. **Identify the weakest hypotheses.** Remove domain assumptions one at a time and retain explicit counterexamples for assumptions that cannot be removed.
3. **Compare against existing routes.** Search for equivalent invariants, coordinate transforms, special cases, and already-known prior art.
4. **Classify the relationship before merging.** Use at least `same`, `strict generalization`, `specialization`, `independent`, or `conflict`.
5. **Choose one mother statement only after Step 4.** The most general proved statement gets one reusable home; original programs retain corollaries and provenance.
6. **Record both directions of reuse.** The source program cites the lifted theorem; the reusable core cites the source discovery and application.
7. **Replay semantically onto latest main.** Never merge a highly diverged historical branch wholesale when a clean current-main replay can isolate the result.
8. **Pass ordinary repository gates.** Bilingual pairing, reference/lineage integrity, tests, and applicable Lean gates remain unchanged.
9. **Do not promote vocabulary into ontology.** Coordinates, charts, witnesses, observations, relations, and physical interpretations stay separated unless a theorem proves an invariant identification.

## 5. Non-destructive migration rules

- Existing branches are history, not clutter to be deleted during this migration.
- Exact checkpoint branches remain fixed audit anchors.
- New continuation branches may point at the same commit as an old branch; this is an intentional namespace migration, not a copy of mathematical authority.
- No existing open PR is closed merely because a better branch name now exists. Close/supersede only after a clean replay or explicit equivalence audit identifies what has been preserved.
- No historical `P019_*` geometry/relation file may be promoted to main under that number. Canonical `P019` already means collapse-word stabilization.
- `P021` physical interpretations remain downstream of mathematical statements and the P016 falsification contract.
- A3/A4 work remains `RESEARCH WIP` until theorem boundaries, prior art, and clean integration are audited.

## 6. Immediate research frontiers after migration

1. Build a theorem-by-theorem lineage matrix for A3 and A4 separately before attempting any bridge theorem.
2. Determine whether any A4 admissible-support family relevant to E001/P022 factors through A3 weighted relation state, and what information is lost when it does not.
3. Prove or refute the exact equivalence between P018 predictive closure and the relevant P023 operation-language closure statements; keep only one general theorem family.
4. Generalize P011 to A4 relations only with separate `W_k` and `G_k` semantics and explicit monotonicity boundaries.
5. Replay P022 geometry from the mixed historical branch onto current main using A3/A4 abstractions only where they genuinely reduce the geometry.
6. Replay P021 onto current main under its canonical number while preserving witness identity and physical/falsification boundaries.
7. Keep E001 engineering measurements separate from mathematical claims; use extracted reusable cores as dependencies rather than growing duplicate theory inside the benchmark branch.
8. Continue P017 as a pressure test: lift general results upward, retain square-basin-specific constraints locally, and stop duplicate coordinate routes once equivalence has been proved.

## 7. Architecture invariant

The migration is successful only if a researcher can answer all four questions without losing prior work:

1. Where was this result discovered?
2. What is its most general proved mathematical form?
3. Which current branch should continue that general form?
4. Which problem/application branch still consumes it?

If reorganizing the repository makes any of these answers harder to recover, the reorganization is wrong.
