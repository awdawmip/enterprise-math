# P005 — Multi-base scale algebra

Status: `PROVED-CONSTRUCTION`  
Open problem: `P005`  
Scope: discrete scale mathematics

## 1. Goal

The v0.1 notation

\[
R_{p,b,s}(n)=R_p\!\left(n b^{ps}\right)
\]

uses one integer base \(b\) and one level \(s\). P005 asks what happens when several integer scale bases coexist and when the order of scale conversion matters.

The clean answer is to separate **scale itself** from one particular base/level representation.

## 2. Scale factor as the primary coordinate

For positive integer scale factor \(d\ge1\), define

\[
S_{p,d}(n)=R_p\!\left(n d^p\right).
\]

The old notation is the special case

\[
R_{p,b,s}(n)=S_{p,b^s}(n).
\]

Thus `(base, level)` is an address for a scale factor, not the fundamental scale object.

For example,

\[
S_{p,4}(n)=R_{p,4,1}(n)=R_{p,2,2}(n).
\]

The two base/level descriptions denote exactly the same scale state.

## 3. The divisibility order of scales

Use positive integers as scale indices and order them by divisibility:

\[
d\preceq e\iff d\mid e.
\]

A larger element in this order is a finer integer scale factor.

If \(d\mid e\), write

\[
r=e/d
\]

and define the canonical projection from scale \(e\) to scale \(d\) by

\[
\pi_{e\to d}(m)=m\operatorname{//}r.
\]

This uses only explicit integer arithmetic.

## 4. Scale compatibility

### P005-T01 — General scale-factor compatibility

Status: `PROVED`

For \(p,d,e\ge1\) with \(d\mid e\),

\[
\pi_{e\to d}(S_{p,e}(n))=S_{p,d}(n).
\]

### Proof

Write \(e=dr\). Then

\[
S_{p,e}(n)=R_p\!\left(n d^p r^p\right).
\]

T015 gives

\[
R_p\!\left(n d^p r^p\right)\operatorname{//}r
=
R_p\!\left((n d^p r^p)\operatorname{//}r^p\right).
\]

Because \(r\ge1\), the division is exact:

\[
(n d^p r^p)\operatorname{//}r^p=n d^p.
\]

Hence

\[
\pi_{e\to d}(S_{p,e}(n))=R_p(nd^p)=S_{p,d}(n).
\]

∎

The original T010 is the special case \(d=b^s\), \(e=b^{s+1}\).

## 5. Projection paths are coherent

### P005-T02 — Projection composition law

Status: `PROVED`

If

\[
d\mid e\mid f,
\]

then

\[
\pi_{e\to d}\circ\pi_{f\to e}=
\pi_{f\to d}.
\]

### Proof

Write

\[
e=dr,
\qquad
f=es=drs.
\]

Then

\[
\pi_{e\to d}(\pi_{f\to e}(m))
=(m\operatorname{//}s)\operatorname{//}r
=m\operatorname{//}(sr)
=\pi_{f\to d}(m).
\]

This is the usual associativity law for positive natural-number floor division. ∎

Consequently every state family

\[
\{S_{p,d}(n):d\ge1\}
\]

is coherent under all canonical coarse-scale projections.

No infinite limit is needed for this statement.

## 6. Two bases commute canonically

Suppose the current scale factor is \(d\) and two refinement factors are \(a,b\ge1\).

Refining the scale index first by \(a\) and then by \(b\) gives

\[
dab.
\]

Reversing the order gives

\[
dba.
\]

Since integer multiplication is commutative,

\[
dab=dba.
\]

Therefore, when the underlying state \(n\) is retained and the scale state is evaluated by its definition,

\[
S_{p,dab}(n)=S_{p,dba}(n).
\]

### P005-T03 — Canonical multi-base refinement is order independent

Status: `PROVED`

Scale-index refinement by positive integer factors is commutative and associative. The resulting canonical scale state depends only on the product of the applied refinement factors, not their order.

Likewise, any sequence of canonical projections along a divisibility chain is path independent by P005-T02.

## 7. GCD and LCM give common scales

Positive integer scale factors form a divisibility lattice:

- the greatest common coarsening of \(d,e\) is

\[
g=\gcd(d,e);
\]

- the least common refinement is

\[
L=\operatorname{lcm}(d,e).
\]

Thus two incomparable scales do not need an arbitrary product as their first meeting point. Their canonical smallest common finer scale is \(L\).

The projection diamond

\[
S_{p,L}(n)
\longrightarrow S_{p,d}(n)
\longrightarrow S_{p,g}(n)
\]

and

\[
S_{p,L}(n)
\longrightarrow S_{p,e}(n)
\longrightarrow S_{p,g}(n)
\]

commutes by P005-T02.

### P005-T04 — Scale diamond coherence

Status: `PROVED`

All canonical projection paths between comparable scale factors give the same result. In particular, the gcd/lcm diamond for any pair of scales commutes.

This gives the multi-base scale family an inverse-system/projective-system structure over the positive integers ordered by divisibility, without requiring a continuum completion.

## 8. Refinement is not the inverse of projection

The previous results must not be misread as saying that a coarse integer state uniquely determines a finer one.

The projection

\[
\pi_{dr\to d}(m)=m\operatorname{//}r
\]

is many-to-one. Its full fiber over a coarse state \(k\) is

\[
\{kr,kr+1,\ldots,(k+1)r-1\}.
\]

So there is no canonical inverse map supplied by the scale algebra itself.

### P005-T05 — Criterion for a state-only refinement map

Status: `PROVED`

Fix two scales \(d\mid e\). A function

\[
U:\mathbb N\to\mathbb N
\]

satisfying

\[
U(S_{p,d}(n))=S_{p,e}(n)
\]

for every \(n\) exists if and only if the finer state is constant on every fiber of the coarse state map:

\[
S_{p,d}(n_1)=S_{p,d}(n_2)
\Longrightarrow
S_{p,e}(n_1)=S_{p,e}(n_2).
\]

### Proof

Necessity is immediate by applying \(U\) to equal coarse states.

For sufficiency, define \(U(k)\) on every coarse state \(k\) in the image of \(S_{p,d}\) to be the common finer value on that fiber; extend \(U\) arbitrarily outside the image. The fiber-constancy assumption makes the definition well-defined. ∎

## 9. Explicit failure of unique refinement

### P005-CE01 — One coarse state can have different canonical finer states

Take square root, coarse scale \(d=1\), and finer scale \(e=10\).

For \(n=2\),

\[
S_{2,1}(2)=R_2(2)=1,
\]

while

\[
S_{2,10}(2)=R_2(200)=14.
\]

For \(n=3\),

\[
S_{2,1}(3)=R_2(3)=1,
\]

but

\[
S_{2,10}(3)=R_2(300)=17.
\]

Thus the same coarse state `1` must refine to both `14` and `17` depending on which underlying integer state generated it.

Therefore no state-only function \(U\) can satisfy

\[
U(S_{2,1}(n))=S_{2,10}(n)
\]

for all \(n\).

This is not numerical error. It is the exact mathematical consequence of many-to-one coarse projection.

## 10. When does order matter?

P005 can now answer this precisely.

### Canonical operations — order does not matter

Order is irrelevant when:

1. scale factors are refined by multiplication while the underlying state \(n\) is retained;
2. a target scale state is recomputed directly from \(S_{p,d}(n)=R_p(nd^p)\);
3. states are projected only toward coarser comparable scales by the canonical maps \(\pi\).

These operations obey exact commutative/associative laws.

### Attempted inverse refinement — path dependence can enter

If only the current coarse integer root state is retained, no canonical finer state is determined in general. Any procedure that chooses one element of a projection fiber is adding extra information or an extra convention.

Different lift conventions, or different sequences of such noncanonical lifts, are not protected by the projection coherence theorems and can be path dependent.

So scale-order dependence is **not** intrinsic to the canonical multi-base scale algebra. It arises when one tries to invert information that a many-to-one projection has already discarded.

## 11. First-stage resolution of P005

The resulting construction is:

\[
\boxed{
\text{scale index }d\in\mathbb N_{>0},
\quad
S_{p,d}(n)=R_p(nd^p),
\quad
\pi_{e\to d}(m)=m//(e/d)	ext{ for }d\mid e
}
\]

with:

- divisibility as the scale order;
- gcd as common coarsening;
- lcm as least common refinement;
- exact path-independent projection;
- base/level notation as a representation of the total scale factor;
- no canonical inverse refinement from a collapsed coarse state alone.

This resolves the mathematical construction requested by P005 without introducing rational numbers, real-number limits, or hidden fractional state.

## 12. Physical/foundational boundary

The scale algebra above is ordinary discrete mathematics. The further claim that physical nature has a maximum available scale factor, or that a coarse state literally destroys rather than hides finer information, belongs to the project's foundational/physical interpretation and is not proved by P005.

No \(d\to\infty\) limit is required or introduced here.

## 13. Prior-art discipline

Divisibility lattices, gcd/lcm, coherent inverse/projective systems, and floor division are established mathematics. P005 combines these ordinary tools with the Enterprise Math integer-root scale state.

A targeted search during this pass did not identify this exact integer-root scale system as a standard named construction. That absence is not a priority result. The construction is therefore project-defined, its stated compatibility theorems are `PROVED`, and historical novelty remains `NOVELTY_UNVERIFIED`.
