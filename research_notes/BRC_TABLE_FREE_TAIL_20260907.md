# BRC table-free certified tail predictor — Round 9

Status: `PROVED TABLE-FREE CERTIFIED TAIL / STORAGE FRONTIER IMPROVEMENT / PYTHON CPU NEGATIVE / NO FACTORIZATION COMPLEXITY CLAIM`
Date: `2026-09-07`
Parents: `t0.brc_multiplier_transition`, `t0.brc_mod8_sparse_transition`, `t0.brc_pairwise_multiplier_transport`

## 1. Question

The current exact BRC multiplier transport uses dyadic approximants to square-root
scale factors.  For a long increasing multiplier horizon this creates an O(M)
predictor-generation/storage dependency even though the per-N root/remainder
transport itself is exact.

Can the large-m tail be transported with **no per-m square-root predictor table**?

Yes, in a certified short-step tail.  The price is a time/storage tradeoff: the
exact high-order rational polynomial is not faster than Python's optimized
`isqrt` in the present implementation.

## 2. Exact alternating lower predictor

Assume

`m*N = J^2 + R`, `0<=R<=2J`,

and take a forward representative step `h in {1,2}` with `m>=h`.  Put

`x=h/m`, so `0<x<=1`.

The binomial series is

`sqrt(1+x)-1 = sum_{k>=1} binom(1/2,k) x^k`.

For `0<=x<=1`, the terms alternate and decrease in magnitude because

`|term_(k+1)/term_k| = ((k-1/2)/(k+1))*x < 1`.

Hence for every even degree `K=2r`,

`L_K(x)=sum_{k=1}^K binom(1/2,k)x^k`

is a rigorous lower bound and the next positive coefficient

`c_(K+1)=binom(1/2,K+1)>0`

bounds the remainder:

`0 <= (sqrt(1+x)-1)-L_K(x) <= c_(K+1)x^(K+1)`.

Define

`d=floor(J*L_K(h/m))`,
`A=J+d`.

Then `A` is a lower target-root candidate.  No irrational or floating state is
used; the executable implementation evaluates `L_K(h/m)` as one exact
homogeneous integer rational polynomial.

## 3. Root-free remainder update

For target multiplier `m+h`,

`G=(m+h)N-A^2`
` = R+hN-d(2J+d)`.

Thus the standard BRC odd-width correction

`G <- G-(2A+1)`, `A <- A+1`

recovers the exact target state without materializing `sqrt((m+h)N)`.

## 4. Exact two-correction certificate

Write

`sqrt(mN)=J+delta`, `0<=delta<1`,

and `beta=sqrt(1+h/m)`.  Since

`beta < 1+h/(2m)`,

the real target root lies less than

`J+d + c_(K+1) J (h/m)^(K+1) + 2 + h/(2m)`.

Therefore the exact condition

`c_(K+1) J (h/m)^(K+1) + h/(2m) <= 1`

certifies that at most two integer BRC basin crossings are required.

The implementation checks this by integer cross multiplication.  An
uncertified state is rejected rather than silently extrapolated.

## 5. Tail-size theorem

Using `J<sqrt(mN)`, for fixed even K and h<=2 a sufficient large-m condition has
scale

`m = O(N^(1/(2K+1)))`.

Since `K=2r`, this is

`m = O(N^(1/(4r+1)))`.

So a long multiplier scan whose natural horizon is much larger than this can,
in principle, use precise/dyadic predictors only on a prefix and switch to an
exact table-free BRC tail afterwards.

This does **not** reduce the number of tested multipliers and therefore does not
change a Hart/Lehman-style factorization exponent.  It reduces predictor-table
or predictor-generation dependence.

## 6. Finite threshold evidence

For one deterministic odd N at each size and worst short step h=2, the first
certified m was:

| N bits | K=4 | K=16 | K=64 | K=128 | K=256 |
|---:|---:|---:|---:|---:|---:|
| 512 | ~1.20e17 | 67,171 | 28 | 8 | 4 |
| 1024 | ~1.71e34 | ~3.20e9 | 439 | 30 | 8 |
| 2048 | ~2.92e68 | ~6.94e18 | 107,213 | 470 | 31 |
| 4096 | ~9.40e136 | ~3.35e37 | ~6.45e9 | 117,617 | 489 |

These values illustrate the time/storage tradeoff: increasing K sharply moves
the table-free frontier left.

In particular, on the 2048-bit probe:

- K=64: certified after about 1.07e5;
- K=128: after about 470;
- K=256: after about 31.

Thus the O(M) predictor-table dependence is not mathematically necessary in the
long tail.

## 7. CPU result: do not promote as the fast Python path

The exact homogeneous polynomial has nontrivial big-integer cost.  At the
certified threshold, current-environment Python timing found direct `isqrt`
faster in every tested case.

Selected `direct_time / table_free_time` ratios were roughly:

| N bits | K | median certified m | direct / table-free |
|---:|---:|---:|---:|
| 512 | 64 | 28 | 0.052x |
| 1024 | 128 | 30 | 0.050x |
| 2048 | 64 | ~107k | 0.169x |
| 2048 | 256 | 31 | 0.041x |
| 4096 | 128 | ~118k | 0.160x |
| 4096 | 256 | 489 | 0.090x |

So the high-order table-free transport is currently about 6x--24x slower than
optimized Python `isqrt` on these single-step probes.

**Decision:** retain it as an exact storage/predictor-dependence frontier and a
future compiled-arithmetic target; do not route the current Python production
factor scan through it for speed.

## 8. Other table-free attempts killed in this round

Two other exact approaches were tested:

1. Increment Newton on the exact quadratic increment
   `d(2J+d)=R+hN`: exact and table-free, but multiple large integer divisions
   made it substantially slower than `isqrt`.
2. Continued-fraction/fixed-point brackets from
   `d=(R+hN)/(2J+d)`: self-certifying but required too many big divisions,
   especially at small m.

They are not promoted as production tools.

## 9. Tool status

`src/enterprise_math/brc_table_free_tail.py` is a strict T0_BRC research
subtool.  It provides:

- exact half-binomial coefficients;
- exact even lower truncations;
- exact two-correction certificate;
- certified h=1,2 table-free root/remainder transport.

It does not modify Foundation state and does not claim a new factoring
principle.

## 10. Next attack

The remaining interesting route is to keep the exact certificate but lower the
CPU cost of evaluating the high-order bound.  Candidates include:

1. a compiled fixed-point/Horner implementation outside Python big-int object
   overhead;
2. a low-degree rational/Pade lower-upper pair with much higher approximation
   order per multiplication;
3. a theorem that composes existing one/two-step BRC predictors over blocks
   without storing one constant per multiplier.

Until one of those wins a wall-clock benchmark, current production should keep
the existing pairwise/mod-8 transport for m<=100 and use this result only as the
proof that an O(M) predictor table is not structurally unavoidable in the tail.
