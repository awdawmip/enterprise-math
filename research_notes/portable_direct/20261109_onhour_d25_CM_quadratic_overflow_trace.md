# D25 AF4 — uniform mod-p² Legendre reflection and finite CM overflow trace

2026-11-09 | TASK_RESEARCH author-side | UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen input c47e13e4aba0e006366f989d6334d443f6333ae3; native frontier b58330b74576153cdadde5d80a3d92df3a819a0e unchanged. Research lane chatgpt-research-onhour-enterprise-math-20260923; maintenance lane excluded.

## Theorem 1 (all primes p>3; complete coefficientwise mod-p² reflection)

Let G_p(X)=sum_{k=0}^{p-1} ((1/4)_k(3/4)_k/(k!)²) X^k in Z_(p)[X]. Define L_n(X)=sum_{k=0}^n (-1)^k binom(n,k)binom(n+k,k) X^k=P_n(1-2X). If p=4q+1 take N=3q; if p=4q+3 take N=3q+2. Then

**4G_p(X) = 3L_q(X)+L_N(X) modulo p², coefficientwise**,

and thus **G_p(1-X) = ((-2)/p) G_p(X) modulo p²**, where ((-2)/p) is the quadratic character.

Proof. For each 0<=k<p, f_k(a)=(a)_k(1-a)_k/(k!)² is a polynomial over Z_(p) in a; its Taylor expansion about a=1/4 is affine to first order in p. For p=4q+1, shifts -p/4 and +3p/4 turn these products into the respective terminating L_q and L_(3q), and 3*(-1/4)+3/4=0. For p=4q+3, shifts +p/4 and -3p/4 turn the products into L_q and L_(3q+2), and 3*(1/4)-3/4=0. This applies for ALL k<p, including coefficients beyond both terminating polynomials. Both degrees have parity q; Legendre reflection L_n(1-X)=(-1)^n L_n(X) completes the proof. In the four odd classes modulo 8, (-1)^q equals ((-2)/p).

## Theorem 2 (exact finite quadratic pullback and signed overflow)

Let F_p(Z)=sum_{k=0}^{p-1} (1/8)_k(3/8)_k Z^k/(k!)², with coefficients f_k. The classical quadratic Gauss formal identity implies the exact finite polynomial equality in Z_(p)[X]:

**F_p(4X(1-X))=G_p(X)+X^p E_p(X)**,

E_p(X)=sum_{n=p}^{2p-2} X^(n-p) sum_{k=ceil(n/2)}^{p-1} 4^k f_k (-1)^(n-k) binom(k,n-k).

Proof: coefficients below degree p agree by Gauss's series identity; direct binomial expansion supplies every remaining high-degree coefficient above. E_p has degree <=p-2. At nonnilpotent points the high-degree terms cannot be discarded.

## Theorem 3 (p≡13 mod24; exact mod-p² CM trace)

In A=(Z/p²)[T]/(T²-2), sigma(T)=-T, put s=(3-2T)/6; then 4s(1-s)=1/9 and sigma(s)=1-s. The previously proved CM(-24) short-root result gives G_p(s)=0 modulo p, and the separately established affine finite reduction gives F_p(1/9)=0 modulo p. Thus E_p(s) is divisible by p in A. Since ((-2)/p)=-1 for p≡13 mod24, Theorem 1 yields G_p(s)+sigma(G_p(s))=0 modulo p². Trace the finite Gauss identity to obtain

**2 F_p(1/9) = Tr_{A/Z_p²}(s^p E_p(s)) modulo p²**.

Write E_p(s)/p ≡ u_p+v_p T modulo p. Since T^p=-T and s^p ≡ 1/2+T/3 (mod p),

**F_p(1/9)/p ≡ (3u_p+4v_p)/6 modulo p**.

Hence the remaining uniform mod-p² Gauss zero conjecture is EXACTLY the new finite signed overflow condition 3u_p+4v_p=0 modulo p. This residual is OPEN: the current argument does not prove all-prime cancellation.

## Actual exact computational evidence

The attached Python standard-library verifier uses exact modular arithmetic, checks the complete Legendre interpolation and full polynomial reflection coefficientwise at p=5,7,11,13,17,19,29,37,41,43,61,73,109,157,181,373 (16/16), independently checks raw original F products versus recurrence and computes the full double-sum overflow and ring trace at p=13,37,61,109,157,181,373 (7/7).

At p=373 in basis (1,T) modulo 139129: G_p(s)=(0,42895), E_p(s)=(55577,62664), s^p E_p(s)=(0,96234), (u_p,v_p)=(149,168), F_p(1/9)=0. The T-odd p-digits are 115 and 258 and cancel; the unsigned even overflow coordinate u_p=149 is nonzero. 3*149+4*168=1119=3p. These are exact finite observations, not the outstanding universal proof.

## BRC / original observer / next

COMPOSE_APPLIED: preserve labeled index ranges n<p vs n>=p, original Gauss and Legendre coefficients, sigma-even and sigma-odd components, and p-adic carry before trace. The external quadratic ring is NOT an Enterprise native X6 spatial coordinate. Do not repeat prior 157-prime CM scan, signed Pfaff five-band proof or accepted D24 UR.

Next exact unit: prove the all-prime overflow identity 3u_p+4v_p=0 by finite WZ/Jacobi pairing of the explicit n>=p signed summands; connect only then to original W/V AF4 signed carry. Independently the same-original-class native p373 H0/B0 divided-power [X]U modulo 139129, native rank/semilinear direction/eta/signed kappa/Delta-R and independent reproduction remain NOT_RUN, issue #1559 PENDING_OWNER. No native Source CLAIM, run, checkpoint, freeze or review is asserted by this note.

Sources: predecessor CM(-24) Pfaff root proof, predecessor finite Gauss/Pfaff signed-band note, DLMF 15.8 classical Gauss transformation.
