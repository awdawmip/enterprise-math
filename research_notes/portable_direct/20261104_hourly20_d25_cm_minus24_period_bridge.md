# D25 author-side CM discriminant −24 bridge for the 2304 Gauss/Jacobi port
Date: 2026-11-04. Status: AUTHOR-DERIVED / ALGEBRAIC IDENTITY EXACT / CM IDENTIFICATION SOURCE-CONFIRMED / 569-PRIME FINITE CHECK / UNREVIEWED / NOT_ADMITTED.

## Exact mathematical result
Let F(x)={}_2F_1(1/8,3/8;1;x), C(x)={}_2F_1(5/8,7/8;1;x). Euler's identity gives C(x)=(1-x)^(-1/2)F(x) as formal series at x=0.

The classical quadratic transformations, with the origin branches fixed, are
F(4X(1-X))={}_2F_1(1/4,3/4;1;X),
{}_2F_1(1/4,3/4;1;4t/(1+t)^2)=sqrt(1+t) {}_2F_1(1/2,1/2;1;t).
The last Gauss series is the Legendre period for E_t:y²=u(u−1)(u−t). This constructs an algebraic period-family bridge, NOT a native crystalline H0/B0 identification.

At x=1/9, 4X(1-X)=1/9 has branches X±=1/2±sqrt(2)/3. With X=4t/(1+t)^2, the Legendre invariant simplifies exactly to
j(t)=256(1-t+t²)^3/[t²(1-t)^2] =64(4-3X)^3/[X²(1-X)].
Direct computation in Q(sqrt(2)) gives
j±=2417472±1707264 sqrt(2),
H(T)=(T−j+)(T−j−)=T²−4834944T+14670139392.
The polynomial H is the known Hilbert class polynomial H_{−24} of Q(sqrt(−6)); verified by published class polynomial tables, OEIS A305474, LMFDB. The discriminant −24 point is therefore an exact external CM anchor for the original x=1/9 Gauss period, including both conjugate branches.

## Short-Jacobi observer and bounded evidence
For p=8q+5 prime define J_p(z)=sum_{k=0}^q binom(q,k)binom(3q+1,k)(z/9)^k in F_p[z]. Since 5/8=−q+5p/8 and 7/8=−(3q+1)+3p/8, coefficients J_p agree modulo p with the first q+1 coefficients of C(z).
An actual exact modular check of all 569 primes p≤20000 with p≡5 mod8 found:
 p≡13 mod24 (288): (-6/p)=−1, J_p(1)=0, J_p'(1)≠0;
 p≡ 5 mod24 (281): (-6/p)=+1, J_p(1)≠0, J_p'(1)=0.
Examples (p,J,J') are (13,0,12),(29,7,0),(37,0,30),(53,27,0),(373,0,41). The finite-class selection remains a CONJECTURE for all p; neither quadratic transformation alone proves the mod-p truncation-to-Hasse-jet comparison.

Deuring's theorem gives supersingular reduction of the CM E_t at good inert primes in Q(sqrt(−6)) and ordinary reduction at good split primes. Thus CM yields a discriminating candidate mechanism. Keep Q(sqrt(2)) (j-conjugacy), Q(sqrt(−6)) (CM Frobenius class), J and J' (two observers), original Hesse/Green odd branch and H0/B0 crystalline module distinct. In particular, a supersingular CM H¹ has no rank-one unit root; a rank-one native source identification still needs its own signed semilinear normalization and cannot be inferred from this curve.

## BRC carrier, verification and next science
Carrier: full quadratic pullback branches, prime class, exact j pair, Frobenius CM character, short Jacobi value and first derivative; target observation is the finite-field value/jet and eventual divided second p-adic digit. Do not collapse the two coefficient branches, signed Green ports, p-adic valuations or native provenance. Existing BRC observer preservation applied: COMPOSE_APPLIED.

Exact source checker: research_notes/portable_direct/d25_cm_minus24_period_bridge_20261104.py. Executed on 2026-11-04 using Python standard library: EXACT_CM_PASS and FINITE_CLASS_PASS primes=569 classes={5:281,13:288}. This is portable exact math, not the native fixed-373 experiment.

Next executable subunit: derive finite-field Hasse invariant + normalized differential pullback for the *specified* x=1/9 transformation, and an exact first-jet comparison J_p(1),J_p'(1) to the CM Hasse invariant and derivative. Then prove or disprove each selection class; apply prior short Jacobi–harmonic Green–Wronskian mod p² interface. Independently acquire genuine original-class native H0/B0 divided-power, [X]U, eta, and odd observer before comparing Delta_p−R_p. No repeated completed Source units.

## Sources and Source control
Hilbert polynomial: https://numberdb.org/Hilbert_class_polynomials ; https://oeis.org/A305474
LMFDB CM−24: https://www.lmfdb.org/EllipticCurve/2.2.8.1/81.1/b/2
Deuring theorem, Theorem 4.1: https://link.springer.com/article/10.1007/s10231-024-01528-x
Prior author-side Green–Wronskian: research_notes/portable_direct/20261104_hourly20_d25_short_jacobi_green_wronskian.md
Current Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3, Objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Read-only native continuation research-hourly20-20261104-2224-current-source-continuation SUCCEEDED Source 77771efa0ba4237a5c7f0710214775973ca435a3: checkpoint SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED; route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION; execution_authorized=false. Existing Source checkpoint/session and protected staging unchanged. This author-side document is NOT native progress, CLAIM, OPEN, Result or review.
