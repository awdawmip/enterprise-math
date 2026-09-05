# BRC formal algebra / Lean frontier

Researcher-ID: `EM-BRCWLOG-6F42A1`  
Mode: `TASK_RESEARCH / DIRECT_USER_CONTINUATION`  
Date: `2026-09-05` (+08:00)  
Status: `RESEARCH_CANDIDATE / LEAN_FORMALIZATION_IN_PROGRESS / NOT_FOUNDATION`

## Objective

Make Branch-Recoalescence Collapse the typed algebraic bridge between Enterprise coordinates and ordinary algebra, while preserving the historical Boolean/result-support BRC as the canonical support shadow.

P000 remains unchanged: native Enterprise space is six-dimensional discrete Cell space, time is separately typed, the existing three-axis construction is a research slice, and rotation is the primary spatial transformation.  The constructions below do not derive or reduce P000 from a classical carrier.

## 1. BRC algebraic contract

A concrete BRC application must distinguish:

1. **branch population** — exact path occurrences or exact path-summary keys;
2. **branch identity** — which fields make two occurrences algebraically identical;
3. **alternative composition** — recoalescence/addition;
4. **serial composition** — ordered path concatenation;
5. **observers** — Boolean support, multiplicity, positive weight, coordinate, frame, length, moments, determinants, roots, etc.;
6. **future operation horizon** — which later compositions/rotations/port operations the compressed state must still support;
7. **scale horizon** — finite exact state versus recurrent/asymptotic readout.

Compression is allowed only relative to a declared observer/future-operation contract.  A distinction cannot be discarded merely because it is invisible to the current scalar output.

## 2. Exact framed path carrier

The new Lean layer introduces a generic coordinate action `rho : G -> C -> C`, requiring only the laws of a monoid action by additive endomorphisms.  It deliberately does not assume a Euclidean representation or a completed native rotation group.

A framed path summary is

`(weight, coord, frame, length)`.

Ordered serial composition is

`(w,n,g,l) * (v,m,h,k) = (wv, n + g.m, gh, l+k)`.

This is now formalized as a Lean `Monoid`.  The `coord` field is therefore not a decorative tag: it participates in multiplication through the preceding frame.

## 3. Positive multiplicity layer and Boolean shadow

Define

`FramedNBRC = MonoidAlgebra Nat FramedPath`.

The outer natural coefficient records multiplicity of identical framed summaries.  The exact positive weight remains a field of the summary key, so multiplicity and weight are not conflated.

Alternative recoalescence is algebra addition.  The current Lean theorem proves that Boolean shadow of positive addition is literal support union.  Thus the enrichment tower is typed as

`framed path occurrences -> N-BRC -> Boolean support`.

This extends rather than mutates historical Boolean BRC.  Reverse recovery of multiplicity/coordinate/frame after support collapse remains forbidden by `NO_RESURRECTION`.

## 4. Observer-safe and observer-unsafe erasures

For the observer `(weight,length)`, deleting coordinate and frame is a valid monoid homomorphism; it is therefore safe for that declared observer.

By contrast, deleting only the frame is not future-safe when a common right context can distinguish the resulting coordinates.  Lean proves this directly from the existing `noResurrection` theorem:

if `eraseFrame a = eraseFrame b` but `(a*c).coord != (b*c).coord`, then no decoder from `eraseFrame` can recover the future-coordinate observer.

This gives BRC a reusable formal information-loss test rather than an informal warning.

## 5. Carry is a typed coboundary, not one hard-coded formula

For any integer-valued compression potential `K` on a monoid, define

`delta_K(a,b) = K(ab)-K(a)-K(b)`.

Lean proves exactly

`delta_K(a,b)+delta_K(ab,c)=delta_K(b,c)+delta_K(a,bc)`.

If `K` is multiplicatively superadditive, the carry is nonnegative.

For framed coordinates this specializes to

`K(n + g.m)-K(n)-K(m)`.

This unifies two already-distinct Enterprise coordinate carries without identifying their observers:

- the earlier K4 optimal star-extraction carry;
- the six-axis CountAtlas/common-depth carry recorded by the current six-axis research frontier.

They are different potentials on different compressed states, but the same exact two-coboundary mechanism explains parenthesization independence.  This is a reusable BRC algebraic law.

## 6. Rotation/relabeling layer

For group-valued frames, global relabeling is

`R_s(w,n,g,l) = (w, s.n, s g s^-1, l)`.

The second Lean layer formalizes:

- `R_s(1)=1`;
- `R_s(ab)=R_s(a)R_s(b)`;
- `R_s(R_t(p))=R_(st)(p)`;
- inverse relabeling;
- rotation invariance of coordinate carry whenever the compression potential is coordinate-invariant.

Thus rotation covariance is inside multiplication rather than a post-hoc geometric annotation.

## 7. Why symmetric optimal fibres must remain branch-valued

A generic Lean theorem now captures the earlier finite S4 obstruction:

if an input is fixed by every declared symmetry and the candidate output carrier has no globally fixed point, then no equivariant deterministic selector exists.

Consequently an optimizer or canonicalizer must retain the entire symmetric optimal fibre (or add explicit symmetry-breaking data) rather than choose an arbitrary representative.  This is a structural BRC requirement, not an implementation preference.

The theorem is generic; instantiating it with the concrete six-axis K4/S4 atlas remains a separate formalization step.

## 8. Algebra bridge beyond the noncommutative layer

The prior rotation-atlas research already established an exact finite-frame lift: retain the frame as part of the state index and write transition entries in an ordinary commutative polynomial ring.  This permits determinant/response/root-atom calculations without applying a commutative determinant directly to the noncommutative framed path monoid.

The intended typed pipeline is therefore

`exact path/provenance`
`-> framed N-BRC`
`-> declared observer quotient`
`-> finite frame-state lift when needed`
`-> commutative polynomial/rational matrix algebra`
`-> determinant / Schur port / root-atom certificate`
`-> Boolean/log/scalar readout only when declared`.

The reverse arrows are not assumed.

## 9. Lean files and current proof boundary

Files in this branch:

- `EnterpriseMath/Relation/BranchRecoalescence.lean` — pre-existing Boolean/support core;
- `EnterpriseMath/Relation/FramedBranchRecoalescence.lean` — framed monoid, N-BRC, Boolean additive shadow, observer erasure, NO_RESURRECTION witness, generic and coordinate carries;
- `EnterpriseMath/Relation/BRCFrameSymmetry.lean` — global frame relabeling, carry covariance, equivariant single-choice obstruction;
- `EnterpriseMath.lean` — umbrella import.

Formalization intentionally does **not yet** claim:

- the full native six-axis Cell-address object;
- a complete native six-dimensional rotation group;
- a unique global native metric;
- the closed-form K4 theorem `K(n)=U(n)-delta(n)` in Lean;
- exact support equality for arbitrary N-BRC serial products;
- recurrent determinant/Schur/root-atom layers in Lean;
- signed/amplitude BRC.

CI status must be read from the final branch head.  A failed intermediate CI run is not erased from provenance and a pending run is not reported as green.

## 10. Next formal milestones

Highest-leverage sequence:

1. obtain warning-fatal Lean green for the generic framed/symmetry layer;
2. formalize atomic serial multiplication and then exact positive-support convolution;
3. instantiate the six-axis atlas action and the K4 symmetric-fibre obstruction;
4. formalize one concrete compression potential (prefer the simpler common-depth potential first), including superadditivity/invariance and its nonnegative carry;
5. formalize the K4 optimal extraction theorem separately;
6. lift a finite framed transition system to a commutative matrix/polynomial semantics and connect determinant/port identities;
7. connect generic root-block certificates only after the preceding semantic map is exact.

This order keeps BRC semantics authoritative and prevents downstream algebra from silently erasing coordinate/provenance distinctions.
