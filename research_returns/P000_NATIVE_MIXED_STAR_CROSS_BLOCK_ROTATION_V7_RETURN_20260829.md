# P000 Native Mixed Star / Cross-Block Rotation V7 — Research Return

Researcher-ID: `EM-P000NATFCC7-7A01E3`

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`

Publication: `TP2-AA2BF67633F3F44D0D87`

Execution branch: `research/p000-native-mixed-star-cross-block-rotation-v7-em-p000natfcc7-7a01e3`

Terminal research verdict:

`EXACT_NATIVE_PRIMITIVE_OBSTRUCTION_PROVED`

Hard-target disposition:

`P000_PRIMITIVE_MIXED_STAR_AND_CROSS_BLOCK_FULL_STATE_ROTATION_EXACTLY_CONSTRUCTED_OR_OBSTRUCTED = OBSTRUCTED_IN_CURRENT_NATIVE_SIGNATURE`

The obstruction is strictly native and earlier than any carrier/cohomology issue:

> the frozen P000 native constructor language generates Cell objects only inside one of the two three-axis blocks, while every extant full-state/clone-product motion preserves the two-block partition up to whole-factor exchange. The desired carrier transposition `b` sends the pure native star `J_A={1,2,3}` to the mixed carrier star `J_B={1,4,5}` and therefore lies outside even the generous native block/whole-factor transformation envelope. Thus the carrier `b` exists exactly, but there is no term in the current native signature that lifts it to a typed full-state motion or makes its image a native Cell.

No theorem-level arithmetic consequence is claimed.

---

## 1. Scope and frozen boundary

This execution did **not** reopen signed-K4 switching, `H^1`, Schur/double-cover classification, binary octahedral alternatives, carrier word enumeration, or the old whole-factor `C2` route. Those were treated only as frozen regressions.

The search was restricted to the primitive native layer requested by Gen7:

1. what objects are actually produced by the recoverable P000 `Cell` construction;
2. what transformations can act on those objects before carrier readout;
3. whether `J_B={E_1,E_4,E_5}` can be constructed in that language;
4. whether the desired axis permutation
   `b=(E_2 E_4)(E_3 E_5)`, with `E_1,E_6` fixed, can be lifted to a native full-state transform.

The Gen5/Gen6 boundary and the earlier L1 bridge/tomography returns agree on the following recoverable native data.

Let

`B0 = {(a,b,c) in Z_{>=0}^3 : min(a,b,c)=0}`.

For every base address `r in B0`, the recoverable construction has two blockwise copies:

- block A local direction families `E_1,E_2,E_3`;
- block B local direction families `E_4,E_5,E_6`.

Accordingly the only already-established native three-axis Cell supports are

`I_A={1,2,3}` and `I_B={4,5,6}`.

The FCC/K4 observation bridge additionally has the four star triples

`J_A={1,2,3}`,
`J_B={1,4,5}`,
`J_C={2,4,6}`,
`J_D={3,5,6}`,

but prior work explicitly froze `J_B,J_C,J_D` as observation/carrier data rather than native Cell constructors.

This distinction is the decisive one below.

---

## 2. A — Primitive native state semantics

### 2.1 Cell-valued native terms

At the currently recoverable primitive level, a native Cell is obtained from one base address and one whole block. Abstractly, the already-proved constructors have the typing

`Cell_A(r) : CELL[A]`, with axis support `I_A`,

and

`Cell_B(r) : CELL[B]`, with axis support `I_B`.

Changing the nonnegative boundary-base address, stack height, payload attached inside the same construction, or the within-block local label does not turn a Cell into a mixed-block Cell. The block is a type/provenance component of the constructor, not a carrier label added afterwards.

The old six-axis full state can contain both factors, schematically

`X6 = Cell_A(r_A) x Cell_B(r_B)`,

but this is a **product of two Cell-typed factors**, not a third constructor whose codomain is a single mixed `CELL[AB]`. A mixed support can therefore be visible at whole-state level without defining a mixed native Cell slice.

### 2.2 Native transformations already available

To avoid relying on an artificially small native motion group, this return uses a deliberately **larger** envelope than the actually established native action:

`W = (S3 x S3) semidirect C2`.

Here the two `S3` factors allow arbitrary reindexing within `I_A` and `I_B`, and `C2` allows whole-factor exchange. `|W|=72`.

Any transform generated only from blockwise moves plus optional whole-factor swap must have its six-axis type action in `W`. This is a generous upper bound: proving the target outside `W` is therefore stronger than proving it outside a smaller presently implemented group.

### 2.3 Readout is not a native quotient

The K4/FCC map

`1->AB, 2->AC, 3->AD, 4->BC, 5->BD, 6->CD`

makes `J_B={1,4,5}` a valid K4 star at vertex B. This is an exact observation fact. It is **not** an inverse constructor from a carrier star to a native Cell. No quotient or readout identification is used below to change native typing.

---

## 3. B — Exact obstruction to a native `J_B` geometric slice

### Theorem 3.1 — block-purity of the current Cell constructor language

Let `T` be any Cell-valued term generated from the currently recoverable native primitives without adding a new mixed constructor. Then the axis-type support of `T` is exactly one pure block:

`support(T) in {I_A,I_B}`.

In particular,

`J_B={1,4,5}`

is not the axis support of a constructible native Cell term.

### Proof

The primitive Cell constructors have support `I_A` or `I_B` by definition of the two copied three-axis constructions. Address/stack/payload changes preserve the block typing. Within-block reindexing sends `I_A` to `I_A` and `I_B` to `I_B`. Whole-factor exchange swaps `I_A` and `I_B`. Product formation may construct a whole state containing both factors, but its result type is a product state and not `CELL[A]` or `CELL[B]`, so it is not an elimination rule producing a new Cell support. Therefore induction over the existing Cell-valued constructor syntax leaves the Cell support in `{I_A,I_B}`. Since `J_B` contains one A-axis and two B-axes, `J_B` is neither `I_A` nor `I_B`. QED.

### Consequence for adjacency / three-axis relation

The carrier readout supplies a three-edge triangle/star relation for `J_B`, but there is no native Cell object on which to evaluate the native Cell adjacency relation. Therefore assigning the FCC adjacency directly to `J_B` would be exactly the forbidden step “observation window -> native geometry”.

### Consequence for `J_A` / `J_B` overlap

At readout level,

`J_A intersect J_B = {1}`.

This is a valid incidence statement. A native gluing law, however, requires two native Cell arguments. `J_A=I_A` is native; `J_B` is not currently Cell-typed. Hence the native overlap expression is not false — it is **undefined in the frozen signature**. The checker enforces this type failure as a negative control.

The exact Gen7 obstruction category is therefore already at least

`MIXED_SLICE_RELATION_MISSING`.

---

## 4. C — Exact obstruction to the cross-block `R~_b`

The required axis action is

`b=(2 4)(3 5)`, with `1,6` fixed.

In zero-based tuple notation used by the checker this is

`B_TARGET=(0,3,4,1,2,5)`.

It is an involution:

`B_TARGET^2=id`.

It also sends the known pure native star to the desired mixed observation:

`b(I_A)=J_B`.

### Theorem 4.1 — target `b` is outside the native block/whole-factor envelope

`B_TARGET notin W=(S3 x S3) semidirect C2`.

### Proof 1: partition image

Every element of `W` either preserves both blocks or swaps the two blocks as wholes. Hence for every `w in W`,

`w(I_A)` is either `I_A` or `I_B`.

But

`B_TARGET(I_A)=J_B={1,4,5}`,

which is neither `I_A` nor `I_B`. Thus `B_TARGET notin W`. QED.

### Proof 2: exhaustive finite certificate

The deterministic checker enumerates all `6*6*2=72` elements of `W` and verifies exact non-membership. This is not a heuristic search.

### Carrier/native separation witness

Let physical carrier `S4` act on the six K4 edges. The K4 vertex transposition `(A B)` induces exactly

`(E_2 E_4)(E_3 E_5)`, fixing `E_1,E_6`.

The checker verifies simultaneously:

- this six-axis permutation belongs to the 24-element physical carrier edge action;
- the same permutation is not in `W`.

This gives the sharp witness:

`carrier b exists` **and** `native b-lift is not expressible by the frozen native motion grammar`.

The failure occurs before payload/support/inverse preservation can even be checked: there is no well-typed native transform term with the required axis action. Therefore adding a passive sign/deck bit cannot repair it.

The exact obstruction category is

`NO_AXIS_REFINED_CROSS_BLOCK_STATE_TRANSFORM`.

This is an `OTHER_EXACT_TYPED_OBSTRUCTION` refinement of the taskbook vocabulary, paired with `MIXED_SLICE_RELATION_MISSING`.

---

## 5. D — Why carrier transport `J_A -> J_B` is not native equivalence

The carrier action has the exact identity

`b(J_A)=J_B`.

If one were allowed to define native geometry by carrier relabeling, this would solve the problem immediately. Gen7 explicitly forbids that move, and the native type calculation explains why it is invalid: the source `J_A` has a native Cell constructor while the target `J_B` does not.

Thus the following square has only its lower/readout arrow:

`native Cell_A  -- R~_b ? -->  native mixed Cell_B?`

`     | Phi                      | Phi`

`     v                          v`

`carrier J_A  ---- b -------> carrier J_B`.

The lower arrow is exact; the upper arrow is absent. There is no proved commutative lifting square.

---

## 6. E/F — Orbit completion and native relations are correctly gated off

The taskbook allows construction of `R~_a`, `J_C`, `J_D`, and checks of

`R~_a^3`, `R~_b^2`, `(R~_a R~_b)^4`

**only after** a genuine `J_B` and native `R~_b` exist.

That gate fails. Consequently this return does not fabricate `R~_a` or group relations at native-state strength.

One carrier-level fact is retained solely as a regression: the desired axis permutation satisfies `b^2=id`. This does **not** imply a native involution because the native lift does not type-check.

Likewise there is no native relation residue to report. The obstruction precedes composition; the correct residue status is

`NATIVE_RELATION_RESIDUE = NOT_REACHED`.

---

## 7. G — Minimal-obstruction theorem and smallest repair interface

### Theorem 7.1 — exact current-signature obstruction

Under the frozen P000 native signature reconstructed in Gen5/Gen6 and the accepted L1/tomography boundary:

1. every Cell-valued term is block-pure;
2. every transform generated by blockwise moves plus whole-factor exchange has axis action in `W`;
3. `J_B` is mixed and therefore not a Cell-valued term;
4. the required `b` action lies outside `W`;
5. yet `J_B` and `b` both exist exactly in the FCC/K4 readout.

Therefore the missing information is not carrier algebra. It is a missing native relation/state primitive connecting axis-refined local data across the two factors.

### Smallest new native capability that can remove the obstruction

There are two logically visible deficits, but they can be discharged by **one sufficiently strong new primitive** rather than two unrelated patches:

`BMix_b` = a native, axis-refined full-state primitive whose domain contains the state carrying `Cell_A(r)`, whose axis-type action is `(2 4)(3 5)`, and whose transport law declares the image of the `J_A` native Cell relation to be a genuine Cell relation on `J_B`, with preserved payload/support data and an inverse.

Equivalently, if the design prefers constructors and transforms to remain separate, the minimal interface can be factored into:

1. a mixed Cell constructor/transport relation
   `mu_r : (E_1-local, E_4-local, E_5-local) -> Cell_mixed(r;1,4,5)`
   together with an overlap law on the shared `E_1`; and
2. a cross-block full-state transform
   `R~_b` with the exact axis action `(2 4)(3 5)`.

This return does **not** assert either primitive exists in P000. It identifies what genuinely new native structure would have to be postulated or independently constructed to proceed.

A passive `C2` bit is insufficient because it changes fiber data without changing the base block partition, while the target requires a base-state axis mixer.

---

## 8. H — Time trace / failed lifting trace

There is one canonical shortest trace and it stops exactly at the native boundary.

`t=0`:

- native state component: `Cell_A(r)` with support `J_A=I_A`;
- native operation: identity;
- readout: `Phi(X_0)=J_A`.

`t=1` attempted carrier step:

- carrier operation: vertex transposition `(A B)`;
- carrier readout: `b(Phi(X_0))=J_B`;
- required native operation: `R~_b`;
- native state `X_1`: **undefined**, because target axis action is outside `W` and the target mixed Cell has no constructor.

So there are not yet two native rotation paths to compare. Time only records the first failed relation change; no hidden quotient is introduced.

---

## 9. I — Deterministic checker

Checker:

`research_checks/P000_NATIVE_MIXED_STAR_CROSS_BLOCK_ROTATION_V7_CHECK_20260829.py`

It uses only the Python standard library and exact finite enumeration.

Covered checks:

1. positive controls for pure native `Cell_A(r)` and `Cell_B(r)` at several base addresses;
2. negative native controls for `J_B,J_C,J_D`;
3. exact K4 star readout showing `J_B` is a valid carrier observation;
4. no-quotient regression: carrier validity does not change native Cell typing;
5. exhaustive construction of the 72-element block/whole-factor envelope `W`;
6. exact non-membership of target `b` in `W`;
7. `b^2=id` at the axis permutation level;
8. exact carrier `S4` six-edge action and identification of carrier `b` with the target permutation;
9. old whole-factor swap `rho` is outside physical carrier `S4`;
10. `J_A/J_B` carrier overlap `{1}` but native overlap type failure;
11. symmetric all-negative carrier representative fixed by `S4` and commuting deck `C2`, preserving the frozen `S4 x C2` split regression;
12. explicit declaration of the missing mixed-Cell / cross-block-transform interfaces.

Local execution output:

```text
PASS
carrier_JB_valid=True; native_JB_constructible=False
native_transform_envelope_order=72; desired_b_in_envelope=False
desired_b_squared=identity; carrier_b_exists=True; native_b_lift_typechecks=False
overlap_JA_JB_readout={1}; native_overlap=UNDEFINED
minimal_obstruction=MIXED_SLICE_RELATION_MISSING + NO_AXIS_REFINED_CROSS_BLOCK_STATE_TRANSFORM
carrier_split_S4xC2_regression=True; no_quotient_regression=True
```

---

## 10. Acceptance matrix

### A. Primitive native state semantics — PASS

The return explicitly separates native Cell-valued constructors, full product state, transformation envelope, and carrier readout. No carrier-to-native inverse definition is introduced.

### B. `J_B` geometric slice — EXACT OBSTRUCTION

`J_B` is carrier-valid but cannot be generated by the current Cell-valued constructor syntax. Native adjacency/gluing cannot be evaluated because target Cell typing is missing.

### C. cross-block `R~_b` — EXACT OBSTRUCTION

The exact target permutation is an involution and a physical carrier action, but is outside the 72-element generous native block/whole-factor envelope. Thus no current primitive composition can yield the requested full-state transform.

### D. `J_A <-> J_B` — EXACT LIFTING FAILURE

Carrier transport is exact; native transport is undefined. No relabeling is promoted to geometry.

### E. `R~_a` / orbit completion — CORRECTLY NOT REACHED

The B/C success gate is false.

### F. Native relations — CORRECTLY NOT REACHED

No native residue is invented before a native `b` exists.

### G. Minimal obstruction theorem — PASS

The obstruction is classified as

`MIXED_SLICE_RELATION_MISSING + NO_AXIS_REFINED_CROSS_BLOCK_STATE_TRANSFORM`.

A minimal new native `BMix_b` transport primitive, or its constructor+transform factorization, is isolated.

### H. Time trace — PASS

The shortest attempted lift is recorded and terminates at the first undefined native state.

### I. Deterministic checker — PASS

Exact finite checker passes with positive and negative controls.

---

## 11. Research conclusion

Gen7 closes a more precise question than Gen6.

Gen6 ended at “the carrier/cohomology lift does not create the missing native motion.” Gen7 now proves why the missing motion cannot be synthesized from the current native construction grammar:

`current native Cell language = block-pure`,

`current generous native motion envelope <= (S3 x S3) semidirect C2`,

while

`J_B` is mixed and `b=(2 4)(3 5)` is a partial block mixer.

The crucial separation is therefore exact:

**FCC/K4 already knows the mixed star and the b permutation; P000 native state semantics do not yet contain the primitive that makes either one geometric.**

This is a constructive obstruction, not evidence against the possibility of a richer P000 primitive. A successor should not revisit carrier algebra. It should either derive `BMix_b` directly from deeper native stack/handle relations not yet exposed in the frozen signature, or explicitly extend the native axiom/constructor system and then re-run the `J_B` gluing, payload/support, inverse, and native relation tests.

No stronger claim is warranted from the current axioms.
