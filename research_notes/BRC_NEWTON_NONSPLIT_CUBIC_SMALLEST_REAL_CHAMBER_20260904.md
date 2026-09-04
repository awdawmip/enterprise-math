# BRC non-split cubic smallest-real selector chamber

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T59/T60, main-backed PR #1208

## 1. Problem

The current selector hierarchy contains:

- WBRC-T60/T61: complete split-affine real-root certificates;
- PR #1208: one non-split monic quadratic cofactor for `SMALLEST_REAL_ROOT`;
- the quadratic smallest-positive companion is being treated separately.

The next non-split class is a monic cubic cofactor.

Fix a declared rational root `r` of multiplicity `m` and a monic cubic

\[
Q(x)=x^3+a x^2+b x+c,
\qquad a,b,c\in\mathbb Q.
\]

Require fixed declared multiplicity:

\[
R:=Q(r)\ne0.
\]

This note treats the non-degenerate cubic case

\[
\Delta(Q)\ne0,
\]

and asks when the declared root `r` is the smallest real root of

\[
E(x)=(x-r)^mQ(x).
\]

Equivalently, when does `Q` have no real root to the left of `r`?

Cubic discriminants, Rolle interlacing, and Sturm root counts are classical prior art.  No generic parametric CAD/Sturm novelty is claimed.

## 2. Exact cubic data

Write

\[
R=Q(r)=r^3+a r^2+b r+c,
\]

\[
R_1=Q'(r)=3r^2+2ar+b,
\]

\[
R_2=Q''(r)=6r+2a.
\]

The monic cubic discriminant is

\[
\boxed{
\Delta
=a^2b^2-4b^3-4a^3c-27c^2+18abc.
}
\]

For a real cubic:

- \(\Delta<0\): exactly one real root;
- \(\Delta>0\): three distinct real roots;
- \(\Delta=0\): a repeated-root boundary, excluded from the theorem below.

## 3. One-real-root regime

Assume

\[
\Delta<0.
\]

Let \(\alpha\) be the unique real root.  Since the cubic is monic,

\[
Q(x)<0\quad(x<\alpha),
\qquad
Q(x)>0\quad(x>\alpha).
\]

Hence

\[
\boxed{
r<\alpha\iff R<0.
}
\]

So in the one-real-root regime the smallest-real selector certificate is simply the sign of the cubic at the declared root.

## 4. Three-real-root regime

Assume

\[
\Delta>0.
\]

Let the three distinct real roots be

\[
\alpha<\beta<\gamma.
\]

Let the two derivative roots be

\[
u<v.
\]

Rolle interlacing gives

\[
\alpha<u<\beta<v<\gamma.
\]

The derivative is a monic-up quadratic:

\[
Q'(x)=3x^2+2ax+b.
\]

Therefore

\[
x<u
\]

is characterized without solving the derivative quadratic by

\[
\boxed{
Q'(x)>0
\quad\text{and}\quad
Q''(x)<0.
}
\]

Indeed, `Q'>0` places `x` outside the interval `[u,v]`, while `Q''<0` places `x` to the left of the derivative midpoint `-a/3`, ruling out the right outer branch `x>v`.

Now the sign pattern of a monic cubic with three simple real roots is

\[
-,+,-,+
\]

across

\[
(-\infty,\alpha),
(\alpha,\beta),
(\beta,\gamma),
(\gamma,\infty).
\]

Thus:

- `R<0` says `r` is either left of `alpha` or between `beta` and `gamma`;
- `R_1>0` and `R_2<0` say `r<u`;
- because `u` lies between `alpha` and `beta`, the second negative-sign interval `(beta,gamma)` is excluded;
- inside `(-infinity,u)`, `R<0` therefore forces `r<alpha`.

Hence

\[
\boxed{
r<\alpha
\iff
R<0,\quad R_1>0,\quad R_2<0
\qquad(\Delta>0).
}
\]

## 5. Non-degenerate cubic selector theorem

Combining the two regimes gives the exact radical-free criterion:

\[
\boxed{
\begin{aligned}
&r<\min\{\text{real roots of }Q\}\\
&\iff
R<0\ \land\
\Bigl[
\Delta<0
\ \lor\ 
(\Delta>0\land R_1>0\land R_2<0)
\Bigr],
\end{aligned}
}
\]

under the hypotheses

\[
R\ne0,
\qquad
\Delta\ne0.
\]

Equivalently, for

\[
E(x)=(x-r)^mQ(x),
\]

the declared rational root `r` remains the smallest real root exactly on that semi-algebraic chamber.

No cubic radical is materialized.

## 6. Why `R<0` alone is insufficient in the three-root regime

Take

\[
Q(x)=x^3-3x.
\]

Its roots are

\[
-\sqrt3,\ 0,\ \sqrt3,
\]

and \(\Delta=108>0\).

At

\[
r=\frac12,
\]

we have

\[
R<0,
\]

but `r` lies between the middle and largest roots, so it is not the smallest real root.  Indeed

\[
R_1=3r^2-3<0,
\]

and the derivative certificate rejects the point.

This is the cubic analogue of the quadratic fact that an endpoint sign alone does not determine an even-number root crossing.

## 7. One-parameter witness spanning both discriminant phases

Consider the depressed cubic

\[
Q_t(x)=x^3-3x+t
\]

with declared root

\[
r=-2.
\]

Then

\[
R=t-2,
\qquad
R_1=9>0,
\qquad
R_2=-12<0,
\]

and

\[
\Delta=108-27t^2=27(4-t^2).
\]

For all non-degenerate parameter values \(t\ne\pm2\), the selector theorem simplifies to

\[
\boxed{t<2}.
\]

This single family crosses both cubic regimes:

- \(-2<t<2\): three distinct real roots, and the derivative-side certificate is active;
- \(t<-2\): one real root, with `R<0` sufficient;
- \(t>2\): one real root lies to the left of the declared root, so the selector fails;
- \(t=2\): fixed-multiplicity collision `Q_t(-2)=0`;
- \(t=-2\): discriminant-zero boundary; the declared root is still left of all real roots, but this theorem intentionally does not classify the repeated-root phase.

## 8. Exact validation route

The independent oracle is the existing rational Sturm machinery.

For each rational tuple `(a,b,c,r)`:

1. build `Q` exactly;
2. classify `R=0` as a fixed-multiplicity collision;
3. classify `Delta=0` as the repeated-root boundary;
4. otherwise count exact distinct roots of `Q` in `(-B,r)` where `B` is a strict rational Cauchy root bound;
5. compare `count==0` with the closed discriminant/derivative formula.

No numerical cubic solver or floating root approximation is required.

## 9. Parametric geometry

For affine coefficient forms `a(lambda),b(lambda),c(lambda)` and affine/rational declared root `r(lambda)`, the selector chamber is semi-algebraic:

- `Delta` is polynomial of degree at most four in the affine coefficient parameters;
- `R`, `R_1`, `R_2` are polynomial/affine forms after substitution;
- the theorem uses only exact sign conditions.

This is strictly more general than the split-affine selector chamber, while still much narrower than a generic higher-degree parametric Sturm/CAD theorem.

## 10. Hard boundaries

- NONDEGENERATE_CUBIC means `Delta!=0`; repeated-root cubic cofactors are not covered.
- FIXED_MULTIPLICITY requires `R!=0`.
- SMALLEST_REAL selector stability is not smallest-positive stability.
- The theorem treats one monic cubic cofactor only.
- No factorization inference from a generic higher-degree polynomial is claimed.
- No complete parametric Sturm/CAD, complete Puiseux solver, multi-generator algebraic field, signed branch interference, or infinite-state claim is made.
