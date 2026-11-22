# PREFIX-1001 — First finite-size correction for Stage46 X6 BRC first-interior probability

Date: 2026-11-22 (+08). Evidence: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Continuation of the verified PREFIX-1000 three-collision scalar law under the frozen Stage46 typed BRC candidate. No physical time calibration or new P000 axiom.

## Input and observer

Six primitive signed spatial directions live on the native X6 Cell torsor (six axes, twelve directed neighbours). Freeze P000 V5 at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d and the original Stage46 signed amplitude rule C[incoming,outgoing]=1/6-1[incoming=outgoing], for a unit initial incoming edge x0-e_i -> x0. For fixed n, let M_n denote the coherent squared norm of the grade n outer boundary and let M_(n,1) denote that of grade n-2, both summing distinct terminal incoming ports *after* interference within the Cell/port fibres.

Define the six-label collision probability Q_m=A_6(m)/36^m with A_6(m)=sum_(h_1+...+h_6=m) (m!/(h_1!...h_6!))². Earlier PREFIX-996 proved M_n=Q_(n-1)/6 and M_n~[9/(8 pi^(5/2))]n^(-5/2). PREFIX-998 proved M_(n,1)/M_n->35/4. PREFIX-1000 established the exact positive-terminal scalar expression, while PREFIX-999 supplies the negative-terminal flux.

## Lemma 1001.1 — Subleading coefficient of the collision probability

As m->infinity,

\[
Q_m=\frac{27}{4\pi^{5/2}}\,m^{-5/2}
\left(1-\frac{5}{8m}+O(m^{-2})\right). \tag{1}
\]

Moreover Q_m has a complete asymptotic expansion in integer powers of 1/m, to any fixed order, with a uniform remainder after that order for the adjacent indices m-1,m,m+1.

**Proof.** The exact multinomial collision is the constant term of S^m R^m/36^m, S=sum_(r=1)^6 x_r, R=sum_r x_r^(-1). Its torus Fourier integral has integrand

\[
\phi(\theta)^m,\quad
\phi(\theta)=\left|\frac16\sum_{r=1}^6e^{i\theta_r}\right|^2.
\]

Only a common phase has modulus one. Factoring out that phase leaves one nondegenerate maximum on the five-dimensional torus. In the local mean-zero six-angle chart, set \(\mu_k=(1/6)\sum_r\theta_r^k\). The local logarithm, by direct expansion, is

\[
\log\phi=-\mu_2+\frac{\mu_4}{12}-\frac{\mu_2^2}{4}
+O(\|\theta\|^6). \tag{2}
\]

Outside a fixed neighbourhood of the unique maximum the integrand is exponentially small in m. After the rescaling \(\theta=y/\sqrt m\), the leading Gaussian on \(\sum y_r=0\) has covariance \(3P\), with P the orthogonal projector onto that subspace. Each coordinate has variance 5/2. Therefore, for its Gaussian expectation,

\[
\mathbb E\mu_4(y)=75/4,\qquad
\mathbb E\mu_2(y)^2=35/4,
\]

and the quartic contribution to the relative 1/m coefficient equals

\[
\mathbb E\left[\frac{\mu_4(y)}{12}
-\frac{\mu_2(y)^2}{4}\right]
=\frac{75}{48}-\frac{35}{16}=-\frac58. \tag{3}
\]

The leading Gaussian factor is \(27/(4\pi^{5/2})\), equivalently the normal-density collision constant from the five-coordinate multinomial covariance, whose determinant is \(6^{-6}\). The local integrand and the phase-reduced torus are analytic, the Hessian is nondegenerate and the complement is exponentially suppressed. Expanding their scaled integrals through any fixed even order with Gaussian domination supplies the stated full expansion (including the uniform adjacent-index assertion); odd contributions vanish by inversion symmetry. Equations (2)–(3) give its explicitly needed first coefficient. QED.

The Fourier integral is an exact mathematical representation of the *already fixed* integer BRC collision count; it does not replace Stage46 dynamics with a classical matrix exponential or phase-propagation surrogate.

## Theorem 1001.2 — Sharp 1/n correction to the first-interior ratio

For each fixed initial incoming axis i, as n->infinity, setting t=n-2,

\[
\boxed{\frac{M_{n,1}}{M_n}
=\frac{35}{4}+\frac{15}{2t}+O(t^{-2}).} \tag{4}
\]

The terminal-sign contributions individually satisfy

\[
\boxed{\frac{M_{n,1}^{+}}{M_n}
=\frac{35}{4}+\frac{5}{t}+O(t^{-2}),\qquad
\frac{M_{n,1}^{-}}{M_n}
=\frac{5}{2t}+O(t^{-2}).} \tag{5}
\]

Here + and - refer to the actual last directed primitive step, not to the sign of an already-squared mass. The first-interior absolute mass also has the expanded asymptotic

\[
\boxed{M_{n,1}=\frac{315}{32\pi^{5/2}}\,n^{-5/2}
\left(1+\frac{153}{56n}+O(n^{-2})\right).} \tag{6}
\]

**Proof.** PREFIX-1000's exact scalar identity, with Q_m=A_6(m)/36^m, is

\[
6M_{n,1}^{+}=(t^2-2t-1)Q_{t+1}
-2t(t-2)Q_t+(t-1)^2Q_{t-1}. \tag{7}
\]

PREFIX-999 gives \(6M_{n,1}^{-}=Q_t-Q_{t+1}\), and \(6M_n=Q_{t+1}\). The coefficient sum in (7) is exactly zero. Substitute the full asymptotic expansion guaranteed by Lemma 1001.1,

\(Q_s=C s^{-\alpha}(1+a/s+b/s^2+\cdots)\), \(\alpha=5/2\), \(a=-5/8\).

Expand the three *adjacent arguments* s=t+1,t,t-1 to the order required by the quadratic t coefficients. The t² and t terms cancel exactly, while the constant and 1/t terms give

\[
\frac{6M_{n,1}^{+}}{Q_{t+1}}
=\alpha(\alpha+1)+\frac{7a+75/8}{t}
+O(t^{-2})
=\frac{35}{4}+\frac5t+O(t^{-2}). \tag{8}
\]

The coefficient b of the 1/s² term cancels from both displayed orders, so its explicit value is not needed; the analytic full expansion controls the remaining finite differences. The negative-terminal ratio is simply

\[
\frac{Q_t-Q_{t+1}}{Q_{t+1}}
=\frac{\alpha}{t}+O(t^{-2})=\frac{5}{2t}+O(t^{-2}).
\]

Adding proves (4)–(5). Finally (1) at m=n-1 yields

\[
M_n=\frac{9}{8\pi^{5/2}}\,n^{-5/2}
\left(1+\frac{15}{8n}+O(n^{-2})\right).
\]

Multiply by (4), using \(1/(n-2)=1/n+O(n^{-2})\), to obtain relative correction
\(15/8+(15/2)/(35/4)=15/8+6/7=153/56\), proving (6). QED.

## Exact integer numerical checks

No floating value is used in the formulas or equality checks. For each displayed n, generate A_6(m) from the exact integer recurrence in PREFIX-1000 and use the same proven three-collision formula to form the exact rational ratio R_n=M_(n,1)/M_n. Decimals below are only displays of those rational values:

| n | exact-rational R_n displayed | (n-2)(R_n-35/4) displayed |
|---:|---:|---:|
| 24 | 9.110596760695 | 7.933128735286 |
| 40 | 8.952704153838 | 7.702757845836 |
| 70 | 8.861775599451 | 7.600740762635 |
| 100 | 8.827212975277 | 7.566871577114 |
| 180 | 8.792332642418 | 7.535210350383 |
| 200 | 8.788037780187 | 7.531480477021 |
| 300 | 8.775236836337 | 7.520577228340 |

These finite checks agree with the new analytic 15/2 correction coefficient. Exact integer recurrence evaluation used built-in Python integers and Fraction and the same BRC-derived formulas already independently checked by the direct 12-port recurrence in PREFIX-1000 at n=1..7. The finite table is not the proof of the asymptotic.

A reproducible extension of the published PREFIX-1000 script is to import `collisions` and `scalar_components`, call `a=collisions(300)`, then for each n compute `p,z=scalar_components(n,a)` and the exact ratio `Fraction(6*(p+z),36**n) / Fraction(a[n-1],36**(n-1))`. Use `Fraction` in the comparisons.

## Scientific and control scope

The exact and asymptotic claims concern the declared Stage46 coherent BRC scalar observer on free native X6 Cells. The formula is not an observer-safe quotient after unspecified Link/Port gates, material occupancy or triadic feedback; the corresponding information-preserving relationship must be derived for each such operation. Updates are discrete counts rather than calibrated physical time. This work does not solve \(B_{\mathrm{fix,odd}}(32)\in\{19,20\}\).

Frozen sources and provenance: P000 V5@f42f2906; Stage46 BRC port model; PREFIX-996/997/998/999; PREFIX-1000 proof at 21c3b92e24ef4803260ee5506594a444dd88aec0, checker at 665f53b1fab1b6201a36410f9cdf6c7ab192f064 and exact certificate at aac2a78e4b3afa6219d9845823a4c7452379b58a. Historical Researcher EM-DIRECT-FBEA5D; original Activity RA-3FB2D033BE6048D8712FF056. No new formal CLAIM/PROGRESS or independent Review asserted.

**Next:** test whether a concrete X6 Link/Port occupation gate preserves the endpoint-summed scalar closed form; a one-link capacity gate is an immediate discriminating candidate. Where it fails, retain enough signed source/port state to compute the exact correction without substituting incoherent path mass.
