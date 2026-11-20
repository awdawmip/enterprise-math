# R762HF — Exact finite signed-fibre saturation of the six-axis Port parity obstruction

Status: AUTHOR-VERIFIED EXACT FINITE CERTIFICATE / NOT_REVIEWED / NATIVE PRIMITIVE ADMISSION OPEN.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142.
Direct continuation of R762HE, Draft PR #2865 at b539f214746af9bd40694f45f7b1198d093f25f6. Frozen P000 source: a72226e2430ffa4786321ac86e7f0c599d5f0389. Original researcher provenance: EM-X6-3050F6; same original research line. This is a separately scoped candidate-language calculation, not a claim that P000 supplies native primitive TRIADIC_CLOSURE_E permission.

## Exact question, observer, and BRC provenance

Let X={0,1,2,3,4,5}. Named Port states are the 15 two-element subsets P of X. At every step P->Q choose a distinct Q meeting P in exactly one axis, yielding eight *named* unsigned choices. Its three-axis support S=P union Q is a composite label, never an extra primitive spatial direction. A signed event additionally chooses sigma in {+1,-1}, with relative X6 Cell displacement sigma*h_S, h_S=sum(e_i for i in S). BRC count is positive integer multiplicity of ordered Port histories and ordered sign choices. The event index increases by one independently of spatial displacement.

Fix P*= {0,1}. For an ordered unsigned walk w=(P0,...,Pm) with P0=Pm=P*, define its exact signed completion fibre:

    n(w) = number of sigma in {+1,-1}^m satisfying sum_t sigma_t*h_(P_(t-1) union P_t)=0 in Z^6.

Let U_m be all unsigned named Port-return walks, H_m the HE parity-zero necessary-filter count, F_m the number of these walks with n(w)>0, and Z_m=sum_w n(w). Distinguish F_m (Boolean support) from Z_m (positive BRC multiplicity).

## Theorem HF1: all-length exact signed BRC coefficient observer

In the Laurent polynomial ring L=Z[z_0^(+-1),...,z_5^(+-1)], for adjacent P,Q put

    K[P,Q] = z^(h_(P union Q)) + z^(-h_(P union Q))

and K[P,Q]=0 otherwise. Then for all m>=0,

    Z_m = CT (K^m)[P*,P*],

where CT extracts coefficient of z_0^0...z_5^0. If m is odd then Z_m=0. For any particular unsigned word w with nonzero Cell return, all six coordinate-incidence counts must be even, so F_m<=H_m. No cancellation of positive BRC paths is used: negative exponents encode displacement and the final coefficient selects a zero displacement.

Proof: multiplying a matrix entry expands into one term for each ordered Port transition and each of its two signed labels. Monomials multiply by adding the six signed Cell displacement coordinates; the constant term selects exactly the zero vector. The sum of the six displacement coordinates in any signed path is 3 sum_t sigma_t, which is odd for odd m and hence cannot vanish.

## Theorem HF2: parity obstruction is sufficient through eight events

For m in {0,2,4,6,8}, **every** unsigned return walk satisfying the HE six-axis support parity filter has at least one full signed X6 Cell-zero completion:

    F_m=H_m.

Exact signed fibre multiplicities and total signed BRC returns:

| m | U_m | H_m=F_m | Z_m |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 2 | 8 | 8 | 16 |
| 4 | 288 | 168 | 624 |
| 6 | 17,536 | 4,960 | 34,688 |
| 8 | 1,118,720 | 177,536 | 2,413,424 |

Thus the necessary parity filter has **zero false positives within the complete finite domain m<=8**. This statement is an exact finite theorem, not an unproved extension to arbitrary m.

The complete nonzero-fibre histogram for eight-event Port returns is:

| number of sign completions per unsigned path | number of paths |
|---:|---:|
| 4 | 9,600 |
| 6 | 19,200 |
| 8 | 33,120 |
| 10 | 7,200 |
| 12 | 47,808 |
| 16 | 18,936 |
| 18 | 7,632 |
| 20 | 4,224 |
| 24 | 23,136 |
| 36 | 2,112 |
| 40 | 4,224 |
| 70 | 344 |

These path multiplicities sum to 177,536. Their completion-weighted sum is 2,413,424. The 941,184 remaining unsigned Port-return histories fail the parity filter. This is an explicit BRC fibre stratification: knowing the parity or even Boolean completion support does not determine the number of signed histories.

## Exhaustive proof certificate, boundaries

R762HF_CHECK.cpp enumerates every ordered unsigned Port walk from the fixed named Port, eight choices at each step, for lengths 0,2,4,6,8, and filters exactly those returning to the initial Port. It computes the six-bit triple-incidence parity. For each parity-zero return it enumerates all 2^m sign vectors and tests all six exact integer sums, counting n(w). This covers all 8^m candidates per stated m, without probabilistic sampling. It checks U_m against the independent Johnson-graph spectral expression (8^m+5*2^m+9*(-2)^m)/15, and checks H_m against the previously established R762HE spectral/DP counts. Exact C++17 integer arithmetic and assertions are used; the largest intermediate here fits signed 64-bit.

Author execution: g++ -O3 -std=c++17 -Wall -Wextra -pedantic R762HF_CHECK.cpp && ./a.out; PASS, with exact histogram. These model-internal conclusions have not undergone independent mathematical review. P000 itself remains the frozen six-axis, one-time-axis ontology; this 3-axis support transition is a candidate composite path label. A native TRIADIC_CLOSURE_E typed permission/force law must be established separately before promoting this observer to original primitive dynamics.

## Next discriminating problem

Determine whether F_m=H_m for every even m for the same *candidate* Port language, or exhibit the shortest parity-zero Port-return walk with n(w)=0 (an explicit source word and six-axis incidence witness). One useful route is to classify balanced two-colourability of consecutive 3-subset supports on closed walks in the Johnson graph J(6,2), preserving the Port ordering; a finite m=10 or 12 exhaustive/semigroup certificate could sharpen the boundary. Independently, obtain the actual native force/Cell/Link/Port/time TRIADIC_CLOSURE_E permissions from the frozen task's applicable sources. No arbitrary-TASK extension, review acceptance, Activity publication or current CLAIM authority is asserted by this file.
