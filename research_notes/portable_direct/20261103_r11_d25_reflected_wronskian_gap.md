# D25 | Reflected Wronskian: exact Frobenius mode, missing coefficients and reciprocal moment

**Author-side new result, 2026-11-03 +08:00.** Status: ALGEBRAICALLY PROVED / FINITELY EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Research lane: chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). Frozen Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Inherited exact interface

For prime p=6r+1>=7 let u=3r=(p-1)/2, a_n=(1/2)_n(1/3)_n(2/3)_n/(n!)^3, s_n=(9n+4)a_n/36, and S(z)=sum_{n=0}^{2r}s_n*z^n, all in F_p. The previously proved finite Gauss-Wronskian at cd37f09ddd8511b790ae4ffe564ae001cf7cc423 and Frobenius top coefficient at 0ae5bca67d0f6da403da76ed437a191d80a0d3d7 give
(1-z)*Omega'(z)+u*Omega(z)=S(z), Omega(0)=0, deg(Omega)<=u,
[z^u]Omega(z)=(-1)^r/6.
Those results, the CM0 assumption for target p mod24=13,19, and the original second-carry question are inherited, not new proofs credited here.

## Theorem R1: reflected support gap and fixed homogeneous coefficient (PROVED)

Define the invertible binomial-coordinate transform
d_k=[x^k]S(1-x)=(-1)^k sum_{n=k}^{2r} binom(n,k)*s_n, 0<=k<=2r.
Then **as a complete polynomial identity in F_p[z]**,

Omega(z) = (1-z)^(3r)/6 + sum_{k=0}^{2r} d_k*(1-z)^k/(3r-k).    (R1)

Thus the reflected coefficients of (1-z)^(2r+1),...,(1-z)^(3r-1) vanish (r-1 missing slots), while the top coefficient is exactly 1/6.

Proof: set x=1-z and H(x)=Omega(1-x). The Wronskian equation becomes -xH'(x)+uH(x)=S(1-x). Comparing coefficients gives (u-k)*[x^k]H=d_k for k<=2r, zero coefficients for 2r<k<u, and leaves the top H coefficient free. It is fixed by the inherited top coefficient: [x^u]H=(-1)^u[z^u]Omega=(-1)^(3r+r)/6=1/6. All denominators u-k lie in {r,...,3r} and are units modulo p. QED.

The original normalization Omega(0)=0 yields the additional **PROVED reciprocal moment**:
sum_{k=0}^{2r} d_k/(3r-k) = -1/6 (mod p).    (R1a)
This is the exact source compensation for the nonzero Frobenius high mode.

## Theorem R2: closed endpoint moments (PROVED)

Let ell(z)=sum_{k=0}^r binom(r,k)binom(2r,k)z^k. The previously established finite Clausen relation says sum_{n=0}^{2r}a_n*z^n=ell(z)^2 modulo p. Therefore 36S=(4+9*theta)ell^2, theta=z*d/dz. Vandermonde and its first factorial-moment identity give ell(1)=binom(3r,r) and (theta ell)(1)=(2r/3)binom(3r,r). Hence 36S(1)=(4+12r)binom(3r,r)^2=2(p+1)binom(3r,r)^2. Evaluating the original Wronskian equation at z=1 gives

sum_{n=0}^{2r}(9n+4)*a_n = 2*binom(3r,r)^2 (mod p),          (R2a)
Omega(1) = -binom(3r,r)^2/9 (mod p).                          (R2b)

Both formulas hold for every p=6r+1>=7, with no CM0 assumption. Since 3r<p, binom(3r,r) is a p-unit and Omega(1) is nonzero. QED.

## Reflected midpoint and precise remaining open claim

Put J_p=sum_{k=0}^{2r} d_k*2^(-k)/(3r-k) modulo p. Euler's criterion evaluates 2^(-3r)=(2/p), so R1 proves for **all** specified primes:

Omega(1/2) = J_p + (2/p)/6 (mod p).                          (R3a)

For target p mod24 in {13,19}, (2/p)=-1. Retain the exact integer mod-p^2 CM quotient g=ell(1/2)/p (mod p) and j=(theta ell)(1/2) (mod p). The inherited **open** second-carry equality
12*g*j-12*Omega(1/2) ?= 1
is now exactly equivalent to the single terminating reciprocal-moment statement

J_p - g*j ?= 1/12 (mod p).                                    (OPEN-R3)

Explicitly,
J_p = sum_{k=0}^{2r} (-1)^k*2^(-k)/(3r-k) *
        sum_{n=k}^{2r} binom(n,k)*(9n+4)*a_n/36.
The reduction to OPEN-R3 is PROVED; the universally quantified equality remains OPEN. This binomial-transform coordinate uses only p-unit denominators and preserves the original 216 coefficient source, signed terms and Frobenius boundary.

## Actually executed exact calculation

The independent author-side script d25_reflected_wr.py computes S from original hypergeometric coefficients; solves the forward Wronskian recurrence; builds the reversed coefficients by Horner substitution z->1-x; verifies R1/R1a/R2 and pointwise readouts for 148 primes p<=2000, p mod6=1. For 11 specified primes (7,13,19,31,37,43,73,181,373,1171,1999), every coefficient of R1 is independently compared. For 77 target primes, OPEN-R3 holds by **finite modular checking**. These checks do not substitute for a general proof, native p=373 H0/B0 experiment, or independent formal admission.

At p=373, r=62, the reflected gap has 61 positions, [x^186]Omega(1-x)=311=6^(-1), Omega(1)=254, J_373=338, Omega(1/2)=27, g=340, j=294, gj=369, and J-gj=342=12^(-1) modulo 373. All are exact finite-field/integer-lift readouts, not fitted parameters.

**BRC/Enterprise coordinate use:** COMPOSE_APPLIED with original indices n, signed coefficients s_n, invertible triangular transformed carrier d_k, one preserved high Frobenius port, and separately typed CM integer-lift quotient. The full polynomial R1 is a source-faithful coordinate representation; the scalar endpoint and midpoint observers are scoped readouts only.

**Next smallest scientific action:** prove or find a valid target-prime counterexample for OPEN-R3 using a terminating binomial-transform/WZ or p-adic CM root-lift certificate. The full source d_k and 1/6 high mode must be preserved. After a proof, propagate the second carry through the existing three-band precision tower toward frozen mother Delta_p-R_p=0 mod p, p mod24=13,19.

**Native control/status observed 2026-11-03 +08:00:** Gateway 0.6.11 reports UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false and active-job quota 5/5. No new native session, claim, run, Source checkpoint, Result or H0/B0 original experiment was created. Control support: Enterprise Math #1558; native p373 support: #1559. Existing Research #6637/#6638 are historical receipts, not new ownership.