# P018 — Finite-Precision Proof Calculus: Supplement 07

Status: `ACTIVE RESEARCH NOTE`  
Scope: additive laxity of adjoint projection, the carry 2-cocycle, cross-precision coherence, and candidate feedback into the foundational logic  
Depends on: P005, P008, P009, and P018 stages 1–7  
Discipline: group cohomology, factor sets, group extensions, adjunctions, and lax-monoidal language are established mathematics. This note studies their exact interface with Enterprise Math finite-precision semantics and does not claim those established structures as project inventions.

## 1. Why carry now deserves to move one layer downward

P018-T04 already proves that for precision ratio `r`, if

\[
x=ra+u,\qquad y=rb+v,\qquad 0\le u,v<r,
\]

then

\[
x+y=r(a+b+c)+t,
\]

where

\[
c=(u+v)//r\in\{0,1\},
\qquad t=(u+v)\bmod r.
\]

This was previously interpreted as an exact event in which fine details jointly change the coarse-layer addition result. That interpretation remains correct, but it is not yet the most structural one.

P008 proves that the scale embedding

\[
L_r(a)=ra
\]

and integer quotient

\[
Q_r(x)=x//r
\]

form an order adjunction

\[
L_r\dashv Q_r.
\]

Moreover, `L_r` strictly preserves addition. A deeper fact therefore appears: **the right adjoint `Q_r` does not strictly preserve addition, and carry measures exactly that failure.**

This supplement promotes that observation from an arithmetic trick to a reusable defect structure and tests whether it belongs immediately above the P008 core.

---

## 2. P018-T63 — An additive left adjoint makes its right adjoint superadditive

Status: `PROVED / ESTABLISHED ORDER-THEORETIC PATTERN`

Let `A,B` be ordered commutative monoids whose addition is monotone. Suppose

\[
l:A\to B
\]

strictly preserves addition and has a right adjoint

\[
l\dashv u.
\]

Then for every `x,y\in B`,

\[
\boxed{u(x)+u(y)\le u(x+y).}
\]

### Proof

By the adjunction counit inequalities,

\[
l(u(x))\le x,
\qquad l(u(y))\le y.
\]

Addition is monotone and `l` preserves addition, hence

\[
l(u(x)+u(y))
=l(u(x))+l(u(y))
\le x+y.
\]

The adjunction equivalence

\[
l(a)\le b\iff a\le u(b)
\]

therefore yields

\[
u(x)+u(y)\le u(x+y).
\]

∎

Taking `l=L_r:a↦ra` and `u=Q_r:x↦x//r` gives immediately

\[
\boxed{Q_r(x)+Q_r(y)\le Q_r(x+y).}
\]

Thus superadditivity of floor projection is not an isolated integer identity; it is forced by the P008 adjunction once addition is present.

The first foundational feedback is therefore: the P008 order-adjoint core does not need to change, but once a state space also carries operations compatible with scale transport, its right-adjoint projection naturally acquires a non-strict operation-preservation structure.

---

## 3. P018-T64 — Additive carry is the exact integer slack of the adjunction

Status: `PROVED`

For any integer `m>=1`, define

\[
Q_m(x)=x//m,
\qquad \delta_m(x)=x\bmod m.
\]

Write

\[
x=ma+u,
\qquad y=mb+v,
\qquad 0\le u,v<m.
\]

Define

\[
\boxed{\kappa_m(u,v)=\left\lfloor\frac{u+v}{m}\right\rfloor.}
\]

Since `u+v<2m`, `kappa_m(u,v) in {0,1}`. Then

\[
\boxed{
Q_m(x+y)-Q_m(x)-Q_m(y)=\kappa_m(u,v).
}
\]

The proof is just the Euclidean decomposition of `x+y=m(a+b)+(u+v)`.

Carry can therefore be defined exactly as

\[
\boxed{\text{operation defect}=Q_m(x+y)-Q_m(x)-Q_m(y).}
\]

It is the **entire** gap between coarse projection and an additive homomorphism, with no hidden remainder. For a degree-`q` P018 state, taking `m=r^q` gives the same theorem.

---

## 4. P018-T65 — Standard carry satisfies the normalized 2-cocycle identity

Status: `PROVED / PRIOR-ART INSTANCE`

Fix `m>=1` and let

\[
D_m=\{0,1,\ldots,m-1\}.
\]

Define modular addition

\[
u\oplus v=(u+v)\bmod m.
\]

For

\[
\kappa_m(u,v)=\left\lfloor\frac{u+v}{m}\right\rfloor,
\]

we have

\[
\boxed{
\kappa_m(u,v)+\kappa_m(u\oplus v,w)
=\kappa_m(v,w)+\kappa_m(u,v\oplus w).
}
\]

Also,

\[
\kappa_m(0,u)=\kappa_m(u,0)=0,
\qquad \kappa_m(u,v)=\kappa_m(v,u).
\]

### Proof

From

\[
u+v=m\kappa_m(u,v)+(u\oplus v),
\]

expand `u+v+w` once by first associating `(u+v)+w` and once by first associating `u+(v+w)`. The final remainders agree because modular addition is associative. Uniqueness of Euclidean decomposition then forces equality of the two coarse coefficients. ∎

### Prior-art boundary

The viewpoint that carrying is a 2-cocycle / factor set related to group extensions is established mathematics. Daniel C. Isaksen's *A Cohomological Viewpoint on Elementary School Arithmetic* (American Mathematical Monthly, 2002, DOI `10.1080/00029890.2002.11919915`) explicitly studies elementary carrying from this viewpoint.

Therefore the cocycle identity in T65 is **not an Enterprise Math invention**. The project-specific question is whether this established cocycle can unify a broader family of operation/refinement defects under the P005/P008/P018 semantics in which finite precision is explicit state and coarsening is a many-to-one projection.

---

## 5. P018-T66 — Coarse state + detail + carry exactly reconstruct integer addition

Status: `PROVED`

Define

\[
\Phi_m:\mathbb N\to\mathbb N\times D_m,
\qquad \Phi_m(x)=(Q_m(x),\delta_m(x)).
\]

By Euclidean decomposition, `Phi_m` is a bijection with inverse

\[
\Phi_m^{-1}(a,u)=ma+u.
\]

Define twisted addition on `N x D_m` by

\[
\boxed{
(a,u)\boxplus(b,v)
=\bigl(a+b+\kappa_m(u,v),\ u\oplus v\bigr).
}
\]

Then

\[
\boxed{\Phi_m(x+y)=\Phi_m(x)\boxplus\Phi_m(y).}
\]

Hence

\[
\boxed{(\mathbb N,+)\cong(\mathbb N\times D_m,\boxplus).}
\]

The right-hand side is not ordinary product addition. The carry cocycle is exactly what glues coarse and detail coordinates into the correct additive algebra. Associativity of `boxplus` is precisely guaranteed by the cocycle identity of T65.

The second foundational feedback is therefore: if the foundational logic decomposes finite-precision state into coarse and detail layers, cross-layer carry cannot be discarded as implementation noise; deleting it changes the algebra itself.

---

## 6. P018-C07 — Forcing projection to be a strict additive homomorphism destroys real structure

Status: `COUNTEREXAMPLE / DESIGN WARNING`

For every `m>1`, take

\[
x=1,\qquad y=m-1.
\]

Then

\[
Q_m(1)=0,
\qquad Q_m(m-1)=0,
\]

but

\[
Q_m(m)=1.
\]

Therefore

\[
\boxed{Q_m(x+y)\ne Q_m(x)+Q_m(y).}
\]

Any future formalization of precision systems that requires every coarse projection to be a strict additive homomorphism would therefore exclude the most elementary finite-precision arithmetic.

The correct direction is not to force the defect to vanish, but to model it explicitly.

---

## 7. P018-T67 — Carry coherence along a two-level precision chain

Status: `PROVED`

Consider two successive precision ratios `r,s>=1`. For a degree-`q` object, write

\[
R=r^q,\qquad S=s^q.
\]

Each finest-level detail can be written uniquely as

\[
t_i=S u_i+v_i,
\qquad 0\le u_i<R,
\qquad 0\le v_i<S.
\]

Define the lowest-detail carry

\[
c_S=\kappa_S(v_1,v_2).
\]

Then the direct carry across the total ratio `RS` satisfies

\[
\boxed{
\kappa_{RS}(t_1,t_2)
=\left\lfloor\frac{u_1+u_2+c_S}{R}\right\rfloor.
}
\]

The total remainder also satisfies

\[
\boxed{
(t_1+t_2)\bmod(RS)
=S\bigl((u_1+u_2+c_S)\bmod R\bigr)
+((v_1+v_2)\bmod S).
}
\]

### Proof

Write

\[
v_1+v_2=Sc_S+w,
\qquad 0\le w<S.
\]

Then

\[
t_1+t_2=S(u_1+u_2+c_S)+w.
\]

Next write

\[
u_1+u_2+c_S=Rc_R+z,
\qquad 0\le z<R.
\]

Hence

\[
t_1+t_2=RS c_R+Sz+w,
\]

with `0<=Sz+w<RS`. Uniqueness of Euclidean decomposition gives both formulas. ∎

Thus **direct coarsening** and **staged coarsening** do not produce contradictory carries. A lower-level carry becomes an integer input to the next level, which then determines whether another boundary is crossed.

P018-T02 nested detail composition and the T65 cocycle therefore form a common coherence structure along finite precision chains.

---

## 8. From one carry to general operation defect

Addition is the cleanest case because its defect is binary and directly forms the standard 2-cocycle.

P018 has already proved, however, that:

- multiplication has `C_times`;
- power maps have `C_p^prec`;
- the collapse/refinement commutation defect is the power carry of the root state;
- general nonnegative homogeneous monomials have bounded integer naturality defects.

The new unifying question should therefore **not** assume that every defect is the same cocycle. That is unproved and likely too strong.

A safer general definition is

\[
\boxed{
D_f^{e:d}(x)
=\pi^{out}_{e\to d}(f_e(x))
-f_d(\pi^{in}_{e\to d}(x)),
}
\]

whenever the difference is defined in the relevant ordered integer object. Then investigate separately:

1. `D_f=0`: the operation is strictly natural under precision projection;
2. nonzero `D_f`: an exact finite defect of non-strict naturality;
3. how defects compose under composition of operations;
4. coherence between direct and staged defects along multi-level precision chains;
5. which defects are cocycles and which require higher or different algebraic structures.

The rule is: **prove the defect law first, then choose the mature mathematical language; do not distort the object merely to fit the word “cohomology.”**

---

## 9. Feedback into P008: a two-layer foundation, not a replacement of the proved core

The current P008 conclusion remains intact: for the v0.1 root / quotient / collapse core, partial order + order embedding + right adjoint are sufficient.

This supplement adds a second layer.

### Layer 0 — Order-adjoint core

\[
\boxed{
\text{partial order}
+\text{order embedding}
+\text{right adjoint}
}
\]

This explains roots, quotients, exact recovery, and interior/collapse.

### Layer 1 — Defect-enriched operation core

When a concrete problem also requires addition, multiplication, or another operation, do not require coarse projection to be a strict homomorphism. Instead add

\[
\boxed{
\text{typed operation}
+\text{precision projection}
+\text{exact operation defect}
+\text{coherence law}.
}
\]

A “minimal foundation” therefore need not place every future operation into P008 at once. It can grow by justified layers, consistent with the P008 rule that stronger structure must be shown necessary operation by operation.

---

## 10. Feedback into P005/P009: scale arrows must remain typed

P009 already proves that erasing scale labels creates spurious dynamics. T67 adds that carry coherence also depends on the explicit precision ratios and degree.

Any future cohomological or defect language must therefore not collapse the system into self-maps of one untyped integer set. A reasonable object must record at least `(d,x,q)` or equivalent type data, where `d` is precision/scale, `x` is the explicit integer state at that level, and `q` is scale degree. Arrows may act only when types match.

---

## 11. Feedback into P012: keep graph geometry and add a quotient/fiber route

P012 stage 1 already proves that shortest-path natural-number distance generated by primitive adjacency is a full intrinsic integer metric. That result should not be replaced.

The new method-level input adds a parallel route:

1. **primitive-step geometry**: primitive relation → graph/word metric;
2. **fiber/quotient geometry**: precision partition / congruence / coset → cost of distinguishing states;
3. **exact lattice lift**: when a finite algebraic problem embeds faithfully into an integer lattice, use the lattice as a proof representation rather than as a pre-assumed physical Euclidean substrate.

The P012-C01 boundary remains important: squared Euclidean distance is integer-valued but is not generally a metric. “Integer-valued” alone cannot replace geometric axioms.

---

## 12. Feedback into P017: move beyond termwise good signs toward global certificates, while preserving every existing route

P017 already contains bulk / carry / shell / half-scale / threshold-complex / duality routes. This supplement does not remove involution, pairing, or termwise cancellation. It adds a higher-level question:

> Even when local shells or carries have mixed signs, can an integer potential / dual witness / certificate on the whole finite precision hierarchy force the target inequality globally?

Priority candidates are:

1. **partition potential** built from cross-level ambiguity/conflict multiplicity;
2. **shell certificate** permitting negative local terms but bounding a designated linear combination of all relevant precision shells;
3. **defect budget** treating carry, Möbius shell, and half-scale dual correction as separate defect accounts in one finite proof, with a proved bound on total budget.

If a global certificate fails, that failure should identify which local structure must remain explicit rather than invalidating the existing route.

---

## 13. Representation switch: proof language may change; ontology may not be silently replaced

Enterprise Math chooses explicit finite integer states and precision as its ontology. That does not require every proof to remain within elementary integer arithmetic.

Adopt the following research discipline:

\[
\boxed{
\text{finite-state problem}
\xrightarrow{\text{faithful representation}}
\text{other mathematical language}
\xrightarrow{\text{proof}}
\text{finite-state theorem}.
}
\]

Group cohomology, category/adjunction/lax structures, algebraic geometry, harmonic or spectral methods, convex duality, topology/homology, lattice theory, finite-field coding, and functional/analytic estimates may all be used as **proof languages**, provided that:

1. the representation map is explicit;
2. the required faithful / injective / equivalence property is proved;
3. the result can be translated back to the original finite state system;
4. a continuum used inside the proof space is not automatically promoted to the ontology of nature.

This turns “change representation” into a formal method rather than route drift.

---

## 14. Candidate foundational skeleton: Defect-Enriched Precision System

Status: `RESEARCH SYNTHESIS / NOT FROZEN`

Combining P005, P008, P009, P010, P012, and P018 suggests the following candidate skeleton.

### A. Typed finite states
Each level has an explicit state space `X_lambda`; precision/scale labels belong to the state type.

### B. Compatible forgetting / projection
Fine observations have canonical projections to coarse observations satisfying path coherence.

### C. Order-adjoint core where available
For root/quotient/collapse structures, retain the P008 embedding/right-adjoint core.

### D. Defect-enriched operations
Operations are not required to be strictly natural under projection. The finite failure of a commuting square is itself first-class mathematical data:

\[
D_f=\pi f-f\pi.
\]

### E. Coherence instead of artificial exactness
A multi-level precision system need not make every local defect zero; it must prove coherence between direct and staged routes.

### F. Proof layer
Use P018 ambiguity, predicate conflict, certificates, and adaptive precision to determine which details are genuinely proof-relevant.

### G. Time layer
Retain P010/P018-T44: precision refinement refines partitions, while deterministic forward time coarsens them. They share a finite-state partition skeleton, but no categorical duality is claimed at present.

The key package is therefore

\[
\boxed{
\text{finite state}
+\text{typed precision}
+\text{many-to-one projection}
+\text{exact defect}
+\text{coherence}
+\text{finite proof certificate}.
}
\]

This is closer than integer root alone to a framework capable of feeding back into the foundational logic, but it is not frozen.

---

## 15. Next falsifiable questions

### P018-Q63 — Which operation defects really form cocycles?
Addition carry is the standard 2-cocycle. Do not assume the answer for multiplication, powers, or collapse/refinement defects; find the right coefficient object and composition law, or give counterexamples showing that a uniform cocycle claim is too strong.

### P018-Q64 — What is the weakest structure for adjoint + algebra?
T63 is stated for ordered commutative monoids. Remove assumptions one at a time: where are commutativity, a unit, total addition, or antisymmetry actually needed? The target is a minimality result in the style of P008.

### P018-Q65 — Defect coherence on multi-path precision diamonds
P005 proves that pure projection around the gcd/lcm diamond commutes strictly. After operations are added, determine whether the four edge defects satisfy an exact diamond identity. This may be closer than the single-chain T67 to a genuine notion of precision curvature.

### P018-Q66 — Does defect curvature exist?
When two precision paths have the same projection endpoint but different defect decompositions, determine whether the transported difference always vanishes. If it does not, define and classify the finite path defect. Do not presuppose that it is literally curvature or a cohomology class.

### P018-Q67 — Can a global certificate advance P017?
Construct at least one nontrivial integer potential that simultaneously sees factor precision, carry shells, and half-scale dual correction. If it fails, exhibit the smallest counterexample and identify the missing state coordinate.

### P018-Q68 — Sufficient conditions for proof-safe representation switches
For a finite problem mapped by `F:X->Y` into an external mathematical representation, characterize minimal conditions under which a theorem in `Y` pulls back without ambiguity to `X`. Compare injective embeddings, predicate-complete quotients, and full equivalences.

---

## 16. Lean formalization priority

Recommended next formalization order:

1. T64: carry-gap identity for `Nat.div` / `Nat.mod`;
2. T65: carry cocycle identity;
3. T66: coarse/detail bijection `Phi_m` and twisted addition;
4. T67: two-level carry coherence;
5. T63: abstract ordered-additive-monoid + Galois-connection theorem.

The purpose of formalization is not to relabel the established carry cocycle as a project invention. It is to verify that its embedding into P005/P008/P018 is type-correct and does not contain mistakes in zero cases, degree, or projection direction.

---

## 17. Current conclusion

This stage does not add stronger axioms to P008 and does not delete any existing P012/P017/P018 route.

Its central structural result is

\[
\boxed{
\text{carry}
=\text{additive laxity gap of right-adjoint projection}
=\text{2-cocycle data required to reconstruct addition from coarse/detail coordinates}.
}
\]

This suggests that non-strict commutation caused by finite precision may be structure that foundational mathematics must retain rather than error that should be eliminated.

The main unifying direction to test next is

\[
\boxed{
\text{order adjunction}
\longrightarrow
\text{typed precision projection}
\longrightarrow
\text{exact operation defect}
\longrightarrow
\text{coherence}
\longrightarrow
\text{proof certificate / time dynamics}.
}
\]

It is now a candidate foundational skeleton, not a frozen new foundation.