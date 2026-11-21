# C87: strict concavity of the complete high-precision position constant

## 1. The result

Retain C84–C86's auxiliary Haar readout model, all correlated integer
competitors, and the original three-source-phase average. Let

\[
I_\theta=\frac1{20}\int_0^\infty[1-F_\theta(a)]a^{-19/20}\,da,
\qquad 0<\theta<1.
\]

The C85 endpoint continuation still uses three independent auxiliary
phases. Set

\[
\gamma=\frac1{20},\quad
D=\zeta(2)(1-\gamma)(1+\gamma)(2+\gamma),\quad C=\frac2D.
\]

**Theorem.** The function \(I_\theta\) extends to a twice continuously
differentiable function on \([0,1]\), with one-sided derivatives at the
endpoints. It is symmetric about \(1/2\), strictly concave, strictly
increasing on \((0,1/2)\), and strictly decreasing on \((1/2,1)\).
Consequently:

- The midpoint is the unique global maximum of the high-precision
  ambiguity constant.
- The two auxiliary endpoints are its equal global minima. Among
  strictly interior positions there is an endpoint infimum, attained
  at no interior position.
- For every \(\theta\in[0,1]\),

\[
\boxed{
I_{1/2}-I_\theta\ge
\frac{C(\theta-1/2)^2}{100\max(\theta,1-\theta)}.}
\tag{1}
\]

The two independently checked positivity certificates used here are
`axis_midpoint_certificate.json` and the parent
`../integrated_kernel_certificate.json`. The proof averages the radial
variable first. It does not require or assert pointwise positivity of
the complete two-variable kernel \(H(r,x)\).

## 2. Separate the position parameter exactly

Let \(H\) be C86's signed finite Mellin kernel, and define

\[
A(x)=\int_0^1 r^\gamma H(r,x)\,dr,
\qquad B(x)=\frac{A(x)}{x^2}\quad(x>0).
\]

The C86 exact all-area formula reads, for \(0<\theta\le1/2\),

\[
I_\theta-I_{1/2}
=-C\int_{q}^{1}\bigl((1-\theta)x-\theta\bigr)B(x)\,dx,
\qquad q=\frac{\theta}{1-\theta}. \tag{2}
\]

The lower endpoint makes the linear factor zero. Since \(H\) is
continuous across its finite chamber interfaces, \(A\) is continuous.
The endpoint expansion proved in `ENDPOINT_AXIS_PROOF.md` shows that
\(B\) extends continuously to zero. Thus the following differentiations
and the endpoint limits are justified by ordinary dominated convergence
and the fundamental theorem of calculus:

\[
\boxed{I'_\theta=C\int_q^1(1+x)B(x)\,dx,}
\tag{3}
\]

\[
\boxed{I''_\theta=-C(1+q)^3B(q).}
\tag{4}
\]

There is no derivative of a numerical approximation in either formula.
They are analytic consequences of the exact C86 identity.

## 3. Positivity on the entire interval

The endpoint certificate proves

\[
B(x)>\frac1{40}\qquad(0<x\le1/8).
\tag{5}
\]

The parent certificate covers every point of \([1/8,1]\) by sixty
closed rational intervals. On each complete interval it proves
\(B(x)\ge1/200\), by weighted one-dimensional radial quadrature and
uniform Taylor/Lipschitz bounds in \(x\). In particular,

\[
\boxed{B(x)\ge\frac1{200}>0\quad(0\le x\le1).}
\tag{6}
\]

The origin value is positive by its exact expression below. Equations
(3) and (4) give strict monotonicity and strict concavity on the left
half of the interval. Endpoint exchange supplies
\(I_\theta=I_{1-\theta}\). Equation (3) gives \(I'_{1/2}=0\), and
the two limits of the second derivative at the midpoint agree. These
facts prove the global assertions.

For the quantitative gap, use (6) directly in (2):

\[
\begin{aligned}
I_{1/2}-I_\theta
&\ge\frac C{200}\int_q^1((1-\theta)x-\theta)\,dx\\
&=\frac C{400}\frac{(1-2\theta)^2}{1-\theta}
\qquad(0\le\theta\le1/2).
\end{aligned}
\]

Symmetry gives (1). A convenient coarser curvature consequence is
\(I''_\theta\le-C/200\) on the entire open interval.

## 4. The midpoint and the endpoint have certified curvature

The same one-dimensional interval computation proves

\[
0.0120635020999547292
<A(1)<0.0132651622361925642.
\]

Therefore

\[
\boxed{-0.063099<I''_{1/2}<-0.057382<0.}
\tag{7}
\]

The complete directed endpoints are in the certificate. The local
expansion is

\[
I_{1/2-h}=I_{1/2}-4C A(1)h^2+o(h^2).
\]

At the endpoint, the exact coefficient is

\[
a_2=B(0)
=\frac{211}{244}2^{-1/20}
-\frac{101}{122}4^{-1/20}+\frac{23}{61}
=0.43991762751109\ldots.
\]

Thus

\[
\boxed{I''_{0+}=-C a_2=-0.26156889623798\ldots.}
\tag{8}
\]

The endpoint value itself is C85's already established continuation
\(I_0=I_1=(40/41)I_2\). The endpoint slope is the finite positive number

\[
I'_{0+}=C\int_0^1(1+x)B(x)\,dx>0.
\]

More precisely, with the certified negative constant \(b_2\) defined
in the axis proof,

\[
\boxed{
I_\theta=I_0+I'_{0+}\theta
-\frac{C a_2}{2}\theta^2
-\frac{C b_2}{(1+\gamma)(2+\gamma)}\theta^{2+\gamma}
+O(\theta^3).}
\tag{9}
\]

Because \(b_2<0\), the fractional-power correction in (9) is positive.
The second derivative is continuous at the endpoint, but is not
differentiable there: its first change has nonzero order
\(\theta^{1/20}\). Hence the endpoint continuation is not \(C^3\).

## 5. Consequence for fixed rational original reading positions

Choose any fixed rational pair

\[
0<\theta_1<\theta_2\le\frac12.
\]

Take a common fixed integer denominator \(n\), so
\(\theta_i=m_i/n\). Compare the original readings at

\[
c,\quad c+m_i b,\quad c+nb,
\]

with the same arrangements, the same outer inventories, three readings,
and the same retained precision in each reading. All added factors of
five remain before the first update. The original bridge requires

\[
\frac b{c^{1/3}}\to\infty,\qquad b=o(c),\qquad
2^{p-p_*(c,nb)}\to L>0.
\]

For each fixed \(L\), the full-inventory unique fractions converge to
\(\Phi_{\theta_i}(L)\), uniformly over the three rounding-grid origins.
The C84 low-precision result gives

\[
\Phi_\theta(L)
=\kappa_3 M_{3/2}\sqrt{\frac{\theta(1-\theta)}2}\,L^3
+O_\theta(L^6).
\]

Since \(\theta(1-\theta)\) increases on \((0,1/2)\),
\(\theta_2\) has the larger unique fraction for all sufficiently small
positive \(L\). The high-precision tail uses the same positive original
spectral constant \(W\):

\[
\Phi_{\theta_1}(L)-\Phi_{\theta_2}(L)
=W(I_{\theta_2}-I_{\theta_1})L^{-1/10}+o(L^{-1/10})>0
\]

for all sufficiently large \(L\). Thus the position nearer the endpoint
wins in the high-precision limit, while the position nearer the midpoint
wins in the low-precision limit.

The limit curves are continuous in \(L>0\). One way to verify continuity
is to use C85's phase-uniform finite-vector reduction: for each fixed
lattice the critical scale is piecewise affine in the phases, with no
positive-scale atom; Haar and source integration then preserve
continuity. The intermediate value theorem therefore gives **at least
one finite crossing** for every such fixed rational pair. This argument
does not determine the crossing value or prove that it is unique.

The order of limits remains explicit: first the inventory limit at fixed
rational positions and fixed \(L\), then the low- or high-precision
limit in \(L\). The auxiliary endpoint infimum does not authorize
simultaneous \(\theta=\theta(c)\to0\), nor does the independent-phase
endpoint continuation describe literally repeating one inventory reading.

## 6. A fixed inventory grid has explicit opposite optimal designs

Fix an integer \(n\ge3\). Keep the first and last inventories equal to
\(c\) and \(c+nb\), and permit the middle inventory to be any member
of the fixed list

\[
c+b,\ c+2b,\ldots,\ c+(n-1)b.
\]

Under the same original-inventory assumptions above, the limiting unique
fraction has the following optimal choices:

- For all sufficiently large fixed precision multipliers \(L\), its
  maxima are the two positions \(k=1\) and \(k=n-1\), nearest the
  endpoints.
- For all sufficiently small positive \(L\), its maxima are the
  positions \(k=\lfloor n/2\rfloor\) and
  \(k=\lceil n/2\rceil\), nearest the midpoint. These are the same
  position when \(n\) is even.

The maxima are strict against every position having a different
distance from the midpoint; reflected positions have equal limit
curves. For \(n=3\) the two lists of maximizers coincide. For every
larger grid the low- and high-precision choices differ.

This follows from the strict ordering of the high-precision constants
and of the low-precision leading coefficients. There are only finitely
many candidates for a fixed \(n\), so the pairwise thresholds may be
replaced by one common sufficiently small or sufficiently large
threshold. No explicit activation threshold is asserted here.

The grid size \(n\) is fixed before the inventory limit. Letting the
design grid become arbitrarily fine afterwards approaches the endpoint
infimum. An inventory-dependent choice \(n=n(c)\to\infty\) would
require an additional uniform version of the native bridge.
