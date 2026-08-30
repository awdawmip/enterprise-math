# GEO6 Mahler dual-support prior-art and duplication synthesis — Research Return

Researcher-ID: `EM-G6MAHPA-B65BDB`  
Task: `RS-GEO6-MAHLER-PRIOR-ART-SYNTHESIS`  
Publication: `TP2-EFB8751B437EF5B5A5BA`  
Claim: `chatgpt-g6mahpa-20260830-2034-5e91c7`  
Branch: `research/geo6-mahler-prior-art-synthesis-em-g6mahpa-b65bdb`  
Accepted Enterprise source: `RR-596D76AA2D95C837AB26`

## Terminal disposition

`AUDIT_COMPLETE / GEO6_MAHLER_ACCEPTED_CLAIMS_PRIOR_ART_EXACTLY_CLASSIFIED`

The finite dual-support result is useful, but most of its algebraic core is not a new Mahler-type theory. The audit separates four layers:

1. the two-sort derivation/Galois/closure layer is standard Formal Concept Analysis;
2. the all-subset anti-involution collapse is a direct specialization of finite Boolean-lattice structure;
3. the cardinality product `k(n-k)` is elementary complement arithmetic, not a geometry-sensitive Mahler product;
4. the unresolved Enterprise content is semantic typing: choosing a native support relation, choosing or rejecting a same-sort self-dual identification, choosing a geometry-sensitive complexity functional, and specifying refinement transport.

Classical Mahler volume product is only an `ADJACENT_METHOD` comparator at this stage. Its objects are convex bodies in `R^n`, together with polarity and volume. The accepted finite P000 result supplies none of those types, so no classical Mahler inequality, polar-body theorem, or extremizer may be imported.

No novelty is inferred from any `NO_MATERIAL_MATCH` row.

## 1. Frozen scope

This audit consumes only the Driver-accepted result `RR-596D76AA2D95C837AB26` as the Enterprise mathematical source. The accepted statements audited are:

- typed common-support derivations and double-dual closure;
- lossless duality on closed objects;
- all-subset anti-involution classification;
- the induced cardinality product `k(n-k)`;
- the exact finite spectra/countermodels showing relation dependence;
- the direct-inclusion refinement defect;
- the remaining P000 typing obstructions.

The task does not identify a Euclidean polar body, convex volume, or classical Mahler object with any native P000 object.

## 2. External source set

### S1 — Formal Concept Analysis foundations

Bernhard Ganter and Rudolf Wille, *Formal Concept Analysis: Mathematical Foundations*, Springer, 1999.  
DOI: `10.1007/978-3-642-59830-2`  
URL: https://doi.org/10.1007/978-3-642-59830-2

This is the standard mathematical foundation for formal contexts, concept lattices and the object/attribute derivation architecture.

### S2 — explicit modern FCA formulation

Alexandre Bazin and Giacomo Kahn, “Distances Between Formal Concept Analysis Structures,” *Transactions on Graph Data and Knowledge* 3(2), 2025.  
DOI: `10.4230/TGDK.3.2.2`  
URL: https://doi.org/10.4230/TGDK.3.2.2

Its preliminaries explicitly define a formal context `(O,A,R)`, the two derivation operators between powersets, state that they form a Galois connection, and state that double derivation is a closure operator. Formal concepts are closed extent/intent pairs.

### S3 — finite Boolean-algebra background

Paul Halmos and Steven Givant, *Introduction to Boolean Algebras*, Springer, 2009.  
DOI: `10.1007/978-0-387-68436-9`  
URL: https://doi.org/10.1007/978-0-387-68436-9

The finite-Boolean-algebra/atom representation gives the standard setting in which an order automorphism of a finite powerset is determined by its action on atoms. Composing an order anti-automorphism with Boolean complement therefore reduces it to an atom permutation.

### S4 — classical Mahler comparator

Matthieu Fradelizi, Mathieu Meyer and Artem Zvavitch, “Volume product,” in *Harmonic Analysis and Convexity*, De Gruyter, 2023, pp. 163–222.  
DOI: `10.1515/9783110775389-005`  
URL: https://doi.org/10.1515/9783110775389-005

The chapter surveys the classical volume product for convex bodies in `R^n` and the Mahler lower-bound problem. This is a type comparator only.

### S5 — finite-poset symmetry background

Richard P. Stanley, “Some Aspects of Groups Acting on Finite Posets,” *Journal of Combinatorial Theory, Series A* 32 (1982), 132–161.  
URL: https://math.mit.edu/~rstan/pubs/pubfiles/50.pdf

This supplies standard finite-poset/Boolean-algebra symmetry background. It does not create a P000 support relation or a Cell/support type identification.

## 3. Claim classification

| ID | Accepted Enterprise claim | Classification | Audit disposition |
|---|---|---|---|
| MAH-01 | A declared finite support context gives antitone two-sort derivations, `A subseteq A''`, `A'''=A'`, and double-dual closure. | `EXACT_DUPLICATE` | Standard FCA derivation/Galois closure. |
| MAH-02 | Raw duality is two-sort; double-prime closed objects give the lossless concept-level domain. | `EXACT_DUPLICATE` | Standard extent/intent closure architecture. |
| MAH-03 | An antitone all-subset involution on a finite self-dual powerset has `D(A)=C\pi(A)` with `pi^2=id`. | `STRICT_ANTECEDENT` | Direct finite-Boolean specialization; proof below. |
| MAH-04 | The induced cardinality product is `k(n-k)` with the elementary finite extrema. | `STRICT_ANTECEDENT` | Immediate complement arithmetic, not geometry. |
| MAH-05 | The exact six-point complement/diagonal/C6 contexts have spectra `{5,8,9}`, `{1}`, `{3,4}`. | `NO_MATERIAL_MATCH` | Exact task-local benchmark table; no novelty inference. |
| MAH-06 | Incidence plus symmetry alone does not force a nontrivial relation-independent lower bound for this cardinality product. | `NO_MATERIAL_MATCH` | Exact internal countermodel boundary; no novelty inference. |
| MAH-07 | Direct-inclusion complement refinement has defect `C_m\i(C_n)` of size `m-n`. | `STRICT_ANTECEDENT` | Elementary set/complement identity. |
| MAH-08 | Bare P000 does not canonically choose the support relation `I(c,s)`. | `NO_MATERIAL_MATCH` | P000-specific typing residue; FCA assumes the relation as input. |
| MAH-09 | Bare P000 does not canonically identify Cell and support sorts to obtain a same-sort endoduality. | `NO_MATERIAL_MATCH` | P000-specific typing residue; FCA remains two-sort. |
| MAH-10 | The finite cardinality product is not an identified instance of classical Mahler volume product. | `ADJACENT_METHOD` | Classical objects/hypotheses are not typed into P000. |

Counts: `2 EXACT_DUPLICATE / 3 STRICT_ANTECEDENT / 1 ADJACENT_METHOD / 4 NO_MATERIAL_MATCH`.

The machine-readable matrix is frozen at:

`research_artifacts/GEO6_MAHLER_PRIOR_ART_SYNTHESIS/claim_source_matrix.json`

## 4. Formal hypothesis comparisons

### 4.1 FCA layer: exact duplication

For a formal context `(O,A,R)`, FCA defines the two derivations

`P(O) -> P(A)` and `P(A) -> P(O)`

by common incidence. Under the literal map

- `O = C`,
- `A = S`,
- `R = I`,
- FCA prime `(')` = Enterprise common-support perpendicular,

the accepted Enterprise formulas are the same construction. The closure facts therefore do not define a new Enterprise tool family or new geometry.

This also fixes a typing point that matters later: the standard construction naturally changes sorts. It does not, by itself, supply an identification `C = S`.

### 4.2 Boolean anti-involution: strict antecedent

Assume the accepted all-subset hypothesis:

- `C` is finite;
- `D:P(C)->P(C)` is antitone;
- `D^2=id`.

Then `D` is an order anti-automorphism of the finite Boolean lattice `P(C)`. Let `c(A)=C\A` be Boolean complement. The composite

`F = c o D`

is an order automorphism of `P(C)`.

An order automorphism preserves the atoms, which in `P(C)` are exactly the one-element subsets. Hence there is a unique permutation `pi` of `C` with

`F({x})={pi(x)}`.

Because every subset is the join/union of its atoms, the automorphism is determined on every subset:

`F(A)=pi(A)`.

Therefore

`D(A)=c(F(A))=C\pi(A)`.

Every permutation commutes with complement, so

`D^2 = pi^2`.

Thus the accepted `D^2=id` condition is equivalent to `pi^2=id`.

The Enterprise theorem additionally packages this Boolean fact through a common-support relation and writes the row relation `R(x,y) iff y != pi(x)`. That packaging is task-specific, but the mathematical collapse is forced by standard finite Boolean structure. This is why the correct label is `STRICT_ANTECEDENT`, not a novelty claim.

### 4.3 The `k(n-k)` product: strict antecedent

For `|C|=n` and `|A|=k`,

`|D(A)| = |C\pi(A)| = n-k`.

Hence

`M(A)=|A||D(A)|=k(n-k)`.

The minimum over nonempty proper subsets is `n-1`; the maximum is `floor(n^2/4)`. These are elementary consequences of the Boolean collapse. They carry no additional P000 geometry.

### 4.4 Classical Mahler: adjacent, not antecedent

The classical volume product reviewed by Fradelizi–Meyer–Zvavitch is a convex-geometric invariant. Its hypotheses include a convex body in `R^n`, polarity/dual body structure and volume. The accepted P000 finite relation model has none of those native types.

Accordingly there is no valid implication

`classical Mahler theorem => accepted finite P000 product theorem`

and no valid reverse identification. The shared word “product” and duality intuition are methodological adjacency only.

## 5. Relation dependence and the finite countermodel layer

The accepted result’s three six-point contexts remain useful as *negative controls*:

- complement incidence gives nontrivial closed-object spectrum `{5,8,9}`;
- diagonal incidence keeps the nonempty proper closed product at `1`;
- closed-neighborhood `C6` gives `{3,4}`.

FCA explains why changing a formal context can change its closure system/concept lattice, but the exact three-context spectrum table is an Enterprise benchmark. The audit did not find a source that should replace that exact table, so it is retained as `NO_MATERIAL_MATCH`, explicitly without any novelty inference.

The diagonal family is enough for the accepted narrow no-go: with the chosen cardinality product, finite incidence and symmetry do not by themselves force a growing nontrivial universal lower bound. This should be preserved as a task-local countermodel boundary, not promoted into a new general theorem about FCA.

## 6. Refinement

For a direct inclusion `i:C_n -> C_m`, `m>n`, and complement duality at each scale,

`D_m(i(A)) = C_m \ i(A)`.

Partition the right side into old and new labels:

`C_m \ i(A) = i(C_n\A) union (C_m\i(C_n))`.

Therefore

`D_m(i(A)) = i(D_n(A)) union (C_m\i(C_n))`.

The defect is exactly the new-label set and has cardinality `m-n`.

The identity itself is elementary and therefore not a new refinement theorem. What remains open is the *semantic selector*: what native P000 transport law should relate support objects across resolutions so that an intended duality is coherent.

## 7. Surviving P000 residue map

Exactly the four taskbook selectors survive; none is deleted by the accepted P000 data frozen for this audit.

### `SUPPORT_RELATION_SELECTOR` — SURVIVES

FCA starts from a relation. It does not select a privileged P000-native support relation from unrelated primitives. The generic Galois tool is therefore classical, while the support selector remains genuinely unresolved at the project-typing layer.

### `SELF_DUAL_IDENTIFICATION_SELECTOR` — SURVIVES

Standard FCA is object/attribute two-sort. A same-sort involution requires extra self-dual structure or a deliberate choice to remain typed. No accepted P000 datum in the frozen scope supplies the canonical identification.

### `COMPLEXITY_FUNCTIONAL_SELECTOR` — SURVIVES

Plain cardinality either collapses to `k(n-k)` in the Boolean case or varies with the incidence context. Classical Mahler volume is not natively typed. A geometry-sensitive P000 functional is still missing.

### `REFINEMENT_TRANSPORT_SELECTOR` — SURVIVES

Naive complement under direct inclusion has an exact new-label defect. No accepted P000 support-transport rule resolves it.

No fifth selector is introduced. The admissible closed-object question is subordinate to the chosen support relation and duality semantics and does not expand the Driver-declared residue list.

## 8. Kill decisions

The audit closes the following continuations:

- `KILL_GENERIC_GALOIS_CLOSURE_CONTINUATION`
- `KILL_BOOLEAN_ANTIINVOLUTION_AS_NOVEL_GEOMETRY`
- `KILL_K_N_MINUS_K_PRODUCT_AS_MAHLER_THEOREM`
- `KILL_CLASSICAL_MAHLER_IMPORT_WITHOUT_EXPLICIT_TYPE_MAP`

Any future GEO6 dual-support work must start from at least one genuinely new accepted P000 datum that resolves a surviving selector. This researcher lane does not publish that successor.

## 9. Hard-target disposition

Hard target:

`GEO6_MAHLER_ACCEPTED_CLAIMS_PRIOR_ART_EXACTLY_CLASSIFIED`

Disposition:

`SATISFIED / AUDIT_COMPLETE`

The research value is a cleaned novelty surface, not a claim of a new Mahler inequality. The classical layers are removed from the frontier, the exact finite countermodels are preserved as bounded evidence, and the unresolved project-specific content is reduced to the four declared selectors.

## 10. Next control-plane action

Driver review this return and the machine-readable claim matrix. If accepted:

- freeze the two FCA rows as exact prior art;
- freeze the Boolean anti-involution and `k(n-k)` rows as strict antecedents/elementary consequences;
- retain the finite countermodel rows only at their exact declared scope;
- retain all four selector residues;
- do not open a stronger Mahler/native-duality task from this researcher result alone.

Researcher-ID: `EM-G6MAHPA-B65BDB`
