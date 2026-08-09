# P025 Supplement 10 — Exact Access Formula for `1+qr=p^m`

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplements 05, 09  
Hard block: `NONE`

## 1. Structured family

Assume an actual primitive relation

\[
\boxed{1+qr=p^m}
\]

with pairwise distinct primes `p,q,r` and `m>=1`.

The term `qr` is squarefree, so Supplement 05 already gives

\[
\boxed{\eta_{\min}=m.}
\]

This supplement solves the corresponding floor-access radius `nu` exactly by reducing the three-coordinate system to a two-variable Diophantine minimization.

## 2. P025-T28 — floor slice collapses to one Bezout equation

Use coordinate order `(q,r,p)`. The raw additive row is

\[
\alpha=(r,q,-m p^{m-1}),
\]

and the raw Wronskian row for `W(1,qr)` is

\[
\beta=(r,q,0).
\]

Let

\[
H=m p^{m-1}.
\]

The nonzero cross minors are

\[
Hr,
\qquad
Hq,
\]

so, since `gcd(q,r)=1`, their gcd is exactly

\[
d=H.
\]

A positive-generator floor witness must satisfy

\[
\alpha\cdot x=0,
\qquad
\beta\cdot x=H.
\]

Subtracting the two equations gives

\[
-Hx_p=-H,
\]

hence

\[
\boxed{x_p=1.}
\]

The remaining equation is

\[
\boxed{r x_q+q x_r=H.}
\]

Therefore

\[
\boxed{
\nu
=
\max\left(
1,
\min_{ru+qv=H}
\max(|u|,|v|)
\right).
}
\]

This is an exact formula with no witness-lattice enumeration.

## 3. P025-T29 — universal triangle lower bound

If

\[
ru+qv=H
\]

and

\[
B=\max(|u|,|v|),
\]

then

\[
H
\le r|u|+q|v|
\le(r+q)B.
\]

Thus

\[
\boxed{
\nu
\ge
L(q,r,p,m)
:=
\max\left(
1,
\left\lceil\frac{m p^{m-1}}{q+r}\right\rceil
\right).
}
\]

This lower bound is sharp exactly when the square

\[
[-L,L]^2
\]

contains an integer point on the line

\[
ru+qv=H.
\]

Because all integer solutions form a one-dimensional affine lattice, this is decided exactly by the same integer interval-intersection calculus as Supplement 09.

## 4. P025-T30 — exact finite solver

Since `gcd(q,r)=1`, choose one Bezout solution `(u_0,v_0)` to

\[
ru+qv=H.
\]

All solutions are

\[
\boxed{
(u,v)
=(u_0,v_0)+k(q,-r),
\qquad k\in\mathbb Z.
}
\]

For a candidate radius `B`, the constraints

\[
|u_0+kq|\le B,
\qquad
|v_0-kr|\le B
\]

are two integer intervals for `k`. Their intersection is nonempty exactly when `B` is feasible.

Starting at the triangle lower bound and using any particular solution as a finite upper bound gives the exact optimum by integer binary search.

So the family requires only:

- extended gcd;
- integer floor/ceiling division;
- interval intersection;
- logarithmically many feasibility checks in the initial upper radius.

## 5. Equality example — `1+15=16`

Here

\[
q=3,
\qquad
r=5,
\qquad
p=2,
\qquad
m=4,
\]

so

\[
H=4\cdot2^3=32.
\]

The lower bound is

\[
L=\left\lceil\frac{32}{3+5}\right\rceil=4.
\]

The balanced solution

\[
5\cdot4+3\cdot4=32
\]

attains it. Hence

\[
\boxed{
\eta_{\min}=4,
\qquad
\nu=4.
}
\]

One floor witness in `(q,r,p)` coordinates is

\[
\boxed{(4,4,1)}.
\]

## 6. Strict-gap example — `1+511=512`

Here

\[
511=7\cdot73,
\qquad
512=2^9,
\]

so

\[
H=9\cdot2^8=2304.
\]

The triangle bound is

\[
L
=
\left\lceil\frac{2304}{7+73}\right\rceil
=29.
\]

But no integer solution lies in `[-29,29]^2`. The exact interval solver gives

\[
\boxed{\nu=33.}
\]

For example

\[
73\cdot33+7\cdot(-15)=2304.
\]

Thus

\[
\boxed{
\eta_{\min}=9,
\qquad
L=29<\nu=33.
}
\]

So even in this highly structured family, the continuous triangle lower bound can miss an irreducible **integrality access gap**.

## 7. Three separate obstructions in one family

For `1+qr=p^m`, the certificate problem decomposes into:

1. **arithmetic absorption obstruction**
   \[
   \eta_{\min}=m;
   \]
2. **continuous balancing lower bound**
   \[
   L=\lceil H/(q+r)\rceil;
   \]
3. **integrality access defect**
   \[
   \boxed{\Gamma_{\rm int}=\nu-L\ge0.}
   \]

The examples show both possibilities:

- `1+15=16`: `Gamma_int=0`;
- `1+511=512`: `Gamma_int=4`.

This is a finer decomposition than treating all certificate difficulty as one norm.

## 8. Relation to P025's broader precision chain

The current hierarchy is now:

\[
\boxed{
\text{support/valuation data}
\to
\eta_{\min}
\to
\text{continuous access lower bound}
\to
\text{integer access defect}
\to
\nu
\to
\text{full Pareto frontier}.
}
\]

For this special family, the first four stages all have explicit finite arithmetic formulas or exact one-dimensional solvers.

## 9. Mature-mathematics boundary

This stage uses standard material:

- linear Diophantine equations;
- Bezout parameterization;
- `L_infinity` minimization on an affine integer line;
- triangle inequalities;
- interval intersection.

P025 claims no priority for those tools. The family is useful because it makes the project distinction between arithmetic obstruction, continuous bound and integer access defect completely explicit.

## 10. Executable assets

Added:

- `src/enterprise_math/abc_absorption_two_variable.py`
  - generic exact `A*u+B*v=N` minimum-`L_infinity` solver;
  - triangle lower bound;
  - structured specialization for `1+qr=p^m`.
- `tests/test_abc_absorption_two_variable.py`
  - generic sharp example;
  - `1+15=16` equality case;
  - `1+511=512` strict integrality-gap case;
  - invalid/unsolvable input boundaries.

## 11. Next frontier

No hard block exists. Continue with:

1. characterize `Gamma_int=0` by a modular interval criterion;
2. seek closed bounds on `Gamma_int` in terms of `q,r`;
3. search whether `Gamma_int` or `delta_abs` can grow unbounded in concrete prime-power families;
4. extend the same decomposition to `1+b=p^m` when `b` has more than two prime factors;
5. compare these exact access defects with the norm bounds used in Pasten's Geometry-of-Numbers argument before drawing any abc-quality conclusion.
