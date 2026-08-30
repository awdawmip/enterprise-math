# GEO6 Second-Wave Packing/Kakeya Prior-Art Synthesis — Research Return

Task: `RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS`  
Publication: `TP2-3B14908767F248123B62`  
Researcher-ID: `EM-G6PA2-7A84C2`  
Claim: `chatgpt-g6pa2-20260830-1908-7a84c2`  
Execution record: `ER-E49169F2D8AB3BCBFB3C`  
Date: `2026-08-30`

## Terminal disposition

`AUDIT_COMPLETE`

Hard target disposition:

`GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACTLY_CLASSIFIED`

The accepted finite Packing and fixed-six-axis Kakeya mathematics is **not a remaining novelty frontier**. The audit finds that the main exact results reduce to standard conflict-graph independent sets, regular-bipartite matching, Hoffman’s ratio bound, finite-index Følner coset equidistribution, graph-homomorphism pullback, orbit-stabilizer, elementary linear independence, and the Euler identity for incidence forests.

This return does **not** infer novelty from missing exact title matches. The only surviving research content is semantic: whether bare P000/Full-Cell mathematics canonically supplies a non-overlap predicate, a translation/Følner structure, a physical refinement interpretation, or a native mixed/refining direction family. The frozen accepted inputs themselves explicitly say those selectors are unresolved.

No Working Truth, Foundation, canonical promotion, or successor theorem authority is asserted.

---

## 1. Frozen inputs and scope

The audit is bound to the accepted Generation-2 envelopes:

- Packing Result: `RR-71FABB059247512DF390`.
- Kakeya Result: `RR-9D6C3A7E42B1F805C264`.
- Packing Driver review: accepted declared-model theorem only.
- Kakeya Driver review: accepted fixed-six-axis negative boundary only.

The claim matrix is frozen separately in:

`research_artifacts/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_SYNTHESIS/claim_matrix_v1.json`

and the bibliography/search provenance in:

`research_artifacts/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_SYNTHESIS/source_manifest_v1.json`.

Classification labels are exactly:

- `EXACT_DUPLICATE`: the accepted statement is the same classical statement after renaming/isomorphism.
- `STRICT_ANTECEDENT`: a strictly more general classical theorem immediately implies the accepted statement.
- `ADJACENT_METHOD`: classical theory explains the mechanism but does not by itself certify the exact project-specific finite witness.
- `NO_MATERIAL_MATCH`: only topic/name adjacency was found; **this never implies novelty**.

---

## 2. Packing audit

### P01 — finite packing = independent set

Once a symmetric irreflexive conflict relation `C` is declared on finite Cell states `X`, a feasible non-overlapping occupancy is literally an independent set of the conflict graph. The optimum `alpha(G)/|X|` is therefore an ordinary maximum-independent-set normalization.

**Classification:** `EXACT_DUPLICATE`.

External conflict-graph formulations of set packing encode mutually incompatible objects by edges and feasible packings by independent sets (source `S01`). No P000-specific theorem survives here after `C` is supplied.

### P02/P03 — the six-axis torus and the exact `1/2`

The graph used in the accepted pressure test,

`T_n=(Z/nZ)^6`, edges `x <-> x ± e_i`, even `n>=4`,

is exactly the standard even `k`-ary `n`-cube family with alphabet size `n` and dimension `6`, equivalently a Cartesian product of six even cycles. The even case is standard bipartite network/Cayley geometry (`S02`, `S12`).

For any finite regular bipartite graph, the two color classes have equal size, and Hall’s theorem gives a perfect matching. Hence:

- one color class is an independent set of size `N/2`;
- a perfect matching forces every independent set to choose at most one endpoint from each matched pair, so `alpha<=N/2`.

Thus `alpha(T_n)=n^6/2`.

**Classification:** graph identification `EXACT_DUPLICATE`; exact optimum `STRICT_ANTECEDENT`.

The antecedent is stronger because it applies to every finite regular bipartite graph, not just this six-dimensional torus.

### P04 — Hoffman certificate

The spectral proof substitutes `d=12` and least adjacency eigenvalue `tau=-12` into the standard Hoffman ratio bound

`alpha/N <= -tau/(d-tau)`,

giving `1/2`.

**Classification:** `EXACT_DUPLICATE` (`S04`).

This remains valuable as an independent certificate, but it is not new mathematics.

### P05 — periodic/Følner density

The accepted theorem says a periodic lift from a finite-index quotient of `Z^6` has density `|I|/|Q|` along every Følner sequence.

Johnson–McClendon, Lemma 2.7 (`S05`), proves the more general statement that for every Følner sequence in `Z^d` and every finite-index subgroup `G`, every coset has limiting proportion

`1/[Z^d:G]`.

Summing the occupied cosets gives the accepted theorem immediately.

**Classification:** `STRICT_ANTECEDENT`.

Therefore the theorem becomes classical as soon as a `Z^6` translation action and finite-index periodic quotient are declared. What is not classical bookkeeping is whether P000 canonically grants that translation structure.

### P06 — finite boundary discrepancy

Both accepted boundary statements are instances of the same elementary partition argument:

- complete periodic fundamental tiles contribute their exact fixed quota;
- complete perfect-matching pairs contribute exactly one parity Cell;
- all discrepancy is confined to blocks/pairs cut by the window boundary.

**Classification:** `STRICT_ANTECEDENT` relative to standard periodic/Følner and matching decompositions (`S03`, `S05`).

Changing window shapes, shifts, thin boxes, or parity conventions does not create a new frontier.

### P07 — quotient/refinement pullback

For a graph homomorphism `phi:G->H`, the inverse image of every independent set of `H` is independent in `G` (`S06`). The accepted `q_{k,n}:T_{kn}->T_n` is such a homomorphism; the extra density identity follows only from the declared constant fiber size `k^6`.

**Classification:** `STRICT_ANTECEDENT`.

So the finite refinement theorem is standard graph homomorphism plus finite counting. The surviving issue is only whether this quotient map is the physically/native P000 scale refinement.

### P08 — translation and carrier-S4 invariance

Any graph automorphism preserves adjacency, independent sets, and `alpha`. Coordinate translations/permutations of the declared torus are ordinary automorphisms. The carrier-S4 bookkeeping is a standard group action.

**Classification:** `EXACT_DUPLICATE`.

It cannot promote carrier `S4` to the full native P000 rotation group.

---

## 3. Kakeya audit

### K01 — carrier `S4` orbit size

Once the carrier action is declared, the `24 / 4 = 6` direction-label orbit count is exactly orbit-stabilizer (`S10`).

**Classification:** `EXACT_DUPLICATE`.

### K02 — independent directions force an incidence forest

This accepted lemma is more general than the frozen six-axis statement.

Take any simple cycle in the bipartite incidence graph alternating between distinct direction paths and shared Cells. On each path, the two incident shared Cells differ by a nonzero scalar multiple of that path’s direction vector. Summing the signed displacements around the closed incidence cycle gives zero. Hence the participating direction vectors satisfy a nontrivial linear relation.

Therefore a linearly independent direction family forbids every incidence/Berge cycle.

This argument uses only:

1. the standard incidence/Berge-cycle framework (`S07`);
2. ordinary linear independence / vector-matroid dependence (`S08`).

It works for any number `p` of independent directions.

**Classification:** `STRICT_ANTECEDENT`.

The six-axis forest theorem is not a specifically Kakeya phenomenon.

### K03 — the exact defect and `K_6(r)=6r-5`

Let there be `p` path nodes. Let `q` be the number of multiply-covered Cell nodes. If their incidence graph is a forest with `c` connected components, then the ordinary forest identity (`S11`) gives

`E = (p+q)-c`.

The overlap defect is

`D = sum_x (m_x-1) = E-q = p-c`.

For equal path length `r`,

`|union| = pr-D = pr-p+c >= pr-p+1`.

Equality holds exactly when the incidence forest is connected (`c=1`).

For `p=6` this becomes

`D<=5`

and

`K_6(r)=6r-5`

whenever a connected admissible realization exists, which the frozen construction supplies.

**Classification:** `STRICT_ANTECEDENT`.

This is the central kill result of the audit: the accepted numerical formula is the `p=6` specialization of a completely general incidence-forest Euler calculation.

### K04 — non-concurrent equality chain

The frozen `r=2` chain is important only because it disproves an overstrong characterization saying equality requires six-way concurrency. In any connected incidence tree the defect is already `p-1`, so many non-isomorphic tree shapes have the same count.

External graph theory does not certify that a specific typed coordinate chain is realizable, but once the witness is written down, its cardinality is forced by the standard tree identity.

**Classification:** `ADJACENT_METHOD`.

Retain it as a regression witness, not as a theorem frontier.

### K05 — dependent direction circuit

`{e1,e2,e1+e2}` is a vector-matroid circuit: it is dependent while every proper pair is independent (`S08`). Thus dependence is exactly where the forest obstruction can fail, and a Berge/incidence cycle becomes possible (`S07`).

The external circuit theory does not itself force the project’s particular support-`3` `r=2` coordinate witness, so that witness remains a model-specific finite counterexample.

**Classification:** `ADJACENT_METHOD`.

Its role is to locate the boundary: mixed/refining native direction semantics, not fixed independent-axis counting, is the unresolved object.

### K06 — classical Kakeya is not the exact antecedent

Finite-field Kakeya (`S09`) requires a full line in **every** direction of `F_q^d` and studies a global cardinality lower bound on such all-direction sets. The frozen project problem uses six selected independent finite paths of length `r` in a declared finite carrier window.

The quantifiers, ambient algebra, direction family, and objective do not match.

**Classification:** `NO_MATERIAL_MATCH`.

So `K_6(r)=6r-5` should not be advertised as a new Kakeya theorem merely because standard Kakeya papers do not state it; the formula is already killed by the elementary incidence-forest reduction above.

---

## 4. Kill list

The following continuations should be closed as duplicate/elementary unless they introduce a genuinely new accepted P000 semantic selector.

1. Re-proving finite Cell packing as maximum independent set after declaring pairwise conflict.
2. Re-proving `delta(T_n)=1/2` for even six-axis tori by parity, matching, coloring, LP, or another equivalent bipartite argument.
3. Re-running Hoffman on the same torus spectrum.
4. Generalizing the torus from six dimensions to arbitrary dimension while retaining the same even nearest-neighbor product graph.
5. Re-proving periodic quotient density from finite-index `Z^d` coset equidistribution.
6. Varying finite windows to obtain new versions of the same boundary-tile or matching-boundary discrepancy.
7. Rebranding graph-homomorphism inverse-image preservation as a new refinement theorem.
8. Re-proving automorphism invariance under translations or coordinate permutations.
9. Replacing six independent directions by `p` independent directions and proving `K_p(r)=pr-p+1` under the same incidence-forest hypothesis.
10. Replacing the concurrent equality witness by another connected tree/chain and treating the unchanged defect `p-1` as a new theorem.
11. Producing more carrier examples of linearly dependent direction circuits without first constructing a native P000 mixed/refining direction family.
12. Importing classical finite-field Kakeya lower bounds as if they directly constrain the six-fixed-path problem.

---

## 5. Surviving P000 selector map

| Selector | What external mathematics settles | What current accepted P000/Full-Cell data still lacks | Concrete accepted datum now capable of resolving it? |
|---|---|---|---|
| `NONOVERLAP_SELECTOR` | Once a conflict predicate exists, packing is ordinary independent-set theory. | No canonical bare-P000 non-overlap/conflict relation is accepted. | `NO` |
| `TRANSLATION_FOLNER_SELECTOR` | Once a `Z^6` action and finite-index quotient exist, periodic density is standard Følner coset equidistribution. | No canonical bare-P000 translation action / invariant-mean semantics is accepted. | `NO` |
| `PHYSICAL_REFINEMENT_SELECTOR` | Finite quotient pullback and equal-fiber density preservation are standard. | No accepted theorem identifies the finite quotient `T_{kn}->T_n` with physical/native P000 scale refinement. | `NO` |
| `MIXED_DIRECTION_SELECTOR` | Independent directions are killed by the forest/Euler reduction; matroid circuits explain where cycles may appear. | No accepted full native direction family beyond carrier `S4`, and no native-legal mixed/refining direction orbit/circuit across refinement levels. | `NO` |

The selector map is deliberately narrow. It does not create additional “semantic gaps” merely because other external theories exist.

---

## 6. Driver recommendation

`NO_CURRENT_SELECTOR_HAS_SUFFICIENT_ACCEPTED_P000_OR_FULL_CELL_DATUM_FOR_A_MATHEMATICAL_SUCCESSOR`.

Therefore:

- accept this audit as closing the finite Packing and fixed-independent-axis Kakeya novelty question;
- do **not** open a successor whose payload is another graph/matching/Følner/forest calculation;
- do **not** infer novelty from the project-specific names or from a failed exact-title search;
- require a new accepted typed datum before mathematical continuation.

If a future accepted datum appears, the closest live frontier is `MIXED_DIRECTION_SELECTOR`, because the frozen dependent-direction circuit already identifies precisely where the independent-direction forest theorem breaks. But **today** there is no accepted native mixed/refining direction family on which to run that continuation.

---

## 7. Source ledger

The machine-readable source ledger is frozen in `source_manifest_v1.json`. Core sources:

- `S01` conflict graph / set packing -> independent set.
- `S02`, `S12` even `k`-ary `n`-cube / torus bipartiteness and symmetry.
- `S03` Hall theorem / regular bipartite perfect matching.
- `S04` Hoffman ratio bound.
- `S05` finite-index subgroup coset equidistribution along every `Z^d` Følner sequence.
- `S06` graph-homomorphism inverse images of independent sets.
- `S07` Berge-acyclic/incidence-forest hypergraph framework.
- `S08` vector-matroid circuits.
- `S09` finite-field Kakeya, explicitly all directions.
- `S10` orbit-stabilizer.
- `S11` finite-forest Euler identity.

## Final research verdict

`AUDIT_COMPLETE / FINITE_PACKING_AND_FIXED_INDEPENDENT_AXIS_KAKEYA_CLASSICALIZED / FOUR_P000_SEMANTIC_SELECTORS_REMAIN_UNRESOLVED / NO_SUCCESSOR_AUTHORIZED_FROM_CURRENT_DATA`
