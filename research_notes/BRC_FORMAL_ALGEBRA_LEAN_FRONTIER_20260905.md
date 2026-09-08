# BRC formal algebra / Lean frontier

Researcher-ID: `EM-BRCWLOG-6F42A1`  
Mode: `TASK_RESEARCH / DIRECT_USER_CONTINUATION`  
Date: `2026-09-05` (+08:00)  
Status: `RESEARCH_CANDIDATE / WARNING_FATAL_LEAN_GREEN_AT_CODE_HEAD_26a3336 / NOT_FOUNDATION`

## Objective

Make Branch-Recoalescence Collapse the typed algebraic bridge between Enterprise coordinates and ordinary algebra, while preserving the historical Boolean/result-support BRC as the canonical support shadow.

P000 remains unchanged: native Enterprise space is six-dimensional discrete Cell space, time is separately typed, the existing three-axis construction is a research slice, and rotation is the primary spatial transformation. The constructions below do not derive or reduce P000 from a classical carrier.

## 1. BRC algebraic contract

A concrete BRC application must distinguish branch population, branch identity, alternative composition, serial composition, declared observers, the future-operation horizon, and the scale/recurrent horizon.

Compression is valid only relative to that contract. A distinction cannot be deleted merely because a current scalar readout ignores it; later composition, rotation, port elimination, provenance or another observer may still distinguish it.

## 2. Exact framed path carrier

Lean now has a generic additive coordinate action `ρ : G -> C -> C` and a framed path summary

`(weight, coord, frame, length)`.

Ordered serial composition is

`(w,n,g,l) * (v,m,h,k) = (wv, n + g·m, gh, l+k)`.

This is proved to form a `Monoid`. The coordinate and frame fields therefore participate in multiplication and are not decorative metadata.

The positive multiplicity layer is

`FramedNBRC = MonoidAlgebra Nat FramedPath`.

The outer natural coefficient records multiplicity of identical summaries while exact weight remains part of the path key.

## 3. Positive N-BRC -> Boolean BRC is now a full support bridge

The Boolean shadow of an N-BRC state is the nonzero support of its natural coefficients.

Lean proves both exact laws:

- alternative recoalescence: `shadow(f+g) = shadow(f) ∪ shadow(g)`;
- serial composition: `shadow(fg) = shadow(f) * shadow(g)` using pointwise set multiplication.

The reverse inclusion in the serial theorem uses positivity/no cancellation of `Nat`. This is the formal reason the theorem does not silently extend to signed/amplitude coefficients.

Thus historical Boolean BRC is an exact support shadow of the positive N-BRC layer, not a replacement for multiplicity or exact-weight semantics.

## 4. Observer algebra and NO_RESURRECTION

Every path-level monoid observer

`φ : FramedPath ->* M`

lifts canonically through `MonoidAlgebra.mapDomainAlgHom` to a whole-N-BRC algebra homomorphism.

This now provides one reusable mechanism for weight histograms, geometry-erased observers and future valuation/moment observers.

Joint observers are represented before recoalescence by the product observer `(φ,ψ)`. Lean proves that the joint observer recovers either component. Conversely, if `φ` merges two paths that `ψ` separates, then `φ` cannot recover `(φ,ψ)`; this is a direct `NO_RESURRECTION` theorem and formalizes the loss of correlation in separate marginals.

The older frame-erasure obstruction remains: if erased-frame states agree but a common right context gives different future coordinates, frame erasure is not future-safe.

## 5. Frame relabeling is internal algebra, not annotation

For group-valued frames,

`R_s(w,n,g,l) = (w, s·n, s g s^-1, l)`.

Lean proves identity, multiplication compatibility, successive relabeling, inverse relabeling, a framed-path monoid equivalence, and the induced algebra equivalence on the entire positive N-BRC.

Coordinate carries are invariant under relabeling whenever their potential is invariant under the declared coordinate action.

A separate generic theorem proves that at a symmetry-fixed input, an equivariant deterministic selector can only return a globally fixed output. If the output carrier has no fixed point, no such single-valued equivariant selector exists. This is the formal reason symmetric optimal fibres must remain branch/set-valued unless explicit symmetry-breaking data are supplied.

## 6. Carry is a typed two-coboundary

For an integer-valued potential `K` on any monoid,

`δ_K(a,b) = K(ab) - K(a) - K(b)`.

Lean proves the exact cocycle identity

`δ_K(a,b)+δ_K(ab,c)=δ_K(b,c)+δ_K(a,bc)`.

Superadditivity of `K` implies nonnegative carry. For framed coordinates this specializes to

`K(n + g·m) - K(n) - K(m)`.

This is the correct unification of two distinct Enterprise carries:

- the earlier K4 optimal-extraction carry;
- the finite CountAtlas/common-depth carry.

They remain different potentials on different observer states; they share the same coboundary law. No equality between those potentials is asserted.

## 7. Exact-weight histogram and character readouts

Exact path weight is a multiplicative observer. It therefore induces

`framed N-BRC -> MonoidAlgebra Nat W`,

a finite exact-weight histogram which is invariant under global frame relabeling.

Lean then uses the universal property `MonoidAlgebra.lift`: every multiplicative character

`χ : W ->* R`

extends to an algebra readout of the exact histogram and hence of the framed N-BRC.

Formalized specializations include:

- constant-one character -> exact branch multiplicity/count;
- power character `q -> q^m` over a commutative semiring -> exact power-sum moment;
- atomic `m=0` and `m=1` specializations -> multiplicity and total-mass contributions.

This is the Lean bridge to the existing Weighted-BRC histogram/moment tower. It does not yet formalize every CWM max/recurrent readout.

## 8. Finite CountAtlas common-depth layer is now a canonical normal form

For a finite axis type `ι`, define

`CountAtlas ι = ι -> Nat`.

The six-axis specialization is `ι = Fin 6`, but the current Lean theorem is deliberately generic. A declared frame action is required to act by coordinate reindexing/permutation.

Define common depth

`h(n) = min_i n_i`

and normalized residue

`r(n)_i = n_i - h(n)`.

Lean proves:

- `h(n)` is below every coordinate and is attained by some axis;
- normalized residue has at least one zero coordinate;
- `h(r(n)) = 0`;
- normalization is idempotent;
- exact restoration `h(n) + r(n)_i = n_i`;
- adding common scalar depth shifts the minimum exactly;
- any normalized `(h,r)` decomposes back to itself;
- the canonical equivalence

  `CountAtlas ι ≃ { (h,r) // commonDepth(r)=0 }`;

- common depth is invariant under axis reindexing;
- normalization and canonical decomposition are equivariant under axis reindexing;
- common depth is superadditive under framed serial coordinate addition;
- the induced common-depth carry is nonnegative, obeys the exact two-coboundary cocycle, and is frame invariant;
- for normalized inputs the carry is exactly `min(r + g·s)`.

This is now a genuine reversible compression certificate, not only a carry formula.

## 9. Typed algebra pipeline and remaining boundary

The intended pipeline is now

`exact path/provenance`
`-> framed N-BRC`
`-> exact support / exact-weight histogram / declared joint observer`
`-> finite frame-state lift when needed`
`-> commutative polynomial/rational matrix algebra`
`-> determinant / Schur port / root-atom certificate`
`-> scalar/log/Boolean readout only when declared`.

Reverse arrows are not assumed without a proved recovery map.

Current Lean formalization intentionally does **not** claim:

- the full native six-axis Cell-address object;
- a complete native six-dimensional rotation group or concrete `Fin 6`/S4 instantiation;
- a unique global native metric;
- the closed-form K4 theorem `K(n)=U(n)-δ(n)` in Lean;
- signed/amplitude cancellation semantics;
- recurrent SCC, determinant, Schur-port or root-atom transfer in Lean;
- every CWM/max/recurrent observer as a histogram character.

## 10. Lean files

- `EnterpriseMath/Relation/FramedBranchRecoalescence.lean` — framed semidirect monoid, N-BRC, erasure tests, generic/coordinate coboundary carries;
- `EnterpriseMath/Relation/BRCPositiveSupport.lean` — exact positive Boolean support under addition and serial multiplication;
- `EnterpriseMath/Relation/BRCFrameSymmetry.lean` — frame relabel equivalences, carry covariance, equivariant single-choice obstruction;
- `EnterpriseMath/Relation/BRCObserverAlgebra.lean` — generic observer lift, joint observers and correlation-loss NO_RESURRECTION boundary;
- `EnterpriseMath/Relation/BRCWeightHistogram.lean` — exact-weight histogram observer and frame invariance;
- `EnterpriseMath/Relation/BRCWeightCharacters.lean` — universal character readouts, count and power moments;
- `EnterpriseMath/Relation/BRCCountAtlas.lean` — finite atlas common depth, canonical normal-form equivalence, carry and equivariance;
- `EnterpriseMath.lean` — umbrella imports.

## 11. Verification checkpoint

Code head `26a33364bf705fd62e6179f4d70478edc8cb1c70` passed GitHub Actions Lean run `1586`, job `101266552945`, compiling the complete umbrella with

`lake build --wfail -KCI EnterpriseMath`.

That is a warning-fatal whole-library verification checkpoint. This research note is a later documentation synchronization commit, so final PR status must still be read from the final branch head; prior failed intermediate runs remain provenance.

## 12. Next formal milestones

Highest-leverage next sequence:

1. instantiate the concrete six-axis/K4 permutation action into the generic CountAtlas/relabel layer and prove the concrete symmetry hypotheses;
2. formalize the K4 optimal-extraction potential and its closed form separately, then connect its carry to the already-proved generic coboundary interface;
3. formalize the finite framed transition-system lift into commutative matrix/polynomial semantics;
4. connect exact histogram moments/valuations to finite recurrent and port transfer;
5. only then lift determinant/Schur/root-atom certificates through the proved semantic maps;
6. treat signed/amplitude cancellation as a separate carrier rather than weakening the positive BRC theorems.

This order keeps BRC carrier/observer semantics authoritative and prevents later algebra from silently erasing coordinate, multiplicity, frame or provenance distinctions.
