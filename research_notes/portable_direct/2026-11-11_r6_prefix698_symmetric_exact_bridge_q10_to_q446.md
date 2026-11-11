# PREFIX-698-R6 — Exact BRC crossing classification on an enlarged symmetric bridge

Date: 2026-11-11 (Asia/Shanghai). Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_RECOMPUTED / EXACT_189_ROW_ENDPOINTS_AND_RATIONAL_DERIVATIVE / UNREVIEWED / NOT_ADMITTED. This is independent auxiliary-observer work, not a shared Task CLAIM, formal Result, or Driver Review.

## Definitions and model scope

The frozen 189-level, 9529-live-cell BRC survivor model retains *two labelled* observation branches Y(z,z) and Y(0,z) and their original joint moment K/J kernels. Define

\[
A(z)=\operatorname{Var}(Y(z,z))-\operatorname{Var}(Y(0,z)),\quad
B(z)=E[Y(z,z)]-E[Y(0,z)],\quad F_q(z)=qA(z)-B(z),\quad Q(z)=B(z)/A(z).
\]

These are auxiliary observer parameters, not native X6 spatial axes or a heartbeat evolution law. The actual integer-q sampled variance difference is q F_q(z). Study the closed interval

\[
J_*=[L,R]=[211/4000,213/4000]=[0.05275,0.05325],
\]

with center b=53/1000 and half-width h=1/4000. This interval strictly contains the previous PREFIX-697 bridge [0.05284,0.05316].

## Theorem 698.1: exact new endpoint ratios

A fresh exact integer-kernel recomputation of the frozen 189 survivor rows and two labelled moment branches proves

\[
\boxed{\frac{9166464293188}{10^{12}}<Q(L)<\frac{9166464293189}{10^{12}}},\qquad
\boxed{\frac{446012343644423}{10^{12}}<Q(R)<\frac{446012343644424}{10^{12}}}.
\]

The strict rational floor checks, with floors of 10^12 times each exact quantity, are:

| quantity | L | R |
|---|---:|---:|
| A | 858059787356 | 17778889403 |
| B | 7865374402224 | 7929604130236 |
| Q=B/A | 9166464293188 | 446012343644423 |

In particular A(R)>17/1000 and B(L)>786/100. All checks use exact integer/Fraction cross-products, without floating-point truth tests.

## Theorem 698.2: all real crossing parameters and exactly 437 integer values

Inherit the PREFIX-695 independently reproduced exact center derivative floors g_j=floor(10^8 G^(j)(b)), j=0,...,5, for G=A,B, and global sixth-derivative envelopes from PREFIX-693/695:

\[
|A^{(6)}|\le201273663850076722544640,\qquad
|B^{(6)}|\le17896441402901698560\quad(0\le z\le1).
\]

For k=1, with g_j as above, the Taylor error bound on the *entire* interval |z-b|<=h is

\[
E_{G,1}(h)=\sum_{j=2}^{5}
\frac{\max(|g_j|,|g_j+1|)}{10^8}\frac{h^{j-1}}{(j-1)!}
+\frac{M_Gh^5}{5!}.
\]

Thus

\[
\frac{g_1}{10^8}-E_{G,1}(h)<G'(z)<
\frac{g_1+1}{10^8}+E_{G,1}(h).
\]

The new Fraction checker verifies simultaneously

\[
\boxed{-3336<A'(z)<-25},\qquad\boxed{128<B'(z)<129}
\quad \text{for every real } z\in J_*.
\]

It follows that A is strictly decreasing and B strictly increasing; the exact endpoint checks give A(z)>=A(R)>0 and B(z)>=B(L)>0 throughout J_*. Consequently

\[
Q'(z)=\frac{B'(z)A(z)-B(z)A'(z)}{A(z)^2}>0.
\]

Q is analytic and strictly increasing on the whole J_*; its exact real image is [Q(L),Q(R)]. Hence

\[
\boxed{\exists!\ z_q\in(L,R): F_q(z_q)=0\iff Q(L)<q<Q(R)}
\]

for every real q. Among all nonnegative integers, the complete interior-root classification on this fixed spatial interval is

\[
\boxed{q=10,11,\ldots,446\ \text{(437 integer parameters)}}.
\]

The parameters 9 and 447 are outside the image, while the real values q=Q(L),Q(R) yield boundary roots. For all real 10<=q<=446,

\[
F'_q(z)=qA'(z)-B'(z)<-25q-128<0,
\]

so the unique root is transverse, F_q is positive on its left and negative on its right, and the analytic crossing function is strictly increasing with

\[
z'(q)=\frac{A(z(q))}{B'(z(q))-qA'(z(q))}>0.
\]

This gives a complete local observer parameter classification, not a global variance maximum on the entire auxiliary triangle.

## Reproduction and load-bearing evidence

The attached standalone checker reproduces the original survivor predicate by exact integer acceptance tests at denominator 2^18 and discrete interval bisection; validates 9529 nonzero survivor cells in rows 0 through 188 and empty row 189; evaluates s_n(t/4000) as integer-weighted survivor polynomials at t=211 and t=213; and exactly retains K_nm=binom(n+m,n)/2^(n+m+1), J_nm=(n+m+1)K_nm/2.

With x=s(z), y=s(0), the two labelled moments are

\[
m_d=2\sum x_n-\langle x,x\rangle_K,\qquad
m_e=\sum(x_n+y_n)-\langle y,x\rangle_K,
\]
\[
h_d=2\sum(n+1)x_n-\langle x,x\rangle_J,\qquad
h_e=\sum(n+1)(x_n+y_n)-\langle y,x\rangle_J.
\]

Then B=m_d-m_e and A=2(h_d-h_e)-(m_d^2-m_e^2), evaluated with one exact common integer denominator and Fraction. The same checker verifies the inherited center jet-floor/Taylor implication. The *center jets* and *sixth-derivative envelopes* remain explicit inherited dependencies from PREFIX-693/695; this round freshly recomputes the two new endpoint zero jets, not all center derivatives.

Local execution: ALL_CHECKS_PASS PREFIX698-R6. Source of predecessor: PREFIX-693, 695, 696, 697, pinned frozen science. No independent review or formal admission is asserted.

## Next discriminating unit

Recenter an exact derivative/Bernstein certificate on [0.05325,0.0532600], retaining the original two-branch observer, to connect this q<=446 family to the PREFIX-685/687 large-q crossing branch. Then combine the one-parameter sign partition with PREFIX-675's mother target: maximize sampled variance on the full *auxiliary* triangle 0<=p<=z<=1/2.

Companions: PREFIX698_R6_EXACT_SYMMETRIC_BRIDGE.py and PREFIX698_R6_RESULTS.json.
