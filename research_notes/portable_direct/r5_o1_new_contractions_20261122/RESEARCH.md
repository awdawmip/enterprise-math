# R5 frozen scalar observer: exact second and third threshold contractions (m=51..100)

Date: 2026-11-22. Status: AUTHOR_EXACT_FINITE_PROOF / INTEGER_MODULAR_CRT / NOT_REVIEWED. Independent portable research; not a formal Task CLAIM/Result/Review. Frozen scientific input: enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15. Parent scientific frontier: enterprise-math@31e611df7fe607a4412be7c918f895065ba69ff0, with exact event definitions and prior m<=50 classification. The rooted mathematical observer does not change P000 or ACTIVE X6 semantics.

## Theorem: exact least coefficient periods for all 51<=m<=100

Let prices p=214,...,314 have multiplicity a_p>=0, N=sum_p p a_p. Put E_i(m)={sum_{p in S_i} a_p < m}, with
S0={214,215,216,217,218};
S1={214,216,217,218,219,220,221};
S2={215,216,217,218,219,220,221};
S3={223,...,290};
S4={296,...,312}.
Let F_m(q)=R_m(q)/D(q), D(q)=prod_{214<=p<=314}(1-q^p), count the union of the five E_i(m). Write M_m(O_m(N)) for the *strict minimum common period* of the degree >=2 quasipolynomial coefficient functions in [q^N]F_m(q). Define L=229746052653717600.

For every integer 51<=m<=100, the exact result is

| m | M_m(O_m(N)) | missing required primitive order |
|---|---:|---|
| 51-53 | L | none |
| 54-58 | L/29 = 7922277677714400 | 29 |
| 59 | L | none |
| 60-64 | L/2 = 114873026326858800 | 32 (order 16 survives) |
| 65-79 | L | none |
| 80-86 | L/43 = 5342931457063200 | 43 |
| 87-100 | L | none |

These include the **first 29-adic contraction** at m=54, **first 2-adic contraction** at m=60 and a second occurrence of the already rigorously classified 43-adic contraction at m=80..86. Every interval in the table is exact; no extrapolation to m>100 is asserted here.

## Upper bound and root-specific exact cancellations

The denominator pole multiplicity at primitive order d is n_d=# {p in [214,314]:d|p}. The 40 orders with n_d>=3 have LCM L; all other poles contribute only degree <=1. Order 29 is the only order divisible by 29 with n_d>=3. Order 32 is the only order carrying a factor 2^5 with n_d>=3. Order 43 is the only order divisible by 43 with n_d>=3. Thus exact cancellation of the order-29, -32 or -43 numerator at every primitive root reduces the respective uniform upper bound to L/29, L/2 or L/43.

Let A_m be the signed, exact joint-constraint numerator for the union of E0,E1,E2; B_m the numerator of E3; C_m that of E4. Since their price supports are disjoint,
R_m=1-(1-A_m)(1-B_m)(1-C_m).
For d=29, all three prices 232,261,290 divisible by 29 lie in S3; for d=32, the three multiples 224,256,288 also lie in S3. Therefore B_m(zeta_d)=0 identically. For S4 the 17 consecutive price residues are pairwise distinct, nonzero modulo d=29 and d=32. Its threshold generating function is
sum_{m>=1} Q_{S4,m}(zeta)t^(m-1) = 1/[(1-t)prod_{p in S4}(1-zeta^p t)]
= B_d(t)/(1-t^d), deg B_d=d-18.
Hence C_m(zeta_29)=0 for m mod29 in {13,...,28,0} and C_m(zeta_32)=0 for m mod32 in {16,...,31,0}. Both vanish on the claimed windows. Thus R_m(zeta_d)=A_m(zeta_d) there.

The crucial new exact cancellations of A_m for d=29,m=54..58 and d=32,m=60..64 are established by a fully exhaustive **multi-prime cyclotomic/CRT certificate**, not by treating a single finite-field zero as a complex zero.

For each nonempty I subset {0,1,2}, put U_I=union_{i in I} S_i, and Q_{I,m} equal the sum of q^(sum p*a_p) over all multiplicity vectors on U_I satisfying every joint bound sum_{p in S_i}a_p < m. Then
A_m(q)=sum_I (-1)^(|I|+1) Q_{I,m}(q) prod_{p in U_I}(1-q^p).
Each p in U_I belongs to at least one constrained S_i, hence a_p<=m-1. Therefore the integer polynomial coefficient L1 norm satisfies
||A_m||_1 <= sum_I 2^|U_I| m^|U_I| <= 7(2m)^8.
Reducing modulo the monic cyclotomic Phi_29 (x^28+...+1) or Phi_32 (x^16+1) gives coefficients whose absolute values are bounded conservatively by
H=2*7*(2*64)^8=1008806316530991104.
For each d we choose five distinct primes p congruent to 1 modulo d. The verifier evaluates the **full joint-event numerator at all phi(d) primitive d-th roots modulo each p**, not just one root. Degree below phi(d) and vanishing at all distinct roots imply the cyclotomic remainder is coefficientwise zero modulo p. Consequently every integer coefficient of the true remainder is divisible by the product P of the five primes. Since P>2H, the coefficient bounds force every coefficient to vanish over Z. This proves Phi_d divides A_m for each listed threshold and therefore R_m(zeta_d)=0 at every complex primitive root.

Exact split-prime sets:
- d=29: 10093,10151,10267,10499,10789; phi=28; P approximately 1.191521249342052e20.
- d=32: 10177,10273,10337,10369,10433; phi=16; P approximately 1.169116152504012e20.

All 5*28*5 plus 5*16*5 root/threshold tests returned zero for A_m, B_m, C_m and R_m, with no floating-point root evaluations. See VERIFY_CYCLOTOMIC_CRT.cpp and CRT_OUTPUT.txt.

For order 43 at m=80..86, reuse the exact characteristic-zero 43-phase theorem established in enterprise-math@c9329abecc9963667647a2774b351a33c0456b0a (RESEARCH.md); its m modulo 43 cancellation set is {0,37,...,42}. No new finite-field zero is used to infer order-43 cancellation.

## Matching lower bounds (strict minimality)

Use W={7,9,11,13,17,19,23,25,27,29,31,32,37,43}, lcm(W)=L. At each of the 50 thresholds m=51..100, the exact modular evaluator computes the numerator R_m(w_d) and Euler jet (q d/dq)R_m(w_d), at a finite-field primitive d-th root w_d. For every d in W other than its row's designated cancelled order, R_m(w_d) !=0, or n_d>=4 and the first jet is !=0. Since the polynomial has integer coefficients, a nonzero finite-field value rules out the corresponding characteristic-zero Phi_d (or Phi_d^2) divisibility. Hence every surviving required order contributes a pole of order >=3 and divides the strict coefficient period.

For m=60..64, the omitted d=32 order would otherwise lose the maximum 2-adic contribution. An additional primitive order-16 witness (field p=10177, w=1750, n_16=6) has nonzero zero-jet:
m: 60,61,62,63,64;
R_m(w): 7049,1456,1847,1665,162.
Therefore 16 divides the period, and lcm((W except 32) union {16})=L/2. For 29 and 43, lcm(W except d)=L/d. In the maximal-period rows every element of W contributes, giving L. Upper and lower bounds agree for every m in 51..100.

The 50*14=700 complete finite-field numerator/first-jet evaluations were executed in exact integer arithmetic. Earlier published m=45..50 full vectors match this new evaluator at all tested regression pairs (for example d=43,m=45..50 gives R0=8782,8662,8239,7185,8459,843 modulo 10321). Source algorithm is an in-place unbounded-knapsack DP indexed by a tuple of *joint* event counts, with coefficient and Euler-derivative jets; grouping by max(counts) recovers every threshold m from the same exact DP. Price occurrences in multiple events update all the corresponding counters simultaneously. See VERIFY_R5_PHASE_SCAN.cpp, and CRT witness implementation for distinct validation of the zero loci.

## Validation scope / provenance

Author-side local C++17 exact-integer execution returned:
- 700 finite-field jet rows for m=51..100, matching the above table, with order-16 extra checks for 60..64;
- 5 distinct split primes x every primitive d-root x 5 thresholds for each exact zero family, exhaustive;
- CRT product exceeds the proven universal coefficient bound by >100x;
- prior m=45..50 saved sample residues were reproduced.

Local evidence SHA256: VERIFY_R5_PHASE_SCAN.cpp = 0bb06e37376621c8fc0d11ab5ae9d1cb68fe0f471eb239a48adbfeca1e62048d; VERIFY_CYCLOTOMIC_CRT.cpp = 566c3a0ebe9ca52da48c55e5583aea50ba49268446036f93db3df2a2bd0a0dc0; CRT_OUTPUT.txt = 64bf9e233da1a1d11d179db3929e534ecc9603361fdd6f9bd05418b78e7fffc2. These refer to the **actual local tested bytes** and should not be substituted for GitHub blob readback. No Lean proof or independent peer review occurred.

The model's mathematical counting observer is a derived scalar projection only. Event intersection provenance and signed cancellation are kept, rather than reducing to a positive weighted BRC count that would lose the relevant root-of-unity information.

## Next open question

The finite-field scan through m=150 additionally *suggests* recurrences of 29- and 32-order zeros at 112..116 and 124..128, respectively, and a simultaneous 32/43 disappearance at 124..128. This is **not** yet a characteristic-zero theorem at those later thresholds: the longer CRT run did not complete within the local execution limit. Derive a genuinely rational all-threshold root-29/32 generating function or complete the exact higher-threshold cyclotomic proof. In particular, a compound contraction of L/86 at 124..128 is a testable conjecture, not an asserted period. Preserve the frozen R5 pin, original ownership, and NOT_REVIEWED status.
