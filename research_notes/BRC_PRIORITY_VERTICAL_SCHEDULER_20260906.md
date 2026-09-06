# BRC Priority Vertical Scheduler — Round 8

Status: `PROVED ARBITRARY-JUMP CERTIFICATE / PRIORITY VERTICAL COMPOSITION / FINITE CROSS-SCALE BENCHMARK / DYNAMIC-GAP HEURISTIC NEGATIVE / NO ASYMPTOTIC FACTORIZATION CLAIM`
Date: `2026-09-06`
Parents: `t0.brc_multiplier_transition`, `t0.brc_admissible_multiplier_scan`, `t0.brc_multiplier_vertical_wheel`

## 1. Question

Round 6 found an experimental static multiplier order based on `nu(m)^4/m` that substantially improved first-hit rank, but did not make that order the default execution path because the exact BRC multiplier transport was monotone in `m`.

Round 7 made the expensive part of a realistic search the vertical `(m,t)` residue wheel rather than repeated horizontal square roots.

The present question is therefore:

1. can retained BRC remainder data support an exact arbitrary multiplier jump if a non-monotone path is ever needed?
2. more importantly for the current Python implementation, can one compute the 75 admissible horizontal states once in the fast monotone BRC order and then reorder only the expensive vertical work without changing the searched rectangle?

Both answers are yes.  The second route is the default performance recommendation.

## 2. Remainder-aware arbitrary multiplier jump theorem

Let `1<=a,b<=100` and retain an exact BRC state

`aN = J^2 + R`, `0<=R<=2J`.

Write

`sqrt(aN)=J+delta`, `0<=delta<1`.

Since

`R=delta(2J+delta)`, define the rational lower coordinate

`L = J + R/(2J+1)`.

Then there is an exact identity

`sqrt(aN)-L = delta(1-delta)/(2J+1)`.

Therefore

`0 <= sqrt(aN)-L <= 1/[4(2J+1)]`.

Now put

`beta=sqrt(b/a)`.

For `a,b<=100`, `beta<=10`.  Let `B0` be the existing Enterprise multiplier-transition precision, so every relevant root satisfies

`J < 2^(B0-1)`.

Use two more bits,

`B=B0+2`,

and the exact lower dyadic coefficient

`C=floor(2^B beta)`.

Set

`q0=floor((C/2^B) L)`.

The runtime evaluates this floor using integer numerators and denominators only; no floating state is introduced.

Because `L<J+1<=2^(B0-1)`,

`(beta-C/2^B)L < 1/8`.

Also

`beta(sqrt(aN)-L) <= 10/[4(2J+1)] <= 5/6`.

Hence

`sqrt(bN) - (C/2^B)L < 23/24 < 1`.

Since `q0` is the floor of the lower dyadic quantity,

`0 <= floor(sqrt(bN))-q0 <= 1`.

Thus an arbitrary jump between any two multipliers in `1..100` needs at most **one** exact BRC odd-width correction.

The provisional remainder can be updated without a new root:

`G0 = R + (b-a)N - d(2J+d)`,

where `d=q0-J`.

If `G0>=2q0+1`, subtract that one basin width and increment the root once.  No second correction is possible by the theorem.

### Observer consequence

This proof uses `R` essentially.  The stronger predictor is unavailable from `J` alone.  Therefore the constructive observer statement strengthens to:

`ROOT_ONLY != ARBITRARY_MULTIPLIER_JUMP_COMPLETE`,

while

`(ROOT, REMAINDER, SOURCE_MULTIPLIER) -> EXACT TARGET STATE`.

## 3. Performance kill: do not use the arbitrary jump as the default CPython priority path

The theorem is mathematically clean, but the exact rational lower predictor requires a large-integer division by a quantity involving `2J+1`.

With the dyadic beta constants warmed/cached, a 10-multiplier priority prefix was benchmarked against simply calling optimized CPython `math.isqrt(mN)` for those same ten multipliers.

Observed `jump_time / direct_priority_isqrt_time`:

| N bits | ratio |
|---:|---:|
| 128 | 2.96x |
| 256 | 2.48x |
| 512 | 2.20x |
| 1024 | 2.42x |
| 2048 | 2.59x |
| 4096 | 2.68x |

So the one-correction theorem is retained as an exact diagnostic/structural interface, **not** as the default Python fast path.

This is an implementation result, not a mathematical lower bound on other languages or arithmetic kernels.

## 4. Production composition: monotone horizontal BRC, priority vertical work

The current fast composition is simpler:

1. compute the complete admissible horizontal state family once with `admissible_root_state_sequence(N)`;
2. index those exact states by multiplier;
3. consume the already-computed states in `heuristic_priority_multipliers()` order;
4. run the expensive Round-7 vertical residue wheel only in that order;
5. stop on the first factor witness.

The horizontal support is unchanged.  The vertical interval for every multiplier is unchanged.  Only evaluation order changes.

Therefore, relative to the same declared rectangle

`m in admissible multipliers <=100`, `0<=t<t_limit`,

priority scheduling has **zero mathematical false negatives**: it is a permutation of the same finite search family.

The heuristic priority remains experimental.  Completeness comes from the preserved rectangle, not from the score.

## 5. Cross-scale exact rank benchmark

For odd semiprimes `N=pq`, the least vertical offset for a fixed multiplier can be computed exactly from same-parity divisor splits `uv=m`:

`x=(up+vq)/2`,

`t=x-ceil(sqrt(mN))`,

including the symmetric assignment.  This provides a cheap exact rank benchmark without simulating every vertical offset.

Three independent 20,000-semiprime samples were used.  The vertical budget was scaled by one decimal order with the prime scale: `10`, `100`, `1000`.

| prime range | t limit | hittable | ascending mean rank | priority mean rank | priority median | priority top-10 | hit-rank improvement |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1009..9999 | 10 | 95.65% | 16.176 | 6.929 | 4 | 74.26% | 2.334x |
| 10007..99999 | 100 | 95.19% | 17.183 | 7.306 | 5 | 72.55% | 2.352x |
| 100003..999999 | 1000 | 95.38% | 17.263 | 7.269 | 5 | 73.18% | 2.375x |

If misses are charged the full 75-multiplier rectangle, the corresponding all-population mean multipliers fall from approximately

`18.7..20.0`

to

`9.9..10.6`.

This finite stability is encouraging, but no distributional or asymptotic theorem is claimed.

## 6. Actual vertical-wheel timing

A separate 300-semiprime sample with primes in `10007..99999` used already-materialized horizontal states and the actual two-stage vertical wheel logic.

| t limit | hittable / 300 | ascending mean rank | priority mean rank | measured speedup |
|---:|---:|---:|---:|---:|
| 30 | 232 | 26.96 | 11.63 | 1.49x |
| 100 | 285 | 16.48 | 7.52 | 1.71x |
| 300 | 300 | 8.04 | 4.31 | 1.78x |

The runtime gain is smaller than the rank gain because wheel construction and fixed overhead are not perfectly proportional to rank, but the priority scheduler remains materially faster in the tested region.

## 7. N-dependent base-gap ordering was tested and rejected

Once all horizontal BRC states are available it is tempting to sort multipliers by quantities such as:

- immediate ceiling gap `D_0`;
- normalized phase `D_0/(2J+1)`;
- `D_0` combined with the static multiplier score.

On 3,000-semiprime subsets of the same three scale regimes, with the corresponding `t_limit=10,100,1000`, the current static priority mean ranks were approximately

`6.84, 7.43, 7.19`.

Pure gap ordering gave

`15.43, 18.30, 20.34`,

normalized phase gave

`18.19, 20.69, 22.93`,

and the best tested gap/static combination still gave

`8.15, 9.37, 9.80`.

**Kill decision:** do not replace the current static factor-ratio priority by an `N`-dependent immediate-gap sort on the evidence available here.

This is a finite negative result, not a theorem that no stronger BRC-dependent ranking exists.

## 8. What changed strategically

The current multiplier-factor pipeline now separates three costs:

`horizontal state generation` -> `multiplier scheduling` -> `vertical search`.

Round 5 made horizontal state generation cheap.

Round 7 made each vertical search sparse through residue wheels.

Round 8 now shows that the expensive vertical searches should be **scheduled**, not simply consumed in increasing multiplier order.

The next open unit is therefore not another root optimization.  It is a resource-allocation problem:

> given a total vertical-work budget, how should different multipliers receive different `t` depths before fallback, while preserving a declared completeness rectangle when full completion is required?

That is a typed scheduling/coverage problem and should be attacked separately from the arithmetic kernel.

## 9. Boundaries

- multiplier-Fermat, Lehman/Hart vertical search and quadratic residue sieving remain classical prior art;
- `nu(m)^4/m` is an experimental static priority, not a theorem;
- the arbitrary one-correction jump theorem is exact, but its current CPython implementation is performance-negative as a priority engine;
- the priority vertical scheduler preserves the full declared finite rectangle only when all admissible multipliers are eventually retained;
- finite cross-scale rank/runtime evidence is not an asymptotic factorization-speedup theorem;
- no Foundation promotion is made in this round.
