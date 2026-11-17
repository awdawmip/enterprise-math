# R749STP — Two initial adjacent scalar observations are exactly optimal for the pair 73/265

Date: 2026-11-17. Mathematical status: AUTHOR_EXACT_NOT_REVIEWED.
Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor: R749STO, https://github.com/awdawmip/enterprise-math/blob/a5a3e4cd753dd8d2ecc518f5533738db1506f64d/research_notes/portable_direct/2026-11-17_R749STO_EXACT_ONE_READ_FIBER_PHASE_TRANSITIONS.md
No shared Task CLAIM is asserted. This is the labeled five-source **auxiliary scalar observer**, not a native X6/Port/Cell equivalence.

## Exact model and quantifiers

There are five distinct labeled nonnegative integer source coordinates, with weights (1,1,2,3,6). Let C_n be the number of tuples of total weighted sum <= n-1 and T_n the sum of their **first** weight-one coordinate. Put

S(n)=18n^4+54n^3-345n^2+2070n-16315,
Y_n(e,d)=n^3 (T_n+e)/(C_n+d)-S(n)/108.

For candidate 73 fix (e,d) in [-2,2]^2 across all reads; for candidate 265 independently fix (E,D) in [-2,2]^2 across all reads. Write F_j=Y_{73+6j}(e,d)-Y_{265+6j}(E,D), for integer j>=0.

## New theorem: exact two-read optimum at the initial horizon

For **every** (e,d,E,D) in the real cube [-2,2]^4,

**F_0-F_1 >= δ**,

where the exact attained minimum is

δ = 980722950443484973593733668 / 6142123829965035791412569735 > 0
  = approximately 0.15967163437163523.

The equality minimizer is (e,d,E,D)=(-2,2,2,-2).

In particular, the two observations j=0,1 cannot both coincide under the two distinct candidates. Nevertheless, **one observation at j=0 can coincide**, since F_0 takes both negative and positive values over the connected nuisance cube. Consequently the exact minimum number of successive initial scalar reads needed to identify the candidate within {73,265} is

m_{73,265}^{initial}=2.

If each of the four measured scalar values has absolute additive error at most η, then the observed separator remains strictly positive whenever

0 <= η < δ/4 = 245180737610871243398433417 / 6142123829965035791412569735,

approximately η<0.03991790859290881. No probability model or independence of measurement errors is assumed.

This is a substantial strengthening of R749STN's sufficient two-time (j,2j) threshold j>=37: adjacent initial reads j=0,1 already separate all permitted nuisance states. Different time designs are being compared.

## Elementary proof with four finite exact rational checks

Define the six-step finite-difference observer

D_n(e,d)=Y_n(e,d)-Y_{n+6}(e,d).

Then F_0-F_1=D_73(e,d)-D_265(E,D). For n in {73,265}, put N=n+6. On the entire rectangle (e,d) in [-2,2]^2, the following positive lower bounds hold:

∂_e D_n = n^3/(C_n+d)-N^3/(C_N+d)
 >= n^3/(C_n+2)-N^3/(C_N-2) = a_n > 0.

-∂_d D_n = n^3(T_n+e)/(C_n+d)^2 - N^3(T_N+e)/(C_N+d)^2
 >= n^3(T_n-2)/(C_n+2)^2 - N^3(T_N+2)/(C_N-2)^2 = b_n > 0.

All denominators are positive: each listed C_n>2. Both inequalities follow by bounding their positive and negative terms separately, so no unverified correlation or numerical optimization enters.

The exact source counts are:

| n | C_n | T_n |
|---:|---:|---:|
| 73 | 707343 | 8931013 |
| 79 | 1020943 | 13914446 |
| 265 | 338147679 | 15099942957 |
| 271 | 377285215 | 17225006406 |

Substitution gives four strict-positive rational witnesses:

a_73 = 48414733542/722157511645 > 0;
b_73 = 188855589955784853136147/521511471625298310606025 > 0;
a_265 = 291148391248134/127578119851541053 > 0;
b_265 = 799849077100258385144721786239507/16276176664854173311160778944348809 > 0.

Thus D_n is strictly increasing in e and decreasing in d. Its minimum is D_n(-2,2), and its maximum D_n(2,-2). Therefore the global minimum of F_0-F_1 is

D_73(-2,2)-D_265(2,-2) = δ > 0.

This equality is exact and attained. On the other hand, the one-read F_0 has exact opposite-corner values

F_0(-2,2,2,-2) = -5139841969075768/717561205762695 < 0,
F_0(2,-2,-2,2) = 23581222102518344/717557156478663 > 0.

Continuity along the straight line joining those two legal nuisance quadruples supplies a genuine exact one-read collision, completing the minimality argument.

## Reproducibility and limits

The paired Python 3 certificate uses only the standard-library fractions module and exact integer dynamic programming. It independently constructs the five-source C_n and T_n counts, checks four derivative lower bounds, the exact attained δ, the one-read sign crossing, and the robust noise threshold. No floating-point or sampling step is used in the proof. Author execution: PASS, 2026-11-17.

The scalar observer intentionally forgets labeled provenance; retaining a future-relevant source difference requires an actual typed BRC/Port/Cell observer correspondence. The two-read theorem operates within the exact frozen auxiliary model and leaves the global unknown-q bound 5<=m_*<=11 untouched.

Next scientific units: classify the exact adjacent-time separators for other residue/gap pairs; derive optimal noise margins for the full two-read vector, rather than just F_0-F_1; construct and verify a provenance-preserving BRC readout with declared future-operation behavior.
