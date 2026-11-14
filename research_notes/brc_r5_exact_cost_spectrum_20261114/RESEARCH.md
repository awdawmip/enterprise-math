# R5: Exact all-pattern low-budget cost spectra and 13 cost-inert gap certificates

Date: 2026-11-14. Status: **author-side exact finite theorem / NOT_REVIEWED**. Science pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.

## Mathematical scope

This result concerns the **derived one-dimensional integer-event radius-2 center-cover observer** used in R5. The frozen generator produces 954 event boundaries ending at 1065 and 28 indexed inter-block gaps of length 3. A closure shortens its selected gap from 3 to 2 and translates all subsequent event positions by one. For any subset B of the 28 gaps, define

```
D_B = minimum number of event-index centers covering all events within radius 2
J_B(K) = minimum sum of distances to nearest chosen center among radius-2
         feasible subsets of event indices of cardinality K.
```

Infeasible budgets have J=+infinity. The 28 gap numbers are zero-based.

## Main exact finite results

1. Across **all 2^28 = 268,435,456 closure choices**, there are **exactly 32 distinct complete optimal-cost spectra**, considered as functions of K including their feasibility domains. This is a partition-DP count with exact integer arithmetic.
2. The following **13 gaps are globally inert for the entire J_B(K) observer**, including the feasibility threshold D_B:
   `0, 1, 7, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24`.
   For any configuration of the other gaps, toggling any one of these 13 does not alter any J_B(K). Thus the remaining 15 gap bits are sufficient to recover the **cost spectrum**, a stronger observer-specific claim than the previous 15-bit preservation of D alone.
3. For **K = 214,...,954**, the spectrum is independent of all 28 closure bits (the earlier fixed-budget monotone-sandwich theorem; newly checked for both endpoints with an independent C++ full-spectrum interval DP). All variation occurs at K=207,...,213.
4. The **joint distribution of all 32 low-budget spectra**, including exact pattern multiplicities, is recorded in `EXACT_OUTPUT.json`. Each count includes the 13 inert-bit multiplicity.

Summary by fixed center budget:

| K | Feasible closure patterns | Distinct finite costs | Min J | Max J |
|---:|---:|---:|---:|---:|
| 207 | 229,376 | 1 | 1116 | 1116 |
| 208 | 5,341,184 | 4 | 1102 | 1111 |
| 209 | 41,492,480 | 7 | 1095 | 1105 |
| 210 | 135,389,184 | 8 | 1088 | 1098 |
| 211 | 228,810,752 | 7 | 1081 | 1091 |
| 212 | 264,019,968 | 4 | 1075 | 1084 |
| 213 | 268,435,456 | 2 | 1069 | 1070 |

For K=207, **every** one of the 229,376 feasible closure configurations has J_B(207)=1116. At K=212, the exact distribution is: J=1075 for 201,326,592 patterns; J=1076 for 33,554,432; J=1077 for 28,508,160; J=1084 for 630,784; and 4,415,488 infeasible patterns. At K=213 the earlier result is recovered: 201,326,592 patterns cost 1069, the rest 67,108,864 cost 1070.

## Proof and exact finite certificate

There are 29 initial blocks, separated by the 28 length-3 gaps. For every block interval 0<=a<=b<=28, let P[a,b] be the optimal-cost profile when all gaps strictly inside that interval are closed. There are exactly 29*30/2=435 such interval profiles.

**Independent-run lemma:** An unclosed gap has length 3. No center on one side of it can cover an event on the other side within radius 2. Accordingly, for a closure pattern whose maximal consecutively connected block runs are R_1,...,R_m, its exact budget spectrum is the *min-plus convolution* of the local run spectra. This holds for event-index centers and sum-of-nearest-distances cost.

**Contiguous-center-cluster lemma:** On the ordered integer event coordinates, use a consistent nearest-center tie rule to partition the event sequence into contiguous served clusters. Each chosen center serves its own event, and a valid cluster [a,b) has event-coordinate diameter <=4. Its exact cost is the minimum, over event indices j in [a,b) with both endpoint distances <=2, of the sum of |x_t-x_j|. The recurrence over interval endings and center count computes P[a,b] exactly, without a heuristic or floating-point arithmetic.

Let d(P) denote the least feasible center count. Store the truncated profile p(P)=(J(d),...,J(d+6)), with +infinity for genuinely unavailable extra budgets. For profiles P=(d,p), Q=(d',q), define

```
P star Q = (d+d', r)
r[e] = min( p[i] + q[e-i] : 0 <= i <= e ), 0 <= e <= 6.
```

The 6-extra-center window is exact for the global low-budget question: all patterns satisfy 207 <= D_B <= 213, and any K<=213 above D_B differs from D_B by at most 6. Convolution of truncated profiles is associative on these coefficients.

**Inert-cut certificate.** For each cut i and every pair a<=i<b, check

```
P[a,b] == P[a,i] star P[i+1,b].
```

There are exactly SUM_{i=0}^{27} (i+1)(28-i) = 4,060 comparisons of exact (minimum-budget, 7-value) profiles. The identity holds for **every** straddling pair precisely for the 13 listed gaps. In any closure pattern, changing an inert cut either splits or joins one maximal run; the identity makes this change preserve its exact low-budget profile, and associativity preserves the global profile. For K>=214 the previously established closure-invariant spectrum completes the all-budget conclusion. This is a certificate of **observer-specific** redundancy, not a collapse of native provenance or X6 state.

**All-pattern distribution certificate.** A partition of the 29 blocks into maximal connected runs is in bijection with a 28-bit closure pattern. Define State[j] as a counter from truncated spectra to the number of partitions of the first j blocks. Initialize State[0] with the identity profile. For every j=1,...,29 and every last-run starting index i<j, convolve each State[i] with P[i,j-1], add its count to State[j]. This adds each partition exactly once. The aggregate count at step j equals 2^(j-1). At j=29, the exact dynamic program yields **32** distinct spectra with multiplicities totaling **268,435,456**. The 32 exact rows and the full per-K distributions are in `EXACT_OUTPUT.json`.

## Verification actually performed

The frozen event generator uses exact Fraction values. A Python implementation computes the 435 local interval profiles with integer-valued contiguous-cluster dynamic programming, checks all 4,060 local identities and builds the 32-state distribution. An independent chosen-center edge DP was executed for all **32 exact representative closure configurations**, checking the complete relevant K=D,...,213 segment. Another 12 seeded closure patterns were independently checked. A separate independently compiled C++ full-spectrum DP checked the no-closure and all-closure endpoints for all K=207,...,954 and verified their equality at every K>=214. The main Python run returned `PASS_EXACT_R5_LOW_BUDGET_FULL_PATTERN_SPECTRUM`.

This proof uses 435 exact interval recurrences and the partition-counting identity to cover all 2^28 configurations. It does **not** claim that all configurations were individually brute-force enumerated. The existing frozen input is the R5 15-weight event generator from the earlier GitHub research note and immutable source pin.

## Preserved scope and next problem

The 15-bit quotient is now exact for the full **fixed-budget optimal total-cost spectrum and feasibility**, for this frozen derived observer. Center identities, number of minimizers, reconfiguration distances, signed/branched BRC provenance, future native updates, and X6 relations remain separately typed.

Next: build a compact **optimal-center witness-set representation** over these 32 spectrum classes and test whether the 13 cost-inert gaps may still change minimizer multiplicities and optimal edit distances. Separately retain the native 2,520-byte/28-coordinate/8,192-prefix-query end-to-end experiment and independent mathematical Result/Review.

Earlier source: `research_notes/brc_r5_all_closure_jk_sandwich_20261114/RESEARCH.md` at `136928dfd4d66b8fefce72a7067fdfed834f3e9f`. This note is not a formal Task CLAIM, Result, independent review or Foundation promotion.
