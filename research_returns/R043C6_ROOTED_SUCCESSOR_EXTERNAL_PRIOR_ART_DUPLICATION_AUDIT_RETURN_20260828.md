# R043-C6 — Rooted Successor External Prior-Art / Duplication Audit Return

Status: `FROZEN FINAL RETURN / NO_DIRECT_MATCH_IN_AUDITED_SET / CLOSE_PARTIAL_ANALOGUES_IDENTIFIED / C7_NOT_CLOSED`

Date: `2026-08-28`  
Task-ID: `RS-R043C6-ROOTED-SUCCESSOR-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`  
Publication-ID: `TP2-F92C19B4A40963360BA6`  
Researcher-ID: `EM-R043C6PA-9C9ACF`  
Claim-ID: `chatgpt-r043c6pa-20260828-1457-8d3a61`  
Execution-ID: `ER-B836B8F262CF8A96CFA4`  
Execution branch: `research/r043c6-rooted-successor-prior-art-duplication-em-r043c6pa-9c9acf`  
Execution base: `a5aebf8537ab59585f2e370482ed729109727e84`

## 0. Primary verdict

`R043C6_EXTERNAL_PRIOR_ART_DUPLICATION_STATUS_EXACTLY_CLASSIFIED = YES`.

Audit result:

`NO_DIRECT_MATCH_FOUND_IN_THE_AUDITED_SET`.

The accepted C6 reduction is **not** duplicated, in the audited literature set, by a theorem with the same four ingredients simultaneously:

1. the observable is one arbitrary reachable rooted **weighted frontier graph** `[G,x]` rather than all local balls of a whole graph;
2. the hidden datum is the bounded exposed-neighbor incidence profile `J_x` with `|Z_x| <= 11`;
3. admissibility is **global realizability inside frozen FCC or HCP**;
4. uniqueness is taken only up to rooted-current automorphisms / successor-equivalence.

Strong neighboring theorems exist in graph reconstruction, local-to-global rigidity, kissing/contact geometry, Barlow packing theory, and digital FCC geometry. They are classified below. None imports a theorem that settles the remaining C7 gate.

A crucial novelty-control correction is also frozen:

> Once `J_x` is defined to contain exactly all successor incidences not already present in `G-x`, the final abstract-graph step “`[G,x] + J_x` determines the successor graph” is essentially definitional. It should not be advertised as a new general graph-reconstruction theorem. The model-specific mathematical content of C6 is the exact proof that **no deeper FCC/HCP geometry can influence one step after `J_x` is fixed**, together with the uniform `|Z_x| <= 11` compression and the resulting realizable-completion orbit gate.

This distinction is the main duplication/novelty hygiene result of the audit.

## 1. Frozen target being audited

The Driver-accepted C6 theorem states that for an admissible root `x` in one connected frontier slice:

- `[G,x]` determines the surviving old frontier;
- `[G,x]` determines all updated weights of surviving old vertices;
- `[G,x]` determines
  `|Z_x| = 12 - w_G(x) - deg_G(x) <= 11`;
- the only missing one-step information is `J_x`, consisting of the induced contact relations inside `Z_x` and contacts from `Z_x` to the surviving old frontier;
- therefore
  `ROOTED G0 + J_x -> EXACT ONE-STEP SUCCESSOR`.

Raw rooted-`G0` sufficiency is exactly the bounded completion question:

> For fixed realizable `[G,x]`, do all globally realizable `J_x` completion profiles induce successor-equivalent weighted graphs, or is there a harmful split?

The present audit asks whether that theorem or its open completion-orbit gate is already an instance/specialization of established external results.

## 2. Exact comparison matrix

| Source / theorem family | External hypothesis/data | External conclusion | Comparison to C6 | Classification |
|---|---|---|---|---|
| Benjamini–Ellis (2016), `3-locally L^d` | every vertex has the same radius-3 lattice ball | finite connected graph is a quotient lattice / globally rigid structure | far stronger and global uniform local data; square lattice, not arbitrary FCC/HCP frontier | `PARTIAL_ANALOGUE` |
| de la Salle (2019), LG-rigidity | every sufficiently large local ball matches a fixed vertex-transitive graph | covering/local-to-global rigidity for broad classes | frontier after arbitrary occupation is not vertex-transitive and does not satisfy uniform ball matching | `PARTIAL_ANALOGUE` |
| Levenshtein et al. (2008), graph from 2-vicinities | radius-2 metric balls around **all** vertices, plus girth/diameter hypotheses | exact reconstruction of whole graph | different observable and target; no lattice realizability or rooted update | `PARTIAL_ANALOGUE` |
| Hammack–Mullican (2017), neighborhood reconstruction | multiset of all open neighborhoods | exact characterization of neighborhood-reconstructible graphs via cancellation | demonstrates local-neighborhood ambiguity but does not address partial FCC/HCP completion | `PARTIAL_ANALOGUE` |
| Flatley–Theil (2015) + Flatley et al. (2013), kissing/contact rigidity | complete 12-neighbor shell with maximal contact count; stronger regularity/second-neighbor conditions for propagation | shell is cuboctahedral or twisted-cuboctahedral; stronger data can select FCC | closest native geometric theorem, but C6 permits arbitrary partial frontier/exposed sets and asks uniqueness of `J_x` over a fixed frontier | `CLOSE_PARTIAL_ANALOGUE` |
| Conway–Sloane (1997), Barlow coordination sequences | entire close-packed stacking | coordination/crystal-ball bounds; FCC and HCP extremal | useful structural warning about stacking information, not an extension/reconstruction theorem | `CONTEXTUAL_ANALOGUE` |
| Čomić–Nagy (2016), digital FCC coordinates | full FCC cell-coordinate carrier | adjacency/incidence computable by integer rules | implementation carrier only; no completion uniqueness | `NONMATCH` |
| Kusner et al. (2018), twelve-sphere configuration space | complete 12-sphere kissing configurations | FCC/HCP occur as distinct constrained contact configurations | shows that 12-neighbor count alone is insufficient; no frontier-completion theorem | `GEOMETRIC_CONTEXT` |
| Yokoyama–Ichikawa–Naito (2026), dual periodic graph reconstruction | full dual periodic graph encoding crystal connectivity | reconstruct FCC/HCP/BCC via standard realization | input dominates C6 and already contains global periodic connectivity | `RECENT_STRONG_INPUT_NONMATCH` |

## 3. Graph-reconstruction literature does not directly duplicate C6

### 3.1 Metric-ball reconstruction

Levenshtein, Konstantinova, Konstantinov and Molodtsov prove exact reconstruction for a connected graph from radius-2 metric balls at **all** vertices under girth/diameter restrictions. This is a genuine local-information reconstruction theorem, but the data model differs in every critical way:

- their balls are taken in the unknown graph itself;
- the full family of balls over every vertex is provided;
- shared vertex labels encode consistency across balls;
- the conclusion reconstructs the entire static graph;
- there is no native-lattice realizability constraint or growth action.

C6 instead has one current rooted frontier state and asks which hidden native contacts will become visible after occupying `x`. Therefore the Levenshtein theorem is not an imported solution to either C6-T1 or the `J_x` orbit gate.

### 3.2 Neighborhood-multiset reconstruction

Hammack–Mullican study reconstruction from the multiset of all open neighborhoods and prove an exact equivalence with a graph-product cancellation property. Their framework is important because it explicitly permits nonisomorphic graphs with identical neighborhood multisets; local neighborhood summaries do not generically imply uniqueness.

However, C6 does not observe the neighborhood multiset of the unknown successor. It observes a rooted weighted induced frontier graph before the action, with native FCC/HCP realizability restricting allowed hidden extensions. Thus this line is a conceptual analogue, not duplication.

### 3.3 One-vertex/graph-extension terminology

Searches for “graph extension theorem”, “one-vertex extension”, rooted graph extension, and extension modulo automorphisms returned several established meanings—distance-hereditary graph construction operations, group-theoretic graph extension theorems, random-graph extension statements, and specialized rooted extension frameworks. None uses C6's extension object: a bounded set `Z_x` of newly exposed lattice sites together with its incidences to an already-visible frontier, filtered by global FCC/HCP realizability.

Consequently, terminology overlap alone is unsafe evidence of duplication.

## 4. Local-to-global rigidity is the closest abstract theorem family, but its hypotheses miss the frontier problem

Benjamini–Ellis prove a sharp local-to-global result for graphs locally indistinguishable from the integer lattice: sufficiently large uniform lattice balls at **every** vertex force a quotient-lattice global structure, with smaller radius known to fail in the corresponding setting.

De la Salle later develops local-to-global rigidity for broad classes of vertex-transitive graphs and also shows the phenomenon is not automatic for every finitely presented Cayley graph.

These results are highly relevant methodologically because they show the right theorem shape for turning finite-radius local data into global rigidity. They do **not** settle C7 because:

1. a finite occupied cluster destroys vertex transitivity of its frontier;
2. `[G,x]` need not be a ball in the ambient FCC/HCP contact graph;
3. weights encode occupancy contacts, not just graph distance;
4. only one rooted action site is fixed, not all vertices;
5. C7 asks whether *multiple hidden completions over the same visible partial state* collapse after the successor quotient.

Thus an FCC/HCP analogue of LG-rigidity, even if available for the full ambient contact graph, would require an additional theorem showing that arbitrary reachable frontier partials inherit a sufficient local-recognition condition. No such bridge was found.

## 5. FCC/HCP geometric literature gives the strongest partial analogue

Flatley–Theil's crystallization analysis uses two exact local facts that are directly adjacent to C6:

- the 3D kissing number is 12;
- among separated points on the unit sphere, a 12-neighbor contact graph has at most 24 tangencies, with equality only in the cuboctahedral (FCC-type) or twisted-cuboctahedral (HCP-type) configurations.

Their local-neighborhood proposition therefore reduces a maximally regular 12-neighbor shell to two close-packed local types. With stronger second-neighbor/global regularity information, their argument can propagate/select FCC structure.

This is **not** C6 duplication. C6's rooted frontier can be very incomplete:

- `Z_x` can have size `0,...,11` rather than 12;
- some native neighbors of `x` are occupied and therefore absent from the unoccupied frontier;
- some are already visible frontier vertices and some are newly exposed;
- `J_x` includes contacts from new sites to arbitrary surviving frontier sites;
- the hidden completion must be compatible with a whole finite occupied configuration, not merely a standalone kissing shell.

The Flatley–Theil theorem could become an ingredient in a future proof if a C7 argument can force a completed 12-shell or enough second-neighbor regularity from `[G,x]`. The current hypotheses do not supply that bridge.

Therefore:

`IMPORTED_FCC_HCP_LOCAL_RECOGNITION_THEOREM_CLOSES_C7 = NO`.

## 6. Barlow packing literature warns against overcompression

Conway–Sloane treat the full class of Barlow packings generated by stacking hexagonal layers. Their coordination-sequence theorem distinguishes FCC and HCP as extremal close-packed structures and records that close-packed stacking choices affect larger contact-distance data.

Kusner–Kusner–Lagarias–Shlosman likewise treat FCC and HCP as distinct 12-sphere contact configurations in the twelve-spheres configuration space.

These sources support a conservative inference:

> “12 native neighbors” or another coarse first-shell statistic is not, by itself, a universal certificate of one close-packed continuation.

They do **not** furnish a harmful C6 collision, because a collision must preserve the *entire rooted weighted frontier isomorphism class* `[G,x]` and differ only through globally realizable `J_x` completions whose successors are inequivalent. No source found constructs that exact pair.

## 7. Digital-topology / crystal-graph sources are carriers, not uniqueness theorems

Čomić–Nagy provide exact FCC coordinate and incidence machinery. This can support an implementation of a native completion classifier but does not prove that a partial frontier has a unique realizable completion orbit.

The 2026 Yokoyama–Ichikawa–Naito graph-to-crystal framework reconstructs FCC/HCP/BCC from dual periodic graphs. That result is useful as recent adjacent prior art, but its input contains a full periodic connectivity object; it is therefore strictly stronger than the C6 observable and cannot be used to infer raw rooted-`G0` sufficiency.

## 8. Direct-duplication verdict by claim component

### 8.1 Claim component A — “successor is determined once all missing incidences are supplied”

`ABSTRACT_GRAPH_NOVELTY = NOT_CLAIMED`.

This is a definitional reconstruction statement: a graph is determined once its vertex set, inherited edges, and every remaining new incidence are specified. External graph theory does not need a special theorem for this final assembly step.

### 8.2 Claim component B — “`J_x` is the only hidden one-step datum in FCC/HCP”

`DIRECT_EXTERNAL_DUPLICATION_FOUND = NO_IN_AUDITED_SET`.

This is the substantive C6 reduction: weights, surviving vertices, new-vertex weights, and old-old edges are forced by `[G,x]`, leaving only root-local native incidences involving `Z_x`.

### 8.3 Claim component C — uniform bound `|Z_x| <= 11`

`DIRECT_EXTERNAL_DUPLICATION_FOUND = NO_SPECIAL_THEOREM_NEEDED`.

The numerical bound is an immediate model-specific consequence of 12-contact degree and `w_G(x) >= 1`; kissing-number literature supplies the broader 12-neighbor geometric background but not the frontier identity in C6's notation/model.

### 8.4 Claim component D — all realizable `J_x` are successor-equivalent for fixed `[G,x]`

`STATUS = OPEN`.

No audited theorem proves it; no audited theorem supplies a harmful collision either.

## 9. C7 importability audit

The task required identification of any external theorem capable of resolving C7. Result:

`C7_RESOLVING_IMPORTED_THEOREM = NONE_FOUND`.

The nearest possible imports fail as follows:

- **Benjamini–Ellis / local-to-global lattice recognition**: requires uniform balls at every vertex and a full lattice-like graph.
- **de la Salle LG-rigidity**: requires a fixed vertex-transitive reference graph and large-ball local equality.
- **Levenshtein metric-ball reconstruction**: needs all vertex balls and girth/diameter restrictions.
- **Flatley–Theil FCC/HCP local recognition**: needs complete maximally regular shells and, for global FCC selection, stronger second-neighbor regularity.
- **dual periodic graph reconstruction**: starts from global periodic connectivity.

A valid import would still need a new bridge theorem translating an arbitrary reachable rooted weighted frontier into one of those stronger data regimes. That bridge is essentially the unresolved C7 mathematics, so importing the external theorem alone does not close the task.

## 10. Recommended mathematical continuation

The prior-art audit changes the next research direction in a useful way: do not spend a continuation re-proving broad graph reconstruction or full-lattice local-to-global rigidity. The narrow live gate is native completion realizability.

Highest-value continuation:

`R043C7_BOUNDED_REALIZABLE_JX_COMPLETION_ORBIT_CLASSIFICATION`.

Recommended attack order:

1. **Native radius bound.** Determine whether global realizability of `J_x` is decidable from a bounded native neighborhood around `x`. If yes, prove the smallest sufficient radius.
2. **Completion CSP modulo `Aut(G,x)`.** Enumerate native slot assignments only after a theorem bounds the needed local carrier; quotient exact completions by rooted-current automorphisms and then by successor isomorphism.
3. **Directed stacking-fault pressure.** In HCP/FCC layer coordinates, explicitly search for two globally extendable local native completions with identical visible `[G,x]` but different `J_x`; Barlow stacking freedom is a principled negative-search source.
4. **Positive local-recognition pressure.** Test whether Flatley–Theil-style shell constraints force a unique completion when enough of the 12-contact shell is already represented in `C union F`.
5. **Do not infer global theorem from root-star census.** The accepted C6 finite census remains regression evidence only until a completeness radius/extension theorem is proved.

## 11. Conservative novelty wording

Safe wording for future Driver/publication use:

> “Within the audited graph-reconstruction, local-to-global rigidity, digital-topology, and close-packed-lattice literature, we found strong partial analogues but no theorem with the same rooted weighted frontier observable, global FCC/HCP realizability condition, bounded `J_x` completion datum, and successor-equivalence quotient. C6 should therefore be described as a model-specific exact reduction to a bounded local completion problem, not as a new general graph-reconstruction theorem. The absence of a direct match is only an audited-set statement, not a global novelty claim.”

Unsafe wording:

- “No prior art exists.”
- “C6 proves a new graph reconstruction theorem.”
- “Local FCC/HCP geometry uniquely determines `J_x`.”
- “The external literature proves raw `G0` rigidity.”
- “The root-star census establishes global uniqueness.”

## 12. Search ledger and limitations

Reproducible query families, venues, source metadata, and source-by-source classifications are frozen in:

`research_artifacts/R043C6_ROOTED_SUCCESSOR_EXTERNAL_PRIOR_ART_DUPLICATION_AUDIT/SEARCH_LEDGER.md`.

The audit is deliberately bounded. It does not claim exhaustive MathSciNet/Zentralblatt/citation-network coverage, complete non-English coverage, or unpublished-manuscript coverage. Some publisher pages were accessible only through abstracts/institutional copies. Therefore the terminal status is exactly:

`NO_DIRECT_MATCH_FOUND_IN_THE_AUDITED_SET`,

not a universal novelty certification.

## 13. Final classification

Hard target:

`R043C6_EXTERNAL_PRIOR_ART_DUPLICATION_STATUS_EXACTLY_CLASSIFIED = SATISFIED`.

Direct duplication:

`DIRECT_DUPLICATION = NONE_FOUND_IN_AUDITED_SET`.

Closest external analogues:

`LOCAL_TO_GLOBAL_LATTICE_RECOGNITION + METRIC_BALL_RECONSTRUCTION + FCC/HCP_LOCAL_SHELL_RIGIDITY`.

Imported theorem resolving C7:

`NONE_FOUND`.

C6 novelty-control refinement:

`ABSTRACT_SUCCESSOR_ASSEMBLY_IS_DEFINITIONAL; MODEL_SPECIFIC_JX_ONLY_COMPRESSION_IS_THE_SUBSTANTIVE_CONTENT`.

Remaining mathematical gate:

`GLOBAL_REALIZABLE_J_X_ORBIT_UNIQUENESS_OR_HARMFUL_COLLISION_FOR_FIXED_ROOTED_G0`.

Recommended next action:

`DRIVER_REVIEW_THIS_AUDIT; IF_ACCEPTED, CONTINUE_ONLY_WITH_BOUNDED_REALIZABLE_JX_COMPLETION_ORBIT_CLASSIFICATION, NOT_A_BROAD_PRIOR_ART_OR_GENERIC_GRAPH_RECONSTRUCTION LANE`.
