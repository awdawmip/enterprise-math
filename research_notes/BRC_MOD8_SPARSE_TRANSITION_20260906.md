# BRC mod-8 sparse multiplier transition

Status: `PROVED SPARSE ROOT TRANSPORT / ZERO EXTRA CHECKED-IN TABLE / FINITE PERFORMANCE BENCHMARK`
Date: `2026-09-06`
Parents: `t0.brc_multiplier_transition`, `t0.brc_multiplier_priority_jump`

## Question

Once the exact odd-N scan quotient has deleted multiplier residues 2,4,6 modulo 8, should the BRC root engine still materialize the root/remainder state at those deleted multipliers merely to advance to the next retained state?

No. In increasing order, the exact representative residues `{0,1,3,5,7} mod 8` have gaps only 1 or 2. A direct two-step BRC transition skips the deleted intermediate multiplier exactly.

For `m=1..100`, root-state materializations therefore fall from 100 to 62, matching the exact 38% scan reduction rather than only reducing gap tests.

## One-step input

The canonical consecutive tool supplies lower dyadic constants

`C_m=floor(2^B*(sqrt((m+1)/m)-1))`.

Put

`A_m=2^B+C_m`.

Then

`A_m/2^B <= sqrt((m+1)/m)`

with error less than `2^-B`.

## Compiled two-step predictor

For a direct jump `m -> m+2`, define

`A_(m,2)=floor(A_m*A_(m+1)/2^B)`

and

`C_(m,2)=A_(m,2)-2^B`.

Because both one-step factors are lower bounds and the final product is truncated downward,

`A_(m,2)/2^B <= sqrt((m+2)/m)`.

Thus no extra checked-in predictor table is required. The two-step constants are compiled once at runtime from adjacent canonical constants and cached/reused.

## Four-correction theorem

Let

`beta_1=sqrt((m+1)/m)`,
`beta_2=sqrt((m+2)/(m+1))`,
`beta=beta_1*beta_2=sqrt((m+2)/m)`.

Let `eps=2^-B`. If `a_i=A_i/2^B`, then

`0 <= beta_i-a_i < eps`.

After the product truncation,

`0 <= beta-a_(m,2) < (beta_1+beta_2+1)*eps < 4*eps`,

because in the worst sparse step m=1,

`beta_1<=sqrt(2)`, `beta_2<=sqrt(3/2)`.

The canonical precision rule gives

`J_m < 2^(B-1)`,

so the predictor error on `J_m` is less than 2. If

`d0=floor(C_(m,2)*J_m/2^B)`,

then

`(beta-1)J_m < d0+3`.

Write

`sqrt(mN)=J_m+delta`, `0<=delta<1`.

Then

`sqrt((m+2)N)=J_m+(beta-1)J_m+beta*delta`

is strictly below

`J_m+d0+3+sqrt(3) < J_m+d0+4.733...`.

The predictor is a lower bound, so the true integer root lies between the candidate and candidate+4. Hence at most four odd-basin corrections are sufficient.

## Root-free two-step remainder update

For a step h in `{1,2}`, set the predicted increment d and candidate `A=J+d`. Since

`mN=J^2+R`,

the provisional remainder at `m+h` is exactly

`G=R+hN-d(2J+d)`.

While

`G>=2A+1`,

perform the usual BRC basin crossing

`G <- G-(2A+1)`,
`A <- A+1`.

For h=1 the existing bound is 2 corrections; for the compiled h=2 predictor the proved bound is 4.

No integer root of `(m+1)N` is materialized when m+1 is statically removed.

## Exact representative sequence

The increasing retained pattern is

`..., 7,8,9,11,13,15,16,17,...`.

Therefore every transition is step 1 or 2. The executable surface

`odd_n_sparse_multiplier_root_sequence(n, max_multiplier=100)`

starts with the only N-dependent root at m=1 and returns states only on the exact scan representatives.

At 100 it returns 62 states.

## Validation

Repository regression includes:

- proof-side check that every compiled two-step constant is below the direct exact B-bit two-step constant;
- exact representative-set equality and 62-state count at m<=100;
- exhaustive odd `N<500` comparison against direct integer square roots;
- random 128..8192-bit comparison against direct roots;
- correction-bound assertions;
- explicit checks that 1->3, 3->5 and 5->7 do not materialize 2,4,6.

In the finite research harness, observed two-step correction counts never exceeded 2, although only the proved bound 4 is registered.

## Finite transport performance

A Python harness compared:

1. full consecutive BRC transport through every integer multiplier;
2. sparse mod-8 transport with precompiled two-step constants.

Representative transport-only speedups after precompilation were:

| max multiplier | N bits | sparse / full speedup |
|---:|---:|---:|
| 100 | 1024 | ~1.59x |
| 100 | 2048 | ~1.61x |
| 100 | 4096 | ~1.55x |
| 1,000 | 1024 | ~1.36x |
| 1,000 | 2048 | ~1.61x |
| 1,000 | 4096 | ~1.72x |
| 10,000 | 1024 | ~1.30x |
| 10,000 | 2048 | ~1.44x |
| 10,000 | 4096 | ~1.54x |

The >100 rows used a research harness with dynamically generated consecutive constants and then the same two-step compiler. The checked-in production transition table remains bounded at 100, so those rows are evidence for the general construction, not a claim that the current static runtime exposes max_multiplier=10,000.

The gain is smaller for small integers because Python overhead dominates.

## Storage consequence

No new on-disk two-step predictor table is required. If a long consecutive predictor table is available, the sparse constants are a deterministic compiled cache. This is important for the earlier long-Hart-stream concern: the exact mod-8 quotient can reduce per-N state updates without multiplying the checked-in predictor payload by another 37.5%.

It does not solve the existing O(M) storage/generation cost of the consecutive predictor family itself.

## Boundary

- Exact finite integer BRC transport.
- Static production path currently `max_multiplier<=100` because it reuses the existing canonical table boundary.
- Long-stream benchmark constants were generated by a research harness and amortized before per-N timing.
- This is a constant-factor implementation improvement and does not change the Hart/Lehman `N^(1/3)` search horizon or imply RSA-scale factorization.
