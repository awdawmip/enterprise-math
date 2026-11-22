# R5 frozen scalar observer: COMPLETE exact least period for every positive threshold

Date: 2026-11-22 (Asia/Shanghai). Status: **AUTHOR_DERIVED_EXACT_CONDITIONAL_COROLLARY / ARITHMETIC_CRT_RECOMPUTED / NOT_REVIEWED**.
This is *independent portable research*; no formal Task CLAIM/RUN/Result/Review or P000 promotion.
Immutable frozen scientific input: `awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15`.

## Theorem: eight regimes constitute the entire infinite classification

On prices p=214,...,314 with nonnegative integer multiplicities a_p, N=Σpa_p, retain the original five failure events E_i(m) with supports S0={214,215,216,217,218}, S1={214,216,217,218,219,220,221}, S2={215,216,217,218,219,220,221}, S3={223,...,290}, S4={296,...,312} and E_i(m) iff the total multiplicity on S_i is <m. Set F_m(q)=R_m(q)/∏_{p=214}^{314}(1-q^p) to count the union. Denote by M_m the strictly least common period of the coefficient quasipolynomial terms of degree ≥2 (modulo O_m(N)).

Set
```
L = 229746052653717600
K = 92119507880400 = L/(29*2*43)
A29(m) : m mod 58 in {0,54,55,56,57}
A32(m) : m mod 64 in {0,60,61,62,63}
A43(m) : m mod 43 in {0,37,38,39,40,41,42}.
```
Then, **conditional on the existing source-pinned author-side characteristic-zero and pole/jet theorems cited below**, for every integer m>=1,
```
M_m = K * (1 if A29(m) else 29)
        * (1 if A32(m) else 2)
        * (1 if A43(m) else 43).
```
The minimal period as a function of m is thus exactly periodic with a period dividing lcm(58,64,43)=79808. All eight distinct values actually occur.

| A29 | A32 | A43 | M_m | Count in one 79808-period | First positive m |
|---|---|---|---:|---:|---:|
| no | no | no | 229746052653717600 | 56304 | 1 |
| no | no | yes | 5342931457063200 | 10948 | 37 |
| no | yes | no | 114873026326858800 | 4752 | 60 |
| no | yes | yes | 2671465728531600 | 924 | 124 |
| yes | no | no | 7922277677714400 | 5292 | 54 |
| yes | no | yes | 184239015760800 | 1029 | 170 |
| yes | yes | no | 3961138838857200 | 468 | 576 |
| yes | yes | yes | 92119507880400 | 91 | 2492 |

This removes the previous open question of how to classify non-triple-contraction thresholds **in this frozen scalar observer**. The claim is a logical *new corollary* of previously saved all-m nonvanishing results, not a claim to have independently rerun their expensive integer-cyclotomic verifiers. Review of those underlying source theorems remains necessary before project admission.

## Proof: exact upper and lower bounds match

1. For a primitive d-th root of unity, the denominator has pole order n_d=# {p in [214,314]: d|p}. Only n_d>=3 can affect the N-degree≥2 coefficient functions. Direct exact integer enumeration gives 40 relevant orders and lcm of all 40 equal to L. Orders 29,32,43 each have n_d=3 and are the *only* relevant orders whose d is divisible by the corresponding order. Thus absence of their root contributions removes precisely the optional factors 29, 2^(5−4)=2 and 43 in the upper bound; all other pole orders divide K. (The factor 2^4 is separately preserved below.)

2. The frozen author-side root theorems yield the three exact all-m dichotomies: R_m(zeta_29)=0 iff A29; R_m(zeta_32)=0 iff A32; R_m(zeta_43)=0 iff A43. At each of 29,32,43 the original denominator pole order is exactly three. Consequently, if the corresponding A-condition holds, the numerator cancels the N-degree≥2 contribution; otherwise an order-three pole survives and the respective d divides M_m. The upper period therefore divides the displayed candidate U_m.

3. The prior all-m jet certificates show that primitive orders d in {7,11,13,17,19,23,25,27,31,37} contribute for every m>=1. At d=37, where n_37=3, the certified zero-order value is nonzero; for all other members n_d>=4 and the certified nonzero zero-order or Euler-first-jet leaves a pole of order >=3. Their least common multiple is the odd part of K.

4. For the 2-adic lower factor, if A32 is false the original order-32 pole survives, so 2^5 divides M_m. If A32 is true, m mod 64 is {0,60,61,62,63}, whence m mod 32 is {0,28,29,30,31}. The previous full-characteristic-zero order-16 theorem guarantees R_m(zeta_16)≠0 on those five residues; since n_16=6, order 16 survives and 2^4 divides M_m. In either case K divides M_m. The corresponding surviving 29,32,43 factors from step 2 make U_m divide M_m; combined with the upper bound M_m|U_m gives equality.

5. This is an exact root-of-unity statement about signed integer polynomials and their Euler jets. It preserves the joint incidence of the first three events; reducing the signed numerator to a positive BRC mass would erase cancellations. No claim about original X6 heartbeat dynamics follows from this scalar projection.

## Exact CRT count

In residues modulo lcm(58,64)=1856, A29 holds in 160 classes, A32 in 145, and both in 13: the two zero-residue sets each have 3 even and 2 odd representatives, so the shared parity compatibility condition gives 3×3+2×2=13. Therefore the four (A29,A32) counts are 13,147,132,1564 (both, only29, only32, neither). Modulo 43 independently, A43 holds in 7 classes and fails in 36. Multiplication gives exactly the eight table counts, summing to 79808. The triple-contraction density is 91/79808; full L occurs on 56304/79808 of positive m. The full theorem is period-79808, and each value is explicitly attained.

The accompanying `VERIFY_GLOBAL_PERIOD.py` computes the 40 denominator orders, lcm witnesses, all 79808 flags and counts, first examples, and eight exact integers with Python's integer-only standard library. Its output is a **logic/arithmetic consistency check**; it does not independently re-evaluate prior cyclotomic input certificates.

## Immutable proof dependencies

- **Frozen source and exact five-event scalar model**: enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15.
- **29/32 all-m characteristic-zero cancellation**: enterprise-math@74c74c94d7971bdd8594824b734e574f85d43fd2:research_notes/portable_direct/r5_allthreshold_29_32_20261122/RESEARCH.md.
- **43 all-m characteristic-zero cancellation**: enterprise-math@c9329abecc9963667647a2774b351a33c0456b0a:research_notes/portable_direct/r5_root43_allthreshold_phase_20261122/RESEARCH.md.
- **Full six additional orders 7/11/13/25/27/31 all-m jet proof**: enterprise-math@12d34b310988f62ecb34ce9b2fe8f56e99b30a12:research_notes/portable_direct/r5_triple_allphase_global_20261122/RESEARCH.md.
- **Other global surviving orders 17/19/23/37**: enterprise-math@6f0635fa79fc610410cdb88f39bf538d2ddac510:research_notes/portable_direct/r5_d23_firstjet_global_20261122.
- **Order16 survival in the exact A32 residue set**: enterprise-math@58cade8a57a76f16792b29fa4f0d2f437608f0b7:research_notes/portable_direct/r5_q_d16_exact_noexceptions_20261122/RESEARCH.md.

## Evidence, review, contribution and continuation

The present contribution is assembly of a missing **global logical implication**, full eight-value classification, exact density/counts, and bounded independent integer arithmetic/CRT verification. The above cyclotomic proofs are **reused** at their pinned author-proven scopes; their independent reviewer status remains NOT_REVIEWED. No native CLAIM/RUN is asserted. Existing identity for provenance: EM-DIRECT-D1A28F / RA-93CBA60ADED3274CF6CD2E83 / SID MCP-72b1951ce5d94267b6e60b1567acb22f; ownership and protected Activity writes require their own current authority.

Next: independently audit the six-cone root-pole bound and the R5 all-m characteristic-zero certificates; then seek structure in the now-complete eight-regime sequence (minimal fundamental threshold period, exact generating function for the classification, relations to native X6 observation maps). A complete conditional corollary is not a new P000 theorem or independently accepted Result.
