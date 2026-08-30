# GEO6 Mahler dual-support prior-art synthesis - Research Return

Researcher-ID: `EM-G6MAHPA-B65BDB`
Task: `RS-GEO6-MAHLER-PRIOR-ART-SYNTHESIS`
Publication: `TP2-EFB8751B437EF5B5A5BA`
Claim: `chatgpt-g6mahpa-20260830-2034-5e91c7`
Branch: `research/geo6-mahler-prior-art-synthesis-em-g6mahpa-b65bdb`
Accepted source result: `RR-596D76AA2D95C837AB26`

## Terminal disposition

`AUDIT_COMPLETE / GEO6_MAHLER_ACCEPTED_CLAIMS_PRIOR_ART_EXACTLY_CLASSIFIED`

The audit closes the accepted finite dual-support result at a sharp prior-art boundary. The generic two-sort derivation/Galois/closure layer is standard Formal Concept Analysis (FCA). Requiring an antitone common-support endomap to be an involution on every subset of a finite self-dual carrier reduces it to Boolean complement composed with a permutation; imposing `D^2=id` forces that permutation to be involutive. The resulting cardinality product `k(n-k)` is therefore definition-driven Boolean arithmetic rather than a geometry-sensitive Mahler invariant.

Classical Mahler volume product is only `ADJACENT_METHOD`: it is defined for convex bodies in `R^n` using polarity and volume, while the accepted P000 object is a finite incidence context with no native convex body, polar body, Euclidean metric, or volume.

No `NO_MATERIAL_MATCH` row is a novelty certificate.

## External sources

- S1: Bernhard Ganter and Rudolf Wille, *Formal Concept Analysis: Mathematical Foundations*, Springer, 1999. DOI `10.1007/978-3-642-59830-2`.
- S2: Alexandre Bazin and Giacomo Kahn, "Distances Between Formal Concept Analysis Structures", *Transactions on Graph Data and Knowledge* 3(2), 2025. DOI `10.4230/TGDK.3.2.2`.
- S3: Paul Halmos and Steven Givant, *Introduction to Boolean Algebras*, Springer, 2009. DOI `10.1007/978-0-387-68436-9`.
- S4: Matthieu Fradelizi, Mathieu Meyer and Artem Zvavitch, "Volume product", in *Harmonic Analysis and Convexity*, De Gruyter, 2023, pp. 163-222. DOI `10.1515/9783110775389-005`.
- S5: Richard P. Stanley, "Some Aspects of Groups Acting on Finite Posets", *Journal of Combinatorial Theory, Series A* 32 (1982), 132-161.

The machine-readable claim/source matrix is:
`research_artifacts/GEO6_MAHLER_PRIOR_ART_SYNTHESIS/claim_source_matrix.json`

## Claim classification

The ten audited rows classify as:

- `MAH-01 EXACT_DUPLICATE`: a declared finite context `(C,S,I)` gives the standard FCA derivations between `P(C)` and `P(S)`, an antitone Galois connection, `A subseteq A''`, `A'''=A'`, and double-prime closure.
- `MAH-02 EXACT_DUPLICATE`: restricting to double-prime-closed extents/intents gives the standard lossless concept-level correspondence.
- `MAH-03 STRICT_ANTECEDENT`: an antitone involution `D:P(C)->P(C)` on the whole finite Boolean lattice is complement composed with a unique atom permutation; `D^2=id` iff that permutation is involutive.
- `MAH-04 STRICT_ANTECEDENT`: for `|C|=n`, `|A|=k`, the Boolean collapse gives `|D(A)|=n-k` and `M(A)=k(n-k)`, with minimum `n-1` on nonempty proper subsets and maximum `floor(n^2/4)`.
- `MAH-05 NO_MATERIAL_MATCH`: the exact six-point complement/diagonal/C6 spectrum table `{5,8,9}`, `{1}`, `{3,4}` is retained as a task-local finite benchmark, without novelty inference.
- `MAH-06 NO_MATERIAL_MATCH`: the exact no-go against a relation-independent growing lower bound for this chosen cardinality product is retained at the internal countermodel scope only.
- `MAH-07 STRICT_ANTECEDENT`: under direct inclusion `i:C_n->C_m`, complement satisfies `D_m(i(A))=i(D_n(A)) union (C_m\i(C_n))`; the defect has size `m-n`. This is elementary set bookkeeping.
- `MAH-08 NO_MATERIAL_MATCH`: bare P000 does not select a canonical support relation. FCA assumes the incidence relation as input.
- `MAH-09 NO_MATERIAL_MATCH`: bare P000 does not canonically identify Cell and support sorts. FCA itself is two-sorted.
- `MAH-10 ADJACENT_METHOD`: classical Mahler volume product is a convex-geometric comparator, not an identified antecedent of the finite P000 cardinality product.

Counts:
`2 EXACT_DUPLICATE / 3 STRICT_ANTECEDENT / 1 ADJACENT_METHOD / 4 NO_MATERIAL_MATCH`.

## Boolean collapse derivation

Let `c(A)=C\A`. If `D` is antitone and `D^2=id`, then `D` is an order anti-automorphism of `P(C)`. Hence `F=c o D` is an order automorphism. An order automorphism of the finite powerset preserves atoms, so there is a unique permutation `pi` of `C` determined by `F({x})={pi(x)}`. Since every subset is the union of its atoms, `F(A)=pi(A)`. Therefore

`D(A)=C\pi(A)`.

Complement commutes with every permutation, so `D^2=pi^2`; thus `D^2=id` iff `pi^2=id`.

This proves that the all-subset involutive class has no extra geometry beyond Boolean complement plus involutive relabeling. The common-support relation formula is a task-specific packaging of this standard finite-Boolean reduction.

## Residue map

Exactly the Driver-declared four selectors survive:

1. `SUPPORT_RELATION_SELECTOR = SURVIVES`: FCA assumes a context relation; accepted P000 data do not canonically choose one.
2. `SELF_DUAL_IDENTIFICATION_SELECTOR = SURVIVES`: standard derivation switches object/support sorts; no accepted P000 datum supplies a canonical same-sort identification.
3. `COMPLEXITY_FUNCTIONAL_SELECTOR = SURVIVES`: cardinality is definition-driven/context-dependent, while classical volume is not typed into P000.
4. `REFINEMENT_TRANSPORT_SELECTOR = SURVIVES`: naive complement under inclusion has the exact new-label defect, and no accepted native transport rule removes it.

No fifth selector is introduced.

## Kill decisions

- `KILL_GENERIC_GALOIS_CLOSURE_CONTINUATION`
- `KILL_BOOLEAN_ANTIINVOLUTION_AS_NOVEL_GEOMETRY`
- `KILL_K_N_MINUS_K_PRODUCT_AS_MAHLER_THEOREM`
- `KILL_CLASSICAL_MAHLER_IMPORT_WITHOUT_EXPLICIT_TYPE_MAP`

Any stronger GEO6 Mahler/native-duality successor requires a new accepted P000 datum that resolves at least one surviving selector. This researcher lane does not publish such a successor.

## Hard-target disposition

Hard target:
`GEO6_MAHLER_ACCEPTED_CLAIMS_PRIOR_ART_EXACTLY_CLASSIFIED`

Disposition:
`SATISFIED / AUDIT_COMPLETE`

Next action: Driver review this return and the claim/source matrix. If accepted, freeze the FCA rows as exact prior art, the Boolean and `k(n-k)` rows as strict antecedents/elementary consequences, the finite spectra only as bounded benchmark evidence, and all four selector residues as unresolved.

Researcher-ID: `EM-G6MAHPA-B65BDB`
