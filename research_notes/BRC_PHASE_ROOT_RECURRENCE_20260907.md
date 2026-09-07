# BRC Fixed-Phase Root/Remainder Recurrence — Round 14

Status: `PROVED THIRD-DIFFERENCE PHASE ROOT TRANSPORT / EXISTING 1KIB TABLE REUSED / UNBOUNDED EXACT STREAM / FINITE LARGE-INTEGER SPEEDUP`
Date: `2026-09-07`
Parents: `t0.brc_linear_deep_tail`, `t0.brc_phase_quotient_remainder`, `t0.brc_square_gap_cascade`

## 1. Question and reuse decision

Round 13 removed the fresh full-size division from the order-one tail after two
quotient/remainder seeds per mod-8 phase. Its own next frontier was the remaining
large arithmetic in

`R+hN-q(2J+q)`

and the possibility of sharing state with the BALANCED square-gap cascade.

The current task therefore does not create a new BRC family.

- `t0.brc_linear_deep_tail`: `REUSE_APPLIED`.
- `t0.brc_phase_quotient_remainder`: `REUSE_EXECUTED`; its existing 1 KiB
  normalized reciprocal table is reused unchanged.
- `t0.brc_square_gap_cascade`: `COMPOSE_APPLIED`; the exact completion gap remains
  the observed output and receives the same zero-false-negative BALANCED filter.
- Missing capability: direct transport of the full `(J,R)` state across repeated
  visits to one fixed mod-8 phase, without reconstructing the order-one quotient.
  This result is therefore an `EXTEND_EXISTING_TOOL` subtool of `T0_BRC`.

The retained carrier is the exact three-state labeled phase history

`((m_i,J_i,R_i))_(i=0,1,2)`.

It is not collapsed to roots alone: the remainder labels are essential in the
exact residual identity below and in the future completion-gap observation.

## 2. Fixed phases

For odd `N`, retained multipliers satisfy

`m mod 8 in {0,1,3,5,7}`.

A fixed residue phase returns after exactly eight multiplier units. Write

`m_i=m_0+8i`,
`m_i N=J_i^2+R_i`,
`0<=R_i<=2J_i`.

Once three exact visits to one phase are known, set

`a=J_1-J_0`,
`b=J_2-J_1`

and use the quadratic extrapolation

`C=3J_2-3J_1+J_0`.

If `J_0=x`, then `J_1=x+a`, `J_2=x+a+b`, so simply

`C=x+3b`.

## 3. Exact candidate-gap identity

From the second phase increment,

`8N=R_2-R_1+2b(x+a)+b^2`.

Since `m_3=m_0+24`,

`m_3N=x^2+R_0+3(8N)`.

Subtracting `C^2=(x+3b)^2` gives

`G=m_3N-C^2`
` =R_0-3R_1+3R_2+6ab-6b^2`
` =R_0-3R_1+3R_2-6b(b-a)`.

Therefore

`boxed: G=R_0-3R_1+3R_2-6b(b-a)`.

This is an exact integer identity. It removes, after phase warmup:

- a target square root;
- the order-one quotient or Round-13 quotient recurrence;
- the former dynamic product `q(2J+q)`.

The phase still retains exact provenance: the three remainders and the two
successive root increments are not interchangeable with a Boolean support or a
total-only statistic.

## 4. Uniform third-difference correction bound

Let

`f(m)=sqrt(mN)`.

Then

`f'''(m)=3 sqrt(N)/(8m^(5/2))`.

For phase spacing eight, the integral representation of a finite difference
gives

`0<=Delta_8^3 f(m)<=8^3 f'''(m)`
` =192 sqrt(N)/m^(5/2)`.

On the common order-one tail,

`4m^5>=N`,

hence

`sqrt(N)/m^(5/2)<=2`

and therefore

`0<=Delta_8^3 f(m)<=384`.

Write `J_i=f(m_i)-theta_i` with `0<=theta_i<1`. The third difference of
the phase noise lies strictly between `-4` and `4`. Consequently the integer

`e=J_3-C=Delta_8^3 J_0`

obeys the exact, horizon-independent bound

`boxed: -3<=e<=387`.

The target root is `J_3=C+e`.

This bound is deliberately uniform and conservative. In the committed finite
benchmark, observed recurrent corrections were `381..387`; those observations
do not replace the proved interval.

## 5. Reusing the existing 1 KiB table

If `G<0`, then `C` is above the target floor root, so `e<0`. The theorem leaves
only `e in {-1,-2,-3}`, resolved by at most three downward odd-basin steps.

Assume `G>=0`, hence `e>=0`, and put

`W=2C+1`.

Because

`G=e(2C+e)+R_3`
` =eW+[e(e-1)+R_3]`

with `0<=R_3<=2(C+e)`, if

`W>387*388-1`

then

`floor(G/W) in {e,e+1}`.

The simple sufficient threshold is

`C>=75078`.

Round 13 already provides a 512-entry, 16-bit normalized reciprocal table:
logical payload `1024` bytes. For a denominator bucket

`W in [u 2^s,(u+1)2^s)`, `512<=u<=1023`,

it stores

`R_u=floor(2^20/(u+1))`.

For the present quotient range `G/W<389`, its lower estimate misses the true
floor by less than

`389/512 + 389*1024/2^20 < 1.14`.

Thus at most two exact increment comparisons recover `floor(G/W)`. One final
sign test of

`G-u(2C+u)`

decides whether `u=e` or `u=e+1`.

No new table is added. The complete logical table budget remains:

- BALANCED square-gap cascade: `3609` bytes;
- Round-13 normalized reciprocal table, now reused twice: `1024` bytes;
- total: `4633` bytes.

The table now has two typed roles:

1. bounded quotient correction in the Round-13 phase quotient backend;
2. constant-time closure of a potentially 384-step phase-root BRC correction.

## 6. Warmup and exact unbounded stream

There are five target phases. Each needs three exact root/remainder visits.
The initial state supplies one visit to one phase, so exactly

`5*3-1=14`

seed transitions are sufficient.

Those seed transitions use the already proved order-one linear tail. Every later
transition is obtained from the three-state phase recurrence. The executable
surface has no `max_multiplier<=100` boundary and materializes only the initial
target square root.

## 7. Optional lifted product state

The only unbounded dynamic product in the new residual formula is `b(b-a)`.
It can also be eliminated algebraically.

Maintain, per phase,

`u=J_1-J_0`,
`v=J_2-2J_1+J_0`,
`P=uv`,
`Q=v^2`.

Since `b=u+v`, the product in the residual is

`b(b-a)=(u+v)v=P+Q`.

After correction `e=Delta^3 J`, the lifted state updates exactly by

`u'=u+v+e`,
`v'=v+e`,
`Q'=Q+2ve+e^2`,
`P'=P+ue+Q'`.

All new multiplications use the bounded correction `e<=387`. This is an exact
no-unbounded-dynamic-product representation.

In the current Python runtime, however, the extra state bookkeeping was slower
than directly evaluating `b(b-a)`. It is recorded as an exact alternative, not
selected as the default execution path.

## 8. Low-word / QR-shadow audit

A second prototype carried completion-gap residues for the registered cascade
moduli instead of reducing the full gap at every stage. The shadow was exact and
preserved the zero-false-negative filter semantics, but Python timings were not
stable enough to beat native `%` consistently after the BALANCED cascade had
already reduced survivors to about `0.0631%`.

Decision:

`LOW_WORD_QR_SHADOW -> NOT PROMOTED`.

The result is a runtime boundary, not a mathematical impossibility statement.

## 9. Validation

Repository regression covers:

- the exact candidate-gap identity on exhaustive small odd inputs;
- direct-root equality on exhaustive and random `64..8192`-bit tails;
- the uniform correction interval `[-3,387]`;
- exactly fourteen seed transitions followed by recurrence only;
- exactly one initial target `isqrt`;
- reuse of the existing `1024`-byte reciprocal table;
- operation beyond multiplier `10000`.

A separate literal-loop comparison confirmed why table reuse matters: replacing
hundreds of ordinary odd-basin iterations by reciprocal-assisted closure was
roughly `27x..34x` faster in the tested prototype.

## 10. Finite equal-semantics benchmark

All three paths used the same BALANCED square-gap cascade and exact gap `isqrt`
on survivors:

1. direct order-one division;
2. Round-13 phase quotient/remainder tracker;
3. Round-14 phase root/remainder recurrence.

The committed fixed run was:

| N bits | direct / phase-root | Round-13 / phase-root |
|---:|---:|---:|
| 1024 | 0.78x | 0.97x |
| 2048 | 0.75x | 0.88x |
| 4096 | 1.41x | 1.20x |
| 8192 | 2.19x | 1.52x |
| 16384 | 2.80x | 1.61x |

An independent rerun on the same code placed the 2048-bit cohort near the
crossover (`direct/phase-root ~=1.06`, `Round-13/phase-root ~=1.12`) while
retaining essentially the same 4096-bit-and-up trend. Therefore no
architecture-independent crossover is claimed.

The robust finite conclusion is narrower:

- keep direct division for small operands;
- Round 13 remains a valid optional large-integer backend;
- on the tested `4096..16384`-bit long streams, full phase-root transport was
  consistently faster and the advantage widened with operand size.

## 11. Decision and boundary

Promote as a `T0_BRC` subtool:

`THREE LABELED PHASE STATES`
` -> QUADRATIC ROOT EXTRAPOLATION`
` -> EXACT REMAINDER IDENTITY`
` -> EXISTING 1KIB TABLE CLOSURE`
` -> EXACT (J,R)`.

This is an exact state-transport optimization. It does not:

- reduce the multiplier horizon;
- change Lehman/Hart factorization complexity;
- prove an asymptotic machine-complexity improvement;
- imply RSA practicality;
- promote a new top-level BRC family.

## 12. Next frontier

The phase method suggests a hierarchy. For `f(m)=sqrt(mN)`, the `k`-th
fixed-spacing finite difference is controlled by `f^(k)(m)`, giving a tail scale
of order

`m = Omega(N^(1/(2k-1)))`.

The next mathematical unit is to determine whether a fourth-order phase moment
carrier admits an exact low-product remainder identity comparable to Round 14.
If so, it could move the division-free recurrence frontier from the
`N^(1/5)` tail toward an `N^(1/7)` tail without erasing the exact `(J,R)`
observer needed by the square-gap cascade.
