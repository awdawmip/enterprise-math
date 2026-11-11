# D25/LIFT — Lucas orbit norm and a signed-residual observer collision

Date: 2026-11-11. Status: AUTHOR-PROVED / EXACT-INTEGER-VERIFIED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_SOURCE_CHECKPOINT.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN. Frozen scientific pin: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. This note extends, without recrediting, the prior Möbius/Lucas quotient results. This finite-field auxiliary observation is not a native second-digit H0/B0 or Frobenius computation.

## Theorem 1 (all characteristics other than 2)

For any field F with char(F) != 2, integer m>=0, and lambda != -1 in F, put

Delta = (lambda+4)^2-8,
R = (lambda^2+6lambda+7)/(lambda+1),
C = (lambda^3+10lambda^2+27lambda+20)/(lambda+1).

Let L_0=2, L_1=C, J_0=0, J_1=1 and both satisfy Z_{n+1}=C Z_n-2 Z_{n-1}. Define H=R Delta J_m(C).

**Universal rational-function identity:**

    H^2 = Delta * (L_m(C)^2 - 2^(m+2)).                    (1)

Proof. In a splitting extension take alpha+beta=C, alpha*beta=2. Recurrences give L_m=alpha^m+beta^m and (alpha-beta)J_m=alpha^m-beta^m, including repeated roots by polynomial specialization. Hence L_m^2-(C^2-8)J_m^2=4*2^m. Direct expansion establishes C^2-8=R^2 Delta. Multiply the first identity by Delta, substitute the second and H=R Delta J_m. No division by Delta or R is used, so fixed fibers and degenerate cases are included. QED.

This constrains the signed BRC residual H by its norm. The reduced observer (L,Delta) determines H^2, but the weighted observer may depend on the sign of H.

## Theorem 2 (actual observer collision at p=31)

For p=31 take epsilon=0, m=5, T(t)=-2(t+1)/(t+2),
U(t)=(t+1)(t+2)^2/t, V(t)=U(t)^5,
w(t)=(2-3t)/(t+2), N=-2^(-10)=-1 mod31.
The legal orbit population is F_31 minus {0,-1,-2}; lambda=t+T(t).
For an orbit O, define A_O=N sum_O V and B_O=N sum_O V w.

| lambda | orbit O | U on ordered O | C | R | Delta | L_5 | J_5 | H | A_O | B_O |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | {13,25} | {11,3} | 14 | 20 | 20 | 1 | 13 | 23 | 30 | 27 |
| 16 | {2,14} | {24,13} | 6 | 12 | 20 | 1 | 30 | 8 | 30 | 10 |

All entries are exact mod31. The two legal moving orbits share (L_5,Delta)=(1,20), but H=23 and H=8=-23, and B_O=27 versus B_O=10. E.g. the lambda=7 orbit has V=(6,26), Vw=(10,25), giving B_O=-(10+25)=27; the lambda=16 orbit has V=(26,6), Vw=(5,16), giving B_O=-(5+16)=10. Each t maps to its other orbit element under T, and each displayed denominator is nonzero. This proves that compression to just (L,Delta) is not sufficient for the later weighted port operation. An orientation/provenance repair such as lambda and signed H, or an equivalent reconstructing carrier, remains necessary. H is computable from lambda and m, so we do not claim independence from the complete original orbit.

For epsilon=0 the prior exact reconstruction is A_O=N nu L and B_O=N nu[(2lambda+5)L-2H], where nu=1 on moving orbits and 1/2 on fixed orbits. For epsilon=1 let Q=((lambda+4)L+H)/2, then A_O=N nu Q and B_O=N nu(16L-13Q). The new norm law may be substituted into either branch, but does not by itself remove the signed H needed for B_O.

## Exact finite regression

An independent executable program in this research bundle checks all legal fibers for every prime 7<=p<=2500. Recurrence-based L,J and direct root powers U(t),U(T(t)) are computed separately, including repeated roots, p=31 collision and both A/B weighted observers. Actual run: **364 primes; 210031 distinct Möbius fibers, 352 fixed; every assertion passed.** The new identity is proved for all stated fields independently of this finite verification.

Next: seek an exact character-dependent moving-orbit cancellation identity preserving (lambda,L,H,epsilon) and fixed-orbit provenance, then bridge to the frozen Delta_p-R_p second-digit target. The earlier finite 3243-prime zero-port selector is not thereby a universal theorem.

Source history: prior author-portable notes `2026-11-11_h40_d25_mobius_orbit_quotient_lucas_two_port_author_portable.md` and `2026-11-11_h40_d25_mobius_fixed_orbit_exact_ports_author_portable.md`. Native Source claim/run unavailable. UR V2 original four-file bundle is still unverified (94687 bytes, SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76); no UR mathematics is repeated.