# D25/LIFT — Six-Hasse source-cell independence and prime-exception repair

Date 2026-10-26. TASK_RESEARCH portable author work; logical Research conversation chatgpt-research-hourly-enterprise-math-20260923 (distinct from maintenance). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

STATUS: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is *corrected-Clausen auxiliary algebra*, not original-class CM/Frobenius, native experimental evidence, authorized CLAIM, Source checkpoint, Driver review or universal WZ closure. Earlier six-Hasse jets, Ward J/E and seam work are inputs, not recredited.

## Theorem — six Hasse channels have full p-local cellwise rank

For every prime p=6m+1 >=13, integer r>=1 and original corrected family

\[
F_k(t)=\frac{(-m-t)_k(-2m-2t)_k}{(1-p/2-3t)_k k!}
=\sum_{a\ge0}u_{a,k}t^a,\qquad 0\le k<p,
\]

define labels \(\mathcal C=\{(0,2),(1,2),(0,3),(2,2),(1,3),(0,4)\}\), and source cells \(C_{ab}(j,\ell)=u_{a,j}u_{b,p-\ell}\) for j,ell in {1,2,3,4}. Every coefficient is p-local. The map

\[
\boxed{
(\mathbb Z_{(p)}/p^r)^6\to(\mathbb Z_{(p)}/p^r)^{16},
\quad (\lambda_{ab})\mapsto
\big(\sum_{ab\in\mathcal C}\lambda_{ab} C_{ab}(j,\ell)\big)_{j,\ell=1}^4
}
\]

is **split injective**. Thus no nonzero *constant in j and ell* six-channel combination vanishes cell by cell on this real Hasse-jet population at any p-power precision. This does NOT exclude coefficients dependent on rank or cell, Ward shifts, independent J/E couplings, left/right faces, positive infinity or high-high contributions: those remain the intended coupled WZ research.

### Exact proof

Let low-row \(L_j=(u_{0,j},u_{1,j},u_{2,j})\) and high-row \(H_\ell=(u_{2,p-\ell},u_{3,p-\ell},u_{4,p-\ell})\). Modulo p and t³, low rows are Taylor coefficients of

\[
L_j(t)=\frac{(1/6-t)_j(1/3-2t)_j}{(1-3t)_j j!}.
\]

For high rows, in F_p[t], \((a+bt)_p=(a+bt)^p-(a+bt)=b(t^p-t)\) for a in F_p. Apply this to (1/6-t) and (1/3-2t), and use \((1-3t)_{p-1}=(3t)^{p-1}-1\) plus Wilson's factorial relation. Because high k=p-ell>2m has two t-zeros, the first three coefficients of \(F_{p-\ell}(t)/t^2\) are exactly the coefficients of the **p-independent rational surrogate**

\[
\boxed{
H_\ell(t)=\frac{2(\ell-1)!\prod_{i=1}^{\ell-1}(i+3t)}
{\prod_{i=1}^{\ell}(1/6-i-t)(1/3-i-2t)}
\pmod{(p,t^3)}\quad (\ell=1,2,3,4).
}
\]

The 3x3 rational Taylor minors of rows 123 and 124 are:

\[
\begin{array}{rlrl}
\det L_{123}&=-223/(2^5 3^{13}),&
\det L_{124}&=-590771/(2^{13}3^{15}),\\
\det H_{123}&=(2\,3^{15}\,8221)/(5^6 11^3 17^3),&
\det H_{124}&=(4\,3^{18}\,114071533)/(5^6 11^6 17^3 23^2).
\end{array}
\]

For all relevant primes p>=13, p≡1 mod6, these denominators are units: 5,11,17,23 are 5 mod6. Since gcd(223,590771)=1 and gcd(8221,114071533)=1, **one of each pair of minors is always a unit**. Therefore low and high 4x3 matrices admit left inverses over every Z_(p)/p^r. Their 16x9 tensor product admits a left inverse; the six selected Hasse channel columns are six of the nine tensor basis columns, giving the claimed split injection.

The naive first three low j-rows have exceptional **p=223** (rank repaired by j=4). The naive first three high ell-rows have exceptional **p=8221** (repaired by ell=4). Neither exceptional minor causes a failure of the six-channel theorem. At p=7 the original low-high window has 2m=2: its real 2x2 cell matrix has rank 4<6; p=7 is explicitly outside the theorem.

### Checks, BRC observer, and next discriminant

The adjacent dependency-free Fraction/finite-field checker actually passed: rational determinants and gcds, exact jet recurrence matching both rational carriers, 16x6 rank=6 for **80** target primes (all p≡1 mod6, 13<=p<=997, plus p8221, including p223 and p733), and the real p7 small-window rank=4. Author computation supports but does not substitute for the all-prime algebraic proof or independent review.

BRC: COMPOSE_APPLIED, with carrier (j,ell,n,Hasse label, orientation, p-valuation). The rank-one scalar V is only a quotient observer; it cannot substitute for six separately labelled cell streams in future source-aware operations. This is a precise auxiliary information-loss boundary, not an X6/P000 native geometry assertion.

**Next executable science unit**: a rank- or shift-dependent WZ ansatz using independent J/E labels and both finite faces; test p13 nonresonant and p733 resonant records while preserving positive infinity and independent ordered high-high. Separately obtain authenticated same-original-class H0/B0, [X]U mod p², Frobenius direction/eta, kappa and Delta_p-R_p; original-class native experiment and independent Driver still not run. D25/LIFT/JT2 mother OPEN. GitHub portable evidence is NOT a Source completed_units record; control owner support remains Issue #1558.
