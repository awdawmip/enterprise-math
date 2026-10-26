# D25/LIFT — No affine-(j,ell) six-Hasse cellwise syzygy, p>=19

2026-10-26 TASK_RESEARCH portable author continuation in the real Research lane chatgpt-research-hourly-enterprise-math-20260923; maintenance lane distinct. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This genuinely strengthens the preceding cellwise-constant six-channel no-go (same-day note 20261026_hourly_d25_six_hasse_cellwise_rank_r11.md). It reuses that note's exact corrected-Clausen low/high rational Taylor carriers, recurrence and tensor injection argument, without recrediting them. Not native CM/Frobenius, full WZ classification, current Source CLAIM/checkpoint, formalization or independent review.

## New theorem — all affine coefficients are ruled out cellwise

Let p=6m+1 be prime **p>=19** and let r>=1. Use the six corrected Hasse channel functions

\[
C_{ab}(j,\ell)=u_{a,j}u_{b,p-\ell},\quad
(a,b)\in\{(0,2),(1,2),(0,3),(2,2),(1,3),(0,4)\}.
\]

For any coefficients A_{ab}, B_{ab}, D_{ab} in R=Z_(p)/p^r, if

\[
\boxed{
\sum_{ab}\left(A_{ab}+jB_{ab}+\ell D_{ab}\right)
C_{ab}(j,\ell)=0
\quad\text{for all }1\le j,\ell\le\min(7,2m),
}
\]

then **all 18 coefficients A,B,D are zero in R**. The 18-column matrix of actual labelled Hasse cells has a p-local left inverse; the theorem applies at **every p-power precision**, not only mod p. It excludes any nontrivial WZ cancellation with an *affine-in-source-cell*, shift-free, undifferentiated, constant-in-p coefficients for the same six channels. It does not exclude nonlinear/rational coefficients, adjacent-cell shifts, actual independent Ward J/E terms or boundaries.

## Proof — two 6x6 confluent jet matrices

Use the previous rational surrogate rows L_j=(u_0j,u_1j,u_2j) and H_ell=(u_2,p-ell,u_3,p-ell,u_4,p-ell), read modulo p from the low/high Taylor formula. Augment them:

\[
\widetilde L_j=(L_j,jL_j)\in R^6,\qquad
\widetilde H_\ell=(H_\ell,\ell H_\ell)\in R^6.
\]

For row sets A=(1,2,3,4,5,6) and B=(1,2,3,4,5,7), exact rational determinant calculation gives

\[
\begin{array}{lll}
\det \widetilde L_A
=6115090146751187/4933357406401147831073850100442726400,\\
\det \widetilde L_B
=4067311166086063/1233339351600286957768462525110681600,\\
\det \widetilde H_A
=365171593153733456612202247837761463284375552/
1317843520492196161221934377615738727453060628857421875,\\
\det \widetilde H_B
=1623108928803144044357925191458383972711122628476928/
2270677331896066290689423480991358220869809790037059326171875.
\end{array}\tag{1}
\]

The *numerator gcds* for the pairs are

\[
\gcd(L_A,L_B)_{\rm num}=49=7^2,\qquad
\gcd(H_A,H_B)_{\rm num}=2^{13}3^{51}.
\]

All denominator prime factors in (1) lie in {2,3,5,7,11,17,23,29,41}, none a prime p>=19 with p≡1 mod6. For **p>=31**, both augmented matrices on rows 1..7 contain a unit 6x6 minor and hence are split injections R^6→R^7. Their tensor is a split injection R^36→R^49. The 18 affine columns \(\{C_{ab},jC_{ab},\ell C_{ab}\}\) occupy **18 distinct tensor basis columns**, hence are linearly independent over R.

For the only target prime p with 19<=p<31, namely **p=19** (2m=6), row 7 is not available, but the A minors in (1) are units: \(\det\widetilde L_A\equiv16\) and \(\det\widetilde H_A\equiv14\pmod{19}\). Their 6x6 tensor already proves the p=19 case. This exhausts the domain and proves the theorem without relying on finite enumeration.

The A minor by itself has a low-side prime exception p=37 and a high-side prime exception p=109; the B minor repairs both. Those are **minor exceptions, not theorem exceptions**. At p=13, only the 4x4 admissible cell window exists and the actual affine 16x18 matrix has rank 14 mod13; the p>=19 theorem deliberately does not extend there.

## Finite author checker and observer implications

The adjacent Python stdlib checker imports (rather than duplicates) the verified rational Taylor carriers from 20261026_hourly_d25_six_hasse_cellwise_rank_r11_check.py. It computes four exact rational 6x6 determinants and both gcds, compares low and high surrogates to the *actual Hasse coefficient recurrence*, checks 18-column matrix rank for **79 primes** (all p≡1 mod6, 19<=p<=997, plus p8221), and confirms p13's actual rank 14 and the p37/p109 minor repairs. All checks actually passed. This is author exact checking, NOT independent review.

BRC: COMPOSE_APPLIED to labelled (j,ell,n,a,b,orientation,v_p) provenance, retaining moment/shift distinctions and p-local unit minors. The evaluated rank-one scalar observer cannot license a source-wise cancellation. The new theorem eliminates the entire **affine, shift-free** search family for p>=19, so the next mathematical attempt should use a genuinely shifted/rational WZ ansatz and keep the authentic J/E/finite-face/infinity/high-high ports. At p13 a separate small-window analysis is needed rather than falsely extending this criterion. The original CM class H0/B0, [X]U mod p², Frobenius eta/kappa, native experiments and independent Driver review remain open. D25/LIFT/JT2 mother OPEN.

Canonical Source authority: this is GitHub PORTABLE_ONLY evidence, not a winning claim, formal completed_units, admitted Result or native checkpoint. Control owner/support Issue #1558 remains the lawful next path; no scheduler change.
