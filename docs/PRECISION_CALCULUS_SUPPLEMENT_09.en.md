# P018 — Finite-Precision Proof Calculus: Supplement 09

Status: `ACTIVE RESEARCH NOTE`  
Scope: mixed-radix precision charts, radix-swap transitions, braid coherence, the detail structure of P005 diamonds, and the boundary of genuine precision curvature  
Depends on: P005, P009, P018-T02, T43, T63–T73  
Discipline: mixed-radix arithmetic, Euclidean decomposition, coordinate changes, and braid/coherence language all have mature prior art. This note studies their combination and foundational meaning inside the Enterprise Math finite-precision projection system; it does not claim those established structures as project inventions.

## 1. The question: P005 proves coarse diamonds commute, but what happens to detail?

P005 proves that whenever

\[
d\mid e\mid f,
\]

canonical coarse projection satisfies

\[
\pi_{f\to d}
=
\pi_{e\to d}\circ\pi_{f\to e}.
\]

More generally, the two coarse paths in a gcd/lcm precision diamond agree strictly at their common endpoint.

P018-T02 also proves that along one chain, a fine state decomposes uniquely into nested details.

This leaves a question that had not been isolated explicitly:

> When the same total precision difference can be decomposed through different factor orders, how are the pathwise detail coordinates related?

The correct answer is not that corresponding local details must be equal. They generally are not.

Instead, **different refinement paths provide different mixed-radix charts on the same finite detail fiber, and the charts are related by canonical, lossless, integer-only transition maps.**

---

## 2. P018-T74 — A two-level mixed-radix detail chart is a bijection

Status: `PROVED / ESTABLISHED ARITHMETIC`

Let `r,s>=1` and define the finite detail fiber

\[
D_n=\{0,1,\ldots,n-1\}.
\]

Every

\[
t\in D_{rs}
\]

has a unique representation

\[
\boxed{t=su+v,}
\]

where

\[
0\le u<r,
\qquad0\le v<s.
\]

Define the chart

\[
\boxed{
\chi_{r,s}:D_{rs}\to D_r\times D_s,
\qquad
\chi_{r,s}(t)=(t//s,t\bmod s).
}
\]

Its inverse is

\[
\boxed{
\chi_{r,s}^{-1}(u,v)=su+v.
}
\]

Hence

\[
\boxed{D_{rs}\cong D_r\times D_s}
\]

as finite sets.

No hidden true value is introduced: `D_(rs)` and `(u,v)` are two equivalent coordinate descriptions of the same explicit finite state.

---

## 3. P018-T75 — Radix swap is a canonical lossless coordinate change

Status: `PROVED`

The same `t in D_(rs)` can also be written in the opposite radix order as

\[
t=ru'+v',
\qquad0\le u'<s,
\qquad0\le v'<r.
\]

Define the chart transition

\[
\boxed{
\tau_{r,s}
=
\chi_{s,r}\circ\chi_{r,s}^{-1}.
}
\]

For `(u,v) in D_r x D_s`, this is

\[
\boxed{
\tau_{r,s}(u,v)
=
((su+v)//r,(su+v)\bmod r).
}
\]

It is a bijection and

\[
\boxed{
\tau_{s,r}\circ\tau_{r,s}
=\operatorname{id}_{D_r\times D_s}.
}
\]

### Meaning

Detail coordinates obtained along two refinement paths need not agree componentwise. What must be preserved is that:

1. both encode the same total detail;
2. the transition is invertible;
3. the transition introduces no continuous completion or hidden remainder.

Thus “preserving multiple routes” acquires a precise mathematical form:

\[
\boxed{
\text{one finite fiber}
+\text{multiple integer charts}
+\text{canonical chart transitions}.
}
\]

---

## 4. P018-T76 — Three-factor radix swaps satisfy braid coherence

Status: `PROVED`

Let `r,s,t>=1` and start from mixed-radix digits

\[
(a,b,c)\in D_r\times D_s\times D_t.
\]

Their encoded integer is

\[
\boxed{N=st\,a+t\,b+c,}
\]

with `0<=N<rst`.

To change the radix order from

\[
(r,s,t)
\]

to

\[
(t,s,r),
\]

there are two adjacent-swap paths:

\[
(r,s,t)
\to(s,r,t)
\to(s,t,r)
\to(t,s,r),
\]

and

\[
(r,s,t)
\to(r,t,s)
\to(t,r,s)
\to(t,s,r).
\]

Writing `tau` for adjacent radix swaps, one has strictly

\[
\boxed{
(\tau_{s,t}\times id_r)
\circ
(id_s\times\tau_{r,t})
\circ
(\tau_{r,s}\times id_t)
=
(id_t\times\tau_{r,s})
\circ
(\tau_{r,t}\times id_s)
\circ
(id_r\times\tau_{s,t}).
}
\]

### Proof

Every adjacent swap preserves the encoded integer `N` and changes only its coordinate description under a new radix order.

Both paths end in radix order `(t,s,r)` and therefore yield the unique mixed-radix representation of the same `N` in that final order. Repeated uniqueness of Euclidean decomposition proves equality. ∎

### Boundary

This has the form of a braid/coherence identity. The note does not claim mixed-radix swaps or braid relations as new inventions.

The project-specific use is to turn consistency among different precision-decomposition routes from an informal expectation into an exact chart-coherence condition.

---

## 5. P018-T77 — The P005 gcd/lcm diamond carries a canonical detail atlas

Status: `PROVED`

Consider the P005 scale diamond. Let

\[
g=\gcd(a,b),
\qquad
\ell=\operatorname{lcm}(a,b).
\]

Write

\[
a=gA,
\qquad b=gB.
\]

Classical integer identities give

\[
\gcd(A,B)=1,
\qquad
\ell=gAB.
\]

Fix a total detail for projection from precision `ell` to `g`:

\[
t\in D_{AB}.
\]

### Path one: `ell -> a -> g`

The successive ratios are `B` and `A`, giving chart

\[
\chi_{A,B}(t)
=(t//B,t\bmod B).
\]

### Path two: `ell -> b -> g`

The successive ratios are `A` and `B`, giving chart

\[
\chi_{B,A}(t)
=(t//A,t\bmod A).
\]

The two detail charts are canonically connected by

\[
\boxed{
\tau_{A,B}
=
\chi_{B,A}\circ\chi_{A,B}^{-1}.
}
\]

Thus the P005 diamond now has two distinct layers:

\[
\boxed{
\text{coarse coordinate: strictly commuting;}
}
\]

\[
\boxed{
\text{detail coordinate: not componentwise equal, but exactly linked by an invertible chart transition.}
}
\]

This preserves more information than forcing all routes to produce the same local detail coordinates.

---

## 6. P018-T78 — Additive carry is flat on a precision diamond

Status: `PROVED`

Fix `r,s>=1` and two total details

\[
t_1,t_2\in D_{rs}.
\]

Direct addition carry from product radix `rs` to the coarse level is

\[
\boxed{
K_{dir}
=\kappa_{rs}(t_1,t_2)
=\left\lfloor\frac{t_1+t_2}{rs}\right\rfloor.
}
\]

### Through the `(r,s)` chart

Write

\[
t_i=su_i+v_i,
\qquad u_i\in D_r,
\quad v_i\in D_s.
\]

First produce the inner carry

\[
c_s=\kappa_s(v_1,v_2),
\]

then transport it to the outer digit:

\[
K_{r,s}
=
\left\lfloor
\frac{u_1+u_2+c_s}{r}
\right\rfloor.
\]

P018-T67 gives

\[
K_{r,s}=K_{dir}.
\]

### Through the swapped `(s,r)` chart

Likewise,

\[
K_{s,r}=K_{dir}.
\]

Hence

\[
\boxed{
K_{r,s}=K_{s,r}=K_{dir}.
}
\]

The **location** of local carries may differ between the two routes, but once transported to the common endpoint by the correct chart/coherence law, the final defect is identical.

If additive diamond curvature is provisionally defined as the difference between the two canonically transported endpoint defects, then

\[
\boxed{\Omega_+(r,s;t_1,t_2)=0.}
\]

Addition therefore has nonzero local defect while the canonical precision connection remains flat.

This is an important negative result:

> **Nonzero defect does not imply nonzero curvature.**

---

## 7. P018-T79 — Path curvature of a canonical endpoint defect is automatically zero

Status: `PROVED STRUCTURAL BOUNDARY`

Consider a compatible precision system in which canonical projection from a finer level `lambda` to a coarser level `mu` depends only on the endpoints, so every composable projection path has the same composite

\[
\pi_{\lambda\to\mu}.
\]

Suppose an operation `F` is defined at both endpoints and define its endpoint defect by

\[
D_F^{\lambda:\mu}(x)
=
\pi^{out}_{\lambda\to\mu}(F_\lambda(x))
-
F_\mu(\pi^{in}_{\lambda\to\mu}(x)).
\]

Then `D_F^{lambda:mu}` itself depends only on the endpoints.

Therefore two paths with the same source and target, using only canonical projections, have zero endpoint-defect path difference.

### Proof

The composite projection along either path is, by assumption, the same endpoint projection. Substituting into the defect definition makes the two expressions identical. ∎

### What does this rule out?

One may not call a difference in local defect decomposition “precision curvature” merely because its coordinates differ. That may be only chart dependence.

### Where can genuine nonzero curvature / holonomy come from?

At least one additional path-dependent structure is required, such as:

1. **different intermediate operation scheduling**: collapse then project versus project then collapse;
2. **noncanonical lift / reconstruction**: different choices of representatives when returning from a coarse fiber to a fine level;
3. **path-dependent operations**: different local transitions on different scale paths;
4. **nontrivial transport rules**: moving a local defect is not just canonical endpoint projection.

This moves the genuine curvature question away from the pure P005 scale lattice and toward the typed nonconfluence already exposed by P009 and the noncommutation of operations and projections studied by P018.

---

## 8. Feedback into P009: the genuine holonomy candidate lies in operation scheduling, not pure scale

P009 already warns that erasing scale labels creates spurious dynamics and that different orders of operation/projection may produce different results.

T79 sharpens the boundary:

- **pure canonical scale refinement/coarsening**: flat; path changes only the detail chart;
- **after adding noncommuting operations**: genuine path effects may appear.

The next stage should therefore not add “curvature” as a primitive to the scale lattice itself.

A better object is an operation-labelled path consisting of

\[
\boxed{
\text{typed precision arrows}
+\text{operation events}
+\text{chart transitions}.
}
\]

One can then compare two paths with the same initial/final types but different operation orderings. If their outputs differ, study whether that difference is composable, localizable, invariant under legitimate chart changes, and capable of forming a genuine holonomy or obstruction.

---

## 9. A mathematical interpretation of “preserve all routes”

“Do not lose routes” can now become a research principle rather than only project-management advice.

For one finite object, if multiple routes satisfy:

1. each route has an explicit representation/chart;
2. verified transitions exist between charts;
3. transitions satisfy composition / braid coherence;
4. genuine conclusions are invariant under chart changes;

then the routes should be **kept in parallel** rather than prematurely deleting all but one “best representation.”

Only when two routes cannot even be related by such chart equivalence, or when they make irreconcilable verifiable predictions about the same structure, should they become genuine competitors.

This matches the defect-equivalence principle of Supplement 08:

\[
\boxed{
\text{route difference}\ne\text{structural difference}.
}
\]

Find the transition law first; only then decide whether there is a real conflict.

---

## 10. A fourth candidate layer for the foundational logic

Supplements 07–09 now suggest that the candidate foundation resembles a **finite-precision atlas system**, not merely a collection of integer operations.

### Layer 0 — Order-adjoint core

P008: partial order + embedding + right adjoint.

### Layer 1 — Defect-enriched operation core

Projection need not strictly preserve operations; retain exact defects and coherence.

### Layer 2 — Defect equivalence / obstruction

Retain representation changes, coboundary-like transformations, and strictification obstructions.

### Layer 3 — Precision atlas / path coherence

One finite detail fiber may carry many charts. Require canonical transitions, inverses, composition, and braid coherence, and distinguish:

- chart-dependent local data;
- chart-invariant endpoint data;
- genuine operation-induced path dependence.

The current candidate skeleton is therefore

\[
\boxed{
\text{typed finite states}
+\text{adjoint projections}
+\text{finite detail fibers}
+\text{chart atlas}
+\text{exact defects}
+\text{coherence}
+\text{obstruction classes}
+\text{proof/time layers}.
}
\]

It remains deliberately unfrozen.

---

## 11. Executable pressure tests

Added:

- `src/enterprise_math/precision_radix.py`
- `tests/test_precision_radix.py`

They use only integer arithmetic and exhaustively test small finite domains for:

1. split/join mixed-radix chart inversion;
2. inversion of `tau_(r,s)` by `tau_(s,r)`;
3. braid agreement of the two three-factor adjacent-swap paths;
4. equality of staged and direct product-radix carry;
5. equality of final carry on the two swapped diamond paths.

The computational checks are counterexample search and implementation verification, not substitutes for the proofs.

---

## 12. Next open questions

### P018-Q74 — Abstract finite precision atlas

Generalize `D_(rs) <-> D_r x D_s` beyond integers. How weak can the structure be while still supporting charts, transitions, and coherence?

### P018-Q75 — Lean formalization of radix braid

Formalize T74–T76, with particular emphasis on the parameterized adjacent-swap braid identity.

### P018-Q76 — Operation-scheduling holonomy

Choose the smallest existing noncommuting example, such as collapse versus projection, and construct two typed paths:

\[
\text{collapse}\to\text{project}
\qquad\text{versus}\qquad
\text{project}\to\text{collapse}.
\]

Define their exact path defect at a common endpoint and determine how it transforms under chart changes.

### P018-Q77 — Does holonomy satisfy a local composition law?

If Q76 gives a nonzero path effect, test whether it is additive/composable across concatenated diamonds or requires nonabelian transport.

### P018-Q78 — A P017 decomposition atlas

Try to organize P017 anchors, carry/shell, half-scale, and factor-precision representations as a chart family and search for transition laws. If no such laws exist, identify exactly which routes are describing genuinely different structures.

---

## 13. Current conclusion

The most important outcome of this stage is not another new term but the elimination of an attractive wrong turn:

\[
\boxed{
\text{pure canonical precision projection has no nonzero path curvature by itself.}
}
\]

Differences among refinement-path details should first be understood as mixed-radix chart changes. Those chart transitions are invertible and satisfy exact braid coherence.

Any genuinely nonzero path obstruction worth pursuing must therefore come from

\[
\boxed{
\text{operation/projection noncommutation}
\quad\text{or}\quad
\text{noncanonical lift/transport}.
}
\]

The foundational logic therefore becomes more focused:

> **Preserve multiple routes, but organize them as an atlas first. Only differences that survive legitimate chart transitions deserve promotion to genuine structural obstructions.**