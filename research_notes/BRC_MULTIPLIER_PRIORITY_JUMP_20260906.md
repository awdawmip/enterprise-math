# BRC Multiplier Priority Jump — Round 6

Status: `EXACT MOD4 SKIP + PROVED DIRECT JUMP / STRUCTURAL PRIORITY HEURISTIC / FINITE VALIDATION`
Date: `2026-09-06`
Parent: `t0.brc_multiplier_transition`
Composition: `t0.brc_square_gap_prefilter`

## 1. Goal

After Round 5 reduced a consecutive m=1..100 scan to one initial root plus local BRC transport, the next question was whether useful multipliers can be tested earlier without first materializing all 100 states.

A gap-sorted order was tested first. It greatly improved hit rank, but it required generating all 99 later states before sorting. Once the 504-byte residue filter had already reduced exact gap-root calls to about 1--3 per N, that reordering did not improve wall-clock time in the tested Python implementation. It is therefore **not promoted**.

The successful replacement is an N-independent structural order combined with exact direct jumps from m=1.

## 2. Exact safe skip for odd N

If N is odd and `m == 2 (mod 4)`, then `mN == 2 (mod 4)`.

Squares modulo 4 are 0 or 1, so a difference of two squares is only 0, 1, or 3 modulo 4. Therefore

`m == 2 (mod 4) -> mN is not x^2-b^2`.

Among m=1..100 this safely removes exactly 25 multipliers before any completion-gap test.

This is classical modular arithmetic, not an Enterprise novelty claim.

## 3. Structural priority score

For an odd semiprime N=pq and a successful multiplier split `m=uv`, the two difference-of-squares factors have the same parity.

Hence the number of same-parity unordered multiplier factor pairs is

- `A(m)=factor_pair_count(m)` for odd m;
- `A(m)=0` for `m == 2 mod 4`;
- `A(m)=factor_pair_count(m/4)` for `4 | m`.

Larger A(m) gives more rational balance candidates u/v that may approximate q/p. This motivates the priority order

`m=1 first`, then decreasing `A(m)`, then increasing m.

This is a **heuristic ordering**. No theorem says it is optimal or universally better.

## 4. Exact direct jump from m=1

Retain

`N=J^2+R`, `0<=R<=2J`.

For a target multiplier t<=100 set

`beta=sqrt(t)`, `gamma=beta-1`.

Choose the same dyadic precision B used by Round 5, so `J<2^(B-1)`, and let

`C_t=floor(2^B gamma)`,
`d0=floor(C_t J / 2^B)`.

As before,

`d0 <= gamma J < d0+3/2`.

Writing `sqrt(N)=J+delta`, `0<=delta<1`, gives

`sqrt(tN)=J+gamma J+beta delta`.

Since beta<=10 for t<=100, the exact target root lies fewer than 12 integers above `J+d0`. Therefore at most 11 exact BRC odd-width corrections recover the root.

The provisional remainder is computed without another root:

`G0=R+(t-1)N-d0(2J+d0)`.

Starting at `a=J+d0`, repeatedly apply

`G <- G-(2a+1)`, `a <- a+1`

while `G>=2a+1`. At most 11 iterations occur, and exit gives

`a=floor(sqrt(tN))`, `G=tN-a^2`.

Thus an arbitrary prioritized candidate can be tested directly from the single m=1 BRC state; no intermediate multiplier states are required.

## 5. Finite rank validation

### Population A

The prior exhaustive bounded population:

- 143 primes in [101,997];
- every p<q pair;
- 10,153 semiprimes.

Restricting to the 75 mod-4-feasible multipliers, ordinary increasing-m order had successful-sample mean/median first-hit ranks

`16.91 / 12`.

The structural priority order gave

`8.82 / 5`.

### Population B

Independent validation population:

- primes in [1009,4999];
- 20,000 deterministic sampled p<q pairs;
- seed 20260906.

Increasing feasible-m order gave

`26.36 / 25`.

Structural priority gave

`10.97 / 5`.

The improvement persisted across tested q/p bands. Near-balanced pairs remain protected by fixing m=1 first.

These are finite population diagnostics, not an asymptotic distribution theorem.

## 6. Runtime prototype

A Python prototype composed:

1. one m=1 root;
2. structural priority order;
3. direct 1->m BRC jumps;
4. mod-4032 static square-residue filter;
5. exact gap root and gcd only on survivors.

Against the Round-5 consecutive-transition+residue pipeline on deterministic probable-prime semiprime samples, observed wall-clock ratios were approximately:

- 128 bit: 1.10x faster;
- 256 bit: 1.24x;
- 512 bit: 1.58x;
- 1024 bit: 1.42x;
- 2048 bit: 1.70x.

The exact values are implementation/environment dependent. The point is that unlike gap sorting, the structural order can save actual transported candidates because it does not need all intermediate m states.

## 7. Boundaries

- The mod-4 elimination is exact and classical.
- The direct jump theorem is exact finite integer BRC transport.
- The A(m) ordering is heuristic and N-independent; it is not an optimality theorem.
- Difference-of-squares / multiplier-Fermat / Lehman ideas remain classical prior art.
- No asymptotic factorization speedup is claimed.
- No Foundation promotion is made.

## 8. Next attack

The new bottleneck is no longer repeated root materialization or blind multiplier order. The next useful question is whether the priority score can be upgraded from `A(m)` to a **small finite rational-approximation cover** of plausible q/p ratios while remaining N-independent, or whether a BRC-visible N-dependent signal can safely choose among those covers without first computing every target state.
