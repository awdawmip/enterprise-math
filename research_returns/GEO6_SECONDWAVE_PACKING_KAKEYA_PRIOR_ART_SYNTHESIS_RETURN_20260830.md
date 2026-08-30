# GEO6 Second-Wave Packing/Kakeya Prior-Art Synthesis — Research Return

Task: `RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS`  
Publication: `TP2-3B14908767F248123B62`  
Researcher-ID: `EM-G6PA2-4A7D2C`  
Claim: `chatgpt-g6pa2-20260830-1648-4a7d2c`  
Execution branch: `research/geo6-secondwave-packing-kakeya-prior-art-em-g6pa2-4a7d2c`  
Execution record: `ER-4A7D2C8F91B3E0675D24`  
Planned Result: `RR-4A7D2CE39B70F54168A2`  
Date: `2026-08-30`

## Terminal verdict

`AUDIT_COMPLETE`

Hard target:

`GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACTLY_CLASSIFIED`

The accepted second-wave Packing and Kakeya claims were decomposed into 18 exact audit rows and compared against graph theory, spectral graph theory, amenable/Følner counting, graph products and Cayley spectra, hypergraph incidence acyclicity, vector matroids, and finite-field/discrete Kakeya literature.

Classification counts:

- `EXACT_DUPLICATE`: **3**
- `STRICT_ANTECEDENT`: **11**
- `ADJACENT_METHOD`: **1**
- `NO_MATERIAL_MATCH`: **3**

The finite combinatorial content is therefore overwhelmingly classical once the required ambient structures are supplied. The surviving research value is concentrated in four P000 semantic selectors:

1. `NONOVERLAP_SELECTOR`
2. `TRANSLATION_FOLNER_SELECTOR`
3. `PHYSICAL_REFINEMENT_SELECTOR`
4. `MIXED_DIRECTION_SELECTOR`

No currently accepted P000/Full-Cell datum was found that resolves any of these four selectors. This audit grants no Working Truth, Foundation, or successor authority.

**Novelty guard:** `NO_MATERIAL_MATCH` is not a novelty certificate. It records only that the searched external theory does not choose or derive the P000-specific semantic datum under equivalent hypotheses.

## 1. Accepted inputs and scope firewall

The Packing lane is read only through accepted Gen2 Result `RR-71FABB059247512DF390`. Its protected boundary remains:

- finite packing becomes independent-set occupancy only **after** a conflict relation is declared;
- the even six-axis torus has exact declared-model optimum `1/2`;
- periodic/Følner density needs an explicit translation action and period structure;
- the finite quotient/refinement law does not itself supply physical scale semantics;
- bare current P000 supplies neither a canonical non-overlap relation nor a canonical translation/invariant-mean structure.

The Kakeya lane is read only through accepted Gen2 Result `RR-9D6C3A7E42B1F805C264`. Its protected boundary remains:

- six linearly independent typed directions force a forest incidence structure;
- overlap defect is at most `5`;
- `K_6(r)=6r-5` for the declared six-axis problem;
- equality requires connected overlap incidence, not six-way concurrency;
- dependent directions can create an incidence cycle and beat the independent-axis formula;
- carrier `S4` is not identified with the full native P000 direction/rotation family.

No external Euclidean `R^6`, Lebesgue measure, Hausdorff dimension, or classical continuum Kakeya theorem is imported as a P000 proof primitive.

## 2. Exact claim/source classification matrix

| Claim | Lane | Class | Accepted claim / obstruction | Strongest antecedent |
|---|---|---|---|---|
| `PCK-01` | PACKING | `EXACT_DUPLICATE` | Once a finite Cell conflict relation C is declared, admissible packings are exactly independent sets and the optimum occupancy is alpha(G)/\|V\|. | EXT-GRAPH-INDEPENDENCE |
| `PCK-02` | PACKING | `STRICT_ANTECEDENT` | Finite packing optimum and occupancy are invariant under every declared Cell bijection preserving the conflict relation. | EXT-GRAPH-INDEPENDENCE |
| `PCK-03` | PACKING | `STRICT_ANTECEDENT` | For a periodic lift from a finite quotient of Z^6, every Følner sequence yields density equal to the occupied quotient fraction. | EXT-FOLNER-COSSETS |
| `PCK-04` | PACKING | `STRICT_ANTECEDENT` | For a fixed periodic fundamental-domain tiling, finite-window density error is confined to incomplete boundary tiles. | EXT-FOLNER-COSSETS |
| `PCK-05` | PACKING | `EXACT_DUPLICATE` | The declared torus conflict graph T_n on (Z/nZ)^6 with neighbors differing by ±e_i is the sixfold Cartesian product of C_n and a finite abelian Cayley graph; for even n it is bipartite by parity. | EXT-CARTESIAN-BIPARTITE, EXT-CAYLEY-CHARACTERS |
| `PCK-06` | PACKING | `STRICT_ANTECEDENT` | For even n, alpha(T_n)=n^6/2, witnessed by one parity class and certified above by the E1 perfect matching. | EXT-CARTESIAN-BIPARTITE, EXT-KONIG |
| `PCK-07` | PACKING | `EXACT_DUPLICATE` | The spectral upper certificate alpha(T_n)/n^6<=1/2 follows from degree 12, least eigenvalue -12, and Hoffman's ratio bound. | EXT-HOFFMAN, EXT-CAYLEY-CHARACTERS |
| `PCK-08` | PACKING | `STRICT_ANTECEDENT` | Translations and the realized carrier-S4 coordinate permutations preserve the declared conflict relation and therefore preserve density. | EXT-GRAPH-INDEPENDENCE |
| `PCK-09` | PACKING | `STRICT_ANTECEDENT` | For q:T_kn->T_n given by coordinate reduction mod n, the full inverse image of an independent set is independent and constant fiber size k^6 preserves occupancy exactly. | EXT-GRAPH-INDEPENDENCE |
| `PCK-10` | PACKING | `NO_MATERIAL_MATCH` | The finite quotient/refinement law does not by itself make n->kn the physical P000 scale refinement. | INT-PACK-GEN2 |
| `PCK-11` | PACKING | `NO_MATERIAL_MATCH` | Bare current P000 does not canonically provide the non-overlap/conflict relation or the translation/Følner structure required for a global packing density. | INT-PACK-GEN2 |
| `KAK-01` | KAKEYA | `STRICT_ANTECEDENT` | For six affine Cell paths with linearly independent direction vectors, the bipartite incidence graph between paths and multiply-covered Cells is a forest. | EXT-MATROID-CIRCUIT, EXT-BERGE-ACYCLIC |
| `KAK-02` | KAKEYA | `STRICT_ANTECEDENT` | For six independent paths the overlap defect D=sum_x(m_x-1) is at most 5. | EXT-CYCLOMATIC, EXT-BERGE-ACYCLIC |
| `KAK-03` | KAKEYA | `STRICT_ANTECEDENT` | For r>=2 in the declared sufficiently large finite window, the exact six-axis support optimum is K_6(r)=6r-5. | EXT-CYCLOMATIC, EXT-BERGE-ACYCLIC |
| `KAK-04` | KAKEYA | `STRICT_ANTECEDENT` | Equality K_6(r)=6r-5 requires connected overlap incidence; six-way concurrency is not required, and the nonconcurrent r=2 chain is a valid equality witness. | EXT-CYCLOMATIC, EXT-BERGE-ACYCLIC |
| `KAK-05` | KAKEYA | `STRICT_ANTECEDENT` | Linear independence is essential: the dependent direction set {e1,e2,e1+e2} admits an overlap cycle and an r=2 support-3 countermodel, beating the independent-direction forest value 4. | EXT-MATROID-CIRCUIT |
| `KAK-06` | KAKEYA | `ADJACENT_METHOD` | Classical finite/discrete Kakeya theory is relevant only as an adjacent comparison, not as the antecedent of K_6(r)=6r-5. | EXT-DVIR-KAKEYA, EXT-BALL-BLOKHUIS-DOMENZAIN |
| `KAK-07` | KAKEYA | `NO_MATERIAL_MATCH` | The full native P000 direction family beyond carrier S4, including mixed/refining direction circuits across refinement levels, remains unresolved. | INT-KAK-GEN2 |

Machine-readable matrix:

`research_artifacts/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_SYNTHESIS/claim_source_matrix.json`

## 3. Packing lane — what is classical

### 3.1 Independent-set reduction and symmetry

Once a finite symmetric irreflexive conflict relation `C` is declared, the optimization problem is literally the graph independence problem. Thus `delta=alpha(G)/|V|` is an `EXACT_DUPLICATE`, and invariance under Cell bijections preserving `C` is only graph-isomorphism/automorphism invariance.

This kills further research effort on the finite optimization statement itself. What graph theory cannot do is choose the native P000 conflict predicate.

### 3.2 Periodic/Følner density

Johnson–McClendon, Lemma 2.7, proves a stronger external statement than the accepted periodic-density theorem: for every Følner sequence in `Z^d` and every finite-index subgroup, every coset has asymptotic proportion equal to the reciprocal index. Summing occupied cosets immediately yields the accepted quotient-density formula.

Therefore the density limit is `STRICT_ANTECEDENT`. Re-proving it inside P000 is not high-value work. The missing datum is the native translation/period/Følner structure itself.

### 3.3 Even six-axis torus and the value 1/2

The graph `T_n=(Z/nZ)^6` with generators `±e_i` is a standard finite abelian Cayley graph and the sixfold Cartesian product of `C_n`. For even `n`, parity gives its standard bipartition.

The exact optimum `alpha(T_n)=n^6/2` follows from:

1. one parity class of size `n^6/2`; and
2. the explicit `E1` perfect matching, which allows at most one occupied endpoint per pair.

The independent spectral certificate is also classical. Character diagonalization gives

`lambda(k)=2 sum_{j=1}^6 cos(2 pi k_j/n)`,

so for even `n` the degree is `d=12` and the least eigenvalue is `tau=-12`. Hoffman's ratio bound gives

`alpha/N <= -tau/(d-tau)=12/24=1/2`.

Accordingly, the declared-model number `1/2` and both upper certificates are frozen continuation kills.

### 3.4 Quotient/refinement

For the declared reduction `q:T_{kn}->T_n`, independence pullback and density preservation are generic consequences of edge preservation plus constant fiber size `k^6`. The mathematics is classical once the map is supplied.

The nonclassical residue is semantic only: current accepted P000 does not identify this combinatorial cover with the physical scale-refinement map.

## 4. Kakeya lane — exact antecedent reduction

### 4.1 Forest theorem as dependence obstruction

Take the bipartite incidence graph whose left vertices are the six paths and whose right vertices are multiply-covered Cells. An alternating incidence cycle produces nonzero scalar increments along the participating path directions; telescoping around the closed cycle yields a nontrivial linear dependence among those directions. Hence linearly independent direction vectors forbid such a cycle.

Equivalently, the path hypergraph is Berge-acyclic when its incidence graph is a forest. This places the accepted forest statement under standard incidence-acyclicity and vector-matroid circuit theory rather than under a new Kakeya mechanism.

### 4.2 Defect `<=5` and `K_6(r)=6r-5`

Let `s` be the number of shared-Cell nodes, let

`E=sum_x m_x`

be the incidence-edge count, and let `c` be the number of connected components of the incidence forest. The forest identity gives

`E=(6+s)-c`.

Therefore the overlap defect is

`D=sum_x(m_x-1)=E-s=6-c <= 5`.

For six length-`r` paths,

`|union_i L_i| = 6r-D >= 6r-5`.

A connected tree of five singleton overlaps realizes equality, so

`K_6(r)=6r-5`.

Moreover, equality is exactly `c=1`, not concurrency. Any connected tree shape can realize the same defect, explaining the mandatory nonconcurrent equality witness. These are `STRICT_ANTECEDENT` consequences of ordinary forest/cycle-rank counting.

### 4.3 Why the dependent triangle matters

The set `{e1,e2,e1+e2}` contains the elementary vector-matroid circuit

`e1 + e2 - (e1+e2) = 0`.

That minimal dependence permits an incidence cycle. The frozen support-3 example is therefore a concrete specialization of standard circuit behavior, and it blocks any extension of the independent-axis formula to arbitrary mixed directions.

### 4.4 Relation to finite Kakeya theory

Dvir's finite-field Kakeya theorem and the Ball–Blokhuis–Domenzain finite Kakeya program are classified only as `ADJACENT_METHOD`. They study line sets over finite fields/direction grids and global `q^n`-scale lower bounds. The accepted GEO6 problem instead fixes exactly six typed finite lattice directions, finite path length `r`, and an incidence-forest objective.

These theories are close enough to prohibit broad “new Kakeya theorem” language, but their hypotheses do not resolve which mixed/refining directions are native P000 directions.

## 5. Continuation kill list

The following should not receive further GEO6 budget under the same frozen hypotheses:

- `PCK-01` — finite packing as independent-set optimization (`EXACT_DUPLICATE`).
- `PCK-02` — graph-automorphism invariance (`STRICT_ANTECEDENT`).
- `PCK-03` — finite-index coset/Følner quotient density (`STRICT_ANTECEDENT`).
- `PCK-04` — periodic boundary-tile error localization (`STRICT_ANTECEDENT`).
- `PCK-05` — even-torus Cayley/product/parity structure (`EXACT_DUPLICATE`).
- `PCK-06` — parity + perfect-matching proof of `1/2` (`STRICT_ANTECEDENT`).
- `PCK-07` — Hoffman spectral certificate for `1/2` (`EXACT_DUPLICATE`).
- `PCK-08` — declared automorphism density invariance (`STRICT_ANTECEDENT`).
- `PCK-09` — uniform-fiber graph-cover density preservation (`STRICT_ANTECEDENT`).
- `KAK-01` — independent-direction incidence forest (`STRICT_ANTECEDENT`).
- `KAK-02` — defect `<=5` (`STRICT_ANTECEDENT`).
- `KAK-03` — `K_6(r)=6r-5` under six independent typed directions (`STRICT_ANTECEDENT`).
- `KAK-04` — connected-incidence equality criterion and nonconcurrent tree witnesses (`STRICT_ANTECEDENT`).
- `KAK-05` — vector-circuit explanation of the dependent-direction countermodel (`STRICT_ANTECEDENT`).

The finite-field Kakeya lane is **not** on the kill list as an exact antecedent; it remains an adjacent comparison. It still blocks novelty language for generic discrete-Kakeya claims.

## 6. Surviving selector map

### NONOVERLAP_SELECTOR
- Status: `SURVIVES`
- External mathematics: Once `C` is declared, graph theory completely handles finite occupancy, automorphism invariance, matching and Hoffman certificates.
- Missing native datum: A canonically selected/derived native Cell non-overlap or exclusion relation, with equivariance and compatibility with any refinement.
- Accepted datum capable now: `FALSE`
- Current evidence: Gen2 Packing explicitly freezes `NO_CANONICAL_BARE_P000_NONOVERLAP_RELATION`. First-wave `CONTACT_SELECTOR` is also still unresolved.
- Driver action: Highest leverage, but do not publish a successor until an accepted P000/Full-Cell contact/exclusion datum is named.

### TRANSLATION_FOLNER_SELECTOR
- Status: `SURVIVES`
- External mathematics: For a declared `Z^6`/amenable translation action and finite period quotient, periodic density along every Følner sequence is classical.
- Missing native datum: A native translation action (or substitute amenable action/invariant-mean structure), plus admissible finite periods/windows.
- Accepted datum capable now: `FALSE`
- Current evidence: Gen2 Packing explicitly freezes `NO_CANONICAL_BARE_P000_TRANSLATION_OR_INVARIANT_MEAN`.
- Driver action: Do not reprove density limits; first obtain a native action datum.

### PHYSICAL_REFINEMENT_SELECTOR
- Status: `SURVIVES`
- External mathematics: Constant-fiber graph-cover pullback preserves the declared density exactly.
- Missing native datum: A theorem identifying the combinatorial `q_{kn,n}` (or another cover) with the physical P000 scale-refinement map.
- Accepted datum capable now: `FALSE`
- Current evidence: T5 precision-refinement machinery is reusable for finite covers, but the accepted Packing return explicitly denies that this alone supplies physical scale semantics.
- Driver action: Treat T5 as method reuse, not as the missing physical datum.

### MIXED_DIRECTION_SELECTOR
- Status: `SURVIVES`
- External mathematics: Given direction vectors, matroid circuit/forest theory predicts exactly when overlap cycles may occur; finite Kakeya literature supplies adjacent global-direction techniques.
- Missing native datum: A native-legal mixed/refining direction family/orbit under the actually granted P000/Full-Cell action, including transport across refinement.
- Accepted datum capable now: `FALSE`
- Current evidence: Gen2 Kakeya freezes `CARRIER_S4 != FULL_NATIVE_P000_ROTATION_GROUP` and leaves the first native mixed/refining direction circuit unresolved.
- Driver action: Do not extend `K_6` formula beyond six independent typed axes until such a direction datum is accepted.

## 7. Driver recommendation

`ACCEPTED_P000_OR_FULL_CELL_DATUM_RESOLVING_ANY_SELECTOR_NOW = NONE_CURRENTLY_IDENTIFIED`.

Therefore this audit should **not** directly publish another mathematical successor.

If a later control-plane update accepts a native datum, the highest-leverage first target is `NONOVERLAP_SELECTOR`, because it is prerequisite to every native Packing optimization and couples directly to the first-wave `CONTACT_SELECTOR`. Once a canonical exclusion relation exists, matching, Hoffman, automorphism, and finite occupancy theory are immediately reusable without new invention.

Until then:

- do not re-prove the `1/2` torus theorem;
- do not re-prove periodic quotient density;
- do not interpret the combinatorial cover as physical refinement;
- do not extend `K_6(r)=6r-5` to mixed directions;
- do not claim Kakeya novelty from the six-axis forest formula.

## 8. Tool-reuse resolution

`REUSE_APPLIED`.

The prior first-wave claim/source matrix method and task-local exact-regression pattern are reused. External graph/matroid/Følner theorems are cited as antecedents rather than repackaged into a new global toolbox family.

`NEW_GLOBAL_TOOL_FAMILY = FALSE`.

## 9. Source ledger

- `EXT-GRAPH-INDEPENDENCE` — Douglas B. West, *Introduction to Graph Theory*, 2nd ed.; standard independent-set/independence-number definitions.  
  https://faculty.math.illinois.edu/~west/igt/
- `EXT-KONIG` — Romeo Rizzi, “A short proof of König's matching theorem,” *Journal of Graph Theory* 33 (2000), 138–139.  
  https://doi.org/10.1002/(SICI)1097-0118(200003)33:3%3C138::AID-JGT2%3E3.0.CO;2-K
- `EXT-HOFFMAN` — Willem H. Haemers, “Hoffman's ratio bound,” *Linear Algebra and its Applications* 617 (2021), 215–219.  
  https://arxiv.org/abs/2102.05529
- `EXT-FOLNER-COSSETS` — Aimee S. A. Johnson and David M. McClendon, “Finite odometer factors of rank one Z^d-actions,” arXiv:2306.09477; Lemma 2.7.  
  https://arxiv.org/abs/2306.09477
- `EXT-CARTESIAN-BIPARTITE` — Sabidussi's Cartesian-product bipartiteness theorem, quoted as Lemma 1 in Kurauskas et al., *Journal of Combinatorial Optimization* 49 (2025), Article 31.  
  https://doi.org/10.1007/s10878-025-01266-7
- `EXT-CAYLEY-CHARACTERS` — classical character diagonalization of finite abelian Cayley graphs; modern statement in “Intersective sets over abelian groups,” *Designs, Codes and Cryptography* (2025/2026).  
  https://link.springer.com/article/10.1007/s10623-025-01760-3
- `EXT-BERGE-ACYCLIC` — I. van Heuven van Staereling, B. de Keijzer, G. Schäfer, “The Ground-Set-Cost Budgeted Maximum Coverage Problem,” MFCS 2016; incidence graph forest/Berge-acyclicity.  
  https://doi.org/10.4230/LIPIcs.MFCS.2016.50
- `EXT-CYCLOMATIC` — standard cycle-rank identity `ν(G)=|E|-|V|+c(G)`, explicitly stated in Si Kaddour–Tahhan Bittar, *Contributions to Discrete Mathematics* 5(1) (2010).  
  https://cdm.ucalgary.ca/article/download/61965/46670/176851
- `EXT-MATROID-CIRCUIT` — *Encyclopedia of Mathematics*, “Matroid”: vector configurations, minimal dependent circuits, graphic matroid.  
  https://encyclopediaofmath.org/wiki/Matroid
- `EXT-DVIR-KAKEYA` — Zeev Dvir, “On the size of Kakeya sets in finite fields,” *JAMS* 22 (2009), arXiv:0803.2336.  
  https://arxiv.org/abs/0803.2336
- `EXT-BALL-BLOKHUIS-DOMENZAIN` — Simeon Ball, Aart Blokhuis, Diego Domenzain, “A finite version of the Kakeya problem,” arXiv:1503.06639.  
  https://arxiv.org/abs/1503.06639
- `INT-PACK-GEN2` — accepted Gen2 Packing Result `RR-71FABB059247512DF390` and Driver review.
- `INT-KAK-GEN2` — accepted Gen2 Kakeya Result `RR-9D6C3A7E42B1F805C264` and Driver review.

External citations are used only for antecedent/hypothesis classification. Internal accepted Results remain the authority for what P000 itself currently grants.

## 10. Exact regression

The deterministic task-local checker at

`research_checks/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_SYNTHESIS_CHECK_20260830.py`

verifies:

- all 18 claim IDs are unique;
- classification counts are exactly `3 / 11 / 1 / 3`;
- every claim has an explicit hypothesis comparison and antecedent source;
- all `NO_MATERIAL_MATCH` rows carry the non-novelty guard;
- the continuation-kill set matches the classical/antecedent rows intended above;
- the surviving selector set is exactly the four task-authorized selectors;
- no selector is marked as currently resolved by an accepted datum;
- the Driver recommendation is `NONE_CURRENTLY_IDENTIFIED`;
- the forest identity gives `D=6-c<=5`, and connected incidence gives `6r-5`;
- the Hoffman substitution gives exactly `1/2`.

Terminal disposition: `AUDIT_COMPLETE`.
