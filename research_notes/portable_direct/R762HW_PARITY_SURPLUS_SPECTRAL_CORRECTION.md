# R762HW — Exact positive parity surplus, strict descent, and second spectral scale

Date: 2026-11-21. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Mode: independent portable research; not a native CLAIM, PROGRESS, Result, Review or Foundation promotion.

## Provenance and scope

Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Frozen scientific inputs: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Direct predecessor R762HV: `30d6ed3e00f11ad5de23424a4fc1d7749f26e16e:research_notes/portable_direct/R762HV_PORT_PARITY_SPECTRAL_LAW.md`. Its exactly enumerated 15-Port / 6-axis composite support model and four characteristic-polynomial classes are reused unchanged. P000 and the ACTIVE worldview are untouched.

Ports are two-element subsets of X={0,...,5}. Each adjacent Port pair p,q (sharing exactly one axis) gives one three-axis support S=p union q. A rooted closed m-transition ordered path starts and ends at one fixed Port. `P_m` counts all such paths, and `E_m` counts those where every one of the six axis support counts is even. The BRC counting carrier is the nonnegative integer mass of labeled ordered paths; signed characters enter **only as a proved exact projection** of those source counts, never as positive mass cancellation. Time order, Port identity, support and multiplicity remain in the retained fine carrier.

## HW1 — exact positive trace decomposition

For a character x in {±1}^6, let M_x[p,q] equal the product of x_i over i in p union q when p,q are adjacent, zero otherwise. Define T_k(m)=tr(M_x^m) for any character with exactly k negative coordinates. Axis permutations make T_k depend only on k; complementing a character changes M_x to -M_x. For even m, T_{6-k}(m)=T_k(m). Symmetry between 15 roots and the six-bit character filter imply the **exact** identity

```text
E_m = [2 T_0(m) + 12 T_1(m) + 30 T_2(m) + 20 T_3(m)] / 960,
P_m = T_0(m)/15 = [8^m + 14·2^m]/15,
D_m := E_m - P_m/32
     = T_1(m)/80 + T_2(m)/32 + T_3(m)/48.         (HW1)
```

This equality holds for every even integer m>=0. For even m, each M_x is a real symmetric integer matrix, so each T_k(m) is the sum of even powers of real eigenvalues and is nonnegative. The k=1 class is nonzero. Thus `D_m>0`. In particular the proportion of parity-even rooted Port histories is **strictly above 1/32 at every finite even length**, while R762HV proved convergence to 1/32.

Proof: The character filter gives E_m(p)=64^{-1}∑_x (M_x^m)[p,p]. Sum over roots p and divide by 15 because S6 acts transitively on root Ports. Group characters by 0..6 negative axes, use binomial multiplicities 1,6,15,20,15,6,1, and for even m use the complement symmetry. Finally T_0=15P_m. The sign assertions follow from symmetry and spectral powers. This projection is limited to the stated parity observer; no quotient is claimed to preserve the underlying ordered path for arbitrary future use.

## HW2 — strict monotonicity of the conditional parity proportion

For every integer r>=1,

```text
E_(2r+2)/P_(2r+2) < E_(2r)/P_(2r),
and E_(2r)/P_(2r) decreases to 1/32.                 (HW2)
```

Here E_2/P_2=1, E_4/P_4=168/288=7/12, proving the first step. For r>=2, all mixed-character eigenvalues have modulus ≤rho=1+sqrt(33), as established from the exact characteristic polynomials in R762HV. Since mixed even traces are sums of nonnegative spectral powers, `D_(2r+2) <= rho^2 D_(2r)`. Meanwhile `P_(2r)= (64^r+14·4^r)/15` is a sum of two positive exponentials, so its successive ratio is increasing. At r=2,

```text
P_6/P_4 = 17536/288 > (1+sqrt(33))^2=34+2sqrt(33).
```

Consequently for all r>=2, `D_(2r+2)/P_(2r+2) < D_(2r)/P_(2r)`. Adding the fixed 1/32 proves HW2. This is an all-length proof, not an extrapolation from the finite census.

## HW3 — exact first correction and second exponential scale

The k=1 twisted characteristic polynomial is

```text
(t+2)^5 · (t²-2t-32) · (t²-2t-2)^4.
```

Its unique dominant eigenvalue in absolute value is `rho=1+sqrt(33)`, with multiplicity one. Across k=1 and k=5, there are twelve characters contributing this eigenvalue (or its negation). The next largest modulus among **all remaining mixed-character eigenvalues** is `sigma=5.850845...,` the unique root of `t³-2t²-28t+32=0` in (5,6). The cubic has its other roots in (-5,-4), (1,2); its positive root lies in (5.850,5.851). Other spectral factors from HV have smaller modulus.

Therefore, as even m tends to infinity,

```text
E_m - P_m/32 = rho^m/80 + O(sigma^m),                 (HW3a)
E_m/P_m = 1/32 + (3/16)(rho/8)^m + O((sigma/8)^m).    (HW3b)
```

These asymptotics have explicit positive leading coefficient, sharpening R762HV's unsigned O(rho^m) estimate. The O constants are absolute for the fixed 15-state model. Derivation: isolate the simple dominant root of T_1; all other terms in HW1 have spectral modulus ≤sigma. Divide by `P_m = 8^m(1+14/4^m)/15`; the denominator correction is exponentially smaller than the displayed second scale.

## HW4 — two reproducible computation routes, and a bounded exploratory search

`R762HW_CHECK.py` uses (i) nonnegative source-count DP over all Port/parity states through m=80, and independently (ii) Newton power sums of four exact characteristic polynomials through m=80. It checks HW1 at all even lengths, the 39 strict ratio inequalities between 2 and 80, and the spectral positivity identity. Exact arithmetic is used for assertions; decimal fractions printed at the end are readout only. Observed `PASS R762HW`. For example:

| m | E_m | P_m | E_m/P_m (display) |
|---:|---:|---:|---:|
| 2 | 8 | 8 | 1 |
| 4 | 168 | 288 | 0.583333333333 |
| 14 | 16,704,767,360 | 293,203,116,032 | 0.05697336231 |
| 26 | 677,370,234,552,288,468,992 | 20,148,763,660,243,882,213,376 | 0.03361845153 |
| 40 | 2,787,372,739,142,589,353,110,830,317,568,000 | 88,615,199,718,994,391,526,921,496,896,208,896 | 0.03145479272 |
| 80 | see executable evidence | see executable evidence | 0.03125021985 |

A separate bounded xorshift64 Port-walk exploration `R762HW_SAMPLE.cpp` sampled 125,000 rooted prefixes at each of m=14,16,18,20,22; the final transition was forced to return to the root when adjacent. Exactly 14,908 sampled closed histories had even axis counts; a carry-free base-32 half-subset test found zero sign-infeasible instances. These are reproducible **samples**, not an exhaustive absence certificate or a proof of the full signability conjecture.

## Research boundary and next unit

The theorem sharpens the parity-eligible population for the composite Port model. It does not decide the stronger finite zero-signing condition `C(n)>0`. Next attack: inspect exact support histograms with `N_p(n)>0` and all-even axis counts but `C(n)=0`; use rooted Port-Eulerian provenance and a lossless half-histogram BRC carrier. The exploratory sample supplies only bounded negative evidence. The P000 primitive triadic force/Cell/Link/Port/time/rotation lifting remains independent.

Independent mathematical review: NOT_REVIEWED. Native execution/CLAIM/PROGRESS: NOT_ASSERTED. Activity source association: pending separately authenticated write.