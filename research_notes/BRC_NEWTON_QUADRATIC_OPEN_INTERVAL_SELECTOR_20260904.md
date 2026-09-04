# BRC quadratic open-interval and smallest-positive selector chambers

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T59/T60 and main-backed PR #1208

## 1. Problem

The split-affine selector theorem handles edge polynomials whose competing real roots are already supplied as explicit affine root branches.  PR #1208 removed that split requirement for the smallest-real selector when the competing cofactor is one monic quadratic.

The next target is the smallest-positive selector.  Its natural question is not merely whether a competing root lies below a declared positive root `r`; negative and zero roots are harmless.  The exact condition is:

> the competing cofactor has no root in the open interval `(0,r)`.

This note proves a more reusable theorem first: an exact four-chamber criterion for a monic quadratic to have no root in an arbitrary rational open interval `(u,v)`.

Quadratic discriminants, Vieta relations, Sturm root counts and semi-algebraic chambers are classical prior art.  The BRC contribution here is the exact typed selector certificate that composes with the Newton schedule/observer stack without materializing irrational roots.

## 2. General open-interval setup

Let

\[
Q(x)=x^2+ax+b,
\qquad a,b\in\mathbb Q,
\]

and fix rational endpoints

\[
u<v.
\]

Define

\[
D=a^2-4b,
\]

\[
A=Q(u),\qquad B=Q(v),
\]

and endpoint slopes

\[
S_u=Q'(u)=2u+a,
\qquad
S_v=Q'(v)=2v+a.
\]

If `D>=0`, write the real roots as

\[
\alpha\le\beta.
\]

Relative to an endpoint `x`, Vieta gives

\[
(\alpha-x)+(\beta-x)=-Q'(x),
\]

\[
(\alpha-x)(\beta-x)=Q(x).
\]

Thus the signs of `Q(x)` and `Q'(x)` determine whether both roots lie on one side of `x` without solving either root.

## 3. Exact four-chamber theorem

The quadratic `Q` has no real zero in the open interval `(u,v)` if and only if exactly one of the following four mutually exclusive cases holds.

### Chamber C0 — complex conjugate pair

\[
\boxed{D<0.}
\]

There are no real roots anywhere.

### Chamber CL — both roots at or to the left of `u`

\[
\boxed{D\ge0,\quad S_u\ge0,\quad A\ge0.}
\]

Indeed, for the shifted roots

\[
t_1=\alpha-u,\qquad t_2=\beta-u,
\]

we have

\[
t_1+t_2=-S_u\le0,
\qquad
t_1t_2=A\ge0.
\]

Two real numbers with non-positive sum and non-negative product are both non-positive.  Hence

\[
\alpha\le\beta\le u.
\]

The converse is immediate.

### Chamber CR — both roots at or to the right of `v`

\[
\boxed{D\ge0,\quad S_v\le0,\quad B\ge0.}
\]

Now the shifted roots relative to `v` have non-negative sum and non-negative product, so

\[
v\le\alpha\le\beta.
\]

### Chamber CS — the roots straddle the whole interval

\[
\boxed{A\le0,\quad B\le0.}
\]

A monic real quadratic is non-positive exactly on the closed interval between its real roots.  Therefore both `u` and `v` lie in `[alpha,beta]`, so

\[
\alpha\le u<v\le\beta.
\]

Conversely, this placement gives `A<=0` and `B<=0`.

### Combined criterion

Therefore

\[
\boxed{
Q^{-1}(0)\cap(u,v)=\varnothing
}
\]

if and only if

\[
\boxed{
D<0
\;\lor\;
(D\ge0\land S_u\ge0\land A\ge0)
\;\lor\;
(D\ge0\land S_v\le0\land B\ge0)
\;\lor\;
(A\le0\land B\le0).
}
\]

The four cases are mutually exclusive when `u<v`.

## 4. Why endpoint signs alone are insufficient

Positive endpoint values do not imply that an upward-opening quadratic is root-free inside the interval.  For example,

\[
Q(x)=x^2-x+\frac18
\]

satisfies

\[
Q(0)=Q(1)=\frac18>0,
\]

but

\[
D=\frac12>0,
\qquad
Q'(0)=-1<0<1=Q'(1),
\]

so both real roots lie strictly inside `(0,1)`.

The slope clauses in `CL` and `CR`, or equivalently the vertex location, are essential.

## 5. Smallest-positive corollary

Let `r>0` be a declared rational root of an edge polynomial

\[
E(y)=(y-r)^m Q(y),
\qquad m\ge1,
\]

where

\[
Q(y)=y^2+ay+b.
\]

Fixed declared multiplicity requires

\[
R:=Q(r)=r^2+ar+b\ne0.
\]

The declared root `r` is the smallest positive real root of `E` exactly when `Q` has no root in `(0,r)`.

Set

\[
L=-a-2r=-Q'(r).
\]

Applying the four-chamber theorem with `u=0`, `v=r` gives:

\[
\boxed{
\begin{aligned}
r\text{ is the smallest positive root}
\iff R\ne0\text{ and }[
& D<0\\
&\lor(D\ge0\land a\ge0\land b\ge0)\\
&\lor(D\ge0\land L\ge0\land R>0)\\
&\lor(b\le0\land R<0)
].
\end{aligned}
}
\]

The four geometric meanings are:

1. the quadratic roots are non-real;
2. both competing roots are non-positive;
3. both competing roots are at or to the right of `r`;
4. one competing root is at or below zero and the other lies strictly above `r`.

A root at zero is permitted because the selector is smallest **positive**, not smallest non-negative.  A root at `r` is excluded by `R!=0` because it changes the declared multiplicity.

No quadratic root or floating square root is needed.

## 6. Disconnected non-split witness

Take

\[
Q_t(y)=y^2-3y+t,
\]

\[
E_t(y)=(y-1)^2Q_t(y),
\]

with declared root

\[
r=1.
\]

Then

\[
D=9-4t,
\qquad
R=Q_t(1)=t-2,
\qquad
L=1.
\]

The exact smallest-positive chamber is

\[
\boxed{t\le0\quad\lor\quad t>2.}
\]

The regimes are:

- `t<=0`: the roots straddle `(0,1)` externally; the non-positive root is harmless and the positive root lies above `1`;
- `0<t<2`: at least one competing root lies in `(0,1)`, so the selector changes;
- `t=2`: `Q_t(1)=0`, so the declared multiplicity collides;
- `2<t<9/4`: both competing roots are real and strictly above `1`;
- `t=9/4`: the competing double root is `3/2`, still above `1`;
- `t>9/4`: the competing roots are complex.

Thus the non-split smallest-positive selector chamber is already disconnected in one rational parameter.

## 7. Semi-algebraic complexity

For fixed rational `u,v`, if `a(lambda)` and `b(lambda)` are rational-affine parameter forms, then

- `A(lambda)=Q(u;lambda)` is affine;
- `B(lambda)=Q(v;lambda)` is affine;
- `S_u(lambda)` and `S_v(lambda)` are affine;
- `D(lambda)=a(lambda)^2-4b(lambda)` is quadratic.

Therefore the exact root-free interval chamber is a finite Boolean combination of rational affine sign conditions and one quadratic discriminant sign condition.

This gives a low-degree non-split selector certificate that composes with the constructible Newton schedule strata of WBRC-T59.

## 8. Relation to the smallest-real quadratic theorem

The smallest-real result of PR #1208 asks whether `Q` has a root in `(-infinity,r)`.  Formally, only the `complex` and `both roots to the right` placements survive the left-end limit.  Its criterion

\[
D<0\quad\lor\quad(-a-2r>0\land Q(r)>0)
\]

is therefore the semi-infinite specialization of the same root-placement geometry.

The present theorem adds the two placements that become legal only because roots at or below zero are irrelevant to the smallest-positive selector.

## 9. Exact regression

The dedicated checker performs:

- `1,215` rational `(a,b,u,v)` interval cases;
- exact comparison of the four-chamber formula with Sturm root counts in `(u,v)`;
- explicit endpoint-root handling by Vieta, so roots at `u` or `v` are not miscounted as interior roots;
- `4,860` shifted-discriminant identity checks;
- `324` smallest-positive `(a,b,r)` cases, including `15` fixed-multiplicity collisions;
- one-root and two-root unstable cases;
- a `65`-point exact sweep of the disconnected witness `t<=0 or t>2`;
- the positive-endpoint/two-interior-root warning example.

The checker never materializes a quadratic root and never uses floating arithmetic.

## 10. Hard boundaries

- MONIC_QUADRATIC_COFACTOR != GENERAL PARAMETRIC POLYNOMIAL.
- OPEN_INTERVAL_ROOT_FREE != ROOT COUNT WITH ENDPOINTS INCLUDED.
- SMALLEST_POSITIVE != SMALLEST_REAL.
- ROOT_AT_ZERO is allowed for smallest-positive selection.
- ROOT_AT_DECLARED_R changes multiplicity and is excluded.
- POSITIVE ENDPOINT VALUES do not by themselves certify an empty interval.
- LOW-DEGREE SEMI-ALGEBRAIC CERTIFICATE != GENERAL PARAMETRIC STURM/SUBRESULTANT CAD.
- No complete Puiseux solver, generic factorization, multi-generator algebraic field, signed branch interference or infinite-state claim is made.

## 11. Next frontier

The next exact extension should not jump immediately to arbitrary degree.  Two controlled routes are now available:

1. combine several certified quadratic cofactors by conjunction, yielding a product of split and non-split selector certificates without expanding the full polynomial;
2. derive a fixed-degree cubic interval-root certificate from a symbolic Sturm/subresultant sign table, keeping parameter degree and branch count explicit.
