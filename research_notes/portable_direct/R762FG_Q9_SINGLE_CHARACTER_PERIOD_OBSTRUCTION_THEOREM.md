# R762FG — Exact single-character 3-adic obstruction to high-precision q=9 BRC periods

Date: 2026-11-19 (Asia/Shanghai).
Status: **AUTHOR_PROVED / EXACT_INTEGER_CHECK_PASSED / NOT_REVIEWED**.
Frozen taskbook: `awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md`.
Predecessors: R762ET, R762EZ/FA, R762FE/FF. This is a result for the positive, six-named-branch three-coordinate BRC research slice, **not** a native signed Cell/Link/Port update, Task CLAIM, Source Result or independent review.

## Definition

In `R = Z[(Z/9Z)^3]`, retain all 729 terminals and the named steps of

\[
P=1+X+Z+XY+YZ+XYZ,\quad X^9=Y^9=Z^9=1.
\]

For \(n\ge9\), put \(f(n)=\lfloor n/3\rfloor-2\). When the coefficientwise quotient is integral, set \(S(n)=3^{-f(n)}P^n\in R\). Its reduction modulo \(3^h\) is the full normalized shadow. Integrality for all \(n\ge9\) is an author-side result of the preceding R762ER work; the new obstruction below only assumes integrality of compared normalized states, and does not use the prior 127-factor spectral calculation.

## Theorem FG1 — exact one-character discrepancy valuation

Let \(\zeta\) be a primitive ninth root of unity and consider the integral character

\[
\chi:R\longrightarrow \mathbb Z[\zeta],\qquad
(X,Y,Z)\longmapsto(1,\zeta,\zeta^2).
\]

Extend \(v_3\) to \(\mathbb Q_3(\zeta)\), normalized by \(v_3(3)=1\). For **every** multiple of three \(n\ge9\) and every positive integer \(L\), the valuation of the evaluated normalized difference is exactly

\[
\boxed{
v_3\bigl(\chi(S(n+L)-S(n))\bigr)=
\begin{cases}
2,&3\nmid L,\\
2,&L=3m,\ 6\nmid m,\\
3+v_3(m/6),&L=3m,\ 6\mid m.
\end{cases}
}
\]

It is independent of the chosen multiple-of-three \(n\).

## Corollary FG2 — every high-precision eventual period grows exponentially

For any integer \(h\ge3\), if the **entire 729-coordinate** normalized sequence \(S(n)\bmod3^h\) has eventual positive period \(L\), then

\[
\boxed{18\cdot3^{h-3}\mid L.}
\]

This is a *necessary divisibility condition*, not a new upper bound or a claim that the displayed number itself is a period. The earlier author-side observation \(T_h=18\cdot3^{h-1}\) for \(h\le8\) is compatible with it. At \(h\ge3\), this universal lower bound leaves a factor-nine gap relative to that proposed exact period. It is not deduced by extrapolating the finite \(h=1,\dots,8\) data.

## Proof and exact cyclotomic certificate

The selected character of the six-branch polynomial is

\[
\lambda=\chi(P)=2+\zeta+\zeta^2+2\zeta^3.
\]

Since \(\Phi_9(\zeta)=\zeta^6+\zeta^3+1=0\), direct integral reduction proves

\[
\lambda^3=3\beta,\qquad
\boxed{\beta=-7-2\zeta+2\zeta^2+5\zeta^4+7\zeta^5\in\mathbb Z[\zeta].}
\]

All congruences below hold in the six-dimensional free integral basis \(1,\zeta,\ldots,\zeta^5\):

\[
\beta^3\equiv-1\pmod3,\quad
\beta^2\not\equiv1\pmod3,\quad
\beta^6-1\equiv3\zeta+6\zeta^2+6\zeta^4+3\zeta^5\pmod9.
\]

Consequently \(\beta\bmod3\) is a unit of **exact order six** in \((\mathbb Z[\zeta]/3)^*\), and \(v_3(\beta^6-1)=1\). Write \(\beta^6=1+3u\) with \(u\in\mathbb Z_3[\zeta]^\times\). Ordinary binomial lifting for the odd prime \(3\) proves for every positive integer \(t\):

\[
\boxed{v_3(\beta^{6t}-1)=1+v_3(t).}
\]

This is a general symbolic identity, not a computational guess. From \(\lambda^3=3\beta\) and \(\beta\) being a 3-adic unit we have \(v_3(\lambda)=1/3\).

Fix \(n=3k\ge9\). Then \(f(n)=k-2\), whence

\[
v_3\left(\frac{\lambda^n}{3^{f(n)}}\right)=2.
\]

Write \(L=3m+r\), \(r\in\{0,1,2\}\). Since \(n\) is a multiple of three, \(f(n+L)-f(n)=m\) and

\[
\chi(S(n+L)-S(n))
=\frac{\lambda^n}{3^{f(n)}}
\left(\frac{\lambda^L}{3^m}-1\right).
\]

For \(r\ne0\), the first term inside the parentheses has valuation \(r/3>0\), so the parentheses are a 3-adic unit. The discrepancy valuation equals two. If \(r=0\), the parentheses are \(\beta^m-1\), with valuation zero unless \(6\mid m\), when the lifting identity gives \(1+v_3(m/6)\). This proves FG1.

If the complete terminal difference lies in \(3^hR\), its integral character evaluation lies in \(3^h\mathbb Z[\zeta]\). For an eventual period \(L\), choose any sufficiently late multiple of three \(n\). As \(h\ge3\), FG1 rules out the first two cases. The third forces \(3+v_3(m/6)\ge h\), equivalently \(6\cdot3^{h-3}\mid m\), hence \(18\cdot3^{h-3}\mid L\). QED.

## Exact execution and reproducibility

`R762FG_CHARACTER_PERIOD_VERIFY.py` independently implements arithmetic in \(\mathbb Z[\zeta_9]\) via six-integer vectors and the integral relation \(\zeta^6=-\zeta^3-1\). It confirms \(\lambda^3=3\beta\), the two order identities modulo 3, the nonzero certificate modulo 9, and for \(k=0,\ldots,7\) confirms exactly \(v_3(\beta^{6\cdot3^k}-1)=k+1\) by modular exponentiation (only \(3^{k+2}\) precision needed). **Local execution: PASS**. `R762FG_CHARACTER_PERIOD_EVIDENCE.json` preserves all vectors, eight independent checks, exact scope and provenance. The universal statement is proved by binomial lifting; eight checks are finite corroboration only.

This output does not certify the R762ET/FA full-vector periods, nor determine the optimal period for \(h>8\), nor prove a native signed triadic closure event. P000's six signed axes, three-dimensional research slice, branch provenance, and live owner boundaries are unchanged.

## Next research questions

1. Close the factor-nine gap: find a provably integral functional/lattice extracting the two additional period-obstruction trits, or give a counterexample showing these valuations are truly lost on this projection.
2. Evaluate R762FE/FF's 251-return **joint Smith-basis** criterion for actual high-precision differences; avoid imposing the known-overconservative +57-trit threshold separately on each scalar.
3. Independently address the native signed `TRIADIC_CLOSURE_E` Cell/Link/Port legal update and V17/V29/V39 future-operation preservation.
