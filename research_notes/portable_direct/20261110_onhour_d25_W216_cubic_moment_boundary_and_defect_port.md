# D25 / W216 — exact cubic moment boundary and one-scalar defect reduction

Date: 2026-11-10, Asia/Hong_Kong. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Original science Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3.

Classification: AUTHOR_SIDE / EXACT_PROOF / FINITE_EXACT_CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0. The research lane label remains chatgpt-research-onhour-enterprise-math-20260923. No authenticated Source execution session, claim, open run, native experiment, review or Result is claimed.

## Exact theorem, valid over Q at every positive truncation

Let N>=1 and define original coefficients and signed binomial moments

\[
 A_k=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k}
 =\frac{(2k)!(3k)!}{(k!)^5\,216^k},\quad
 M_j(N)=\sum_{k=0}^{N-1}\binom{k}{j}A_k\quad(j=0,1,2,3).
\]

Then the following rational identity holds for **every integer N>=1**:

\[
\boxed{27(M_2+2M_3)-M_0-11M_1
=-9\bigl(N-\tfrac12\bigr)\bigl(N-\tfrac23\bigr)\bigl(N-\tfrac13\bigr)A_{N-1}.} \tag{1}
\]

Proof: The original factorial ratio gives

\[
 \frac{A_{k+1}}{A_k}
 =\frac{(k+1/2)(k+1/3)(k+2/3)}{2(k+1)^3}.
\]

With F_N(z)=sum_{k<N} A_k z^k and theta=z d/dz, the *finite* hypergeometric operator

\[
 {\cal L}=\theta^3-\frac z2(\theta+\tfrac12)(\theta+\tfrac13)(\theta+\tfrac23)
\]

annihilates every interior coefficient and leaves precisely

\[
 {\cal L}F_N(z)=-\frac12(N-\tfrac12)(N-\tfrac23)(N-\tfrac13)A_{N-1}z^N. \tag{2}
\]

Because

\[
 M_2+2M_3=\left[\frac{2\theta^3-3\theta^2+\theta}{6}F_N\right]_{z=1},
\]

a direct expansion at z=1 gives

\[
 27(M_2+2M_3)-M_0-11M_1=18[{\cal L}F_N]_{z=1}.
\]

Insert (2). QED. This is a symbolic proof, not numerical interpolation.

## A new uniform terminal-carry identity at p^4

For every prime p>3, the earlier *proved* terminal theorem gives v_p(A_{p-1})=3 and A_{p-1}=-p^3 (mod p^4). The coefficient on the right of (1) has residue 1 mod p since -9(-1/2)(-2/3)(-1/3)=1. Therefore

\[
\boxed{27(M_2(p)+2M_3(p))\equiv M_0(p)+11M_1(p)-p^3\pmod{p^4}.} \tag{3}
\]

This preserves the sign and the first surviving terminal carry. The derived BRC moment projection is sufficient for the specific observer M2+2M3 at the stated precision, not for all later observers.

## Connection to the frozen W216 Dwork defect

Reuse the earlier *proved* p-block filtered transfer, with

\[
 C_p(a)=A_a^{-1}\sum_{b=0}^{p-1}(6pa+6b+1)A_{pa+b},\qquad
 q_j=\Delta^j C_p(0)\pmod{p^4}.
\]

For every prime p>=5, the p-block theorem, q0=W_p, and W_p=M0+6M1 yield

\[
 W_{p^2}-pW_p\equiv(W_p-p)M_0+(q_1-6p)M_1+q_2M_2+q_3M_3\pmod{p^4}. \tag{4}
\]

For the frozen target classes p=13,19 (mod 24), chi_p=+1. Under the **additional hypotheses**

\[
 M_0=M_1=0\pmod p,\qquad
 W_p=p,\ q_1=6p,\ q_2=0\pmod{p^3}, \tag{H}
\]

equation (3) implies M2+2M3=0 (mod p). The p-block filtration and (H) then give the **proved conditional identity**

\[
\boxed{\frac{W_{p^2}-pW_p}{p^3}\equiv
\frac{q_3-2q_2}{p^3}\,M_3\pmod p.} \tag{5}
\]

All indicated fractions are p-local integers under (H). This isolates one concrete obstruction, q3-2q2, while retaining the nonzero odd/cubic moment M3. It does not assert uniform proof of (H) or of q3=2q2.

## Exact evidence (finite)

A Python script performs two independent types of checks: direct rational factorial computation for N=1,...,12, and p-adic integral coefficient streaming with retained valuations. It verified (3), the observed first jet, and the *finite conjecture* q3=2*q2 (mod p^4) for all **301** primes 5<=p<=2000. All **77** target-class primes in that finite range had M0=M1=0 (mod p). Additional p=10069,10099 cases checked the same scalar identities without any full p^2 sum. These finite observations are not a uniform proof of the two outstanding congruences.

| p | M0 mod p | M1 mod p | M2 mod p | M3 mod p | q2/p^3 mod p | q3/p^3 mod p |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 0 | 0 | 10 | 8 | 4 | 8 |
| 19 | 0 | 0 | 1 | 9 | 18 | 17 |
| 373 | 0 | 0 | 273 | 50 | 185 | 370 |
| 10069 | 0 | 0 | 9211 | 429 | 6895 | 3721 |
| 10099 | 0 | 0 | 1987 | 4056 | 4007 | 8014 |

At p373, M2+2M3=273+100=0 (mod 373), although M3=50 is not zero. The pair structure is retained rather than replacing the moments by their separate absolute values. BRC status: COMPOSE_APPLIED (signed moment-jet and terminal carry).

## Continuation and native gate

The *mother target* remains original signed Delta_p-R_p=0 (mod p) for every p=13,19 (mod24) or an exact original-class refutation. The present p-block identities serve its Frobenius-lift port but do not replace native H0/B0.

Source continuation request onhour11-20261110-1407-exact-cont was read as SUCCEEDED (as-of Source c64f3e3b5cb007159795c89434003f03a57d82a3, 2026-11-10 06:10 UTC). Own recovery_status returned SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED; no winning CLAIM/open run or formal Source checkpoint is represented.

Original native Issue #1559 was OPEN without assignee on 2026-11-10: [X]U modulo 139129, native module rank, semilinear Frobenius direction, eta, odd signed kappa/Delta-R and independent reproduction remain NOT_RUN / PENDING_OWNER. The accepted D24 RR/DR, Source progress, science pin and other real authors are preserved.

Next smallest unit: prove or falsify q3=2q2 (mod p^4) from the original exceptional-factor b-bands, then independently discharge uniform supersingular M0/M1 and first-jet (H). Native H0/B0 stays separately assigned to the responsible Source/Codex executor path through existing #1559; no surrogate benchmark is declared completed.