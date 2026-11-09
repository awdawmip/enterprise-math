# BRC-X6: Gram second-moment 13-minor bounds, universal 6037 / native 6017

2026-11-09. **AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**.

Frozen science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. This is an exact combinatorial theorem on the existing 24-by-38 labelled source/action incidence carrier of the 96-port, 576-labelled-action, nine-frozen-root signed-native system, not an unperformed D25 native Frobenius/CM experiment. The four preserved source ports are (6,7,28,29), with six actions each. The previous author-source balance 6387 bound / B=6388 construction (commit `b57db33df8b793cb856c45b0c84df0d0382fb730`) and the lawful thirteen-policy prefix are reused, not recredited.

## Theorem A: universal 13-column one-hot determinant bound

Let U be any 24-by-13 binary matrix whose rows have four blocks of six labelled source actions, with exactly one 1 in each block of each column. Every 13-by-13 row minor satisfies

```
abs(det(U_R)) <= 6037.
```

Put G=U^T U (PSD, diagonal 4, trace 52), let n_{p,a} be source/action occupancy across 13 columns, H=sum_{p,a} n_{p,a}^2, t_i=sum_p n_{p,v_{i,p}}, and T=sum_i t_i^2. For u=1/sqrt(13) times the all-ones column and P=I-uu^T, write G in basis u and u-perp as [[h,b^T],[b,B]], h=H/13. Then

```
det G <= h * det B                                 [Schur complement]
tr B = 52 - h
tr B^2 = tr G^2 - 2*T/13 + h^2
tr G^2 >= 156 + H                                 [integer overlaps m^2 >= m]
det B <= (((tr B)^2 - tr B^2)/132)^6              [Maclaurin e2, 12 eigenvalues]
```

and hence the **exact second-moment occupancy bound**

```
det G <= (H/13)*((2548 - 9*H + 2*T/13)/132)^6.        (1)
```

Every source has six nonnegative integer occupancies totalling 13. Each source sum of squares is at least 29; H is even and H>=116.

For H>=126, Rayleigh gives lambda_max(G)>=H/13>=126/13. By AM-GM for the other 12 eigenvalues and monotonicity on [4,52], det G <= (126/13)*((52-126/13)/12)^12 < 5980^2, all by exact rational comparison.

For 116<=H<=124, each source's occupancy-square sum is <=37, giving exactly nine sorted six-integer occupancy patterns. There are 21 unordered quadruples of patterns with total H<=124. For each source, create the 13-vector of occupancy counts repeated by their own multiplicities. The rearrangement inequality bounds T above by the sum of squared coordinatewise totals of the four *sorted* vectors. Inserting the 21 Tmax values into (1), with exact fractions, yields:

| H | patterns | maximal floor sqrt(det-G upper bound) |
| --- | ---: | ---: |
| 116 | 1 | 6037 |
| 118 | 1 | 5953 |
| 120 | 3 | 5909 |
| 122 | 5 | 5833 |
| 124 | 11 | 5803 |

Cauchy–Binet gives det G=sum_R det(U_R)^2, proving the claim, including rank-deficient cases. Enumeration can be reproduced with the following all-integer/fraction code (same counts as both supplied author's implementations):

```python
from itertools import combinations_with_replacement
from fractions import Fraction as F
from math import isqrt
patterns=[]
for a in combinations_with_replacement(range(14),6):
    if sum(a)!=13: continue
    h=sum(x*x for x in a)
    if h<=37:
        v=sorted((x for x in a for _ in range(x)),reverse=True)
        patterns.append((a,h,v))
assert len(patterns)==9
cases=[]
for ids in combinations_with_replacement(range(9),4):
    ps=[patterns[i] for i in ids]
    H=sum(p[1] for p in ps)
    if H>124: continue
    T=sum(sum(p[2][i] for p in ps)**2 for i in range(13))
    q=F(H,13)*F(33124-117*H+2*T,1716)**6
    b=isqrt(q.numerator//q.denominator)
    assert q.numerator < 6038**2*q.denominator
    cases.append((H,b))
assert len(cases)==21 and max(b for H,b in cases)==6037
assert F(126,13)*((F(52)-F(126,13))/12)**12 < 5980**2
```

## Theorem B: lawful native 38-strategy minor bound

Any 13 distinct legal columns from the frozen 24-by-38 matrix obey **abs(det(U_R))<=6017**. Source enumeration gives exactly 38 lawful tuples out of 1296; under all nine native roots they preserve the original signed joint observation. Their 703 distinct policy pairs have Hamming-distance census {2:160,3:120,4:423}; no pair coincides in three source actions.

For H>=118 Theorem A's case bounds are <=5979. If H=116, all four sources have occupancy (3,2,2,2,2,2). Each has one triple-occupied cell. Let q_i count how many source triple cells contain policy i. Sum_i q_i=12 and t_i=8+q_i, so T=1024+sum_i q_i^2. If q_i<=3 for all i, sum_i q_i^2 <=36. If any q_i=4, every other q_j<=2 (else the two columns share at least three labelled sources, contradicting Hamming>=2), so sum_i q_i^2<=16+2*8=32. Therefore T<=1060. The exact inequality (1) at H=116 gives det G<6018^2; all 13-row integer minors have absolute value <=6017. QED.

For any k<=12, column-norm Hadamard gives abs(det of any k-minor)<=2^k<=4096. Hence **all lawful minor orders k<=13 are bounded by 6017**.

## Corollary: strictly positive exact 9..13 minimum-support spectrum at radix 6018

Reuse the previously verified lawful 13-policy prefix, without independent novelty claims:

```
(0,0,2,2) (1,0,3,2) (2,2,4,4) (3,3,5,5) (4,4,0,0)
(4,4,5,5) (4,5,0,1) (5,1,1,3) (5,5,5,5)
(0,0,0,0) (0,0,1,1) (0,0,4,4) (0,1,2,3)
```

All prefixes k=9..13 have rank k and cover all 24 original source/action coordinates. For the native incidence column c(v), let B=6018, D_k=sum_{j=0}^{k-1} B^j, and x_k=(sum B^j c(v_j))/D_k. These are strictly positive source-normalized native strategies.

Suppose <=k-1 lawful columns span x_k. A nonzero integer minor functional annihilating their span has coefficients a_j on the independent prefix bounded by 6017, and at least one a_j nonzero. For the largest nonzero index d, the leading base-6018 term cannot cancel the smaller terms: 6017*sum_{j<d}6018^j=6018^d-1. Contradiction. Explicit k-term mixture supplies the upper bound; thus **minSupport(x_k)=k** exactly.

| k | old B=6388 denominator bits | new B=6018 denominator bits |
| ---: | ---: | ---: |
| 9 | 102 | **101** |
| 10 | 114 | **113** |
| 11 | 127 | **126** |
| 12 | 140 | **139** |
| 13 | 152 | **151** |

For k=13 the denominator is `2256827539473744321051951905733763772215981951` (151 bits). The independent challenge of constructing an *explicit* <=35-bit full-positive 13-minimal rational witness remains OPEN; previously claimed existential-only evidence is not replaced.

## Evidence and source boundary

The author's reproducible bundle contains: frozen native 9-root integer kernel, inherited exact-policy validator, exact 21-case + five native-witness verifier, separate ordered 140-case enumerator plus 48 deterministic exact Gram/minor checks, full 21-case rational JSON certificate, expanded theorem and per-file hash manifest. These are independent algorithms run by the same author/source, not an independent Driver review. Finite enumeration proves only the declared finite case; the universal claim additionally relies on the symbolic inequalities above.

The historical UR V2 four-file archive, 94687 bytes with SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`, has not been recovered, so its original publication/writer evidence remains pending. Previously completed UR mathematics is not redone. D25 original-class H0/B0, [X]U mod p², native eta/Frobenius/kappa and CM remain unfinished under their own frozen source. A historical continuation SUCCESS does not grant a present authenticated winning CLAIM. This author note is **NOT** a Source checkpoint, a frozen Result, a formal review or an admission.

Next exact unit: compute native arrangement-aware certificates to exclude <=12 supports for an **explicit** full-positive rational 13-optimal witness with <=35-bit denominator; conserve previous authors, science pin and Research1 J1/J2 separation.
