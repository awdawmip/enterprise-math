# HODGE H0 Literature / Prior-Art Matrix

Status: `FROZEN / H0 BENCHMARK ONLY`  
Researcher-ID: `EM-HODGE-H0-2F8C71`  
Task: `RS-HODGE-H0-ENTERPRISE-REALIZATION-NONTRIVIALITY`  
Verified: `2026-08-17`

The matrix is a firewall, not a generator. Classical and prior-art constructions below may test or calibrate H0 but are not inherited as Enterprise primitives.

| Item | Exact object / theorem | Assumptions | Status | H0 may use | H0 may not inherit |
|---|---|---|---|---|---|
| Hodge decomposition | `H^n(X,C)=⊕_{p+q=n}H^{p,q}(X)` for compact Kähler `X`; smooth projective complex varieties are included | compact Kähler / smooth projective complex | `CLASSICAL_THEOREM` | type/target benchmark | decomposition, harmonic representatives, Kähler metric as Enterprise generator |
| Cycle class map | codimension-`p` algebraic cycle `Z` gives `cl(Z)∈H^{2p}(X,Z)` and its complex image is `(p,p)` | smooth projective complex variety | `CLASSICAL_THEOREM` | define eventual comparison/lifting target | prelabel an Enterprise cycle with the known classical cycle class |
| Hodge conjecture | `H^{2p}(X,Q)∩H^{p,p}(X)` is spanned over `Q` by algebraic cycle classes | smooth projective complex variety | `CLASSICAL_OPEN_CONJECTURE` | freeze exact target only | any part of the conjectural answer |
| Lefschetz `(1,1)` | integral `(1,1)` classes in `H^2` are first Chern classes of line bundles/divisors | smooth projective complex variety | `CLASSICAL_THEOREM` | later algebraicity gate; H0 benchmark | use its proof/result to manufacture Enterprise chains |
| Hard Lefschetz | cup product with a hyperplane/Kähler class gives the classical Lefschetz isomorphisms | smooth projective / compact Kähler | `CLASSICAL_THEOREM` | later structural comparison | Enterprise Lefschetz operator |
| Hodge–Riemann bilinear relations | primitive Hodge components obey the classical sign/positivity relations | compact Kähler / smooth projective | `CLASSICAL_THEOREM` | later signature benchmark | imported Enterprise pairing/sign rule |
| Mixed Hodge structures | Deligne's functorial mixed Hodge structures extend pure Hodge theory beyond smooth projective objects | complex algebraic varieties in the stated theory | `CLASSICAL_THEOREM / PRIOR ART` | example of a genuine change of realization/filtration apparatus | weights/filtrations as Enterprise primitives without derivation |
| Algebraic cycles / Chow groups | cycles modulo rational equivalence form Chow groups; cycle class maps connect them to cohomology | algebraic varieties with usual hypotheses | `CLASSICAL_THEOREM / PRIOR ART` | state the eventual algebraic landing space | preselect algebraic cycles matching a target class |
| Motives | Grothendieck-style motivic framework organizes cohomology theories and algebraic cycles; major standard conjectures remain open | category/conjecture dependent | `CLASSICAL_PRIOR_ART_METHOD + OPEN COMPONENTS` | conceptual comparison of realizations | motivic realization or full faithfulness as an Enterprise premise |
| Tropical homology | `H_{p,q}` for smooth tropical varieties; in realizable degeneration settings dimensions recover Hodge numbers of a general complex member | smooth tropical variety with stated degeneration/realizability conditions | `CLASSICAL_PRIOR_ART_METHOD / THEOREM IN STATED DOMAIN` | positive control for non-coordinate realization | tropical output renamed Enterprise |
| Combinatorial Hodge theory | Adiprasito–Huh–Katz prove Hard Lefschetz and Hodge–Riemann relations for the matroid Chow ring | arbitrary matroid, associated Chow ring | `CLASSICAL_PRIOR_ART_METHOD / THEOREM` | show that “Hodge-like” structures can occur combinatorially | treat matroid theorem as Hodge conjecture or Enterprise theorem |
| Non-Archimedean / tropicalization realization | analytification/tropicalization/skeleta yield valuation/polyhedral realizations; Payne shows analytification as inverse limit of tropicalizations | non-Archimedean valued field / stated embeddings | `CLASSICAL_PRIOR_ART_METHOD / THEOREM` | comparator for genuine realization change and functoriality | import valuation/tropical data as Enterprise-native without a new construction theorem |

## Primary / authoritative sources used

1. Pierre Deligne, *The Hodge Conjecture*, official Clay Mathematics Institute problem description:  
   `https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf`
2. Clay Mathematics Institute, current Hodge Conjecture status page:  
   `https://www.claymath.org/millennium/hodge-conjecture/`
3. Pierre Deligne, *Théorie de Hodge II*, Publ. Math. IHÉS 40 (1971):  
   `https://www.numdam.org/item/?id=PMIHES_1971__40__5_0`
4. Ilia Itenberg, Ludmil Katzarkov, Grigory Mikhalkin, Ilia Zharkov, *Tropical Homology*:  
   `https://arxiv.org/abs/1604.01838`
5. Karim Adiprasito, June Huh, Eric Katz, *Hodge theory for combinatorial geometries*, Annals of Mathematics 188 (2018):  
   `https://annals.math.princeton.edu/2018/188-2/p01`
6. Sam Payne, *Analytification is the limit of all tropicalizations*:  
   `https://arxiv.org/abs/0805.1916`
7. Walter Gubler, Joseph Rabinoff, Annette Werner, *Skeletons and tropicalizations*:  
   `https://arxiv.org/abs/1404.7044`

## H0 interpretation

Prior art establishes an important discriminator: a realization can be genuinely different without proving the Hodge conjecture. Conversely, attaching a new coordinate chart, a label, a refinement, or a generic relation/path compiler does not become Hodge-relevant merely because its vocabulary is new. H0 therefore credits only Enterprise-specific structure that survives presentation and automorphism audit and has a theorem-relevant non-factorizing observable.
