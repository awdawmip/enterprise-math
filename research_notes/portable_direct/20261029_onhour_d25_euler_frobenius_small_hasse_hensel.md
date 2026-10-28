# D25 — Euler–Frobenius first-digit reduction, simple roots and Hensel lift defect

2026-10-29, onhour Research lane (chatgpt-research-onhour-enterprise-math-20260923). AUTHOR-SIDE / PROVED ALGEBRA / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. No native Source claim, result or H0/B0 execution.

Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Consume prior 20261029_onhour_d25_cm24_gauss_padic_fourclass_precision.md (Git blob 7188810ecce8834ad38ac7142dfb5d444b9bf0d3), not a repetition of its CM(-24) or cutoff work.

## New finite-field theorem (exact, all p = 5 or 7 mod 8)

For prime p>3 let beta_n=(1/8)_n(3/8)_n/(n!)^2, and let r1,r3 be the first n for which p divides 8n+1 and 8n+3. Let a=min(r1,r3), b=max(r1,r3), and K_b(z)=sum(n=0..b) beta_n z^n. Set

m=a+b+1-p=(p+1)/2, c=p-1-b, d=p-1-a;
P(z)=sum(n=0..a) binom(a,n)binom(b,n)z^n;
R(z)=sum(n=0..c) binom(c,n)binom(d,n)z^n.

Then, as a polynomial identity in F_p[z],

K_b(z) = P(z) = (1-z)^m R(z)  (mod p).

For p=5 mod8, c=(p-5)/8, d=(3p-7)/8; for p=7 mod8, c=(p-7)/8, d=(3p-5)/8. Thus the original first-digit problem of degree approximately 5p/8 reduces to a polynomial of degree approximately p/8. In the frozen p=13 mod24 class: p=8c+5, d=3c+1. In the observed p=23 mod24 extension: p=8c+7, d=3c+2.

Proof: n<=a has beta_n=binom(a,n)binom(b,n) mod p because 1/8=-r1 and 3/8=-r3 mod p; a<n<=b coefficients vanish mod p. Hence K_b=P. The Gauss differential operator L_(u,v)y=z(1-z)y''+[1-(u+v+1)z]y'-uv y annihilates P for (u,v)=(-a,-b), and annihilates R for (u,v)=(-c,-d); check from recurrence n^2 f_n=(n-1+u)(n-1+v)f_(n-1). The Euler gauge identity obtained by differentiating (1-z)^s y uses s=1-u-v and transports a solution of L_(1-u,1-v) to a solution of L_(u,v). Mod p, 1+a=-d, 1+b=-c, s=1+a+b=m (mod p). Thus (1-z)^m R solves the same equation as P. Both have constant coefficient 1 and degree m+c=a<p. The coefficient recurrence has invertible n^2 for 1<=n<p, establishing uniqueness and the asserted full polynomial identity. This uses neither a noncanonical p-adic transformation nor a hidden quotient.

## New squarefreeness theorem, all p>3

In the p=5/7 mod8 classes the root z=1 of P has multiplicity EXACTLY m=(p+1)/2: Vandermonde gives R(1)=binom(c+d,c), and c+d=(p-3)/2<p, hence R(1) is nonzero mod p. All remaining c roots are simple, and none is 0 or 1. Indeed P(0)=1. If P(z0)=P'(z0)=0 at z0 not in {0,1}, expand the Gauss equation in (z-z0). Its leading factor z0(1-z0) times r(r-1) is nonzero for every degree r<p. Induction kills every Taylor coefficient, contradicting P(0)=1. The same argument proves nonsingular-root simplicity for p=1/3 mod8 as well (without claiming the Euler factor in those classes).

For z0=1/9 in Z_p (p>3), if K_b(z0)=0 mod p, then D=theta K_b(z0)=z0 K_b'(z0) is a p-unit. At a zero of reduced R, D=(1-z0)^m theta R(z0) mod p. Hensel therefore gives a UNIQUE root z*=z0+p epsilon (mod p^2) with

epsilon = -(K_b(z0)/p)*z0/D (mod p).

The proposed Root2 for p=13 mod24 is precisely epsilon=0, conditional on the still-unproved universal first-digit root. This is an exact source-aware normalization-defect reduction, NOT a proof of universal p^2 vanishing. The p=23 mod24 extension remains conjectural; 17 and 19 are negative controls for p^2 precision.

## Actually executed exact checks

The companion script d25_gauss_euler_hensel_guard_20261029.py uses independent binomial polynomial convolution and original p^2 hypergeometric recurrence, no floating point. Results: 86/86 full polynomial factorizations for primes p<1000 with p mod8=5/7. All primes 5<=p<1000 were checked for correct first-digit and derivative observers; every observed nonsingular root has nonzero theta-jet and satisfies the exact p^2 Hensel Taylor equation. Among CM-inert classes p mod24 =13,17,19,23, observed epsilon=0 counts were respectively 22/22, 0/23, 0/23, 22/22; THESE ARE FINITE OBSERVATIONS, not universal proofs.

Selected (p; a,b; m; c,d; K modp^2; theta K modp; epsilon):
13; 8,11; 7; 1,4; 0; 11; 0
23; 14,20; 12; 2,8; 0; 8; 0
37; 23,32; 19; 4,13; 0; 35; 0
373; 233,326; 187; 46,139; 0; 5; 0
17; no Euler factor; K=255=15*17; theta=8; epsilon=9
19; no Euler factor; K=171=9*19; theta=7; epsilon=8

## Provenance and recovery

BRC COMPOSE_APPLIED: carrier includes ordered r1/r3 numerator hits, original beta_n valuations, degree, Euler factor m, reduced polynomial R, observed z0, first jet D and p^2 Hensel displacement epsilon. These cannot be replaced by the Boolean (-6/p) inertness without losing the precision split. External finite-field observer only; no unproved bridge to P000 six-axis native geometry, native 3D slice, or original Delta_p-R_p is asserted.

Native #1559 remains separate: fixed original p=373 H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius and normalization eta, signed odd Hesse/Green, kappa, Delta_p-R_p require genuine authorized native execution. Source checkpoint, Result, review, task/parent closure remain absent. Source onhour authority/claim/run/request must be freshly re-read; existing original request IDs are not to be reissued or borrowed from maintenance lane.

NEXT: Prove or falsify the reduced degree-c Jacobi/character-sum evaluation R(1/9)=0 mod p for ALL p=13 mod24; then determine the finite p-adic transformation/period-normalization defect forcing Hensel epsilon=0 (and NOT forcing it for 17/19). Afterwards return to the signed A216/B2304 mod p^3 bridge and native benchmark. Do not re-run completed Clausen, CM(-24), or 373 scalar work as purported new research.
