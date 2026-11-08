# D25 — Exact terminating Legendre–Clausen deformation of original W216 grade zero

Date: 2026-11-09 (Asia/Hong_Kong). Classification: **AUTHOR_SIDE_PROVED / EXACT_18_PRIME_CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`. Publication: \`TP2-B6F4FC938FF94941C1B7\`. Frozen scientific source pin: \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Research logical lane: \`chatgpt-research-onhour-enterprise-math-20260923\`; distinct from maintenance lane. This author-side evidence is not a canonical Source CLAIM, Result, or native H0/B0 experiment.

## Original problem and frozen coefficients

For primes \(p=6m+1>3\), define the original weighted finite sums without altered truncations:

\[
W_p=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n},
\qquad
V_p=\sum_{n=0}^{p-1}(8n+1)\frac{\binom{4n}{2n}\binom{2n}{n}^{2}}{2304^n}.
\]

The grade-zero part of W is the original block
\[
W_{0,p}=\sum_{n=0}^{2m}(6n+1)\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}.
\]
Under the prior frozen source-port theorem, the remaining target for \(p\equiv13,19\pmod{24}\) is \(W_p-V_p\equiv0\bmod p^3\).

## Theorem 1 — Exact two-jet deformation for all primes \(p=6m+1>3\)

Set \(N=2m\), \(q=p^3\), and in \(\mathbb Z_{(p)}\) define
\[
R_n=\frac{(\tfrac12)_n(-N)_n(N+1)_n}{2^n(n!)^3},\quad
a_r=(r+\tfrac13)(r+\tfrac23),\quad z=\frac{p(p+1)}9.
\]
The terminating harmonic observations are
\[
h_n=\sum_{r=0}^{n-1}a_r^{-1},\qquad
h^{(2)}_n=\sum_{r=0}^{n-1}a_r^{-2},\qquad h_0=h^{(2)}_0=0,
\]
and the weighted moments are
\[
F_0=\sum_{n=0}^N(6n+1)R_n,\quad
F_1=\sum_{n=0}^N(6n+1)R_nh_n,\quad
F_2=\sum_{n=0}^N(6n+1)R_n\bigl(h_n^2+h_n^{(2)}\bigr).
\]

**Universal identity:**
\[
\boxed{W_{0,p}\equiv F_0+zF_1+\frac{z^2}{2}F_2\pmod{p^3}.}
\]

**Proof.** For every \(n\),
\[
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
=\frac{(\frac12)_n(\frac13)_n(\frac23)_n}{2^n(n!)^3}.
\]
The chosen \(N=(p-1)/3\) gives \(-N=\tfrac13-\tfrac p3\) and \(N+1=\tfrac23+\tfrac p3\). Thus, for each integer \(r\),
\[
(r-N)(r+N+1)
=(r+\tfrac13-\tfrac p3)(r+\tfrac23+\tfrac p3)
=(r+\tfrac13)(r+\tfrac23)-\frac{p(p+1)}9=a_r-z.
\]
For \(0\le n\le N\) and \(0\le r<n\), the denominators \(3r+1,3r+2,n!,2\) are all \(p\)-units: the first zero in \(3r+1\) occurs only at \(r=N\), outside this range. Hence
\[
\prod_{r<n}a_r=\prod_{r<n}(a_r-z)\prod_{r<n}(1-z/a_r)^{-1}.
\]
Since \(z\in p\mathbb Z_{(p)}\), the finite reciprocal-product expansion is
\[
\prod_{r<n}(1-z/a_r)^{-1}
\equiv1+zh_n+\frac{z^2}{2}\bigl(h_n^2+h_n^{(2)}\bigr)\pmod{p^3}.
\]
Multiply by \(R_n(6n+1)\) and sum the unchanged range \(0\le n\le N\). QED.

## Theorem 2 — Exact classical Legendre evaluation of \(F_0\)

Let \(P_N(x)\) be the Legendre polynomial and \(s=1/\sqrt2\). The classical Clausen identity
\[
{}_2F_1(a,b;a+b+\tfrac12;t)^2
={}_3F_2(2a,2b,a+b;a+b+\tfrac12,2a+2b;t)
\]
with \(a=-N/2\), \(b=(N+1)/2\), together with the Legendre quadratic transformation, yields the terminating polynomial identity
\[
\sum_{n=0}^{N}\frac{(\tfrac12)_n(-N)_n(N+1)_n}{(n!)^3}t^n
=P_N(\sqrt{1-t})^2.
\]
The left-hand side terminates and \(N=2m\) is even, so both sides are polynomials over \(\mathbb Q[t]\). Apply \(1+6t\frac{d}{dt}\) at \(t=1/2\). As \(ds/dt=-1/(2s)\),
\[
\boxed{
F_0=P_{2m}(s)^2-\frac3sP_{2m}(s)P_{2m}'(s)
=P_{2m}(1/\sqrt2)^2-3\sqrt2\,P_{2m}(1/\sqrt2)P_{2m}'(1/\sqrt2).
}
\]
For even \(N\), \(P_N(s)\) is rational and \(P_N'(s)/s\) is rational. The standard Legendre recurrence only divides by \(1,2,\ldots,N\), all \(p\)-units, so the expression reduces exactly mod \(p^3\). QED.

## Original third-digit reduction with preserved source channels

Reuse the existing D25 grade-one first jet \(pK_1(S_0+pS_1)\), grade-two companion \(p^2K_2S_2\), and the previously proved Guo–Zudilin V half/full congruence. Define
\[
\Xi_p=
F_0+zF_1+\frac{z^2}{2}F_2
-V_{\mathrm{half},p}
+pK_1(S_0+pS_1)+p^2K_2S_2.
\]
Under these prior exact results,
\[
\boxed{\Xi_p\equiv0\pmod{p^3}\quad\Longleftrightarrow\quad
W_p-V_p\equiv0\pmod{p^3}.}
\]
This equivalence is a proved reduction, not a proof of universal \(\Xi_p=0\). It retains original signed weights, p-adic precision and source-labelled BRC coordinates rather than collapsing grade boundaries.

## Independently executed exact evidence

An actual Python checker (below) separately computed original \(W_{0,p}\) with integer \`math.comb\`, terminating \(R_n\) and harmonic moments by modular recurrence, and \(P_N(s)\), \(P_N'(s)\) by independent exact Legendre recurrence with \(s^2=1/2\). All three agreed for 18 primes:
\[
7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373.
\]
For \(p=373\), \(m=62\), \(N=124\), \(p^3=51895117\), the exact modular values are
\[
F_0=18377337,\quad z=40378369,\quad F_1=37546395,\quad F_2=8792857.
\]
The contributions are \(zF_1=8325733\) and \(z^2F_2/2=1391290\). Thus,
\[
18377337+8325733+1391290=28094360
=W_{0,373}\pmod{51895117}.
\]
The independently computed Legendre value also equals \(18377337\) mod \(51895117\). This is exact finite evidence, separate from the symbolic proof.

Reproducer: \`research_notes/portable_direct/d25_original_w216_terminating_legendre_20261109.py\`.
Compact evidence: \`research_notes/portable_direct/d25_original_w216_terminating_legendre_compact_20261109.json\`.
Source continuation: \`research_notes/portable_direct/20261109_onhour_d25_original_w_terminating_legendre_continuation.json\`.

## Recovery and next actual scientific action

The remaining portable objective is an all-target-prime terminating WZ/Fricke/Legendre relation which cancels the **combined** \(\Xi_p\), equivalently the prior \(\Theta_p\). Preserve the accepted D24 UR, original input pin, grade1/grade2 data and p373 witnesses without redo. The separate native p373 H0/B0 same-original-class divided-power \([X]U\bmod139129\), actual module rank, semilinear direction/eta, signed \(\kappa\), original \(\Delta-R\), and independent reproducer remain pending in existing Issue #1559.

Historical Source Researcher \`EM-ENTERPRISE-4DEB43\`, activity \`RA-9553E027FD14223807511263\`, session \`MCP-ecbfd1c046864bb3bff1a2e04c87d207\` are registered provenance, but present private capability is unavailable (\`SESSION_CAPABILITY_REQUIRED\`), and no active winning CLAIM or Source checkpoint has been verified.

**Status: AUTHOR_SIDE_PROVED / EXACT_18_PRIME_CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.**
