# BRC Multi-Strip Smooth Relation Lattice

Status: `PROVED CROSS-STRIP CARRIER / CLASSICAL DIXON-QS-MPQS COMPOSITION / FINITE RELATION-YIELD BENCHMARK / NO NOVEL FACTORIZATION CLAIM`
Date: `2026-09-06`
Parents: `t0.brc_admissible_multiplier_scan`, `t0.brc_multiplier_vertical_wheel`, `t0.brc_fixed_wheel_complexity_boundary`

## 1. Route switch

The fixed-wheel boundary proves that any fixed nonempty quadratic-residue wheel keeps `Theta(T)` vertical positions.  Therefore further enlargement of a fixed squarehood wheel cannot by itself change the exponent of the single-point vertical search.

The next layer must combine information across several gaps rather than require one gap to be an integer square.

This is classical factor-base mathematics: Dixon and the quadratic-sieve family collect B-smooth values, retain exponent-parity vectors and use linear algebra over GF(2) to create a congruence of squares.  MPQS/SIQS use many short polynomial intervals specifically to keep relation values smaller.  The present result does not claim novelty for any of those mechanisms.

The BRC question is narrower: can gaps produced on distinct multiplier strips share one exact typed relation carrier, and what information may be quotient-compressed without breaking later dependency reconstruction?

## 2. Cross-multiplier gluing law

For every retained BRC multiplier/vertical point,

`x_i^2 - D_i = m_i N`.

Therefore

`x_i^2 == D_i (mod N)`

independently of the multiplier label `m_i`.

If the positive gap is B-smooth over one shared factor base

`P=(p_1,...,p_r)`,

write

`D_i = product_j p_j^(e_ij)`.

The exact relation carrier used here is

`(x_i, m_i, t_i, D_i, P, e_i)`.

Its dependency observer is only

`v_i = e_i mod 2 in GF(2)^r`.

If a finite subset S satisfies

`xor_{i in S} v_i = 0`,

then every total exponent

`E_j=sum_{i in S} e_ij`

is even.  Set

`X=product_{i in S} x_i (mod N)`,
`Y=product_j p_j^(E_j/2) (mod N)`.

Then

`X^2 == Y^2 (mod N)`.

Thus `gcd(X-Y,N)` or `gcd(X+Y,N)` may reveal a nontrivial factor.

No condition on the product of the multiplier labels is required.  The `m_i N` terms vanish individually modulo N before relation multiplication.

## 3. Observer-safe compression result

This relation layer gives a concrete BRC observer lattice.

### Safe for dependency detection

The full exponent vector may be projected to parity:

`e_i -> e_i mod 2`.

GF(2) dependency detection factors through this projection exactly.

### Not safe for square reconstruction

Parity alone does not determine

`E_j/2`.

Two relations can have the same parity vector and different exact exponents.  The regression example `N=14111=103*137` has

- `m=1,t=0`: `x=119`, `D=50=2*5^2`;
- `m=8,t=0`: `x=336`, `D=8=2^3`.

Their parity vectors agree, but their full exponent vectors do not.  Combining them gives

`D_1 D_2 = 400 = 20^2`.

The full exponents reconstruct `Y=20`; parity alone cannot.

Likewise `x_i` provenance must survive until `X` is assembled.

Hence

`PARITY_VECTOR = DEPENDENCY_SUFFICIENT`,

but

`PARITY_VECTOR != CONGRUENCE_RECONSTRUCTION_COMPLETE`.

The multiplier label itself may be forgotten after exact relation extraction if future operations are restricted to dependency/congruence construction, although the implementation keeps it as labeled provenance for diagnostics and scheduling.

## 4. Why shallow multi-strip sampling can help

For one multiplier strip let

`x_0=ceil(sqrt(mN))`,
`D_t=D_0+t(2x_0+t)`.

For positive nonzero `D_0`,

`D_0 <= 2x_0-1`,

so

`D_t <= 2(t+1)x_0+t^2-1`.

A single `m=1` strip driven to E points reaches `t=E-1`.

With M retained multiplier strips sampled round-robin, after E total points every strip has depth at most

`ceil(E/M)-1`.

For the current odd-N admissible family `M=75` and `m<=100`,

`x_0 <= ceil(10 sqrt(N))`.

Thus the multi-strip schedule deterministically keeps every individual vertical depth much shallower.  Smaller auxiliary values are heuristically more likely to be B-smooth, which explains the direction of the finite experiment, but **this size bound is not a smoothness-probability theorem**.

The mechanism is directly analogous in spirit to classical MPQS/SIQS use of many short polynomial intervals instead of extending one polynomial indefinitely.

## 5. Finite smooth-relation yield

Reference sample:

- 20 semiprimes with both primes in `[100000,1000000)`;
- deterministic seed `610`;
- factor base all primes `<=200` (46 primes);
- 3000 raw points per semiprime.

Observed full-budget B-smooth relations:

- single `m=1` strip: mean `22.85`, median `18.0`;
- 75-strip shallow round-robin: mean `61.30`, median `58.5`.

Mean relation-yield ratio:

`61.30 / 22.85 = 2.6827...`.

This is finite evidence only.

## 6. Finite dependency-to-factor benchmark

The reference collector uses exact trial division over the declared factor base, incremental GF(2) row elimination and tests each new dependency basis vector for a nontrivial gcd.  It is intentionally a correctness reference, not a production sieve or block linear-algebra engine.

Misses are charged the full point budget.

| prime range | factor base | point budget | single success | 75-strip success | single mean points | 75-strip mean points | ratio |
|---|---:|---:|---:|---:|---:|---:|---:|
| 100k..1m | <=200 | 10,000 | 37/50 | 50/50 | 4653.34 | 2334.44 | 1.993x |
| 1m..10m | <=300 | 20,000 | 24/50 | 49/50 | 14354.74 | 9010.20 | 1.593x |
| 10m..100m | <=500 | 50,000 | 20/30 | 29/30 | 29947.57 | 23705.33 | 1.263x |

The finite advantage persists across these ranges but decreases with scale under the hand-chosen factor-base/budget parameters.  This is not an asymptotic claim.

Conditional medians among only the successful single-strip cases can look better because that conditioning selects the easiest instances.  The miss-charged mean and success count are the fair quantities for the fixed-budget comparison used here.

## 7. Minimum-gap 75-way scheduler

Each vertical gap sequence is strictly increasing in t.  Therefore a heap containing one live head from every strip gives the exact k-way merge of all strip points in nondecreasing `D`.

This scheduler is pointwise optimal only for the declared observer `next smallest gap`; it does not prove optimal smoothness probability or factoring time.

Finite comparison against simple round-robin:

| prime range | bound/budget | round-robin success | min-gap success | round-robin mean points | min-gap mean points | extra ratio |
|---|---|---:|---:|---:|---:|---:|
| 100k..1m | 200 / 10k | 30/30 | 30/30 | 2113.8 | 1668.1 | 1.267x |
| 1m..10m | 300 / 20k | 29/30 | 29/30 | 8292.73 | 7800.43 | 1.063x |
| 10m..100m | 500 / 50k | 20/20 | 20/20 | 20096.5 | 18959.45 | 1.060x |

The heap is retained as a cheap optional scheduler, but the extra benefit beyond multi-strip sampling is modest at the larger tested scales.

## 8. Prior-art boundary

Nothing in this round promotes a new factorization algorithm.

Classical components include:

- B-smooth relation collection;
- factor bases;
- exponent parity vectors;
- Gaussian elimination / nullspaces over GF(2);
- congruences of squares;
- Dixon/QS/MPQS/SIQS multi-polynomial smoothness strategy.

The BRC-specific reusable payload is the typed bridge from the already-established `(m,t)` lattice into that relation algebra, together with explicit information-loss boundaries and exact cross-strip provenance.

## 9. Implementation boundary

`src/enterprise_math/brc_smooth_relations.py` is a reference correctness facade.  It uses trial division and an incremental integer-bitset GF(2) eliminator.  It is not a production quadratic sieve.

`src/enterprise_math/brc_smooth_relation_scheduler.py` implements the exact 75-way minimum-gap merge.

A production continuation should not optimize trial division.  It should reuse classical sieving and investigate whether the existing BRC horizontal transport lets sieve-root initialization be shared cheaply across multiplier strips.  That is the next discriminating unit against MPQS/SIQS prior art.
