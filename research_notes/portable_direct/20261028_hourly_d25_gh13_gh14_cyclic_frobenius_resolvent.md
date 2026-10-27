# D25/LIFT GH-13 & GH-14 — Frobenius cyclic rational resolvent and rank-pole certificate

Date 2026-10-28 (Asia/Hong_Kong). Author-side TASK_RESEARCH; Research logical conversation 'chatgpt-research-hourly-enterprise-math-20260923'. Task 'RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT'; publication 'TP2-B6F4FC938FF94941C1B7'; frozen scientific source pin 'c47e13e4aba0e006366f989d6334d443f6333ae3'. Status AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

These two results consume the original GH-3 coefficient source, GH-9/10 p-adic reflection, and GH-11/12 global denominator and finite-window interpolation results. They do not count predecessor work as a new contribution. Auxiliary scalar rank r is not native Heartbeat World X6 spatial coordinate; original W/S, distinct MM/LH, Hasse, boundaries and experimental acceptance are preserved.

## GH-13. Exact global resolvent and uniqueness over F_p(x)

For prime p>=5, K=F_p(x), z in F_p, define

\[
B(x)=(4x+2)(4x+3)(4x+4),\quad A_z(x)=z(4x+1)^3,\quad
a_z=A_z/B,\quad f(x)=8x+1.
\]

Let t_0=1, t_j(x)=\prod_{i=0}^{j-1}a_z(x+i), and S_z(x)=\sum_{j=0}^{p-1}t_j(x)f(x+j). Then

\[
\boxed{t_p(x)=z,\qquad a_z(x)S_z(x+1)-S_z(x)=(z-1)f(x).}
\]

For every z!=1 (including z=0), the **unique** rational solution over K of

\[
A_z(x)R_z(x+1)-B(x)R_z(x)=B(x)(8x+1)
\]

is

\[
\boxed{R_z(x)=S_z(x)/(z-1).}
\]

**Proof.** For c in F_p, \(\prod_{j=0}^{p-1}[4(x+j)+c]=4^p[(x+c/4)^p-(x+c/4)]=4(x^p-x)\). Apply this to all three factors in numerator and denominator, obtaining t_p=z^p=z. Since a_z(x)t_j(x+1)=t_{j+1}(x), the difference of two translated length-p sums telescopes to t_p f(x+p)-f(x)=(z-1)f(x). Thus R_z solves the equation. A homogeneous solution H obeys a_z(x)H(x+1)=H(x); its p-fold translation gives z H(x)=H(x), forcing H=0 for z!=1. QED.

For z=9, z-1=8 is invertible for p>=5: GH-11's rational equation **always has a characteristic-p global solution**, while its proven denominator lower bound still applies. GH-7 excluded a characteristic-zero rational solution. The resonant z=1 case remains a separate question.

## GH-14. Exact pole obstruction at the authentic cutoff p=19

For p=19, d=(p-3)/4=4, the unique global R_9=N/D has reduced coprime numerator and denominator

\[
\boxed{D(x)=\prod_{k=0}^{4}(x-k)\prod_{k=1}^{4}(x+k)^2},\quad \deg D=13,
\]

\[
\boxed{N(x)=x^{14}+8x^{11}+5x^{10}+15x^9+5x^8
+11x^7+x^6+16x^5+6x^4+13x^3+8x^2+3x+12}
\quad\text{in }\mathbb F_{19}[x].
\]

The full cleared polynomial identity (with A=9(4x+1)^3) is

\[
\boxed{A(x)N(x+1)D(x)-B(x)N(x)D(x+1)
-B(x)(8x+1)D(x)D(x+1)=0.}
\]

The five numerator evaluations N(0),...,N(4) are (12,9,5,10,15) mod 19, **all nonzero**. Therefore R_9 has a genuine pole at every required rank 0,...,4; it also has double poles at ranks 15,...,18. Direct finite-field polynomial gcd on the p-cycle formula gives this reduced N/D, and the displayed cleared identity independently certifies it. Uniqueness from GH-13 proves that *no other global rational solution* can be evaluated at all finite ranks. Thus global rational solvability does not imply a valid finite-rank Gosper telescope. GH-12's independently constructed rank-local interpolation remains applicable and is not contradicted.

Original source coefficients C_0=1, C_(r+1)/C_r=9(4r+1)^3/[(4r+2)(4r+3)(4r+4)], evaluated for 0<=r<=4, still give T_19=\sum_{r=0}^4(8r+1)C_r=0 mod 19. The global rational function cannot be substituted into this sum because its ranks are poles. This is an exact single-prime information-loss certificate, not a universal T_p=0 proof.

## Exact author checks; BRC; continuation

The companion Python standard-library checker actually executed full polynomial monodromy, cyclic construction with polynomial gcd, and the cleared global identity for 13 primes: 5,7,11,13,17,19,23,29,31,37,41,43,47. It checked the complete p=19 reduced numerator, denominator factors and nonvanishing at all nine poles. All checks passed. Finite T_p=0 observations at these 13 primes are not universal proof; the general GH-13 theorem follows from the preceding algebra.

BRC COMPOSE_APPLIED: source population (p,z,r,A,B,C_r,cutoff, original S MM/LH labels), intended observer T_p, future operations rankwise evaluation, endpoint telescope, mod-p^2 harmonic transport. The global F_p(x) relation preserves cyclic monodromy, but evaluation at singular finite ranks is *not* an information-preserving projection. Retain denominator zeros and numerator evaluations as repair coordinates. No native X6 or original W/S identity is inferred.

Next smallest unit: determine the target p=19(mod24) Laurent principal parts on the true rank window, and seek a **regularized rank-local / multi-rank** finite-field certificate retaining both endpoints and GH-10's two independent next-digit moments. If proven, compose with GH-5 MM port and R23/R36, without collapsing original W/S or six Hasse J/E labels. Parent still needs original H0/B0 divided-power p=373, [X]U mod p^2, Frobenius eta/kappa and independent Driver review.

Last read-only Research-lane recovery #6622 and continuation #6623 (2026-10-27) verified execution_authorized=false and route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION. Fresh gateway v0.6.11 status in this turn reported research_authority_granted=false, executor_binding_configured=false, control CODE_REVIEW_REQUIRED and active jobs 5/5. Predecessor CAS support issue #1558 stays assigned. This file is author-side portable progress, not a new current CLAIM/open, native checkpoint, Result or Research-Activity admission.