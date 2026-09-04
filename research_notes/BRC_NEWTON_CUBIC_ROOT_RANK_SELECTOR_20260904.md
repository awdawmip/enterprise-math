# BRC cubic root-rank selector calculus

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T59/T60/T61, non-split quadratic selector work, cubic smallest-real PR line

## 1. Motivation

The selector problem can be organized more economically than one theorem per selector.

For a non-degenerate monic cubic

\[
Q(x)=x^3+a x^2+b x+c,
\qquad
\Delta(Q)\ne0,
\]

define the exact real-root rank

\[
\nu_Q(x)=\#\{\alpha\in\mathbb R:Q(\alpha)=0,\ \alpha<x\}
\]

for any real point `x` that is not itself a root.

Once \(\nu_Q\) is available:

- a declared root `r` is smaller than every cubic competitor iff \(\nu_Q(r)=0\);
- for `r>0`, it is the smallest positive root iff no cubic root lies in `(0,r)`, equivalently
  \[
  \nu_Q(r)=\nu_Q(0^+),
  \]
  where \(\nu_Q(0^+)\) counts real roots \(\le0\).

Thus smallest-real and smallest-positive selector stability become two readouts of one exact cubic rank carrier.

Root ordering, cubic discriminants, Rolle interlacing, and Sturm counts are classical prior art.  No generic root-count novelty is claimed.

## 2. Discriminant regimes

Use the monic cubic discriminant

\[
\Delta
=a^2b^2-4b^3-4a^3c-27c^2+18abc.
\]

This note assumes

\[
\Delta\ne0.
\]

Then:

- \(\Delta<0\): exactly one real root;
- \(\Delta>0\): three distinct real roots.

## 3. One-real-root rank

When \(\Delta<0\), let \(\alpha\) be the unique real root.  The complex-conjugate quadratic factor is positive on the real line, so the sign of the monic cubic is simply the sign of \(x-\alpha\):

\[
\boxed{
\nu_Q(x)=
\begin{cases}
0,&Q(x)<0,\\
1,&Q(x)>0.
\end{cases}
}
\]

## 4. Three-real-root rank

Assume \(\Delta>0\), with

\[
\alpha<\beta<\gamma.
\]

Let the derivative roots be

\[
u<v,
\]

so Rolle interlacing gives

\[
\alpha<u<\beta<v<\gamma.
\]

The cubic sign alternates

\[
-,+,-,+
\]

across the four root intervals.

The two negative-sign intervals are distinguished exactly by the derivative side:

- on `(-infinity,alpha)`, one has \(Q'>0\) and \(Q''<0\);
- on `(beta,gamma)`, it is impossible to have both \(Q'>0\) and \(Q''<0\): before the right critical point `v`, \(Q'<0\); after `v`, \(Q''>0\).

Similarly the two positive-sign intervals are distinguished by

- on `(gamma,infinity)`, \(Q'>0\) and \(Q''>0\);
- on `(alpha,beta)`, it is impossible to have both positive.

Therefore, for any non-root `x`,

\[
\boxed{
Q(x)<0:\quad
\nu_Q(x)=
\begin{cases}
0,&Q'(x)>0\ \land\ Q''(x)<0,\\
2,&\text{otherwise},
\end{cases}
}
\]

and

\[
\boxed{
Q(x)>0:\quad
\nu_Q(x)=
\begin{cases}
3,&Q'(x)>0\ \land\ Q''(x)>0,\\
1,&\text{otherwise}.
\end{cases}
}
\]

The formula remains valid when `x` is a derivative critical point or the inflection point, provided `Q(x)!=0`: zero derivative values simply fall into the `otherwise` inner-interval branch.

## 5. Recovery of the cubic smallest-real theorem

For a declared rational root `r` with

\[
Q(r)\ne0,
\]

smallest-real selector stability is simply

\[
\boxed{\nu_Q(r)=0}.
\]

Unpacking the rank formula gives

\[
Q(r)<0
\land
\bigl[
\Delta<0
\lor
(\Delta>0\land Q'(r)>0\land Q''(r)<0)
\bigr],
\]

recovering the non-split cubic smallest-real formula as a corollary.

## 6. Exact right-rank at zero

For smallest-positive selection, the relevant base count is

\[
\nu_Q(0^+)=\#\{\text{real roots }\le0\}.
\]

If

\[
c=Q(0)\ne0,
\]

then zero is not a root and

\[
\nu_Q(0^+)=\nu_Q(0).
\]

If

\[
c=0,
\]

non-degeneracy implies that zero is a simple root.

### One-real regime

If \(\Delta<0\) and `c=0`, zero is the unique real root, hence

\[
\boxed{\nu_Q(0^+)=1}.
\]

### Three-real regime

If \(\Delta>0\) and `c=0`, factor

\[
Q(x)=x(x^2+a x+b).
\]

The quadratic roots are distinct and nonzero.

- `b<0`: one quadratic root is negative and one positive, so zero is the middle cubic root:
  \[
  \boxed{\nu_Q(0^+)=2}.
  \]
- `b>0,a<0`: both quadratic roots are positive, so zero is the smallest cubic root:
  \[
  \boxed{\nu_Q(0^+)=1}.
  \]
- `b>0,a>0`: both quadratic roots are negative, so zero is the largest cubic root:
  \[
  \boxed{\nu_Q(0^+)=3}.
  \]

The cases `b=0` or `b>0,a=0` are incompatible with `Delta>0,c=0`.

## 7. Cubic smallest-positive theorem

Let

\[
r>0,
\qquad
Q(r)\ne0,
\qquad
\Delta\ne0.
\]

Then the declared root `r` is the smallest positive root of

\[
E(x)=(x-r)^mQ(x)
\]

iff

\[
\boxed{
\nu_Q(r)=\nu_Q(0^+).
}
\]

This is exact because the difference between the two ranks is exactly the number of cubic roots in the open interval `(0,r)`.

No cubic root is materialized.

## 8. One-real smallest-positive corollary

When \(\Delta<0\), the rank equality collapses to an especially simple formula:

\[
\boxed{
\text{smallest-positive safe}
\iff
c\ge0\ \lor\ Q(r)<0.
}
\]

Interpretation:

- `c>=0`: the unique real cubic root is non-positive;
- `Q(r)<0`: the unique real root lies strictly to the right of the declared positive root.

## 9. Disconnected one-real witness

Consider

\[
Q_t(x)=x^3+x+t
\]

with declared root

\[
r=1.
\]

The discriminant is

\[
\Delta=-4-27t^2<0
\]

for every rational `t`, so there is always exactly one real cubic root.

Moreover

\[
c=t,
\qquad
Q_t(1)=t+2.
\]

Hence the smallest-positive chamber is

\[
\boxed{
t<-2\ \lor\ t\ge0.
}
\]

The intervals have distinct mechanisms:

- `t<-2`: the unique positive cubic root lies to the right of `1`;
- `-2<t<0`: the unique cubic root lies in `(0,1)` and destroys the selector;
- `t=-2`: fixed-multiplicity collision at `r=1`;
- `t=0`: the cubic competitor is exactly the zero root, which is not positive and is therefore harmless;
- `t>0`: the unique cubic root is negative.

Thus even a one-real-root non-split cubic can produce a disconnected smallest-positive selector chamber.

## 10. Exact validation plan

The dedicated checker must:

1. exhaust non-degenerate rational cubic coefficient catalogs and rational probe points;
2. compare the closed root-rank formula against exact Sturm counts from a strict Cauchy left bound;
3. verify all four rank values `0,1,2,3` occur in the three-real regime;
4. verify the rank-zero readout reproduces the cubic smallest-real formula;
5. independently compute `nu_Q(0+)`, including `c=0` endpoint-root cases;
6. compare `nu_Q(r)=nu_Q(0+)` with an exact Sturm count of roots in `(0,r)` for positive declared roots;
7. sweep the disconnected `x^3+x+t` witness through the thresholds `-2` and `0`;
8. preserve `Delta=0` and `Q(r)=0` as separate typed boundaries.

## 11. Hard boundaries

- ROOT_RANK is defined here only for non-degenerate monic cubics.
- A probe point that is itself a cubic root requires a one-sided convention; the declared selector root keeps `Q(r)!=0`.
- `nu_Q(0+)` is a right-rank and differs from `nu_Q(0)` when zero is a cubic root.
- SMALLEST_REAL and SMALLEST_POSITIVE remain different readouts.
- No repeated-root cubic classification, generic higher-degree root-rank formula, parametric CAD/Sturm decomposition, complete Puiseux solver, multi-generator algebraic field, signed branch interference, or infinite-state claim is made.
