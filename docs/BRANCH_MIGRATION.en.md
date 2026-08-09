# Enterprise Math Branch Migration and Research Continuity Map

Status: `ACTIVE MIGRATION PLAN / NON-DESTRUCTIVE`  
Snapshot date: `2026-08-09`  
Architecture branch base: `main@9fe0eb4b9a5a635a029ca5c0d0b5211280aa0c2c`

## 1. Purpose

This migration changes **where future work should continue**, not the history of where earlier work happened.

No existing research branch is deleted, force-moved, or rewritten by this plan. A new continuation branch created at an old head is a new future-research home; the old branch remains an auditable provenance object.

Because several branches are highly diverged from current `main`, these continuation branches are **not merge candidates as a whole**. Canonical integration must later be performed by semantic replay of selected results onto latest main.

A continuation branch may advance after the split while another branch deliberately remains at the common split point. The migration map therefore records both the **split commit** and the **current frontier**.

## 2. Exact branch moves and current frontiers

### 2.1 Former P019 minimum-precision geometry / relation branch

Historical mixed branch:

`research/p019-minimum-precision-lattice-geometry`

Common split commit used when the new homes were created:

`6b0a6160ed96d397c84bcb03926e5267256dfa99`

Two continuation branches were created from that exact state:

- `research/core/relation-quotient`
- `research/p022-minimum-precision-geometry`

The split immediately exposed a real ownership test. Three later commits on the historical mixed branch added observation-aware minimum exact relation precision, relation-rank cost, and operation/observation language refinement. Those results did not use new lattice geometry. They were therefore routed only to the relation-state continuation.

Current frontiers at this snapshot:

- historical mixed branch: `research/p019-minimum-precision-lattice-geometry@3caa6a1cf8562747b12a808d1c2ade333280083d`
- A3 relation-state continuation: `research/core/relation-quotient@3caa6a1cf8562747b12a808d1c2ade333280083d`
- P022 geometry continuation: `research/p022-minimum-precision-geometry@6b0a6160ed96d397c84bcb03926e5267256dfa99`

This is intentional. It is the first post-migration example where new work was classified by mathematical ownership instead of being copied to both descendants.

#### Continue on `research/core/relation-quotient` for A3 work

The central object is the structured weighted integer relation-state, not a general binary support relation.

Continue here for:

- capacity-weighted relation state `(m,C,Z)` with `Z_ij=m_j c_i-m_i c_j`;
- arbitrary partition quotient `Q_A` and `Z'=AZA^T`;
- partition kernel `K_A`, invisible-motion/state-fiber identification;
- relation rank, relation-scale quantum, and exact refinement cost;
- exact present-state refinement data / Refinement Forest;
- linear operation and observation languages on the structured relation state;
- coarsest observation refinement and stable-dynamics refinement;
- minimum exact relation precision required by a declared future task;
- comparison with P018/P023 future-compatible quotient as a structured specialization;
- explicit bridge questions to A4, without assuming the two relation objects are identical.

Do **not** add a new `P` number yet. First distill the mathematical interface, bridge hypotheses, and prior-art boundary.

#### Continue on `research/p022-minimum-precision-geometry` for geometry-owned work

Continue here for:

- `A_p`, FCC/HCP/BCC or other lattice candidates;
- primitive graph distance and geometry-specific shortest paths;
- finite balls/shells and coordinator counts;
- radial/quadratic distance observations and triangle/distance carry;
- spherical excavation specifically as a geometry theorem;
- isotropy/anisotropy tests and geometry-specific counterexamples;
- geometry-aware collapse.

Before P022 promotion, replay only geometry-owned results onto latest main and rename historical `P019_*` assets to canonical `P022_*` names. Do not merge the mixed historical branch wholesale.

### 2.2 P019 relation checkpoint history

The earlier pause checkpoint remains unchanged:

- `checkpoint/p019-relation-quotient-20260809-0914@1bc0e4a3e96833a553bc52dc51ea88483bedf486`
- `research/p019-relation-quotient-continuation@1bc0e4a3e96833a553bc52dc51ea88483bedf486`

The original mixed branch later advanced first to `6b0a616...` and then to `3caa6a1...`. The `1bc0e4a...` refs are therefore **historical audit anchors**, not the current continuation frontier. They must not be force-updated to hide the intervening research history.

### 2.3 Historical P019 black-hole branch → P021

Historical branch:

`research/p019-discrete-black-hole-horizon`

Migration head:

`e8d176b30e7e52ca75b2ae9467066ea4f8f5af6c`

New continuation:

`research/p021-causal-focusing@e8d176b30e7e52ca75b2ae9467066ea4f8f5af6c`

Continue P021 work on the new branch. Preserve:

- causal boundary/horizon constructions;
- future-section expansion and focusing spectra;
- direction orbits and causal roles;
- witness-level direction transport;
- the demonstrated distinction between cardinality shadows and the identities required for exact later composition.

When a statement becomes independent of causal/physical interpretation and becomes a general quotient or witness-sufficiency theorem, compare it against A2/P023 before creating another general theorem family. P021 keeps direction/causal applications and provenance.

Physical claims remain downstream of the mathematical model and P016 falsification requirements.

### 2.4 E001 engineering branch → A4 admissible-support continuation

E001 branch and split/current head at this snapshot:

`agent/e001-multires-collision@6e2dc72e46885c081278228838831cd87eb8167c`

A4 continuation created from the same exact state and currently still there:

`research/core/admissible-support-relations@6e2dc72e46885c081278228838831cd87eb8167c`

The E001 branch contains two different kinds of assets and they now have different future owners.

#### Continue on `agent/e001-multires-collision` for

- collision engine implementation;
- broad phase and adaptive refinement schedule;
- terminal oracle comparison;
- workload/CPU/materialization benchmarks;
- engineering certificates, negative results, and performance analysis.

#### Continue on `research/core/admissible-support-relations` for A4 work

The central object is a finite multivalued support/correspondence `R⊆X×Z`, not A3's structured integer field.

Continue here for:

- functional versus relational collapse;
- radius-indexed admissible support families `R_r`;
- relation composition and common-target relations;
- relational subadditivity and split-completeness boundaries;
- MAY/MUST support semantics as an input to P018 precision;
- `W_k` witness spectra and `G_k` group/event spectra;
- exact `W_k=G_k=J_k` degeneration for graphs of total functions;
- higher-order common-target structure not recoverable from pair graphs;
- admissibility constraints preventing unconstrained universal support graphs;
- future bridge theorems to A3 only when an explicit generator/factorization is proved.

The two branches share history at the split point. After the split, a general A4 theorem should be developed on the A4 branch and consumed by E001 instead of being duplicated in engineering modules.

### 2.5 A3 and A4 must not be silently recombined

The architecture audit found that the word “relation” denotes two different objects:

- A3: a structured weighted integer relation-state `Z_ij=m_jc_i-m_ic_j` attached to capacities/totals and partition quotients;
- A4: a finite binary support/correspondence `R⊆X×Z` describing allowed target states.

They are currently `COMPOSABLE_INDEPENDENT`, not one unified relation theory. A bridge must be a theorem, not a naming decision.

## 3. Active routes deliberately not renamed now

### 3.1 P018

Current active route remains:

`agent/p018-critical-grid@948e2dd452ccbd3e33e81586f566715c094f5551` / PR #68.

P018 owns precision interpretation, pair/kernel precision structure, defect/response, precision-time filtration, and precision-specific dynamic closure.

The theorem audit now gives a stronger deduplication rule:

- P018 T160–T168 and P023 T03–T07 are the same finite-unary mother theorem family;
- P023 T10–T14 is the finite operation-family strict generalization;
- future general extensions go through P023/A2;
- P018 adds only precision-specific consequences and applications.

### 3.2 P023

Current branch remains:

`research/p023-composition-safe-collapse@3601235fd87cc8dcb961599155ff9500a4e67d52`

P023 remains the candidate general home for future-compatible quotient, factorization/congruence, operation-family closure, and minimal repair. Its one-step/minimal-repair line is related to but not identical with predictive closure.

Promotion still requires clean latest-main replay and ordinary repository gates.

### 3.3 P017

P017 remains a pressure-test program whose accepted results are integrated incrementally into main. Existing `agent/p017-*`, `agent/legendre-*`, and `integration/p017-*` history is not bulk-renamed.

Future rule:

- square-basin/least-factor/resource-specific constraints remain P017;
- remove prime/Legendre assumptions when proofs permit and lift the mother theorem upward;
- once two routes are proved to be the same object in different coordinates, maintain one canonical statement and retain the other as a representation/corollary;
- stale historical PRs are closed only after an equivalence audit preserves their unique mathematics.

### 3.4 Canonical P019/P020

Canonical `P019` remains collapse-word stabilization. `P020` remains well-founded finite stabilization. Historical `P019_*` geometry/relation filenames are a naming collision only and confer no canonical ownership.

## 4. Researcher resume table

| Research subject | Resume branch | Immediate next question |
|---|---|---|
| A3 structured relation-state / partition quotient | `research/core/relation-quotient` | Prove the exact bridge from A3 task-derived linear relation precision to the general A2/P023 future-compatible quotient language; then test whether any A4 support query factors through it. |
| P022 minimum-precision geometry | `research/p022-minimum-precision-geometry` | Replay the geometry-only theorem stack from the split point and identify which radial/distance results remain after all A3-generic machinery is removed. |
| P021 causal focusing / black-hole application | `research/p021-causal-focusing` | Separate causal/direction-specific witness identities from the already-general P023 quotient-sufficiency rule before adding physical interpretation. |
| A4 admissible supports / common-target correspondence | `research/core/admissible-support-relations` | Find nontrivial admissibility axioms and determine exactly which A4 observables are generated by geometry or can factor through an A3 state. |
| E001 engineering | `agent/e001-multires-collision` | Determine whether reduced exact work yields a robust implementation win without changing exact semantics; keep negative benchmark evidence. |
| P018 precision calculus | `agent/p018-critical-grid` | Stop duplicating the unary closure mother theorem; push precision-specific kernel/time/defect/repair consequences around the P023 general core. |
| P023 quotient safety | `research/p023-composition-safe-collapse` | Consolidate the unary duplicate, retain operation-family closure as the general extension, and continue minimal-repair/arithmetic sufficiency research. |
| P017 pressure test | fresh/current P017 branch from latest main | Seek genuinely new deterministic lower-band/resource coupling rather than another coordinate rewrite. |

## 5. Cross-branch synchronization rule

Do not synchronize long-lived branches by repeated wholesale merges.

For a reusable result:

1. prove/audit it in the owning continuation branch;
2. record the source branch/commit where it was first exposed;
3. classify its relation to existing theorems as `same`, `strict generalization`, `specialization`, `independent`, or `conflict`;
4. create a clean integration branch from **latest main**;
5. replay only the mother theorem, executable specification, tests, bilingual prose, and provenance records;
6. add application corollaries separately or in clearly delimited commits;
7. allow source research branches to retain historical numbering and experiments.

This prevents stale ledgers or manifests from overwriting concurrent canonical work.

## 6. No-delete / no-orphan guarantee

A historical branch or open PR may be marked superseded only when all of the following are known:

- every unique proved statement has a new owner or is explicitly rejected by counterexample;
- unique executable tests/counterexamples are preserved or intentionally retired with a recorded reason;
- prior-art/source lineage is carried forward;
- the old researcher's next branch is named explicitly;
- the new route can reconstruct provenance back to the old commit.

Until then, historical branches stay available.

## 7. Next migration step

The theorem-level concept-lineage matrix now exists in `docs/CONCEPT_LINEAGE.*`. Therefore the next migration pass is no longer “compare two relation cores and merge them.” The audit proved they are distinct.

The next work is:

1. formalize the A3→A2/P023 specialization bridge;
2. search for restricted A3↔A4 bridge theorems without presupposing equivalence;
3. isolate the smallest clean A3 integration slice independent of historical P019/P022 naming;
4. isolate the smallest clean A4 integration slice independent of E001 engineering;
5. replay P022 and P021 only after those reusable dependencies are explicit;
6. decide on a new numbered problem or `FOUNDATIONS` status only after these slices survive prior-art and integration review.
