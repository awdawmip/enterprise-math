# D25 original W_p: exact coupled Picard–Fuchs three-jet and sharp cubic cutoff defect

2026-10-25. Author-side independent TASK_RESEARCH mathematical derivation, not Source-native task progress. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen science source c47e13e4aba0e006366f989d6334d443f6333ae3. Research conversation chatgpt-research-onhour-enterprise-math-20260923; no maintenance-lane identity. Reuses (without redoing) the original three-band signed-rank result committed at 7d434503edbe095201e82ba6f526b7d8964c6415. Status: AUTHOR_EXACT_DERIVATION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Native benchmark NOT_RUN.

## Algebraic theorem: true coupling, not three unrelated tails

For any positive integer m, write (a)_n for the ascending factorial, theta=z*d/dz, and introduce the formal parameter t:

    u[n](t)=((-3m+t/2)_n (-2m+t/3)_n (-4m+2t/3)_n)/(2^n*(n!)^3).
    H(t,z)=sum(n=0..4m) u[n](t)*z^n.
    F_j(z)=[t^j]H(t,z), j=0,1,2.

All statements in this section are exact identities over Q, not prime experiments. The t-adic order of u[n] is [n>2m]+[n>3m]+[n>4m]. Therefore the EXACT polynomial degrees are

    deg F_0=2m, deg F_1=3m, deg F_2=4m.

The three coefficient jets have a triangular original-rank meaning: F_0 is the low-band leading polynomial; F_1 contains low first derivatives plus middle leading terms; F_2 contains low second derivatives plus middle first derivatives plus the complete high-band leading terms. No rank/source/valuation was discarded.

The base polynomial is the explicit signed integer-binomial sum

    F_0(z)=sum(n=0..2m) (-1/2)^n binom(2m,n)binom(3m,n)binom(4m,n)*z^n.

Define the three polynomial differential operators

    P0(theta)=(theta-3m)(theta-2m)(theta-4m);
    P1(theta)=(3/2)theta^2-(26/3)m*theta+12m^2;
    P2(theta)=(13/18)theta-2m;
    L0=theta^3-(z/2)P0(theta).

**Exact coupled certificate (PF3):**

    L0 F_0 = 0;
    L0 F_1 = (z/2) P1(theta) F_0;
    L0 F_2 = (z/2) [P1(theta) F_1 + P2(theta) F_0].

With F_0(0)=1 and F_1(0)=F_2(0)=0, these polynomial equations uniquely determine each jet: the coefficient of z^n in theta^3 is n^3, and every term multiplied by z only involves lower-degree coefficients. For any prime p=6m+1, the same triangular uniqueness applies in F_p through degree 4m+1<p, because n is a unit for every n<p. Hence a proposed high/medium/low combined source certificate can be verified by one coupled ODE system rather than separately trusting three data streams.

## Exact original recurrence and endpoint

Set

    P_t(X)=(X-3m+t/2)(X-2m+t/3)(X-4m+2t/3).
    P_t(X)=P0(X)+t P1(X)+t^2 P2(X)+t^3/9.  [exact expansion]

The defining recurrence is

    2(n+1)^3 u[n+1](t)=P_t(n)u[n](t).

Coefficientwise telescoping gives the exact, nonhomogeneous boundary equality

    [theta^3-(z/2)P_t(theta)] H(t,z)
       = -(4m+1)^3 u[4m+1](t) z^(4m+1).                 (BOUND)

At n=4m+1 the third distinct crossed factor occurs. Directly extracting the three factors t/3, t/2, 2t/3 and retaining every signed factorial proves

    [t^3]u[4m+1](t)
      = (-1)^m m^2 (2m)!(2m-1)!(3m)!(m-1)!
        / (9*2^(4m)*(4m+1)^3*((4m)!)^2).                (LEAD)

This is nonzero in Q and a p-unit for every p=6m+1>=7: every listed factorial argument is below p, while 2,3,m,4m+1 are all p-units. The *first excluded-rank differential obstruction* starts at EXACTLY t^3. Because the right-hand side of BOUND vanishes through order t^2, comparing coefficients of t^0,t^1,t^2 proves PF3 with no unaccounted endpoint. In particular, the p^3 boundary is genuinely sharp; computing modulo p^4 requires the fourth valuation band and cannot be achieved by prolonging the three-jet closure.

## Exact identification with the frozen original signed scalar

At p=6m+1 prime and t=p:

    -3m+p/2=1/2, -2m+p/3=1/3, -4m+2p/3=2/3.

Thus u[n](p) is EXACTLY (1/2)_n(1/3)_n(2/3)_n/(2^n(n!)^3), not a model substitute. All denominators for n<=4m<p are p-units. The authentic original weighted ranks n=4m+1..p-1 each have valuation at least 3 (the separately proved predecessor source). Consequently

    W_p = sum(n=0..p-1) (6n+1)u[n](p)
        = [(1+6theta)(F_0+pF_1+p^2F_2)] at z=1   (mod p^3).     (ORIGINAL)

The low-band n=m factor 6m+1=p remains as an original signed weight. This formula preserves the original full W_p observer, and no unproven WZ/seam or shifted-terminal auxiliary conjecture is used.

**Actual still-open target**, NOT inferred from PF3:

    [(1+6theta)(F_0+pF_1+p^2F_2)] at z=1 = p (mod p^3)
    for every prime p=13 or 19 (mod 24).

The new result is an exact *cross-band differential constraint plus sharp boundary*, not that the final target is true.

## Mathematical verification and provenance limits

An independent local author-side program, d25_picard_fuchs_three_jet_check_20261025.py, actually executed:
- symbolic exact expansion of P_t;
- exact Fraction construction of u[4m+1](t) through t^3 for m=1..5 and equality with LEAD;
- direct original Pochhammer coefficient recurrence compared rank-by-rank to the distinct polynomial-jet recurrence, and full W_p sums, for p=7,13,19,211,19963;
- first excluded cubic boundary leading coefficient modulo each prime.

All checks passed. W_p residues modulo p^3 for those five primes were 7,13,19,211,19963. The LEAD residues modulo p were 5,5,1,113,18031. The proof of the all-m statements is the rational factorization, recurrence and coefficient induction above, not the five-prime data. Finite numeric agreement is not a universal proof of the still-open original congruence.

BRC/Enterprise-coordinate discipline: this is a valuation-labelled, signed, original-rank jet carrier with future operations restricted to the linear differential system and mod-p^3 observer. Its auxiliary z is NOT a new native X6 spatial axis, and no BRC/Heartbeat native physical run was performed. Retain original signed ranks, P000, and frozen scientific Source; do not turn the scalar quotient into complete microscopic state.

## Next real scientific unit and exact Source boundary

Seek a bilinear concomitant for L0 and its formal adjoint that evaluates the combined source terms P1 F0 and P1 F1+P2 F0 under (1+6theta) at z=1; prove the still-open combined congruence for the two specified residue classes, or derive a genuine exact counterexample. This is stronger than separately assuming C_p=q_p(4/3) and S_m=p+p^2 q_p(4/3). Any p^4 extension must retain the now explicit nonzero cubic boundary defect.

Gateway 0.6.11 Site role currently has research_authority_granted=false and write_relay_enabled=false. No current Source-winning Researcher claim/run is evidenced, no native mathematical benchmark has run, no Source checkpoint/Result has been written, and no independent review/admission has occurred. Existing support enterprise-math#1539 still requires a validated own-session/permission recovery. This file is an allowed neutral GitHub author-side preservation record, never a source-native checkpoint, activity registration or role authorization. Do not reissue unsettled native requests under a different ID or borrow the maintenance conversation's identity.