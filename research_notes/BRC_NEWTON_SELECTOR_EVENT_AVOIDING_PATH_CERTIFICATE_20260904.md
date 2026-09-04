# BRC event-avoiding selector path certificate

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: selector event theorem, one-parameter chamber compiler line

## 1. Motivation

For more than one real parameter, an event hypersurface

\[
H(\lambda)=0
\]

contains all possible selector-transition parameters, but computing every connected component of its complement is a genuine semi-algebraic geometry problem.

Often a much smaller task is enough:

> certify that two specified parameter points have the same selector state.

A full CAD is unnecessary if one can exhibit a path between the points that avoids the event hypersurface.

## 2. Event-avoiding transport theorem

Let

\[
\lambda\in\mathbb R^m
\]

parameterize a polynomial selector family, and suppose an exact theorem certifies that the selector state can change only on

\[
H(\lambda)=0,
\qquad
H\in\mathbb Q[\lambda_1,\dots,\lambda_m].
\]

Let

\[
\gamma:[0,1]\to\mathbb R^m
\]

be a continuous path such that

\[
H(\gamma(s))\ne0
\qquad
\forall s\in[0,1].
\]

Then the selector state is constant along the path.  In particular,

\[
\boxed{
\mathcal L(\gamma(0))=\mathcal L(\gamma(1)).
}
\]

This is simply transport inside one connected subset of the event-free parameter region.

## 3. Exact polynomial-path certificate

Assume every coordinate of the path is a rational polynomial in a scalar path parameter:

\[
\gamma_j(s)\in\mathbb Q[s].
\]

Then the pullback

\[
\boxed{
h(s)=H(\gamma(s))\in\mathbb Q[s]
}
\]

is exact.

A complete certificate that one path segment avoids the event hypersurface is:

1. \(h(0)\ne0\);
2. \(h(1)\ne0\);
3. the squarefree Sturm count of roots of `h` in the open interval `(0,1)` is zero.

No floating path sampling is needed.

For a piecewise polynomial path, certify each segment and require exact endpoint matching.

## 4. Sufficient, not necessary for a proposed path

Failure of one candidate path does **not** imply that the two endpoint parameters lie in different selector chambers.

The path may cross a non-minimal event hypersurface even though another path can avoid it.

Thus the semantics are:

\[
\boxed{
\text{event-avoiding path found}
\Longrightarrow
\text{same selector state},
}

but

\[
\boxed{
\text{one proposed path hits }H=0
\centernot\Longrightarrow
\text{different selector state}.
}

## 5. Exact two-parameter witness

Consider

\[
Q_{u,v}(x)
=
x^2+\frac{1-u^2-v^2}{4}
\]

with declared smallest-real root/probe

\[
r=-2.
\]

For the monic quadratic,

\[
\operatorname{Res}_x(Q,Q_x)
=1-u^2-v^2.
\]

Also

\[
4Q_{u,v}(-2)
=17-u^2-v^2.
\]

Hence a valid selector event polynomial, up to a nonzero scalar, is

\[
\boxed{
H(u,v)
=(1-u^2-v^2)(17-u^2-v^2).
}
\]

The event set is the union of two circles:

\[
u^2+v^2=1,
\qquad
u^2+v^2=17.
\]

Take

\[
A=(-2,0),
\qquad
B=(2,0).
\]

Both have

\[
u^2+v^2=4,
\]

and the competing quadratic roots are approximately inside `[-1,1]`, so the declared `-2` root is safely smaller.

## 6. Straight-line failure

The direct segment

\[
\gamma_0(s)=(-2+4s,0)
\]

has

\[
u^2+v^2=(-2+4s)^2.
\]

It meets the inner event circle at

\[
s=\frac14,
\qquad
s=\frac34.
\]

Therefore

\[
H(\gamma_0(s))
\]

has two roots in `(0,1)`, and the straight-line certificate fails.

Yet the selector state does not actually change there: when the quadratic competitors become complex, the declared root remains the smallest real root.  The inner discriminant circle is an over-approximate event barrier for this observer.

## 7. Exact detour certificate

Use the two segments

\[
\gamma_1(s)=(-2+2s,\ 2s),
\]

\[
\gamma_2(s)=(2s,\ 2-2s).
\]

They join

\[
(-2,0)\to(0,2)\to(2,0).
\]

On either segment,

\[
\boxed{
\rho^2(s)=u(s)^2+v(s)^2
=4(1-2s+2s^2).
}
\]

For \(0\le s\le1\),

\[
2\le\rho^2(s)\le4.
\]

Hence

\[
1-\rho^2(s)<0,
\qquad
17-\rho^2(s)>0,
\]

so

\[
H(\gamma_j(s))\ne0
\]

on both closed segments.

The exact Sturm pullback certificate therefore proves that `A` and `B` belong to the same event-free connected region without computing the full complement topology.

## 8. Genuine separator witness

Keep the same family and compare

\[
A=(-2,0)
\]

with

\[
C=(5,0).
\]

At `A`, \(u^2+v^2=4<17\) and the declared root is safe.  At `C`,

\[
\frac{1-u^2-v^2}{4}=-6,
\]

so the competing smaller root is

\[
-\sqrt6<-2,
\]

and the declared root is unsafe.

Any continuous path from radius-squared `4` to radius-squared `25` must cross the outer event circle

\[
u^2+v^2=17.
\]

Thus in this case the event hypersurface contains a genuine selector separator.

## 9. Piecewise path certificate state

An exact certificate can be stored as:

- rational endpoint parameter vectors;
- a finite list of polynomial path segments;
- for each segment, the exact pullback polynomial `h_j(s)`;
- a Sturm attestation `N_{h_j}((0,1))=0`;
- nonzero endpoint evaluations;
- the selector label at one endpoint.

The final endpoint label follows by transport.

This is much smaller than a global CAD decomposition when only pairwise chamber connectivity is needed.

## 10. Relation to BRC observer leases

The event hypersurface is observer-dependent.

A richer observer can have more event factors, making an event-avoiding path certificate stricter.  A coarser selector-value observer may admit paths that would be illegal for a multiplicity/provenance observer.

Thus the path certificate inherits the T56-T58 principle:

\[
\boxed{
\text{safe transport depends on the declared observer lease}.
}
\]

## 11. Hard boundaries

- The event-coverage theorem is an input.
- Failure of one proposed path is not a chamber-separation proof.
- The method does not compute all connected components of a multivariate event complement.
- Polynomial/piecewise-polynomial paths are certified; arbitrary analytic paths are not handled here.
- Event avoidance does not determine typed semantics exactly at event points.
- No multi-parameter CAD, complete Puiseux solver, generic multi-generator algebraic field, signed branch interference, or infinite-state claim is made.
