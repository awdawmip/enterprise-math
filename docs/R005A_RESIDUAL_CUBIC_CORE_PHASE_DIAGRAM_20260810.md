# R005-A — Residual Cubic Core and Collapse-Dimension Prime-Gap Phase Diagram

Status: `PROVED R005 STRUCTURE / ASYMPTOTIC COROLLARY FROM PRIOR-ART BHP / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-10`

## 1. The generic danger radius can be compressed again

Let a divisor-witness domain be the integer interval `A<n<=U`, with candidate prime witnesses `q<=F=floor(sqrt(U))`. R005 already established: every residual composite has at least two distinct non-forced candidate prime divisors, and every non-forced candidate q satisfies `q<=sqrt(A)` because otherwise `q^2` is itself an exclusive collision.

These two facts imply a universal third-factor obstruction.

## 2. T-A20 — residual cubic-core theorem

Define

`C(U)=floor(U^(1/3))`.

Assume every candidate prime witness `q<=C(U)` is forced. Then the forced core covers every composite and is the unique least safe witness basis.

Proof: suppose residual n exists. Choose distinct non-forced candidate divisors q1,q2. By the non-forced square bound, `q1*q2<=A`. Since `n>A`, write `n=q1*q2*m` with integer `m>=2`, and choose a prime `s|m`. If `s<=F`, then s is a candidate divisor of residual n and cannot be forced; if `s>F`, then `s>C(U)` automatically because `F>=C(U)`. By hypothesis all candidate primes at most C(U) are forced, so `q1,q2,s>C(U)`. Hence `q1*q2*s>U`, while `n=q1*q2*m>=q1*q2*s`, contradicting `n<=U`.

The cube root is not imported from the p-power basin. It comes from the minimal multiplicative arity of a residual obstruction: two non-forced candidate witnesses plus at least one further prime factor.

## 3. p=3 becomes exact

For the cubic basin `A=k^3`, `U=(k+1)^3-1`, we have `k^3<U<(k+1)^3`, so

`C(U)=k`.

Thus T-A20 specializes exactly to the cubic-core theorem:

`force all candidate primes q<=k -> unique least safe divisor-witness basis`.

## 4. Two different prime-gap exponents

For the p-power basin `A=k^p`, `U=(k+1)^p-1`, the relative width satisfies `(U-A)/A ~ p/k`.

### Least-basis core

The cubic core has scale `q~k^(p/3)`. For the worst core witness, `x=A/q~k^(2p/3)`, and the cofactor interval length is `(U-A)/q ~ x/k`. Since `k~x^(3/(2p))`, the required short-prime scale is

`lambda_least(p)=1-3/(2p)`.

### Full forcing saturation

To force every candidate witness, the worst candidate has scale `q~sqrt(A)~k^(p/2)`. Then `x=A/q~k^(p/2)` and the required cofactor interval scale is

`lambda_full(p)=1-2/p`.

These are different thresholds: existence of a least basis is strictly weaker than full forced saturation.

## 5. BHP phase transition

Baker–Harman–Pintz supply the established exponent `theta=0.525=21/40` for sufficiently large prime gaps / short intervals.

`lambda_least(p)>21/40` iff integer `p>=4`.

`lambda_full(p)>21/40` iff integer `p>=5`.

Therefore, as an asymptotic corollary of established BHP theory:

- for every fixed `p>=4`, sufficiently large p-power basins have a unique least safe divisor-witness basis;
- for every fixed `p>=5`, sufficiently large p-power basins have full forced-core saturation.

No new prime-gap theorem is claimed.

## 6. Collapse-dimension phase diagram

| p | least-basis exponent `1-3/(2p)` | full-forcing exponent `1-2/p` | current structural regime |
|---:|---:|---:|---|
| 2 | 1/4 | 0 | residual-choice counterexamples already observed |
| 3 | 1/2 | 1/3 | least-basis critical square-gap scale; full forcing harder |
| 4 | 5/8 | 1/2 | asymptotic least basis follows BHP; full forcing square-gap critical |
| 5 | 7/10 | 3/5 | BHP suffices even for full forcing |
| 6 | 3/4 | 2/3 | BHP suffices for both |
| p->infinity | ->1 | ->1 | both witness problems become progressively easier relative to basin width |

This gives a sharper meaning to different collapse dimensions: p changes the prime-gap strength required to make the primality observation language minimal.

## 7. Why p=3 is the central transition dimension

p=2 lies below the phase transition and already exhibits explicit residual hypergraphs. p>=4 is asymptotically controlled for least-basis existence by BHP. Therefore p=3 is the only nontrivial integer exponent in the current framework whose least-basis problem sits exactly at the square-root prime-gap scale `lambda_least(3)=1/2`.

For p=4 the same square-gap scale reappears only for the stronger full-saturation question: `lambda_full(4)=1/2`.

## 8. Foundation feedback candidate

`FF-R005A-9 — Residual cubic core and witness-gap phase diagram`

Candidate reusable content:

1. residual support ambiguity requires a universal cube-root forced core;
2. p-power least-basis and full-saturation questions correspond to different short-prime exponents;
3. BHP separates the integer dimensions at p=4 and p=5;
4. p=3 is the least-basis square-gap critical dimension;
5. p=4 is the full-saturation square-gap critical dimension.

Relation: `A2 minimal observation language + A4 support multiplicity + A0 root scale`.

Status: `PROVED R005 STRUCTURE / PRIOR-ART PRIME-GAP INPUT / NOVELTY UNVERIFIED`.

Do not promote before Lean validation and prior-art review.

## 9. Next

- p=3: square-gap / Oppermann-scale forcing of the exact cubic core q<=k;
- p=4: separate the BHP-controlled least basis from Legendre-scale full saturation;
- p=2: classify residual 3-factor hypergraphs rather than expecting a universal least basis;
- formalize T-A20 independently of p, because it is the reusable mother theorem behind the dimension phase diagram.
