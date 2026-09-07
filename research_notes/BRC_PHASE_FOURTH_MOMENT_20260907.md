# BRC Fourth-Order Phase Moment Tail — Round 15

Status: `PROVED N^(1/7) FIXED-PHASE TAIL / LIFTED MOMENT CLOSURE / EXISTING 1KIB TABLE REUSED / FINITE LARGE-INTEGER SPEEDUP`
Date: `2026-09-07`
Parents: `t0.brc_phase_root_recurrence`, `t0.brc_phase_quotient_remainder`, `t0.brc_square_gap_cascade`

## 1. Question and BRC observer contract

Round 14 established an exact third-difference phase-root recurrence on the
common order-one tail `4m^5>=N`. Its next mathematical unit was whether a
higher phase jet could begin earlier, while preserving the exact root/remainder
observer required by the completion-gap square test.

The current result is an extension of `T0_BRC`, not a new family.

Reuse resolution:

- `t0.brc_phase_root_recurrence`: `EXTEND_EXISTING_TOOL`;
- `t0.brc_phase_quotient_remainder`: `REUSE_EXECUTED`, specifically its existing
  1024-byte normalized reciprocal table;
- `t0.brc_square_gap_cascade`: `COMPOSE_APPLIED`, with the same exact completion
  gap and zero-false-negative BALANCED filter.

The adequate carrier is not a scalar fourth difference. Each phase retains:

- four labeled exact states `(m_i,J_i,R_i)`;
- the first three root differences `(u,v,w)`;
- the lifted quadratic moments `(uw,v^2,vw,w^2)`.

The individual remainders and their order remain observable because the exact
next residual uses the signed combination `-R0+4R1-6R2+4R3`.

## 2. Cubic extrapolation on one mod-8 phase

Fix one of the five odd-N multiplier phases. Successive visits have spacing 8:

`m_i=m_0+8i`,
`m_iN=J_i^2+R_i`,
`0<=R_i<=2J_i`.

Define the Newton differences

`u=J_1-J_0`,
`v=J_2-2J_1+J_0`,
`w=J_3-3J_2+3J_1-J_0`.

The cubic extrapolation with fourth difference set to zero is

`C=4J_3-6J_2+4J_1-J_0`
` =J_0+4u+6v+4w`.

The exact correction is

`e=J_4-C=Delta_8^4 J_0`.

## 3. Exact target-residual identity

The multiplier target sequence `m_iN` is linear in i, hence its fourth finite
difference vanishes:

`m_4N=4m_3N-6m_2N+4m_1N-m_0N`.

Substitute `m_iN=J_i^2+R_i` and subtract `C^2`. The root-square part reduces
exactly to the quadratic form

`4J_3^2-6J_2^2+4J_1^2-J_0^2-C^2`
` =-2(4uw+3v^2+12vw+6w^2)`.

Therefore the exact provisional residual is

`boxed:`
`G=m_4N-C^2`
` =-R_0+4R_1-6R_2+4R_3`
`  -2(4uw+3v^2+12vw+6w^2)`.

This formula requires no target square root, no multiplier-root quotient, and no
product involving the full root C.

## 4. N^(1/7) correction theorem

Let `f(m)=sqrt(mN)`. Its fourth derivative is

`f^(4)(m)=-15 sqrt(N)/(16m^(7/2))`.

The integral representation of a fourth finite difference with spacing 8 gives

`-8^4*15 sqrt(N)/(16m^(7/2))`
` <= Delta_8^4 f(m) <= 0`,

so

`-3840 sqrt(N)/m^(7/2) <= Delta_8^4 f(m) <= 0`.

Impose the root-free tail condition

`boxed: m^7>=128N`.

Then

`sqrt(N)/m^(7/2)<=1/sqrt(128)`

and

`3840/sqrt(128)=240sqrt(2)<340`.

Write `J_i=f(m_i)-theta_i`, `0<=theta_i<1`. The signed fourth difference of
the floor phase has positive and negative coefficient mass 8, so

`-8<Delta_8^4 theta<8`.

Consequently the integer correction satisfies

`boxed: -347<=e<=7`.

This is a uniform bound independent of N, m and the final multiplier horizon
once the declared tail begins.

The new tail begins at

`T_4(N)=ceil((128N)^(1/7))`

before alignment to the exact mod-8 representative set. It is asymptotically
earlier than the Round-14 `Theta(N^(1/5))` frontier.

Relative to a classical `Theta(N^(1/3))` multiplier horizon,

`T_4(N)/N^(1/3)=O(N^(-4/21))->0`.

This changes state-transport cost, not factor-search complexity.

## 5. Reusing the 1 KiB table for the negative correction

The smooth fourth difference is negative, so the dominant case has `G<0`.
Put

`H=-G`, `d=-e`, `1<=d<=347`.

Since the exact target root is `J_4=C-d`,

`H=d(2C-d)-R_4`,
`0<=R_4<=2(C-d)`.

Use the even denominator `2C` and let

`q=floor(H/(2C))`.

If

`2C>d(d-2)`,

then

`q in {d-2,d-1}`.

The worst case `d=347` is covered by the simple threshold

`C>=59858`.

Thus `d` is one of `q+1,q+2`; one comparison with

`(q+1)(2C-q-1)`

selects the exact decrement, after which

`R_4=d(2C-d)-H`.

For `q<=346`, the same Round-13 normalized reciprocal table estimates
`floor(H/(2C))` from below. Its worst-case deficit is less than

`346/512 + 346*1024/2^20 < 1.02`,

so at most two increment comparisons recover q exactly.

The positive case has only `0<=e<=7` and is closed by at most seven ordinary
upward BRC basin steps.

No new table payload is introduced. The total logical table budget remains
4633 bytes when composed with the BALANCED square-gap cascade.

## 6. Lifted quadratic moments eliminate unbounded products

Direct evaluation of

`4uw+3v^2+12vw+6w^2`

would require products of independently growing phase differences at every
step. Instead retain the four moments

`UW=uw`, `V2=v^2`, `VW=vw`, `W2=w^2`.

After the bounded correction `e=Delta^4J`, shifting the phase window gives

`u'=u+v`,
`v'=v+w`,
`w'=w+e`.

The moments update exactly as

`UW'=UW+VW+e(u+v)`,
`V2'=V2+2VW+W2`,
`VW'=VW+W2+e(v+w)`,
`W2'=W2+2ew+e^2`.

All new multiplications involve only the bounded integer `e` or fixed small
coefficients. After the seed moments are created, there is no multiplication
between two independently unbounded dynamic coordinates.

This is the principal execution improvement over a raw fourth-order formula.

## 7. Warmup

There are five mod-8 phases and each fourth-order recurrence needs four visits.
The initial state supplies one visit, so the exact fixed warmup is

`5*4-1=19`

additional target roots.

After these nineteen seed transitions, every later retained multiplier is
transported by the fourth-order moment recurrence. The implementation has no
maximum multiplier boundary.

The fixed seed cost is intentionally explicit. It is amortized only on a long
tail; for short scans direct roots remain preferable.

## 8. Validation

Repository-equivalent regression passed 10 tests and covers:

- exact minimality of the seventh-root threshold;
- the exact candidate-gap identity;
- exhaustive small odd-N streams;
- random `64..8192`-bit streams;
- correction range `[-347,7]`;
- exactly nineteen seed-root transitions and recurrence thereafter;
- exactly twenty total target `isqrt` calls including initialization;
- the fact that the fourth-order frontier precedes the order-one frontier for
  large N;
- reuse of the existing 1024-byte reciprocal table;
- unbounded operation beyond multiplier 10000.

No float arithmetic is used in the executable theorem surface.

## 9. Finite equal-semantics benchmark

The committed benchmark compares:

1. a fair direct baseline that carries `mN` incrementally and applies `isqrt` at
   every retained multiplier;
2. the fourth-order lifted-moment phase recurrence.

Both use the same BALANCED square-gap cascade and exact gap `isqrt` on survivors.

| N bits | threshold bits | direct / fourth-phase |
|---:|---:|---:|
| 1024 | 148 | 0.97x |
| 2048 | 294 | 1.28x |
| 4096 | 587 | 2.46x |
| 8192 | 1172 | 4.34x |
| 16384 | 2342 | 3.35x |

An independent population rerun produced approximately

`0.72x, 1.26x, 2.57x, 4.03x, 6.74x`

over the same bit-size sequence. The exact crossover and high-end timing are
runtime dependent, but both runs agree on the structural boundary:

- 1024 bits: fixed warmup and Python state overhead dominate;
- 2048 bits: the recurrence is at or above crossover;
- 4096 bits and above: the lifted-moment route has a substantial finite
  advantage in the tested long streams.

The committed sample observed corrections only in `[-346,-332]`, consistent
with the negative smooth fourth derivative. This finite concentration is not
used to weaken the proved `[-347,7]` interval.

## 10. Decision and hard boundary

Promote as a `T0_BRC` subtool:

`FOUR LABELED PHASE (J,R) STATES`
` -> CUBIC ROOT EXTRAPOLATION`
` -> LIFTED QUADRATIC MOMENTS`
` -> EXISTING 1KIB TABLE CLOSURE`
` -> EXACT NEXT (J,R)`.

The result is an exact transport optimization. It does not:

- reduce the multiplier horizon;
- change Lehman/Hart factorization complexity;
- establish an architecture-independent machine-complexity theorem;
- imply practical RSA factorization;
- mutate Foundation or create a new top-level BRC family.

## 11. Next frontier

For the fifth phase difference,

`f^(5)(m)=105 sqrt(N)/(32m^(9/2))`.

A fixed-spacing fifth-order correction would therefore become uniformly bounded
on a `Theta(N^(1/9))` tail. The unresolved unit is algebraic rather than
analytic: derive and close the exact cubic moment form in

`m_5N-C_5^2`

without reintroducing products between independently unbounded coordinates.
The Round-15 lifted-moment construction suggests that a finite symmetric moment
carrier should exist, but its minimum dimension and practical update cost remain
to be established.
