# BRC Multiplier × Vertical Residue Wheel — Round 7

Status: `PROVED EXACT 2D STATE LAW / SAFE PERIODIC RESIDUE WHEEL / LAZY EXACT MATERIALIZATION / FINITE PERFORMANCE BENCHMARK / NO FACTORIZATION-COMPLEXITY CLAIM`
Date: `2026-09-06`
Parents: `t0.brc_multiplier_transition`, `t0.brc_admissible_multiplier_scan`, `t0.brc_square_gap_prefilter`

## 1. Why open a second coordinate

Round 6 showed that the immediate ceiling-square surface `t=0` becomes sparse as factor scale grows. A meaningful continuation must therefore allow

`x_t = ceil(sqrt(mN)) + t`, `t>=0`.

This is the classical vertical Fermat/Lehman direction. The question here is not whether that direction is new; it is whether the already-retained BRC multiplier state can make the two-dimensional `(m,t)` search substantially cheaper without losing candidates.

## 2. Exact vertical state law

From one horizontally transported multiplier state

`mN = J_m^2 + R_m`, `0<=R_m<=2J_m`,

set

- `x_0=J_m` and `D_0=0` if `R_m=0`;
- otherwise `x_0=J_m+1` and `D_0=2J_m+1-R_m`.

Then

`D_0=x_0^2-mN` and for every `t>=0`,

`x_t=x_0+t`,
`D_t=x_t^2-mN=D_0+t(2x_0+t)`.

The one-step update is

`D_(t+1)=D_t+2x_t+1`, `x_(t+1)=x_t+1`.

So the 2D state is exactly carried by the horizontal BRC root/remainder plus one vertical integer offset.

The vertical recurrence itself is classical Fermat arithmetic. Lehman's original inner loop already exploited additive updates and congruence strides rather than recomputing squares from scratch. No novelty claim is made for that recurrence.

## 3. Periodic residue wheel theorem

Fix a modulus `M` and let `Q_M` be its exact quadratic-residue set. A necessary condition for a true square hit is

`D_t mod M in Q_M`.

Because

`D_t = (x_0+t)^2-mN`,

we have

`D_(t+M) == D_t (mod M)`.

Therefore the safe first-stage support is the finite periodic wheel

`W_M(m,N,x_0)={r in 0..M-1 : (x_0+r)^2-mN in Q_M mod M}`.

Every true square hit satisfies

`t mod M in W_M`.

Hence one may build `W_M` once and enumerate only its translated copies. This is a zero-false-negative quotient for the declared squarehood observer.

## 4. Lazy exactness

The key implementation gain is to avoid carrying the large integer `D_t` through rejected vertical states.

Algorithm:

1. Build the first-modulus wheel using only small residues.
2. Enumerate `t=period*M+r` only for `r in W_M`.
3. Test the second modulus `46189` using only `(x_0+t) mod 46189` and `mN mod 46189`.
4. **Only if both residue stages pass**, materialize
   `D_t=D_0+t(2x_0+t)` as a large integer.
5. Only then run exact `isqrt(D_t)`.

Thus a rejected `t` performs no large-integer gap update and no exact gap square root.

This is the BRC-relevant observer discipline: coarse modular observers are used only as one-way safe rejection quotients; exact `(m,t,D_t)` state is reconstructed only on surviving fibers.

## 5. Adaptive first wheel

Finite timing showed a build-cost/density crossover. The reference implementation uses:

- `M=1008` for `t_limit < 150000`;
- `M=20160` for longer windows;
- second stage always `M=46189`.

The threshold is an implementation policy from this benchmark, **not** a theorem and not a universal hardware-independent optimum. The exact wheel API accepts any positive first modulus.

## 6. Validation

The regression surface checks:

- the closed form `D_t=D_0+t(2x_0+t)` against repeated vertical updates;
- exact first-wheel periodicity;
- candidate-set equality with direct two-table filtering on bounded domains;
- inclusion of every actual square gap (zero false negatives);
- the known vertical Fermat witness `5959=59*101`, whose `m=1` hit occurs at `t=2`;
- the adaptive policy boundary.

Independent local derivation checks additionally compared the wheel support with direct residue evaluation across many small odd `N`, admissible multipliers and vertical positions.

## 7. Finite performance

For each row, 15 `(N,m)` samples were used: three random odd N values and `m in {1,5,15,45,96}`. Compared:

1. `exact cascade`: maintain the full large integer gap at every t, then apply both residue tests;
2. `lazy step`: update only small modular gap states each t and materialize exact D only on survivors;
3. `wheel`: enumerate only first-stage periodic support, apply second-stage residue test, then materialize exact D.

Median ratios:

| N bits | t window | exact-cascade / wheel | lazy-step / wheel |
|---:|---:|---:|---:|
| 512 | 10,000 | 4.59x | 4.46x |
| 512 | 100,000 | 9.41x | 8.75x |
| 512 | 1,000,000 | 10.93x | 10.19x |
| 1024 | 10,000 | 7.63x | 5.40x |
| 1024 | 100,000 | 11.30x | 8.15x |
| 1024 | 1,000,000 | 12.11x | 8.53x |
| 2048 | 10,000 | 8.24x | 4.29x |
| 2048 | 100,000 | 20.09x | 9.89x |
| 2048 | 1,000,000 | 24.84x | 12.10x |

These are Python implementation timings, not asymptotic factoring claims. The strongest observed gains arise because the wheel skips most Python loop iterations and most large-integer work, not because it changes the classical search rectangle size.

## 8. Prior-art and complexity boundary

Lehman's 1974 method already searches a bounded vertical interval above `sqrt(4kN)`, uses additive gap updates, and applies congruence restrictions. Its classical bound is `O(N^(1/3))` arithmetic operations after the associated small-factor stage. Modern descriptions give the inner width on the order of `N^(1/6)/sqrt(k)`.

Therefore this round does **not** claim a new asymptotic factoring algorithm. A residue wheel is a modular sieve; the vertical Fermat coordinate is classical.

The project-specific result is the exact composition:

`horizontal BRC (J,R) transport`
`-> vertical base (x_0,D_0)`
`-> periodic safe residue quotient`
`-> lazy exact fiber reconstruction`.

Any future complexity claim must compare the total number of `(m,t)` fibers and preprocessing cost against the Lawrence/Lehman/Hart search, not just compare implementation timings inside a fixed rectangle.

## 9. Next attack

The remaining expensive object is now **rectangle size**, not square testing or repeated roots.

The next useful question is whether the `(m,t)` lattice admits a BRC-safe cross-multiplier quotient or transport in t that skips entire rectangles/strips, rather than merely sieving points inside the classical rectangle.

A candidate direction is to compare neighboring multipliers' vertical gap parabolas

`D_{m,t}=(x_{m,0}+t)^2-mN`

under the already-proved horizontal `(J,R)` transport and search for an exact relation between their residue-wheel supports. If no stronger shared quotient exists, the route should be classified as a constant-factor implementation of classical Lehman/Fermat rather than a new factorization method.
