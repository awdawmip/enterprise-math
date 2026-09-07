# BRC Quotient/Remainder Jet Tail — Round 13

Status: `PROVED STRIDE-8 QUOTIENT JET / FIFTEEN-DIVISION SEED / DIVISION-FREE LONG TAIL / FINITE PIPELINE BENCHMARK`
Date: `2026-09-07`
Parents: `t0.brc_linear_deep_tail`, `t0.brc_square_gap_cascade`

## 1. Question

Round 11 reduced every certified long-tail multiplier transition to

`d = floor(2*h*J/(4*m+h))`, `h in {1,2}`,

followed by at most two ordinary BRC odd-basin corrections. Round 12 then used
staged square-residue tables to remove almost every second squarehood root test.
The remaining recurrent high-cost operation was the fresh large-integer division
that materializes `d` at every multiplier.

Can its exact quotient and remainder be transported between multiplier states,
without a reciprocal table and without replacing exact arithmetic by a floating
approximation?

Yes. The exact odd-N mod-8 scan decomposes the division sequence into five
stride-8 residue orbits. Three exact samples seed each orbit. Thereafter a
second-difference quotient jet plus its exact division remainder advances the
orbit using at most four additions/subtractions of the new denominator. Thus a
whole unbounded tail needs exactly 15 seed divisions and no later fresh quotient
division.

## 2. BRC carrier and observer audit

The retained source state remains

`m*N = J_m^2 + R_m`, `0 <= R_m <= 2*J_m`.

The new repair state for one fixed residue orbit is

`(q_m, rho_m, v_m, a_m, P_m)`

where

- `q_m` is the exact order-one predictor quotient;
- `rho_m` is its exact Euclidean remainder;
- `v_m` is the first stride-8 difference of `q`;
- `a_m` is the second stride-8 difference;
- `P_m` carries the only otherwise-large quotient-difference/denominator
  product required by the next residual update.

The observer is the exact next BRC root/remainder state and the completion gap
used by the existing square-residue cascade. Future operations require exact
Euclidean normalization, so Boolean support, quotient-only state, a fitted real
trend, or a total-error scalar is not adequate. In particular, dropping
`rho_m` destroys the bounded repair law.

Reuse resolution:

- `t0.brc_linear_deep_tail`: `EXTEND_EXISTING_TOOL`;
- `t0.brc_square_gap_cascade`: `COMPOSE_APPLIED`;
- no current quotient/remainder-jet executable was found in the bounded toolbox
  and source lookup, so the exact missing capability was confirmed as
  cross-multiplier Euclidean quotient transport.

No new top-level BRC family is introduced.

## 3. Five exact stride-8 quotient orbits

The exact odd-N representative multipliers have residues

`{0,1,3,5,7} mod 8`.

Their outgoing sparse steps are fixed by residue:

| source residue | outgoing step `h` |
|---:|---:|
| 0 | 1 |
| 1 | 2 |
| 3 | 2 |
| 5 | 2 |
| 7 | 1 |

For one residue orbit, consecutive source multipliers differ by 8 and the same
`h` is reused. Define

`D_m = 4*m+h`,

`2*h*J_m = q_m*D_m + rho_m`, `0 <= rho_m < D_m`.

The root predictor used by Round 11 is exactly `d=q_m`.

## 4. Smooth backbone and gradually changing error

Define

`F_h(m) = 2*h*sqrt(m*N)/(4*m+h)`.

Writing `sqrt(m*N)=J_m+delta_m`, `0<=delta_m<1`, gives

`x_m = 2*h*J_m/(4*m+h) = F_h(m)-s_m`,

`0 <= s_m < 2*h/(4*m+h)`,

and

`q_m=floor(x_m)`.

For `m>=h`, direct differentiation gives

`F_h''(m)`
`= -sqrt(N) h (h^2+24hm-48m^2)`
`  / (2 m^(3/2)(h+4m)^3) > 0`,

and

`F_h'''(m)`
`= 3 sqrt(N) h (h^3+20h^2m+240hm^2-320m^3)`
`  / (4 m^(5/2)(h+4m)^4) < 0`.

The following simple bounds suffice on this range:

`0 < F_h''(m) < 3h sqrt(N)/(8m^(5/2))`,

`|F_h'''(m)| < 15h sqrt(N)/(16m^(7/2))`.

For stride `H=8`, finite differences admit exact repeated-integral forms. Hence
at the oldest multiplier of an orbit window,

`0 < Delta_8^2 F_h < 24h sqrt(N)/m^(5/2)`,

`|Delta_8^3 F_h| < 480h sqrt(N)/m^(7/2)`.

The existing common linear-tail condition

`4m^5 >= N`

implies `sqrt(N)<=2m^(5/2)`, so

`Delta_8^2 F_h < 48h`,

`|Delta_8^3 F_h| < 960h/m`.

Thus the quotient surface is decreasing and convex to second order, while its
third-difference curvature decays like `1/m` after the Round-11 normalization.

## 5. Exact bounded third-difference theorem

Let `theta_m=x_m-q_m` be the floor phase. Since `0<=theta_m<1`, the positive
and negative coefficient masses of a third finite difference are both 4, so

`-4 < Delta_8^3 theta_m < 4`.

Likewise, because `0<=s_m<h/(2m)`,

`|Delta_8^3 s_m| < 2h/m`.

Therefore, under

`4m^5 >= N` and `m>=962h`,

`|Delta_8^3 x_m|`
`<= |Delta_8^3 F_h| + |Delta_8^3 s_m|`
`< 962h/m <= 1`.

Since

`Delta_8^3 q = Delta_8^3 x - Delta_8^3 theta`

is an integer, it follows that

`-4 <= Delta_8^3 q <= 4`.

This is the exact repair theorem for quadratic quotient extrapolation.

A parallel second-difference estimate gives

`-2 <= Delta_8^2 q <= 98`

for `h<=2` under the same common tail. This keeps all updates involving the
second-difference coordinate as multiplication by a uniformly small integer.

For all five residue classes simultaneously, the worst case is `h=2`. The
uniform guard is therefore

`m>=1924`.

The executable starting threshold is the first representative multiplier at or
above

`max(ceil((N/4)^(1/5)), 1924)`.

## 6. Exact quotient/remainder jet

For three consecutive samples in one residue orbit, define

`v_m = q_m-q_(m-8)`,

`a_m = q_m-2q_(m-8)+q_(m-16)`.

The quadratic extrapolation to the next visit is

`q_hat_(m+8) = q_m+v_m+a_m`
`              = 3q_m-3q_(m-8)+q_(m-16)`.

Let

`epsilon_m=q_(m+8)-q_hat_(m+8)`.

The theorem above gives `epsilon_m in {-4,...,4}`.

To recover the exact Euclidean remainder without recomputing the division, also
retain

`P_m=(v_m+a_m)(D_m+32)`.

At the next same-residue source multiplier `m+8`, the new denominator is
`D'=D_m+32`. Given the already exact root `J'`, form

`S = rho_m + 2h(J'-J_m) - 32q_m - P_m`.

This is exactly

`2hJ' - q_hat D'`.

Normalize it by at most four signed denominator steps:

- while `S<0`, set `q_hat<-q_hat-1`, `S<-S+D'`;
- while `S>=D'`, set `q_hat<-q_hat+1`, `S<-S-D'`.

At exit,

`q_hat=q_(m+8)` and `S=rho_(m+8)`.

No large numerator/denominator division and no generic `q_m*D_m` product is
performed.

The jet then updates exactly by

`v' = v+a+epsilon`,

`a' = a+epsilon`,

`P' = P + (2a'-a)D' + 32(v+2a')`.

Because `a,a'` are uniformly small, the extra products are large-integer times
small-integer operations.

## 7. Fifteen divisions for an unbounded tail

There are five source residue classes. Each needs exactly three exact quotient
samples. The representative stream visits each source class once per block of
8 multipliers. Consequently:

`5 orbits * 3 seed samples = 15 exact divisions`.

After the fifteenth transition all five jets are active. Every later source
state, at any multiplier horizon, uses the bounded recurrence. The division
count is therefore `O(1)` per complete tail rather than `O(M)` in the number of
scanned multipliers.

This is an execution/storage result only. It does not shorten the multiplier
search horizon.

## 8. Composition with exact BRC closure and the square table cascade

For every source transition, the recovered exact quotient `q` is fed unchanged
into the Round-11 root update:

`G = R_m + hN - q(2J_m+q)`.

The candidate root `J_m+q` is then closed by at most two standard BRC odd-width
crossings. The resulting exact completion gap is sent through the existing
BALANCED square-residue cascade

`4032 -> 12155 -> 12673`.

Thus the complete hot path is

`15 seed divisions`
`-> five quotient/remainder jets`
`-> <=4 denominator repairs per orbit visit`
`-> <=2 BRC root repairs per multiplier`
`-> staged square-gap table`
`-> exact gap isqrt only for table survivors`.

The table continues to filter squarehood; the quotient jet removes the upstream
predictor division. Their information roles are distinct and composable.

## 9. Validation

Repository regression covers:

- exact outgoing-step residue pattern;
- the common fifth-root plus `m>=1924` threshold certificate;
- exactly 15 seed divisions followed by recurrence-only execution;
- agreement between the allocation-free hot-path API and the diagnostic step
  record API;
- exhaustive odd `N<500`, 200 transitions per value;
- deterministic random scans from 64 through 8192 bits;
- exact comparison of every transported quotient/remainder against `divmod`;
- exact comparison of every root/remainder against direct `isqrt`;
- root correction count at most 2;
- quotient correction magnitude at most 4;
- retained second difference in `[-2,98]`;
- a fixed finite witness attaining correction `-4`, so the proved interval is
  not silently narrowed to the more common observed range.

A wider local stress harness additionally checked odd `N<5000` and random values
through 16384 bits. No mismatch was observed. This is finite validation, not a
replacement for the proof above.

## 10. Finite full-pipeline benchmark

The committed benchmark uses the same BALANCED square-gap cascade on all paths,
1500 retained transitions per sample, deterministic random odd `N`, and median
of three timed repeats. It compares:

1. direct incremental target plus `isqrt` at every multiplier;
2. Round-11 linear BRC with a fresh quotient division every multiplier;
3. the quotient jet, including its 15 seed divisions.

| N bits | samples | direct / jet | fresh-division linear / jet |
|---:|---:|---:|---:|
| 1024 | 16 | 1.12x | 0.75x |
| 2048 | 12 | 1.60x | 0.95x |
| 4096 | 8 | 2.29x | 1.16x |
| 8192 | 4 | 2.80x | 1.43x |
| 16384 | 2 | 3.35x | 1.58x |

Therefore the quotient jet is not the preferred Python route at small sizes,
but crosses the fresh-division implementation around the 4096-bit range in this
finite environment and widens its advantage as integer size grows. The exact
crossover is runtime-dependent.

The benchmark includes the seed cost. On a much longer tail the fixed 15 seed
divisions are amortized further.

## 11. Negative alternatives retained

- A reciprocal/Newton table for `1/(4m+h)` was already exact but slower than the
  native division in the tested Python runtime.
- Replacing the bounded signed correction loop by another `divmod(S,D')` loses
  the point of the jet and did not improve the finite hot path.
- A quotient-only quadratic fit is invalid: the exact Euclidean remainder is the
  repair coordinate that makes bounded correction possible.
- The quotient jet does not improve the small-integer path enough to justify a
  universal switch. A practical implementation should retain the fresh-division
  path below an empirically selected bit-size threshold.

## 12. Decision and next frontier

Promote as a derived T0_BRC subtool:

`ORDER-1 LINEAR TAIL`
`-> FIVE STRIDE-8 QUOTIENT/REMAINDER JETS`
`-> FIFTEEN SEED DIVISIONS`
`-> DIVISION-FREE UNBOUNDED TAIL`.

The result removes the last recurring division from the current large-integer
linear-tail predictor. It does not change the classical factor-search horizon,
prove an asymptotic factorization speedup, or imply an RSA-practical attack.

After the square-gap cascade and quotient jet, the largest remaining recurrent
operation is the full-width product in

`q(2J+q)`

inside the exact BRC root-gap update. The next local question is whether the
retained Euclidean relation

`2hJ=q(4m+h)+rho`

can be composed with the transported root/remainder state to reduce that product
without reintroducing division, a large side table, or loss of exactness.
