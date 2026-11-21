# C87: a complete positive axis bound and the endpoint expansion

## 1. Definitions

Let \(\gamma=1/20\), \(p=2+\gamma=41/20\), and use the exact C86
Mellin chambers. Define

\[
A(x)=\int_0^1r^\gamma H(r,x)\,dr,
\qquad B(x)=A(x)/x^2.
\]

For \(0\le x\le1/3\), the second chamber coordinate is always
\(s=rx\le1/3\). Only the four \((r\text{-index},s\text{-index})
=(i,0)\) expressions are needed. Every term has the form

\[
w|a+(b+cr)x|^p.
\]

The exact finite data have \(a\in\{0,1/2,1\}\). For every term with
\(a>0\), throughout its complete radial interval,

\[
|b+cr|\le a. \tag{1}
\]

This is checked at both radial endpoints; the absolute value of an
affine function has no larger interior value.

## 2. Expand at the axis without numerical cancellation

For \(a>0\), Taylor's theorem gives

\[
|a+(b+cr)x|^p
=a^p+p a^{p-1}(b+cr)x
+\frac{p(p-1)}2a^\gamma(b+cr)^2x^2+R.
\]

The constant and linear terms cancel exactly in each radial chamber,
even after grouping separately by the bases \(a=1/2\) and \(a=1\).
Terms with \(a=0\) contribute exactly
\(w|b+cr|^p x^{2+\gamma}\). Hence

\[
B(x)=a_2+b_2x^\gamma+O(x),\tag{2}
\]

where

\[
b_2=\sum_{i=0}^3\int_{r_i}^{r_{i+1}}
r^\gamma\sum_{a=0}w|b+cr|^p\,dr,
\quad (r_0,\ldots,r_4)=(0,1/3,1/2,2/3,1).
\tag{3}
\]

The pointwise quadratic coefficient is particularly simple. Put
\(k=2^{-1/20}\). It is

\[
h_2(r)=\frac{861}{200}r^2,\qquad 0\le r\le1/2,
\]

and

\[
h_2(r)=\frac{861}{400}(1-r)
\{2k(1-2r)+4r-1\},\qquad 1/2\le r\le1.
\]

Integrating \(r^\gamma h_2(r)\) exactly gives

\[
\boxed{a_2=\frac{211}{244}2^{-1/20}
-\frac{101}{122}4^{-1/20}+\frac{23}{61}.}\tag{4}
\]

The coefficient is positive even without numerical roots: its numerator
over 244 is \(92+k(211-202k)>92\), because \(0<k<1\).

## 3. An explicit uniform remainder on \(0\le x\le1/8\)

For a nonzero-base term let

\[
M=\max_{r\in\{r_i,r_{i+1}\}}|b+cr|,
\qquad \ell=a-M/8.
\]

By (1), \(0<\ell\le1\). Along the Taylor segment,

\[
\left|\frac{d^3}{dx^3}(a+(b+cr)x)^p\right|
\le p(p-1)\gamma M^3\ell^{\gamma-1}
\le\frac{p(p-1)\gamma M^3}{\ell}.
\]

Since \(r^\gamma\le1\), summing the integrated absolute remainders
and dividing by \(x^2\) gives the entirely rational bound

\[
\boxed{
|B(x)-a_2-b_2x^\gamma|\le Ex,
\qquad E=\frac{9318931}{47520000}<0.197,
\quad 0\le x\le1/8.}\tag{5}
\]

The script verifies every constant/linear cancellation, every inequality
(1), the three collected radical coefficients in (4), and the exact
sum defining \(E\). It does not estimate the Taylor error from sampled
function values.

## 4. Certified one-dimensional integrals

The script `certify_axis_midpoint.py --n 192` evaluates (3) and \(A(1)\)
using the positive measure \(r^\gamma dr\). All radial chamber
boundaries lie on the mesh. On each interval it uses the exact weighted
centroid, approximated by a certified dyadic node. For a twice
differentiable formula \(G\), the average quadrature error is at most

\[
\frac18\sup|G''|\,h^2+\sup|G'|\,\epsilon,
\]

where \(\epsilon\) is the certified centroid displacement. The
second derivative of \(|a+cr|^{41/20}\) exists continuously even at
an argument zero. Thus no omitted sign-change boundary is required.

Every twentieth root is bracketed by two exact integer-power
inequalities; all accumulated arithmetic uses 112-bit outward
intervals. The executed result is

\[
-0.432249975662706300<b_2
<-0.431787736623156071<0.
\tag{6}
\]

In particular \(b_2>-433/1000\). Combining (4)–(6), and using the
monotonicity of \(x^\gamma\) and \(x\), proves on the complete axis
strip

\[
\begin{aligned}
B(x)
&\ge a_2-\frac{433}{1000}(1/8)^\gamma-\frac E8\\
&>0.02516299590851>\frac1{40},\qquad 0<x\le1/8.
\end{aligned}\tag{7}
\]

The same run proves

\[
0.0120635020999547292<A(1)<0.0132651622361925642.
\]

Its 7,107 root brackets and exact interval endpoints are stored in
`axis_midpoint_certificate.json`. This is a numerical certificate with
analytic error bounds, rather than a sample-based positivity claim.

## 5. Consequence for endpoint regularity

The position derivative identity from `GLOBAL_POSITION_THEOREM.md` is

\[
I''_\theta=-C(1+q)^3B(q),\qquad q=\theta/(1-\theta).
\]

Substitute (2). Since \(q=\theta+O(\theta^2)\),

\[
I''_\theta=-Ca_2-Cb_2\theta^\gamma+O(\theta).
\]

Integrating twice yields

\[
I_\theta=I_0+I'_{0+}\theta-\frac{Ca_2}{2}\theta^2
-\frac{Cb_2}{(1+\gamma)(2+\gamma)}\theta^{2+\gamma}
+O(\theta^3).
\]

The endpoint value \(I_0=(40/41)I_2\) remains the C85 auxiliary
endpoint value. The new result is the differentiable expansion, its
exact quadratic coefficient, the certified sign of the fractional
coefficient, and the complete axis bound (7).
