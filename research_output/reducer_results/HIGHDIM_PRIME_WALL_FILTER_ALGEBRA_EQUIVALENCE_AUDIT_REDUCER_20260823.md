# Reducer Result — High-Dimensional Prime Wall Filter Algebra

Status: `TERMINAL_EXACT_CLASSIFICATION`

Researcher-ID: `EM-HDPWA-03E870`

Task-ID: `RS-HIGHDIM-PRIME-WALL-FILTER-ALGEBRA-EQUIVALENCE-AUDIT`

## Exact reduction certificate

Let `X` denote the positive-coordinate series `S(q)` and let
`delta_square(n)=[q^n]S(q)`.

1. Four-dimensional wall:

   `P4(X)=2(1+X)^4-4(1+X)^3+3(1+X)^2`

   `     =1+2X+3X^2+4X^3+2X^4`.

   Therefore

   `(1+2X)^4=8P4(X)-7-8X`,

   and, coefficientwise for `n>=1`,

   `Q4(n)=r4(n)/8+delta_square(n)`.

2. Eight-dimensional wall:

   `P8(X)=16(1+X)^8-64(1+X)^7+112(1+X)^6-112(1+X)^5`

   `     +70(1+X)^4-28(1+X)^3+7(1+X)^2`

   `     =1+2X+7X^2+28X^3+70X^4+112X^5+112X^6+64X^7+16X^8`.

   Therefore

   `(1+2X)^8=16P8(X)-15-16X`,

   and

   `Q8(n)=r8(n)/16+delta_square(n)`.

3. Insert the exact square-representation formulas:

   `r4(n)/8=sum_{d|n,4 does not divide d}d`,

   `r8(n)/16=sum_{d|n}(-1)^(n+d)d^3`.

   For odd `n`, this reduces to

   `Q4(n)=sigma1(n)+delta_square(n)`,

   `Q8(n)=sigma3(n)+delta_square(n)`.

4. Prime-wall reducer:

   For prime `p`, both square indicators vanish and the divisor sums are
   `1+p` and `1+p^3`.  For composite odd `n`, at least one additional proper divisor
   gives strict excess.  Hence both biconditionals are exact.  For distinct odd primes,

   `Q4(pq)-(pq+1)=p+q`.

5. Lambda reducer:

   On formal prime-admissible grades `s=2,3,4`, compare

   `(6lambda^2,4lambda^3,lambda^4)` with `(3,4,2)`.

   Nonzero proportionality is equivalent to

   `2lambda^2=lambda^3=lambda^4/2`,

   whose unique characteristic-zero solution is `lambda=2`.  The per-fixed-prime
   active-grade reading is not equivalent and is refuted by singleton support at `p=3`.

6. Twelve-dimensional reducer:

   With `eta(2z)^12=sum a(n)q^n`,

   `r12(n)=8sigma5(n)-512sigma5(n/4)+16a(n)`.

   For primes,

   `r12(p)=8(p^5+1)+16a(p)`.

   BLGHT Corollary 8.6 proves that

   `(r12(p)-8(p^5+1))/(32p^(5/2))=a(p)/(2p^(5/2))`

   is Sato–Tate distributed.  The post-classical project residual is exactly zero.

## H1–H8 terminal labels

| H | Label |
|---|---|
| H1 | `EXACT_NEW_PRESENTATION_ONLY` |
| H2 | `REQUIRES_SCOPE_NARROWING` |
| H3 | `REQUIRES_SCOPE_NARROWING` |
| H4 | `EXACT_NEW_PRESENTATION_ONLY` |
| H5 | `CLASSICALLY_EQUIVALENT` |
| H6 | `CLASSICALLY_EQUIVALENT` |
| H7 | `REQUIRES_SCOPE_NARROWING` |
| H8 | `CLASSICALLY_EQUIVALENT` |

Aggregate verdict: `SCOPE_NARROWING_REQUIRED`.

After the stated repairs, all surviving content is classical mathematics or a useful
project-specific presentation.  No falsifiable nonclassical residual survives subtraction.

## Validation summary

- Independent checker: `PASS`, `0<=n<=2048`, `d<=12`.
- Prime powers, products of two and three distinct primes, and 4-adic cases: `PASS`.
- Deliberately incorrect `Q4` coefficient vector: `FAIL_AS_EXPECTED`, first odd mismatch `n=5`.
- Source-free proof checkpoint frozen before classical audit: `PASS`.
- Withheld source proof/branch read: `NO` (Driver reconciliation boundary preserved).
- Tool reuse lookup: `COMPOSE_EXISTING_TOOLS` (`T1_SCALE_ENUMERATION_VALUATION` plus
  `D1_PRIME_TOOLKIT`); checker classified as task-specific evidence, not a new tool family.
