# D25/LIFT GH-120 — exact 2-primary torsion in all extension fields of the reflected CM curve

2026-10-30 Asia/Hong_Kong. Author-side conditional derivation with exact finite CM tests. UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Research lane chatgpt-research-hourly-enterprise-math-20260923, separately from maintenance. Preserve P000 and frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Scope and imported arithmetic

For any rational prime p>=11, p==3 (mod8), let q=p^2 and define C_T over F_q by

    v^2=u^3+u^2+((1+T)/8)u, T=2r/3, r^2=2 in F_q.

We consume the still-unreviewed GH-113, GH-116 and GH-117 discriminant -24 maximal-order CM bridge and signed Frobenius classification. For inert p==19 mod24 the q-Frobenius is scalar pi=[p]. For split p==11 mod24 choose p=2x^2+3y^2, x even, y odd, put A=2x^2-3y^2 and B=2xy, so pi=-A +/- B*s in the ring O=Z[s], s^2=-6. The sign of B will not affect the conclusions. As in GH-118/119, rational 2-primary torsion over F_q is exactly (Z/2)^2.

## New general theorem

For EVERY n>=1 put k(n)=1 when n is odd, and k(n)=v_2(n)+2 when n is even. Then

    C_T(F_(q^n))[2^infinity] = (Z/(2^{k(n)})Z)^2.

Consequently the least extension degree over F_q needed to make ALL geometric 2^j-torsion rational is

    1       if j=1;
    2       if j=2 or j=3;
    2^{j-2} if j>=4.

In particular, over F_(p^2) rational 2-primary torsion is (Z/2)^2, over F_(p^4) it is (Z/8)^2, over F_(p^8) it is (Z/16)^2, and over F_(p^16) it is (Z/32)^2. This is a statement about the auxiliary elliptic curve and finite-field extensions, not the Heartbeat native clock, GH-3 or the reflected tail R_p(9).

## Proof

In both CM branches pi == -1 (mod4 O). Inert: p==3 (mod8). Split: A==5 (mod8) and B is divisible by4, hence pi=-A +/- B*s == -1 (mod4 O). For any odd n this gives pi^n-1 divisible by2, with the scalar coefficient of (pi^n-1)/2 odd, and no divisibility by4 in O.

For n=2, in the split case

    pi^2-1=(A^2-6B^2-1) -/+ 2AB*s.

Since A==5 (mod8), A^2-1==8 (mod16). Since B is divisible by4, 6B^2 is divisible by16 and 2AB is divisible by8. Therefore pi^2-1=8u_1 with u_1 in O whose scalar coefficient is odd. The inert case has the identical property, since p^2-1==8 (mod16).

Inductively, assume pi^(2^t)-1=2^(t+2)u_t for t>=1, with u_t of odd scalar coefficient. Squaring,

    pi^(2^(t+1))-1 = 2^(t+3) * (u_t+2^(t+1)u_t^2).

The parenthesis reduces to u_t mod2, so has odd scalar coefficient. Thus pi^(2^t)-1 has maximal ordinary integer 2-power divisor exactly 2^(t+2) in O. For n=2^t h with h odd, expanding (1+2^(t+2)u_t)^h-1 and dividing by 2^(t+2) similarly gives h*u_t ==u_t modulo2; the maximal integer 2-power divisor is 2^(t+2).

The norm N(a+b*s)=a^2+6b^2 is ODD whenever the scalar coefficient a is odd. Hence N(pi^n-1), which equals #E(F_(q^n)), has exact 2-adic valuation 2k(n). Also pi^n-1 is divisible by [2^{k(n)}] as an endomorphism, so every geometric 2^{k(n)}-torsion point is rational over F_(q^n). Such full torsion contains 2^{2k(n)} points, exhausting the rational 2-primary order. This proves the claimed group. The minimal extension degree follows from k(n)>=j. QED.

## Actually executed bounded exact checks

Companion standard-library script d25_gh120_cm_torsion_tower_check.py uses exact arithmetic in Z[sqrt(-6)] (integer scalar inert branch). For each p=11,19,43,59,83,107,347,3347 and each extension degree n=1,...,12 it calculates pi^n-1, verifies exact integer divisibility by 2^{k(n)}, odd scalar quotient, odd norm quotient and v_2(N(pi^n-1))=2k(n). All 96 cases returned PASS. The p3347 sequence k(1..12) is 1,3,1,4,1,3,1,5,1,3,1,4. No additional finite-field point enumeration was performed. The all-prime/all-extension statement rests on the displayed conditional proof, not finite extrapolation.

BRC COMPOSE_APPLIED: preserve p, F_q, the elliptic curve, signed pi, extension degree n, exact 2-adic valuation and the 2^j-torsion observer. Passing only the order over F_q loses the higher extension behavior. The auxiliary number n is not asserted to be physical or native X6 time. Mathematical admission and independent review remain outstanding. The next different scientific obligation is independent CM/Jacobi/WZ/p-adic-period evaluation of R_p(9), with information beyond the signed trace, group and 2-primary tower; also preserve GH-83, original GH-3 and native p373 experimental obligations separately. Native Source ownership/recovery and protected session state remain under existing issue enterprise-math#1558.
