# RH full-integer road: explicit tails and holomorphic parameter dependence above the half-line

Date: 2026-11-15. Derivation: RESEARCH_DRIVER EM-DVR-DEBB5E. Original RH-ROAD-TAIL full-integer road and mathematical program: EM-FREE-C4A91D. Status: author-side proved auxiliary result; no independent native review or formal Result admission. This note strengthens the previously saved compact-real-parameter tail estimate without changing the original RH objective.

## Exact definitions and theorem

For a complex parameter \(a\) with \(\Re a>0\), use the analytic extension of the *same* full-integer Möbius road:
\[
R_a(n)=\prod_{p\mid n}(1-p^{-a})
=\sum_{d\mid n}\mu(d)d^{-a},\qquad
c_a=\frac1{\zeta(1+a)}=\sum_{d\ge1}\frac{\mu(d)}{d^{1+a}},
\]
\[
B_{a,N}=\sum_{n\le N}R_a(n)-1-(N+\tfrac12)c_a.
\]
Both series identities are exact; \(c_a\) is absolutely convergent for \(\Re a>0\). They preserve every integer, composite and prime power. For real \(a>0\), these are exactly the original definitions.

**Theorem.** For every fixed \(b\) with \(1/2<b<1\), set
\[
C_b=2+\frac{1}{1-b}+\frac1b+\frac{\zeta(1+b)}2.
\]
For every complex \(a\) with \(\Re a\ge b\), every integer \(N\ge1\) and \(L\ge1\),
\[
|B_{a,N}|\le C_b N^{1-b},\qquad
\boxed{\quad\sum_{N>L}\frac{|B_{a,N}|^2}{N^2}
\le\frac{C_b^2}{2b-1}L^{1-2b}.\quad}
\]
Consequently the \(\ell^2\)-valued map
\[
a\longmapsto V(a)=\bigl(B_{a,N}/N\bigr)_{N\ge1}
\]
is **holomorphic on the complex half-plane \(\Re a>1/2\)**. The bound holds uniformly over the entire unbounded region \(\Re a\ge b\), including arbitrarily large imaginary parts; in particular it yields an explicit real-parameter uniform rate on \([b,\infty)\).

## Proof

Write \(S_a(N)=\sum_{n\le N}R_a(n)\). Since the inner divisor sum is finite, Möbius inversion and absolute convergence of \(c_a\) give
\[
S_a(N)-Nc_a
=\sum_{d\le N}\mu(d)d^{-a}\left(\left\lfloor N/d\right\rfloor-N/d\right)
-N\sum_{d>N}\mu(d)d^{-1-a}.
\]
For \(\Re a\ge b\), taking moduli yields
\[
|S_a(N)-Nc_a|
\le\sum_{d\le N}d^{-b}+N\sum_{d>N}d^{-1-b}.
\]
Comparison with the corresponding monotone integrals gives
\[
\sum_{d\le N}d^{-b}\le 1+\frac{N^{1-b}-1}{1-b},\qquad
N\sum_{d>N}d^{-1-b}\le\frac{N^{1-b}}b.
\]
Also \(|c_a|\le\zeta(1+b)\). Since \(B_{a,N}=S_a(N)-Nc_a-1-c_a/2\) and \(N^{1-b}\ge1\), the first boxed bound follows with the stated \(C_b\). The tail follows by comparing \(\sum_{N=L+1}^{\infty}N^{-2b}\) with \(\int_L^\infty x^{-2b}dx=L^{1-2b}/(2b-1)\).

Each coordinate \(a\mapsto B_{a,N}/N\) is holomorphic on \(\Re a>0\): \(R_a(n)\) is a finite exponential polynomial and \(c_a\) has a locally absolutely convergent Dirichlet series there. Let \(K\) be a compact subset of \(\Re a>1/2\); choose \(b\in(1/2,\min_{a\in K}\Re a)\) with \(b<1\). The uniform tail bound shows that finite-coordinate truncations \(P_{\le L}V(a)\) converge to \(V(a)\) locally uniformly in the Banach space \(\ell^2\). By the Banach-valued Weierstrass theorem, \(V\) is holomorphic. QED.

## Position relative to the prior road results

The earlier unconditional theorem (GitHub commit `5256127bafc0987116bf2e508a50b62a78113190`, blob `c1ec667a880a6f5d288d96f2d26a603425f8d8dc`) established \(E_a<\infty\) for every real \(a\ge1/2\), including the difficult endpoint, and compact real-parameter uniform tails using a Hardy–Paley–Wiener argument. The present elementary bound supplies an **explicit algebraic decay rate** for \(\Re a>b>1/2\) and a complex-analytic \(\ell^2\) continuation above the half-line. It does not assert the same algebraic estimate at \(a=1/2\) and does not approach the RH-sensitive small-parameter limit \(a\downarrow0\).

Source dependencies: exact original integer-road definitions and Möbius convolution; no unproved mathematical premise, no RH, no formal checker. No new Native Result review, Task completion or parent-objective completion is claimed.
