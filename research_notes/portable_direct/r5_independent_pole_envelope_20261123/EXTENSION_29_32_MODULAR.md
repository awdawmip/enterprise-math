# R5 independent finite-field audit of the primitive-29/32 phase masks

Date: 2026-11-23. Status: INDEPENDENT_IMPLEMENTATION_FINITE_FIELD_CROSSCHECK / CONDITIONAL_SCIENCE / NOT_REVIEWED. Supplements RESEARCH.md in the same directory. No shared CLAIM/RUN or formal independent mathematical review.

## What was independently recomputed

The previously archived proof at enterprise-math@74c74c94d7971bdd8594824b734e574f85d43fd2 used seven nonempty inclusion-exclusion subsets with a joint-incidence dynamic program, and characteristic-zero quotient rings, to prove the exact phase-zero sets for primitive root orders 29 and 32. This new checker does **not** reuse that DP or those cyclotomic arrays: it evaluates the *closed, disjoint six-cone rational series* from the accompanying RESEARCH.md over three prime fields F_p, with p∈{929,5569,8353} and p≡1 mod lcm(29,32).

At each d it constructs a primitive dth root z in F_p and evaluates, coefficient by coefficient, the t generating series
G_A(t,z) = sum_(m>=1) A_m(z)t^(m-1)
using the six permutation cones, the three shared-price geometric factors, and the Lagrange coefficients for the 219/220/221 block. It evaluates the genuine total-item-count S4 series
G_C(t,z)=D_Z(z)/[(1-t) prod_(p∈Z)(1-z^p t)]
rather than the previously incorrect product of (1-z^(mp)). It then evaluates R_m=A_m+C_m−A_m*C_m pointwise in m.

The program generates all 4d consecutive threshold coefficients for each (p,d), including two full periods of length 2d, and verifies A,C,R at m and m+2d agree. The results were:

| p | order d | primitive z mod p | exact finite-field zero phases among 1..4d |
|--:|--:|--:|---|
| 929 | 29 | 347 | 54..58, 112..116 |
| 929 | 32 | 701 | 60..64, 124..128 |
| 5569 | 29 | 3887 | 54..58, 112..116 |
| 5569 | 32 | 2391 | 60..64, 124..128 |
| 8353 | 29 | 6329 | 54..58, 112..116 |
| 8353 | 32 | 1516 | 60..64, 124..128 |

Actual local run result: PASS: 3 primes x 2 orders, exact finite-field cone-series masks and 2d phase duplication. No floating point arithmetic is used; all divisions are only by field elements known nonzero from the root/cone conditions. The 29-order computation has 106 nonzero and 10 zero phases across 116 thresholds; the 32-order computation has 118 nonzero and 10 zero phases across 128.

## What the calculation proves, and what remains conditional

A finite-field **nonzero** evaluation at a primitive dth root is a valid witness that the corresponding characteristic-zero cyclotomic polynomial does not vanish, since integer-polynomial divisibility by Φ_d would imply zero upon every such reduction to a primitive mod-p root. Thus all observed nonzero phase results here independently certify characteristic-zero nonvanishing for their respective congruence classes, combined with the previously proved *rational* all-m 2d-periodicity.

A finite-field zero, even for three primes, is not a characteristic-zero zero proof. Accordingly the exact zero classification at 54..58 and 60..64 retains its source-pinned characteristic-zero joint-DP proof at @74c74c94; this check is a genuine independent implementation crosscheck and cannot replace that proof.

The all-m periodicity follows analytically from the rational pole factorization (not from the two-cycle comparison). The six-cone exact decomposition and the properness/no-finite-prefix argument are in RESEARCH.md; the modular code independently supplies the small characteristic-prime validation that they yield the expected target phase behavior.

## Reproduce and next

Run Python 3 standard-library command: python VERIFY_29_32_PHASES_MODULAR.py. The script computes the modular primitive roots and all coefficients from scratch without reading archives.

Next: a direct second characteristic-zero proof of the five *zero* phases for 29 and 32 using the cone rational identity, avoiding the original seven-subset DP, and a separate check of the global eight-regime lower-bound jet witnesses under the repaired S4 transfer. This note changes no frozen model or canonical P000 truth status.
