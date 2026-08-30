# RS-GEO6-MAHLER-DUAL-SUPPORT-PRODUCT — Research Return

Researcher-ID: `EM-G6MAH-91C2AF`
Claim: `chatgpt-g6mah-20260830-1119-91c2af`
Publication: `TP2-910A2E65E9C380AA438F`
Branch: `research/geo6-mahler-dual-support-product-em-g6mah-91c2af`
Task hard target: `P000_DISCRETE_DUAL_SUPPORT_PRODUCT_DEFINED_AND_EXTREMAL_STRUCTURE_CLASSIFIED_OR_DUALITY_NO_GO`

## Terminal disposition

`SUCCESS / BARE_P000_CANONICAL_DUALITY_NO_GO + CONDITIONAL_SELF_DUAL_INCIDENCE_MODEL_EXACTLY_CLASSIFIED`

The task closes at a sharp boundary rather than by importing classical polarity.

The strongest exact conclusion is:

> A relation-only common-support dual exists canonically as a **typed Galois pair** after a support relation is declared, but bare P000 does not canonically provide the extra self-dual support identification needed to turn that typed pair into a single endoduality on Cell objects. If one nevertheless demands a single common-support operator `D` satisfying `D^2 = id` on **every** subset of a finite self-dual carrier, then `D` is forced to be Boolean complement composed with an involutive relabeling. Consequently its cardinality product is `|A||D(A)| = k(n-k)`, which is a Boolean-complement law and not a geometry-sensitive Mahler analogue.

A natural native-relation candidate based on symmetric closed adjacency does not escape this boundary: raw double dual is closure rather than identity. Restricting to closed objects restores concept-level involution, but exact six-point models with comparable symmetry have incompatible product spectra. Therefore no nontrivial Mahler-style product bound is forced by bare incidence/P000 data alone.

This is an **exact duality obstruction**, not a claim that no useful conditional duality can ever be added to Enterprise Math.

---

## 1. Scope and typing

P000 is assumed unchanged:

- six native spatial dimensions plus one time dimension;
- discrete Cell space;
- rotation is primary;
- current carrier/readout structure is not native identity;
- classical Euclidean `R^6`, inner products, convex bodies, polar bodies, and volume are external comparison structures only.

No Euclidean metric, scalar product, convex hull, volume, or classical polar was used in the proof or checker.

The current FCC/carrier `S4` information is used only as a possible finite permutation-regression action. Nothing below promotes carrier `S4` to the full native P000 rotation group.

### Tool-reuse resolution

The project toolbox already records Galois/residuation machinery as pre-existing/P008-owned and finite symmetry/equivariance as reusable machinery (`T7_FINITE_SYMMETRY_EQUIVARIANCE`). Therefore this task does **not** introduce a new generic Galois, closure, or symmetry tool family.

Reuse resolution:

- Galois/adjunction layer: `REUSE_APPLIED / P008-owned standard mechanism`;
- finite symmetry covariance: `REUSE_APPLIED / T7`;
- new task-local mathematics: classification of when common-support duality can be an all-subset involution, the exact Boolean collapse, six-point product regressions, and the refinement obstruction.

Formal Concept Analysis is prior art for the standard extent/intent Galois closure architecture. The task-specific result is therefore not presented as a novelty claim about Galois connections.

---

## 2. Native finite support context

Let

`K = (C,S,I)`

be a finite declared support context, where:

- `C` is a finite Cell-object window or finite object family;
- `S` is a separately tagged finite support/test family;
- `I(c,s)` is a declared native relation-derived admissibility/support predicate.

For `A subseteq C`, define the support functional

`Sigma_A(s)=1  iff  I(c,s) for every c in A`.

The support dual is

`A^perp = {s in S : Sigma_A(s)=1}`.

For `B subseteq S`, define the transpose dual

`B^perp = {c in C : I(c,s) for every s in B}`.

These definitions are purely finite and relational.

### Theorem 2.1 — typed Galois laws

For every finite context `K`:

1. `A subseteq B  =>  B^perp subseteq A^perp`;
2. `A subseteq A^(perp perp)`;
3. `A^(perp perp perp)=A^perp`;
4. `cl_C(A)=A^(perp perp)` is extensive and idempotent;
5. the analogous statements hold on the support side.

#### Proof

Antitonicity follows because a support common to every element of the larger set is common to every element of the smaller set.

For extensivity, if `c in A` and `s in A^perp`, then by definition `I(c,s)`, hence `c in A^(perp perp)`.

Applying antitonicity to `A subseteq A^(perp perp)` gives

`A^(perp perp perp) subseteq A^perp`.

Applying extensivity on the support side to `A^perp` gives the reverse containment. Thus equality holds. Idempotence follows immediately.

So the canonical relation-only object is a **closure duality**, not automatically an involution on raw objects.

---

## 3. Rotation/equivariance law

Suppose a declared transformation `g` acts bijectively on both `C` and `S` and preserves incidence:

`I(c,s) iff I(g c, g s)`.

Then

`(gA)^perp = g(A^perp)`.

This is exact and requires no metric. Therefore a support dual can be rotation-covariant whenever its defining relation is rotation-covariant.

The obstruction below is **not** failure of equivariance. It is failure of canonical self-duality/involution and failure of a relation-independent product law.

---

## 4. First obstruction: typed duality is not an endoduality

The Galois pair naturally switches sorts:

`P(C)  <->  P(S)`.

To obtain one operator on the same native object class, one needs at least an additional identification

`j : C -> S`

or an equivalent self-dual pairing structure.

Bare P000 fixes dimension/Cell/rotation typing but does not supply a canonical `Cell object = support object` identification. The current FCC line-family readout also cannot be silently used as native identity.

Therefore:

`P000 + DECLARED INCIDENCE  =>  TYPED GALOIS PAIR`

but not

`P000  =>  CANONICAL CELL ENDODUALITY`.

This is already a minimal structural obstruction.

The next theorem shows that even after adding a self-dual identification, requiring lossless duality everywhere is too strong: it collapses the geometry to Boolean complement.

---

## 5. Boolean anti-involution collapse theorem

Let `C` be a finite set with `|C|=n`. After a declared self-dual identification of support and object sorts, write a single common-support map

`D(A) = {y in C : R(x,y) for every x in A}`.

Assume the hard losslessness condition

`D(D(A)) = A`

for **every** `A subseteq C`.

### Theorem 5.1 — complete classification

There exists a unique permutation `pi` of `C` such that

`D(A) = C \ pi(A)`

for every `A`, and `pi^2=id`.

Equivalently, the relation has the exact form

`R(x,y)  iff  y != pi(x)`

for an involutive permutation `pi`.

Conversely every such involutive `pi` defines an all-subset involutive common-support dual.

### Proof

`D` is antitone by construction. The identity `D^2=id` makes `D` bijective, hence an order anti-automorphism of the Boolean lattice `P(C)`.

An atom `{x}` must therefore map to a coatom. Thus there is a unique element `pi(x)` with

`D({x}) = C \ {pi(x)}`.

Distinct atoms have distinct images, so `pi` is a permutation.

Because common support turns unions into intersections,

`D(A) = intersection_{x in A} D({x})`

`     = intersection_{x in A} (C \ {pi(x)})`

`     = C \ pi(A)`.

Since permutation commutes with set complement,

`D^2(A) = pi^2(A)`.

Hence `D^2=id` for all subsets iff `pi^2=id`.

The row relation is exactly `y != pi(x)`. If `pi` is involutive this relation is symmetric, so the two typed Galois maps indeed identify with the same endodual operator.

QED.

### Consequence

A common-support duality that is lossless on **all** subsets contains no deeper geometry than:

`BOOLEAN COMPLEMENT + INVOLUTIVE RELABELING`.

So the strongest possible raw involutivity requirement destroys the very incidence sensitivity that a Mahler-like native duality was supposed to measure.

---

## 6. Exact product law in the only all-subset involutive class

Use the minimal cardinality complexity pair

`p(A)=|A|`,

`s(A)=|D(A)|`,

and stress-test product

`M(A)=p(A)s(A)`.

For the classified anti-involution family,

`|D(A)|=n-|A|`.

Thus if `k=|A|`,

`M(A)=k(n-k)`.

For nonempty proper subsets:

`n-1 <= M(A) <= floor(n^2/4)`.

The lower extremizers are exactly `k=1` or `k=n-1`; balanced cardinalities maximize the product.

### Six-point regression

For `n=6`:

- minimum `M=5` at sizes `1,5`;
- `M=8` at sizes `2,4`;
- maximum `M=9` at size `3`.

Exact subset counts:

- product `5`: 12 subsets;
- product `8`: 30 subsets;
- product `9`: 20 subsets.

This model is equivariant under every permutation, so it is certainly compatible with any declared finite rotation action on the six labels, including the current carrier-level `S4` permutation action when used only as a carrier regression.

But this is **not accepted as the sought native Mahler theorem**, because the product is forced solely by Boolean complement. It is exactly the kind of definition-driven success the task criteria require us to reject as a final native theory.

---

## 7. Natural adjacency support loses information

A more geometry-sensitive candidate uses a symmetric native relation such as closed adjacency:

`R(x,y) iff (x=y) or Adj(x,y)`.

Then `D(A)` is the common closed neighborhood of `A`.

This relation is symmetric and is automatically equivariant under adjacency-preserving rotations/automorphisms.

However raw involutivity fails generically.

### Exact six-cycle witness

On a six-cycle with closed neighborhoods, label vertices modulo 6. For

`A={0,2}`,

one gets

`D(A)={1}`

but

`D^2(A)={0,1,2}`.

So double dual strictly closes the object and loses the distinction between `{0,2}` and `{0,1,2}`.

The exact checker finds 20 Galois-closed subsets in this six-point model. For nontrivial closed subsets, the simple product `|A||D(A)|` takes only values

`{3,4}`.

Thus a natural relation-derived support gives concept-level duality, not raw-object polarity.

---

## 8. Product non-universality on closed objects

One might repair the information-loss problem by restricting admissible objects to Galois-closed sets:

`A = D^2(A)`.

On these objects, `D` is an involution because `D^3=D`.

This is mathematically clean, but it does not produce a canonical Mahler product.

Three exact six-point contexts already separate the possibilities:

### Model A — complement incidence

`R(i,j) iff i != j`.

Every subset is closed. Nontrivial product spectrum:

`{5,8,9}`.

### Model B — diagonal incidence

`R(i,j) iff i=j`.

Closed subsets are exactly:

- empty set;
- six singletons;
- full set.

Every nonempty proper closed object has product

`1`.

This model is also equivariant under the full permutation group.

### Model C — closed-neighborhood six-cycle

20 closed subsets. Nontrivial product spectrum:

`{3,4}`.

The three contexts have the same underlying cardinality and can have substantial finite symmetry, yet their dual-closed object classes and product spectra are incompatible.

Therefore no nontrivial relation-independent lower product law follows from finite incidence + symmetry alone. At most one obtains tautological cardinality statements after imposing nonemptiness.

In particular, a dimension/window-size-growing lower bound fails immediately across the diagonal family, where the nontrivial closed product remains `1` for arbitrary `n`.

---

## 9. Refinement obstruction

P000 treats finite precision/refinement as endogenous, so a viable native duality must also specify how duality behaves when a finite support universe is refined.

Even the perfect complement model fails the naive inclusion test.

Let `i:C_n -> C_m` be the obvious inclusion with `m>n`, and let complement duality be used at both resolutions. Then

`D_m(i(A)) = C_m \ i(A)`

while

`i(D_n(A)) = i(C_n \ A)`.

Exactly,

`D_m(i(A)) = i(D_n(A)) union (C_m \ i(C_n))`.

The refinement defect is therefore the full set of newly introduced support labels and has size

`m-n`.

Hence absolute duality does not commute with refinement without an additional rule deciding how new supports interact with old objects.

This is an exact obstruction, not a numerical artifact.

---

## 10. Minimal missing structure for a genuine native theory

The research isolates the missing data in increasing strength.

### M1 — declared native support relation

A specific `I(c,s)` must be selected from native relations. P000 alone does not choose which relation is “support”.

### M2 — self-dual identification or typed-duality semantics

If the desired dual must return the same object type, an equivariant identification between Cell objects and support objects is required. It may not be silently borrowed from a carrier readout.

### M3 — nondegenerate admissible object class

Raw subsets are too broad: natural incidence gives closure rather than involution. Restricting to closed concepts is canonical relative to `I`, but then the object class itself depends on `I`.

### M4 — a geometry-sensitive complexity functional

Plain cardinality product either becomes Boolean-complement arithmetic or varies arbitrarily with the incidence context. A future theory needs a complexity functional that is native, operation-safe, rotation-invariant, and not merely renamed Euclidean volume.

### M5 — refinement transport

A rule must specify how supports are transported, created, or forgotten across finite resolutions. Without it, even exact finite dualities need not define a coherent multi-resolution geometry.

The earliest obstruction is M1/M2. M4/M5 block the stronger Mahler-style extremal theory even after a conditional duality is supplied.

---

## 11. What is positively preserved

The no-go does leave a useful positive architecture:

1. **Typed support duality is legitimate and native-friendly.** It needs only finite relation data.
2. **Rotation covariance is automatic** for relation-preserving actions.
3. **Galois-closed Cell objects** form the correct lossless domain for a chosen support relation.
4. A genuinely new Enterprise duality problem should therefore not ask for arbitrary raw-set polarity. It should ask whether a particular native relation produces a distinguished closed-object family plus a nontrivial refinement-stable complexity pairing.

This narrows the next mathematical question substantially without manufacturing a successor task.

---

## 12. Exact checker

Checker:

`research_checks/GEO6_MAHLER_DUAL_SUPPORT_PRODUCT_CHECK_20260830.py`

Local exact run in the research session:

```text
PASS
typed_contexts=530
typed_assertions=30630
raw_involution_counts={1: 1, 2: 2, 3: 4, 4: 10}
classification_checks=34
n6_complement_product_spectrum={5: 12, 8: 30, 9: 20}
n6_eq_closed_count=8
n6_cycle_closed_count=20
n6_cycle_nontrivial_product_values=[3, 4]
refinement_assertions=528
```

The raw-involution counts `1,2,4,10` for `n=1..4` exactly equal the counts of involutive permutations, providing exhaustive finite regression for Theorem 5.1 in addition to the general proof.

No floating-point arithmetic appears in the checker.

---

## 13. Prior-art / novelty boundary

Standard Galois connections, formal concepts, extent/intent closure, and Boolean-lattice anti-automorphisms are classical mathematics and are not claimed as Enterprise inventions.

The classical Mahler template uses a convex body and a polar defined through a bilinear/inner-product inequality together with volume product; that machinery remains external and is deliberately not imported as native P000 structure.

Task-local contribution is the exact **structural-transfer classification**:

- the typed-vs-endodual distinction under P000;
- the all-subset involution collapse to complement + involutive relabeling;
- the exact product consequence showing why that positive model is too Boolean to count as the desired geometry;
- the adjacency-closure witness;
- the incompatible six-point closed-product spectra;
- the explicit refinement defect;
- the resulting minimal-data boundary for any future P000 dual-support theory.

---

## 14. Hard-target decision

Hard target:

`P000_DISCRETE_DUAL_SUPPORT_PRODUCT_DEFINED_AND_EXTREMAL_STRUCTURE_CLASSIFIED_OR_DUALITY_NO_GO`

Disposition:

`SATISFIED_BY_EXACT_DUALITY_NO_GO_AT_BARE_P000_STRENGTH`.

More precisely:

`BARE_P000_CANONICAL_CELL_POLARITY = NOT_DERIVED`;

`DECLARED_INCIDENCE_TYPED_GALOIS_DUAL = EXACT`;

`ALL_SUBSET_ENDODUAL_INVOLUTION = COMPLEMENT_AFTER_INVOLUTIVE_RELABELING_ONLY`;

`BOOLEAN_PRODUCT_EXTREMAL_LAW = EXACT_BUT_DEFINITION_DRIVEN`;

`NATURAL_ADJACENCY_RAW_INVOLUTION = FALSE_IN_EXACT_6_POINT_MODEL`;

`CLOSED_OBJECT_PRODUCT = RELATION_DEPENDENT / NO_NONTRIVIAL_UNIVERSAL_MAHLER_BOUND_FROM_CURRENT_PRIMITIVES`;

`REFINEMENT_COHERENCE = REQUIRES_EXTRA_TRANSPORT_DATA`.

No Working Truth, Foundation, or canonical P000 promotion is requested by this return. Driver review must decide whether to accept the no-go boundary and whether any narrower successor is worth publishing.

## References / provenance

- Taskbook: `research_tasks/GEO6_MAHLER_DUAL_SUPPORT_PRODUCT_20260830.md`.
- P000: `GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/P000_REALITY_FOUNDATION.json`.
- Current foundation: `GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/00_CURRENT_FOUNDATION.md` and `definitions/00_CURRENT_NATIVE_FOUNDATION.md`.
- External geometry intake: `GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md`.
- Standard FCA comparison: formal concepts are extent/intent fixed points of a Galois connection; used here only as prior-art typing.
- Contemporary Mahler-status comparison: symmetric Mahler remains open in dimensions `n>=4`; only its primal/dual extremal-product architecture is used as an external template.
