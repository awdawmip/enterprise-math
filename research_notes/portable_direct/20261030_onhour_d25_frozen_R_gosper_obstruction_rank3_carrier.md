# D25 / SECOND-DIGIT-LIFT — frozen R Gosper obstruction and regular rank-three transport

2026-10-30 Asia/Hong_Kong. AUTHOR-SIDE / PROVED RATIONAL NO-GOSPER OBSTRUCTION / PROVED REGULAR VECTOR TRANSPORT / EXACT FINITE CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

Scope: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; original scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Research logical lane chatgpt-research-onhour-enterprise-math-20260923, NOT the maintenance lane. This is author-side arithmetic, not native p=373 H0/B0 execution, Source CLAIM/checkpoint, Result or independent review.

## Original observer and exact question

Reuse the already frozen coefficient sequence and original signed inner observer:

    C_1 = 1/10,
    C_(a+1)/C_a = r(a) = 36*a^2/((6*a+5)*(3*a+2))
                  = 2*a^2/((a+5/6)*(a+2/3)).
    T_i = sum_(a=1)^i (1+6*(i-a))*C_a; T_0=0.
    R_p = 2*sum_(i=1)^m binom(m,i)*binom(2m,i)*2^(-i)*T_i (mod p),
    p=6m+1 prime.

The previous Gauss high-tail reflection identified this same C sequence as a p-adic coefficient carrier, but kept high tail F_p and the signed R_p as distinct observers (research_notes/portable_direct/20261030_onhour_d25_gauss_high_tail_frozen_C_reflection.md, commit 1d6845f8f03cbd6d6647a57d5ad25877f0d06a7e).

We test whether there exists a one-index rational Gosper antidifference q_i(a) in Q(a) solving, identically as a rational function,

    r(a)*q_i(a+1) - q_i(a) = 1+6*(i-a).                  (G)

## Theorem 1: uniform no-Gosper statement

For every fixed i in Q, no rational function q_i(a) in Q(a) satisfies (G). This rules out this one-index rational antidifference class, not bivariate WZ, finite modular interpolation, higher-order telescopers or CM/p-adic transformations.

Proof: Suppose q has poles. At a pole lambda of maximal real part, q(a+1) is analytic; cancellation of the pole of -q(a) in (G) forces r(a) to have a pole at lambda. Hence lambda is -5/6 or -2/3. At a pole mu of minimal real part, q(a) is analytic at a=mu-1 while q(a+1) is singular; for the left side to be polynomial, r(a) must have a zero at a=mu-1. The sole finite zero of r is 0, so mu=1. This contradicts Re(mu)<=Re(lambda)<0. Therefore q has no poles and is a polynomial.

Since r(a)=2+O(1/a), a nonzero polynomial q of degree d gives a left side of degree d; the right side has degree one. Thus q(a)=A*a+B and A=-6. Clear the denominator (a+5/6)(a+2/3) and equate the coefficients of a^2, a and 1. They are:

    B-6*i+5=0;
    -3*B/2-9*i+31/6=0;
    -5*B/9-10*i/3-5/9=0.

The first gives B=6*i-5; the second then requires i=19/27, while the third requires i=1/3. Contradiction. q=0 cannot solve (G). QED.

## Theorem 2: regular source-preserving vector recurrence

Introduce S_i=sum_(a=1)^i C_a, S_0=0. The following equalities hold over Q for every i>=0:

    S_(i+1)=S_i+C_(i+1);
    T_(i+1)=T_i+6*S_i+C_(i+1);
    C_(i+2)=r(i+1)*C_(i+1).

The vector v_i=(T_i,S_i,C_(i+1))^t obeys

    v_(i+1) = [[1,6,1],[0,1,1],[0,0,r(i+1)]] * v_i,
    v_0=(0,0,1/10)^t.

For every p=6m+1 >=7 and 0<=i<m, all numerator and denominator factors of r(i+1) are units modulo p; the transition determinant r(i+1) is nonzero mod p. This gives a uniformly nonsingular O(m) finite-field evaluation of the original signed R_p while preserving the indexed source, signed weight and future operations.

Its scalar order-three consequence does have *apparent* singularities. Set

    D_i=(6*i+5)*(3*i+2)=18*i^2+27*i+10;
    N_i=5*D_i+36*i^2=126*i^2+135*i+50;
    U_i=T_(i+1)-2*T_i+T_(i-1)=5*C_i+C_(i+1).

Then, exactly over Q and without unsafe division,

    D_(i+1)*N_i*U_(i+1) - 36*i^2*N_(i+1)*U_i = 0.   (H)

At the genuine frozen target-class prime p=67=19 mod24, m=11 and i=7,

    N_7=7169=107*67,
    C_7=39, U_7=0, C_8=6, U_8=20 (mod 67).

The scalar (H) becomes 0=0 at i=7 and cannot determine the nonzero U_8. The original vector transition stays invertible. Thus eliminating the two repair coordinates creates a provable spurious modular singularity for the intended forward-operation horizon.

## Actual executed certificate and status

Executed Python standard-library checker:
research_notes/portable_direct/d25_frozen_R_gosper_obstruction_guard_20261030.py

The local executable checked the exact rational recurrences on 16 initial terms and compared (H), the vector recurrence, and the original independent signed triangular double sum for all 80 primes p=1 mod6, 7<=p<1000. Eleven primes in this finite range have an i in [1,m) with N_i=0 mod p; examples include 67,97,103,211. Fixed original witnesses (p,m,R_p,T_m) are (13,2,0,11), (19,3,12,3), (373,62,196,44). It terminated PASS_D25_FROZEN_R_GOSPER_OBSTRUCTION_AND_RANK3_RECURRENCE. The proof of Theorem 1, rational identities, and vector invertibility is symbolic; finite checks do not establish the all-prime LIFT.

BRC COMPOSE_APPLIED: typed state (C_(i+1), S_i, T_i), original signed joint (i,a) observer and original Gauss three-stratum downstream operation. Scalar U_i loses next-step reconstructibility at p=67, as independently witnessed. Retain the vector carrier rather than deleting the source/repair ports. This is external arithmetic, not a new native X6/H0/B0 operator or a scalar surrogate for it.

Next exact arithmetic step: seek a *joint (i,a) creative-telescoping/summation-by-parts certificate* coupling the frozen B_i binomial factor with the preserved vector state and the previously proved three-stratum harmonic jet, to prove or disprove Delta_p-R_p=0 mod p for all primes p=13,19 mod24. The one-index rational certificate (G) has been ruled out and need not be retried.

Separate native highest-priority acceptance: Issue #1559 remains OPEN/PENDING_OWNER as checked 2026-10-30: original same-class H0/B0 divided-power [X]U mod139129 at p373; module rank; actual semilinear Frobenius direction and eta; signed odd Green/Hesse; kappa; independent reproducible native run. This scalar arithmetic does not satisfy any of those. The 2026-10-30 13:57 UTC Site status had research_authority_granted=false, write_relay_enabled=false, executor_binding_configured=false; source_sync.control.state=CODE_REVIEW_REQUIRED. Own checkpoint list returned ACCESS_DENIED; control_continuation returned CONTROL_QUOTA. Preserve existing request/staging provenance, no role-bound writes and no maintenance-lane adoption. Original scheduler and frozen Source pin unchanged.
