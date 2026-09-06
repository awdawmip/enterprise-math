# BRC Fixed Residue-Wheel Complexity Boundary — Round 9

Status: `PROVED NEGATIVE BOUNDARY / EXACT FINITE COUNTS / CLASSICAL NUMBER THEORY / NO FACTORIZATION IMPROVEMENT CLAIM`
Date: `2026-09-06`
Parent: `t0.brc_multiplier_vertical_wheel`

## 1. Question

Can the very strong modular residue wheels from Rounds 6–7 be enlarged until they change the exponent of the vertical search, rather than only its implementation constant?

For every **fixed finite wheel**, no.

## 2. Exact fixed-wheel count

Let one wheel have period `P` and sorted support

`S={r_1,...,r_s} subset {0,...,P-1}`.

For a vertical horizon `0<=t<T`, write `T=qP+a`, `0<=a<P`. The number of retained positions is exactly

`N_S(T)=q*s + #{r in S : r<a}`.

Therefore

`N_S(T)=(s/P)T+O(P)`.

If `s>0`, then

`N_S(T)=Theta(T)`.

So a fixed wheel can change the constant density `s/P`, but not the linear exponent of the t horizon.

## 3. Why the support cannot be empty on an admissible strip

A positive integer C is a difference of two integer squares exactly when `C != 2 mod 4`.

Explicitly:

- if C is odd, `C=((C+1)/2)^2-((C-1)/2)^2`;
- if 4|C, writing C=4q gives `C=(q+1)^2-(q-1)^2` (with the harmless y=0 boundary at C=4).

Let `x0=ceil(sqrt(C))` and let `t=x-x0` for either explicit representation. Then

`(x0+t)^2-C=y^2`.

Modulo every fixed M, this t residue therefore survives the exact quadratic-residue wheel. Hence every classically admissible strip has nonempty support for every fixed QR modulus or finite CRT product.

This rules out a hidden 'perfect modulus' that deletes a whole admissible strip solely by square-residue testing.

## 4. Exact odd-prime local density

For an odd prime p and fixed c, count x mod p for which `x^2-c` is a quadratic residue, zero included.

For `c != 0 mod p`, the classical character sum

`sum_x chi(x^2-c)=-1`

gives:

- if c is a nonzero quadratic residue: `(p+1)/2` allowed x;
- if c is a nonresidue: `(p-1)/2` allowed x.

If `c=0 mod p`, all p values are allowed.

Thus adding an independent large odd prime typically reduces density by only about a factor of two.

The executable reference routine checks this formula against exact enumeration for small odd primes.

## 5. Why one gigantic CRT wheel does not automatically escape

For r pairwise-coprime odd-prime filters, the CRT support density is a product of the local densities, typically on the scale `2^-r` up to small local factors.

To force this density to shrink like a power `T^-alpha`, one needs `r=Omega(log T)` genuinely independent prime conditions.

But a fully materialized CRT wheel then has period

`P=product_{i=1}^r p_i`.

For distinct increasing odd primes this product grows much faster than `2^r`; using the first r odd primes already gives `log P=Theta(r log r)`. With `r=Theta(log T)`, the full period becomes super-polynomial in the simple target density scale.

Therefore 'keep multiplying moduli and store one complete wheel' merely transfers work into wheel period, memory or preprocessing. Segmented/local sieving can avoid materializing P, but then it processes the search interval in another form; no exponent reduction follows from residue filtering alone.

This is a route boundary, not a lower bound against every possible arithmetic algorithm.

## 6. Difference-of-squares semantic completeness

Every exact point hit in the Round-7 lattice satisfies

`D_{m,t}=y^2`

iff

`(x_{m,t}-y)(x_{m,t}+y)=mN`.

So single-point square detection is exactly a divisor-pair search for mN. BRC coordinates make transport and observer-safe rejection cheaper, but do not create hidden factor information at the point level.

That observation explains the route progression:

- root transport removed repeated square roots;
- residue wheels removed most point work;
- 2-adic normalization removed universal duplicate strips;
- after these optimizations, the remaining obstruction is the number of arithmetic relations/points, not their local evaluation cost.

## 7. Required method switch

To go beyond the single-point square wall, a next route must use information shared by **multiple** gaps.

The classical Dixon/continued-fraction/quadratic-sieve idea does exactly this: require several values to be smooth over a factor base, retain their exponent-parity vectors and provenance, then find a GF(2) dependency whose product is a square modulo N.

This is classical factoring mathematics, not a BRC novelty. But it is structurally relevant to current BRC discipline because Boolean support alone is insufficient: the relation layer must retain exponent parity and labeled provenance until the dependency is assembled.

Round 10 therefore tests a prior-art-safe smooth-relation facade over the BRC `(m,t)` lattice. Any value found there must be judged against classical Dixon/QS/MPQS, not against the now-closed fixed-wheel point route.

## 8. Tool

`src/enterprise_math/brc_residue_wheel_complexity.py` provides exact diagnostic interfaces:

- `periodic_support_count`;
- `canonical_difference_square_pair`;
- `fixed_squarehood_wheel_must_be_nonempty`;
- `prime_shift_square_support_count`;
- `fixed_wheel_boundary`.

These freeze the no-go boundary so later research does not rediscover a larger static table as an exponent-changing mechanism.
