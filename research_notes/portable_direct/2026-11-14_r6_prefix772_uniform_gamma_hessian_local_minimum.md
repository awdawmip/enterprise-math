# PREFIX-772 / R6 — Uniform rational-interval Gamma Hessian certificate and unique local minimum

Date: 2026-11-14 (Asia/Shanghai). Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: `AUTHOR_INTEGER_INTERVAL_CERTIFICATE / UNREVIEWED / NOT_ADMITTED`.
Scope: the **external auxiliary** 189-layer killed-Pascal BRC first-stop model, two independent Gamma clocks, and their maximum. It follows PREFIX-770/771 under unchanged model inputs.

## 1. Definitions and prior exact identities

For the survivor polynomials \(s(u)=(S_0(u),\ldots,S_{188}(u))\), put \(d=s'\), \(e=s''\), \(f=s'''\), and
\[
K_{ij}=\frac{\binom{i+j}{i}}{2^{i+j+1}},\qquad L_{ij}=(i+j+1)K_{ij}.
\]
For \(Y(p,z)=\max(C_p,C_z)\), set \(\mu=\mathbb E[Y]\), \(W=\operatorname{Var}(Y)\),
\[
A(p,z)=-\partial_p\partial_z\mu(p,z),\quad
D(p,z)=-\partial_p\partial_z W(p,z),\quad
Q(p,z)=\frac{A(p,z)}{D(p,z)}\quad(D>0).
\]
Let \(Q(u)=Q(u,u)\) on the diagonal. PREFIX-771 established
\[
Q''(u)=\frac{(A''D-AD'')D-2(A'D-AD')D'}{D^3},
\]
where primes are derivatives along the diagonal. PREFIX-770 established the transverse expansion
\[
Q(u+t,u-t)=Q(u,u)+Q_2(u)t^2+O(t^4),\qquad
Q_2(u)=\frac{A_2D-AD_2}{D^2}.
\]
The exact first/second jet and transverse formulas from those sources are reproduced algebraically in the checker.

## 2. Theorem 772.1: uniform diagonal and transverse positivity

Let
\[
I=\left[\frac{502971451}{10^{10}},\frac{502971452}{10^{10}}\right].
\]
For **every real** \(u\in I\), the frozen model satisfies
\[
\boxed{D(u,u)>0,\quad 4<Q''(u)<5,\quad 21<Q_2(u)<22.}
\]

**Proof and certificate.** Reconstruct the 189 survivor polynomials using the integer width predicate from PREFIX-771. The terminal survivor row is empty, and the 189 nonterminal rows contain exactly 9,529 nonzero positions. At every \(u=x/B\) with integer \(x_L\le x\le x_R\), each order-\(r\) derivative term (\(0\le r\le3\)) is an exact integer linear combination of signed, nonnegative monomials
\[
u^{k-a}(1-u)^{n-k-(r-a)}.
\]
Bound each unsigned monomial using \(x_L^{k-a}(B-x_R)^{n-k-(r-a)}\) from below and \(x_R^{k-a}(B-x_L)^{n-k-(r-a)}\) from above, divided by its known power of \(B\). Apply signs by reversing endpoints as needed. An integer common denominator \(B^{191}\) is valid for all four jets.

Use fixed-point rational intervals of scale \(F=10^{48}\): each lower endpoint is rounded **down** by integer floor, each upper endpoint **up** by integer ceiling. Apply the same outward enclosure to positive Gamma kernels \(K,L\). All subsequent sums, products, differences and bilinear contractions use integer interval arithmetic. Straight induction proves each resulting interval contains the exact expression at every real \(u\in I\).

The attached executable checks \(D_{\mathrm{lo}}>0\) and the following **strict exact-integer inequalities**, with \(N''=(A''D-AD'')D-2(A'D-AD')D'\) and \(N_2=A_2D-AD_2\):
\[
4(D^3)_{\mathrm{hi}}<(N'')_{\mathrm{lo}},\quad
(N'')_{\mathrm{hi}}<5(D^3)_{\mathrm{lo}},
\]
\[
21(D^2)_{\mathrm{hi}}<(N_2)_{\mathrm{lo}},\quad
(N_2)_{\mathrm{hi}}<22(D^2)_{\mathrm{lo}}.
\]
They establish the uniform claims. This verifies a **continuous interval**, rather than a sampled parameter grid. QED.

## 3. Theorem 772.2: unique stationary root and strict two-parameter minimum

PREFIX-771 supplies exact endpoint signs
\[
Q'(502971451/10^{10})<0<Q'(502971452/10^{10}).
\]
Since the preceding theorem proves \(Q''>4\) on \(I\), \(Q'\) is strictly increasing there. Its zero \(u_*\) exists by continuity and is **unique within \(I\)**.

Symmetry of \(Q(p,z)=Q(z,p)\) gives zero first transverse derivative along the diagonal; at \(u_*\), diagonal stationarity also gives zero gradient. Under local coordinates \(u=(p+z)/2\), \(t=(p-z)/2\), exchange symmetry makes the mixed \(u,t\) second derivative vanish at \(t=0\). The diagonal Hessian entries are \(Q''(u_*)>4\) and \(2Q_2(u_*)>42\). They are strictly positive, so the two-parameter Hessian is positive definite:
\[
\boxed{(u_*,u_*)\text{ is a strict local minimum of }Q(p,z).}
\]
This certifies both local diagonal uniqueness and full two-parameter local minimality, without requiring a global minimizer. QED.

## 4. Theorem 772.3: sharper critical-parameter upper bound

At the new rational witness
\[
u_0=\frac{5029714515}{10^{11}}=0.05029714515,
\]
a second exact outward-interval evaluation gives \(Q(u_0,u_0)\) approximately \(0.02851859116285760930849746304026\) for display. The actual certified inequality is the **integer cross-product**
\[
10^{21}A_{\mathrm{hi}}<28518591162857609310\,D_{\mathrm{lo}}.
\]
Consequently, using the PREFIX-763 curvature threshold definition,
\[
\boxed{0<q_c\le Q(u_0,u_0)<
\frac{28518591162857609310}{10^{21}}
=0.028518591162857609310.}
\]
This improves PREFIX-771's strict upper bound \(0.028518591162857609314\).

## 5. Reproduction, scope and next question

Execute the Python 3 standard-library script
`research_notes/portable_direct/PREFIX772_R6_UNIFORM_INTERVAL_HESSIAN_CHECK.py`.
The author-local run returned `ALL_CHECKS_PASS PREFIX772 UNIFORM_HESSIAN_AND_POINT_Q` and generated the complete structured result
`research_notes/portable_direct/PREFIX772_R6_UNIFORM_INTERVAL_HESSIAN_RESULTS.json`. The exact inequality assertions use integers only; displayed decimals are explanatory.

Dependencies: exact frozen input `f42f2906d77f24085c123f3ccfe9667d41caa96d`, PREFIX-770 transverse jet and PREFIX-771 diagonal jet and endpoint signs. Research status is `AUTHOR_INTEGER_INTERVAL_CERTIFICATE / UNREVIEWED / NOT_ADMITTED`.

The new local minimum need not be the global minimum on the complete \([0,1/2]^2\) auxiliary parameter domain. Next, compare potential off-diagonal and boundary extrema with this stationary pair, and use an exact Gamma sign certificate on a previously unverified \(1/768\) cell. The historical excluded-cell area is unchanged.
