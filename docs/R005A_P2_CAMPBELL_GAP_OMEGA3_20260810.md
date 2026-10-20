# R005-A — p=2 Residual Arity Extension via Campbell 2026

Status: `PROVED R005 TRANSFER FROM PUBLISHED FINITE GAP INPUT / NOT CANONICAL`  
Date: `2026-08-10`

## 1. New external input

Campbell's 2026 paper proves that every interval between consecutive squares contains an integer with at most three prime factors. That ambient almost-prime theorem is not the same as the R005 residual statement.

However, Campbell's finite-verification argument records a stronger input directly useful here: for every positive real `x<6.8*10^19`, there exists a prime in `(x,x+1724]`. The paper derives this from current maximal-prime-gap record computations. R005 consumes this only as an external published premise.

## 2. Fourth-root core transfer

For a square basin `A=k^2`, `U=k^2+2k`, `F=k`, the fourth-root core is `C4=floor(U^(1/4))=floor(sqrt(k))`.

For `q<=C4`, put `x=A/q`. If a prime r lies in `(x,x+1724]` and `1724<=2k/q`, then `A<q*r<=U`. Also `x>F` for the relevant range, so `r>F`; hence q*r is an exclusive collision forcing q.

Since `q<=C4<=sqrt(k)`, `2k/q>=2sqrt(k)`. Therefore the width condition is guaranteed once `2sqrt(k)>=1724`, i.e.

`k>=862^2=743,044`.

## 3. Upper endpoint

The largest cofactor point occurs at q=2: `x_max=k^2/2`. Campbell's stated finite-gap range applies while `k^2/2<6.8*10^19`.

The exact largest integer satisfying this is

`k=11,661,903,789`.

Thus Campbell's gap input directly forces the entire fourth-root core for

`743,044<=k<=11,661,903,789`.

## 4. Continuous combination

The previous R005 certificate already covers every `2<=k<=894,427,190` by an exact prefix plus the double-checked record-gap table. The ranges overlap substantially.

Therefore, under the stated external computational/published inputs,

`for every 2<=k<=11,661,903,789`,

every square-basin residual composite, if one exists, satisfies

`Omega(n)=3`.

This is currently the strongest continuous p=2 residual-arity range in R005.

## 5. Prior-art boundary

Campbell proves an ambient existence theorem: `exists a in (k^2,(k+1)^2) with Omega(a)<=3` for every k. R005 proves a different structural statement about the unresolved fiber: `a residual -> Omega(a)=3` through the stated finite range.

The two statements must not be merged.

Campbell also explicitly uses maximal prime-gap computations to construct almost primes in square intervals. Therefore R005 must not claim novelty for using finite prime-gap records in square intervals.

The candidate R005 contribution is instead the forced/non-forced observation semantics, residual arity filtration T-A21, the root-core precision hierarchy, the exact three-factor residual shell T-A23, and mapping external gap inputs to mandatory observation depth.

## 6. Consequence

Inside the continuous range, p=2 research is reduced to the three-factor shell, not general factor complexity:

`k^2<abc<(k+1)^2`, `U^(1/4)<a<=U^(1/3)`,

with at least two non-forced candidate witness coordinates.

The next useful work is exact classification of repeated-prime versus squarefree residual closure, not further Omega-level searches inside this range.
