# BRC Order-1 Linear Deep Tail — Round 11

Status: `PROVED ORDER-1 PELL COLLAPSE / UNBOUNDED TABLE-FREE MOD-8 TAIL / FINITE PIPELINE SPEEDUP`
Date: `2026-09-07`
Parents: `t0.brc_error_linearization_pell`, `t0.brc_mod8_sparse_transition`

## 1. Question

Round 10 showed that high-order predictor error becomes linear after the right
transform and that the table-free Padé/Pell predictor satisfies a second-order
linear recurrence in approximation order.  The next question is whether a long
multiplier stream still needs to regenerate a nontrivial Pell pair at every m.

The answer is no on the deep tail.  The required Padé order eventually falls to
one, and order one itself collapses to a rational function with a denominator
that is exactly linear in m.

## 2. Order-one Pell pair

For source multiplier m and short forward step h in {1,2}, Round 10 gives the
order-one pair

`A=4m+3h`,
`B=4m+h`.

The exact Pell identity is

`(m+h)B^2 - mA^2 = h^3`.

Therefore

`A/B < sqrt((m+h)/m)`.

Since

`A/B = 1 + 2h/(4m+h)`,

an exact source BRC root J needs only the increment predictor

`d = floor(2h J / (4m+h))`.

Thus the high-order Padé state disappears.  The predictor depends only on the
linear denominator `4m+h`.

## 3. Exact two-correction certificate

Let

`beta=sqrt((m+h)/m)`.

The Pell norm gives

`beta-A/B < h^3/(2mAB)`.

Hence the exact state-dependent sufficient condition

`J h^3 <= mAB`

guarantees

`J(beta-A/B) <= 1/2`.

Combining this with the bounded source-root fractional phase from the Round-10
argument places the exact target integer root at most two BRC basins above

`J + floor(2hJ/(4m+h))`.

So the final correction remains the ordinary odd-width BRC operation and needs
at most two crossings.

## 4. Root-free deep-tail certificate

Use

`J <= sqrt(mN)`,
`A >= 4m`,
`B >= 4m`.

The exact order-one certificate is implied by

`h^3 sqrt(mN) <= 16m^3`.

Squaring and cancelling m yields

`N h^6 <= 256 m^5`.

Therefore a table-free root-independent sufficient condition is

`256 m^5 >= N h^6`.

For h=1 this becomes

`256 m^5 >= N`.

For h=2 it becomes

`4 m^5 >= N`.

The odd-N exact mod-8 representative stream has only h=1 or h=2 gaps, so h=2
dominates.  Consequently the single common condition

`4 m^5 >= N`

certifies **every later retained multiplier transition**.

Define

`T(N)=ceil((N/4)^(1/5))`.

After aligning T(N) to the next representative multiplier, the entire remaining
mod-8 stream is order-one linear Pell/BRC transport and requires no
sqrt-ratio table at any horizon.

The h=1 steps can enter earlier at

`T_1(N)=ceil((N/256)^(1/5))`.

## 5. Exact transport

Assume

`mN=J^2+R`, `0<=R<=2J`.

For h in {1,2}, put

`d=floor(2hJ/(4m+h))`,
`a=J+d`.

Then the provisional target remainder is exactly

`G=R+hN-d(2J+d)`.

While

`G>=2a+1`,

perform

`G <- G-(2a+1)`,
`a <- a+1`.

On the certified tail this loop executes at most twice.  The result is exactly

`a=floor(sqrt((m+h)N))`,
`G=(m+h)N-a^2`.

No square root of the target and no multiplier-ratio predictor is materialized.

## 6. Why this is the final linear collapse of the Round-10 error chain

Round 10 found three linearizations:

1. differentiated truncation error has an affine derivative-order ratio;
2. BRC correction gap has linear first differences and constant second
   differences;
3. Padé/Pell pairs have a second-order linear recurrence in approximation order.

Round 11 adds the deep-tail collapse:

`A_1(m,h)=4m+3h`,
`B_1(m,h)=4m+h`.

For fixed h both are exactly affine in m and satisfy

`Delta_m A_1 = Delta_m B_1 = 4`.

The actual root increment predictor further reduces to the single quotient

`floor(2hJ/(4m+h))`.

Thus the long-tail predictor is literally a linear-denominator stream followed
by the exact quadratic BRC closure from Round 10.

## 7. Relation to a classical N^(1/3) multiplier horizon

This does not shorten a Lehman/Hart-style factor-search horizon.  If the
reference horizon is

`M(N)=Theta(N^(1/3))`,

while the common linear tail begins at

`T(N)=Theta(N^(1/5))`,

then

`T(N)/M(N)=O(N^(-2/15)) -> 0`.

So the table/high-order prefix is an asymptotically vanishing fraction of such a
long multiplier horizon, even though the factorization search complexity itself
is unchanged.

For a 2048-bit N, the common threshold has about 410 bits while N^(1/3) has
about 683 bits.  These are astronomically large multipliers; this comparison is
structural and not an RSA-practicality claim.

## 8. Validation

Repository regression includes:

- exact order-one Pell identity over a multiplier grid;
- exact minimality of the declared fifth-root sufficient thresholds;
- exhaustive small odd N tail streams against direct integer roots;
- random 128..8192-bit streams against direct roots;
- correction count <=2;
- representative gaps only 1 or 2;
- explicit operation beyond the old multiplier<=100 production boundary.

The executable tail has no MAX_MULTIPLIER table boundary.

## 9. Finite full-pipeline benchmark

The benchmark uses 16 deterministic odd N values per bit size and 300 retained
mod-8 transitions per N.  Both paths use the same mod-4032 square-residue filter
and exact gap isqrt on survivors.

The direct baseline is deliberately fair: it carries the previous target and
updates it by `hN` before each new `math.isqrt`; it does not recompute `mN` by a
large multiplication on every step.

| N bits | direct / linear deep-tail speedup |
|---:|---:|
| 512 | 1.22x |
| 1024 | 1.39x |
| 2048 | 1.70x |
| 4096 | 1.93x |
| 8192 | 1.97x |

The equality checks include survivor counts and exact-square outcomes, so the
speed comparison preserves pipeline semantics.

These are finite Python timings.  They do not establish an asymptotic machine
complexity improvement.

## 10. Decision

Promote the order-one deep tail as a T0_BRC subtool:

`HIGH-ORDER / TABLE PREFIX -> ORDER-1 LINEAR PELL TAIL -> <=2 BRC CLOSURE`.

The main result is stronger than the Round-9 storage statement: beyond the
N^(1/5) tail the table-free route is not only exact but is already faster than
optimized direct isqrt in the tested large-integer Python pipeline.

## 11. Boundary / next attack

- Difference-of-squares multiplier search remains classical.
- The N^(1/3) reference horizon is not reduced.
- The deep-tail threshold is enormous for RSA-size N, so no practical RSA break
  is claimed.
- The current per-step cost still includes the integer division
  `floor(2hJ/(4m+h))`.

The next local execution target is therefore the quotient itself: determine
whether its quotient/remainder can be transported between adjacent retained
multipliers without a full fresh big-integer division, while keeping an exact
certificate and avoiding an O(M) side table.
