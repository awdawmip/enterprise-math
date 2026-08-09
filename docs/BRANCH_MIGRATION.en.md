# Enterprise Math Branch Migration and Research Continuity Map

Status: `ACTIVE MIGRATION PLAN / NON-DESTRUCTIVE`  
Snapshot date: `2026-08-09`  
Architecture branch base: `main@9fe0eb4b9a5a635a029ca5c0d0b5211280aa0c2c`

## 1. Purpose

This migration changes **where future work should continue**, not the history of where earlier work happened.

No existing research branch is deleted, force-moved, or rewritten by this plan. A new continuation branch created at an old head is an alias for future research ownership; the old branch remains an auditable provenance object.

Because several branches are highly diverged from current `main`, these continuation branches are **not merge candidates as a whole**. Canonical integration must be done later by semantic replay of selected results onto latest main.

## 2. Exact branch moves made in this migration

### 2.1 Former P019 minimum-precision geometry / relation branch

Historical mixed branch:

`research/p019-minimum-precision-lattice-geometry`

Repository branch head observed for this migration:

`6b0a6160ed96d397c84bcb03926e5267256dfa99`

The branch contains both geometry-specific research and a later, more general relation/partition theory. It must therefore split by **future ownership**, while retaining one shared history.

New continuation branches created at the exact same head:

- `research/core/relation-quotient` @ `6b0a6160ed96d397c84bcb03926e5267256dfa99`
- `research/p022-minimum-precision-geometry` @ `6b0a6160ed96d397c84bcb03926e5267256dfa99`

#### Continue on `research/core/relation-quotient` when working on

- capacity-weighted relation state `(m,C,Z)`;
- arbitrary partition quotient `Q_A`;
- partition kernel `K_A` and invisible-motion/state-fiber identification;
- relation rank and relation scale;
- exact refinement memory / Refinement Forest as a present-state reconstruction tool;
- relation observations that are not inherently geometric;
- generic witness/value/provenance distinctions;
- comparison with E001 admissible-support relations;
- the minimum exact relation state required by a declared future operation language.

Do **not** add a new `P` number here yet. First distill the mathematical interface and prior-art boundary.

#### Continue on `research/p022-minimum-precision-geometry` when working on

- `A_p`, FCC/HCP/BCC or other lattice candidates;
- primitive graph distance and geometry-specific shortest-path structure;
- finite balls/shells and coordinator counts;
- radial/quadratic distance observations and triangle/distance carry;
- spherical excavation specifically as a geometry theorem;
- isotropy/anisotropy tests and geometry-specific counterexamples;
- geometry-aware collapse.

Before P022 promotion, replay only the geometry-owned results onto latest main and rename historical `P019_*` assets to canonical `P022_*` names. Do not merge the mixed historical branch wholesale.

### 2.2 P019 relation checkpoint history

The earlier pause checkpoint remains unchanged:

- `checkpoint/p019-relation-quotient-20260809-0914` @ `1bc0e4a3e96833a553bc52dc51ea88483bedf486`
- `research/p019-relation-quotient-continuation` @ `1bc0e4a3e96833a553bc52dc51ea88483bedf486`

After that checkpoint, the original mixed branch advanced by additional commits to `6b0a616...`. Therefore these two `1bc0e4a...` refs are **historical audit anchors**, not the current continuation frontier. They must not be force-updated to hide the gap.

### 2.3 Historical P019 black-hole branch → P021

Historical branch:

`research/p019-discrete-black-hole-horizon`

Observed head:

`e8d176b30e7e52ca75b2ae9467066ea4f8f5af6c`

New continuation branch created at the exact same head:

`research/p021-causal-focusing` @ `e8d176b30e7e52ca75b2ae9467066ea4f8f5af6c`

Continue P021 work on the new branch. Preserve:

- causal boundary/horizon constructions;
- future-section expansion and focusing spectra;
- direction orbits and causal roles;
- witness-level direction transport;
- the demonstrated distinction between a count/cardinality shadow and the identities required for exact composition.

When a statement becomes a general quotient/witness-sufficiency theorem independent of the physical interpretation, lift that mother statement into A2/P023 or the relation core and keep the P021 specialization here.

Physical claims remain downstream of the mathematical model and P016 falsification requirements.

### 2.4 E001 engineering branch → separate general relation continuation

Current E001 branch:

`agent/e001-multires-collision`

Observed head:

`6e2dc72e46885c081278228838831cd87eb8167c`

The branch started as an engineering collision pressure test but now also contains reusable mathematics: admissible support relations, common-target composition, relation spectra, support precision, and limits of functional-collapse modeling.

New general-mathematics continuation created at the exact same head:

`research/core/admissible-support-relations` @ `6e2dc72e46885c081278228838831cd87eb8167c`

#### Continue on `agent/e001-multires-collision` for

- collision engine implementation;
- broad phase and adaptive refinement schedule;
- terminal oracle comparison;
- workload/CPU/materialization benchmarks;
- engineering certificates and failure/performance analysis.

#### Continue on `research/core/admissible-support-relations` for

- functional versus relational collapse;
- radius-indexed admissible relation families;
- common-target relation composition;
- split-completeness and atomic counterexamples;
- MAY/MUST support semantics as a relation input to P018 precision;
- `W_k` witness spectra and `G_k` group/event spectra;
- the theorem `W_k=G_k=J_k` for graphs of total functions;
- higher-order common-target structure not recoverable from pair graphs;
- admissibility constraints that prevent arbitrary support-intersection graphs from becoming an unconstrained ontology.

The two branches share history at the split point. After the split, a general theorem should be developed in the core branch and consumed by E001 rather than copied into two independent implementations.

## 3. Active routes that are deliberately not renamed now

### 3.1 P018

Current active branch/PR route remains:

`agent/p018-critical-grid` / PR #68, verified research head `948e2dd452ccbd3e33e81586f566715c094f5551` at its recorded checkpoint.

P018 continues to own precision interpretation, pair/kernel precision structure, defect/response, precision-time filtration, and precision-specific dynamic closure.

Before adding another general predictive-closure theorem, compare it directly with P023. If P023 already supplies a strictly more general operation-language statement, P018 should add only the precision specialization/corollary.

### 3.2 P023

Current branch remains:

`research/p023-composition-safe-collapse`

Recorded PR head:

`3601235fd87cc8dcb961599155ff9500a4e67d52`

The branch name already matches its emerging general role. It remains the candidate home for future-compatible quotient, factorization/congruence, minimal repair, and operation-family closure. Promotion still requires its own clean current-main replay and gates.

### 3.3 P017

P017 remains a pressure-test program whose canonical accepted results are integrated incrementally into main. Existing `agent/p017-*`, `agent/legendre-*`, and `integration/p017-*` branches are not bulk-renamed in this migration.

Rule for future P017 work:

- square-basin-specific constraints remain P017;
- a result whose prime/Legendre assumptions can be removed is lifted to the appropriate reusable home;
- once two P017 routes are proved to be the same object in different coordinates, maintain one canonical statement and mark the other as a representation/corollary;
- stale historical PRs are closed only after an equivalence audit verifies that their unique mathematics has been preserved.

### 3.4 Canonical P019/P020

Canonical `P019` remains collapse-word stabilization; `P020` remains well-founded finite stabilization. No branch migration in this document changes those canonical meanings.

## 4. Researcher resume table

| Research subject | Resume branch | Immediate next question |
|---|---|---|
| General relation / partition quotient | `research/core/relation-quotient` | What is the minimum exact relation state for a declared future operation/observation language? |
| Minimum-precision geometry | `research/p022-minimum-precision-geometry` | Which geometry results remain after extracting relation-generic machinery? |
| Causal focusing / black-hole application | `research/p021-causal-focusing` | Which witness identities are mathematically necessary before any physical interpretation is added? |
| Admissible supports / common-target relations | `research/core/admissible-support-relations` | What axioms on generated support relations are strong enough to yield nontrivial theorems without being universally expressive? |
| E001 engineering | `agent/e001-multires-collision` | Can the structural reduction in exact work become a robust implementation win without changing exact semantics? |
| P018 precision calculus | `agent/p018-critical-grid` | Which remaining results are precision-specific after comparison with P023? |
| P023 quotient safety | `research/p023-composition-safe-collapse` | Can one general theorem cover unary predictive closure, finite operation families, and minimal repair cleanly? |
| P017 pressure test | fresh/current P017 research branch from latest main | Can lower-band descent or resource coupling create a genuinely new deterministic bound rather than another coordinate rewrite? |

## 5. Cross-branch synchronization rule

Do not synchronize these long-lived branches by repeated wholesale merges.

For a reusable result:

1. prove/audit it in its owning continuation branch;
2. record the source branch/commit where it was first discovered;
3. create a clean integration branch from **latest main**;
4. replay only the owning theorem, executable specification, tests, bilingual prose, and provenance records;
5. add application corollaries in separate or clearly delimited commits;
6. allow source research branches to keep their historical local numbering and experiments.

This prevents old ledgers or stale bilingual manifests from overwriting concurrent canonical work.

## 6. No-delete / no-orphan guarantee

A historical branch or open PR may be marked superseded only when all of the following are known:

- every unique proved statement has a new owner or is explicitly rejected by counterexample;
- unique executable tests/counterexamples have been preserved or intentionally retired with a reason;
- prior-art/source lineage has been carried forward;
- the old researcher's next branch is named explicitly;
- the new route can reconstruct the provenance link back to the old commit.

Until then, historical branches stay available.

## 7. Next migration step

The next architecture pass should not create more branch aliases automatically. It should:

1. compare the two new relation-core continuations theorem-by-theorem;
2. build a single concept-lineage matrix with `same / strict generalization / specialization / independent / conflict` edges;
3. identify the smallest clean relation-core integration slice that can be replayed onto latest main;
4. only then decide whether that reusable core deserves a new numbered problem, a non-numbered library module, or eventual `FOUNDATIONS` status.
