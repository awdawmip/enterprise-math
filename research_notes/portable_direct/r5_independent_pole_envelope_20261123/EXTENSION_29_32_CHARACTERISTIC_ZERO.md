# R5 primitive-29/32 cancellation: a second characteristic-zero proof without the joint-mask DP

Date: 2026-11-23 (Asia/Shanghai). Status: AUTHOR_EXACT_CHARACTERISTIC_ZERO_ZERO_PROOF / INDEPENDENT_FINITE_FIELD_NONZERO_CERTIFIED / NOT_REVIEWED. Source remains the frozen R5 five-event scalar model @75d986aa23b68a7ecf9b29dc1006f0e322b35a15. Extends the independent six-cone proof and modular experiment in this directory; it is not a formal independent Driver review.

## Result

For **all** integers m≥1, letting z_d be any primitive complex dth root of unity and R_m the correctly defined signed five-event numerator,

\[
R_m(z_{29})=0 \Longleftrightarrow m\bmod58\in\{0,54,55,56,57\},
\]
\[
R_m(z_{32})=0 \Longleftrightarrow m\bmod64\in\{0,60,61,62,63\}.
\]

The new part is an *algebraic characteristic-zero* reason for the five zero phases for each d, independent of the 2026-11-22 seven-mask inclusion-exclusion DP. The nonzero directions are separately witnessed by the independent finite-field six-cone checker in this directory, along with the rational all-m periodicity. The result is model-internal and not yet independently peer reviewed.

## Algebraic tail-vanishing lemma

From the exact disjoint six-cone identity in RESEARCH.md, write
\[
G_A(t,z)=\sum_{m\ge1}A_m(z)t^{m-1}.
\]
For each r∈{219,220,221} and each permutation (a,b,c) of (214,215,r), its rational cone summand is a t-independent scalar times
\[
\frac{a_*^{\delta_1}(a_*b_*t)^{\delta_2}}
{(1-t)\prod_{v=216}^{218}(1-z^v t)\,
(1-a_*b_*t)(1-a_*b_*c_*t^2)},\tag{1}
\]
where a_*=z^a, b_*=z^b, c_*=z^c, δ1=1 iff a>b in the fixed 214<215<r label order, and δ2=1 iff b>c. All scalar factors are regular: the cancelled D_U/(1-z^a) and the Lagrange β_r(z). Formula (1) holds in the characteristic-zero cyclotomic field Q(z) as a formal t series.

Take d=32. The five linear exponents modulo 32 are among 0,24,25,26,13,17,18,19,20; within each actual cone all five are pairwise distinct. The quadratic exponent 214+215+r is 8,9,10 modulo 32 for r=219,220,221, respectively. For the *same* r, none of the actual five linear exponents n obeys 2n ≡ 214+215+r (mod 32). Thus every denominator in (1) is a product of mutually coprime factors of 1−t^64, five linear and one quadratic, **total degree 7**. Its numerator has t-degree δ2≤1. Hence multiplying by 1−t^64 produces a polynomial of degree at most 64−7+1=58:
\[
\deg_t((1-t^{64})G_A(t,z_{32}))\le58.\tag{2}
\]
Because the product is a polynomial, and coefficient t^(m−1) for 1≤m≤64 is A_m(z), this proves **A_60(z)=⋯=A_64(z)=0** and A_(m+64)(z)=A_m(z) for every m≥1.

Take d=29. The five linear exponents are among 0,13,14,15,23,27,28,0,1. A collision with the fixed 1−t factor occurs **only** for four cones: r=220, ordered pair {215,220}, and r=221, ordered pair {214,221}, in both orientations. Apart from these the linear factors are distinct; and for each r the quadratic exponent 429+r is 10,11,12 modulo 29, never equal to twice any linear exponent in the same cone. Therefore every noncollision cone has the same degree-7 denominator property as at d32, and contributes a polynomial of degree ≤58−7+1=52 after multiplication by 1−t^58.

For the four collision cones, *pair the two cones with the same unordered first-two prices and the same last price c before multiplying by 1−t^58*. Let a_*,b_* be the root weights of the colliding pair, so a_*b_*=1 and b_*/(1−b_*)=−1/(1−a_*). Their shared other t factors include two copies of 1−t: the universal one and the pair factor. The scalar prefactors, the r-specific Lagrange coefficient, the shared-price factors, and the quadratic factor are identical for the two reversed orientations. The numerator after extracting their common factors is:

- r=220, (a,b,c)=(215,220,214) and (220,215,214). Since δ2=1 for both and δ1 is 0 and 1 respectively, the combination is
\[
\frac{t}{1-a_*}+\frac{b_*t}{1-b_*}=0.
\]
The pair cancels identically.
- r=221, (a,b,c)=(214,221,215) and (221,214,215). Here (δ1,δ2)=(0,1) and (1,0) respectively, so the combination is
\[
\frac{t}{1-a_*}+\frac{b_*}{1-b_*}
=\frac{t-1}{1-a_*}.
\]
The factor t−1 cancels **one** of the two 1−t denominator factors. The remaining denominator has degree 6, the remaining numerator degree 0. Therefore, after multiplication by 1−t^58, this combined contribution has degree at most 58−6=52.

After this exhaustive pairing, **every** surviving cone contribution to (1−t^58)G_A is polynomial of degree ≤52. Thus
\[
\deg_t((1-t^{58})G_A(t,z_{29}))\le52.\tag{3}
\]
In particular A_54(z)=⋯=A_58(z)=0 and A_(m+58)(z)=A_m(z) for every m≥1.

The simple collision inventory was independently enumerated by exact modular congruences over all 3×6×2d possible (r,permutation,t-root) cases: d32 has no repeated or mixed roots; d29 has only the four listed pair repetitions and no mixed quadratic-linear collision. No finite observation, numerical approximation or finite-characteristic zero is used for equations (2) and (3).

## Correct S4 zeros and full R_m

The disjoint long block B_m(z) vanishes identically for d29 and d32 because its Euler-type denominator factor D_{223..290}(z) contains at least three 29- or 32-divisible prices (so its zero-order value is 0). The **true** C_m(q)=D_Z(q)∑_{j=0}^{m−1}h_j(q^296,...,q^312) satisfies the exact d-periodic S4 transfer from RESEARCH.md because Z has 17 distinct nonzero residues modulo d29 and d32. In particular C_m(z)=0 for m mod d in {0,d−16,...,d−1}. Thus C_m(z29)=0 at m=54..58, and C_m(z32)=0 at m=60..64, including their respective 2d translates. Combining R_m=1−(1−A_m)(1−B_m)(1−C_m) and B_m=0 yields R_m=A_m+C_m−A_mC_m. Equations (2),(3) prove the stated **exact characteristic-zero zero phases** for every positive m.

## Independent nonzero half and what is *not* proved here

The accompanying Python script VERIFY_29_32_PHASES_MODULAR.py reconstructs A,C,R *without the seven-mask DP* as finite-field coefficients of the independent six-cone rational function. At primes p=929,5569,8353 (all p≡1 mod lcm(29,32)), for d29 there are 53 nonzero and 5 zero phases in 1..58; for d32 there are 59 nonzero and 5 zero phases in 1..64. It verifies the correct nonzero phase sets for each primitive root in all six (p,d) cases. An integer polynomial divisible by Φ_d vanishes at *every* primitive dth root in F_p for these p, so any observed nonzero value certifies characteristic-zero nonvanishing at all primitive complex roots by Galois conjugacy. Consequently this modular check establishes the **nonzero** half, while the new algebraic degree argument establishes the **zero** half. The classification is exact for all m, since the rational generating series prove 2d periodicity analytically.

This independently discharges one of the 8-regime theorem's main load-bearing author-level dependencies. It does not independently review the other full-threshold characteristic-zero root order 43, the ten surviving higher-pole orders or their corrected first jets. The eight-regime minimal-period theorem therefore remains an AUTHOR_CONDITIONAL_COROLLARY / NOT_REVIEWED. The proof uses signed cyclotomic values, not unsigned positive BRC mass; no lossless native X6 observation bridge is claimed.

## Reproduction and origin

Companion scientific notes: RESEARCH.md, EXTENSION_29_32_MODULAR.md.
Companion verifier: VERIFY_29_32_PHASES_MODULAR.py (three primes × two orders, all 4d thresholds).
Frozen input: enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15.
Original author implementation whose source dependency is independently rederived: enterprise-math@74c74c94d7971bdd8594824b734e574f85d43fd2.
S4 correction: enterprise-math@f5ef1521521888705104239328bbc1e6c62219db.
Next: audit root43 and the remaining lower-bound jet certificates at independent characteristic-zero semantics, including the typed source->observer preservation map.
