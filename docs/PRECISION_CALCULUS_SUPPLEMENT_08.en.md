# P018 — Finite-Precision Proof Calculus: Supplement 08

Status: `ACTIVE RESEARCH NOTE`  
Scope: operation defects of adjoint projection, the carry cocycle, signed extension obstruction, mixed-radix precision atlases, and the boundary of path flatness  
Depends on: P005, P006, P008, P009, and P018 stages 1–8 (mainline T001–T70)  
Discipline: group extensions, 2-cocycles, coboundaries, adjunctions, mixed-radix arithmetic, and braid/coherence all have mature prior art. This note studies their exact interface with Enterprise Math finite-precision semantics and does not claim those established structures themselves as project inventions.

## 1. Why this stage is not a separate research branch

P018 already proves that precision projection is not an error bar around a hidden real-valued truth. It is a many-to-one map between explicit finite states. P008 also proves that the integer scale embedding

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

Carry, borrow, multiplication carry, and power carry have already been treated as exact integer events in cross-precision operations.

This stage asks a more foundational question:

> When projection and an operation fail to commute strictly, is that failure an accidental arithmetic effect, a coordinate artifact, or structure that cannot be removed by any legitimate representation change?

The answer naturally separates into four layers:

1. operation defect;
2. defect coherence;
3. representation change / obstruction;
4. multi-path precision atlas.

The development preserves all existing P005/P006/P008/P009/P012/P017/P018 routes rather than replacing them with new vocabulary.

---

## 2. P018-T71 — An additive left adjoint makes its right adjoint superadditive

Status: `PROVED / ESTABLISHED ORDER-THEORETIC PATTERN`

Let `A,B` be ordered commutative monoids with monotone addition. Suppose

\[
l:A\to B
\]

strictly preserves addition and has a right adjoint

\[
l\dashv u.
\]

Then for every `x,y in B`,

\[
\boxed{u(x)+u(y)\le u(x+y).}
\]

### Proof

By the adjunction counit,

\[
l(u(x))\le x,
\qquad
l(u(y))\le y.
\]

Hence

\[
l(u(x)+u(y))
=l(u(x))+l(u(y))
\le x+y.
\]

Using

\[
l(a)\le b\iff a\le u(b)
\]

gives the result. ∎

Taking `l=L_r` and `u=Q_r` yields immediately

\[
\boxed{Q_r(x)+Q_r(y)\le Q_r(x+y).}
\]

Thus superadditivity of integer floor projection is not an isolated trick. It is forced by the P008 adjunction once addition is present.

---

## 3. P018-T72 — Carry is the exact additive defect of right-adjoint projection

Status: `PROVED`

Fix `m>=1` and define

\[
Q_m(x)=x//m,
\qquad
\delta_m(x)=x\bmod m.
\]

Write

\[
x=ma+u,
\qquad y=mb+v,
\qquad0\le u,v<m.
\]

Define

\[
\boxed{
\kappa_m(u,v)
=\left\lfloor\frac{u+v}{m}\right\rfloor
\in\{0,1\}.
}
\]

Then

\[
\boxed{
Q_m(x+y)-Q_m(x)-Q_m(y)
=\kappa_m(u,v).
}
\]

Carry is therefore not an approximation error. It is the **entire integer gap** between coarse projection and an additive homomorphism.

For a degree-`q` precision object, replacing `m` by `r^q` gives the same result.

---

## 4. P018-T73 — Standard carry satisfies the normalized 2-cocycle identity

Status: `PROVED / PRIOR-ART INSTANCE`

Let

\[
D_m=\{0,1,\ldots,m-1\},
\qquad
u\oplus v=(u+v)\bmod m.
\]

Then

\[
\boxed{
\kappa_m(u,v)
+
\kappa_m(u\oplus v,w)
=
\kappa_m(v,w)
+
\kappa_m(u,v\oplus w).
}
\]

Also,

\[
\kappa_m(0,u)=\kappa_m(u,0)=0,
\qquad
\kappa_m(u,v)=\kappa_m(v,u).
\]

### Proof

Perform Euclidean decomposition of `u+v+w` once as `(u+v)+w` and once as `u+(v+w)`. The final remainders modulo `m` agree by associativity of modular addition, and uniqueness of Euclidean decomposition forces equality of the coarse coefficients. ∎

### Prior-art boundary

The connection between carrying and 2-cocycles / group extensions is established mathematics. Daniel C. Isaksen's *A Cohomological Viewpoint on Elementary School Arithmetic* (American Mathematical Monthly, 2002, DOI `10.1080/00029890.2002.11919915`) explicitly discusses this viewpoint.

Enterprise Math therefore does not claim “carry is a cocycle” as original. The project question is which broader precision defects become controllable when that established structure is combined with the P005/P008/P018 finite-precision ontology.

---

## 5. P018-T74 — Coarse + detail + carry exactly reconstruct natural-number addition

Status: `PROVED`

Define

\[
\Phi_m:\mathbb N\to\mathbb N\times D_m,
\qquad
\Phi_m(x)=(Q_m(x),\delta_m(x)).
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
\boxed{
\Phi_m(x+y)=\Phi_m(x)\boxplus\Phi_m(y).
}
\]

Hence

\[
\boxed{
(\mathbb N,+)
\cong
(\mathbb N\times D_m,\boxplus).
}
\]

Associativity of `boxplus` is exactly guaranteed by the cocycle identity in T73.

Thus if the foundation decomposes a state into coarse/detail layers, carry is not implementation noise. Removing it changes the additive algebra itself.

---

## 6. P018-C08 — Forcing coarse projection to be a strict additive homomorphism loses structure

Status: `COUNTEREXAMPLE / DESIGN WARNING`

For any `m>1`, let

\[
x=1,
\qquad y=m-1.
\]

Then

\[
Q_m(x)=Q_m(y)=0,
\]

but

\[
Q_m(x+y)=Q_m(m)=1.
\]

Therefore

\[
\boxed{Q_m(x+y)\ne Q_m(x)+Q_m(y).}
\]

A future precision algebra must not impose “every coarse projection strictly preserves every operation” as an axiom. The correct direction is to retain the defect and study its coherence and eliminability.

---

## 7. P018-T75 — Carry coherence along a two-level precision chain

Status: `PROVED`

Consider two successive ratios `r,s>=1`. For a degree-`q` object write

\[
R=r^q,
\qquad S=s^q.
\]

Write each total detail as

\[
t_i=S u_i+v_i,
\qquad0\le u_i<R,
\qquad0\le v_i<S.
\]

Define the lower carry

\[
c_S=\kappa_S(v_1,v_2).
\]

Then the direct carry across total ratio `RS` satisfies

\[
\boxed{
\kappa_{RS}(t_1,t_2)
=
\left\lfloor
\frac{u_1+u_2+c_S}{R}
\right\rfloor.
}
\]

The total remainder satisfies

\[
\boxed{
(t_1+t_2)\bmod(RS)
=
S((u_1+u_2+c_S)\bmod R)
+((v_1+v_2)\bmod S).
}
\]

Direct and staged coarsening therefore do not conflict. A lower-level carry is transported as an explicit integer input to the next level, which then decides whether another boundary is crossed.

---

## 8. P018-T76 — Signed Euclidean precision decomposition

Status: `PROVED / ESTABLISHED`

Fix `m>=1`. For every

\[
z\in\mathbb Z
\]

there exist unique

\[
q_m(z)\in\mathbb Z,
\qquad
\rho_m(z)\in D_m
\]

such that

\[
\boxed{z=mq_m(z)+\rho_m(z).}
\]

Here the quotient is the Euclidean/floor quotient paired with a nonnegative canonical remainder, not truncation toward zero.

This matches the P006 discipline: signed-state order and quotient conventions must be explicit mathematical choices rather than programming-language defaults.

This construction is independent of P006's `orderRootOdd`, `magnitudeRoot`, and `signedMagnitudeCollapse`; it does not revise those results.

---

## 9. P018-T77 — The same carry controls signed additive defect

Status: `PROVED`

For `x,y in Z`, write

\[
x=mq_x+r_x,
\qquad y=mq_y+r_y,
\qquad0\le r_x,r_y<m.
\]

Then

\[
\boxed{
q_m(x+y)
=q_m(x)+q_m(y)+\kappa_m(r_x,r_y),
}
\]

and

\[
\boxed{
\rho_m(x+y)
=(r_x+r_y)\bmod m.
}
\]

The carry defect is therefore not an artifact of the boundary of `N`; under the correct signed quotient it extends unchanged to `Z`.

---

## 10. P018-T78 — Coarse/detail/carry on `Z` forms a twisted group

Status: `PROVED`

Define

\[
\Phi_m^{\mathbb Z}(z)
=(q_m(z),\rho_m(z))
\]

and continue to use

\[
(a,u)\boxplus(b,v)
=\bigl(a+b+\kappa_m(u,v),(u+v)\bmod m\bigr).
\]

Then

\[
\boxed{
(\mathbb Z,+)
\cong
(\mathbb Z\times D_m,\boxplus)
}
\]

as groups.

Inverses are explicit:

\[
-(a,0)=(-a,0),
\]

while for `0<u<m`,

\[
\boxed{-(a,u)=(-a-1,m-u).}
\]

Since `u+(m-u)=m`, exactly one carry cancels the additional `-1` in the coarse coordinate.

Carry and borrow therefore belong to one signed extension algebra rather than being separate numerical errors.

---

## 11. P018-T79 — Carry is the section defect of the standard residue extension

Status: `PROVED / ESTABLISHED EXTENSION-THEORY INSTANCE`

Consider the short exact sequence

\[
\boxed{
0
\longrightarrow\mathbb Z
\xrightarrow{\times m}
\mathbb Z
\xrightarrow{\rho}
\mathbb Z/m\mathbb Z
\longrightarrow0.
}
\]

Choose the standard section

\[
s([u])=u,
\qquad0\le u<m.
\]

The section is generally not a group homomorphism, and

\[
\boxed{
s(u)+s(v)-s(u+v)
=m\kappa_m(u,v).
}
\]

Hence

\[
\boxed{
\kappa_m(u,v)
=
\frac{s(u)+s(v)-s(u+v)}{m}.
}
\]

The cohomological meaning of carry is therefore the kernel coordinate of the failure of a chosen detail-representative section to preserve the group operation.

---

## 12. P018-T80 — Changing section changes carry only by a coboundary

Status: `PROVED / PRIOR-ART COHOMOLOGY PATTERN`

Suppose another section has the form

\[
s'(u)=s(u)+m h(u).
\]

Its defect

\[
\kappa'_m(u,v)
=
\frac{s'(u)+s'(v)-s'(u+v)}{m}
\]

satisfies

\[
\boxed{
\kappa'_m(u,v)
=
\kappa_m(u,v)
+h(u)+h(v)-h(u+v).
}
\]

A concrete carry table can therefore depend on representation, while legitimate representation changes obey an exact transformation law.

Precision-defect research must henceforth distinguish:

1. coordinate-dependent defect;
2. change-of-representation law;
3. representation-invariant obstruction.

---

## 13. P018-T81 — For `m>1`, the carry obstruction cannot be globally strictified

Status: `PROVED / ESTABLISHED GROUP-THEORETIC CONSEQUENCE`

For `m>1`,

\[
0\to\mathbb Z\xrightarrow{\times m}\mathbb Z\to\mathbb Z/m\mathbb Z\to0
\]

does not split.

### Elementary proof

If it split, there would be a group-homomorphic section

\[
s:\mathbb Z/m\mathbb Z\to\mathbb Z.
\]

Then `s(1)` would have order `m` in the additive group `Z`. But `Z` is torsion-free, so no nonzero element has finite order. Contradiction. ∎

Thus no choice of representatives can make the carry cocycle identically zero:

\[
\boxed{
\text{carry may change coordinates, but it cannot be eliminated globally.}
}
\]

This yields a strong foundational filter:

> Before promoting a precision defect into the foundation, ask whether it can be strictified under all legitimate representation changes. If it cannot, identify the actual obstruction class rather than treating the defect as numerical noise.

---

## 14. P018-T82 — A two-level mixed-radix detail chart is a bijection

Status: `PROVED / ESTABLISHED ARITHMETIC`

Define

\[
D_n=\{0,1,\ldots,n-1\}.
\]

For `r,s>=1` and `t in D_(rs)`, uniquely

\[
\boxed{t=su+v,}
\qquad
u\in D_r,
\quad v\in D_s.
\]

Hence

\[
\boxed{
\chi_{r,s}:D_{rs}\to D_r\times D_s,
\qquad
\chi_{r,s}(t)=(t//s,t\bmod s)
}
\]

is a bijection with inverse

\[
\boxed{
\chi_{r,s}^{-1}(u,v)=su+v.
}
\]

This introduces no hidden value. `D_(rs)` and `(u,v)` are two coordinate descriptions of the same explicit finite detail state.

---

## 15. P018-T83 — Radix swap is a canonical lossless chart transition

Status: `PROVED`

The same `t` can be written in the reversed radix order as

\[
t=ru'+v',
\qquad u'\in D_s,
\quad v'\in D_r.
\]

Define

\[
\boxed{
\tau_{r,s}
=
\chi_{s,r}\circ\chi_{r,s}^{-1}.
}
\]

Then

\[
\boxed{
\tau_{r,s}(u,v)
=
((su+v)//r,(su+v)\bmod r).
}
\]

Moreover,

\[
\boxed{
\tau_{s,r}\circ\tau_{r,s}=id.
}
\]

Detail coordinates from two refinement routes need not agree componentwise. They may instead be different integer charts on the same finite fiber, provided the transition is exact and invertible.

---

## 16. P018-T84 — Three-factor radix swaps satisfy braid coherence

Status: `PROVED`

For

\[
(a,b,c)\in D_r\times D_s\times D_t,
\]

define the encoded integer

\[
\boxed{N=st\,a+t\,b+c.}
\]

Changing the radix order from `(r,s,t)` to `(t,s,r)` can be done by two adjacent-swap paths:

\[
(r,s,t)
\to(s,r,t)
\to(s,t,r)
\to(t,s,r),
\]

or

\[
(r,s,t)
\to(r,t,s)
\to(t,r,s)
\to(t,s,r).
\]

Strictly,

\[
\boxed{
(\tau_{s,t}\times id_r)
\circ(id_s\times\tau_{r,t})
\circ(\tau_{r,s}\times id_t)
=
(id_t\times\tau_{r,s})
\circ(\tau_{r,t}\times id_s)
\circ(id_r\times\tau_{s,t}).
}
\]

Each swap preserves `N`, and both paths end in the same radix order. Uniqueness of mixed-radix representation therefore forces the same final coordinates. ∎

This turns compatibility among different precision-decomposition routes into an exact chart-coherence law.

---

## 17. P018-T85 — The P005 gcd/lcm diamond has a canonical detail atlas

Status: `PROVED`

Let

\[
g=\gcd(a,b),
\qquad
\ell=\operatorname{lcm}(a,b),
\]

and write

\[
a=gA,
\qquad b=gB.
\]

Then

\[
\gcd(A,B)=1,
\qquad
\ell=gAB.
\]

Fix a total detail from `ell` to `g`:

\[
t\in D_{AB}.
\]

The path

\[
\ell\to a\to g
\]

gives chart

\[
\chi_{A,B}(t)=(t//B,t\bmod B),
\]

while

\[
\ell\to b\to g
\]

gives

\[
\chi_{B,A}(t)=(t//A,t\bmod A).
\]

The charts are canonically related by

\[
\boxed{
\tau_{A,B}
=
\chi_{B,A}\circ\chi_{A,B}^{-1}.
}
\]

The P005 diamond therefore has two levels:

\[
\boxed{\text{coarse coordinates commute strictly;}}
\]

\[
\boxed{\text{detail coordinates may differ but are linked by an exact invertible chart transition.}}
\]

---

## 18. P018-T86 — Additive carry is flat on a canonical precision diamond

Status: `PROVED`

Fix `r,s>=1` and

\[
t_1,t_2\in D_{rs}.
\]

The direct product-radix carry is

\[
\boxed{
K_{dir}
=\kappa_{rs}(t_1,t_2)
=\left\lfloor\frac{t_1+t_2}{rs}\right\rfloor.
}
\]

In the `(r,s)` chart write

\[
t_i=su_i+v_i.
\]

First form

\[
c_s=\kappa_s(v_1,v_2),
\]

then

\[
K_{r,s}
=
\left\lfloor
\frac{u_1+u_2+c_s}{r}
\right\rfloor.
\]

By T75,

\[
K_{r,s}=K_{dir}.
\]

The swapped `(s,r)` chart likewise gives

\[
K_{s,r}=K_{dir}.
\]

Hence

\[
\boxed{K_{r,s}=K_{s,r}=K_{dir}.}
\]

The **location** of local carry events may differ by route, but after correct transport to the common endpoint the defect is identical.

Thus

\[
\boxed{\text{nonzero defect}\not\Rightarrow\text{nonzero path curvature}.}
\]

---

## 19. P018-T87 — Path curvature of a canonical endpoint defect is automatically zero

Status: `PROVED STRUCTURAL BOUNDARY`

Consider a compatible precision system whose canonical projection depends only on source and target, so every projection path from `lambda` to `mu` composes to the same

\[
\pi_{\lambda\to\mu}.
\]

Suppose an operation `F` is defined at both endpoints and define

\[
D_F^{\lambda:\mu}(x)
=
\pi^{out}_{\lambda\to\mu}(F_\lambda(x))
-
F_\mu(\pi^{in}_{\lambda\to\mu}(x)).
\]

Then `D_F^(lambda:mu)` itself depends only on the endpoints.

Therefore two paths with the same source and target that use only canonical projections have zero endpoint-defect path difference.

### Consequence

A difference between local defect decompositions cannot by itself be called “precision curvature.” It may be only chart dependence.

Genuinely nonzero holonomy/path obstruction requires additional path-dependent structure, for example:

1. different intermediate operation ordering, such as collapse→project versus project→collapse;
2. noncanonical lift/reconstruction;
3. operations that vary with path;
4. a nontrivial defect-transport rule.

This moves the genuine path-dependence problem away from the pure P005 scale lattice and toward the typed nonconfluence already exposed by P009 and the operation/projection noncommutation studied in P018.

---

## 20. Feedback into P008: the foundation should grow by justified layers

The proved P008 core remains unchanged:

\[
\boxed{
\text{partial order}
+\text{order embedding}
+\text{right adjoint}
}
\]

is enough for the current root / quotient / collapse core.

Only when an operation is needed do we add

\[
\boxed{
\text{typed operation}
+\text{precision projection}
+\text{exact defect}
+\text{coherence}.
}
\]

Only when representation dependence itself matters do we further add

\[
\boxed{
\text{representation change}
+\text{defect transformation law}
+\text{strictification obstruction}.
}
\]

No stronger structure is forced back into P008 prematurely.

---

## 21. Feedback into P006/P009: signed semantics and typed paths must remain explicit

The distinct signed-root semantics of P006 remain distinct. Euclidean signed quotient is an independent coordinate layer.

P009 scale labels also cannot be erased, because carry coherence depends on the actual ratio, radix charts depend on factor order, and genuine path effects depend on the typed scale at which an operation event occurs.

A reasonable state must retain at least `(scale, value, degree)` or equivalent type information.

---

## 22. Feedback into P012: retain primitive graph geometry and add representation-invariant derived geometry

P012 already proves that shortest-path natural-number distance generated by primitive adjacency can form an intrinsic integer metric. That remains the stable baseline.

In parallel, investigate:

1. fiber/quotient geometry;
2. exact lattice lifts as proof representations;
3. chart-change invariance of derived geometry.

Any proposed distance must still prove the metric axioms. Integer-valuedness alone does not make a function geometrically valid.

---

## 23. Feedback into P017: keep every local route while searching for a global invariant certificate

P017 involution, carry, shell, half-scale, factor-precision, and threshold-complex routes are all retained.

The new question is whether different decompositions, anchors, or precision axes form a chart family. If so, search for:

- change-of-chart laws;
- boundary/coboundary corrections;
- chart-invariant total certificates;
- genuine obstructions that cannot be strictified.

Termwise positivity is therefore no longer required as a default goal. A negative local shell may be only a decomposition artifact in one representation.

---

## 24. Formal discipline for representation switches

Allow

\[
\boxed{
\text{finite-state problem}
\xrightarrow{\text{faithful representation}}
\text{external mathematical language}
\xrightarrow{\text{proof}}
\text{finite-state theorem}.
}
\]

Group cohomology, category/adjunction theory, algebraic geometry, harmonic/spectral methods, convex duality, topology, lattice/coding theory, and analysis may all serve as proof languages, provided that:

1. the representation map is explicit;
2. the required faithful/injective/equivalence property is proved;
3. the result translates back to the original finite state;
4. a continuum used inside the proof space is not silently promoted to the ontology of nature.

---

## 25. Candidate foundational skeleton: Defect-Enriched Precision Atlas

Status: `RESEARCH SYNTHESIS / NOT FROZEN`

The current minimal candidate layering is:

### Layer 0 — Order-adjoint core

Order, embedding, right adjoint, interior/collapse.

### Layer 1 — Defect-enriched operations

Operations need not commute strictly with projection. Retain exact finite defects and composition/coherence laws.

### Layer 2 — Defect equivalence / obstruction

Distinguish coordinate-dependent defects, legitimate representation changes, coboundary-like transformations, and obstructions that cannot be strictified.

### Layer 3 — Precision atlas / path coherence

One finite detail fiber may carry multiple charts. Require invertible transitions and composition/braid coherence, and distinguish chart dependence from genuine operation-induced path dependence.

### Layer 4 — Proof/time layers

Continue to connect P018 predicate certificates/adaptive precision and P010/P018 time-partition coarsening. No categorical duality between time and precision is claimed yet.

The current candidate skeleton is therefore

\[
\boxed{
\text{typed finite states}
+\text{adjoint projections}
+\text{finite detail fibers}
+\text{precision atlas}
+\text{exact defects}
+\text{coherence}
+\text{obstructions}
+\text{proof/time layers}.
}
\]

It remains deliberately unfrozen.

---

## 26. Executable pressure tests and formalization entry points

This stage adds or plans to connect:

- `EnterpriseMath/Precision/Carry.lean`
- `src/enterprise_math/precision_radix.py`
- `tests/test_precision_radix.py`

Lean first targets:

1. T72 additive carry defect;
2. T73 carry cocycle;
3. later T74/T75 and T82–T84.

Small finite-domain Python tests exhaustively check:

1. mixed-radix split/join inversion;
2. radix-swap inversion;
3. agreement of the two three-factor braid paths;
4. staged carry = direct product-radix carry;
5. equality of endpoint carry on swapped diamond paths.

Computation is used for counterexample search and implementation validation, not as a replacement for proof.

---

## 27. Next open questions

### P018-Q79 — Which operation defects really form cocycles?

Addition does. Do not assume the answer for multiplication, powers, or collapse/refinement defects; find the correct coefficient object or explicit counterexamples.

### P018-Q80 — Weakest adjoint + operation structure

Continue weakening T71 to determine which assumptions—commutativity, a unit, total addition, antisymmetry—are genuinely necessary.

### P018-Q81 — Lean formalization of signed carry

First verify mathlib's canonical integer Euclidean-division convention, then formalize T76–T81.

### P018-Q82 — Abstract minimal structure for a finite precision atlas

Generalize `D_(rs) <-> D_r x D_s` beyond the integer case without assuming a multiplicative integer factorization in advance.

### P018-Q83 — Lean formalization of radix braid

Formalize T82–T84.

### P018-Q84 — Operation-scheduling holonomy

Start from the smallest noncommuting example: compare collapse→project and project→collapse at a common typed endpoint, define the exact path effect, and derive its chart-change law.

### P018-Q85 — Feed a global certificate back into P017

Try to organize carry, Möbius shell, half-scale, and factor-precision decompositions as an atlas. If that fails, identify exactly which routes are not coordinate changes but genuinely different structures.

---

## 28. Current conclusion

The central continuous chain of this stage is not a single formula but

\[
\boxed{
\text{right-adjoint laxity}
\to
\text{exact carry defect}
\to
\text{2-cocycle coherence}
\to
\text{section/coboundary change}
\to
\text{nonsplitting obstruction}
\to
\text{mixed-radix atlas}
\to
\text{path-flatness boundary}.
}
\]

This suggests a more natural foundational principle than “all operations should commute strictly”:

> **A finite-precision foundation need not eliminate defects. It should retain them, control how they change under representation, and promote only differences that survive all legitimate chart changes to genuine structural status.**

At the same time we obtain a useful negative result:

\[
\boxed{
\text{pure canonical precision projection is path-flat by itself.}
}
\]

Any genuinely nonzero holonomy worth studying must therefore arise from operation/projection noncommutation, noncanonical lifts, or another genuine path-dependent structure, not merely from different routes producing different local coordinates.