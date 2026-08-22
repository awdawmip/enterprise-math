# Prime-BRC divisor-antichain switching weight

Status: `L3 OWNER-LOCAL RESEARCH CHECKPOINT / NOT CANONICAL`
Date: `2026-08-22`
Researcher-ID: `EM-PRIMEBRC-7F3A21`

## 1. Square-root frontier branch poset

Let `n` lie strictly between consecutive squares `k^2<n<(k+1)^2`. Since there is no square in the open basin, `sqrt(n)` lies strictly between `k` and `k+1`.

Define the proper large-divisor poset

`P_>(n)={d:d|n, k<d<n}`

ordered by divisibility, and let

`width_>(n)`

be its maximum antichain size.

This is a branch-concurrency observable: it records how many large divisor branches can remain mutually incomparable at the square-root frontier. It is not the same as total factor count.

## 2. Exact squarefree P1/P2/P3 classification

For squarefree factorization with ordered primes:

### Prime `n=p`

`P_>(n)=empty`, so `width_>=0`.

### Semiprime `n=pq`, `p<q`

Because `p<sqrt(n)<q`, the only proper large divisor is `q`, hence

`width_>=1`.

### Triprime `n=pqr`, `p<=q<=r`

There are two canonical frontier types.

A-type: `pq<r`. The proper large divisors are

`{r,pr,qr}`.

Here `r|pr` and `r|qr`, while `pr` and `qr` are incomparable. Hence

`width_>=2` exactly.

B-type: `r<pq`. The proper large divisors are

`{pq,pr,qr}`.

These three pair products are pairwise incomparable, so

`width_>=3` exactly.

Freeze squarefree classification:

`P1 -> 0`, `P2 -> 1`, `P3_A -> 2`, `P3_B -> 3`.

## 3. Richert-weight match

In the Campbell square-interval Richert parameterization used in the external P3 argument, let `lambda=0.83` and `k2=3.17`. The earlier Prime-BRC audit establishes the structural squarefree triprime bounds:

- A-type triprime: `w_Richert <= lambda/2`;
- B-type triprime: `w_Richert <= lambda`.

Therefore define the owner-local branch-width penalized weight

`w_PBRC(n)=w_Richert(n) - (lambda/2)*max(width_>(n)-1,0)`.

Then:

- semiprime: no penalty;
- A-type squarefree triprime: subtract exactly `lambda/2`, hence contribution is nonpositive;
- B-type squarefree triprime: subtract exactly `lambda`, hence contribution is nonpositive;
- states already nonpositive under the original Richert high-factor gate remain nonpositive after a nonnegative penalty.

This is strictly cheaper than a uniform `lambda` penalty on every triprime because it pays only half on the A branch.

## 4. Repeated-prime triprime exception

A triprime such as `a*b^2` can have frontier width `2` while its Richert weight exceeds `lambda/2` when the repeated prime lies above the square-exclusion range. This is a real boundary; do not silently classify all multiplicity-three states by the squarefree table.

However, after Campbell's existing exclusion of square factors with `z<=b<y`, any surviving repeated prime satisfies

`b>=y=X^(1/3.17)>X^(1/4)`.

For `n=a*b^2~X` with the rough lower bound `a>=X^(1/8)`, one has

`b<=X^(7/16)`.

Also `b^2>X^(1/2)`, so across a square interval of length `~2X^(1/2)` each fixed `b` yields only O(1) possible multipliers `a`; using only a crude count of possible b values gives

`REPEATED_TRIPRIME_EXCEPTION = O(X^(7/16)) = o(X^(1/2)/log X)`.

Prime cubes are thinner still: consecutive cubes near X have spacing of order `X^(2/3)`, larger than the square-interval length, so at most O(1) lie in one basin.

The exact constants/error bookkeeping needed for an explicit theorem are not claimed here; the exponent separation is the frozen asymptotic point.

## 5. Empirical pressure test

Exact bounded factor scans (discovery evidence only) at k=5,000, 10,000 and 20,000 found that the branch-width penalized total Richert weight remained roughly `2.7--3.0 * k/log X`, while squarefree A/B triprime net contribution became nonpositive. A repeated-prime witness occurs, e.g. `109*479^2`, exactly in the declared exception class.

These scans are not proof of global positivity.

## 6. Research meaning

The branch-width observable is a genuine BRC-style refinement:

- it does not store an unbounded factor counter;
- it records concurrency of future large-divisor branches at the square-root frontier;
- it distinguishes the cheap A switching branch from the expensive B branch;
- it leaves P2 states untouched.

The remaining theorem target is analytic:

`PROVE_POSITIVE_TOTAL_PBRC_WEIGHT_AFTER_SWITCHED_UPPER_BOUNDS`.

Success would yield a P2 statement in the same general P3-weighted framework. It would **not** by itself solve P2->P1 / Legendre; the semiprime hard core remains the parity boundary.
