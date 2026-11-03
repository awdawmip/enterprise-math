# PREFIX-456 — Exact quintic X6–BRC boundary ranks for every q≥2

Date: 2026-11-03. Status: AUTHOR_PROVED / EXACT_COMPUTER_CERTIFICATE / UNREVIEWED. Continues PREFIX-455 at 8950812aa6528f7c3c465e3fd9870cf5dfc40b25. Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. P000 native six-axis path semantics, history provenance, and declared polynomial BRC observer are retained.

## Theorem

Let q≥2, N=q+3, and let each ordered native X6 path consist of N signed unit-axis steps. Its history sector r is the number of negative e₁ steps modulo q. For each r observe all six-axis joint endpoint monomials of total degree≤5, integrated against arbitrary nonnegative rational path weights. There are B₅=binom(11,6)=462 nominal coordinates in each sector. The exact rational linear snapshot rank is

    R₅(q)=882          q=2
          1329         q=3
          1785         q=4
          462q−64      q≥5.

The first q−1 sectors each have rank 462. The final sector has rank 420, 405, 399 or 398 when q is 2, 3, 4 or at least 5, respectively. Their defects from 462 are 42,57,63,64. At N=q+3, degree≤4 moments have full 210q rank; the minimum additional independent *linear* fifth-degree moment coordinates are 462,699,945,252q−64, respectively. Minimality is for the declared fixed-support rational linear observer.

## Exact support derivation

Define D as the eleven native steps {+e₁,±e₂,±e₃,±e₄,±e₅,±e₆}; W_m is its m-step endpoint set. A residue-r path has k=r+ℓq negative-e₁ steps, hence its support is the union of −(r+ℓq)e₁+W_(N−r−ℓq) for allowed ℓ.

For each r≤q−2, construct a path with r negative e₁ steps, q−r−2 positive e₁ steps, and five D-steps. Seven D-vectors have six independent affine differences and their five-step sums contain an invertible affine image of the complete six-variable simplex of degree≤5. Multivariate falling-factorial interpolation proves all 462 fifth-degree monomial evaluations independent in these sectors.

For the final sector r=q−1, translate its first coordinate by q−1. The support becomes

    T_q = union over ℓ≥0 with ℓq≤4 of (−ℓq e₁+W_(4−ℓq)).

For q=2 this is W₄∪(−2e₁+W₂)∪{−4e₁}, with 805 distinct points; for q=3 it is W₄∪(−3e₁+W₁), with 754; for q=4 it is W₄∪{−4e₁}, with 744; and for all q≥5 it is W₄, with 743. Thus only four finite integer evaluation matrices, each of width 462, are needed for the complete all-q classification.

## Characteristic-zero exact rank certificate

The attached executed Python/NumPy program enumerates the complete sets T_q by exact integer recurrence, all 462 degree≤5 monomials, and their integer matrices A. Every entry has absolute value at most 1024. It generates 66 distinct primes for q=2 and 64 distinct primes for q=3,4,5, starting below 2³¹; primality is checked by integer trial division to the square root.

At each prime p, modular Gaussian elimination yields exactly the claimed rank r. This gives rank_Q(A)≥r. To prove the opposite inequality, the program computes P, the product of all selected distinct primes, and the *exact* squared Hadamard bound H², obtained by multiplying the r+1 largest squared Euclidean norms of the integer columns of A. Every (r+1)×(r+1) determinant is divisible by P because all modular ranks equal r. Hadamard gives determinant squared≤H². The strict exact-integer test P²>H² therefore forces every such determinant to be zero. Hence rank_Q(A)≤r, proving equality over Q.

All modular arithmetic fits int64: for p<2³¹, the largest intermediate product or subtraction magnitude is bounded by (p−1)²+(p−1)<2⁶³.

| q | terminal support | exact rank | primes checked | bits(P²) | bits(H²) |
|---:|---:|---:|---:|---:|---:|
| 2 | 805 | 420 | 66 | 4092 | 4038 |
| 3 | 754 | 405 | 64 | 3968 | 3947 |
| 4 | 744 | 399 | 64 | 3968 | 3910 |
| ≥5 | 743 | 398 | 64 | 3968 | 3905 |

For q=4 there is also a direct analytic one-coordinate explanation: all W₄ endpoints have first coordinate z∈{0,1,2,3,4}, so g(z)=z(z−1)(z−2)(z−3)(z−4) vanishes on W₄ but not at the new point −4e₁. By the previous exact W₄ rank 398, one extra point raises it to 399. Relative to q≥5, the wraparound terminal states recover 22 coordinates at q=2, seven at q=3, one at q=4.

## BRC readout and future operations

Carrier: positive-rational masses on reachable endpoint/history pairs, with ordered native path multiplicities and provenance retained at source. Observer: all mixed-axis degree≤5 moments, sector by sector. Allowed future language: finite parallel addition, history-conditioned positive-rational branching, and rational-affine polynomial pullbacks. On each fixed reachable support, choose a rational monomial basis of the proven dimension and reconstruct all omitted quintic moments by exact rational linear combinations. Reconstruct the full standard fifth-degree port before applying the native BRC moment update. This yields exact declared-future degree≤5 observations. A changed support uses its own decoder. BRC status: REUSE_APPLIED; no new BRC family or global theorem admission claimed.

## Reproduction and status

Files in this directory:
- prefix456_quintic_crt_certificate.py — fully executed finite exact certificate; invoke separately as python prefix456_quintic_crt_certificate.py 2 3 and python prefix456_quintic_crt_certificate.py 4 5.
- PREFIX456_CRT_EXACT.log — the combined actual stdout from both completed invocations.

All four certificates returned PASS, including exact modular ranks and the full upper-bound inequalities. During development the same modular implementation reproduced PREFIX-455's degree-four q=2,3,4 ranks 169,163,162. This is an author-side exact computer-assisted mathematical proof. Independent review, formal Source Result and admission remain separate steps. Scientific pin remains unchanged.

## Next precise question

PREFIX-457: classify the general-degree nullspace of polynomials of degree≤d on W_(d−1)(D), testing and proving or correcting the candidate 16(d−1) deficiency for d≥3. A parallel integration unit is to construct explicit compressed quintic rational decoders for the four support regimes and measure their bit-length, streaming, and native BRC typed-codec costs.
