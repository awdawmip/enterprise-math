# R043-C6 — Rooted Successor External Prior-Art and Duplication Audit Return

Status: `FROZEN FINAL RETURN / NO_DIRECT_MATCH_IN_AUDITED_SET / GENERIC_EXTENSION_ORBIT_AND_LOCALITY_SKELETONS_PRIOR_ART / NOT CANONICAL`

Date: `2026-08-29`  
Task-ID: `RS-R043C6-ROOTED-SUCCESSOR-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`  
Publication-ID: `TP2-F92C19B4A40963360BA6`  
Researcher-ID: `EM-R043C6PA-E712E0`  
Claim-ID: `chatgpt-r043c6pa-20260829-1931-e712e0`  
Execution branch: `research/r043c6-rooted-successor-external-prior-art-audit-em-r043c6pa-e712e0`  
Execution base: `1b134d8c55ccd941e4b338752825443589726be2`

## 0. Primary verdict

The hard target is satisfied at **audit scope**:

`R043C6_EXTERNAL_PRIOR_ART_DUPLICATION_STATUS_EXACTLY_CLASSIFIED`.

The classification is:

`NO_DIRECT_MATCH_FOUND_IN_AUDITED_SET / GENERIC_GRAPH_EXTENSION_AUTOMORPHISM_ORBIT_AND_LOCALITY_SKELETONS_ARE_MATURE_PRIOR_ART / NO_IMPORTED_THEOREM_CLOSES_C7`.

This is deliberately not a global novelty or priority claim.

The main boundary is sharp:

1. The generic statement that a base graph plus all missing incidence data determines an augmented graph is ordinary extension bookkeeping, not a novelty basis.
2. Quotienting possible augmentations by `Aut(G,x)` or using a canonical construction path is standard isomorph-free graph-generation machinery.
3. Finite-local update rules are standard in symbolic dynamics/cellular automata.
4. Local topology predicates, including FCC-specific topology-preserving point-deletion rules, are established digital-topology prior art.
5. What was **not** found in the audited set is a theorem with the complete C6/C7 signature: from the **compressed rooted weighted frontier observable** `[G,x]`, classify all **globally FCC/HCP-realizable** hidden `J_x` completions and prove that they form one successor-equivalence orbit, or force a collision.

Therefore any theorem-facing value that survives the audit is in the **compressed-observable native-realizability injectivity/equivalence gate**, not in locality, graph augmentation, automorphism orbits, or FCC neighborhood analysis by themselves.

## 1. Frozen C6/C7 target being compared

The accepted C6 input is:

`ROOTED G0 + J_x -> EXACT ONE-STEP SUCCESSOR`.

For a rooted action `x` in one unoccupied component, the twelve native neighbors split as

`N(x) = I_x disjoint_union A_x disjoint_union Z_x`

with

`|Z_x| = 12 - w_G(x) - deg_G(x) <= 11`.

The hidden completion datum `J_x` consists exactly of:

- edges induced on the newly exposed set `Z_x`;
- native incidences from `Z_x` to the surviving old frontier `F\{x}`.

Once those incidences are supplied, the successor weighted frontier is deterministic.

The C7 research result further reduces the native support of `J_x` to a fixed two-shell carrier: 54 non-root slots in FCC and 56 in HCP, with participating-support bounds 53 and 55 respectively, while explicitly refuting a naïve bounded **abstract-`G0` graph-radius** shortcut.

Thus the external question is not “is graph augmentation/locality known?” It is:

> For one fixed realizable compressed rooted weighted graph `[G,x]`, do all globally native-realizable two-shell slot assignments that induce legal `J_x` data yield successor-equivalent completions, separately in FCC and HCP?

No located source answered that question.

## 2. Reproducible search ledger

Frozen ledger:

`research_artifacts/R043C6_ROOTED_SUCCESSOR_EXTERNAL_PRIOR_ART_DUPLICATION_AUDIT/search_ledger.json`

It records the exact target signature, query families, primary-source metadata, theorem/result paraphrases, C6 hypothesis comparisons, classifications, import value, and explicit limitations.

Search families covered:

- canonical graph augmentation and isomorph-free exhaustive generation;
- graph reconstruction and rooted reconstruction refinements;
- Curtis–Hedlund–Lyndon / cellular local-rule characterization;
- classic 3D digital simple-point theorems;
- FCC-specific topology-preserving reductions;
- FCC topological coordinate/incidence systems;
- HCP/FCC graph-theoretic crystal reconstruction;
- explicit HCP digital-topology keyword combinations.

The audit used theorem/result statements, not keyword resemblance, as the classification unit.

## 3. McKay canonical construction path — closest method-level duplication

Primary source:

Brendan D. McKay, *Isomorph-Free Exhaustive Generation*, Journal of Algorithms 26 (1998), 306–324, DOI `10.1006/jagm.1997.0898`.

McKay's Theorem 1 proves, under the construction-path axioms, that the recursive `scan` procedure outputs exactly one labelled representative of each unlabelled descendant isomorphism class up to the requested order. The procedure explicitly iterates over orbits of admissible upper objects under `Aut(X)`. In the graph specialization, an upper object `<X,W>` appends a new vertex to `X` with neighborhood `W`.

### Exact comparison

| feature | McKay 1998 | C6/C7 |
|---|---|---|
| fixed base object | yes | yes: rooted weighted `[G,x]` |
| augmentation data | yes | yes: `J_x` / native slot assignment |
| automorphism-orbit quotient | yes, central | yes: `Aut(G,x)` |
| isomorph-free representatives | yes | useful for C7 classifier |
| FCC/HCP native realizability | no | essential |
| compressed-observable hidden-completion injectivity | no | essential remaining gate |
| proves one successor orbit for all legal native completions | no | exactly the open C7 question |

Classification:

`PARTIAL_ANALOGUE / METHOD DUPLICATION`.

Consequence: **the orbit quotient itself is not a novelty candidate**. The strongest safe import is algorithmic: a future C7 classifier should use canonical augmentation/orbit representatives rather than raw slot assignments. McKay does not close the mathematical gate.

## 4. Graph reconstruction — related recoverability problem, different observable

Primary source:

Deisiane Lopes Gonçalves and Bhalchandra D. Thatte, *A refinement of Kelly's lemma for graph reconstruction for counting rooted subgraphs*, arXiv:2312.17022 (2023).

The paper recalls Kelly's counting lemma from the vertex-deleted deck and proves a rooted refinement boundary: counting rooted subgraphs with the root at the deleted vertex is impossible in general, while a multiset of rooted subgraphs of fixed height `k` can be counted when the graph radius exceeds `k`; an edge-reconstruction analogue is also proved.

Classification:

`PARTIAL_ANALOGUE / RECONSTRUCTION CONTEXT`.

It does **not** duplicate C6/C7 because:

- its input is a deck of vertex-deleted graphs, not one rooted weighted frontier graph;
- its output is subgraph-count information, not exact one-step successor reconstruction;
- it has no FCC/HCP native realization constraint;
- it supplies neither a uniqueness theorem nor a collision theorem for `J_x`.

Its methodological value is cautionary: rooted hidden information is not automatically reconstructible from a coarser graph observable.

## 5. Cellular automata / symbolic dynamics — locality is prior art, injectivity is not supplied

Primary classic source:

Gustav A. Hedlund, *Endomorphisms and automorphisms of the shift dynamical system*, Mathematical Systems Theory 3 (1969), 320–375, DOI `10.1007/BF01691062`.

The Curtis–Hedlund–Lyndon characterization identifies cellular automata with continuous shift-commuting maps; equivalently, the global update is induced uniformly by a finite local rule on the full symbolic configuration.

Classification:

`PARTIAL_ANALOGUE / LOCALITY`.

The difference is decisive: CHL assumes the relevant local configuration is available. C6/C7 starts from a **lossy quotient** `[G,x]` and asks whether the missing native completion is recoverable up to successor equivalence. Locality of an update from full state gives no injectivity theorem after that information loss.

Hence “the next state is root-local” is not by itself a novelty claim.

## 6. Digital topology — local topology predicates are mature, including on FCC

### 6.1 Classic cubic-grid simple points

Gilles Bertrand and Grégoire Malandain, *A new characterization of three-dimensional simple points*, Pattern Recognition Letters 15 (1994), 169–175, DOI `10.1016/0167-8655(94)90046-9`.

The paper proves a 3D simple-point characterization using two connected-component counts in the point neighborhood, without explicit genus/hole computation.

Gilles Bertrand, *Simple points, topological numbers and geodesic neighborhoods in cubic grids*, Pattern Recognition Letters 15 (1994), 1003–1011, DOI `10.1016/0167-8655(94)90032-9`.

For the `{6,26}` and `{6,18}` connectivity pairs, the paper gives a simple-point characterization by two local conditions derived from geodesic-neighborhood topological numbers.

Classification:

`PARTIAL_ANALOGUE / DIGITAL-TOPOLOGY LOCAL SUFFICIENCY`.

These theorems decide a topology-preservation predicate on a cubic grid. They do not reconstruct the entire weighted successor frontier and do not address hidden completion orbits.

### 6.2 FCC-specific topology-preserving reductions

Gábor Karai, Péter Kardos and Kálmán Palágyi, *Sufficient Conditions for Topology-Preserving Parallel Reductions on the Face-Centered Cubic Grid*, Journal of Mathematical Imaging and Vision 66 (2024), 271–292, DOI `10.1007/s10851-024-01177-y`.

The paper gives sufficient conditions for topology-preserving parallel reductions on three types of 3D FCC binary pictures and local characterizations of P-simple points whose simultaneous deletion preserves topology.

Classification:

`STRONG PARTIAL ANALOGUE / SAME-GRID LOCAL PREDICATE`.

This is an especially important novelty boundary: FCC-specific local point-update theory already exists. But its input is a binary native neighborhood and its conclusion is topology preservation under deletion, not exact addition/frontier exposure from the compressed `[G,x]`. It neither covers HCP nor proves `J_x` orbit uniqueness.

## 7. FCC coordinate reconstruction — exact incidence from a richer carrier

Lidija Čomić and Benedek Nagy, *A topological 4-coordinate system for the face centered cubic grid*, Pattern Recognition Letters 83 (2016), 67–74, DOI `10.1016/j.patrec.2016.03.012`.

The paper proves the coordinate system unambiguous and consistent and shows that incidence, boundary/co-boundary and adjacency relations among FCC cells can be obtained by simple integer operations on the coordinates.

Classification:

`PARTIAL ANALOGUE / RICH-CARRIER INCIDENCE`.

This does not duplicate C7 because coordinates provide **more information** than `[G,x]`: once native slots are identified, incidence is easy; the unresolved problem is whether slot identity/completion is forced up to successor equivalence by the compressed graph observable.

This source supports a useful conceptual separation:

`native coordinate/slot assignment -> incidence`

is established machinery, whereas

`compressed rooted G0 -> native slot-assignment orbit`

is the unresolved map.

## 8. HCP and recent FCC/HCP graph reconstruction search

A recent graph-theoretic crystal-structure paper was audited:

Tomoyasu Yokoyama, Kazuhide Ichikawa and Hisashi Naito, *From polyhedra to crystals: a graph-theoretic framework for crystal structure generation*, CrystEngComm 28 (2026), 2293–2304, DOI `10.1039/D5CE01176K`.

It reconstructs FCC, HCP and BCC structures from **dual periodic graphs** using standard realization.

Classification:

`CONTEXTUAL NONMATCH / RICH GLOBAL GRAPH REALIZATION`.

The dual periodic graph is a much richer global input than one local compressed frontier observable. The work does not decide local hidden-completion uniqueness.

Explicit HCP digital-topology and neighborhood queries did not locate a direct HCP theorem with the C6/C7 signature. This statement is only about the documented audited query set; it is not an absence theorem for the literature.

## 9. Hypothesis-by-hypothesis classification

| source family | rooted weighted `[G,x]` | hidden `J_x` completion | FCC | HCP | global native realizability over same observable | automorphism/orbit machinery | exact weighted successor equivalence | classification |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| McKay canonical augmentation | no | generic analogue | no | no | no | **yes** | generic isomorphism only | partial / method duplicate |
| Kelly/rooted reconstruction | different rooted object | no | no | no | no | not the target | no | partial |
| CHL cellular locality | no | full local state instead | generic lattice | generic lattice | no | no | local rule, different output | partial |
| Bertrand digital topology | no | no | no | no | no | no | topology predicate only | partial |
| Karai–Kardos–Palágyi | no | native binary neighborhood | **yes** | no | no | no | topology predicate only | strong partial |
| Čomić–Nagy FCC coordinates | no | explicit rich coordinates | **yes** | no | no | no | incidence only | partial |
| Yokoyama–Ichikawa–Naito | no | global dual periodic graph | **yes** | **yes** | different realization problem | no | crystal realization | contextual nonmatch |

No audited row matches all target columns.

## 10. What is prior art, and what remains genuinely open after the audit

### Mature / should not be sold as new

- “base + explicit missing edges determines extension”;
- automorphism-orbit quotienting of augmentations;
- canonical isomorph-free enumeration;
- finite-local update from full cellular configurations;
- local simple-point/topology-preservation criteria;
- FCC-specific local topology-preserving reductions;
- exact FCC incidence calculation from richer coordinate data.

### Search-bounded unmatched residue

No audited theorem establishes:

`fixed rooted weighted G0 + global FCC/HCP realizability -> one successor-equivalence orbit of J_x`.

Nor did the audit locate a theorem forcing a harmful pair.

Therefore the exact C7 gate survives:

`NATIVE-REALIZABLE TWO-SHELL SLOT ASSIGNMENT ORBIT UNIQUENESS VS HARMFUL COLLISION`.

This is the appropriate locus for future mathematical effort.

## 11. Imported theorem/method assessment for C7

`IMPORTED_THEOREM_CLOSING_C7 = NONE_FOUND`.

`IMPORTED_METHOD = MCKAY_CANONICAL_CONSTRUCTION_PATH`.

A disciplined next classifier can:

1. fix `[G,x]`;
2. enumerate only native two-shell slot assignments compatible with visible weights/edges;
3. quotient candidate assignments under the root stabilizer and `Aut(G,x)`;
4. reject globally unrealizable assignments;
5. construct `Succ([G,x],J_x)`;
6. canonicalize the successor weighted graph;
7. stop immediately if one current class splits into two successor classes.

This avoids a broad animal census and uses established isomorph-free generation methodology without confusing the method with the missing theorem.

## 12. Conservative novelty wording

Safe wording:

> In the documented audited source set, the generic extension, automorphism-orbit and locality ingredients of C6 are established prior art. No theorem was found that combines the frozen FCC/HCP native-realizability constraint with the compressed rooted weighted frontier observable and proves or refutes successor-equivalence of all compatible `J_x` completions. This is a search-bounded nonmatch, not a claim of global novelty or priority.

Unsafe wording to reject:

- “C6 is new because it is local.”
- “Using `Aut(G,x)` to quotient completions is new.”
- “FCC local point-update rules are new.”
- “No one has studied graph reconstruction on FCC/HCP.”
- “The audit proves C7 uniqueness.”

## 13. Search limitations

- The audit is high-recall and primary-source oriented but not exhaustive over subscription theorem indexes such as MathSciNet/zbMATH/Scopus.
- Several publisher records exposed precise abstracts/results rather than full theorem bodies; those were used only at the result scope visible from the primary/publisher record.
- Search failure is reported only as `NO_DIRECT_MATCH_FOUND_IN_AUDITED_SET`.
- Literature similarity is not mathematical evidence for C7 itself.
- No Foundation or Working Truth promotion is requested.

## 14. Final classification

Hard target:

`R043C6_EXTERNAL_PRIOR_ART_DUPLICATION_STATUS_EXACTLY_CLASSIFIED = SATISFIED_AT_AUDIT_SCOPE`.

Final audit class:

`NO_DIRECT_MATCH_IN_AUDITED_SET`.

Prior-art guard:

`GENERIC_EXTENSION + AUT_ORBIT + CANONICAL_AUGMENTATION + LOCALITY + FCC_LOCAL_TOPOLOGY = NOT NOVELTY-BEARING_BY_THEMSELVES`.

Remaining theorem-facing residue:

`COMPRESSED_ROOTED_WEIGHTED_G0 -> NATIVE_REALIZABLE_J_X_SUCCESSOR_ORBIT UNIQUENESS/COLLISION`.

C7 closure imported from literature:

`NONE_FOUND`.

Recommended next control-plane action:

`DRIVER_REVIEW; IF C7 RETURNS TO EXECUTION, USE AN EXACT MCKAY-STYLE CANONICAL NATIVE TWO-SHELL SLOT-ASSIGNMENT CLASSIFIER MODULO ROOT STABILIZER AND Aut(G,x), WITH GLOBAL REALIZABILITY FILTERS AND SUCCESSOR-CLASS SPLIT AS THE KILL CONDITION.`

No Foundation promotion is requested.
