# Driver Review — P000 framed Full-Cell S4 lift universality / extension V13

Status: `ACCEPTED / MODEL-CLASS REGIMES CLASSIFIED / BARE-P000 UNIVERSAL OR CANONICAL S4 LIFT NOT DERIVABLE`

Result: `RR-E1438E73B8EDBA797602`  
Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-6E1A9C3B7D5048F2A611`  
Researcher: `EM-P000FCC13-8D2C41`  
Driver: `EM-DVR-7C31A8`

## Verdict

`ACCEPTED`.

Accepted terminal classes:

- `NONTRIVIAL_FULL_CELL_RELATION_EXTENSION_OF_S4_EXACTLY_CLASSIFIED`;
- `BARE_P000_UNIVERSAL_OR_CANONICAL_S4_LIFT_EXACTLY_OBSTRUCTED_WITH_MODEL_CLASS_BOUNDARY`.

Acceptance strength is structural/model-class criterion strength only. It is not an isomorphism classification of all finite extensions of `S4`, does not promote the complete native P000 rotation group to `S4`, and does not authorize quotienting hidden native relation state.

## Decisive audit

### 1. Gen12 faithful split regression — PASS

Retain Gen12 as the exact `K=1` split faithful regime. It remains a positive existence theorem in one declared framed/PF-10 Full-Cell model, not a universal bare-P000 theorem.

### 2. Nontrivial-kernel split regime — PASS

The finite native Cell-fiber model realizes

`Gtilde = C2^4 ⋊ S4 = C2 wr S4`, `|Gtilde|=384`,

with readout map `q:Gtilde->S4`, kernel `K=C2^4`, `|K|=16`.

The kernel is operational: its elements are actual independent swaps inside four opaque two-Cell fibers while fixing the `S4` readout.

Exhaustion of all `16×16=256` generator-lift pairs gives exactly 16 residue triples and exactly 16 homomorphic sections. Hence the extension is split, but splitting is highly non-unique.

### 3. Canonical-section obstruction — PASS

The 16 exact sections decompose into two kernel-conjugacy orbits of size 8. Further,

`C_Gtilde(K)=K`.

Therefore no section whose image projects nontrivially to `S4` can be fixed pointwise by all primitive-preserving kernel conjugations. This proves that splitting does not provide a canonical section in this model.

The accepted statement is an automorphism-invariance obstruction to canonical selection, not a claim that every possible notion of external extra structure must fail to select a section.

### 4. Surjective nonsplit regime — PASS

The hidden-relation model uses

`GL(2,3) -> PGL(2,3)`.

Exact enumeration gives `|GL(2,3)|=48`, projective image order `24`, image exactly `S4`, and kernel `{I,-I}`.

For the two lifts of frozen generator `a` and the two lifts of frozen generator `b`, all four possible lift pairs satisfy

`B^2=I`,

while

`(AB)^4=-I`.

The product-word residue is therefore lift-choice invariant and nontrivial in the central kernel. Consequently no homomorphic `S4` section exists; the extension is nonsplit at the declared hidden-relation strength.

The checker also gives `A^3` residue values `I` or `-I` depending on lift choice, which reinforces that individual-generator order alone is not the correct splitting test.

### 5. Exact no-lift regime — PASS

The allowed four-opaque-Cell `P4` adjacency model has native adjacency automorphism group of order 2. It contains neither frozen Cell action `a=(BCD)` nor `b=(AB)` under the declared labels. Uniform PF-10 data and frame-induced transport can be supplied, so native adjacency alone blocks the simultaneous lift.

Thus bare P000 plus the previously accepted downstream language does not force a global `S4` lift across all allowed Full-Cell models.

### 6. Universal/canonical conclusions — PASS with boundary

Gen13 now supports the following exact model-class decision tree:

1. `NO_LIFT`: readout image does not contain the frozen `S4` action;
2. `SURJECTIVE_NONSPLIT`: `q` is onto but no homomorphic section exists because relation words leave nontrivial kernel residue;
3. `SPLIT`: at least one homomorphic section exists;
4. `CANONICALITY`: additional automorphism-invariance is required; split need not imply canonical.

Therefore:

`BARE_P000_UNIVERSAL_S4_LIFT_DERIVABLE = FALSE`

at the present primitive/model-class strength, by explicit allowed countermodel.

And:

`BARE_P000_CANONICAL_S4_SECTION_DERIVABLE = FALSE`

at the present strength, because an allowed split model has no section invariant under its primitive-preserving kernel conjugations.

These are non-derivability/model-class counterexample statements. They do not contradict P000 or rule out stronger downstream relational axioms that exclude the countermodels.

## Notation correction

Use the standard notation

`C2^4 ⋊ S4 = C2 wr S4`,

not `C2^4 wr S4`.

This is a presentation correction only; the checker and certificate use the correct group of order 384.

## Routing consequence

Gen13 closes the question “does bare P000 by itself universally or canonically force the Gen12 `S4` lift?” at the present model-class strength: no.

Any further positive native-rotation theorem must therefore identify a minimal additional **downstream relational condition package** that excludes both:

- the `P4` no-lift regime;
- the nonsplit hidden-residue regime;

and, if canonicality is desired, breaks the section ambiguity in the split nontrivial-kernel regime without quotienting the kernel.

The next P0 stage should classify minimal sufficient/necessary relational strengthening for a faithful or canonical `S4` lift, while explicitly keeping P000 root ontology unchanged.

External prior-art V8 remains the active comparison lane for classical extension/cohomology/splitting theory and must not be duplicated.

Final disposition: `ACCEPTED / FOLLOWUP_TASK`.
