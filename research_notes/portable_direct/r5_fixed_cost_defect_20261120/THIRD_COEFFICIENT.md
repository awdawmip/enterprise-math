# R5 — Third asymptotic coefficient: two seven-label witnesses enter exactly at order N^93

Date: 2026-11-20. Additive derivation to RESEARCH_R5_DEFECT_EXPONENT.md at the **same frozen scalar R5 pin**. Author symbolic proof and independent moment checks; NOT_REVIEWED.

Let m=2f+e+1 >=1 remain fixed, N the exact paid multiset cost, and Delta_m(N) the nondecodable-design count defined in the main R5 fifth-order manuscript. Set

Pout = product_{k=219}^{314} k,
J0 = binom(m+4,5),
J1 = 180(m-1)J0,
J2 = 116105 binom(m+4,6) + 699845 binom(m+4,7),
J7 = binom(m+6,7).

Here J1 is the first raw price moment of the finite failure-A polynomial Q_m at q=1; J2 is one-half of its second factorial price moment, i.e. Q''_m(1)/2.

## Strengthened exact asymptotic theorem

For each fixed integer m>=1,

Delta_m(N)
= J0 N^95/(95! Pout)
+ (12792 J0-J1) N^94/(94! Pout)
+ Gamma_m N^93/(93! Pout)
+ O_m(N^92),

where

Gamma_m = (244591414/3) J0
        - (25583/2) J1
        + J2
        + J7 * (219*220*221) * (1/214+1/215).

The **first contribution from the two seven-label witnesses B,C** is the last positive term. It has strictly positive leading coefficient, and appears at exactly N^93, two powers below the dominant five-label A witness. The other two witnesses M,L contribute at orders at most N^32 and N^83 respectively. Witness intersections start at most at N^92 and cannot change the stated N^93 coefficient.

Equivalently, if A_m(N) denotes the exact number of designs failing the five-label A witness,

Delta_m(N)-A_m(N)
= binom(m+6,7) * (219*220*221) * (1/214+1/215)
  * N^93/(93! Pout)
+ O_m(N^92).

Thus the new order-N^93 coefficient is an observer-specific, completely explicit "next separating-witness" correction, not merely the generic third Taylor coefficient of the dominant witness.

## Proof

For witness A, the generating function is Q_m(q) product_{k=219}^{314}(1-q^k)^-1, with Q_m from the main manuscript. For each s, the uniform occupancy vector (alpha_0,...,alpha_4) over all five-compositions of s has E(price)=216s. Writing w=(-2,-1,0,1,2), the standard occupancy moments are E(alpha_i)=s/5, E(alpha_i(alpha_i-1))=s(s-1)/15, E(alpha_i alpha_j)=s(s-1)/30 for i != j. Hence E[(sum_i w_i alpha_i)^2]=s(s+5)/3, and E[price^2]=(216s)^2+s(s+5)/3.

Using sum_s s*binom(s+4,4)=5 binom(m+4,6) and sum_s s(s-1)*binom(s+4,4)=30 binom(m+4,7), summing price*(price-1)/2 gives the exact J2 above. This is also independently verified by direct finite enumeration of all A-compositions for m in {1,2,3,4,5,17}.

Let S1=sum_{k=219}^{314}k=25584 and S2=sum_{k=219}^{314}k^2=6891856. The coefficient of N^93 in the polynomial part of the unrestricted 96-price product, after factoring 1/(93!Pout), is (3*S1^2-S2)/24=244591414/3. Combining it with the Q_m moments, including shifts of N by each A-composition's exact cost, yields the order N^93 coefficient

J2 - ((S1-1)/2)J1 + ((3*S1^2-S2)/24)J0.

The other four failure witnesses have cardinalities 7,7,68,17. Fixing fewer than m copies of a seven-price witness leaves 94 unconstrained types, hence its failure count has leading order N^93. The first coefficient for each is binom(m+6,7)/(93! product of complementary prices). For B and C the complementary products are respectively Pout*215/(219*220*221) and Pout*214/(219*220*221), giving the last term in Gamma_m.

The support-union of any two of A,B,C contains all eight distinct early labels {214,...,221}. Simultaneously failing any such pair bounds the total multiplicity of all eight labels by at most 2(m-1), leaving at most 93 unconstrained prices. Each such intersection is O_m(N^92). Intersections with M or L likewise cannot increase the order, and the individual M and L failure counts are O_m(N^32), O_m(N^83). By inclusion-exclusion, the claimed Gamma_m and O_m(N^92) remainder follow. QED.

## Checked values for Gamma_m * 93! * Pout

m=1: 1126735465100/13803
m=2: 2191356722009/4601
m=3: 7456025574970/4601
m=17: 4699616850358836/4601

These values are exact rationals, not decimal fits. No new native X6/BRC assertion or adaptive minimax bound is inferred.

## Next

The order N^92 term requires the second coefficients for B,C, the A-witness fourth pole coefficient, and the pairwise A/B, A/C and B/C intersections of eight early query labels. This is an explicit next finite combinatorial problem at the unchanged frozen pin.
