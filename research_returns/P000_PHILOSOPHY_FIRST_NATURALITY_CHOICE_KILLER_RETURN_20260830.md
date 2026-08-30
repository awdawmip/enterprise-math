# P000 Philosophy-First Q7 — Naturality and Arbitrary-Choice Killer

Task: `RS-P000-PHILOSOPHY-FIRST-NATURALITY-CHOICE-KILLER`  
Publication: `TP2-9F907FC5D0A68696607A`  
Researcher: `EM-P000Q7-7C4A2E`  
Claim: `chatgpt-p000q7-20260830-1157-7c4a2e`  
Execution: `ER-488BE9C979E5C0764616`  
Result: `RR-1ECF8B93CCAF6463224F`

Terminal research state:

`SUCCESS / NONCANONICAL_CHOICE_CERTIFICATES_CONSTRUCTED`

Hard target disposition:

`P000_NATURALITY_AND_ARBITRARY_CHOICE_EXACTLY_SEPARATED`

## 1. Exact model-level naturality criterion

Let `Gamma` be a finite groupoid of declared finite P000 models and primitive-preserving model isomorphisms. Let

`C : Gamma -> FinSet`

be a candidate-construction functor: `C(M)` is the finite set of admissible candidate frames, sections, probe choices, coordinates, or other constructions on `M`, and each model isomorphism transports candidates functorially.

A **natural selection** is a natural transformation

`eta : 1 -> C`,

where `1` is the singleton functor. Equivalently, one chooses `eta_M in C(M)` for every model and requires

`C(phi)(eta_M) = eta_N`

for every primitive-preserving isomorphism `phi:M->N`.

### Theorem — finite groupoid component fixed-point criterion

Choose one representative `M_i` from each connected component / isomorphism class of `Gamma`. Then

`Nat(1,C)  ~=  product_i C(M_i)^{Aut_Gamma(M_i)}`.

Hence

`|Nat(1,C)| = product_i |C(M_i)^{Aut_Gamma(M_i)}|`.

In particular:

`POINTWISE_NONEMPTY_CANDIDATES != NATURAL_SELECTION_EXISTS`.

If one component has no candidate fixed by every primitive-preserving automorphism, then no global natural selection exists.

### Proof

A natural selection restricted to a representative `M_i` must be fixed by every `alpha in Aut(M_i)` because naturality gives `C(alpha)(eta_i)=eta_i`.

Conversely, choose `c_i in C(M_i)^{Aut(M_i)}`. For any `N` in the same component, choose an isomorphism `f:M_i->N` and define `c_N=C(f)(c_i)`. If `g:M_i->N` is another isomorphism, then `g^{-1}f in Aut(M_i)`, so fixedness of `c_i` implies `C(f)(c_i)=C(g)(c_i)`. Thus the transported choice is well-defined and natural. Components are independent, giving the product formula.

This is standard finite groupoid/group-action mathematics, not a novelty claim. Its role here is to turn the P000 word “natural” into an exact falsifiable gate.

## 2. Four different strengths must not be conflated

The following notions are not one undifferentiated notion of canonicity.

1. **Unique object:** `|C(M)|=1`.
2. **Unique isomorphism class:** the candidate action groupoid has one orbit.
3. **Fixed point:** some candidate is fixed by the full primitive-preserving `Aut(M)` action.
4. **Natural section:** a coherent family over the whole model groupoid.

On one connected component, natural sections are exactly the fixed candidates at one representative. Therefore a unique object is automatically fixed, but a **unique isomorphism class need not contain any fixed representative**. A torsor is the canonical counterexample: one orbit, no fixed point.

Likewise, several fixed points give several natural sections, so naturality alone does not imply uniqueness.

## 3. Certificate A — six-channel coordinate selection

The accepted Gen9 bridge records the symmetric PF-10 channel relabeling image as `S6`, of order `720`, before additional axis-channel frame data are supplied.

Audit the candidate construction “choose one of the six channels as the distinguished coordinate.”

- primitive-preserving automorphism image: `S6`;
- candidates: `6` channels;
- orbit decomposition: one orbit of size `6`;
- stabilizer of one channel: `S5`, order `120`;
- global fixed candidates: `0`.

Therefore

`SIX_SYMMETRIC_CHANNELS -> NO_NATURAL_DISTINGUISHED_COORDINATE`.

Every model admits six pointwise choices, but the bare symmetric model admits no equivariant singleton choice.

## 4. Certificate B — axis-channel frame torsor

For the current frame interface `f:A->C`, with six native axis labels and six symmetric channels, the candidate frames are all bijections. There are

`6! = 720`

frames.

`S6` acts by postcomposition `sigma.f`. This action is free and transitive:

- for any two frames `f,g`, the unique relabeling `sigma=g f^{-1}` sends `f` to `g`;
- if `sigma.f=f`, surjectivity of `f` forces `sigma=id`.

Thus:

- candidate count: `720`;
- orbit count: `1`;
- orbit size: `720`;
- stabilizer: `1`;
- global fixed frame count: `0`.

This is an exact instance of

`ONE_ISOMORPHISM_CLASS != CANONICAL_REPRESENTATIVE`.

It sharpens the Gen9 `720`-frame ambiguity: a frame is not made natural merely because all frames are equivalent. The correct bare object at this strength is the frame torsor/orbit-valued datum, unless some additional primitive or derived invariant breaks the symmetry.

## 5. Certificate C — ordered K4-star probe atlas

The strict bridge accepts a `K4` star observation atlas. This result does **not** add a vector-space structure or claim that an ordered basis is primitive. It audits only the extra choice of **ordering** the four accepted star probes.

The carrier `S4` acts on the four stars. The set of total orderings has `4!=24` elements and is a regular `S4` torsor:

- candidate orderings: `24`;
- orbit count: `1`;
- stabilizer: `1`;
- global fixed ordering count: `0`.

Therefore the unordered four-star atlas may be invariant while

`NO_NATURAL_ORDERED_K4_STAR_PROBE_BASIS`

holds at the same primitive strength. Downstream formulas may choose an ordering for computation, but that order cannot be re-imported as native data.

## 6. Certificate D — split `C2 x S4 -> S4` lift sections

The accepted carrier-lift envelope includes the split extension

`q : C2 x S4 -> S4`,  `q(z,g)=g`.

A homomorphic section has the form

`s_chi(g)=(chi(g),g)`

for a character `chi:S4->C2`.

Since `[S4,S4]=A4`, the abelianization is `C2`, so there are exactly two characters:

- `chi=0`;
- `chi=sign`.

Hence there are exactly **two** homomorphic sections.

Now classify all automorphisms of the extension that preserve the quotient map `q`. Because `Aut(C2)` is trivial, every such automorphism is uniquely

`alpha_psi(z,g)=(z+psi(g),g)`

with `psi in Hom(S4,C2)`. Thus there are exactly two `q`-preserving automorphisms, and

`alpha_psi . s_chi = s_(psi+chi)`.

The nontrivial automorphism swaps the two sections. Therefore the section action groupoid has:

- candidate sections: `2`;
- one isomorphism orbit of size `2`;
- trivial stabilizer;
- invariant section count: `0`.

So the exact frozen conclusion is

`SPLIT_EXTENSION + HOMOMORPHIC_SECTIONS_EXIST + UNIQUE_SECTION_ISOMORPHISM_CLASS`

but

`NO_NATURAL_SECTION_UNDER_FULL_q_PRESERVING_AUTOMORPHISMS`.

This is the required `EXISTS_POINTWISE_BUT_NO_EQUIVARIANT_SELECTION` certificate and directly attacks the Gen13 canonicality gap. Splitting is an existence statement, not a canonicity theorem.

## 7. Positive regressions — naturality is not a blanket no-go

### 7.1 Genuine primitive root

If a distinguished channel `c0` is genuinely part of the primitive model data, primitive-preserving automorphisms reduce from `S6` to the subgroup `S5` fixing `c0`.

On the six channel candidates the global fixed set is then exactly `{c0}`. Thus the same coordinate-selection problem has one and only one natural answer after an actual symmetry-breaking datum is supplied.

This proves the intended discipline:

`ARBITRARY_SYMMETRY_BREAKING_FORBIDDEN`, but `STRUCTURALLY_GIVEN_SYMMETRY_BREAKING_ALLOWED`.

### 7.2 Gen12 `K=1` frozen generated lift group

At the accepted Gen12 strength, the frozen generated enriched action has order `24`, axis image order `24`, and axis-readout kernel `K=1`. On that **already fixed framed model and generated lift group**, `q` is an isomorphism, so its inverse is the unique homomorphic section.

Thus Gen12 is a positive singleton-section regression **relative to the declared framed model**.

It does not solve the bare-P000 naturality problem because bare P000 does not canonically select that framed model or its axis-channel frame in the first place.

## 8. Current candidate audit

| Candidate | Primitive symmetry at audited strength | Candidate orbit/fiber | Aut-fixed candidates | Q7 verdict |
|---|---:|---:|---:|---|
| one PF-10 channel as coordinate | `S6` | `6` | `0` | nonnatural |
| axis-channel frame `A->C` | `S6` | one free orbit of `720` | `0` | nonnatural torsor |
| ordering of accepted K4 star probes | `S4` | one free orbit of `24` | `0` | unordered atlas survives; ordering does not |
| section of split `C2 x S4 -> S4` | quotient-preserving `C2` action | one free orbit of `2` | `0` | split but no natural section |
| coordinate with primitive root `c0` | `S5` | `{c0}` plus the other-channel orbit | `1` | unique natural coordinate |
| Gen12 `K=1` section on fixed generated lift group | trivial over-quotient ambiguity | singleton | `1` | unique relative section |

## 9. Reusable `FINITE_NATURALITY_CHECKER_V1` specification

Input:

1. finite model-groupoid connected-component representatives;
2. finite candidate set for each representative;
3. the exact primitive-preserving automorphism permutation image on each candidate set;
4. verified candidate transports for model isomorphisms.

Checks:

1. validate every automorphism image as a finite group action;
2. compute candidate orbits, stabilizers, and global fixed candidates;
3. for an explicit multi-object groupoid, validate identity/composition/inverse transport laws;
4. compute
   `N_nat = product_i |Fix_Aut(M_i)(C(M_i))|`;
5. return a fixed candidate/natural section certificate when `N_nat>0`, otherwise return one component with empty fixed set as an exact obstruction.

Tool resolution:

`T7_FINITE_SYMMETRY_EQUIVARIANCE / REUSE_APPLIED`.

The task-local checker imports and uses the existing `enterprise_math.finite_symmetry` orbit/fixed-point calculus. No new global tool family is proposed.

## 10. Exact checker certificate

The task-local checker verifies the finite groups and orbit/fixed-point claims, including:

- `|S6|=720` and channel stabilizer `120`;
- the `720`-frame free transitive action;
- the `24` ordered K4-star probe-atlas free transitive action;
- `[S4,S4]=A4` and exactly the trivial/sign `C2` characters;
- the two-section free quotient-preserving automorphism orbit;
- the rooted `S5` positive fixed-point regression;
- the singleton `K=1` logical regression.

Expected exact summary:

`PASS P000_NATURALITY_CHOICE_KILLER; checks=20; finite_groupoid_rule=natural_selections_product_of_component_Aut_fixed_sets; coordinate=S6:candidates6:fixed0:stab120; frame=S6:candidates720:one_free_orbit:fixed0; probe_order=S4:candidates24:one_free_orbit:fixed0; split_lift=C2xS4:sections2:one_free_qAut_orbit:fixed0; rooted_coordinate=S5:fixed1; gen12_K1_section=singleton`

## 11. What is proved, and what is not

Proved at the declared finite-model strength:

1. naturality is exactly an automorphism-equivariance/fixed-point condition, not an aesthetic label;
2. pointwise existence does not imply natural selection;
3. unique isomorphism class does not imply a fixed representative;
4. current symmetric frame, coordinate and ordered-probe choices are exact noncanonical choices at their audited symmetry strength;
5. the split `C2 x S4` extension supplies an exact section-existence/no-natural-section certificate;
6. genuine primitive symmetry breaking can restore a unique natural choice.

Not proved:

- that every future P000 model has the same automorphism group;
- that the split `C2 x S4` envelope is the only Gen13 lift regime;
- that carrier `S4` is the full native P000 rotation group;
- that an unordered K4 star atlas is a native complete probe language;
- that no enriched primitive can canonically determine a frame or coordinate;
- any novelty of the classical fixed-point/naturality theorem.

## 12. Control-plane recommendation

Driver review should freeze the following gate for any future claim using words such as `canonical`, `natural`, `distinguished`, `preferred`, or `intrinsic`:

`DECLARE_MODEL_GROUPOID -> DECLARE_CANDIDATE_FUNCTOR -> COMPUTE_PRIMITIVE_PRESERVING_AUT_ACTION -> REQUIRE_FIXED_POINT/NATURALITY_CERTIFICATE`.

For current bare-P000 work, use torsor/orbit/groupoid-valued data instead of silently choosing a frame, coordinate, ordered probe atlas, or split section when the full primitive-preserving symmetry has no fixed candidate.

For Gen13 specifically, `SECTION_EXISTS` and `EXTENSION_SPLITS` must remain separate from `NATURAL_SECTION_EXISTS`; canonicality requires the full primitive-preserving `q`-automorphism action on the section set.

Q8 may consume this result as one exact reason to retain morphisms/isotropy rather than collapsing immediately to a set of isomorphism classes, but this Researcher does not publish a successor merely because Q7 succeeded.
