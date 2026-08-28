# R043-C6 External Prior-Art Audit — Reproducible Search Ledger

Date: 2026-08-28  
Researcher-ID: `EM-R043C6PA-9C9ACF`  
Task: `RS-R043C6-ROOTED-SUCCESSOR-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`

## 1. Frozen comparison target

The audit compares external literature against the accepted internal reduction:

- current observable: a rooted weighted frontier graph `[G,x]` in a frozen FCC or HCP 12-contact world;
- hidden one-step datum: `J_x`, containing the induced relations among newly exposed zero-weight neighbors `Z_x` and their incidences to the surviving old frontier;
- exact internal reduction: `[G,x] + J_x -> exact one-step successor`;
- uniform bound: `|Z_x| = 12 - w_G(x) - deg_G(x) <= 11`;
- unresolved gate: for fixed realizable `[G,x]`, whether every globally realizable `J_x` lies in one successor-equivalence orbit modulo rooted-current automorphisms.

The audit therefore rejects a source as a direct match if it requires substantially stronger data, reconstructs a different object, omits global FCC/HCP realizability, or proves only a generic local-to-global/cell-complex statement.

## 2. Query ledger

Web-indexed primary-source and institutional-source searches were executed on 2026-08-28. Query families included:

1. `locally indistinguishable from a lattice graph Benjamini Ellis theorem Z^d`
2. `r-locally graph covering lattice theorem Benjamini Ellis`
3. `local-to-global rigidity Cayley graph ball covering theorem`
4. `neighborhood reconstruction graph theorem open neighborhoods graph reconstruction`
5. `rooted graph extension neighborhood reconstruction theorem graph`
6. `graph extension prescribed neighborhood theorem`
7. `one-vertex extension graph reconstruction neighborhood theorem`
8. `reconstructing a graph from balls Levenshtein metric balls graph`
9. `Levenshtein graph radius 2 metric balls reconstruction`
10. `Barlow packings FCC HCP stacking sequences primary paper`
11. `close-packed stacking sequence FCC HCP Barlow packing local structure`
12. `Barlow packings coordination sequence theorem 1997`
13. `face-centered cubic graph local recognition theorem`
14. `face-centered cubic crystallization atomistic configurations theorem 3.5`
15. `FCC HCP contact graph sphere packing`
16. `face-centered cubic digital topology adjacency graph`
17. `face centered cubic grid digital topology`
18. `graph extension automorphism orbit prescribed neighborhood`
19. `rooted graph automorphism extension uniqueness`

Venues/surfaces reached included Cambridge/Forum of Mathematics Sigma, Wiley/Journal of Topology, Electronic Journal of Combinatorics, ScienceDirect/Discrete Applied Mathematics and Discrete Mathematics, Archive for Rational Mechanics and Analysis via Warwick/arXiv, Proceedings of the Royal Society A / author archive, Pattern Recognition Letters institutional metadata, RSC/CrystEngComm, arXiv, and author/institutional publication pages.

## 3. Audited primary or primary-adjacent sources

### S1 — Benjamini & Ellis (2016), local lattice recognition

Itai Benjamini and David Ellis, *On the structure of graphs which are locally indistinguishable from a lattice*, Forum of Mathematics, Sigma 4 (2016), e31. DOI: `10.1017/fms.2016.30`.

Precise relevant statement audited: for `d >= 3`, finite connected graphs whose radius-3 ball about every vertex is isomorphic to the radius-3 ball of the integer lattice `L^d` have a rigid quotient-lattice description `L^d / Gamma` by an appropriate crystallographic group. The paper also establishes that radius 2 does not suffice in the corresponding sense.

Audit relevance: strong local-to-global reconstruction analogue, but its observation is *all radius-3 balls at all vertices* of an entire graph, not a single rooted weighted frontier state. Its model is `Z^d`, not the FCC/HCP frontier-completion category, and it does not classify `J_x` or successor-equivalence orbits.

Classification: `PARTIAL_ANALOGUE / NOT_DIRECT_DUPLICATION`.

### S2 — de la Salle (2019), local-to-global rigidity from large balls

Mikael de la Salle, *Characterizing a vertex-transitive graph by a large ball*, Journal of Topology 12(3) (2019), 705–743. DOI: `10.1112/topo.12095`.

Precise relevant statement audited: a large class of vertex-transitive graphs has local-to-global rigidity—there exists a radius such that any graph locally matching that graph at the specified scale is covered by it. The paper also supplies counterexamples showing that finite presentation alone does not guarantee this property.

Audit relevance: this is conceptually close to the desired shape “finite local data force global structure”, but it presupposes uniform large-ball agreement with a fixed vertex-transitive graph. A reachable frontier graph after arbitrary finite occupation is neither vertex-transitive nor globally locally identical to FCC/HCP.

Classification: `PARTIAL_ANALOGUE / HYPOTHESES_TOO_STRONG_AND_DIFFERENT`.

### S3 — Levenshtein–Konstantinova–Konstantinov–Molodtsov (2008), reconstruction from 2-balls

V. I. Levenshtein, E. V. Konstantinova, E. V. Konstantinov, S. G. Molodtsov, *Reconstruction of a graph from 2-vicinities of its vertices*, Discrete Applied Mathematics 156(9) (2008), 1399–1406. DOI: `10.1016/j.dam.2006.11.016`.

Precise relevant statement audited: a connected graph of diameter at least 4 and girth at least 7 is exactly reconstructible from the radius-2 metric balls centered at all vertices; examples at smaller girth/diameter show failure outside the stated regime.

Audit relevance: genuine reconstruction from local metric information, but the input is the complete family of all radius-2 vertex balls with shared labels. C6 observes only one rooted frontier graph plus weights, and the open gate concerns admissible *extensions of that partial frontier* inside FCC/HCP.

Classification: `PARTIAL_ANALOGUE / DIFFERENT_DATA_MODEL`.

### S4 — Hammack & Mullican (2017), neighborhood reconstruction

Richard H. Hammack and Cristina Mullican, *Neighborhood Reconstruction and Cancellation of Graphs*, Electronic Journal of Combinatorics 24(2) (2017), P2.8. DOI: `10.37236/6676`.

Precise relevant statement audited: graphs reconstructible from the multiset of their open vertex-neighborhoods are exactly the cancellation graphs for the relevant direct-product cancellation property; the paper explicitly notes that non-isomorphic graphs can share the same neighborhood multiset.

Audit relevance: confirms that neighborhood data can be insufficient and gives an exact characterization in a different reconstruction model. It neither uses lattice realizability nor a rooted action/update map, and therefore does not decide the `J_x` orbit gate.

Classification: `PARTIAL_ANALOGUE / NONMATCH_TO_C6_OBSERVABLE`.

### S5 — Flatley & Theil (2015), FCC/HCP local-neighborhood rigidity

Lisa Flatley and Florian Theil, *Face-centered cubic crystallization of atomistic configurations*, Archive for Rational Mechanics and Analysis 218(1) (2015), 363–416. DOI: `10.1007/s00205-015-0862-1`. Preprint: arXiv:1407.0692.

Precise relevant statements audited:

- The 3D kissing number is 12.
- For a separated set on the unit sphere, the contact graph has at most 24 edges; equality occurs only for the cuboctahedral or twisted-cuboctahedral 12-point configurations. The paper cites Flatley–Tarasov–Taylor–Theil (2013) for that tangency theorem.
- Under its regularity assumptions, a nearest-neighborhood attaining the maximal local edge count is therefore locally of FCC or HCP type; stronger second-neighbor information can select the FCC lattice globally.

Audit relevance: this is the closest geometric prior art found. It recognizes complete 12-neighbor local shells and propagates full-lattice structure under stronger regularity conditions. C6 instead starts from an arbitrary finite occupied state and a partial *frontier* graph with weights. `Z_x` may be any size from 0 to 11 and the open question is which partial completion profiles are globally realizable over the same rooted frontier. The cited theorem does not state or imply uniqueness of those completion orbits.

Classification: `CLOSE_PARTIAL_ANALOGUE / DOES_NOT_CLOSE_C7`.

### S6 — Conway & Sloane (1997), Barlow packing coordination sequences

J. H. Conway and N. J. A. Sloane, *Low-Dimensional Lattices VII: Coordination Sequences*, Proceedings of the Royal Society A 453 (1997), 2369–2389. DOI: `10.1098/rspa.1997.0126`.

Precise relevant statement audited: for Barlow packings (stackings of hexagonal layers), the paper proves extremal bounds on coordination/crystal-ball sequences and identifies FCC and HCP as the extremal packings in the stated all-center/all-distance sense.

Audit relevance: establishes that close-packed stacking geometry affects higher contact-distance data even though all Barlow packings share close-packed local structure. It is useful warning evidence against inferring global stacking from too-small local summaries, but it does not present the C6 frontier observable or a one-step completion theorem.

Classification: `CONTEXTUAL_ANALOGUE / NOT_RECONSTRUCTION_DUPLICATION`.

### S7 — Čomić & Nagy (2016), digital FCC incidence coordinates

Lidija Čomić and Benedek Nagy, *A topological 4-coordinate system for the face centered cubic grid*, Pattern Recognition Letters 83 (2016), 67–74. DOI: `10.1016/j.patrec.2016.03.012`.

Precise relevant content audited: the paper gives a symmetric coordinate system for FCC cells in which incidence, co-boundary, and adjacency relations can be derived by integer operations.

Audit relevance: useful carrier/implementation prior art for FCC digital topology, but no theorem reconstructs a frontier successor from a rooted weighted graph or proves uniqueness of globally realizable local completion profiles.

Classification: `IMPLEMENTATION_ANALOGUE / NONMATCH`.

### S8 — Kusner–Kusner–Lagarias–Shlosman (2018), twelve-sphere configuration space

Rob Kusner, Wöden Kusner, Jeffrey C. Lagarias, Senya Shlosman, *Configuration Spaces of Equal Spheres Touching a Given Sphere: The Twelve Spheres Problem*, Bolyai Society Mathematical Studies 27 (2018), 219–277; arXiv:1611.10297.

Precise relevant content audited: the FCC and HCP kissing configurations are treated as distinct 12-sphere contact configurations with different symmetry/contact structures inside the constrained configuration space.

Audit relevance: reinforces that “12 neighbors” by itself does not identify one unique close-packed local geometry. It does not classify partial exposed-neighbor completion orbits over a frontier graph.

Classification: `GEOMETRIC_CONTEXT / NONMATCH`.

### S9 — Yokoyama–Ichikawa–Naito (2026), reconstruction from dual periodic graphs

Tomoyasu Yokoyama, Kazuhide Ichikawa, Hisashi Naito, *From polyhedra to crystals: a graph-theoretic framework for crystal structure generation*, CrystEngComm 28 (2026), 2293–2304. DOI: `10.1039/D5CE01176K`.

Precise relevant content audited: FCC, HCP, and BCC crystal structures are reconstructed through a pipeline whose input is a dual *periodic* graph encoding full space-filling polyhedral connectivity, followed by standard realization.

Audit relevance: recent graph-to-crystal reconstruction prior art, but the input already contains global periodic connectivity far richer than `[G,x]` or `J_x`. It therefore cannot be imported to settle C7.

Classification: `RECENT_STRONG-INPUT_NONMATCH`.

## 4. Negative-search domains

No direct theorem was located in the audited set under combinations of:

- rooted weighted graph + prescribed local completion + automorphism orbit;
- FCC/HCP frontier graph + one-step growth/reconstruction;
- close-packed contact graph + partial boundary completion uniqueness;
- digital FCC adjacency + unique local extension;
- local weak / local-to-global graph reconstruction + one rooted action;
- graph extension + global lattice realizability + successor equivalence.

The phrase “graph extension theorem” also retrieves unrelated group-theoretic and random-graph extension theorems; these were rejected because their extension objects/hypotheses are not C6 completions.

## 5. Search limitations

This is a theorem-level web-indexed audit, not an exhaustive bibliographic proof of global novelty. Limitations:

- no claim of complete MathSciNet/Zentralblatt/citation-graph exhaustion;
- some publisher full texts are paywalled, so institutional/arXiv versions and publisher abstracts were used where available;
- the search was English-language and theorem/key-concept focused;
- no assertion is made about unpublished manuscripts or terminology so different that it is absent from indexed abstracts/full-text search.

The only licensed conclusion is therefore: `NO_DIRECT_MATCH_FOUND_IN_THE_AUDITED_SET`, not “no prior art exists”.
