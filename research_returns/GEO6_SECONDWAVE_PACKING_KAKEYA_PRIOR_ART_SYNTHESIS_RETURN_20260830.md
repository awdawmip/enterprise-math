# GEO6 Second-Wave Packing/Kakeya Prior-Art Synthesis — Research Return

Task: `RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS`  
Publication: `TP2-3B14908767F248123B62`  
Researcher-ID: `EM-G6PA2-4A7D2C`  
Claim: `chatgpt-g6pa2-20260830-1648-4a7d2c`  
Execution: `ER-4A7D2C8F91B3E0675D24`  
Branch: `research/geo6-secondwave-packing-kakeya-prior-art-em-g6pa2-4a7d2c`  
Date: `2026-08-30`

## Terminal verdict

`AUDIT_COMPLETE`

Hard target:

`GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACTLY_CLASSIFIED`

The two accepted Gen2 Results were decomposed into 18 claim-level rows and audited against graph independence/matching/spectral theory, finite-index Følner equidistribution, Cayley/product graphs, Berge incidence acyclicity, vector matroids, and finite/discrete Kakeya literature.

Classification:

- `EXACT_DUPLICATE = 3`
- `STRICT_ANTECEDENT = 11`
- `ADJACENT_METHOD = 1`
- `NO_MATERIAL_MATCH = 3`

Full source-backed row matrix:

`research_artifacts/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_SYNTHESIS/claim_source_matrix.json`

`NO_MATERIAL_MATCH` is not a novelty certificate.

## Packing classification

1. Once a symmetric irreflexive Cell conflict relation `C` is declared, admissible packing is exactly graph independence and `delta=alpha(G)/|V|`. This is `EXACT_DUPLICATE`.
2. Conflict-preserving Cell bijections preserve packing optimum by ordinary graph isomorphism/automorphism invariance: `STRICT_ANTECEDENT`.
3. For a periodic lift from a finite quotient of `Z^6`, density along every Følner sequence equals the occupied quotient fraction. Johnson–McClendon Lemma 2.7 gives the stronger coset statement for every finite-index subgroup of `Z^d`; summing occupied cosets yields the accepted theorem: `STRICT_ANTECEDENT`.
4. Boundary-tile error localization is ordinary periodic/Følner boundary counting: `STRICT_ANTECEDENT`.
5. The declared graph `T_n=(Z/nZ)^6` with generators `±e_i` is a finite abelian Cayley graph / sixfold Cartesian product of `C_n`; for even `n` parity gives the standard bipartition: `EXACT_DUPLICATE`.
6. `alpha(T_n)=n^6/2` follows from the parity side plus the explicit `E1` perfect matching: `STRICT_ANTECEDENT`.
7. Character diagonalization gives `lambda(k)=2 sum_j cos(2 pi k_j/n)`. For even `n`, `d=12` and `tau=-12`; Hoffman's ratio bound gives `alpha/N<=12/24=1/2`: `EXACT_DUPLICATE`.
8. Translation and realized carrier-`S4` invariance are ordinary graph-automorphism consequences: `STRICT_ANTECEDENT`.
9. For `q:T_{kn}->T_n`, independent-set pullback plus constant fiber size `k^6` preserves density: `STRICT_ANTECEDENT`.
10. What survives is semantic: the combinatorial cover does not select the physical P000 scale map, and bare P000 still lacks a canonical non-overlap relation and translation/Følner structure. These are the three Packing-side `NO_MATERIAL_MATCH` residues feeding `PHYSICAL_REFINEMENT_SELECTOR`, `NONOVERLAP_SELECTOR`, and `TRANSLATION_FOLNER_SELECTOR`.

## Kakeya classification

For the accepted six independent typed directions, let the bipartite incidence graph have six path vertices and one right vertex for each multiply-covered Cell.

An alternating incidence cycle telescopes to a nontrivial scalar relation among participating direction vectors. Linear independence forbids it. Thus the incidence graph is a forest; this is standard vector-dependence/Berge-acyclic structure (`STRICT_ANTECEDENT`).

Let `s` be the number of shared-Cell vertices, `E=sum_x m_x` the incidence-edge count, and `c` the number of forest components. Then

`E=(6+s)-c`

and the overlap defect is

`D=sum_x(m_x-1)=E-s=6-c<=5`.

Hence for six length-`r` paths,

`|union_i L_i|=6r-D>=6r-5`.

A connected tree of five singleton overlaps realizes equality, so

`K_6(r)=6r-5`.

Equality is exactly the connected-incidence case `c=1`; concurrency is unnecessary, explaining the nonconcurrent chain witness. These are all `STRICT_ANTECEDENT` consequences of ordinary forest/cycle-rank counting.

The dependent set `{e1,e2,e1+e2}` contains the vector-matroid circuit

`e1+e2-(e1+e2)=0`.

That dependence permits the frozen incidence cycle/support-3 countermodel, so the independent-axis formula must not be generalized to arbitrary mixed directions.

Dvir's finite-field Kakeya theorem and Ball–Blokhuis–Domenzain are `ADJACENT_METHOD`, not exact antecedents: they quantify over finite-field direction universes and global `q^n`-scale sets, while GEO6 fixes six typed finite lattice paths and an incidence-forest objective.

The Kakeya semantic residue is therefore `MIXED_DIRECTION_SELECTOR`: current accepted P000 does not yet supply a native-legal mixed/refining direction family under the actually granted rotation/refinement semantics.

## Continuation kill list

Freeze further work that merely re-derives, under the same hypotheses:

- finite packing as independent sets;
- graph-automorphism invariance;
- finite-index Følner coset/periodic density;
- periodic boundary counting;
- even-torus parity/product/Cayley structure;
- the parity/perfect-matching proof of `1/2`;
- the Hoffman proof of `1/2`;
- constant-fiber cover density preservation;
- independent-direction incidence forest;
- defect `<=5`;
- `K_6(r)=6r-5`;
- connected-incidence equality/nonconcurrent tree shapes;
- the vector-circuit explanation of the dependent-direction countermodel.

Finite-field Kakeya is not an exact kill antecedent, but it blocks broad novelty language.

## Surviving selector map

### `NONOVERLAP_SELECTOR`
External graph theory solves the finite optimization after `C` exists. Missing datum: canonical native Cell non-overlap/exclusion, equivariant and refinement-compatible.  
Accepted resolver now: `NONE`.

### `TRANSLATION_FOLNER_SELECTOR`
External amenable/Følner theory solves periodic density after the action/period is declared. Missing datum: native translation or substitute amenable action/invariant mean and admissible periods/windows.  
Accepted resolver now: `NONE`.

### `PHYSICAL_REFINEMENT_SELECTOR`
External graph-cover counting solves density preservation after a cover is declared. T5 precision refinement is reusable method only. Missing datum: theorem identifying a combinatorial cover with physical P000 scale refinement.  
Accepted resolver now: `NONE`.

### `MIXED_DIRECTION_SELECTOR`
External matroid theory analyzes any supplied direction family. Missing datum: native-legal mixed/refining direction orbit and transport across refinement under actual P000/Full-Cell operations.  
Accepted resolver now: `NONE`.

## Driver recommendation

`ACCEPTED_P000_OR_FULL_CELL_DATUM_RESOLVING_ANY_SELECTOR_NOW = NONE_CURRENTLY_IDENTIFIED`.

Do not publish a mathematical successor from this audit. A future successor must first name one accepted P000/Full-Cell datum capable of resolving one surviving selector.

If such a datum later appears, the highest-leverage selector is `NONOVERLAP_SELECTOR`, because it is prerequisite to every native Packing optimization and couples to the unresolved first-wave `CONTACT_SELECTOR`.

## Tool reuse

`REUSE_APPLIED`.

The first-wave claim/source matrix method and task-local exact regression pattern were reused. No new global toolbox family was introduced.

## Principal external antecedents

- Willem H. Haemers, “Hoffman's ratio bound,” *Linear Algebra and its Applications* 617 (2021), 215–219; arXiv:2102.05529.
- Aimee S. A. Johnson and David M. McClendon, “Finite odometer factors of rank one Z^d-actions,” arXiv:2306.09477, Lemma 2.7.
- Romeo Rizzi, “A short proof of König's matching theorem,” *Journal of Graph Theory* 33 (2000), 138–139.
- Standard finite abelian Cayley-character diagonalization and Cartesian-product bipartiteness.
- Standard Berge-acyclic incidence-forest and cycle-rank identities.
- Standard vector-matroid circuit theory.
- Zeev Dvir, “On the size of Kakeya sets in finite fields,” *JAMS* 22 (2009), arXiv:0803.2336.
- Simeon Ball, Aart Blokhuis, Diego Domenzain, “A finite version of the Kakeya problem,” arXiv:1503.06639.

## Exact regression

`research_checks/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_SYNTHESIS_CHECK_20260830.py`

verifies the 18 unique rows, exact class counts `3/11/1/3`, the four-authorized-selector set, zero accepted selector resolvers, the continuation-kill rows, `D=6-c<=5`, connected `6r-5`, and the Hoffman value `1/2`.

Terminal disposition: `AUDIT_COMPLETE`.
