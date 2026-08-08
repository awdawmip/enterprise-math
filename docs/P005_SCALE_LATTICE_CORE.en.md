# P005 — Total-factor scale lattice core

Status: `PROVED STRUCTURAL RESOLUTION`

## 1. Replace `(base, level)` by one total scale factor

For a positive integer total scale factor

\[
d\in\mathbb N_{>0},
\]

define

\[
S_{p,d}(n)=R_p(nd^p).
\]

The old `(base, level)` notation is only one representation of the same factor:

\[
d=b^s.
\]

Hence, for example, `(4,1)` and `(2,2)` denote the same scale factor `4` and therefore the same scaled root state.

This removes an artificial distinction between different factorisations of one scale.

## 2. Canonical projection along divisibility

If

\[
d\mid e,
\]

write

\[
r=e/d.
\]

Define the projection from the finer scale `e` to the coarser scale `d` by

\[
\pi_{e\to d}(m)=m//r.
\]

This is a typed scale projection: the input coordinate lives at scale `e` and the output coordinate lives at scale `d`.

## 3. P005-T01 — General scale compatibility

Status: `PROVED`

For positive `p,d,e` with `d|e`,

\[
\boxed{
\pi_{e\to d}(S_{p,e}(n))=S_{p,d}(n).
}
\]

### Proof

Let `e=dr`. The P008/P014 root-division interchange gives

\[
R_p(N)//r=R_p(N//r^p).
\]

Apply this to

\[
N=ne^p=n(dr)^p=nd^pr^p.
\]

Exact integer division by `r^p` leaves `nd^p`, so

\[
R_p(ne^p)//r=R_p(nd^p).
\]

No real-valued limit is used. ∎

The original v0.1 base/level law is the special case

\[
e=b^{s+1},\qquad d=b^s.
\]

## 4. P005-T02 — Projection composition is path independent

Status: `PROVED`

If

\[
d\mid e\mid f,
\]

then

\[
\boxed{
\pi_{e\to d}\circ\pi_{f\to e}
=
\pi_{f\to d}.
}
\]

Indeed, if `e=da` and `f=eb=dab`, then

\[
(m//b)//a=m//(ab).
\]

Thus the coordinate obtained at one fixed target scale is independent of how the projection ratio is factored into intermediate scales.

## 5. Divisibility is the scale order

Order scale factors by divisibility:

\[
d\preceq e
\iff
d\mid e.
\]

Then `d` is coarser and `e` is finer.

For two positive scale factors `a,b`:

- the greatest common coarsening is
  \[
  \gcd(a,b);
  \]
- the least common refinement is
  \[
  \operatorname{lcm}(a,b).
  \]

Therefore positive integer scale factors form the standard divisibility lattice.

This lattice is established mathematics; Enterprise Math does not claim it as new.

## 6. P005-T03 — The gcd/lcm projection diamond commutes

Status: `PROVED`

Let

\[
g=\gcd(a,b),
\qquad
\ell=\operatorname{lcm}(a,b).
\]

Then `g|a|ell` and `g|b|ell`, and the two projection paths

\[
\ell\to a\to g
\]

and

\[
\ell\to b\to g
\]

produce exactly the same coordinate as the direct projection

\[
\ell\to g.
\]

This follows immediately from P005-T02.

## 7. Multi-base refinement is representation-independent

Suppose one researcher refines by base `a` and another by base `b`. If both paths retain the underlying state `n`, then the final scaled root depends only on the product total factor.

For example, applying refinements by factors `a` then `b` gives

\[
S_{p,ab}(n),
\]

which is the same scale as refining by `b` then `a`.

Thus factor multiplication is commutative/associative at the scale-index level.

The important distinction is between:

- **recomputing from retained underlying state `n`**, which is canonical; and
- **trying to invert a many-to-one coarse root coordinate alone**, which is not.

## 8. P005-C01 — Coarse root coordinates do not determine unique fine coordinates

Status: `COUNTEREXAMPLE`

Take square root (`p=2`) with coarse scale factor `1` and finer scale factor `10`.

At the coarse scale,

\[
S_{2,1}(2)=1,
\qquad
S_{2,1}(3)=1.
\]

The same coarse coordinate `1` therefore represents at least two distinct underlying states.

At the finer scale,

\[
S_{2,10}(2)=R_2(200)=14,
\]

while

\[
S_{2,10}(3)=R_2(300)=17.
\]

Hence no state-only function

\[
\rho:X_1\to X_{10}
\]

can reconstruct both correct fine states from the single coarse root coordinate `1`.

Refinement is therefore not the inverse of projection unless additional information is retained.

## 9. Where path dependence can actually enter

Canonical projection to a fixed coarser target is path independent.

Path dependence can enter only after adding extra noncanonical structure, for example:

- choosing one fine-state lift from a projection fiber;
- discarding the underlying source state and later guessing a refinement;
- mixing scale projections with other noncommuting collapse operations without an interchange theorem.

These are not defects of the scale lattice. They are consequences of adding choices after information has already been collapsed.

## 10. P005 status

P005 is structurally resolved at the minimal scale-algebra level:

- use one positive total scale factor `d`;
- use divisibility as the scale order;
- use exact floor-division projections from finer to coarser comparable scales;
- use gcd/lcm as common coarsening/refinement;
- projection paths to the same target commute;
- no canonical inverse refinement exists from a coarse root coordinate alone.

More elaborate refinement policies or mixed collapse/scale normal forms belong to P009, not to the minimal scale algebra itself.

## 11. Prior-art discipline

Divisibility lattices, gcd/lcm, integer floor division and projective-system language are established mathematics. P008/P014 already connect root and division through standard Galois-adjoint structure.

Enterprise Math's project-specific contribution is the finite-scale semantics and the explicit separation between canonical projection/recomputation and noncanonical inverse lifting. Historical novelty of the integrated packaging remains `NOVELTY_UNVERIFIED`.
