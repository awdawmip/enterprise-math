# P000 Cross-Block Native Product / Block-System Prior-Art Audit V6 — Research Return

Status: `RESEARCH_RETURN_FROZEN / HARD_TARGET_CLOSED_AT_EXTERNAL_DUPLICATION_BOUNDARY / AWAITING_DRIVER_REVIEW`

Task: `RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT`  
Publication: `TP2-E4143818BDA70C70113B`  
Researcher-ID: `EM-P0006DPA6-E61B42`  
Claim: `chatgpt-p0006dpa6-20260829-1809-e61b42`  
Execution branch: `research/p000-6d-rotation-prior-art-v6-em-p0006dpa6-e61b42`

Hard target:

`P000_CROSS_BLOCK_NATIVE_PRODUCT_OBSTRUCTION_EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED`

## 1. Terminal verdict

Freeze the task-level verdict as:

`SUCCESS / PRODUCT_AND_BLOCK_SYSTEM_CORE_CLASSICAL / PARTIAL_MIXER_OUTSIDE_W_CLASSICAL / NAIVE_GLOBAL_b_EXTENSION_COLLAPSES_TO_S6 / PARTIAL_ACTIONS_AND_GRAPH_BUNDLES_ARE_ADJACENT_FRAMEWORKS / P000_MINIMAL_BMix_b_AND_NO_QUOTIENT_RULE_REMAIN_PROJECT_SPECIFIC`

The central result is not merely that the Gen7 obstruction resembles familiar product mathematics.

At the externally comparable level:

1. connected Cartesian products have classical prime-factor rigidity (Sabidussi–Vizing) and product automorphisms are controlled by factor automorphisms plus permutations of isomorphic factors;
2. the two equal 3-axis block envelope
   `W=(S3 x S3) semidirect C2 ~= S3 wr S2`
   is the classical stabilizer of a `3+3` equipartition of six points;
3. the desired
   `b=(E2 E4)(E3 E5)`, fixing `E1,E6`,
   is exactly a permutation outside that partition stabilizer;
4. the equal-block stabilizer `S3 wr S2` is a maximal imprimitive subgroup of `S6`;
5. therefore, because `b notin W`,
   **the naive global extension `<W,b>` is all of `S6`**.

The last point is the most useful new boundary for the active Gen8 construction. It means that if `BMix_b` is implemented merely by adjoining the desired `b` as one more total global six-axis permutation to the already generous `W`, then the extension does not stay “minimally cross-block”: it automatically grants every permutation in `S6`.

The exact finite checker independently enumerates:

- `|W|=72`;
- `b notin W`;
- `|<W,b>|=720=|S6|`;
- a block-pure axis relation is not preserved by `b`;
- `Aut(H(2,3))` has exactly `72` elements, matching the standard abstract wreath product `S3 wr S2` in its product action.

This does **not** prove that mixed-support native motion is impossible. It proves that a safe minimal extension cannot be represented simply as a larger global permutation subgroup between `W` and `S6`, because there is no such subgroup containing this `b`: maximality forces the jump to `S6`.

Accordingly, the operation-safe route is necessarily richer in typing or locality: a partial/domain-sensitive relation, inverse-semigroup/groupoid arrow, bundle-like transition, or some other native relation object whose composition laws are not identical to adjoining a total element of `S6`.

No novelty claim is made.

---

## 2. Frozen internal input and claim boundary

This audit accepts the Driver-approved Gen7 result as frozen:

- native full state is currently represented schematically as `X6=Cell_A x Cell_B`;
- native support blocks are
  `I_A={E1,E2,E3}` and `I_B={E4,E5,E6}`;
- current Cell-valued constructor/relation language is block-pure;
- carrier readout contains the mixed observation star
  `J_B={E1,E4,E5}`;
- the desired carrier-induced axis action is
  `b=(E2 E4)(E3 E5)`;
- the generous current block-system motion envelope is
  `W=(S3 x S3) semidirect C2`;
- `b notin W`;
- the current Cartesian/product adjacency diagnostic fails under the partial cross-block relabel;
- `Q6`-type witnesses already show that “six axes” alone do not imply a universal no-go.

This task does not reopen carrier signed-K4/cohomology and does not decide the P000 root ontology.

The audit question is only:

> Which parts of the Gen7 current-language obstruction are standard Cartesian-product / permutation-group / partial-symmetry mathematics, and which P000-specific typing questions remain after that reduction?

---

## 3. Cartesian product factorization and automorphism boundary

### 3.1 Unique factorization is classical

Hammack–Imrich–Klavžar's *Handbook of Product Graphs* records the Sabidussi–Vizing theorem: connected graphs have unique prime factorization under the Cartesian product, up to order and isomorphism of factors.

The same Cartesian-product chapter treats the automorphism group in terms of the prime factors. In standard form, automorphisms act factorwise and may permute isomorphic prime factors.

Classification:

`EXACT_DUPLICATE` at the ordinary Cartesian graph level.

P000 residue:

the project-specific assertion that a given `Cell_A x Cell_B` presentation is the authoritative native relation structure, including its Cell typing and payload semantics, is not supplied by that classical theorem.

### 3.2 Hamming product as a clean reference model

For the Hamming graph `H(d,q)`, the full automorphism group is the wreath product

`S_q wr S_d`.

Thus for

`H(2,3)=K3 square K3`

the full automorphism group has order

`|S3 wr S2| = 6^2 * 2 = 72`.

The checker independently brute-forces all `9!` vertex permutations of `H(2,3)` and finds exactly `72` graph automorphisms.

This Hamming action is a product action on nine states. It should not be confused with the six-point imprimitive action of `W` on the six axis labels; the important external antecedent is the same standard wreath-product structure arising from interchangeable factors.

---

## 4. The `3+3` block-system envelope is classical

Let

`Omega={E1,E2,E3,E4,E5,E6}`

with equipartition

`P={I_A,I_B}`.

The setwise stabilizer of this partition is exactly

`Stab_S6(P) ~= S3 wr S2
             ~= (S3 x S3) semidirect C2`.

This is precisely the Gen7 generous envelope `W`.

Dixon–Mortimer's standard symmetric-group subgroup classification identifies stabilizers of partitions into equal blocks with imprimitive wreath products. Fumagalli–Garonzi restate the same exact fact for the imprimitive maximal subgroups of `S_n`.

Classification:

`EXACT_DUPLICATE`.

The order `72` is not a P000-specific discovery; the task-specific contribution is only the exact identification of the frozen native block labels with this standard partition stabilizer.

---

## 5. Why the target partial mixer is outside `W`

The target is

`b=(E2 E4)(E3 E5)`

with `E1,E6` fixed.

Apply it to the A-block:

`b({E1,E2,E3}) = {E1,E4,E5} = J_B`.

But every element of the partition stabilizer `W` sends the whole A-block either to `I_A` or to `I_B`.

Since `J_B` is neither, `b notin W`.

Classification:

`EXACT_DUPLICATE` as a partition-stabilizer membership fact.

The checker verifies this by exact enumeration of all `72` elements.

---

## 6. Product adjacency / block relation diagnostic

At the abstract product level, a Cartesian edge changes one factor coordinate while the other factor is fixed. Product automorphisms preserve the corresponding factor/layer structure up to permitted permutations of whole isomorphic factors.

At the six axis-type level, take the most generous block-pure relation consisting of all unordered pairs lying wholly inside `I_A` or wholly inside `I_B`. Under `b`, for example,

`{E1,E2} -> {E1,E4}`.

The target pair is cross-block and is absent from the original block-pure relation.

The checker verifies the full finite relation set is not invariant under `b`.

Classification:

`PARTIAL_ANTECEDENT`.

Why not `EXACT_DUPLICATE` for the whole P000 claim? Because classical Cartesian graph theory supplies the product/layer preservation theorem, but the project's exact Cell adjacency, relation typing, payload and legal restriction rules are additional native semantics.

---

## 7. Closure of block-pure generators

There are two levels.

### Total transformations

For total six-axis permutations, the statement is immediate group theory:

if every generator preserves the equipartition `P`, their group closure remains inside

`Stab_S6(P)=W`.

Composition and inverse cannot manufacture a permutation outside the subgroup generated by the declared maps.

### Partial transformations

Lawson's inverse-semigroup framework treats partial symmetries as structure-preserving partial bijections. Restriction of an existing block-preserving total map can produce smaller-domain partial maps, but this does not canonically create a new cross-block image rule absent from the supplied maps.

Thus the generic mathematical form of the Gen7 statement is standard:

`restriction/partialization != automatic invention of a new arrow`.

Classification:

`PARTIAL_ANTECEDENT`.

The stronger P000 statement that *all legal Cell-valued relation terms* carry a specific block-purity support invariant is a task-language typing theorem, not a theorem supplied by inverse-semigroup literature.

---

## 8. Partial actions / inverse semigroups / groupoids do not give a free escape

Exel's standard definition makes the point particularly clean.

A partial action includes, for each group element, explicit domains and an isomorphism/bijection between them. Composition is only defined on the compatible domain.

Therefore partiality is not an operator that takes a missing total map and automatically manufactures the desired local map. To obtain a cross-block partial `R~_b`, one still has to specify or derive:

- a source domain;
- a target domain;
- a partial bijection/isomorphism;
- compatibility of compositions.

Inverse semigroups similarly provide a language for supplied partial symmetries.

Hence:

`PARTIAL/GROUPOID FORMALISM CAN REPRESENT BMix_b`

does not imply

`CURRENT BLOCK-PURE DATA DERIVE BMix_b`.

Classification:

`PARTIAL_ANTECEDENT`.

This also prevents an overclaim in the other direction: partial-action theory certainly *can* accommodate mixed-support arrows if such domains/maps are supplied. Gen7 only showed those arrows are absent from the current frozen relation language.

---

## 9. Graph bundles as an adjacent construction family

Imrich–Pisanski–Žerovnik explicitly describe graph bundles as generalizations of graph products and covering graphs.

This is relevant because a bundle-like model can carry transition data between fibers rather than forcing every legal motion to be an automorphism of one globally split Cartesian product.

That gives a useful external design analogy for a future typed `BMix_b`:

- local source/target fibers or slices;
- transition maps on overlaps;
- nontrivial gluing without identifying all states by a global quotient.

But no audited graph-bundle theorem proves that the P000 `J_B` slice exists, determines the correct Cell state, or satisfies the project's payload/no-quotient rules.

Classification:

`ADJACENT_METHOD`.

---

## 10. Strongest audit result: the naive global extension collapses to `S6`

This is the decisive external reduction.

The `3+3` partition stabilizer

`W ~= S3 wr S2`

is a maximal imprimitive subgroup of `S6`.

The target `b` lies outside `W`.

Therefore there is no proper subgroup `G` with

`W < G < S6`

and `b in G`.

Hence

`<W,b> = S6`.

The checker independently derives the same conclusion by exact BFS closure of a compact generating set:

```text
W_order=72=S3_wr_S2
target_b_in_W=False
global_extension_<W,b>_order=720=S6
```

### Consequence for Gen8

A proposal

`BMix_b := add b as a new global axis permutation`

fails the Gen8 independence/minimality intent in a precise way.

Once the whole `W` envelope remains available, that proposal automatically closes to all of `S6`. It therefore cannot simultaneously claim:

1. `b` is a total global native motion;
2. all of `W` remains globally composable;
3. arbitrary `S6` permutations are *not* thereby native motions.

At least one of those three properties must be weakened by typing/domain/relation semantics.

This is not a new group-theory theorem; it is an exact classical maximality theorem specialized to the Gen8 interface, independently checker-backed.

Classification:

`EXACT_DUPLICATE` for the mathematical group-theory implication, with a project-specific design consequence.

---

## 11. What a genuinely minimal extension must change

The audit does **not** prescribe a unique Gen8 solution, but it sharply narrows the admissible shape.

If arbitrary `S6` native rotations remain forbidden, then a successful `BMix_b` cannot be just a total element adjoined to `W`.

A viable construction must distinguish something that ordinary global permutation-group closure forgets, for example:

- typed source and target objects;
- a restricted domain;
- support/payload conditions;
- a groupoid rather than one global group of total maps;
- a bundle/transition structure;
- a relation object whose composition is defined only when typing matches.

Lawson/Exel partial-symmetry machinery and graph bundles show these are standard mathematical patterns.

Classification of the generic methods:

`ADJACENT_METHOD`.

Classification of the exact P000-minimal `BMix_b`:

`NO_MATERIAL_MATCH` after the bounded audit if stated as the full Cell/stack/handle/no-quotient construction problem.

Again:

`NO_MATERIAL_MATCH != NOVELTY`.

---

## 12. P000 no-quotient / native identity boundary

Classical product decomposition identifies factor structures up to graph isomorphism. Partial-action/globalization literature studies restrictions and extensions of actions. Bundle and covering theory use projection/fiber equivalences.

None of those external frameworks decides the internal rule:

`EQUAL_CARRIER_READOUT != EQUAL_NATIVE_STATE`

or the stronger operation-safety requirement that carrier/product equivalence must not silently quotient native state.

That is a model-design/ontology guard specific to the P000 programme as presently defined.

Classification:

`NO_MATERIAL_MATCH`.

This audit grants no originality status to it.

---

## 13. Mandatory claim map

| Claim | Classification | Frozen boundary |
|---|---|---|
| Cartesian factorization / factor-controlled automorphisms | `EXACT_DUPLICATE` | Classical Sabidussi–Vizing / product-graph theory |
| `W ~= S3 wr S2`, order 72 | `EXACT_DUPLICATE` | Standard 3+3 partition stabilizer; same abstract group appears as `Aut(H(2,3))` |
| target `b` outside W | `EXACT_DUPLICATE` | Standard partition-stabilizer membership |
| product adjacency failure under partial cross-factor mixer | `PARTIAL_ANTECEDENT` | Classical factor/layer rigidity; exact P000 adjacency is project-typed |
| block-pure generator closure cannot invent mixed support | `PARTIAL_ANTECEDENT` | Group/partial-bijection closure is standard; Cell support grammar is internal |
| partial action/inverse semigroup/groupoid escape | `PARTIAL_ANTECEDENT` | Domains/maps are explicit data; partiality alone does not infer missing arrow |
| graph bundles/fibered transport | `ADJACENT_METHOD` | Standard richer framework beyond direct product |
| global `W + b` extension | `EXACT_DUPLICATE` | Maximality gives `<W,b>=S6`; exact checker confirms 720 |
| typed/local `BMix_b` minimal extension | `ADJACENT_METHOD` / project-specific residue | Standard tool families exist; exact P000 minimal interface unresolved |
| no-quotient native-state identity guard | `NO_MATERIAL_MATCH` | Internal ontology/operation-safety rule |

Machine-readable version:

`research_artifacts/P000_CROSS_BLOCK_NATIVE_PRODUCT_PRIOR_ART_AUDIT_V6/claim_map.json`

---

## 14. Search ledger

Search date: `2026-08-29`.

Surfaces included publisher/book/journal pages from Taylor & Francis/CRC, Springer, ScienceDirect, De Gruyter, AMS, World Scientific/author notes, and Discrete Mathematics.

Exact search queries are frozen in:

`research_artifacts/P000_CROSS_BLOCK_NATIVE_PRODUCT_PRIOR_ART_AUDIT_V6/source_ledger.json`

Load-bearing sources include:

1. Hammack–Imrich–Klavžar, *Handbook of Product Graphs*, 2nd ed.;
2. standard full automorphism group `Aut(H(d,q))=S_q wr S_d` as restated in the 2022 Discrete Applied Mathematics Hamming-graph paper;
3. Dixon–Mortimer, *Permutation Groups*;
4. Fumagalli–Garonzi's peer-reviewed statement of imprimitive maximal subgroups of `S_n`;
5. Lawson, *Inverse Semigroups: The Theory of Partial Symmetries*;
6. Exel, *Partial Dynamical Systems, Fell Bundles and Applications*;
7. Imrich–Pisanski–Žerovnik, *Recognizing Cartesian graph bundles*.

The source ledger records DOI/URL, verification note and claim role.

---

## 15. Deterministic checker

Path:

`research_checks/P000_CROSS_BLOCK_NATIVE_PRODUCT_PRIOR_ART_AUDIT_V6_CHECK_20260829.py`

It uses only the Python standard library and no network.

Exact checks:

- exhaustive construction of all `72` elements of the `3+3` block stabilizer;
- every `W` element maps an entire block to an entire block;
- target `b` maps `I_A` to mixed `J_B` and is absent from `W`;
- `b^2=id`;
- a block-pure axis relation is not invariant under `b`;
- exact closure `<W,b>` has `720` elements and equals all permutations of six labels;
- brute-force automorphism count of `H(2,3)` is exactly `72`.

Expected output:

```text
PASS
W_order=72=S3_wr_S2
target_b_in_W=False
target_b_squared=identity
block_pure_axis_relation_preserved_by_b=False
global_extension_<W,b>_order=720=S6
H(2,3)_vertices=9; edges=18; automorphisms=72
minimal_extension_guard=GLOBAL_b_ON_TOP_OF_W_COLLAPSES_TO_S6
```

---

## 16. Acceptance disposition

A. Cartesian graph/product automorphism antecedents: PASS.

B. Wreath-product/block-system antecedent: PASS.

C. Partial mixing outside block-preserving envelope: PASS.

D. Product adjacency preservation boundary: PASS at external/product level; P000-specific relation typing kept separate.

E. Relation-closure boundary: PASS with strict strength control.

F. Partial actions/inverse semigroups/groupoids: PASS; they are formalisms for explicit domains/maps, not automatic missing-arrow generators.

G. Graph bundles/fibered adjacent methods: PASS.

H. Minimal extension audit: strengthened — global `W+b` necessarily collapses to `S6`.

I. No-quotient/native identity boundary: `NO_MATERIAL_MATCH`, no novelty inference.

Deterministic checker: PASS.

Hard target: CLOSED at the requested external duplication boundary.

---

## 17. Conclusion and routing consequence

Gen7's central *product/block-system* obstruction is largely classical once stripped of P000 typing:

- Cartesian factor rigidity is classical;
- the `3+3` envelope is the standard wreath-product partition stabilizer;
- a partial block mixer is outside that stabilizer;
- partial/global/local action machinery is already standard mathematics.

The most consequential specialization is:

`W = S3 wr S2` is maximal imprimitive in `S6`,
`b notin W`,
therefore
`<W,b> = S6`.

So the active Gen8 search should **not** spend effort on a global total-permutation enlargement of the existing envelope if it wants to preserve the guard against arbitrary `S6` native rotations.

The remaining real P000 question is more sharply typed:

> Can a mixed-support `BMix_b` be derived or added as a typed/domain-sensitive native relation with legal Cell state, support, payload, inverse/composition and `J_A -> J_B` gluing, without turning the native motion system into the total global `S6` action or quotienting native state by carrier equivalence?

External mathematics supplies several frameworks for expressing such locality, but this audit found no material source that answers that exact P000 construction problem.

No Working Truth, Foundation, canonical promotion, or novelty status is granted.

Driver review required.
