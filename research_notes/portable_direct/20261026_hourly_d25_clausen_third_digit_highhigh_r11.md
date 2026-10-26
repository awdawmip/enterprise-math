# D25/LIFT — Third normalized Clausen digit and indispensable high–high corner

2026-10-26; TASK_RESEARCH conversation chatgpt-research-hourly-enterprise-math-20260923, distinct from CONTROL_PLANE_MAINTENANCE chatgpt-hourly-enterprise-math-20260921. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** Auxiliary corrected-Clausen mathematics checked against the exact original ordered hypergeometric cutoff; not original-class CM/Frobenius, LIFT/JT2 completion, native checkpoint or formal independent review.

## Input and new target

Existing 20261026_hourly_d25_corrected_clausen_jet_reflection_p4_bridge.md proves the normalized cutoff Q_p/p² mod p², using only low–high rank pairs and Hasse jets through degree 3. This unit addresses Q_p/p² **mod p³** and identifies an additional ordered high–high corner that earlier precision legitimately excluded.

For prime p=6m+1>=7 define

\[
\widetilde b_n(x)=\frac{(-x)_n(-2x)_n}{(\tfrac12-3x)_n n!},
\quad u_{k,n}=[t^k]\widetilde b_n(m+t),\quad
r_n=2^{-n}\widetilde b_n(m-p/6),
\]

and original ordered cutoff

\[
Q_p=\sum_{\substack{0\le a,b<p\\a+b\ge p}}(6(a+b)+1)r_ar_b.
\]

All Taylor-jet denominators for n<p are p-units. For 1<=ell<=j<=2m write n=p-ell, alpha=6(j-ell)+1 and

\[
A_{j\ell}=u_{0,j}u_{2,n},\quad
B_{j\ell}=u_{1,j}u_{2,n}+u_{0,j}u_{3,n},
\]
\[
C_{j\ell}=u_{2,j}u_{2,n}+u_{1,j}u_{3,n}+u_{0,j}u_{4,n}.
\]

## Theorem — full third normalized digit (all target primes)

\[
\boxed{\begin{aligned}
\frac{Q_p}{p^2}\equiv {}&
\frac1{18}\sum_{j=1}^{2m}\sum_{\ell=1}^{j} 2^{-(j+p-\ell)}
\left[
\alpha A_{j\ell}
+p\left(6A_{j\ell}-\frac{\alpha}{6}B_{j\ell}\right)
+p^2\left(\frac{\alpha}{36}C_{j\ell}-B_{j\ell}\right)
\right]\\
&+\frac{p^2}{1296}
\sum_{\substack{2m<a,b<p\\a+b\ge p}}
(6(a+b)+1)2^{-(a+b)}u_{2,a}u_{2,b}
\pmod{p^3}.
\end{aligned}}\tag{1}
\]

**Proof.** The two numerator factors of the corrected polynomial quotient imply u_0,j=0 for j>m and u_0,n=u_1,n=0 for n>2m. Therefore a low j<=2m and a high n>2m have the p-local expansions

\[
r_j=2^{-j}(u_{0,j}-pu_{1,j}/6+p^2u_{2,j}/36)+O(p^3),
\]
\[
r_n/p^2=2^{-n}(u_{2,n}/36-pu_{3,n}/216+p^2u_{4,n}/1296)+O(p^3).
\]

Low–low indices never reach the cutoff: a+b<=4m<p. A low–high pair has n=p-ell, 1<=ell<=j, and two possible orders; multiplying the displayed expansions with exact weight (alpha+6p) and ordering factor 2 gives the first sum in (1). The previous theorem is its reduction modulo p². In contrast, high–high pairs now matter: each r is p² times the first nonzero high jet, so an *ordered* high–high product contributes p⁴/1296 before division by p²; precisely the second sum in (1) survives at the new modulus p³. Higher omitted terms vanish modulo p³ after normalization. The three disjoint index sectors exhaust the original ordered Q. QED.

This new high–high term is **not** a correction to the finite Ward left boundary or the Laurent-infinity port. It is a genuinely new carrier population that must be retained separately for a source-faithful third-digit identity.

## Independent exact certificate

The companion standard-library checker constructs the original hypergeometric r_n directly modulo p⁵ by

\[
r_{n+1}=r_n(6n+1)(3n+1)/(36(n+1)^2),
\]

and enumerates *all ordered* cutoff pairs. Independently it constructs the u_0 through u_4 coefficients from the corrected rational parameter recurrence over Z/p³, checks the expanded low–high formula against direct Taylor multiplication, and checks the high–high sector and total against the original Q_p/p².

**PASS:** all 22 primes p=6m+1 in 7<=p<=211, plus a fresh p=733 certificate.

| p | Q_p/p² mod p³ | low–high mod p³ | high–high mod p³ | high–high /p² mod p |
| ---: | ---: | ---: | ---: | ---: |
| 7 | 87 | 136 | 294 | 6 |
| 13 | 104 | 2132 | 169 | 1 |
| 19 | 5275 | 1665 | 3610 | 10 |
| 31 | 10796 | 5991 | 4805 | 5 |
| 37 | 32571 | 7929 | 24642 | 18 |
| 43 | 64429 | 16355 | 48074 | 26 |
| **733** | **99531942** | **28072505** | **71459437** | **133** |

In particular, at p=733 the high–high contribution is 733²·133=71,459,437 modulo 733³ and is nonzero. The original **ordered** Q_733 mod 733⁵ is 53,477,417,585,238, exactly 733²·99,531,942. Reducing 99,531,942 modulo 733² gives the earlier verified 133,477. Thus extending the low–high-only formula by one digit **without the high–high sector is disproved** by an exact p=733 counterexample, not merely a numerical suspicion.

**BRC COMPOSE_APPLIED:** the carrier must retain corner-sector tag (low–high/high–high), ordered rank, corrected parameter/Hasse jet, p-adic valuation and observer precision. The sector omitted safely at one precision can become obligatory at the next. These auxiliary ranks are neither P000 native Cell axes nor a complete native three-dimensional slice.

**Next mathematical unit:** carry the new low–high u2/u2, u1/u3, u0/u4 jets and the ordered high–high population through the signed Ward/infinity source observer, retaining both finite cutoff faces; only then test whether the p=733 (1,2) tangent boundary survives or cancels in Q_p/p² mod p³. Do not infer higher precision from the old two-digit channel equation. Same-original-class H0/B0, [X]U mod p², Frobenius direction/eta, kappa, Delta_p-R_p, native CM experiment and independent Driver review remain outstanding. Mother D25/LIFT/JT2 OPEN.

Control provenance: Research-lane recovery https://github.com/awdawmip/kimi-query-bridge/issues/6520; exact continuation https://github.com/awdawmip/kimi-query-bridge/issues/6521; full pages https://github.com/awdawmip/kimi-query-bridge/issues/6522 and https://github.com/awdawmip/kimi-query-bridge/issues/6523. The historic CLAIM/predecessor mismatch remains under https://github.com/awdawmip/enterprise-math/issues/1558. No native CLAIM, OPEN or Source checkpoint is asserted.