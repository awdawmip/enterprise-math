# BRC non-split quadratic smallest-positive selector chamber

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T59, WBRC-T60/T61, main-backed PR #1208

## 1. Problem

WBRC-T61 gives an exact smallest-positive selector chamber when the competing real roots are supplied by a complete split-affine root certificate. PR #1208 then treats the first genuinely non-split class for the smallest-real selector: one monic quadratic cofactor.

The remaining quadratic gap is the smallest-positive selector.

Fix a declared rational root

\[
r>0
\]

of multiplicity \(m\), and a monic quadratic competing cofactor

\[
Q(y)=y^2+ay+b,
\qquad a,b\in\mathbb Q.
\]

Assume fixed declared multiplicity:

\[
R:=Q(r)=r^2+ar+b\ne0.
\]

Then \(r\) is the smallest positive root of

\[
E(y)=(y-r)^mQ(y)
\]

iff \(Q\) has no root in the open interval \((0,r)\).

The goal is to decide this exactly without materializing quadratic radicals.

Quadratic discriminants, root ordering, and Sturm interval counts are classical prior art. No generic selector/CAD novelty is claimed.

## 2. Exact data

Define

\[
D=a^2-4b,
\qquad
R=r^2+ar+b,
\qquad
L=-a-2r.
\]

The useful identity from PR #1208 remains

\[
L^2-D=4R.
\]

The new issue is that roots \(\le0\) are harmless for a smallest-positive observer, so the smallest-real formula cannot simply be reused.

## 3. Closed smallest-positive chamber

### Theorem

Assume \(r>0\) and \(R\ne0\). Then the declared root \(r\) is the smallest positive root of \((y-r)^mQ(y)\) iff the following piecewise condition holds.

If

\[
D<0,
\]

then the condition always holds because \(Q\) has no real root.

If

\[
D\ge0,
\]

then:

### Case A: \(b<0\)

The two quadratic roots have opposite signs. Writing them as \(\alpha<0<\beta\),

\[
R=(r-\alpha)(r-\beta).
\]

Since \(r-\alpha>0\), there is no quadratic root in \((0,r)\) iff \(r<\beta\), equivalently

\[
\boxed{R<0}.
\]

### Case B: \(b=0\)

The roots are

\[
0,\ -a.
\]

The root at zero is not positive and is therefore harmless. The second root is outside \((0,r)\) iff

\[
-a\le0
\quad\text{or}\quad
-a\ge r.
\]

Using \(R=r(r+a)\ne0\), this is equivalent to

\[
\boxed{a\ge0\ \text{or}\ R<0}.
\]

### Case C: \(b>0\)

When \(D\ge0\), the two roots have the same sign.

If

\[
a\ge0,
\]

their sum \(-a\le0\), so both are non-positive and the smallest-positive selector is safe.

If

\[
a<0,
\]

then both roots are positive. Safety therefore requires the smaller root to lie strictly to the right of \(r\):

\[
\frac{-a-\sqrt D}{2}>r.
\]

Because \(R\ne0\), this is equivalent to

\[
L>0
\quad\text{and}\quad
L^2>D.
\]

Using \(L^2-D=4R\), the radical-free criterion is

\[
\boxed{L>0\ \text{and}\ R>0}.
\]

Hence the full exact piecewise chamber is

\[
\boxed{
\begin{aligned}
\mathrm{SPQ}(a,b,r)
\iff{}& R\ne0\ \land\\
&\Bigl[
D<0\\
&\quad\lor\bigl(D\ge0\land b<0\land R<0\bigr)\\
&\quad\lor\bigl(D\ge0\land b=0\land(a\ge0\lor R<0)\bigr)\\
&\quad\lor\bigl(D\ge0\land b>0\land(a\ge0\lor(L>0\land R>0))\bigr)
\Bigr].
\end{aligned}
}
\]

No square root appears in the certificate.

### Compact equivalent chamber

The cases above collapse exactly to

\[
\boxed{
\mathrm{SPQ}(a,b,r)
\iff
R\ne0
\land bR\ge0
\land
\bigl(
 b<0
 \lor R<0
 \lor D<0
 \lor a\ge0
 \lor a\le -2r
\bigr).
}
\]

This compact form is useful operationally: it uses only rational arithmetic and sign tests. The dedicated checker exhaustively verifies equivalence between the piecewise and compact forms over the rational catalog.

## 4. Sturm-variation form

The theorem is exactly the statement

\[
N_Q((0,r))=0,
\]

where \(N_Q\) counts distinct real roots of \(Q\) in the open interval.

For

\[
Q(y)=y^2+ay+b,
\]

a Sturm sequence is, up to positive scalar normalization,

\[
Q(y),\qquad 2y+a,\qquad D,
\]

with zero entries ignored in sign variation. Therefore, under the fixed-multiplicity endpoint condition \(R=Q(r)\ne0\),

\[
\boxed{
N_Q((0,r))
=
V(b,a,D)-V(R,2r+a,D),
}
\]

where \(V\) denotes sign variation after deleting zero entries.

This same formula remains valid at \(D=0\): the zero final Sturm term is simply ignored. It also handles \(b=0\): the zero root lies at the open left endpoint and is not counted.

Thus an equivalent selector certificate is

\[
\boxed{
r>0,\quad R\ne0,\quad
V(b,a,D)=V(R,2r+a,D).
}
\]

This Sturm-variation form is the direct bridge to higher-degree non-split selector chambers: the quadratic closed formula is the explicit simplification of an interval root-count invariant.

The endpoint \(0\) must remain open: a quadratic root at zero is not positive and must not invalidate the selector. The endpoint \(r\) is excluded by the fixed-multiplicity condition \(R\ne0\).

## 5. One-parameter non-split witness

Take

\[
E_t(y)=(y-1)^2(y^2+ty+1).
\]

Here

\[
r=1,
\qquad
b=1,
\qquad
D=t^2-4,
\qquad
R=t+2,
\qquad
L=-t-2.
\]

The fixed-multiplicity collision is

\[
t=-2.
\]

The smallest-positive chamber simplifies exactly to

\[
\boxed{t>-2}.
\]

Indeed:

- \(-2<t<2\): the quadratic roots are complex;
- \(t\ge2\): both quadratic roots are non-positive;
- \(t=-2\): the quadratic is \((y-1)^2\), so the declared multiplicity collides;
- \(t<-2\): the quadratic has two positive reciprocal roots and the smaller one lies in \((0,1)\).

This is the smallest-positive mirror of the PR #1208 witness

\[
(y+1)^2(y^2+ty+1),
\]

whose smallest-real chamber is \(t<2\).

## 6. Geometry of the chamber

For affine parameter forms \(a(\lambda),b(\lambda)\) and fixed rational \(r>0\), the chamber is a finite semi-algebraic Boolean combination of:

- the quadratic discriminant inequality \(D<0\) or \(D\ge0\);
- the sign of \(b\);
- the sign of \(R\);
- the affine order inequalities \(a\ge0\) and \(a\le-2r\).

Unlike the split-affine T61 chamber, this non-split chamber need not be an affine half-space arrangement because the discriminant is quadratic in the affine parameters.

## 7. Relation to current Foundation

The intended composition is

\[
\text{T59 declared schedule-valid stratum}
+
\text{monic quadratic cofactor certificate}
+
\mathrm{SPQ}
\Longrightarrow
\text{actual smallest-positive selector stability}.
\]

This does not replace T59 and does not infer a quadratic cofactor from an arbitrary higher-degree polynomial.

Together with T62 smallest-real selection, the monic-quadratic non-split tier now has exact selectors for both root-order semantics without materializing radicals.

## 8. Exact validation plan

The dedicated checker must:

1. exhaust a rational catalog of \((a,b,r)\) with \(r>0\);
2. classify fixed-multiplicity collisions \(R=0\) separately;
3. compare the closed piecewise and compact formulas with an independent exact Sturm count of roots in \((0,r)\);
4. treat a root at \(0\) as harmless and verify the \(b=0\) boundary separately;
5. record negative/zero/positive discriminant regimes;
6. include irrational-real quadratic competitors without materializing \(\sqrt D\);
7. sweep the one-parameter witness and verify the exact threshold \(t=-2\);
8. verify the identity \(L^2-D=4R\) throughout.

## 9. Hard boundaries

- SMALLEST_POSITIVE != SMALLEST_REAL.
- ZERO_ROOT_IS_NOT_POSITIVE.
- FIXED_SELECTOR_VALUE != FIXED_MULTIPLICITY at \(R=0\).
- QUADRATIC_COFACTOR_CERTIFICATE != GENERAL PARAMETRIC STURM/CAD.
- The theorem covers one monic quadratic cofactor only.
- Higher-degree non-split cofactors remain separate.
- The exact Sturm-variation formula does not imply a generic parametric sign-cell enumerator.
- No complete Puiseux solver, generic multi-generator algebraic field, signed branch interference, or infinite-state claim is made.

## 10. Next frontier

The next genuinely new selector tier is a higher-degree non-split cofactor. The natural exact route is no longer ad hoc root formulas but a fixed symbolic Sturm/subresultant sign chamber: root counts and order remain constant while the relevant sign data avoid zero.
