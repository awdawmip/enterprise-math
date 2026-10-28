# D25/LIFT GH-51/GH-52 — Gosper obstruction and homogeneous reciprocal carrier

2026-10-28. Portable author-side derivation; **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. This research lane is chatgpt-research-hourly-enterprise-math-20260923, not maintenance. No native CLAIM/OPEN/Source checkpoint or mathematical admission is claimed.

## Input

GH-38/39 original hypergeometric source (not Gauss-square quotient):

\[
c_0=1,\quad c_{r+1}/c_r=(4r+1)^3/[(4r+2)(4r+3)(4r+4)],\quad T_d(z)=\sum_{r=0}^{d}(8r+1)c_rz^r.
\]

## GH-51 — PROVED: no uniform rational one-term Gosper antidifference

For every nonzero rational \(z\), no \(G(k)\in\mathbb Q(k)\) solves the identity

\[
z(4k+1)^3G(k+1)-(4k+2)(4k+3)(4k+4)G(k)
=(8k+1)(4k+2)(4k+3)(4k+4).\tag{51.1}
\]

Equivalently, the summand \((8k+1)c_kz^k\) has no indefinite antidifference \(G(k)c_kz^k\) with rational \(G\).

**Proof.** Set \(A(k)=z(4k+1)^3\), \(B(k)=(4k+2)(4k+3)(4k+4)\). If a rational solution has poles, a pole \(\beta\) with minimum real part requires \(A(\beta-1)=0\), so \(\beta=3/4\): at \(k=\beta-1\), only \(G(k+1)\) is singular. A pole \(\alpha\) with maximum real part requires \(B(\alpha)=0\), so \(\alpha\in\{-1,-3/4,-1/2\}\): at \(k=\alpha\), only \(G(k)\) is singular. Contradiction. Thus \(G\) is polynomial.

For \(z\ne1\), comparison of leading degrees forces \(G(k)=ak+b\), then comparison of \(k^4,k^3\) forces \(a=8/(z-1)\), \(b=(5z-1)/(z-1)^2\). The residuals at \(k^2,k^1\) are respectively

\[
-\frac{128z(2z+1)}{(z-1)^2},\qquad-\frac{4z(33z+59)}{(z-1)^2}.
\]

For \(z\ne0\) these cannot vanish simultaneously. At \(z=9\) the forced candidate is \(G(k)=k+11/16\) with residual \(-342\) already at \(k^2\). For \(z=1\), leading degree is \(N+2\) with nonzero coefficient \(64N-96\); hence \(N=2\). The \(k^4,k^3,k^2\) equations force \(G(k)=16k^2-4k-1/6\), whose \(k^1\) residual is \(-38/3\ne0\). QED.

**Exact scope:** characteristic-zero rational \(G(k)\) independent of \(p,d\). Does not rule out prime-sensitive WZ, Frobenius/CM, finite-character or nonlocal certificates.

## GH-52 — PROVED: direct reverse source, homogeneous fourth-order equation

For prime \(p=4d+3\ge7\), work in \(\mathbb F_p\). Define

\[
\rho_0=1,\quad
\frac{\rho_{r+1}}{\rho_r}=
\frac{(4r+3)(4r+4)(4r+5)}{(4r+6)^3}\;(0\le r<d),
\qquad R_d(u)=\sum_{r=0}^{d}\rho_ru^r.
\]

All denominators and all \(\rho_r\) are nonzero modulo \(p\) in this range. Reversing the original ranks, without Gauss-pair convolution, proves

\[
\boxed{c_{d-r}=c_d\rho_r,\qquad
T_d(z)=-c_d z^d(8\theta_u+5)R_d(z^{-1})
\quad(z\in\mathbb F_p^\times).}\tag{52.1}
\]

Proof: \(4d=p-3\) gives \(c_{d-r-1}/c_{d-r}=\rho_{r+1}/\rho_r\) and \(8(d-r)+1=2p-5-8r\equiv-(8r+5)\).

With \(\theta=u\partial_u\), define

\[
\mathscr L_4=\theta(\theta+\tfrac12)^3-u(\theta+\tfrac34)(\theta+1)^2(\theta+\tfrac54).
\]

Then, as a **whole polynomial**, not merely a truncated formal series,

\[
\boxed{\mathscr L_4R_d=0\quad\text{in }\mathbb F_p[u].}\tag{52.2}
\]

Proof: at \(1\le n\le d\) the coefficient is
\(n(n+1/2)^3\rho_n-(n-1/4)n^2(n+1/4)\rho_{n-1}=0\) by the ratio.
The constant vanishes. At the first omitted degree \(n=d+1\), the sole possible forcing is
\(-(d+3/4)(d+1)^2(d+5/4)\rho_d=0\), because \(d+3/4=p/4=0\). All higher degrees vanish. Leading recurrence coefficients for \(1\le n\le d\) are units, so \(R_d(0)=1\) uniquely fixes this solution among degree-\(\le d\) polynomials. QED.

This is the polynomial reduction of \({}_4F_3(3/4,1,1,5/4;3/2,3/2,3/2;u)\). Its homogeneous reciprocal carrier is distinct from GH-38's inhomogeneous **forward** Picard–Fuchs carrier. This is a new route, not a proof of the still-open special value

\[
(8\theta+5)R_d(1/9)\stackrel{?}{=}0
\quad\Longleftrightarrow\quad T_d(9)\stackrel{?}{=}0.\tag{52.3}
\]

## Verification, observer and continuation

Python standard-library exact checker tested rational coefficient contradictions at \(z=1/9,9,-1/2,2,1\), and checked the full reciprocal coefficient identity, all coefficients of the homogeneous operator including its first omitted degree, and the exact source inversion at \(z=2,9,-1\) for all **338 primes** \(7\le p<5000\), \(p\equiv3\bmod4\). All checks passed. The observed special value zero at these finite primes is not a general theorem and was already observed in GH-38.

BRC **COMPOSE_APPLIED**: full integer ranks, signed field coefficients, forward/reverse source provenance, variable inversion, differential/jet future operations are retained. The scalar quotient is sufficient only for \(T_d(z)\) under (52.1); original W/S, six Hasse ports, native X6, p-adic GH-20/21 and R23/R36 Green ports remain separate.

**Next:** obtain an independent Frobenius connection, character sum, or prime-sensitive WZ certificate for (52.3) using the homogeneous \(\mathscr L_4\) carrier, then pull back through (52.1). Do not repeat the prior Laurent reassembly, Gauss-square tail, or finite samples as if they prove vanishing. Original GH-3, native p=373 and formal D25 execution/Driver review remain OPEN.
