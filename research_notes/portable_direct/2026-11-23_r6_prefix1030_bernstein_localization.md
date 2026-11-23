# PREFIX-1030 — Bernstein localization of the signed spectral functional and exact positive witnesses through total degree 5000

Date: 2026-11-23 (Asia/Shanghai). Parent: PREFIX-1029. Research status: AUTHOR_ANALYTIC_PROOF + EXACT_INTEGER_CHECK + CONDITIONAL_DENSITY_LOCALIZATION / NOT_REVIEWED.

## Frozen input and observer

The scientific input remains `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json` (P000 V5). We use the unchanged Stage46 candidate signed BRC kernel `W=J12-6I12`, incoming `-e1`, bidirectionally forbidden Link `{0,e1}`, exactly one negative outgoing step, and the coherent X6 Cell–terminal-port–grade square-mass observer. In particular, the contrast sequence and the six-phase Laurent spectrum are observer outputs, not a quotient that can replace native signed state or native Cell identity.

Recall from PREFIX-1026 and PREFIX-1028:
- \(\mu\) is a probability measure on \([0,36]\), the spectral pushforward of the six phases, with \(\int y^r\,d\mu=A_6(r)\).
- \(\nu\) is the fixed real linear functional on polynomials (and continuously differentiable test functions) satisfying
\[
5\nu[f]=-4\int y^2(y-36)^2 f'(y)\,d\mu(y)
-2\int y(y-36)(17y-91)f(y)\,d\mu(y)
+12\int(6-y)\int_0^y(11+x)f(x)\,dx\,d\mu(y).
\]
- \(a_m=\nu[y^m]\), including formal \(a_0=2412\), and \(E_{m,k}=\nu[y^m(36-y)^k]\), so \(E_{m,k+1}=36E_{m,k}-E_{m+1,k}\). The native physical port contrast is asserted only for \(m\ge1\).

## Theorem A — exact distributional spectral localization

Put \(H(y)=y^2(36-y)^2\), \(P(y)=y(y-36)(17y-91)\), and \(F(x)=\int_{[x,36]}(6-y)\,\mu(dy)\). As a distribution on the real line (restricted to \([0,36]\)),
\[
\boxed{\quad5\nu=4\,\partial_y(H\mu)-2P\mu+12(11+y)F(y)\,dy.\quad}
\]
Here \((\partial_y T)[f]=-T[f']\). The statement is unconditional for the frozen \(\mu\) and all smooth test functions: the first term can be a distribution and is not assumed to be a positive measure.

**Proof.** Distributional differentiation transforms the first defining integral exactly into \(4\partial_y(H\mu)\). Fubini transforms the final integral into \(\int_0^{36} (11+x)f(x)F(x)\,dx\), because the integrands are bounded on the compact interval. This gives the identity without any smooth-density hypothesis.

On any open \(I\subset(0,36)\) where \(\mu\) has a \(C^1\) density \(\rho\) and no additional singular component, the restriction of \(\nu\) has the ordinary density
\[
\boxed{\quad g(y)=\frac15\left(4(H(y)\rho(y))'-2P(y)\rho(y)+12(11+y)F(y)\right).\quad}
\]
Its sign is the precise local obstruction to globally positive spectral representation; this formula does **not** establish that sign.

## Theorem B — exact Bernstein probes and their local limit

For \(n=m+k\) define the normalized Bernstein probe
\[
D_{m,k}:=\frac{(n+1)\binom nm}{36^{n+1}}E_{m,k}.
\]
The factor is exact: \(D_{m,k}=\nu[b_{m,k}]\) for the normalized Beta kernel \(b_{m,k}(y)=(n+1)\binom nm y^m(36-y)^k/36^{n+1}\), whose ordinary Lebesgue integral is 1.

If the distribution \(\nu\) has a continuous density \(g\) in a neighborhood of \(y_*=36t\), \(0<t<1\), with its remaining distributional support separated from \(y_*\), then for any integers \(m,k\to\infty\) satisfying \(m/(m+k)\to t\),
\[
\boxed{D_{m,k}\longrightarrow g(36t).}
\]
The same conclusion holds under a global finite signed-density representation with \(g\) continuous at \(36t\). In the latter case, if \(g\) is \(L\)-Lipschitz on \([0,36]\), the explicit localization error is
\[
|D_{m,k}-g(36m/n)|\le36L\left(\frac1{n+2}+\frac1{2\sqrt{n+3}}\right).
\]

**Proof.** With \(U\sim{\rm Beta}(m+1,k+1)\), the normalized integral against \(g\) is \(\mathbb E[g(36U)]\). Beta concentration gives \(U\to t\) in probability. The Lipschitz bound follows from \(|\mathbb EU-m/n|\le1/(n+2)\) and \(\operatorname{Var}U\le1/(4(n+3))\). A distribution supported outside a fixed neighborhood contributes only an exponentially smaller quantity: its fixed finite order derivatives acting on the sharply localized Bernstein kernel do not defeat exponential separation. Hence the local statement.

**Consequence.** If some regular interior point has \(g(y_*)<0\), then all sufficiently large proportional probes tending to \(y_*\) are negative and explicitly refute global Hausdorff positivity. Conversely, positive probes throughout a finite triangle are finite evidence, not a pointwise sign proof.

## Theorem C — finite exact positivity implies a quantitative C³ positivity certificate

Assume only \(E_{m,k}\ge0\) for all \(m,k\ge0\) with \(m+k=N\). Then for every nonnegative \(f\in C^3([0,36])\), the original signed functional satisfies
\[
\boxed{\displaystyle
\nu[f]\ge-\frac{C_2\|f''\|_\infty+C_3\|f'''\|_\infty}{N},\qquad
C_2=1617408+\frac{324}{5}\sqrt{581720790},\quad C_3=5552064.
}
\]
The conclusion is a uniform lower bound on infinitely many nonnegative smooth observers from one exact finite triangle; it does not assume a density for \(\nu\).

**Proof.** Let \(B_Nf(y)=\sum_{m=0}^N f(36m/N)\binom Nm(y/36)^m(1-y/36)^{N-m}\). All coefficients \(f(36m/N)\) are nonnegative, so by the verified probes \(\nu[B_Nf]\ge0\).

Writing \(M_2=\|f''\|_\infty,M_3=\|f'''\|_\infty\), elementary binomial Taylor estimates give
\[
\|B_Nf-f\|_\infty\le162M_2/N,\qquad
\|(B_Nf)'-f'\|_\infty\le(18M_2+216M_3)/N.
\]
For the second estimate, represent \((B_Nf)'=\mathbb Ef'(36(J+U)/N)\) with \(J\sim{\rm Bin}(N-1,y/36)\), independent \(U\sim{\rm Uniform}[0,1]\). The displacement \(Z=36(J+U)/N-y\) has \(|\mathbb EZ|\le18/N\) and \(\mathbb EZ^2\le432/N\), giving the stated \(C^3\) Taylor bound.

The exact six-phase moment values \(A_6(1)=6,A_6(2)=66,A_6(3)=996,A_6(4)=18306\) yield
\[
\int H\,d\mu=A_6(4)-72A_6(3)+1296A_6(2)=32130,
\]
and the exact squared-polynomial identity gives \(\int P^2\,d\mu=581720790\). Cauchy–Schwarz bounds \(\int|P|d\mu\) by its square root, while
\[
\int|6-y|(11y+y^2/2)\,d\mu\le30(11A_6(1)+A_6(2)/2)=2970.
\]
Insert both Bernstein errors into the defining formula for \(\nu\). Its derivative coefficient is \((4/5)32130=25704\); its function coefficient is bounded by \((2/5)\sqrt{581720790}+7128\). Combining the bounds yields the exact constants \(C_2,C_3\), and \(\nu[B_Nf]\ge0\) finishes the proof.

**Further consequence.** If the exact positive triangle extends to arbitrarily large N, this bound proves \(\nu[f]\ge0\) for every \(C^3\) nonnegative \(f\), and hence yields its unique positive Radon measure extension of total mass 2412. This is a direct Bernstein/functional proof of the infinite-positive-measure implication, distinct from any finite-N acceptance claim.

## Exact computation: total degree at most 5000

The attached Python script recomputes the exact A6 collision recurrence, the original three-shift rational formula for every \(a_m\), and the complete difference triangle \(E_{m,k}\) for \(m,k\ge0,m+k\le5000\). It uses Python integers and `Fraction`; signs are tested without floating-point operations.

**Result:** all \((5001)(5002)/2=12,507,501\) integer entries are strictly positive. This extends PREFIX-1028's exact N=1200 frontier (721,801 entries). Its original full-triangle SHA-256 `a7565656208a7ff3f6fd9ff269a63879b8e0d3e76c3537dcaf130e7241e60d06` and original m≥1 hash `b626fc2e4e12db5ce219ab6f5e69f0c0344f38d6fe63d189a768a935d888439e` were independently reproduced in a separate N=1200 run. The first five a_m are `[2412,25620,386028,7124592,149251656]`.

The \(D_{m,k}\) values at N=5000, obtained as exact rational numbers and displayed in decimal, include:
| m/5000 | spectral y | D (approximate density probe) |
|---|---:|---:|
| 250/5000 | 1.8 | 118.291065925357 |
| 500/5000 | 3.6 | 160.079166872370 |
| 1000/5000 | 7.2 | 149.704319437834 |
| 1666/5000 | 11.9952 | 123.673177997036 |
| 2500/5000 | 18 | 59.302841660713 |
| 3333/5000 | 23.9976 | 32.652760783394 |
| 4000/5000 | 28.8 | 10.880024473284 |
| 4500/5000 | 32.4 | 2.138607385783 |
| 4750/5000 | 34.2 | 0.398650955597 |

All density-probe figures are numerical values of **exact nonnegative rational Bernstein statistics**; identifying their limits with a continuous density at each point requires the analytic hypotheses in Theorem B. The full data record contains each sample's exact parameters and high-precision decimal.

## Next discriminating question

Prove regularity of the six-phase spectral density on each interval cut by the critical levels 0,4,16,36, and establish or refute \(g(y)\ge0\) using the explicit local formula. An exact negative proportional Bernstein probe would refute global positivity. Otherwise obtain interval-wise lower bounds sufficient for a pointwise positivity proof, including treatment at critical levels and any singular distributional terms. Keep the unchanged X6 signed/provenance observer: a positive spectral approximation is an observer-level result, not a lossless reduction of the native BRC state.

Files: `PREFIX1030_R6_BERNSTEIN_LOCALIZATION_CHECK.py` and `PREFIX1030_R6_INTERIOR_CERTIFICATE.json`. Historical contributor provenance: `EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056`, original SID `MCP-45ad6d29cd534c1aad25595a72e3c532`; current formal execution authority not established. No shared CLAIM, PROGRESS, Result, Review, theorem promotion, P000 edit, or closed mother problem is asserted. Mother objective `B_fix,odd(32) in {19,20}` remains open.
